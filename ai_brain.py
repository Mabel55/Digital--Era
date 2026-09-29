import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Database Imports
from sqlalchemy.orm import Session
from database import SessionLocal
import models

# LangChain & AI Imports
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Phase 3 RAG Service
from services.rag_service import rag_service

# Load variables from .env file securely
load_dotenv()

# ── EMBEDDING MODEL CONFIGURATION (Using Fast Cloud API) ──────────────
def load_embedding_model():
    """
    Uses Google Gemini embedding model.
    Significantly faster startup than local PyTorch embeddings.
    """
    print("⚡ Loading Google Gemini embedding model...")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    print("✅ Embedding model ready.")
    return embeddings


# ── GEMINI LLM INFERENCE ENGINE (Stable 2.5 Flash) ────────────────
def ask_gemini(question: str, context_chunks: list[str] = None, chat_history: list = None, course_title: str = "", student_level: str = "Beginner", student_track: str = "General", specific_course: str = "", system_prompt_override: str = None) -> str:
    """
    Prompts Gemini 2.5 Flash using LangChain's chat invocation sequence.
    """
    api_key = os.getenv("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=api_key,
        temperature=0.3
    )

    if system_prompt_override:
        system_prompt = system_prompt_override
    else:
        course_hint = f" Specifically, they are currently taking the module: '{specific_course}'." if specific_course else ""
        subject_hint = f" The student is studying: {course_title}." if course_title else ""
        
        level_instruction = ""
        if student_level == "Beginner":
            level_instruction = "Use simple analogies, avoid overly complex jargon, and explain foundational concepts step-by-step."
        elif student_level == "Advanced":
            level_instruction = "Assume the student knows the basics. Provide highly optimized, production-level code and discuss edge cases and performance."
            
        system_prompt = (
                f"You are a Senior Technical Instructor and Expert Code Tutor at Mabel's Coding School teaching a {student_level} student in the {student_track} track.{subject_hint}\n"
                f"{level_instruction}\n"
                "Your goal is to provide highly technical, professional, and code-centric answers to the student's questions.\n"
                "CRITICAL INSTRUCTIONS:\n"
                "1. BE STRICTLY TOPIC-SPECIFIC. ONLY explain the exact code the student provides or the exact topic being discussed. DO NOT introduce external concepts, unrelated libraries, or unprompted tangents.\n"
                "2. BE EXTREMELY CODE-SPECIFIC. Do not give long theoretical essays without backing them up with code. Your primary method of teaching should be through code snippets, code analysis, and syntax breakdowns.\n"
                "3. NEVER mention 'the database', or 'the lesson'. Do not explain where your information comes from. Just answer the question directly.\n"
                "4. Maintain a professional, authoritative, yet encouraging tone. Speak like a senior software engineer mentoring a junior developer during a pair-programming session.\n"
                "5. PHASE 6 REASONING: Before you provide your final response, you MUST think step-by-step. "
                "Write out your internal reasoning, planning, and validation inside `<think>...</think>` XML tags. "
                "Only the content outside of these tags will be shown to the user.\n"
        )

    # 1. Start the message array with your system prompt instructions
    
    # Inject RAG Context if available
    context_str = ""
    if context_chunks:
        context_str = "\n\n--- COURSE MATERIAL CONTEXT ---\nThe following is the exact course material the student is currently learning. Use this to guide your answer:\n" + "\n".join(context_chunks) + "\n-------------------------------\n"

    # ── SEMANTIC CACHING LOGIC ──
    # We only cache standalone questions (no chat history) to ensure context isn't lost.
    cache_id = None
    if not chat_history:
        import hashlib
        from database import SessionLocal
        hash_input = f"{system_prompt}|{context_str}|{question}".encode('utf-8')
        cache_id = hashlib.sha256(hash_input).hexdigest()
        
        db = SessionLocal()
        try:
            cached = db.query(models.AITutorCache).filter(models.AITutorCache.id == cache_id).first()
            if cached:
                print("⚡ Serving AI Tutor response from Semantic Cache! (Cost: $0)")
                return cached.response
        finally:
            db.close()

    messages = [("system", system_prompt + context_str)]

    # 2. Memory Injection: Loop through PostgreSQL rows and convert them to LangChain tuples
    if chat_history:
        for msg in chat_history:
            # Map DB roles ("user", "model") to LangChain syntax ("human", "ai")
            role = "human" if msg.role == "user" else "ai"
            messages.append((role, msg.content))

    # 3. Append the current question at the very end of the conversation thread
    messages.append(("human", question))

    # Invoke the model with the complete historical thread
    response = llm.invoke(messages)
    response_text = response.content.strip()

    # Save to Cache
    if cache_id:
        db = SessionLocal()
        try:
            new_cache = models.AITutorCache(id=cache_id, question=question, response=response_text)
            db.add(new_cache)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"⚠️ Failed to cache AI response: {e}")
        finally:
            db.close()

    return response_text


