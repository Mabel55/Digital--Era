from pydantic import BaseModel
from typing import Optional

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