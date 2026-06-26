from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
import json
from auth import get_current_user
from ai_brain import ask_gemini

router = APIRouter(tags=["Courses & Lessons"])

@router.post("/courses/", response_model=schemas.CourseResponse)
def create_course(
    course: schemas.CourseCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    # 1. Role Check: Only admins can manage structural course assets
    if current_user.role.lower() != "admin" and current_user.email != "nasaadanna@gmail.com":
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
    if current_user.role.lower() != "admin" and current_user.email != "nasaadanna@gmail.com":
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

@router.get("/lessons/", response_model=list[schemas.LessonResponse])
def get_all_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()

@router.get("/courses/{course_id}/lessons", response_model=list[schemas.LessonResponse])
def get_course_lessons(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return db.query(models.Lesson).filter(models.Lesson.course_id == course_id).all()

@router.get("/lessons/{lesson_id}", response_model=schemas.LessonResponse)
def get_single_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.put("/lessons/{lesson_id}", response_model=schemas.LessonResponse)
def update_lesson(
    lesson_id: int,
    lesson_update: schemas.LessonBase,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role.lower() != "admin" and current_user.email != "nasaadanna@gmail.com":
        raise HTTPException(status_code=403, detail="Not authorized to update lessons")
    
    db_lesson = db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()
    if not db_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
        
    db_lesson.title = lesson_update.title
    db_lesson.content = lesson_update.content
    db_lesson.expected_output = lesson_update.expected_output
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

@router.delete("/lessons/{lesson_id}")
def delete_lesson(
    lesson_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role.lower() != "admin" and current_user.email != "nasaadanna@gmail.com":
        raise HTTPException(status_code=403, detail="Not authorized to delete lessons")
        
    db_lesson = db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()
    if not db_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
        
    db.delete(db_lesson)
    db.commit()
    return {"message": "Lesson deleted successfully"}

@router.post("/lessons/{lesson_id}/submit")
def submit_code(
    lesson_id: int,
    submission: schemas.CodeSubmission,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    lesson = db.query(models.Lesson).filter(models.Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    system_prompt = f"""You are an automated grading system.
The student has submitted code for the lesson '{lesson.title}'.
Lesson Content: {lesson.content}
Expected Output/Behavior: {lesson.expected_output or 'Determine if the code accomplishes the main objective of the lesson.'}

Student's code:
```
{submission.code}
```

Evaluate the code. You must reply strictly in valid JSON format:
{{
  "passed": true or false,
  "feedback": "A short, encouraging sentence explaining why it passed or failed."
}}"""

    try:
        response = ask_gemini("Evaluate the code.", context_chunks=[], system_prompt_override=system_prompt)
        
        # Parse the JSON. Gemini might wrap it in markdown block.
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0].strip()
        elif "```" in response:
            response = response.split("```")[1].strip()
            
        result = json.loads(response)
        
        return result
        
    except Exception as e:
        return {"passed": False, "feedback": f"Grading Error: {str(e)}"}
