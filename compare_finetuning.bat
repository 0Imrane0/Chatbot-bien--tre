@echo off
REM ===================================================================
REM Comparaison Feature Extraction vs Fine-tuning
REM ===================================================================

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║    📊 COMPARAISON FEATURE EXTRACTION VS FINE-TUNING 📊        ║
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

echo 🚀 Lancement de la comparaison...
echo.
echo ⚠️  Note: Le fine-tuning peut prendre quelques minutes la première fois
echo.

REM Exécuter le script de comparaison
python compare_approaches.py

REM Pause à la fin
echo.
pause
