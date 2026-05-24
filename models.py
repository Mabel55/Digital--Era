from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime
from database import Base
from sqlalchemy.orm import relationship


class Student(Base):
    # This is the actual name the table will have inside PostgreSQL
    __tablename__ = "students"

    # These are the columns inside our table
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    grade_level = Column(String)

class Teacher(Base):
    # The name of the table in PostgreSQL
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subject = Column(String) # What subject do they teach?

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True) # Added for LMS
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    # --- NEW: Level and Track columns ---
    level = Column(String, default="Beginner") # e.g., "Beginner", "Intermediate", "Advanced"
    track = Column(String, default="General")  # e.g., "Backend", "Data Science", "AI"

    # Magic link to the new lessons we are about to create!
    lessons = relationship("Lesson", back_populates="course")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text) # Your markdown notes and AI context go here
    expected_output = Column(Text, nullable=True) # For auto-grading code later
    course_id = Column(Integer, ForeignKey("courses.id"))

    # Links back up to your Course table
    course = relationship("Course", back_populates="lessons")


class User(Base):
    __tablename__ = "users"
    chat_messages = relationship("ChatMessage", back_populates="user", cascade="all, delete-orphan")

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String, default="student") # Can be "student" or "admin"
    is_active = Column(Boolean, default=True)

# Add this to the bottom of models.py

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    role = Column(String, nullable=False)  # Will store either "user" or "model"
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship to easily link messages back to a user profile
    user = relationship("User", back_populates="chat_messages")

