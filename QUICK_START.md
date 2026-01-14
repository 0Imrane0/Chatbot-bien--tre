# 🚀 QUICK START - Chatbot Bien-Être IA

> **Guide rapide pour installer et lancer le chatbot en 5 minutes**

---

## 📋 Prérequis

Avant de commencer, assure-toi d'avoir :

| Prérequis | Version | Vérifier |
|-----------|---------|----------|
| **Python** | 3.10 ou plus | `python --version` |
| **pip** | Dernière version | `pip --version` |
| **RAM** | 8 Go minimum | Pour charger BERT (110M paramètres) |

---

## 🛠️ Installation (Une seule fois)

### Étape 1 : Ouvrir un Terminal

- **Windows** : Clic droit → "Ouvrir dans le Terminal" ou `cmd`
- **Mac/Linux** : Ouvrir le Terminal

### Étape 2 : Se placer dans le dossier du projet

```bash
cd "chemin/vers/Chatbot bien-être"
```

### Étape 3 : Créer un environnement virtuel

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

> 💡 Tu verras `(.venv)` au début de ta ligne de commande

### Étape 4 : Installer les dépendances

```bash
pip install -r requirements.txt
```

⏳ **Temps estimé** : 5-10 minutes (télécharge ~2 Go de modèles)

### Étape 5 : Télécharger les données NLTK (optionnel)

```bash
python setup_nltk.py
```

---

## 🎯 Lancement du Chatbot

### Option 1 : Double-clic (Windows) ⭐ RECOMMANDÉ

1. Double-clique sur **`launch_interface.bat`**
2. Une fenêtre noire s'ouvre et lance le serveur
3. Ton navigateur s'ouvre automatiquement sur `http://localhost:8502`

### Option 2 : Ligne de commande

```bash
# Activer l'environnement (si pas déjà fait)
# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate

# Lancer l'interface
streamlit run ui/streamlit_app.py --server.port 8502
```

### Option 3 : Menu interactif (Windows)

```bash
menu.bat
# Puis taper 2 et Entrée pour "Interface Web Avancée"
```

---

## 🖥️ Utilisation de l'Interface

### Premier Démarrage

1. **Attends le chargement** - Le modèle BERT (110M paramètres) prend ~10 secondes à charger
2. Tu verras dans le terminal : `✅ Modèle BERT chargé (110M paramètres)`

### Comment Chatter

1. **Écris ton message** dans la barre de saisie en bas
2. **Appuie sur Entrée** ou clique sur le bouton **📤 Envoyer**
3. Le bot analyse ton message et répond !

### Ce que tu vois

| Zone | Description |
|------|-------------|
| **💬 Chat** | Tes messages et les réponses du bot |
| **📊 Statistiques** | Messages session, humeur moyenne, total, CBT activations |
| **📈 Graphiques** | Évolution humeur, distribution sentiments, confiance |
| **📖 Sidebar** | Guide CBT, historique, paramètres |

---

## ⚠️ Problèmes Courants

### ❌ "Python n'est pas reconnu"

**Solution** : Installe Python depuis [python.org](https://www.python.org/downloads/) et coche "Add to PATH"

### ❌ "Module not found: torch"

**Solution** : Réinstalle les dépendances
```bash
pip install -r requirements.txt
```

### ❌ "Port 8502 déjà utilisé"

**Solution** : Ferme l'autre instance ou change le port
```bash
streamlit run ui/streamlit_app.py --server.port 8503
```

### ❌ "CUDA out of memory" ou erreur GPU

**Solution** : Le modèle fonctionne aussi sur CPU, pas besoin de GPU
```bash
# Forcer l'utilisation du CPU (dans le code c'est déjà géré)
```

### ❌ Le navigateur ne s'ouvre pas automatiquement

**Solution** : Ouvre manuellement `http://localhost:8502` dans ton navigateur

---

## 🛑 Arrêter le Chatbot

1. Va dans le terminal où tourne Streamlit
2. Appuie sur **Ctrl + C**
3. Le serveur s'arrête

---

## 📁 Structure Importante

```
Chatbot bien-être/
├── launch_interface.bat    ← Double-clique pour lancer !
├── requirements.txt        ← Liste des dépendances
├── ui/
│   └── streamlit_app.py    ← Interface web
├── src/
│   └── approach3/          ← Code du chatbot BERT fine-tuné
└── models/
    └── approach3/
        └── bert_finetuned/ ← Modèle entraîné (110M paramètres)
```

---

## 🎉 C'est Prêt !

Tu peux maintenant :
- ✅ Discuter avec le chatbot
- ✅ Voir l'analyse de tes émotions
- ✅ Recevoir des conseils CBT
- ✅ Suivre l'évolution de ton humeur

---

## 📞 Besoin d'Aide ?

- 📖 Lis la [PRESENTATION.md](docs/PRESENTATION.md) pour comprendre le projet
- 📄 Consulte le [RAPPORT_FINAL.md](docs/RAPPORT_FINAL.md) pour les détails techniques

---

*Créé avec ❤️ - Janvier 2026*
