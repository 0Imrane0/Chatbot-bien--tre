"""
Module de Visualisation d'Humeur
Crée des représentations visuelles de l'état émotionnel

Fonctionnalités :
- Émoji/visage selon le sentiment
- Barre de progression d'humeur
- Animation ASCII du visage
- Interprétation visuelle

Auteur : Étudiant ENSA Berrechid
Date : Décembre 2024
"""

from typing import Dict


class MoodVisualizer:
    """
    Visualisation de l'humeur avec emojis et animations
    """
    
    def __init__(self):
        """
        Initialise le visualiseur avec les emojis et visages ASCII
        """
        # Mapping sentiment → emoji
        self.mood_emojis = {
            'très positif': '😄',
            'positif': '🙂',
            'neutre': '😐',
            'négatif': '🙁',
            'très négatif': '😢'
        }
        
        # Visages ASCII détaillés
        self.mood_faces = {
            'très positif': r"""
    ╔═══════════════╗
    ║   😄 RADIEUX  ║
    ║   \(^o^)/     ║
    ╚═══════════════╝
""",
            'positif': r"""
    ╔═══════════════╗
    ║   🙂 CONTENT  ║
    ║    \(^_^)     ║
    ╚═══════════════╝
""",
            'neutre': r"""
    ╔═══════════════╗
    ║   😐 CALME    ║
    ║     (-_-)     ║
    ╚═══════════════╝
""",
            'négatif': r"""
    ╔═══════════════╗
    ║   🙁 TRISTE   ║
    ║    (T_T)      ║
    ╚═══════════════╝
""",
            'très négatif': r"""
    ╔═══════════════╗
    ║  😢 TRÈS MAL  ║
    ║   (╥_╥)       ║
    ╚═══════════════╝
"""
        }
        
        # Couleurs textuelles (pour console)
        self.mood_colors = {
            'très positif': '🟢',
            'positif': '🔵',
            'neutre': '⚪',
            'négatif': '🟠',
            'très négatif': '🔴'
        }
    
    def get_mood_face(self, sentiment: str) -> str:
        """
        Retourne le visage ASCII correspondant au sentiment
        
        Args:
            sentiment (str): Sentiment ('très positif', 'positif', etc.)
        
        Returns:
            str: Visage ASCII
        """
        return self.mood_faces.get(sentiment, self.mood_faces['neutre'])
    
    def get_mood_bar(self, score: float, width: int = 30) -> str:
        """
        Génère une barre de progression d'humeur
        
        Args:
            score (float): Score de -1 à 1
            width (int): Largeur de la barre
        
        Returns:
            str: Barre de progression formatée
        
        Exemple :
        Score 0.6 → [████████████▓▓▓▓▓▓] 80%
        """
        # Normaliser le score de -1,1 à 0,1
        normalized = (score + 1) / 2
        filled = int(normalized * width)
        empty = width - filled
        
        # Choisir le caractère selon le score
        if normalized > 0.75:
            char = '█'  # Très bon
            emoji = '😄'
        elif normalized > 0.5:
            char = '▓'  # Bon
            emoji = '🙂'
        elif normalized > 0.35:
            char = '▒'  # Neutre
            emoji = '😐'
        elif normalized > 0.2:
            char = '░'  # Pas bien
            emoji = '🙁'
        else:
            char = '▁'  # Très mal
            emoji = '😢'
        
        bar = char * filled + '·' * empty
        percentage = int(normalized * 100)
        
        return f"{emoji} [{bar}] {percentage}%"
    
    def get_trend_arrow(self, trend: float) -> str:
        """
        Retourne une flèche indiquant la tendance
        
        Args:
            trend (float): Valeur de tendance
        
        Returns:
            str: Flèche avec description
        """
        if trend > 0.3:
            return "📈 Forte amélioration !"
        elif trend > 0.1:
            return "↗️  Légère amélioration"
        elif trend > -0.1:
            return "➡️  Stable"
        elif trend > -0.3:
            return "↘️  Légère baisse"
        else:
            return "📉 Forte baisse"
    
    def display_mood_dashboard(self, sentiment: str, score: float, 
                              confidence: float, trend: float = None) -> str:
        """
        Affiche un tableau de bord complet de l'humeur
        
        Args:
            sentiment (str): Sentiment actuel
            score (float): Score numérique
            confidence (float): Confiance (0-1)
            trend (float): Tendance (optionnel)
        
        Returns:
            str: Dashboard formaté
        """
        emoji = self.mood_emojis.get(sentiment, '😐')
        color = self.mood_colors.get(sentiment, '⚪')
        
        dashboard = f"""
╔═══════════════════════════════════════════════════════════╗
║             {emoji} TABLEAU DE BORD D'HUMEUR {emoji}                ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  État actuel : {color} {sentiment.upper():^20} {color}              ║
║                                                           ║
║  Niveau d'humeur :                                        ║
║  {self.get_mood_bar(score)}                   ║
║                                                           ║
║  Confiance : {int(confidence*100):3d}% {'█' * int(confidence*20)}{'·' * (20-int(confidence*20))}              ║
║                                                           ║"""
        
        if trend is not None:
            dashboard += f"""
║  Tendance : {self.get_trend_arrow(trend):^30}          ║
║                                                           ║"""
        
        dashboard += """
╚═══════════════════════════════════════════════════════════╝
"""
        return dashboard
    
    def animate_mood_change(self, old_sentiment: str, new_sentiment: str) -> str:
        """
        Affiche une transition animée entre deux sentiments
        
        Args:
            old_sentiment (str): Ancien sentiment
            new_sentiment (str): Nouveau sentiment
        
        Returns:
            str: Animation textuelle
        """
        old_emoji = self.mood_emojis.get(old_sentiment, '😐')
        new_emoji = self.mood_emojis.get(new_sentiment, '😐')
        
        animation = f"""
    {old_emoji}  ➡️  {new_emoji}
    
    Évolution : {old_sentiment} → {new_sentiment}
"""
        return animation


