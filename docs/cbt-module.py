"""
Module CBT (Cognitive Behavioral Therapy) pour Chatbot de Bien-être
====================================================================

Ce module implémente les techniques de base de la thérapie cognitivo-comportementale
pour aider l'utilisateur à restructurer ses pensées négatives.

IMPORTANT : Ce chatbot est un outil de bien-être, PAS un remplacement pour 
une thérapie professionnelle.
"""

import re
from typing import Dict, List, Tuple


class CBTEngine:
    """
    Moteur de thérapie cognitivo-comportementale
    """
    
    def __init__(self):
        # Distorsions cognitives courantes
        self.cognitive_distortions = {
            "catastrophizing": {
                "keywords": ["toujours", "jamais", "terrible", "horrible", "catastrophe"],
                "pattern": r"\b(toujours|jamais|terrible|horrible|catastrophe)\b",
                "name": "Catastrophisation",
                "description": "Tu imagines le pire scénario possible",
                "challenge_questions": [
                    "Quelle est la probabilité réelle que le pire arrive ?",
                    "Qu'est-ce qui pourrait arriver de plus probable ?",
                    "Comment as-tu géré des situations similaires dans le passé ?"
                ]
            },
            
            "all_or_nothing": {
                "keywords": ["tout", "rien", "parfait", "raté"],
                "pattern": r"\b(tout|rien|parfait|complètement raté)\b",
                "name": "Pensée Tout-ou-Rien",
                "description": "Tu vois les choses en noir et blanc, sans nuances",
                "challenge_questions": [
                    "Y a-t-il des nuances de gris entre 'tout' et 'rien' ?",
                    "Peux-tu réussir partiellement quelque chose ?",
                    "Quelle est la zone entre ces deux extrêmes ?"
                ]
            },
            
            "overgeneralization": {
                "keywords": ["je suis", "je ne suis pas", "je suis nul", "je suis un raté"],
                "pattern": r"je (suis|ne suis pas) (un )?(raté|nul|incapable|mauvais)",
                "name": "Surgénéralisation",
                "description": "Tu tires des conclusions générales d'un événement isolé",
                "challenge_questions": [
                    "Est-ce qu'UN événement définit QUI tu es ?",
                    "Quels sont des exemples où tu as réussi ?",
                    "Qu'est-ce que cette situation dit vraiment de toi ?"
                ]
            },
            
            "mind_reading": {
                "keywords": ["il pense que", "elle pense que", "ils pensent que", "personne ne"],
                "pattern": r"(il|elle|ils) (pense|pensent) que",
                "name": "Lecture de Pensées",
                "description": "Tu assumes savoir ce que les autres pensent",
                "challenge_questions": [
                    "As-tu des preuves concrètes de ce qu'ils pensent ?",
                    "Y a-t-il d'autres explications possibles ?",
                    "Peux-tu vérifier directement avec eux ?"
                ]
            },
            
            "emotional_reasoning": {
                "keywords": ["je sens que", "j'ai l'impression que"],
                "pattern": r"(je sens|j'ai l'impression) que",
                "name": "Raisonnement Émotionnel",
                "description": "Tu crois que ce que tu ressens est forcément la réalité",
                "challenge_questions": [
                    "Qu'est-ce que les FAITS disent, indépendamment de tes émotions ?",
                    "Tes émotions reflètent-elles toujours la réalité ?",
                    "Que dirais-tu à un ami dans cette situation ?"
                ]
            }
        }
        
        # Techniques de restructuration cognitive
        self.restructuring_templates = {
            "positive": [
                "Au lieu de penser '{negative}', que dirais-tu de '{positive}' ?",
                "Une façon plus équilibrée de voir ça serait : '{positive}'",
                "Transformons cette pensée : '{negative}' → '{positive}'"
            ],
            "evidence": [
                "Quelles sont les preuves POUR et CONTRE cette pensée ?",
                "Si ton meilleur ami pensait ça, que lui dirais-tu ?",
                "Que dirait quelqu'un d'objectif sur cette situation ?"
            ]
        }
        
        # Activation comportementale (actions concrètes)
        self.behavioral_activation = {
            "depression": {
                "immediate": [
                    "Fais une promenade de 10 minutes en plein air",
                    "Écoute 2-3 de tes chansons préférées",
                    "Fais 5 minutes d'étirements légers",
                    "Appelle ou envoie un message à un ami"
                ],
                "short_term": [
                    "Programme une activité plaisante cette semaine",
                    "Établis une petite routine quotidienne",
                    "Fais une chose qui te donnait de la joie avant",
                    "Aide quelqu'un (bénévolat, service)"
                ],
                "long_term": [
                    "Rejoins un club ou une activité de groupe",
                    "Fixe-toi un objectif réaliste à 1 mois",
                    "Développe une nouvelle compétence progressive"
                ]
            },
            
            "anxiety": {
                "immediate": [
                    "Respiration 4-7-8 : Inspire 4s, retiens 7s, expire 8s",
                    "Technique 5-4-3-2-1 : Nomme 5 choses que tu vois, 4 que tu touches, etc.",
                    "Ancrage : Pose tes pieds au sol, sens la connexion",
                    "Écrire tes inquiétudes pendant 5 minutes"
                ],
                "short_term": [
                    "Pratique la méditation 10min/jour",
                    "Limite la caféine et les écrans avant de dormir",
                    "Crée une 'worry window' : 15min/jour pour s'inquiéter",
                    "Tiens un journal des pensées anxieuses"
                ],
                "long_term": [
                    "Apprends des techniques de relaxation musculaire progressive",
                    "Expose-toi graduellement à tes peurs (avec soutien)",
                    "Développe une pratique régulière de mindfulness"
                ]
            },
            
            "stress": {
                "immediate": [
                    "Prends 5 respirations profondes",
                    "Fais une pause de 5 minutes",
                    "Bois un verre d'eau lentement",
                    "Étire-toi ou bouge pendant 2 minutes"
                ],
                "short_term": [
                    "Décompose ta tâche en petites étapes",
                    "Utilise la technique Pomodoro (25min travail, 5min pause)",
                    "Identifie 1 chose que tu peux déléguer",
                    "Dis 'non' à une demande non-essentielle"
                ],
                "long_term": [
                    "Établis des limites claires travail/vie personnelle",
                    "Apprends à prioriser avec la matrice d'Eisenhower",
                    "Développe un système de gestion du temps"
                ]
            }
        }
        
        # Questions socratiques pour guider la réflexion
        self.socratic_questions = {
            "evidence": [
                "Quelles sont les preuves qui soutiennent cette pensée ?",
                "Quelles sont les preuves qui contredisent cette pensée ?",
                "Y a-t-il des faits que tu ignores ?"
            ],
            "alternative": [
                "Y a-t-il d'autres façons de voir cette situation ?",
                "Comment quelqu'un d'autre interpréterait-il ceci ?",
                "Qu'est-ce que tu dirais à un ami dans cette situation ?"
            ],
            "consequences": [
                "Quel est l'effet de penser comme ça ?",
                "Comment cette pensée influence-t-elle ton comportement ?",
                "Est-ce que cette façon de penser t'aide ou te freine ?"
            ],
            "action": [
                "Que peux-tu faire maintenant pour améliorer la situation ?",
                "Quelle est la plus petite action que tu pourrais prendre ?",
                "Qu'as-tu contrôlé dans cette situation ?"
            ]
        }
    
    def detect_cognitive_distortions(self, text: str) -> List[Dict]:
        """
        Détecte les distorsions cognitives dans le texte
        
        Args:
            text: Le texte à analyser
            
        Returns:
            Liste des distorsions détectées avec leurs détails
        """
        detected = []
        text_lower = text.lower()
        
        for distortion_type, details in self.cognitive_distortions.items():
            # Vérifier les keywords
            if any(keyword in text_lower for keyword in details["keywords"]):
                # Vérifier le pattern regex
                if re.search(details["pattern"], text_lower):
                    detected.append({
                        "type": distortion_type,
                        "name": details["name"],
                        "description": details["description"],
                        "challenge_questions": details["challenge_questions"]
                    })
        
        return detected
    
    def generate_cbt_response(self, user_message: str, sentiment: str, 
                             emotional_intensity: float) -> Dict:
        """
        Génère une réponse basée sur la CBT
        
        Args:
            user_message: Message de l'utilisateur
            sentiment: Sentiment détecté (positive/negative/neutral)
            emotional_intensity: Intensité émotionnelle (0-1)
            
        Returns:
            Réponse structurée avec techniques CBT
        """
        response = {
            "empathy": "",
            "distortions": [],
            "restructuring": "",
            "actions": [],
            "questions": []
        }
        
        # 1. EMPATHIE (toujours commencer par valider l'émotion)
        if sentiment == "negative":
            if emotional_intensity > 0.7:
                response["empathy"] = "Je comprends que tu traverses un moment vraiment difficile. Tes émotions sont valides."
            else:
                response["empathy"] = "Ça semble compliqué pour toi en ce moment. C'est normal de se sentir comme ça."
        
        # 2. DÉTECTER LES DISTORSIONS COGNITIVES
        distortions = self.detect_cognitive_distortions(user_message)
        response["distortions"] = distortions
        
        # 3. PROPOSER UNE RESTRUCTURATION
        if distortions:
            main_distortion = distortions[0]
            response["restructuring"] = f"Je remarque que tu as peut-être une pensée de type '{main_distortion['name']}'. {main_distortion['description']}. "
            response["questions"] = main_distortion["challenge_questions"][:2]  # Poser 2 questions max
        
        # 4. ACTIVATION COMPORTEMENTALE
        emotion_category = self._map_sentiment_to_category(sentiment, user_message)
        if emotion_category in self.behavioral_activation:
            response["actions"] = {
                "immediate": self.behavioral_activation[emotion_category]["immediate"][:2],
                "short_term": self.behavioral_activation[emotion_category]["short_term"][:2]
            }
        
        return response
    
    def _map_sentiment_to_category(self, sentiment: str, message: str) -> str:
        """
        Détermine la catégorie émotionnelle (depression/anxiety/stress)
        """
        message_lower = message.lower()
        
        # Mots-clés pour l'anxiété
        anxiety_keywords = ["anxieux", "stressé", "inquiet", "peur", "angoisse", "panique"]
        # Mots-clés pour la dépression
        depression_keywords = ["triste", "déprimé", "vide", "seul", "désespoir", "fatigué"]
        # Mots-clés pour le stress
        stress_keywords = ["débordé", "pressé", "submergé", "trop", "épuisé"]
        
        anxiety_count = sum(1 for kw in anxiety_keywords if kw in message_lower)
        depression_count = sum(1 for kw in depression_keywords if kw in message_lower)
        stress_count = sum(1 for kw in stress_keywords if kw in message_lower)
        
        # Retourner la catégorie la plus probable
        counts = {
            "anxiety": anxiety_count,
            "depression": depression_count,
            "stress": stress_count
        }
        
        return max(counts, key=counts.get) if max(counts.values()) > 0 else "stress"
    
    def format_response_for_user(self, cbt_response: Dict) -> str:
        """
        Formate la réponse CBT en message conversationnel
        """
        parts = []
        
        # 1. Empathie
        if cbt_response["empathy"]:
            parts.append(cbt_response["empathy"])
        
        # 2. Restructuration cognitive
        if cbt_response["restructuring"]:
            parts.append(cbt_response["restructuring"])
        
        # 3. Questions socratiques
        if cbt_response["questions"]:
            parts.append("\nRéfléchissons ensemble :")
            for i, question in enumerate(cbt_response["questions"], 1):
                parts.append(f"{i}. {question}")
        
        # 4. Actions concrètes
        if cbt_response["actions"]:
            parts.append("\n💡 Actions que tu peux essayer maintenant :")
            for action in cbt_response["actions"]["immediate"]:
                parts.append(f"• {action}")
        
        return "\n".join(parts)


