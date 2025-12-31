@echo off
REM ===================================================================
REM Lanceur Tests - Chatbot de Bien-être
REM Active l'environnement virtuel et exécute tous les tests
REM ===================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║            🧪 EXÉCUTION DES TESTS 🧪                          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Se placer dans le répertoire du projet
cd /d "%~dp0"

REM Vérifier si l'environnement virtuel existe
if not exist "venv\Scripts\activate.bat" (
    echo ❌ ERREUR: Environnement virtuel non trouvé!
    pause
    exit /b 1
)

echo 🔄 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo ✅ Environnement virtuel activé!
echo.

echo 🧪 Exécution des tests unitaires...
echo.

REM Exécuter les tests
python tests\test_approach1.py

REM Pause à la fin
echo.
echo ✅ Tests terminés!
pause
