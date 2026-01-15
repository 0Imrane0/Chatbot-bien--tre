# 📥 INSTALLATION - Chatbot Bien-Être IA

> **Guide d'installation complet - Résout tous les problèmes**

---

## 🚀 Installation Ultra-Rapide (Windows)

### **Étape 1 : Double-clique sur `setup.bat`** ⭐

```
setup.bat ← Clic droit + "Ouvrir"
```

**Ce que fait `setup.bat` :**
1. ✅ Crée l'environnement virtuel (`.venv`)
2. ✅ Installe toutes les dépendances (pip)
3. ✅ Configure tout automatiquement
4. ✅ Affiche les prochaines étapes

⏳ **Temps :** 5-10 minutes

---

### **Étape 2 : Double-clique sur `download_models.bat`**

```
download_models.bat ← Clic droit + "Ouvrir"
```

**Ce que fait ce script :**
- Télécharge le modèle BERT depuis Hugging Face (650 MB)

⏳ **Temps :** 10-15 minutes

---

### **Étape 3 : Double-clique sur `launch_interface.bat`**

```
launch_interface.bat ← Clic droit + "Ouvrir"
```

**Le navigateur s'ouvre automatiquement !** 🎉

---

## 🔧 Si tu as l'erreur "No module named streamlit"

### ❌ Problème
```
C:\Python313\python.exe: No module named streamlit
```

### ✅ Solutions

#### **Solution 1 : Exécuter setup.bat (RECOMMANDÉ)**
```
1. Double-clique sur setup.bat
2. Attends 5-10 minutes
3. Relance launch_interface.bat
```

#### **Solution 2 : Manuellement en ligne de commande**
```bash
# 1. Ouvrir PowerShell/CMD dans le dossier du projet
cd "C:\chemin\vers\Chatbot bien-être"

# 2. Créer l'environnement virtuel
python -m venv .venv

# 3. Activer l'environnement
.venv\Scripts\activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Télécharger les modèles
python download_models.py

# 6. Lancer l'interface
streamlit run ui/streamlit_app.py --server.port 8502
```

---

## 🆘 Autres Problèmes Courants

### ❌ "Python n'est pas reconnu"

**Cause :** Python n'est pas dans le PATH

**Solution :**
1. Désinstalle Python
2. Réinstalle depuis [python.org](https://www.python.org/downloads/)
3. **IMPORTANT** : Coche "Add Python to PATH"
4. Redémarre ton ordinateur

---

### ❌ "Permission denied" ou "Access denied"

**Cause :** Manque de droits administrateur

**Solution :**
1. Clic droit sur `setup.bat`
2. "Exécuter en tant qu'administrateur"

---

### ❌ "Module not found: transformers"

**Cause :** Installation incomplète

**Solution :**
```bash
# Supprimer le venv et recommencer
rmdir .venv /s /q
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt --upgrade
```

---

### ❌ "Port 8502 already in use"

**Cause :** Un autre processus utilise ce port

**Solution 1 (Facile) :**
Attendre 1 minute et relancer

**Solution 2 (Avancé) :**
```bash
# Changer le port dans launch_interface.bat
streamlit run ui/streamlit_app.py --server.port 8503
```

---

### ❌ "CUDA out of memory" ou erreur GPU

**Cause :** Pas de GPU ou pas assez de RAM

**Solution :**
- Le modèle fonctionne aussi sur **CPU** (plus lent mais ça marche)
- Ferme d'autres applications
- Redémarre ton ordinateur

---

## 📋 CHECKLIST D'INSTALLATION

### ✅ Avant de lancer setup.bat
- [ ] Python 3.10+ installé
- [ ] Git installé
- [ ] Connexion Internet stable
- [ ] 3 GB d'espace disque libre

### ✅ Après setup.bat
- [ ] Dossier `.venv` créé
- [ ] Pas d'erreur dans la fenêtre
- [ ] `download_models.bat` prêt à être lancé

### ✅ Après download_models.bat
- [ ] Dossier `models/approach3/bert_finetuned/` non vide
- [ ] Fichiers : config.json, pytorch_model.bin, tokenizer.json

### ✅ Avant launch_interface.bat
- [ ] Le navigateur s'ouvre
- [ ] URL : `http://localhost:8502`
- [ ] Message : "✅ Modèle BERT chargé (110M paramètres)"

---

## 🎯 Étapes Graphique

```
┌─────────────────────────────────────┐
│  1️⃣ setup.bat                       │
│  (Créé venv + installe dépendances) │
│                                     │
│  ❌ Erreur? → Voir section "Solutions"
│  ✅ OK?    → Étape suivante         │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  2️⃣ download_models.bat             │
│  (Télécharge BERT 650 MB)           │
│                                     │
│  ❌ Erreur? → Vérifier Internet      │
│  ✅ OK?    → Étape suivante         │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  3️⃣ launch_interface.bat            │
│  (Lance Streamlit)                  │
│                                     │
│  ✅ Navigateur s'ouvre!             │
│  ✅ Chatbot prêt à utiliser!        │
└─────────────────────────────────────┘
```

---

## 💻 Pour Utilisateurs Avancés (Mac/Linux)

```bash
# Créer environnement
python3 -m venv .venv
source .venv/bin/activate

# Installer dépendances
pip install -r requirements.txt

# Télécharger modèles
python download_models.py

# Lancer interface
streamlit run ui/streamlit_app.py --server.port 8502
```

---

## 📞 Besoin d'Aide ?

1. **Lire** : [QUICK_START.md](QUICK_START.md)
2. **Vérifier** : [README.md](README.md)
3. **Présentation** : [PRESENTATION.md](docs/PRESENTATION.md)

---

*Créé avec ❤️ - Janvier 2026*
