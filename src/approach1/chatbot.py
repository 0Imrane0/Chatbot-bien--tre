"""
Chatbot de Bien-être Principal - Approche 1 (Transfer Learning)
Intègre tous les modules pour créer une expérience conversationnelle complète

Modules intégrés :
- SentimentAnalyzer : Analyse du sentiment
- MoodTracker : Suivi de l'humeur
- ResponseGenerator : Génération de réponses
- MoodVisualizer : Visualisation de l'état

Auteur : Étudiant ENSA Berrechid  
Date : Décembre 2024
"""

import os
import sys
from datetime import datetime
from typing import Dict, List, Any

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from sentiment_analyzer import SentimentAnalyzer
from mood_tracker import MoodTracker
from response_generator import ResponseGenerator
from mood_visualizer import MoodVisualizer


class WellbeingChatbot:
    """
    Chatbot de bien-être complet
    
    Fonctionnalités :
    - Conversation naturelle et empathique
    - Analyse de sentiment en temps réel
    - Suivi de l'humeur sur le long terme
    - Conseils personnalisés
    - Détection de situations critiques
    - Visualisation de l'état émotionnel
    
    Architecture :
    Utilisateur → Chatbot → [Analyzer, Tracker, Generator, Visualizer] → Réponse
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialise le chatbot avec tous ses composants
        
        Args:
            config_path (str): Chemin vers config.yaml (optionnel)
        """
        print("\n" + "="*70)
        print("🤖 INITIALISATION DU CHATBOT DE BIEN-ÊTRE")
        print("="*70 + "\n")
        
        # Initialiser tous les modules
        print("📦 Chargement des modules...\n")
        
        # 1. Analyseur de sentiment (BERT)
        self.analyzer = SentimentAnalyzer(config_path)
        
        # 2. Tracker d'humeur (historique + tendances)
        self.tracker = MoodTracker("data/mood_history.json")
        
        # 3. Générateur de réponses (empathie + conseils)
        self.generator = ResponseGenerator()
        
        # 4. Visualiseur d'humeur (emojis + dashboards)
        self.visualizer = MoodVisualizer()
        
        # Contexte conversationnel
        self.conversation_history = []  # Historique de la session actuelle
        self.user_name = None  # Nom de l'utilisateur (optionnel)
        self.session_start = datetime.now()
        
        print("\n" + "="*70)
        print("✅ CHATBOT PRÊT À L'EMPLOI !")
        print("="*70 + "\n")
    
    def process_message(self, user_message: str) -> Dict[str, Any]:
        """
        Traite un message utilisateur de bout en bout
        
        Args:
            user_message (str): Message de l'utilisateur
        
        Returns:
            dict: Réponse complète avec tous les éléments
        
        Pipeline :
        1. Analyser le sentiment du message
        2. Enregistrer dans l'historique
        3. Calculer la tendance récente
        4. Générer une réponse appropriée
        5. Créer la visualisation
        6. Retourner le tout
        """
        # Étape 1 : ANALYSE DU SENTIMENT
        sentiment_result = self.analyzer.analyze(user_message)
        
        # Étape 2 : ENREGISTRER DANS L'HISTORIQUE
        self.tracker.add_mood(
            text=user_message,
            sentiment=sentiment_result['sentiment'],
            confidence=sentiment_result['confidence'],
            score=self._convert_to_score(sentiment_result['predicted_class'])
        )
        
        # Étape 3 : CALCULER LA TENDANCE (7 derniers jours)
        mood_trend = self.tracker.get_trend(7)
        
        # Étape 4 : GÉNÉRER LA RÉPONSE
        response_data = self.generator.generate_response(
            sentiment=sentiment_result['sentiment'],
            sentiment_detail=sentiment_result['sentiment_detail'],
            confidence=sentiment_result['confidence'],
            text=user_message,
            mood_trend=mood_trend
        )
        
        # Étape 5 : CRÉER LA VISUALISATION
        visualization = self.visualizer.display_mood_dashboard(
            sentiment=sentiment_result['sentiment_detail'],
            score=self._convert_to_score(sentiment_result['predicted_class']),
            confidence=sentiment_result['confidence'],
            trend=mood_trend.get('trend', None)
        )
        
        # Étape 6 : ASSEMBLER LA RÉPONSE COMPLÈTE
        full_response = {
            'sentiment_analysis': sentiment_result,
            'response': response_data,
            'visualization': visualization,
            'mood_trend': mood_trend,
            'timestamp': datetime.now().isoformat()
        }
        
        # Ajouter au contexte conversationnel
        self.conversation_history.append({
            'user_message': user_message,
            'response': full_response,
            'timestamp': datetime.now().isoformat()
        })
        
        return full_response
    
    def _convert_to_score(self, predicted_class: int) -> float:
        """
        Convertit la classe prédite (0-4) en score (-1 à 1)
        
        Args:
            predicted_class (int): Classe BERT (0=très négatif, 4=très positif)
        
        Returns:
            float: Score normalisé
        """
        mapping = {
            0: -1.0,   # Très négatif
            1: -0.5,   # Négatif
            2: 0.0,    # Neutre
            3: 0.5,    # Positif
            4: 1.0     # Très positif
        }
        return mapping.get(predicted_class, 0.0)
    
    def format_response(self, response_data: Dict[str, Any]) -> str:
        """
        Formate la réponse complète pour affichage
        
        Args:
            response_data (dict): Données de réponse du chatbot
        
        Returns:
            str: Réponse formatée prête à afficher
        """
        lines = []
        
        # En-tête avec emoji
        sentiment_detail = response_data['sentiment_analysis']['sentiment_detail']
        emoji = self.visualizer.mood_emojis.get(sentiment_detail, '😐')
        
        lines.append("\n" + "="*70)
        lines.append(f"  {emoji} RÉPONSE DU CHATBOT {emoji}")
        lines.append("="*70 + "\n")
        
        # Réponse principale du générateur
        formatted_response = self.generator.format_full_response(
            response_data['response']
        )
        lines.append(formatted_response)
        
        # Visualisation
        lines.append("\n" + "─"*70)
        lines.append(response_data['visualization'])
        
        return "\n".join(lines)
    
    def get_statistics(self) -> str:
        """
        Obtient les statistiques complètes de l'utilisateur
        
        Returns:
            str: Statistiques formatées
        """
        return self.tracker.get_summary()
    
    def start_conversation(self):
        """
        Démarre une conversation interactive en console
        
        Boucle principale :
        1. Afficher le prompt
        2. Lire le message utilisateur
        3. Traiter le message
        4. Afficher la réponse
        5. Répéter jusqu'à /quit
        
        Commandes spéciales :
        - /quit : Quitter
        - /stats : Afficher statistiques
        - /history : Voir l'historique
        - /help : Aide
        - /clear : Effacer l'écran
        """
        # Message d'accueil
        self._display_welcome()
        
        # Boucle conversationnelle
        while True:
            try:
                # Prompt utilisateur
                user_input = input("\n💬 Vous : ").strip()
                
                # Vérifier si c'est une commande spéciale
                if user_input.startswith('/'):
                    if not self._handle_command(user_input):
                        break  # /quit
                    continue
                
                # Vérifier si le message est vide
                if not user_input:
                    print("⚠️  Message vide. Tapez quelque chose ou /help pour aide.")
                    continue
                
                # Traiter le message
                print("\n🔄 Analyse en cours...")
                response_data = self.process_message(user_input)
                
                # Afficher la réponse
                formatted_response = self.format_response(response_data)
                print(formatted_response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Interruption détectée. Au revoir !")
                break
            except Exception as e:
                print(f"\n❌ Erreur : {e}")
                print("Réessayez ou tapez /quit pour quitter.")
    
    def _display_welcome(self):
        """
        Affiche le message d'accueil
        """
        welcome = f"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║           💙 BIENVENUE SUR TON CHATBOT DE BIEN-ÊTRE 💙            ║
║                                                                   ║
║   Je suis là pour t'écouter, te soutenir et suivre ton humeur.   ║
║   Parle-moi librement de ce que tu ressens ! 🌈                  ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  📝 Commandes disponibles :                                       ║
║     /stats   - Voir tes statistiques d'humeur                     ║
║     /history - Historique de la conversation                      ║
║     /help    - Afficher l'aide                                    ║
║     /clear   - Effacer l'écran                                    ║
║     /quit    - Quitter le chatbot                                 ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

Tape ton premier message ou /help pour plus d'informations ! 😊
"""
        print(welcome)
    
    def _handle_command(self, command: str) -> bool:
        """
        Gère les commandes spéciales
        
        Args:
            command (str): Commande (ex: /quit, /stats)
        
        Returns:
            bool: True pour continuer, False pour quitter
        """
        command = command.lower().strip()
        
        if command == '/quit' or command == '/q':
            self._display_goodbye()
            return False
        
        elif command == '/stats':
            print("\n" + "="*70)
            print(self.get_statistics())
            print("="*70)
        
        elif command == '/history':
            self._display_conversation_history()
        
        elif command == '/help':
            self._display_help()
        
        elif command == '/clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            self._display_welcome()
        
        else:
            print(f"⚠️  Commande inconnue : {command}")
            print("Tape /help pour voir les commandes disponibles.")
        
        return True
    
    def _display_conversation_history(self):
        """
        Affiche l'historique de la conversation actuelle
        """
        if not self.conversation_history:
            print("\n📭 Aucun message dans cette session.")
            return
        
        print("\n" + "="*70)
        print("📜 HISTORIQUE DE LA CONVERSATION")
        print("="*70 + "\n")
        
        for i, entry in enumerate(self.conversation_history, 1):
            timestamp = datetime.fromisoformat(entry['timestamp']).strftime('%H:%M:%S')
            sentiment = entry['response']['sentiment_analysis']['sentiment']
            
            print(f"{i}. [{timestamp}] {sentiment.upper()}")
            print(f"   Vous : {entry['user_message']}")
            print()
    
    def _display_help(self):
        """
        Affiche l'aide détaillée
        """
        help_text = """
╔═══════════════════════════════════════════════════════════════════╗
║                          📚 AIDE DU CHATBOT                       ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  🎯 Comment utiliser le chatbot :                                 ║
║                                                                   ║
║  1. Tape simplement ce que tu ressens                             ║
║  2. Le chatbot analyse ton sentiment                              ║
║  3. Il te répond avec empathie et conseils                        ║
║  4. Ton humeur est suivie dans le temps                           ║
║                                                                   ║
║  📝 Commandes disponibles :                                       ║
║                                                                   ║
║  /stats    - Affiche tes statistiques d'humeur complètes          ║
║  /history  - Montre l'historique de cette conversation            ║
║  /help     - Affiche cette aide                                   ║
║  /clear    - Efface l'écran                                       ║
║  /quit     - Quitte le chatbot                                    ║
║                                                                   ║
║  💡 Exemples de messages :                                        ║
║                                                                   ║
║  • "Je me sens triste aujourd'hui"                                ║
║  • "Je suis super content !"                                      ║
║  • "Je ne sais pas comment je me sens"                            ║
║  • "J'ai besoin de parler"                                        ║
║                                                                   ║
║  🆘 Aide d'urgence :                                              ║
║                                                                   ║
║  Si tu as des pensées suicidaires, contacte :                     ║
║  • France : 3114 (prévention suicide)                             ║
║  • Maroc : 0801000180 (SOS Maroc)                                 ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""
        print(help_text)
    
    def _display_goodbye(self):
        """
        Affiche le message de départ
        """
        # Calculer la durée de la session
        duration = datetime.now() - self.session_start
        minutes = int(duration.total_seconds() / 60)
        
        # Statistiques de session
        num_messages = len(self.conversation_history)
        
        goodbye = f"""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║                     👋 AU REVOIR ET PRENDS SOIN DE TOI ! 👋       ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  📊 Résumé de cette session :                                     ║
║     • Durée : {minutes} minutes                                       ║
║     • Messages échangés : {num_messages}                                       ║
║                                                                   ║
║  💙 N'oublie pas :                                                ║
║     • Tu n'es jamais seul(e)                                      ║
║     • Chaque jour est une nouvelle opportunité                    ║
║     • Prendre soin de soi est essentiel                           ║
║                                                                   ║
║  🌈 Reviens quand tu veux ! À bientôt ! 😊                        ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""
        print(goodbye)


# ============================================
# DÉMONSTRATION RAPIDE
# ============================================

def demo():
    """
    Démonstration rapide avec quelques messages
    """
    print("\n" + "="*70)
    print("🧪 DÉMONSTRATION RAPIDE DU CHATBOT")
    print("="*70 + "\n")
    
    # Créer le chatbot
    chatbot = WellbeingChatbot()
    
    # Messages de test
    test_messages = [
        "Je suis vraiment heureux aujourd'hui !",
        "Je me sens un peu triste...",
        "Ça va mieux maintenant, merci !"
    ]
    
    print("\n🔄 Simulation de conversation avec 3 messages...\n")
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n{'='*70}")
        print(f"MESSAGE {i}/3")
        print('='*70)
        print(f"\n💬 Utilisateur : {message}")
        
        # Traiter le message
        response_data = chatbot.process_message(message)
        
        # Afficher la réponse
        formatted = chatbot.format_response(response_data)
        print(formatted)
        
        input("\n⏸️  Appuie sur ENTRÉE pour continuer...")
    
    # Statistiques finales
    print("\n" + "="*70)
    print("📊 STATISTIQUES FINALES")
    print("="*70)
    print(chatbot.get_statistics())
    
    print("\n" + "="*70)
    print("✅ Démonstration terminée !")
    print("="*70)


# ============================================
# POINT D'ENTRÉE
# ============================================

def main():
    """
    Point d'entrée principal
    Lance le chatbot en mode interactif
    """
    chatbot = WellbeingChatbot()
    chatbot.start_conversation()


if __name__ == "__main__":
    # Pour démo rapide, décommenter :
    # demo()
    
    # Pour conversation interactive :
    main()
