"""Phase 3 — Content Embeddings (RAG)

Revision ID: a3c0_phase3_rag
Revises: a2b0_phase2_memory
Create Date: 2026-09-29

Creates the following new table:
- content_embeddings: Stores document chunks and embeddings for semantic search
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3c0_phase3_rag'
down_revision: Union[str, Sequence[str], None] = 'a2b0_phase2_memory'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create Phase 3 RAG tables."""
    
    # Check if pgvector extension is available in PostgreSQL
    bind = op.get_bind()
    if bind.dialect.name == "postgresql":
        try:
            op.execute("CREATE EXTENSION IF NOT EXISTS vector")
        except Exception as e:
            print(f"Warning: Could not create vector extension: {e}")

    # ─── Content Embeddings ───
    op.create_table(
        'content_embeddings',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('source_type', sa.String(50), nullable=False, index=True),
        sa.Column('source_id', sa.Integer(), nullable=True),
        sa.Column('chunk_index', sa.Integer(), server_default='0'),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('metadata_json', sa.JSON(), server_default='{}'),
        
        # We use JSON for maximum compatibility across SQLite and PostgreSQL during dev.
        # RAGService handles the pgvector optimization when on Postgres.
        sa.Column('embedding', sa.JSON(), nullable=True),
        
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # Note: On PostgreSQL, we will create the IVFFlat index via the RAGService 
    # or a separate postgres-only migration when we formally cast to VECTOR.


def downgrade() -> None:
    """Drop Phase 3 RAG tables."""
    op.drop_table('content_embeddings')
