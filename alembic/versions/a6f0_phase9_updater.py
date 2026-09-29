"""Phase 9 — Automated Lesson Updater

Revision ID: a6f0_phase9_updater
Revises: a5e0_phase7_eval
Create Date: 2026-09-29

Creates the following new table:
- lesson_update_proposals: AI-generated proposals for rewriting low-performing lessons.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6f0_phase9_updater'
down_revision: Union[str, Sequence[str], None] = 'a5e0_phase7_eval'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create Phase 9 Lesson Updater tables."""
    
    op.create_table(
        'lesson_update_proposals',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('lesson_id', sa.Integer(), sa.ForeignKey('lessons.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('reason', sa.Text(), nullable=False),
        sa.Column('original_content', sa.Text(), nullable=False),
        sa.Column('proposed_content', sa.Text(), nullable=False),
        sa.Column('status', sa.String(20), server_default='pending'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade() -> None:
    """Drop Phase 9 Updater tables."""
    op.drop_table('lesson_update_proposals')
