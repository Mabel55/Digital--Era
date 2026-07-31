from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import hash_password, verify_password, create_access_token, get_current_user
import traceback
from datetime import datetime, timedelta, date
from pydantic import BaseModel
from fastapi import Request
from limiter import limiter
import os

# Load admin emails from environment variable (comma-separated)
ADMIN_EMAILS = [e.strip().lower() for e in os.getenv("ADMIN_EMAILS", "nasaadanna@gmail.com").split(",") if e.strip()]

def _is_admin(user: models.User) -> bool:
    """Check if user has admin privileges via role or environment-configured email list."""
    return user.role.lower() in ["admin", "teacher"] or user.email.lower() in ADMIN_EMAILS


def _create_free_subscription(db: Session, user_id: int):
    """Create a default free subscription for a new user."""
    sub = models.Subscription(user_id=user_id, plan="free", status="active")
    db.add(sub)
    db.commit()


def _track_activity(db: Session, user_id: int, xp: int = 0, lessons: int = 0, challenges: int = 0):
    """Track daily user activity for real analytics charts."""
    today = date.today()
    activity = db.query(models.UserActivity).filter(
        models.UserActivity.user_id == user_id,
        models.UserActivity.activity_date == today
    ).first()
    
    if not activity:
        activity = models.UserActivity(user_id=user_id, activity_date=today)
        db.add(activity)
    
    activity.xp_earned += xp
    activity.lessons_completed += lessons
    activity.challenges_completed += challenges
    db.commit()


def _create_notification(db: Session, user_id: int, type: str, title: str, message: str, action_url: str = None):
    """Create an in-app notification."""
    notif = models.Notification(
        user_id=user_id,
        type=type,
        title=title,
        message=message,
        action_url=action_url
    )
    db.add(notif)
    db.commit()


router = APIRouter(prefix="/users", tags=["Users & Auth"])

@router.post("/signup")
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
        
        # 3. Auto-create a free subscription for the new user (or apply referral)
        _create_free_subscription(db, new_user.id)
        
        # 4. Create welcome notification
        _create_notification(db, new_user.id, "system", "Welcome to Digital Era! 🎉", 
                           "Start your coding journey with our interactive courses.", "/dashboard")
        
        # 5. Handle Referral Code
        if hasattr(user, 'referral_code') and user.referral_code:
            try:
                referrer_id = int(user.referral_code)
                referrer_sub = db.query(models.Subscription).filter(models.Subscription.user_id == referrer_id).first()
                new_user_sub = db.query(models.Subscription).filter(models.Subscription.user_id == new_user.id).first()
                
                if referrer_sub and new_user_sub:
                    now = datetime.utcnow()
                    # Upgrade referrer
                    if not referrer_sub.current_period_end or referrer_sub.current_period_end < now:
                        referrer_sub.current_period_end = now + timedelta(days=30)
                    else:
                        referrer_sub.current_period_end += timedelta(days=30)
                    referrer_sub.plan = "pro"
                    referrer_sub.status = "trialing"
                    
                    # Upgrade new user
                    new_user_sub.plan = "pro"
                    new_user_sub.status = "trialing"
                    new_user_sub.current_period_end = now + timedelta(days=30)
                    
                    # Notify referrer
                    _create_notification(db, referrer_id, "achievement", "Referral Bonus! 🎁",
                                       f"{new_user.full_name or new_user.email} joined using your code. You got 30 days free Pro!", "/profile")
                    
                    db.commit()
            except ValueError:
                pass # Invalid referral code format, ignore
        
        return {"message": "User created successfully in PostgreSQL!", "email": new_user.email}
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print("SIGNUP CRASH", traceback.format_exc())
        raise HTTPException(status_code=400, detail=f"DB_CRASH: {str(e)}")

@router.post("/login")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email.ilike(form_data.username)).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        if not user.is_active:
            raise HTTPException(status_code=403, detail="Your account has been blocked.")
        
        # Gamification: Streak Calculation
        now = datetime.utcnow()
        if user.last_login:
            # If logged in yesterday, increment streak
            if (now.date() - user.last_login.date()).days == 1:
                user.streak += 1
                # Track longest streak
                if user.streak > (user.longest_streak or 0):
                    user.longest_streak = user.streak
                # Notify on streak milestones
                if user.streak in [3, 7, 14, 30, 60, 100]:
                    _create_notification(db, user.id, "streak", f"🔥 {user.streak}-Day Streak!",
                                       f"You've been coding for {user.streak} days straight! Keep it up!", "/profile")
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
def get_leaderboard(period: str = "all", db: Session = Depends(get_db)):
    """Get leaderboard with optional time period filter."""
    query = db.query(models.User)
    
    if period == "week":
        week_ago = datetime.utcnow() - timedelta(days=7)
        query = query.filter(models.User.last_login >= week_ago)
    elif period == "month":
        month_ago = datetime.utcnow() - timedelta(days=30)
        query = query.filter(models.User.last_login >= month_ago)
    
    return query.order_by(models.User.xp.desc()).limit(100).all()

