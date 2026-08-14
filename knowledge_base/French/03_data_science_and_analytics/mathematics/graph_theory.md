---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Théorie des graphes
Un **graphe** est une structure mathématique constituée de sommets (nœuds) reliés par des arêtes (liens). Les graphiques modélisent les relations : réseaux sociaux, feuilles de route, réseaux de neurones, dépendances, canaux de communication. La théorie des graphes – l'étude de ces structures – fournit des algorithmes et des théorèmes qui sont au cœur de l'informatique, de la recherche opérationnelle et de la science des données.
---

## Concepts fondamentaux
### Définitions
| Terme | Définition | Notations |
|------|------------|--------------|
| **Graphique** | Une paire G = (V, E) de sommets et d'arêtes | G |
| **Sommet (nœud)** | Un élément de V | v, vous, w |
| **Bord** | Une connexion entre deux sommets | e = (u, v) ou {u, v} |
| **Commander** | Nombre de sommets | \|V\| = n |
| **Taille** | Nombre d'arêtes | \|E\| = m |
| **Diplôme** | Nombre d'arêtes incidentes à un sommet | degré(v) |
| **Chemin** | Séquence de sommets distincts reliés par des arêtes | v₁, v₂, ..., vₖ |
| **Cycle** | Un chemin qui commence et se termine au même sommet | v₁ → v₂ → ... → vₖ → v₁ |
| **Connecté** | Un chemin existe entre chaque paire de sommets | — |
| **Composant** | Un sous-graphe connecté maximal | — |
| **Sous-graphique** | Un graphe formé à partir d'un sous-ensemble de V et E | H ⊆ G |
### Types de graphiques
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Non dirigé** | Les bords n'ont aucune direction | Réseau d'amitié |
| **Réalisé (digraphe)** | Les bords ont une direction (arcs) | Liens vers des pages Web |
| **Pondéré** | Les arêtes portent des valeurs numériques | Distances routières |
| **Non pondéré** | Toutes les arêtes sont équivalentes | Liens sociaux |
| **Simple** | Pas de boucles, pas de bords multiples | La plupart des graphiques de manuels |
| **Multigraphe** | Plusieurs arêtes entre les mêmes sommets autorisées | Itinéraires de vol (vols multiples entre villes) |
| **Complet** | Chaque paire de sommets est connectée | Kₙ a n(n−1)/2 arêtes |
| **Bipartite** | Sommets divisés en deux groupes ; arêtes uniquement groupes transversaux | Matrices de recommandation d'éléments utilisateur |
| **Planaire** | Peut être dessiné sans croisement de bords | Dispositions de circuits imprimés |
| **Arbre** | Graphique connecté et acyclique | Arbres de décision, systèmes de fichiers |
| **DAG** | Cycles dirigés, non dirigés | Planification des tâches, graphiques de dépendances |
### Le lemme de la poignée de main
La somme de tous les degrés des sommets est égale à deux fois le nombre d’arêtes :
Σᵥ deg(v) = 2|E|
**Corollaire :** Chaque graphique a un nombre pair de sommets de degré impair.
**Exemple :** Dans un groupe de 10 personnes où tout le monde serre la main d'exactement 3 autres : Σ deg = 30, donc |E| = 15 poignées de main au total.
---

## Représentations graphiques
La manière dont vous stockez un graphique en mémoire détermine l’efficacité de chaque algorithme que vous exécutez dessus.
| Représentation | Espace | Recherche de bord | Itérer les voisins | Idéal pour |
|----------------|-------|-------------|----------|--------------|
| **Matrice de contiguïté** | O(n²) | O(1) | O(n) | Graphiques denses, tests de bord rapides |
| **Liste de contiguïté** | O(n + m) | O(deg(v)) | O(deg(v)) | Graphiques clairsemés, la plupart des réseaux du monde réel |
| **Liste de bord** | O(m) | O(m) | O(m) | Algorithmes simples, MST de Kruskal |
| **Matrice d'incidence** | O(n·m) | O(m) | O(m) | Algorithmes spécialisés |
### Matrice de contiguïté
Une matrice n × n A où A[i][j] = 1 si l'arête (i,j) existe, 0 sinon. Pour les graphiques pondérés, A[i][j] = poids.
**Propriétés :**
- Symétrique pour les graphiques non orientés
- Aᵏ[i][j] = nombre de marches de longueur k de i à j
- Les valeurs propres de A révèlent des propriétés structurelles (voir Théorie des graphes spectraux)
### Liste de contiguïté
Un tableau (ou une carte de hachage) où chaque sommet v stocke une liste de ses voisins.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Il s'agit de la représentation la plus courante pour les graphiques du monde réel, qui sont généralement clairsemés (m ≪ n²).
---

