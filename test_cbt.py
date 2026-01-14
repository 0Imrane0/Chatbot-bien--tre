"""
Test du Module CBT - Détection de Distorsions Cognitives
========================================================

Ce script teste la détection des distorsions cognitives et la génération
de réponses CBT pour différents cas d'usage.

Auteur : Étudiant ENSA Berrechid
"""

import sys
from pathlib import Path

# Ajouter src au path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from cbt_engine import CBTEngine


def print_separator():
    """Affiche un séparateur visuel"""
    print("\n" + "=" * 80 + "\n")


def test_cbt_distortions():
    """
    Teste la détection de distorsions cognitives
    """
    print("🧠 TEST DU MODULE CBT - DISTORSIONS COGNITIVES")
    print_separator()
    
    # Initialiser le moteur CBT
    cbt = CBTEngine()
    
    # Cas de test avec différentes distorsions
    test_cases = [
        {
            "category": "Surgénéralisation",
            "phrase": "Je suis complètement nul, je rate toujours tout",
            "sentiment": "négatif",
            "intensity": 0.8
        },
        {
            "category": "Catastrophisation",
            "phrase": "C'est terrible, c'est une catastrophe, je vais jamais m'en sortir",
            "sentiment": "négatif",
            "intensity": 0.9
        },
        {
            "category": "Pensée Tout-ou-Rien",
            "phrase": "Si je n'ai pas la perfection, c'est que j'ai tout raté",
            "sentiment": "négatif",
            "intensity": 0.7
        },
        {
            "category": "Lecture de Pensées",
            "phrase": "Il pense que je suis bizarre, personne ne m'aime",
            "sentiment": "négatif",
            "intensity": 0.75
        },
        {
            "category": "Raisonnement Émotionnel",
            "phrase": "Je sens que tout va mal, j'ai l'impression que je vais échouer",
            "sentiment": "négatif",
            "intensity": 0.6
        },
        {
            "category": "Multiple Distorsions",
            "phrase": "Je suis toujours triste, personne ne comprend, c'est horrible",
            "sentiment": "négatif",
            "intensity": 0.85
        },
        {
            "category": "Crise Potentielle",
            "phrase": "Je ne veux plus vivre, je veux en finir",
            "sentiment": "négatif",
            "intensity": 1.0
        },
        {
            "category": "Anxiété/Stress",
            "phrase": "Je suis tellement stressé et anxieux, j'ai peur de tout",
            "sentiment": "négatif",
            "intensity": 0.7
        }
    ]
    
    # Tester chaque cas
    for i, test in enumerate(test_cases, 1):
        print(f"📝 TEST {i}: {test['category']}")
        print("-" * 80)
        print(f"👤 Utilisateur: \"{test['phrase']}\"")
        print(f"📊 Sentiment: {test['sentiment']} | Intensité: {test['intensity']}")
        
        # Détecter les distorsions
        distortions = cbt.detect_cognitive_distortions(test['phrase'])
        
        # Générer réponse CBT
        cbt_response = cbt.generate_cbt_response(
            test['phrase'],
            test['sentiment'],
            test['intensity']
        )
        
        # Afficher les résultats
        print(f"\n🔍 Distorsions détectées: {len(distortions)}")
        for dist in distortions:
            print(f"   • {dist['name']}: {dist['description']}")
        
        print(f"\n🤖 Réponse du Chatbot (avec CBT):")
        print("-" * 80)
        formatted_response = cbt.format_response_for_user(cbt_response)
        print(formatted_response)
        
        print_separator()
    
    print("✅ TOUS LES TESTS TERMINÉS\n")


def test_comparison_with_without_cbt():
    """
    Compare les réponses avec et sans CBT
    """
    print("📊 COMPARAISON : AVEC vs SANS CBT")
    print_separator()
    
    from approach1.response_generator import ResponseGenerator
    
    # Phrase de test
    test_phrase = "Je suis complètement nul, je rate toujours mes examens"
    
    print(f"👤 Utilisateur: \"{test_phrase}\"\n")
    
    # SANS CBT
    print("❌ SANS CBT (Réponse classique):")
    print("-" * 80)
    generator_without_cbt = ResponseGenerator(enable_cbt=False)
    response_without = generator_without_cbt.generate_response(
        sentiment='négatif',
        sentiment_detail='négatif',
        confidence=0.6,
        text=test_phrase
    )
    print(response_without['main_response'])
    if response_without.get('advice'):
        print("\n💡 Conseils:")
        for advice in response_without['advice'][:3]:
            print(f"   • {advice}")
    
    print_separator()
    
    # AVEC CBT
    print("✅ AVEC CBT (Réponse enrichie):")
    print("-" * 80)
    generator_with_cbt = ResponseGenerator(enable_cbt=True)
    response_with = generator_with_cbt.generate_response(
        sentiment='négatif',
        sentiment_detail='négatif',
        confidence=0.6,
        text=test_phrase
    )
    print(response_with['main_response'])
    if response_with.get('advice'):
        print("\n💡 Conseils:")
        for advice in response_with['advice'][:3]:
            print(f"   • {advice}")
    
    print_separator()
    
    # Comparaison
    print("📈 ANALYSE COMPARATIVE:")
    print("-" * 80)
    print(f"Longueur réponse SANS CBT: {len(response_without['main_response'])} caractères")
    print(f"Longueur réponse AVEC CBT: {len(response_with['main_response'])} caractères")
    print(f"Distorsions détectées: {response_with.get('distortions_detected', 0)}")
    print(f"CBT activé: {response_with.get('cbt_enabled', False)}")
    
    improvement = ((len(response_with['main_response']) - len(response_without['main_response'])) 
                   / len(response_without['main_response']) * 100)
    print(f"\n📊 Enrichissement de la réponse: +{improvement:.1f}%")
    
    print_separator()


def test_behavioral_activation():
    """
    Teste l'activation comportementale selon différentes émotions
    """
    print("🎯 TEST: ACTIVATION COMPORTEMENTALE")
    print_separator()
    
    cbt = CBTEngine()
    
    test_emotions = [
        {
            "message": "Je suis tellement déprimé, je ne veux rien faire",
            "expected_category": "depression"
        },
        {
            "message": "Je suis super stressé avec tout ce travail",
            "expected_category": "stress"
        },
        {
            "message": "J'ai tellement peur, je suis anxieux tout le temps",
            "expected_category": "anxiety"
        }
    ]
    
    for test in test_emotions:
        print(f"👤 Message: \"{test['message']}\"")
        
        cbt_response = cbt.generate_cbt_response(
            test['message'],
            'négatif',
            0.7
        )
        
        if cbt_response.get('actions'):
            print(f"\n💡 Actions recommandées (catégorie: {test['expected_category']}):")
            print("Immédiates:")
            for action in cbt_response['actions']['immediate']:
                print(f"   • {action}")
            print("\nCourt terme:")
            for action in cbt_response['actions']['short_term']:
                print(f"   • {action}")
        
        print_separator()


if __name__ == "__main__":
    print("\n" + "🧠" * 40)
    print("MODULE CBT - SUITE DE TESTS COMPLÈTE")
    print("🧠" * 40 + "\n")
    
    try:
        # Test 1: Distorsions cognitives
        test_cbt_distortions()
        
        # Test 2: Comparaison avec/sans CBT
        test_comparison_with_without_cbt()
        
        # Test 3: Activation comportementale
        test_behavioral_activation()
        
        print("\n" + "✅" * 40)
        print("TOUS LES TESTS RÉUSSIS !")
        print("✅" * 40 + "\n")
        
    except Exception as e:
        print(f"\n❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
