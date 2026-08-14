---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Optimisation
L'optimisation est la mathématique consistant à trouver la meilleure solution à partir d'un ensemble de solutions réalisables. Il demande : étant donné une fonction et des contraintes, quelle entrée minimise (ou maximise) la sortie ? L'optimisation est le moteur de l'apprentissage automatique : former un modèle signifie minimiser une fonction de perte. Il apparaît dans la recherche opérationnelle, l’économie, la conception technique et pratiquement tous les domaines quantitatifs.
---

## Formulation du problème
Un **problème d'optimisation** général a la forme :
Réduire f(x)
Soumis à : gᵢ(x) ≤ 0 (contraintes d'inégalité), hⱼ(x) = 0 (contraintes d'égalité)
| Terme | Signification |
|------|--------------|
| **Fonction objectif** f(x) | La quantité à minimiser (ou maximiser) |
| **Variables de décision** x | Les valeurs que nous pouvons contrôler |
| **Région réalisable** | Ensemble de tous les x satisfaisant toutes les contraintes |
| **Minimum global** | Réalisable x* avec f(x*) ≤ f(x) pour tout réalisable x |
| **Minimum local** | Réalisable x* avec f(x*) ≤ f(x) pour tout x réalisable dans un quartier |
| **Problème convexe** | f est convexe, la région réalisable est un ensemble convexe (min local = min global) |
---

