# 🚀 INSTALLATION & SETUP - Guide Complet

## Vue d'ensemble

Ce guide couvre tout ce qu'il faut pour installer et configurer le chatbot de bien-être sur ton système. Nous couvrons Windows, Mac et Linux.

---

## Table des Matières

1. [Installation Rapide](#rapide)
2. [Installation Détaillée](#detaillee)
3. [Téléchargement des Modèles](#modeles)
4. [Configuration GPU (Optionnel)](#gpu)
5. [Résolution de Problèmes](#problemes)

---

## Installation Rapide (5 min) {#rapide}

### Windows - Méthode Automatique ⭐

**Étape 1: Double-clique `launch_interface.bat`**

C'est tout ! Le script fera automatiquement:
1. Créer l'environnement virtuel
2. Installer les dépendances
3. Télécharger les modèles
4. Lancer l'interface

### Mac / Linux - Méthode Automatique

```bash
# 1. Clone le projet
git clone <repo_url>
cd "Chatbot bien-être"

# 2. Exécute le script de setup
chmod +x setup.sh
./setup.sh

# 3. Lancer l'interface
python launch_interface.py
```

---

## Installation Détaillée (15 min) {#detaillee}

### Prérequis Système

**Windows:**
- Python 3.9+ (télécharger depuis python.org)
- 4-8 GB RAM minimum
- 3 GB espace disque

**Mac (M1/M2):**
- Python 3.9+ (via Homebrew recommandé)
- 4-8 GB RAM
- 3 GB espace disque
- CommandLineTools: `xcode-select --install`

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3.9 python3-pip python3-venv
```

### Étape 1: Cloner le Projet

```bash
# Via HTTPS
git clone https://github.com/user/chatbot-bien-etre.git
cd "Chatbot bien-être"

# Ou via SSH
git clone git@github.com:user/chatbot-bien-etre.git
cd "Chatbot bien-être"
```

### Étape 2: Créer l'Environnement Virtuel

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Étape 3: Installer les Dépendances

```bash
# Upgrade pip d'abord
pip install --upgrade pip setuptools wheel

# Installer les requirements
pip install -r requirements.txt
```

**Dépendances principales:**
```
transformers==4.35.2      # BERT
torch==2.1.1              # PyTorch
google-generativeai==0.3.0  # Gemini API
streamlit==1.28.1         # UI
plotly==5.17.0            # Graphiques
pyyaml==6.0               # Config
numpy==1.24.3             # Calculs
pandas==2.0.3             # Data processing
```

### Étape 4: Télécharger les Modèles

```bash
# Option A: Script Python automatique
python download_models.py

# Option B: Depuis Hugging Face manuellement
python scripts/download_models.py
```

⏳ **Attendre 10-15 minutes** (première fois seulement)

### Étape 5: Configuration API Gemini

**Créer un fichier `.env`:**
```bash
# À la racine du projet
echo GOOGLE_API_KEY="ta-clé-api" > .env
```

**Ou modifier `config.yaml`:**
```yaml
google_api_key: "ta-clé-api"
streamlit_port: 8501
```

Obtenir une clé API Gemini:
1. Aller sur [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Cliquer "Create API Key"
3. Copier la clé
4. Ajouter dans `.env` ou `config.yaml`

### Étape 6: Vérifier l'Installation

```bash
# Vérifier Python
python --version
# Output: Python 3.9+

# Vérifier Streamlit
streamlit --version
# Output: Streamlit, version 1.28+

# Vérifier BERT
python -c "from transformers import AutoModel; print('✅ Transformers OK')"
# Output: ✅ Transformers OK

# Vérifier Gemini
python -c "import google.generativeai; print('✅ Gemini OK')"
# Output: ✅ Gemini OK
```

### Étape 7: Lancer l'Interface

```bash
streamlit run ui/streamlit_app.py
```

🎉 Le navigateur s'ouvre automatiquement à `http://localhost:8501`

---

## Téléchargement des Modèles {#modeles}

### Pourquoi Télécharger?

Le modèle BERT fine-tuné est volumineux (638 MB), trop gros pour GitHub. Il est téléchargé depuis Hugging Face lors de la première utilisation.

### Modèles Nécessaires

```
models/
├── approach3/
│   └── bert_finetuned/          # BERT fine-tuné (420 MB)
│       ├── config.json
│       ├── pytorch_model.bin    # (ou model.safetensors)
│       ├── tokenizer.json
│       ├── vocab.txt
│       └── special_tokens_map.json
│
└── approach1/                   # (Optionnel - pré-entraîné)
    └── bert_pretrained/         # Téléchargé automatiquement
```

### Téléchargement Automatique

```python
# download_models.py
from transformers import BertTokenizer, BertForSequenceClassification

# BERT fine-tuned
model = BertForSequenceClassification.from_pretrained(
    "path/to/bert_finetuned",
    local_files_only=False
)
model.save_pretrained("models/approach3/bert_finetuned/")

# Tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
tokenizer.save_pretrained("models/approach3/bert_finetuned/")
```

### Téléchargement Manuel

```bash
# Si l'auto-téléchargement échoue
cd models/approach3

# Télécharger depuis Hugging Face
git clone https://huggingface.co/bert-base-multilingual-cased

# Ou via curl
curl -L -o bert_finetuned.zip <URL>
unzip bert_finetuned.zip
```

### Vérifier le Téléchargement

```bash
# Vérifier la structure
ls models/approach3/bert_finetuned/
# Output: config.json pytorch_model.bin tokenizer.json vocab.txt ...

# Ou en Python
import os
assert os.path.exists("models/approach3/bert_finetuned/config.json")
assert os.path.exists("models/approach3/bert_finetuned/pytorch_model.bin")
print("✅ Modèles vérifiés")
```

**Espace disque utilisé:**
- Modèle BERT: 420 MB
- Tokenizer: 231 MB
- Total: ~650 MB

---

## Configuration GPU (Optionnel) {#gpu}

### Pourquoi GPU?

- **CPU:** 80-100ms par analyse (acceptable)
- **GPU:** 20-30ms par analyse (optimal)

Pour le fine-tuning de BERT, GPU est recommandé.

### NVIDIA GPU Setup

**Prérequis:**
- GPU NVIDIA (pas AMD/Intel)
- CUDA 11.8 ou 12.1

**Installation CUDA:**

```bash
# 1. Télécharger CUDA
# https://developer.nvidia.com/cuda-downloads

# 2. Installer cuDNN
# https://developer.nvidia.com/cudnn

# 3. Vérifier l'installation
nvidia-smi
# Output: CUDA Version: 12.1, Driver Version: 535.x

# 4. Installer PyTorch avec CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**Vérifier PyTorch utilise GPU:**

```python
import torch
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"CUDA Version: {torch.version.cuda}")
print(f"GPU: {torch.cuda.get_device_name(0)}")

# Output:
# CUDA Available: True
# CUDA Version: 12.1
# GPU: NVIDIA GeForce RTX 3090
```

### Google Colab (GPU Gratuit)

Pour fine-tuning sans GPU local:

```python
# Dans notebook Colab
!pip install -r requirements.txt
!python src/approach3/train_finetuner.py

# Résultats: 3 min d'entraînement sur T4 GPU gratuit
```

### AMD GPU Setup (MacOS M1/M2)

```bash
# Metal acceleration (automatique)
# PyTorch utilise Metal Framework sur Mac M1/M2

pip install torch torchvision torchaudio
# Fonctionne avec acceleration GPU automatiquement
```

---

## Résolution de Problèmes {#problemes}

### ❌ "ModuleNotFoundError: No module named 'streamlit'"

**Cause:** Environnement virtuel pas activé ou pip install incomplet

**Solution:**
```bash
# 1. Vérifier activation
which python  # Mac/Linux: devrait être dans .venv/bin/
where python  # Windows: devrait être dans .venv\Scripts\

# 2. Réinstaller
pip install --upgrade pip
pip install -r requirements.txt

# 3. Vérifier
python -c "import streamlit; print(streamlit.__version__)"
```

### ❌ "python: No such file or directory"

**Cause:** Python non installé ou pas dans PATH

**Solution Windows:**
1. Désinstaller Python complètement
2. Réinstaller depuis python.org
3. **IMPORTANT:** Cocher "Add Python to PATH" pendant l'installation
4. Redémarrer l'ordinateur

**Solution Mac:**
```bash
# Installer via Homebrew
brew install python3.11
# Vérifier
python3 --version
```

### ❌ "Permission denied" ou "Access denied"

**Cause:** Manque de droits administrateur

**Solution Windows:**
- Clic droit sur `launch_interface.bat`
- "Exécuter en tant qu'administrateur"

**Solution Mac/Linux:**
```bash
sudo chown -R $USER:$USER .
chmod +x *.sh
```

### ❌ "Port 8501 already in use"

**Cause:** Un autre processus Streamlit est actif

**Solution:**
```bash
# Option 1: Utiliser un autre port
streamlit run ui/streamlit_app.py --server.port 8502

# Option 2: Tuer le processus (Linux/Mac)
lsof -i :8501
kill -9 <PID>

# Option 2: Tuer le processus (Windows)
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### ❌ "CUDA out of memory" ou erreur GPU

**Cause:** RAM GPU insuffisante

**Solution:**
```python
# Forcer CPU au lieu de GPU
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Ou réduire batch size
model = load_model(device='cpu')
```

### ❌ "Connection timeout" lors du téléchargement des modèles

**Cause:** Connexion internet lente ou serveur HF indisponible

**Solution:**
```bash
# Augmenter le timeout
pip install --default-timeout=1000 transformers

# Réessayer
python download_models.py
```

### ❌ Modèles ne téléchargent pas

**Cause:** Stockage plein ou permissions

**Solution:**
```bash
# Vérifier l'espace disque
# Windows: dir
# Linux/Mac: df -h

# Vérifier les permissions
chmod 755 models/
chmod 755 models/approach3/

# Télécharger manuellement depuis Hugging Face
# https://huggingface.co/models
```

### ❌ Streamlit s'arrête immédiatement

**Cause:** Erreur d'import ou configuration

**Solution:**
```bash
# 1. Lancer en debug
streamlit run ui/streamlit_app.py --logger.level=debug

# 2. Vérifier les imports
python -c "from src.approach3.sentiment_analyzer import SentimentAnalyzer"

# 3. Vérifier la config
cat config.yaml
```

---

## Vérification Complète

```bash
# Script de diagnostic
python -c "
import sys
print(f'Python: {sys.version}')

import streamlit; print(f'Streamlit: {streamlit.__version__}')
import torch; print(f'PyTorch: {torch.__version__}')
import transformers; print(f'Transformers: {transformers.__version__}')
import plotly; print(f'Plotly: {plotly.__version__}')

import google.generativeai; print('Google Generative AI: OK')
from src.cbt_engine import CBTEngine; print('CBT Engine: OK')
print('✅ All dependencies OK')
"
```

---

## Structure Post-Installation

Après installation complète:

```
Chatbot bien-être/
├── .venv/                         # Environnement virtuel
├── models/
│   └── approach3/
│       └── bert_finetuned/        # ✅ Téléchargé (650 MB)
├── data/
│   ├── mood_history.json          # ✅ Créé automatiquement
│   ├── training_wellbeing_data.json
│   └── ...
├── src/
│   ├── __init__.py
│   ├── cbt_engine.py
│   ├── gemini_wrapper.py
│   ├── approach3/
│   │   ├── sentiment_analyzer.py
│   │   ├── response_generator.py
│   │   ├── mood_tracker.py
│   │   └── ...
│   └── ...
├── ui/
│   ├── streamlit_app.py           # ✅ Interface principale
│   └── ...
├── .env                           # ✅ Clé API Gemini
├── config.yaml                    # ✅ Configuration
├── requirements.txt               # ✅ Dépendances
├── launch_interface.bat (Windows)
└── launch_interface.py (Mac/Linux)
```

---

## Prochaines Étapes

✅ **Installation terminée!**

Maintenant tu peux:

1. **Lancer l'interface:**
   ```bash
   streamlit run ui/streamlit_app.py
   ```

2. **Essayer un message:**
   - Clique sur une phrase rapide
   - Observe la réponse et les stats

3. **Explorer les features:**
   - Distorsions CBT détectées
   - Historique d'humeur
   - Graphiques en temps réel

4. **(Optionnel) Fine-tuner le modèle:**
   ```bash
   python src/approach3/train_finetuner.py
   # Ou via Colab notebook: notebooks/02_finetuning_bert_gpu.ipynb
   ```

---

## Support

Si tu rencontres un problème:

1. Vérifier la section "Résolution de Problèmes" ci-dessus
2. Consulter les logs: `streamlit run ui/streamlit_app.py --logger.level=debug`
3. Vérifier l'issue sur GitHub
4. Ouvrir une nouvelle issue avec les détails

---

**Dernière mise à jour:** 17 janvier 2026
**Status:** ✅ Installation Simplifiée & Testée
