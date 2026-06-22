from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
import os
import shutil
from ai_brain import add_pdf_to_vector_db

router = APIRouter(prefix="/teachers", tags=["Teachers"])

@router.post("/upload-pdf/")
async def upload_pdf(
    file: UploadFile = File(...),
    course_title: str = Form(...),
    course_level: str = Form("Beginner"),
    course_track: str = Form("General"),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Save temp file
    temp_path = f"/tmp/{file.filename}"
    # Windows compatibility for temp path:
    temp_path = os.path.join(os.environ.get("TEMP", "/tmp"), file.filename)
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        add_pdf_to_vector_db(temp_path, course_title, course_level, course_track)
        return {"message": "PDF ingested successfully into the AI Brain."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to ingest PDF: {str(e)}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@router.post("/")
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(
        first_name=teacher.first_name,
        last_name=teacher.last_name,
        email=teacher.email,
        subject=teacher.subject
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
    all_teachers = db.query(models.Teacher).all()
    return all_teachers

@router.put("/{teacher_id}")
def update_teacher(teacher_id: int, teacher_data: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    # Update only the fields provided
    for key, value in teacher_data.dict(exclude_unset=True).items():
        setattr(db_teacher, key, value)
        
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
