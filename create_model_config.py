#!/usr/bin/env python3
"""
Script simple pour créer les fichiers de modèle BERT nécessaires
sans télécharger depuis Hugging Face (si la connexion est lente)
"""

import json
from pathlib import Path

model_dir = Path("models/approach3/bert_finetuned")
model_dir.mkdir(parents=True, exist_ok=True)

# Créer un config.json minimaliste basé sur BERT
config = {
    "architectures": ["BertForSequenceClassification"],
    "attention_probs_dropout_prob": 0.1,
    "gradient_checkpointing": False,
    "hidden_act": "gelu",
    "hidden_dropout_prob": 0.1,
    "hidden_size": 768,
    "id2label": {
        "0": "TRÈS_NÉGATIF",
        "1": "NÉGATIF", 
        "2": "NEUTRE",
        "3": "POSITIF",
        "4": "TRÈS_POSITIF"
    },
    "initializer_range": 0.02,
    "intermediate_size": 3072,
    "label2id": {
        "TRÈS_NÉGATIF": 0,
        "NÉGATIF": 1,
        "NEUTRE": 2,
        "POSITIF": 3,
        "TRÈS_POSITIF": 4
    },
    "layer_norm_eps": 1e-12,
    "max_position_embeddings": 512,
    "model_type": "bert",
    "num_attention_heads": 12,
    "num_hidden_layers": 12,
    "num_labels": 5,
    "output_hidden_states": False,
    "output_past": False,
    "pad_token_id": 0,
    "position_embedding_type": "absolute",
    "problem_type": "single_label_classification",
    "pruned_heads": {},
    "torch_dtype": "float32",
    "transformers_version": "4.35.0",
    "type_vocab_size": 2,
    "use_cache": True,
    "vocab_size": 30522
}

if not (model_dir / "config.json").exists():
    with open(model_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)
    print(f"✅ Created config.json")
else:
    print(f"✅ config.json exists")

print("\n⚠️  NOTE: Model files (pytorch_model.bin) still need to be downloaded.")
print("This is a limitation of the network connection.")
print("\nTo download the model, run:")
print("  python download_models.py")
print("\nOr manually from Hugging Face:")
print("  https://huggingface.co/bert-base-uncased")
