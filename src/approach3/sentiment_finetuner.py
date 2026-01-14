"""
Fine-tuning BERT pour l'analyse de sentiment bien-être
Entraîne un modèle BERT spécialisé sur les données bien-être
"""

import torch
import numpy as np
from typing import List, Dict, Tuple
from pathlib import Path
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from torch.utils.data import Dataset


class WellbeingDataset(Dataset):
    """
    Dataset PyTorch pour le fine-tuning BERT
    Convertit les textes en tokens que BERT comprend
    """
    
    def __init__(self, texts: List[str], labels: List[int], 
                 tokenizer, max_length: int = 128):
        """
        Initialise le dataset
        
        Args:
            texts (list): Liste de textes à analyser
            labels (list): Liste d'IDs de sentiments (0-4)
            tokenizer: Tokenizer BERT pour convertir texte → nombres
            max_length (int): Longueur max des séquences (default: 128)
        """
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self) -> int:
        """Retourne le nombre d'exemples"""
        return len(self.texts)
    
    def __getitem__(self, idx: int) -> Dict:
        """
        Récupère et traite un exemple
        
        Args:
            idx (int): Index de l'exemple
            
        Returns:
            dict: Dictionnaire avec input_ids, attention_mask, labels
        """
        text = self.texts[idx]
        label = self.labels[idx]
        
        # 🔑 TOKENIZATION : Convertir le texte en nombres
        # "Je suis heureux" → [1234, 5678, 9012]
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,      # Tronquer si trop long
            padding='max_length',             # Padder à max_length
            truncation=True,                  # Couper si > max_length
            return_tensors='pt'               # Retourner en PyTorch tensors
        )
        
        return {
            'input_ids': encoding['input_ids'].squeeze(),           # [0, 1, 2, ..., 128]
            'attention_mask': encoding['attention_mask'].squeeze(), # [1, 1, 1, ..., 0]
            'labels': torch.tensor(label, dtype=torch.long)         # 0-4
        }


