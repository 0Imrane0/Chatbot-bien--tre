"""
SOLUTION PRAGMATIQUE: Analyseur de sentiment basé sur dictionnaire + règles
Utilisé quand le modèle BERT fine-tuné n'est pas disponible
"""

import re
from typing import Dict


class KeywordSentimentAnalyzer:
    """
    Analyseur de sentiment utilisant un dictionnaire de mots-clés
    Fallback quand le BERT fine-tuné n'est pas disponible
    
    Approche:
    - Compter les mots positifs/négatifs/neutres
    - Appliquer des intensificateurs (très, extrêmement, etc.)
    - Détecter la négation
    - Mapper au sentiment final
    """
    
    def __init__(self):
        # Dictionnaires de mots-clés par sentiment
        self.very_negative_words = {
            'nul', 'nuls', 'nulle', 'pire', 'pis', 'catastrophe', 'horrifiant',
            'tragique', 'desespoir', 'suicide', 'mort', 'deteste', 'hais', 'abhorr',
            'insupportable', 'infernal', 'horrible', 'atroce', 'ignoble', 'abject',
            'suicider', 'tuer', 'mourir', 'en finir', 'disparaitre',
            'plus rien', 'inutile', 'sans espoir', 'ne peux plus', 'abandonner'
        }
        
        self.negative_words = {
            'triste', 'tristesse', 'malheureux', 'malheur', 'depression', 'deprime',
            'angoisse', 'anxieux', 'anxiete', 'peur', 'peureux', 'terreur', 'terrifie',
            'frustration', 'frustré', 'colère', 'coléreux', 'fureur', 'furieux',
            'enerve', 'enervant', 'irrite', 'irritant', 'agace', 'agacant',
            'mauvais', 'mal', 'negatif', 'negatif', 'faible', 'faibles', 'faiblesse',
            'malade', 'maladie', 'souffrance', 'souffre', 'souffrir', 'douleur',
            'echec', 'echec', 'echouer', 'rate', 'rate', 'rater', 'echouer',
            'perte', 'perdu', 'perdre', 'decu', 'deception', 'desappointe',
            'regret', 'regretter', 'culpabilite', 'coupable', 'honte', 'honteuse',
            'pitie', 'pauvre', 'miserable', 'misere', 'probleme', 'problematique',
            'difficile', 'difficulté', 'dur', 'durent', 'dure', 'penible', 'eprouvant',
            'stresse', 'stress', 'stressant', 'stressé', 'stressée', 'stressé',
            'preoccupe', 'preoccupation', 'preocupe', 'preocupée',
            'inquiet', 'inquiete', 'inquietude', 'inquietant',
            'incompetent', 'incompetence', 'nul', 'nulle', 'incapable', 'incapacite',
            'nerveux', 'nerveuse', 'nervosité', 'nervos',  # AJOUT: mots manquants
            'tension', 'tendu', 'tendue', 'tendresse',
            'oppresse', 'oppression', 'oppressant'
        }
        
        self.positive_words = {
            'bien', 'bonne', 'bon', 'bonheur', 'heureuse', 'heureux', 'joie', 'joyeuse',
            'amour', 'aimé', 'aimer', 'adorable', 'adoré', 'merveilleux', 'merveilleuse',
            'fantastique', 'super', 'super', 'génial', 'génialement', 'brillant',
            'magnifique', 'sublime', 'splendide', 'superbe', 'extraordinaire',
            'confident', 'confiance', 'fierté', 'fière', 'fier', 'fiers', 'fierté',
            'réussi', 'réussite', 'succès', 'réussir', 'victoire', 'victorieuse',
            'soulagement', 'soulagé', 'soulager', 'apaisé', 'apaiser', 'calme',
            'sérénité', 'serein', 'tranquille', 'tranquillité', 'paix', 'paisible',
            'optimiste', 'optimisme', 'espoir', 'espérance', 'positif', 'positivité',
            'énergie', 'énergique', 'vitalité', 'vivant', 'vif', 'vivacité',
            'plaisir', 'plaisant', 'agréable', 'délice', 'délicieux', 'succulent',
            'gratitude', 'gratitude', 'reconnaissant', 'remerciement', 'remercier',
            'fly', 'cool', 'chill', 'ouf', 'dingue', 'fou', 'folle', 'content', 'contente',
            'sympathique', 'gentil', 'gentille', 'drole', 'marrant', 'rigolo', 'va'  # Ajout de 'va' pour "ça va"
        }
        
        self.very_positive_words = {
            'extraordinaire', 'incroyable', 'incroyablement', 'merveilleux', 'merveilleuse',
            'fantastique', 'magnifique', 'sublime', 'splendide', 'exceptionnel',
            'époustouflant', 'génial', 'super', 'supers', 'superbe', 'excellent',
            'excellent', 'excellente', 'perfection', 'parfait', 'parfaite', 'idéal',
            'divin', 'divine', 'céleste', 'paradis', 'paradisiaque', 'bonheur absolu',
            'réussi', 'réussite', 'fier', 'fière', 'fierté', 'victoire',
            'incroyable', 'wow', 'amazing', 'awesome', 'epic', 'fire', 'lit'
        }
        
        # Intensificateurs (plus complets)
        self.intensifiers = {
            'très': 1.3, 'extrêmement': 1.4, 'absolument': 1.35, 'totalement': 1.3, 
            'complètement': 1.3, 'vraiment': 1.25, 'énormément': 1.4, 'terriblement': 1.3, 
            'affreusement': 1.3, 'super': 1.2, 'hyper': 1.25, 'mega': 1.3, 'ultra': 1.3,
            'beaucoup': 1.2, 'trop': 1.15, 'bien': 1.1, 'fort': 1.15, 'grave': 1.2,
            'tellement': 1.25, 'vraiment': 1.25, 'vachement': 1.2, 'drôlement': 1.2,
            'follement': 1.25, 'immensément': 1.35, 'démesurément': 1.35
        }
        
        # Négatifs
        self.negations = ['ne', 'pas', 'non', 'aucun', 'aucune', 'jamais', 'rien']
    
    def _tokenize(self, text: str) -> list:
        """Tokenizer simple"""
        return re.findall(r'\b\w+\b', text.lower())
    
    def _remove_accents(self, word: str) -> str:
        """Enlever les accents"""
        accents = {
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'à': 'a', 'â': 'a', 'ä': 'a',
            'ô': 'o', 'ö': 'o',
            'ù': 'u', 'û': 'u', 'ü': 'u',
            'î': 'i', 'ï': 'i',
            'ç': 'c'
        }
        return ''.join(accents.get(c, c) for c in word)
    
    def analyze(self, text: str) -> Dict:
        """
        Analyse le sentiment avec intensité réelle
        
        Returns:
            dict: {sentiment, sentiment_detail, confidence, scores}
        """
        words = self._tokenize(text)
        words_clean = [self._remove_accents(w) for w in words]
        text_lower = text.lower()
        
        # Compter les mots
        very_negative_count = sum(1 for w in words_clean if w in self.very_negative_words)
        negative_count = sum(1 for w in words_clean if w in self.negative_words)
        positive_count = sum(1 for w in words_clean if w in self.positive_words)
        very_positive_count = sum(1 for w in words_clean if w in self.very_positive_words)
        
        # Compter les intensificateurs et leurs niveaux
        intensifier_count = 0
        intensifier_boost = 1.0
        
        for word_clean, word_original in zip(words_clean, words):
            if word_clean in self.intensifiers:
                intensifier_count += 1
                intensifier_boost *= self.intensifiers[word_clean]
        
        # Limiter le boost à un max raisonnable
        intensifier_boost = min(intensifier_boost, 1.8)
        
        # Calculer le score BRUT
        # Poids: very_negative=2, negative=1, positive=1, very_positive=2
        raw_sentiment_score = (
            (very_positive_count * 2) + positive_count 
            - negative_count - (very_negative_count * 2)
        )
        
        # Appliquer le boost des intensificateurs
        if intensifier_count > 0:
            raw_sentiment_score *= intensifier_boost
        
        # Compter les mots de sentiment
        total_sentiment_words = very_negative_count + negative_count + positive_count + very_positive_count
        
        # ========== CLASSIFICATION DYNAMIQUE ==========
        
        # Déterminer sentiment_detail et confiance en fonction du score et intensité
        
        if very_negative_count >= 2:
            # Très fort négatif
            sentiment_detail = 'très négatif'
            base_confidence = 0.92 + (0.03 * min(very_negative_count, 3))
            confidence = min(0.99, base_confidence * intensifier_boost)
            
        elif very_negative_count == 1 and negative_count >= 1:
            # Négatif fort
            sentiment_detail = 'très négatif'
            confidence = min(0.97, 0.90 + (0.03 * negative_count))
            
        elif very_negative_count == 1:
            # Négatif fort mais seul
            sentiment_detail = 'très négatif'
            confidence = min(0.95, 0.88 + (0.02 * intensifier_count))
            
        elif negative_count >= 3:
            # Plusieurs mots négatifs
            sentiment_detail = 'très négatif'
            confidence = min(0.98, 0.85 + (0.04 * negative_count))
            
        elif negative_count >= 2:
            # Deux mots négatifs ou plus
            sentiment_detail = 'négatif'
            confidence = min(0.95, 0.78 + (0.05 * negative_count) + (0.02 * intensifier_count))
            
        elif negative_count == 1:
            # Un seul mot négatif
            sentiment_detail = 'négatif'
            confidence = min(0.85, 0.65 + (0.05 * intensifier_count) + (0.03 * total_sentiment_words))
            
        # --- POSITIFS ---
        
        elif very_positive_count >= 2:
            # Très fort positif
            sentiment_detail = 'très positif'
            base_confidence = 0.92 + (0.03 * min(very_positive_count, 3))
            confidence = min(0.99, base_confidence * intensifier_boost)
            
        elif very_positive_count == 1 and positive_count >= 2:
            # Positif très fort
            sentiment_detail = 'très positif'
            confidence = min(0.97, 0.90 + (0.03 * positive_count))
            
        elif very_positive_count == 1:
            # Positif fort seul
            sentiment_detail = 'très positif'
            confidence = min(0.95, 0.88 + (0.02 * intensifier_count))
            
        elif positive_count >= 4:
            # Beaucoup de mots positifs
            sentiment_detail = 'très positif'
            confidence = min(0.98, 0.85 + (0.03 * positive_count))
            
        elif positive_count >= 3:
            # Plusieurs mots positifs
            sentiment_detail = 'positif'
            confidence = min(0.95, 0.78 + (0.05 * positive_count) + (0.03 * intensifier_count))
            
        elif positive_count >= 2:
            # Deux mots positifs
            sentiment_detail = 'positif'
            confidence = min(0.90, 0.72 + (0.05 * positive_count) + (0.04 * intensifier_count))
            
        elif positive_count == 1:
            # Un seul mot positif
            sentiment_detail = 'positif'
            confidence = min(0.80, 0.60 + (0.06 * intensifier_count) + (0.04 * total_sentiment_words))
            
        # --- NEUTRE ---
        else:
            sentiment_detail = 'neutre'
            # Confiance basse pour neutre
            confidence = 0.35 if total_sentiment_words == 0 else 0.55
        
        # Assurer une plage valide de confiance (30% à 99%)
        confidence = min(0.99, max(0.30, confidence))
        
        # Mapper au sentiment principal
        if sentiment_detail in ['très négatif', 'négatif']:
            sentiment = 'negatif'
        elif sentiment_detail in ['très positif', 'positif']:
            sentiment = 'positif'
        else:
            sentiment = 'neutre'
        
        # Créer les scores pour compatibilité
        if sentiment == 'negatif':
            scores = {
                'très négatif': 0.45 if sentiment_detail == 'très négatif' else 0.20,
                'négatif': 0.35 if sentiment_detail == 'négatif' else 0.15,
                'neutre': 0.10,
                'positif': 0.05,
                'très positif': 0.05,
            }
        elif sentiment == 'positif':
            scores = {
                'très négatif': 0.05,
                'négatif': 0.05,
                'neutre': 0.10,
                'positif': 0.35 if sentiment_detail == 'positif' else 0.20,
                'très positif': 0.45 if sentiment_detail == 'très positif' else 0.20,
            }
        else:
            scores = {
                'très négatif': 0.10,
                'négatif': 0.15,
                'neutre': 0.50,
                'positif': 0.15,
                'très positif': 0.10,
            }
        
        return {
            'sentiment': sentiment,
            'sentiment_detail': sentiment_detail,
            'confidence': confidence,
            'scores': scores,
            'approach': 'keyword-based',
            'debug': {
                'very_negative': very_negative_count,
                'negative': negative_count,
                'positive': positive_count,
                'very_positive': very_positive_count,
                'intensifiers': intensifier_count,
                'raw_score': raw_sentiment_score
            }
        }


if __name__ == '__main__':
    analyzer = KeywordSentimentAnalyzer()
    
    tests = [
        'Je suis complètement nul, je vais rater mon examen et ma vie est fichue',
        'Je me sens triste',
        'J\'ai réussi ma présentation, je suis fier de moi !',
        'C\'est magnifique!',
        'Rien de spécial',
    ]
    
    for text in tests:
        result = analyzer.analyze(text)
        print(f"Texte: {text}")
        print(f"  Sentiment: {result['sentiment_detail']} ({result['confidence']:.0%})")
        print()
