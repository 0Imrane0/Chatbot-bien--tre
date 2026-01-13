"""
Module Générateur de Réponses - Approche 1
Génère des réponses empathiques et des conseils personnalisés selon :
- Le sentiment actuel
- L'historique d'humeur
- Le contexte de la conversation

Auteur : Étudiant ENSA Berrechid
Date : Décembre 2024
"""

import random
from typing import Dict, List, Any


class ResponseGenerator:
    """
    Générateur de réponses empathiques et conseils personnalisés
    
    Fonctionnalités :
    - Templates de réponses par sentiment
    - Adaptation selon l'historique
    - Base de conseils de bien-être
    - Détection de situations critiques
    - Éviter les répétitions
    
    Stratégie :
    1. Analyser le sentiment actuel
    2. Vérifier l'historique (tendance)
    3. Choisir un template approprié
    4. Personnaliser avec le contexte
    5. Ajouter des conseils pertinents
    """
    
    def __init__(self):
        """
        Initialise le générateur avec les templates et la base de conseils
        """
        print("🔧 Initialisation du Générateur de Réponses...")
        
        # ============================================
        # DÉTECTION DE CONVERSATIONS NATURELLES
        # ============================================
        
        # Salutations reconnues
        self.greetings = [
            'salut', 'hello', 'hi', 'bonjour', 'bonsoir', 'coucou',
            'hey', 'yo', 'wesh', 'cc', 'slt', 'bjr', 'bsr',
            'bonne journée', 'bonne soirée', 'good morning', 
            'good evening', 'good afternoon'
        ]
        
        # Réponses naturelles aux salutations
        self.greeting_responses = [
            "Salut ! 👋 Comment tu te sens aujourd'hui ?",
            "Hey ! 😊 Comment vas-tu ? Raconte-moi ta journée !",
            "Bonjour ! 🌟 Comment te sens-tu en ce moment ?",
            "Coucou ! 💬 Qu'est-ce qui t'amène aujourd'hui ?",
            "Hello ! 👋 Je suis là pour toi. Comment ça va ?",
            "Salut ! 😊 Ça me fait plaisir de te voir ! Comment tu vas ?"
        ]
        
        # Questions sur le bot
        self.bot_questions = [
            'qui es-tu', 'tu es qui', 'c\'est quoi', 'comment tu marches',
            'qui t\'a créé', 'comment tu fonctionne', 'what are you',
            'tu fais quoi', 'quel est ton nom', 'ton nom'
        ]
        
        # Réponses sur le bot
        self.bot_responses = [
            "Je suis ton assistant de bien-être ! 🤖💙 Je suis là pour écouter comment tu te sens et t'aider à suivre ton humeur. Comment vas-tu aujourd'hui ?",
            "Je suis un chatbot de bien-être ! 😊 Mon rôle est de t'écouter, comprendre tes émotions et te donner des conseils. Parle-moi de toi !",
            "Je suis ici pour t'accompagner dans ton bien-être émotionnel ! 🌟 Dis-moi comment tu te sens !"
        ]
        
        # Remerciements
        self.thanks_words = [
            'merci', 'thanks', 'thank you', 'thx', 'cool', 'super',
            'génial', 'parfait', 'ok merci', 'merci beaucoup'
        ]
        
        # Réponses aux remerciements
        self.thanks_responses = [
            "Avec plaisir ! 😊 Je suis là pour toi. N'hésite pas si tu veux parler !",
            "De rien ! 💙 C'est mon rôle de t'accompagner. Comment te sens-tu maintenant ?",
            "Je t'en prie ! 🌟 Prends soin de toi ! Tu veux continuer à discuter ?",
            "Pas de quoi ! 😊 Je suis content de pouvoir t'aider !"
        ]
        
        # Au revoir
        self.goodbye_words = [
            'bye', 'au revoir', 'à bientôt', 'ciao', 'salut',
            'bonne nuit', 'à plus', 'a+', 'goodbye', 'see you'
        ]
        
        # Réponses au revoir
        self.goodbye_responses = [
            "À bientôt ! 👋 Prends soin de toi ! 💙",
            "Au revoir ! 😊 N'hésite pas à revenir quand tu veux !",
            "Bonne continuation ! 🌟 Je suis là si tu as besoin !",
            "À plus tard ! 💪 Reste positif(ve) !"
        ]
        
        # ============================================
        # TEMPLATES DE RÉPONSES PAR SENTIMENT
        # ============================================
        
        self.response_templates = {
            'très positif': [
                "C'est merveilleux ! 🎉 Tu rayonnes de positivité !",
                "Quelle énergie incroyable ! 😊 Continue comme ça !",
                "Je suis vraiment content pour toi ! 🌟 Tu vas super bien !",
                "Wow ! Tu es au top aujourd'hui ! 💪",
                "Fantastique ! Cette énergie positive est contagieuse ! ✨"
            ],
            'positif': [
                "C'est bien ! 🙂 Tu as l'air d'aller mieux !",
                "Je vois que tu es de bonne humeur aujourd'hui ! 😊",
                "Super ! Continue sur cette lancée positive ! 💪",
                "Tu sembles en bonne forme ! C'est encourageant ! 🌈",
                "Ça fait plaisir de te voir comme ça ! 😊"
            ],
            'neutre': [
                "Je t'écoute. Comment puis-je t'aider aujourd'hui ? 🤔",
                "Je suis là pour toi. Veux-tu en parler ? 💭",
                "Journée tranquille ? Je suis là si besoin ! 🙂",
                "Comment te sens-tu vraiment ? N'hésite pas à partager ! 💬",
                "Je suis à ton écoute. Raconte-moi ta journée ! 🌤️"
            ],
            'négatif': [
                "Je comprends que tu traverses un moment difficile. 😔",
                "C'est dur parfois, mais tu n'es pas seul(e). 💙",
                "Je suis là pour toi. Parlons-en ensemble. 🤝",
                "Les jours difficiles font partie de la vie. On est là ! 💪",
                "Prends ton temps. Je t'écoute sans jugement. 🌙"
            ],
            'très négatif': [
                "Je sens que tu vas vraiment mal. Je suis là pour toi. 💙",
                "C'est vraiment difficile en ce moment, n'est-ce pas ? 😔",
                "Tu traverses une période très dure. Parlons-en. 🤝",
                "Je suis inquiet pour toi. Puis-je t'aider ? 💙",
                "Tu n'as pas à affronter ça seul(e). Je suis là. 🫂"
            ]
        }
        
        # ============================================
        # BASE DE CONSEILS DE BIEN-ÊTRE
        # ============================================
        
        self.advice_database = {
            'très positif': {
                'encouragements': [
                    "Profite de cette énergie positive ! 🌟",
                    "Partage cette joie avec tes proches ! 🤗",
                    "Note ce moment dans un journal de gratitude ! 📝",
                    "Fais quelque chose que tu aimes pour célébrer ! 🎨"
                ],
                'activities': [
                    "Appelle un ami pour partager ta joie",
                    "Fais une activité créative",
                    "Aide quelqu'un qui en a besoin",
                    "Écris ce qui te rend heureux"
                ]
            },
            'positif': {
                'encouragements': [
                    "Continue sur cette belle lancée ! 💪",
                    "Chaque jour positif est une victoire ! 🏆",
                    "Tu vas dans la bonne direction ! 🎯",
                    "Garde cette énergie ! ⚡"
                ],
                'activities': [
                    "Prends du temps pour toi",
                    "Fais une activité que tu aimes",
                    "Marche en plein air",
                    "Écoute de la musique inspirante"
                ]
            },
            'neutre': {
                'suggestions': [
                    "Que dirais-tu d'une petite activité pour booster ton moral ? 🎨",
                    "Une promenade pourrait te faire du bien ! 🚶",
                    "Prends un moment pour méditer ou respirer profondément 🧘",
                    "Parle à quelqu'un qui te comprend ! 💬"
                ],
                'activities': [
                    "Méditation de 5 minutes",
                    "Écouter de la musique apaisante",
                    "Lire quelques pages d'un livre",
                    "Faire du stretching léger"
                ]
            },
            'négatif': {
                'réconfort': [
                    "C'est normal de ne pas aller bien parfois. 💙",
                    "Les émotions difficiles sont temporaires. 🌈",
                    "Tu as le droit de te sentir ainsi. 🤝",
                    "Prends soin de toi, tu le mérites. 💆"
                ],
                'activities': [
                    "Exercice de respiration profonde (4-7-8)",
                    "Écrire tes pensées dans un journal",
                    "Parler à un ami de confiance",
                    "Regarder quelque chose de réconfortant",
                    "Prendre un bain chaud ou une douche"
                ],
                'techniques': [
                    "🫁 Respiration 4-7-8 : Inspire 4s, retiens 7s, expire 8s",
                    "✍️ Écris 3 choses pour lesquelles tu es reconnaissant(e)",
                    "🎵 Écoute ta musique préférée",
                    "☎️ Appelle quelqu'un qui te fait du bien"
                ]
            },
            'très négatif': {
                'soutien': [
                    "Tu n'es pas seul(e). Des gens se soucient de toi. 💙",
                    "Les moments difficiles passent. Tiens bon. 🤝",
                    "Demander de l'aide est une force, pas une faiblesse. 💪",
                    "Ta vie a de la valeur. Parlons-en. 🫂"
                ],
                'ressources_urgence': [
                    "🆘 Numéro d'urgence France : 3114 (prévention suicide)",
                    "🆘 Numéro d'urgence Maroc : 0801000180 (SOS Maroc)",
                    "📞 SOS Amitié France : 09 72 39 40 50",
                    "💬 Besoin d'aide immédiate ? N'hésite pas à appeler !"
                ],
                'actions_immediates': [
                    "Respire profondément pendant 2 minutes",
                    "Contacte une personne de confiance MAINTENANT",
                    "Va dans un endroit sûr et calme",
                    "Appelle un numéro d'urgence si besoin"
                ]
            }
        }
        
        # ============================================
        # MOTS-CLÉS DE CRISE (DÉTECTION)
        # ============================================
        
        self.crisis_keywords = [
            'suicide', 'suicider', 'me tuer', 'tuer', 'mourir', 'mort',
            'en finir', 'disparaître', 'plus rien', 'inutile',
            'sans espoir', 'désespoir', 'ne peux plus', 'abandonner'
        ]
        
        # Historique des réponses données (pour éviter répétitions)
        self.response_history = []
        
        print("✅ Générateur prêt ! (Templates chargés)\n")
    
    def generate_response(self, sentiment: str, sentiment_detail: str,
                         confidence: float, text: str = "",
                         mood_trend: Dict = None) -> Dict[str, Any]:
        """
        Génère une réponse complète personnalisée
        
        Args:
            sentiment (str): 'positif', 'négatif', 'neutre'
            sentiment_detail (str): Version détaillée (ex: 'très positif')
            confidence (float): Score de confiance (0-1)
            text (str): Texte original de l'utilisateur
            mood_trend (dict): Tendance d'humeur (optionnel)
        
        Returns:
            dict: {
                'main_response': str,      # Réponse principale
                'advice': list,            # Conseils
                'encouragement': str,      # Encouragement
                'is_crisis': bool,         # Situation critique ?
                'emergency_resources': list # Ressources d'urgence
            }
        
        Processus :
        1. Détecter situation de crise
        2. Choisir template approprié
        3. Ajouter contexte de tendance
        4. Générer conseils pertinents
        5. Éviter répétitions
        """
        # ========================================
        # ÉTAPE 0 : DÉTECTION CONVERSATION NATURELLE
        # ========================================
        
        # Vérifier si c'est une salutation, remerciement, etc.
        conversational_response = self._detect_conversational(text)
        if conversational_response:
            return {
                'main_response': conversational_response,
                'advice': [],
                'encouragement': '',
                'is_crisis': False,
                'emergency_resources': [],
                'is_conversational': True,  # Flag pour UI
                'sentiment': sentiment,
                'confidence': confidence
            }
        
        # Étape 1 : DÉTECTION DE CRISE
        is_crisis = self._detect_crisis(text)
        
        # Étape 2 : CHOISIR LE TEMPLATE
        # Utiliser sentiment_detail pour plus de précision
        templates = self.response_templates.get(
            sentiment_detail,
            self.response_templates.get(sentiment, self.response_templates['neutre'])
        )
        
        # Éviter les répétitions récentes
        available_templates = [t for t in templates if t not in self.response_history[-3:]]
        if not available_templates:
            available_templates = templates
        
        main_response = random.choice(available_templates)
        self.response_history.append(main_response)
        
        # Étape 3 : AJOUTER CONTEXTE DE TENDANCE
        trend_comment = ""
        if mood_trend:
            trend_value = mood_trend.get('trend', 0)
            if trend_value > 0.2:
                trend_comment = " Tu t'améliores beaucoup ! 📈 Continue !"
            elif trend_value > 0:
                trend_comment = " Je vois une légère amélioration. 🙂"
            elif trend_value < -0.2:
                trend_comment = " Je remarque que c'est plus difficile ces derniers temps. 😔"
        
        # Étape 4 : GÉNÉRER CONSEILS
        advice_list = self._select_advice(sentiment_detail, is_crisis)
        
        # Étape 5 : ENCOURAGEMENT
        encouragement = self._generate_encouragement(sentiment_detail, mood_trend)
        
        # Étape 6 : RESSOURCES D'URGENCE (si crise)
        emergency_resources = []
        if is_crisis:
            emergency_resources = self.advice_database['très négatif']['ressources_urgence']
        
        # Construire la réponse finale
        response = {
            'main_response': main_response + trend_comment,
            'advice': advice_list,
            'encouragement': encouragement,
            'is_crisis': is_crisis,
            'emergency_resources': emergency_resources,
            'sentiment': sentiment,
            'confidence': confidence
        }
        
        return response
    
    def _detect_crisis(self, text: str) -> bool:
        """
        Détecte si le message contient des mots-clés de crise
        
        Args:
            text (str): Texte à analyser
        
        Returns:
            bool: True si crise détectée
        """
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.crisis_keywords)
    
    def _detect_conversational(self, text: str) -> str:
        """
        Détecte si le message est conversationnel (salutation, remerciement, etc.)
        et retourne une réponse appropriée
        
        Args:
            text (str): Texte de l'utilisateur
        
        Returns:
            str: Réponse conversationnelle ou None si pas conversationnel
        """
        text_lower = text.lower().strip()
        text_words = text_lower.split()
        
        # Message très court (1-3 mots) = probablement conversationnel
        is_short = len(text_words) <= 3
        
        # ========================================
        # DÉTECTION SALUTATIONS
        # ========================================
        for greeting in self.greetings:
            if greeting in text_lower or text_lower == greeting:
                return random.choice(self.greeting_responses)
        
        # ========================================
        # DÉTECTION QUESTIONS SUR LE BOT
        # ========================================
        for question in self.bot_questions:
            if question in text_lower:
                return random.choice(self.bot_responses)
        
        # ========================================
        # DÉTECTION REMERCIEMENTS
        # ========================================
        for thanks in self.thanks_words:
            if thanks in text_lower:
                return random.choice(self.thanks_responses)
        
        # ========================================
        # DÉTECTION AU REVOIR
        # ========================================
        for goodbye in self.goodbye_words:
            # "salut" peut être bonjour ou au revoir, on check le contexte
            if goodbye == 'salut' and is_short:
                continue  # Traité dans greetings
            if goodbye in text_lower:
                return random.choice(self.goodbye_responses)
        
        # ========================================
        # DÉTECTION QUESTIONS SIMPLES
        # ========================================
        simple_questions = {
            'ça va': "Oui ça va bien, merci ! 😊 Et toi, comment te sens-tu ?",
            'comment vas-tu': "Je vais bien ! 🤖 Merci de demander. Et toi, comment vas-tu ?",
            'tu vas bien': "Oui je vais très bien ! 😊 Toi alors, comment tu te sens aujourd'hui ?",
            'comment tu vas': "Super bien ! 💙 Et toi ? Raconte-moi comment tu te sens !",
            'quoi de neuf': "Je suis là pour toi ! 😊 Qu'est-ce qui se passe de ton côté ?",
            'what\'s up': "Hey ! 👋 Je suis prêt à t'écouter. Comment ça va ?",
            'sup': "Hey ! 😊 Qu'est-ce qui se passe ? Comment tu te sens ?"
        }
        
        for question, response in simple_questions.items():
            if question in text_lower:
                return response
        
        # Pas de match conversationnel → traitement normal du sentiment
        return None
    
    def _select_advice(self, sentiment_detail: str, is_crisis: bool) -> List[str]:
        """
        Sélectionne des conseils pertinents
        
        Args:
            sentiment_detail (str): Sentiment détaillé
            is_crisis (bool): Situation de crise ?
        
        Returns:
            list: Liste de conseils
        """
        # Si crise, donner actions immédiates
        if is_crisis:
            advice_data = self.advice_database['très négatif']
            return (
                random.sample(advice_data.get('actions_immediates', []), 
                            min(2, len(advice_data.get('actions_immediates', []))))
            )
        
        # Sinon, conseils normaux selon le sentiment
        advice_data = self.advice_database.get(
            sentiment_detail,
            self.advice_database.get('neutre', {})
        )
        
        advice_list = []
        
        # Ajouter 1-2 activités
        activities = advice_data.get('activities', [])
        if activities:
            advice_list.extend(random.sample(activities, min(2, len(activities))))
        
        # Ajouter techniques si sentiment négatif
        if sentiment_detail in ['négatif', 'très négatif']:
            techniques = advice_data.get('techniques', [])
            if techniques:
                advice_list.append(random.choice(techniques))
        
        return advice_list
    
    def _generate_encouragement(self, sentiment_detail: str, 
                                mood_trend: Dict = None) -> str:
        """
        Génère un message d'encouragement personnalisé
        
        Args:
            sentiment_detail (str): Sentiment détaillé
            mood_trend (dict): Tendance d'humeur
        
        Returns:
            str: Message d'encouragement
        """
        # Messages d'encouragement selon sentiment
        encouragements = {
            'très positif': [
                "Continue à briller ! ✨",
                "Tu es sur la bonne voie ! 🌟",
                "Garde cette énergie positive ! ⚡"
            ],
            'positif': [
                "Tu vas bien, continue ! 💪",
                "Chaque jour est une victoire ! 🏆",
                "Tu progresses, c'est super ! 📈"
            ],
            'neutre': [
                "Un pas à la fois ! 🚶",
                "Je crois en toi ! 💙",
                "Tu n'es pas seul(e) ! 🤝"
            ],
            'négatif': [
                "Les jours difficiles passent. Courage ! 💙",
                "Tu es plus fort(e) que tu ne le penses ! 💪",
                "Demain est un nouveau jour. 🌅"
            ],
            'très négatif': [
                "Ta vie a de la valeur. Tiens bon ! 💙",
                "L'aide existe. N'hésite pas à la demander. 🤝",
                "Tu n'es pas seul(e). On est là. 🫂"
            ]
        }
        
        encouragement_list = encouragements.get(sentiment_detail, encouragements['neutre'])
        
        # Ajouter contexte de tendance si amélioration
        if mood_trend and mood_trend.get('trend', 0) > 0.1:
            return "Tu t'améliores vraiment ! Continue comme ça ! 📈✨"
        
        return random.choice(encouragement_list)
    
    def format_full_response(self, response_data: Dict[str, Any]) -> str:
        """
        Formate la réponse complète pour affichage
        
        Args:
            response_data (dict): Données de réponse générées
        
        Returns:
            str: Réponse formatée prête à afficher
        """
        lines = []
        
        # Réponse principale
        lines.append(f"💬 {response_data['main_response']}")
        lines.append("")
        
        # Conseils
        if response_data['advice']:
            lines.append("💡 Suggestions pour toi :")
            for advice in response_data['advice']:
                lines.append(f"   • {advice}")
            lines.append("")
        
        # Encouragement
        if response_data['encouragement']:
            lines.append(f"✨ {response_data['encouragement']}")
            lines.append("")
        
        # ALERTE CRISE
        if response_data['is_crisis']:
            lines.append("⚠️  " + "="*60)
            lines.append("🆘 JE SUIS INQUIET POUR TOI")
            lines.append("="*60)
            lines.append("")
            lines.append("Si tu as des pensées suicidaires, contacte IMMÉDIATEMENT :")
            lines.append("")
            for resource in response_data['emergency_resources']:
                lines.append(f"   {resource}")
            lines.append("")
            lines.append("Ta vie a de la valeur. L'aide existe. 💙")
            lines.append("="*60)
        
        return "\n".join(lines)


