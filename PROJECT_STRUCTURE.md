# 📁 Documentation Complète - Structure du Projet

Guide détaillé de chaque fichier, dossier et fonction du chatbot de bien-être.

---

## 🏗️ STRUCTURE GÉNÉRALE DU PROJET

```
Chatbot bien-être/
├── 📄 Fichiers de Configuration (racine)
│   ├── main.py                      ← Point d'entrée principal
│   ├── config.yaml                  ← Configuration globale
│   ├── requirements.txt             ← Dépendances Python
│   ├── setup_nltk.py               ← Configuration NLTK
│   ├── launch_menu.bat             ← Lanceur unique (Windows)
│   ├── README.md                   ← Documentation utilisateur
│   └── PROJECT_STRUCTURE.md        ← Ce fichier (documentation technique)
│
├── 📁 src/                          ← CODE SOURCE (cœur du projet)
│   ├── __init__.py
│   ├── approach1/                  ← APPROCHE 1 : Feature Extraction (IMPLÉMENTÉE) ✅
│   │   ├── __init__.py
│   │   ├── sentiment_analyzer.py          ← Analyse de sentiment (BERT)
│   │   ├── response_generator.py          ← Génération de réponses
│   │   ├── mood_tracker.py                ← Suivi d'humeur
│   │   ├── mood_visualizer.py             ← Graphiques et visualisations
│   │   ├── chatbot.py                     ← Orchestrateur principal
│   │   ├── sentiment_finetuner.py         ← Fine-tuning optionnel
│   │   └── data/
│   │       └── mood_history.json          ← Historique utilisateur
│   │
│   └── approach2/                  ← APPROCHE 2 : Custom LSTM/GRU (FUTUR)
│       └── __init__.py
│
├── 🌐 ui/                           ← INTERFACES UTILISATEUR
│   └── streamlit_ui.py             ← Interface Web (Streamlit)
│
├── 📊 data/                         ← DONNÉES
│   ├── mood_history.json           ← Historique global des humeurs
│   └── mood_test.json              ← Données de test
│
├── 🤖 models/                       ← MODÈLES PRÉ-ENTRAÎNÉS
│   ├── approach1/                  ← Modèles BERT
│   │   └── sentiment_model/        ← Modèle fine-tuné (optionnel)
│   └── approach2/                  ← Futurs modèles custom
│
├── 🧪 tests/                        ← TESTS AUTOMATIQUES
│   └── test_approach1.py           ← 23 tests unitaires
│
├── 📓 notebooks/                    ← JUPYTER NOTEBOOKS
│   └── 01_exploration_data.ipynb   ← Exploration interactive
│
├── 📚 docs/                         ← DOCUMENTATION
│   └── copilot-prompt.md           ← Cahier des charges initial
│
├── .git/                            ← VERSION CONTROL
└── venv/                            ← ENVIRONNEMENT VIRTUEL PYTHON
```

---

# 📄 FICHIERS RACINE - Configuration & Lancement

## 1. **main.py** 🎯
**Rôle :** Point d'entrée principal du projet  
**Ce qu'il fait :** Lance le menu interactif pour choisir l'interface et l'approche

### Code principal :
```python
"""
Point d'Entrée Principal - Chatbot de Bien-être
Permet de choisir :
- Interface Console ou Web (Streamlit)
- Approche 1 ou 2
- Mode démo ou production
"""

def print_menu():
    """Affiche le menu principal avec 6 options"""
    print(menu)  # Menu interactif ASCII

def main():
    """Workflow principal"""
    1. Affiche la bannière
    2. Affiche le menu
    3. Récupère le choix de l'utilisateur
    4. Lance l'interface appropriée
```

### Utilisation :
```bash
# Lancer le menu
python main.py

# Lancer en mode console directement
python main.py --console

# Lancer interface web
streamlit run ui/streamlit_ui.py
```

### Options du menu :
```
1. 🌐 Lancer l'interface Web (Streamlit)
2. 💻 Lancer l'interface Console
3. 📊 Exécuter la démo
4. 🧪 Lancer les tests
5. 🎯 Quitter
```

