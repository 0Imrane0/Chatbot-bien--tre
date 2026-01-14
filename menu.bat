@echo off
REM ================================================================
REM   CHATBOT BIEN-ETRE - MENU PRINCIPAL
REM   Sélectionne l'action que tu veux faire
REM ================================================================

chcp 65001 >nul
cls
color 0A

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║         🤖 CHATBOT DE BIEN-ETRE - MENU PRINCIPAL          ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

:menu
echo.
echo 📋 MENU PRINCIPAL:
echo.
echo 1) 🤖 Lancer le CHATBOT (Approche 1 - Feature Extraction)
echo 2) 🤖 Lancer le CHATBOT (Approche 3 - Fine-tuning)
echo 3) 📊 Comparer les Approches 1 vs 3
echo 4) 🧠 Tester le MODULE CBT (Distorsions Cognitives)
echo 5) 🧪 Tester le Module CBT Rapidement
echo 6) 📄 Voir la Documentation
echo 7) 🏃 Quitter
echo.

set /p choice="Choisis une option (1-7): "

if "%choice%"=="1" goto chatbot1
if "%choice%"=="2" goto chatbot3
if "%choice%"=="3" goto compare
if "%choice%"=="4" goto test_cbt_full
if "%choice%"=="5" goto test_cbt_quick
if "%choice%"=="6" goto docs
if "%choice%"=="7" goto quit

echo ❌ Option invalide. Réessaie.
goto menu

:chatbot1
cls
echo 🤖 Lancement du Chatbot Approche 1...
echo.
python src/approach1/chatbot.py
pause
cls
goto menu

:chatbot3
cls
echo 🤖 Lancement du Chatbot Approche 3...
echo.
python src/approach3/chatbot.py
pause
cls
goto menu

:compare
cls
echo 📊 Comparaison Approche 1 vs 3...
echo.
python compare_approaches.py
pause
cls
goto menu

:test_cbt_full
cls
echo 🧠 Tests Complets du Module CBT...
echo.
python test_cbt.py
pause
cls
goto menu

:test_cbt_quick
cls
echo 🧪 Test Rapide Module CBT...
echo.
python quick_test_cbt.py
pause
cls
goto menu

:docs
cls
echo 📄 DOCUMENTATION DISPONIBLE:
echo.
echo ✅ docs/README.md                      - Guide Principal
echo ✅ docs/RAPPORT_FINAL.md               - Rapport Complet
echo ✅ docs/CBT_README.md                  - Guide CBT
echo ✅ docs/CBT_INTEGRATION_SUMMARY.md     - Résumé CBT
echo ✅ docs/COMPARISON_IDEAS.md            - Idées Comparaisons
echo ✅ docs/cbt-integration-guide.md       - Guide Théorique CBT
echo.
echo 💡 REMARQUE: Ouvre ces fichiers avec un éditeur texte ou Markdown
echo.
pause
cls
goto menu

:quit
cls
echo.
echo 👋 Au revoir! À bientôt pour tester le chatbot! 
echo.
pause
exit /b 0
