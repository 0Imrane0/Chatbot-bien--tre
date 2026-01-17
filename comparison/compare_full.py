"""
COMPARAISON COMPLÈTE : Approach 1 vs Approach 3 + Approach 2
Test tous les sentiments sur le même texte
"""
import sys
sys.path.insert(0, 'src')

print("\n" + "="*80)
print("🔬 COMPARAISON EXHAUSTIVE APPROACH 1 vs APPROACH 3")
print("="*80)

test_cases = [
    ('je veux suicider', 'très négatif'),
    ('Je suis complètement nul, je vais rater mon examen et ma vie est fichue', 'très négatif'),
    ('Je suis stressé, tout le monde pense que je suis incompétent', 'négatif'),
    ('Je me sens triste', 'négatif'),
    ('Rien de spécial', 'neutre'),
    ('J\'ai réussi ma présentation, je suis fier de moi !', 'très positif'),
    ('C\'est magnifique!', 'très positif'),
]

# ======================================================================
# APPROACH 3 - ACTUELLE (KeywordAnalyzer fallback)
# ======================================================================
print("\n📊 APPROACH 3 (Approach 3 = dictionnaire fallback):")
print("-"*80)

from approach3.keyword_analyzer import KeywordSentimentAnalyzer
analyzer3 = KeywordSentimentAnalyzer()

a3_pass = 0
a3_total = 0
for text, expected in test_cases:
    result = analyzer3.analyze(text)
    is_pass = expected.lower() == result['sentiment_detail'].lower()
    a3_pass += (1 if is_pass else 0)
    a3_total += 1
    
    status = "✅" if is_pass else "❌"
    print(f"{status} {result['sentiment_detail']:15} | '{text[:50]}'")

print(f"\n   Score: {a3_pass}/{a3_total} ({a3_pass*100//a3_total}%)")

# ======================================================================
# APPROACH 1 - FEATURE EXTRACTION (si disponible)
# ======================================================================
print("\n📊 APPROACH 1 (Feature Extraction - BERT gelé):")
print("-"*80)

try:
    from approach1.sentiment_analyzer import SentimentAnalyzer as Analyzer1
    analyzer1 = Analyzer1()
    
    a1_pass = 0
    a1_total = 0
    for text, expected in test_cases:
        result = analyzer1.analyze(text)
        sentiment = result.get('sentiment_detail', 'neutre')
        is_pass = expected.lower() == sentiment.lower()
        a1_pass += (1 if is_pass else 0)
        a1_total += 1
        
        status = "✅" if is_pass else "❌"
        print(f"{status} {sentiment:15} | '{text[:50]}'")
    
    print(f"\n   Score: {a1_pass}/{a1_total} ({a1_pass*100//a1_total}%)")
    
except Exception as e:
    print(f"❌ Approach 1 non disponible: {e}")
    a1_pass = 0
    a1_total = 0

# ======================================================================
# RÉSUMÉ
# ======================================================================
print("\n" + "="*80)
print("📊 RÉSUMÉ COMPARATIF")
print("="*80)
print(f"Approach 1 (Feature Extraction): {a1_pass}/{a1_total} ({a1_pass*100//a1_total if a1_total else 0}%)")
print(f"Approach 3 (Dictionnaire):       {a3_pass}/{a3_total} ({a3_pass*100//a3_total}%)")
print("="*80)

if a1_pass > a3_pass:
    print(f"🎯 Approach 1 est meilleur (+{a1_pass - a3_pass} points)")
elif a3_pass > a1_pass:
    print(f"🎯 Approach 3 est meilleur (+{a3_pass - a1_pass} points)")
else:
    print("🎯 Les deux approches sont équivalentes")

print("="*80 + "\n")
