"""
Script pour télécharger les ressources NLTK nécessaires
"""
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

print("📥 Téléchargement des ressources NLTK...")

# Télécharger les ressources nécessaires
resources = ['punkt', 'stopwords', 'punkt_tab', 'wordnet', 'averaged_perceptron_tagger']

for resource in resources:
    try:
        nltk.download(resource, quiet=False)
        print(f"✅ {resource} téléchargé avec succès")
    except Exception as e:
        print(f"⚠️ Erreur pour {resource}: {e}")

print("\n✅ Configuration NLTK terminée!")
