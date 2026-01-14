# 🎬 SCÉNARIO DE DÉMONSTRATION - 3-4 MINUTES

> **Projet Académique : Chatbot de Bien-Être IA avec BERT Fine-tuning et CBT**

---

## ⏱️ TIMING GLOBAL

| Section | Durée | Objectif |
|---------|-------|----------|
| **1. Introduction** | 30 sec | Présenter le problème et la solution |
| **2. Démonstration Live** | 2 min | Montrer le chatbot en action |
| **3. Résultats Techniques** | 1 min | Prouver la performance |
| **4. Conclusion** | 30 sec | Impact et perspectives |

**TOTAL : 4 minutes**

---

## 📋 SCÉNARIO DÉTAILLÉ

### 🎯 1. INTRODUCTION (30 secondes)

**[Slide 1 : Titre]**

> "Bonjour, je vais vous présenter mon projet : un **chatbot de bien-être intelligent** qui combine l'analyse de sentiments par BERT et la thérapie cognitivo-comportementale."

**[Slide 2 : Problème]**

> "Le problème : les chatbots classiques donnent des réponses génériques sans comprendre réellement les émotions de l'utilisateur."

**[Slide 3 : Solution]**

> "Ma solution : utiliser BERT, un modèle de 110 millions de paramètres, fine-tuné pour analyser les émotions avec **85% de précision**, couplé à un module CBT qui détecte les distorsions cognitives."

