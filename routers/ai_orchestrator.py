"""
AI Orchestrator Router — Digital Era AI 2.0 (Phase 4)

Provides the /api/v2/ai/chat endpoint.
This runs in parallel with the legacy /chat endpoint to ensure
existing clients don't break during the transition.
"""

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional
import traceback

from database import get_db, SessionLocal
import models
from auth import get_current_user
from limiter import limiter
from fastapi import Request

from services.ai_orchestrator import AIOrchestrator, OrchestratorRequest
from services.evaluator_service import EvaluatorService

router = APIRouter(prefix="/api/v2/ai", tags=["AI 2.0 — Orchestrator"])

FREE_DAILY_AI_LIMIT = 3
PRO_DAILY_AI_LIMIT = 30


class ChatV2Request(BaseModel):
    message: str
    course: str = "General"
    lesson_id: Optional[int] = None
    persona: str = "study_buddy"  # 'study_buddy', 'code_reviewer', 'lecturer'


def _check_ai_limit_v2(db: Session, user: models.User) -> tuple[bool, int, int]:
    """
    Check if user has hit their daily AI message limit.
    Returns: (is_allowed, messages_used, daily_limit)
    """
    from datetime import date
    today = date.today()
    usage = db.query(models.AIUsage).filter(
        models.AIUsage.user_id == user.id,
        models.AIUsage.usage_date == today
    ).first()

    if not usage:
        usage = models.AIUsage(user_id=user.id, usage_date=today, message_count=0)
        db.add(usage)
        db.commit()

    sub = db.query(models.Subscription).filter(
        models.Subscription.user_id == user.id
    ).first()
    is_pro = sub and sub.is_pro

    if is_pro:
        is_allowed = usage.message_count < PRO_DAILY_AI_LIMIT
        return is_allowed, usage.message_count, -1
    else:
        is_allowed = usage.message_count < FREE_DAILY_AI_LIMIT
        return is_allowed, usage.message_count, FREE_DAILY_AI_LIMIT


def _increment_ai_usage_v2(db: Session, user_id: int):
    """Increment today's AI message count for the user."""
    from datetime import date
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


def _run_background_evaluation(interaction_log_id: int):
    """
    Runs the evaluator in the background with its OWN database session.
    This avoids the stale/closed session bug from using the request-scoped session.
    """
    db = SessionLocal()
    try:
        interaction_log = db.query(models.AIInteractionLog).filter(
            models.AIInteractionLog.id == interaction_log_id
        ).first()
        if interaction_log:
            EvaluatorService.evaluate_interaction(db, interaction_log)
    except Exception as e:
        print(f"[Background Evaluator] Error: {e}")
    finally:
        db.close()


@router.post("/chat")
@limiter.limit("50/day")
def chat_orchestrated(
    request: Request,
    payload: ChatV2Request,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Phase 4: Orchestrated AI Chat Endpoint.
    Uses the new pipeline: Intent -> Memory -> RAG -> Generation -> Learning.
    Phase 7: Evaluates the response in the background.
    """
    # Check AI usage limits (was missing on V2 endpoint)
    is_allowed, messages_used, daily_limit = _check_ai_limit_v2(db, current_user)
    if not is_allowed:
        raise HTTPException(
            status_code=429,
            detail=f"You've used all {daily_limit} free AI messages for today. Upgrade to Pro for unlimited access!"
        )

    try:
        # Build the orchestrator request
        orch_req = OrchestratorRequest(
            user_id=current_user.id,
            message=payload.message,
            course_name=payload.course,
            lesson_id=payload.lesson_id,
            level=current_user.level or "Beginner",
            track=getattr(current_user, 'track', None) or "General",
            persona=payload.persona
        )
        
        # Process through the orchestrator
        response, interaction_log = AIOrchestrator.process_chat(db, orch_req)
        
        # Dispatch background evaluation (Phase 7)
        # Uses a dedicated session via _run_background_evaluation to avoid stale session bugs
        if interaction_log:
            background_tasks.add_task(_run_background_evaluation, interaction_log.id)
        
        # Increment AI usage counter
        _increment_ai_usage_v2(db, current_user.id)
        
        # Calculate remaining messages
        remaining = (daily_limit - messages_used - 1) if daily_limit > 0 else -1
        
        return {
            "answer": response.answer,
            "sources": response.sources,
            "remaining_messages": remaining,
            "daily_limit": daily_limit,
            "metadata": {
                "intent_detected": response.intent,
                "latency_ms": response.latency_ms,
                "thought_process": response.thought_process
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        # Log the FULL stack trace so we can actually debug production issues
        error_detail = traceback.format_exc()
        print(f"[Router Error] Orchestrator failed for user {current_user.id}:")
        print(error_detail)
        raise HTTPException(
            status_code=500, 
            detail=f"The AI brain encountered an error processing your request. ({type(e).__name__}: {str(e)[:200]})"
        )
