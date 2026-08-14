---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Méthodes numériques
Les méthodes numériques constituent le pont entre la théorie mathématique et le calcul pratique. Alors que les mathématiques pures prouvent que des solutions existent, les méthodes numériques calculent en réalité des réponses approximatives avec une précision finie. Chaque modèle d'apprentissage automatique, simulation physique et pipeline d'analyse de données repose en fin de compte sur le calcul numérique. Comprendre ces méthodes (leur précision, leur stabilité et leurs limites) est essentiel pour créer des logiciels fiables.
---

## Arithmétique à virgule flottante
Les ordinateurs représentent des nombres réels avec une précision finie. La **norme IEEE 754** définit la manière dont les nombres à virgule flottante sont stockés et manipulés.
### Formats IEEE 754
| Formater | Morceaux | Exposant | Mantisse | Chiffres décimaux approximatifs | Gamme |
|--------|------|----------|--------------|-------------------------------|-------|
| Moitié (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Simple (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Double (fp64) | 64 | 11 | 52 | 15.9 | ±1,8 × 10³⁰⁸ |
### Machine Epsilon
**Machine epsilon** (ε_mach) est le plus petit nombre tel que 1 + ε_mach > 1 en virgule flottante.
| Formater | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Pièges courants
| Piège | Exemple | Conséquence |
|---------|---------|-------------|
| **Annulation catastrophique** | Informatique (1 + x) − 1 pour les petits x | Perte de chiffres significatifs |
| **Absorption** | 10⁸ + 1 = 10⁸ en fp32 | De petites valeurs perdues en grosses sommes |
| **Non-associativité** | (une + b) + c ≠ une + (b + c) | L'ordre de somme compte |
| **Division par près de zéro** | 1 / 10⁻³⁰⁰ → débordement | Infini ou NaN |
### Stratégies d'atténuation
| Stratégie | Descriptif |
|--------------|-------------|
| **Résumé Kahan** | Somme compensée pour réduire l'erreur d'absorption |
| **Kahan-Babuska-Neumaier** | Version améliorée de la sommation de Kahan |
| **Résumé trié** | Additionnez d'abord les petits nombres pour éviter l'absorption |
| ** Arithmétique double-double ** | Utilisez des paires de doubles pour une précision étendue |
| **Analyse conditionnelle** | Comprendre si le problème lui-même amplifie les erreurs |
---

## Recherche de racine
Trouver x tel que f(x) = 0.
### Méthode de bissection
| Propriété | Valeur |
|--------------|-------|
| Nécessite | f continue, f(a) et f(b) sont de signes opposés |
| Convergence | Linéaire (l'erreur divise par deux chaque étape) |
| Garanti? | Oui — converge toujours |
| Itérations pour les chiffres d | ≈ d / log₁₀(2) ≈ 3,32d |
**Algorithme :**
1. Commencez par l'intervalle [a, b] où f(a) · f(b) < 0
2. Calculer le point médian c = (a + b) / 2
3. Si f(c) = 0 ou |b − a| < tolérance, arrête
4. Si f(a) · f(c) < 0, définissez b = c; sinon, définissez a = c
5. Répétez
### Méthode Newton-Raphson
| Propriété | Valeur |
|--------------|-------|
| Nécessite | f différentiable, f'(x) ≠ 0 à la racine |
| Convergence | Quadratique (près de la racine) |
| Garanti? | Non – peut diverger ou faire un cycle |
| Règle de mise à jour | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Exemple pratique :** Trouvez √2 en résolvant f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (corriger à 8 décimales)
### Méthode sécante
Comme la méthode de Newton mais se rapproche de la dérivée :
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Propriété | Valeur |
|--------------|-------|
| Convergence | Superlinéaire (ordre ≈ 1,618, le nombre d'or) |
| Nécessite | Deux suppositions initiales (aucune dérivée nécessaire) |
### Comparaison des méthodes de recherche de racine
| Méthode | Convergence | Dérivé nécessaire ? | Garanti? | Coût par étape |
|--------|-------------|---------|-------------|---------------|
| Bisection | Linéaire (1) | Non | Oui | 1 évaluation de fonction |
| Newton-Raphson | Quadratique (2) | Oui | Non | 2 évaluations de fonctions |
| Sécante | Superlinéaire (1,618) | Non | Non | 1 évaluation de fonction |
| Méthode de Brent | Superlinéaire | Non | Oui | Varie |
**La méthode de Brent** combine la bissection (convergence garantie) avec une interpolation quadratique sécante/inverse (convergence rapide). C'est le chercheur de racine par défaut dans la plupart des bibliothèques numériques.
---

## Intégration numérique (Quadrature)
Calcul de ∫ₐᵇ f(x) dx environ.
### Méthodes
| Méthode | Formule | Erreur | Commander |
|--------|---------|-------|-------|
| **Rectangle (milieu)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapézoïdal** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Les Simpsons 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Les Simpsons 3/8** | Utilise 4 points équidistants | O(h⁴) | 4 |
| **Quadrature gaussienne** | Placement optimal des nœuds | O(h²ⁿ) | n points |
### Règles composites
Pour n sous-intervalles de largeur h = (b−a)/n :
| Règle | Formule composite | Erreur |
|------|---------|-------|
| Trapézoïdal composite | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Composite Simpson | h/3[f(a) + 4Σf(impair) + 2Σf(pair) + f(b)] | O(h⁴) |
**Exemple pratique :** Calculez ∫₀¹ e^(−x²) dx en utilisant un trapèze composite avec n = 4.
- h = 0,25, points : 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Valeur vraie : ≈ 0,7468 (erreur ≈ 0,5%)
### Quadrature adaptative
Subdivise automatiquement les intervalles où la fonction varie rapidement, en utilisant moins de points là où elle est fluide. C'est ce qu'utilise`scipy.integrate.quad`(basé sur QUADPACK).
---

##Interpolation
Estimation des valeurs entre des points de données connus.
### Méthodes
| Méthode | Descriptif | Douceur | Oscillations |
|--------|-------------|------------|-------------|
| **Voisin le plus proche** | Utiliser le point de données le plus proche | Discontinu | Aucun |
| **Linéaire** | Relier les points avec des lignes droites | C⁰ (continu) | Aucun |
| **Polynôme (Lagrange)** | Polynôme unique passant par tous les points | C^∞ | Sévère sur de nombreux points (phénomène de Runge) |
| **Spline cubique** | Cube par morceaux, lisse aux joints | C² | Minime |
| **Fonction de base radiale** | Somme pondérée des noyaux radiaux | Dépend du noyau | Faible |
### Interpolation de Lagrange
Étant donné n+1 points (x₀, y₀), ..., (xₙ, yₙ), l'unique polynôme de degré ≤ n passant par tous les points :
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Phénomène de Runge :** L'interpolation polynomiale de haut degré en des points équidistants peut osciller énormément près des bords. Atténué en utilisant des nœuds ou des splines de Chebyshev.
### Splines cubiques
Polynômes cubiques par morceaux qui sont C² continus (dérivées secondes continues).
| Tapez | Condition aux limites |
|------|---------|
| Cannelure naturelle | S''(x₀) = S''(xₙ) = 0 |
| Cannelure serrée | S'(x₀) et S'(xₙ) spécifiés |
| Pas un nœud | Dérivée troisième continue en x₁ et xₙ₋₁ |
---

## Solveurs ODE
Résolution numérique des équations différentielles ordinaires dy/dt = f(t, y).
### Méthode d'Euler
Le solveur ODE le plus simple.
**Mise à jour :** y_{n+1} = y_n + h · f(t_n, y_n)
| Propriété | Valeur |
|--------------|-------|
| Commander | 1 (erreur par étape : O(h²), global : O(h)) |
| Stabilité | Conditionnellement stable (petit h requis) |
| Coût | 1 évaluation de fonction par étape |
### Méthodes Runge-Kutta
| Méthode | Commander | Étapes | Remarques |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Le plus simple |
| **Milieu** | 2 | 2 | Meilleure précision |
| **Heun (RK2)** | 2 | 2 | Prédicteur-correcteur |
| **Classique RK4** | 4 | 4 | Cheval de bataille standard |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Taille de pas adaptative (utilisée dans ode45) |
### Classic RK4 (Runge-Kutta d'ordre 4)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Propriété | Valeur |
|--------------|-------|
| Commander | 4 (erreur globale : O(h⁴)) |
| Coût | 4 évaluations de fonctions par étape |
| Stabilité | Bien mieux qu'Euler |
| Utilisation | Par défaut pour les ODE non rigides |
### ODE rigides
Une ODE **rigide** comporte des composants qui varient sur des échelles de temps très différentes. Les méthodes explicites (Euler, RK4) nécessitent des pas peu pratiques.
| Méthode | Tapez | Stabilité |
|--------|------|---------------|
| Euler implicite | Implicite | A-stable (inconditionnellement stable) |
| Formule de différenciation vers l'arrière (BDF) | Implicite | A-stable (jusqu'à l'ordre 5) |
| Runge-Kutta implicite | Implicite | Des variantes L-stables existent |
| LSODA | Automatique | Bascule entre rigide/non rigide |
---

## Stabilité numérique et conditionnement
### Numéro de condition
Le **numéro de condition** mesure dans quelle mesure le résultat d'un problème change par rapport à de petits changements dans l'entrée.
Pour un système linéaire Ax = b : κ(A) = ||A|| · ||A⁻¹||
| κ(UNE) | Interprétation |
|-------|--------------------|
| ≈ 1 | Bien conditionné |
| 10³ | Légèrement sensible |
| 10⁸ | Mauvais conditionnement (perte d'environ 8 chiffres de précision) |
| → ∞ | Singulier (pas de solution unique) |
### Stabilité des algorithmes
Un algorithme est **numériquement stable** si de petites perturbations en entrée entraînent de petites perturbations en sortie (par rapport au numéro de condition du problème).
| Algorithme | Écurie? | Remarques |
|-----------|---------|-------|
| Élimination gaussienne avec pivotement partiel | Oui | Approche standard |
| Calcul des valeurs propres via QR | Oui | Rétro-stable |
| Somme naïve (grand + petit en premier) | Non | Utiliser la sommation Kahan |
| Calcul de la variance comme E[X²] − (E[X])² | Potentiellement non | Utiliser l'algorithme en ligne de Welford |
### Algorithme en ligne de Welford
Calcul numériquement stable de la moyenne mobile et de la variance :
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Cela évite l’annulation catastrophique qui se produit dans la formule naïve en deux passes.
---

## Pertinence pour l'apprentissage automatique et la science des données
| Méthode numérique | Demande |
|-----------------|-------------|
| Virgule flottante (fp16/fp32/bf16) | Entraînement à précision mixte, quantification de modèles, efficacité mémoire |
| Recherche de racine | Estimation du maximum de vraisemblance (trouver où gradient = 0) |
| Intégration numérique | Inférence bayésienne (calcul des vraisemblances marginales), valeurs attendues |
| Interpolation | Lissage, imputation, modèles de substitution, fonctions d'activation |
| Solveurs ODE | ODE neuronales, RNN en temps continu, dynamique des populations, ML basé sur la physique |
| Numéro d'état | Comprendre les problèmes numériques en régression linéaire, équations normales |
| Somme stable | Calcul des fonctions de perte, statistiques de normalisation par lots |
| RK4 / solveurs adaptatifs | Simulation de systèmes dynamiques, formation de réseaux en profondeur continue |
---

## Résumé
| Sujet | Idée de base | Méthode clé |
|-------|-----------|------------|
| Virgule flottante | Représentation de précision finie | IEEE 754, résumé de Kahan |
| Recherche de racine | Résoudre f(x) = 0 | Bisection, Newton-Raphson, Brent |
| Intégration numérique | ∫f(x)dx approximatif | Trapézoïdale, Simpson, quadrature gaussienne |
| Interpolation | Estimation entre les points de données | Splines cubiques, Lagrange, RBF |
| Solveurs ODE | Résoudre dy/dt = f(t,y) | Euler, RK4, méthodes adaptatives |
| Stabilité | Sensibilité aux erreurs d'arrondi | Numéro de condition, algorithmes stables |
Les méthodes numériques sont le point où les mathématiques rencontrent la réalité. Aucun ordinateur ne peut représenter exactement la plupart des nombres réels, aucune dérivée n'est calculée symboliquement dans la pratique et aucune intégrale n'est évaluée sous forme fermée pour des problèmes du monde réel. Comprendre les méthodes numériques vous permet de choisir le bon algorithme, de prédire sa précision et d'éviter les bugs subtils résultant de l'arithmétique à précision finie.