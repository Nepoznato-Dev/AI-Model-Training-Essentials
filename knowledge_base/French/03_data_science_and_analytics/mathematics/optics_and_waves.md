---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
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
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Optique et Ondes
Les ondes sont partout : le son, la lumière, l’eau, les signaux radio, les amplitudes de probabilité quantique, les fluctuations boursières et les vibrations des activations des réseaux neuronaux. L’optique – l’étude de la lumière – est la science ondulatoire la plus développée, et ses outils mathématiques (analyse de Fourier, interférence, diffraction) s’appliquent à tous les phénomènes ondulatoires. Comprendre les ondes est essentiel pour le traitement du signal, l’analyse d’images, les communications et la couche physique de toute technologie moderne.
---

## L'équation des vagues
### Équation générale des vagues
L'équation d'onde unidimensionnelle :
∂²u/∂t² = c² ∂²u/∂x²
où u(x,t) est le déplacement des vagues et c est la vitesse des vagues.
### Solution générale (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
où f est une onde se propageant vers la droite et g est une onde se propageant vers la gauche.
### Paramètres d'onde clé
| Paramètre | Symbole | Unité | Descriptif |
|---------------|--------|------|-------------|
| Amplitude | Un | varie | Déplacement maximal |
| Longueur d'onde | λ | mètres | Distance entre crêtes consécutives |
| Fréquence | f ou ν | Hertz (Hz) | Cycles par seconde |
| Période | T = 1/f | secondes | Temps pour un cycle complet |
| Numéro de vague | k = 2π/λ | rad/m | Fréquence spatiale |
| Fréquence angulaire | ω = 2πf | rad/s | Fréquence temporelle |
| Vitesse des vagues | c = fλ = ω/k | m/s | Vitesse de propagation |
### Onde sinusoïdale
u(x,t) = A sin(kx − ωt + φ)
où φ est la constante de phase.
### Vitesse des vagues dans différents médias
| Type d'onde | Moyen | Formule de vitesse |
|-----------|--------|---------------|
| Chaîne | Tension T, densité linéaire μ | c = √(T/µ) |
| Son | Module de masse B, densité ρ | c = √(B/ρ) |
| Son (gaz parfait) | y, R, T, M | c = √(γRT/M) |
| onde EM | Permittivité ε, perméabilité μ | c = 1/√(με) |
| Onde EM (vide) | ε₀, µ₀ | c = 3 × 10⁸m/s |
---

## Superposition et interférence
### Principe de superposition
Lorsque deux vagues ou plus se chevauchent, le déplacement résultant est la somme des déplacements individuels :
u_total = u₁ + u₂ + ... + uₙ
Cela vaut pour les équations d’ondes linéaires.
### Interférence de deux vagues
Deux ondes de même fréquence et amplitude, différence de phase Δφ :
u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Différence de phase | Résultat | Intensité |
|-----------------|--------|---------------|
| Δφ = 0, 2π, 4π, ... | **Constructif** (amplitude = 2A) | 4I₀ (maximum) |
| Δφ = π, 3π, 5π, ... | **Destructeur** (amplitude = 0) | 0 (minimum) |
| Δφ = π/2 | Partielle | 2I₀ |
### Conditions d'interférence
| État | Tapez | Différence de chemin |
|---------------|------|-----------------|
| Constructif | Frange lumineuse | ΔL = mλ (m = 0, 1, 2, ...) |
| Destructeur | Frange foncée | ΔL = (m + ½)λ |
---

## L'expérience de double fente de Young
La lumière passe à travers deux fentes étroites séparées par la distance d, créant un motif d'interférence sur un écran à la distance L.
### Positions marginales
| Frange | Position à l'écran |
|--------|---------|
| Lumineux (maximum) | y_m = mλL/d |
| Foncé (minima) | y_m = (m + ½)λL/d |
| Espacement des franges | Δy = λL/d |
Cette expérience a prouvé la nature ondulatoire de la lumière (Thomas Young, 1801) et est devenue plus tard essentielle à la mécanique quantique (dualité onde-particule).
---

