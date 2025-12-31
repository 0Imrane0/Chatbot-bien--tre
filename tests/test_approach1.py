"""
🧪 Tests Unitaires - Approche 1 (BERT)
======================================

Tests pour valider tous les composants du chatbot de bien-être.

Auteur : Étudiant ENSA Berrechid
Module : Programmation Python et IA
"""

import unittest
import sys
import os
import tempfile
from datetime import datetime

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'approach1'))

from src.approach1.sentiment_analyzer import SentimentAnalyzer
from src.approach1.mood_tracker import MoodTracker
from src.approach1.response_generator import ResponseGenerator
from src.approach1.mood_visualizer import MoodVisualizer


# ============================================================
# TESTS DE L'ANALYSEUR DE SENTIMENT
# ============================================================

class TestSentimentAnalyzer(unittest.TestCase):
    """Tests pour la classe SentimentAnalyzer."""
    
    @classmethod
    def setUpClass(cls):
        """Initialise l'analyseur une seule fois pour tous les tests."""
        print("\n🔄 Chargement du modèle BERT pour les tests...")
        cls.analyzer = SentimentAnalyzer()
        print("✅ Modèle chargé !")
    
    def test_analyze_positive_sentiment(self):
        """Test 1 : Sentiment positif."""
        result = self.analyzer.analyze("Je suis vraiment heureux aujourd'hui !")
        
        self.assertIn('sentiment', result)
        self.assertIn('confidence', result)
        self.assertIn(result['sentiment'].lower(), ['positif', 'très positif'])
        self.assertGreater(result['confidence'], 0.5)
    
    def test_analyze_negative_sentiment(self):
        """Test 2 : Sentiment négatif."""
        result = self.analyzer.analyze("Je me sens triste et déprimé.")
        
        self.assertIn('sentiment', result)
        self.assertIsNotNone(result['sentiment'])
    
    def test_analyze_neutral_sentiment(self):
        """Test 3 : Sentiment neutre."""
        result = self.analyzer.analyze("Il est 15 heures.")
        
        self.assertIn('sentiment', result)
        self.assertIsNotNone(result['sentiment'])
    
    def test_analyze_empty_text(self):
        """Test 4 : Texte vide."""
        result = self.analyzer.analyze("")
        
        self.assertIn('sentiment', result)
        self.assertIn('confidence', result)
    
    def test_analyze_text_with_emojis(self):
        """Test 5 : Texte avec emojis."""
        result = self.analyzer.analyze("Super journée ! 😊🎉💖")
        
        self.assertIn('sentiment', result)
    
    def test_result_structure(self):
        """Test : Structure du résultat."""
        result = self.analyzer.analyze("Test de structure")
        
        expected_keys = ['sentiment', 'confidence', 'all_scores', 'predicted_class']
        for key in expected_keys:
            self.assertIn(key, result, f"Clé manquante : {key}")
    
    def test_confidence_range(self):
        """Test : La confiance doit être entre 0 et 1."""
        result = self.analyzer.analyze("Test de confiance")
        
        self.assertGreaterEqual(result['confidence'], 0)
        self.assertLessEqual(result['confidence'], 1)


# ============================================================
# TESTS DU TRACKER D'HUMEUR
# ============================================================

