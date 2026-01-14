"""
Chatbot de bien-être - Approche 3 (Fine-tuning BERT)
Réutilise les composants d'Approche 1 (mood_tracker, response_generator)
avec le nouvel analyseur fine-tuné
"""

import os
import sys
from typing import Dict
import json

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from approach3.sentiment_analyzer import SentimentAnalyzer
from approach1.mood_tracker import MoodTracker
from approach1.response_generator import ResponseGenerator


class WellbeingChatbot:
    """
    Chatbot de bien-être utilisant Approche 3 (Fine-tuning BERT)
    
    Différence avec Approche 1:
    - Utilise BERT fine-tuné au lieu de Feature Extraction
    → Meilleure compréhension des sentiments bien-être
    """
    
    def __init__(self, user_id: str = 'user_default'):
        """
        Initialise le chatbot
        
        Args:
            user_id (str): ID de l'utilisateur pour suivre l'historique
        """
        print("\n" + "=" * 60)
        print("🤖 CHATBOT DE BIEN-ÊTRE - Approche 3 (Fine-tuning BERT)")
        print("=" * 60)
        
        self.user_id = user_id
        
        # Composants
        self.analyzer = SentimentAnalyzer()              # Fine-tuned BERT
        self.tracker = MoodTracker(user_id)             # Suivi historique
        self.generator = ResponseGenerator()             # Réponses empathiques
        
        print("✅ Chatbot initialisé et prêt!")
        print("-" * 60)
    
    def process_message(self, user_message: str) -> Dict:
        """
        Traite un message utilisateur et génère une réponse
        
        Args:
            user_message (str): Message de l'utilisateur
            
        Returns:
            dict: Réponse du chatbot avec contexte
        """
        
        # ✅ ÉTAPE 1 : Analyser le sentiment (BERT fine-tuné)
        sentiment_result = self.analyzer.analyze(user_message)
        
        # ✅ ÉTAPE 2 : Enregistrer dans l'historique
        self.tracker.add_mood(
            text=user_message,
            sentiment=sentiment_result['sentiment'],
            confidence=sentiment_result['confidence'],
            score=sentiment_result['confidence']
        )
        
        # ✅ ÉTAPE 3 : Récupérer la tendance
        mood_trend = self.tracker.get_trend(days=7)
        
        # ✅ ÉTAPE 4 : Générer une réponse
        response_data = self.generator.generate_response(
            sentiment=sentiment_result['sentiment'],
            sentiment_detail=sentiment_result['sentiment_detail'],
            confidence=sentiment_result['confidence'],
            text=user_message,
            mood_trend=mood_trend
        )
        
        # ✅ ÉTAPE 5 : Ajouter le contexte de Fine-tuning
        response_data['approach'] = 'fine-tuning'
        response_data['sentiment_detail'] = sentiment_result['sentiment_detail']
        response_data['all_scores'] = sentiment_result['scores']
        
        return response_data
    
    def get_statistics(self) -> Dict:
        """Récupère les statistiques de l'utilisateur"""
        return self.tracker.get_statistics()
    
    def get_mood_history(self, days: int = 7) -> list:
        """Récupère l'historique d'humeur"""
        return self.tracker.get_mood_history(days)
    
    def start_conversation(self):
        """Lance une conversation interactive"""
        print("\n💬 CONVERSATION INTERACTIVE")
        print("Tapez 'quit' pour quitter, 'stats' pour les statistiques")
        print("-" * 60)
        
        while True:
            user_input = input("\nToi : ").strip()
            
            if user_input.lower() == 'quit':
                print("\n👋 Au revoir! Prends soin de toi.")
                break
            
            if user_input.lower() == 'stats':
                stats = self.get_statistics()
                print(f"\n📊 Statistiques:")
                print(f"   Sentiment moyen: {stats.get('average_sentiment', 'N/A')}")
                print(f"   Nombre d'interactions: {stats.get('total_interactions', 0)}")
                continue
            
            if not user_input:
                continue
            
            # Traiter le message
            response = self.process_message(user_input)
            
            # Afficher la réponse
            print(f"\n🤖 Chatbot : {response['main_response']}")
            
            if response.get('advice'):
                print(f"\n💡 Conseils:")
                for advice in response['advice']:
                    print(f"   • {advice}")
            
            if response.get('sentiment_detail'):
                print(f"\n📊 Sentiment détecté : {response['sentiment_detail']} ({response.get('confidence', 0):.0%})")


# ============================================================================
# Test
# ============================================================================

if __name__ == '__main__':
    try:
        chatbot = WellbeingChatbot()
        chatbot.start_conversation()
    except Exception as e:
        print(f"❌ Erreur: {e}")
