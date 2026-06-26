from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user
from ai_brain import ask_gemini
import shutil
import os

router = APIRouter(tags=["AI Tutor"])

@router.post("/chat")
def chat_with_study_buddy(
    payload: schemas.ChatRequest, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    try:
        # 1. Fetch all past messages between this student and the AI from PostgreSQL
        past_messages = db.query(models.ChatMessage)\
                          .filter(models.ChatMessage.user_id == current_user.id)\
                          .order_by(models.ChatMessage.timestamp.asc())\
                          .all()
        
        # 2. Extract question text
        question_text = payload.question if hasattr(payload, 'question') else payload.message
        
        # 3. Fetch lesson context if lesson_id is provided
        context_chunks = []
        if getattr(payload, 'lesson_id', None):
            lesson = db.query(models.Lesson).filter(models.Lesson.id == payload.lesson_id).first()
            if lesson:
                context_chunks.append(f"CURRENT LESSON CONTEXT:\nTitle: {lesson.title}\nContent: {lesson.content}\nExpected Output: {lesson.expected_output or 'N/A'}")

        # 4. Run your LangChain engine passing the database history AND lesson context
        answer = ask_gemini(
            question=question_text, 
            context_chunks=context_chunks, 
            chat_history=past_messages
        )
        
        # 4. Save the student's input question to PostgreSQL
        student_msg = models.ChatMessage(user_id=current_user.id, role="user", content=question_text)
        db.add(student_msg)

        # 5. Save Gemini's answer to PostgreSQL right next to it
        ai_msg = models.ChatMessage(user_id=current_user.id, role="model", content=answer)
        db.add(ai_msg)
        
        db.commit()
        
        return {
            "answer": answer,
            "sources_used": []
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Brain Error: {str(e)}")

@router.post("/ask-ai/")
def ask_ai_tutor(chat: schemas.ChatRequest): 
    try:
        system_prompt = f"""You are Mabel, a senior software engineering instructor at Mabel Academy - a coding school for Nigerian developers.
        You are teaching a {chat.level} student who wants to master {chat.track}.
        Current course: {chat.course}.
        Be encouraging, concise, and use Nigerian examples when helpful (Lagos, Naira, jollof rice, etc).
        Never give full solutions unless grading - give hints, ask questions, guide thinking.
        Format code with proper markdown code blocks."""

        ai_reply = ask_gemini(chat.message, context_chunks=[], system_prompt_override=system_prompt)
        return {"reply": ai_reply}

    except Exception as e:
        return {"reply": f"System Error: Could not connect to the model. Details: {str(e)}"}