class TestMoodTracker(unittest.TestCase):
    """Tests pour la classe MoodTracker."""
    
    def setUp(self):
        """Crée un nouveau tracker pour chaque test."""
        self.temp_file = os.path.join(tempfile.gettempdir(), "test_mood.json")
        self.tracker = MoodTracker(history_file=self.temp_file)
        self.tracker.mood_history = []
    
    def tearDown(self):
        """Nettoie après chaque test."""
        if os.path.exists(self.temp_file):
            try:
                os.remove(self.temp_file)
            except:
                pass
    
    def test_add_mood(self):
        """Test : Ajout d'une entrée d'humeur."""
        self.tracker.add_mood(
            text="Test positif",
            sentiment="positif",
            confidence=0.8
        )
        
        self.assertEqual(len(self.tracker.mood_history), 1)
        self.assertEqual(self.tracker.mood_history[0]['sentiment'], 'positif')
    
    def test_add_multiple_moods(self):
        """Test : Ajout de plusieurs entrées."""
        for i in range(5):
            self.tracker.add_mood(
                text=f"Message {i}",
                sentiment="neutre",
                confidence=0.5
            )
        
        self.assertEqual(len(self.tracker.mood_history), 5)
    
    def test_get_trend_empty(self):
        """Test : Tendance avec historique vide."""
        trend = self.tracker.get_trend(days=7)
        
        self.assertIn('message_count', trend)
        self.assertEqual(trend['message_count'], 0)
    
    def test_get_trend_with_data(self):
        """Test : Tendance avec des données."""
        for conf in [0.3, 0.5, 0.7, 0.6, 0.8]:
            self.tracker.add_mood(
                text="Test",
                sentiment="positif",
                confidence=conf
            )
        
        trend = self.tracker.get_trend(days=7)
        self.assertGreater(trend['message_count'], 0)
    
    def test_get_statistics(self):
        """Test : Calcul des statistiques."""
        sentiments = ['positif', 'négatif', 'neutre', 'positif', 'positif']
        
        for sentiment in sentiments:
            self.tracker.add_mood(
                text="Test",
                sentiment=sentiment,
                confidence=0.7
            )
        
        stats = self.tracker.get_statistics()
        
        # Vérifie que les stats contiennent des infos pertinentes
        self.assertIsInstance(stats, dict)
        self.assertGreater(len(stats), 0)


# ============================================================
# TESTS DU GÉNÉRATEUR DE RÉPONSES
# ============================================================

class TestResponseGenerator(unittest.TestCase):
    """Tests pour la classe ResponseGenerator."""
    
    @classmethod
    def setUpClass(cls):
        """Initialise le générateur."""
        cls.generator = ResponseGenerator()
    
    def test_generate_positive_response(self):
        """Test : Génération de réponse positive."""
        response = self.generator.generate_response(
            sentiment="positif",
            sentiment_detail="très positif",
            confidence=0.8,
            text="Je suis content"
        )
        
        self.assertIn('main_response', response)
        self.assertIsInstance(response['main_response'], str)
        self.assertGreater(len(response['main_response']), 0)
    
    def test_generate_negative_response(self):
        """Test : Génération de réponse négative."""
        response = self.generator.generate_response(
            sentiment="négatif",
            sentiment_detail="négatif",
            confidence=0.7,
            text="Je suis triste"
        )
        
        self.assertIn('main_response', response)
    
    def test_generate_neutral_response(self):
        """Test : Génération de réponse neutre."""
        response = self.generator.generate_response(
            sentiment="neutre",
            sentiment_detail="neutre",
            confidence=0.5,
            text="Il fait beau"
        )
        
        self.assertIn('main_response', response)
    
    def test_crisis_detection(self):
        """Test : Détection de crise."""
        response = self.generator.generate_response(
            sentiment="très négatif",
            sentiment_detail="très négatif",
            confidence=0.9,
            text="Je veux me suicider"
        )
        
        self.assertTrue(response.get('is_crisis', False))
    
    def test_response_variety(self):
        """Test : Variété des réponses."""
        responses = set()
        
        for _ in range(10):
            response = self.generator.generate_response(
                sentiment="positif",
                sentiment_detail="positif",
                confidence=0.8,
                text="Bonne journée"
            )
            responses.add(response['main_response'])
        
        self.assertGreater(len(responses), 1)


# ============================================================
# TESTS DU VISUALISEUR
# ============================================================

class TestMoodVisualizer(unittest.TestCase):
    """Tests pour la classe MoodVisualizer."""
    
    @classmethod
    def setUpClass(cls):
        """Initialise le visualiseur."""
        cls.visualizer = MoodVisualizer()
    
    def test_get_mood_face_positive(self):
        """Test : Visage pour sentiment positif."""
        face = self.visualizer.get_mood_face("très positif")
        
        self.assertIsInstance(face, str)
        self.assertGreater(len(face), 0)
    
    def test_get_mood_face_negative(self):
        """Test : Visage pour sentiment négatif."""
        face = self.visualizer.get_mood_face("négatif")
        
        self.assertIsInstance(face, str)
    
    def test_get_mood_bar(self):
        """Test : Barre de progression."""
        bar = self.visualizer.get_mood_bar(0.75)
        
        self.assertIsInstance(bar, str)
    
    def test_display_mood_dashboard(self):
        """Test : Affichage du tableau de bord."""
        try:
            self.visualizer.display_mood_dashboard(
                sentiment="positif",
                score=0.8,
                confidence=0.85,
                trend=0.2
            )
            success = True
        except Exception as e:
            print(f"Erreur: {e}")
            success = False
        
        self.assertTrue(success)


