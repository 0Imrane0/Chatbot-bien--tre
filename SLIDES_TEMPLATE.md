# 📊 SLIDES POUR LA PRÉSENTATION

> **Template pour créer tes slides PowerPoint/Google Slides**

---

## 🎨 STYLE GÉNÉRAL

**Thème recommandé :** Sombre/Professionnel  
**Police :** Montserrat, Poppins, ou Roboto  
**Couleurs :**
- 🔵 Bleu : `#3B82F6` (primaire)
- 🟣 Violet : `#8B5CF6` (accent)
- ⚫ Fond : `#1E1E2E` (sombre)
- ⚪ Texte : `#F8FAFC` (blanc cassé)

---

## 📑 SLIDE 1 : PAGE DE TITRE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    🤖 CHATBOT DE BIEN-ÊTRE IA
    
    Intelligence Artificielle + Psychologie
    BERT Fine-tuning + Thérapie Cognitive

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Étudiant : [TON NOM]
    Encadrant : [NOM PROF]
    
    ENSA Berrechid
    Janvier 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Image suggérée :** Logo d'un chatbot ou cerveau + circuits

---

## 📑 SLIDE 2 : CONTEXTE & PROBLÈME

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 CONTEXTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• 1 personne sur 4 souffre de troubles mentaux
• Besoin d'outils d'accompagnement accessibles
• Les chatbots existants sont limités

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ❌ PROBLÈME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ Réponses génériques et pré-définies
❌ Pas de compréhension émotionnelle
❌ Aucune aide psychologique concrète
❌ Pas de suivi personnalisé
```

**Image suggérée :** Chatbot basique avec bulle de texte générique

---

## 📑 SLIDE 3 : SOLUTION PROPOSÉE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ✅ MA SOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────────────────────────────┐
│  1️⃣ ANALYSE DE SENTIMENT          │
│  BERT Fine-tuning (110M paramètres)│
│  → 85% de précision                │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  2️⃣ MODULE CBT                     │
│  Détection de distorsions cognitives│
│  → Questions socratiques           │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  3️⃣ INTERFACE WEB MODERNE         │
│  Streamlit + Visualisations         │
│  → Suivi de l'humeur en temps réel │
└────────────────────────────────────┘
```

**Image suggérée :** Schéma des 3 blocs avec flèches

---

## 📑 SLIDE 4 : ARCHITECTURE TECHNIQUE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🏗️ ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

      Utilisateur
           ↓
    ┌──────────────────┐
    │   Streamlit UI   │
    └──────────────────┘
           ↓
    ┌──────────────────┐
    │  BERT Fine-tuné  │ → Sentiment Analysis
    │  (110M params)   │
    └──────────────────┘
           ↓
    ┌──────────────────┐
    │   CBT Engine     │ → Distortion Detection
    └──────────────────┘
           ↓
    ┌──────────────────┐
    │Response Generator│ → Actions + Conseils
    └──────────────────┘
```

**Image suggérée :** Diagramme avec flèches et icônes

---

## 📑 SLIDE 5 : BERT FINE-TUNING

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 BERT FINE-TUNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Qu'est-ce que BERT ?
• Bidirectional Encoder Representations
• 110 millions de paramètres
• Pré-entraîné sur Wikipedia + BookCorpus

📌 Mon adaptation :
• Dataset : 500+ exemples bien-être
• 5 classes : très négatif → très positif
• 3 epochs d'entraînement
• Framework : PyTorch + Hugging Face

📌 Résultat :
✅ 85% de précision
✅ Temps d'inférence : ~200ms
```

**Image suggérée :** Logo BERT + schéma du modèle

---

