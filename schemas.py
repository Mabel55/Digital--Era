from __future__ import annotations
from pydantic import BaseModel, Field, AliasChoices
from typing import Optional, List
from datetime import datetime

# --- STUDENT SCHEMAS ---
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    grade_level: str

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    grade_level: Optional[str] = None

# --- TEACHER SCHEMAS ---
class TeacherCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    subject: str

class TeacherUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    subject: str | None = None

# --- LESSON SCHEMAS ---
class LessonBase(BaseModel):
    title: str
    content: str
    expected_output: Optional[str] = None

class LessonCreate(LessonBase):
    course_id: int

class LessonResponse(LessonBase):
    id: int
    course_id: int

    class Config:
        from_attributes = True

# --- COURSE SCHEMAS ---
class CourseBase(BaseModel):
    title: str = Field(validation_alias=AliasChoices('title', 'name'))
    description: str | None = None

class CourseCreate(CourseBase):
    teacher_id: int

class CourseResponse(CourseBase):
    id: int
    teacher_id: int
    lessons: List[LessonResponse] = []

    class Config:
        from_attributes = True

# --- USER SCHEMAS ---
class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    role: str = "student"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: Optional[bool] = True
    xp: Optional[int] = 0
    level: Optional[str] = "Beginner"
    streak: Optional[int] = 0
    progress: Optional[dict] = {}

    class Config:
        from_attributes = True

# --- MISC SCHEMAS ---
class ChatRequest(BaseModel):
    message: str
    level: str = "Beginner"
    track: str = "General"
    course: str = "General Setup"
    lesson_id: Optional[int] = None

class UserLogin(BaseModel):
    email: str
    password: str

class CodeSubmission(BaseModel):
    code: Optional[str] = None
    language: str = "python"
    files: Optional[dict[str, str]] = None
    entrypoint: Optional[str] = "main.py"

class ChatMessage(BaseModel):
    message: str

class UserResetPassword(BaseModel):
    email: str
    new_password: str

# --- FORUM SCHEMAS ---
class ForumCommentBase(BaseModel):
    content: str

class ForumCommentCreate(ForumCommentBase):
    pass

class ForumCommentResponse(ForumCommentBase):
    id: int
    thread_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ForumThreadBase(BaseModel):
    title: str
    lesson_name: str

class ForumThreadCreate(ForumThreadBase):
    pass

class ForumThreadResponse(ForumThreadBase):
    id: int
    user_id: int
    created_at: datetime
    comments: List[ForumCommentResponse] = []

    class Config:
        from_attributes = True

# Rebuild models
LessonResponse.model_rebuild()
CourseResponse.model_rebuild()
ForumThreadResponse.model_rebuild()