# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI(
    title="EduSync AI Backend",
    description="Modular Agentic RAG System powered by Gemini + LangChain",
    version="0.1.0",
)

# CORS — allow frontend to connect (adjust origins in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registration
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/", tags=["Root"])
async def root():
    return {"status": "EduSync backend is live"}
