from fastapi import APIRouter
from pydantic import BaseModel
from ai_brain import query_support_brain

router = APIRouter(prefix="/api/support", tags=["Support"])

class SupportQuery(BaseModel):
    message: str

@router.post("/chat")
def support_chat(query: SupportQuery):
    """
    Handles customer support queries using the Support FAISS Brain.
    """
    try:
        answer = query_support_brain(query.message)
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Sorry, I am facing technical difficulties. Error: {e}. Please contact us via phone."}
