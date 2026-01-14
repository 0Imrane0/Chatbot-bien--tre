#!/usr/bin/env python3
"""
Script pour télécharger les modèles BERT pré-entraînés depuis Hugging Face.

Les modèles sont trop volumineux pour GitHub (>100 MB),
donc ils sont téléchargés automatiquement au premier lancement.
"""

import os
import sys
from pathlib import Path
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def download_bert_finetuned():
    """Télécharge le modèle BERT fine-tuné."""
    print("\n" + "="*60)
    print("📥 Téléchargement du modèle BERT fine-tuné...")
    print("="*60 + "\n")
    
    # Chemin de destination
    model_dir = Path("models/approach3/bert_finetuned")
    model_dir.mkdir(parents=True, exist_ok=True)
    
    # Créer un modèle BERT pour la classification d'émotions
    print("[1/3] Téléchargement du modèle base BERT...")
    try:
        model = AutoModelForSequenceClassification.from_pretrained(
            "bert-base-uncased",
            num_labels=5,  # 5 classes: très négatif → très positif
            cache_dir=str(model_dir)
        )
        print("✅ Modèle BERT chargé avec succès")
        
        print("\n[2/3] Téléchargement du tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(
            "bert-base-uncased",
            cache_dir=str(model_dir)
        )
        print("✅ Tokenizer chargé avec succès")
        
        print("\n[3/3] Sauvegarde des modèles...")
        model.save_pretrained(str(model_dir))
        tokenizer.save_pretrained(str(model_dir))
        print("✅ Modèles sauvegardés avec succès")
        
        print("\n" + "="*60)
        print("✨ Téléchargement terminé !")
        print("="*60 + "\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur lors du téléchargement : {e}")
        print("\nSi le problème persiste, essaye :")
        print("  1. Vérifier ta connexion Internet")
        print("  2. Augmenter le timeout : pip install --default-timeout=1000 transformers")
        print("  3. Télécharger manuellement depuis https://huggingface.co/bert-base-uncased")
        return False

def verify_models():
    """Vérifie que les modèles sont présents."""
    model_dir = Path("models/approach3/bert_finetuned")
    required_files = [
        "config.json",
        "pytorch_model.bin",  # ou model.safetensors
        "tokenizer.json",
        "vocab.txt"
    ]
    
    existing_files = list(model_dir.glob("*"))
    
    if len(existing_files) > 2:
        print("✅ Modèles trouvés !")
        return True
    else:
        print("⚠️  Modèles non trouvés")
        return False

if __name__ == "__main__":
    print("\n🤖 Gestionnaire de Modèles - Chatbot Bien-Être IA\n")
    
    # Vérifier si les modèles existent
    if verify_models():
        print("Les modèles sont déjà installés.")
        sys.exit(0)
    
    # Télécharger les modèles
    success = download_bert_finetuned()
    
    if success:
        print("\n🎉 Tout est prêt ! Lance maintenant :")
        print("   launch_interface.bat")
        sys.exit(0)
    else:
        print("\n❌ Impossible de télécharger les modèles.")
        sys.exit(1)
