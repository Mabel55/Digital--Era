from fastapi.responses import FileResponse
import bcrypt
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, User
import schemas
import models
from jose import jwt, JWTError
from schemas import ChatRequest, UserCreate, UserLogin
from ai_brain import load_embedding_model, ask_gemini
from langchain_community.vectorstores import FAISS
from auth import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM
import shutil
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pydantic import BaseModel
import requests
from schemas import CodeSubmission, ChatMessage
import subprocess
import tempfile


# 1. Build the database tables safely
Base.metadata.create_all(bind=engine)

# 2. Initialize the web server
app = FastAPI()


# 3. Security Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")





# (And just in case you need the verify function to match it!)
def verify_password(plain_password: str, hashed_password: str):
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_bytes)

def get_password_hash(password: str):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')


@app.get("/")
def serve_frontend_root():
    # This loads the dashboard when students visit digital-era.live
    return FileResponse("index.html")

@app.get("/index.html")
def serve_frontend_explicit():
    # This catches anyone who manually types /index.html in the address bar
    return FileResponse("index.html")


# This is your brand new route to ADD a student!

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token using our secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Fetch the user matching the token's email
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

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


@app.get("/courses/")
def get_courses(db: Session = Depends(get_db)):
    all_courses = db.query(models.Course).all()
    return all_courses

@app.put("/teachers/{teacher_id}")
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

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Check if the email is already taken
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the raw password
    hashed_pwd = get_password_hash(user.password)
    
    # 3. Create the new user object
    new_user = models.User(
        email=user.email,
        hashed_password=hashed_pwd,
        full_name=user.full_name,
        role=user.role
    )
    
    # 4. Save to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # 5. Return the user (FastAPI will automatically use UserResponse to hide the password!)
    return new_user


@app.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    # This route is completely locked down. Only users with a valid token can get here!
    return current_user

# ==========================================
# COURSE ENDPOINTS
# ==========================================

@app.post("/courses/", response_model=schemas.CourseResponse)
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

@app.get("/courses/", response_model=list[schemas.CourseResponse])
def get_all_courses(db: Session = Depends(get_db)):
    # Publicly accessible so students can browse courses
    return db.query(models.Course).all()

@app.get("/courses/{course_id}", response_model=schemas.CourseResponse)
def get_single_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


# ==========================================
# LESSON ENDPOINTS
# ==========================================

@app.post("/lessons/", response_model=schemas.LessonResponse)
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



