from __future__ import annotations
from pydantic import BaseModel, Field, AliasChoices
from typing import Optional
from pydantic import BaseModel
#This validates the data a user send when creating a new student
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    grade_level: str

# This allows us to update only specific fields without overwriting everything
class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    grade_level: Optional[str] = None

# Validates data when creating a new teacher
class TeacherCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    subject: str

class CourseCreate(BaseModel):
    name: str
    teacher_id: int

class TeacherUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    subject: str | None = None

# ==========================================
# LESSON SCHEMAS (For AI Curriculum)
# ==========================================
class LessonBase(BaseModel):
    title: str
    content: str
    expected_output: Optional[str] = None

class LessonCreate(LessonBase):
    course_id: int

class Lesson(LessonBase):
    id: int
    course_id: int

    class Config:
        from_attributes = True

# ==========================================
# COURSE RESPONSE (To link lessons to courses)
# ==========================================
class CourseResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    teacher_id: int
    lessons: List[Lesson] = [] # This automatically fetches all lessons for the course!

    class Config:
        from_attributes = True

# ==========================================
# USER SCHEMAS (For Authentication/Login)
# ==========================================
class UserBase(BaseModel):
    email: str
    full_name: str
    role: str = "student" # Defaults to student for security

class UserCreate(UserBase):
    password: str # Raw password (we will hash this in main.py)

class UserResponse(UserBase):
    id: int
    is_active: bool
    xp: int
    level: str
    streak: int
    progress: dict
    # We explicitly exclude the password here so it never leaks to the frontend!

    class Config:
        from_attributes = True



# --- LESSON SCHEMAS ---
class LessonBase(BaseModel):
    title: str
    content: str

class LessonCreate(LessonBase):
    course_id: int

class LessonResponse(LessonBase):
    id: int
    course_id: int

    class Config:
        from_attributes = True


# --- COURSE SCHEMAS ---
class CourseBase(BaseModel):
    title: str
    description: str | None = None  # Clean, modern native type hint

class CourseCreate(CourseBase):
    teacher_id: int

class CourseResponse(CourseBase):
    id: int
    title: str = Field(validation_alias=AliasChoices('title', 'name'))
    teacher_id: int  # Added this so you can see the teacher's ID in the response!
    lessons: list[LessonResponse] = []

    class Config:
        from_attributes = True

# Explicitly tell Pydantic to seal both schemas perfectly
LessonResponse.model_rebuild()
CourseResponse.model_rebuild()

from pydantic import BaseModel

# --- AI Chat Schemas ---
class ChatRequest(BaseModel):
    message: str
    level: str = "Beginner"
    track: str = "General"
    course: str ="General Setup"

# --- Authentication Schemas ---
class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str
    role: str ="student"

class UserLogin(BaseModel):
    email: str
    password: str

class CodeSubmission(BaseModel):
    code: str

class ChatMessage(BaseModel):
    message: str