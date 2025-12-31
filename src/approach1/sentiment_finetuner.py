"""
🎯 Fine-tuning de BERT pour l'Analyse de Sentiment - Approche 1 bis
====================================================================

Ce module implémente le FINE-TUNING de BERT sur des données
spécifiques au bien-être mental.

Différence avec l'approche actuelle (Feature Extraction) :
- Feature Extraction : On utilise BERT tel quel (poids gelés)
- Fine-tuning : On réentraîne BERT sur nos données (poids modifiables)

Avantages du Fine-tuning :
✅ Meilleure précision sur notre domaine
✅ Comprend le vocabulaire spécifique (bien-être, anxiété, etc.)
✅ S'adapte aux nuances de notre contexte

Inconvénients :
❌ Nécessite des données d'entraînement (500+ exemples)
❌ Plus lent (1-3h d'entraînement)
❌ Besoin de GPU (recommandé)

Auteur : Étudiant ENSA Berrechid
Module : Programmation Python et IA
"""

import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    EarlyStoppingCallback
)
from torch.utils.data import Dataset
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
import os
from datetime import datetime


# ============================================================
# DATASET PERSONNALISÉ
# ============================================================

class WellbeingDataset(Dataset):
    """
    Dataset PyTorch pour le fine-tuning BERT.
    
    Prépare les données dans le format attendu par le Trainer.
    
    Structure :
    - Textes : Les messages utilisateur
    - Labels : Les sentiments (0=très négatif, 4=très positif)
    - Tokenization : Conversion en tokens BERT
    """
    
    def __init__(self, texts: List[str], labels: List[int], tokenizer, max_length: int = 128):
        """
        Initialise le dataset.
        
        Args:
            texts: Liste des textes à classifier
            labels: Liste des labels (0-4)
            tokenizer: Tokenizer BERT
            max_length: Longueur maximale des séquences
        """
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        """Retourne le nombre d'exemples."""
        return len(self.texts)
    
    def __getitem__(self, idx):
        """
        Retourne un exemple tokenisé.
        
        Process :
        1. Prendre le texte et le label
        2. Tokeniser le texte
        3. Retourner au format attendu par BERT
        """
        text = str(self.texts[idx])
        label = self.labels[idx]
        
        # Tokenization avec padding et truncation
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        # Retourner un dictionnaire
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }


# ============================================================
# CLASSE PRINCIPALE DE FINE-TUNING
# ============================================================

