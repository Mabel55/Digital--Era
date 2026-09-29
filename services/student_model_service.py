"""
Student Model Service — Digital Era AI 2.0 (Phase 2)

Builds and maintains a comprehensive model of each student's
learning state. This is the "understanding" layer that sits
on top of raw memory data.

The student model answers questions like:
- What does this student know?
- What are they struggling with?
- What difficulty level should we use?
- What topics need revision?
- What's the best way to explain something to this student?
"""

from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
import models
from services.memory_service import MemoryService, FactType, StudentContext


class StudentModelService:
    """
    Higher-level service that interprets raw memory data
    into actionable student understanding.
    """

    @staticmethod
    def get_difficulty_level(db: Session, user_id: int) -> str:
        """
        Calculate the appropriate difficulty level for a student
        based on their skill proficiencies and assessment history.

        Returns: "beginner", "intermediate", or "advanced"
        """
        skills = MemoryService.get_skills(db, user_id)

        if not skills:
            # No data yet — default to beginner
            return "beginner"

        # Only consider skills that have been assessed at least once
        assessed_skills = [s for s in skills if s.assessment_count > 0]

        if not assessed_skills:
            return "beginner"

        avg_proficiency = sum(s.proficiency for s in assessed_skills) / len(assessed_skills)

        if avg_proficiency >= 0.75:
            return "advanced"
        elif avg_proficiency >= 0.45:
            return "intermediate"
        else:
            return "beginner"

    @staticmethod
    def get_revision_topics(db: Session, user_id: int, limit: int = 5) -> list[dict]:
        """
        Get topics that need revision, ordered by urgency.

        Revision is needed when:
        1. Skill proficiency is low AND the skill has been assessed
        2. The student has struggled with the topic recently
        3. Enough time has passed since last practice (spaced repetition)
        """
        # Skills flagged for revision
        revision_skills = MemoryService.get_skills(db, user_id, needs_revision_only=True)

        topics = []
        for skill in revision_skills[:limit]:
            days_since_practice = None
            if skill.last_practiced:
                days_since_practice = (datetime.utcnow() - skill.last_practiced).days

            topics.append({
                "topic": skill.skill_name,
                "proficiency": skill.proficiency,
                "days_since_practice": days_since_practice,
                "assessment_count": skill.assessment_count,
                "urgency": _calculate_revision_urgency(skill),
            })

        # Sort by urgency (highest first)
        topics.sort(key=lambda t: t["urgency"], reverse=True)
        return topics

    @staticmethod
    def get_learning_summary(db: Session, user_id: int) -> dict:
        """
        Generate a comprehensive learning summary for the student.
        Used by the profile page and admin dashboard.
        """
        skills = MemoryService.get_skills(db, user_id)
        facts = MemoryService.get_facts(db, user_id)
        strengths = MemoryService.get_strengths(db, user_id)
        weaknesses = MemoryService.get_weaknesses(db, user_id)
        struggles = MemoryService.get_struggle_topics(db, user_id)
        difficulty = StudentModelService.get_difficulty_level(db, user_id)
        revision_topics = StudentModelService.get_revision_topics(db, user_id)

        # Count recent interactions
        week_ago = datetime.utcnow() - timedelta(days=7)
        recent_interactions = (
            db.query(func.count(models.AIInteractionLog.id))
            .filter(
                models.AIInteractionLog.user_id == user_id,
                models.AIInteractionLog.created_at >= week_ago,
            )
            .scalar() or 0
        )

        return {
            "difficulty_level": difficulty,
            "total_skills_tracked": len(skills),
            "strengths": strengths,
            "weaknesses": weaknesses,
            "struggle_topics": struggles,
            "revision_needed": [t["topic"] for t in revision_topics],
            "ai_interactions_this_week": recent_interactions,
            "known_facts_count": len(facts),
            "goals": [
                f.value for f in facts if f.fact_type == FactType.GOAL
            ],
        }

    @staticmethod
    def update_after_chat(
        db: Session,
        user_id: int,
        topic: Optional[str] = None,
        course_name: Optional[str] = None,
        user_message: str = "",
        ai_response: str = "",
    ):
        """
        Update the student model after a chat interaction.
        This is the hook that connects the existing AI tutor
        to the new memory system.
        """
        from services.memory_service import MemoryAnalyzer

        # Analyze the interaction and record relevant memories
        MemoryAnalyzer.analyze_chat_interaction(
            db=db,
            user_id=user_id,
            user_message=user_message,
            ai_response=ai_response,
            topic=topic,
            course_name=course_name,
        )

    @staticmethod
    def update_after_assessment(
        db: Session,
        user_id: int,
        topic: str,
        score: int,
        max_score: int,
    ):
        """
        Update the student model after an assessment.
        """
        from services.memory_service import MemoryAnalyzer

        MemoryAnalyzer.record_assessment_result(
            db=db,
            user_id=user_id,
            topic=topic,
            score=score,
            max_score=max_score,
        )

    @staticmethod
    def update_after_lesson_completion(
        db: Session,
        user_id: int,
        course_name: str,
        lesson_topic: Optional[str] = None,
    ):
        """
        Update the student model after a lesson completion.
        """
        from services.memory_service import MemoryAnalyzer

        MemoryAnalyzer.record_lesson_completion(
            db=db,
            user_id=user_id,
            course_name=course_name,
            lesson_topic=lesson_topic,
        )

    @staticmethod
    def get_context_for_ai(
        db: Session,
        user_id: int,
        topic: Optional[str] = None,
    ) -> str:
        """
        Build a context string for the AI system prompt.
        This is the primary interface between the student model
        and the AI tutor. Returns a formatted string that can
        be injected into the system prompt.
        """
        context = MemoryService.get_student_context(db, user_id, topic=topic)
        return context.to_prompt_context()


# ─── HELPERS ───

def _calculate_revision_urgency(skill: models.StudentSkill) -> float:
    """
    Calculate how urgently a skill needs revision.
    Higher = more urgent.

    Factors:
    - Lower proficiency = more urgent
    - More time since last practice = more urgent
    - More assessment failures = more urgent
    """
    urgency = 0.0

    # Proficiency factor (inverse: lower proficiency = higher urgency)
    urgency += (1.0 - skill.proficiency) * 0.5

    # Time factor (more days since practice = higher urgency)
    if skill.last_practiced:
        days_since = (datetime.utcnow() - skill.last_practiced).days
        time_factor = min(days_since / 30.0, 1.0)  # Caps at 30 days
        urgency += time_factor * 0.3
    else:
        urgency += 0.3  # Never practiced

    # Assessment count factor (assessed but still low = more urgent)
    if skill.assessment_count > 0:
        urgency += 0.2

    return min(urgency, 1.0)