# ── MAIN VECTOR INDEX BUILDER (Phase 3 DB-backed) ────────────────────────────
def build_ai_brain(force_rebuild: bool = False):
    db: Session = SessionLocal()
    try:
        print("🔍 Querying lessons from PostgreSQL database...")
        lessons = db.query(models.Lesson).all()
        if not lessons:
            print("⚠️  No database records found. Add lessons through Swagger UI first.")
            return

        if force_rebuild:
            print("🗑️ Clearing existing lesson embeddings...")
            db.execute(models.ContentEmbedding.__table__.delete().where(models.ContentEmbedding.source_type == "lesson"))
            db.commit()

        # We keep track of which lessons are already indexed
        indexed_ids = set()
        if not force_rebuild:
            rows = db.query(models.ContentEmbedding.source_id).filter(models.ContentEmbedding.source_type == "lesson").distinct().all()
            indexed_ids = {r[0] for r in rows}

        lessons_to_process = [l for l in lessons if l.id not in indexed_ids][:5] # Limit for development

        if not lessons_to_process:
            print("✅ AI Brain is already up-to-date. Sync skipped.")
            return

        print(f"⚡ Indexing {len(lessons_to_process)} new lesson(s) into database...")

        total_chunks = 0
        for lesson in lessons_to_process:
            if not lesson.content or not lesson.content.strip():
                continue

            metadata = {
                "lesson_id": lesson.id,
                "course_id": lesson.course_id,
                "title": lesson.title
            }
            
            chunks_indexed = rag_service.index_content(
                db=db,
                source_type="lesson",
                content=lesson.content,
                source_id=lesson.id,
                metadata=metadata,
                chunk_size=500
            )
            total_chunks += chunks_indexed

        print(f"✅ Indexed {total_chunks} lesson chunks successfully.")

    finally:
        db.close()


# ── ROUTE INTEGRATION INTERFACE (Invoked directly by FastAPI) ───────────────
def query_ai_brain(question: str, course_id: int = None, top_k: int = 4, student_level: str = "Beginner", student_track: str = "General", specific_course:str = "") -> dict:
    db: Session = SessionLocal()
    try:
        results = rag_service.retrieve(db, question, top_k=top_k, source_type="lesson", source_id=course_id)
        
        if not results:
            return {"answer": "No matching concepts found.", "sources": [], "raw_chunks": []}

        context_chunks = [r["content"] for r in results]
        course_title = results[0]["metadata"].get("title", "") if results else ""

        try:
            answer = ask_gemini(question, context_chunks, course_title=course_title, student_level=student_level, student_track=student_track, specific_course=specific_course)
        except Exception as e:
            answer = f"[Inference Engine Unavailable: {e}]"

        sources = [
            {"title": r["metadata"].get("title"), "lesson_id": r["metadata"].get("lesson_id"), "chunk_index": r["id"]}
            for r in results
        ]

        return {"answer": answer, "sources": sources, "raw_chunks": context_chunks}
    finally:
        db.close()


# ── PDF INGESTION ────────────────────────────────────────────────────────────
def add_pdf_to_vector_db(file_path: str, course_title: str, course_level: str, course_track: str):
    """
    Reads a PDF, chops it into readable chunks, and injects it into the DB vector database.
    """
    # 1. Load the PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # 2. Combine into a single text
    full_text = "\n\n".join([doc.page_content for doc in documents])

    metadata = {
        "title": course_title,
        "level": course_level,
        "track": course_track,
        "filename": os.path.basename(file_path)
    }

    db = SessionLocal()
    try:
        chunks_indexed = rag_service.index_content(
            db=db,
            source_type="pdf_document",
            content=full_text,
            metadata=metadata,
            chunk_size=1000
        )
        print(f"🎉 Success! PDF has been completely ingested ({chunks_indexed} chunks).")
    finally:
        db.close()

# ── CUSTOMER SUPPORT BRAIN ───────────────────────────────────────────────────
def build_support_brain():
    """
    Reads the support_knowledge.md file and builds a DB index for customer support.
    """
    file_path = "support_knowledge.md"
    if not os.path.exists(file_path):
        print(f"⚠️ {file_path} not found. Cannot build support brain.")
        return

    print("🎧 Building Customer Support AI Brain...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    db = SessionLocal()
    try:
        print("🗑️ Clearing old support embeddings...")
        db.execute(models.ContentEmbedding.__table__.delete().where(models.ContentEmbedding.source_type == "support"))
        db.commit()
        
        chunks = rag_service.index_content(
            db=db,
            source_type="support",
            content=content,
            chunk_size=600
        )
        print(f"✅ Support Brain built and saved to Database! ({chunks} chunks)")
    finally:
        db.close()

def query_support_brain(question: str, top_k: int = 3) -> str:
    """
    Queries the customer support DB index and returns an answer using Gemini.
    """
    db = SessionLocal()
    try:
        results = rag_service.retrieve(db, question, top_k=top_k, source_type="support")
        
        if not results:
            return "I couldn't find an exact answer to that. Please reach out to nasaadanna@gmail.com or WhatsApp +234 703 719 7261."

        context_chunks = [r["content"] for r in results]
        
        system_prompt = (
            "You are the official Customer Support AI for Digital Era, a premium tech training center in Lagos. "
            "Your job is to answer prospective students' questions accurately, politely, and enthusiastically. "
            "Use ONLY the context provided to answer the question. If the answer is not in the context, "
            "apologize and tell them to contact +234 703 719 7261 or nasaadanna@gmail.com. "
            "Do NOT mention that you are reading from a 'context' or 'document'. "
            "Keep your answers concise and helpful."
        )
        
        return ask_gemini(question, context_chunks, system_prompt_override=system_prompt)
    finally:
        db.close()

if __name__ == "__main__":
    build_ai_brain()
    build_support_brain()