# 2. Create the API Route
@app.post("/chat", tags=["AI Tutor"])
def chat_with_study_buddy(
    payload: schemas.ChatRequest, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user) # 🔒 Protects the route and tracks the student
):
    try:
        # 1. Fetch all past messages between this student and the AI from PostgreSQL
        past_messages = db.query(models.ChatMessage)\
                          .filter(models.ChatMessage.user_id == current_user.id)\
                          .order_by(models.ChatMessage.timestamp.asc())\
                          .all()

        # 2. Your core embedding layout
        
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=os.getenv("GEMINI_API_KEY"))
        
        # 3. Connect to your local FAISS brain matrix safely
        vector_db = FAISS.load_local(
            "study_buddy_brain",
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        # 4. Search your vector database for the 3 most relevant lesson chunks
        docs = vector_db.similarity_search(payload.question, k=3)
        context_chunks = [doc.page_content for doc in docs]
        
        # 5. Run your LangChain engine passing BOTH the vector context AND the database history!
        answer = ask_gemini(
            question=payload.question, 
            context_chunks=context_chunks, 
            chat_history=past_messages
        )
        
        # 6. Save the student's input question to PostgreSQL
        student_msg = models.ChatMessage(user_id=current_user.id, role="user", content=payload.question)
        db.add(student_msg)

        # 7. Save Gemini's answer to PostgreSQL right next to it
        ai_msg = models.ChatMessage(user_id=current_user.id, role="model", content=answer)
        db.add(ai_msg)
        
        # Commit the transaction to save the chat long-term
        db.commit()
        
        # Return the response along with your document sources
        return {
            "answer": answer,
            "sources_used": [doc.metadata.get("title", "Unknown") for doc in docs]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Brain Error: {str(e)}")

@app.post("/signup", tags=["Authentication"])
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Check if the email is already in PostgreSQL
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the password and save the new user to the database
    hashed_pw = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pw)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully in PostgreSQL!", "email": new_user.email}

@app.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), # 👈 Captures the Swagger popup fields!
    db: Session = Depends(get_db)
):
    # 1. Look up the user (Note: Swagger saves the email inside form_data.username)
    db_user = db.query(models.User).filter(models.User.email == form_data.username).first()
    
    # 2. Check if user exists and password matches
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # 3. Generate and hand back the secure token
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# 2. Add the secure Admin Upload Route
@app.post("/admin/upload-course-pdf/", tags=["Admin Panel"])
def upload_course_material(
    course_title: str,
    file: UploadFile = File(...),
    current_user: models.User = Depends(get_current_user)
):
    # 1. Ultimate Security Check: Only Admins can upload curriculums!
    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Only academy admins can upload materials.")
        
    # 2. Ensure it's actually a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    # 3. Save the uploaded file temporarily to the server
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # 4. Send the file to the AI Brain for processing!
        from ai_brain import add_pdf_to_vector_db
        chunks_learned = add_pdf_to_vector_db(temp_file_path, course_title)
        
        return {
            "status": "Success",
            "message": f"Successfully digested '{file.filename}'.",
            "knowledge_chunks_added": chunks_learned
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Brain processing failed: {str(e)}")
        
    finally:
        # 5. Clean up! Delete the temporary PDF off the server so it doesn't waste space
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


# 2. Create the execution endpoint



@app.post("/run-python/")
def execute_python_code(submission: CodeSubmission):
    # 1. Create a secure temporary file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_file:
        temp_file.write(submission.code)
        temp_file_path = temp_file.name

    try:
        # 2. Run the file natively with a 5-second timeout
        result = subprocess.run(
            ["python", temp_file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        # 3. Grab the output
        output = result.stdout
        error_output = result.stderr
        exit_code = result.returncode
        
        final_output = output if exit_code == 0 else error_output
        
        return {
            "output": final_output,
            "exit_code": exit_code
        }
            
    except subprocess.TimeoutExpired:
        return {"output": "Error: Code took too long to run (Infinite Loop?).", "exit_code": 1}
    except Exception as e:
        return {"output": f"Server Error: {str(e)}", "exit_code": 1}
    finally:
        # 4. Always clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
   

@app.post("/ask-ai/")
def ask_ai_tutor(chat: schemas.ChatRequest): # 1. Changed to ChatRequest to accept the 4 entities!
    try:
        # 1. Initialize your Google Embeddings
        embeddings = load_embedding_model()

        # 2. Load your saved FAISS textbook database
        vector_db = FAISS.load_local("study_buddy_brain", embeddings, allow_dangerous_deserialization=True)

        # 3. Search the database for relevant context (using chat.message now!)
        docs = vector_db.similarity_search(chat.message, k=3)

        # 4. Combine those paragraphs into one big string of context
        textbook_context = "\n\n".join([doc.page_content for doc in docs])

        # 5. Create a dynamic system prompt using the student's level, track, and course!
        system_prompt = f"""You are Mabel, a senior software engineering instructor at Mabel Academy - a coding school for Nigerian developers.
        You are teaching a {chat.level} student who wants to master {chat.track}.
        Current course: {chat.course}.
        Be encouraging, concise, and use Nigerian examples when helpful (Lagos, Naira, jollof rice, etc).
        Never give full solutions unless grading - give hints, ask questions, guide thinking.
        Format code with proper markdown code blocks.
        
        Use the following textbook context to help answer the student's question accurately:
        {textbook_context}"""

        # 6. Send BOTH the question and our custom system prompt context to Gemini!
        ai_reply = ask_gemini(chat.message, system_prompt)

        return {"reply": ai_reply}

    except Exception as e:
        return {"reply": f"System Error: Could not connect to the database. Details: {str(e)}"}

@app.get("/courses.js")
def serve_courses_js():
    return FileResponse("courses.js")