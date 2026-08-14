---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Structures de données et algorithmes
Les structures de données sont la manière dont nous organisons les données en mémoire afin que les opérations sur celles-ci soient efficaces. Les algorithmes sont des procédures étape par étape permettant de résoudre des problèmes. Ensemble, ils constituent le fondement de l’informatique : tous les programmes que vous avez utilisés en dépendent. Choisir la bonne structure de données peut transformer un programme incroyablement lent en un programme rapide, et connaître le bon algorithme peut transformer un problème insoluble en un problème trivial.
---

## Structures de données fondamentales
### Structures linéaires
| Structure | Accès | Rechercher | Insérer | Supprimer | Cas d'utilisation |
|-----------|--------|--------|--------|--------|----------|
| **Tableau** | O(1) par indice | O(n) | O(n) | O(n) | Collections à taille fixe ; accès aléatoire |
| **Liste chaînée** | O(n) | O(n) | O(1) en tête | O(1) en tête | Taille dynamique ; insertions/suppressions |
| **Pile** | O(n) | O(n) | O(1) pousser/pop | O(1) pop | Appels de fonction ; défaire; analyse |
| **File d'attente** | O(n) | O(n) | O(1) mise en file d'attente | O(1) retirer la file d'attente | Planification des tâches ; BFS ; files d'attente de messages |
| **Deque** | O(1) aux deux extrémités | O(n) | O(1) aux deux extrémités | O(1) aux deux extrémités | Fenêtre coulissante ; vol de travail |
### Structures basées sur le hachage
| Structure | Rechercher | Insérer | Supprimer | Cas d'utilisation |
|-----------|--------|--------|--------|--------------|
| **Table de hachage** | O(1) moyenne | O(1) moyenne | O(1) moyenne | Recherches de valeurs-clés ; caches ; ensembles |
| **Ensemble de hachage** | O(1) | O(1) | O(1) | Tests d'adhésion ; déduplication |
** Collisions de hachage ** : lorsque deux clés sont hachées vers le même emplacement, elles sont stockées dans une liste chaînée (chaînage) ou dans l'emplacement disponible suivant (adressage ouvert). De bonnes fonctions de hachage minimisent les collisions.
### Structures arborescentes
| Structure | Rechercher | Insérer | Supprimer | Cas d'utilisation |
|-----------|--------|--------|--------|--------------|
| **Arbre de recherche binaire** | O(log n) moyenne | O(logn) | O(logn) | Données triées ; requêtes de plage |
| **AVL / Arbre Rouge-Noir** | O(log n) garanti | O(logn) | O(logn) | Auto-équilibrage ; utilisé dans les cartes/ensembles |
| **Arbre B / Arbre B+** | O(logn) | O(logn) | O(logn) | Index de bases de données ; systèmes de fichiers |
| **Trie** | O(k) où k = longueur de clé | O(k) | O(k) | Saisie semi-automatique ; correspondance de préfixe |
| **Tas (binaire)** | O(n) | O(logn) | O(logn) | Files d'attente prioritaires ; planification |
### Représentations graphiques
| Représentation | Espace | Recherche de bord | Ajouter un bord | Itérer les voisins |
|---------------|-------|-------------|----------|-------------------|
| **Matrice de contiguïté** | O(V²) | O(1) | O(1) | O(V) |
| **Liste de contiguïté** | O(V+E) | O(degré) | O(1) | O(degré) |
| **Liste de bord** | O(E) | O(E) | O(1) | O(E) |
---

## Complexité de l'algorithme (Big-O)
La notation Big-O décrit comment les besoins en temps ou en espace d'un algorithme augmentent à mesure que la taille d'entrée augmente.
| Complexité | Nom | Exemple |
|---------------|------|--------------|
| **O(1)** | Constante | Recherche de table de hachage ; accès au tableau par index |
| **O(log n)** | Logarithmique | Recherche binaire ; opérations d'arbres équilibrées |
| **O(n)** | Linéaire | Recherche linéaire ; itérer un tableau |
| **O(n journal n)** | Linéarithmique | Tri par fusion ; tri en tas ; tris à usage général les plus efficaces |
| **O(n²)** | Quadratique | Tri à bulles ; boucles imbriquées sur les mêmes données |
| **O(2^n)** | Exponentiel | Génération de sous-ensembles par force brute ; Fibonacci récursif naïf |
| **O(n!)** | Factorielle | Voyageur de commerce (force brute); permutations |
### Idées fausses courantes
| Idée fausse | Réalité |
|--------------|---------|
| "O(n) est toujours plus rapide que O(n²)" | Pour n petit, le facteur constant compte davantage |
| "Un Big-O inférieur est toujours meilleur" | Des compromis spatio-temporels existent ; La recherche O(1) utilise la mémoire O(n) |
| "Big-O vous indique la vitesse exacte" | Il décrit le taux de croissance, pas le temps absolu |
---

