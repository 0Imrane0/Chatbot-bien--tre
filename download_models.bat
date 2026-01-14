@echo off
:: ============================================================
:: DOWNLOAD MODELS - Télécharge les modèles BERT
:: ============================================================
:: Les modèles sont trop volumineux pour GitHub,
:: ce script les télécharge depuis Hugging Face
:: ============================================================

title Chatbot Bien-etre - Téléchargement des Modèles
color 0A

echo.
echo  ========================================================
echo.
echo       TELECHARGER LES MODELES
echo.
echo       BERT Fine-tune (650 MB)
echo.
echo  ========================================================
echo.

:: Se placer dans le répertoire du script
cd /d "%~dp0"

:: Vérifier si le virtual env existe
if exist ".venv\Scripts\activate.bat" (
    echo [INFO] Activation de l'environnement virtuel...
    call .venv\Scripts\activate.bat
) else (
    echo [WARN] Environnement virtuel non trouve, utilisation de Python global
)

echo.
echo [INFO] Téléchargement des modèles depuis Hugging Face...
echo [INFO] Cela peut prendre quelques minutes (500-650 MB)
echo.

:: Lancer le script de téléchargement
python download_models.py

if errorlevel 1 (
    echo.
    echo [ERREUR] Le téléchargement a échoué.
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo [SUCCESS] Les modèles sont téléchargés !
    echo.
    pause
)
