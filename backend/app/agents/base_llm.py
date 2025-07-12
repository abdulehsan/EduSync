from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Gemini setup with streaming
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or "gemini-pro"
    temperature=0.2,
    streaming=True,
    max_tokens=None,
    callbacks=[StreamingStdOutCallbackHandler()]  # Optional: logs chunks to stdout
)
