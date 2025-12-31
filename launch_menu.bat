@echo off
REM ===================================================================
REM Lanceur Menu Principal - Chatbot de Bien-être
REM Active automatiquement l'environnement virtuel et affiche le menu
REM ===================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║          🎯 MENU PRINCIPAL DU CHATBOT 🎯                      ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Se placer dans le répertoire du projet
cd /d "%~dp0"

REM Vérifier si l'environnement virtuel existe
if not exist "venv\Scripts\activate.bat" (
    echo ❌ ERREUR: Environnement virtuel non trouvé!
    echo.
    echo 💡 Créez d'abord l'environnement virtuel:
    echo    python -m venv venv
    echo    venv\Scripts\activate
    echo    pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo 🔄 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo ✅ Environnement virtuel activé!
echo.

REM Lancer le menu principal
python main.py

REM Pause à la fin
echo.
pause
