"""
Memory Router — Digital Era AI 2.0 (Phase 2)

API endpoints for the memory and student model system.
These are v2 endpoints that run alongside existing endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional
from database import get_db
from auth import get_current_user
import models
from services.memory_service import MemoryService, FactType, MemoryType
from services.student_model_service import StudentModelService

router = APIRouter(prefix="/api/v2/memory", tags=["AI 2.0 — Memory & Student Model"])


# ─── REQUEST SCHEMAS ───

class RecordEpisodeRequest(BaseModel):
    memory_type: str = Field(..., description="Type: struggle, breakthrough, misconception, preference, error_pattern")
    topic: Optional[str] = None
    summary: str
    importance: float = Field(default=0.5, ge=0.0, le=1.0)
    metadata: Optional[dict] = None


class SetFactRequest(BaseModel):
    fact_type: str = Field(..., description="Type: skill, strength, weakness, goal, preference, background")
    key: str
    value: str
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)


class UpdateSkillRequest(BaseModel):
    skill_name: str
    proficiency_delta: float = Field(default=0.0, ge=0.0, le=1.0)
    assessed: bool = False
    practiced: bool = False


# ─── RESPONSE SCHEMAS ───

class EpisodeResponse(BaseModel):
    id: int
    memory_type: str
    topic: Optional[str]
    summary: str
    importance: float
    created_at: str

    class Config:
        from_attributes = True


class FactResponse(BaseModel):
    id: int
    fact_type: str
    key: str
    value: str
    confidence: float

    class Config:
        from_attributes = True


class SkillResponse(BaseModel):
    id: int
    skill_name: str
    proficiency: float
    assessment_count: int
    practice_count: int
    needs_revision: bool

    class Config:
        from_attributes = True


# ─── STUDENT CONTEXT (main endpoint for AI) ───

@router.get("/context")
def get_student_context(
    topic: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Get the full student context that the AI uses to personalize responses.
    This is the primary endpoint that shows what the system knows about a student.
    """
    context = MemoryService.get_student_context(db, current_user.id, topic=topic)
    return {
        "user_id": current_user.id,
        "recent_episodes": context.recent_episodes,
        "known_facts": context.known_facts,
        "skills": context.skills,
        "struggle_topics": context.struggle_topics,
        "strength_topics": context.strength_topics,
        "prompt_context": context.to_prompt_context(),
    }


# ─── LEARNING SUMMARY ───

@router.get("/summary")
def get_learning_summary(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Get a comprehensive learning summary including difficulty level,
    strengths, weaknesses, and topics needing revision.
    """
    return StudentModelService.get_learning_summary(db, current_user.id)


# ─── EPISODIC MEMORY ───

@router.get("/episodes")
def list_episodes(
    topic: Optional[str] = None,
    memory_type: Optional[str] = None,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """List the student's episodic memories (important learning events)."""
    episodes = MemoryService.get_recent_episodes(
        db, current_user.id, limit=min(limit, 50), topic=topic, memory_type=memory_type
    )
    return [
        {
            "id": ep.id,
            "memory_type": ep.memory_type,
            "topic": ep.topic,
            "summary": ep.summary,
            "importance": ep.importance,
            "created_at": ep.created_at.isoformat() if ep.created_at else None,
        }
        for ep in episodes
    ]


@router.post("/episodes")
def record_episode(
    req: RecordEpisodeRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Manually record an episodic memory (usually called by AI system, not users directly)."""
    valid_types = [MemoryType.STRUGGLE, MemoryType.BREAKTHROUGH, MemoryType.MISCONCEPTION,
                   MemoryType.PREFERENCE, MemoryType.ERROR_PATTERN, MemoryType.REPEATED_QUESTION]
    if req.memory_type not in valid_types:
        raise HTTPException(status_code=400, detail=f"Invalid memory_type. Must be one of: {valid_types}")

    episode = MemoryService.record_episode(
        db=db,
        user_id=current_user.id,
        memory_type=req.memory_type,
        topic=req.topic,
        summary=req.summary,
        importance=req.importance,
        metadata=req.metadata,
    )
    return {"id": episode.id, "message": "Episode recorded"}


# ─── SEMANTIC MEMORY (FACTS) ───

@router.get("/facts")
def list_facts(
    fact_type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """List known facts about the student."""
    facts = MemoryService.get_facts(db, current_user.id, fact_type=fact_type)
    return [
        {
            "id": f.id,
            "fact_type": f.fact_type,
            "key": f.key,
            "value": f.value,
            "confidence": f.confidence,
        }
        for f in facts
    ]


@router.post("/facts")
def set_fact(
    req: SetFactRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Store or update a fact about the student (upsert by fact_type + key)."""
    valid_types = [FactType.SKILL, FactType.STRENGTH, FactType.WEAKNESS,
                   FactType.GOAL, FactType.PREFERENCE, FactType.BACKGROUND]
    if req.fact_type not in valid_types:
        raise HTTPException(status_code=400, detail=f"Invalid fact_type. Must be one of: {valid_types}")

    fact = MemoryService.set_fact(
        db=db,
        user_id=current_user.id,
        fact_type=req.fact_type,
        key=req.key,
        value=req.value,
        confidence=req.confidence,
    )
    return {"id": fact.id, "message": "Fact stored"}


# ─── SKILLS ───

@router.get("/skills")
def list_skills(
    revision_only: bool = False,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """List tracked skills with proficiency levels."""
    skills = MemoryService.get_skills(db, current_user.id, needs_revision_only=revision_only)
    return [
        {
            "id": s.id,
            "skill_name": s.skill_name,
            "proficiency": round(s.proficiency, 2),
            "assessment_count": s.assessment_count,
            "practice_count": s.practice_count,
            "needs_revision": s.needs_revision,
            "last_assessed": s.last_assessed.isoformat() if s.last_assessed else None,
            "last_practiced": s.last_practiced.isoformat() if s.last_practiced else None,
        }
        for s in skills
    ]


@router.put("/skills")
def update_skill(
    req: UpdateSkillRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Update a student's skill proficiency."""
    skill = MemoryService.update_skill(
        db=db,
        user_id=current_user.id,
        skill_name=req.skill_name,
        proficiency_delta=req.proficiency_delta,
        assessed=req.assessed,
        practiced=req.practiced,
    )
    return {
        "skill_name": skill.skill_name,
        "proficiency": round(skill.proficiency, 2),
        "needs_revision": skill.needs_revision,
    }


# ─── REVISION RECOMMENDATIONS ───

@router.get("/revision")
def get_revision_topics(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Get topics that the student should revise, ordered by urgency."""
    return StudentModelService.get_revision_topics(db, current_user.id)


# ─── DIFFICULTY LEVEL ───

@router.get("/difficulty")
def get_difficulty_level(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Get the recommended difficulty level for this student."""
    level = StudentModelService.get_difficulty_level(db, current_user.id)
    return {"difficulty_level": level}