class BERTFineTuner:
    """
    Fine-tune BERT pour analyser les sentiments bien-être
    
    Processus :
    1. Charger BERT multilingual pré-entraîné
    2. Créer datasets d'entraînement et validation
    3. Fine-tuner les poids avec learning_rate très faible
    4. Évaluer et sauvegarder le meilleur modèle
    """
    
    # Mapping sentiment → ID (5 classes)
    SENTIMENT_MAP = {
        0: 'très négatif',
        1: 'négatif',
        2: 'neutre',
        3: 'positif',
        4: 'très positif'
    }
    
    def __init__(self, model_name: str = 'bert-base-multilingual-uncased',
                 output_dir: str = 'models/approach3/bert_finetuned'):
        """
        Initialise le fine-tuner
        
        Args:
            model_name (str): Nom du modèle BERT (de HuggingFace)
            output_dir (str): Répertoire pour sauvegarder le modèle
        """
        print(f"\n🔧 Chargement de {model_name}...")
        
        # Créer le répertoire de sortie
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        self.output_dir = output_dir
        
        # ✅ Charger le tokenizer BERT
        # Il convertira nos textes en IDs de tokens
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        print(f"   ✅ Tokenizer chargé")
        
        # ✅ Charger le modèle BERT MODIFIABLE (pas gelé)
        # num_labels=5 car nous avons 5 classes de sentiments
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=5  # très négatif, négatif, neutre, positif, très positif
        )
        print(f"   ✅ Modèle BERT chargé (110M paramètres)")
        
        # Vérifier GPU
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        print(f"   ✅ Device: {self.device}")
        
        print(f"✅ Fine-tuner prêt!")
    
    def train(self, 
              train_texts: List[str], 
              train_labels: List[int],
              val_texts: List[str], 
              val_labels: List[int],
              epochs: int = 3,
              batch_size: int = 8,
              learning_rate: float = 2e-5):
        """
        Fine-tune BERT sur nos données bien-être
        
        Args:
            train_texts (list): Textes d'entraînement
            train_labels (list): Sentiments d'entraînement (0-4)
            val_texts (list): Textes de validation
            val_labels (list): Sentiments de validation (0-4)
            epochs (int): Nombre d'epochs d'entraînement
            batch_size (int): Taille du batch
            learning_rate (float): Learning rate (default: 2e-5 pour fine-tuning)
        """
        
        print(f"\n🔥 FINE-TUNING BERT")
        print("=" * 60)
        print(f"📊 Données:")
        print(f"   Train  : {len(train_texts)} exemples")
        print(f"   Validation : {len(val_texts)} exemples")
        print(f"⚙️  Configuration:")
        print(f"   Epochs : {epochs}")
        print(f"   Batch size : {batch_size}")
        print(f"   Learning rate : {learning_rate}")
        print("=" * 60)
        
        # ✅ Créer les datasets PyTorch
        train_dataset = WellbeingDataset(
            train_texts, train_labels, 
            self.tokenizer,
            max_length=128
        )
        val_dataset = WellbeingDataset(
            val_texts, val_labels, 
            self.tokenizer,
            max_length=128
        )
        
        # ✅ Configurer les arguments d'entraînement
        training_args = TrainingArguments(
            # Répertoire de sortie
            output_dir=self.output_dir,
            
            # Entraînement
            num_train_epochs=epochs,                          # Nombre d'epochs
            per_device_train_batch_size=batch_size,          # Batch size
            per_device_eval_batch_size=batch_size,
            learning_rate=learning_rate,                     # 🔑 2e-5 pour fine-tuning!
            
            # Évaluation
            eval_strategy='epoch',                            # Évaluer à chaque epoch
            save_strategy='epoch',                            # Sauvegarder à chaque epoch
            
            # Optimization
            weight_decay=0.01,                                # Régularisation L2
            
            # Early stopping
            load_best_model_at_end=True,                      # Charger le meilleur modèle
            metric_for_best_model='eval_loss',
            greater_is_better=False,
            
            # Logging
            logging_dir='./logs',
            logging_steps=10,
            
            # Autres
            seed=42,
        )
        
        # ✅ Créer le Trainer (classe HuggingFace qui gère tout)
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
        )
        
        # 🚀 LANCER L'ENTRAÎNEMENT (modifie les poids de BERT)
        print(f"\n▶️  Lancement du fine-tuning...")
        trainer.train()
        
        # ✅ Sauvegarder le meilleur modèle
        trainer.save_model(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)
        print(f"✅ Modèle sauvegardé dans : {self.output_dir}")
        
        return trainer
    
    def predict(self, text: str) -> Dict:
        """
        Utilise le modèle fine-tuné pour prédire le sentiment
        
        Args:
            text (str): Texte à analyser
            
        Returns:
            dict: Sentiment, confiance, et tous les scores
        """
        # Tokenize le texte
        inputs = self.tokenizer(
            text,
            return_tensors='pt',
            padding=True,
            truncation=True,
            max_length=128
        )
        
        # Placer sur le même device que le modèle
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Prédire (sans calcul de gradient)
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Récupérer les logits et les convertir en probabilités
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1)
        
        # Trouver la classe avec la plus haute probabilité
        predicted_id = torch.argmax(probabilities).item()
        confidence = probabilities[0, predicted_id].item()
        
        return {
            'sentiment': self.SENTIMENT_MAP[predicted_id],
            'sentiment_id': predicted_id,
            'confidence': confidence,
            'all_scores': {
                self.SENTIMENT_MAP[i]: probabilities[0, i].item()
                for i in range(5)
            }
        }
    
    def predict_batch(self, texts: List[str]) -> List[Dict]:
        """
        Prédire sur plusieurs textes
        
        Args:
            texts (list): Liste de textes
            
        Returns:
            list: Résultats pour chaque texte
        """
        return [self.predict(text) for text in texts]


# ============================================================================
# Script de test
# ============================================================================

if __name__ == '__main__':
    # Test d'import seulement
    print("✅ Module sentiment_finetuner.py chargé avec succès")
    print("   Prêt à fine-tuner BERT!")
