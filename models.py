from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime, JSON, Date, Float
from database import Base
from sqlalchemy.orm import relationship


# ─── Utility: Consistent XP → Level Calculation ───
def calculate_level(xp: int) -> str:
    """Single source of truth for XP-based level calculation."""
    if xp >= 1000:
        return "Master"
    elif xp >= 500:
        return "Advanced"
    elif xp >= 100:
        return "Intermediate"
    return "Beginner"


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
    xp = Column(Integer, default=0)
    level = Column(String, default="Beginner")
    streak = Column(Integer, default=0)
    last_login = Column(DateTime, nullable=True)
    progress = Column(JSON, default=dict)

    # Relationship to subscription
    subscription = relationship("Subscription", back_populates="user", uselist=False)
    certificates = relationship("Certificate", back_populates="user")

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

class ForumThread(Base):
    __tablename__ = "forum_threads"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    lesson_name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User")
    comments = relationship("ForumComment", back_populates="thread", cascade="all, delete-orphan")

class ForumComment(Base):
    __tablename__ = "forum_comments"
    
    id = Column(Integer, primary_key=True, index=True)
    thread_id = Column(Integer, ForeignKey("forum_threads.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    thread = relationship("ForumThread", back_populates="comments")
    user = relationship("User")


# ─── MONETIZATION MODELS ───

class Subscription(Base):
    """Tracks user subscription plans (Free, Pro, Team)."""
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    plan = Column(String, default="free")  # "free", "pro_monthly", "pro_yearly"
    status = Column(String, default="active")  # "active", "canceled", "past_due", "trialing"
    stripe_customer_id = Column(String, nullable=True, index=True)
    stripe_subscription_id = Column(String, nullable=True, index=True)
    current_period_start = Column(DateTime, nullable=True)
    current_period_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="subscription")

    @property
    def is_pro(self) -> bool:
        """Check if user has an active Pro subscription."""
        if self.plan == "free":
            return False
        if self.status not in ("active", "trialing"):
            return False
        if self.current_period_end and self.current_period_end < datetime.utcnow():
            return False
        return True


class Certificate(Base):
    """Stores issued certificates with unique verification codes."""
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    course_name = Column(String, nullable=False)
    verification_code = Column(String, unique=True, index=True, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="certificates")


class AIUsage(Base):
    """Tracks daily AI tutor message usage per user for free-tier limits."""
    __tablename__ = "ai_usage"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    usage_date = Column(Date, default=date.today, nullable=False)
    message_count = Column(Integer, default=0)

class PasswordResetToken(Base):
    """Stores tokens for the forgot password flow."""
    __tablename__ = "password_reset_tokens"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    
    user = relationship("User")