---

## 2. **config.yaml** ⚙️
**Rôle :** Fichier de configuration centralisé  
**Ce qu'il fait :** Définit tous les paramètres du projet

### Contenu :
```yaml
# Approche par défaut
default_approach: "approach1"

# Configuration APPROCHE 1 (BERT)
approach1:
  model_name: "nlptown/bert-base-multilingual-uncased-sentiment"
  max_length: 512
  confidence_threshold: 0.6
  languages: ["fr", "en", "ar"]

# Configuration APPROCHE 2 (Custom)
approach2:
  max_words: 10000
  embedding_dim: 128
  lstm_units: 64
```

### Pourquoi c'est utile :
- Change les paramètres **sans modifier le code**
- Supporte plusieurs modèles BERT
- Configure les langues supportées
- Paramètres d'entraînement centralisés

---

## 3. **requirements.txt** 📦
**Rôle :** Liste toutes les dépendances Python  
**Ce qu'il fait :** Permet installer toutes les librairies nécessaires

### Installation :
```bash
pip install -r requirements.txt
```

### Dépendances clés :

| Paquet | Version | Rôle |
|--------|---------|------|
| **transformers** | 4.35.0 | Modèles BERT, RoBERTa |
| **torch** | 2.1.0 | Framework deep learning |
| **streamlit** | 1.28.0 | Interface web |
| **pandas** | 2.0.3 | Manipulation données |
| **plotly** | 5.18.0 | Graphiques interactifs |
| **nltk** | 3.8.1 | NLP (tokenization, stopwords) |
| **scikit-learn** | 1.3.2 | ML classique |

---

## 4. **setup_nltk.py** 🔧
**Rôle :** Configure les ressources NLTK  
**Ce qu'il fait :** Télécharge les données nécessaires pour NLTK

### Ressources téléchargées :
```
✅ punkt          - Tokeniseur de phrases
✅ stopwords      - Mots vides (le, la, de, etc.)
✅ punkt_tab      - Token patterns
✅ wordnet        - Base lexicale
✅ averaged_perceptron_tagger - POS tagger
```

### Utilisation :
```bash
python setup_nltk.py
```

---

## 5. **launch_menu.bat** 🚀
**Rôle :** Lanceur Windows unique  
**Ce qu'il fait :** Active venv et lance le menu automatiquement

### Code :
```batch
@echo off
REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Lancer le menu principal
python main.py
```

### Utilisation :
```
Double-clic sur launch_menu.bat → Le chatbot se lance!
```

---

## 6. **compare_approaches.py** 📊
**Rôle :** Comparer Feature Extraction vs Fine-tuning  
**Ce qu'il fait :** Teste les 2 approches sur les mêmes phrases

### Workflow :
```python
1. Charger BERT pré-entraîné (Feature Extraction)
2. Charger modèle fine-tuné (si disponible)
3. Tester 8 phrases sur les deux modèles
4. Comparer les résultats
5. Afficher statistiques et temps
```

### Output :
```
APPROCHE 1: Feature Extraction
Phrase: "Je me sens bien"
→ Sentiment: très positif (94%)
→ Temps: 0.32 sec

APPROCHE 2: Fine-tuning
Phrase: "Je me sens bien"
→ Sentiment: très positif (96%)
→ Temps: 0.41 sec

COMPARAISON:
✅ Accord: 8/8 (100%)
📊 Moyenne Confidence A1: 88%
📊 Moyenne Confidence A2: 92%
```

---

# 🗂️ DOSSIER src/ - Code Source

## Structure :
```
src/
├── __init__.py          (fichier vide pour Python)
├── approach1/           (IMPLÉMENTÉE) ✅
│   ├── sentiment_analyzer.py
│   ├── response_generator.py
│   ├── mood_tracker.py
│   ├── mood_visualizer.py
│   ├── chatbot.py
│   ├── sentiment_finetuner.py
│   └── data/
└── approach2/           (Futur)
    └── __init__.py
```

---

