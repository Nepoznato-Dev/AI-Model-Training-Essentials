<!--
---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [graph, neural, networks, ai-and-machine-learning]
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

-->
# Graphiquer les réseaux de neurones
Les réseaux de neurones graphiques (GNN) sont des réseaux de neurones conçus pour fonctionner sur des données structurées en graphes – des réseaux de nœuds connectés par des bords. Alors que les réseaux de neurones traditionnels fonctionnent sur des grilles (images) ou des séquences (texte), les GNN gèrent des structures relationnelles arbitraires : réseaux sociaux, graphes moléculaires, graphes de connaissances, réseaux routiers, graphes de recommandations, etc. Ils sont devenus essentiels pour la découverte de médicaments, la détection des fraudes, les systèmes de recommandation et tout domaine où les relations entre entités sont importantes.
---

## Qu'est-ce qu'un graphique ?
| Composant | Descriptif | Exemple |
|---------------|-------------|---------|
| **Nœud (sommet)** | Une entité | Une personne, un atome de molécule, une ville |
| **Bord** | Une relation entre deux nœuds | Amitié, liaison chimique, route |
| **Poids des bords** | Force ou type de relation | Distance, similarité, capacité |
| **Fonctionnalités du nœud** | Attributs de chaque nœud | Âge, numéro atomique, population |
| **Fonctionnalités de pointe** | Attributs de chaque bord | Type de relation, distance |
| **Matrice de contiguïté** | Matrice A où A[i][j] = 1 si les nœuds i et j sont connectés | Encode la structure du graphe |
### Types de graphiques
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Non dirigé** | Les bords n'ont aucune direction | Réseau d'amitié |
| **Réalisé** | Les bords ont une direction (A → B ≠ B → A) | Abonnés Twitter |
| **Pondéré** | Les arêtes ont des valeurs numériques | Réseau routier avec distances |
| **Hétérogène** | Plusieurs types de nœuds et de bords | Graphique académique (articles, auteurs, lieux) |
| **Dynamique** | La structure du graphique change au fil du temps | Le réseau social évolue au fil du temps |
| **Bipartite** | Deux types de nœuds ; bords uniquement entre les types | Graphique de recommandation d'élément utilisateur |
---

## Pourquoi pas des réseaux de neurones réguliers ?
| Approche | Pourquoi ça échoue |
|--------------|-------------|
| **Réseau à réaction** | Nécessite une entrée de taille fixe ; les graphiques varient en taille et en structure |
| **CNN** | Suppose une structure de grille ; les graphiques n'ont pas de grille régulière |
| **RNN/Transformateur** | Suppose un ordre séquentiel ; les graphiques n'ont pas d'ordre naturel |
Les GNN résolvent ce problème en opérant directement sur la structure du graphe, en traitant chaque nœud dans le contexte de ses voisins.
---

