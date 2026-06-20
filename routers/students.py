from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        grade_level=student.grade_level
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/")
def get_students(db: Session = Depends(get_db)):
    all_students = db.query(models.Student).all()
    return all_students

@router.put("/{student_id}")
def update_student(student_id: int, student_update: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_data = student_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
        
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"message": f"Student {student_id} has been successfully deleted from Digital Era"}
