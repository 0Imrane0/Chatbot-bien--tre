@echo off
REM Script de lancement du Chatbot de Bien-être
REM Windows Batch Script

echo ============================================================
echo    LANCEMENT DU CHATBOT DE BIEN-ÊTRE
echo ============================================================
echo.

REM Aller dans le bon répertoire
cd /d "%~dp0src\approach1"

REM Activer l'environnement virtuel et lancer le chatbot
..\..\venv\Scripts\python.exe chatbot.py

pause
