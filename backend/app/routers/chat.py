from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from agents.base_llm import llm

class ChatRequest(BaseModel):
    message: str

def stream_response(generator):
    for chunk in generator:
        if chunk.content:
            yield chunk.content

def generate_prompt(user_input: str):
    prompt = ChatPromptTemplate.from_messages([
        ("human", "{input}")
    ])
    return prompt.format_messages(input=user_input)

def chat_stream_generator(user_input: str):
    prompt = generate_prompt(user_input)
    return stream_response(llm.stream(prompt))
