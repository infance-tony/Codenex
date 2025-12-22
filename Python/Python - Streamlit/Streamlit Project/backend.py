from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, User, ChatLog, ChatSession, UploadedFile
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from cerebras.cloud.sdk import Cerebras

load_dotenv()
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    session_id: int

class SessionRequest(BaseModel):
    name: str

class FileUploadRequest(BaseModel):
    session_id: int
    filename: str
    file_type: str
    file_content: str  # Base64 encoded
    extracted_text: str
    session_id: int

class SessionRequest(BaseModel):
    name: str

def get_cerebras_client():
    return Cerebras(api_key=CEREBRAS_API_KEY)

@app.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    message = request.message
    session_id = request.session_id

    # Call Cerebras API
    try:
        client = get_cerebras_client()
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
        print(f"Cerebras API error: {e}")
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
def get_history(session_id: int, db: Session = Depends(get_db)):
    logs = db.query(ChatLog).filter(ChatLog.session_id == session_id).all()
    return [{"message": log.message, "response": log.response, "timestamp": log.timestamp} for log in logs]

@app.post("/session")
def create_session(request: SessionRequest, db: Session = Depends(get_db)):
    session = ChatSession(name=request.name)
    db.add(session)
    db.commit()
    return {"id": session.id, "name": session.name}

@app.get("/sessions")
def get_sessions(db: Session = Depends(get_db)):
    sessions = db.query(ChatSession).all()
    return [{"id": s.id, "name": s.name, "created_at": s.created_at} for s in sessions]

@app.delete("/session/{session_id}")
def delete_session(session_id: int, db: Session = Depends(get_db)):
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

@app.post("/upload")
def upload_file(request: FileUploadRequest, db: Session = Depends(get_db)):
    import base64
    # Decode base64 file content
    file_bytes = base64.b64decode(request.file_content)
    
    # Save to database
    uploaded_file = UploadedFile(
        session_id=request.session_id,
        filename=request.filename,
        file_type=request.file_type,
        file_content=file_bytes,
        extracted_text=request.extracted_text
    )
    db.add(uploaded_file)
    db.commit()
    
    return {"status": "saved", "id": uploaded_file.id, "filename": request.filename}

@app.get("/files/{session_id}")
def get_session_files(session_id: int, db: Session = Depends(get_db)):
    files = db.query(UploadedFile).filter(UploadedFile.session_id == session_id).all()
    return [{"id": f.id, "filename": f.filename, "file_type": f.file_type, "timestamp": f.timestamp} for f in files]