# ============================================
# DÉMONSTRATION
# ============================================

def demo():
    """
    Démonstration du Générateur de Réponses
    """
    print("\n" + "="*70)
    print("🧪 DÉMONSTRATION - GÉNÉRATEUR DE RÉPONSES")
    print("="*70 + "\n")
    
    # Créer le générateur
    generator = ResponseGenerator()
    
    # Test 1 : Message positif
    print("="*70)
    print("TEST 1 : Message TRÈS POSITIF")
    print("="*70)
    response = generator.generate_response(
        sentiment='positif',
        sentiment_detail='très positif',
        confidence=0.85,
        text="Je suis vraiment heureux aujourd'hui !"
    )
    print(generator.format_full_response(response))
    
    # Test 2 : Message négatif avec tendance d'amélioration
    print("\n" + "="*70)
    print("TEST 2 : Message NÉGATIF (mais s'améliore)")
    print("="*70)
    mock_trend = {'trend': 0.25, 'mean_score': 0.3}
    response = generator.generate_response(
        sentiment='négatif',
        sentiment_detail='négatif',
        confidence=0.72,
        text="Je me sens pas bien",
        mood_trend=mock_trend
    )
    print(generator.format_full_response(response))
    
    # Test 3 : Message neutre
    print("\n" + "="*70)
    print("TEST 3 : Message NEUTRE")
    print("="*70)
    response = generator.generate_response(
        sentiment='neutre',
        sentiment_detail='neutre',
        confidence=0.55,
        text="Journée normale"
    )
    print(generator.format_full_response(response))
    
    # Test 4 : CRISE (mots-clés critiques)
    print("\n" + "="*70)
    print("TEST 4 : DÉTECTION DE CRISE ⚠️")
    print("="*70)
    response = generator.generate_response(
        sentiment='négatif',
        sentiment_detail='très négatif',
        confidence=0.88,
        text="Je veux en finir, je ne peux plus"
    )
    print(generator.format_full_response(response))
    
    print("\n" + "="*70)
    print("✅ Démonstration terminée !")
    print("="*70)


if __name__ == "__main__":
    demo()
