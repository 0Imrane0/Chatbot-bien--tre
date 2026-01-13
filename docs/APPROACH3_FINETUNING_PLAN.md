# 🤖 Prompt pour GitHub Copilot Pro - Chatbot de Bien-être (V2 - MISE À JOUR)

## 📋 CONTEXTE DU PROJET

Je suis étudiant ingénieur en Ingénierie des Systèmes d'Information et Big Data à l'ENSA Berrechid. Je dois réaliser un projet de **Chatbot de Bien-être et d'Humeur** dans le cadre de mon module "Programmation Python et IA".

**Objectif :** Créer un chatbot conversationnel qui :
- Analyse le sentiment des messages utilisateur
- Suit l'évolution de l'humeur dans le temps
- Donne des conseils personnalisés
- Maintient une conversation empathique

**Important :** Je veux **comprendre** chaque étape, pas seulement avoir le code. Je veux apprendre en construisant !

---

## 🎯 INSTRUCTIONS POUR COPILOT

### Principes à respecter :

1. **Approche pédagogique** : Explique-moi CHAQUE concept avant de coder
2. **Progression étape par étape** : Ne passe à l'étape suivante qu'après mon approbation
3. **Code commenté** : Chaque ligne importante doit avoir un commentaire explicatif
4. **Questions de compréhension** : Pose-moi des questions pour vérifier ma compréhension
5. **Trois implémentations complètes** :
   - **Approche 1** : Modèle pré-entraîné BERT (Feature Extraction) - ✅ COMPLÉTÉE
   - **Approche 3** : Fine-tuning de BERT sur données bien-être - À FAIRE (PRIORITAIRE)
   - **Approche 2** : Modèle custom LSTM/GRU - À FAIRE (ensuite)

---

## 📊 STATUT DU PROJET (13 Janvier 2026)

### ✅ APPROCHE 1 - COMPLÉTÉE À 100%
```
PHASE 1-6 : TERMINÉE
✅ Sentiment Analyzer (BERT Feature Extraction)
✅ Mood Tracker (historique + tendances)
✅ Response Generator (réponses empathiques)
✅ Mood Visualizer (graphiques Plotly)
✅ Interface Web Streamlit
✅ Interface Console
✅ 23 tests unitaires (TOUS PASSANTS)
✅ Documentation complète
```

### 🔥 APPROCHE 3 - PRIORITAIRE (À FAIRE)
```
PHASE 3B : À COMMENCER
[ ] Fine-tuning BERT sur données bien-être
[ ] Données d'entraînement
[ ] Entraînement & sauvegarde
[ ] Comparaison avec Approche 1
[ ] Tests & intégration
```

### 🚀 APPROCHE 2 - FUTURE (À FAIRE APRÈS APPROCHE 3)
```
PHASE 7-12 : À FAIRE APRÈS APPROCHE 3
[ ] Data Preparation
[ ] Model Builder (LSTM/GRU)
[ ] Model Trainer
[ ] Integration
[ ] Tests
```

---

## 🗂️ STRUCTURE DU PROJET (MISE À JOUR)

