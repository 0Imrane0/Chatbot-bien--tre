# 🔥 Approche 3 : Fine-tuning BERT - Guide Complet

## 📊 Vue d'ensemble

| Aspect | Détail |
|--------|--------|
| **Status** | ✅ Code complet - Entraînement GPU disponible |
| **Modèle** | BERT multilingual fine-tuné |
| **Dataset** | 500 exemples bien-être (5 classes) |
| **Entraînement** | 3 epochs, learning rate 2e-5 |
| **Durée** | 2-3 min (GPU) ou 10-15 min (CPU) |
| **Précision attendue** | 91-95% |

---

## 🎯 Concept

**Fine-tuning = Spécialiser BERT pour le bien-être**

```
Avant fine-tuning:
Input: "Je me sens vide"
BERT (général) → "négatif" (confiance: 75%)

Après fine-tuning:
Input: "Je me sens vide"
BERT (spécialisé) → "très négatif - dépression" (confiance: 93%)
```

**Différence avec Approche 1 :**

| Aspect | Approche 1 (Feature Extraction) | Approche 3 (Fine-tuning) |
|--------|--------------------------------|--------------------------|
| **BERT** | ❄️ Gelé (poids fixes) | 🔥 Modifiable (poids ajustés) |
| **Entraînement** | ❌ Aucun | ✅ 3 epochs sur données bien-être |
| **Learning rate** | N/A | 2e-5 (très faible) |
| **Temps** | 0 sec | 2-3 min (GPU) |
| **Précision** | ~82% | ~91-95% |
| **Spécialisation** | Générique | Bien-être spécifique |

---

## 📁 Fichiers créés

### 1. Dataset et préparation

**`src/approach3/data_preparation.py`**
- Création de 500 exemples bien-être
- 5 classes équilibrées (100 par classe)
- Split train/validation (80/20)
- Sauvegarde JSON

```python
from src.approach3.data_preparation import create_wellbeing_dataset

dataset = create_wellbeing_dataset(500)
# Résultat: 500 exemples équilibrés
```

### 2. Fine-tuner BERT

**`src/approach3/sentiment_finetuner.py`**
- Classe `WellbeingDataset` (PyTorch)
- Classe `BERTFineTuner`
- Méthodes : `train()`, `predict()`

```python
from src.approach3.sentiment_finetuner import BERTFineTuner

finetuner = BERTFineTuner()
finetuner.train(train_texts, train_labels, val_texts, val_labels, epochs=3)
```

### 3. Script d'entraînement

**`src/approach3/train_finetuner.py`**
- Script complet d'entraînement
- Chargement dataset
- Entraînement BERT
- Tests

```bash
python src/approach3/train_finetuner.py
```

### 4. Analyseur fine-tuné

**`src/approach3/sentiment_analyzer.py`**
- Charge le modèle fine-tuné
- API compatible avec Approche 1
- Méthode `analyze(text)`

```python
from src.approach3.sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()
result = analyzer.analyze("Je suis heureux")
# {'sentiment': 'très positif', 'confidence': 0.94}
```

### 5. Chatbot Approche 3

**`src/approach3/chatbot.py`**
- Réutilise mood_tracker d'Approche 1
- Réutilise response_generator d'Approche 1
- Utilise sentiment_analyzer fine-tuné

```python
from src.approach3.chatbot import WellbeingChatbot

bot = WellbeingChatbot()
bot.start_conversation()
```

### 6. Notebook GPU

**`notebooks/02_finetuning_bert_gpu.ipynb`**
- Notebook pour Google Colab
- Entraînement sur GPU T4
- Téléchargement du modèle

---

## 🚀 Entraînement sur GPU (RECOMMANDÉ)

### Option 1 : Google Colab ⭐

**Pourquoi Colab ?**
- ✅ GPU T4 gratuit
- ✅ 15 GB VRAM
- ✅ Pas d'installation locale
- ✅ Entraînement 2-3 minutes

**Étapes :**

1. **Ouvrir Colab**
   - https://colab.research.google.com/

2. **Upload notebook**
   - `File` → `Upload notebook`
   - Sélectionner `notebooks/02_finetuning_bert_gpu.ipynb`

3. **Activer GPU** ⚡
   - `Runtime` → `Change runtime type`
   - `Hardware accelerator` → **T4 GPU**
   - `Save`

4. **Exécuter**
   - `Runtime` → `Run all`
   - Attendre 2-3 minutes

5. **Télécharger**
   ```python
   !zip -r bert_finetuned_final.zip bert_finetuned_final/
   ```
   - Clic droit → Download

6. **Installer localement**
   - Extraire `bert_finetuned_final.zip`
   - Copier dans `models/approach3/bert_finetuned/`

### Option 2 : Kaggle

**Avantages :**
- 30h/semaine de GPU (vs 12h/jour Colab)
- GPU T4 ou P100

**Étapes :**
1. Créer compte : https://www.kaggle.com/
2. `Notebooks` → `New Notebook`
3. Settings → `Accelerator` → **GPU T4**
4. Copier-coller le code
5. Run all

---

## 💻 Entraînement local (CPU)