## 🧠 src/approach1/sentiment_analyzer.py
**Rôle :** Analyser le sentiment d'un texte  
**Ce qu'il fait :** Utilise BERT pour classifier l'humeur

### Classe principale : `SentimentAnalyzer`

#### Initialisation :
```python
class SentimentAnalyzer:
    def __init__(self, config_path=None):
        """
        Étapes :
        1. Charger config.yaml
        2. Charger le tokenizer BERT
        3. Charger le modèle BERT pré-entraîné
        4. Mapper les 5 labels (très négatif → très positif)
        """
        self.tokenizer = AutoTokenizer.from_pretrained(
            'nlptown/bert-base-multilingual-uncased-sentiment'
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(...)
```

#### Méthode clé : `analyze()`
```python
def analyze(self, text: str) -> Dict[str, Any]:
    """
    Analyse le sentiment d'un texte
    
    Args:
        text (str): Texte à analyser
    
    Returns:
        {
            'sentiment': 'positif',           # Label final
            'sentiment_detail': 'très positif', # Plus détaillé
            'confidence': 0.94,               # Confiance 0-1
            'scores': {...}                   # Scores bruts
        }
    
    Processus:
    1. Tokenize le texte → tokens
    2. Passe dans BERT (forward pass)
    3. Récupère logits (scores bruts)
    4. Applique softmax → probabilités
    5. Prend le max → sentiment
    6. Retourne sentiment + confiance
    """
```

#### Workflow complet :
```
"Je suis heureux"
        ↓
[Tokenization] → ['Je', 'suis', 'heureux']
        ↓
[BERT Forward] → logits [0.1, 0.2, 2.5, 0.3, 0.1]
        ↓
[Softmax] → probs [0.05, 0.08, 0.82, 0.03, 0.02]
        ↓
[Argmax] → index 2 → label "très positif"
        ↓
Result: {'sentiment': 'positif', 'confidence': 0.82}
```

#### Les 5 catégories :
```
0: 'très négatif'   😤  → "Je veux tout abandonner"
1: 'négatif'        😔  → "Je suis triste"
2: 'neutre'         😐  → "Bonjour, comment ça va?"
3: 'positif'        😄  → "Ça va bien"
4: 'très positif'   😊  → "Je suis heureux!"
```

---

## 💬 src/approach1/response_generator.py
**Rôle :** Générer des réponses empathiques et conseils  
**Ce qu'il fait :** Crée une réponse personnalisée selon le sentiment

### Classe principale : `ResponseGenerator`

#### Structure :
```python
class ResponseGenerator:
    def __init__(self):
        """
        Initialise avec :
        1. Templates de réponses (par sentiment)
        2. Base de conseils (bien-être)
        3. Ressources d'urgence
        4. Historique des réponses (éviter répétitions)
        """
        self.response_templates = {
            'très positif': [
                "C'est merveilleux ! 🎉",
                "Wow ! Tu vas super bien ! 💪",
                ...
            ],
            'positif': [...],
            'neutre': [...],
            'négatif': [...],
            'très négatif': [...]
        }
        
        self.advice_database = {
            'très positif': {...},
            'positif': {...},
            ...
        }
```

#### Méthode clé : `generate_response()`
```python
def generate_response(self, sentiment: str, sentiment_detail: str,
                     confidence: float, text: str,
                     mood_trend: Dict = None) -> Dict[str, Any]:
    """
    Génère une réponse complète
    
    Étapes :
    1. Détecter si c'est une crise
    2. Choisir un template approprié
    3. Ajouter contexte de tendance
    4. Sélectionner des conseils pertinents
    5. Générer encouragement
    6. Ajouter ressources d'urgence si crise
    
    Returns:
    {
        'main_response': "Je comprends...",
        'advice': ['Respiration', 'Pause'],
        'encouragement': "Tu as les ressources...",
        'is_crisis': False,
        'emergency_resources': []
    }
    """
```

#### Sous-méthodes :

