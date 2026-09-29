"""
Evaluator Router — Digital Era AI 2.0 (Phase 7)

Provides admin endpoints to view AI evaluation metrics and
trigger manual evaluations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any

from database import get_db
import models
from auth import get_current_user
from services.evaluator_service import EvaluatorService

router = APIRouter(prefix="/api/v2/admin/evaluations", tags=["AI 2.0 — Evaluation System"])


def require_admin(current_user: models.User = Depends(get_current_user)):
    # Assuming role == 'admin' or similar, simplified for now
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user


@router.get("/metrics")
def get_evaluation_metrics(
    limit: int = 100,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin)
):
    """
    Get aggregate performance metrics of the AI across the last N interactions.
    """
    return EvaluatorService.get_aggregate_metrics(db, limit)


@router.post("/evaluate-interaction/{interaction_id}")
def force_evaluate_interaction(
    interaction_id: int,
    db: Session = Depends(get_db),
    admin: models.User = Depends(require_admin)
):
    """
    Manually force an evaluation on a specific interaction log.
    """
    log = db.query(models.AIInteractionLog).filter(models.AIInteractionLog.id == interaction_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Interaction not found")
        
    evaluation = EvaluatorService.evaluate_interaction(db, log)
    
    return {
        "success": True,
        "verdict": evaluation.verdict,
        "scores": {
            "correctness": evaluation.correctness_score,
            "relevance": evaluation.relevance_score,
            "safety": evaluation.safety_score
        }
    }
