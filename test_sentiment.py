"""
Testeur d'Analyseur de Sentiment - Approche 1
Fichier pour tester l'analyseur avec tes propres phrases sans modifier le code principal

À utiliser comme :
    python test_sentiment.py
"""

from src.approach1.sentiment_analyzer import SentimentAnalyzer


def test_custom_phrases():
    """
    Teste l'analyseur avec des phrases personnalisées
    MODIFIE CETTE FONCTION POUR AJOUTER TES PROPRES PHRASES !
    """
    print("=" * 70)
    print("🧪 TESTEUR DE SENTIMENT - ANALYSE PERSONNALISÉE")
    print("=" * 70)
    print()
    
    # Initialiser l'analyseur
    analyzer = SentimentAnalyzer()
    
    # ============================================
    # 📝 AJOUTE TES PHRASES ICI !
    # ============================================
    # Tu peux facilement ajouter/modifier les phrases ci-dessous
    # sans toucher au reste du code
    
    custom_phrases = [
        # Tes résultats précédents
        {
            'text': 'La vie est belle',
            'expected_sentiment': 'positif'
        },
        {
            'text': 'Je suis malade et fatigué',
            'expected_sentiment': 'négatif'
        },
        {
            'text': "C'est mieux que jamais",
            'expected_sentiment': 'positif'
        },
        
        # Ajoute tes nouvelles phrases ici :
        # {
        #     'text': 'Ta phrase ici',
        #     'expected_sentiment': 'positif' ou 'négatif' ou 'neutre'
        # },
    ]
    
    # ============================================
    # Analyser chaque phrase
    # ============================================
    
    for i, item in enumerate(custom_phrases, 1):
        text = item['text']
        expected = item['expected_sentiment']
        
        print(f"\n🔍 Test {i} : \"{text}\"")
        print("-" * 70)
        
        # Analyser
        result = analyzer.analyze(text)
        
        # Afficher les résultats
        sentiment = result['sentiment']
        confidence = result['confidence_percent']
        detail = result['sentiment_detail']
        
        # Vérifier si c'est correct
        is_correct = sentiment == expected
        check_mark = "✅" if is_correct else "❌"
        
        print(f"   {check_mark} Sentiment détecté : {sentiment.upper()} ({detail})")
        print(f"   💪 Confiance : {confidence}%")
        print(f"   🎯 Attendu : {expected.upper()}")
        
        if not is_correct:
            print(f"   ⚠️  DIFFÉRENT ! Attendu {expected} mais obtenu {sentiment}")
        
        # Afficher l'interprétation
        interpretation = analyzer.get_emotion_interpretation(result)
        print(f"   💬 Interprétation : {interpretation}")
        
        # Afficher la fiabilité
        is_confident = analyzer.is_confident(result)
        fiability = "🟢 Très fiable" if is_confident else "🟡 À confirmer"
        print(f"   {fiability}")
        
        # Afficher les probabilités détaillées (optionnel)
        show_details = True
        if show_details:
            print(f"\n   📊 Détail des probabilités :")
            for label, score in sorted(result['all_scores'].items(), 
                                      key=lambda x: x[1], 
                                      reverse=True):
                bar_length = int(score * 35)
                bar = "█" * bar_length
                print(f"      {label:15} : {bar} {score*100:.1f}%")
    
    print("\n" + "=" * 70)
    print("✅ Tests personnalisés terminés !")
    print("=" * 70)


def test_with_softmax_explanation():
    """
    Teste l'analyseur et explique ce que Softmax fait
    """
    print("\n" + "=" * 70)
    print("🧠 DÉMONSTRATION SOFTMAX")
    print("=" * 70)
    print()
    
    analyzer = SentimentAnalyzer()
    
    # Une phrase pour voir softmax en action
    test_phrase = "Je suis vraiment heureux !"
    
    print(f"Phrase : \"{test_phrase}\"\n")
    
    result = analyzer.analyze(test_phrase)
    
    print("Ce qui se passe derrière les coulisses :\n")
    print("1️⃣  BERT donne des scores bruts (logits) :")
    print("   - Très négatif : -8.5")
    print("   - Négatif      : -6.2")
    print("   - Neutre       : -1.3")
    print("   - Positif      : 3.7")
    print("   - Très positif : 5.2  ← Le plus haut !\n")
    
    print("2️⃣  SOFTMAX convertit ces scores en probabilités :")
    print("   (e^score / Σ(e^tous_scores))\n")
    
    for label, score in result['all_scores'].items():
        bar_length = int(score * 40)
        bar = "▓" * bar_length
        print(f"   {label:15} : {bar} {score*100:5.1f}%")
    
    print(f"\n3️⃣  Résultat : {result['sentiment'].upper()} ({result['sentiment_detail']})")
    print(f"   Confiance : {result['confidence_percent']}%")
    print(f"\n✨ Softmax a transformé des nombres étranges en probabilités claires !")


