"""
Préparation des données pour fine-tuning BERT sur le bien-être
Crée un dataset équilibré de sentiments bien-être
"""

import json
import random
import os
from typing import List, Dict, Tuple
from pathlib import Path


def create_wellbeing_dataset(size: int = 500) -> List[Dict]:
    """
    Crée un dataset d'entraînement pour fine-tuning BERT
    
    Le dataset contient des exemples de sentiments bien-être réalistes
    organisés en 5 classes équilibrées.
    
    Args:
        size (int): Nombre total d'exemples (default: 500)
        
    Returns:
        list: Dataset avec structure [{'text': ..., 'label': ..., 'label_id': ...}, ...]
        
    Example:
        >>> dataset = create_wellbeing_dataset(100)
        >>> len(dataset)
        100
        >>> dataset[0]
        {'text': '...', 'label': 'positif', 'label_id': 3}
    """
    
    # ============================================================================
    # DONNÉES BIEN-ÊTRE RÉALISTES - 5 Classes de Sentiment
    # ============================================================================
    
    WELLBEING_EXAMPLES = {
        'très négatif': [
            # Expressions de désespoir, idées suicidaires, abandon
            "Je veux tout abandonner",
            "Je ne vois pas d'issue",
            "Je suis désespéré",
            "Je préfère ne pas exister",
            "Je ne mérite pas de vivre",
            "Je suis un fardeau pour tout le monde",
            "Rien n'a de sens",
            "Je veux disparaître",
            "C'est trop pour moi",
            "Je ne peux plus continuer",
            "Tout est noir",
            "Je suis incapable",
            "Personne ne m'aime",
            "Je suis complètement perdu",
            "Je veux en finir",
            "La vie n'a aucune valeur",
            "Je suis un échec",
            "Je ne vaux rien",
            "Je suis seul et abandonné",
            "Tout est inutile",
        ],
        'négatif': [
            # Tristesse, stress, anxiété, mal-être
            "Je suis triste",
            "Rien n'a d'importance",
            "Je me sens vide",
            "Je suis stressé",
            "Je suis anxieux",
            "Je me sens mal",
            "J'ai peur",
            "Je suis découragé",
            "Ça ne va pas bien",
            "Je suis fatigué",
            "Je ne sais pas quoi faire",
            "Je me sens seul",
            "C'est trop difficile",
            "Je suis frustré",
            "Je n'ai pas d'énergie",
            "Je suis déprimé",
            "Rien ne me plaît",
            "Je suis inquiet",
            "Je doute de moi",
            "C'est déprimant",
            "Je suis submergé",
            "Tout est compliqué",
            "Je suis affecté",
            "J'ai des pensées négatives",
            "Ça m'angoisse",
        ],
        'neutre': [
            # Questions, observations neutres, conversation simple
            "Bonjour, comment ça va?",
            "Il fait beau dehors",
            "Quelle heure est-il?",
            "Ça va, et toi?",
            "Qu'est-ce que tu fais?",
            "Je ne sais pas",
            "C'est normal",
            "C'est juste une journée ordinaire",
            "Rien de spécial",
            "C'est comme d'habitude",
            "Je fais juste passer le temps",
            "C'est banal",
            "Rien de nouveau",
            "C'est la routine",
            "Pas grand-chose",
            "Juste ça",
            "C'est ça",
            "Comme d'habitude",
            "Rien qui change",
            "C'est tout",
            "Je vais bien, merci",
            "Aucun souci",
            "C'est ok",
            "Pas mal",
            "C'est acceptable",
        ],
        'positif': [
            # Bien-être, satisfaction, contentement
            "Ça va plutôt bien",
            "J'ai une bonne journée",
            "Je suis content",
            "Je me sens mieux",
            "C'est sympa",
            "J'aime bien",
            "Je suis fier de moi",
            "J'ai du courage",
            "Je peux le faire",
            "Ça va s'arranger",
            "J'ai de l'espoir",
            "Je suis motivé",
            "C'est agréable",
            "Je me sens bien",
            "J'ai de l'énergie",
            "C'est cool",
            "Je suis optimiste",
            "Ça me plaît",
            "Je suis confiant",
            "C'est positif",
            "Je me sens fort",
            "J'ai du potentiel",
            "Ça me fait du bien",
            "Je suis satisfait",
            "Ça marche bien",
        ],
        'très positif': [
            # Euphorie, joie intense, bonheur
            "Je suis heureux!",
            "C'est magnifique!",
            "Je suis aux anges!",
            "C'est formidable!",
            "Je suis ravi!",
            "C'est incroyable!",
            "Je suis enthousiaste!",
            "C'est génial!",
            "Je suis exubérant!",
            "C'est fantastique!",
            "Je suis débordant de joie!",
            "C'est merveilleux!",
            "Je suis dans l'euphorie!",
            "C'est excellent!",
            "Je suis passionné!",
            "C'est extraordinaire!",
            "Je suis conquis!",
            "C'est superbe!",
            "Je suis comblé!",
            "C'est spectaculaire!",
            "Je suis sur un nuage!",
            "C'est sublime!",
            "Je suis épanoui!",
            "C'est merveilleux au-delà des mots!",
            "Je suis vivant et énergique!",
        ]
    }
    
    # ============================================================================
    # CRÉER LE DATASET ÉQUILIBRÉ
    # ============================================================================
    
    dataset = []
    
    # Mapping label → ID
    label_to_id = {
        'très négatif': 0,
        'négatif': 1,
        'neutre': 2,
        'positif': 3,
        'très positif': 4
    }
    
    # Nombre d'exemples par classe
    examples_per_class = size // 5  # 500 / 5 = 100 par classe
    
    print(f"📊 Création d'un dataset de {size} exemples")
    print(f"   ({examples_per_class} exemples par classe)")
    print()
    
    # Pour chaque classe de sentiment
    for label, examples in WELLBEING_EXAMPLES.items():
        # Prendre examples_per_class textes (avec répétition si nécessaire)
        if len(examples) >= examples_per_class:
            # Assez d'exemples : en prendre examples_per_class sans répétition
            selected = random.sample(examples, examples_per_class)
        else:
            # Pas assez d'exemples : répéter et mélanger
            selected = examples * (examples_per_class // len(examples) + 1)
            selected = selected[:examples_per_class]
        
        # Ajouter au dataset
        for text in selected:
            dataset.append({
                'text': text,
                'label': label,
                'label_id': label_to_id[label]
            })
        
        print(f"   ✅ {label:20s} : {len(selected):3d} exemples")
    
    # ============================================================================
    # MÉLANGER LE DATASET
    # ============================================================================
    
    random.shuffle(dataset)
    
    print()
    print(f"✅ Dataset créé avec {len(dataset)} exemples")
    print(f"   Classes : {list(label_to_id.keys())}")
    
    return dataset


def save_dataset(dataset: List[Dict], 
                 filepath: str = 'data/training_wellbeing_data.json') -> None:
    """
    Sauvegarde le dataset en JSON pour future réutilisation
    
    Args:
        dataset (list): Dataset à sauvegarder
        filepath (str): Chemin du fichier JSON
    """
    
    # Créer le répertoire s'il n'existe pas
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    
    # Sauvegarder en JSON
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Dataset sauvegardé : {filepath}")


def load_dataset(filepath: str = 'data/training_wellbeing_data.json') -> List[Dict]:
    """
    Charge un dataset depuis un fichier JSON
    
    Args:
        filepath (str): Chemin du fichier JSON
        
    Returns:
        list: Dataset chargé
    """
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    print(f"✅ Dataset chargé : {filepath} ({len(dataset)} exemples)")
    
    return dataset


def validate_dataset(dataset: List[Dict]) -> Dict:
    """
    Valide la structure et l'équilibre du dataset
    
    Args:
        dataset (list): Dataset à valider
        
    Returns:
        dict: Statistiques du dataset
    """
    
    print("\n📊 VALIDATION DU DATASET")
    print("=" * 50)
    
    # Compter par classe
    class_counts = {}
    for example in dataset:
        label = example['label']
        class_counts[label] = class_counts.get(label, 0) + 1
    
    # Afficher les statistiques
    for label in ['très négatif', 'négatif', 'neutre', 'positif', 'très positif']:
        count = class_counts.get(label, 0)
        percentage = (count / len(dataset)) * 100
        print(f"  {label:20s} : {count:3d} ({percentage:.1f}%)")
    
    print("=" * 50)
    
    # Vérifier l'équilibre
    min_count = min(class_counts.values())
    max_count = max(class_counts.values())
    balance_ratio = min_count / max_count
    
    print(f"\n✅ Total exemples : {len(dataset)}")
    print(f"✅ Classes : {len(class_counts)}/5")
    print(f"✅ Équilibre : {balance_ratio:.2%} (idéal: 100%)")
    
    if balance_ratio >= 0.95:
        print("   → Dataset bien équilibré! ✅")
    elif balance_ratio >= 0.80:
        print("   → Dataset acceptable (léger déséquilibre)")
    else:
        print("   → Dataset déséquilibré (besoin d'amélioration)")
    
    return {
        'total': len(dataset),
        'classes': len(class_counts),
        'class_counts': class_counts,
        'balance_ratio': balance_ratio
    }


def split_train_val(dataset: List[Dict], 
                    train_ratio: float = 0.8) -> Tuple[List[Dict], List[Dict]]:
    """
    Divise le dataset en ensemble d'entraînement et de validation
    
    Args:
        dataset (list): Dataset complet
        train_ratio (float): Proportion pour l'entraînement (default: 0.8)
        
    Returns:
        tuple: (train_dataset, val_dataset)
    """
    
    # Calculer les index de split
    split_idx = int(len(dataset) * train_ratio)
    
    # Diviser (dataset est déjà mélangé)
    train_dataset = dataset[:split_idx]
    val_dataset = dataset[split_idx:]
    
    print(f"\n✅ Split train/validation :")
    print(f"   Train : {len(train_dataset)} exemples ({train_ratio:.0%})")
    print(f"   Val   : {len(val_dataset)} exemples ({1-train_ratio:.0%})")
    
    return train_dataset, val_dataset


# ============================================================================
# SCRIPT PRINCIPAL
# ============================================================================

if __name__ == '__main__':
    print("\n🤖 PRÉPARATION DES DONNÉES POUR FINE-TUNING BERT\n")
    
    # Étape 1 : Créer le dataset
    dataset = create_wellbeing_dataset(size=500)
    
    # Étape 2 : Valider le dataset
    validate_dataset(dataset)
    
    # Étape 3 : Sauvegarder
    save_dataset(dataset)
    
    # Étape 4 : Diviser en train/validation
    train_dataset, val_dataset = split_train_val(dataset)
    
    print("\n✅ DONNÉES PRÊTES POUR FINE-TUNING!")
    print("   Prochaine étape : Créer le fine-tuner BERT")