```
Chatbot bien-être/
│
├── data/                          # Données et historiques
│   ├── mood_history.json          # Suivi de l'humeur (tous utilisateurs)
│   ├── mood_test.json             # Données de test
│   ├── training_wellbeing_data.json  # Données pour fine-tuning (Approche 3)
│   └── training_data.csv          # Données pour modèle custom (Approche 2)
│
├── models/                        # Modèles sauvegardés
│   ├── approach1/                 # Approche 1 : BERT Pré-entraîné
│   │   └── bert_pretrained/       # BERT original (depuis HuggingFace)
│   │
│   ├── approach3/                 # Approche 3 : BERT Fine-tuné
│   │   └── bert_finetuned/        # BERT ajusté sur données bien-être
│   │       ├── config.json
│   │       ├── pytorch_model.bin
│   │       └── tokenizer files
│   │
│   └── approach2/                 # Approche 2 : Custom LSTM/GRU
│       ├── lstm_model.h5
│       └── preprocessor.pkl
│
├── src/                           # Code source
│   ├── __init__.py
│   │
│   ├── approach1/                 # ✅ Approche 1 : Feature Extraction (COMPLÉTÉE)
│   │   ├── __init__.py
│   │   ├── sentiment_analyzer.py  # Utilise BERT pré-entraîné (gelé)
│   │   ├── mood_tracker.py        # Suivi de l'humeur
│   │   ├── response_generator.py  # Génération de réponses
│   │   ├── mood_visualizer.py     # Graphiques Plotly
│   │   ├── chatbot.py             # Orchestrateur principal
│   │   └── data/
│   │       └── mood_history.json  # Historique utilisateur
│   │
│   ├── approach3/                 # 🔥 Approche 3 : Fine-tuning BERT (À FAIRE)
│   │   ├── __init__.py
│   │   ├── sentiment_finetuner.py # Entraînement BERT (NOUVEAU)
│   │   ├── sentiment_analyzer.py  # Analyse avec BERT fine-tuné
│   │   ├── mood_tracker.py        # Suivi (réutilisé d'Approche 1)
│   │   ├── response_generator.py  # Réponses (réutilisé d'Approche 1)
│   │   ├── mood_visualizer.py     # Graphiques (réutilisé d'Approche 1)
│   │   ├── chatbot.py             # Orchestrateur
│   │   └── data/
│   │       └── training_wellbeing_data.json
│   │
│   └── approach2/                 # 🚀 Approche 2 : Custom LSTM/GRU (À FAIRE APRÈS)
│       ├── __init__.py
│       ├── data_preparation.py    # Préparation des données
│       ├── model_builder.py       # Construction du réseau LSTM
│       ├── model_trainer.py       # Entraînement
│       ├── sentiment_analyzer.py  # Analyse avec modèle custom
│       ├── mood_tracker.py        # Suivi (réutilisé)
│       ├── response_generator.py  # Réponses (réutilisé)
│       ├── mood_visualizer.py     # Graphiques (réutilisé)
│       ├── chatbot.py             # Orchestrateur
│       └── data/
│           └── training_data.csv  # Données pour entraînement
│
├── tests/                         # Tests unitaires
│   ├── test_approach1.py          # ✅ Tests Approche 1 (23 tests PASSANTS)
│   ├── test_approach3.py          # Tests Approche 3 (À CRÉER)
│   └── test_approach2.py          # Tests Approche 2 (À CRÉER)
│
├── notebooks/                     # Jupyter notebooks (exploration)
│   ├── 01_exploration_data.ipynb  # Exploration données
│   ├── 02_finetuning_bert.ipynb   # Fine-tuning analysis (À CRÉER)
│   ├── 03_model_comparison.ipynb  # Comparaison 3 approches (À CRÉER)
│   └── 04_analysis_results.ipynb  # Résultats finaux (À CRÉER)
│
├── ui/                            # Interfaces utilisateur
│   ├── console_ui.py              # Interface console
│   └── streamlit_ui.py            # Interface web (déjà fonctionnelle)
│
├── docs/                          # Documentation
│   ├── copilot-prompt.md          # Prompt original (CE FICHIER)
│   └── rapport.md                 # Rapport du projet
│
├── .git/                          # Version control
├── .gitignore                     # Fichiers à ignorer
├── venv/                          # Environnement virtuel Python
├── launch_menu.bat                # Lanceur unique (Windows)
├── main.py                        # Point d'entrée principal
├── compare_approaches.py          # Comparaison des 3 approches
├── config.yaml                    # Configuration globale
├── requirements.txt               # Dépendances Python
├── setup_nltk.py                  # Configuration NLTK
├── README.md                      # Documentation utilisateur
└── PROJECT_STRUCTURE.md           # Documentationen techniques complète
```

---

## 📊 COMPARAISON DES 3 APPROCHES

