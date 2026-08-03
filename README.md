# Intern Calculator Task

This workspace contains a simple FastAPI backend and an HTML frontend scaffold.

## Run the backend

1. Create and activate a Python virtual environment:
   - Windows PowerShell:
     `python -m venv .venv`
     `./.venv/Scripts/Activate.ps1`
   - macOS/Linux:
     `python3 -m venv .venv`
     `source .venv/bin/activate`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Start the server:
   `uvicorn backend.main:app --reload`
4. Open the frontend in your browser via the server:
   `http://127.0.0.1:8000`