**1. `_detect_crisis(text)` - Détecte les situations critiques**
```python
def _detect_crisis(self, text: str) -> bool:
    """
    Mots-clés de crise :
    - "se tuer", "suicide", "mourir"
    - "tout est sans espoir"
    - "je ne peux plus"
    - etc.
    
    Returns:
        bool: True si crise détectée
    """
    crisis_keywords = [
        'suicide', 'mourir', 'tuer', 'sans espoir',
        'tout est foutu', 'impossible', 'désespéré'
    ]
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in crisis_keywords)
```

**2. `_select_advice(sentiment, is_crisis)` - Choisit des conseils**
```python
def _select_advice(self, sentiment: str, is_crisis: bool) -> List[str]:
    """
    Conseils par sentiment :
    
    Très positif:
    - Partager ta joie avec les autres
    - Profiter du moment
    - Noter tes réussites
    
    Très négatif (normal):
    - Respiration profonde
    - Pause 5 minutes
    - Parler à quelqu'un
    
    Très négatif (crise):
    - RESSOURCES D'URGENCE
    - Appeler un numéro d'aide
    """
```

**3. `_generate_encouragement()` - Crée encouragement**
```python
def _generate_encouragement(self, sentiment: str) -> str:
    """
    Messages personnalisés selon le sentiment
    
    Très négatif:
    "Tu n'es pas seul(e). Ces difficultés sont temporaires."
    
    Positif:
    "Continue comme ça ! Tu as une belle énergie !"
    """
```

---

## 📊 src/approach1/mood_tracker.py
**Rôle :** Enregistrer et analyser l'humeur dans le temps  
**Ce qu'il fait :** Historique complet + tendances + statistiques

### Classe principale : `MoodTracker`

#### Initialisation :
```python
class MoodTracker:
    def __init__(self, history_file: str = "data/mood_history.json"):
        """
        Charge l'historique existant ou crée un nouveau
        """
        self.history_file = history_file
        self.history = self._load_history()  # Liste de moods
```

#### Structure d'une entrée mood :
```python
mood_entry = {
    'timestamp': '2026-01-13T14:30:45',
    'sentiment': 'positif',
    'sentiment_detail': 'très positif',
    'confidence': 0.94,
    'text': 'Je me sens bien'
}
```

#### Méthodes principales :

**1. `log_mood(sentiment, confidence, text)` - Enregistrer une humeur**
```python
def log_mood(self, sentiment: str, confidence: float, text: str):
    """
    Enregistre une nouvelle humeur avec timestamp
    Sauvegarde immédiatement dans mood_history.json
    """
    mood_entry = {
        'timestamp': datetime.now().isoformat(),
        'sentiment': sentiment,
        'confidence': confidence,
        'text': text[:50]  # Limiter à 50 caractères
    }
    self.history.append(mood_entry)
    self._save_history()
```

**2. `get_trend(days=7)` - Calculer la tendance**
```python
def get_trend(self, days: int = 7) -> Dict:
    """
    Calcule la tendance sur N jours
    
    Étapes:
    1. Récupérer les moods des N derniers jours
    2. Convertir sentiment → score numérique:
       - très négatif: -1.0
       - négatif: -0.5
       - neutre: 0
       - positif: 0.5
       - très positif: 1.0
    3. Calculer moyenne première moitié et seconde moitié
    4. Tendance = (moyenne fin - moyenne début) / jours
    5. Retourner tendance + direction
    
    Returns:
    {
        'trend': 0.32,              # +0.32 par jour
        'direction': 'UP',          # Positif
        'average': 0.65,            # Score moyen
        'data_points': 42           # Nombre de points
    }
    """
```

**3. `get_statistics()` - Statistiques globales**
```python
def get_statistics(self) -> Dict:
    """
    Retourne statistiques complètes:
    - Nombre total d'interactions
    - Sentiment le plus fréquent
    - Sentiment prédominant (sur 7j, 30j)
    - Moments du jour où humeur est meilleure
    - Patterns détectés
    """
```

#### Persistence (Sauvegarde) :
```python
def _save_history(self):
    """Sauvegarde l'historique dans data/mood_history.json"""
    with open(self.history_file, 'w') as f:
        json.dump(self.history, f, indent=2)

def _load_history(self):
    """Charge l'historique depuis JSON"""
    if os.path.exists(self.history_file):
        with open(self.history_file, 'r') as f:
            return json.load(f)
    return []
```

