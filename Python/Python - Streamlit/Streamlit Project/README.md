# Personalized Learning Assistant Chatbot

A chatbot built with Streamlit (frontend), FastAPI (backend), SQLite (database), and OpenRouter API (AI responses) to help users learn programming topics.

## Features
- Chat interface for Q&A
- Message history storage
- Quiz mode based on chat history
- Rating system for responses

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment: Create `.env` file with `OPENROUTER_API_KEY=your_key_here`
3. Run backend: `uvicorn backend:app --reload`
4. Run frontend: `streamlit run app.py`

## Usage
- Enter user ID and start chatting.
- Use buttons to load history, generate quizzes, or rate responses.

## Troubleshooting
- Ensure backend is running on port 8000.
- Check API key validity.
- Database file `learning_assistant.db` is created automatically.