## Arbres
Un **arbre** est un graphe connecté et acyclique non orienté. Une **forêt** est une union disjointe d'arbres.
### Propriétés des arbres
Pour un arbre à n sommets :
- Il a exactement n − 1 arêtes
- Il y a exactement un chemin entre deux sommets
- La suppression d'un bord le déconnecte
- L'ajout d'un bord crée exactement un cycle
### Types d'arbres
| Tapez | Descriptif | Demande |
|------|-------------|-------------|
| **Arbre enraciné** | Un sommet désigné comme racine | Systèmes de fichiers, organigrammes |
| **Arbre binaire** | Chaque nœud a au plus 2 enfants | BST, analyse d'expressions, arbres de décision |
| **Arbre équilibré** | La hauteur est O(log n) | Arbres AVL, arbres rouge-noir (bases de données) |
| **Arbre couvrant** | Sous-graphe qui inclut tous les sommets et est un arbre | Conception de réseaux, algorithmes d'approximation |
| **Arbre couvrant minimum** | Arbre couvrant avec un poids total minimum des bords | Conception de réseau, clustering |
| **Graphique en étoile** | Un nœud central connecté à tous les autres | Réseaux en étoile |
### Propriétés de l'arbre binaire
| Propriété | Formule |
|--------------|---------|
| Nombre maximum de nœuds à la profondeur d | 2ᵈ |
| Nombre maximum de nœuds dans l'arbre de hauteur h | 2ʰ⁺¹ − 1 |
| Hauteur minimale pour n nœuds | ⌊log₂(n)⌋ |
| Nœuds feuilles dans un arbre binaire complet | Nœuds internes + 1 |
### Traversées d'arbres
| Traversée | Commander | Cas d'utilisation |
|---------------|-------|--------------|
| **Précommande** | Racine → Gauche → Droite | Copie d'un arbre, expression de préfixe |
| **Dans l'ordre** | Gauche → Racine → Droite | Sortie triée de BST |
| **Post-commande** | Gauche → Droite → Racine | Suppression d'un arbre, expression postfixée |
| **Ordre de niveau (BFS)** | Niveau par niveau, de gauche à droite | Chemin le plus court dans un arbre non pondéré |
---

## Traversées de graphiques
Les algorithmes de traversée visitent systématiquement chaque sommet accessible.
### Recherche en largeur d'abord (BFS)
Explorez les sommets couche par couche, à l'aide d'une **file d'attente**.
| Propriété | Valeur |
|--------------|-------|
| Structure des données | File d'attente (FIFO) |
| Complexité temporelle | O(V+E) |
| Complexité spatiale | O(V) |
| Trouve le chemin le plus court ? | Oui (graphiques non pondérés) |
| Complet? | Oui (explore tous les sommets accessibles) |
**Algorithme :**
1. Commencez au sommet source s. Mark est visité. Mettre en file d'attente s.
2. Tant que la file d'attente n'est pas vide : retirez le sommet u de la file d'attente. Pour chaque voisin non visité v de u : marquez v visité, mettez v en file d'attente.
**Applications :** chemin le plus court dans les graphiques non pondérés, les composants connectés, les tests de bipartité, l'exploration du Web.
### Recherche en profondeur d'abord (DFS)
Explore le plus profondément possible avant de revenir en arrière, en utilisant une **pile** (ou récursivité).
| Propriété | Valeur |
|--------------|-------|
| Structure des données | Pile (LIFO) / récursion |
| Complexité temporelle | O(V+E) |
| Complexité spatiale | O(V) |
| Trouve le chemin le plus court ? | Non |
| Complet? | Oui (pour les graphes finis) |
**Algorithme :**
1. Commencez au sommet s. Mark est visité.
2. Pour chaque voisin non visité v de s : récursivement DFS à partir de v.
**DFS classe les arêtes en :**
- **Bords de l'arbre :** partie de l'arborescence DFS
- **Arêtes arrière :** connectent un sommet à son ancêtre (indiquent les cycles)
- **Arêtes avant :** connectent un sommet à son descendant
- **Arêtes croisées :** reliez les sommets de différentes branches
**Applications :** tri topologique, détection de cycles, composants fortement connectés, résolution de labyrinthes.
### Comparaison BFS et DFS
| Critère | BFS | DFS |
|-----------|-----|-----|
| Stratégie | Large puis profond | Profond puis large |
| Mémoire | Supérieur (frontière des magasins) | Inférieur (chemin des magasins) |
| Chemin le plus court (non pondéré) | Garanti | Non garanti |
| À utiliser lorsque la solution est sur le point de démarrer | Mieux | Pire |
| À utiliser lorsque le graphique est très profond | Pire | Mieux |
| Tri topologique | Variante de l'algorithme de Kahn | Approche standard |
---

