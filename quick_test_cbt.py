"""
Test Rapide du Chatbot avec CBT
================================

Compare les réponses du chatbot avec et sans CBT sur des phrases types.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src' / 'approach1'))

from sentiment_analyzer import SentimentAnalyzer
from response_generator import ResponseGenerator


def test_chatbot_responses():
    """
    Teste le chatbot avec des phrases contenant des distorsions
    """
    print("\n" + "="*80)
    print("🤖 TEST CHATBOT AVEC CBT")
    print("="*80 + "\n")
    
    # Initialiser analyseur
    analyzer = SentimentAnalyzer()
    
    # Générateur SANS CBT
    generator_no_cbt = ResponseGenerator(enable_cbt=False)
    
    # Générateur AVEC CBT
    generator_cbt = ResponseGenerator(enable_cbt=True)
    
    # Phrases de test
    test_phrases = [
        "Je suis complètement nul, je rate toujours tout",
        "Personne ne m'aime, tout le monde me déteste",
        "C'est une catastrophe, je vais jamais m'en sortir"
    ]
    
    for phrase in test_phrases:
        print(f"\n👤 Utilisateur: \"{phrase}\"")
        print("-" * 80)
        
        # Analyser sentiment
        result = analyzer.analyze(phrase)
        sentiment = result['sentiment']
        confidence = result['confidence']
        
        print(f"📊 Sentiment: {sentiment} ({confidence:.1%})\n")
        
        # SANS CBT
        print("❌ RÉPONSE SANS CBT:")
        response_no_cbt = generator_no_cbt.generate_response(
            sentiment=sentiment,
            sentiment_detail=sentiment,
            confidence=confidence,
            text=phrase
        )
        print(f"🤖 {response_no_cbt['main_response']}")
        
        print()
        
        # AVEC CBT
        print("✅ RÉPONSE AVEC CBT:")
        response_cbt = generator_cbt.generate_response(
            sentiment=sentiment,
            sentiment_detail=sentiment,
            confidence=confidence,
            text=phrase
        )
        print(f"🤖 {response_cbt['main_response']}")
        
        # Statistiques
        print(f"\n📈 Stats:")
        print(f"   Distorsions détectées: {response_cbt.get('distortions_detected', 0)}")
        print(f"   Longueur SANS CBT: {len(response_no_cbt['main_response'])} car.")
        print(f"   Longueur AVEC CBT: {len(response_cbt['main_response'])} car.")
        improvement = ((len(response_cbt['main_response']) - len(response_no_cbt['main_response'])) 
                       / len(response_no_cbt['main_response']) * 100)
        print(f"   📊 Enrichissement: +{improvement:.0f}%")
        
        print("\n" + "="*80)


if __name__ == "__main__":
    test_chatbot_responses()
    print("\n✅ Test terminé!\n")