# ============================================
# DÉMONSTRATION
# ============================================

def demo():
    """
    Démonstration du visualiseur d'humeur
    """
    print("\n" + "="*70)
    print("🎨 DÉMONSTRATION - VISUALISEUR D'HUMEUR")
    print("="*70 + "\n")
    
    visualizer = MoodVisualizer()
    
    # Test 1 : Très positif
    print("TEST 1 : Sentiment TRÈS POSITIF")
    print(visualizer.get_mood_face('très positif'))
    print(visualizer.display_mood_dashboard('très positif', 0.9, 0.85, 0.25))
    
    # Test 2 : Négatif
    print("\nTEST 2 : Sentiment NÉGATIF")
    print(visualizer.get_mood_face('négatif'))
    print(visualizer.display_mood_dashboard('négatif', -0.4, 0.72, -0.15))
    
    # Test 3 : Neutre
    print("\nTEST 3 : Sentiment NEUTRE")
    print(visualizer.get_mood_face('neutre'))
    print(visualizer.display_mood_dashboard('neutre', 0.0, 0.55))
    
    # Test 4 : Animation de changement
    print("\nTEST 4 : ANIMATION DE CHANGEMENT")
    print(visualizer.animate_mood_change('négatif', 'positif'))
    
    # Test 5 : Différentes barres
    print("\nTEST 5 : BARRES D'HUMEUR")
    print(f"Score  1.0 : {visualizer.get_mood_bar(1.0)}")
    print(f"Score  0.5 : {visualizer.get_mood_bar(0.5)}")
    print(f"Score  0.0 : {visualizer.get_mood_bar(0.0)}")
    print(f"Score -0.5 : {visualizer.get_mood_bar(-0.5)}")
    print(f"Score -1.0 : {visualizer.get_mood_bar(-1.0)}")
    
    print("\n" + "="*70)
    print("✅ Démonstration terminée !")
    print("="*70)


if __name__ == "__main__":
    demo()
