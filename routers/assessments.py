from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models
from models import calculate_level
from auth import get_current_user
from ai_brain import ask_gemini
import json
from typing import Optional

router = APIRouter(prefix="/assessments", tags=["Assessments"])

class AssessmentGenerateRequest(BaseModel):
    topic: str
    level: str = "Beginner"

class AssessmentSubmitRequest(BaseModel):
    score: int
    max_score: int
    topic: str
    questions_data: Optional[dict] = None  # Store Q&A for review

@router.post("/generate")
def generate_assessment(req: AssessmentGenerateRequest, current_user: models.User = Depends(get_current_user)):
    system_prompt = (
        f"You are an expert assessment generator. Create a 10-question multiple-choice quiz on '{req.topic}' for a {req.level} student.\n"
        "Return the output STRICTLY as a raw JSON array of objects. Do not use Markdown formatting (no ```json). Do not add any conversational text.\n"
        "Each object must have exactly these keys: 'question' (string), 'options' (array of 4 strings), 'correctAnswer' (integer index 0-3), 'explanation' (string explaining why the correct answer is right).\n"
    )
    
    try:
        raw_json_str = ask_gemini("Generate the assessment JSON now.", system_prompt_override=system_prompt)
        # Strip markdown if model disobeys
        raw_json_str = raw_json_str.strip()
        if raw_json_str.startswith("```json"):
            raw_json_str = raw_json_str[7:]
        if raw_json_str.endswith("```"):
            raw_json_str = raw_json_str[:-3]
            
        questions = json.loads(raw_json_str.strip())
        return {"questions": questions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate assessment: {str(e)}")

@router.post("/submit")
def submit_assessment(req: AssessmentSubmitRequest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Calculate a score out of 300
    normalized_score = int((req.score / req.max_score) * 300)
    
    # Give them some XP for completing an assessment
    xp_gained = req.score * 15
    
    current_user.xp += xp_gained
    # Use centralized level calculation for consistency
    current_user.level = calculate_level(current_user.xp)
    
    # Save assessment result to DB for history tracking
    result = models.AssessmentResult(
        user_id=current_user.id,
        topic=req.topic,
        score=req.score,
        max_score=req.max_score,
        skill_score=normalized_score,
        xp_gained=xp_gained,
        questions_data=req.questions_data
    )
    db.add(result)
    db.commit()
    
    return {
        "skill_score": normalized_score,
        "xp_gained": xp_gained,
        "new_level": current_user.level,
        "total_xp": current_user.xp
    }

@router.get("/history")
def get_assessment_history(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Get all past assessment results for the user."""
    results = db.query(models.AssessmentResult).filter(
        models.AssessmentResult.user_id == current_user.id
    ).order_by(models.AssessmentResult.taken_at.desc()).limit(50).all()
    
    return [
        {
            "id": r.id,
            "topic": r.topic,
            "score": r.score,
            "max_score": r.max_score,
            "skill_score": r.skill_score,
            "xp_gained": r.xp_gained,
            "taken_at": r.taken_at.isoformat() if r.taken_at else None
        }
        for r in results
    ]

