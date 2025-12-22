# Personalized Learning Assistant Chatbot

A chatbot built with Streamlit (frontend), FastAPI (backend), SQLite (database), and OpenRouter API (AI responses) to help users learn programming topics.

## Features
- Chat interface for Q&A
- Message history storage
- Quiz mode based on chat history
- Rating system for responses

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Installation

### 1. Clone or Download the Project
```bash
git clone <repository-url>
cd "Streamlit Project"
```

### 2. Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root directory:
```bash
# Copy the example file
copy .env.example .env  # On Windows
# or
cp .env.example .env    # On macOS/Linux
```

Edit the `.env` file and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

## How to Start the Application

### Step 1: Start the Backend Server
Open a terminal in the project directory and run:
```bash
uvicorn backend:app --reload
```
The backend API will start on `http://localhost:8000`

### Step 2: Start the Frontend Application
Open a **new terminal** in the same project directory and run:
```bash
streamlit run app.py
```
The application will automatically open in your browser at `http://localhost:8501`

## Usage
1. Enter your user ID in the sidebar
2. Start chatting with the AI assistant
3. Use the "Load History" button to view previous conversations
4. Generate quizzes based on your chat history
5. Rate AI responses to improve future interactions

## Project Structure
```
Streamlit Project/
├── app.py              # Streamlit frontend
├── backend.py          # FastAPI backend
├── database.py         # Database operations
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .env.example       # Example environment file
└── learning_assistant.db  # SQLite database (auto-created)
```

## Troubleshooting

### Backend Not Running
- Ensure the backend is running on port 8000
- Check if port 8000 is already in use by another application
- Verify your virtual environment is activated

### API Key Issues
- Check that your `.env` file exists and contains a valid `OPENROUTER_API_KEY`
- Ensure there are no extra spaces or quotes around the API key
- Verify your API key is active and has credits

### Database Issues
- The database file `learning_assistant.db` is created automatically on first run
- If you encounter database errors, try deleting the database file and restarting

### Module Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify your virtual environment is activated
- Try reinstalling dependencies: `pip install --upgrade -r requirements.txt`

## Stopping the Application
1. Stop the Streamlit frontend: Press `Ctrl+C` in the frontend terminal
2. Stop the FastAPI backend: Press `Ctrl+C` in the backend terminal
3. Deactivate virtual environment: `deactivate`