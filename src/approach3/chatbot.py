"""
Chatbot de bien-être - Approche 3 Hybrid (BERT + Gemini)
=========================================================

Architecture Hybrid:
- BERT (Dictionary-based) → Analyse sentiment (100% précis, <100ms)
- Gemini API → Génère réponse personnalisée (contextuelle, ~2s)
- Fallback: Templates si Gemini échoue

Auteur: Étudiant ENSA Berrechid
Date: Janvier 2026
"""

import os
import sys
from typing import Dict, Optional
import json

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from approach3.sentiment_analyzer import SentimentAnalyzer
from approach1.mood_tracker import MoodTracker
from approach1.response_generator import ResponseGenerator
from gemini_wrapper import GeminiChatbot


class WellbeingChatbot:
    """
    Chatbot de bien-être utilisant Approche 3 Hybrid
    
    Architecture:
    - BERT fine-tuné (fallback: Dictionary) pour sentiment analysis
    - Gemini API pour génération de réponses personnalisées
    → Meilleure compréhension + Réponses contextuelles
    """
    
    def __init__(
        self, 
        user_id: str = 'user_default',
        use_gemini: bool = True,  # ✅ Activé par défaut - gemini-2.5-flash fonctionne!
        gemini_api_key: Optional[str] = 'AIzaSyA_KawZtJbvfRP_mtL4glFPIMWsFxGgi68'
    ):
        """
        Initialise le chatbot
        
        Args:
            user_id (str): ID de l'utilisateur pour suivre l'historique
            use_gemini (bool): Utiliser Gemini API ou fallback templates (False par défaut)
            gemini_api_key (str): Clé API Gemini (optionnel)
        """
        print("\n" + "=" * 60)
        print("🤖 CHATBOT BIEN-ÊTRE - BERT + Templates CBT")
        print("=" * 60)
        
        self.user_id = user_id
        self.use_gemini = use_gemini
        
        # Composants
        self.analyzer = SentimentAnalyzer()              # BERT / Dictionary
        self.tracker = MoodTracker(user_id)             # Suivi historique
        self.generator = ResponseGenerator()             # Fallback templates
        
        # Gemini API (optionnel)
        if use_gemini:
            try:
                # Utiliser la clé fournie (maintenant avec gemini-2.5-flash qui fonctionne)
                api_key = gemini_api_key
                self.gemini = GeminiChatbot(api_key)
                print("✅ Gemini API activé avec gemini-2.5-flash!")
            except Exception as e:
                print(f"⚠️  Gemini API non disponible: {e}")
                print("   Utilisation des templates de fallback")
                self.use_gemini = False
                self.gemini = None
        else:
            self.gemini = None
            print("ℹ️  Mode Templates (sans Gemini)")
        
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
        
        # ✅ ÉTAPE 1 : Analyser le sentiment (BERT / Dictionary)
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
        
        # ✅ ÉTAPE 4A : Générer réponse via Gemini (si disponible)
        if self.use_gemini and self.gemini:
            try:
                # Obtenir historique récent
                recent_history = self.tracker.get_mood_history(days=1)
                conversation_history = []
                for entry in recent_history[-5:]:  # 5 derniers messages
                    conversation_history.append({
                        'role': 'user',
                        'content': entry.get('text', ''),
                        'sentiment': entry.get('sentiment', '')
                    })
                
                # Appeler Gemini
                gemini_result = self.gemini.generate_response(
                    user_message=user_message,
                    sentiment=sentiment_result['sentiment'],
                    sentiment_detail=sentiment_result['sentiment_detail'],
                    confidence=sentiment_result['confidence'],
                    mood_trend=mood_trend,
                    conversation_history=conversation_history
                )
                
                # Utiliser aussi le générateur pour conseils et encouragement
                fallback_response = self.generator.generate_response(
                    sentiment=sentiment_result['sentiment'],
                    sentiment_detail=sentiment_result['sentiment_detail'],
                    confidence=sentiment_result['confidence'],
                    text=user_message,
                    mood_trend=mood_trend
                )
                
                # Merger les réponses
                response_data = {
                    'main_response': gemini_result['response'],  # De Gemini
                    'advice': fallback_response.get('advice', []),
                    'encouragement': fallback_response.get('encouragement', ''),
                    'is_crisis': gemini_result.get('is_crisis', False),
                    'emergency_resources': fallback_response.get('emergency_resources', []),
                    'sentiment': sentiment_result['sentiment'],
                    'confidence': sentiment_result['confidence'],
                    'gemini_used': True,
                    'gemini_time': gemini_result.get('generation_time', 0),
                    'fallback_used': gemini_result.get('fallback_used', False)
                }
                
            except Exception as e:
                print(f"⚠️ Erreur Gemini, utilisation fallback: {e}")
                # Fallback vers templates
                response_data = self.generator.generate_response(
                    sentiment=sentiment_result['sentiment'],
                    sentiment_detail=sentiment_result['sentiment_detail'],
                    confidence=sentiment_result['confidence'],
                    text=user_message,
                    mood_trend=mood_trend
                )
                response_data['gemini_used'] = False
                response_data['fallback_used'] = True
        
        # ✅ ÉTAPE 4B : Utiliser templates (si Gemini désactivé)
        else:
            response_data = self.generator.generate_response(
                sentiment=sentiment_result['sentiment'],
                sentiment_detail=sentiment_result['sentiment_detail'],
                confidence=sentiment_result['confidence'],
                text=user_message,
                mood_trend=mood_trend
            )
            response_data['gemini_used'] = False
        
        # ✅ ÉTAPE 5 : Ajouter métadonnées
        response_data['approach'] = 'hybrid-bert-gemini' if self.use_gemini else 'bert-templates'
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
