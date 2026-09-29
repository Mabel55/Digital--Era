"""Phase 7 — AI Evaluation System

Revision ID: a5e0_phase7_eval
Revises: a4d0_phase5_tools
Create Date: 2026-09-29

Creates the following new table:
- ai_evaluations: Independent evaluations of AI responses for quality tracking.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5e0_phase7_eval'
down_revision: Union[str, Sequence[str], None] = 'a4d0_phase5_tools'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create Phase 7 Evaluation tables."""
    
    op.create_table(
        'ai_evaluations',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('interaction_id', sa.Integer(), sa.ForeignKey('ai_interaction_logs.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('correctness_score', sa.Float(), nullable=True),
        sa.Column('relevance_score', sa.Float(), nullable=True),
        sa.Column('hallucination_risk', sa.Float(), nullable=True),
        sa.Column('code_validity_score', sa.Float(), nullable=True),
        sa.Column('safety_score', sa.Float(), nullable=True),
        sa.Column('verdict', sa.String(50), nullable=False),
        sa.Column('evaluation_metadata', sa.JSON(), server_default='{}'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade() -> None:
    """Drop Phase 7 Evaluation tables."""
    op.drop_table('ai_evaluations')
