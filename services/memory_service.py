"""
Memory Service — Digital Era AI 2.0 (Phase 2)

Manages all forms of AI memory:
- Short-term: Current conversation context (handled in-request, not persisted here)
- Episodic: Important past interactions and events
- Semantic: Stable facts about the learner
- Procedural: Teaching strategies that worked/failed

This service is the single interface for storing and retrieving
memories. The AI Orchestrator (Phase 4) will use this to build
student-aware context for every response.
"""

from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_, func
import models


# ─── MEMORY TYPES (constants for consistency) ───

class MemoryType:
    """Episodic memory type constants."""
    STRUGGLE = "struggle"
    BREAKTHROUGH = "breakthrough"
    MISCONCEPTION = "misconception"
    PREFERENCE = "preference"
    ERROR_PATTERN = "error_pattern"
    REPEATED_QUESTION = "repeated_question"


class FactType:
    """Semantic memory fact type constants."""
    SKILL = "skill"
    STRENGTH = "strength"
    WEAKNESS = "weakness"
    GOAL = "goal"
    PREFERENCE = "preference"
    BACKGROUND = "background"


# ─── DATA CLASSES FOR SERVICE RETURNS ───

class StudentContext:
    """Aggregated context about a student for AI consumption."""

    def __init__(
        self,
        user_id: int,
        recent_episodes: list[dict],
        known_facts: list[dict],
        skills: list[dict],
        struggle_topics: list[str],
        strength_topics: list[str],
    ):
        self.user_id = user_id
        self.recent_episodes = recent_episodes
        self.known_facts = known_facts
        self.skills = skills
        self.struggle_topics = struggle_topics
        self.strength_topics = strength_topics

    def to_prompt_context(self) -> str:
        """
        Converts student context into a concise text block
        suitable for injection into an AI system prompt.
        Only includes information that would actually help
        the AI give a better response.
        """
        parts = []

        if self.struggle_topics:
            parts.append(
                f"Topics this student struggles with: {', '.join(self.struggle_topics[:5])}"
            )

        if self.strength_topics:
            parts.append(
                f"Topics this student is strong in: {', '.join(self.strength_topics[:5])}"
            )

        # Include recent relevant episodes (max 3 to keep context small)
        if self.recent_episodes:
            episode_lines = []
            for ep in self.recent_episodes[:3]:
                episode_lines.append(f"- [{ep['type']}] {ep['summary']}")
            parts.append("Recent learning events:\n" + "\n".join(episode_lines))

        # Include key facts (max 5)
        relevant_facts = [
            f for f in self.known_facts
            if f["fact_type"] in (FactType.WEAKNESS, FactType.PREFERENCE, FactType.GOAL)
        ]
        if relevant_facts:
            fact_lines = [f"- {f['key']}: {f['value']}" for f in relevant_facts[:5]]
            parts.append("Known about this student:\n" + "\n".join(fact_lines))

        if not parts:
            return ""

        return "\n\n--- STUDENT CONTEXT (from memory) ---\n" + "\n".join(parts) + "\n---\n"


# ─── MAIN MEMORY SERVICE ───

