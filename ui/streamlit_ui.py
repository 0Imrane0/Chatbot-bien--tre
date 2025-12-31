"""
🎨 Interface Web Streamlit pour le Chatbot de Bien-être
======================================================

Ce module crée une interface web moderne et interactive
pour le chatbot de bien-être utilisant Streamlit.

Fonctionnalités :
- Chat interactif avec bulles de conversation
- Visualisation de l'humeur en temps réel
- Statistiques et graphiques
- Export des données

Auteur : Étudiant ENSA Berrechid
Module : Programmation Python et IA
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
import os
import json

# Ajouter le chemin du projet pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'approach1'))

# Import des modules du chatbot
from src.approach1.sentiment_analyzer import SentimentAnalyzer
from src.approach1.mood_tracker import MoodTracker
from src.approach1.response_generator import ResponseGenerator
from src.approach1.mood_visualizer import MoodVisualizer


# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="🧘 Chatbot Bien-être",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    /* Style général */
    .main {
        background-color: #f0f4f8;
    }
    
    /* Style pour les messages */
    .user-message {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        border-left: 4px solid #2196F3;
    }
    
    .bot-message {
        background-color: #f3e5f5;
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        border-left: 4px solid #9c27b0;
    }
    
    /* Style pour les cartes de statistiques */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    
    /* Style pour le header */
    .header-title {
        text-align: center;
        color: #1a237e;
        padding: 20px 0;
    }
    
    /* Animation pour les emojis */
    .emoji-large {
        font-size: 48px;
        animation: bounce 1s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# INITIALISATION DES COMPOSANTS
# ============================================================

@st.cache_resource
def load_chatbot_components():
    """
    Charge les composants du chatbot (mis en cache pour performance).
    
    Le décorateur @st.cache_resource permet de ne charger
    le modèle BERT qu'une seule fois, même si la page se rafraîchit.
    """
    analyzer = SentimentAnalyzer()
    tracker = MoodTracker()
    generator = ResponseGenerator()
    visualizer = MoodVisualizer()
    return analyzer, tracker, generator, visualizer


def init_session_state():
    """
    Initialise les variables de session Streamlit.
    
    session_state permet de conserver les données entre
    les interactions de l'utilisateur (rechargements de page).
    """
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'mood_history' not in st.session_state:
        st.session_state.mood_history = []
    
    if 'conversation_started' not in st.session_state:
        st.session_state.conversation_started = False


# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================

def get_emoji_for_sentiment(sentiment: str) -> str:
    """Retourne l'emoji correspondant au sentiment."""
    emoji_map = {
        'très positif': '😄',
        'positif': '🙂',
        'neutre': '😐',
        'négatif': '😔',
        'très négatif': '😢'
    }
    return emoji_map.get(sentiment.lower(), '🤔')


def get_color_for_sentiment(sentiment: str) -> str:
    """Retourne la couleur correspondant au sentiment."""
    color_map = {
        'très positif': '#4CAF50',
        'positif': '#8BC34A',
        'neutre': '#FFC107',
        'négatif': '#FF9800',
        'très négatif': '#F44336'
    }
    return color_map.get(sentiment.lower(), '#9E9E9E')


