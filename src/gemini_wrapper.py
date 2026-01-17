"""
🤖 Gemini API Wrapper - Génération de Réponses Personnalisées
==============================================================

Utilise Gemini 1.5 Flash pour générer des réponses empathiques et personnalisées
basées sur le sentiment détecté par BERT.

Architecture Hybrid:
- BERT (Approach 3) → Analyse sentiment (100% précis, < 100ms)
- Gemini API → Génère réponse personnalisée (contextuelle, ~2s)

Auteur: Étudiant ENSA Berrechid
Date: Janvier 2026
"""

from google import genai
from google.genai import types
from typing import Dict, List, Optional
import json
from datetime import datetime

class GeminiChatbot:
    """
    Wrapper pour Gemini API - Génération de réponses thérapeutiques
    """
    
    def __init__(self, api_key: str):
        """
        Initialise le client Gemini
        
        Args:
            api_key: Clé API Google Gemini
        """
        self.api_key = api_key
        
        # Nouveau client Gemini (nouvelle bibliothèque)
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = 'gemini-2.5-flash'  # Modèle rapide et performant
        
        # Configuration de génération
        self.generation_config = types.GenerateContentConfig(
            temperature=0.8,  # Créativité modérée
            top_p=0.95,
            top_k=40,
            max_output_tokens=500,
        )
        
        # Prompt système - Guide le comportement de Gemini
        self.system_prompt = self._create_system_prompt()
        
        print("✅ Gemini API configuré et prêt (nouvelle version)!")
    
    def _create_system_prompt(self) -> str:
        """
        Crée le prompt système qui guide Gemini
        
        Returns:
            str: Prompt système complet
        """
        return """Tu es un assistant de bien-être empathique et bienveillant. Ton rôle est d'écouter, comprendre et soutenir les utilisateurs dans leurs émotions.

RÈGLES IMPORTANTES:
1. Réponds TOUJOURS en français
2. Sois empathique et chaleureux
3. Adapte ton ton au sentiment détecté:
   - Très négatif/Crise: Sérieux, préoccupé, propose aide immédiate
   - Négatif: Compréhensif, encourageant, suggère des actions
   - Neutre: Amical, ouvert, pose des questions pour comprendre
   - Positif: Enthousiaste, partage la joie
   - Très positif: Célèbre avec l'utilisateur
4. Utilise des emojis appropriés (maximum 2-3)
5. Garde les réponses concises (2-4 phrases)
6. Ne donne JAMAIS de diagnostic médical
7. Si crise détectée, oriente vers aide professionnelle

CONTEXTE:
Tu as accès à:
- Le message de l'utilisateur
- Le sentiment détecté par IA (très négatif, négatif, neutre, positif, très positif)
- La confiance de la détection (0-100%)
- L'historique récent de l'humeur

Génère une réponse personnalisée qui montre que tu comprends et que tu es là pour aider."""
    
    def generate_response(
        self,
        user_message: str,
        sentiment: str,
        sentiment_detail: str,
        confidence: float,
        mood_trend: Optional[Dict] = None,
        conversation_history: Optional[List[Dict]] = None
    ) -> Dict:
        """
        Génère une réponse personnalisée via Gemini
        
        Args:
            user_message: Message de l'utilisateur
            sentiment: Sentiment général (positif/négatif/neutre)
            sentiment_detail: Sentiment détaillé (très négatif, négatif, etc.)
            confidence: Confiance de la détection (0-1)
            mood_trend: Tendance d'humeur sur 7 jours (optionnel)
            conversation_history: Historique récent (optionnel)
        
        Returns:
            dict: {
                'response': str,           # Réponse générée
                'is_crisis': bool,         # Crise détectée ?
                'fallback_used': bool,     # Fallback utilisé ?
                'generation_time': float   # Temps de génération
            }
        """
        start_time = datetime.now()
        
        # Détecter situation de crise
        is_crisis = self._is_crisis(user_message, sentiment_detail)
        
        # Construire le contexte pour Gemini
        context = self._build_context(
            user_message=user_message,
            sentiment=sentiment,
            sentiment_detail=sentiment_detail,
            confidence=confidence,
            mood_trend=mood_trend,
            conversation_history=conversation_history,
            is_crisis=is_crisis
        )
        
        try:
            # Appel à Gemini avec la NOUVELLE API
            full_prompt = f"{self.system_prompt}\n\n{context}"
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config=self.generation_config
            )
            
            generated_text = response.text.strip()
            
            # Temps de génération
            generation_time = (datetime.now() - start_time).total_seconds()
            
            return {
                'response': generated_text,
                'is_crisis': is_crisis,
                'fallback_used': False,
                'generation_time': generation_time,
                'sentiment_used': sentiment_detail,
                'confidence': confidence
            }
            
        except Exception as e:
            print(f"⚠️ Erreur Gemini API: {e}")
            
            # Fallback: Utiliser un template simple
            fallback_response = self._get_fallback_response(sentiment_detail, is_crisis)
            
            generation_time = (datetime.now() - start_time).total_seconds()
            
            return {
                'response': fallback_response,
                'is_crisis': is_crisis,
                'fallback_used': True,
                'generation_time': generation_time,
                'error': str(e)
            }
    
    def _build_context(
        self,
        user_message: str,
        sentiment: str,
        sentiment_detail: str,
        confidence: float,
        mood_trend: Optional[Dict],
        conversation_history: Optional[List[Dict]],
        is_crisis: bool
    ) -> str:
        """
        Construit le contexte pour Gemini
        
        Returns:
            str: Contexte formaté
        """
        context_parts = []
        
        # Message utilisateur
        context_parts.append(f"MESSAGE UTILISATEUR:\n\"{user_message}\"")
        
        # Sentiment détecté
        context_parts.append(f"\nSENTIMENT DÉTECTÉ:")
        context_parts.append(f"- Catégorie: {sentiment_detail}")
        context_parts.append(f"- Confiance: {confidence*100:.0f}%")
        
        if is_crisis:
            context_parts.append("- ⚠️ ALERTE CRISE: Mots-clés critiques détectés (suicide, etc.)")
        
        # Tendance d'humeur
        if mood_trend:
            trend_value = mood_trend.get('trend', 0)
            if trend_value > 0.2:
                context_parts.append(f"\nTENDANCE: Amélioration récente (+{trend_value:.1f})")
            elif trend_value < -0.2:
                context_parts.append(f"\nTENDANCE: Détérioration récente ({trend_value:.1f})")
            else:
                context_parts.append(f"\nTENDANCE: Stable")
        
        # Historique récent (optionnel)
        if conversation_history and len(conversation_history) > 0:
            context_parts.append("\nHISTORIQUE RÉCENT:")
            for msg in conversation_history[-3:]:  # 3 derniers messages
                role = "Utilisateur" if msg.get('role') == 'user' else "Bot"
                content = msg.get('content', '')[:100]  # Limiter à 100 chars
                context_parts.append(f"- {role}: {content}")
        
        # Instruction de génération
        context_parts.append("\nGÉNÈRE UNE RÉPONSE:")
        if is_crisis:
            context_parts.append("- Montre une préoccupation immédiate")
            context_parts.append("- Propose des ressources d'urgence")
            context_parts.append("- Encourage à chercher aide professionnelle")
        else:
            context_parts.append("- Empathique et personnalisée")
            context_parts.append("- Adaptée au sentiment détecté")
            context_parts.append("- Concise (2-4 phrases)")
        
        return "\n".join(context_parts)
    
    def _is_crisis(self, message: str, sentiment: str) -> bool:
        """
        Détecte si c'est une situation de crise
        
        Args:
            message: Message utilisateur
            sentiment: Sentiment détecté
        
        Returns:
            bool: True si crise détectée
        """
        crisis_keywords = [
            'suicide', 'suicider', 'tuer', 'mourir', 'en finir',
            'disparaitre', 'plus rien', 'sans espoir', 'ne peux plus',
            'abandonner', 'partir', 'fin'
        ]
        
        message_lower = message.lower()
        
        # Vérifier mots-clés
        for keyword in crisis_keywords:
            if keyword in message_lower:
                return True
        
        # Si très négatif avec forte confiance
        if sentiment == 'très négatif':
            return True
        
        return False
    
    def _get_fallback_response(self, sentiment: str, is_crisis: bool) -> str:
        """
        Génère une réponse de fallback si Gemini échoue
        
        Args:
            sentiment: Sentiment détecté
            is_crisis: Si crise détectée
        
        Returns:
            str: Réponse de fallback
        """
        if is_crisis:
            return ("Je suis vraiment inquiet pour toi. 😟 "
                    "S'il te plaît, contacte immédiatement une ligne d'urgence. "
                    "Tu n'es pas seul(e), et il y a des gens qui peuvent t'aider. 🆘")
        
        fallback_templates = {
            'très négatif': "Je vois que tu traverses une période très difficile. 💙 Je suis là pour t'écouter.",
            'négatif': "Je comprends que ce soit dur en ce moment. 😔 Veux-tu en parler ?",
            'neutre': "Je suis là pour toi. Comment te sens-tu vraiment ? 🤗",
            'positif': "C'est bien de te voir dans un meilleur état ! 😊 Qu'est-ce qui te rend heureux ?",
            'très positif': "Wow, c'est génial ! 🎉 Je suis content pour toi !"
        }
        
        return fallback_templates.get(sentiment, "Je suis là pour t'écouter. 💙")
    
    def get_cbt_analysis(
        self,
        user_message: str,
        sentiment: str
    ) -> Dict:
        """
        Analyse CBT via Gemini (optionnel)
        
        Args:
            user_message: Message utilisateur
            sentiment: Sentiment détecté
        
        Returns:
            dict: Analyse CBT
        """
        if sentiment not in ['négatif', 'très négatif']:
            return {'distortions': [], 'restructuring': None}
        
        cbt_prompt = f"""{self.system_prompt}

MESSAGE UTILISATEUR:
"{user_message}"

TÂCHE: Identifie les distorsions cognitives présentes (catastrophisation, tout-ou-rien, surgénéralisation, lecture de pensées, raisonnement émotionnel).

Réponds en JSON:
{{
    "distortions": ["nom distorsion 1", "nom distorsion 2"],
    "restructuring": "Pensée alternative plus équilibrée"
}}
"""
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=cbt_prompt,
                config=self.generation_config
            )
            result_text = response.text.strip()
            
            # Parser JSON
            if '```json' in result_text:
                result_text = result_text.split('```json')[1].split('```')[0].strip()
            elif '```' in result_text:
                result_text = result_text.split('```')[1].split('```')[0].strip()
            
            cbt_data = json.loads(result_text)
            return cbt_data
            
        except Exception as e:
            print(f"⚠️ Erreur CBT Analysis: {e}")
            return {'distortions': [], 'restructuring': None}


