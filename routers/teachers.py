from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/teachers", tags=["Teachers"])

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
