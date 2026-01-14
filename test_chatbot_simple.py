#!/usr/bin/env python
"""Test simple du chatbot Approche 3"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.approach3.chatbot import WellbeingChatbot

def main():
    print("\n" + "="*80)
    print("🚀 TEST CHATBOT APPROCHE 3 (Fine-tuning BERT + CBT)")
    print("="*80 + "\n")
    
    # Initialiser le chatbot
    print("⏳ Initialisation du chatbot...")
    chatbot = WellbeingChatbot('test_user')
    print("✅ Chatbot prêt!\n")
    
    # Test phrases
    test_phrases = [
        "Je suis triste",
        "Je suis complètement nul, je rate toujours tout",
        "Tout le monde pense que je suis incompétent",
        "J'aime cette journée, c'est formidable!",
    ]
    
    for i, phrase in enumerate(test_phrases, 1):
        print("="*80)
        print(f"TEST {i}: {phrase}")
        print("="*80)
        
        response = chatbot.process_message(phrase)
        
        print(f"\n📊 Analyse:")
        print(f"   Sentiment détecté: {response.get('sentiment_detail', 'N/A')}")
        print(f"   Confiance: {response.get('confidence', 'N/A'):.1%}")
        
        print(f"\n💬 Réponse du chatbot:")
        main_response = response.get('main_response', 'Pas de réponse')
        # Afficher les 300 premiers caractères
        if len(main_response) > 300:
            print(f"   {main_response[:300]}...")
        else:
            print(f"   {main_response}")
        
        # CBT info
        if response.get('cbt_enabled'):
            distortions = response.get('distortions_detected', [])
            if distortions:
                print(f"\n🧠 CBT Détecté:")
                for dist in distortions:
                    print(f"   • {dist}")
            
            if response.get('behavioral_actions'):
                print(f"\n💡 Actions proposées:")
                for action in response.get('behavioral_actions', [])[:3]:
                    print(f"   • {action}")
        
        print(f"\n{'─'*80}\n")
    
    # Statistiques
    print("📈 STATISTIQUES FINALES:")
    stats = chatbot.get_statistics()
    print(f"   Messages: {stats.get('total_messages', 0)}")
    print(f"   Humeur moyenne: {stats.get('average_mood', 0):.2f}")
    print(f"   Tendance: {stats.get('trend', 'N/A')}")
    print()

if __name__ == '__main__':
    main()