# ============================================================
# FONCTION HELPER POUR TESTER
# ============================================================

def test_gemini():
    """Test rapide de Gemini API"""
    api_key = "AIzaSyA_KawZtJbvfRP_mtL4glFPIMWsFxGgi68"
    
    gemini = GeminiChatbot(api_key)
    
    test_cases = [
        ("Je me sens complètement nul", "très négatif", 0.95),
        ("Je suis un peu stressé", "négatif", 0.85),
        ("J'ai réussi mon examen!", "très positif", 0.95)
    ]
    
    print("\n" + "="*60)
    print("🧪 TEST GEMINI API")
    print("="*60)
    
    for msg, sentiment, confidence in test_cases:
        print(f"\n📝 Message: '{msg}'")
        print(f"   Sentiment: {sentiment} ({confidence*100:.0f}%)")
        
        result = gemini.generate_response(
            user_message=msg,
            sentiment=sentiment.split()[0] if ' ' in sentiment else sentiment,
            sentiment_detail=sentiment,
            confidence=confidence
        )
        
        print(f"   🤖 Réponse: {result['response']}")
        print(f"   ⏱️  Temps: {result['generation_time']:.2f}s")
        print(f"   🔄 Fallback: {result['fallback_used']}")


if __name__ == "__main__":
    test_gemini()
