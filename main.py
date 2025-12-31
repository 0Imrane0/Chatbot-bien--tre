"""
🤖 Point d'Entrée Principal - Chatbot de Bien-être
==================================================

Ce module est le point d'entrée principal du projet.
Il permet de choisir entre :
- Interface Console ou Web (Streamlit)
- Approche 1 (Modèle pré-entraîné) ou Approche 2 (Modèle custom)
- Mode démo ou production

Auteur : Étudiant ENSA Berrechid
Module : Programmation Python et IA
"""

import sys
import os
import argparse
import subprocess

# Ajouter le chemin racine pour les imports
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)


def print_banner():
    """Affiche la bannière de bienvenue."""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          🧘 CHATBOT DE BIEN-ÊTRE ET D'HUMEUR 🧘              ║
║                                                               ║
║     Votre compagnon pour le suivi de votre santé mentale     ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   📚 Approche 1 : Modèle BERT pré-entraîné (recommandé)      ║
║   🔬 Approche 2 : Modèle Deep Learning custom (avancé)       ║
║                                                               ║
║   💻 Interface Console : Interaction dans le terminal        ║
║   🌐 Interface Web     : Application Streamlit moderne       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_menu():
    """Affiche le menu principal."""
    menu = """
╭─────────────────────────────────────────────────────────────╮
│                    🎯 MENU PRINCIPAL                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. 🖥️  Interface Console (Approche 1 - BERT)             │
│   2. 🌐  Interface Web Streamlit (Approche 1 - BERT)       │
│   3. 🔬  Interface Console (Approche 2 - Custom)           │
│   4. 📊  Mode Démo (test rapide)                           │
│   5. 📖  Aide et Documentation                             │
│   6. 🚪  Quitter                                           │
│                                                             │
╰─────────────────────────────────────────────────────────────╯
"""
    print(menu)


def run_console_approach1():
    """Lance l'interface console avec l'approche 1 (BERT)."""
    print("\n🚀 Lancement de l'interface console (BERT)...\n")
    
    try:
        # Importer et lancer le chatbot
        from src.approach1.chatbot import WellbeingChatbot
        
        chatbot = WellbeingChatbot()
        chatbot.start_conversation()
        
    except ImportError as e:
        print(f"\n❌ Erreur d'import : {e}")
        print("💡 Assurez-vous que toutes les dépendances sont installées.")
        print("   Exécutez : pip install -r requirements.txt")
    except Exception as e:
        print(f"\n❌ Erreur : {e}")


def run_streamlit():
    """Lance l'interface web Streamlit."""
    print("\n🌐 Lancement de l'interface Streamlit...")
    print("📝 L'application va s'ouvrir dans votre navigateur.\n")
    print("💡 Pour arrêter : appuyez sur Ctrl+C\n")
    
    streamlit_path = os.path.join(ROOT_DIR, "ui", "streamlit_ui.py")
    
    if not os.path.exists(streamlit_path):
        print(f"❌ Fichier non trouvé : {streamlit_path}")
        return
    
    try:
        # Lancer Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            streamlit_path,
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false"
        ], cwd=ROOT_DIR)
    except KeyboardInterrupt:
        print("\n\n👋 Interface Streamlit arrêtée.")
    except Exception as e:
        print(f"\n❌ Erreur lors du lancement de Streamlit : {e}")
        print("💡 Assurez-vous que Streamlit est installé : pip install streamlit")


def run_console_approach2():
    """Lance l'interface console avec l'approche 2 (Custom)."""
    print("\n🔬 Approche 2 (Modèle Custom)")
    print("─" * 50)
    print("\n⚠️  Cette approche n'est pas encore implémentée.")
    print("\n📋 Pour l'implémenter, il faut :")
    print("   1. Créer/collecter un dataset d'entraînement")
    print("   2. Construire l'architecture du réseau (LSTM/GRU)")
    print("   3. Entraîner le modèle")
    print("   4. Intégrer au chatbot")
    print("\n💡 Consultez le fichier docs/copilot-prompt.md pour le plan détaillé.")
    print("   (Phases 7-12 du plan)")
    input("\n[Appuyez sur Entrée pour revenir au menu]")


