"""
Script d'entraînement du fine-tuning BERT
Lance l'entraînement complet : préparation → fine-tuning → sauvegarde
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer nos modules
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.approach3.data_preparation import (
    load_dataset,
    split_train_val,
    validate_dataset
)
from src.approach3.sentiment_finetuner import BERTFineTuner


def main():
    """Lance le processus complet d'entraînement"""
    
    print("\n" + "=" * 70)
    print("🔥 FINE-TUNING BERT POUR L'ANALYSE DE SENTIMENT BIEN-ÊTRE")
    print("=" * 70)
    
    # ============================================================================
    # ÉTAPE 1 : Charger le dataset
    # ============================================================================
    
    print("\n📥 ÉTAPE 1 : Chargement du dataset...")
    try:
        dataset = load_dataset('data/training_wellbeing_data.json')
    except FileNotFoundError:
        print("❌ Dataset non trouvé! Créer le dataset d'abord:")
        print("   python src/approach3/data_preparation.py")
        return
    
    # ============================================================================
    # ÉTAPE 2 : Valider le dataset
    # ============================================================================
    
    print("\n✅ ÉTAPE 2 : Validation du dataset...")
    validate_dataset(dataset)
    
    # ============================================================================
    # ÉTAPE 3 : Split train/validation
    # ============================================================================
    
    print("\n📊 ÉTAPE 3 : Split train/validation...")
    train_dataset, val_dataset = split_train_val(dataset, train_ratio=0.8)
    
    # Extraire textes et labels
    train_texts = [d['text'] for d in train_dataset]
    train_labels = [d['label_id'] for d in train_dataset]
    
    val_texts = [d['text'] for d in val_dataset]
    val_labels = [d['label_id'] for d in val_dataset]
    
    # ============================================================================
    # ÉTAPE 4 : Créer le fine-tuner
    # ============================================================================
    
    print("\n🤖 ÉTAPE 4 : Initialisation du fine-tuner...")
    finetuner = BERTFineTuner(
        model_name='bert-base-multilingual-uncased',
        output_dir='models/approach3/bert_finetuned'
    )
    
    # ============================================================================
    # ÉTAPE 5 : Fine-tuner BERT
    # ============================================================================
    
    print("\n🔥 ÉTAPE 5 : Fine-tuning BERT...")
    print("   ⏱️  Durée estimée: 5-10 minutes (CPU) ou 1-2 minutes (GPU)")
    
    trainer = finetuner.train(
        train_texts=train_texts,
        train_labels=train_labels,
        val_texts=val_texts,
        val_labels=val_labels,
        epochs=1,              # Réduit à 1 epoch pour viter les problèmes CPU
        batch_size=16,         # Augmenter batch size pour plus d'efficacité
        learning_rate=2e-5     # 2e-5 = standard pour fine-tuning BERT
    )
    
    # ============================================================================
    # ÉTAPE 6 : Tester le modèle fine-tuné
    # ============================================================================
    
    print("\n🧪 ÉTAPE 6 : Test du modèle fine-tuné...")
    print("=" * 70)
    
    test_phrases = [
        "Je suis heureux!",
        "Je me sens déprimé",
        "Comment ça va?",
        "Je ne veux plus continuer",
        "C'est magnifique!",
        "Je suis très stressé",
        "Tout va bien",
        "Je suis désespéré",
    ]
    
    print("\n📊 Prédictions:")
    print("-" * 70)
    
    for phrase in test_phrases:
        result = finetuner.predict(phrase)
        sentiment = result['sentiment']
        confidence = result['confidence']
        
        # Format couleur (emoji)
        emoji_map = {
            'très négatif': '🔴',
            'négatif': '🟠',
            'neutre': '🟡',
            'positif': '🟢',
            'très positif': '🟢🟢'
        }
        emoji = emoji_map.get(sentiment, '⚪')
        
        print(f"{emoji} '{phrase}'")
        print(f"   → {sentiment:15s} ({confidence:.1%})")
    
    # ============================================================================
    # ÉTAPE 7 : Résumé et prochaines étapes
    # ============================================================================
    
    print("\n" + "=" * 70)
    print("✅ FINE-TUNING COMPLÉTÉ!")
    print("=" * 70)
    print(f"\n📁 Modèle sauvegardé : models/approach3/bert_finetuned/")
    print("\n🎯 Prochaines étapes:")
    print("   1. Comparer Approche 1 vs Approche 3")
    print("   2. Intégrer le modèle fine-tuné dans le chatbot")
    print("   3. Lancer Approche 2 (Custom LSTM)")


if __name__ == '__main__':
    main()
