@echo off
REM ===================================================================
REM Lanceur Console - Interface Terminal du Chatbot de Bien-être
REM Active automatiquement l'environnement virtuel et lance le chatbot
REM ===================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║        💻 LANCEMENT DE L'INTERFACE CONSOLE 💻                ║
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

echo 🚀 Lancement du chatbot en mode console...
echo.

REM Lancer le chatbot en mode console
python main.py --console

REM Pause à la fin
echo.
pause