class BERTFineTuner:
    """
    Classe pour fine-tuner BERT sur des données de bien-être mental.
    
    Fonctionnalités :
    - Charger un modèle BERT de base
    - Fine-tuner sur des données custom
    - Sauvegarder et charger le modèle ajusté
    - Évaluer les performances
    - Comparer avec Feature Extraction
    """
    
    def __init__(self, 
                 model_name: str = 'bert-base-multilingual-uncased',
                 num_labels: int = 5,
                 output_dir: str = './models/finetuned'):
        """
        Initialise le fine-tuner.
        
        Args:
            model_name: Nom du modèle de base à fine-tuner
            num_labels: Nombre de classes (5 sentiments)
            output_dir: Dossier de sauvegarde
        """
        print("🔧 Initialisation du Fine-Tuner BERT...")
        print(f"   📦 Modèle de base : {model_name}")
        print(f"   🎯 Nombre de classes : {num_labels}")
        
        self.model_name = model_name
        self.num_labels = num_labels
        self.output_dir = output_dir
        
        # Charger le tokenizer
        print("📥 Chargement du tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Charger le modèle
        print("📥 Chargement du modèle BERT...")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=num_labels
        )
        
        # Vérifier si GPU disponible
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"   💻 Device : {self.device}")
        
        if self.device.type == 'cpu':
            print("   ⚠️  Pas de GPU détecté - L'entraînement sera plus lent")
        else:
            print("   ✅ GPU disponible - Entraînement rapide !")
        
        self.model.to(self.device)
        
        print("✅ Fine-Tuner prêt !\n")
    
    def prepare_data(self, 
                     texts: List[str], 
                     labels: List[int],
                     val_split: float = 0.2) -> Tuple[Dataset, Dataset]:
        """
        Prépare les données pour l'entraînement.
        
        Args:
            texts: Liste des textes
            labels: Liste des labels
            val_split: Proportion pour validation (0.2 = 20%)
        
        Returns:
            train_dataset, val_dataset
        
        Process :
        1. Convertir les labels texte en numérique si besoin
        2. Split train/validation
        3. Créer les datasets PyTorch
        """
        print(f"📊 Préparation des données...")
        print(f"   • Total exemples : {len(texts)}")
        
        # Mélanger les données
        indices = np.random.permutation(len(texts))
        texts = [texts[i] for i in indices]
        labels = [labels[i] for i in indices]
        
        # Split train/val
        split_idx = int(len(texts) * (1 - val_split))
        
        train_texts = texts[:split_idx]
        train_labels = labels[:split_idx]
        
        val_texts = texts[split_idx:]
        val_labels = labels[split_idx:]
        
        print(f"   • Entraînement : {len(train_texts)}")
        print(f"   • Validation : {len(val_texts)}")
        
        # Créer les datasets
        train_dataset = WellbeingDataset(train_texts, train_labels, self.tokenizer)
        val_dataset = WellbeingDataset(val_texts, val_labels, self.tokenizer)
        
        print("✅ Données préparées !\n")
        
        return train_dataset, val_dataset
    
    def train(self,
              train_dataset: Dataset,
              val_dataset: Dataset,
              epochs: int = 3,
              batch_size: int = 8,
              learning_rate: float = 2e-5,
              warmup_steps: int = 500):
        """
        Fine-tune le modèle sur les données.
        
        Args:
            train_dataset: Dataset d'entraînement
            val_dataset: Dataset de validation
            epochs: Nombre d'epochs
            batch_size: Taille du batch
            learning_rate: Taux d'apprentissage
            warmup_steps: Étapes de warmup
        
        Process :
        1. Configurer les arguments d'entraînement
        2. Créer le Trainer
        3. Lancer le fine-tuning
        4. Sauvegarder le modèle
        """
        print("=" * 60)
        print("🎯 DÉBUT DU FINE-TUNING")
        print("=" * 60)
        print(f"\n⚙️  Configuration :")
        print(f"   • Epochs : {epochs}")
        print(f"   • Batch size : {batch_size}")
        print(f"   • Learning rate : {learning_rate}")
        print(f"   • Warmup steps : {warmup_steps}")
        print(f"   • Device : {self.device}")
        print()
        
        # Configuration de l'entraînement
        training_args = TrainingArguments(
            output_dir=self.output_dir,
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            learning_rate=learning_rate,
            warmup_steps=warmup_steps,
            weight_decay=0.01,
            logging_dir=f'{self.output_dir}/logs',
            logging_steps=10,
            evaluation_strategy='epoch',
            save_strategy='epoch',
            load_best_model_at_end=True,
            metric_for_best_model='eval_loss',
            greater_is_better=False,
            save_total_limit=2,  # Garder seulement les 2 meilleurs modèles
            report_to='none'  # Désactiver wandb, tensorboard, etc.
        )
        
        # Créer le Trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
        )
        
        # 🔥 FINE-TUNING - Les poids de BERT changent !
        print("🚀 Lancement de l'entraînement...\n")
        start_time = datetime.now()
        
        train_result = trainer.train()
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print("\n" + "=" * 60)
        print("✅ FINE-TUNING TERMINÉ !")
        print("=" * 60)
        print(f"⏱️  Durée totale : {duration/60:.2f} minutes")
        print(f"📈 Loss finale : {train_result.training_loss:.4f}")
        
        # Sauvegarder le modèle
        print(f"\n💾 Sauvegarde du modèle dans {self.output_dir}...")
        self.model.save_pretrained(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)
        
        print("✅ Modèle sauvegardé !")
        print()
        
        return trainer
    
    def evaluate(self, val_dataset: Dataset) -> Dict:
        """
        Évalue le modèle fine-tuné.
        
        Args:
            val_dataset: Dataset de validation
        
        Returns:
            Métriques d'évaluation
        """
        print("📊 Évaluation du modèle...\n")
        
        # Créer un trainer pour l'évaluation
        trainer = Trainer(
            model=self.model,
            eval_dataset=val_dataset
        )
        
        # Évaluer
        metrics = trainer.evaluate()
        
        print("📈 Résultats :")
        for key, value in metrics.items():
            print(f"   • {key}: {value:.4f}")
        
        return metrics
    
    def load_finetuned_model(self, model_path: str):
        """
        Charge un modèle déjà fine-tuné.
        
        Args:
            model_path: Chemin vers le modèle sauvegardé
        """
        print(f"📥 Chargement du modèle fine-tuné depuis {model_path}...")
        
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model.to(self.device)
        
        print("✅ Modèle chargé !")
    
    def predict(self, text: str) -> Dict:
        """
        Fait une prédiction avec le modèle fine-tuné.
        
        Args:
            text: Texte à analyser
        
        Returns:
            Dictionnaire avec sentiment et confiance
        """
        # Tokeniser
        inputs = self.tokenizer(
            text,
            return_tensors='pt',
            max_length=128,
            padding='max_length',
            truncation=True
        )
        
        # Déplacer sur le bon device
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Prédiction
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Interpréter les résultats
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1)
        predicted_class = torch.argmax(probs, dim=1).item()
        confidence = probs[0][predicted_class].item()
        
        # Mapping des labels
        sentiment_map = {
            0: 'très négatif',
            1: 'négatif',
            2: 'neutre',
            3: 'positif',
            4: 'très positif'
        }
        
        return {
            'sentiment': sentiment_map[predicted_class],
            'predicted_class': predicted_class,
            'confidence': confidence,
            'all_scores': probs[0].cpu().numpy().tolist()
        }


# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================

def create_sample_dataset() -> Tuple[List[str], List[int]]:
    """
    Crée un dataset d'exemple pour tester le fine-tuning.
    
    En production, tu devrais :
    - Collecter de vraies données
    - Annoter manuellement
    - Utiliser des datasets publics
    
    Returns:
        texts, labels
    """
    print("📝 Création d'un dataset d'exemple...\n")
    
    # Dataset d'exemple sur le bien-être mental
    data = [
        # Très positif (4)
        ("Je me sens incroyablement bien aujourd'hui !", 4),
        ("Quelle joie de vivre, je suis épanoui !", 4),
        ("J'ai réussi à surmonter mon anxiété, je suis fier !", 4),
        ("La thérapie m'aide énormément, je vais beaucoup mieux !", 4),
        ("Je suis en paix avec moi-même, c'est merveilleux !", 4),
        
        # Positif (3)
        ("Je me sens bien, ça va mieux qu'hier", 3),
        ("La méditation m'aide à me relaxer", 3),
        ("J'ai passé une bonne journée, je suis content", 3),
        ("Je commence à voir du positif dans ma vie", 3),
        ("Mes proches me soutiennent beaucoup", 3),
        
        # Neutre (2)
        ("Je suis allé me promener aujourd'hui", 2),
        ("J'ai lu un livre sur la psychologie", 2),
        ("Il fait beau dehors", 2),
        ("J'ai pris mes médicaments ce matin", 2),
        ("J'ai rendez-vous chez le médecin demain", 2),
        
        # Négatif (1)
        ("Je me sens stressé par le travail", 1),
        ("J'ai du mal à dormir ces derniers temps", 1),
        ("L'anxiété revient souvent", 1),
        ("Je me sens fatigué et démotivé", 1),
        ("C'est difficile en ce moment", 1),
        
        # Très négatif (0)
        ("Je me sens complètement désespéré", 0),
        ("Je n'arrive plus à gérer mon anxiété", 0),
        ("Je me sens seul et incompris", 0),
        ("Rien ne va, je suis au bout du rouleau", 0),
        ("Je n'ai plus d'énergie pour continuer", 0),
    ]
    
    texts = [item[0] for item in data]
    labels = [item[1] for item in data]
    
    print(f"✅ Dataset créé : {len(texts)} exemples")
    print(f"   • Distribution des classes :")
    for i in range(5):
        count = labels.count(i)
        print(f"     - Classe {i}: {count} exemples")
    print()
    
    return texts, labels


# ============================================================
# SCRIPT D'EXEMPLE
# ============================================================

def main():
    """
    Script d'exemple pour le fine-tuning.
    """
    print("\n" + "=" * 60)
    print("🎯 FINE-TUNING DE BERT POUR LE BIEN-ÊTRE MENTAL")
    print("=" * 60)
    print()
    
    # 1. Créer des données d'exemple
    texts, labels = create_sample_dataset()
    
    # 2. Initialiser le fine-tuner
    finetuner = BERTFineTuner(
        model_name='bert-base-multilingual-uncased',
        num_labels=5,
        output_dir='./models/finetuned_wellbeing'
    )
    
    # 3. Préparer les données
    train_dataset, val_dataset = finetuner.prepare_data(texts, labels, val_split=0.2)
    
    # 4. Fine-tuner le modèle
    trainer = finetuner.train(
        train_dataset=train_dataset,
        val_dataset=val_dataset,
        epochs=3,
        batch_size=4,  # Petit batch pour CPU
        learning_rate=2e-5
    )
    
    # 5. Évaluer
    metrics = finetuner.evaluate(val_dataset)
    
    # 6. Tester quelques prédictions
    print("\n" + "=" * 60)
    print("🧪 TESTS DE PRÉDICTION")
    print("=" * 60)
    print()
    
    test_phrases = [
        "Je me sens vraiment bien aujourd'hui !",
        "Je suis anxieux pour mon avenir",
        "Il fait beau"
    ]
    
    for phrase in test_phrases:
        result = finetuner.predict(phrase)
        print(f"📝 \"{phrase}\"")
        print(f"   → {result['sentiment']} ({result['confidence']:.2%})")
        print()
    
    print("✅ Fine-tuning terminé avec succès !")
    print(f"💾 Modèle sauvegardé dans : ./models/finetuned_wellbeing")


if __name__ == "__main__":
    main()
