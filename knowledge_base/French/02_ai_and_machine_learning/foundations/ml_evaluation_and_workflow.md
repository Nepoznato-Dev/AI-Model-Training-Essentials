---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, evaluation, workflow, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Évaluation et flux de travail de l'apprentissage automatique
Un guide pratique sur le cycle de vie du ML — de la définition des problèmes à la surveillance de la production — en mettant l'accent sur les métriques, la validation et le débogage.
---

## Le flux de travail ML (CRISP-ML)
1. **Business Understanding** : Définir l'objectif et les critères de réussite.
2. **Compréhension des données** : explorez les données disponibles, identifiez les problèmes de qualité.
3. **Préparation des données** : nettoyez, transformez et fractionnez les données.
4. **Modélisation** : entraînez des modèles, ajustez les hyperparamètres.
5. **Évaluation** : évaluez les performances par rapport à des indicateurs.
6. **Déploiement** : servir le modèle en production.
7. **Surveillance** : suivez la dérive, les performances et les anomalies.
Il s’agit d’une boucle itérative : vous revisiterez les étapes précédentes en fonction des résultats de l’évaluation.
---

## Fractionnement des données
### Entraînement / Validation / Répartition des tests
- **Ensemble de formation** (~70 %) : utilisé pour ajuster les paramètres du modèle.
- **Ensemble de validation** (~15 %) : utilisé pour régler les hyperparamètres et sélectionner les variantes du modèle.
- **Ensemble de tests** (~15 %) : utilisé une seule fois à la toute fin pour estimer les performances de généralisation.
**Important :** L'ensemble de test doit rester complètement intact jusqu'à l'évaluation finale pour éviter les fuites de données.
### Validation croisée (k-fold)
Pour les petits ensembles de données, utilisez la validation croisée k fois : divisez les données en k fois, entraînez-vous sur k-1, validez sur le reste et répétez k fois. Faites la moyenne des performances. k=5 ou k=10 est courant.
### Fractionnement stratifié
Pour la classification avec des classes déséquilibrées, utilisez des répartitions stratifiées pour préserver les proportions de classe dans chaque sous-ensemble.
### Fractionnement basé sur le temps
Pour les données de séries chronologiques, répartissez chronologiquement (entraînement sur le passé, test sur le futur) plutôt que de manière aléatoire.
---

## Métriques d'évaluation
### Métriques de classification
| Métrique | Ce qu'il mesure | Mieux utilisé pour |
|--------|--------|---------------|
| **Précision** | (TP + TN) / (TP + TN + FP + FN) | Ensembles de données équilibrés |
| **Précision** | TP / (TP + FP) | Quand les faux positifs coûtent cher (par exemple, détection de spam) |
| **Rappel** | TP / (TP + FN) | Quand les faux négatifs coûtent cher (ex. : dépistage du cancer) |
| **Score F1** | Moyenne harmonique de précision et de rappel | Ensembles de données déséquilibrés, métrique à nombre unique |
| **AUC-ROC** | Aire sous la courbe ROC ; compromis entre TPR et FPR | Performances générales du classificateur indépendantes du seuil |
| **AUC-PR** | Aire sous la courbe Précision-Rappel | Ensembles de données très déséquilibrés |
**Définitions :**
- TP = Vrai Positif
- TN = Vrai Négatif
- FP = Faux Positif (Erreur de Type I)
- FN = Faux Négatif (Erreur de Type II)
### Métriques de régression
| Métrique | Ce qu'il mesure | Sensibilité aux valeurs aberrantes |
|--------|--------|-------------------------------|
| **MSE** (erreur quadratique moyenne) | Différence quadratique moyenne | Élevé |
| **RMSE** (erreur quadratique moyenne) | Racine carrée de MSE (mêmes unités que la cible) | Élevé |
| **MAE** (erreur absolue moyenne) | Différence absolue moyenne | Faible |
| **R²** (Coefficient de Détermination) | Proportion de variance expliquée | Aucun directement, mais sensible indirectement aux valeurs aberrantes |
### Métriques de classement et de récupération
- **Precision@k** : fraction des éléments pertinents parmi les k recommandations les plus importantes.
- **Recall@k** : fraction de tous les éléments pertinents qui apparaissent dans le top-k.
- **NDCG** (Gain cumulatif actualisé normalisé) : tient compte de la pertinence du poste.
- **Taux de réussite** : indique si un élément pertinent apparaît dans le top-k.
### Métriques génératives / LLM
- **Perplexité** : À quel point le modèle est "surpris" par un texte tendu (plus bas est mieux).
- **BLEU** : chevauchement de n-grammes avec des traductions de référence (axées sur la précision).
- **ROUGE** : Chevauchement orienté rappel pour la synthèse.
- **BERTScore** : Similitude sémantique utilisant des plongements contextuels (plus robuste que BLEU).
- **METEOR** : s'aligne sur les synonymes et les racines WordNet.
---

