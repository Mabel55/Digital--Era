"""Phase 2 — Memory System and Student Model

Revision ID: a2b0_phase2_memory
Revises: d31fbca6164c
Create Date: 2026-09-29

Creates the following new tables:
- episodic_memories: Important past learning events per student
- semantic_memories: Stable facts about each student
- student_skills: Skill proficiency tracking
- procedural_memories: Teaching strategies effectiveness (shared)
- ai_interaction_logs: Structured AI interaction logs
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2b0_phase2_memory'
down_revision: Union[str, Sequence[str], None] = 'd31fbca6164c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create Phase 2 memory tables."""

    # ─── Episodic Memories ───
    op.create_table(
        'episodic_memories',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('memory_type', sa.String(50), nullable=False, index=True),
        sa.Column('topic', sa.String(255), nullable=True, index=True),
        sa.Column('summary', sa.Text(), nullable=False),
        sa.Column('importance', sa.Float(), server_default='0.5'),
        sa.Column('metadata_json', sa.JSON(), server_default='{}'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('last_accessed', sa.DateTime(), server_default=sa.func.now()),
    )

    # ─── Semantic Memories ───
    op.create_table(
        'semantic_memories',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('fact_type', sa.String(50), nullable=False, index=True),
        sa.Column('key', sa.String(255), nullable=False),
        sa.Column('value', sa.Text(), nullable=False),
        sa.Column('confidence', sa.Float(), server_default='0.5'),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )
    # Unique constraint: one fact per (user_id, fact_type, key)
    op.create_index(
        'ix_semantic_unique_fact',
        'semantic_memories',
        ['user_id', 'fact_type', 'key'],
        unique=True,
    )

    # ─── Student Skills ───
    op.create_table(
        'student_skills',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('skill_name', sa.String(255), nullable=False, index=True),
        sa.Column('proficiency', sa.Float(), server_default='0.0'),
        sa.Column('assessment_count', sa.Integer(), server_default='0'),
        sa.Column('practice_count', sa.Integer(), server_default='0'),
        sa.Column('last_assessed', sa.DateTime(), nullable=True),
        sa.Column('last_practiced', sa.DateTime(), nullable=True),
        sa.Column('needs_revision', sa.Boolean(), server_default='0'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )
    # Unique constraint: one skill record per (user_id, skill_name)
    op.create_index(
        'ix_student_skills_unique',
        'student_skills',
        ['user_id', 'skill_name'],
        unique=True,
    )

    # ─── Procedural Memories (shared, not per-user) ───
    op.create_table(
        'procedural_memories',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('procedure_type', sa.String(100), nullable=False, index=True),
        sa.Column('topic', sa.String(255), nullable=True, index=True),
        sa.Column('procedure', sa.Text(), nullable=False),
        sa.Column('success_count', sa.Integer(), server_default='0'),
        sa.Column('failure_count', sa.Integer(), server_default='0'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # ─── AI Interaction Logs ───
    op.create_table(
        'ai_interaction_logs',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('interaction_type', sa.String(50), nullable=False, index=True),
        sa.Column('topic', sa.String(255), nullable=True),
        sa.Column('course_name', sa.String(255), nullable=True),
        sa.Column('user_message', sa.Text(), nullable=False),
        sa.Column('ai_response', sa.Text(), nullable=False),
        sa.Column('response_quality', sa.String(20), nullable=True),
        sa.Column('tools_used', sa.JSON(), server_default='[]'),
        sa.Column('context_sources', sa.JSON(), server_default='[]'),
        sa.Column('latency_ms', sa.Integer(), nullable=True),
        sa.Column('token_count', sa.Integer(), nullable=True),
        sa.Column('metadata_json', sa.JSON(), server_default='{}'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )
    # Index for quick lookup by user + type + date range
    op.create_index(
        'ix_ai_logs_user_type',
        'ai_interaction_logs',
        ['user_id', 'interaction_type'],
    )


def downgrade() -> None:
    """Drop Phase 2 memory tables."""
    op.drop_table('ai_interaction_logs')
    op.drop_table('procedural_memories')
    op.drop_table('student_skills')
    op.drop_index('ix_semantic_unique_fact', table_name='semantic_memories')
    op.drop_table('semantic_memories')
    op.drop_table('episodic_memories')
