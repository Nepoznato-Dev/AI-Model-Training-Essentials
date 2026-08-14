<!--
---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Méthodes d'ensemble
Les méthodes d'ensemble combinent plusieurs modèles d'apprentissage automatique pour produire de meilleures prédictions que ce qu'un seul modèle pourrait réaliser seul. L’intuition est simple : si vous disposez de plusieurs modèles qui sont chacun assez précis mais commettent des erreurs différentes, la combinaison de leurs prédictions annulera les erreurs individuelles et produira un résultat plus robuste. Les ensembles sont à l'origine des solutions d'apprentissage automatique les plus compétitives et restent parmi les techniques les plus fiables dans les systèmes de production.
---

## Pourquoi les ensembles fonctionnent
| Principe | Descriptif |
|---------------|-------------|
| **Sagesse des foules** | Plusieurs estimations imparfaites, moyennées, valent mieux que n’importe quelle estimation unique |
| **Compromis biais-variance** | Les ensembles peuvent réduire la variance (bagging) ou les biais (boosting) sans sacrifier les autres |
| **Diversité des erreurs** | Si les modèles font des erreurs différentes, leur combinaison annule les erreurs individuelles |
| **Lissage des limites de décision** | Plusieurs modèles créent une surface de décision plus robuste qu'un seul modèle |
---

## Ensachage (agrégation Bootstrap)
### Comment ça marche
| Étape | Descriptif |
|------|-------------|
| **1. Échantillonnage bootstrap** | Tirez plusieurs échantillons aléatoires (avec remplacement) à partir des données d'entraînement |
| **2. Modèles de base de train** | Former un modèle sur chaque échantillon bootstrap (généralement des arbres de décision) |
| **3. Agrégat** | Pour la régression : prédictions moyennes. Pour classement : vote majoritaire |
### Caractéristiques clés
| Caractéristique | Descriptif |
|---------------|-------------|
| **Réduit la variance** | La moyenne atténue les fluctuations des modèles individuels |
| **Formation parallèle** | Chaque modèle de base est indépendant ; peuvent être formés simultanément |
| **Évaluation hors sac** | Chaque échantillon est exclu de certains échantillons bootstrap ; utilisez-les pour la validation |
| **Décorrélation** | La sélection aléatoire des caractéristiques à chaque division réduit la corrélation entre les arbres |
### Forêt aléatoire
| Aspects | Descriptif |
|--------|-------------|
| **Apprenant de base** | Arbres de décision |
| **Ajout clé** | À chaque division, considérez uniquement un sous-ensemble aléatoire de fonctionnalités (généralement sqrt(n_features)) |
| **Pourquoi ça marche** | La sélection aléatoire de caractéristiques décorrèle les arbres, rendant l'ensemble plus robuste |
| **Hyperparamètres** | Nombre d'arbres ; profondeur maximale ; échantillons minimum par feuille ; fonctionnalités maximales |
| **Forces** | Gère les données de grande dimension ; robuste aux valeurs aberrantes ; fournit l'importance des fonctionnalités |
| **Faiblesses** | Moins interprétable que les arbres isolés ; peut surajuster les tâches de régression bruyantes |
---

## Boosting
### Comment ça marche
| Étape | Descriptif |
|------|-------------|
| **1. Former le premier modèle** | Former un modèle de base (souvent un arbre peu profond / "souche") sur les données |
| **2. Identifier les erreurs** | Trouver les instances dans lesquelles le modèle s'est trompé |
| **3. Former le prochain modèle** | Former un nouveau modèle axé sur les erreurs (repondéré ou ajusté résiduel) |
| **4. Combiner séquentiellement** | Chaque nouveau modèle corrige les erreurs accumulées de tous les modèles précédents |
| **5. Répéter** | Continuez pendant un nombre spécifié de tours |
### Booster les algorithmes
| Algorithme | Fonction de perte | Caractéristique clé |
|---------------|--------------|-------------|
| **AdaBoost** | Exponentiel | Repondère les instances mal classées ; simple; sensible au bruit |
| **Amélioration du dégradé** | Toute perte différenciable | Ajuste les résidus (gradient de perte) ; plus flexible |
| **XGBoost** | Boosting de gradient régularisé | Régularisation L1/L2 ; gradients de second ordre ; optimisation matérielle |
| **LightGBM** | Échantillonnage unilatéral basé sur un gradient | Croissance foliaire ; basé sur un histogramme ; rapide sur de grands ensembles de données |
| **CatBoost** | Renforcement ordonné | Gère les fonctionnalités catégorielles de manière native ; réduit le surapprentissage |
### Boosting vs ensachage
| Dimensions | Ensachage | Booster |
|-----------|---------|---------------|
| **Formation** | Parallèle | Séquentiel |
| **Concentration** | Réduit la variance | Réduit les biais |
| **Modèles de base** | Haute variance, faible biais (arbres profonds) | Faible variance, biais élevé (arbres / souches peu profonds) |
| **Combinaison** | Poids égal | Pondéré par la performance |
| **Surapprentissage** | Moins sujet | Peut être surajusté si trop de tours |
| **Sensibilité au bruit** | Robuste | Sensible aux données bruitées |
---

