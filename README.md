# 🧠 Chatbot Bien-être Mental - Approche 3 Hybride

**Chatbot intelligent combinant l'analyse de sentiment (BERT) avec la thérapie cognitivo-comportementale (CBT) et l'IA générative (Gemini).**

Développé à **ENSA Berrechid** par **Salma Bouziane Ouaritini** et **Imrane Hajji** (ISIBD 2025-2026).

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Interface-Streamlit-red.svg)](https://streamlit.io)
[![BERT](https://img.shields.io/badge/Model-BERT-orange.svg)](https://huggingface.co)
[![Gemini](https://img.shields.io/badge/IA-Google%20Gemini-yellow.svg)](https://ai.google.dev/)

---

## 🎯 Vue d'ensemble

Le **Chatbot Bien-être** est un assistant IA empathique qui :
- **Écoute** les préoccupations émotionnelles
- **Analyse** les sentiments en temps réel
- **Détecte** les distorsions cognitives problématiques
- **Répond** avec empathie et conseils thérapeutiques
- **Suit** l'évolution émotionnelle dans le temps

### ✨ Caractéristiques principales
✅ Analyse de sentiment précise (5 catégories)  
✅ Confiance dynamique (30-99%) basée sur le contexte  
✅ Module CBT pour détection de distorsions cognitives  
✅ Réponses personnalisées via Gemini (avec fallback intelligent)  
✅ Historique persistant avec visualisations Plotly  
✅ Confidentialité garantie (données stockées localement)  
✅ Interface Web fluide et responsive (Streamlit)  

---

## 🚀 Démarrage rapide

### Installation

```bash
# Cloner/accéder au projet
cd "Chatbot bien-être"

# Créer environnement virtuel
python -m venv .venv

# Activer (Windows)
.venv\Scripts\activate

# Installer dépendances
pip install -r requirements.txt
```

### Lancer l'application

```bash
streamlit run ui/streamlit_app.py
```

Accédez à : **http://localhost:8501**

---

## 🏗️ Architecture Approche 3

C'est un pipeline **Hybride** à 5 étapes :

```
Message Utilisateur
    ↓
[1] SentimentAnalyzer (BERT/Keywords)
    └─ Détecte: {sentiment, confidence}
    ↓
[2] CBTEngine (Détection Distorsions)
    └─ Scanne: {distortions, is_crisis}
    ↓
[3] MoodTracker (Persistance)
    └─ Sauvegarde: JSON historique
    ↓
[4] ResponseGenerator
    ├─ Plan A: Gemini API (réponse créative)
    └─ Plan B: Templates (fallback)
    └─ Retourne: {response, advice, encouragement}
    ↓
[5] UI Streamlit
    └─ Affiche: Message + Graphiques + Stats
```

### Les trois "cerveaux"

| Composant | Rôle | Technologie |
|-----------|------|-------------|
| **BERT Fine-tuné** | Classification sentiment | Transformers NLP |
| **CBT Engine** | Détection thérapeutique | Regex + Rules |
| **Gemini** | Génération réponse | Google Cloud API |

---

## 📂 Structure du projet

```
Chatbot bien-être/
├── README.md                    # Ce fichier
├── requirements.txt             # Dépendances
├── config.yaml                  # Configuration
├── launch_interface.bat         # Lancer l'app
│
├── src/
│   ├── cbt_engine.py           # 🧠 Module CBT
│   ├── gemini_wrapper.py       # 💬 Wrapper Gemini
│   │
│   ├── approach1/              # Fallback (templates)
│   │   ├── mood_tracker.py     # Persistance JSON
│   │   ├── response_generator.py # Templates
│   │   └── mood_visualizer.py  # Graphiques
│   │
│   └── approach3/              # ⭐ APPROCHE FINALE
│       ├── chatbot.py          # WellbeingChatbot
│       ├── sentiment_analyzer.py # BERT analysis
│       ├── keyword_analyzer.py # Keywords
│       ├── mood_tracker.py     # Tracking
│       └── response_generator.py # Réponses
│
├── ui/
│   ├── streamlit_app.py        # 🎨 Interface Web
│   └── streamlit_test.py       # Tests UI
│
├── notebooks/
│   ├── 01_exploration_data.ipynb
│   ├── 02_finetuning_bert_gpu.ipynb
│   └── Partie_1_MNIST.ipynb    # MNIST CNN
│
├── data/
│   ├── mood_history.json       # 💾 Historique
│   ├── training_wellbeing_data.json
│   └── mood_test.json
│
├── models/
│   └── approach3/
│       ├── bert_finetuned/     # 🤖 BERT
│       └── keyword_models/
│
├── docs/                        # 📚 Documentation consolidée
│   ├── 01_APPROACH3_COMPLETE_GUIDE.md
│   ├── 02_CBT_MODULE_GUIDE.md
│   ├── 03_INTERFACE_USER_GUIDE.md
│   ├── 04_INSTALLATION_GUIDE.md
│   └── 05_RAPPORT_FINAL_COMPLET.md
│
├── comparison/                  # 🔬 Analyse comparative
│   ├── compare_approaches.py
│   ├── DEEP_ANALYSIS.md
│   └── SYNTHESIS.py
│
└── tests/
    └── (divers tests)
```

---

## 🔑 Composants clés

### 1. **SentimentAnalyzer** (`src/approach3/sentiment_analyzer.py`)
Analyse le sentiment en 5 catégories avec confiance :
- **Très Positif** (+1.0)
- **Positif** (+0.5)
- **Neutre** (0.0)
- **Négatif** (-0.5)
- **Très Négatif** (-1.0)

### 2. **CBTEngine** (`src/cbt_engine.py`)
Détecte 5 distorsions cognitives (pensées fausses) :
1. **Surgénéralisation** ("toujours raté")
2. **Pensée Tout-ou-Rien** ("tout ou rien")
3. **Lecture de pensées** ("il pense que...")
4. **Raisonnement émotionnel** ("je sens = réalité")
5. **Catastrophisation** ("terrible", "horrible")

### 3. **MoodTracker** (`src/approach1/mood_tracker.py`)
Gère la persistance et statistiques :
- Sauvegarde en JSON
- Statistiques (moyenne, médiane, écart-type)
- Tendances 7/14/30 jours
- Détection patterns

### 4. **GeminiChatbot** (`src/gemini_wrapper.py`)
Wraps Google Gemini API :
- Injection contexte thérapeutique
- Gestion erreurs réseau
- Détection situations critiques

### 5. **Streamlit App** (`ui/streamlit_app.py`)
Interface Web interactive :
- Chat temps réel
- Historique messages
- Graphiques Plotly (évolution + distribution)
- Statistiques en direct

---

## 💾 Gestion des données

### Historique (format JSON)
```json
{
  "user_id": "default_user",
  "mood_history": [
    {
      "timestamp": "2026-01-15T18:00:00",
      "text": "Je suis nul...",
      "sentiment": "très négatif",
      "confidence": 0.96,
      "score": -1.0
    }
  ]
}
```

### Confidentialité
✅ Données stockées localement (`data/mood_history.json`)  
✅ Aucun upload (sauf contexte anonymisé à Gemini)  
✅ Suppression instantanée possible  

---

## 🧪 Exemple du pipeline

**Input :** "Je suis nul, personne ne m'aime, je rate toujours tout"

**Processus :**
1. **Sentiment** → Détecté "Très Négatif" (96%)
2. **CBT** → Identifie:
   - ⚠️ Surgénéralisation ("toujours")
   - ⚠️ Lecture de pensée ("personne ne m'aime")
   - ⚠️ Étiquetage ("je suis nul")
3. **Tracking** → Enregistré dans mood_history.json
4. **Gemini** → Génère réponse empathique guidée par le contexte CBT
5. **UI** → Affiche réponse + tags distorsions + conseils

---

## 📦 Dépendances principales

```
streamlit==1.52.2              # Interface Web
plotly==5.17.0                 # Graphiques interactifs
google-generativeai==1.58.0    # Gemini API
transformers==4.30.0           # BERT
torch==2.0.0                   # PyTorch
numpy==1.24.0
pandas==2.0.0
pyyaml==6.0
```

Voir `requirements.txt` pour la liste complète.

---

## ❓ FAQ

**Q: Que se passe-t-il si Gemini ne fonctionne pas ?**  
R: Bascule automatique en mode Fallback avec templates pré-rédigés.

**Q: Où sont stockées les données utilisateur ?**  
R: Localement dans `data/mood_history.json` - aucun serveur externe.

**Q: Peut-on utiliser sans clé API Gemini ?**  
R: Oui, en mettant `use_gemini=False` dans `src/approach3/chatbot.py`.

**Q: Comment ajouter une nouvelle distorsion CBT ?**  
R: Éditer `src/cbt_engine.py`, ajouter pattern regex + keywords.

**Q: Quel est le coût d'utilisation ?**  
R: Gratuit (sauf si Gemini API quotas dépassés). L'app fonctionne aussi hors-ligne avec fallbacks.

---

## 📚 Documentation détaillée

Voir le dossier **`docs/`** :
- `01_APPROACH3_COMPLETE_GUIDE.md` - Guide technique complet (approche hybride BERT + Gemini)
- `02_CBT_MODULE_GUIDE.md` - Module thérapeutique (distorsions, restructuration, actions)
- `03_INTERFACE_USER_GUIDE.md` - Guide utilisateur de l'interface Streamlit
- `04_INSTALLATION_GUIDE.md` - Installation, modèles, GPU, troubleshooting
- `05_RAPPORT_FINAL_COMPLET.md` - Rapport final consolidé

Voir le dossier **`comparison/`** :
- `compare_approaches.py` - Benchmark Approche 1 vs 3
- `DEEP_ANALYSIS.md` - Résultats détaillés
- `SYNTHESIS.py` - Synthèse comparative

---

## 👥 Contributeurs

- **Salma Bouziane Ouaritini** (ENSA Berrechid, ISIBD 2026)
- **Imrane Hajji** (ENSA Berrechid, ISIBD 2026)

**Superviseur académique :** M. Lahcen MOUMOUN

---

## 📄 Licence

Projet éducatif pour ENSA Berrechid, cursus ISIBD.

---

## 🔗 Ressources utiles

- [Documentation Streamlit](https://docs.streamlit.io/)
- [Transformers HuggingFace](https://huggingface.co/docs/transformers/)
- [Google Gemini API](https://ai.google.dev/)
- [CBT: Thérapie Cognitivo-Comportementale](https://fr.wikipedia.org/wiki/Th%C3%A9rapie_cognitivo-comportementale)
- [BERT & NLP](https://huggingface.co/docs/transformers/model_doc/bert)

---

**Dernière mise à jour :** 17 janvier 2026  
**Version :** Approche 3 Hybride (Production-Ready)
