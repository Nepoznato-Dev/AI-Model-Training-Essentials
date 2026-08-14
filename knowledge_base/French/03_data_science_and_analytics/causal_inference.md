---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Inférence causale
L'inférence causale est la science qui consiste à déterminer si une chose en provoque réellement une autre, et pas seulement si elles sont corrélées. La corrélation vous indique que deux variables évoluent ensemble. La causalité vous dit que changer l’un changera l’autre. Cette distinction est extrêmement importante en médecine (ce médicament est-il efficace ?), en politique (cette intervention réduit-elle la pauvreté ?), en affaires (cette campagne publicitaire augmente-t-elle les ventes ?) et en science (ce mécanisme explique-t-il le phénomène ?).
---

## Corrélation vs causalité
| Concepts | Descriptif | Exemple |
|---------|-------------|---------|
| **Corrélation** | Deux variables évoluent ensemble | Les ventes de glaces et les décès par noyade augmentent tous deux en été |
| **Causalité** | Une variable en affecte directement une autre | Le tabagisme provoque le cancer du poumon |
| **Confondant** | Une troisième variable provoque à la fois | Le temps chaud provoque à la fois la vente de glaces et la baignade (et la noyade) |
| **Causalité inverse** | L'effet provoque en réalité la cause supposée | Les gens achètent des suppléments de santé parce qu'ils sont malades, et non l'inverse |
| **Fausse corrélation** | Relation fortuite | La consommation de fromage par habitant est en corrélation avec les décès dus à l'enchevêtrement des draps |
---

## Le cadre des résultats potentiels
### Modèle causal de Rubin
| Concepts | Descriptif |
|---------|-------------|
| **Résultats potentiels** | Pour chaque unité, il y a un résultat si traité Y(1) et un résultat si non traité Y(0) |
| **Effet du traitement** | La différence : Y(1) - Y(0) pour une unité donnée |
| **Problème fondamental** | Nous ne pouvons jamais observer à la fois Y(1) et Y(0) pour la même unité — nous ne pouvons en voir qu'un seul |
| **Effet moyen du traitement (ATE)** | La moyenne des effets individuels des traitements dans la population |
| **Contrefactuel** | Le résultat inobservé – que se serait-il passé dans l’autre condition |
### Hypothèses clés
| Hypothèse | Signification | Comment satisfaire |
|-----------|--------|----------------|
| **Ignorabilité (absence de confusion)** | L'attribution du traitement est indépendante des résultats potentiels, compte tenu des covariables observées | Randomisation ; mesurer tous les facteurs de confusion |
| **Positivité (chevauchement)** | Chaque unité a une probabilité non nulle de recevoir l'un ou l'autre traitement | Vérifier le chevauchement des covariables entre les groupes |
| **SUTVA** (hypothèse de valeur de traitement unitaire stable) | Le traitement d'une unité n'affecte pas le résultat d'une autre ; le traitement est cohérent | Aucune interférence ; pas de versions cachées du traitement |
| **Cohérence** | Le résultat observé est égal au résultat potentiel du traitement reçu | Traitement bien défini |
---

