"""
Analyseur de sentiment pour Approche 3 (Fine-tuning BERT)
Charge le modèle fine-tuné et l'utilise pour les prédictions
"""

import os
import sys
from typing import Dict
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from approach3.sentiment_finetuner import BERTFineTuner
from approach3.keyword_analyzer import KeywordSentimentAnalyzer


class SentimentAnalyzer:
    """
    Analyseur de sentiment utilisant BERT fine-tuné
    
    Différence avec Approche 1 :
    - Approche 1 : BERT gelé + petit classifieur
    - Approche 3 : BERT fine-tuné sur données bien-être
    → Meilleure précision sur les sentiments bien-être
    """
    
    def __init__(self, model_dir: str = None):
        """
        Initialise l'analyseur
        
        Args:
            model_dir (str): Répertoire du modèle fine-tuné
        """
        # Si pas de model_dir, utiliser le chemin par défaut
        if model_dir is None:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            model_dir = os.path.join(project_root, 'models', 'approach3', 'bert_finetuned')
        
        print("🤖 Initialisation du Sentiment Analyzer (Approche 3)...")
        print(f"   Chemin du modèle: {model_dir}")
        
        self.finetuner = None
        self.keyword_analyzer = KeywordSentimentAnalyzer()
        self.use_bert = False
        
        # Essayer de charger le modèle BERT fine-tuné si disponible
        try:
            if Path(model_dir).exists() and (Path(model_dir) / 'pytorch_model.bin').exists():
                print(f"🔧 Chargement depuis répertoire local (BERT fine-tuné)...")
                self.finetuner = BERTFineTuner(
                    model_name=model_dir,
                    output_dir=model_dir
                )
                self.use_bert = True
                print("✅ BERT fine-tuné chargé!")
            else:
                print(f"⚠️  Modèle fine-tuné non disponible.")
                print(f"   Utilisation de l'analyseur basé sur dictionnaire...")
        except Exception as e:
            print(f"❌ Erreur BERT: {e}")
            print(f"   Basculement vers analyseur par dictionnaire...")
        
        print("✅ Sentiment Analyzer prêt! (Analyseur par dictionnaire)")
    
    def analyze(self, text: str) -> Dict:
        """
        Analyse le sentiment d'un texte
        
        Utilise:
        - BERT fine-tuné si disponible
        - Sinon: analyseur basé sur dictionnaire de mots-clés
        
        Args:
            text (str): Texte à analyser
            
        Returns:
            dict: Résultat de l'analyse avec:
                - sentiment: Sentiment principal (négatif, neutre, positif)
                - sentiment_detail: Détail du sentiment (5 niveaux)
                - confidence: Confiance (0-1)
                - scores: Tous les scores par sentiment
        """
        
        # Utiliser BERT si disponible et bien entraîné
        if self.use_bert and self.finetuner:
            try:
                result = self.finetuner.predict(text)
                # Vérifier que ce n'est pas des scores aléatoires
                # (scores uniformes = pas entraîné)
                scores = result['all_scores']
                std_dev = (
                    (sum((v - 0.2)**2 for v in scores.values()) / len(scores)) ** 0.5
                )
                if std_dev > 0.05:  # Si écart-type > 0.05, le modèle est OK
                    return {
                        'sentiment': self._map_sentiment_to_category(result['sentiment']),
                        'sentiment_detail': result['sentiment'],
                        'confidence': result['confidence'],
                        'scores': result['all_scores'],
                        'approach': 'BERT fine-tuned'
                    }
            except Exception as e:
                print(f"⚠️  BERT erreur: {e}, basculement vers dictionnaire")
                self.use_bert = False
        
        # Fallback: analyseur par dictionnaire (plus fiable que BERT non-entraîné)
        result = self.keyword_analyzer.analyze(text)
        return {
            'sentiment': result['sentiment'],
            'sentiment_detail': result['sentiment_detail'],
            'confidence': result['confidence'],
            'scores': result['scores'],
            'approach': 'keyword-based (dictionnaire)'
        }
    
    def _map_sentiment_to_category(self, detailed_sentiment: str) -> str:
        """
        Mappe les 5 sentiments détaillés à 3 catégories
        
        très négatif + négatif → negatif
        neutre → neutre
        positif + très positif → positif
        
        Args:
            detailed_sentiment (str): Sentiment détaillé (0-4)
            
        Returns:
            str: Catégorie (negatif, neutre, positif)
        """
        if detailed_sentiment in ['très négatif', 'négatif']:
            return 'negatif'
        elif detailed_sentiment == 'neutre':
            return 'neutre'
        else:  # positif ou très positif
            return 'positif'


# ============================================================================
# Test
# ============================================================================

if __name__ == '__main__':
    try:
        analyzer = SentimentAnalyzer()
        
        test_text = "Je suis heureux!"
        result = analyzer.analyze(test_text)
        
        print(f"\nTest: '{test_text}'")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Détail: {result['sentiment_detail']}")
        print(f"Confiance: {result['confidence']:.1%}")
        
    except FileNotFoundError as e:
        print(f"⚠️  {e}")
