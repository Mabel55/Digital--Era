from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import hash_password, verify_password, create_access_token, get_current_user
import traceback
from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi import Request
from limiter import limiter


def _create_free_subscription(db: Session, user_id: int):
    """Create a default free subscription for a new user."""
    sub = models.Subscription(user_id=user_id, plan="free", status="active")
    db.add(sub)
    db.commit()

router = APIRouter(tags=["Users & Auth"])

@router.post("/signup")
@limiter.limit("5/minute")
def register_user(request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # 1. Check if the email is already in PostgreSQL
        existing_user = db.query(models.User).filter(models.User.email.ilike(user.email)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # 2. Hash the password and save the new user to the database
        hashed_pw = hash_password(user.password)
        new_user = models.User(email=user.email, hashed_password=hashed_pw, full_name=user.full_name, role=user.role)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        # 3. Auto-create a free subscription for the new user
        _create_free_subscription(db, new_user.id)
        
        return {"message": "User created successfully in PostgreSQL!", "email": new_user.email}
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print("SIGNUP CRASH", traceback.format_exc())
        raise HTTPException(status_code=400, detail=f"DB_CRASH: {str(e)}")

@router.post("/login")
@limiter.limit("10/minute")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email.ilike(form_data.username)).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        # Gamification: Streak Calculation
        now = datetime.utcnow()
        if user.last_login:
            # If logged in yesterday, increment streak
            if (now.date() - user.last_login.date()).days == 1:
                user.streak += 1
            # If missed a day, reset streak
            elif (now.date() - user.last_login.date()).days > 1:
                user.streak = 1
        else:
            user.streak = 1
        
        user.last_login = now
        db.commit()
        
        access_token = create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException:
        raise
    except Exception as e:
        error_details = traceback.format_exc()
        print("LOGIN CRASH:", error_details) 
        raise HTTPException(status_code=500, detail=f"LOGIN ERROR: {str(e)}")

@router.get("/leaderboard", response_model=list[schemas.UserResponse])
def get_leaderboard(db: Session = Depends(get_db)):
    return db.query(models.User).order_by(models.User.xp.desc()).limit(100).all()

@router.get("/users/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if user exists
        db_user = db.query(models.User).filter(models.User.email.ilike(user.email)).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Create new user
        hashed_pw = hash_password(user.password)
        new_user = models.User(
            email=user.email, 
            hashed_password=hashed_pw, 
            full_name=user.full_name, 
            role=user.role
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        # Auto-create a free subscription
        _create_free_subscription(db, new_user.id)
        
        return new_user

    except Exception as e:
        error_details = traceback.format_exc()
        print("BACKEND CRASH:", error_details) 
        raise HTTPException(status_code=500, detail=f"PYTHON ERROR: {str(e)}")

@router.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Ensure user has a subscription record (handles users created before monetization)
    if not current_user.subscription:
        _create_free_subscription(db, current_user.id)
        db.refresh(current_user)
    return current_user

class ProgressUpdate(BaseModel):
    course_name: str
    lesson_index: int | None = None
    lesson_id: int | None = None

@router.post("/users/me/progress", response_model=schemas.UserResponse)
def update_progress(payload: ProgressUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    xp_to_add = 10
    
    progress = dict(current_user.progress) if current_user.progress else {}
    if payload.course_name not in progress:
        progress[payload.course_name] = {"completed_lessons": 0, "completed_lesson_ids": []}
        
    current_completed = progress[payload.course_name].get("completed_lessons", 0)
    completed_ids = progress[payload.course_name].get("completed_lesson_ids", [])
    
    awarded_xp = False

    # 1. Legacy Static Course tracking (lesson_index)
    if payload.lesson_index is not None:
        if payload.lesson_index >= current_completed:
            progress[payload.course_name]["completed_lessons"] = payload.lesson_index + 1
            awarded_xp = True

    # 2. Dynamic DB Course tracking (lesson_id)
    if payload.lesson_id is not None:
        if payload.lesson_id not in completed_ids:
            completed_ids.append(payload.lesson_id)
            progress[payload.course_name]["completed_lesson_ids"] = completed_ids
            awarded_xp = True
            
    if awarded_xp:
        current_user.xp += xp_to_add
        
        # Use centralized level calculation
        current_user.level = models.calculate_level(current_user.xp)
            
    # Assign progress dict back since SQLAlchemy JSON mutations aren't always tracked
    current_user.progress = progress
    db.commit()
    db.refresh(current_user)
    
    return current_user

@router.post("/users/reset-password")
def reset_password(payload: schemas.UserResetPassword, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email.ilike(payload.email)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Security: Verify old password before allowing reset
        if not verify_password(payload.old_password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Current password is incorrect")
        
        hashed_pw = hash_password(payload.new_password)
        user.hashed_password = hashed_pw
        db.commit()
        return {"message": "Password reset successfully"}
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print("RESET PASSWORD CRASH:", traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"ERROR: {str(e)}")

@router.get("/admin/analytics")
def get_admin_analytics(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Check if user is admin
    if current_user.role.lower() not in ["admin", "teacher"] and current_user.email != "nasaadanna@gmail.com":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    from sqlalchemy import func
    from datetime import date
    today = date.today()
    
    total_users = db.query(models.User).count()
    
    # Calculate MRR (Monthly users * $9.99 + Yearly users * ($79/12))
    monthly_subs = db.query(models.Subscription).filter(
        models.Subscription.plan == "pro_monthly", 
        models.Subscription.status.in_(["active", "trialing"])
    ).count()
    
    yearly_subs = db.query(models.Subscription).filter(
        models.Subscription.plan == "pro_yearly",
        models.Subscription.status.in_(["active", "trialing"])
    ).count()
    
    mrr = (monthly_subs * 9.99) + (yearly_subs * (79.00 / 12))
    
    # AI Messages Today
    ai_msgs_today = db.query(func.sum(models.AIUsage.message_count)).filter(
        models.AIUsage.usage_date == today
    ).scalar() or 0
    
    # Active Pro Users
    active_pro = monthly_subs + yearly_subs
    
    return {
        "total_users": total_users,
        "mrr": round(mrr, 2),
        "ai_messages_today": int(ai_msgs_today),
        "active_pro_users": active_pro
    }


# ─── FORGOT PASSWORD FLOW ───
import os
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reset_email(to_email: str, token: str):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    if not all([smtp_server, smtp_username, smtp_password]):
        print(f"DEBUG: Missing SMTP credentials. Reset link: http://localhost:5173/reset-password?token={token}")
        return

    reset_link = f"http://localhost:5173/reset-password?token={token}"
    
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = "Reset Your Password - Digital Era"
    
    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>Password Reset Request</h2>
        <p>We received a request to reset your password for Digital Era.</p>
        <p>Click the link below to set a new password:</p>
        <p><a href="{reset_link}" style="background-color: #00e5a0; color: #0d0f14; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Reset Password</a></p>
        <p>This link will expire in 1 hour.</p>
        <p>If you didn't request this, you can safely ignore this email.</p>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print(f"Successfully sent reset email to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        print(f"DEBUG Reset link: {reset_link}")


@router.post("/users/forgot-password")
def forgot_password(payload: schemas.ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email.ilike(payload.email)).first()
    if not user:
        # Prevent email enumeration by always returning success
        return {"message": "If that email exists, a reset link has been sent."}
    
    # Generate token
    token = str(uuid.uuid4())
    expires = datetime.utcnow() + timedelta(hours=1)
    
    reset_token = models.PasswordResetToken(
        user_id=user.id,
        token=token,
        expires_at=expires
    )
    db.add(reset_token)
    db.commit()
    
    send_reset_email(user.email, token)
    return {"message": "If that email exists, a reset link has been sent."}

@router.post("/users/reset-password-with-token")
def reset_password_with_token(payload: schemas.ResetPasswordTokenRequest, db: Session = Depends(get_db)):
    reset_token = db.query(models.PasswordResetToken).filter(
        models.PasswordResetToken.token == payload.token
    ).first()
    
    if not reset_token:
        raise HTTPException(status_code=400, detail="Invalid or expired token.")
        
    if reset_token.expires_at < datetime.utcnow():
        db.delete(reset_token)
        db.commit()
        raise HTTPException(status_code=400, detail="Invalid or expired token.")
        
    user = db.query(models.User).filter(models.User.id == reset_token.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
        
    user.hashed_password = hash_password(payload.new_password)
    db.delete(reset_token)
    db.commit()
    
    return {"message": "Password has been successfully reset."}
