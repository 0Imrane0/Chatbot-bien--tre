@echo off
REM ===================================================================
REM Lanceur Démo - Chatbot de Bien-être
REM Active l'environnement virtuel et lance la démonstration rapide
REM ===================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║            📊 MODE DÉMONSTRATION 📊                           ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Se placer dans le répertoire du projet
cd /d "%~dp0"

REM Vérifier si l'environnement virtuel existe
if not exist "venv\Scripts\activate.bat" (
    echo ❌ ERREUR: Environnement virtuel non trouvé!
    echo.
    pause
    exit /b 1
)

echo 🔄 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo ✅ Environnement virtuel activé!
echo.

echo 🎬 Lancement de la démonstration...
echo.

REM Lancer le mode démo
python main.py --demo

REM Pause à la fin
echo.
pause
