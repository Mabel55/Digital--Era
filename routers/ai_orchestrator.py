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

from database import get_db
import models
from auth import get_current_user
from limiter import limiter
from fastapi import Request

from services.ai_orchestrator import AIOrchestrator, OrchestratorRequest
from services.evaluator_service import EvaluatorService

router = APIRouter(prefix="/api/v2/ai", tags=["AI 2.0 — Orchestrator"])


class ChatV2Request(BaseModel):
    message: str
    course: str = "General"
    lesson_id: Optional[int] = None
    persona: str = "study_buddy"  # 'study_buddy', 'code_reviewer', 'lecturer'


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
    try:
        # Build the orchestrator request
        orch_req = OrchestratorRequest(
            user_id=current_user.id,
            message=payload.message,
            course_name=payload.course,
            lesson_id=payload.lesson_id,
            level=current_user.level or "Beginner",
            track=current_user.track or "General",
            persona=payload.persona
        )
        
        # Process through the orchestrator
        response, interaction_log = AIOrchestrator.process_chat(db, orch_req)
        
        # Dispatch background evaluation (Phase 7)
        if interaction_log:
            background_tasks.add_task(EvaluatorService.evaluate_interaction, db, interaction_log)
        
        return {
            "answer": response.answer,
            "sources": response.sources,
            "metadata": {
                "intent_detected": response.intent,
                "latency_ms": response.latency_ms,
                "thought_process": response.thought_process
            }
        }
        
    except Exception as e:
        print(f"[Router Error] Orchestrator failed: {e}")
        raise HTTPException(status_code=500, detail="The AI brain encountered an error processing your request.")