## Algorithmes de chemin le plus court
Trouver le chemin le plus court entre les sommets est l’un des problèmes graphiques les plus importants en pratique.
### L'algorithme de Dijkstra
Recherche les chemins les plus courts d'une source unique à tous les autres sommets d'un graphique avec des poids d'arête **non négatifs**.
| Propriété | Valeur |
|--------------|-------|
| Poids des bords | Doit être ≥ 0 |
| Temps (tas binaire) | O((V + E)logV) |
| Temps (tas de Fibonacci) | O(E + Vlog V) |
| Cupide? | Oui |
| Gère les poids négatifs ? | Non |
**Algorithme :**
1. Initialisez dist[s] = 0, dist[v] = ∞ pour tout v ≠ s. File d'attente prioritaire Q avec tous les sommets.
2. Tant que Q n'est pas vide : extrayez le sommet u avec une distance minimale. Pour chaque voisin v de u avec un poids de bord w : si dist[u] + w < dist[v], mettre à jour dist[v] = dist[u] + w.
**Exemple concret :**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algorithme Bellman-Ford
Gère les poids de bord **négatifs** et détecte les cycles négatifs.
| Propriété | Valeur |
|--------------|-------|
| Poids des bords | Any (détecte les cycles négatifs) |
| Complexité temporelle | O(V · E) |
| Complexité spatiale | O(V) |
| Gère les cycles négatifs ? | Oui (détecte et signale) |
**Algorithme :**
1. Initialisez dist[s] = 0, dist[v] = ∞ pour tout v ≠ s.
2. Répétez V − 1 fois : pour chaque arête (u, v) de poids w : si dist[u] + w < dist[v], mettez à jour dist[v].
3. Vérifiez les cycles négatifs : si un bord peut encore être détendu, un cycle négatif existe.
### Algorithme Floyd-Warshall
Trouve les chemins les plus courts entre **toutes les paires** de sommets.
| Propriété | Valeur |
|--------------|-------|
| Complexité temporelle | O(V³) |
| Complexité spatiale | O(V²) |
| Gère les poids négatifs ? | Oui (mais pas de cycles négatifs) |
| Approche | Programmation dynamique |
**Récurrence :** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) pour chaque sommet intermédiaire k.
### Guide de sélection d'algorithme
| Scénario | Algorithme |
|--------------|---------------|
| Source unique, pondérations non négatives | Dijkstra |
| Source unique, pondérations négatives possibles | Bellman-Ford |
| Toutes les paires, graphe dense | Floyd-Warshall |
| Toutes les paires, graphique clairsemé | Exécutez Dijkstra à partir de chaque sommet |
| Graphique non pondéré | BFS |
| DAG (pas de cycles) | Tri topologique + relaxation |
| A* (guidée heuristique) | Recherche A* (pour une recherche de chemin avec une bonne heuristique) |
---