## 📑 SLIDE 6 : COMPARAISON DES APPROCHES

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📊 RÉSULTATS COMPARATIFS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────┐
│ APPROCHE 1 : Feature Extraction     │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  82%          │
│                                     │
│ • BERT gelé (pas d'entraînement)    │
│ • Rapide à développer               │
│ • Moins précis                      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ APPROCHE 3 : Fine-tuning ⭐         │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░  85%          │
│                                     │
│ • BERT entraîné complètement        │
│ • Meilleure compréhension           │
│ • +3% de précision                  │
└─────────────────────────────────────┘

    → Gain de 3% = moins d'erreurs
```

**Image suggérée :** Graphique en barres comparatif

---

## 📑 SLIDE 7 : MODULE CBT

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🧠 MODULE CBT (Thérapie Cognitive)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5 DISTORSIONS DÉTECTÉES :

1️⃣ Catastrophisation
   "Ma vie est fichue" → Penser au pire

2️⃣ Tout-ou-rien
   "Je suis complètement nul" → Noir ou blanc

3️⃣ Surgénéralisation
   "Je rate toujours tout" → Généraliser

4️⃣ Lecture de pensées
   "Il pense que je suis idiot" → Deviner

5️⃣ Raisonnement émotionnel
   "Je me sens nul donc je suis nul" → Émotion = réalité

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ✨ IMPACT CBT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

+782% d'enrichissement des réponses
Questions socratiques + Actions concrètes
```

**Image suggérée :** Icônes pour chaque distorsion

---

## 📑 SLIDE 8 : STACK TECHNIQUE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🛠️ TECHNOLOGIES UTILISÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────┐
│ 🐍 PYTHON 3.13                      │
│    Langage principal                │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 🔥 PYTORCH                          │
│    Framework deep learning          │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 🤗 TRANSFORMERS (Hugging Face)      │
│    Modèles pré-entraînés            │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 🌐 STREAMLIT                        │
│    Interface web interactive        │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 📊 PLOTLY                           │
│    Visualisations interactives      │
└─────────────────────────────────────┘
```

**Image suggérée :** Logos des technologies

---

## 📑 SLIDE 9 : DÉMONSTRATION

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💻 DÉMONSTRATION LIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Cette slide reste affichée pendant la démo]

🔴 CAS 1 : Sentiment négatif
   → Détection de distorsions

🟠 CAS 2 : Anxiété
   → Exercices de respiration

🟢 CAS 3 : Sentiment positif
   → Renforcement positif

📊 Statistiques en temps réel
```

**Note :** Basculer sur l'interface pendant cette partie

---

## 📑 SLIDE 10 : RÉSULTATS DÉTAILLÉS

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📈 RÉSULTATS MESURÉS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────────────┬──────────────┐
│ Métrique             │ Valeur       │
├──────────────────────┼──────────────┤
│ Précision            │ 85%          │
│ Temps d'inférence    │ ~200ms       │
│ Paramètres BERT      │ 110 millions │
│ Classes détectées    │ 5            │
│ Distorsions CBT      │ 5 types      │
│ Enrichissement       │ +782%        │
└──────────────────────┴──────────────┘

✅ Performances optimales
✅ Temps réel assuré
✅ Intégration CBT réussie
```

**Image suggérée :** Tableau avec checkmarks verts

---

## 📑 SLIDE 11 : INTERFACE UTILISATEUR

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎨 INTERFACE WEB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ FONCTIONNALITÉS :

💬 Zone de chat intuitive
   → Messages utilisateur + réponses bot

📊 Statistiques en temps réel
   → Session, Humeur, Total, CBT

📈 Graphiques interactifs
   → Évolution humeur (7 jours)
   → Distribution sentiments
   → Jauge de confiance

🎨 Design moderne
   → Dark theme (réduit fatigue oculaire)
   → Responsive design
   → Animations fluides
```

**Image suggérée :** Screenshots de l'interface

---

## 📑 SLIDE 12 : COMPARAISON AVANT/APRÈS CBT

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔄 IMPACT DU MODULE CBT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ SANS CBT (chatbot classique) :

User: "Je suis complètement nul"
Bot:  "Je comprends que c'est difficile."
      (57 caractères)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ AVEC CBT (mon chatbot) :

User: "Je suis complètement nul"
Bot:  "Je comprends ta frustration. Je remarque 
       une pensée 'tout-ou-rien'. Est-ce vraiment 
       TOUT ou rien ? Peux-tu penser à quelque 
       chose que tu as bien fait récemment ?
       
       Actions : Écris 3 choses positives"
      (245 caractères - +782%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Image suggérée :** Avant/Après côte à côte

---

## 📑 SLIDE 13 : DÉFIS RENCONTRÉS

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ⚠️ DÉFIS & SOLUTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ DÉFI : Entraînement du modèle BERT
   ✅ Solution : Utilisation de GPU + batch optimal

2️⃣ DÉFI : Dataset limité (500 exemples)
   ✅ Solution : Data augmentation + fine-tuning

3️⃣ DÉFI : Détection précise des distorsions CBT
   ✅ Solution : Patterns + règles linguistiques

4️⃣ DÉFI : Interface réactive
   ✅ Solution : Streamlit + cache pour BERT

5️⃣ DÉFI : Modèles trop lourds pour GitHub
   ✅ Solution : Script de téléchargement auto
```

**Image suggérée :** Icônes problème → solution

---

## 📑 SLIDE 14 : PERSPECTIVES

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 PERSPECTIVES D'AMÉLIORATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 COURT TERME (3-6 mois)

• Déploiement sur Azure/AWS
• Support multilingue (CamemBERT)
• Application mobile (React Native)
• Plus de données d'entraînement

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔬 MOYEN TERME (6-12 mois)

• Intégration GPT-4 (réponses génératives)
• Détection de crise suicidaire avancée
• Recommandations personnalisées
• Collaboration avec psychologues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 LONG TERME (1-2 ans)

• Validation clinique
• Partenariat avec établissements santé
• Certification médicale
```

**Image suggérée :** Roadmap timeline

---

## 📑 SLIDE 15 : CONCLUSION

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🎯 CONCLUSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ OBJECTIFS ATTEINTS :

1. Analyse de sentiment avec BERT (85%)
2. Module CBT fonctionnel (5 distorsions)
3. Interface web professionnelle
4. +782% d'enrichissement des réponses

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 APPORTS DU PROJET :

• NLP avancé (fine-tuning BERT)
• Psychologie computationnelle
• Développement full-stack
• Gestion de projet

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   MERCI DE VOTRE ATTENTION ! 🙏
   
   Questions ?
```

**Image suggérée :** Image inspirante ou logo de fin

---

## 📑 SLIDE 16 : QUESTIONS FRÉQUENTES (BACKUP)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ❓ QUESTIONS FRÉQUENTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q: Pourquoi BERT et pas GPT ?
A: BERT est bidirectionnel, meilleur pour 
   la classification de sentiments

Q: Le modèle est-il déployé ?
A: Actuellement local, déploiement cloud prévu

Q: Quel est le dataset utilisé ?
A: 500+ exemples annotés bien-être

Q: Le chatbot remplace-t-il un psy ?
A: Non, c'est un outil de soutien, pas un 
   remplacement de thérapie professionnelle
```

---

## 🎨 CONSEILS DE DESIGN

### Police :
- **Titres :** 36-48pt, Bold
- **Texte :** 18-24pt, Regular
- **Code :** Fira Code ou Consolas

### Animations :
- ✅ Entrée progressive (Fade In)
- ❌ Éviter effets trop flashy

### Images :
- Haute résolution (min 1920x1080)
- Fond transparent si possible
- Icônes cohérentes (Material Design)

---

**Prêt à créer tes slides ! 🎨**