##Diffractions
La **diffraction** est la courbure et la propagation des ondes autour des obstacles et à travers les ouvertures.
### Diffraction à fente unique
La lumière traversant une fente de largeur a produit un motif de franges claires et sombres.
| Fonctionnalité | État |
|---------|-----------|
| Maximum central | Le plus large et le plus lumineux ; largeur = 2λL/a |
| Minima (franges sombres) | un péché θ = mλ (m = ±1, ±2, ...) |
| Maximaux secondaires | Environ entre les minima ; beaucoup plus faible |
### Réseau de diffraction
N fentes équidistantes (espacement d) produisent des maxima très nets :
d péché θ = mλ (m = 0, 1, 2, ...)
| Propriété | Effet |
|--------------|--------|
| Plus de fentes (N plus grand) | Des maxima plus nets et plus lumineux |
| Pouvoir de résolution | R = mN (peut distinguer les longueurs d'onde proches) |
| Applications | Spectroscopie, mesure de longueur d'onde |
### Critère de Rayleigh (limite de résolution)
Deux sources ponctuelles peuvent simplement être résolues lorsque le maximum central de l'une tombe sur le premier minimum de l'autre :
θ_min = 1,22 λ/D
où D est le diamètre de l'ouverture.
| Système | λ | D | θ_min |
|--------|---|---|-------|
| Oeil humain | 550 nm | 5 millimètres | 1,3 × 10⁻⁴ rad (~0,01°) |
| Télescope spatial Hubble | 550 nm | 2,4 m | 2,8 × 10⁻⁷ rads |
| Radiotélescope (Arecibo) | 21 cm | 305 m | 8,4 × 10⁻⁴ rads |
---

## Polarisation
**Polarisation** décrit l'orientation de l'oscillation du champ électrique dans une onde transversale.
### Types de polarisation
| Tapez | Descriptif |
|------|-------------|
| **Linéaire** | E oscille dans un plan fixe |
| **Circulaire** | E tourne en cercle (droitier ou gaucher) |
| **Elliptique** | E trace une ellipse (la plus générale) |
| **Non polarisé** | Mélange aléatoire de toutes les polarisations (la plupart de la lumière naturelle) |
### Loi de Malus
Lorsque la lumière polarisée traverse un polariseur selon un angle θ par rapport à la direction de polarisation :
je = je₀ cos²θ
| Angle θ | Intensité transmise |
|---------|----------------------|
| 0° | 100 % (I₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (complètement bloqué) |
### Polarisation par réflexion (angle de Brewster)
La lumière réfléchie sous l’angle de Brewster est complètement polarisée :
tan θ_B = n₂/n₁
| Interfaces | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Air → verre | 1.0 | 1.5 | 56,3° |
| Air → eau | 1.0 | 1.33 | 53,1° |
| Verre → diamant | 1.5 | 2.42 | 58,1° |
---

## Optique géométrique
L'optique géométrique (à rayons) traite la lumière comme des rayons qui se déplacent en lignes droites et se courbent aux interfaces.
### Loi de Snell (Réfraction)
n₁ péché θ₁ = n₂ péché θ₂
| Matériel | Indice de réfraction n |
|----------|---------|
| Aspirateur | 1.000 |
| Aérien | 1.0003 |
| Eau | 1.33 |
| Verre (couronne) | 1,52 |
| Verre (silex) | 1,62 |
| Diamant | 2.42 |
### Réflexion interne totale
Lorsque la lumière se déplace d'un milieu plus dense à un milieu moins dense, au-delà de l'**angle critique** :
θ_c = arcsin(n₂/n₁)
Toute la lumière est réfléchie : c’est ainsi que fonctionnent les fibres optiques.
### Équation de lentille mince
1/f = 1/d_o + 1/d_i
| Quantité | Signification |
|--------------|---------|
| f | Distance focale |
| d_o | Distance de l'objet |
| d_i | Distance des images |
| M = −d_i/d_o | Grossissement |
| Type d'objectif | f | Images |
|-----------|---|-------|
| Convergent (convexe) | Positif | Réel (si d_o > f) ou virtuel |
| Divergent (concave) | Négatif | Toujours virtuel, droit, réduit |
### Équation miroir
Même forme que l'équation de la lentille : 1/f = 1/d_o + 1/d_i, où f = R/2 pour les miroirs sphériques.
---

## Optique de Fourier
L'optique de Fourier traite l'imagerie et la diffraction comme des opérations de transformée de Fourier.
### Principe clé
Le diagramme de diffraction en champ lointain d'une ouverture est la **transformée de Fourier** de la fonction d'ouverture.
| Ouverture | Diagramme de diffraction (transformation de Fourier) |
|--------------|----------------------------------------|
| Fente unique | fonction sin |
| Ouverture circulaire | Disque aéré (J₁(r)/r) |
| Ouverture rectangulaire | 2D depuis |
| Grille | Fonctions delta discrètes |
### Transformée de Fourier optique
Un objectif effectue une transformée de Fourier 2D : placer un objet au plan focal avant produit sa transformée de Fourier au plan focal arrière.
### Candidatures
| Demande | Comment l'optique de Fourier aide |
|-------------|------------------------------|
| Filtrage d'images | Placez des masques sur le plan de Fourier pour bloquer/passer les fréquences spatiales |
| Détection des contours | Filtrage passe-haut dans le plan de Fourier |
| Reconnaissance de formes | Corrélation via transformées de Fourier |
| Holographie | Enregistrement et reconstruction des fronts d'onde |
| Informatique optique | Effectuer des transformées de Fourier à la vitesse de la lumière |
---

## Son et acoustique
### Propriétés des ondes sonores
| Propriété | Gamme typique | Unité |
|--------------|--------------|------|
| Fréquence | 20 − 20 000 (audition humaine) | Hz |
| Vitesse (air, 20°C) | 343 | m/s |
| Vitesse (eau) | 1 480 | m/s |
| Vitesse (acier) | 5 960 | m/s |
| Seuil d'intensité | 10⁻¹² | W/m² |
### Échelle de décibels
β = 10 log₁₀(I/I₀) dB, où I₀ = 10⁻¹² W/m²
| Son | Intensité (W/m²) | Niveau (dB) |
|-------|---------|------------|
| Seuil d'audition | 10⁻¹² | 0 |
| Feuilles bruissantes | 10⁻¹¹ | 10 |
| Conversation normale | 10⁻⁶ | 60 |
| Concert de rock | 1 | 120 |
| Seuil de douleur | 10 | 130 |
| Moteur à réaction | 100 | 140 |
### Effet Doppler
Fréquence observée lorsque la source et l'observateur se déplacent l'un par rapport à l'autre :
f' = f(v ± v_o)/(v ∓ v_s)
| Scénario | Effet |
|--------------|--------|
| Source approaching | Fréquence plus élevée (décalage vers le bleu pour la lumière) |
| Source receding | Fréquence inférieure (décalage vers le rouge pour la lumière) |
| Applications | Radar, échographie médicale, astronomie (redshift des galaxies) |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept Onde/Optique | Demande |
|-----------|-------------|
| Équation d'onde | Réseaux de neurones basés sur la physique, analyse de données sismiques, traitement audio |
| Analyse de Fourier | Fondation du traitement du signal, analyse spectrale, extraction de caractéristiques |
| Transformée de Fourier | Les CNN effectuent implicitement une analyse de Fourier locale ; FFT utilisée dans le prétraitement des données |
| Interférence | Informatique analogique, réseaux de neurones optiques |
| Diffractions | Modèles de formation d'images, algorithmes de suppression du flou, photographie informatique |
| Polarisation | Télédétection, classification des matériaux, analyse d'images satellite |
| Optique géométrique | Modèles de caméras en vision par ordinateur, lancer de rayons pour la génération de données synthétiques |
| Équation de lentille | Calibrage de la caméra, estimation de la profondeur, reconstruction 3D |
| Optique de Fourier | Informatique optique, réseaux de neurones profonds diffractifs (D²NN) |
| Effet Doppler | Traitement du signal radar, imagerie médicale (échographie Doppler), estimation de vitesse |
| Échelle de décibels | Ingénierie des fonctionnalités audio, prétraitement de la reconnaissance vocale |
| Théorie de l'échantillonnage | Le théorème de Nyquist-Shannon relie la théorie des ondes au traitement du signal numérique |
---

## Résumé
| Sujet | Idée de base | Équation clé |
|-------|-----------|-------------|
| Équation d'onde | Les vagues se propagent à la vitesse c | ∂²u/∂t² = c²∂²u/∂x² |
| Superpositions | Les vagues s'ajoutent linéairement | u = u₁ + u₂ |
| Interférence | Phase détermine le renforcement | Δφ = 2πΔL/λ |
| Diffractions | Les vagues contournent les obstacles | a sin θ = mλ (fente unique) |
| Polarisation | Orientation des oscillations | Loi de Malus : I = I₀cos²θ |
| Optique géométrique | Lumière comme des rayons | Loi de Snell : n₁sinθ₁ = n₂sinθ₂ |
| Optique de Fourier | Imagerie comme transformée de Fourier | Champ lointain = FT d'ouverture |
| Effet Doppler | Changement de fréquence dû au mouvement | f' = f(v ± v_o)/(v ∓ v_s) |
Les ondes sont le langage universel des systèmes oscillants. Qu'il s'agisse de traiter des signaux audio, d'analyser des séries temporelles, de concevoir des systèmes de reconnaissance d'images ou de créer des simulations physiques, les mathématiques des ondes (superposition, analyse de Fourier, interférence, diffraction) constituent la boîte à outils essentielle. L’optique, en tant que science ondulatoire la plus aboutie, offre à la fois les fondements théoriques et les techniques pratiques qui imprègnent la science moderne des données.