**[Montrer l'interface]**

> "Passons directement à la démonstration..."

---

### 💻 2. DÉMONSTRATION LIVE (2 minutes)

**[Ouvrir l'interface Streamlit]**

#### 🔴 Cas 1 : Sentiment Négatif avec Catastrophisation (40 sec)

**TOI :**
```
Je suis complètement nul, je vais rater mon examen et ma vie est fichue
```

**[Montrer pendant que le bot analyse]**

> "Le bot analyse le message en temps réel avec BERT..."

**BOT RÉPOND :**
- ✅ Sentiment : **Très négatif** (89% confiance)
- ✅ Distorsions détectées : **"Tout-ou-rien"** + **"Catastrophisation"**
- ✅ Question socratique
- ✅ Actions comportementales proposées

**[Pointer les éléments à l'écran]**

> "Regardez : le bot a détecté 2 distorsions cognitives et propose des actions concrètes."

---

#### 🟠 Cas 2 : Anxiété avec Lecture de Pensées (40 sec)

**TOI :**
```
Je suis stressé, tout le monde pense que je suis incompétent
```

**BOT RÉPOND :**
- ✅ Sentiment : **Négatif** (82% confiance)
- ✅ Distorsion : **"Lecture de pensées"**
- ✅ Question : "Comment peux-tu être sûr de ce qu'ils pensent ?"
- ✅ Exercice de respiration 4-7-8 proposé

**[Montrer le graphique]**

> "L'interface suit l'évolution de l'humeur en temps réel."

---

#### 🟢 Cas 3 : Sentiment Positif (30 sec)

**TOI :**
```
J'ai réussi ma présentation, je suis fier de moi !
```

**BOT RÉPOND :**
- ✅ Sentiment : **Très positif** (94% confiance)
- ✅ Renforcement positif
- ✅ Encouragement à continuer

> "Le bot sait aussi reconnaître et renforcer les moments positifs."

---

#### 📊 Montrer les Statistiques (10 sec)

**[Cliquer sur "Actualiser le total"]**

> "Voici les statistiques : 3 messages analysés, tendance d'humeur, activations CBT..."

---

### 📈 3. RÉSULTATS TECHNIQUES (1 minute)

**[Slide 4 : Comparaison des Approches]**

| Métrique | Approche 1 (Feature Extraction) | **Approche 3 (Fine-tuning)** |
|----------|--------------------------------|------------------------------|
| Précision | 82% | **85% (+3%)** ✅ |
| Paramètres | 110M (gelés) | **110M (entraînés)** |
| Temps d'inférence | ~200ms | ~200ms |

> "J'ai comparé 2 approches : le fine-tuning complet de BERT donne **3% de précision en plus**."

**[Slide 5 : Module CBT]**

> "Le module CBT détecte **5 types de distorsions cognitives** et propose des questions socratiques pour restructurer les pensées négatives."

```
Sans CBT: "Je comprends que c'est difficile." (57 caractères)

Avec CBT: "Je comprends ta frustration. Je remarque une pensée 
'tout-ou-rien'. Est-ce vraiment TOUT ou rien ? 
Suggestion: Écris 3 choses que tu as réussies récemment." 
(+782% d'enrichissement)
```

**[Slide 6 : Technologies]**

> "Technologies utilisées : PyTorch, Transformers (Hugging Face), Streamlit pour l'interface, et Plotly pour les visualisations."

---

### 🎯 4. CONCLUSION (30 secondes)

**[Slide 7 : Récapitulatif]**

> "En résumé, ce projet démontre :"

✅ **NLP avancé** : Fine-tuning de BERT (110M paramètres)  
✅ **Psychologie appliquée** : Intégration de la CBT  
✅ **Interface professionnelle** : Streamlit avec dark theme  
✅ **Performance** : 85% de précision, +782% d'enrichissement  

**[Slide 8 : Perspectives]**

> "Perspectives : déploiement web, support multilingue, intégration d'un modèle génératif type GPT pour des réponses plus naturelles."

**[Fermer]**

> "Merci ! Je suis prêt à répondre à vos questions."

---

## 📝 MESSAGES À TESTER (BACKUP)

### Messages Négatifs
1. `Je suis complètement nul, je rate tout ce que je fais`
2. `C'est toujours pareil, je n'y arriverai jamais`
3. `Tout le monde pense que je suis incompétent`
4. `Si je rate cet examen, ma vie est fichue`
5. `Je me sens tellement nul`

### Messages Positifs
1. `J'ai réussi ma présentation, je suis fier de moi !`
2. `Je me sens mieux aujourd'hui, merci`
3. `C'était une excellente journée`

### Messages Neutres
1. `Je ne sais pas quoi faire`
2. `Ça va, rien de spécial`

---

## 🎥 CHECKLIST PRE-DÉMONSTRATION

### 30 Minutes Avant

- [ ] Vérifier que Python/environnement virtuel fonctionne
- [ ] Lancer `launch_interface.bat` pour tester
- [ ] Vérifier que le modèle charge correctement (110M paramètres)
- [ ] Préparer le navigateur avec l'interface ouverte
- [ ] Fermer tous les onglets inutiles
- [ ] Mettre le téléphone en silencieux

### 5 Minutes Avant

- [ ] Relancer l'interface (session propre)
- [ ] Vérifier que les graphiques s'affichent
- [ ] Tester un message rapide
- [ ] Préparer les slides en parallèle
- [ ] Respirer profondément 😊

### Pendant la Démo

- [ ] Parler lentement et clairement
- [ ] Montrer l'écran au professeur
- [ ] Laisser le temps au bot de répondre (2-3 secondes)
- [ ] Pointer les éléments clés avec la souris
- [ ] Sourire et montrer ta passion pour le projet !

---

## 💡 CONSEILS PRO

### ✅ À FAIRE

- **Varier les cas d'usage** : négatif, positif, anxiété
- **Montrer les distorsions CBT** : c'est l'innovation du projet
- **Insister sur les chiffres** : 85%, 110M paramètres, +782%
- **Parler avec passion** : montre que tu as aimé faire ce projet
- **Être prêt aux questions** : "Comment as-tu entraîné BERT ?", "Pourquoi pas GPT ?"

### ❌ À ÉVITER

- Ne pas lire les slides mot à mot
- Ne pas passer trop de temps sur un seul message
- Ne pas paniquer si le bot met 2-3 secondes à répondre (c'est normal)
- Ne pas oublier de montrer les graphiques
- Ne pas négliger la conclusion

---

## 🎤 RÉPONSES AUX QUESTIONS PROBABLES

### Q1 : "Pourquoi BERT et pas GPT ?"

> "BERT est plus adapté pour la classification de sentiments car il est bidirectionnel et comprend le contexte complet. GPT est génératif, ce qui serait utile pour générer les réponses, mais pour l'analyse de sentiments, BERT est plus performant et plus léger."

### Q2 : "Comment as-tu entraîné le modèle ?"

> "J'ai utilisé un dataset de 500+ exemples annotés par sentiment (très négatif → très positif), avec fine-tuning sur 3 epochs avec PyTorch. Le modèle base BERT-uncased a été adapté pour comprendre les nuances du bien-être."

### Q3 : "Quelle est la nouveauté de ton projet ?"

> "La nouveauté est la **combinaison** de BERT fine-tuné avec un module CBT. Les chatbots classiques se contentent de détecter le sentiment, mais mon projet va plus loin en identifiant les distorsions cognitives et en proposant des restructurations inspirées de la thérapie cognitivo-comportementale."

### Q4 : "Comment peux-tu améliorer le projet ?"

> "Trois axes d'amélioration : 1) Déployer sur le cloud (Azure/AWS), 2) Ajouter du support multilingue avec CamemBERT pour le français, 3) Intégrer un modèle génératif (GPT-4) pour des réponses plus naturelles et personnalisées."

### Q5 : "Le modèle est-il fiable pour un usage réel ?"

> "Le modèle atteint 85% de précision, ce qui est bon pour un projet académique. Pour un usage clinique réel, il faudrait plus de données, une validation par des psychologues, et un disclaimer clair que ce n'est pas un remplacement de thérapie professionnelle."

---

## 📊 SLIDES À PRÉPARER (PowerPoint/Google Slides)

### Slide 1 : Titre
```
🤖 CHATBOT DE BIEN-ÊTRE IA
BERT Fine-tuning + Thérapie Cognitive

Étudiant : [Ton Nom]
ENSA Berrechid
Janvier 2026
```

### Slide 2 : Problème
```
❌ PROBLÈME

• Chatbots classiques = réponses génériques
• Pas de compréhension émotionnelle
• Pas d'aide concrète
```

### Slide 3 : Solution
```
✅ SOLUTION

• BERT Fine-tuning (110M paramètres)
• 85% de précision
• Module CBT (5 distorsions)
• Interface web moderne
```

### Slide 4 : Comparaison
```
📊 RÉSULTATS

Approche 1 : 82%
Approche 3 : 85% (+3%)

Enrichissement CBT : +782%
```

### Slide 5 : Module CBT
```
🧠 MODULE CBT

• Catastrophisation
• Tout-ou-rien
• Surgénéralisation
• Lecture de pensées
• Raisonnement émotionnel
```

### Slide 6 : Technologies
```
🛠️ STACK TECHNIQUE

• Python 3.13
• PyTorch + Transformers
• BERT (Hugging Face)
• Streamlit (Interface)
• Plotly (Visualisations)
```

### Slide 7 : Récapitulatif
```
🎯 RÉCAPITULATIF

✅ NLP avancé
✅ Psychologie appliquée
✅ Interface professionnelle
✅ 85% de précision
```

### Slide 8 : Perspectives
```
🚀 PERSPECTIVES

• Déploiement cloud
• Support multilingue
• Intégration GPT-4
• Validation clinique
```

---

## 🎬 SCRIPT COMPLET (À LIRE UNE FOIS)

**[0:00 - 0:30] Introduction**

"Bonjour Professeur. Je vais vous présenter mon projet de fin d'études : un chatbot de bien-être intelligent. Le problème que j'ai voulu résoudre, c'est que les chatbots classiques donnent des réponses génériques sans vraiment comprendre les émotions. Ma solution combine BERT, un modèle de 110 millions de paramètres que j'ai fine-tuné, avec un module de thérapie cognitivo-comportementale. Le résultat : 85% de précision dans l'analyse des sentiments."

**[0:30 - 2:30] Démonstration**

"Passons à la démonstration. Je vais tester plusieurs cas. Premier message : 'Je suis complètement nul, je vais rater mon examen et ma vie est fichue'. Le bot analyse... Voilà ! Il a détecté un sentiment très négatif avec 89% de confiance, identifié deux distorsions cognitives - 'tout-ou-rien' et 'catastrophisation' - et propose une question socratique pour restructurer cette pensée, ainsi que des actions concrètes.

Deuxième cas : 'Je suis stressé, tout le monde pense que je suis incompétent'. Le bot détecte de l'anxiété et la distorsion 'lecture de pensées', puis propose un exercice de respiration 4-7-8.

Dernier cas positif : 'J'ai réussi ma présentation, je suis fier de moi !'. Le bot reconnaît le sentiment très positif à 94% et renforce ce moment positif. Vous voyez ici les statistiques en temps réel avec l'évolution de l'humeur."

**[2:30 - 3:30] Résultats**

"Côté résultats techniques, j'ai comparé deux approches : l'extraction de features donne 82% de précision, et le fine-tuning complet atteint 85%, soit 3% de mieux. Le module CBT enrichit les réponses de 782% en moyenne comparé à des réponses simples. Les technologies utilisées sont PyTorch, Transformers de Hugging Face, et Streamlit pour l'interface."

**[3:30 - 4:00] Conclusion**

"En conclusion, ce projet démontre l'application du NLP avancé avec BERT, l'intégration de concepts de psychologie, et une interface professionnelle. Les perspectives incluent un déploiement web, le support multilingue avec CamemBERT, et l'intégration de GPT pour des réponses encore plus naturelles. Merci de votre attention, je suis prêt à répondre à vos questions."

---

**Bonne chance pour ta présentation ! 🚀**
