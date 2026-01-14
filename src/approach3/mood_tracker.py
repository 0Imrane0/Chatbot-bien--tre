"""
Module de Suivi d'Humeur (Mood Tracker) - Approche 1
Enregistre, analyse et suit l'évolution de l'humeur/sentiment dans le temps

Ce module permet de :
- Historique complet des sentiments
- Tendances et évolutions
- Détection de patterns
- Statistiques et insights
- Persistance des données (sauvegarde JSON)

Auteur : Étudiant ENSA Berrechid
Date : Décembre 2024
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
import statistics


class MoodTracker:
    """
    Suivi complet de l'humeur et du sentiment de l'utilisateur
    
    Fonctionnalités principales :
    - Enregistrement des sentiments avec timestamps
    - Calcul des tendances (7j, 14j, 30j)
    - Détection des patterns
    - Génération de statistiques
    - Persistance en JSON
    
    Architecture :
    - mood_history (list) : Liste de tous les sentiments enregistrés
    - save/load : Sauvegarde et chargement depuis JSON
    """
    
    def __init__(self, history_file: str = "data/mood_history.json"):
        """
        Initialise le tracker d'humeur
        
        Args:
            history_file (str): Chemin vers le fichier JSON de l'historique
        
        Processus :
        1. Définir le chemin de sauvegarde
        2. Charger l'historique existant (s'il existe)
        3. Initialiser les structures de données
        """
        self.history_file = history_file
        self.mood_history = []  # Liste des sentiments
        
        print("🔧 Initialisation du Tracker d'Humeur...")
        
        # Charger l'historique s'il existe
        if os.path.exists(history_file):
            print(f"📂 Chargement de l'historique existant...")
            self.load_history()
        else:
            print(f"✨ Nouvel historique créé")
        
        print(f"✅ Tracker prêt ! ({len(self.mood_history)} messages en mémoire)\n")
    
    def add_mood(self, text: str, sentiment: str, confidence: float, 
                 score: float = None) -> Dict[str, Any]:
        """
        Ajoute un nouveau sentiment à l'historique
        
        Args:
            text (str): Le message original de l'utilisateur
            sentiment (str): 'positif', 'négatif', ou 'neutre'
            confidence (float): Score de confiance (0-1)
            score (float): Score numérique du sentiment (-1 à 1)
        
        Returns:
            dict: L'enregistrement ajouté
        
        Processus :
        1. Créer l'enregistrement avec timestamp
        2. L'ajouter à l'historique
        3. Sauvegarder automatiquement
        4. Retourner l'enregistrement
        """
        # Calculer le score numérique si pas fourni
        if score is None:
            score_mapping = {
                'très positif': 1.0,
                'positif': 0.5,
                'neutre': 0.0,
                'négatif': -0.5,
                'très négatif': -1.0
            }
            score = score_mapping.get(sentiment, 0.0)
        
        # Créer l'enregistrement
        entry = {
            'timestamp': datetime.now().isoformat(),  # Format ISO 8601
            'text': text,
            'sentiment': sentiment,
            'confidence': confidence,
            'score': score
        }
        
        # Ajouter à l'historique
        self.mood_history.append(entry)
        
        # Sauvegarder automatiquement
        self.save_history()
        
        return entry
    
    def get_trend(self, days: int = 7) -> Dict[str, Any]:
        """
        Calcule la tendance sur les N derniers jours
        
        Args:
            days (int): Nombre de jours à analyser (7, 14, 30)
        
        Returns:
            dict: Contient :
                - mean_score : Score moyen sur la période
                - trend : Évolution (positif si augmente)
                - sentiment_distribution : % des sentiments
                - message_count : Nombre de messages
                - start_date, end_date : Dates de la période
        
        Exemple :
        {
            'mean_score': 0.65,
            'trend': 0.15,  # Augmente !
            'sentiment_distribution': {
                'positif': 60%,
                'neutre': 25%,
                'négatif': 15%
            },
            'message_count': 12
        }
        """
        # Calculer la date limite
        cutoff_date = datetime.now() - timedelta(days=days)
        cutoff_iso = cutoff_date.isoformat()
        
        # Filtrer les messages de cette période
        period_messages = [
            msg for msg in self.mood_history
            if msg['timestamp'] >= cutoff_iso
        ]
        
        # Si pas de messages dans cette période
        if not period_messages:
            return {
                'mean_score': 0.0,
                'trend': 0.0,
                'sentiment_distribution': {},
                'message_count': 0,
                'start_date': cutoff_date.isoformat(),
                'end_date': datetime.now().isoformat(),
                'message': f"Aucun message sur les {days} derniers jours"
            }
        
        # Étape 1 : Calculer le score moyen
        scores = [msg['score'] for msg in period_messages]
        mean_score = statistics.mean(scores)
        
        # Étape 2 : Calculer la tendance
        # Comparer le début et la fin de la période
        first_half = period_messages[:len(period_messages)//2]
        second_half = period_messages[len(period_messages)//2:]
        
        trend = 0.0
        if first_half and second_half:
            first_avg = statistics.mean([msg['score'] for msg in first_half])
            second_avg = statistics.mean([msg['score'] for msg in second_half])
            trend = second_avg - first_avg  # Négatif = baisse, positif = hausse
        
        # Étape 3 : Distribution des sentiments
        sentiment_counts = {}
        for msg in period_messages:
            sentiment = msg['sentiment']
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
        
        total_messages = len(period_messages)
        sentiment_distribution = {
            sentiment: round((count / total_messages) * 100, 1)
            for sentiment, count in sentiment_counts.items()
        }
        
        # Étape 4 : Construire le résultat
        result = {
            'mean_score': round(mean_score, 3),
            'trend': round(trend, 3),
            'sentiment_distribution': sentiment_distribution,
            'message_count': total_messages,
            'start_date': cutoff_date.isoformat(),
            'end_date': datetime.now().isoformat(),
            'period_days': days
        }
        
        return result
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Calcule les statistiques globales sur tout l'historique
        
        Returns:
            dict: Statistiques détaillées
        """
        if not self.mood_history:
            return {
                'total_messages': 0,
                'message': 'Aucun message enregistré'
            }
        
        # Scores
        scores = [msg['score'] for msg in self.mood_history]
        
        # Confiances
        confidences = [msg['confidence'] for msg in self.mood_history]
        
        # Sentiments
        sentiment_counts = {}
        for msg in self.mood_history:
            sentiment = msg['sentiment']
            sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
        
        total = len(self.mood_history)
        sentiment_distribution = {
            sentiment: round((count / total) * 100, 1)
            for sentiment, count in sentiment_counts.items()
        }
        
        # Dates
        dates = [datetime.fromisoformat(msg['timestamp']) 
                for msg in self.mood_history]
        first_date = min(dates).isoformat() if dates else None
        last_date = max(dates).isoformat() if dates else None
        
        stats = {
            'total_messages': total,
            'mean_score': round(statistics.mean(scores), 3),
            'median_score': round(statistics.median(scores), 3),
            'std_dev': round(statistics.stdev(scores), 3) if len(scores) > 1 else 0,
            'min_score': round(min(scores), 3),
            'max_score': round(max(scores), 3),
            'mean_confidence': round(statistics.mean(confidences), 3),
            'sentiment_distribution': sentiment_distribution,
            'most_common_sentiment': max(sentiment_counts, 
                                        key=sentiment_counts.get) if sentiment_counts else None,
            'first_message_date': first_date,
            'last_message_date': last_date,
            'days_tracked': (max(dates) - min(dates)).days if len(dates) > 1 else 0
        }
        
        return stats
    
    def detect_patterns(self, window_size: int = 3) -> List[Dict[str, Any]]:
        """
        Détecte les patterns d'amélioration ou de dégradation
        
        Args:
            window_size (int): Nombre de messages pour calculer une tendance
        
        Returns:
            list: Liste des patterns détectés
        
        Example :
        [
            {
                'type': 'improving',
                'strength': 0.8,  # Force du pattern
                'description': 'Amélioration constante depuis 5 messages',
                'messages': [...]
            }
        ]
        """
        if len(self.mood_history) < window_size:
            return [{'message': 'Pas assez de messages pour détecter des patterns'}]
        
        patterns = []
        
        # Analyser les fenêtres glissantes
        for i in range(len(self.mood_history) - window_size + 1):
            window = self.mood_history[i:i+window_size]
            scores = [msg['score'] for msg in window]
            
            # Vérifier si c'est une amélioration ou dégradation
            trend = scores[-1] - scores[0]
            
            if trend > 0.3:  # Amélioration significative
                patterns.append({
                    'type': 'improving',
                    'strength': trend,
                    'position': i,
                    'window': [msg['timestamp'] for msg in window],
                    'scores': scores
                })
            
            elif trend < -0.3:  # Dégradation significative
                patterns.append({
                    'type': 'declining',
                    'strength': abs(trend),
                    'position': i,
                    'window': [msg['timestamp'] for msg in window],
                    'scores': scores
                })
        
        # Si aucun pattern détecté
        if not patterns:
            patterns.append({
                'type': 'stable',
                'message': 'Humeur relativement stable'
            })
        
        return patterns
    
    def save_history(self) -> bool:
        """
        Sauvegarde l'historique en JSON
        
        Returns:
            bool: True si succès, False sinon
        
        Processus :
        1. Créer le dossier s'il n'existe pas
        2. Convertir en JSON
        3. Écrire dans le fichier
        4. Retourner succès/échec
        """
        try:
            # Créer le dossier parent s'il n'existe pas
            os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
            
            # Préparer les données
            data = {
                'created_at': self.mood_history[0]['timestamp'] 
                             if self.mood_history else datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'messages': self.mood_history
            }
            
            # Écrire en JSON
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return True
        
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde : {e}")
            return False
    
    def load_history(self) -> bool:
        """
        Charge l'historique depuis JSON
        
        Returns:
            bool: True si succès, False sinon
        """
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.mood_history = data.get('messages', [])
            
            print(f"✅ Historique chargé : {len(self.mood_history)} messages")
            return True
        
        except Exception as e:
            print(f"⚠️  Impossible de charger l'historique : {e}")
            return False
    
    def get_summary(self) -> str:
        """
        Génère un résumé textuel de l'état actuel
        
        Returns:
            str: Résumé en langage naturel
        """
        if not self.mood_history:
            return "Aucune donnée enregistrée. Commence à discuter pour tracker ton humeur !"
        
        # Tendance sur 7 jours
        trend_7d = self.get_trend(7)
        mean_score = trend_7d['mean_score']
        trend = trend_7d['trend']
        
        # Général
        stats = self.get_statistics()
        most_common = stats['most_common_sentiment']
        
        # Construire le résumé
        summary = f"""
📊 RÉSUMÉ DE TON BIEN-ÊTRE
{'='*50}

🎯 État actuel (7 derniers jours) :
   • Score moyen : {mean_score:.2f}/1.0
   • Tendance : {'+' if trend > 0 else ''}{trend:.2f}
   • Sentiment dominant : {most_common}
   • Messages : {trend_7d['message_count']}

📈 Statistiques globales :
   • Messages total : {stats['total_messages']}
   • Score moyen global : {stats['mean_score']:.2f}/1.0
   • Jours suivis : {stats['days_tracked']}
   • Confiance moyenne : {stats['mean_confidence']*100:.1f}%

🎭 Distribution des sentiments :
"""
        
        for sentiment, percentage in stats['sentiment_distribution'].items():
            summary += f"   • {sentiment.capitalize()} : {percentage}%\n"
        
        # Interprétation
        if mean_score > 0.5:
            summary += "\n✨ Tu vas plutôt bien ! Continue comme ça ! 😊"
        elif mean_score > 0:
            summary += "\n🙂 Tu es dans une bonne moyenne, on peut faire mieux ! 💪"
        else:
            summary += "\n😔 Ça semble difficile en ce moment. Parlons-en ! 💙"
        
        return summary
    
    def export_data(self, format_type: str = 'json', filename: str = None) -> bool:
        """
        Exporte les données dans différents formats
        
        Args:
            format_type (str): 'json', 'csv'
            filename (str): Nom du fichier (optionnel)
        
        Returns:
            bool: Succès ou non
        """
        if format_type == 'json':
            filename = filename or f"export_mood_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.mood_history, f, ensure_ascii=False, indent=2)
                print(f"✅ Export JSON réussi : {filename}")
                return True
            except Exception as e:
                print(f"❌ Erreur export JSON : {e}")
                return False
        
        return False


