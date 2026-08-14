---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Processus stochastiques
Un **processus stochastique** est une collection de variables aléatoires indexées par le temps (ou l'espace). Alors que la théorie des probabilités étudie des événements aléatoires individuels, les processus stochastiques étudient la manière dont le caractère aléatoire évolue au fil du temps. Ils modélisent les cours des actions, les longueurs d’attente, la propagation des maladies, la génération de langage et la dynamique de formation des modèles d’apprentissage automatique.
---

## Fondations
### Définition
Un processus stochastique {X_t : t ∈ T} est une famille de variables aléatoires définies sur un espace de probabilité commun. T est l'**ensemble d'index** (heure) :
- **Temps discret :** T = {0, 1, 2, ...}
- **Temps continu :** T = [0, ∞)
L'**espace d'état** S est l'ensemble des valeurs possibles que X_t peut prendre.
### Propriétés clés
| Propriété | Définition |
|--------------|------------|
| **Stationnarité** | Distribution conjointe de (X_{t₁}, ..., X_{tₖ}) identique à (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Indépendance** | X_t indépendant de X_s pour t ≠ s |
| **Ergodicité** | Les moyennes temporelles convergent vers les moyennes d'ensemble |
| **Propriété Markov** | L'avenir ne dépend que du présent, pas du passé |
| **Martingale** | La valeur future attendue est égale à la valeur actuelle |
---

## Chaînes de Markov
Une **chaîne de Markov** est un processus stochastique où l'état futur dépend uniquement de l'état actuel (propriété sans mémoire).
### Chaînes de Markov à temps discret (DTMC)
P(X_{n+1} = j | X_n = je, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = je) = p_{ij}
La **matrice de transition** P a des entrées p_{ij} = P(aller à j | actuellement à i).
| Propriété | Déclaration |
|--------------|---------------|
| Sommes de lignes | Chaque ligne totalise 1 : Σⱼ p_{ij} = 1 |
| transition en n étapes | P(X_{n+m} = j | X_m = je) = (Pⁿ)_{ij} |
| Distribution stationnaire | πP = π (vecteur propre gauche de valeur propre 1) |
### Classification des États
| Terme | Définition |
|------|------------|
| **Récurrent** | La chaîne revient à l'état i avec une probabilité 1 |
| **Transitoire** | Probabilité non nulle de ne jamais revenir |
| **Absorbant** | p_{ii} = 1 (une fois entré, jamais quitté) |
| **Période** | GCD des heures de retour ; période 1 = apériodique |
| **Communiquer** | Les états i et j peuvent se joindre |
### Distribution stationnaire
Pour une chaîne de Markov irréductible et récurrente positive, la distribution stationnaire π existe, est unique et satisfait :
πP = π, Σᵢ πᵢ = 1
**Interprétation :** πᵢ = proportion à long terme du temps passé dans l'État i.
**Exemple pratique :** Modèle météo avec les états {Ensoleillé, Pluvieux}.
P = [[0.9, 0.1], [0.5, 0.5]] (lignes : de Sunny, de Rainy)
Distribution stationnaire : πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Résolution : π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Convergence vers la stationnarité
Pour une chaîne récurrente positive irréductible, apériodique :
- Pⁿ → Π (matrice avec toutes les lignes égales à π) comme n → ∞
- **Temps de mélange :** Nombre d'étapes jusqu'à ce que la distribution soit proche de π
- **Écart spectral :** 1 − |λ₂| (où λ₂ est la deuxième plus grande valeur propre) détermine la vitesse de mélange
### Chaînes de Markov en temps continu (CTMC)
Les transitions se produisent à des moments aléatoires régis par des distributions exponentielles.
| Concepts | Descriptif |
|---------|-------------|
| **Matrice de taux Q** | q_{ij} ≥ 0 pour je ≠ j ; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Probabilités de transition** | P(t) = e^{Qt} (matrice exponentielle) |
| **Distribution stationnaire** | πQ = 0 |
| **Temps de maintien** | Le temps dans l'état i est Exp(−q_{ii}) |
---

## Promenades aléatoires
Une **marche aléatoire** est un chemin formé d'étapes aléatoires successives.
### Marche aléatoire simple
X_n = X_{n-1} + Z_n, où Z_n ∈ {+1, −1} avec probabilités p, q = 1−p.
| Propriété | p = 1/2 (symétrique) | p ≠ 1/2 (biaisé) |
|----------|-----------|-------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Retours à l'origine ? | Oui (avec probabilité 1) | Non (s'éloigne) |
| Récurrent? | Oui (en 1D et 2D) | Non |
### Marche aléatoire dans des dimensions supérieures
| Dimensions | Récurrent? | Intuitions |
|---------------|------------|---------------|
| 1D | Oui | "Un homme ivre retrouve toujours le chemin du retour" |
| 2D | Oui | "Un oiseau ivre retrouve toujours le chemin de la maison" |
| 3D+ | Non | "Un moineau ivre ne retrouve jamais le chemin de sa maison" |
### Connexion au mouvement brownien
Mise à l'échelle d'une marche aléatoire : soit S_n = ΣZ_i. Puis comme taille de pas → 0 et pas → ∞ :
S_{⌊nt⌋} / √n → B(t) (mouvement brownien, par le théorème de Donsker)
---

## Mouvement brownien
**Mouvement brownien** (processus Wiener) B(t) est la limite de temps continu d'une marche aléatoire.
### Définition
B(t) satisfait :
1.B(0) = 0
2. B(t) a des chemins continus
3. Incréments indépendants : B(t) − B(s) est indépendant de B(s) − B(r) pour r < s < t
4. B(t) − B(s) ~ N(0, t − s) (incréments gaussiens)
### Propriétés clés
| Propriété | Déclaration |
|--------------|---------------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Nulle part différenciable | Les chemins sont continus mais n'ont pas de dérivée |
| Dimension fractale | Le graphique a une dimension Hausdorff 3/2 |
| Propriété de Markov | L'avenir ne dépend que de la position actuelle |
| Martingale | E[B(t) | F_s] = B(s) pour s < t |
### Mouvement brownien géométrique
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Il s’agit du modèle standard pour les cours boursiers dans le cadre Black-Scholes.
- μ : dérive (retour attendu)
- σ : volatilité
---

## Processus de Poisson
Un **processus Poisson** N(t) compte le nombre d'événements se produisant dans [0, t].
### Définition
N(t) ~ Poisson(λt), où λ est le taux (événements par unité de temps).
| Propriété | Déclaration |
|--------------|---------------|
| N(0) = 0 | — |
| Incréments indépendants | Les événements dans des intervalles disjoints sont indépendants |
| Incréments stationnaires | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Horaires inter-arrivées | Distribuée exponentiellement : T_i ~ Exp(λ) |
### Généralisations
| Variante | Descriptif |
|---------|-------------|
| **Non homogène** | Le taux λ(t) varie avec le temps |
| **Composé Poisson** | Chaque événement a une taille aléatoire : S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Mesure aléatoire de Poisson** | Points dans l'espace-temps, pas seulement dans le temps |
| **Multivarié** | Plusieurs types d'événements avec interactions possibles |
---

## Martingales
Une **martingale** est un jeu équitable : la valeur future attendue, compte tenu de toutes les informations actuelles, est égale à la valeur actuelle.
### Définition
{X_n} est une martingale par rapport à la filtration {F_n} si :
1. X_n est F_n-mesurable (adapté)
2. E[|X_n|] < ∞ (intégrable)
3. E[X_{n+1} | F_n] = X_n (jeu équitable)
| Variante | État | Interprétation |
|---------|-----------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Jeu équitable |
| **Sous-martingale** | E[X_{n+1} | F_n] ≥X_n | Jeu favorable (tendance à la hausse) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Jeu défavorable (tendance à la baisse) |
### Théorèmes clés
| Théorème | Déclaration |
|---------|-----------|
| **Arrêt facultatif** | Sous conditions, E[X_T] = E[X_0] pour un temps d'arrêt T |
| **Convergence** | Une martingale bornée converge presque sûrement |
| **Inégalité maximale** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |
---

## Méthodes de Monte Carlo
**Méthodes de Monte Carlo** utilisent un échantillonnage aléatoire pour estimer des quantités déterministes.
### Idée de base
Pour estimer E[f(X)] où X ~ P :
1. Tirez N échantillons : x₁, x₂, ..., x_N à partir de P
2. Calculer : Î = (1/N) Σᵢ f(xᵢ)
3. Par la loi des grands nombres : Î → E[f(X)] comme N → ∞
**Erreur :** Erreur standard = σ_f / √N, où σ_f² = Var[f(X)]
### Techniques de réduction des écarts
| Techniques | Idée | Accélération |
|---------------|------|--------------|
| **Échantillonnage important** | Échantillon de Q au lieu de P, poids par P/Q | Peut être dramatique |
| **Variantes antithétiques** | Utilisez des paires (x, −x) pour annuler la variance | ~2x |
| **Le contrôle varie** | Soustraire la fonction d'espérance connue corrélée à f | Varie |
| **Échantillonnage stratifié** | Divisez le domaine, échantillonnez chaque strate | Réduit la variance |
| **Rao-Blackwell** | Condition de statistiques suffisantes | Aide toujours |
---

## Chaîne de Markov Monte Carlo (MCMC)
MCMC construit une chaîne de Markov dont la distribution stationnaire est la distribution cible. Après une période de « déverminage », les échantillons se rapprochent des tirages de la cible.
### Algorithme Metropolis-Hastings
| Étape | Actions |
|------|--------|
| 1 | État actuel : x_t |
| 2 | Proposer : x* ~ q(x* \| x_t) (distribution des propositions) |
| 3 | Taux d'acceptation : α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Accepter avec probabilité α : x_{t+1} = x* (accepter) ou x_t (rejeter) |
**Cas particulier — Algorithme Metropolis :** Proposition symétrique q(x*|x) = q(x|x*), donc α = min(1, π(x*)/π(x_t)).
### Échantillonnage Gibbs
Un cas particulier de Metropolis-Hastings où chaque variable est mise à jour à partir de sa distribution conditionnelle complète.
Pour la cible π(x₁, x₂, ..., xₖ) :
1. Échantillon x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Échantillon x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Continuez pour toutes les variables
4. Répétez
| Propriété | Déclaration |
|--------------|---------------|
| Accepte toujours | α = 1 (pas d'étape de rejet) |
| Nécessite | Possibilité d'échantillonner chaque conditionnel complet |
| Convergence | Garanti pour les chaînes irréductibles et apériodiques |
### Diagnostic MCMC
| Diagnostique | Objectif |
|-----------|---------|
| **Trace du tracé** | Contrôle visuel du mélange et de la stationnarité |
| **Autocorrélation** | Mesure la dépendance à l'échantillon (vous souhaitez une faible autocorrélation) |
| **Gelman-Rubin (R̂)** | Comparez plusieurs chaînes ; R̂ < 1,05 suggère une convergence |
| **Taille effective de l'échantillon** | N_eff = N/(1 + 2Σρₖ) ; comptes pour l'autocorrélation |
| **Burn-in** | Jeter les échantillons initiaux avant que la chaîne n'atteigne la stationnarité |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Processus stochastique | Demande |
|---------|-------------|
| Chaînes de Markov | PageRank (marche aléatoire sur un graphique Web), génération de texte (modèles n-gram), MCMC |
| Promenades aléatoires | Node2Vec et DeepWalk (graph embeddings), exploration en RL |
| Mouvement brownien | Modélisation du cours des actions, modèles de diffusion en IA générative |
| Processus de Poisson | Modélisation des arrivées d'événements (clics, échecs), théorie des files d'attente |
| Martingales | Mathématiques financières, prouvant la convergence du SGD (approximation stochastique) |
| Monte-Carlo | Estimation des valeurs attendues, inférence bayésienne, apprentissage par renforcement (évaluation des politiques) |
| MCMC (Métropolis-Hastings) | Échantillonnage postérieur bayésien, programmation probabiliste (Stan, PyMC) |
| Échantillonnage Gibbs | Modèles thématiques (LDA), réseaux bayésiens, débruitage d'images |
| Diagnostic MCMC | Garantir une inférence fiable à partir de modèles probabilistes |
---

## Résumé
| Processus | Espace d'état | Temps | Propriété clé |
|---------|-------------|------|--------------|
| Chaîne de Markov | Discret/continu | Discret/continu | Sans mémoire (propriété Markov) |
| Promenade aléatoire | ℤᵈ | Discret | Somme de l'i.i.d. étapes |
| Mouvement brownien | ℝ | Continu | Incréments gaussiens, chemins continus |
| Processus de Poisson | ℕ | Continu | Processus de comptage avec écarts exponentiels |
| Martingale | ℝ | Discret/continu | Jeu équitable (E[X_{t+1}|F_t] = X_t) |
Les processus stochastiques sont les mathématiques du hasard au fil du temps. Ils sous-tendent l’inférence bayésienne moderne (MCMC), l’apprentissage par renforcement (processus de décision de Markov), la modélisation générative (modèles de diffusion), les mathématiques financières et la théorie des files d’attente. Comprendre ces processus vous donne les outils nécessaires pour modéliser l'incertitude de manière dynamique, non seulement sous forme d'instantané, mais au fur et à mesure de son évolution.