## Pièges de l'évaluation
### Fuite de données
Se produit lorsque les informations de l’ensemble de tests influencent par inadvertance la formation.
- **Prévenir :** N'utilisez jamais de données de test pour l'ingénierie de fonctionnalités, la normalisation ou le réglage d'hyperparamètres.
- **Détecter :** Si votre modèle obtient un score suspect, suspectez une fuite.
### Surapprentissage
Le modèle fonctionne bien sur les données d'entraînement mais mal sur la validation/test.
- **Atténuer :** Utilisez la régularisation, l'arrêt anticipé, simplifiez l'architecture ou collectez davantage de données.
### Sous-ajustement
Le modèle fonctionne mal à la fois en termes de formation et de validation.
- **Atténuer :** Utilisez un modèle plus complexe, ajoutez des fonctionnalités ou réduisez la régularisation.
### Données déséquilibrées
- **Atténuer :** Utilisez des pondérations de classe, un suréchantillonnage (SMOTE), un sous-échantillonnage ou utilisez des métriques appropriées (F1, AUC-PR) plutôt que la précision.
### Dérive temporelle (Dérive conceptuelle)
La relation entre les fonctionnalités et la cible change avec le temps.
- **Atténuer :** Entraînez-vous périodiquement, surveillez les performances, utilisez des algorithmes de détection de dérive.
---

## Réglage des hyperparamètres
- **Grid Search** : essayez de manière exhaustive toutes les combinaisons d'un ensemble prédéfini d'hyperparamètres. Simple mais coûteux en calcul.
- **Recherche aléatoire** : échantillonnez des combinaisons aléatoires à partir de distributions. Plus efficace que la recherche par grille pour les espaces de grande dimension.
- **Optimisation bayésienne** : construit un modèle probabiliste de la fonction objectif et sélectionne intelligemment les hyperparamètres. Bibliothèques : Optuna, Hyperopt, scikit-optimise.
- **Réglage automatisé** : utilisez des outils tels que Optuna, Ray Tune ou Weights & Biases Sweeps pour un réglage distribué.
**Plages de recherche suggérées pour les hyperparamètres courants :**
| Paramètre | Plage suggérée (échelle logarithmique) |
|---------------|-----------------------------|
| Taux d'apprentissage | 1e-5 à 1e-1 |
| Taille du lot | 16, 32, 64, 128, 256 |
| Nombre de couches (NN) | 2 à 6 |
| Nombre de neurones (NN) | 32 à 1024 |
| Régularisation (L2) | 1e-6 à 1e-2 |
| Profondeur de l'arbre (XGBoost) | 3 à 12 |
---

## Sélection et validation du modèle
1. **Modèle de base** : commencez par une heuristique ou un modèle simple (par exemple, régression logistique, prédicteur de moyenne) pour établir une limite inférieure.
2. **Modèles candidats** : formez plusieurs familles de modèles (par exemple, Random Forest, XGBoost, Neural Network).
3. **Validation croisée** chaque candidat sur l'ensemble de validation.
4. **Comparez les métriques** (avec intervalles de confiance) et sélectionnez le meilleur candidat.
5. **Évaluation finale** sur l'ensemble de test retenu.
6. **Analyse des erreurs** : regardez des exemples dans lesquels le modèle se trompe. Identifiez les modèles (par exemple, classes rares, entrées ambiguës) et intégrez des informations à la préparation des données ou à l'ingénierie des fonctionnalités.
---

## Déploiement et surveillance
### Modèles de diffusion
- **Inférence par lots** : traitez de gros volumes de données hors ligne (par exemple, recommandations nocturnes).
- **Inférence en ligne** : prédictions en temps réel via API (par exemple, notation de crédit, détection de fraude).
- **Inférence de streaming** : basée sur des événements, en temps réel avec une faible latence (par exemple, alertes de capteurs IoT).
### Surveillance du modèle
- **Surveillance des performances** : suivez la précision/F1 au fil du temps sur les données en direct (lorsque la vérité sur le terrain est disponible).
- **Dérive des données** : surveillez les changements dans les distributions des caractéristiques d'entrée (par exemple, en utilisant le PSI – Population Stability Index).
- **Dérive du concept** : Surveiller les changements dans la relation entre les entrées et les sorties.
- **Dérive de prédiction** : suivez la distribution des résultats prédits.
- **Latence et débit** : assurez-vous que les SLA (Service Level Agreements) sont respectés.
### Journalisation et alertes
- Enregistrez toutes les demandes et réponses de prédiction (avec anonymisation).
- Définir des alertes pour :
  - Baisse importante des performances.
  - Pourcentage élevé d'entrées manquantes ou invalides.
  - Résultats du modèle en dehors des limites attendues.
### Versionnement et registre des modèles
- Utilisez un registre de modèles (par exemple, MLflow, Weights & Biases, Sagemaker Model Registry) pour stocker et versionner les modèles, les métadonnées et les résultats d'évaluation.
- Stockez le code de formation et la version des données (via DVC ou Git LFS) à côté du modèle.
---

## Liste de contrôle pratique du flux de travail
- [ ] Problème défini et mesure de réussite définie.
- [ ] Exploration des données effectuée (valeurs manquantes, valeurs aberrantes, distribution).
- [ ] Répartition train/validation/test créée (stratifiée si nécessaire).
- [ ] Modèle de base établi.
- [ ] Modèles candidats formés et validés.
- [ ] Hyperparamètres réglés.
-[ ] Meilleur modèle sélectionné via validation croisée.
- [ ] Évaluation finale sur l'ensemble de test.
- [ ] Analyse des erreurs effectuée.
- [ ] Plan de déploiement prêt (infrastructure de service).
- [ ] Mise en place du tableau de bord de suivi.
- [ ] Documentation (carte de données, carte modèle) complétée.