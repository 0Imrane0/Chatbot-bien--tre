# 🤖 Chatbot de Bien-être et d'Humeur

## 📋 Description du Projet

Chatbot conversationnel intelligent qui analyse le sentiment des messages utilisateur, suit l'évolution de l'humeur dans le temps, et fournit des conseils personnalisés de bien-être.

**Projet académique** - ENSA Berrechid - Module : Programmation Python et IA

---

## 🎯 Fonctionnalités

- ✅ **Analyse de sentiment** en temps réel (positif, négatif, neutre)
- ✅ **Suivi de l'humeur** avec historique et tendances
- ✅ **Conseils personnalisés** adaptés à l'état émotionnel
- ✅ **Détection de crise** avec ressources d'aide
- ✅ **Interface console** et **interface web** (Streamlit)
- ✅ **Export des données** pour analyse
- ✅ **Support multilingue** (FR, EN, AR)

---

## 🚀 Deux Approches Implémentées

### Approche 1 : Transfer Learning (Modèle Pré-entraîné)
- Utilise BERT multilingue de Hugging Face
- Rapide à mettre en place
- Très précis (entraîné sur millions de textes)
- **Recommandé pour débuter**

### Approche 2 : Deep Learning Custom
- Réseau de neurones LSTM/GRU construit from scratch
- Données d'entraînement personnalisées
- Contrôle total sur le modèle
- **Pour approfondir le Deep Learning**

---

## 📦 Installation

### Prérequis
- Python 3.9 ou supérieur
- pip
- 4 GB RAM minimum
- Connexion internet (pour télécharger les modèles)

### Étapes

1. **Cloner/Télécharger le projet**
```bash
cd "C:\Users\LOQ\Documents\Chatbot bien-être"
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement**
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Télécharger les ressources NLTK** (première fois seulement)
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

---

## 🎮 Utilisation

### Interface Console
```bash
python main.py --mode console --approach 1
```

### Interface Web (Streamlit)
```bash
streamlit run ui/streamlit_ui.py
```

### Commandes Spéciales (Console)
- `/stats` - Afficher les statistiques d'humeur
- `/history` - Voir l'historique des conversations
- `/export` - Exporter les données
- `/help` - Aide
- `/quit` - Quitter

---

## 📁 Structure du Projet

```
chatbot-bien-etre/
├── data/                  # Données et historiques
├── models/                # Modèles sauvegardés
├── src/                   # Code source
│   ├── approach1/         # Approche 1
│   └── approach2/         # Approche 2
├── tests/                 # Tests unitaires
├── notebooks/             # Jupyter notebooks
├── ui/                    # Interfaces utilisateur
├── docs/                  # Documentation
├── config.yaml            # Configuration
├── requirements.txt       # Dépendances
└── main.py                # Point d'entrée
```

---

## 🧪 Tests

```bash
pytest tests/ -v
```

---

## 📊 Exemples de Résultats

### Analyse de Sentiment
```
Utilisateur: "Je suis vraiment heureux aujourd'hui !"
Chatbot: Sentiment détecté - POSITIF (confiance: 94%)
```

### Suivi d'Humeur
- Graphique d'évolution sur 7 jours
- Statistiques : % positif, négatif, neutre
- Détection de patterns

---

## 🛠️ Technologies Utilisées

- **Python 3.9+**
- **PyTorch** - Deep Learning
- **Transformers (Hugging Face)** - Modèles NLP
- **Streamlit** - Interface web
- **Plotly** - Visualisations
- **NLTK** - Traitement du langage

---

## 👨‍💻 Auteur

**Étudiant Ingénieur** - ENSA Berrechid
Module : Programmation Python et IA

---

## � Licence

Projet académique - ENSA Berrechid

---

## � Support

En cas de problème :
1. Vérifier que toutes les dépendances sont installées
2. Consulter les logs dans `logs/chatbot.log`
3. Voir la documentation dans `docs/`

---

## 🎓 Pour Aller Plus Loin

- Ajouter plus de langues
- Intégrer une API vocale
- Déployer sur le cloud
- Mobile app (React Native)

---

**Bonne utilisation ! 🚀**
