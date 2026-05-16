from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas

# Build the tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# This is a helper function to open and close the database connection safely
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Digital Era!"}

# This is your brand new route to ADD a student!
@app.post("/students/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # 1. Translate the user's data into a database model
    db_student = models.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        grade_level=student.grade_level
    )
    # 2. Add it to the database and save (commit)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    # 3. Return the newly created student to the screen
    return db_student

# This is your route to GET all students!
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    # Query the database for every single student in the table
    all_students = db.query(models.Student).all()
    return all_students

# This is your route to UPDATE a specific student!
@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: schemas.StudentUpdate, db: Session = Depends(get_db)):
    # 1. Search the database for the student with this ID
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    # 2. If they don't exist, throw a 404 error
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # 3. Only update the fields the user actually typed in
    update_data = student_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
        
    # 4. Save the changes to PostgreSQL
    db.commit()
    db.refresh(db_student)
    return db_student

# This is your route to DELETE a student!
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    # 1. Search the database for the student
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    # 2. If they don't exist, throw a 404 error
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # 3. Delete the record and save the changes
    db.delete(db_student)
    db.commit()
    
    # 4. Return a success message
    return {"message": f"Student {student_id} has been successfully deleted from Digital Era"}

# --- TEACHER ROUTES ---

@app.post("/teachers/")
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

@app.get("/teachers/")
def get_teachers(db: Session = Depends(get_db)):
    all_teachers = db.query(models.Teacher).all()
    return all_teachers

# --- COURSE ROUTES ---

@app.post("/courses/")
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(
        name=course.name,
        teacher_id=course.teacher_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/")
def get_courses(db: Session = Depends(get_db)):
    all_courses = db.query(models.Course).all()
    return all_courses