## Arbres couvrant minimum
Un **arbre couvrant minimum (MST)** connecte tous les sommets avec un poids total minimum des arêtes.
### Propriétés
- Un MST a exactement n − 1 arêtes (pour n sommets)
- Un MST existe si le graphe est connecté
- Un graphique avec des poids de bord distincts a un MST unique
- MST satisfait la **propriété de coupe** : le bord de poids minimum traversant toute coupe appartient au MST
- MST satisfait la **propriété de cycle** : le bord de poids maximum dans aucun cycle n'appartient au MST
### L'algorithme de Kruskal
| Propriété | Valeur |
|--------------|-------|
| Stratégie | Greedy — ajoutez des bords par ordre de poids |
| Structure des données | Ensemble disjoint (union-find) |
| Complexité temporelle | O (E log E) |
| Idéal pour | Graphiques clairsemés |
**Algorithme :**
1. Triez tous les bords par poids.
2. Pour chaque arête (dans l'ordre) : si son ajout ne crée pas de cycle (vérifiez avec union-find), ajoutez-le au MST.
3. Arrêtez-vous lorsque n − 1 arêtes sont sélectionnées.
### L'algorithme de Prim
| Propriété | Valeur |
|--------------|-------|
| Stratégie | Greedy - faire pousser un arbre à partir d'un sommet de départ |
| Structure des données | File d'attente prioritaire (min-tas) |
| Complexité temporelle | O (E log V) avec tas binaire |
| Idéal pour | Graphiques denses |
**Algorithme :**
1. Commencez à partir de n’importe quel sommet. Marquez-le comme faisant partie du MST.
2. Ajoutez à plusieurs reprises l'arête de poids minimum reliant un sommet du MST à un sommet à l'extérieur de celui-ci.
3. Arrêtez-vous lorsque tous les sommets sont inclus.
### Applications MST
| Demande | Comment MST aide |
|-------------|--------------------|
| Conception de réseau | Poser un minimum de câbles/tuyaux pour connecter tous les emplacements |
| Regroupement | Supprimez les k − 1 arêtes MST les plus longues pour obtenir k clusters |
| Algorithmes d'approximation | 2-approximation pour le TSP métrique |
| Segmentation d'images | Regrouper les pixels par MST de similarité des couleurs |
| Élimination de fonctionnalités | Supprimez les fonctionnalités redondantes à l'aide du MST du graphique de corrélation |
---

## Flux réseau
Les problèmes de flux réseau modélisent le mouvement des ressources à travers un système.
### Définition du réseau de flux
Un **réseau de flux** est un graphe orienté avec :
- Un sommet **source** s (produit un flux)
- Un **puits** sommet t (consomme du flux)
- **Capacités** c(u,v) ≥ 0 sur chaque arête
- **Flux** f(u,v) satisfaisant :
  - **Contrainte de capacité :** 0 ≤ f(u,v) ≤ c(u,v)
  - **Conservation du flux :** flux entrant = flux sortant à chaque sommet sauf s et t
### Problème de débit maximum
Trouvez le débit total maximum de s à t.
**Méthode Ford-Fulkerson :**
1. Bien qu’il existe un chemin croissant de s à t dans le graphe résiduel :
2. Trouvez la capacité de goulot d'étranglement le long du chemin
3. Augmenter le débit le long du chemin du montant du goulot d'étranglement
4. Mettre à jour les capacités résiduelles
| Algorithme | Complexité temporelle | Remarques |
|---------------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) où f* est le débit maximum | Ne peut pas se terminer avec des capacités irrationnelles |
| Edmonds-Karp (BFS) | O(V · E²) | Se termine toujours, choisit le chemin d'augmentation le plus court |
| L'algorithme de Dinic | O(V² · E) | Utilise le blocage des flux ; O(V^(1/2) · E) pour les capacités unitaires |
### Théorème du débit maximum et de la coupe minimale
Le **débit maximum** de s à t est égal à la capacité de **coupe minimale** séparant s de t.
A **cut** (S, T) divise les sommets en S (contenant s) et T (contenant t). La capacité de coupe est la somme des capacités des bords de S à T.
**Applications du débit maximum :**
- Matching bipartite (affecter les travailleurs aux emplois)
- Segmentation d'image (séparer le premier plan de l'arrière-plan)
- Élimination du baseball (l'équipe X peut-elle encore gagner ?)
- Fiabilité du réseau (débit de données maximum)
### Correspondance bipartite via Max Flow
Étant donné un graphe biparti G = (L ∪ R, E) :
1. Ajoutez des sources avec des arêtes à tous les sommets de L (capacité 1)
2. Ajoutez un puits t avec les arêtes de tous les sommets de R (capacité 1)
3. Définissez toutes les capacités de bord d'origine sur 1.
4. Débit maximum = correspondance maximale
---

## Théorie des graphes spectraux
La théorie des graphes spectraux étudie les graphes à travers les valeurs propres et les vecteurs propres des matrices associées au graphe.
### Matrices clés
| Matrice | Définition | Ce qu'il capture |
|--------|------------|--------|
| **Matrice de contiguïté** A | A[i][j] = 1 si l'arête (i,j) existe | Modèle de connectivité |
| **Matrice de diplôme** D | Diagonale; D[i][i] = deg(i) | Importance des sommets par degré |
| **Laplacien** L = D − A | L[i][j] = −1 si arête, deg(i) sur la diagonale | Fluidité des fonctions sur graphique |
| **Laplacien normalisé** L_norm = D^(−1/2) L D^(−1/2) | Version invariante d'échelle | Structure communautaire |
### Valeurs propres du Laplacien
Le Laplacien L est semi-défini positif, donc toutes les valeurs propres sont ≥ 0.
| Valeur propre | Signification |
|------------|---------|
| λ₁ = 0 | Toujours zéro ; le vecteur propre est le vecteur constant |
| λ₂ (connectivité algébrique) | > 0 si le graphe est connecté ; plus grand = mieux connecté |
| Nombre de valeurs propres nulles | Égal au nombre de composants connectés |
| λₙ | Lié au degré maximum et à l'expansion du graphique |
### Applications des méthodes spectrales
| Demande | Méthode |
|-------------|--------|
| **Partitionnement de graphiques** | Utiliser les vecteurs propres de L pour diviser le graphique en parties équilibrées |
| **Détection communautaire** | Regroupement spectral : intégrez les sommets à l'aide des vecteurs propres inférieurs, puis regroupez |
| **PageRank** | Vecteur propre de la matrice d'adjacence (ou matrice de transition) du graphe web |
| **Dessin graphique** | Positionner les sommets à l'aide des vecteurs propres du Laplacien |
| **Apprentissage semi-supervisé** | Propager des étiquettes à l'aide du graphe Laplacien (propagation d'étiquettes) |
| **Réseaux de neurones graphiques** | Convolutions spectrales : filtrer les signaux sur des graphiques en utilisant les vecteurs propres de L |
### L'inégalité de Cheeger
Relie la deuxième valeur propre λ₂ à l'**expansion** du graphique (à quel point il est bien connecté) :
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
où h(G) est la constante de Cheeger (nombre isopérimétrique). Cela signifie que λ₂ mesure approximativement la difficulté de couper le graphique en deux morceaux – un élément clé pour le clustering.
---

