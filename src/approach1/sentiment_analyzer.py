"""
Module d'Analyse de Sentiment - Approche 1 (Transfer Learning)
Utilise un modèle BERT pré-entraîné pour analyser le sentiment des messages

Auteur : Étudiant ENSA Berrechid
Date : Décembre 2024
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
from typing import Dict, Any
import yaml


class SentimentAnalyzer:
    """
    Analyseur de sentiment basé sur BERT multilingue
    
    Ce modèle peut analyser des textes en français, anglais, arabe et autres langues.
    Il retourne un sentiment (positif/négatif/neutre) avec un score de confiance.
    
    Architecture :
    - Tokenizer : Découpe le texte en tokens (morceaux)
    - Modèle BERT : Analyse le sentiment
    - Softmax : Convertit les scores en probabilités
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialise l'analyseur de sentiment
        
        Args:
            config_path (str): Chemin vers le fichier config.yaml
                              Si None, utilise la config par défaut
        
        Étapes d'initialisation :
        1. Charger la configuration
        2. Charger le tokenizer (découpage des mots)
        3. Charger le modèle BERT pré-entraîné
        4. Définir le mapping des labels
        """
        print("🔧 Initialisation de l'analyseur de sentiment...")
        
        # Étape 1 : Charger la configuration
        if config_path:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                self.config = config['approach1']
        else:
            # Configuration par défaut si pas de fichier
            self.config = {
                'model_name': 'nlptown/bert-base-multilingual-uncased-sentiment',
                'max_length': 512,
                'confidence_threshold': 0.6
            }
        
        # Étape 2 : Charger le tokenizer
        # Le tokenizer découpe le texte en tokens (morceaux)
        # Exemple : "Je suis content" → ["Je", "suis", "content"]
        print(f"📥 Chargement du tokenizer : {self.config['model_name']}")
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.config['model_name']
        )
        
        # Étape 3 : Charger le modèle BERT pré-entraîné
        # Ce modèle a déjà été entraîné sur des millions de textes !
        print(f"📥 Chargement du modèle BERT...")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.config['model_name']
        )
        
        # Mettre le modèle en mode évaluation (pas d'entraînement)
        self.model.eval()
        
        # Étape 4 : Définir le mapping des labels
        # Le modèle retourne des chiffres (0-4), on les convertit en sentiments
        self.label_mapping = {
            0: 'très négatif',
            1: 'négatif',
            2: 'neutre',
            3: 'positif',
            4: 'très positif'
        }
        
        # Simplification en 3 catégories principales
        self.simplified_mapping = {
            0: 'négatif',
            1: 'négatif',
            2: 'neutre',
            3: 'positif',
            4: 'positif'
        }
        
        print("✅ Analyseur de sentiment prêt !\n")
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Analyse le sentiment d'un texte
        
        Args:
            text (str): Le texte à analyser (peut être en FR, EN, AR, etc.)
        
        Returns:
            dict: Dictionnaire contenant :
                - sentiment (str): 'positif', 'négatif', ou 'neutre'
                - sentiment_detail (str): Version détaillée (ex: 'très positif')
                - confidence (float): Score de confiance (0-1)
                - confidence_percent (float): Score en pourcentage (0-100)
                - all_scores (dict): Tous les scores pour chaque catégorie
                - text_length (int): Longueur du texte analysé
        
        Processus :
        1. Tokenization : Découper le texte
        2. Conversion en tenseurs PyTorch
        3. Passage dans le modèle BERT
        4. Softmax pour obtenir des probabilités
        5. Interprétation des résultats
        """
        # Validation de l'entrée
        if not text or not text.strip():
            return {
                'sentiment': 'neutre',
                'sentiment_detail': 'neutre',
                'confidence': 0.0,
                'confidence_percent': 0.0,
                'all_scores': {},
                'text_length': 0,
                'error': 'Texte vide'
            }
        
        # Étape 1 : TOKENIZATION
        # Découper le texte en tokens que BERT peut comprendre
        # padding=True : Ajoute des tokens spéciaux pour atteindre max_length
        # truncation=True : Coupe le texte s'il est trop long
        # return_tensors='pt' : Retourne des tenseurs PyTorch
        inputs = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            max_length=self.config['max_length'],
            return_tensors='pt'  # 'pt' = PyTorch tensors
        )
        
        # Étape 2 : PRÉDICTION avec BERT
        # torch.no_grad() : Désactive le calcul des gradients (on n'entraîne pas)
        # Économise de la mémoire et accélère le calcul
        with torch.no_grad():
            # Passer les tokens dans le modèle BERT
            outputs = self.model(**inputs)
            
            # Récupérer les logits (scores bruts avant softmax)
            logits = outputs.logits
            
            # Étape 3 : SOFTMAX
            # Convertir les logits en probabilités qui somment à 1
            # Exemple : [-2.1, 0.5, 3.2] → [0.01, 0.12, 0.87]
            probabilities = torch.softmax(logits, dim=1)
            
            # Étape 4 : TROUVER LA PRÉDICTION
            # torch.argmax : Trouve l'indice du score maximum
            predicted_class = torch.argmax(probabilities, dim=1).item()
            
            # Récupérer le score de confiance pour cette prédiction
            confidence = probabilities[0][predicted_class].item()
        
        # Étape 5 : FORMATER LES RÉSULTATS
        
        # Créer un dictionnaire avec tous les scores
        all_scores = {}
        for i, label in self.label_mapping.items():
            all_scores[label] = float(probabilities[0][i].item())
        
        # Récupérer le sentiment détaillé et simplifié
        sentiment_detail = self.label_mapping[predicted_class]
        sentiment_simple = self.simplified_mapping[predicted_class]
        
        # Construire le résultat final
        result = {
            'sentiment': sentiment_simple,
            'sentiment_detail': sentiment_detail,
            'confidence': round(confidence, 3),
            'confidence_percent': round(confidence * 100, 1),
            'all_scores': all_scores,
            'text_length': len(text),
            'predicted_class': predicted_class
        }
        
        return result
    
    def analyze_batch(self, texts: list) -> list:
        """
        Analyse plusieurs textes en même temps (plus efficace)
        
        Args:
            texts (list): Liste de textes à analyser
        
        Returns:
            list: Liste de dictionnaires de résultats
        """
        results = []
        for text in texts:
            results.append(self.analyze(text))
        return results
    
    def get_emotion_interpretation(self, result: Dict[str, Any]) -> str:
        """
        Génère une interprétation textuelle du sentiment
        
        Args:
            result (dict): Résultat de la méthode analyze()
        
        Returns:
            str: Interprétation en langage naturel
        """
        sentiment = result['sentiment']
        confidence = result['confidence_percent']
        
        # Interprétations selon le sentiment et la confiance
        if sentiment == 'positif':
            if confidence > 80:
                return "Tu sembles vraiment de bonne humeur ! 😊"
            elif confidence > 60:
                return "Tu as l'air plutôt positif aujourd'hui 🙂"
            else:
                return "Il y a une touche de positivité dans ton message"
        
        elif sentiment == 'négatif':
            if confidence > 80:
                return "Je sens que tu traverses un moment difficile 😔"
            elif confidence > 60:
                return "Tu n'as pas l'air dans ton assiette..."
            else:
                return "Il y a une petite nuance négative"
        
        else:  # neutre
            return "Ton message est plutôt neutre, ni très positif ni négatif"
    
    def is_confident(self, result: Dict[str, Any]) -> bool:
        """
        Vérifie si l'analyse est suffisamment confiante
        
        Args:
            result (dict): Résultat de la méthode analyze()
        
        Returns:
            bool: True si la confiance dépasse le seuil
        """
        threshold = self.config['confidence_threshold']
        return result['confidence'] >= threshold