## Méthodes d'inférence causale
### Méthodes expérimentales
| Méthode | Descriptif | Force | Limitation |
|--------|-------------|--------------|------------|
| **Essai contrôlé randomisé (ECR)** | Attribuer au hasard des unités au traitement ou au contrôle | L’étalon-or ; élimine la confusion | Cher; parfois contraire à l’éthique ; ne peut pas généraliser |
| **Tests A/B** | ECR dans un contexte business/tech | Simple; rigoureux | Mesures à court terme ; effets de nouveauté ; interférence |
| **Expériences de commutation** | Traitement alternatif au fil du temps | Gère les interférences sur les marchés | Nécessite un environnement stable |
### Méthodes quasi-expérimentales
| Méthode | Descriptif | Hypothèse clé |
|--------|-------------|----------------|
| **Différence dans les différences (DiD)** | Comparez l'évolution des résultats entre les groupes traités et témoins au fil du temps | Tendances parallèles : des groupes auraient suivi la même trajectoire sans traitement |
| **Discontinuité de régression (RD)** | Comparez les unités juste au-dessus et juste en dessous d'un seuil de traitement | Les unités proches du seuil sont comparables (comme si elles étaient aléatoires) |
| **Variables instrumentales (IV)** | Utiliser une variable qui affecte le traitement mais pas le résultat, sauf via le traitement | L'instrument est corrélé au traitement ; affecte les résultats uniquement grâce au traitement |
| **Contrôle synthétique** | Construire une combinaison pondérée d'unités de contrôle pour correspondre à l'unité traitée | Le contrôle synthétique représente avec précision le contrefactuel de l'unité traitée |
| **Correspondance du score de propension** | Faire correspondre les unités traitées et les unités témoins présentant des probabilités de traitement similaires | Tous les facteurs de confusion sont mesurés et inclus dans le modèle de propension |
### Différence dans les différences (visualisée)
| Période | Groupe traité | Groupe de contrôle | Différence |
|--------|--------------|---------------|------------|
| **Prétraitement** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Post-traitement** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **Estimation Did** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Graphiques acycliques dirigés (DAG)
Les DAG sont des outils visuels permettant de coder des hypothèses causales et d’identifier les facteurs confondants.
### Structures de base
| Structure | Modèle | Implications |
|-----------|---------|-------------|
| **Chaîne** | UNE → B → C | A et C sont associés via B ; contrôler B bloque le chemin |
| **Fourchette** | UNE ← B → C | A et C sont confondus avec B ; contrôler B bloque le chemin |
| **Collisionneur** | UNE → B ← C | A et C sont indépendants ; contrôler B ouvre le chemin (crée une association parasite) |
### Règles pour les DAG
| Règle | Descriptif |
|------|-------------|
| **Critère de porte dérobée** | Pour estimer l'effet causal de X sur Y, bloquez tous les chemins de porte dérobée (chemins avec une flèche vers X) en conditionnant sur les variables appropriées |
| **Critère de la porte d'entrée** | Si les chemins de porte dérobée ne peuvent pas être bloqués, utilisez des médiateurs : estimez X → M → Y en deux étapes |
| **Ne conditionnez pas les collisionneurs** | Contrôler un effet commun ouvre une voie fallacieuse |
| **Ne conditionnez pas les descendants des collisionneurs** | Même problème que le conditionnement sur le collisionneur lui-même |
---

## Pièges courants
| Piège | Descriptif | Exemple |
|---------|-------------|---------|
| **Biais variable omis** | Ne pas contrôler un facteur de confusion | Estimation de l'éducation → gains sans contrôle des capacités |
| **Surcontrôle** | Conditionnement sur médiateur ou collisionneur | Contrôler le titre du poste lors de l'estimation de l'éducation → gains |
| **Biais de sélection** | Conditionnement sur une variable affectée par le traitement | Analyser uniquement les personnes employées lors d'études de formation → salaires |
| **Biais du temps immortel** | Mauvaise classification du temps-personne dans les études de cohorte | Les patients doivent survivre suffisamment longtemps pour recevoir un traitement |
| **Régression vers la moyenne** | Les valeurs extrêmes ont tendance à se rapprocher de la moyenne | Les patients malades s'améliorent malgré le traitement |
| **Biais post-traitement** | Conditionnement sur des variables qui surviennent après le traitement | Contrôle des événements indésirables lors de l'estimation de l'efficacité des médicaments |
---

## Outils et bibliothèques
| Outil | Langue | Descriptif |
|------|----------|-------------|
| **FairePourquoi** | Python | Bibliothèque Microsoft ; Inférence causale basée sur DAG |
| **CasalML** | Python | Bibliothèque d'Uber pour la modélisation d'uplift et le ML causal |
| **ÉconML** | Python | Double ML, forêts causales, variables instrumentales |
| **modèles linéaires** | Python | IV, modèles de données de panel, DiD |
| **MatchIt** | R | Correspondance du score de propension |
| **dagitté** | R/Web | Analyse DAG ; identifier les ensembles d'ajustement |
| **Impact causal** | R/Python | Série temporelle structurelle bayésienne pour l'inférence causale |
---

## Résumé
L'inférence causale consiste à aller au-delà de « ce qui s'est passé » et à « ce qui se serait passé si les choses avaient été différentes ». Le défi fondamental est que nous ne pouvons jamais observer à la fois les résultats traités et non traités pour la même unité – le contrefactuel est toujours manquant. Les expériences randomisées résolvent ce problème en rendant les groupes de traitement et les groupes témoins comparables. Lorsque la randomisation n'est pas possible, des méthodes quasi expérimentales – DiD, discontinuité de régression, variables instrumentales, contrôle synthétique – tentent de reconstruire le contrefactuel à partir de données d'observation. Les DAG aident à expliciter les hypothèses et à identifier les bonnes variables à contrôler. La compétence clé consiste à réfléchir attentivement au processus de génération de données : qu'est-ce qui cause quoi, qu'est-ce qu'un facteur de confusion, qu'est-ce qu'un collisionneur et ce qui se serait passé dans l'alternative.