| Critère | Approche 1 (Feature) | Approche 3 (Fine-tuning) | Approche 2 (Custom) |
|---------|----------------------|--------------------------|---------------------|
| **Concept** | BERT gelé | BERT modifié | Réseau custom |
| **Entraînement** | ❌ Zéro | ✅ 5-10 min | ✅ 30-60 min |
| **Données** | 100-200 | 500-1000 | 1000-5000 |
| **Performance** | ~82% | ~91% | ~85-90% |
| **Temps/réponse** | ⚡ 0.3 sec | 0.5 sec | 🐢 1-2 sec |
| **Mémoire** | 500 MB | 2.5 GB | 3-5 GB |
| **GPU** | ❌ Non | ⭐ Optionnel | ⭐ Recommandé |
| **Meilleur pour** | Prototypes | Production | Recherche/custom |
| **Facilité** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Code** | Simple | Modéré | Complexe |

---

# 🚀 PLAN D'EXÉCUTION - APPROCHE 1 (✅ COMPLÉTÉE)

**STATUS:** Phase 1-6 terminées à 100%
- ✅ Sentiment Analyzer avec BERT (Feature Extraction)
- ✅ Mood Tracker & Visualizations
- ✅ Response Generator
- ✅ Interface Web & Console
- ✅ 23 tests unitaires passants
- ✅ Documentation complète

**NE RIEN MODIFIER dans Approche 1 - elle fonctionne parfaitement!**

---

# 🔥 PLAN D'EXÉCUTION - APPROCHE 3 : FINE-TUNING BERT (PRIORITAIRE ⭐)

**CONCEPT CLÉS :**
- Approche 1 : Utiliser BERT comme un dictionnaire général
- Approche 3 : Spécialiser ce dictionnaire pour le bien-être

### PHASE 3B : FINE-TUNING BERT (Étapes 8-12)

#### Étape 8 : Théorie du Fine-tuning
**AVANT DE CODER, comprendre :**

1. **Feature Extraction vs Fine-tuning :**
```
Feature Extraction:
Input → [BERT GELÉ ❄️] → Features → [Petit classifieur] → Résultat

Fine-tuning:
Input → [BERT MODIFIABLE 🔥] → [Entraînement] → Meilleur résultat
```

2. **Comment fonctionne le fine-tuning :**
   - BERT connaît déjà la langue française (pré-entraîné)
   - Nous ajustons les poids pour reconnaître les sentiments bien-être
   - Learning rate très faible (2e-5) pour ne pas tout casser
   - Early stopping pour éviter l'overfitting

3. **Learning rate :**
   - Feature Extraction : pas d'entraînement
   - Fine-tuning : 2e-5 (très faible!)
   - Custom : 1e-3 (plus élevé)

4. **Quand utiliser quoi :**
   - Peu de données ? → Approche 1
   - Temps limité ? → Approche 1
   - Données bien-être spécialisées ? → Approche 3
   - Besoin ultra-personnalisé ? → Approche 2

**QUESTIONS POUR TOI :**
1. Pourquoi BERT est pré-entraîné et pas custom ?
2. C'est quoi un gradient et pourquoi c'est important ?
3. Si on met learning_rate=0.1, que se passe-t-il ?
4. Pourquoi l'early stopping est utile ?

---

#### Étape 9 : Données pour Fine-tuning
**CRÉER :**
- `src/approach3/data_preparation.py`