# ============================================
# FONCTION DE TEST / DÉMO
# ============================================

def demo():
    """
    Fonction de démonstration de l'analyseur de sentiment
    Teste avec différentes phrases en français
    """
    print("=" * 60)
    print("🤖 DÉMONSTRATION - ANALYSEUR DE SENTIMENT")
    print("=" * 60)
    print()
    
    # Créer l'analyseur
    analyzer = SentimentAnalyzer()
    
    # Phrases de test
    test_phrases = [
        "Je suis vraiment heureux aujourd'hui !",
        "Je me sens triste et seul...",
        "Le temps est nuageux",
        "Je déteste tout ça, c'est horrible",
        "C'était une journée normale, ni bien ni mal",
        "J'adore cette application, elle est géniale ! 😊",
        "Je ne sais pas quoi faire, je suis perdu",
        "La vie est belle",
        "Je suis malade et fatigué",    
        "C'est mieux que jamais"
    ]
    
    # Analyser chaque phrase
    for i, phrase in enumerate(test_phrases, 1):
        print(f"\n📝 Test {i} : \"{phrase}\"")
        print("-" * 60)
        
        result = analyzer.analyze(phrase)
        
        print(f"   Sentiment : {result['sentiment'].upper()} ({result['sentiment_detail']})")
        print(f"   Confiance : {result['confidence_percent']}%")
        print(f"   Interprétation : {analyzer.get_emotion_interpretation(result)}")
        print(f"   Fiable ? {'✅ Oui' if analyzer.is_confident(result) else '⚠️ Incertain'}")
        
        # Afficher tous les scores
        print(f"\n   Détail des scores :")
        for label, score in result['all_scores'].items():
            bar_length = int(score * 30)
            bar = "█" * bar_length
            print(f"      {label:15} : {bar} {score*100:.1f}%")
    
    print("\n" + "=" * 60)
    print("✅ Démonstration terminée !")
    print("=" * 60)


# Point d'entrée si on exécute ce fichier directement
if __name__ == "__main__":
    demo()