class MemoryService:
    """
    Service for managing all forms of AI memory.
    Thread-safe: each method receives its own db session.
    """

    # ─── EPISODIC MEMORY ───

    @staticmethod
    def record_episode(
        db: Session,
        user_id: int,
        memory_type: str,
        summary: str,
        topic: Optional[str] = None,
        importance: float = 0.5,
        metadata: Optional[dict] = None,
    ) -> models.EpisodicMemory:
        """
        Record a notable event in the student's learning history.

        Use sparingly — not every interaction is worth recording.
        Good candidates:
        - Student struggled with a concept multiple times
        - Student had an "aha" moment
        - Student showed a persistent misconception
        - Student expressed a preference
        """
        episode = models.EpisodicMemory(
            user_id=user_id,
            memory_type=memory_type,
            topic=topic,
            summary=summary,
            importance=min(max(importance, 0.0), 1.0),  # Clamp to [0, 1]
            metadata_json=metadata or {},
        )
        db.add(episode)
        db.commit()
        db.refresh(episode)
        return episode

    @staticmethod
    def get_recent_episodes(
        db: Session,
        user_id: int,
        limit: int = 10,
        topic: Optional[str] = None,
        memory_type: Optional[str] = None,
    ) -> list[models.EpisodicMemory]:
        """Retrieve recent episodic memories, optionally filtered."""
        query = db.query(models.EpisodicMemory).filter(
            models.EpisodicMemory.user_id == user_id
        )
        if topic:
            query = query.filter(models.EpisodicMemory.topic == topic)
        if memory_type:
            query = query.filter(models.EpisodicMemory.memory_type == memory_type)

        return query.order_by(
            desc(models.EpisodicMemory.importance),
            desc(models.EpisodicMemory.created_at),
        ).limit(limit).all()

    @staticmethod
    def get_struggle_topics(db: Session, user_id: int, limit: int = 5) -> list[str]:
        """Get topics where the student has struggled most."""
        results = (
            db.query(models.EpisodicMemory.topic)
            .filter(
                models.EpisodicMemory.user_id == user_id,
                models.EpisodicMemory.memory_type == MemoryType.STRUGGLE,
                models.EpisodicMemory.topic.isnot(None),
            )
            .group_by(models.EpisodicMemory.topic)
            .order_by(desc(func.count(models.EpisodicMemory.id)))
            .limit(limit)
            .all()
        )
        return [r[0] for r in results]

    # ─── SEMANTIC MEMORY ───

    @staticmethod
    def set_fact(
        db: Session,
        user_id: int,
        fact_type: str,
        key: str,
        value: str,
        confidence: float = 0.5,
    ) -> models.SemanticMemory:
        """
        Store or update a stable fact about a student.
        Uses upsert logic: if (user_id, fact_type, key) exists, update it.
        """
        existing = db.query(models.SemanticMemory).filter(
            models.SemanticMemory.user_id == user_id,
            models.SemanticMemory.fact_type == fact_type,
            models.SemanticMemory.key == key,
        ).first()

        if existing:
            existing.value = value
            existing.confidence = min(max(confidence, 0.0), 1.0)
            existing.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(existing)
            return existing
        else:
            fact = models.SemanticMemory(
                user_id=user_id,
                fact_type=fact_type,
                key=key,
                value=value,
                confidence=min(max(confidence, 0.0), 1.0),
            )
            db.add(fact)
            db.commit()
            db.refresh(fact)
            return fact

    @staticmethod
    def get_facts(
        db: Session,
        user_id: int,
        fact_type: Optional[str] = None,
    ) -> list[models.SemanticMemory]:
        """Get all known facts about a student, optionally filtered by type."""
        query = db.query(models.SemanticMemory).filter(
            models.SemanticMemory.user_id == user_id
        )
        if fact_type:
            query = query.filter(models.SemanticMemory.fact_type == fact_type)
        return query.order_by(desc(models.SemanticMemory.confidence)).all()

    @staticmethod
    def get_fact(
        db: Session, user_id: int, fact_type: str, key: str
    ) -> Optional[models.SemanticMemory]:
        """Get a specific fact about a student."""
        return db.query(models.SemanticMemory).filter(
            models.SemanticMemory.user_id == user_id,
            models.SemanticMemory.fact_type == fact_type,
            models.SemanticMemory.key == key,
        ).first()

    # ─── STUDENT SKILLS ───

    @staticmethod
    def update_skill(
        db: Session,
        user_id: int,
        skill_name: str,
        proficiency_delta: float = 0.0,
        assessed: bool = False,
        practiced: bool = False,
    ) -> models.StudentSkill:
        """
        Update a student's skill proficiency.
        Uses exponential moving average for smooth progression.
        """
        skill_name_lower = skill_name.lower().strip()

        skill = db.query(models.StudentSkill).filter(
            models.StudentSkill.user_id == user_id,
            models.StudentSkill.skill_name == skill_name_lower,
        ).first()

        now = datetime.utcnow()

        if not skill:
            skill = models.StudentSkill(
                user_id=user_id,
                skill_name=skill_name_lower,
                proficiency=max(0.0, min(1.0, proficiency_delta)),
            )
            db.add(skill)
        else:
            # Exponential moving average: new = old * 0.7 + delta * 0.3
            # This gives recent performance more weight but doesn't
            # wildly swing from a single bad attempt.
            new_prof = skill.proficiency * 0.7 + proficiency_delta * 0.3
            skill.proficiency = max(0.0, min(1.0, new_prof))

        if assessed:
            skill.assessment_count += 1
            skill.last_assessed = now

        if practiced:
            skill.practice_count += 1
            skill.last_practiced = now

        # Flag for revision if proficiency drops below threshold
        skill.needs_revision = skill.proficiency < 0.4

        db.commit()
        db.refresh(skill)
        return skill

    @staticmethod
    def get_skills(
        db: Session,
        user_id: int,
        needs_revision_only: bool = False,
    ) -> list[models.StudentSkill]:
        """Get all tracked skills for a student."""
        query = db.query(models.StudentSkill).filter(
            models.StudentSkill.user_id == user_id
        )
        if needs_revision_only:
            query = query.filter(models.StudentSkill.needs_revision == True)
        return query.order_by(desc(models.StudentSkill.proficiency)).all()

    @staticmethod
    def get_skill(
        db: Session, user_id: int, skill_name: str
    ) -> Optional[models.StudentSkill]:
        """Get a specific skill for a student."""
        return db.query(models.StudentSkill).filter(
            models.StudentSkill.user_id == user_id,
            models.StudentSkill.skill_name == skill_name.lower().strip(),
        ).first()

    @staticmethod
    def get_strengths(db: Session, user_id: int, limit: int = 5) -> list[str]:
        """Get the student's top skills (proficiency > 0.7)."""
        results = (
            db.query(models.StudentSkill.skill_name)
            .filter(
                models.StudentSkill.user_id == user_id,
                models.StudentSkill.proficiency >= 0.7,
            )
            .order_by(desc(models.StudentSkill.proficiency))
            .limit(limit)
            .all()
        )
        return [r[0] for r in results]

    @staticmethod
    def get_weaknesses(db: Session, user_id: int, limit: int = 5) -> list[str]:
        """Get skills where the student is weakest (proficiency < 0.4, assessed at least once)."""
        results = (
            db.query(models.StudentSkill.skill_name)
            .filter(
                models.StudentSkill.user_id == user_id,
                models.StudentSkill.proficiency < 0.4,
                models.StudentSkill.assessment_count > 0,
            )
            .order_by(models.StudentSkill.proficiency.asc())
            .limit(limit)
            .all()
        )
        return [r[0] for r in results]

    # ─── INTERACTION LOGGING ───

    @staticmethod
    def log_interaction(
        db: Session,
        user_id: int,
        interaction_type: str,
        user_message: str,
        ai_response: str,
        topic: Optional[str] = None,
        course_name: Optional[str] = None,
        latency_ms: Optional[int] = None,
        tools_used: Optional[list] = None,
        context_sources: Optional[list] = None,
        metadata: Optional[dict] = None,
    ) -> models.AIInteractionLog:
        """
        Log a structured AI interaction for analysis and evaluation.
        Called after every AI response.
        """
        log = models.AIInteractionLog(
            user_id=user_id,
            interaction_type=interaction_type,
            topic=topic,
            course_name=course_name,
            user_message=user_message[:2000],   # Truncate very long messages
            ai_response=ai_response[:5000],     # Truncate very long responses
            tools_used=tools_used or [],
            context_sources=context_sources or [],
            latency_ms=latency_ms,
            metadata_json=metadata or {},
        )
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    # ─── COMPOSITE: FULL STUDENT CONTEXT ───

    @staticmethod
    def get_student_context(
        db: Session,
        user_id: int,
        topic: Optional[str] = None,
    ) -> StudentContext:
        """
        Build a complete student context for AI consumption.
        This is the main method the AI Orchestrator will call.
        """
        # Recent episodes (filtered by topic if provided)
        episodes = MemoryService.get_recent_episodes(
            db, user_id, limit=5, topic=topic
        )
        recent_episodes = [
            {
                "type": ep.memory_type,
                "topic": ep.topic,
                "summary": ep.summary,
                "importance": ep.importance,
                "created_at": ep.created_at.isoformat() if ep.created_at else None,
            }
            for ep in episodes
        ]

        # Known facts
        facts = MemoryService.get_facts(db, user_id)
        known_facts = [
            {
                "fact_type": f.fact_type,
                "key": f.key,
                "value": f.value,
                "confidence": f.confidence,
            }
            for f in facts
        ]

        # Skills
        all_skills = MemoryService.get_skills(db, user_id)
        skills = [
            {
                "name": s.skill_name,
                "proficiency": s.proficiency,
                "needs_revision": s.needs_revision,
                "assessment_count": s.assessment_count,
            }
            for s in all_skills
        ]

        # Struggle and strength topics
        struggle_topics = MemoryService.get_struggle_topics(db, user_id)
        strength_topics = MemoryService.get_strengths(db, user_id)

        return StudentContext(
            user_id=user_id,
            recent_episodes=recent_episodes,
            known_facts=known_facts,
            skills=skills,
            struggle_topics=struggle_topics,
            strength_topics=strength_topics,
        )


