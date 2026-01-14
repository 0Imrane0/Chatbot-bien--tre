# 🚀 Guide d'Entraînement GPU - Approche 3

## 🎯 Objectif

Entraîner le modèle BERT fine-tuné sur GPU gratuit (Google Colab) pour l'Approche 3.

**Durée totale : 5-10 minutes** (dont 2-3 min d'entraînement GPU)

---

## 📋 Option 1 : Google Colab (RECOMMANDÉ ⭐)

### Étape 1 : Ouvrir le notebook

1. Ouvrir Google Colab : https://colab.research.google.com/
2. `File` → `Upload notebook`
3. Sélectionner : `notebooks/02_finetuning_bert_gpu.ipynb`

### Étape 2 : Activer le GPU

**⚡ CRITIQUE - Sans GPU, ça prend 10 minutes!**

1. Menu : `Runtime` → `Change runtime type`
2. `Hardware accelerator` → Sélectionner **T4 GPU**
3. Cliquer `Save`

### Étape 3 : Exécuter toutes les cellules

1. Menu : `Runtime` → `Run all`
2. Attendre 2-3 minutes ⏳
3. Le modèle s'entraîne automatiquement

### Étape 4 : Télécharger le modèle

**Option A : Téléchargement direct**
```python
# Exécuter la cellule de compression
!zip -r bert_finetuned_final.zip bert_finetuned_final/
```
- Clic droit sur `bert_finetuned_final.zip` dans l'explorateur
- Télécharger (~280 MB)

**Option B : Sauvegarder sur Google Drive**
```python
from google.colab import drive
drive.mount('/content/drive')
!cp -r bert_finetuned_final /content/drive/MyDrive/
```

### Étape 5 : Installer localement

1. Extraire `bert_finetuned_final.zip`
2. Copier le dossier dans : `models/approach3/bert_finetuned/`
3. Structure finale :
```
models/
  approach3/
    bert_finetuned/
      config.json
      pytorch_model.bin
      tokenizer_config.json
      vocab.txt
      special_tokens_map.json
```

### Étape 6 : Tester

```bash
cd "C:\Users\LOQ\Documents\Chatbot bien-être"
python compare_approaches.py
```

✅ Vous devriez voir la comparaison Approche 1 vs Approche 3!

---

## 📋 Option 2 : Kaggle (Alternative)

### Avantages Kaggle
- 30h/semaine de GPU gratuit (vs 12h/jour Colab)
- GPU T4 ou P100
- Pas de déconnexion automatique

### Étapes

1. Créer compte : https://www.kaggle.com/
2. `Notebooks` → `New Notebook`
3. Settings → `Accelerator` → **GPU T4**
4. Copier-coller le code du notebook Colab
5. Run all
6. Download output

---

## 🔍 Vérification du GPU

Avant d'entraîner, vérifier que le GPU est actif :

```python
import torch

if torch.cuda.is_available():
    print(f"✅ GPU: {torch.cuda.get_device_name(0)}")
    print(f"   Mémoire: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("❌ GPU non disponible!")
```

**Résultat attendu :**
```
✅ GPU: Tesla T4
   Mémoire: 15.0 GB
```

---

## 📊 Performances attendues

| Configuration | Temps entraînement (3 epochs) | Précision finale |
|---------------|-------------------------------|------------------|
| **GPU T4** (Colab) | ⚡ 2-3 minutes | ~91-95% |
| **GPU P100** (Kaggle) | ⚡ 1-2 minutes | ~91-95% |
| CPU (local) | 🐢 10-15 minutes | ~91-95% |

---

## 🎯 Résumé de l'entraînement

### Données
- **500 exemples** bien-être
- **5 classes** : très négatif, négatif, neutre, positif, très positif
- **100 exemples par classe** (équilibré)
- **Split 80/20** : 400 train / 100 validation

### Hyperparamètres
- **Learning rate** : 2e-5 (standard pour fine-tuning)
- **Batch size** : 16 (GPU) ou 8 (CPU)
- **Epochs** : 3
- **Optimizer** : AdamW
- **Weight decay** : 0.01

### Résultats attendus

**Training loss** :
- Epoch 1 : ~1.2
- Epoch 2 : ~0.6
- Epoch 3 : ~0.4

**Validation loss** :
- Epoch 1 : ~0.8
- Epoch 2 : ~0.5
- Epoch 3 : ~0.4

**Précision validation** : ~91-95%

---

## ❓ Troubleshooting

### Problème 1 : GPU non disponible sur Colab

**Solution :**
1. Runtime → Disconnect and delete runtime
2. Runtime → Change runtime type → T4 GPU
3. Runtime → Run all

### Problème 2 : Out of memory (OOM)

**Solution :** Réduire le batch size
```python
per_device_train_batch_size=8,  # Au lieu de 16
```

### Problème 3 : Téléchargement lent

**Solution :** Utiliser Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')
!cp -r bert_finetuned_final /content/drive/MyDrive/
```

### Problème 4 : Modèle ne charge pas localement

**Vérifier la structure :**
```bash
ls models/approach3/bert_finetuned/
```

**Fichiers requis :**
- config.json
- pytorch_model.bin
- tokenizer_config.json
- vocab.txt

---

## 🚀 Commandes rapides

### Entraînement local (CPU - si vous insistez)
```bash
cd "C:\Users\LOQ\Documents\Chatbot bien-être"
python src/approach3/train_finetuner.py
```
⏳ Durée : 10-15 minutes

### Comparaison Approche 1 vs 3
```bash
python compare_approaches.py
```

### Test du chatbot Approche 3
```bash
python -c "from src.approach3.chatbot import WellbeingChatbot; bot = WellbeingChatbot(); bot.start_conversation()"
```

---

## ✅ Checklist finale

- [ ] Notebook uploadé sur Colab
- [ ] GPU T4 activé
- [ ] Toutes les cellules exécutées
- [ ] Modèle téléchargé (`bert_finetuned_final.zip`)
- [ ] Modèle extrait dans `models/approach3/bert_finetuned/`
- [ ] Testé avec `compare_approaches.py`
- [ ] Approche 3 fonctionne! 🎉

---

## 📚 Ressources

- **Google Colab** : https://colab.research.google.com/
- **Kaggle Notebooks** : https://www.kaggle.com/code
- **HuggingFace Docs** : https://huggingface.co/docs/transformers/
- **PyTorch GPU** : https://pytorch.org/get-started/locally/

---

**Bon entraînement! 🚀**
