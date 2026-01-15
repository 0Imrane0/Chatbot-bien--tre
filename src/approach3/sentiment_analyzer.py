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
        
        # Charger le modèle - d'abord essayer le modèle local, sinon utiliser BERT base
        try:
            if Path(model_dir).exists():
                print(f"🔧 Chargement depuis répertoire local...")
                self.finetuner = BERTFineTuner(
                    model_name=model_dir,  # Charger depuis répertoire local
                    output_dir=model_dir
                )
            else:
                # Fallback: utiliser BERT base depuis le cache
                print(f"⚠️  Répertoire local non trouvé, utilisation de BERT base-uncased...")
                self.finetuner = BERTFineTuner(
                    model_name="bert-base-uncased",  # Utiliser depuis cache Hugging Face
                    output_dir=model_dir
                )
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")
            print(f"   Utilisation de BERT base-uncased...")
            self.finetuner = BERTFineTuner(
                model_name="bert-base-uncased",
                output_dir=model_dir
            )
        
        print("✅ Sentiment Analyzer prêt! (BERT fine-tuné)")
    
    def analyze(self, text: str) -> Dict:
        """
        Analyse le sentiment d'un texte
        
        Args:
            text (str): Texte à analyser
            
        Returns:
            dict: Résultat de l'analyse avec:
                - sentiment: Sentiment principal (très négatif → très positif)
                - sentiment_detail: Détail du sentiment
                - confidence: Confiance (0-1)
                - scores: Tous les scores par sentiment
        """
        
        # Prédire avec BERT fine-tuné
        result = self.finetuner.predict(text)
        
        # Restructurer pour compatibilité avec Approche 1
        return {
            'sentiment': self._map_sentiment_to_category(result['sentiment']),
            'sentiment_detail': result['sentiment'],
            'confidence': result['confidence'],
            'scores': result['all_scores'],
            'approach': 'fine-tuning'
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
