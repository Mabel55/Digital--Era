from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime, JSON, Date, Float
from database import Base
from sqlalchemy.orm import relationship


# ─── Utility: Consistent XP → Level Calculation ───
def calculate_level(xp: int) -> str:
    """Single source of truth for XP-based level calculation."""
    if xp >= 5000:
        return "Grandmaster"
    elif xp >= 2500:
        return "Expert"
    elif xp >= 1000:
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

    # --- Level, Track and Duration columns ---
    level = Column(String, default="Beginner") # e.g., "Beginner", "Intermediate", "Advanced"
    track = Column(String, default="General")  # e.g., "Backend", "Data Science", "AI"
    estimated_hours = Column(Float, default=2.0)  # Estimated hours to complete

    # Magic link to the new lessons we are about to create!
    lessons = relationship("Lesson", back_populates="course")
    reviews = relationship("CourseReview", back_populates="course")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text) # Your markdown notes and AI context go here
    expected_output = Column(Text, nullable=True) # For auto-grading code later
    course_id = Column(Integer, ForeignKey("courses.id"))
    order_index = Column(Integer, default=0)  # For lesson ordering

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
    longest_streak = Column(Integer, default=0)  # Track personal best streak
    last_login = Column(DateTime, nullable=True)
    progress = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)  # Track when users joined

    # Profile fields for international competitiveness
    avatar_url = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    github_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    country = Column(String, nullable=True)
    preferred_language = Column(String, default="en")
    goal = Column(String, nullable=True)  # Learning goal
    weekly_goal_days = Column(Integer, default=5)  # Days per week target
    last_active_course = Column(String, nullable=True)  # For "Continue Learning"
    last_active_lesson_idx = Column(Integer, default=0)  # For "Continue Learning"

    # Relationship to subscription
    subscription = relationship("Subscription", back_populates="user", uselist=False)
    certificates = relationship("Certificate", back_populates="user")
    activities = relationship("UserActivity", back_populates="user", cascade="all, delete-orphan")
    completions = relationship("CourseCompletion", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("CourseReview", back_populates="user")
    learning_goals = relationship("LearningGoal", back_populates="user", cascade="all, delete-orphan")


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
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    plan = Column(String, default="free")
    status = Column(String, default="active")
    current_period_end = Column(DateTime, nullable=True)

    paystack_customer_code = Column(String, nullable=True)
    paystack_subscription_code = Column(String, nullable=True)

    access_grants = Column(JSON, default=dict) # {"track:Backend": "2026-10-09T00:00:00Z", "course:Python Basics": None}

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


# ─── NEW: ENGAGEMENT & ANALYTICS MODELS ───

class UserActivity(Base):
    """Tracks daily XP gains for real analytics charts (replaces mock data)."""
    __tablename__ = "user_activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    activity_date = Column(Date, default=date.today, nullable=False)
    xp_earned = Column(Integer, default=0)
    lessons_completed = Column(Integer, default=0)
    challenges_completed = Column(Integer, default=0)
    time_spent_minutes = Column(Integer, default=0)

    user = relationship("User", back_populates="activities")


class CourseCompletion(Base):
    """Tracks actual course completions with timestamps for certificates."""
    __tablename__ = "course_completions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    course_name = Column(String, nullable=False, index=True)
    completed_at = Column(DateTime, default=datetime.utcnow)
    total_lessons = Column(Integer, default=0)
    score_percent = Column(Float, default=100.0)

    user = relationship("User", back_populates="completions")


class DailyChallenge(Base):
    """Stores daily coding challenges — DataCamp's #1 retention driver."""
    __tablename__ = "daily_challenges"

    id = Column(Integer, primary_key=True, index=True)
    challenge_date = Column(Date, default=date.today, unique=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String, default="Beginner")  # Beginner, Intermediate, Advanced
    language = Column(String, default="python")
    starter_code = Column(Text, nullable=True)
    solution = Column(Text, nullable=True)
    hint = Column(Text, nullable=True)
    test_cases = Column(JSON, nullable=True)  # [{input: "", expected: ""}]
    xp_reward = Column(Integer, default=25)
    created_at = Column(DateTime, default=datetime.utcnow)


class DailyChallengeSubmission(Base):
    """Tracks user submissions for daily challenges."""
    __tablename__ = "daily_challenge_submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    challenge_id = Column(Integer, ForeignKey("daily_challenges.id", ondelete="CASCADE"), nullable=False)
    submitted_code = Column(Text, nullable=True)
    passed = Column(Boolean, default=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    challenge = relationship("DailyChallenge")


class Notification(Base):
    """In-app notifications for engagement and re-engagement."""
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    type = Column(String, nullable=False)  # streak, achievement, course, challenge, system
    title = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    action_url = Column(String, nullable=True)  # e.g., /workspace/PythonFundamentals
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")


class CourseReview(Base):
    """Course ratings and reviews for social proof."""
    __tablename__ = "course_reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=True)
    course_name = Column(String, nullable=False, index=True)  # For static courses
    rating = Column(Integer, nullable=False)  # 1-5 stars
    review_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    course = relationship("Course", back_populates="reviews")


class LearningGoal(Base):
    """Weekly/monthly learning goals for commitment tracking."""
    __tablename__ = "learning_goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    week_start = Column(Date, nullable=False)
    target_days = Column(Integer, default=5)
    actual_days = Column(Integer, default=0)
    target_xp = Column(Integer, default=50)
    actual_xp = Column(Integer, default=0)
    completed = Column(Boolean, default=False)

    user = relationship("User", back_populates="learning_goals")


class AssessmentResult(Base):
    """Stores assessment history to track improvement over time."""
    __tablename__ = "assessment_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    topic = Column(String, nullable=False, index=True)
    score = Column(Integer, nullable=False)
    max_score = Column(Integer, nullable=False)
    skill_score = Column(Integer, nullable=False)  # Normalized 0-300
    xp_gained = Column(Integer, default=0)
    questions_data = Column(JSON, nullable=True)  # Store Q&A for review
    taken_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

class LessonTranslationCache(Base):
    """Caches AI-generated translations to save cost and increase speed."""
    __tablename__ = "lesson_translation_cache"

    id = Column(String, primary_key=True, index=True) # Hash of english_text + target_language
    original_text = Column(Text, nullable=False)
    target_language = Column(String, nullable=False, index=True)
    translated_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class AITutorCache(Base):
    """Caches AI Tutor questions and responses to lower API costs."""
    __tablename__ = "ai_tutor_cache"

    id = Column(String, primary_key=True, index=True) # Hash of normalized question + context
    question = Column(String, index=True)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


# ─── DIGITAL ERA AI 2.0 — MEMORY SYSTEM (Phase 2) ───

class EpisodicMemory(Base):
    """
    Stores important past interactions and events for each student.
    Examples: "Student struggled with Python loops 3 times",
              "Student had a breakthrough understanding recursion".
    Used by the AI Orchestrator to personalize responses.
    """
    __tablename__ = "episodic_memories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    memory_type = Column(String(50), nullable=False, index=True)  # struggle, breakthrough, misconception, preference, error_pattern
    topic = Column(String(255), nullable=True, index=True)
    summary = Column(Text, nullable=False)
    importance = Column(Float, default=0.5)       # 0.0 to 1.0, for retrieval ranking
    metadata_json = Column(JSON, default=dict)    # Flexible storage for context (lesson_id, course, error details, etc.)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_accessed = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")


class SemanticMemory(Base):
    """
    Stores stable facts about the learner and their knowledge.
    Examples: "Knows Python basics", "Goal: become data scientist",
              "Prefers code examples over theory".
    Updated infrequently as the system learns more about the student.
    """
    __tablename__ = "semantic_memories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    fact_type = Column(String(50), nullable=False, index=True)  # skill, strength, weakness, goal, preference, background
    key = Column(String(255), nullable=False)                    # e.g., "python_loops", "learning_style"
    value = Column(Text, nullable=False)                         # e.g., "struggles with nested loops", "visual learner"
    confidence = Column(Float, default=0.5)                      # 0.0 to 1.0, how certain we are
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

    __table_args__ = (
        # Each user has at most one fact per (fact_type, key) combination
        # This is enforced at the DB level to prevent duplicate facts
        {"sqlite_autoincrement": True},
    )


class StudentSkill(Base):
    """
    Tracks individual skill proficiency for each student.
    Updated after assessments, lesson completions, and AI interactions.
    Used for adaptive difficulty and prerequisite recommendations.
    """
    __tablename__ = "student_skills"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_name = Column(String(255), nullable=False, index=True)   # e.g., "python_loops", "sql_joins", "recursion"
    proficiency = Column(Float, default=0.0)                        # 0.0 to 1.0
    assessment_count = Column(Integer, default=0)                   # How many times assessed
    practice_count = Column(Integer, default=0)                     # How many practice attempts
    last_assessed = Column(DateTime, nullable=True)
    last_practiced = Column(DateTime, nullable=True)
    needs_revision = Column(Boolean, default=False)                 # Flagged for spaced repetition
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

    __table_args__ = (
        {"sqlite_autoincrement": True},
    )


class ProceduralMemory(Base):
    """
    Stores useful teaching procedures and explanation strategies
    that have worked well (or poorly) in the past.
    Shared across all students — this is how the system learns
    which approaches are effective for different topics.
    """
    __tablename__ = "procedural_memories"

    id = Column(Integer, primary_key=True, index=True)
    procedure_type = Column(String(100), nullable=False, index=True)  # explanation_strategy, debugging_approach, analogy
    topic = Column(String(255), nullable=True, index=True)
    procedure = Column(Text, nullable=False)
    success_count = Column(Integer, default=0)
    failure_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class AIInteractionLog(Base):
    """
    Structured log of AI interactions for evaluation and learning.
    This replaces blind chat history with actionable metadata.
    Stores what the system did, why, and whether it worked.
    """
    __tablename__ = "ai_interaction_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    interaction_type = Column(String(50), nullable=False, index=True)  # chat, code_review, assessment, explanation
    topic = Column(String(255), nullable=True)
    course_name = Column(String(255), nullable=True)
    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    response_quality = Column(String(20), nullable=True)               # pass, fail, unknown (from evaluator)
    tools_used = Column(JSON, default=list)                            # ["calculator", "code_executor"]
    context_sources = Column(JSON, default=list)                       # ["lesson:42", "memory:7"]
    latency_ms = Column(Integer, nullable=True)                        # Response time in milliseconds
    token_count = Column(Integer, nullable=True)                       # Tokens used
    metadata_json = Column(JSON, default=dict)                         # Flexible extra data
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")


# ─── DIGITAL ERA AI 2.0 — RAG SYSTEM (Phase 3) ───

class ContentEmbedding(Base):
    """
    Stores course content, documentation, and their vector embeddings
    for Semantic Search (RAG). Replaces the file-based FAISS index.
    In SQLite, embedding is stored as JSON. In Postgres, it's VECTOR.
    """
    __tablename__ = "content_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    source_type = Column(String(50), nullable=False, index=True) # lesson, documentation, support
    source_id = Column(Integer, nullable=True)                   # e.g. lesson_id
    chunk_index = Column(Integer, default=0)
    content = Column(Text, nullable=False)
    metadata_json = Column(JSON, default=dict)
    
    # Store the vector embedding as a JSON array to ensure 
    # cross-compatibility between SQLite (dev) and PostgreSQL (prod)
    embedding = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)


# ─── DIGITAL ERA AI 2.0 — TOOL REGISTRY (Phase 5) ───

class ToolInvocationLog(Base):
    """
    Audit log of all tools executed by the AI or the user.
    Ensures accountability for code execution, searches, etc.
    """
    __tablename__ = "tool_invocation_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    tool_name = Column(String(100), nullable=False, index=True)
    input_data = Column(JSON, default=dict)
    output_data = Column(JSON, default=dict)
    is_success = Column(Boolean, default=True)
    error_message = Column(Text, nullable=True)
    latency_ms = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")


# ─── DIGITAL ERA AI 2.0 — EVALUATION SYSTEM (Phase 7) ───

class AIEvaluation(Base):
    """
    Independent evaluations of AI responses.
    Used to track correctness, relevance, and safety metrics over time.
    """
    __tablename__ = "ai_evaluations"

    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("ai_interaction_logs.id", ondelete="CASCADE"), nullable=False, index=True)
    correctness_score = Column(Float, nullable=True)      # 0.0 to 1.0
    relevance_score = Column(Float, nullable=True)        # 0.0 to 1.0
    hallucination_risk = Column(Float, nullable=True)     # 0.0 to 1.0
    code_validity_score = Column(Float, nullable=True)    # 0.0 to 1.0
    safety_score = Column(Float, nullable=True)           # 0.0 to 1.0
    verdict = Column(String(50), nullable=False)          # pass, revise, fail
    evaluation_metadata = Column(JSON, default=dict)      # Full reasoning
    created_at = Column(DateTime, default=datetime.utcnow)

    interaction = relationship("AIInteractionLog")


# ─── DIGITAL ERA AI 2.0 — AUTOMATED LESSON UPDATER (Phase 9) ───

class LessonUpdateProposal(Base):
    """
    Stores AI-generated proposals for rewriting lessons that have low performance.
    Admins can review these proposals in the dashboard.
    """
    __tablename__ = "lesson_update_proposals"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False, index=True)
    reason = Column(Text, nullable=False)                 # Why is this update needed? (e.g. 80% failure rate)
    original_content = Column(Text, nullable=False)
    proposed_content = Column(Text, nullable=False)
    status = Column(String(20), default="pending")        # pending, approved, rejected
    created_at = Column(DateTime, default=datetime.utcnow)

    lesson = relationship("Lesson")