def test_bidirectional_example():
    """
    Montre comment la bidirectionnalité aide BERT à comprendre
    """
    print("\n" + "=" * 70)
    print("🔄 DÉMONSTRATION BIDIRECTIONNALITÉ")
    print("=" * 70)
    print()
    
    analyzer = SentimentAnalyzer()
    
    # Phrases similaires mais avec sens opposés
    phrases = [
        ("Je suis heureux", "positif"),
        ("Je ne suis pas heureux", "négatif"),
        ("Je suis triste", "négatif"),
        ("Je ne suis pas triste", "positif"),
        ("C'est bon", "positif"),
        ("Ce n'est pas bon", "négatif"),
    ]
    
    print("Observe comment BERT comprend les négatifs :\n")
    
    for text, expected in phrases:
        result = analyzer.analyze(text)
        sentiment = result['sentiment']
        confidence = result['confidence_percent']
        
        match = "✅" if sentiment == expected else "❌"
        
        print(f"{match} \"{text}\"")
        print(f"   → {sentiment.upper()} ({confidence}%)")
        print(f"   → Attendu : {expected.upper()}\n")
    
    print("Remarque : BERT lit de gauche à droite ET de droite à gauche,")
    print("ce qui lui permet de comprendre que 'pas' change le sens !")


def test_emoji_handling():
    """
    Teste comment BERT traite les emojis
    """
    print("\n" + "=" * 70)
    print("😊 DÉMONSTRATION - TRAITEMENT DES EMOJIS")
    print("=" * 70)
    print()
    
    analyzer = SentimentAnalyzer()
    
    emoji_phrases = [
        "Je suis heureux 😊",
        "Je suis heureux",
        "C'est terrible 😔",
        "C'est terrible",
        "J'adore ! 🎉",
        "J'adore !",
    ]
    
    print("Comparons les mêmes phrases avec et sans emojis :\n")
    
    for i in range(0, len(emoji_phrases), 2):
        text_with_emoji = emoji_phrases[i]
        text_without_emoji = emoji_phrases[i+1]
        
        result_with = analyzer.analyze(text_with_emoji)
        result_without = analyzer.analyze(text_without_emoji)
        
        print(f"📝 SANS emoji : \"{text_without_emoji}\"")
        print(f"   → {result_without['sentiment'].upper()} ({result_without['confidence_percent']}%)\n")
        
        print(f"😊 AVEC emoji : \"{text_with_emoji}\"")
        print(f"   → {result_with['sentiment'].upper()} ({result_with['confidence_percent']}%)\n")
        
        # Comparer
        if result_with['sentiment'] == result_without['sentiment']:
            print("   ✅ Même résultat : BERT comprend le sentiment du texte\n")
        else:
            print("   ⚠️  Résultat DIFFÉRENT : L'emoji influence le résultat\n")
    
    print("Conclusion : BERT tokenize les emojis comme du texte ordinaire.")
    print("L'emoji aide mais n'est pas crucial pour le sentiment.\n")


# ============================================
# POINT D'ENTRÉE
# ============================================

if __name__ == "__main__":
    # Choisis quelle démo exécuter :
    
    # 1. Tests personnalisés
    test_custom_phrases()
    
    # 2. Explication de Softmax
    test_with_softmax_explanation()
    
    # 3. Explication de la bidirectionnalité
    test_bidirectional_example()
    
    # 4. Traitement des emojis
    test_emoji_handling()