def run_demo():
    """Lance une démonstration rapide."""
    print("\n📊 MODE DÉMONSTRATION")
    print("═" * 50)
    
    try:
        from src.approach1.sentiment_analyzer import SentimentAnalyzer
        from src.approach1.mood_tracker import MoodTracker
        from src.approach1.response_generator import ResponseGenerator
        from src.approach1.mood_visualizer import MoodVisualizer
        
        print("\n🔄 Chargement des composants...")
        analyzer = SentimentAnalyzer()
        tracker = MoodTracker()
        generator = ResponseGenerator()
        visualizer = MoodVisualizer()
        
        print("✅ Tous les composants sont chargés !\n")
        
        # Phrases de test
        test_phrases = [
            ("Je suis vraiment heureux aujourd'hui ! 😊", "positif attendu"),
            ("Je me sens triste et fatigué...", "négatif attendu"),
            ("Il fait beau dehors.", "neutre attendu"),
            ("J'ai réussi mon examen, quelle joie !", "très positif attendu"),
            ("Je suis anxieux pour demain.", "négatif attendu")
        ]
        
        print("🧪 TEST D'ANALYSE DE SENTIMENT")
        print("─" * 50)
        
        for phrase, expected in test_phrases:
            result = analyzer.analyze(phrase)
            emoji = "✅" if expected.split()[0] in result['sentiment'].lower() else "⚠️"
            
            print(f"\n📝 \"{phrase}\"")
            print(f"   → {result['sentiment']} ({result['confidence']:.0%})")
            print(f"   {emoji} Attendu : {expected}")
            
            # Ajouter au tracker
            tracker.add_mood(
                text=phrase,
                sentiment=result['sentiment'],
                score=result['confidence'],
                predicted_class=result['predicted_class']
            )
        
        # Statistiques
        print("\n\n📈 STATISTIQUES DU TRACKER")
        print("─" * 50)
        stats = tracker.get_statistics()
        print(f"   • Messages analysés : {stats.get('total_entries', 0)}")
        print(f"   • Score moyen : {stats.get('mean_score', 0):.2%}")
        
        # Tendance
        trend = tracker.get_trend(days=7)
        print(f"   • Tendance : {trend.get('trend_direction', 0):+.2f}")
        
        # Visualisation
        print("\n\n🎨 VISUALISATION")
        print("─" * 50)
        visualizer.display_mood_dashboard(
            sentiment=result['sentiment'],
            score=result['confidence'],
            trend=trend.get('trend_direction', 0)
        )
        
        print("\n✅ Démonstration terminée !")
        
    except Exception as e:
        print(f"\n❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
    
    input("\n[Appuyez sur Entrée pour revenir au menu]")


def show_help():
    """Affiche l'aide et la documentation."""
    help_text = """
╔═══════════════════════════════════════════════════════════════╗
║                    📖 AIDE ET DOCUMENTATION                   ║
╚═══════════════════════════════════════════════════════════════╝

🎯 OBJECTIF DU PROJET
─────────────────────
Ce chatbot de bien-être analyse vos messages pour :
• Détecter votre sentiment (positif, négatif, neutre)
• Suivre l'évolution de votre humeur dans le temps
• Vous donner des conseils personnalisés
• Vous accompagner avec empathie

📂 STRUCTURE DU PROJET
─────────────────────
chatbot-bien-etre/
├── src/approach1/      # Code principal (BERT)
│   ├── sentiment_analyzer.py   # Analyse de sentiment
│   ├── mood_tracker.py         # Suivi d'humeur
│   ├── response_generator.py   # Génération de réponses
│   ├── mood_visualizer.py      # Visualisation
│   └── chatbot.py              # Chatbot intégré
├── ui/                 # Interfaces utilisateur
│   └── streamlit_ui.py        # Interface web
├── data/               # Données et historique
└── docs/               # Documentation

🎮 COMMANDES DANS LE CHAT
─────────────────────────
• /stats    - Voir les statistiques d'humeur
• /history  - Voir l'historique de conversation
• /help     - Afficher l'aide
• /clear    - Effacer l'écran
• /quit     - Quitter le chatbot

🔧 DÉPANNAGE
────────────
❌ "Module not found" → pip install -r requirements.txt
❌ "BERT loading error" → Vérifiez votre connexion internet
❌ "Streamlit error" → pip install streamlit plotly

📚 RESSOURCES
─────────────
• README.md           - Documentation principale
• GUIDE_UTILISATION.md - Guide utilisateur détaillé
• docs/copilot-prompt.md - Plan de développement

🆘 NUMÉROS D'URGENCE (France)
─────────────────────────────
• SOS Amitié : 09 72 39 40 50
• Fil Santé Jeunes : 0 800 235 236
• SOS Dépression : 01 45 22 44 44
"""
    print(help_text)
    input("\n[Appuyez sur Entrée pour revenir au menu]")


def parse_arguments():
    """Parse les arguments de ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Chatbot de Bien-être et d'Humeur",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python main.py              # Menu interactif
  python main.py --console    # Interface console directe
  python main.py --web        # Interface Streamlit directe
  python main.py --demo       # Mode démonstration
        """
    )
    
    parser.add_argument(
        '--console', '-c',
        action='store_true',
        help='Lancer directement l\'interface console'
    )
    
    parser.add_argument(
        '--web', '-w',
        action='store_true',
        help='Lancer directement l\'interface Streamlit'
    )
    
    parser.add_argument(
        '--demo', '-d',
        action='store_true',
        help='Lancer le mode démonstration'
    )
    
    parser.add_argument(
        '--approach', '-a',
        type=int,
        choices=[1, 2],
        default=1,
        help='Choisir l\'approche (1: BERT, 2: Custom)'
    )
    
    return parser.parse_args()


def main():
    """
    Fonction principale du programme.
    
    Gère le menu interactif ou les arguments de ligne de commande
    pour lancer les différentes interfaces du chatbot.
    """
    # Parser les arguments
    args = parse_arguments()
    
    # Mode direct via arguments
    if args.console:
        print_banner()
        if args.approach == 1:
            run_console_approach1()
        else:
            run_console_approach2()
        return
    
    if args.web:
        print_banner()
        run_streamlit()
        return
    
    if args.demo:
        print_banner()
        run_demo()
        return
    
    # Mode menu interactif
    while True:
        # Effacer l'écran (optionnel)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print_banner()
        print_menu()
        
        try:
            choice = input("Votre choix (1-6) : ").strip()
            
            if choice == '1':
                run_console_approach1()
            
            elif choice == '2':
                run_streamlit()
            
            elif choice == '3':
                run_console_approach2()
            
            elif choice == '4':
                run_demo()
            
            elif choice == '5':
                show_help()
            
            elif choice == '6':
                print("\n👋 Merci d'avoir utilisé le Chatbot de Bien-être !")
                print("🌟 Prenez soin de vous ! 💙\n")
                break
            
            else:
                print("\n⚠️ Choix invalide. Veuillez entrer un nombre entre 1 et 6.")
                input("[Appuyez sur Entrée pour continuer]")
        
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir !")
            break
        except Exception as e:
            print(f"\n❌ Erreur : {e}")
            input("[Appuyez sur Entrée pour continuer]")


# ============================================================
# POINT D'ENTRÉE
# ============================================================

if __name__ == "__main__":
    main()
