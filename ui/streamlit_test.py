import streamlit as st
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from approach3.chatbot import WellbeingChatbot

# Configuration de la page
st.set_page_config(
    page_title="🧠 Chatbot Bien-être IA",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Chatbot de Bien-être IA")

# Initialiser le chatbot
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = WellbeingChatbot()

# Messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Interface
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_input("💬 Dis-moi ce que tu ressens:", key="user_input")

with col2:
    if st.button("📤 Envoyer"):
        if user_input.strip():
            # Analyser
            response = st.session_state.chatbot.process_message(user_input)
            
            # Ajouter au historique
            st.session_state.messages.append({
                'role': 'user',
                'content': user_input,
                'sentiment': response['sentiment_detail']
            })
            st.session_state.messages.append({
                'role': 'assistant',
                'content': response['main_response'],
                'confidence': response.get('confidence', 0)
            })

# Afficher les messages
st.markdown("---")
for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"**👤 Toi:** {msg['content']}")
        st.markdown(f"*Sentiment: {msg['sentiment']}*")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")
        st.markdown(f"*Confiance: {msg.get('confidence', 0):.0%}*")
    st.markdown("---")