**CODE :**
```python
"""
Préparation des données pour fine-tuning BERT
Crée un dataset de textes bien-être avec labels
"""

import json
import random
from typing import List, Tuple

def create_wellbeing_dataset(size: int = 500) -> List[dict]:
    """
    Crée un dataset d'entraînement pour fine-tuning
    
    Args:
        size (int): Nombre total d'exemples
        
    Returns:
        list: Dataset avec structure [{'text': ..., 'label': ...}, ...]
    """
    
    # Exemples par sentiment (à compléter avec VRAIES données)
    DATASET = {
        'très négatif': [
            "Je veux tout abandonner",
            "Je ne vois pas d'issue",
            "Je suis désespéré",
            # À ajouter 100+ exemples réels
        ],
        'négatif': [
            "Je suis triste",
            "Rien n'a d'importance",
            "Je me sens vide",
            # À ajouter 100+ exemples
        ],
        'neutre': [
            "Bonjour, comment ça va?",
            "Il fait beau dehors",
            "Quelle heure est-il?",
            # À ajouter 100+ exemples
        ],
        'positif': [
            "Ça va plutôt bien",
            "J'ai une bonne journée",
            "Je suis content",
            # À ajouter 100+ exemples
        ],
        'très positif': [
            "Je suis heureux!",
            "C'est une journée formidable!",
            "Je me sens vivant et énergique!",
            # À ajouter 100+ exemples
        ]
    }
    
    # Créer le dataset équilibré
    dataset = []
    examples_per_class = size // 5  # 5 classes
    
    label_to_id = {
        'très négatif': 0,
        'négatif': 1,
        'neutre': 2,
        'positif': 3,
        'très positif': 4
    }
    
    for label, texts in DATASET.items():
        # Prendre examples_per_class textes par classe
        selected = random.sample(texts, min(examples_per_class, len(texts)))
        for text in selected:
            dataset.append({
                'text': text,
                'label': label,
                'label_id': label_to_id[label]
            })
    
    # Mélanger le dataset
    random.shuffle(dataset)
    
    return dataset


def save_dataset(dataset: List[dict], filepath: str = 'data/training_wellbeing_data.json'):
    """Sauvegarde le dataset en JSON"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)


def load_dataset(filepath: str = 'data/training_wellbeing_data.json') -> List[dict]:
    """Charge le dataset depuis JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
```

**DEMANDE-MOI :**
1. Comment trouver des données réelles bien-être ?
2. Comment créer 500 exemples manuellement ?
3. Qu'est-ce qu'un dataset équilibré ?

---

#### Étape 10 : Implémentation du Fine-tuner
**CRÉER :**
- `src/approach3/sentiment_finetuner.py`

**CODE :**
```python
"""
Fine-tuning BERT pour l'analyse de sentiment bien-être
"""

import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    Trainer, 
    TrainingArguments
)
from torch.utils.data import Dataset
from typing import List, Dict


class WellbeingDataset(Dataset):
    """Dataset PyTorch pour le fine-tuning de BERT"""
    
    def __init__(self, texts: List[str], labels: List[int], 
                 tokenizer, max_length: int = 128):
        """
        Initialise le dataset
        
        Args:
            texts: Liste de textes
            labels: Liste d'IDs de labels (0-4)
            tokenizer: Tokenizer BERT
            max_length: Longueur max des séquences
        """
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        """Nombre d'exemples dans le dataset"""
        return len(self.texts)
    
    def __getitem__(self, idx):
        """Récupère un exemple"""
        text = self.texts[idx]
        label = self.labels[idx]
        
        # Tokenize le texte
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',  # Pad toutes les séquences à max_length
            truncation=True,        # Tronque si trop long
            return_tensors='pt'     # Retourne des tensors PyTorch
        )
        
        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(label, dtype=torch.long)
        }


class BERTFineTuner:
    """Fine-tune BERT pour l'analyse de sentiment"""
    
    def __init__(self, model_name: str = 'bert-base-multilingual-uncased'):
        """
        Initialise le fine-tuner
        
        Args:
            model_name: Nom du modèle BERT (de HuggingFace)
        """
        print(f"🔧 Chargement de {model_name}...")
        
        # Charger le tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Charger le modèle MODIFIABLE (pas gelé)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=5  # 5 sentiments
        )
        
        print("✅ Modèle chargé avec succès!")
    
    def train(self, 
              train_texts: List[str], 
              train_labels: List[int],
              val_texts: List[str], 
              val_labels: List[int],
              epochs: int = 3,
              batch_size: int = 8):
        """
        Fine-tune BERT sur nos données
        
        Args:
            train_texts: Textes d'entraînement
            train_labels: Labels d'entraînement
            val_texts: Textes de validation
            val_labels: Labels de validation
            epochs: Nombre d'epochs
            batch_size: Taille du batch
        """
        
        print(f"\n🔥 Fine-tuning sur {len(train_texts)} exemples...")
        
        # Créer les datasets PyTorch
        train_dataset = WellbeingDataset(
            train_texts, train_labels, 
            self.tokenizer
        )
        val_dataset = WellbeingDataset(
            val_texts, val_labels, 
            self.tokenizer
        )
        
        # Configurer l'entraînement
        training_args = TrainingArguments(
            output_dir='./models/approach3/bert_finetuned',
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            learning_rate=2e-5,  # 🔑 TRÈS FAIBLE pour fine-tuning
            evaluation_strategy='epoch',
            save_strategy='epoch',
            load_best_model_at_end=True,
            early_stopping_patience=2,  # Arrêter si 2 epochs sans amélioration
            logging_steps=10,
            report_to=['tensorboard']  # Visualiser avec TensorBoard
        )
        
        # Créer le Trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset
        )
        
        # 🚀 ENTRAÎNER (modifie les poids de BERT)
        trainer.train()
        
        # Sauvegarder le meilleur modèle
        trainer.save_model('./models/approach3/bert_finetuned')
        print("✅ Modèle sauvegardé!")
    
    def predict(self, text: str) -> Dict:
        """
        Utilise le modèle pour prédire le sentiment
        
        Args:
            text: Texte à analyser
            
        Returns:
            dict: Sentiment et confiance
        """
        # Tokenize le texte
        inputs = self.tokenizer(
            text, 
            return_tensors='pt',
            padding=True,
            truncation=True
        )
        
        # Prédire (sans gradient)
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Récupérer les logits
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1)
        
        # Trouver la classe avec la plus haute probabilité
        predicted_class = torch.argmax(probabilities).item()
        confidence = probabilities[0, predicted_class].item()
        
        # Mapper l'ID au label
        id_to_label = {
            0: 'très négatif',
            1: 'négatif',
            2: 'neutre',
            3: 'positif',
            4: 'très positif'
        }
        
        return {
            'sentiment': id_to_label[predicted_class],
            'confidence': confidence,
            'all_scores': {
                id_to_label[i]: probabilities[0, i].item()
                for i in range(5)
            }
        }
```

