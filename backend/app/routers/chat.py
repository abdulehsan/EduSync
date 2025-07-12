# app/routers/chat.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.base_llm import run_llm

router = APIRouter()

# Request + Response Schemas
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat_handler(payload: ChatRequest):
    try:
        if not payload.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        reply = run_llm(payload.message)
        return {"response": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")