---

## 📈 src/approach1/mood_visualizer.py
**Rôle :** Créer des graphiques et visualisations  
**Ce qu'il fait :** Affiche les tendances d'humeur visuellement

### Classe principale : `MoodVisualizer`

#### Graphiques générés :

**1. Graphique des 7 derniers jours**
```python
def plot_7day_trend(self, mood_data: List[Dict]) -> Figure:
    """
    Graphique en ligne : sentiment par jour
    - X : Dates
    - Y : Score de sentiment (-1 à +1)
    - Couleurs : Dégradé rouge → vert
    """
```

**2. Distribution des sentiments**
```python
def plot_sentiment_distribution(self, mood_data: List[Dict]) -> Figure:
    """
    Graphique circulaire : % de chaque sentiment
    - Très négatif : 10%
    - Négatif : 15%
    - Neutre : 20%
    - Positif : 35%
    - Très positif : 20%
    """
```

**3. Heatmap temporelle**
```python
def plot_hourly_heatmap(self, mood_data: List[Dict]) -> Figure:
    """
    Heatmap : sentiment par heure du jour
    Montre quels moments ont meilleure humeur
    """
```

---

## 🤖 src/approach1/chatbot.py
**Rôle :** Orchestrateur principal  
**Ce qu'il fait :** Coordonne tous les modules

### Classe principale : `Chatbot`

#### Initialisation :
```python
class Chatbot:
    def __init__(self):
        """
        Initialise tous les composants :
        1. SentimentAnalyzer (BERT)
        2. ResponseGenerator (réponses)
        3. MoodTracker (historique)
        4. MoodVisualizer (graphiques)
        """
        self.analyzer = SentimentAnalyzer()
        self.generator = ResponseGenerator()
        self.tracker = MoodTracker()
        self.visualizer = MoodVisualizer()
```

#### Workflow principal : `chat(user_message)`
```python
def chat(self, user_message: str) -> Dict[str, Any]:
    """
    Workflow complet :
    1. Analyser sentiment du message
    2. Enregistrer dans historique
    3. Calculer tendance
    4. Générer réponse
    5. Ajouter contexte de tendance
    
    Returns:
    {
        'sentiment': 'positif',
        'confidence': 0.94,
        'response': "C'est merveilleux...",
        'advice': [...],
        'trend': {...}
    }
    """
```

---

## 🔧 src/approach1/sentiment_finetuner.py
**Rôle :** Entraîner BERT sur nos données  
**Ce qu'il fait :** Fine-tuning optionnel pour améliorer BERT

### Classe principale : `BERTFineTuner`

#### Workflow :
```python
class BERTFineTuner:
    def __init__(self):
        """Charge BERT modifiable (pas gelé)"""
        self.model = AutoModelForSequenceClassification.from_pretrained(
            'bert-base-multilingual-uncased',
            num_labels=5
        )
    
    def train(self, train_dataset, val_dataset, epochs=3):
        """
        Entraîne BERT sur nos données
        
        Étapes:
        1. Créer TrainingArguments
        2. Créer Trainer
        3. Lancer trainer.train() ← MODIFIE BERT
        4. Sauvegarder le modèle amélioré
        """
```

---

# 🌐 DOSSIER ui/ - Interfaces Utilisateur

## ui/streamlit_ui.py 🎨
**Rôle :** Interface web moderne  
**Ce qu'il fait :** Crée l'app Streamlit interactive

### Architecture :
```python
"""
Interface Streamlit pour chatbot bien-être

Composants:
1. Header + titre
2. Sidebar avec config
3. Zone chat (messages/réponses)
4. Zone graphiques (tendances)
5. Zone stats (statistiques)
"""
```

### Fonction principale : `main()`
```python
def main():
    """
    Workflow Streamlit:
    1. Configurer la page
    2. Afficher header/titre
    3. Créer sidebar
    4. Afficher chat area
    5. Afficher analytics
    6. Rerun() pour mise à jour
    """
```

