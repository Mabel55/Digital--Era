from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
import hashlib
import models
import database
import auth
from ai_brain import ask_gemini

router = APIRouter(
    prefix="/translate",
    tags=["Translation"]
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class TranslationResponse(BaseModel):
    translated_text: str
    target_language: str
    from_cache: bool

@router.post("", response_model=TranslationResponse)
def translate_text(
    request: TranslationRequest,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    text = request.text.strip()
    target_language = request.target_language.strip().lower()
    
    if not text:
        return TranslationResponse(translated_text="", target_language=target_language, from_cache=True)
        
    if target_language in ["en", "english"]:
        return TranslationResponse(translated_text=text, target_language="en", from_cache=True)

    # 1. Create a unique hash for this exact text + target language
    hash_input = f"{target_language}:{text}".encode('utf-8')
    hash_id = hashlib.sha256(hash_input).hexdigest()
    
    # 2. Check the database cache
    cached_translation = db.query(models.LessonTranslationCache).filter(
        models.LessonTranslationCache.id == hash_id
    ).first()
    
    if cached_translation:
        return TranslationResponse(
            translated_text=cached_translation.translated_text,
            target_language=target_language,
            from_cache=True
        )
        
    # 3. Cache miss: Ask Gemini to translate
    system_prompt = (
        f"You are a professional technical translator translating educational programming content into {target_language.title()}.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "1. Translate ONLY the prose/explanations.\n"
        "2. DO NOT translate any code blocks (text inside ``` or `). Leave code syntax, keywords, and variable names strictly in English.\n"
        "3. Maintain all original markdown formatting, bullet points, and structure EXACTLY as they are.\n"
        "4. Output ONLY the translated text, with no introductory conversational filler like 'Here is the translation:'."
    )
    
    try:
        translated_text = ask_gemini(
            question=text,
            system_prompt_override=system_prompt
        )
        
        # 4. Save to cache
        new_cache = models.LessonTranslationCache(
            id=hash_id,
            original_text=text,
            target_language=target_language,
            translated_text=translated_text
        )
        db.add(new_cache)
        db.commit()
        
        return TranslationResponse(
            translated_text=translated_text,
            target_language=target_language,
            from_cache=False
        )
        
    except Exception as e:
        # If translation fails (e.g., API error), fallback to English so the UI doesn't break
        print(f"Translation Error: {e}")
        return TranslationResponse(translated_text=text, target_language="en", from_cache=True)