# ─── MEMORY ANALYSIS HELPERS ───

class MemoryAnalyzer:
    """
    Analyzes AI interactions to automatically create episodic memories.
    This is the "learning from interaction" part — the system
    watches what happens and records important events.
    """

    @staticmethod
    def analyze_chat_interaction(
        db: Session,
        user_id: int,
        user_message: str,
        ai_response: str,
        topic: Optional[str] = None,
        course_name: Optional[str] = None,
    ):
        """
        Analyze a chat interaction and record relevant memories.
        Called after each AI tutor response.

        Currently uses simple heuristics. Phase 4 (Orchestrator) will
        use the AI itself to classify interactions more intelligently.
        """
        msg_lower = user_message.lower()

        # Detect struggle indicators
        struggle_keywords = [
            "i don't understand", "confused", "doesn't work",
            "error", "bug", "wrong", "help me", "stuck",
            "what does this mean", "why doesn't", "can't figure",
            "i'm lost", "makes no sense", "keep getting",
        ]
        is_struggle = any(kw in msg_lower for kw in struggle_keywords)

        if is_struggle and topic:
            # Check if this is a repeated struggle on the same topic
            existing_struggles = (
                db.query(models.EpisodicMemory)
                .filter(
                    models.EpisodicMemory.user_id == user_id,
                    models.EpisodicMemory.memory_type == MemoryType.STRUGGLE,
                    models.EpisodicMemory.topic == topic,
                )
                .count()
            )

            importance = min(0.5 + (existing_struggles * 0.1), 1.0)

            MemoryService.record_episode(
                db=db,
                user_id=user_id,
                memory_type=MemoryType.STRUGGLE,
                topic=topic,
                summary=f"Student struggled with {topic}: '{user_message[:100]}'",
                importance=importance,
                metadata={
                    "course": course_name,
                    "struggle_count": existing_struggles + 1,
                    "user_message_preview": user_message[:200],
                },
            )

            # If struggling repeatedly (3+), also update the skill
            if existing_struggles >= 2:
                MemoryService.update_skill(
                    db=db,
                    user_id=user_id,
                    skill_name=topic,
                    proficiency_delta=0.2,  # Low proficiency signal
                    practiced=True,
                )

        # Detect error patterns
        error_keywords = ["traceback", "syntaxerror", "typeerror", "nameerror",
                          "indexerror", "keyerror", "valueerror", "attributeerror"]
        has_error = any(kw in msg_lower for kw in error_keywords)

        if has_error and topic:
            MemoryService.record_episode(
                db=db,
                user_id=user_id,
                memory_type=MemoryType.ERROR_PATTERN,
                topic=topic,
                summary=f"Student encountered an error in {topic}",
                importance=0.4,
                metadata={
                    "course": course_name,
                    "message_preview": user_message[:200],
                },
            )

    @staticmethod
    def record_assessment_result(
        db: Session,
        user_id: int,
        topic: str,
        score: int,
        max_score: int,
    ):
        """
        Update student model based on assessment results.
        Called after every assessment submission.
        """
        proficiency = score / max_score if max_score > 0 else 0.0

        # Update the skill
        MemoryService.update_skill(
            db=db,
            user_id=user_id,
            skill_name=topic,
            proficiency_delta=proficiency,
            assessed=True,
        )

        # Record episodic memory for notable results
        if proficiency < 0.4:
            MemoryService.record_episode(
                db=db,
                user_id=user_id,
                memory_type=MemoryType.STRUGGLE,
                topic=topic,
                summary=f"Scored {score}/{max_score} ({proficiency:.0%}) on {topic} assessment",
                importance=0.7,
                metadata={"score": score, "max_score": max_score, "proficiency": proficiency},
            )
        elif proficiency >= 0.9:
            MemoryService.record_episode(
                db=db,
                user_id=user_id,
                memory_type=MemoryType.BREAKTHROUGH,
                topic=topic,
                summary=f"Excellent score {score}/{max_score} ({proficiency:.0%}) on {topic}",
                importance=0.6,
                metadata={"score": score, "max_score": max_score, "proficiency": proficiency},
            )

    @staticmethod
    def record_lesson_completion(
        db: Session,
        user_id: int,
        course_name: str,
        lesson_topic: Optional[str] = None,
    ):
        """
        Update student model when a lesson is completed.
        Called after lesson completion tracking.
        """
        if lesson_topic:
            MemoryService.update_skill(
                db=db,
                user_id=user_id,
                skill_name=lesson_topic,
                proficiency_delta=0.6,  # Completing a lesson is a positive signal
                practiced=True,
            )