# ============================================================
# TESTS D'INTÉGRATION
# ============================================================

class TestIntegration(unittest.TestCase):
    """Tests d'intégration - tous les composants ensemble."""
    
    @classmethod
    def setUpClass(cls):
        """Initialise tous les composants."""
        print("\n🔄 Chargement des composants pour tests d'intégration...")
        cls.analyzer = SentimentAnalyzer()
        cls.tracker = MoodTracker()
        cls.generator = ResponseGenerator()
        cls.visualizer = MoodVisualizer()
        print("✅ Composants chargés !")
    
    def test_full_pipeline(self):
        """Test : Pipeline complet."""
        message = "Je suis vraiment content de ma journée !"
        
        # 1. Analyser
        sentiment_result = self.analyzer.analyze(message)
        self.assertIn('sentiment', sentiment_result)
        
        # 2. Tracker
        self.tracker.add_mood(
            text=message,
            sentiment=sentiment_result['sentiment'],
            confidence=sentiment_result['confidence']
        )
        
        # 3. Tendance
        trend = self.tracker.get_trend(days=7)
        self.assertIn('message_count', trend)
        
        # 4. Réponse
        response = self.generator.generate_response(
            sentiment=sentiment_result['sentiment'],
            sentiment_detail=sentiment_result['sentiment'],
            confidence=sentiment_result['confidence'],
            text=message,
            mood_trend=trend
        )
        self.assertIn('main_response', response)
        
        print(f"\n✅ Message: {message}")
        print(f"   Sentiment: {sentiment_result['sentiment']}")
        print(f"   Confiance: {sentiment_result['confidence']:.2%}")
        print(f"   Réponse: {response['main_response'][:50]}...")
    
    def test_conversation_simulation(self):
        """Test : Simulation d'une conversation."""
        messages = [
            "Bonjour !",
            "Je me sens stressé",
            "Merci pour les conseils",
            "Je vais mieux maintenant",
            "Bonne journée !"
        ]
        
        for msg in messages:
            sentiment = self.analyzer.analyze(msg)
            
            self.tracker.add_mood(
                text=msg,
                sentiment=sentiment['sentiment'],
                confidence=sentiment['confidence']
            )
            
            response = self.generator.generate_response(
                sentiment=sentiment['sentiment'],
                sentiment_detail=sentiment['sentiment'],
                confidence=sentiment['confidence'],
                text=msg
            )
            
            self.assertIn('main_response', response)
        
        stats = self.tracker.get_statistics()
        self.assertIsInstance(stats, dict)
        print(f"\n✅ Conversation de {len(messages)} messages simulée")


# ============================================================
# POINT D'ENTRÉE
# ============================================================

def run_tests():
    """Exécute tous les tests."""
    print("\n" + "=" * 60)
    print("🧪 EXÉCUTION DES TESTS UNITAIRES")
    print("=" * 60)
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestSentimentAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestMoodTracker))
    suite.addTests(loader.loadTestsFromTestCase(TestResponseGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestMoodVisualizer))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 60)
    
    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    successes = total - failures - errors
    
    print(f"   ✅ Réussis  : {successes}/{total}")
    print(f"   ❌ Échoués  : {failures}/{total}")
    print(f"   ⚠️  Erreurs  : {errors}/{total}")
    
    if total > 0:
        print(f"   📈 Taux     : {(successes/total)*100:.1f}%")
    
    if failures == 0 and errors == 0:
        print("\n🎉 TOUS LES TESTS SONT PASSÉS !")
    
    return result


if __name__ == "__main__":
    run_tests()