## Algorithmes de tri
| Algorithme | Meilleur | Moyenne | Le pire | Espace | Stable | Sur place |
|-----------|------|---------|-------|-------|--------|----------|
| **Tri à bulles** | O(n) | O(n²) | O(n²) | O(1) | Oui | Oui |
| **Tri par insertion** | O(n) | O(n²) | O(n²) | O(1) | Oui | Oui |
| **Tri de sélection** | O(n²) | O(n²) | O(n²) | O(1) | Non | Oui |
| **Fusionner le tri** | O(n journal n) | O(n journal n) | O(n journal n) | O(n) | Oui | Non |
| **Tri rapide** | O(n journal n) | O(n journal n) | O(n²) | O(logn) | Non | Oui |
| **Tri en tas** | O(n journal n) | O(n journal n) | O(n journal n) | O(1) | Non | Oui |
| **Tim Trier** | O(n) | O(n journal n) | O(n journal n) | O(n) | Oui | Non |
**Conseils pratiques** : utilisez le tri intégré à votre langage (le`sorted()`de Python, le`Array.sort()`de JavaScript). Ils utilisent des algorithmes hautement optimisés (Tim Sort, Introsort) qui gèrent tous les cas extrêmes.
---

## Algorithmes de recherche
| Algorithme | Structure des données | Complexité | Exigence |
|-----------|---------------|---------------|-------------|
| **Recherche linéaire** | N'importe quel | O(n) | Aucun |
| **Recherche binaire** | Tableau trié | O(logn) | Les données doivent être triées |
| **Recherche dans une table de hachage** | Table de hachage | O(1) moyenne | Bonne fonction de hachage |
| **BFS** (recherche en largeur d'abord) | Graphique / arbre | O(V+E) | Chemin le plus court non pondéré |
| **DFS** (recherche en profondeur) | Graphique / arbre | O(V+E) | Recherche de chemin ; détection de cycles |
| **Dijkstra** | Graphique pondéré | O((V + E)logV) | Poids non négatifs ; chemin le plus court |
| **A* Recherche** | Graphique pondéré | O((V + E)logV) | Guidé par des heuristiques ; optimal avec heuristique admissible |
---

## Modèles d'algorithmes clés
| Modèle | Descriptif | Exemples de problèmes |
|---------|-------------|-----------------|
| ** Diviser pour mieux régner ** | Diviser le problème en sous-problèmes ; résoudre de manière récursive ; combiner | Tri par fusion ; tri rapide ; recherche binaire |
| **Programmation dynamique** | Divisez en sous-problèmes qui se chevauchent ; résultats du cache | Fibonacci ; sac à dos; sous-séquence commune la plus longue |
| **Gourmand** | Faire le choix localement optimal à chaque étape | celui de Dijkstra ; Codage de Huffman ; sélection d'activité |
| **Retour en arrière** | Essayez les possibilités ; annuler les mauvais choix ; essayez des alternatives | Solveur de Sudoku ; N-reines ; permutations |
| **Fenêtre coulissante** | Maintenir une fenêtre d'éléments ; faites-le glisser sur les données | Sous-tableau de somme maximale de taille K ; sous-chaîne la plus longue sans répétitions |
| **Deux pointeurs** | Utilisez deux pointeurs se déplaçant l'un vers l'autre ou dans la même direction | Somme de paire dans un tableau trié ; supprimer les doublons |
| **Recherche binaire sur la réponse** | Recherche binaire dans l'espace de réponse | Allouer un minimum de pages ; vaches agressives |
---

## Quand utiliser quoi
| Problème | Structure des données | Algorithme |
|---------|---------------|---------------|
| Recherche rapide de valeur-clé | Table de hachage/dictionnaire | Hachage |
| Maintenir l'ordre trié | BST équilibré (TreeMap, std::set) | Opérations sur les arbres |
| Traitement prioritaire | Tas/file d'attente prioritaire | Opérations sur le tas |
| Chemin le plus court (non pondéré) | Graphique (liste de contiguïté) | BFS |
| Chemin le plus court (pondéré) | Graphique (liste de contiguïté) | Dijkstra / A* |
| Test d'adhésion | Ensemble de hachage / filtre Bloom | Hachage |
| Correspondance de préfixe | Essayer | Trie traversée |
| Requêtes de plage | Arbre segmenté / Arbre Fenwick | Opérations sur les arbres |
| Cache LRU | Carte de hachage + liste doublement chaînée | Opérations combinées |
| Composants connectés | Union d'ensembles disjoints (Union-Recherche) | Union et recherche |
---

## Résumé
Les structures de données et les algorithmes ne sont pas seulement des sujets d'entretien : ils sont les éléments constitutifs d'un logiciel efficace. Les tableaux et les tables de hachage répondent à la plupart des besoins quotidiens. Les arbres et les graphiques gèrent des données hiérarchiques et relationnelles. Le tri et la recherche sont des problèmes résolus dans les bibliothèques standards. Les modèles algorithmiques – diviser pour mieux régner, programmation dynamique, gourmande, retour en arrière – sont des stratégies réutilisables pour résoudre de nouveaux problèmes. La compétence clé n’est pas la mémorisation des algorithmes ; il s'agit de reconnaître quel modèle correspond à un problème donné et de choisir la bonne structure de données pour le travail.