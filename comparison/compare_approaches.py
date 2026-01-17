"""
📊 Comparaison : Approche 1 vs Approche 3
==========================================

Ce script compare les deux approches :
1. Approche 1 : Feature Extraction (BERT gelé)
2. Approche 3 : Fine-tuning BERT

Auteur : Étudiant ENSA Berrechid
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.approach1.sentiment_analyzer import SentimentAnalyzer as Analyzer1
from typing import List, Dict
import json
import time
import pandas as pd


def compare_approaches():
    """
    Compare Approche 1 vs Approche 3
    """
    print("\n" + "=" * 70)
    print("📊 COMPARAISON : APPROCHE 1 vs APPROCHE 3")
    print("=" * 70)
    print()
    
    # Phrases de test
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
    
    # ========================================
    # APPROCHE 1 : FEATURE EXTRACTION
    # ========================================
    
    print("🟢 APPROCHE 1 : FEATURE EXTRACTION (BERT gelé)")
    print("-" * 70)
    print("   Utilisation de BERT pré-entraîné sans modification")
    print()
    
    analyzer1 = Analyzer1()
    approach1_times = []
    approach1_results = []
    
    for phrase in test_phrases:
        start = time.time()
        result = analyzer1.analyze(phrase)
        elapsed = time.time() - start
        approach1_times.append(elapsed)
        approach1_results.append(result)
        
        print(f"   '{phrase}'")
        print(f"   → {result['sentiment']:10s} ({result['confidence']:.1%}) [{elapsed:.3f}s]")
    
    print()
    print(f"⏱️  Temps moyen: {sum(approach1_times)/len(approach1_times):.4f}s")
    print()
    
    # ========================================
    # APPROCHE 3 : FINE-TUNING
    # ========================================
    
    print()
    print("🔥 APPROCHE 3 : FINE-TUNING BERT")
    print("-" * 70)
    
    try:
        from src.approach3.sentiment_analyzer import SentimentAnalyzer as Analyzer3
        
        print("   Utilisation de BERT fine-tuné sur données bien-être")
        print()
        
        analyzer3 = Analyzer3()
        approach3_times = []
        approach3_results = []
        
        for phrase in test_phrases:
            start = time.time()
            result = analyzer3.analyze(phrase)
            elapsed = time.time() - start
            approach3_times.append(elapsed)
            approach3_results.append(result)
            
            print(f"   '{phrase}'")
            print(f"   → {result['sentiment']:10s} ({result['confidence']:.1%}) [{elapsed:.3f}s]")
        
        print()
        print(f"⏱️  Temps moyen: {sum(approach3_times)/len(approach3_times):.4f}s")
        
        # ========================================
        # COMPARAISON STATISTIQUE
        # ========================================
        
        print("\n" + "=" * 70)
        print("📊 RÉSUMÉ COMPARATIF")
        print("=" * 70)
        print()
        
        agreement = sum(
            1 for r1, r3 in zip(approach1_results, approach3_results)
            if r1['sentiment'] == r3['sentiment']
        )
        
        print(f"Total de tests: {len(test_phrases)}")
        print(f"Accord Approche 1/3: {agreement}/{len(test_phrases)} ({agreement/len(test_phrases)*100:.1f}%)")
        print()
        
        # Sauvegarder le rapport
        report = {
            'total_tests': len(test_phrases),
            'agreement': agreement,
            'agreement_rate': agreement / len(test_phrases),
            'results': [
                {
                    'phrase': phrase,
                    'approach1': {'sentiment': r1['sentiment'], 'confidence': r1['confidence']},
                    'approach3': {'sentiment': r3['sentiment'], 'confidence': r3['confidence']},
                    'agreement': r1['sentiment'] == r3['sentiment']
                }
                for phrase, r1, r3 in zip(test_phrases, approach1_results, approach3_results)
            ]
        }
        
        with open('data/comparison_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print("✅ Rapport sauvegardé: data/comparison_report.json")
        
        # Retourner tous les résultats nécessaires
        feature_results = approach1_results
        finetuned_results = approach3_results
        feature_time = sum(approach1_times)
        finetuned_time = sum(approach3_times)
        
        return test_phrases, feature_results, finetuned_results, feature_time, finetuned_time
        
    except FileNotFoundError as e:
        print(f"❌ Approche 3 non disponible")
        print(f"   {e}")
        print()
        print("   Pour faire le fine-tuning:")
        print("   python src/approach3/train_finetuner.py")
        return None


if __name__ == '__main__':
    results = compare_approaches()
    
    if results is None:
        sys.exit(1)
    
    test_phrases, feature_results, finetuned_results, feature_time, finetuned_time = results
    
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
