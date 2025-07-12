# app/agents/base_llm.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from app.config import gemini_api_key

def run_llm(prompt: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # or gemini-1.5-flash
        temperature=0.7,
        google_api_key=gemini_api_key
    )
    
    messages = [HumanMessage(content=prompt)]
    return llm.invoke(messages).content
