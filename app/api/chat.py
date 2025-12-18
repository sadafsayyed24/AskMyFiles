from fastapi import APIRouter
from app.rag.qa import answer_question

router = APIRouter()

@router.post("/chat")
def chat(query: str):
    answer = answer_question(query)
    return {"answer": answer}
