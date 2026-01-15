@echo off
:: ============================================================
:: SETUP - Installation Initiale Chatbot Bien-etre IA
:: ============================================================
:: Créé l'environnement virtuel et installe toutes les dépendances
:: À exécuter UNE SEULE FOIS au premier lancement
:: ============================================================

title Chatbot Bien-etre - Installation Initiale
color 0A

echo.
echo  ========================================================
echo.
echo       INSTALLATION INITIALE
echo.
echo       Chatbot Bien-etre IA
echo.
echo  ========================================================
echo.

:: Se placer dans le répertoire du script
cd /d "%~dp0"

:: ÉTAPE 1 : Créer l'environnement virtuel
echo [ÉTAPE 1/4] Création de l'environnement virtuel...
echo.

if exist ".venv" (
    echo [INFO] Environnement virtuel existant detected
) else (
    echo [INFO] Création du dossier .venv...
    python -m venv .venv
    if errorlevel 1 (
        echo.
        echo [ERREUR] Impossible de créer l'environnement virtuel.
        echo.
        echo Assurez-vous que :
        echo   1. Python est installé (python --version)
        echo   2. Python est dans le PATH
        echo   3. Vous avez les droits d'administrateur
        echo.
        pause
        exit /b 1
    )
    echo [OK] Environnement virtuel créé
)

echo.
echo [ÉTAPE 2/4] Activation de l'environnement virtuel...
echo.

call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo [ERREUR] Impossible d'activer l'environnement virtuel
    pause
    exit /b 1
)

echo [OK] Environnement activé

echo.
echo [ÉTAPE 3/4] Mise à jour de pip...
echo.

python -m pip install --upgrade pip --quiet

if errorlevel 1 (
    echo [ERREUR] Impossible de mettre à jour pip
    pause
    exit /b 1
)

echo [OK] pip mis à jour

echo.
echo [ÉTAPE 4/4] Installation des dépendances...
echo.
echo Cela peut prendre 5-10 minutes...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERREUR] Impossible d'installer les dépendances.
    echo.
    echo Options :
    echo   1. Vérifier votre connexion Internet
    echo   2. Supprimer le dossier .venv et réessayer
    echo   3. Utiliser un proxy si vous êtes derrière un firewall
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] Dépendances installées

echo.
echo  ========================================================
echo.
echo       ✅ INSTALLATION TERMINÉE !
echo.
echo  ========================================================
echo.
echo Prochaines étapes :
echo.
echo   1. Télécharger les modèles BERT :
echo      → double-clique sur download_models.bat
echo      → ou : python download_models.py
echo.
echo   2. Lancer le chatbot :
echo      → double-clique sur launch_interface.bat
echo      → ou : streamlit run ui/streamlit_app.py --server.port 8502
echo.
echo.
echo Appuyez sur une touche pour fermer cette fenêtre...
pause
