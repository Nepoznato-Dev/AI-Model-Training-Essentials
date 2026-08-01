<!-- 
This file was automatically translated from English to French.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Évaluation et workflow du machine learning

Guide pratique du cycle de vie du ML — du cadrage du problème à la supervision en production — avec un accent sur les métriques, la validation et le débogage.

---

## Workflow ML (CRISP-ML)

1. **Compréhension métier** : définir l'objectif et les critères de réussite.
2. **Compréhension des données** : explorer les données disponibles, identifier les problèmes de qualité.
3. **Préparation des données** : nettoyer, transformer et découper les données.
4. **Modélisation** : entraîner les modèles, régler les hyperparamètres.
5. **Évaluation** : mesurer les performances à l'aide de métriques.
6. **Déploiement** : mettre le modèle en production.
7. **Supervision** : suivre la dérive, les performances et les anomalies.

Il s'agit d'une boucle itérative — vous reviendrez sur les étapes précédentes en fonction des résultats d'évaluation.

---

## Découpage des données

### Séparation entraînement / validation / test
- **Jeu d'entraînement** (~70 %) : utilisé pour ajuster les paramètres du modèle.
- **Jeu de validation** (~15 %) : utilisé pour régler les hyperparamètres et sélectionner les variantes de modèle.
- **Jeu de test** (~15 %) : utilisé une seule fois, tout à la fin, pour estimer les performances de généralisation.

**Important :** le jeu de test doit rester totalement intact jusqu'à l'évaluation finale afin d'éviter toute fuite de données.

### Validation croisée (k-fold)
Pour les petits jeux de données, utilisez la validation croisée en k plis : divisez les données en k blocs, entraînez sur k-1 blocs, validez sur le bloc restant, puis répétez k fois. Faites ensuite la moyenne des performances. k=5 ou k=10 est courant.

### Découpage stratifié
Pour la classification avec classes déséquilibrées, utilisez un découpage stratifié afin de préserver les proportions de classes dans chaque sous-ensemble.

### Découpage temporel
Pour les données de séries temporelles, effectuez le découpage de manière chronologique (apprendre sur le passé, tester sur le futur) plutôt qu'aléatoirement.

---

## Métriques d'évaluation

### Métriques de classification

| Metric | What it measures | Best used for |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Jeux de données équilibrés |
| **Precision** | TP / (TP + FP) | Quand les faux positifs coûtent cher (ex. détection de spam) |
| **Recall** | TP / (TP + FN) | Quand les faux négatifs coûtent cher (ex. dépistage du cancer) |
| **F1-score** | Moyenne harmonique de la precision et du recall | Jeux de données déséquilibrés, métrique synthétique |
| **AUC-ROC** | Aire sous la courbe ROC ; compromis entre TPR et FPR | Performance générale d'un classifieur indépendamment du seuil |
| **AUC-PR** | Aire sous la courbe Precision-Recall | Jeux de données très déséquilibrés |

**Définitions :**
- TP = True Positive
- TN = True Negative
- FP = False Positive (erreur de type I)
- FN = False Negative (erreur de type II)

### Métriques de régression

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Différence quadratique moyenne | Élevée |
| **RMSE** (Root Mean Squared Error) | Racine carrée de la MSE (mêmes unités que la cible) | Élevée |
| **MAE** (Mean Absolute Error) | Différence absolue moyenne | Faible |
| **R²** (Coefficient of Determination) | Proportion de variance expliquée | Pas directement, mais sensible indirectement aux valeurs aberrantes |

### Métriques de ranking et de retrieval
- **Precision@k** : fraction d'éléments pertinents parmi les k premières recommandations.
- **Recall@k** : fraction de tous les éléments pertinents qui apparaissent dans le top-k.
- **NDCG** (Normalised Discounted Cumulative Gain) : tient compte de la pertinence selon la position.
- **Hit Rate** : indique si un élément pertinent apparaît dans le top-k.

### Métriques génératives / LLM
- **Perplexity** : mesure à quel point le modèle est « surpris » par un texte mis de côté (plus bas = mieux).
- **BLEU** : chevauchement des n-grammes avec des traductions de référence (centré sur la précision).
- **ROUGE** : chevauchement orienté rappel pour le résumé.
- **BERTScore** : similarité sémantique fondée sur des embeddings contextuels (plus robuste que BLEU).
- **METEOR** : aligne les synonymes et les racines via WordNet.

---

## Pièges d'évaluation

### Fuite de données
Cela se produit lorsque des informations issues du jeu de test influencent involontairement l'entraînement.
- **Prévenir :** n'utilisez jamais les données de test pour le feature engineering, la normalisation ou le réglage d'hyperparamètres.
- **Détecter :** si votre modèle obtient des scores anormalement élevés, soupçonnez une fuite de données.

