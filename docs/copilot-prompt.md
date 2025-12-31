# 🤖 Prompt pour GitHub Copilot Pro - Chatbot de Bien-être

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
5. **Deux implémentations complètes** : 
   - Approche 1 avec modèle pré-entraîné (prioritaire)
   - Approche 2 avec modèle custom (ensuite)

### Format de réponse attendu :

Pour chaque étape, structure ta réponse comme suit :

```
📚 EXPLICATION THÉORIQUE
[Explique le concept avec des exemples simples]

🎯 OBJECTIF DE CETTE ÉTAPE
[Ce qu'on va accomplir]

💡 CONCEPTS CLÉS
[Liste les concepts importants à comprendre]

📝 CODE ANNOTÉ
[Code avec commentaires détaillés]

✅ VÉRIFICATION
[Questions pour vérifier ma compréhension]

🚀 PROCHAINE ÉTAPE
[Aperçu de ce qui vient après]
```

---

## 📂 STRUCTURE DU PROJET

Crée cette structure de dossiers :

```
chatbot-bien-etre/
│
├── data/                          # Données et historiques
│   ├── conversations.json         # Historique des conversations
│   ├── mood_history.json          # Suivi de l'humeur
│   └── training_data.csv          # Données d'entraînement (Approche 2)
│
├── models/                        # Modèles sauvegardés
│   ├── approach1/                 # Modèle pré-entraîné
│   └── approach2/                 # Modèle custom
│       ├── sentiment_model.h5
│       └── preprocessor.pkl
│
├── src/                           # Code source
│   ├── __init__.py
│   ├── approach1/                 # Approche 1
│   │   ├── __init__.py
│   │   ├── sentiment_analyzer.py  # Analyse avec transformers
│   │   ├── mood_tracker.py        # Suivi de l'humeur
│   │   ├── response_generator.py  # Génération de réponses
│   │   └── chatbot.py             # Logique principale
│   │
│   └── approach2/                 # Approche 2
│       ├── __init__.py
│       ├── data_preparation.py    # Préparation des données
│       ├── model_builder.py       # Construction du réseau
│       ├── model_trainer.py       # Entraînement
│       ├── sentiment_analyzer.py  # Analyse custom
│       ├── mood_tracker.py        # Suivi de l'humeur
│       ├── response_generator.py  # Génération de réponses
│       └── chatbot.py             # Logique principale
│
├── tests/                         # Tests unitaires
│   ├── test_approach1.py
│   └── test_approach2.py
│
├── notebooks/                     # Jupyter notebooks (exploration)
│   ├── 01_exploration_data.ipynb
│   ├── 02_model_comparison.ipynb
│   └── 03_analysis_results.ipynb
│
├── ui/                            # Interfaces utilisateur
│   ├── console_ui.py              # Interface console
│   └── streamlit_ui.py            # Interface web
│
├── docs/                          # Documentation
│   ├── rapport.md                 # Rapport du projet
│   └── presentation.md            # Support de soutenance
│
├── requirements.txt               # Dépendances
├── config.yaml                    # Configuration
├── main.py                        # Point d'entrée
└── README.md                      # Documentation principale
```

---

## 🚀 PLAN D'EXÉCUTION - APPROCHE 1

### PHASE 1 : SETUP ET CONFIGURATION (Étape 1-2)

#### Étape 1 : Configuration de l'environnement
**À faire :**
- Créer l'environnement virtuel
- Installer les dépendances nécessaires
- Configurer VSCode

**Dépendances pour Approche 1 :**
```
transformers==4.35.0
torch==2.1.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.2
textblob==0.17.1
nltk==3.8.1
streamlit==1.28.0
plotly==5.18.0
```

**Questions avant de commencer :**
1. Explique-moi ce que fait chaque librairie
2. Pourquoi avons-nous besoin de transformers ?
3. C'est quoi la différence entre torch et tensorflow ?

#### Étape 2 : Structure du projet
**À faire :**
- Créer tous les dossiers
- Créer les fichiers __init__.py
- Configurer config.yaml

