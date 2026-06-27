from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database, auth

router = APIRouter(
    prefix="/forum",
    tags=["Forum"]
)

# 1. Get all threads for a specific lesson
@router.get("/lesson/{lesson_name}", response_model=List[schemas.ForumThreadResponse])
def get_lesson_threads(lesson_name: str, db: Session = Depends(database.get_db)):
    threads = db.query(models.ForumThread).filter(models.ForumThread.lesson_name == lesson_name).all()
    return threads

# 2. Create a new thread
@router.post("/", response_model=schemas.ForumThreadResponse)
def create_thread(thread: schemas.ForumThreadCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_thread = models.ForumThread(
        title=thread.title,
        lesson_name=thread.lesson_name,
        user_id=current_user.id
    )
    db.add(db_thread)
    db.commit()
    db.refresh(db_thread)
    return db_thread

# 3. Add a comment to a thread
@router.post("/{thread_id}/comments", response_model=schemas.ForumCommentResponse)
def add_comment(thread_id: int, comment: schemas.ForumCommentCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Verify thread exists
    thread = db.query(models.ForumThread).filter(models.ForumThread.id == thread_id).first()
    if not thread:
        raise HTTPException(status_code=404, detail="Thread not found")
        
    db_comment = models.ForumComment(
        thread_id=thread_id,
        user_id=current_user.id,
        content=comment.content
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
