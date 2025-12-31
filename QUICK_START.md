# 🚀 GUIDE DE LANCEMENT RAPIDE

## 🎯 Lancement en Un Clic

Tu as maintenant **6 fichiers .bat** pour lancer le chatbot facilement :

### 1. 🌐 **launch_streamlit.bat** (RECOMMANDÉ)
```
Double-clic sur ce fichier → Interface web s'ouvre automatiquement
```
- ✅ Active automatiquement l'environnement virtuel
- ✅ Lance l'interface Streamlit dans le navigateur
- ✅ Belle interface graphique avec graphiques

**Utilisation :**
1. Double-clic sur `launch_streamlit.bat`
2. Attendre quelques secondes
3. Le navigateur s'ouvre automatiquement
4. Commence à chatter ! 💬

---

### 2. 💻 **launch_console.bat**
```
Double-clic → Chatbot dans le terminal
```
- ✅ Mode terminal classique
- ✅ Rapide et léger
- ✅ Commandes spéciales (/stats, /help, etc.)

---

### 3. 🎯 **launch_menu.bat**
```
Double-clic → Menu avec choix d'options
```
- ✅ Menu interactif
- ✅ Choisir l'interface (console ou web)
- ✅ Accès aux démos et options

---

### 4. 📊 **launch_demo.bat**
```
Double-clic → Démonstration automatique
```
- ✅ Test rapide de toutes les fonctionnalités
- ✅ Parfait pour montrer le projet
- ✅ Aucune interaction nécessaire

---

### 5. 🧪 **run_tests.bat**
```
Double-clic → Exécution de tous les tests
```
- ✅ Valide que tout fonctionne
- ✅ 23 tests automatiques
- ✅ Affiche les résultats

---

### 6. 🎯 **compare_finetuning.bat** (NOUVEAU !)
```
Double-clic → Compare Feature Extraction vs Fine-tuning
```
- ✅ Montre la différence entre les deux approches
- ✅ Parfait pour le rapport et la soutenance
- ✅ Génère des statistiques comparatives

---

## ⚠️ EN CAS DE PROBLÈME

### Erreur : "venv not found"

**Problème :** L'environnement virtuel n'existe pas

**Solution :**
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer
venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

---

### Erreur : "streamlit not found"

**Problème :** Streamlit n'est pas installé

**Solution :**
```bash
# Activer l'environnement
venv\Scripts\activate

# Installer streamlit
pip install streamlit plotly
```

---

### Erreur : "Module not found"

**Problème :** Dépendances manquantes

**Solution :**
```bash
# Activer l'environnement
venv\Scripts\activate

# Tout réinstaller
pip install -r requirements.txt
```

---

## 🎓 POUR LA PRÉSENTATION

### Démo Recommandée :

1. **Lancer** `launch_streamlit.bat`
2. **Montrer** l'interface web moderne
3. **Taper** quelques messages :
   - "Je me sens très heureux aujourd'hui !"
   - "Je suis un peu stressé par les examens"
   - "Ça va mieux, merci pour les conseils"
4. **Afficher** les graphiques (onglet "Analyses")
5. **Montrer** les statistiques dans la sidebar
6. **Export** des données (bouton "Exporter")

### Points Forts à Souligner :

✅ Interface moderne et interactive  
✅ Analyse en temps réel avec BERT  
✅ Visualisations dynamiques  
✅ Suivi de l'évolution de l'humeur  
✅ Détection de crise intégrée  
✅ Export des données pour analyse  

---

## 📁 FICHIERS IMPORTANTS

```
Chatbot bien-être/
│
├── launch_streamlit.bat    ← 🌟 Utilise celui-ci !
├── launch_console.bat
├── launch_menu.bat
├── launch_demo.bat
├── run_tests.bat
│
├── src/approach1/           ← Code principal
│   ├── chatbot.py
│   ├── sentiment_analyzer.py
│   ├── mood_tracker.py
│   └── response_generator.py
│
├── ui/
│   └── streamlit_ui.py      ← Interface web
│
├── data/
│   └── mood_history.json    ← Historique sauvegardé
│
└── docs/
    ├── GUIDE_UTILISATION.md
    └── FEATURE_EXTRACTION_VS_FINETUNING.md
```

---

## 🎯 COMMANDES UTILES

### Dans le Chat (Mode Console)

| Commande | Action |
|----------|--------|
| `/stats` | Voir les statistiques d'humeur |
| `/history` | Afficher l'historique |
| `/help` | Aide et commandes |
| `/clear` | Effacer l'écran |
| `/quit` | Quitter |

---

## 💡 TIPS

### Pour la Soutenance :
1. Tester AVANT de présenter
2. Préparer quelques phrases d'exemple
3. Avoir les statistiques prêtes
4. Montrer les graphiques
5. Expliquer la détection de crise

### Pour le Développement :
1. Toujours activer le venv d'abord
2. Tester après chaque modification
3. Sauvegarder régulièrement
4. Consulter les logs en cas d'erreur

---

## 📞 SUPPORT

En cas de problème :
1. Vérifier que Python 3.8+ est installé
2. Vérifier que l'environnement virtuel existe
3. Réinstaller les dépendances
4. Consulter les logs d'erreur

---

**Projet ENSA Berrechid - Chatbot de Bien-être**  
*Créé avec ❤️ - Décembre 2024*