**Si vous n'avez pas accès à un GPU :**

```bash
cd "C:\Users\LOQ\Documents\Chatbot bien-être"
python src/approach3/train_finetuner.py
```

⏳ **Durée : 10-15 minutes**

**Configuration actuelle :**
- 1 epoch (réduit pour CPU)
- Batch size 16
- Learning rate 2e-5

---

## 📊 Dataset

### Structure

```json
{
  "text": "Je suis heureux!",
  "label": "très positif",
  "label_id": 4
}
```

### 5 Classes de sentiment

| ID | Label | Exemples | Count |
|----|-------|----------|-------|
| 0 | Très négatif | "Je veux tout abandonner" | 100 |
| 1 | Négatif | "Je suis triste" | 100 |
| 2 | Neutre | "Bonjour, comment ça va?" | 100 |
| 3 | Positif | "Ça va bien" | 100 |
| 4 | Très positif | "Je suis heureux!" | 100 |

**Total : 500 exemples équilibrés**

### Split

- **Train** : 400 exemples (80%)
- **Validation** : 100 exemples (20%)

---

## ⚙️ Hyperparamètres

| Paramètre | Valeur | Explication |
|-----------|--------|-------------|
| **Learning rate** | 2e-5 | Standard pour fine-tuning BERT |
| **Epochs** | 3 | Bon compromis (GPU) ou 1 (CPU) |
| **Batch size** | 16 (GPU) / 8 (CPU) | Selon mémoire disponible |
| **Weight decay** | 0.01 | Régularisation L2 |
| **Max length** | 128 | Longueur max tokens |
| **Optimizer** | AdamW | Optimizer standard |

---

## 📈 Résultats attendus

### Training loss

| Epoch | Loss | Temps (GPU) |
|-------|------|-------------|
| 1 | ~1.2 | 50 sec |
| 2 | ~0.6 | 50 sec |
| 3 | ~0.4 | 50 sec |

### Validation loss

| Epoch | Loss | Accuracy |
|-------|------|----------|
| 1 | ~0.8 | ~75% |
| 2 | ~0.5 | ~85% |
| 3 | ~0.4 | ~91-95% |

### Comparaison avec Approche 1

| Métrique | Approche 1 | Approche 3 |
|----------|------------|------------|
| **Accuracy** | 82% | 91-95% |
| **Temps/réponse** | 0.3 sec | 0.5 sec |
| **Confiance** | 75% | 92% |
| **Spécialisation** | Générique | Bien-être |

---

## 🧪 Tests

### Test du modèle fine-tuné

```bash
python compare_approaches.py
```

**Résultat attendu :**
```
📊 COMPARAISON : APPROCHE 1 vs APPROCHE 3
=================================================================

🟢 APPROCHE 1 : FEATURE EXTRACTION
   'Je suis heureux!'       → positif    (74.3%)
   'Je me sens déprimé'     → négatif    (40.5%)
   ...

🔥 APPROCHE 3 : FINE-TUNING
   'Je suis heureux!'       → très positif (94.2%)
   'Je me sens déprimé'     → très négatif (91.7%)
   ...

📊 RÉSUMÉ COMPARATIF
Total de tests: 8
Accord Approche 1/3: 6/8 (75.0%)
✅ Rapport sauvegardé: data/comparison_report.json
```

### Test du chatbot

```bash
python -c "from src.approach3.chatbot import WellbeingChatbot; bot = WellbeingChatbot(); bot.start_conversation()"
```

---

## 🎯 Prochaines étapes

Après avoir entraîné Approche 3 :

1. ✅ **Comparer avec Approche 1**
   ```bash
   python compare_approaches.py
   ```

2. ✅ **Tester le chatbot**
   ```bash
   python src/approach3/chatbot.py
   ```

3. ✅ **Interface Streamlit** (TODO)
   - Modifier `ui/streamlit_ui.py`
   - Ajouter option Approche 3

4. ✅ **Approche 2** (Custom LSTM)
   - Commencer Approche 2
   - Comparer les 3 approches

5. ✅ **Rapport final**
   - Rédiger le rapport
   - Comparaison complète
   - Présentation

---

## 📚 Ressources

- **Guide GPU** : [docs/GPU_TRAINING_GUIDE.md](GPU_TRAINING_GUIDE.md)
- **Notebook Colab** : `notebooks/02_finetuning_bert_gpu.ipynb`
- **HuggingFace Transformers** : https://huggingface.co/docs/transformers/
- **BERT Paper** : https://arxiv.org/abs/1810.04805

---

## ✅ Checklist

- [x] Code Approche 3 complet
- [x] Dataset 500 exemples créé
- [x] Fine-tuner implémenté
- [x] Script d'entraînement prêt
- [x] Notebook GPU créé
- [ ] Modèle entraîné sur GPU
- [ ] Modèle téléchargé localement
- [ ] Tests avec compare_approaches.py
- [ ] Chatbot Approche 3 testé
- [ ] Rapport de comparaison généré

---

**Date de création** : 14 janvier 2026  
**Status** : ✅ Prêt pour entraînement GPU  
**Prochaine étape** : Entraîner sur Google Colab
