@echo off
:: ============================================================
:: LAUNCHER - Interface Web Chatbot Bien-etre IA
:: ============================================================
:: Lance directement l'interface Streamlit du chatbot
:: avec le modele BERT fine-tune (Approche 3)
:: ============================================================

title Chatbot Bien-etre IA - Interface Web
color 0A

echo.
echo  ========================================================
echo.
echo       CHATBOT BIEN-ETRE IA - INTERFACE WEB
echo.
echo       BERT Fine-tune + CBT
echo       Precision: 85%%
echo.
echo  ========================================================
echo.

:: Se placer dans le repertoire du script
cd /d "%~dp0"

:: VERIFICATION 1 : Vérifier que l'environnement virtuel existe
if not exist ".venv\Scripts\activate.bat" (
    echo.
    echo [ERREUR] Environnement virtuel non trouve!
    echo.
    echo ❌ Le dossier .venv n'existe pas.
    echo.
    echo SOLUTION : Double-clique sur setup.bat pour installer
    echo            les dépendances (une seule fois)
    echo.
    echo Puis relance launch_interface.bat
    echo.
    pause
    exit /b 1
)

:: VERIFICATION 2 : Vérifier que requirements.txt existe
if not exist "requirements.txt" (
    echo [ERREUR] requirements.txt non trouve!
    pause
    exit /b 1
)

echo [INFO] Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo [ERREUR] Impossible d'activer l'environnement virtuel
    pause
    exit /b 1
)

:: VERIFICATION 3 : Vérifier que streamlit est installé
echo [INFO] Vérification de streamlit...
python -m pip show streamlit >nul 2>&1

if errorlevel 1 (
    echo.
    echo [ERREUR] Streamlit n'est pas installé!
    echo.
    echo Les dépendances n'ont pas été correctement installées.
    echo.
    echo SOLUTION : Double-clique sur setup.bat
    echo.
    pause
    exit /b 1
)

echo.
echo [INFO] Demarrage de l'interface web Streamlit...
echo [INFO] L'interface s'ouvrira dans votre navigateur
echo [INFO] Veuillez patienter ~5 secondes pour le chargement du modele BERT
echo.
echo  ========================================================
echo.
echo       URL: http://localhost:8502
echo.
echo       Pour arreter: Appuyez sur Ctrl+C
echo.
echo  ========================================================
echo.

:: Lancer Streamlit sur le port 8502 et ouvrir le navigateur
python -m streamlit run ui/streamlit_app.py --server.port 8502 --browser.gatherUsageStats false

:: Si Streamlit s'arrete
echo.
echo [INFO] Interface fermee.
pause
