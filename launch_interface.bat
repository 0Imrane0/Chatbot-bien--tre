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

:: Verifier si le virtual env existe
if exist ".venv\Scripts\activate.bat" (
    echo [INFO] Activation de l'environnement virtuel...
    call .venv\Scripts\activate.bat
) else (
    echo [WARN] Environnement virtuel non trouve, utilisation de Python global
)

echo.
echo [INFO] Demarrage de l'interface web Streamlit...
echo [INFO] L'interface s'ouvrira dans votre navigateur
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
