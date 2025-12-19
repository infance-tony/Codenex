from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_db, User, ChatLog, ChatSession
import requests
import os
from dotenv import load_dotenv
import json
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")
API_KEY = os.getenv("API_KEY")

security = HTTPBearer()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    session_id: int

class SessionRequest(BaseModel):
    name: str

client = OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=CEREBRAS_API_KEY,
)

@app.post("/chat")
def chat(request: ChatRequest, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    if credentials.credentials != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    message = request.message
    session_id = request.session_id

    # Call OpenRouter API using OpenAI client
    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful chatbot named 'EduBot'. Provide precise, accurate, and concise answers for learning purposes."},
                {"role": "user", "content": message}
            ],
            model="llama-3.3-70b",
            max_completion_tokens=1024,
            temperature=0.2,
            top_p=1,
            stream=False
        )
        ai_response = completion.choices[0].message.content
    except Exception as e:
        print(f"OpenAI client error: {e}")
        ai_response = f"Mock response: I'm sorry, but the AI service is unavailable. Your question was: '{message}'"

    # Save chat log
    chat_log = ChatLog(session_id=session_id, message=message, response=ai_response)
    db.add(chat_log)
    db.commit()

    # Update session name if it's the first message
    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    if session and session.name == "New Chat":
        session.name = message[:20] + "..." if len(message) > 20 else message
        db.commit()

    return {"response": ai_response}

@app.get("/history/{session_id}")
def get_history(session_id: int, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    logs = db.query(ChatLog).filter(ChatLog.session_id == session_id).all()
    return [{"message": log.message, "response": log.response, "timestamp": log.timestamp} for log in logs]

@app.post("/session")
def create_session(request: SessionRequest, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    session = ChatSession(name=request.name)
    db.add(session)
    db.commit()
    return {"id": session.id, "name": session.name}

@app.get("/sessions")
def get_sessions(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    sessions = db.query(ChatSession).all()
    return [{"id": s.id, "name": s.name, "created_at": s.created_at} for s in sessions]

@app.delete("/session/{session_id}")
def delete_session(session_id: int, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    db.query(ChatLog).filter(ChatLog.session_id == session_id).delete()
    db.query(ChatSession).filter(ChatSession.id == session_id).delete()
    db.commit()
    return {"status": "deleted"}

@app.put("/session/{session_id}")
def update_session(session_id: int, request: SessionRequest, db: Session = Depends(get_db)):
    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    if session:
        session.name = request.name
        db.commit()
    return {"status": "updated"}