## Empilement
### Comment ça marche
| Étape | Descriptif |
|------|-------------|
| **1. Modèles de base de train** | Former divers modèles (par exemple, forêt aléatoire, SVM, réseau neuronal, boosting de gradient) |
| **2. Générer des prédictions** | Utiliser des prédictions hors de portée (validation croisée) comme fonctionnalités d'entrée |
| **3. Former le méta-modèle** | Entraîner un modèle de deuxième niveau sur les prédictions des modèles de base |
| **4. Prédiction finale** | Les modèles de base prédisent ; méta-modèle combine leurs prédictions |
### Bonnes pratiques d'empilement
| Pratique | Raison |
|--------------|--------|
| **Utilisez divers modèles de base** | Différents algorithmes font différentes erreurs ; la diversité est tout l'intérêt |
| **Utiliser la validation croisée pour les prédictions de base** | Empêche le méta-modèle d'apprendre à exploiter les modèles de base surajustés |
| **Gardez le méta-modèle simple** | Régression logistique ou arbre peu profond ; les modèles de base font le gros du travail |
| **Inclure les fonctionnalités brutes dans le méta-modèle** | Parfois utile pour donner également au méta-modèle l'accès aux fonctionnalités d'origine |
---

## Vote et moyenne
### Vote dur (Classification)
| Modèle | Prédiction |
|-------|---------------|
| Modèle A | Classe 1 |
| Modèle B | Classe 0 |
| Modèle C | Classe 1 |
| **Vote majoritaire** | **Classe 1** |
### Vote doux (Classification)
| Modèle | P(Classe 0) | P(Classe 1) |
|-------|-----------|---------------|
| Modèle A | 0,3 | 0,7 |
| Modèle B | 0,6 | 0,4 |
| Modèle C | 0,4 | 0,6 |
| **Moyenne** | **0,43** | **0,57** |
| **Prédiction** | | **Classe 1** |
### Moyenne pondérée
| Modèle | Poids | Prédiction |
|-------|--------|---------------|
| Modèle A | 0,5 | 0,8 |
| Modèle B | 0,3 | 0,6 |
| Modèle C | 0,2 | 0,9 |
| **Moyenne pondérée** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Conseils pratiques
### Quand utiliser quel ensemble
| Scénario | Méthode recommandée |
|----------|---------|
| **Référence rapide ; données tabulaires** | Forêt aléatoire |
| **Précision maximale ; données tabulaires** | XGBoost / LightGBM / CatBoost |
| **Données bruyantes** | Ensachage (l'amplification surajustera le bruit) |
| **Interprétabilité nécessaire** | Modèle unique ou petit ensemble avec importance des fonctionnalités |
| **Divers types de modèles** | Empilement ou vote |
| **Apprentissage en ligne** | Méthodes d'ensemble de diffusion en continu ; boost adaptatif |
| **Données déséquilibrées** | Forêt aléatoire équilibrée ; stimulation sensible aux coûts |
### Stratégies de diversité d'ensemble
| Stratégie | Descriptif |
|--------------|-------------|
| **Différents algorithmes** | Combinez des modèles arborescents, linéaires et neuronaux |
| **Différentes fonctionnalités** | Entraîner des modèles sur différents sous-ensembles de fonctionnalités |
| **Différents sous-ensembles de données** | Ensachage ; sous-échantillonnage |
| **Différents hyperparamètres** | Même algorithme avec des configurations variées |
| **Différentes périodes** | Entraînez-vous sur différentes plages horaires |
---

## Résumé
Les méthodes d'ensemble fonctionnent car elles combinent plusieurs modèles imparfaits en un seul prédicteur robuste. L'ensachage (forêts aléatoires) réduit la variance en entraînant des modèles en parallèle sur des échantillons bootstrap et en faisant la moyenne. Le boosting (XGBoost, LightGBM, CatBoost) réduit les biais en entraînant les modèles de manière séquentielle, chacun corrigeant les erreurs précédentes. Stacking utilise un méta-modèle pour combiner divers modèles de base. Le vote et la moyenne sont les ensembles les plus simples. Le fil conducteur est la diversité : les ensembles fonctionnent mieux lorsque leurs modèles composants sont individuellement raisonnables mais commettent des erreurs différentes. En pratique, l’augmentation du gradient sur les données tabulaires constitue souvent l’approche la plus performante, tandis que l’empilement de divers modèles améliore la précision dans les compétitions et les applications à enjeux élevés.