---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
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

# Mécanique classique
La mécanique classique décrit le mouvement d'objets sous l'influence de forces. Des pommes qui tombent aux planètes en orbite, des cordes vibrantes aux particules qui entrent en collision, ses principes régissent le monde macroscopique. Au-delà de ses applications physiques, la mécanique classique a donné naissance au calcul des variations, à la géométrie symplectique et au cadre hamiltonien qui sous-tend la mécanique quantique et l'optimisation moderne.
---

## Mécanique newtonienne
### Les trois lois de Newton
| Droit | Déclaration | Forme mathématique |
|-----|-----------|-------------------|
| **Premier (Inertie)** | Un objet reste au repos ou en mouvement uniforme à moins qu'il ne soit soumis à une force | Si F_net = 0, alors v = constante |
| **Deuxième (F = ma)** | La force est égale à la masse multipliée par l'accélération | **F** = m**a** = m(d²**x**/dt²) |
| **Troisième (Action-Réaction)** | Chaque action a une réaction égale et opposée | **F**₁₂ = −**F**₂₁ |
### Diagrammes du corps libre
Un **diagramme du corps libre** isole un objet et montre toutes les forces agissant sur lui.
**Forces communes :**
| Forcer | Formule | Itinéraire |
|-------|---------|---------------|
| Gravité (près de la Terre) | F = mg | Vers le bas |
| Force normale | N | Perpendiculaire à la surface |
| Friction (statique) | f_s ≤ µ_s N | S'oppose à une motion imminente |
| Friction (cinétique) | f_k = μ_k N | S'oppose au mouvement |
| Printemps (loi de Hooke) | F = −kx | Restaurer (vers l’équilibre) |
| Tensions | T | Le long de la ficelle/corde |
| Faites glisser | F_d = ½C_d ρAv² | S'oppose à la vitesse |
### Exemple concret : bloquer sur une inclinaison
Un bloc de masse m sur une pente sans frottement à un angle θ.
- Forces : gravité (mg vers le bas), force normale (N perpendiculaire à la surface)
- Décomposer la gravité : mg sin θ (le long de la pente), mg cos θ (dans la surface)
- N = mg cos θ (pas de mouvement perpendiculaire à la surface)
- Accélération le long de la pente : a = g sin θ
---

## Méthodes énergétiques
### Travail et énergie cinétique
**Travail** effectué par une force : W = ∫ **F** · d**r**
**Théorème travail-énergie :** W_net = ΔKE = ½mv₂² − ½mv₁²
### Énergie potentielle
| Forcer | Énergie potentielle | Remarques |
|-------|-------|-------|
| Gravité (près de la surface) | U = mgh | h = hauteur au-dessus de la référence |
| Gravité (général) | U = −GMm/r | Zéro à l'infini |
| Printemps | U = ½kx² | x = déplacement par rapport à l'équilibre |
| Électrostatique | U = kq₁q₂/r | Charges similaires : U positif |
### Conservation de l'énergie
Si seules des forces conservatrices agissent : E = KE + PE = constante
½mv₁² + U₁ = ½mv₂² + U₂
**Exemple concret :** Une balle est tombée d'une hauteur h.
- Initiale : KE = 0, PE = mgh
- Juste avant de toucher sol : KE = ½mv², PE = 0
- Conservation : mgh = ½mv² → v = √(2gh)
### Pouvoir
P = dW/dt = **F** · **v** (taux de travail)
---

## Momentum et collisions
### Moment linéaire
**p** = m**v**
Deuxième loi de Newton (forme alternative) : **F** = d**p**/dt
### Conservation de l'élan
S'il n'y a pas de forces extérieures : la quantité de mouvement totale est conservée.
| Type de collision | KE conservé ? | L’élan conservé ? |
|--------------------|---------------|---------------|
| **Élastique** | Oui | Oui |
| **Inélastique** | Non | Oui |
| **Parfaitement inélastique** | Non (perte maximale) | Oui (les objets collent ensemble) |
**Collision élastique 1D :** Deux masses m₁, m₂ de vitesses initiales u₁, u₂ :
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Moment angulaire
**L** = **r** × **p** = m(**r** × **v**)
Couple : **τ** = d**L**/dt = **r** × **F**
**Conservation :** En l'absence de couple externe, le moment cinétique est conservé.
---

## Mécanique lagrangienne
La formulation **Lagrangienne** remplace les forces par l'énergie, offrant un cadre plus élégant et général.
### Le Lagrangien
L = T − V (énergie cinétique moins énergie potentielle)
### Principe de moindre action (principe de Hamilton)
Le chemin réel emprunté par un système entre les instants t₁ et t₂ minimise (plus précisément, rend stationnaire) l'**action** :
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Équations d'Euler-Lagrange
La condition δS = 0 donne :
d/dt(∂L/∂q̇) − ∂L/∂q = 0
pour chaque coordonnée généralisée q.
**Exemple pratique :** Pendule simple (longueur l, masse m, angle θ par rapport à la verticale).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange : ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Avantages de la mécanique lagrangienne
| Avantage | Explication |
|---------------|-------------|
| Indépendant des coordonnées | Fonctionne dans n'importe quel système de coordonnées |
| Gère les contraintes naturellement | Pas besoin de calculer les forces de contrainte |
| Symétrie → conservation | Le théorème de Noether relie les symétries aux quantités conservées |
| Se généralise facilement | Aux champs, relativité, mécanique quantique |
---

