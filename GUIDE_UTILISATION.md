# 🤖 Guide d'Utilisation du Chatbot de Bien-être

## 🚀 Comment lancer le chatbot

### Méthode 1 : Double-clic (Facile)
1. Double-cliquez sur le fichier `run_chatbot.bat`
2. Le chatbot se lance automatiquement !

### Méthode 2 : Terminal
```bash
cd "c:\Users\LOQ\Documents\Chatbot bien-être\src\approach1"
..\..\venv\Scripts\python.exe chatbot.py
```

---

## 💬 Comment utiliser le chatbot

### Conversation normale
Tape simplement ce que tu ressens :
```
💬 Vous : Je suis heureux aujourd'hui !
```

Le chatbot va :
1. ✅ Analyser ton sentiment
2. ✅ Enregistrer dans l'historique
3. ✅ Te répondre avec empathie
4. ✅ Afficher un dashboard visuel
5. ✅ Donner des conseils personnalisés

---

## 📝 Commandes spéciales

| Commande | Description |
|----------|-------------|
| `/stats` | Affiche tes statistiques d'humeur complètes |
| `/history` | Montre l'historique de cette conversation |
| `/help` | Affiche l'aide |
| `/clear` | Efface l'écran |
| `/quit` | Quitte le chatbot |

---

## 💡 Exemples de messages

### Messages positifs
- "Je me sens super bien !"
- "J'ai passé une excellente journée"
- "Je suis tellement heureux !"

### Messages neutres
- "Journée normale"
- "Rien de spécial"
- "Ça va"

### Messages négatifs
- "Je me sens triste"
- "J'ai besoin de parler"
- "Journée difficile"

---

## 🎨 Ce que le chatbot fait

### 1. Analyse de sentiment (BERT)
```
"Je suis heureux !" → POSITIF (85% confiance)
```

### 2. Suivi d'humeur dans le temps
```
Tendance 7 jours : 📈 +0.25 (amélioration)
```

### 3. Réponses empathiques
```
💬 C'est génial ! Continue comme ça ! 🌟

💡 Suggestions :
   • Partage ta joie avec tes proches
   • Fais une activité créative
```

### 4. Visualisation
```
╔═══════════════════════════════════════════════════╗
║        😄 TABLEAU DE BORD D'HUMEUR 😄            ║
╠═══════════════════════════════════════════════════╣
║  État actuel : 🟢  TRÈS POSITIF  🟢           ║
║  Niveau : 😄 [████████████████] 85%              ║
║  Tendance : 📈 Amélioration !                   ║
╚═══════════════════════════════════════════════════╝
```

---

## 🆘 Détection de crise

Si tu mentionnes des pensées suicidaires, le chatbot :
- ⚠️ Détecte automatiquement
- 🆘 Affiche les numéros d'urgence
- 💙 Te guide vers l'aide

**Numéros d'urgence** :
- 🇫🇷 France : 3114 (prévention suicide)
- 🇲🇦 Maroc : 0801000180 (SOS Maroc)
- 📞 SOS Amitié : 09 72 39 40 50

---

## 📊 Statistiques

Tape `/stats` pour voir :
- 📈 Score moyen d'humeur
- 📊 Distribution des sentiments (% positif/négatif/neutre)
- 📅 Nombre de jours suivis
- 🎯 Tendances et patterns

---

## 💾 Sauvegarde des données

Toutes tes conversations sont sauvegardées dans :
```
data/mood_history.json
```

Tu peux :
- ✅ Fermer le chatbot sans perdre tes données
- ✅ Voir ton historique à long terme
- ✅ Suivre ton évolution sur plusieurs jours/semaines

---

## 🎯 Conseils d'utilisation

### Pour de meilleurs résultats :

1. **Sois honnête** : Le chatbot est là pour toi, sans jugement
2. **Utilise-le régulièrement** : Plus tu l'utilises, meilleur est le suivi
3. **Explore les stats** : Tape `/stats` pour voir ton évolution
4. **Prends les conseils au sérieux** : Les activités suggérées peuvent vraiment aider

### Ne remplace pas :
- ⚠️ Un professionnel de santé mentale
- ⚠️ Un traitement médical
- ⚠️ Une aide d'urgence si nécessaire

**Le chatbot est un outil de soutien, pas un substitut à une aide professionnelle.**

---

## 🐛 En cas de problème

### Le chatbot ne se lance pas
1. Vérifie que l'environnement virtuel est activé
2. Réinstalle les dépendances : `pip install -r requirements.txt`

### Erreur de module
```bash
cd "c:\Users\LOQ\Documents\Chatbot bien-être\src\approach1"
..\..\venv\Scripts\python.exe chatbot.py
```

### Données corrompues
Supprime `data/mood_history.json` et relance

---

## 🎓 Projet académique

**Créé par** : Étudiant ENSA Berrechid  
**Module** : Programmation Python et IA  
**Date** : Décembre 2024

**Technologies** :
- Python 3.13
- PyTorch 2.9
- Transformers (BERT)
- Analyse de sentiment
- NLP multilingue

---

## 🌈 Prends soin de toi ! 💙

Le chatbot est là pour t'accompagner dans ton bien-être.  
N'hésite pas à l'utiliser quand tu en as besoin ! 😊

**Bon chat ! 🤖💬**
