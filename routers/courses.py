from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

router = APIRouter(tags=["Courses & Lessons"])

@router.post("/courses/", response_model=schemas.CourseResponse)
def create_course(
    course: schemas.CourseCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    # 1. Role Check: Only admins can manage structural course assets
    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to create courses")
    
    # 2. Database Safety Check: Ensure the chosen teacher user actually exists
    teacher_exists = db.query(models.User).filter(models.User.id == course.teacher_id).first()
    if not teacher_exists:
        raise HTTPException(
            status_code=404, 
            detail=f"PostgreSQL Safety Block: User ID {course.teacher_id} does not exist."
        )

    # 3. Map Pydantic input directly to your SQLAlchemy columns dynamically
    db_course = models.Course(
        name=course.title, 
        description=course.description, 
        teacher_id=course.teacher_id  # 👈 Dynamic instead of hardcoded 1!
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses/", response_model=list[schemas.CourseResponse])
def get_all_courses(db: Session = Depends(get_db)):
    # Publicly accessible so students can browse courses
    return db.query(models.Course).all()

@router.get("/courses/{course_id}", response_model=schemas.CourseResponse)
def get_single_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/lessons/", response_model=schemas.LessonResponse)
def create_lesson(
    lesson: schemas.LessonCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    # Role-based check: Only allow admins to create lessons
    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to create lessons")
        
    # Verify the target course actually exists
    course = db.query(models.Course).filter(models.Course.id == lesson.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Target course not found")
        
    db_lesson = models.Lesson(
        title=lesson.title,
        content=lesson.content,
        course_id=lesson.course_id
    )
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson
