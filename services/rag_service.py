"""
RAG Service — Digital Era AI 2.0 (Phase 3)

Manages vector embeddings and retrieval for course content and documentation.
This service replaces the file-based FAISS index with a robust database-backed
vector store.

Features:
- Stores embeddings in the database (content_embeddings table)
- Cross-compatible: Uses SQL-native vector search (pgvector) in production PostgreSQL, 
  and falls back to fast in-memory Python similarity search for local SQLite dev.
- Supports metadata filtering (by course, lesson, difficulty) alongside semantic search.
"""

import json
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
import numpy as np

import models

class RAGService:
    """
    Service for indexing and retrieving vector embeddings.
    """
    
    def __init__(self):
        # We lazily load the embedding model to avoid startup delays
        self._embedding_model = None

    @property
    def embedding_model(self):
        if self._embedding_model is None:
            # Import here to avoid circular import with ai_brain
            from ai_brain import load_embedding_model
            self._embedding_model = load_embedding_model()
        return self._embedding_model

    def index_content(
        self, 
        db: Session, 
        source_type: str, 
        content: str, 
        source_id: Optional[int] = None, 
        metadata: Optional[Dict[str, Any]] = None,
        chunk_size: int = 1000
    ) -> int:
        """
        Embed and index content into the database.
        Returns the number of chunks indexed.
        """
        # Split text into chunks
        chunks = self._chunk_text(content, chunk_size)
        
        # Calculate embeddings for all chunks in a batch
        embeddings = self.embedding_model.embed_documents(chunks)
        
        # Save to database
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            db_record = models.ContentEmbedding(
                source_type=source_type,
                source_id=source_id,
                chunk_index=i,
                content=chunk,
                metadata_json=metadata or {},
                embedding=embedding
            )
            db.add(db_record)
            
        db.commit()
        return len(chunks)

    def retrieve(
        self, 
        db: Session, 
        query: str, 
        top_k: int = 4, 
        source_type: Optional[str] = None,
        source_id: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve the most relevant content chunks for a given query.
        """
        # 1. Embed the query
        query_embedding = self.embedding_model.embed_query(query)
        
        # 2. Check dialect to determine search method
        dialect = db.bind.dialect.name
        
        if dialect == "postgresql":
            return self._retrieve_pgvector(db, query_embedding, top_k, source_type, source_id)
        else:
            return self._retrieve_sqlite_fallback(db, query_embedding, top_k, source_type, source_id)

    def _retrieve_pgvector(
        self, db: Session, query_embedding: List[float], top_k: int, 
        source_type: Optional[str], source_id: Optional[int]
    ) -> List[Dict[str, Any]]:
        """Optimized retrieval using native pgvector cosine similarity."""
        
        # Construct raw SQL for pgvector search
        # We assume the embedding column was cast to vector during Postgres deployment
        query_str = """
            SELECT id, source_type, source_id, content, metadata_json,
                   1 - (embedding::vector <=> :embedding::vector) AS similarity
            FROM content_embeddings
            WHERE 1=1
        """
        params = {"embedding": f"[{','.join(map(str, query_embedding))}]", "top_k": top_k}
        
        if source_type:
            query_str += " AND source_type = :source_type"
            params["source_type"] = source_type
            
        if source_id:
            query_str += " AND source_id = :source_id"
            params["source_id"] = source_id
            
        query_str += " ORDER BY embedding::vector <=> :embedding::vector LIMIT :top_k"
        
        result = db.execute(text(query_str), params).fetchall()
        
        return [
            {
                "id": r[0],
                "source_type": r[1],
                "source_id": r[2],
                "content": r[3],
                "metadata": r[4],
                "similarity": r[5]
            }
            for r in result
        ]

    def _retrieve_sqlite_fallback(
        self, db: Session, query_embedding: List[float], top_k: int, 
        source_type: Optional[str], source_id: Optional[int]
    ) -> List[Dict[str, Any]]:
        """In-memory numpy retrieval for local SQLite development."""
        
        # Fetch all candidate embeddings from DB
        query = db.query(models.ContentEmbedding)
        if source_type:
            query = query.filter(models.ContentEmbedding.source_type == source_type)
        if source_id:
            query = query.filter(models.ContentEmbedding.source_id == source_id)
            
        candidates = query.all()
        if not candidates:
            return []
            
        # Compute cosine similarity using numpy
        q_vec = np.array(query_embedding)
        q_norm = np.linalg.norm(q_vec)
        
        results = []
        for candidate in candidates:
            if not candidate.embedding:
                continue
                
            c_vec = np.array(candidate.embedding)
            c_norm = np.linalg.norm(c_vec)
            
            if c_norm == 0 or q_norm == 0:
                similarity = 0.0
            else:
                similarity = np.dot(q_vec, c_vec) / (q_norm * c_norm)
                
            results.append({
                "id": candidate.id,
                "source_type": candidate.source_type,
                "source_id": candidate.source_id,
                "content": candidate.content,
                "metadata": candidate.metadata_json,
                "similarity": float(similarity)
            })
            
        # Sort by highest similarity
        results.sort(key=lambda x: x["similarity"], reverse=True)
        return results[:top_k]

    def _chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
        """Simple fallback text splitter if Langchain's isn't available."""
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )
        return splitter.split_text(text)

# Singleton instance for easy import
rag_service = RAGService()
