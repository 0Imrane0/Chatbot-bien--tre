"""
📊 Comparaison : Feature Extraction vs Fine-tuning
===================================================

Ce script compare les deux approches :
1. Feature Extraction : Utilisation de BERT pré-entraîné tel quel
2. Fine-tuning : BERT ajusté sur nos données

Auteur : Étudiant ENSA Berrechid
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.approach1.sentiment_analyzer import SentimentAnalyzer
from src.approach1.sentiment_finetuner import BERTFineTuner, create_sample_dataset
import time
import pandas as pd


def compare_approaches():
    """
    Compare Feature Extraction vs Fine-tuning.
    """
    print("\n" + "=" * 70)
    print("📊 COMPARAISON : FEATURE EXTRACTION VS FINE-TUNING")
    print("=" * 70)
    print()
    
    # Phrases de test
    test_phrases = [
        "Je me sens incroyablement bien aujourd'hui !",
        "La méditation m'aide énormément",
        "J'ai du mal à dormir",
        "Je me sens complètement désespéré",
        "Il fait beau dehors",
        "Mon anxiété revient souvent",
        "Je suis fier d'avoir surmonté mes peurs",
        "Je me sens fatigué et démotivé"
    ]
    
    # ========================================
    # APPROCHE 1 : FEATURE EXTRACTION
    # ========================================
    
    print("⚡ APPROCHE 1 : FEATURE EXTRACTION")
    print("-" * 70)
    print("   Utilisation de BERT pré-entraîné tel quel (pas de fine-tuning)")
    print()
    
    # Charger l'analyseur actuel
    feature_analyzer = SentimentAnalyzer()
    
    # Tester et mesurer le temps
    start_time = time.time()
    feature_results = []
    
    for phrase in test_phrases:
        result = feature_analyzer.analyze(phrase)
        feature_results.append({
            'text': phrase,
            'sentiment': result['sentiment'],
            'confidence': result['confidence']
        })
    
    feature_time = time.time() - start_time
    
    print("✅ Feature Extraction terminée")
    print(f"⏱️  Temps total : {feature_time:.3f}s")
    print(f"⏱️  Temps moyen par phrase : {feature_time/len(test_phrases):.3f}s")
    print()
    
    # ========================================
    # APPROCHE 2 : FINE-TUNING
    # ========================================
    
    print("\n🎯 APPROCHE 2 : FINE-TUNING")
    print("-" * 70)
    print("   BERT ajusté sur données de bien-être mental")
    print()
    
    # Vérifier si un modèle fine-tuné existe
    finetuned_path = './models/finetuned_wellbeing'
    
    if not os.path.exists(finetuned_path):
        print("⚠️  Modèle fine-tuné non trouvé. Création en cours...")
        print()
        
        # Créer et entraîner
        texts, labels = create_sample_dataset()
        finetuner = BERTFineTuner(output_dir=finetuned_path)
        train_dataset, val_dataset = finetuner.prepare_data(texts, labels)
        finetuner.train(train_dataset, val_dataset, epochs=2, batch_size=4)
    else:
        print("📥 Chargement du modèle fine-tuné existant...")
        finetuner = BERTFineTuner(output_dir=finetuned_path)
        finetuner.load_finetuned_model(finetuned_path)
    
    # Tester et mesurer le temps
    start_time = time.time()
    finetuned_results = []
    
    for phrase in test_phrases:
        result = finetuner.predict(phrase)
        finetuned_results.append({
            'text': phrase,
            'sentiment': result['sentiment'],
            'confidence': result['confidence']
        })
    
    finetuned_time = time.time() - start_time
    
    print()
    print("✅ Fine-tuning terminé")
    print(f"⏱️  Temps total : {finetuned_time:.3f}s")
    print(f"⏱️  Temps moyen par phrase : {finetuned_time/len(test_phrases):.3f}s")
    print()
    
    # ========================================
    # COMPARAISON DES RÉSULTATS
    # ========================================
    
    print("\n" + "=" * 70)
    print("📊 COMPARAISON DES RÉSULTATS")
    print("=" * 70)
    print()
    
    # Créer un DataFrame pour la comparaison
    comparison_data = []
    
    for i, phrase in enumerate(test_phrases):
        comparison_data.append({
            'Phrase': phrase[:40] + "..." if len(phrase) > 40 else phrase,
            'Feature Ext.': feature_results[i]['sentiment'],
            'Conf. FE': f"{feature_results[i]['confidence']:.1%}",
            'Fine-tuning': finetuned_results[i]['sentiment'],
            'Conf. FT': f"{finetuned_results[i]['confidence']:.1%}",
            'Identique': '✅' if feature_results[i]['sentiment'] == finetuned_results[i]['sentiment'] else '❌'
        })
    
    df = pd.DataFrame(comparison_data)
    
    print(df.to_string(index=False))
    print()
    
    # ========================================
    # STATISTIQUES GLOBALES
    # ========================================
    
    print("\n" + "=" * 70)
    print("📈 STATISTIQUES GLOBALES")
    print("=" * 70)
    print()
    
    # Calculer les statistiques
    same_predictions = sum(1 for i in range(len(test_phrases)) 
                          if feature_results[i]['sentiment'] == finetuned_results[i]['sentiment'])
    
    agreement_rate = same_predictions / len(test_phrases)
    
    avg_conf_feature = sum(r['confidence'] for r in feature_results) / len(feature_results)
    avg_conf_finetuned = sum(r['confidence'] for r in finetuned_results) / len(finetuned_results)
    
    print(f"📊 Taux d'accord : {agreement_rate:.1%}")
    print(f"   ({same_predictions}/{len(test_phrases)} prédictions identiques)")
    print()
    
    print(f"🎯 Confiance moyenne :")
    print(f"   • Feature Extraction : {avg_conf_feature:.1%}")
    print(f"   • Fine-tuning : {avg_conf_finetuned:.1%}")
    print()
    
    print(f"⏱️  Vitesse d'inférence :")
    print(f"   • Feature Extraction : {feature_time/len(test_phrases):.3f}s/phrase")
    print(f"   • Fine-tuning : {finetuned_time/len(test_phrases):.3f}s/phrase")
    print()
    
    # ========================================
    # RECOMMANDATIONS
    # ========================================
    
    print("\n" + "=" * 70)
    print("💡 RECOMMANDATIONS")
    print("=" * 70)
    print()
    
    print("⚡ Feature Extraction - À utiliser si :")
    print("   ✅ Tu veux des résultats immédiats")
    print("   ✅ Tu n'as pas de données d'entraînement")
    print("   ✅ Tu n'as pas de GPU")
    print("   ✅ Performance \"bonne\" suffit (80-85%)")
    print()
    
    print("🎯 Fine-tuning - À utiliser si :")
    print("   ✅ Tu veux la meilleure précision possible")
    print("   ✅ Tu as des données spécifiques")
    print("   ✅ Tu as accès à un GPU")
    print("   ✅ Tu peux investir 1-3h d'entraînement")
    print()
    
    print("🏆 VERDICT :")
    if avg_conf_finetuned > avg_conf_feature:
        diff = (avg_conf_finetuned - avg_conf_feature) * 100
        print(f"   Fine-tuning est {diff:.1f}% plus confiant en moyenne !")
        print("   → Recommandé pour la production")
    else:
        print("   Feature Extraction est suffisant pour ce cas d'usage")
        print("   → Recommandé pour le prototypage")
    print()
    
    print("=" * 70)
    print("✅ COMPARAISON TERMINÉE")
    print("=" * 70)
    print()


if __name__ == "__main__":
    compare_approaches()
