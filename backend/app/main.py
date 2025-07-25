from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from app.routers.chat import chat_stream_generator
app = FastAPI()

# Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    # allow_origins=["https://edusync-ai.netlify.app/"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    return StreamingResponse(chat_stream_generator(user_input), media_type="text/plain")

@app.get("/")
def root():
    return {"message": "EduSync Backend is running"}