### Zones principales :

**1. Zone Chat**
```python
def render_chat_area(analyzer, tracker, generator):
    """
    - Affiche historique des messages
    - Input pour nouvel message
    - Génère réponse en temps réel
    - Affiche analyse sentiment
    """
```

**2. Zone Analytics**
```python
def render_analytics(tracker):
    """
    - Graphique 7 jours
    - Distribution des sentiments
    - Statistiques
    - Tendance
    """
```

---

# 🧪 DOSSIER tests/ - Tests Automatiques

## tests/test_approach1.py 🧪
**Rôle :** Valider tous les composants  
**Ce qu'il fait :** 23 tests unitaires automatiques

### Tests inclus :
```python
# Tests Sentiment Analyzer
✅ test_sentiment_analysis
✅ test_sentiment_multilingual
✅ test_confidence_scores

# Tests Response Generator
✅ test_response_generation
✅ test_crisis_detection
✅ test_advice_selection

# Tests Mood Tracker
✅ test_mood_logging
✅ test_trend_calculation
✅ test_statistics
✅ test_persistence

# Tests Mood Visualizer
✅ test_plot_generation
✅ test_plot_types

# Tests Chatbot Integration
✅ test_full_workflow
✅ test_chat_response
```

### Lancer les tests :
```bash
python tests/test_approach1.py

# Résultat :
===== 23 passed in 2.34s =====
✅ Tous les tests passent!
```

---

# 📊 DOSSIER data/ - Données

## Fichiers JSON :

### **data/mood_history.json** 📝
**Rôle :** Historique complet des humeurs  
**Format :**
```json
[
  {
    "timestamp": "2026-01-13T14:30:45.123456",
    "sentiment": "positif",
    "sentiment_detail": "très positif",
    "confidence": 0.94,
    "text": "Je me sens bien aujourd'hui"
  },
  {
    "timestamp": "2026-01-13T15:45:12.654321",
    "sentiment": "négatif",
    "sentiment_detail": "négatif",
    "confidence": 0.87,
    "text": "J'ai du mal à me concentrer"
  }
]
```

### **data/mood_test.json** 🧪
**Rôle :** Données de test  
**Utilisé :** Pour validation des models

---

# 🤖 DOSSIER models/ - Modèles

## Structure :
```
models/
├── approach1/
│   └── sentiment_model/
│       ├── config.json
│       ├── pytorch_model.bin
│       └── tokenizer files
│
└── approach2/
    └── (À créer)
```

### Modèle BERT utilisé :
```
nlptown/bert-base-multilingual-uncased-sentiment

- Taille: 500 MB
- Langues: 104 langues (français OK)
- Labels: 5 sentiments
- Pré-entraîné: Oui (pas besoin de fine-tune)
```

---

# 📓 DOSSIER notebooks/

## 01_exploration_data.ipynb 📓
**Rôle :** Exploration interactive des données  
**Ce qu'il fait :** Jupyter notebook pour analyser les données

### Sections :
```
1. Import des données
2. Statistiques descriptives
3. Visualisations
4. Analyse exploratoire
5. Insights et patterns
```

---

# 📚 DOSSIER docs/

## copilot-prompt.md 📋
**Rôle :** Cahier des charges initial  
**Contient :** Spécifications techniques détaillées du projet

---

# 🔄 FLUX DE DONNÉES - Workflow Complet

