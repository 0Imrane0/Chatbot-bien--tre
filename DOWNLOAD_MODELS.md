# 📥 Téléchargement des Modèles

## ⚠️ Pourquoi ce fichier ?

Le modèle BERT fine-tuné est **très volumineux** (638 MB), ce qui dépasse la limite de GitHub (100 MB).

Pour cette raison, les modèles **ne sont pas stockés** dans le dépôt Git mais téléchargés automatiquement lors du premier lancement.

---

## 🚀 Installation Automatique

### Option 1 : Double-clic (Windows) ⭐ RECOMMANDÉ

1. **Double-clique** sur `download_models.bat`
2. Le script télécharge automatiquement les modèles depuis Hugging Face
3. Une fois terminé, tu peux lancer `launch_interface.bat`

### Option 2 : Ligne de commande

```bash
# Activer l'environnement virtuel
.venv\Scripts\activate  # Windows
# ou
source .venv/bin/activate  # Mac/Linux

# Télécharger les modèles
python download_models.py
```

---

## ⏱️ Temps d'Attente

| Étape | Temps |
|-------|-------|
| **Téléchargement** | 10-15 minutes (dépend de ta connexion) |
| **Extraction** | 2-3 minutes |
| **Total** | 12-18 minutes la première fois |

> ☕ Prendre un café pendant ce temps !

---

## ✅ Vérification

Une fois le téléchargement terminé, tu devrais avoir :

```
models/
└── approach3/
    └── bert_finetuned/
        ├── config.json
        ├── pytorch_model.bin (ou model.safetensors)
        ├── tokenizer.json
        ├── tokenizer_config.json
        ├── vocab.txt
        └── special_tokens_map.json
```

---

## ❌ Problèmes Courants

### "Connection timeout"

```bash
# Augmente le timeout
pip install --default-timeout=1000 transformers
python download_models.py
```

### "Out of memory"

Le modèle nécessite **4-8 GB de RAM**. Si tu n'as pas assez :
- Ferme d'autres applications
- Redémarre ton ordinateur

### "Permission denied"

```bash
# Ré-exécute comme administrateur
```

---

## 📊 Espace Disque Requis

| Élement | Taille |
|---------|--------|
| **Modèle BERT** | 420 MB |
| **Tokenizer** | 231 MB |
| **Dependencies (pip)** | ~2 GB |
| **Total** | ~2.5-3 GB |

---

## 🎉 C'est Prêt !

Une fois les modèles téléchargés, tu peux :

```bash
launch_interface.bat
```

Et commencer à chatter ! 💬

---

*Créé avec ❤️ - Janvier 2026*