# ============================================
# DÉMONSTRATION
# ============================================

def demo():
    """
    Démonstration du Tracker d'Humeur
    """
    print("\n" + "="*70)
    print("🧪 DÉMONSTRATION - TRACKER D'HUMEUR")
    print("="*70 + "\n")
    
    # Créer un tracker
    tracker = MoodTracker("data/mood_test.json")
    
    # Simulations de messages (comme si l'utilisateur parlait)
    test_data = [
        ("Je suis triste aujourd'hui", "négatif", 0.72, -0.5),
        ("Ça va un peu mieux", "neutre", 0.45, 0.0),
        ("Je suis content maintenant !", "positif", 0.85, 0.5),
        ("Journée formidable !", "très positif", 0.91, 1.0),
        ("Un peu fatigue mais heureux", "positif", 0.67, 0.5),
        ("Super jour !", "très positif", 0.88, 1.0),
        ("Je me sens mieux", "positif", 0.73, 0.5),
    ]
    
    print("📝 Ajout de 7 messages de test...\n")
    for text, sentiment, confidence, score in test_data:
        entry = tracker.add_mood(text, sentiment, confidence, score)
        print(f"   ✅ \"{text}\"")
        print(f"      → {sentiment} ({confidence*100:.0f}%)\n")
    
    # Afficher la tendance sur 7 jours
    print("\n" + "="*70)
    print("📈 TENDANCE SUR 7 JOURS")
    print("="*70)
    trend = tracker.get_trend(7)
    print(f"\n   Score moyen : {trend['mean_score']:.3f}")
    print(f"   Tendance : {trend['trend']:.3f} ({'Amélioration ⬆️' if trend['trend'] > 0 else 'Dégradation ⬇️'})")
    print(f"   Messages : {trend['message_count']}")
    print(f"\n   Distribution des sentiments :")
    for sentiment, percentage in trend['sentiment_distribution'].items():
        print(f"      • {sentiment:15} : {percentage:5.1f}%")
    
    # Afficher les statistiques globales
    print("\n" + "="*70)
    print("📊 STATISTIQUES GLOBALES")
    print("="*70)
    stats = tracker.get_statistics()
    print(f"\n   Total messages : {stats['total_messages']}")
    print(f"   Score moyen : {stats['mean_score']:.3f}")
    print(f"   Médiane : {stats['median_score']:.3f}")
    print(f"   Écart-type : {stats['std_dev']:.3f}")
    print(f"   Score min/max : {stats['min_score']:.3f} / {stats['max_score']:.3f}")
    print(f"   Confiance moyenne : {stats['mean_confidence']*100:.1f}%")
    print(f"   Sentiment dominant : {stats['most_common_sentiment']}")
    
    # Patterns
    print("\n" + "="*70)
    print("🔍 PATTERNS DÉTECTÉS")
    print("="*70)
    patterns = tracker.detect_patterns(3)
    for i, pattern in enumerate(patterns, 1):
        print(f"\n   Pattern {i}:")
        if 'type' in pattern:
            print(f"      Type : {pattern['type']}")
            if pattern['type'] != 'stable':
                print(f"      Force : {pattern['strength']:.3f}")
                print(f"      Scores : {[f'{s:.1f}' for s in pattern['scores']]}")
        else:
            print(f"      {pattern.get('message', pattern)}")
    
    # Résumé
    print(tracker.get_summary())
    
    # Sauvegarde
    print("\n" + "="*70)
    print("💾 SAUVEGARDE DES DONNÉES")
    print("="*70)
    print("\n✅ Données sauvegardées dans data/mood_test.json\n")


if __name__ == "__main__":
    demo()