```
UTILISATEUR ÉCRIT UN MESSAGE
    ↓
┌─────────────────────────────────────────────────────┐
│ 1. ANALYSE (sentiment_analyzer.py)                  │
│    - Tokenization                                   │
│    - BERT forward pass                              │
│    - Softmax + Argmax                               │
│    → Retourne: sentiment + confidence               │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ 2. ENREGISTREMENT (mood_tracker.py)                 │
│    - Créer mood_entry avec timestamp                │
│    - Ajouter à l'historique                         │
│    - Sauvegarder dans JSON                          │
│    → Retourne: historique mis à jour                │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ 3. GÉNÉRATION DE RÉPONSE (response_generator.py)    │
│    - Détecter crise?                                │
│    - Choisir template                               │
│    - Ajouter conseils                               │
│    - Générer encouragement                          │
│    → Retourne: réponse complète                     │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ 4. VISUALISATION (mood_visualizer.py)               │
│    - Calculer tendance                              │
│    - Générer graphiques                             │
│    - Créer statistiques                             │
│    → Retourne: plots Plotly                         │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│ 5. AFFICHAGE (streamlit_ui.py)                      │
│    - Afficher réponse du chatbot                    │
│    - Afficher graphiques                            │
│    - Afficher statistiques                          │
│    → Mise à jour instantanée                        │
└─────────────────────────────────────────────────────┘
    ↓
UTILISATEUR VOIT LA RÉPONSE AVEC GRAPHIQUES
```

---

# 📦 DÉPENDANCES & VERSIONS

### Essentielles (Deep Learning) :
```
transformers==4.35.0    # BERT & modèles
torch==2.1.0            # PyTorch (CPU/GPU)
numpy==1.24.3           # Calculs numériques
```

### Interface :
```
streamlit==1.28.0       # App web
plotly==5.18.0          # Graphiques interactifs
```

### NLP :
```
nltk==3.8.1             # Tokenization, stopwords
scikit-learn==1.3.2     # ML classique
```

### Utilitaires :
```
pandas==2.0.3           # DataFrames
pyyaml==6.0.1           # Config YAML
emoji==2.8.0            # Emojis
```

---

# 🎯 RÉSUMÉ PAR FICHIER

| Fichier | Type | Rôle | Importance |
|---------|------|------|-----------|
| **main.py** | Script | Entrée principale | 🔴 ESSENTIEL |
| **config.yaml** | Config | Paramètres globaux | 🔴 ESSENTIEL |
| **requirements.txt** | Config | Dépendances | 🔴 ESSENTIEL |
| **sentiment_analyzer.py** | Module | Analyse sentiment | 🔴 ESSENTIEL |
| **response_generator.py** | Module | Génère réponses | 🔴 ESSENTIEL |
| **mood_tracker.py** | Module | Historique humeur | 🔴 ESSENTIEL |
| **streamlit_ui.py** | UI | Interface web | 🟡 Important |
| **sentiment_finetuner.py** | Module | Fine-tuning | 🟢 Optionnel |
| **mood_visualizer.py** | Module | Graphiques | 🟡 Important |
| **test_approach1.py** | Tests | Validation | 🟡 Important |
| **compare_approaches.py** | Script | Comparaison | 🟢 Utile |
| **setup_nltk.py** | Script | Configuration NLTK | 🟢 Setup initial |

---

# 🚀 POUR DÉMARRER

```bash
# 1. Cloner/télécharger le projet
cd "Chatbot bien-être"

# 2. Créer environnement virtuel
python -m venv venv

# 3. Activer venv
venv\Scripts\activate

# 4. Installer dépendances
pip install -r requirements.txt

# 5. Setup NLTK
python setup_nltk.py

# 6. Lancer le chatbot
./launch_menu.bat
# OU
python main.py
```

---

# ❓ QUESTIONS FRÉQUENTES

**Q: Quel fichier lance le chatbot?**
A: `launch_menu.bat` (recommandé) ou `python main.py`

**Q: Où sont stockées les données?**
A: `data/mood_history.json`

**Q: Quel modèle est utilisé?**
A: BERT multilingual de HuggingFace: `nlptown/bert-base-multilingual-uncased-sentiment`

**Q: Comment ajouter une nouvelle langue?**
A: Éditer `config.yaml` → `approach1.languages`

**Q: Comment améliorer l'analyse?**
A: Utiliser le fine-tuning: `python compare_approaches.py`

**Q: Comment lancer les tests?**
A: `python tests/test_approach1.py`

**Q: Où est l'interface web?**
A: `ui/streamlit_ui.py` (lancée avec menu option 1)

---

**Dernière mise à jour:** 13/01/2026  
**Auteur:** Étudiant ENSA Berrechid  
**Licence:** MIT
