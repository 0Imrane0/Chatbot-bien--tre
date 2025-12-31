@echo off
REM ===================================================================
REM Lanceur Streamlit - Interface Web du Chatbot de Bien-être
REM Active automatiquement l'environnement virtuel et lance Streamlit
REM ===================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║        🌐 LANCEMENT DE L'INTERFACE STREAMLIT 🌐              ║
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

echo 🚀 Lancement de Streamlit...
echo.
echo 📌 L'application va s'ouvrir dans votre navigateur
echo 📌 Pour arrêter: Fermez cette fenêtre ou appuyez sur Ctrl+C
echo.

REM Lancer Streamlit
python -m streamlit run ui\streamlit_ui.py --server.headless false

REM Si erreur
if errorlevel 1 (
    echo.
    echo ❌ Erreur lors du lancement de Streamlit
    echo.
    echo 💡 Assurez-vous que Streamlit est installé:
    echo    pip install streamlit plotly
    echo.
    pause
)
