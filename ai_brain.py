import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Database Imports
from sqlalchemy.orm import Session
from database import SessionLocal
import models

# LangChain & AI Imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings

# Load variables from .env file securely
load_dotenv()

# ── EMBEDDING MODEL CONFIGURATION (100% Local - No Quota) ──────────────
def load_embedding_model():
    """
    Uses HuggingFace sentence-transformers locally.
    Zero API calls, zero quota limits, works offline.
    """
    print("⚡ Loading local HuggingFace embedding model (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    print("✅ Local embedding model ready. Zero quota used.")
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
        )

    # 1. Start the message array with your system prompt instructions
    messages = [("system", system_prompt)]

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
    return response.content.strip()


# ── BRAIN STORAGE & META TRACKING ───────────────────────────────────────────
BRAIN_DIR = "study_buddy_brain"
METADATA_FILE = os.path.join(BRAIN_DIR, "brain_meta.json")

def _load_brain_metadata() -> dict:
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as f:
            return json.load(f)
    return {"last_built": None, "lesson_ids": []}

def _save_brain_metadata(lesson_ids: list):
    os.makedirs(BRAIN_DIR, exist_ok=True)
    with open(METADATA_FILE, "w") as f:
        json.dump({
            "last_built": datetime.utcnow().isoformat(),
            "lesson_ids": lesson_ids
        }, f)


# ── MAIN VECTOR INDEX BUILDER ────────────────────────────────────────────────
def build_ai_brain(force_rebuild: bool = False):
    db: Session = SessionLocal()
    try:
        print("🔍 Step 1: Querying lessons from PostgreSQL database...")
        lessons = db.query(models.Lesson).all()
        if not lessons:
            print("⚠️  No database records found. Add lessons through Swagger UI first.")
            return

        meta = _load_brain_metadata()
        existing_ids = set(meta.get("lesson_ids", []))
        current_ids = {lesson.id for lesson in lessons}

        if not force_rebuild and os.path.exists(os.path.join(BRAIN_DIR, "index.faiss")):
            new_lessons = [l for l in lessons if l.id not in existing_ids]
            if not new_lessons:
                print("✅ AI Brain vector cache is already up-to-date. Sync skipped.")
                return
            lessons_to_process = new_lessons
            print(f"⚡ Syncing updates: processing {len(new_lessons)} new lesson(s)...")
            incremental = True
        else:
            lessons_to_process = lessons
            incremental = False
            print(f"🏗️  Executing full rebuild: processing all {len(lessons)} lesson(s)...")

        print("📦 Step 2: Running text splitters into semantic chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=75,
            separators=["\n\n", "\n", ". ", " ", ""],
        )
        docs_to_embed: list[Document] = []

        for lesson in lessons_to_process:
            if not lesson.content or not lesson.content.strip():
                continue

            chunks = text_splitter.split_text(lesson.content)
            for index, chunk in enumerate(chunks):
                doc = Document(
                    page_content=chunk,
                    metadata={
                        "lesson_id": lesson.id,
                        "course_id": lesson.course_id,
                        "title": lesson.title,
                        "chunk_index": index,
                        "total_chunks": len(chunks),
                    }
                )
                docs_to_embed.append(doc)

        print(f"✅ Generated {len(docs_to_embed)} vector-ready document objects.")

        print("🤖 Step 3: Initializing active vector model mapping...")
        embedding_model = load_embedding_model()

        print("🧠 Step 4: Compiling vector coordinates inside FAISS matrix...")
        if incremental:
            vector_db = FAISS.load_local(BRAIN_DIR, embedding_model, allow_dangerous_deserialization=True)
            vector_db.add_documents(docs_to_embed)
        else:
            vector_db = FAISS.from_documents(docs_to_embed, embedding_model)

        vector_db.save_local(BRAIN_DIR)
        _save_brain_metadata(list(current_ids))
        print(f"✅ AI Brain vector records updated successfully inside '{BRAIN_DIR}/'.")

        print("\n🔎 Running active diagnostic script validation with Gemini 2.5 Flash...")
        query = "What is Python?"
        results = vector_db.similarity_search(query, k=3)

        if results:
            context_chunks = [r.page_content for r in results]
            source_titles = list({r.metadata["title"] for r in results})
            print(f"   📖 Sources extracted: {source_titles}")

            try:
                answer = ask_gemini(query, context_chunks)
                print(f"\n   🤖 Gemini Diagnostic Response:\n   {answer}")
            except Exception as e:
                print(f"   ⚠️  Gemini inference connection skipped ({e}).")
        else:
            print("   ⚠️  Diagnostic test query yielded zero structural matches.")

    finally:
        db.close()


# ── ROUTE INTEGRATION INTERFACE (Invoked directly by FastAPI) ───────────────
def query_ai_brain(question: str, course_id: int = None, top_k: int = 4, student_level: str = "Beginner", student_track: str = "General", specific_course:str = "") -> dict:
    if not os.path.exists(os.path.join(BRAIN_DIR, "index.faiss")):
        return {"answer": "AI brain unbuilt.", "sources": [], "raw_chunks": []}

    embedding_model = load_embedding_model()
    vector_db = FAISS.load_local(BRAIN_DIR, embedding_model, allow_dangerous_deserialization=True)

    fetch_k = top_k * 3 if course_id else top_k
    results = vector_db.similarity_search(question, k=fetch_k)

    if course_id is not None:
        results = [r for r in results if r.metadata.get("course_id") == course_id]
    results = results[:top_k]

    if not results:
        return {"answer": "No matching concepts found.", "sources": [], "raw_chunks": []}

    context_chunks = [r.page_content for r in results]
    course_title = results[0].metadata.get("title", "") if results else ""

    try:
        answer = ask_gemini(question, context_chunks, course_title=course_title, student_level=student_level, student_track=student_track, specific_course=specific_course)
    except Exception as e:
        answer = f"[Inference Engine Unavailable: {e}]"

    sources = [
        {"title": r.metadata.get("title"), "lesson_id": r.metadata.get("lesson_id"), "chunk_index": r.metadata.get("chunk_index")}
        for r in results
    ]

    return {"answer": answer, "sources": sources, "raw_chunks": context_chunks}


# ── PDF INGESTION ────────────────────────────────────────────────────────────
def add_pdf_to_vector_db(file_path: str, course_title: str, course_level: str, course_track: str):
    """
    Reads a PDF, chops it into readable chunks, and injects it into the FAISS vector database.
    """
    # 1. Load the PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # 2. Tag every page with the course title, level, and track
    for doc in documents:
        doc.metadata["title"] = course_title
        doc.metadata["level"] = course_level
        doc.metadata["track"] = course_track

    # 3. Chop into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # 4. Load local embedding model (no quota, no API key needed)
    embeddings = load_embedding_model()

    # 5. Inject into FAISS - no batching/sleep needed (local model)
    try:
        vector_db = FAISS.load_local(BRAIN_DIR, embeddings, allow_dangerous_deserialization=True)
        is_new_brain = False
        print(f"🔄 Found existing {BRAIN_DIR}. Appending new documents...")
    except Exception:
        is_new_brain = True
        print(f"✨ No existing brain found. Creating a fresh {BRAIN_DIR}...")

    if is_new_brain:
        vector_db = FAISS.from_documents(chunks, embeddings)
    else:
        vector_db.add_documents(chunks)

    vector_db.save_local(BRAIN_DIR)
    print("🎉 Success! PDF has been completely ingested with no errors.")


if __name__ == "__main__":
    build_ai_brain()