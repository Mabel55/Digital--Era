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

router = APIRouter(tags=["Users & Auth"])

@router.post("/signup")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # 1. Check if the email is already in PostgreSQL
        existing_user = db.query(models.User).filter(models.User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # 2. Hash the password and save the new user to the database
        hashed_pw = hash_password(user.password)
        new_user = models.User(email=user.email, hashed_password=hashed_pw, full_name=user.full_name, role=user.role)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {"message": "User created successfully in PostgreSQL!", "email": new_user.email}
    except HTTPException:
        raise
    except Exception as e:
        # Return a 400 instead of 500 so Azure doesn't mask the error text!
        import traceback
        print("SIGNUP CRASH", traceback.format_exc())
        raise HTTPException(status_code=400, detail=f"DB_CRASH: {str(e)}")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email == form_data.username).first()
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

@router.get("/users/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if user exists
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
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
        return new_user

    except Exception as e:
        error_details = traceback.format_exc()
        print("BACKEND CRASH:", error_details) 
        raise HTTPException(status_code=500, detail=f"PYTHON ERROR: {str(e)}")

@router.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

class ProgressUpdate(BaseModel):
    course_name: str
    lesson_index: int

@router.post("/users/me/progress", response_model=schemas.UserResponse)
def update_progress(payload: ProgressUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    xp_to_add = 10
    
    progress = dict(current_user.progress) if current_user.progress else {}
    if payload.course_name not in progress:
        progress[payload.course_name] = {"completed_lessons": 0}
        
    current_completed = progress[payload.course_name].get("completed_lessons", 0)
    
    # Award XP if they completed a new lesson
    if payload.lesson_index >= current_completed:
        progress[payload.course_name]["completed_lessons"] = payload.lesson_index + 1
        current_user.xp += xp_to_add
        
        # Calculate level based on XP
        if current_user.xp >= 1000:
            current_user.level = "Master"
        elif current_user.xp >= 500:
            current_user.level = "Advanced"
        elif current_user.xp >= 100:
            current_user.level = "Intermediate"
        else:
            current_user.level = "Beginner"
            
    # Assign progress dict back since SQLAlchemy JSON mutations aren't always tracked
    current_user.progress = progress
    db.commit()
    db.refresh(current_user)
    
    return current_user
