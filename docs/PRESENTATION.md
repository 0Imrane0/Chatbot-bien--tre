# 🧠 CHATBOT BIEN-ÊTRE IA - PRÉSENTATION COMPLÈTE

> **Un guide complet pour comprendre, apprendre et reproduire ce projet d'Intelligence Artificielle**

---

## 📋 Table des Matières

1. [Introduction](#1-introduction)
2. [Qu'est-ce qu'un Chatbot de Bien-être ?](#2-quest-ce-quun-chatbot-de-bien-être)
3. [Les Technologies Utilisées](#3-les-technologies-utilisées)
4. [Architecture du Projet](#4-architecture-du-projet)
5. [Les Deux Approches : Feature Extraction vs Fine-tuning](#5-les-deux-approches)
6. [Le Module CBT (Thérapie Cognitive)](#6-le-module-cbt)
7. [Comment fonctionne le Bot ?](#7-comment-fonctionne-le-bot)
8. [L'Interface Web](#8-linterface-web)
9. [Résultats et Performances](#9-résultats-et-performances)
10. [Comment Utiliser le Projet](#10-comment-utiliser-le-projet)
11. [Ce que j'ai Appris](#11-ce-que-jai-appris)
12. [Ressources pour Aller Plus Loin](#12-ressources)

---

## 1. Introduction

### 🎯 Objectif du Projet

Créer un **chatbot intelligent** capable de :
- ✅ Comprendre les émotions de l'utilisateur
- ✅ Analyser le sentiment (positif, négatif, neutre)
- ✅ Détecter les pensées négatives (distorsions cognitives)
- ✅ Répondre avec empathie
- ✅ Proposer des actions concrètes pour se sentir mieux

### 👤 Pour Qui ?

Ce projet est destiné à :
- **Étudiants** qui veulent apprendre le NLP (Natural Language Processing)
- **Développeurs** intéressés par l'IA appliquée au bien-être
- **Curieux** qui veulent comprendre comment fonctionne un chatbot moderne

### 📊 Informations Clés

| Information | Valeur |
|-------------|--------|
| **Langage** | Python 3.13 |
| **Modèle IA** | BERT (110 millions de paramètres) |
| **Précision** | 85% |
| **Interface** | Web (Streamlit) |
| **Établissement** | ENSA Berrechid |
| **Date** | Janvier 2026 |

---

## 2. Qu'est-ce qu'un Chatbot de Bien-être ?

### 📝 Définition Simple

Un **chatbot de bien-être** est un programme informatique qui :
1. **Écoute** ce que tu écris
2. **Comprend** ton état émotionnel
3. **Répond** de manière empathique et utile

### 🔄 Différence avec un Chatbot Classique

| Chatbot Classique | Chatbot Bien-être IA |
|-------------------|----------------------|
| Réponses pré-définies | Réponses adaptées à l'émotion |
| Ne comprend pas les émotions | Analyse le sentiment avec IA |
| Réponses génériques | Détecte les distorsions cognitives |
| Pas de suivi | Suit l'évolution de l'humeur |

### 💡 Exemple Concret

**Toi :** "Je suis complètement nul, je rate tout ce que je fais"

**Chatbot classique :** "Je comprends que c'est difficile"

**Notre Chatbot IA :**
- 🔍 **Détecte** : Sentiment très négatif (95% confiance)
- 🧠 **Identifie** : Distorsion cognitive "Tout-ou-rien" et "Surgénéralisation"
- 💬 **Répond** : "Je ressens ta frustration. Mais est-ce vraiment TOUT ? Peux-tu me donner un exemple récent où quelque chose a bien fonctionné ?"
- 💡 **Propose** : Actions concrètes (respiration, écriture, etc.)

---

## 3. Les Technologies Utilisées

### 🐍 Python

**Qu'est-ce que c'est ?**
- Un langage de programmation simple et puissant
- Le plus utilisé en Intelligence Artificielle

**Pourquoi ?**
- Facile à apprendre
- Beaucoup de bibliothèques pour l'IA

### 🤖 BERT (Bidirectional Encoder Representations from Transformers)

**Qu'est-ce que c'est ?**
- Un modèle de langage créé par Google en 2018
- 110 millions de paramètres (comme 110 millions de "neurones")
- Comprend le contexte des mots dans une phrase

**Comment ça marche ?**
```
Phrase: "Je ne suis pas content"
        ↓
BERT lit dans les deux sens: ← et →
        ↓
Comprend que "pas" inverse le sens de "content"
        ↓
Résultat: Sentiment NÉGATIF
```

**Pourquoi BERT ?**
- Comprend le contexte (contrairement aux anciens modèles)
- Pré-entraîné sur des milliards de textes
- On peut l'adapter (fine-tuner) pour notre tâche

### 🔥 PyTorch

**Qu'est-ce que c'est ?**
- Une bibliothèque pour créer des réseaux de neurones
- Créée par Facebook (Meta)

**Pourquoi ?**
- Plus flexible que TensorFlow
- Plus facile à débugger

### 🤗 Transformers (Hugging Face)

**Qu'est-ce que c'est ?**
- Une bibliothèque qui donne accès à des milliers de modèles pré-entraînés
- Simplifie l'utilisation de BERT

**Exemple de code :**
```python
from transformers import AutoModelForSequenceClassification

# Charger BERT en une ligne !
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
```

### 🌐 Streamlit

**Qu'est-ce que c'est ?**
- Une bibliothèque pour créer des interfaces web facilement
- Pas besoin de connaître HTML/CSS/JavaScript

**Exemple :**
```python
import streamlit as st

st.title("Mon Chatbot")
message = st.text_input("Ton message:")
st.write(f"Tu as écrit: {message}")
```

### 📊 Plotly

**Qu'est-ce que c'est ?**
- Une bibliothèque pour créer des graphiques interactifs

**Utilisé pour :**
- Graphique d'évolution de l'humeur
- Distribution des sentiments
- Jauge de confiance du modèle

---

## 4. Architecture du Projet

### 📁 Structure des Dossiers

```
Chatbot bien-être/
│
├── 📄 launch_interface.bat     ← Double-clique pour lancer !
├── 📄 requirements.txt         ← Liste des dépendances
│
├── 📁 src/                     ← Code source
│   ├── 📁 approach1/           ← Approche 1 (Feature Extraction)
│   ├── 📁 approach3/           ← Approche 3 (Fine-tuning) ⭐
│   └── cbt_engine.py           ← Module thérapie cognitive
│
├── 📁 models/                  ← Modèles entraînés
│   └── approach3/
│       └── bert_finetuned/     ← Notre modèle BERT personnalisé
│
├── 📁 ui/                      ← Interface utilisateur
│   └── streamlit_app.py        ← Interface web
│
├── 📁 data/                    ← Données
│   ├── training_wellbeing_data.json  ← Dataset d'entraînement
│   └── mood_history.json       ← Historique des conversations
│
├── 📁 notebooks/               ← Notebooks Jupyter
│   └── 02_finetuning_bert_gpu.ipynb  ← Entraînement sur GPU
│
└── 📁 docs/                    ← Documentation
    └── PRESENTATION.md         ← Ce fichier !
```

### 🔄 Pipeline Principal

```
┌─────────────────────────────────────────────────────────────┐
│                    UTILISATEUR                               │
│                        │                                     │
│                        ▼                                     │
│              ┌─────────────────┐                            │
│              │  "Je suis triste" │  ← Message texte          │
│              └────────┬────────┘                            │
│                       │                                      │
│                       ▼                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           SENTIMENT ANALYZER                          │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │              BERT Fine-tuné                   │    │   │
│  │  │         (110M paramètres)                     │    │   │
│  │  │                                               │    │   │
│  │  │  1. Tokenization (découpage en mots)         │    │   │
│  │  │  2. Embedding (conversion en vecteurs)       │    │   │
│  │  │  3. Attention (comprendre le contexte)       │    │   │
│  │  │  4. Classification (5 catégories)            │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                       │                              │   │
│  │                       ▼                              │   │
│  │  Résultat: "négatif" (85% confiance)                │   │
│  └─────────────────────────────────────────────────────┘   │
│                       │                                      │
│                       ▼                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           MOOD TRACKER                               │   │
│  │                                                      │   │
│  │  • Enregistre le sentiment                          │   │
│  │  • Calcule la tendance (7 derniers jours)           │   │
│  │  • Sauvegarde dans mood_history.json                │   │
│  └─────────────────────────────────────────────────────┘   │
│                       │                                      │
│                       ▼                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           CBT ENGINE (Thérapie Cognitive)            │   │
│  │                                                      │   │
│  │  • Analyse les distorsions cognitives               │   │
│  │  • Détecte: "Tout-ou-rien", "Catastrophisation"...  │   │
│  │  • Génère des questions de restructuration          │   │
│  └─────────────────────────────────────────────────────┘   │
│                       │                                      │
│                       ▼                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           RESPONSE GENERATOR                         │   │
│  │                                                      │   │
│  │  • Sélectionne un template de réponse               │   │
│  │  • Ajoute les éléments CBT                          │   │
│  │  • Propose des actions comportementales             │   │
│  └─────────────────────────────────────────────────────┘   │
│                       │                                      │
│                       ▼                                      │
│              ┌─────────────────┐                            │
│              │  Réponse finale  │                            │
│              │  + Suggestions   │                            │
│              │  + Actions       │                            │
│              └─────────────────┘                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Les Deux Approches

### 🔬 Approche 1 : Feature Extraction (82% précision)

**Principe :**
- Utiliser BERT comme un "extracteur de caractéristiques"
- BERT est **gelé** (on ne modifie pas ses poids)
- On ajoute une couche de classification par-dessus

**Avantages :**
- ✅ Rapide à entraîner
- ✅ Peu de données nécessaires
- ✅ Fonctionne sur CPU

**Inconvénients :**
- ❌ Moins précis
- ❌ Ne s'adapte pas aux nuances du bien-être

**Code simplifié :**
```python
# BERT est gelé (pas de mise à jour)
for param in bert_model.parameters():
    param.requires_grad = False

# On extrait les features
features = bert_model(text)

# On classifie avec une nouvelle couche
sentiment = classifier(features)
```

### 🎯 Approche 3 : Fine-tuning BERT (85% précision) ⭐

**Principe :**
- Modifier les poids de BERT lui-même
- BERT apprend les nuances spécifiques au bien-être
- Entraînement complet du modèle

**Avantages :**
- ✅ Plus précis (+3%)
- ✅ Comprend mieux le contexte émotionnel
- ✅ Meilleure détection des cas limites

**Inconvénients :**
- ❌ Plus long à entraîner
- ❌ Nécessite un GPU
- ❌ Risque de sur-apprentissage

**Code simplifié :**
```python
# BERT est dégelé (mise à jour permise)
for param in bert_model.parameters():
    param.requires_grad = True

# Entraînement complet
for epoch in range(3):
    for batch in dataloader:
        # Forward pass
        outputs = bert_model(batch)
        loss = criterion(outputs, labels)
        
        # Backward pass (mise à jour de TOUS les poids)
        loss.backward()
        optimizer.step()
```

### 📊 Comparaison

| Critère | Approche 1 | Approche 3 |
|---------|------------|------------|
| **Précision** | 82% | **85%** ⭐ |
| **Temps d'entraînement** | 5 minutes | 30 minutes |
| **Matériel requis** | CPU | GPU |
| **Données nécessaires** | 200 exemples | 500 exemples |
| **Complexité** | Facile | Moyenne |

### 🏆 Pourquoi on utilise l'Approche 3 ?

- **+3% de précision** = moins d'erreurs
- Meilleure compréhension des **nuances émotionnelles**
- Plus **professionnel** pour un projet de fin d'études

---

## 6. Le Module CBT (Thérapie Cognitive)

### 🧠 Qu'est-ce que la CBT ?

**CBT** = Cognitive Behavioral Therapy (Thérapie Cognitivo-Comportementale)

C'est une méthode de psychothérapie qui aide à :
1. **Identifier** les pensées négatives automatiques
2. **Questionner** leur validité
3. **Remplacer** par des pensées plus réalistes

### 🔍 Les 5 Distorsions Cognitives Détectées

| Distorsion | Description | Exemple |
|------------|-------------|---------|
| **Catastrophisation** | Imaginer le pire scénario | "Si je rate cet examen, ma vie est foutue" |
| **Tout-ou-rien** | Pensée en noir et blanc | "Je suis soit parfait, soit nul" |
| **Surgénéralisation** | Généraliser à partir d'un cas | "J'ai raté une fois, je rate toujours" |
| **Lecture de pensées** | Deviner ce que pensent les autres | "Il pense sûrement que je suis idiot" |
| **Raisonnement émotionnel** | Confondre émotion et réalité | "Je me sens nul, donc je suis nul" |

### 📝 Comment le Bot Détecte ?

**Mots-clés utilisés :**

```python
PATTERNS = {
    'catastrophisation': [
        'catastrophe', 'terrible', 'horrible', 'fin du monde',
        'jamais m\'en remettre', 'foutu', 'fichu'
    ],
    'tout_ou_rien': [
        'toujours', 'jamais', 'tout', 'rien', 'complètement',
        'totalement', 'parfait', 'nul'
    ],
    'surgeneralisation': [
        'tout le monde', 'personne', 'chaque fois',
        'à chaque fois', 'encore une fois'
    ],
    # ... etc
}
```

### 💬 Questions Socratiques

Quand une distorsion est détectée, le bot pose des **questions pour faire réfléchir** :

| Distorsion | Question Socratique |
|------------|---------------------|
| Catastrophisation | "Quel est le scénario le plus réaliste ?" |
| Tout-ou-rien | "Y a-t-il des nuances entre ces deux extrêmes ?" |
| Surgénéralisation | "Est-ce vraiment TOUJOURS le cas ?" |
| Lecture de pensées | "Comment peux-tu être sûr de ce qu'il pense ?" |
| Raisonnement émotionnel | "Est-ce que se sentir ainsi prouve que c'est vrai ?" |

### 💡 Actions Comportementales

Le bot propose des **actions concrètes** selon l'émotion :

**Pour la dépression :**
- 🚶 Faire une courte promenade (10 minutes)
- 📝 Écrire 3 choses positives de la journée
- 📞 Appeler un ami ou un proche

**Pour l'anxiété :**
- 🧘 Exercice de respiration 4-7-8
- 🎯 Se concentrer sur l'instant présent
- 📋 Faire une liste des choses sous ton contrôle

**Pour le stress :**
- ⏸️ Faire une pause de 5 minutes
- 🎵 Écouter une musique relaxante
- 📊 Prioriser les tâches (urgent vs important)

---

## 7. Comment fonctionne le Bot ?

### 📥 Étape 1 : Réception du Message

```python
message = "Je suis complètement nul, je rate tout"
```

### 🔤 Étape 2 : Tokenization

Le texte est découpé en **tokens** (morceaux) :

```
["[CLS]", "je", "suis", "complète", "##ment", "nul", ",", "je", "rate", "tout", "[SEP]"]
```

- `[CLS]` = début de séquence
- `[SEP]` = fin de séquence
- `##ment` = sous-mot (continuation de "complète")

### 🔢 Étape 3 : Conversion en Nombres

Chaque token devient un nombre (ID) :

```python
[101, 2183, 5765, 9876, 1234, 5678, 102]
```

### 🧮 Étape 4 : Passage dans BERT

```
Tokens → Embedding Layer → 12 couches Transformer → Vecteur de sortie
```

Le vecteur de sortie a **768 dimensions** (768 nombres qui représentent le sens du texte).

### 📊 Étape 5 : Classification

Le vecteur passe dans une couche de classification :

```python
# Couche de classification
logits = classifier(bert_output)  # [0.1, 0.1, 0.05, 0.35, 0.4]

# Softmax pour avoir des probabilités
probs = softmax(logits)

# Classes: [très_positif, positif, neutre, négatif, très_négatif]
# Résultat: très_négatif (40%)
```

### 🧠 Étape 6 : Analyse CBT

```python
# Recherche de patterns
if "complètement" in message and "nul" in message:
    distortion = "tout_ou_rien"
    
if "tout" in message and "rate" in message:
    distortion = "surgénéralisation"
```

### 💬 Étape 7 : Génération de Réponse

```python
response = {
    "main_response": "Je comprends que tu te sens découragé...",
    "distortions_detected": ["tout_ou_rien", "surgénéralisation"],
    "socratic_question": "Est-ce vraiment TOUT que tu rates ?",
    "behavioral_actions": [
        "Écris 3 choses que tu as réussies récemment",
        "Fais une pause de 5 minutes"
    ]
}
```

### 🖥️ Étape 8 : Affichage

L'interface web affiche :
- La bulle de réponse
- Le tag de sentiment (😢 très négatif)
- Les distorsions détectées
- Les actions suggérées

---

## 8. L'Interface Web

### 🎨 Design

L'interface utilise un **thème sombre** pour :
- Réduire la fatigue oculaire
- Créer une ambiance apaisante
- Meilleure lisibilité

### 🧩 Composants

| Composant | Description |
|-----------|-------------|
| **Header Hero** | Bannière avec titre et badges |
| **Zone de Chat** | Messages utilisateur et bot |
| **Barre de Saisie** | Input + bouton envoi |
| **Statistiques** | 4 cartes (Session, Humeur, Total, CBT) |
| **Graphiques** | Évolution, Distribution, Confiance |
| **Sidebar** | Menu, historique, guide CBT |

### 🖼️ Captures d'Écran (Description)

**Zone de Chat :**
```
┌─────────────────────────────────────────┐
│  👤 Toi                          14:32  │
│  Je me sens triste aujourd'hui          │
│                    ┌────────────────────┤
│                    │ Bulle violette     │
└────────────────────┴────────────────────┘

┌────────────────────┐
│ Bulle grise        │  🤖 Chatbot IA
│                    │  😔 négatif (85%)
├────────────────────┤
│ Je comprends...    │  14:32
└────────────────────┘
```

**Statistiques :**
```
┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐
│   💬   │  │   😊   │  │   📈   │  │   🧠   │
│   5    │  │  0.2   │  │   32   │  │   2    │
│Session │  │Humeur  │  │ Total  │  │  CBT   │
└────────┘  └────────┘  └────────┘  └────────┘
```

---

## 9. Résultats et Performances

### 📊 Métriques du Modèle

| Métrique | Valeur |
|----------|--------|
| **Précision (Accuracy)** | 85% |
| **Paramètres** | 110 millions |
| **Temps d'inférence** | ~200ms |
| **Classes** | 5 (très négatif → très positif) |

### 📈 Comparaison des Approches

```
Précision (%)
│
│  85% ████████████████████ Approche 3 (Fine-tuning)
│  82% █████████████████    Approche 1 (Feature Extraction)
│
└────────────────────────────────────────
```

### 🎯 Exemples de Prédictions

| Message | Prédiction | Confiance |
|---------|------------|-----------|
| "Je suis super content !" | très positif | 92% |
| "Ça va bien" | positif | 78% |
| "Bof" | neutre | 65% |
| "Je suis triste" | négatif | 85% |
| "Je suis complètement nul" | très négatif | 89% |

### 🔥 Enrichissement CBT

```
Sans CBT:  "Je comprends que c'est difficile"

Avec CBT:  "Je comprends que c'est difficile. 
           Je remarque une pensée 'tout-ou-rien'. 
           Est-ce vraiment tout ou rien ?
           Suggestion: Écris 3 choses positives"

Enrichissement: +782%
```

---

## 10. Comment Utiliser le Projet

### 📋 Prérequis

1. **Python 3.10+** installé
2. **Git** installé
3. **8 Go de RAM** minimum (pour BERT)

### 📥 Installation

```bash
# 1. Cloner le projet
git clone https://github.com/ton-username/chatbot-bien-etre.git
cd chatbot-bien-etre

# 2. Créer un environnement virtuel
python -m venv .venv

# 3. Activer l'environnement
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

### 🚀 Lancement

**Option 1 : Double-clic**
- Double-clique sur `launch_interface.bat`

**Option 2 : Ligne de commande**
```bash
streamlit run ui/streamlit_app.py
```

**Option 3 : Menu**
```bash
menu.bat
# Puis choisir l'option 2
```

### 🖥️ Utilisation

1. Le navigateur s'ouvre sur `http://localhost:8502`
2. Écris un message dans la barre de chat
3. Appuie sur **Entrée** ou clique sur **📤**
4. Le bot analyse et répond !

---

## 11. Ce que j'ai Appris

### 🧠 Concepts d'IA

- **NLP** (Natural Language Processing) : Comment les ordinateurs comprennent le texte
- **Transformers** : L'architecture révolutionnaire derrière BERT et GPT
- **Attention** : Comment le modèle se concentre sur les mots importants
- **Fine-tuning** : Adapter un modèle pré-entraîné à une tâche spécifique
- **Transfer Learning** : Réutiliser les connaissances d'un modèle existant

### 💻 Compétences Techniques

- **Python avancé** : Classes, décorateurs, gestion d'erreurs
- **PyTorch** : Création et entraînement de réseaux de neurones
- **Hugging Face** : Utilisation de modèles pré-entraînés
- **Streamlit** : Création d'interfaces web
- **Git** : Gestion de versions

### 🎨 Design & UX

- **Thème sombre** : Meilleur pour les yeux
- **Responsive design** : S'adapte à la taille de l'écran
- **Feedback visuel** : L'utilisateur sait ce qui se passe

### 🧘 Psychologie

- **CBT** : Thérapie cognitivo-comportementale
- **Distorsions cognitives** : Erreurs de pensée courantes
- **Questions socratiques** : Guider vers la réflexion

---

## 12. Ressources

### 📚 Pour Apprendre le NLP

| Ressource | Description | Lien |
|-----------|-------------|------|
| **Hugging Face Course** | Cours gratuit sur les Transformers | [huggingface.co/course](https://huggingface.co/course) |
| **Stanford CS224N** | Cours universitaire NLP | [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ) |
| **Jay Alammar Blog** | Visualisations des Transformers | [jalammar.github.io](http://jalammar.github.io/) |

### 📖 Papers Importants

| Paper | Année | Importance |
|-------|-------|------------|
| **Attention Is All You Need** | 2017 | L'architecture Transformer |
| **BERT** | 2018 | Le modèle qu'on utilise |
| **CamemBERT** | 2019 | BERT pour le français |

### 🛠️ Outils Utiles

| Outil | Usage |
|-------|-------|
| **Google Colab** | GPU gratuit pour entraîner |
| **Weights & Biases** | Suivi des expériences |
| **Streamlit** | Interfaces web rapides |

### 🧘 Ressources CBT

| Ressource | Description |
|-----------|-------------|
| **Feeling Good** (David Burns) | Livre de référence sur la CBT |
| **MoodGym** | Programme CBT en ligne gratuit |

---

## 🙏 Remerciements

Ce projet a été réalisé dans le cadre de mes études à **ENSA Berrechid**.

Merci à :
- **Hugging Face** pour les modèles pré-entraînés
- **Streamlit** pour la simplicité de création d'interfaces
- **La communauté open-source** pour tous les outils

---

## 📞 Contact

Pour toute question sur ce projet :
- 📧 Email : [ton-email]
- 🐙 GitHub : [ton-github]

---

*Créé avec ❤️ et beaucoup de ☕ - Janvier 2026*