**Demande-moi :**
- Es-tu prêt à passer à la phase 2 ?
- As-tu des questions sur la structure ?

---

### PHASE 2 : ANALYSEUR DE SENTIMENT (Étape 3-5)

#### Étape 3 : Comprendre l'analyse de sentiment
**Explique-moi :**
1. C'est quoi un modèle de transformer ?
2. Comment BERT fonctionne-t-il ?
3. Qu'est-ce que le tokenization ?
4. C'est quoi les embeddings ?

**Crée ensuite :**
- `src/approach1/sentiment_analyzer.py`

**Structure attendue :**
```python
class SentimentAnalyzer:
    """
    [Docstring détaillée expliquant la classe]
    """
    
    def __init__(self):
        """[Explique ce qui se passe ici]"""
        pass
    
    def analyze(self, text):
        """
        [Explique le processus d'analyse]
        
        Args:
            text (str): Texte à analyser
            
        Returns:
            dict: Résultat structuré
        """
        pass
```

**Après le code, demande-moi :**
1. Peux-tu m'expliquer ce que fait la méthode analyze() ?
2. Pourquoi utilisons-nous un dictionnaire pour le retour ?
3. Teste le code avec 3 phrases de ton choix

#### Étape 4 : Tests de l'analyseur
**Crée :**
- `tests/test_approach1.py`

**Cas de test à implémenter :**
```python
# Test 1 : Sentiment positif
# Test 2 : Sentiment négatif
# Test 3 : Sentiment neutre
# Test 4 : Texte vide
# Test 5 : Texte avec emojis
```

**Demande-moi :**
- Exécute les tests et partage les résultats
- Qu'est-ce que tu remarques ?

#### Étape 5 : Amélioration de l'analyseur
**À faire :**
- Ajouter la gestion des emojis
- Ajouter le multi-langue
- Ajouter le score de confiance
- Ajouter la détection d'émotions spécifiques

**Demande-moi :**
- Quelle amélioration te semble la plus importante ?
- Pourquoi ?

---

### PHASE 3 : TRACKER D'HUMEUR (Étape 6-8)

#### Étape 6 : Conception du tracker
**Explique-moi d'abord :**
1. Comment stocker l'historique efficacement ?
2. C'est quoi un timestamp ?
3. Comment calculer des tendances ?

**Crée ensuite :**
- `src/approach1/mood_tracker.py`

**Fonctionnalités à implémenter :**
```python
class MoodTracker:
    def add_mood(self, sentiment, score, timestamp)
    def get_trend(self, days=7)
    def get_statistics(self)
    def get_mood_calendar(self, month)
    def detect_patterns(self)
    def export_data(self, format='json')
```

**Demande-moi :**
1. Explique-moi comment fonctionne get_trend()
2. Qu'est-ce qu'un pattern dans le contexte de l'humeur ?
3. Teste avec des données fictives

#### Étape 7 : Visualisation des données
**À faire :**
- Créer des graphiques d'évolution
- Créer un calendrier d'humeur
- Créer des statistiques

**Utilise :** plotly pour les graphiques interactifs

**Demande-moi :**
- Quel type de graphique est le plus pertinent ?
- Comment interpréter les résultats ?

#### Étape 8 : Intégration avec persistence
**Explique-moi :**
1. Pourquoi utiliser JSON vs SQLite ?
2. Comment gérer les erreurs de lecture/écriture ?

**Implémente :**
- Sauvegarde automatique
- Chargement au démarrage
- Gestion des erreurs

---

### PHASE 4 : GÉNÉRATEUR DE RÉPONSES (Étape 9-11)

#### Étape 9 : Stratégies de réponse
**Explique-moi :**
1. Qu'est-ce qu'une réponse empathique ?
2. Comment personnaliser selon le contexte ?
3. C'est quoi un template de réponse ?

**Crée :**
- `src/approach1/response_generator.py`