## Architectures GNN de base
### Cadre de transmission des messages
La plupart des GNN suivent le même modèle : chaque nœud collecte les informations de ses voisins, les combine et met à jour sa propre représentation.
| Étape | Descriptif |
|------|-------------|
| **1. Message** | Chaque nœud envoie un message à ses voisins (en fonction de ses fonctionnalités actuelles) |
| **2. Agrégat** | Chaque nœud collecte et combine les messages de tous les voisins |
| **3. Mise à jour** | Chaque nœud met à jour sa propre représentation à l'aide du message agrégé |
| **4. Répéter** | Faites cela pour K couches → chaque nœud capture les informations à K sauts |
### Modèles GNN clés
| Modèle | Méthode d'agrégation | Innovation clé |
|-------|---------|----------------|
| **GCN** (réseau convolutionnel graphique) | Moyenne des caractéristiques voisines | Simple; efficace; motivation spectrale |
| **GraphiqueSAGE** | Échantillonner et regrouper ; peut utiliser la moyenne, le LSTM ou le pooling | Inductif (gère les nœuds invisibles); évolutif |
| **GAT** (Réseau d'attention graphique) | Agrégation de voisins pondérée par l'attention | Apprend quels voisins comptent le plus |
| **GIN** (Réseau d'isomorphisme graphique) | Somme des fonctionnalités voisines | Maximalement expressif ; peut distinguer tous les graphiques distinguables par le test WL |
| **MPNN** (réseau neuronal de transmission de messages) | Cadre général de transmission de messages | Unifie de nombreuses variantes de GNN |
### Comment fonctionne GCN (étape par étape)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Après K couches, la représentation de chaque nœud code les informations de K sauts dans le graphique.
---

## Tâches au niveau du graphique
| Tâche | Descriptif | Exemple |
|------|-------------|--------------|
| **Classification des nœuds** | Prédire l'étiquette de chaque nœud | Classer les utilisateurs comme robots ou humains |
| **Prédiction de lien** | Prédire si une arête existe (ou existera) | Prédire les relations manquantes ; recommander des connexions |
| **Classification des graphiques** | Prédire une étiquette pour l'ensemble du graphique | Classer les molécules comme toxiques ou non toxiques |
| **Détection communautaire** | Trouver des clusters de nœuds densément connectés | Identifier les groupes sociaux |
| **Génération de graphiques** | Générez de nouveaux graphiques avec les propriétés souhaitées | Concevoir de nouvelles molécules |
---

## Candidatures
### Découverte de médicaments et prédiction des propriétés moléculaires
| Tâche | Comment les GNN aident |
|------|--------------|
| **Prédiction des propriétés moléculaires** | Représenter les molécules sous forme de graphiques (atomes = nœuds, liaisons = bords) ; prédire la toxicité, la solubilité, l'affinité de liaison |
| **Interaction médicamenteuse** | Modéliser les médicaments et les cibles sous forme de graphique ; prédire les interactions indésirables |
| **Conception de médicaments de novo** | Générez de nouveaux graphiques moléculaires avec les propriétés souhaitées |
### Systèmes de recommandation
| Approche | Descriptif |
|--------------|-------------|
| **Graphique des éléments utilisateur** | Les utilisateurs et les éléments sont des nœuds ; les achats/vues sont des bords |
| **Filtrage collaboratif basé sur des graphiques** | Les GNN propagent les préférences à travers le graphique |
| **Recommandations relatives au graphique de connaissances** | Combinez les préférences de l'utilisateur avec la connaissance des éléments (genres, acteurs, réalisateurs) |
### Détection de fraude
| Demande | Structure du graphique |
|-------------|----------------|
| **Fraude financière** | Les transactions forment un graphique ; des modèles frauduleux émergent sous forme de structures de sous-graphes |
| **Fraude à l'assurance** | Les demandeurs, les prestataires et les polices forment un graphique ; des réseaux de fraudeurs sont détectés |
| **Reprises de comptes** | Les modèles de connexion forment un graphique ; connexions anormales signalent une compromission |
### Graphiques de connaissances
| Tâche | Descriptif |
|------|-------------|
| **Prédiction de lien** | Prédire les faits manquants (par exemple, "Paris est la capitale de ?") |
| **Résolution d'entité** | Déterminer si deux mentions font référence à la même entité |
| **Réponse aux questions** | Parcourez le graphique pour trouver des réponses |
---

## Concepts GNN avancés
### Lissage excessif
| Problème | Descriptif | Solutions |
|---------|-------------|--------------|
| **Sur-lissage** | Après plusieurs couches, toutes les représentations de nœuds deviennent similaires | Profondeur limite (2-4 couches); utiliser des connexions résiduelles ; utiliser les connaissances en matière de saut |
### Écrasement excessif
| Problème | Descriptif | Solutions |
|---------|-------------|--------------|
| **Sur-écrasement** | Les informations provenant de nœuds distants sont compressées en vecteurs de taille fixe | Utiliser des transformateurs graphiques ; mutualisation hiérarchique |
### Transformateurs graphiques
| Modèle | Caractéristique clé |
|-------|-------------|
| **Transformateur graphique** | Appliquer l'attention standard du Transformer à toutes les paires de nœuds |
| **GPS** (système d'invite graphique) | Combinez les couches GNN locales avec les couches Transformer globales |
| **Graphomètre** | Ajouter un codage positionnel basé sur la structure du graphique |
### Réseaux de graphes hétérogènes
| Modèle | Descriptif |
|-------|-------------|
| **R-GCN** | GCN relationnel ; différentes matrices de poids pour différents types d'arêtes |
| **HAN** | Réseau d'attention hétérogène ; attention aux différents types de nœuds et de bords |
| **HetGNN** | Réseau neuronal à graphes hétérogènes ; gère plusieurs types de nœuds |
---

## Évolutivité
| Défi | Solutions |
|-----------|----------|
| **Grands graphiques** (millions de nœuds) | Formation en mini-lots ; échantillonnage voisin |
| **Mémoire** | Partitionnement de graphiques sur les GPU |
| **Vitesse** | Opérations matricielles clairsemées ; bibliothèques spécialisées |
### Stratégies d'échantillonnage
| Stratégie | Descriptif |
|--------------|-------------|
| **Échantillonnage de nœuds** | Échantillonner un sous-ensemble de nœuds et leurs quartiers K-hop |
| **Échantillonnage de bord** | Exemples d'arêtes et les nœuds qu'ils connectent |
| **Échantillonnage en grappes** | Partitionnez le graphique en clusters ; s'entraîner sur les clusters |
| **Échantillonnage à pied aléatoire** | Échantillonner des nœuds via des marches aléatoires à partir de nœuds cibles |
---

## Outils et cadres
| Outil | Objectif |
|------|--------------|
| **PyTorch Géométrique (PyG)** | Bibliothèque GNN la plus populaire ; riche ensemble de modèles et d'ensembles de données |
| **DGL** (Bibliothèque de graphiques profonds) | Indépendant du framework ; prend en charge PyTorch, TensorFlow, MXNet |
| **RéseauX** | Algorithmes de graphes classiques ; manipulation de données |
| **OGB** (Open Graph Benchmark) | Repères et ensembles de données standard pour la recherche GNN |
| **CogDL** | Apprentissage profond pour les graphiques ; orienté recherche |
| **Spectral** | Bibliothèque GNN pour TensorFlow/Keras |
---

## Résumé
Les réseaux de neurones graphiques étendent l'apprentissage en profondeur aux données relationnelles : réseaux, molécules, graphiques de connaissances et tout système où les entités sont connectées. Ils fonctionnent en transmettant des messages entre voisins, permettant à chaque nœud d'apprendre de son contexte local. Les GNN ont trouvé leurs applications les plus importantes dans la découverte de médicaments, les systèmes de recommandation, la détection des fraudes et les graphiques de connaissances. Le domaine évolue vers des transformateurs de graphes, des graphes hétérogènes et une formation évolutive pour les réseaux massifs du monde réel. Si vos données ont des relations, les GNN valent probablement la peine d'être envisagés.