### Surapprentissage (overfitting)
Le modèle fonctionne bien sur les données d'entraînement mais mal sur les jeux de validation/test.
- **Limiter :** utilisez de la régularisation, l'early stopping, une architecture plus simple ou davantage de données.

### Sous-apprentissage (underfitting)
Le modèle obtient de mauvaises performances à la fois sur l'entraînement et la validation.
- **Limiter :** utilisez un modèle plus complexe, ajoutez des features ou réduisez la régularisation.

### Données déséquilibrées
- **Limiter :** utilisez des poids de classe, du suréchantillonnage (SMOTE), du sous-échantillonnage ou des métriques adaptées (F1, AUC-PR) plutôt que l'accuracy.

### Dérive temporelle (concept drift)
La relation entre les features et la cible change avec le temps.
- **Limiter :** réentraînez régulièrement, surveillez les performances et utilisez des algorithmes de détection de dérive.

---

## Réglage des hyperparamètres

- **Grid Search** : essaie exhaustivement toutes les combinaisons d'un ensemble prédéfini d'hyperparamètres. Simple, mais coûteux en calcul.
- **Random Search** : échantillonne des combinaisons aléatoires à partir de distributions. Plus efficace que la grid search dans les espaces de grande dimension.
- **Bayesian Optimisation** : construit un modèle probabiliste de la fonction objectif et sélectionne intelligemment les hyperparamètres. Bibliothèques : Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning** : utilisez des outils comme Optuna, Ray Tune ou Weights & Biases Sweeps pour un réglage distribué.

**Plages de recherche suggérées pour des hyperparamètres courants :**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Sélection et validation des modèles

1. **Modèle de base** : commencez par une heuristique simple ou un modèle simple (par exemple régression logistique, prédicteur moyen) pour établir un plancher de performance.
2. **Modèles candidats** : entraînez plusieurs familles de modèles (par exemple Random Forest, XGBoost, réseau de neurones).
3. **Validez en croisé** chaque candidat sur le jeu de validation.
4. **Comparez les métriques** (avec des intervalles de confiance) et sélectionnez le meilleur candidat.
5. **Évaluation finale** sur le jeu de test conservé à part.
6. **Analyse des erreurs** : examinez les exemples que le modèle traite mal. Identifiez les motifs récurrents (par exemple classes rares, entrées ambiguës) et réinjectez ces enseignements dans la préparation des données ou le feature engineering.

---

## Déploiement et supervision

### Modes de service
- **Batch inference** : traiter de gros volumes de données hors ligne (par exemple des recommandations nocturnes).
- **Online inference** : prédictions en temps réel via API (par exemple credit scoring, détection de fraude).
- **Streaming inference** : traitement piloté par événements, en temps réel et à faible latence (par exemple alertes issues de capteurs IoT).

### Supervision du modèle
- **Suivi des performances** : suivez accuracy/F1 dans le temps sur les données en production (quand la vérité terrain est disponible).
- **Data drift** : surveillez l'évolution des distributions des features d'entrée (par exemple avec le PSI – Population Stability Index).
- **Concept drift** : surveillez les changements dans la relation entre entrées et sorties.
- **Prediction drift** : suivez la distribution des sorties prédites.
- **Latence et débit** : vérifiez le respect des SLA (Service Level Agreements).

### Logging et alertes
- Journalisez toutes les requêtes de prédiction et leurs réponses (avec anonymisation).
- Définissez des alertes pour :
  - une baisse significative des performances ;
  - un pourcentage élevé d'entrées manquantes ou invalides ;
  - des sorties du modèle en dehors des bornes attendues.

### Versioning et registry des modèles
- Utilisez un model registry (par exemple MLflow, Weights & Biases, Sagemaker Model Registry) pour stocker et versionner les modèles, les métadonnées et les résultats d'évaluation.
- Stockez le code d'entraînement et la version des données (via DVC ou Git LFS) aux côtés du modèle.

---

## Checklist pratique du workflow

- [ ] Problème cadré et métrique de succès définie.
- [ ] Exploration des données effectuée (valeurs manquantes, outliers, distribution).
- [ ] Découpage entraînement/validation/test créé (stratifié si nécessaire).
- [ ] Modèle de base établi.
- [ ] Modèles candidats entraînés et validés.
- [ ] Hyperparamètres réglés.
- [ ] Meilleur modèle sélectionné via validation croisée.
- [ ] Évaluation finale sur le jeu de test.
- [ ] Analyse des erreurs effectuée.
- [ ] Plan de déploiement prêt (infrastructure de service).
- [ ] Tableau de bord de supervision en place.
- [ ] Documentation (data card, model card) terminée.