def create_mood_gauge(score: float, sentiment: str) -> go.Figure:
    """
    Crée une jauge de sentiment avec Plotly.
    
    Args:
        score: Score de 0 à 1
        sentiment: Label du sentiment
        
    Returns:
        Figure Plotly avec la jauge
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': f"Humeur Actuelle: {sentiment}", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1},
            'bar': {'color': get_color_for_sentiment(sentiment)},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 20], 'color': '#FFEBEE'},
                {'range': [20, 40], 'color': '#FFF3E0'},
                {'range': [40, 60], 'color': '#FFFDE7'},
                {'range': [60, 80], 'color': '#F1F8E9'},
                {'range': [80, 100], 'color': '#E8F5E9'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "#333", 'family': "Arial"}
    )
    
    return fig


def create_mood_timeline(mood_history: list) -> go.Figure:
    """
    Crée un graphique d'évolution de l'humeur dans le temps.
    
    Args:
        mood_history: Liste des entrées d'humeur
        
    Returns:
        Figure Plotly avec la timeline
    """
    if not mood_history:
        # Créer un graphique vide avec un message
        fig = go.Figure()
        fig.add_annotation(
            text="Pas encore d'historique d'humeur",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        fig.update_layout(
            height=300,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        return fig
    
    # Préparer les données
    times = [entry['timestamp'] for entry in mood_history]
    scores = [entry['score'] * 100 for entry in mood_history]
    sentiments = [entry['sentiment'] for entry in mood_history]
    colors = [get_color_for_sentiment(s) for s in sentiments]
    
    # Créer le graphique
    fig = go.Figure()
    
    # Ligne d'évolution
    fig.add_trace(go.Scatter(
        x=times,
        y=scores,
        mode='lines+markers',
        name='Humeur',
        line=dict(color='#667eea', width=3),
        marker=dict(size=10, color=colors, line=dict(width=2, color='white')),
        hovertemplate='<b>%{text}</b><br>Score: %{y:.0f}%<extra></extra>',
        text=sentiments
    ))
    
    # Zone de remplissage
    fig.add_trace(go.Scatter(
        x=times,
        y=scores,
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.2)',
        line=dict(color='rgba(0,0,0,0)'),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Ligne de référence (50%)
    fig.add_hline(
        y=50, 
        line_dash="dash", 
        line_color="gray",
        annotation_text="Neutre",
        annotation_position="right"
    )
    
    fig.update_layout(
        title="📈 Évolution de l'Humeur",
        xaxis_title="Temps",
        yaxis_title="Score (%)",
        yaxis=dict(range=[0, 100]),
        height=350,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(248, 249, 250, 0.8)',
        hovermode='x unified'
    )
    
    return fig


def create_sentiment_distribution(mood_history: list) -> go.Figure:
    """
    Crée un graphique en camembert de la distribution des sentiments.
    
    Args:
        mood_history: Liste des entrées d'humeur
        
    Returns:
        Figure Plotly avec le camembert
    """
    if not mood_history:
        fig = go.Figure()
        fig.add_annotation(
            text="Pas encore de données",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        fig.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)')
        return fig
    
    # Compter les sentiments
    sentiment_counts = {}
    for entry in mood_history:
        sentiment = entry['sentiment']
        sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
    
    labels = list(sentiment_counts.keys())
    values = list(sentiment_counts.values())
    colors = [get_color_for_sentiment(s) for s in labels]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(colors=colors, line=dict(color='white', width=2)),
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>%{value} messages<br>%{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title="🎯 Distribution des Sentiments",
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    
    return fig


# ============================================================
# COMPOSANTS DE L'INTERFACE
# ============================================================

def render_sidebar(tracker: MoodTracker):
    """Affiche la barre latérale avec les statistiques."""
    
    with st.sidebar:
        st.markdown("## 📊 Tableau de Bord")
        st.markdown("---")
        
        # Statistiques rapides
        stats = tracker.get_statistics()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="💬 Messages",
                value=stats.get('total_entries', 0),
                delta=None
            )
        
        with col2:
            avg_score = stats.get('mean_score', 0)
            st.metric(
                label="📈 Score Moyen",
                value=f"{avg_score:.0%}",
                delta=None
            )
        
        st.markdown("---")
        
        # Tendance actuelle
        trend = tracker.get_trend(days=7)
        trend_direction = trend.get('trend_direction', 0)
        
        if trend_direction > 0.1:
            trend_emoji = "📈"
            trend_text = "En hausse"
            trend_color = "green"
        elif trend_direction < -0.1:
            trend_emoji = "📉"
            trend_text = "En baisse"
            trend_color = "red"
        else:
            trend_emoji = "➡️"
            trend_text = "Stable"
            trend_color = "orange"
        
        st.markdown(f"""
        ### {trend_emoji} Tendance (7 jours)
        <p style="color: {trend_color}; font-size: 18px; font-weight: bold;">
            {trend_text}
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Boutons d'action
        st.markdown("### ⚙️ Actions")
        
        if st.button("🗑️ Effacer l'historique", use_container_width=True):
            st.session_state.messages = []
            st.session_state.mood_history = []
            tracker.history = []
            st.rerun()
        
        if st.button("💾 Exporter les données", use_container_width=True):
            export_data = {
                'messages': st.session_state.messages,
                'mood_history': st.session_state.mood_history,
                'statistics': stats
            }
            st.download_button(
                label="📥 Télécharger JSON",
                data=json.dumps(export_data, ensure_ascii=False, indent=2),
                file_name=f"chatbot_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        st.markdown("---")
        
        # Informations
        st.markdown("""
        ### ℹ️ À propos
        
        Ce chatbot utilise **BERT multilingue** pour analyser
        vos émotions et vous accompagner dans votre bien-être.
        
        🔒 Vos données restent sur votre ordinateur.
        
        ---
        
        **🆘 En cas d'urgence :**
        - SOS Amitié : 09 72 39 40 50
        - Fil Santé Jeunes : 0 800 235 236
        
        ---
        
        *Projet ENSA Berrechid - 2024*
        """)


def render_header():
    """Affiche l'en-tête de l'application."""
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="header-title">
            <h1>🧘 Chatbot Bien-être</h1>
            <p style="font-size: 18px; color: #666;">
                Votre compagnon pour le suivi de votre humeur
            </p>
        </div>
        """, unsafe_allow_html=True)


def render_chat_area(analyzer: SentimentAnalyzer, 
                     tracker: MoodTracker,
                     generator: ResponseGenerator):
    """
    Affiche la zone de chat principale.
    
    Args:
        analyzer: Analyseur de sentiment
        tracker: Tracker d'humeur
        generator: Générateur de réponses
    """
    
    # Afficher l'historique des messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])
    
    # Zone de saisie
    if prompt := st.chat_input("Comment vous sentez-vous aujourd'hui ? 💭"):
        
        # Ajouter le message de l'utilisateur
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "avatar": "👤"
        })
        
        # Afficher le message de l'utilisateur
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
        
        # Analyser le sentiment
        with st.spinner("🔍 Analyse en cours..."):
            sentiment_result = analyzer.analyze(prompt)
        
        # Enregistrer dans le tracker
        tracker.add_mood(
            text=prompt,
            sentiment=sentiment_result['sentiment'],
            confidence=sentiment_result['confidence']
        )
        
        # Ajouter à l'historique de session
        st.session_state.mood_history.append({
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'sentiment': sentiment_result['sentiment'],
            'score': sentiment_result['confidence'],
            'text': prompt[:50] + "..." if len(prompt) > 50 else prompt
        })
        
        # Obtenir la tendance
        mood_trend = tracker.get_trend(days=7)
        
        # Générer la réponse
        response_data = generator.generate_response(
            sentiment=sentiment_result['sentiment'],
            score=sentiment_result['confidence'],
            mood_trend=mood_trend,
            user_message=prompt
        )
        
        # Construire la réponse du bot
        emoji = get_emoji_for_sentiment(sentiment_result['sentiment'])
        
        bot_response = f"{emoji} {response_data['response']}\n\n"
        
        if response_data.get('advice'):
            bot_response += f"💡 **Conseil :** {response_data['advice']}\n\n"
        
        if response_data.get('activity'):
            bot_response += f"🎯 **Activité suggérée :** {response_data['activity']}\n\n"
        
        # Ajouter info de sentiment (discret)
        bot_response += f"\n---\n*Sentiment détecté : {sentiment_result['sentiment']} ({sentiment_result['confidence']:.0%})*"
        
        # Ajouter le message du bot
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_response,
            "avatar": "🤖"
        })
        
        # Afficher la réponse du bot
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(bot_response)
        
        # Rafraîchir pour mettre à jour les graphiques
        st.rerun()


def render_analytics(tracker: MoodTracker):
    """Affiche les graphiques d'analyse."""
    
    st.markdown("---")
    st.markdown("## 📈 Analyses")
    
    # Ligne avec jauge et timeline
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Dernière humeur
        if st.session_state.mood_history:
            last_mood = st.session_state.mood_history[-1]
            fig_gauge = create_mood_gauge(
                last_mood['score'],
                last_mood['sentiment']
            )
            st.plotly_chart(fig_gauge, use_container_width=True)
        else:
            st.info("💭 Commencez une conversation pour voir votre humeur")
    
    with col2:
        # Timeline
        fig_timeline = create_mood_timeline(st.session_state.mood_history)
        st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Distribution des sentiments
    col3, col4 = st.columns(2)
    
    with col3:
        fig_pie = create_sentiment_distribution(st.session_state.mood_history)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col4:
        # Statistiques textuelles
        st.markdown("### 📋 Résumé de Session")
        
        if st.session_state.mood_history:
            total = len(st.session_state.mood_history)
            avg_score = sum(m['score'] for m in st.session_state.mood_history) / total
            
            # Trouver le sentiment dominant
            sentiment_counts = {}
            for entry in st.session_state.mood_history:
                s = entry['sentiment']
                sentiment_counts[s] = sentiment_counts.get(s, 0) + 1
            dominant = max(sentiment_counts, key=sentiment_counts.get)
            
            st.markdown(f"""
            | Métrique | Valeur |
            |----------|--------|
            | 💬 Messages analysés | **{total}** |
            | 📊 Score moyen | **{avg_score:.0%}** |
            | 🎭 Sentiment dominant | **{dominant}** |
            | ⏱️ Début session | **{st.session_state.mood_history[0]['timestamp']}** |
            """)
        else:
            st.info("Aucune donnée pour le moment")


# ============================================================
# FONCTION PRINCIPALE
# ============================================================

def main():
    """Point d'entrée principal de l'application Streamlit."""
    
    # Initialiser la session
    init_session_state()
    
    # Charger les composants du chatbot
    try:
        analyzer, tracker, generator, visualizer = load_chatbot_components()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du chatbot : {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")
        return
    
    # Afficher l'interface
    render_header()
    render_sidebar(tracker)
    
    # Onglets pour organiser le contenu
    tab1, tab2 = st.tabs(["💬 Conversation", "📊 Analyses"])
    
    with tab1:
        # Message de bienvenue si première visite
        if not st.session_state.conversation_started:
            st.info("""
            👋 **Bienvenue !**
            
            Je suis votre compagnon de bien-être. Partagez avec moi comment vous vous sentez,
            et je vous accompagnerai avec des conseils personnalisés.
            
            Commencez par me dire comment vous allez aujourd'hui ! 💙
            """)
            st.session_state.conversation_started = True
        
        render_chat_area(analyzer, tracker, generator)
    
    with tab2:
        render_analytics(tracker)


# ============================================================
# POINT D'ENTRÉE
# ============================================================

if __name__ == "__main__":
    main()