@router.get("/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    return db.query(models.User).all()

@router.post("/")
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

@router.get("/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Ensure user has a subscription record (handles users created before monetization)
    if not current_user.subscription:
        _create_free_subscription(db, current_user.id)
        db.refresh(current_user)
    return current_user

# ─── REAL PROFILE EDIT (replaces the mocked save) ───
@router.put("/me", response_model=schemas.UserResponse)
def update_profile(
    payload: schemas.UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Update user profile — no longer mocked!"""
    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if hasattr(current_user, field):
            setattr(current_user, field, value)
    db.commit()
    db.refresh(current_user)
    return current_user

# ─── REAL ACTIVITY DATA (replaces mock chart) ───
@router.get("/me/activity", response_model=list[schemas.UserActivityResponse])
def get_user_activity(
    days: int = 30,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Returns real XP activity data for the last N days."""
    since = date.today() - timedelta(days=days)
    activities = db.query(models.UserActivity).filter(
        models.UserActivity.user_id == current_user.id,
        models.UserActivity.activity_date >= since
    ).order_by(models.UserActivity.activity_date.asc()).all()
    return activities

# ─── COURSE COMPLETIONS ───
@router.get("/me/completions", response_model=list[schemas.CourseCompletionResponse])
def get_user_completions(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Returns all completed courses for the user."""
    return db.query(models.CourseCompletion).filter(
        models.CourseCompletion.user_id == current_user.id
    ).order_by(models.CourseCompletion.completed_at.desc()).all()

# ─── NOTIFICATIONS ───
@router.get("/notifications", response_model=list[schemas.NotificationResponse])
def get_notifications(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Returns user's notifications, newest first."""
    return db.query(models.Notification).filter(
        models.Notification.user_id == current_user.id
    ).order_by(models.Notification.created_at.desc()).limit(50).all()

@router.get("/notifications/unread-count")
def get_unread_count(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    count = db.query(models.Notification).filter(
        models.Notification.user_id == current_user.id,
        models.Notification.is_read == False
    ).count()
    return {"count": count}

@router.post("/notifications/read-all")
def mark_all_read(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db.query(models.Notification).filter(
        models.Notification.user_id == current_user.id,
        models.Notification.is_read == False
    ).update({"is_read": True})
    db.commit()
    return {"message": "All notifications marked as read"}

@router.post("/notifications/{notif_id}/read")
def mark_read(
    notif_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    notif = db.query(models.Notification).filter(
        models.Notification.id == notif_id,
        models.Notification.user_id == current_user.id
    ).first()
    if notif:
        notif.is_read = True
        db.commit()
    return {"message": "Marked as read"}


class ProgressUpdate(BaseModel):
    course_name: str
    lesson_index: int | None = None
    lesson_id: int | None = None

@router.post("/me/progress", response_model=schemas.UserResponse)
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
        
        # Track real activity
        _track_activity(db, current_user.id, xp=xp_to_add, lessons=1)
        
        # XP milestone notifications
        milestones = [100, 250, 500, 1000, 2500, 5000]
        for milestone in milestones:
            if current_user.xp >= milestone and (current_user.xp - xp_to_add) < milestone:
                _create_notification(db, current_user.id, "achievement", 
                                   f"🏆 {milestone} XP Milestone!", 
                                   f"You've earned {milestone} XP! You're now level: {current_user.level}", "/profile")
    
    # Track "Continue Learning" state
    current_user.last_active_course = payload.course_name
    if payload.lesson_index is not None:
        current_user.last_active_lesson_idx = payload.lesson_index
            
    # Assign progress dict back since SQLAlchemy JSON mutations aren't always tracked
    current_user.progress = progress
    db.commit()
    db.refresh(current_user)
    
    return current_user

# ─── LEARNING GOALS ───
@router.get("/me/goals", response_model=list[schemas.LearningGoalResponse])
def get_learning_goals(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.LearningGoal).filter(
        models.LearningGoal.user_id == current_user.id
    ).order_by(models.LearningGoal.week_start.desc()).limit(12).all()

@router.get("/me/goals/current", response_model=schemas.LearningGoalResponse)
def get_current_goal(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Get or create this week's learning goal."""
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    
    goal = db.query(models.LearningGoal).filter(
        models.LearningGoal.user_id == current_user.id,
        models.LearningGoal.week_start == week_start
    ).first()
    
    if not goal:
        goal = models.LearningGoal(
            user_id=current_user.id,
            week_start=week_start,
            target_days=current_user.weekly_goal_days or 5,
            target_xp=50
        )
        db.add(goal)
        db.commit()
        db.refresh(goal)
    
    return goal

# ─── SEARCH ───
@router.get("/search")
def search_platform(q: str, db: Session = Depends(get_db)):
    """Search across courses, lessons, and tracks."""
    if not q or len(q) < 2:
        return {"results": []}
    
    results = []
    search_term = f"%{q}%"
    
    # Search courses in DB
    courses = db.query(models.Course).filter(
        models.Course.name.ilike(search_term)
    ).limit(10).all()
    
    for c in courses:
        results.append({
            "type": "course",
            "name": c.name,
            "description": c.description,
            "track": c.track,
            "level": c.level
        })
    
    # Search lessons in DB
    lessons = db.query(models.Lesson).filter(
        models.Lesson.title.ilike(search_term)
    ).limit(10).all()
    
    for l in lessons:
        results.append({
            "type": "lesson",
            "name": l.title,
            "description": l.content[:100] if l.content else None,
            "track": None,
            "level": None
        })
    
    return {"results": results}

# ─── COURSE REVIEWS ───
@router.post("/reviews", response_model=schemas.CourseReviewResponse)
def create_review(
    review: schemas.CourseReviewCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Check if user already reviewed this course
    existing = db.query(models.CourseReview).filter(
        models.CourseReview.user_id == current_user.id,
        models.CourseReview.course_name == review.course_name
    ).first()
    
    if existing:
        # Update existing review
        existing.rating = review.rating
        existing.review_text = review.review_text
        db.commit()
        db.refresh(existing)
        existing.author_name = current_user.full_name
        return existing
    
    db_review = models.CourseReview(
        user_id=current_user.id,
        course_name=review.course_name,
        rating=review.rating,
        review_text=review.review_text
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    db_review.author_name = current_user.full_name
    return db_review

@router.get("/reviews/{course_name}", response_model=list[schemas.CourseReviewResponse])
def get_reviews(course_name: str, db: Session = Depends(get_db)):
    reviews = db.query(models.CourseReview).filter(
        models.CourseReview.course_name == course_name
    ).order_by(models.CourseReview.created_at.desc()).all()
    
    for r in reviews:
        user = db.query(models.User).filter(models.User.id == r.user_id).first()
        r.author_name = user.full_name if user else "Anonymous"
    
    return reviews


@router.post("/reset-password")
def reset_password(payload: schemas.UserResetPassword, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email.ilike(payload.email)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.is_active:
            raise HTTPException(status_code=403, detail="User account is blocked or inactive")
        
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
    if not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    from sqlalchemy import func
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
    
    # New users this week
    week_ago = datetime.utcnow() - timedelta(days=7)
    new_users_week = db.query(models.User).filter(
        models.User.created_at >= week_ago
    ).count()
    
    # Course completions today
    completions_today = db.query(models.CourseCompletion).filter(
        models.CourseCompletion.completed_at >= datetime.combine(today, datetime.min.time())
    ).count()
    
    return {
        "total_users": total_users,
        "mrr": round(mrr, 2),
        "ai_messages_today": int(ai_msgs_today),
        "active_pro_users": active_pro,
        "new_users_week": new_users_week,
        "completions_today": completions_today
    }

# ─── NEW ADMIN CONTROL ENDPOINTS ───

@router.post("/admin/users/{user_id}/grant-pro")
def grant_pro_access(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """Grant a user free lifetime Pro access."""
    if not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    user_to_upgrade = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_to_upgrade:
        raise HTTPException(status_code=404, detail="User not found")
        
    sub = db.query(models.Subscription).filter(models.Subscription.user_id == user_id).first()
    if not sub:
        sub = models.Subscription(user_id=user_id)
        db.add(sub)
        
    sub.plan = "pro_lifetime"
    sub.status = "active"
    sub.current_period_end = None # Lifetime
    db.commit()
    
    return {"message": f"Successfully granted Pro access to {user_to_upgrade.email}"}

@router.post("/admin/users/{user_id}/toggle-block")
def toggle_user_block(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """Toggle a user's blocked (is_active) status."""
    if not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
        
    user_to_toggle = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_to_toggle:
        raise HTTPException(status_code=404, detail="User not found")
        
    if user_to_toggle.id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot block yourself")
        
    user_to_toggle.is_active = not user_to_toggle.is_active
    db.commit()
    
    status_str = "unblocked" if user_to_toggle.is_active else "blocked"
    return {"message": f"User {user_to_toggle.email} is now {status_str}"}

# ─── HEALTH CHECK ───
@router.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


# ─── FORGOT PASSWORD FLOW ───
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

    base_url = os.getenv("BASE_URL", "http://localhost:5173")
    reset_link = f"{base_url}/reset-password?token={token}"
    
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


@router.post("/forgot-password")
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

@router.post("/reset-password-with-token")
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