## Programmation linéaire (LP)
Lorsque l'objectif et toutes les contraintes sont **linéaires**, le problème est un programme linéaire.
### Formulaire standard
Réduire cᵀx
Sous réserve de : Ax ≤ b, x ≥ 0
où c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Propriétés
| Propriété | Déclaration |
|--------------|---------------|
| Convexité | LP est toujours un problème convexe |
| Solution optimale | Toujours à un sommet (point de coin) du polytope réalisable |
| Existence | Si la région réalisable est délimitée et non vide, une solution optimale existe |
| Optima multiples | Si deux sommets sont optimaux, chaque point sur l’arête qui les sépare est également optimal |
### La méthode simplexe
La **méthode simplex** (Dantzig, 1947) se déplace le long des bords du polytope réalisable de sommet en sommet, améliorant toujours l'objectif, jusqu'à atteindre l'optimum.
| Propriété | Valeur |
|--------------|-------|
| Dans le pire des cas | O(2ⁿ) (exponentiel — rare en pratique) |
| Durée moyenne du cas | Polynôme pour la plupart des problèmes pratiques |
| Idée clé | Déplacer vers le sommet adjacent avec une meilleure valeur d'objectif |
**Algorithme (aperçu) :**
1. Commencer par une solution réalisable de base (sommet du polytope)
2. Choisissez une variable entrante (celle qui améliore l'objectif)
3. Choisissez une variable de sortie (maintenir la faisabilité)
4. Pivot : passer au nouveau sommet
5. Répétez jusqu'à ce qu'aucune direction d'amélioration n'existe
### Méthodes de points intérieurs
Alternative au simplexe : approchez l’optimum depuis l’intérieur de la région réalisable.
| Propriété | Valeur |
|--------------|-------|
| Dans le pire des cas | Polynôme (O(n³·⁵) pour certaines variantes) |
| Performance pratique | Compétitif avec le simplexe sur les gros problèmes |
| Idée clé | Suivez un "chemin central" à travers l'intérieur |
### Exemple de LP travaillé
**Problème :** Une usine produit des chaises (x₁) et des tables (x₂).
- Bénéfice : 30$ par chaise, 50$ par table
- Bois : 2x₁ + 4x₂ ≤ 100 (pieds-planche disponibles)
- Main d'oeuvre : x₁ + 3x₂ ≤ 60 (heures disponibles)
- Maximiser : 30x₁ + 50x₂
**Solution (méthode graphique pour 2 variables) :**
- Sommets de la région réalisable : (0,0), (30,0), (40,10), (0,20)
- Évaluer l'objectif à chaque sommet :
  - (0,0) : bénéfice = 0
  - (30,0) : bénéfice = 900
  - (40,10) : profit = 1700 ← optimal
  - (0,20) : bénéfice = 1000
- **Optimal :** x₁ = 40 chaises, x₂ = 10 tables, profit = 1 700 $
---

## Optimisation convexe
Un problème est **convexe** si la fonction objectif est convexe et la région réalisable est un ensemble convexe.
### Ensembles et fonctions convexes
| Concepts | Définition |
|--------------|------------|
| **Ensemble convexe** | Pour tout x, y dans l'ensemble et t ∈ [0,1] : tx + (1−t)y est également dans l'ensemble |
| **Fonction convexe** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) pour tout t ∈ [0,1] |
| **Strictement convexe** | L'inégalité est stricte pour t ∈ (0,1) et x ≠ y |
**Propriété clé :** Pour l'optimisation convexe, chaque minimum local est un minimum global.
### Fonctions convexes courantes
| Fonction | Convexe? | Où |
|--------------|---------|-------|
| hache + b (linéaire) | Oui (et concave) | Partout |
| x² | Oui | ℝ |
| eˣ | Oui | ℝ |
| −log(x) | Oui | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Oui | ℝⁿ |
| max(f₁, f₂) si f₁, f₂ convexe | Oui | Intersection de domaines |
### Descente de dégradé
L'algorithme d'optimisation le plus fondamental de l'apprentissage automatique.
**Règle de mise à jour :** x_{k+1} = x_k − α∇f(x_k)
où α > 0 est le **taux d'apprentissage** (taille du pas).
| Variante | Mettre à jour la règle | Avantage |
|---------|-------------|---------------|
| **Lot GD** | x ← x − α∇f(x) | Convergence stable |
| **GD stochastique (SGD)** | x ← x − α∇fᵢ(x) (un échantillon) | Rapide par itération, échappe aux minima locaux |
| **Mini-lot SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Equilibre entre batch et stochastique |
| **Élan** | v ← βv − α∇f(x); X ← X + v | Accélère dans les régions plates |
| **Adam** | Taux d'apprentissage adaptatif par paramètre | Fonctionne bien dès le départ pour l'apprentissage en profondeur |
| **RMSprop** | Échelle du taux d'apprentissage en fonction de la moyenne courante de l'ampleur du gradient | Bon pour les RNN |
### Taux de convergence
| Méthode | Convexe f | Fortement convexe f |
|--------|----------|---------|
| Descente de gradient | O(1/k) | O((1−μ/L)ᵏ) (linéaire) |
| SGD | O(1/√k) | O(1/k) |
| GD accéléré (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
où k = nombre d'itérations, μ = paramètre de forte convexité, L = constante de Lipschitz.
### Choisir le taux d'apprentissage
| Stratégie | Descriptif |
|--------------|-------------|
| α fixe | Simple mais peut diverger (trop grand) ou converger lentement (trop petit) |
| Recherche de ligne | Trouver α qui minimise f(x − α∇f(x)) le long de la direction du gradient |
| Calendriers de décroissance | α_t = α₀ / (1 + βt) ou α_t = α₀ · βᵗ |
| Échauffement | Commencez petit, augmentez, puis décroissez (courant dans la formation des transformateurs) |
| Adaptatif (Adam) | Taux d'apprentissage par paramètre basés sur des statistiques de gradient |
---

## Optimisation contrainte
### Multiplicateurs de Lagrange
Pour le problème : minimiser f(x) sous réserve de h(x) = 0.
**Lagrangien :** L(x, λ) = f(x) + λh(x)
A l'optimum : ∇ₓL = 0 et ∇_λL = 0 (ce qui donne h(x) = 0).
**Exemple pratique :** Minimisez f(x,y) = x² + y² sous réserve de x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Contrainte : x + y = 1 → −λ = 1 → λ = −1
-Solution : x = 1/2, y = 1/2, f = 1/2
### Conditions KKT
Les **conditions de Karush-Kuhn-Tucker (KKT)** généralisent les multiplicateurs de Lagrange aux contraintes d'inégalité.
Pour : minimiser f(x) sous réserve de gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrangien :** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Conditions KKT** (nécessaires pour l'optimalité) :
| État | Équation |
|-----------|----------|
| Stationnarité | ∇ₓL = 0 |
| Faisabilité initiale | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Double faisabilité | λᵢ ≥ 0 |
| Laxisme complémentaire | λᵢgᵢ(x) = 0 pour tout i |
**Slackness complémentaire** signifie : si la contrainte gᵢ n'est pas active (gᵢ(x) < 0), alors λᵢ = 0 (la contrainte n'affecte pas la solution).
Pour les problèmes convexes satisfaisant la condition de Slater, les conditions KKT sont à la fois nécessaires et suffisantes.
---

## Dualité
Chaque problème d'optimisation (le **primal**) est associé à un problème **double**.
### Dualité faible et forte
| Concepts | Déclaration |
|---------|-----------|
| **Double fonction** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Double problème** | Maximiser g(λ, ν) sous réserve de λ ≥ 0 |
| **Faible dualité** | Double optimal ≤ Primal optimal (tient toujours) |
| **Forte dualité** | Double optimal = Primal optimal (est valable pour les problèmes convexes avec la condition de Slater) |
| **Écart de dualité** | Primal optimal - Dual optimal (zéro sous forte dualité) |
### Pourquoi la dualité est importante
| Demande | Comment la dualité aide |
|-------------|---------|
| Limites inférieures | Dual donne un certificat sur la qualité de la solution primale |
| SVM | Le double problème SVM conduit à l'astuce du noyau |
| Analyse de sensibilité | Les variables doubles mesurent dans quelle mesure l'optimum change si les contraintes sont assouplies |
| Décomposition | Les gros problèmes peuvent être divisés en sous-problèmes plus petits via le double |
---

## Programmation en nombres entiers
Lorsque certaines ou toutes les variables doivent être des **entiers**, le problème devient beaucoup plus difficile (NP-difficile en général).
###Type
| Tapez | Descriptif |
|------|-------------|
| Propriété intellectuelle pure | Toutes les variables doivent être des entiers |
| IP mixte (MIP) | Certaines variables sont entières, d'autres continues |
| IP binaire | Variables limitées à {0, 1} |
### Méthodes de résolution
| Méthode | Idée |
|--------|------|
| **Branche et relié** | Diviser en sous-problèmes, résoudre les relaxations LP, tailler |
| **Plans de coupe** | Ajouter des contraintes linéaires pour resserrer la relaxation LP |
| **Branche et coupe** | Combiner branchement et reliure avec des plans de coupe |
| **Heuristique** | Recherche gourmande et locale, recuit simulé pour des solutions approximatives |
---

## Méthodes heuristiques et métaheuristiques
Lorsque l’optimisation exacte est insoluble, les heuristiques trouvent de bonnes solutions (pas nécessairement optimales).
| Méthode | Idée clé | Idéal pour |
|--------|----------|--------------|
| **Descente en pente** | Suivez la descente la plus raide | Fonctions fluides et différenciables |
| **Méthode de Newton** | Utiliser des informations de second ordre (courbure) | Problèmes fluides et bien conditionnés |
| **Recuit simulé** | Accepter des solutions pires avec une probabilité décroissante | Optimisation globale, combinatoire |
| **Algorithmes génétiques** | Faire évoluer une population par sélection, croisement, mutation | Multi-objectifs, non différenciables |
| **Essaim de particules** | Les agents explorent l'espace, influencés par les positions les plus connues | Continu, non convexe |
| **Optimisation bayésienne** | Construire un modèle de substitution, utiliser la fonction d'acquisition | Fonctions coûteuses de boîte noire (réglage des hyperparamètres) |
### Méthode d'optimisation de Newton
**Règle de mise à jour :** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
où H est la matrice hessienne (matrice des dérivées secondes).
| Propriété | Valeur |
|--------------|-------|
| Taux de convergence | Quadratique (presque optimal) |
| Coût par itération | O(n³) pour l'inversion hessienne |
| Nécessite | Hesse définie positive, deux fois différentiable |
| Quasi-Newton (BFGS) | Hesse approximative à partir de dégradés | O(n²) par itération |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept d'optimisation | Demande |
|-----------|-------------|
| Descente de gradient | Réseaux de neurones d'entraînement, régression logistique, tout modèle différenciable |
| SGD et variantes | ML à grande échelle (formation mini-batch), apprentissage en ligne |
| Adam, RMSprop | Optimiseurs par défaut pour le deep learning |
| Optimisation convexe | SVM, régression logistique, LASSO, Ridge (optimum global garanti) |
| Multiplicateurs de Lagrange | Apprentissage contraint, ML équitable, allocation des ressources |
| Conditions KKT | Dérivation du dual SVM, compréhension de l'activité des contraintes |
| Dualité | Astuce du noyau SVM, analyse de sensibilité, méthodes de décomposition |
| Programmation linéaire | Allocation de ressources, optimisation de portefeuille, flux réseau |
| Programmation entière | Sélection de fonctionnalités (binaires), planification, problèmes combinatoires |
| Optimisation bayésienne | Réglage des hyperparamètres (Optuna, Hyperopt) |
| Newton/quasi-Newton | Méthodes du second ordre pour les problèmes petits à moyens (L-BFGS) |
---

## Résumé
| Méthode | Type de problème | Garanties | Échelle |
|--------|-------------|------------|-------|
| Simplexe | Programmation linéaire | Optimum exact | Des millions de variables |
| Point intérieur | Convexe (LP, QP, SOCP) | Optimum exact | À grande échelle |
| Descente de gradient | Lisse sans contrainte | Converge vers le min local | Très grand (apprentissage profond) |
| SGD | Risque empirique à grande échelle | Converge (avec désintégration) | Ensembles de données massifs |
| Newton / BFGS | Lisse, deux fois différenciable | Convergence quadratique | Petit à moyen |
| KKT / Lagrange | Contraint (convexe) | Exact sous conditions | Moyen |
| Branché et relié | Programmation entière | Optimum exact | Petit à moyen |
| Heuristique | Tout (non convexe, combinatoire) | Aucune garantie | Varie |
L’optimisation est sans doute l’outil mathématique le plus important en apprentissage automatique. Chaque modèle que vous entraînez (de la régression linéaire aux grands modèles de langage) implique la résolution d'un problème d'optimisation. Comprendre quand un problème est convexe (optimum global garanti), quand la descente de gradient convergera et comment gérer les contraintes vous donne les bases théoriques pour concevoir, déboguer et améliorer des algorithmes d'apprentissage.