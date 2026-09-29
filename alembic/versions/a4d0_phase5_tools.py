"""Phase 5 — Tool Registry

Revision ID: a4d0_phase5_tools
Revises: a3c0_phase3_rag
Create Date: 2026-09-29

Creates the following new table:
- tool_invocation_logs: Audit log of all tools executed by the AI or the user.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4d0_phase5_tools'
down_revision: Union[str, Sequence[str], None] = 'a3c0_phase3_rag'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create Phase 5 Tool Registry tables."""
    
    op.create_table(
        'tool_invocation_logs',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('tool_name', sa.String(100), nullable=False, index=True),
        sa.Column('input_data', sa.JSON(), server_default='{}'),
        sa.Column('output_data', sa.JSON(), server_default='{}'),
        sa.Column('is_success', sa.Boolean(), server_default='1'),
        sa.Column('error_message', sa.Text(), nullable=True),
        sa.Column('latency_ms', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade() -> None:
    """Drop Phase 5 Tool Registry tables."""
    op.drop_table('tool_invocation_logs')
