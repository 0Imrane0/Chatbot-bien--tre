"""
🎨 Interface Web Avancée V2 - Chatbot Bien-être avec BERT Fine-tuné
===================================================================

Interface ultra-moderne avec:
- BERT Fine-tuné (Approche 3) - 85% précision
- Module CBT intégré (détection distorsions cognitives)
- Visualisations intelligentes et interactives
- Historique avec refresh
- Design professionnel

Auteur: Étudiant ENSA Berrechid
Date: Janvier 2026
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import sys
import os
import json
import time
from collections import Counter

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import des modules - APPROCHE 3 (BERT + Gemini API)
from approach3.chatbot import WellbeingChatbot
from approach3.sentiment_analyzer import SentimentAnalyzer
from approach3.mood_tracker import MoodTracker
from approach3.response_generator import ResponseGenerator
from gemini_wrapper import GeminiChatbot

# ============================================================
# CONFIGURATION DE LA PAGE
# ============================================================

st.set_page_config(
    page_title="🧠 Chatbot Bien-être IA",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# STYLES CSS ULTRA-MODERNES
# ============================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #1e293b; border-radius: 10px; }
    ::-webkit-scrollbar-thumb { background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 10px; }
    
    /* Background sombre élégant */
    .stApp { 
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%) !important; 
    }
    
    /* Texte principal clair */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp div {
        color: #f1f5f9 !important;
    }
    
    /* Titres bien visibles */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #ffffff !important;
    }
    
    /* Input de chat amélioré */
    .stTextInput > div > div > input {
        background: linear-gradient(135deg, #1e293b, #334155) !important;
        border: 2px solid #6366f1 !important;
        border-radius: 16px !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.2) !important;
        transition: all 0.3s ease !important;
        height: auto !important;
        min-height: 45px !important;
    }
    
    .stTextInput > div > div {
        overflow: visible !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.3), 0 8px 30px rgba(99, 102, 241, 0.5) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #94a3b8 !important;
        font-style: italic;
    }
    
    /* Container de chat - Styliser le formulaire Streamlit */
    .stForm {
        background: linear-gradient(135deg, #1e293b, #0f172a) !important;
        border-radius: 20px !important;
        padding: 1rem 1.5rem !important;
        margin-top: 1.5rem !important;
        border: 2px solid #6366f1 !important;
        box-shadow: 0 10px 40px rgba(99, 102, 241, 0.3) !important;
        overflow: visible !important;
    }
    
    /* Bouton du formulaire */
    .stForm button[kind="secondaryFormSubmit"],
    .stForm button[data-testid="stFormSubmitButton"] {
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 0.8rem 1.5rem !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        height: 55px !important;
        min-width: 60px !important;
        transition: all 0.3s ease !important;
    }
    
    .stForm button:hover {
        transform: translateY(-2px) scale(1.05) !important;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.5) !important;
    }
    
    /* Label de l'input */
    .stTextInput label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }
    
    .hero-container {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
        padding: 2.5rem 2rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.35);
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 100%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
        animation: pulse-bg 4s ease-in-out infinite;
    }
    
    @keyframes pulse-bg {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.3; }
    }
    
    .hero-title {
        color: white;
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        margin: 0;
        text-shadow: 2px 4px 8px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        color: rgba(255,255,255,0.95);
        font-size: 1.15rem;
        text-align: center;
        margin-top: 0.75rem;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    .hero-badges {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }
    
    .hero-badge {
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        color: white;
        padding: 0.5rem 1.25rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .user-bubble {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: #ffffff !important;
        padding: 1.25rem 1.5rem;
        border-radius: 24px 24px 8px 24px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 10px 35px rgba(99, 102, 241, 0.35);
        animation: slideInRight 0.4s ease;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .user-bubble strong {
        color: #ffffff !important;
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .bot-bubble {
        background: linear-gradient(135deg, #1e293b, #334155);
        color: #f1f5f9 !important;
        padding: 1.25rem 1.5rem;
        border-radius: 24px 24px 24px 8px;
        margin: 1rem 0;
        margin-right: 20%;
        box-shadow: 0 10px 35px rgba(0,0,0,0.3);
        border: 1px solid #475569;
        animation: slideInLeft 0.4s ease;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .bot-bubble strong {
        color: #ffffff !important;
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .sentiment-tag {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.35rem 0.85rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .sentiment-very-positive { background: linear-gradient(135deg, #10b981, #34d399); color: white; }
    .sentiment-positive { background: linear-gradient(135deg, #34d399, #6ee7b7); color: #064e3b; }
    .sentiment-neutral { background: linear-gradient(135deg, #94a3b8, #cbd5e1); color: #1e293b; }
    .sentiment-negative { background: linear-gradient(135deg, #fb923c, #fdba74); color: #7c2d12; }
    .sentiment-very-negative { background: linear-gradient(135deg, #ef4444, #f87171); color: white; }
    
    .cbt-card {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border-radius: 16px;
        padding: 1rem;
        margin: 0.75rem 0;
        border-left: 5px solid #f59e0b;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.15);
    }
    
    .cbt-card {
        color: #92400e !important;
    }

    .cbt-card * {
        color: #92400e !important;
    }
    
    /* Force text color inside cbt-card - override global white */
    .stApp .cbt-card,
    .stApp .cbt-card * {
        color: #92400e !important;
    }
    
    .distortion-tag {
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        color: #991b1b;
        padding: 0.5rem 1rem;
        border-radius: 12px;
        margin: 0.25rem;
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid #fca5a5;
    }
    
    .action-card {
        background: linear-gradient(135deg, #d1fae5, #a7f3d0);
        border-radius: 12px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #10b981;
        font-size: 0.9rem;
        color: #065f46 !important;
    }

    .action-card * {
        color: #065f46 !important;
    }

    /* Force dark text for encouragement and advice sections */
    .stApp .action-card,
    .stApp .action-card * {
        color: #065f46 !important;
    }

    .cbt-card strong {
        color: #2563eb !important;
    }

    .action-card strong {
        color: #065f46 !important;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #1e293b, #334155);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        border: 1px solid #475569;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7);
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a5b4fc, #c4b5fd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        color: #cbd5e1 !important;
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 0.25rem;
    }
    
    .model-card {
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border-radius: 20px;
        padding: 1.5rem;
        color: white;
        box-shadow: 0 10px 40px rgba(30, 27, 75, 0.3);
    }
    
    .crisis-alert {
        background: linear-gradient(135deg, #dc2626, #ef4444);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 50px rgba(220, 38, 38, 0.35);
        animation: pulse-alert 2s ease-in-out infinite;
    }
    
    @keyframes pulse-alert {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.35) !important;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1b4b 0%, #312e81 50%, #3730a3 100%);
    }
    
    section[data-testid="stSidebar"] .stMarkdown { color: white; }
    
    /* Slider et autres widgets */
    .stSlider > div > div > div {
        background: #6366f1 !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #f1f5f9 !important;
        background: #1e293b !important;
    }
    
    /* Responsive Design - Media Queries */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2rem !important;
        }
        
        .hero-subtitle {
            font-size: 1rem !important;
        }
        
        .user-bubble, .bot-bubble {
            margin-left: 0 !important;
            margin-right: 0 !important;
            font-size: 0.9rem !important;
        }
        
        .stat-card {
            padding: 1rem !important;
        }
        
        .stat-value {
            font-size: 1.5rem !important;
        }
    }
    
    @media (max-width: 480px) {
        .hero-title {
            font-size: 1.5rem !important;
        }
        
        .hero-badges {
            flex-direction: column !important;
        }
        
        .stButton > button {
            font-size: 0.85rem !important;
            padding: 0.6rem 1rem !important;
        }
    }
    
    /* Message de bienvenue */
    .welcome-container {
        background: linear-gradient(135deg, #1e293b, #334155);
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        border: 1px solid #475569;
    }
    
    .welcome-container h3 {
        color: #ffffff !important;
    }
    
    .welcome-container p {
        color: #cbd5e1 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# INITIALISATION SESSION STATE
# ============================================================

@st.cache_resource
def load_models():
    """Charge les modèles une seule fois - Approche 3 avec Gemini"""
    # Utiliser le chatbot approche 3 qui intègre Gemini
    chatbot = WellbeingChatbot(
        user_id='streamlit_user',
        use_gemini=True,  # ✅ Gemini activé
        gemini_api_key='AIzaSyA_KawZtJbvfRP_mtL4glFPIMWsFxGgi68'
    )
    
    analyzer = chatbot.analyzer
    tracker = chatbot.tracker
    generator = chatbot.generator
    gemini = chatbot.gemini
    
    return analyzer, tracker, generator, gemini

def init_session_state():
    """Initialise les variables de session"""
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.messages = []
        st.session_state.mood_history = []
        st.session_state.session_start = datetime.now()
        
        with st.spinner("🔧 Chargement du modèle BERT + Gemini API..."):
            st.session_state.analyzer, st.session_state.tracker, st.session_state.generator, st.session_state.gemini = load_models()

init_session_state()

# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================

def get_sentiment_class(sentiment):
    mapping = {
        'très positif': 'sentiment-very-positive',
        'positif': 'sentiment-positive',
        'neutre': 'sentiment-neutral',
        'négatif': 'sentiment-negative',
        'très négatif': 'sentiment-very-negative'
    }
    return mapping.get(sentiment, 'sentiment-neutral')

def get_sentiment_emoji(sentiment):
    emojis = {
        'très positif': '🌟',
        'positif': '😊',
        'neutre': '😐',
        'négatif': '😔',
        'très négatif': '😢'
    }
    return emojis.get(sentiment, '😐')

def get_mood_score(sentiment):
    scores = {
        'très positif': 1.0,
        'positif': 0.5,
        'neutre': 0.0,
        'négatif': -0.5,
        'negatif': -0.5,  # Version sans accent
        'très négatif': -1.0,
        'tres negatif': -1.0  # Version sans accent
    }
    return scores.get(sentiment, 0.0)

def generate_response_with_gemini(sentiment_result, phrase, mood_trend):
    """Génère une réponse courte avec Gemini (fallback sur templates)"""
    # Essayer Gemini d'abord
    if st.session_state.gemini:
        try:
            gemini_result = st.session_state.gemini.generate_response(
                user_message=phrase,
                sentiment=sentiment_result['sentiment'],
                sentiment_detail=sentiment_result['sentiment_detail'],
                confidence=sentiment_result['confidence'],
                mood_trend=mood_trend,
                conversation_history=[]
            )
            
            # Merger avec conseils et encouragements des templates
            template_response = st.session_state.generator.generate_response(
                sentiment=sentiment_result['sentiment'],
                sentiment_detail=sentiment_result['sentiment_detail'],
                confidence=sentiment_result['confidence'],
                text=phrase,
                mood_trend=mood_trend
            )
            
            # Raccourcir la réponse principale (2 phrases max)
            main_resp = gemini_result.get('response', 'Je suis là pour toi.')
            parts = [p.strip() for p in main_resp.split('.') if p.strip()]
            short_main = '. '.join(parts[:2]) + ('.' if parts[:2] else '')

            # Limiter conseils et encouragement
            advice_short = (template_response.get('advice', []) or [])[:2]
            encouragement_short = (template_response.get('encouragement', '') or '')
            if len(encouragement_short) > 120:
                encouragement_short = encouragement_short[:117] + '...'

            response = {
                'main_response': short_main,
                'advice': advice_short,
                'encouragement': encouragement_short,
                'distortions_detected': template_response.get('distortions_detected', 0),
                'distortions_list': template_response.get('distortions_list', []),
                'behavioral_actions': template_response.get('behavioral_actions', []),
                'emergency_resources': template_response.get('emergency_resources', []),
                'is_crisis': gemini_result.get('is_crisis', False),
                'gemini_used': True
            }
            return response
        except Exception as e:
            print(f"⚠️ Gemini échoué, fallback sur templates: {e}")
    
    # Fallback sur templates
    t_resp = st.session_state.generator.generate_response(
            sentiment=sentiment_result['sentiment'],
            sentiment_detail=sentiment_result['sentiment_detail'],
            confidence=sentiment_result['confidence'],
            text=phrase,
            mood_trend=mood_trend
        )
    # Raccourcir aussi le fallback
    main_f = t_resp.get('main_response', 'Je suis là pour toi.')
    parts = [p.strip() for p in main_f.split('.') if p.strip()]
    t_resp['main_response'] = '. '.join(parts[:2]) + ('.' if parts[:2] else '')
    t_resp['advice'] = (t_resp.get('advice', []) or [])[:2]
    enc = t_resp.get('encouragement', '') or ''
    if len(enc) > 120:
        enc = enc[:117] + '...'
    t_resp['encouragement'] = enc
    return t_resp

# ============================================================
# HEADER HERO
# ============================================================

st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">🧠 Chatbot Bien-être IA</h1>
    <p class="hero-subtitle">Intelligence Artificielle au service de votre bien-être mental</p>
    <div class="hero-badges">
        <span class="hero-badge">🎯 BERT Fine-tuné</span>
        <span class="hero-badge">📊 85% Précision</span>
        <span class="hero-badge">🧠 CBT Intégré</span>
        <span class="hero-badge">💡 Actions Concrètes</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LAYOUT PRINCIPAL
# ============================================================

col_main, col_side = st.columns([2, 1])

# ============================================================
# COLONNE PRINCIPALE - CHAT
# ============================================================

with col_main:
    st.markdown("### 💬 Conversation avec l'IA")
    
    # Messages Container
    chat_container = st.container()
    
    with chat_container:
        if not st.session_state.messages:
            st.markdown("""
            <div class="welcome-container">
                <div style="font-size: 4rem; margin-bottom: 1rem;">💭</div>
                <h3 style="color: #ffffff; margin-bottom: 0.5rem;">Bienvenue !</h3>
                <p style="color: #cbd5e1; font-size: 1.1rem;">Comment te sens-tu aujourd'hui ? Je suis là pour t'écouter.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in st.session_state.messages:
                if msg['role'] == 'user':
                    st.markdown(f"""
                    <div class="user-bubble">
                        <strong>👤 Toi</strong> <span style="font-size: 0.75rem; opacity: 0.8;">{msg.get('time', '')}</span><br>
                        {msg['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    sentiment = msg.get('sentiment', 'neutre')
                    sentiment_class = get_sentiment_class(sentiment)
                    emoji = get_sentiment_emoji(sentiment)
                    
                    st.markdown(f"""
                    <div class="bot-bubble">
                        <div style="margin-bottom: 0.5rem;">
                            <strong>🤖 Chatbot IA</strong>
                            <span class="sentiment-tag {sentiment_class}">{emoji} {sentiment}</span>
                            <span style="font-size: 0.75rem; color: #94a3b8;">{msg.get('confidence', 0):.0%}</span>
                        </div>
                        {msg['content']}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if msg.get('encouragement'):
                        st.markdown(f"""
                        <div class="cbt-card" style="border-color:#2563eb;">
                            <strong style="color:#2563eb;">💪 Encouragement</strong><br>
                            {msg['encouragement']}
                        </div>
                        """, unsafe_allow_html=True)

                    if msg.get('advice'):
                        advice_html = "".join([f"<div class='action-card'>💡 {a}</div>" for a in msg['advice'][:5]])
                        st.markdown(f"<div style='margin-top:0.25rem;'>{advice_html}</div>", unsafe_allow_html=True)

                    if msg.get('emergency'):
                        emergency_html = "".join([f"<div class='cbt-card' style='border-color:#b91c1c;color:#b91c1c;'>🚨 {e}</div>" for e in msg['emergency'][:3]])
                        st.markdown(emergency_html, unsafe_allow_html=True)

                    if msg.get('distortions') or msg.get('distortions_count', 0) > 0:
                        # Sécuriser: accepter liste ou entier
                        dist_list = msg.get('distortions', [])
                        dist_count = msg.get('distortions_count', 0)
                        if isinstance(dist_list, int):
                            dist_count = dist_list
                            dist_list = []
                        if not dist_count:
                            dist_count = len(dist_list)
                        # Construire HTML: tags si noms disponibles, sinon badge de nombre détecté
                        if dist_list:
                            distortions_html = " ".join([f'<span class="distortion-tag">⚠️ {d}</span>' for d in dist_list])
                        else:
                            distortions_html = f'<span class="distortion-tag">⚠️ {dist_count} détectée(s)</span>'
                        st.markdown(f"""
                        <div class="cbt-card">
                            <strong style="color: #92400e;">💭 Distorsions Cognitives Détectées</strong><br>
                            {distortions_html}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if msg.get('actions'):
                        actions_html = "".join([f'<div class="action-card">💡 {a}</div>' for a in msg['actions'][:3]])
                        st.markdown(f"<div>{actions_html}</div>", unsafe_allow_html=True)
    
    # Quick Actions - Responsive
    st.markdown("#### 💡 Suggestions rapides")
    # Adapter le nombre de colonnes selon la largeur d'écran
    # Desktop: 4 colonnes, Tablet: 2 colonnes, Mobile: 1 colonne
    quick_cols = st.columns([1, 1, 1, 1])  # Desktop
    quick_phrases = ["Je me sens triste", "Je suis stressé", "Ça va bien !", "J'ai besoin d'aide"]
    
    for i, phrase in enumerate(quick_phrases):
        with quick_cols[i]:
            if st.button(phrase, key=f"quick_{i}", use_container_width=True):
                # Envoyer directement le message
                current_time = datetime.now().strftime("%H:%M")
                
                # Ajouter message utilisateur
                st.session_state.messages.append({
                    'role': 'user',
                    'content': phrase,
                    'time': current_time
                })
                
                # Traiter la réponse
                sentiment_result = st.session_state.analyzer.analyze(phrase)
                st.session_state.tracker.add_mood(
                    text=phrase,
                    sentiment=sentiment_result['sentiment'],
                    confidence=sentiment_result['confidence']
                )
                
                mood_trend = st.session_state.tracker.get_trend(7)
                response = generate_response_with_gemini(
                    sentiment_result=sentiment_result,
                    phrase=phrase,
                    mood_trend=mood_trend
                )
                
                # Ajouter réponse bot
                st.session_state.messages.append({
                    'role': 'bot',
                    'content': response.get('main_response', 'Je suis là pour toi.'),
                    'sentiment': sentiment_result['sentiment_detail'],
                    'confidence': sentiment_result['confidence'],
                    'gemini_used': response.get('gemini_used', False),
                    'distortions': response.get('distortions_list', []),
                    'distortions_count': response.get('distortions_detected', 0),
                    'actions': response.get('behavioral_actions', []),
                    'advice': response.get('advice', []),
                    'encouragement': response.get('encouragement', ''),
                    'emergency': response.get('emergency_resources', []),
                    'time': current_time
                })
                
                st.session_state.mood_history.append({
                    'timestamp': datetime.now(),
                    'sentiment': sentiment_result['sentiment_detail'],
                    'score': get_mood_score(sentiment_result['sentiment_detail']),
                    'confidence': sentiment_result['confidence']
                })
                
                # Rafraîchir l'interface
                st.rerun()
    
    # Input Area - Barre de chat améliorée
    # Utiliser un formulaire pour permettre l'envoi avec Enter
    with st.form(key="chat_form", clear_on_submit=True, border=False):
        col_input, col_btn = st.columns([6, 1])
        
        default_val = st.session_state.get('pending_input', '')
        if 'pending_input' in st.session_state:
            del st.session_state.pending_input
        
        with col_input:
            user_input = st.text_input(
                "Message",
                value=default_val,
                placeholder="💭 Exprime-toi librement... (Appuie sur Entrée pour envoyer)",
                label_visibility="collapsed",
                key="user_input_main"
            )
        
        with col_btn:
            send_btn = st.form_submit_button("📤", use_container_width=True)
    
    # Traitement du message (soit bouton, soit Enter)
    if send_btn and user_input:
        current_time = datetime.now().strftime("%H:%M")
        
        st.session_state.messages.append({
            'role': 'user',
            'content': user_input,
            'time': current_time
        })
        
        with st.spinner("🔍 Analyse en cours..."):
            sentiment_result = st.session_state.analyzer.analyze(user_input)
            
            st.session_state.tracker.add_mood(
                text=user_input,
                sentiment=sentiment_result['sentiment'],
                confidence=sentiment_result['confidence']
            )
            
            mood_trend = st.session_state.tracker.get_trend(7)
            response = generate_response_with_gemini(
                sentiment_result=sentiment_result,
                phrase=user_input,
                mood_trend=mood_trend
            )
            
            st.session_state.messages.append({
                'role': 'bot',
                'content': response.get('main_response', 'Je suis là pour toi.'),
                'sentiment': sentiment_result['sentiment_detail'],
                'confidence': sentiment_result['confidence'],
                'gemini_used': response.get('gemini_used', False),
                'distortions': response.get('distortions_list', []),
                'distortions_count': response.get('distortions_detected', 0),
                'actions': response.get('behavioral_actions', []),
                'advice': response.get('advice', []),
                'encouragement': response.get('encouragement', ''),
                'emergency': response.get('emergency_resources', []),
                'time': current_time
            })
            
            st.session_state.mood_history.append({
                'timestamp': datetime.now(),
                'sentiment': sentiment_result['sentiment_detail'],
                'score': get_mood_score(sentiment_result['sentiment_detail']),
                'confidence': sentiment_result['confidence']
            })
            
            if response.get('is_crisis'):
                st.markdown("""
                <div class="crisis-alert">
                    <h2>⚠️ Message Important</h2>
                    <p>Si tu traverses une période très difficile:</p>
                    <p style="font-size: 1.5rem;"><strong>📞 SOS Amitié: 09 72 39 40 50</strong></p>
                    <p>🆘 Urgence: 112</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.rerun()

# ============================================================
# COLONNE STATS & VISUALISATIONS
# ============================================================

with col_side:
    # Refresh Button
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        if st.button("🔄 Rafraîchir", key="refresh"):
            st.session_state.tracker.load_history()
            st.rerun()
    with col_r2:
        if st.button("🗑️ Effacer", key="clear"):
            # Effacer session + historique complet
            st.session_state.messages = []
            st.session_state.mood_history = []
            # Effacer le fichier JSON pour remettre à zéro le total
            st.session_state.tracker.mood_history = []
            st.session_state.tracker.save_history()
            st.rerun()
    
    st.markdown("### 📊 Statistiques")
    
    stats = st.session_state.tracker.get_statistics()
    total_msgs = stats.get('total_messages', 0)
    avg_mood = stats.get('mean_score', 0)  # Corrigé: mean_score au lieu de average_mood
    session_msgs = len([m for m in st.session_state.messages if m['role'] == 'user'])
    # CBT Count: Compter messages avec distorsions détectées
    cbt_count = sum(1 for m in st.session_state.messages 
                    if m.get('role') == 'bot' and (
                        m.get('distortions') or 
                        m.get('distortions_detected')
                    ))
    
    # Responsive columns pour stats
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 1.5rem;">💬</div>
            <div class="stat-value">{session_msgs}</div>
            <div class="stat-label">Session</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        mood_emoji = "😊" if avg_mood > 0.2 else "😐" if avg_mood > -0.2 else "😔"
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 1.5rem;">{mood_emoji}</div>
            <div class="stat-value">{avg_mood:.1f}</div>
            <div class="stat-label">Humeur</div>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 1.5rem;">📈</div>
            <div class="stat-value">{total_msgs}</div>
            <div class="stat-label">Total</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄", key="refresh_total", help="Rafraîchir le total"):
            st.session_state.tracker.load_history()
            st.rerun()
    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 1.5rem;">🧠</div>
            <div class="stat-value">{cbt_count}</div>
            <div class="stat-label">CBT</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Évolution de l'Humeur
    if st.session_state.mood_history:
        st.markdown("### 📈 Évolution")
        
        fig_mood = go.Figure()
        times = [m['timestamp'] for m in st.session_state.mood_history]
        scores = [m['score'] for m in st.session_state.mood_history]
        
        fig_mood.add_trace(go.Scatter(
            x=times, y=scores,
            mode='lines+markers',
            line=dict(color='#6366f1', width=3, shape='spline'),
            marker=dict(size=10, color='#8b5cf6'),
            fill='tozeroy',
            fillcolor='rgba(99, 102, 241, 0.1)'
        ))
        
        fig_mood.add_hline(y=0, line_dash="dash", line_color="#94a3b8", opacity=0.5)
        
        fig_mood.update_layout(
            height=200,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)', range=[-1.2, 1.2], tickvals=[-1, 0, 1], ticktext=['😢', '😐', '😊']),
            showlegend=False
        )
        
        st.plotly_chart(fig_mood, use_container_width=True)
    
    # Distribution
    if st.session_state.messages:
        st.markdown("### 🎯 Distribution")
        
        sentiments = [m.get('sentiment', 'neutre') for m in st.session_state.messages if m['role'] == 'bot']
        
        if sentiments:
            sentiment_counts = Counter(sentiments)
            colors_map = {
                'très positif': '#10b981', 'positif': '#34d399',
                'neutre': '#94a3b8', 'négatif': '#fb923c', 'très négatif': '#ef4444'
            }
            
            fig_pie = go.Figure(data=[go.Pie(
                labels=list(sentiment_counts.keys()),
                values=list(sentiment_counts.values()),
                hole=0.5,
                marker_colors=[colors_map.get(s, '#94a3b8') for s in sentiment_counts.keys()]
            )])
            
            fig_pie.update_layout(
                height=180,
                margin=dict(l=10, r=10, t=10, b=10),
                showlegend=True,
                legend=dict(orientation="h", y=-0.2, font=dict(size=9))
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
    
    # Jauge Confiance
    if st.session_state.mood_history:
        st.markdown("### 🎚️ Confiance")
        
        avg_conf = sum(m['confidence'] for m in st.session_state.mood_history) / len(st.session_state.mood_history)
        
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=avg_conf * 100,
            number={'suffix': '%', 'font': {'size': 20, 'color': '#6366f1'}},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': '#6366f1'},
                'steps': [
                    {'range': [0, 33], 'color': '#fee2e2'},
                    {'range': [33, 66], 'color': '#fef3c7'},
                    {'range': [66, 100], 'color': '#d1fae5'}
                ]
            }
        ))
        
        fig_gauge.update_layout(height=150, margin=dict(l=20, r=20, t=20, b=10), paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    # Modèle Info
    st.markdown("### 🤖 Modèle")
    st.markdown("""
    <div class="model-card">
        <strong style="font-size: 1.1rem;">🧠 BERT Fine-tuné</strong>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-top: 1rem;">
            <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; border-radius: 8px; text-align: center;">
                <div style="font-weight: 700;">110M</div>
                <div style="font-size: 0.7rem; opacity: 0.8;">Params</div>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; border-radius: 8px; text-align: center;">
                <div style="font-weight: 700;">85%</div>
                <div style="font-size: 0.7rem; opacity: 0.8;">Précision</div>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; border-radius: 8px; text-align: center;">
                <div style="font-weight: 700;">5</div>
                <div style="font-size: 0.7rem; opacity: 0.8;">Distorsions</div>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; border-radius: 8px; text-align: center;">
                <div style="font-weight: 700;">CBT</div>
                <div style="font-size: 0.7rem; opacity: 0.8;">Intégré ✓</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 1rem;">
        <div style="font-size: 3rem;">🧘</div>
        <h2 style="color: white; margin: 0;">Bien-être IA</h2>
        <p style="color: rgba(255,255,255,0.7); font-size: 0.85rem;">Ton assistant personnel</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📜 Historique")
    history_days = st.slider("Jours", 1, 30, 7)
    
    if st.button("📥 Charger historique"):
        # Utiliser mood_history directement au lieu de get_mood_history()
        history = st.session_state.tracker.mood_history if st.session_state.tracker.mood_history else []
        if history:
            st.success(f"✅ {len(history)} messages")
        else:
            st.info("Pas d'historique")
    
    st.markdown("---")
    
    with st.expander("🧠 Guide CBT"):
        st.markdown("""
        **Distorsions Cognitives:**
        
        1. **Catastrophisation** 🌪️
        2. **Tout-ou-Rien** ⚫⚪
        3. **Surgénéralisation** 🔄
        4. **Lecture de Pensées** 🔮
        5. **Raisonnement Émotionnel** 💭
        """)
    
    st.markdown("---")
    
    st.error("""
    **🆘 Aide d'Urgence:**
    
    📞 SOS Amitié: 09 72 39 40 50
    
    🆘 Urgence: 112
    """)
    
    st.markdown("---")
    
    if st.button("💾 Exporter"):
        if st.session_state.messages:
            export_data = json.dumps(st.session_state.messages, indent=2, default=str, ensure_ascii=False)
            st.download_button("📥 Télécharger", export_data, f"conversation_{datetime.now().strftime('%Y%m%d')}.json", "application/json")
    
    st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.5); font-size: 0.7rem; padding: 1rem;">
        <p>ENSA Berrechid © 2026</p>
        <p>v2.0 BERT Fine-tuné + CBT</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #64748b; font-size: 0.85rem;">
    🧠 Chatbot Bien-être IA | BERT Fine-tuné + CBT | ⚠️ Outil de bien-être, pas médical
</div>
""", unsafe_allow_html=True)