## Mécanique hamiltonienne
La formulation **Hamiltonienne** est une reformulation de la mécanique lagrangienne qui utilise des positions et des impulsions (au lieu de positions et de vitesses).
### L'hamiltonien
H = Σᵢ pᵢq̇ᵢ − L = T + V (pour la plupart des systèmes mécaniques)
où pᵢ = ∂L/∂q̇ᵢ sont les **impulsions généralisées**.
### Les équations de Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Il s'agit de 2n ODE du premier ordre (vs n équations d'Euler-Lagrange du second ordre).
**Exemple pratique :** Oscillateur harmonique (masse m, constante du ressort k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (comme prévu)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (loi de Hooke)
### Supports de Poisson
Pour les fonctions f(q, p) et g(q, p) :
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Propriété | Déclaration |
|--------------|---------------|
| Evolution temporelle | df/dt = {f, H} + ∂f/∂t |
| Conservation | f est conservé ssi {f, H} = 0 (et ∂f/∂t = 0) |
| Supports fondamentaux | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Connexion à la mécanique quantique :** Les crochets de Poisson deviennent des commutateurs : {f, g} → (1/iℏ)[f̂, ĝ]
---

## Lois de conservation et théorème de Noether
### Théorème de Noether
Toute symétrie continue du lagrangien correspond à une quantité conservée.
| Symétrie | Quantité conservée |
|----------|---------|
| Traduction invariance temporelle | Énergie |
| Traduction spatiale | Moment linéaire |
| Invariance rotationnelle | Moment angulaire |
| Invariance de jauge | Charge électrique |
C’est l’un des résultats les plus profonds de toute la physique : il relie la géométrie de l’espace-temps aux lois fondamentales de conservation.
---

## Dynamique des corps rigides
Un **corps rigide** est un objet où toutes les distances internes restent fixes.
### Concepts clés
| Concepts | Formule | Descriptif |
|---------|---------|-------------|
| **Moment d'inertie** | I = Σmᵢrᵢ² ou I = ∫r² dm | Résistance à l'accélération de rotation |
| **KE rotatif** | KE = ½Iω² | Énergie de rotation |
| **Moment angulaire** | L = jeω | Analogue rotationnel de p = mv |
| **Couple** | τ = Iα | Analogue rotationnel de F = ma |
### Moments d'inertie (formes courantes)
| Forme | Axe | Je |
|-------|------|---|
| Sphère solide | Par le centre | (2/5)MR² |
| Sphère creuse | Par le centre | (2/3)MR² |
| Cylindre plein | Le long de l'axe | (1/2)MR² |
| Tige fine | Traversant le centre, perpendiculaire | (1/12)ML² |
| Tige fine | Extrémité traversante, perpendiculaire | (1/3)ML² |
| Disque | Traversant le centre, perpendiculaire | (1/2)MR² |
---

## Mécanique orbitale
### Lois de Kepler
| Droit | Déclaration |
|-----|-----------|
| **Premier (Ellipses)** | Les planètes se déplacent selon des ellipses avec le Soleil au même foyer |
| **Deuxième (Zones égales)** | Une ligne allant du Soleil à la planète balaie des zones égales en des temps égaux |
| **Troisième (harmonique)** | T² ∝ a³ (période au carré proportionnelle au demi-grand axe au cube) |
### Énergie orbitale
E = ½mv² − GMm/r
| E | Type d'orbite |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hyperbolique (non lié) |
### Vitesse de fuite
v_escape = √(2GM/R)
Pour la Terre : v_escape ≈ 11,2 km/s
---

## Pertinence pour l'apprentissage automatique et la science des données
| Notion de mécanique | Demande |
|-----------------|-------------|
| Les lois de Newton | Moteurs physiques dans les simulations, l'IA des jeux, la robotique |
| Méthodes énergétiques | Modèles basés sur l'énergie, réseaux Hopfield, machines Boltzmann |
| Mécanique lagrangienne | Réseaux de neurones basés sur la physique, contrôle optimal, optimisation de trajectoire |
| Mécanique hamiltonienne | Réseaux de neurones hamiltoniens (HNN), intégrateurs symplectiques pour la simulation |
| Lois de conservation | Biais inductifs dans les modèles ML, réseaux de neurones équivariants |
| Théorème de Noether | Apprentissage automatique prenant en compte la symétrie, apprentissage profond géométrique |
| Dynamique des corps rigides | Simulation robotique, dynamique moléculaire, animation 3D |
| Mécanique orbitale | Positionnement par satellite (GPS pour ML basé sur la localisation), conception de missions spatiales |
| Espace des phases (Hamiltonien) | Comprendre les systèmes dynamiques, les réseaux d'attracteurs |
| Calcul des variations | Transport optimal, modélisation générative (flow matching) |
---

## Résumé
| Cadre | Équation de base | Force |
|-----------|--------------|--------------|
| Newtonien | **F** = merde** | Analyse de force intuitive et directe |
| Lagrangien | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Sans coordonnées, gère les contraintes |
| Hamiltonien | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Structure symplectique, se connecte à QM |
| Lois de conservation | Théorème de Noether | Connexion profonde symétrie-conservation |
La mécanique classique ne consiste pas seulement à faire tomber des balles et à balancer des pendules. Ses cadres mathématiques – la mécanique lagrangienne et hamiltonienne – comptent parmi les idées les plus influentes de toute la science. Ils se généralisent à la mécanique quantique, à la théorie des champs et même à l’apprentissage automatique moderne, où les modèles basés sur l’énergie et les réseaux neuronaux basés sur la physique s’appuient directement sur ces formulations vieilles de plusieurs siècles.