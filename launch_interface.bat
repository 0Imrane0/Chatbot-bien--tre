@echo off
setlocal

REM Launch Streamlit UI for Chatbot Bien-etre (Approche 3)
REM Assumes Windows and a virtual environment in .venv

if not exist .venv (
    echo [INFO] Creating virtual environment .venv...
    python -m venv .venv
)

call .venv\Scripts\activate

if not exist .venv\Scripts\activate (
    echo [ERROR] Virtual environment not found. Please create .venv manually.
    pause
    exit /b 1
)

echo [INFO] Installing dependencies (if missing)...
pip install --upgrade pip >nul
pip install -r requirements.txt

set STREAMLIT_SERVER_PORT=8501
set STREAMLIT_SERVER_HEADLESS=true

streamlit run ui\streamlit_app.py

endlocal
pause