**Structure :**
```python
class ResponseGenerator:
    def __init__(self):
        self.response_templates = {
            'positive': [...],
            'negative': [...],
            'neutral': [...]
        }
        self.advice_database = {...}
    
    def generate_response(self, sentiment, context, mood_trend)
    def select_advice(self, sentiment)
    def personalize_response(self, response, user_history)
```

**Demande-moi :**
1. Crée 5 templates pour chaque sentiment
2. Comment éviter les réponses répétitives ?

#### Étape 10 : Base de conseils
**À faire :**
- Créer une base de conseils pour chaque émotion
- Ajouter des techniques de bien-être
- Ajouter des ressources (numéros d'urgence, etc.)

**Structure de la base :**
```python
ADVICE_DATABASE = {
    'sad': {
        'activities': [...],
        'techniques': [...],
        'resources': [...]
    },
    'anxious': {...},
    'stressed': {...}
}
```

#### Étape 11 : Détection de crise
**Important :** Implémenter la détection de situations critiques

**Demande-moi :**
1. Quels mots-clés indiquent une crise ?
2. Comment réagir de manière appropriée ?

---

### PHASE 5 : CHATBOT PRINCIPAL (Étape 12-14)

#### Étape 12 : Intégration des composants
**Crée :**
- `src/approach1/chatbot.py`

**Classe principale :**
```python
class WellbeingChatbot:
    def __init__(self):
        # Initialiser tous les composants
        
    def process_message(self, user_message):
        # Pipeline complet
        
    def start_conversation(self):
        # Début de session
        
    def end_conversation(self):
        # Fin de session
```

**Demande-moi :**
1. Explique le flux complet d'un message
2. Comment gérer le contexte conversationnel ?

#### Étape 13 : Gestion du contexte
**À faire :**
- Mémoriser les derniers messages
- Détecter les références au passé
- Adapter les réponses au contexte

#### Étape 14 : Tests d'intégration
**Crée des scénarios de test :**
1. Conversation courte (5 messages)
2. Conversation longue (20+ messages)
3. Changement d'humeur
4. Situation de crise

---

### PHASE 6 : INTERFACE UTILISATEUR (Étape 15-17)

#### Étape 15 : Interface console
**Crée :**
- `ui/console_ui.py`

**Fonctionnalités :**
- Boucle de conversation
- Commandes spéciales (/stats, /history, /export)
- Affichage coloré

#### Étape 16 : Interface Streamlit
**Crée :**
- `ui/streamlit_ui.py`

**Composants :**
- Zone de chat
- Graphiques d'humeur
- Statistiques en temps réel
- Export des données

**Demande-moi :**
1. Lance l'interface et teste
2. Qu'est-ce qui pourrait être amélioré ?

#### Étape 17 : Point d'entrée principal
**Crée :**
- `main.py`

**Permet de choisir :**
- Interface console ou web
- Approche 1 ou 2
- Mode démo ou production

---

## 🚀 PLAN D'EXÉCUTION - APPROCHE 2

### PHASE 7 : PRÉPARATION DES DONNÉES (Étape 18-20)

#### Étape 18 : Comprendre le Deep Learning pour NLP
**Avant de coder, explique-moi :**
1. C'est quoi un réseau de neurones ?
2. Comment ça "apprend" ?
3. Différence entre LSTM et GRU ?
4. C'est quoi le backpropagation ?
5. Qu'est-ce qu'une epoch ?

**Dessine-moi :** L'architecture du réseau que nous allons créer

#### Étape 19 : Collecte et préparation des données
**Crée :**
- `src/approach2/data_preparation.py`

**Fonctions à implémenter :**
```python
def create_training_dataset(size=1000):
    """Crée un dataset d'entraînement"""
    
def load_external_dataset(filepath):
    """Charge un dataset externe"""
    
def augment_data(df):
    """Augmente le dataset"""
    
def clean_text(text):
    """Nettoie le texte"""
    
def balance_dataset(df):
    """Équilibre les classes"""
```

**Demande-moi :**
1. Où trouver des datasets français ?
2. Comment créer mes propres données ?

#### Étape 20 : Exploration des données
**Crée :**
- `notebooks/01_exploration_data.ipynb`

**Analyses à faire :**
- Distribution des sentiments
- Longueur moyenne des textes
- Mots les plus fréquents
- Visualisations

---

### PHASE 8 : PRÉTRAITEMENT (Étape 21-23)

#### Étape 21 : Comprendre le prétraitement
**Explique-moi :**
1. C'est quoi le tokenization ?
2. Pourquoi le padding ?
3. C'est quoi un vocabulaire ?
4. Comment encoder les labels ?

#### Étape 22 : Implémentation du préprocesseur
**Crée :**
- `src/approach2/data_preparation.py` (compléter)

**Classe TextPreprocessor :**
```python
class TextPreprocessor:
    def __init__(self, max_words, max_len)
    def fit(self, texts, labels)
    def transform(self, texts, labels=None)
    def save(self, filepath)
    @classmethod
    def load(cls, filepath)
```

**Demande-moi :**
1. Teste avec quelques phrases
2. Qu'est-ce que tu observes dans les séquences ?

#### Étape 23 : Validation du preprocessing
**Vérifie :**
- Toutes les séquences ont la même longueur ?
- Les labels sont correctement encodés ?
- Le vocabulaire est cohérent ?

---

### PHASE 9 : CONSTRUCTION DU MODÈLE (Étape 24-27)

#### Étape 24 : Architecture du réseau
**Explique-moi en détail :**
1. Couche Embedding : À quoi ça sert ?
2. Couche LSTM : Comment ça fonctionne ?
3. Couche Dense : Pourquoi à la fin ?
4. Fonction d'activation : Softmax vs Sigmoid ?

**Dessine :** L'architecture couche par couche

#### Étape 25 : Implémentation du modèle
**Crée :**
- `src/approach2/model_builder.py`

**Classe SentimentNeuralNetwork :**
```python
class SentimentNeuralNetwork:
    def build_model(self):
        """Construit l'architecture"""
        
    def compile_model(self):
        """Compile avec optimizer et loss"""
        
    def summary(self):
        """Affiche l'architecture"""
```

**Demande-moi :**
1. Explique chaque couche du modèle
2. Pourquoi ces hyperparamètres ?

#### Étape 26 : Fonction de perte et optimiseur
**Explique-moi :**
1. C'est quoi categorical_crossentropy ?
2. Comment fonctionne Adam optimizer ?
3. C'est quoi le learning rate ?

#### Étape 27 : Callbacks et monitoring
**Implémente :**
- ModelCheckpoint (sauvegarder le meilleur modèle)
- EarlyStopping (arrêter si pas d'amélioration)
- TensorBoard (visualiser l'entraînement)

---

### PHASE 10 : ENTRAÎNEMENT (Étape 28-30)

#### Étape 28 : Configuration de l'entraînement
**Crée :**
- `src/approach2/model_trainer.py`

**Paramètres à définir :**
```python
TRAINING_CONFIG = {
    'epochs': 50,
    'batch_size': 32,
    'validation_split': 0.2,
    'learning_rate': 0.001,
    'early_stopping_patience': 5
}
```

**Demande-moi :**
1. Qu'est-ce qu'un bon nombre d'epochs ?
2. Comment choisir le batch_size ?

#### Étape 29 : Lancer l'entraînement
**Script d'entraînement :**
```python
def train_model():
    # 1. Charger les données
    # 2. Prétraiter
    # 3. Split train/val/test
    # 4. Construire le modèle
    # 5. Entraîner
    # 6. Évaluer
    # 7. Sauvegarder
```

**Pendant l'entraînement, demande-moi :**
1. Interprète les métriques (loss, accuracy)
2. Le modèle overfitte-t-il ?
3. Quand arrêter l'entraînement ?

#### Étape 30 : Évaluation et analyse
**Crée :**
- `notebooks/02_model_comparison.ipynb`

**Analyses :**
- Courbes de loss et accuracy
- Matrice de confusion
- Exemples de prédictions correctes/incorrectes
- Comparaison avec Approche 1

---

### PHASE 11 : INTÉGRATION APPROCHE 2 (Étape 31-33)

#### Étape 31 : Adapter le chatbot
**Crée :**
- `src/approach2/sentiment_analyzer.py`
- `src/approach2/chatbot.py`

**Réutilise :**
- mood_tracker.py (identique)
- response_generator.py (identique)

#### Étape 32 : Tests comparatifs
**Compare les deux approches :**
- Temps de réponse
- Précision
- Utilisation mémoire
- Cas d'usage spécifiques

#### Étape 33 : Interface unifiée
**Modifie main.py :**
```python
def main():
    print("Quelle approche utiliser ?")
    print("1. Modèle pré-entraîné (rapide, précis)")
    print("2. Modèle custom (personnalisé)")
    choice = input("Choix (1 ou 2): ")
```

---

### PHASE 12 : FINALISATION (Étape 34-36)

#### Étape 34 : Documentation
**Crée :**
- README.md complet
- Docstrings pour toutes les fonctions
- Guide d'utilisation

#### Étape 35 : Rapport du projet
**Structure du rapport :**
```markdown
# Rapport : Chatbot de Bien-être

## 1. Introduction
## 2. État de l'art
## 3. Méthodologie
   ### 3.1 Approche 1 : Transfer Learning
   ### 3.2 Approche 2 : Deep Learning Custom
## 4. Implémentation
## 5. Résultats et Analyse
## 6. Comparaison des Approches
## 7. Conclusion et Perspectives
```

#### Étape 36 : Préparation de la soutenance
**Crée :**
- Présentation PowerPoint/PDF
- Démo live du chatbot
- Vidéo de démonstration (backup)

---

## ✅ VALIDATION DE CHAQUE ÉTAPE

Après chaque étape, tu dois me poser ces questions :

### Questions de Compréhension :
1. "Explique-moi ce que fait ce code avec tes propres mots"
2. "Quel est le rôle de [concept] dans cette étape ?"
3. "Que se passerait-il si on modifiait [paramètre] ?"

### Questions Pratiques :
1. "Teste le code avec ces exemples : [...]"
2. "Que remarques-tu dans les résultats ?"
3. "Comment pourrions-nous améliorer cela ?"

### Questions de Validation :
1. "Es-tu prêt à passer à l'étape suivante ?"
2. "As-tu des questions sur cette étape ?"
3. "Veux-tu approfondir un point particulier ?"

---

## 🎓 FORMAT DE RÉPONSE EXEMPLE

Voici comment tu dois structurer chaque réponse :

```markdown
## 📚 ÉTAPE X : [Titre]

### Explication Théorique
[Paragraphe explicatif avec analogies simples]

### Concepts Clés
- **Concept 1** : Définition et exemple
- **Concept 2** : Définition et exemple

### Objectif
Ce que nous allons accomplir dans cette étape.

### Code
[Code avec commentaires ligne par ligne]

### Test
[Exemples de test à exécuter]

### Vérification
1. Question 1 ?
2. Question 2 ?
3. Question 3 ?

### Prochaine Étape
Aperçu de l'étape suivante.
```

---

## 🚨 RÈGLES IMPORTANTES

1. **Ne jamais sauter d'étape** sans mon accord explicite
2. **Toujours expliquer avant de coder**
3. **Commentaires en français** dans le code
4. **Exemples concrets** pour chaque concept
5. **Tests après chaque fonctionnalité**
6. **Validation avant de continuer**

---

## 🎯 COMMENCER MAINTENANT

Copilot, commence par l'**Étape 1 : Configuration de l'environnement**.

Avant de me donner le code :
1. Explique-moi pourquoi nous avons besoin de chaque librairie
2. Explique la différence entre transformers et tensorflow
3. Puis guide-moi pour la configuration

**Je suis prêt à commencer ! 🚀**
