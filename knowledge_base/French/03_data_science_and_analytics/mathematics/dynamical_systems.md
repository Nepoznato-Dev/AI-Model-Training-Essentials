---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Systèmes dynamiques
Un **système dynamique** décrit comment un état évolue dans le temps selon une règle fixe. Des orbites planétaires à la dynamique des populations, des conditions météorologiques à la formation des réseaux neuronaux, la théorie des systèmes dynamiques fournit le langage et les outils nécessaires pour comprendre comment les choses changent. Ce fichier couvre les équations différentielles ordinaires (ODE), les équations aux dérivées partielles (PDE), l'analyse de stabilité, le chaos et les bifurcations.
---

## Équations différentielles ordinaires (ODE)
Une ODE relie une fonction à ses dérivées par rapport à une seule variable indépendante (généralement le temps).
###Classement
| Propriété | Types |
|--------------|-------|
| **Commander** | Dérivée la plus élevée présente (1er ordre, 2e ordre, etc.) |
| **Linéaire ou non linéaire** | Linéaire : y'' + p(t)y' + q(t)y = g(t); Non linéaire : tout le reste |
| **Homogène** | g(t) = 0 (pas de terme de forçage) |
| **Autonome** | Aucune dépendance temporelle explicite : dy/dt = f(y) |
| **Coefficients constants** | p, q sont des constantes |
### ODE de premier ordre
**Forme générale :** dy/dt = f(t, y)
| Tapez | Formulaire | Méthode de résolution |
|------|------|-----------------|
| Séparable | dy/dt = g(t)h(y) | Séparer et intégrer : ∫dy/h(y) = ∫g(t)dt |
| Linéaire du premier ordre | dy/dt + p(t)y = q(t) | Facteur d'intégration : μ(t) = e^(∫p dt) |
| Exact | M(t,y)dt + N(t,y)dy = 0 avec ∂M/∂y = ∂N/∂t | Trouver la fonction potentielle F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Remplacez v = y^(1−n) pour linéariser |
**Exemple pratique (facteur d'intégration) :** Résolvez dy/dt + 2y = e^(−t), y(0) = 1.
- Facteur d'intégration : μ(t) = e^(∫2 dt) = e^(2t)
- Multiplier : d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Intégrer : e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Condition initiale : y(0) = 1 → 1 = 1 + C → C = 0
- Solution : y(t) = e^(−t)
### EDO linéaires du second ordre
**Forme générale :** ay'' + by' + cy = g(t)
**Cas homogène** (g ​​= 0) : Résolvez l'équation caractéristique ar² + br + c = 0.
| Discriminant | Racines | Solution générale |
|-------------|-------|--------|
| b² > 4ac (suramorti) | Deux réels distincts r₁, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (amortissement critique) | Racine réelle répétée r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (sous-amorti) | Racines complexes α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Interprétation physique :** Un système masse-ressort-amortisseur mx'' + bx' + kx = 0.
- Suramortisseur : amortissement important, pas d'oscillation (ferme-porte)
- Amortissement critique : retour le plus rapide sans oscillation (objectif de conception de suspension de voiture)
- Underdamped : oscille avec une amplitude décroissante (corde de guitare)
### Systèmes d'ODE
De nombreux systèmes réels impliquent plusieurs variables en interaction :
dx/dt = f(x, y)
dy/dt = g(x, y)
Cela peut s'écrire sous forme vectorielle : d**x**/dt = **F**(**x**)
**Systèmes linéaires :** d**x**/dt = A**x**, où A est une matrice.
La solution dépend des valeurs propres de A :
| Valeurs propres | Comportement |
|-------------|-----------|
| À la fois réel et négatif | Nœud stable (toutes les trajectoires convergent vers l'origine) |
| À la fois réel et positif | Nœud instable |
| Signes réels et opposés | Point de selle (instable) |
| Partie réelle complexe et négative | Spirale stable (oscillation amortie) |
| Partie réelle complexe et positive | Spirale instable |
| Pur imaginaire | Centre (orbites fermées) |
---

## Portraits de phases
Un **portrait de phase** visualise les trajectoires d'un système dynamique dans l'espace d'état (sans résolution explicite).
### Principales fonctionnalités
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Point fixe (équilibre)** | Où dx/dt = 0 (pas de mouvement) |
| **Trajectoire** | Chemin tracé par le système dans l'espace d'état |
| **Clinaison nulle** | Courbe où la dérivée d'une composante est nulle |
| **Cycle limite** | Orbite fermée isolée (oscillation auto-entretenue) |
| **Bassin d'attraction** | Ensemble de conditions initiales conduisant à un attracteur donné |
| **Séparatrice** | Frontière entre différents bassins d'attraction |
### Modèle prédateur-proie (Lotka-Volterra)
dx/dt = αx − βxy (proie)
dy/dt = δxy − γy (prédateur)
**Points fixes :**
1. (0, 0) - extinction (point de selle)
2. (γ/δ, α/β) — coexistence (centre — orbites fermées)
Le système présente des oscillations périodiques : les proies augmentent → les prédateurs augmentent → les proies diminuent → les prédateurs diminuent → les répétitions du cycle.
---

## Analyse de stabilité
### Stabilité linéaire
Pour un point fixe x*, linéarisez autour de lui : soit u = x − x*, alors du/dt ≈ J(x*)u où J est la matrice jacobienne.
**Critère de stabilité :** Le point fixe est :
- **Stable** si toutes les valeurs propres de J ont des parties réelles négatives
- **Instable** si une valeur propre a une partie réelle positive
- **Marginalement stable** si les valeurs propres n'ont aucune partie réelle (nécessite une analyse non linéaire)
### Stabilité de Lyapunov
**Méthode directe de Lyapunov** détermine la stabilité sans linéarisation.
Une **fonction de Lyapunov** V(x) satisfait :
1. V(x*) = 0 et V(x) > 0 pour x ≠ x* (défini positif)
2. dV/dt ≤ 0 le long des trajectoires (non croissant)
| État | Conclusion |
|---------------|------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Instable |
**Exemple pratique :** Système dx/dt = −x + y², dy/dt = −y.
- Essayez V(x,y) = x² + y² (fonction de type énergétique)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Proche de l'origine : dV/dt ≈ −2x² − 2y² < 0 (pour y petit, le −2y² domine)
- Conclusion : l'origine est localement asymptotiquement stable
---

## Théorie du chaos
Le **chaos** est déterministe mais imprévisible : le système suit des règles exactes, mais d'infimes différences dans les conditions initiales conduisent à des résultats très différents.
### Conditions requises pour le chaos
| Propriété | Descriptif |
|--------------|-------------|
| Déterministe | Pas de hasard – régi par des équations exactes |
| Sensible aux conditions initiales | Les trajectoires proches divergent de façon exponentielle |
| Délimité | Les trajectoires ne s'échappent pas vers l'infini |
| Non périodique | Ne se répète jamais exactement |
### Le système Lorenz
L’exemple classique du chaos déterministe :
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz
Avec paramètres standards σ = 10, ρ = 28, β = 8/3 :
- Le système comporte trois points fixes, tous instables
- Les trajectoires tournent autour d'un point fixe, puis passent soudainement à l'autre
- Le résultat est l'**attracteur de Lorenz** — un étrange attracteur à structure fractale
**Exposant de Lyapunov :** Mesure le taux de divergence des trajectoires proches.
- Exposant de Lyapunov positif → chaos
- Pour système de Lorenz avec paramètres standards : plus grand exposant ≈ 0,9 > 0
### La carte logistique
Un système discret simple qui présente le chaos :
x_{n+1} = rx_n(1 − x_n)
| Paramètre r | Comportement |
|-------------|-----------|
| 0 < r < 1 | La population disparaît (x → 0) |
| 1 < r < 3 | Point fixe stable à x = 1 − 1/r |
| 3 < r < 3,449 | Oscillation de période 2 |
| 3,449 < r < 3,544 | Oscillation de période 4 |
| 3,544 < r < 3,570 | Période-8, 16, 32, ... (cascade de doublement de période) |
| r ≈ 3,570 | Début du chaos |
| 3,570 < r < 4 | Généralement chaotique, avec des fenêtres périodiques |
| r = 4 | Complètement chaotique sur [0, 1] |
### Effet papillon
Nom populaire désignant la dépendance sensible aux conditions initiales. Dans les systèmes météorologiques (modélisés par les équations de Lorenz), un papillon battant des ailes au Brésil pourrait déclencher une tornade au Texas – non pas parce que le papillon en est la cause, mais parce que de minuscules perturbations augmentent de façon exponentielle.
---

## Théorie des bifurcations
Une **bifurcation** est un changement qualitatif dans le comportement du système lorsqu'un paramètre varie.
### Types de bifurcations
| Bifurcation | Forme normale | Que se passe-t-il |
|-------------|-------------|--------------|
| **Nœud de selle** | dx/dt = r − x² | Deux points fixes apparaissent/disparaissent |
| **Transcritique** | dx/dt = rx − x² | Stabilité d'échange à deux points fixes |
| **Pitchfork (supercritique)** | dx/dt = rx − x³ | Un point stable se divise en deux stables + un instable |
| **Pitchfork (sous-critique)** | dx/dt = rx + x³ | Effondrement de branches instables (souvent catastrophique) |
| **Hop** | Système 2D | Le point fixe devient instable, le cycle limite apparaît |
### Diagramme de bifurcation
Un tracé de points fixes en fonction de la valeur du paramètre, montrant la stabilité (solide = stable, pointillé = instable). Le diagramme de bifurcation de la carte logistique révèle la voie du doublement des périodes vers le chaos et la fameuse **constante de Feigenbaum** δ ≈ 4,669 (rapport universel entre les intervalles de bifurcation successifs).
---

## Équations aux dérivées partielles (PDE)
Les PDE impliquent des fonctions de plusieurs variables et leurs dérivées partielles.
### Classification des PDE linéaires du second ordre
Pour Au_xx + 2Bu_xy + Cu_yy + ... = 0 :
| Tapez | État | Comportement | Exemple |
|------|-----------|---------------|---------|
| **Elliptique** | B² − CA< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Propagation des ondes, préserve les caractéristiques nettes | Équation d'onde : u_tt = c²u_xx |
### L'équation de la chaleur
∂u/∂t = α ∂²u/∂x²
Modélise la diffusion de la chaleur, la répartition de la population, la tarification des options (Black-Scholes).
| Propriété | Déclaration |
|--------------|---------------|
| Lissage | Les solutions deviennent instantanément fluides, même à partir de données initiales discontinues |
| Principe maximum | La température maximale se produit à la limite ou au moment initial |
| Réversibilité temporelle | Irréversible – ne peut pas reculer |
### L'équation des vagues
∂²u/∂t² = c² ∂²u/∂x²
Modèles de cordes vibrantes, sonores, ondes électromagnétiques.
| Propriété | Déclaration |
|--------------|---------------|
| Propagation | Les perturbations se déplacent à la vitesse c |
| Réversibilité | Réversible dans le temps |
| solution d'Alembert | u(x,t) = f(x−ct) + g(x+ct) (superposition of left/right waves) |
### L'équation de Laplace
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0
Les solutions (fonctions harmoniques) représentent la température en régime permanent, le potentiel électrostatique et le débit de fluide incompressible.
| Propriété | Déclaration |
|--------------|---------------|
| Propriété à valeur moyenne | u(x₀) = moyenne de u sur n'importe quel cercle centré en x₀ |
| Principe maximum | Pas de maximum ou de minimum intérieur |
| Unicité | Déterminé entièrement par les conditions aux limites |
---

## Pertinence pour l'apprentissage automatique et la science des données
| DS-Concept | Demande |
|---------------|-------------|
| ODE | ODE neuronales (réseaux à profondeur continue), dynamique de réseau récurrente |
| Analyse de stabilité | Dynamique d'entraînement de descente de gradient (la perte diminue-t-elle de manière stable ?) |
| Fonctions de Lyapunov | Prouver la convergence des algorithmes d'apprentissage et la stabilité de l'apprentissage par renforcement |
| Chaos | Comprendre la sensibilité des RNN (gradients qui disparaissent/explosent), prévisions météorologiques |
| Bifurcation | Transitions de phases dans l'apprentissage (grokking), changements de régime dans la dynamique de formation |
| PDE | Modèles de diffusion (modèles génératifs basés sur des scores), réseaux de neurones basés sur la physique |
| Équation de chaleur | Processus de diffusion en modélisation générative, lissage graphique laplacien |
| Équation d'onde | Traitement des données sismiques, modélisation du signal audio |
| Lotka-Volterra | Dynamique des populations, épidémiologie, agents ML concurrents |
| Portraits de phases | Visualiser la dynamique du paysage des pertes et comprendre la formation GAN |
---

## Résumé
| Sujet | Idée de base | Outil clé |
|-------|-----------|--------------|
| ODE | Fonctions et leurs dérivées temporelles | Équations caractéristiques, facteurs d'intégration |
| Systèmes d'ODE | Plusieurs variables en interaction | Analyse des valeurs propres du jacobien |
| Portraits de phases | Visualiser la dynamique dans l'espace d'état | Points fixes, lignes nulles, cycles limites |
| Stabilité | Le système reviendra-t-il à l’équilibre ? | Linéarisation, fonctions de Lyapunov |
| Chaos | Imprévisibilité déterministe | Exposants de Lyapunov, attracteurs étranges |
| Bifurcations | Modifications qualitatives avec paramètres | Formes normales, diagrammes de bifurcation |
| PDE | Fonctions de plusieurs variables | Chaleur, vagues et équations de Laplace |
La théorie des systèmes dynamiques est la mathématique du changement. Cela explique pourquoi certains systèmes s’installent, pourquoi certains oscillent et pourquoi certains se comportent de manière chaotique. Pour les data scientists, il fournit des outils pour comprendre la dynamique de formation, concevoir des algorithmes stables, modéliser des séries temporelles et créer la prochaine génération de modèles d'apprentissage automatique basés sur la physique.