## Structures de graphiques spéciales
| Graphique | Sommets | Bords | Propriétés |
|-------|----------|-------|------------|
| Terminer Kₙ | n | n(n−1)/2 | Chaque paire connectée ; diamètre 1 |
| Cycle Cₙ | n | n | 2-régulier ; connecté |
| Chemin Pₙ | n | n−1 | Arbre; diamètre n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-régulier ; diamètre k; bipartite |
| Bipartite complet K_{m,n} | m+n | m·n | Chaque sommet d'une partie se connecte à tous les autres |
| Graphique de Petersen | 10 | 15 | 3-régulier ; diamètre 2 ; pas planaire; pas de cycle hamiltonien |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept de graphique | Demande |
|---------------|-------------|
| BFS/DFS | Exploration du Web, analyse des réseaux sociaux, étiquetage des composants connectés |
| Dijkstra / A* | Planification d'itinéraire, recherche de chemin par l'IA de jeu, navigation robotique |
| Arbre couvrant minimum | Clustering (liaison unique), sélection de fonctionnalités, conception de réseau |
| Débit max / coupe min | Segmentation d'images, correspondance bipartite, attribution de recommandations |
| Méthodes spectrales | Regroupement spectral, réseaux de neurones graphiques, réduction de dimensionnalité (cartes propres laplaciennes) |
| Classement de page | Classement des moteurs de recherche, analyse d'influence sur les réseaux sociaux |
| DAG | Réseaux bayésiens, inférence causale, planification de tâches, graphiques de calcul en apprentissage profond |
| Graphiques bipartis | Matrices d'éléments utilisateur dans les systèmes de recommandation, marchés bifaces |
| Structures arborescentes | Arbres de décision, forêts aléatoires, clustering hiérarchique, navigation dans le système de fichiers |
| Représentations graphiques | Graphiques de connaissances (Wikidata, DBpedia), graphiques moléculaires (découverte de médicaments), réseaux de citations |
---

## Résumé
| Sujet | Idée de base | Algorithme clé / Résultat |
|-------|-----------|----------------------|
| Fondamentaux | Sommets, arêtes, degrés, chemins | Lemme de la poignée de main |
| Représentations | Comment stocker des graphiques | Matrice de contiguïté vs liste de contiguïté |
| Arbres | Graphiques acycliques connectés | n sommets → n−1 arêtes |
| Traversées | Exploration systématique des sommets | BFS (chemin le plus court), DFS (exploration profonde) |
| Chemins les plus courts | Itinéraires à poids minimum | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Arbre couvrant minimum | Le moyen le moins cher de connecter tous les sommets | Kruskal, Prim's |
| Flux de réseau | Débit maximal | Ford-Fulkerson, théorème de coupe min-débit maximum |
| Théorie spectrale | Les valeurs propres révèlent la structure | Valeurs propres laplaciennes, regroupement spectral |
La théorie des graphes est sans doute la branche des mathématiques la plus directement applicable à la science des données moderne. Les réseaux sociaux, les graphes de connaissances, les structures moléculaires, les graphes de calcul dans les cadres d'apprentissage profond, la résolution des dépendances, les systèmes de recommandation — tous sont fondamentalement des problèmes de graphes. Les algorithmes abordés ici ne sont pas seulement théoriques ; ils fonctionnent quotidiennement à grande échelle dans les systèmes de production.