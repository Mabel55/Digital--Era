from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Request
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user
from ai_brain import ask_gemini
from limiter import limiter
from datetime import date
import shutil
import os

router = APIRouter(tags=["AI Tutor"])

FREE_DAILY_AI_LIMIT = 3
PRO_DAILY_AI_LIMIT = 30


def _check_ai_limit(db: Session, user: models.User) -> tuple[bool, int, int]:
    """
    Check if user has hit their daily AI message limit.
    Returns: (is_allowed, messages_used, daily_limit)
    """
    # 1. Get or create today's usage for the user
    today = date.today()
    usage = db.query(models.AIUsage).filter(
        models.AIUsage.user_id == user.id,
        models.AIUsage.usage_date == today
    ).first()
    
    if not usage:
        usage = models.AIUsage(user_id=user.id, usage_date=today, message_count=0)
        db.add(usage)
        db.commit()

    # 2. Check subscription status
    sub = db.query(models.Subscription).filter(
        models.Subscription.user_id == user.id
    ).first()
    is_pro = sub and sub.is_pro
    
    # 3. Enforce limits
    if is_pro:
        # Enforce fair usage limit silently (prevent abuse)
        is_allowed = usage.message_count < PRO_DAILY_AI_LIMIT
        # Return -1 for the limit so the frontend doesn't show a limit banner
        return is_allowed, usage.message_count, -1
    else:
        # Enforce free tier limits
        is_allowed = usage.message_count < FREE_DAILY_AI_LIMIT
        return is_allowed, usage.message_count, FREE_DAILY_AI_LIMIT


def _increment_ai_usage(db: Session, user_id: int):
    """Increment today's AI message count for the user."""
    today = date.today()
    usage = db.query(models.AIUsage).filter(
        models.AIUsage.user_id == user_id,
        models.AIUsage.usage_date == today
    ).first()
    
    if usage:
        usage.message_count += 1
    else:
        usage = models.AIUsage(user_id=user_id, usage_date=today, message_count=1)
        db.add(usage)
    db.commit()


@router.get("/ai-usage", response_model=schemas.AIUsageResponse)
def get_ai_usage(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Returns the current user's AI usage for today."""
    is_allowed, used, limit = _check_ai_limit(db, current_user)
    return schemas.AIUsageResponse(
        messages_used=used,
        daily_limit=limit if limit > 0 else 999,
        is_limited=limit > 0
    )


@router.post("/chat")
@limiter.limit("15/minute")
def chat_with_study_buddy(
    request: Request,
    payload: schemas.ChatRequest, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Check AI usage limits for free users
    is_allowed, messages_used, daily_limit = _check_ai_limit(db, current_user)
    if not is_allowed:
        raise HTTPException(
            status_code=429,
            detail=f"You've used all {daily_limit} free AI messages for today. Upgrade to Pro for unlimited access!"
        )

    try:
        # 1. Fetch all past messages between this student and the AI from PostgreSQL
        past_messages = db.query(models.ChatMessage)\
                          .filter(models.ChatMessage.user_id == current_user.id)\
                          .order_by(models.ChatMessage.timestamp.asc())\
                          .all()
        
        # 2. Extract question text
        question_text = payload.question if hasattr(payload, 'question') else payload.message
        
        # 3. Fetch lesson context if lesson_id is provided
        context_chunks = []
        if getattr(payload, 'lesson_id', None):
            lesson = db.query(models.Lesson).filter(models.Lesson.id == payload.lesson_id).first()
            if lesson:
                context_chunks.append(f"CURRENT LESSON CONTEXT:\nTitle: {lesson.title}\nContent: {lesson.content}\nExpected Output: {lesson.expected_output or 'N/A'}")

        # 4. Run your LangChain engine passing the database history AND lesson context
        answer = ask_gemini(
            question=question_text, 
            context_chunks=context_chunks, 
            chat_history=past_messages
        )
        
        # 5. Save the student's input question to PostgreSQL
        student_msg = models.ChatMessage(user_id=current_user.id, role="user", content=question_text)
        db.add(student_msg)

        # 6. Save Gemini's answer to PostgreSQL right next to it
        ai_msg = models.ChatMessage(user_id=current_user.id, role="model", content=answer)
        db.add(ai_msg)
        
        # 7. Increment AI usage counter
        _increment_ai_usage(db, current_user.id)
        
        db.commit()
        
        # Calculate remaining messages
        remaining = (daily_limit - messages_used - 1) if daily_limit > 0 else -1
        
        return {
            "answer": answer,
            "sources_used": [],
            "remaining_messages": remaining,
            "daily_limit": daily_limit
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Brain Error: {str(e)}")

@router.post("/ask-ai/")
@limiter.limit("10/minute")
def ask_ai_tutor(request: Request, chat: schemas.ChatRequest): 
    try:
        system_prompt = f"""You are Mabel, a senior software engineering instructor at Mabel Academy - a coding school for Nigerian developers.
        You are teaching a {chat.level} student who wants to master {chat.track}.
        Current course: {chat.course}.
        Be encouraging, concise, and use Nigerian examples when helpful (Lagos, Naira, jollof rice, etc).
        Never give full solutions unless grading - give hints, ask questions, guide thinking.
        Format code with proper markdown code blocks."""

        ai_reply = ask_gemini(chat.message, context_chunks=[], system_prompt_override=system_prompt)
        return {"reply": ai_reply}

    except Exception as e:
        return {"reply": f"System Error: Could not connect to the model. Details: {str(e)}"}


