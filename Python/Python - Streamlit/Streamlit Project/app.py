import streamlit as st
import requests
import json
import time
import PyPDF2
from docx import Document
from PIL import Image
import pytesseract

# Backend URL
BACKEND_URL = "http://localhost:8000"

if 'pause' not in st.session_state:
    st.session_state.pause = False

def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_docx_text(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_image_text(file):
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        if text.strip():
            return text
        else:
            return f"An image named '{file.name}' has been uploaded. No text was extracted via OCR. Please analyze or describe what this image might show based on the filename and any relevant context. If you have a description, provide it for better analysis."
    except Exception as e:
        return f"An image named '{file.name}' has been uploaded. OCR failed due to: {str(e)}. Please analyze or describe what this image might show based on the filename and any relevant context. If you have a description, provide it for better analysis."

st.title("Personalized Learning Assistant Chatbot")

# Sidebar for sessions
st.sidebar.header("Chat Sessions")

# Get sessions
try:
    response = requests.get(f"{BACKEND_URL}/sessions")
    sessions = response.json() if response.status_code == 200 else []
except:
    sessions = []

# Auto-create session if none
if "current_session" not in st.session_state:
    try:
        response = requests.post(f"{BACKEND_URL}/session", json={"name": "New Chat"})
        if response.status_code == 200:
            new_session = response.json()
            st.session_state.current_session = new_session["id"]
            st.session_state.messages = []
    except:
        pass

session_names = [s["name"] for s in sessions]

# Include current session in options if not already
if "current_session" in st.session_state:
    current_name = None
    for s in sessions:
        if s["id"] == st.session_state.current_session:
            current_name = s["name"]
            break
    if current_name and current_name not in session_names:
        session_names.append(current_name)

# New Chat button
if st.sidebar.button("New Chat"):
    try:
        response = requests.post(f"{BACKEND_URL}/session", json={"name": "New Chat"})
        if response.status_code == 200:
            new_session = response.json()
            st.session_state.current_session = new_session["id"]
            st.session_state.messages = []
            st.sidebar.success("New chat created!")
            st.rerun()
        else:
            st.sidebar.error("Failed to create new chat")
    except:
        st.sidebar.error("Backend not running")

# Select session
selected = st.sidebar.selectbox("Select Chat", [""] + session_names)

if st.sidebar.button("Load Selected Chat") and selected and selected != "":
    session_id = sessions[session_names.index(selected)]["id"]
    st.session_state.current_session = session_id
    # Load messages
    try:
        response = requests.get(f"{BACKEND_URL}/history/{session_id}")
        if response.status_code == 200:
            history = response.json()
            st.session_state.messages = []
            for h in history:
                st.session_state.messages.append({"role": "user", "content": h["message"]})
                st.session_state.messages.append({"role": "assistant", "content": h["response"]})
            st.sidebar.success("Chat loaded!")
        else:
            st.sidebar.error("Failed to load chat history")
    except:
        st.sidebar.error("Error loading chat")
    st.rerun()

# Rename session
if "current_session" in st.session_state:
    new_name = st.sidebar.text_input("Rename Chat", value=selected if selected else "")
    if st.sidebar.button("Update Name"):
        if new_name.strip():
            try:
                response = requests.put(f"{BACKEND_URL}/session/{st.session_state.current_session}", json={"name": new_name})
                if response.status_code == 200:
                    st.sidebar.success("Chat name updated!")
                    st.rerun()
                else:
                    st.sidebar.error("Failed to update name")
            except:
                st.sidebar.error("Backend not running")
        else:
            st.sidebar.error("Name cannot be empty")

    if st.sidebar.button("Delete Chat"):
        try:
            response = requests.delete(f"{BACKEND_URL}/session/{st.session_state.current_session}")
            if response.status_code == 200:
                st.session_state.messages = []
                if "current_session" in st.session_state:
                    del st.session_state.current_session
                st.sidebar.success("Chat deleted!")
                st.rerun()
            else:
                st.sidebar.error("Failed to delete chat")
        except:
            st.sidebar.error("Error deleting chat")

    if st.sidebar.button("Delete All Chats"):
        try:
            response = requests.get(f"{BACKEND_URL}/sessions")
            if response.status_code == 200:
                all_sessions = response.json()
                for sess in all_sessions:
                    requests.delete(f"{BACKEND_URL}/session/{sess['id']}")
                st.session_state.messages = []
                if "current_session" in st.session_state:
                    del st.session_state.current_session
                st.sidebar.success("All chats deleted!")
                st.rerun()
            else:
                st.sidebar.error("Failed to get sessions")
        except:
            pass
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
uploaded_file_inline = st.file_uploader("📎", type=["pdf", "docx", "png", "jpg", "jpeg"], label_visibility="collapsed")

if uploaded_file_inline and "current_session" in st.session_state:
    file_type = uploaded_file_inline.type
    extracted = ""
    try:
        if file_type == "application/pdf":
            extracted = extract_pdf_text(uploaded_file_inline)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            extracted = extract_docx_text(uploaded_file_inline)
        elif file_type.startswith("image/"):
            extracted = extract_image_text(uploaded_file_inline)
        else:
            st.error("Unsupported file type")
    except Exception as e:
        st.error(f"Error processing file: {e}")
    
    if extracted.strip():
        analysis_prompt = f"Please analyze the following content from the uploaded {file_type.split('/')[-1]} file:\n\n{extracted}"
        st.session_state.messages.append({"role": "user", "content": analysis_prompt})
        with st.chat_message("user"):
            st.markdown(analysis_prompt)
        # Call backend
        try:
            response = requests.post(f"{BACKEND_URL}/chat", json={"message": analysis_prompt, "session_id": st.session_state.current_session})
            if response.status_code == 200:
                ai_response = response.json()["response"]
                with st.chat_message("assistant"):
                    st.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                st.error("Error getting response")
        except:
            pass
    else:
        st.error("No text extracted from the file")

if "current_session" in st.session_state:
    prompt = st.chat_input("Ask a question...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call backend
        try:
            response = requests.post(f"{BACKEND_URL}/chat", json={"message": prompt, "session_id": st.session_state.current_session})
            if response.status_code == 200:
                ai_response = response.json()["response"]
                with st.chat_message("assistant"):
                    st.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                st.error("Error getting response")
        except:
            pass