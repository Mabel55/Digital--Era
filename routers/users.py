from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import hash_password, verify_password, create_access_token, get_current_user
import traceback

router = APIRouter(tags=["Users & Auth"])

@router.post("/signup")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Check if the email is already in PostgreSQL
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the password and save the new user to the database
    hashed_pw = hash_password(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_pw)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully in PostgreSQL!", "email": new_user.email}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email == form_data.username).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        access_token = create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException:
        raise
    except Exception as e:
        error_details = traceback.format_exc()
        print("LOGIN CRASH:", error_details) 
        raise HTTPException(status_code=500, detail=f"LOGIN ERROR: {str(e)}")

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