# ============= EXEMPLE D'UTILISATION =============

if __name__ == "__main__":
    # Créer l'instance CBT
    cbt_engine = CBTEngine()
    
    # Exemples de messages utilisateurs
    test_messages = [
        {
            "message": "Je suis complètement nul, je rate toujours tout",
            "sentiment": "negative",
            "intensity": 0.8
        },
        {
            "message": "Je suis tellement stressé, j'ai trop de travail",
            "sentiment": "negative",
            "intensity": 0.6
        },
        {
            "message": "Je sens que personne ne m'aime, tout le monde pense que je suis bizarre",
            "sentiment": "negative",
            "intensity": 0.7
        }
    ]
    
    print("=" * 80)
    print("DÉMONSTRATION DU MODULE CBT")
    print("=" * 80)
    
    for i, test in enumerate(test_messages, 1):
        print(f"\n{'='*80}")
        print(f"EXEMPLE {i}")
        print(f"{'='*80}")
        print(f"\n👤 Utilisateur: {test['message']}")
        print(f"📊 Sentiment: {test['sentiment']} (Intensité: {test['intensity']})")
        
        # Générer la réponse CBT
        cbt_response = cbt_engine.generate_cbt_response(
            test['message'],
            test['sentiment'],
            test['intensity']
        )
        
        # Afficher la réponse formatée
        print(f"\n🤖 Chatbot (avec CBT):")
        print("-" * 80)
        formatted_response = cbt_engine.format_response_for_user(cbt_response)
        print(formatted_response)
        
        # Afficher les distortions détectées
        if cbt_response["distortions"]:
            print(f"\n🔍 Distorsions cognitives détectées:")
            for dist in cbt_response["distortions"]:
                print(f"   • {dist['name']}: {dist['description']}")
    
    print("\n" + "=" * 80)
    print("FIN DE LA DÉMONSTRATION")
    print("=" * 80)
