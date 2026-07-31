from __future__ import annotations
from pydantic import BaseModel, Field, AliasChoices
from typing import Optional, List
from datetime import datetime, date

try:
    from pydantic import EmailStr
except ImportError:
    # Fallback if pydantic[email] not installed
    EmailStr = str

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

# --- SUBSCRIPTION SCHEMAS ---
class SubscriptionResponse(BaseModel):
    plan: str = "free"
    status: str = "active"
    is_pro: bool = False
    current_period_end: Optional[datetime] = None
    paystack_customer_code: Optional[str] = None

    class Config:
        from_attributes = True

# --- USER SCHEMAS ---
class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    role: str = "student"

class UserCreate(UserBase):
    password: str
    referral_code: Optional[str] = None

class UserProfileUpdate(BaseModel):
    """Schema for updating user profile — replaces the mocked save."""
    full_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    country: Optional[str] = None
    preferred_language: Optional[str] = None
    goal: Optional[str] = None
    weekly_goal_days: Optional[int] = None

class UserResponse(UserBase):
    id: int
    is_active: Optional[bool] = True
    xp: Optional[int] = 0
    level: Optional[str] = "Beginner"
    streak: Optional[int] = 0
    longest_streak: Optional[int] = 0
    progress: Optional[dict] = {}
    subscription: Optional[SubscriptionResponse] = None
    created_at: Optional[datetime] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    country: Optional[str] = None
    preferred_language: Optional[str] = "en"
    goal: Optional[str] = None
    weekly_goal_days: Optional[int] = 5
    last_active_course: Optional[str] = None
    last_active_lesson_idx: Optional[int] = 0

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
    email: EmailStr
    old_password: str
    new_password: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordTokenRequest(BaseModel):
    token: str
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
    author_name: Optional[str] = None
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
    author_name: Optional[str] = None
    created_at: datetime
    comments: List[ForumCommentResponse] = []

    class Config:
        from_attributes = True

# --- CERTIFICATE SCHEMAS ---
class CertificateResponse(BaseModel):
    id: int
    course_name: str
    verification_code: str
    issued_at: datetime
    student_name: Optional[str] = None

    class Config:
        from_attributes = True

# --- AI USAGE SCHEMAS ---
class AIUsageResponse(BaseModel):
    messages_used: int = 0
    daily_limit: int = 5
    is_limited: bool = True

# --- USER ACTIVITY SCHEMAS (Real analytics) ---
class UserActivityResponse(BaseModel):
    activity_date: date
    xp_earned: int = 0
    lessons_completed: int = 0
    challenges_completed: int = 0
    time_spent_minutes: int = 0

    class Config:
        from_attributes = True

# --- COURSE COMPLETION SCHEMAS ---
class CourseCompletionResponse(BaseModel):
    id: int
    course_name: str
    completed_at: datetime
    total_lessons: int = 0
    score_percent: float = 100.0

    class Config:
        from_attributes = True

# --- DAILY CHALLENGE SCHEMAS ---
class DailyChallengeResponse(BaseModel):
    id: int
    challenge_date: date
    title: str
    description: str
    difficulty: str = "Beginner"
    language: str = "python"
    starter_code: Optional[str] = None
    hint: Optional[str] = None
    xp_reward: int = 25
    already_completed: bool = False

    class Config:
        from_attributes = True

class DailyChallengeSubmit(BaseModel):
    challenge_id: int
    code: str

# --- NOTIFICATION SCHEMAS ---
class NotificationResponse(BaseModel):
    id: int
    type: str
    title: str
    message: str
    action_url: Optional[str] = None
    is_read: bool = False
    created_at: datetime

    class Config:
        from_attributes = True

# --- COURSE REVIEW SCHEMAS ---
class CourseReviewCreate(BaseModel):
    course_name: str
    rating: int  # 1-5
    review_text: Optional[str] = None

class CourseReviewResponse(BaseModel):
    id: int
    user_id: int
    course_name: str
    rating: int
    review_text: Optional[str] = None
    created_at: datetime
    author_name: Optional[str] = None

    class Config:
        from_attributes = True

# --- LEARNING GOAL SCHEMAS ---
class LearningGoalResponse(BaseModel):
    id: int
    week_start: date
    target_days: int = 5
    actual_days: int = 0
    target_xp: int = 50
    actual_xp: int = 0
    completed: bool = False

    class Config:
        from_attributes = True

class LearningGoalCreate(BaseModel):
    target_days: int = 5
    target_xp: int = 50

# --- ASSESSMENT RESULT SCHEMAS ---
class AssessmentResultResponse(BaseModel):
    id: int
    topic: str
    score: int
    max_score: int
    skill_score: int
    xp_gained: int = 0
    taken_at: datetime
    questions_data: Optional[dict] = None

    class Config:
        from_attributes = True

# --- SEARCH SCHEMA ---
class SearchResult(BaseModel):
    type: str  # "course", "lesson", "track"
    name: str
    description: Optional[str] = None
    track: Optional[str] = None
    level: Optional[str] = None

# Rebuild models
LessonResponse.model_rebuild()
CourseResponse.model_rebuild()
ForumThreadResponse.model_rebuild()
UserResponse.model_rebuild()