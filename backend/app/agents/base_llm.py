from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from app.config import gemini_api_key

# Gemini setup with streaming
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # or "gemini-pro"
    temperature=0.2,
    streaming=True,
    max_tokens=None,
    google_api_key=gemini_api_key,
    callbacks=[StreamingStdOutCallbackHandler()]  # Optional: logs chunks to stdout
)