**DEMANDE-MOI :**
1. Explique le rôle de `WellbeingDataset`
2. Pourquoi `learning_rate=2e-5` ?
3. C'est quoi l'early stopping ?

---

#### Étape 11 : Entraîner et Tester
**CRÉER :**
- `src/approach3/train_finetuner.py` (script d'entraînement)

**CODE COMPLET :**
```python
"""
Script d'entraînement du fine-tuning BERT
"""

from src.approach3.data_preparation import (
    create_wellbeing_dataset, 
    load_dataset, 
    save_dataset
)
from src.approach3.sentiment_finetuner import BERTFineTuner
from sklearn.model_selection import train_test_split


def main():
    # Étape 1 : Créer ou charger le dataset
    print("📥 Création du dataset...")
    dataset = create_wellbeing_dataset(size=500)
    save_dataset(dataset)
    
    # Étape 2 : Split train/validation (80/20)
    texts = [d['text'] for d in dataset]
    labels = [d['label_id'] for d in dataset]
    
    train_texts, val_texts, train_labels, val_labels = train_test_split(
        texts, labels, test_size=0.2, random_state=42
    )
    
    # Étape 3 : Créer le fine-tuner
    finetuner = BERTFineTuner()
    
    # Étape 4 : Entraîner
    finetuner.train(
        train_texts, train_labels,
        val_texts, val_labels,
        epochs=3,
        batch_size=8
    )
    
    # Étape 5 : Tester sur quelques phrases
    test_phrases = [
        "Je suis heureux",
        "Je me sens déprimé",
        "Comment ça va?",
        "Je suis stressé au travail",
        "C'est magnifique!"
    ]
    
    print("\n📊 Résultats sur phrases de test:")
    for phrase in test_phrases:
        result = finetuner.predict(phrase)
        print(f"'{phrase}' → {result['sentiment']} ({result['confidence']:.2%})")


if __name__ == '__main__':
    main()
```

**À EXÉCUTER :**
```bash
python src/approach3/train_finetuner.py
```

---

#### Étape 12 : Comparaison des Approches
**MODIFIER :**
- `compare_approaches.py`

**AJOUTER :**
```python
def compare_all_approaches():
    """Compare les 3 approches"""
    
    test_phrases = [
        "Je suis heureux",
        "Je me sens stressé",
        "Bonjour",
        "Je ne veux plus continuer",
        "C'est magnifique!"
    ]
    
    # Approche 1 : Feature Extraction
    print("APPROCHE 1 : Feature Extraction")
    from src.approach1.sentiment_analyzer import SentimentAnalyzer
    analyzer1 = SentimentAnalyzer()
    
    # Approche 3 : Fine-tuning
    print("APPROCHE 3 : Fine-tuning BERT")
    from src.approach3.sentiment_analyzer import SentimentAnalyzer as SentimentAnalyzer3
    analyzer3 = SentimentAnalyzer3()
    
    # Comparer
    for phrase in test_phrases:
        result1 = analyzer1.analyze(phrase)
        result3 = analyzer3.analyze(phrase)
        
        print(f"\n'{phrase}'")
        print(f"  Approche 1: {result1['sentiment']} ({result1['confidence']:.2%})")
        print(f"  Approche 3: {result3['sentiment']} ({result3['confidence']:.2%})")
```

---

### PHASE 5B : INTÉGRATION APPROCHE 3 (Étape 13)

#### Étape 13 : Créer Chatbot Approche 3
**CRÉER :**
- `src/approach3/sentiment_analyzer.py` (charge le modèle fine-tuné)
- `src/approach3/chatbot.py` (réutilise mood_tracker & response_generator)

**MODIFIER :**
- `main.py` pour permettre le choix entre Approche 1, 3, et 2

```python
def main():
    print("\n🤖 CHATBOT DE BIEN-ÊTRE\n")
    print("Quelle approche utiliser?\n")
    print("1. 🚀 Feature Extraction (BERT gelé)")
    print("   ├─ Rapide (0.3 sec/réponse)")
    print("   ├─ Précision: ~82%")
    print("   └─ Pas d'entraînement")
    print()
    print("2. 🔥 Fine-tuning BERT (BERT modifié)")
    print("   ├─ Équilibré (0.5 sec/réponse)")
    print("   ├─ Précision: ~91%")
    print("   └─ Entraîné 5-10 min sur données")
    print()
    print("3. 🧠 Custom LSTM/GRU")
    print("   ├─ Lent (1-2 sec/réponse)")
    print("   ├─ Précision: ~85-90%")
    print("   └─ Custom et personnalisable")
    print()
    
    choice = input("Choix (1-3): ").strip()
    
    if choice == '1':
        from src.approach1.chatbot import WellbeingChatbot
        chatbot = WellbeingChatbot()
    elif choice == '2':
        from src.approach3.chatbot import WellbeingChatbot
        chatbot = WellbeingChatbot()
    elif choice == '3':
        from src.approach2.chatbot import WellbeingChatbot
        chatbot = WellbeingChatbot()
    
    chatbot.start()
```

---

## 🚀 PLAN D'EXÉCUTION - APPROCHE 2 : CUSTOM LSTM/GRU (À FAIRE APRÈS APPROCHE 3)

### PHASE 7 : PRÉPARATION DES DONNÉES (Étape 14-16)

#### Étape 14 : Comprendre le Deep Learning

(Même structure qu'avant mais avec numérotation correcte)

---

## ✅ CHECKLIST - ORDRE D'EXÉCUTION

### ACTUELLEMENT EN COURS :
- [ ] Approche 1 - ✅ COMPLÉTÉE
- [ ] Approche 3 (Fine-tuning) - À COMMENCER
  - [ ] Étape 8 : Théorie
  - [ ] Étape 9 : Data Preparation
  - [ ] Étape 10 : Fine-tuner
  - [ ] Étape 11 : Entraînement
  - [ ] Étape 12 : Comparaison
  - [ ] Étape 13 : Intégration

### ENSUITE :
- [ ] Approche 2 (Custom LSTM)
  - [ ] Étape 14-16 : Data Prep
  - [ ] Étape 17-19 : Model Builder
  - [ ] Étape 20-22 : Training
  - [ ] Étape 23-25 : Integration

### FINALISATION :
- [ ] Rapport final
- [ ] Soutenance

---

**VERSION:** 2.0 - Mise à jour avec 3 approches distinctes  
**DATE:** 13 Janvier 2026  
**STATUT:** Approche 1 complétée, Approche 3 prête à commencer
