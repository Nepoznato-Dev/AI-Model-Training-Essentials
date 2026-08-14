<!--
---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mécanique quantique
La mécanique quantique est la théorie de la physique aux plus petites échelles : les atomes, les électrons, les photons et les particules fondamentales de la nature. Il remplace le monde déterministe de la mécanique classique par les probabilités, les superpositions et l'intrication. Malgré sa nature contre-intuitive, la mécanique quantique est la théorie la plus précisément testée de toutes les sciences. Aujourd’hui, ses principes deviennent directement pertinents pour l’informatique grâce aux ordinateurs quantiques, qui promettent de résoudre certains problèmes de manière exponentielle plus rapidement que les machines classiques.
---

## Motivation historique
### Échecs de la physique classique
| Problème | Prédiction classique | Observations | Résolution |
|---------|-----------|-------------|------------|
| Rayonnement du corps noir | Catastrophe ultraviolette (énergie infinie à court λ) | Longueur d'onde de crête finie | Planck : l'énergie est quantifiée (E = nhν) |
| Effet photoélectrique | KE dépend de l'intensité et non de la fréquence | KE dépend de la fréquence | Einstein : la lumière est quantifiée (photons, E = hν) |
| Spectres atomiques | Spectre d'émission continu | Lignes spectrales discrètes | Bohr : les électrons occupent des orbites quantifiées |
| Diffraction électronique | Les particules ne diffractent pas | Les électrons produisent des modèles d'interférence | de Broglie : les particules ont une longueur d'onde λ = h/p |
### Constantes clés
| Constante | Symbole | Valeur |
|--------------|--------|-------|
| Constante de Planck | h | 6,626 × 10⁻³⁴ J·s |
| Constante de Planck réduite | ℏ = h/2π | 1,055 × 10⁻³⁴ J·s |
| Vitesse de la lumière | c | 3,0 × 10⁸ m/s |
| Masse électronique | m_e | 9,109 × 10⁻³¹ kg |
| Charge élémentaire | e | 1,602 × 10⁻¹⁹ C |
| Rayon de Bohr | une₀ | 5,292 × 10⁻¹¹ m |
---

## Dualité onde-particule
### Longueur d'onde de Broglie
Chaque particule d'impulsion p a une longueur d'onde associée :
λ = h/p = h/(mv)
| Particule | Typique λ | Comportement des vagues observable ? |
|----------|-----------|--------------------------------|
| Électron (100 eV) | 0,12 nm | Oui (diffraction cristalline) |
| Proton | 0,003 nm | Oui (diffusion des neutrons) |
| Base-ball (40 m/s) | 10⁻³⁴ m | Non (beaucoup trop petit pour être détecté) |
### Expérience à double fente
L’expérience quantique par excellence :
1. Enflammer les particules (électrons, photons) une à la fois dans deux fentes
2. Chaque particule atterrit en un seul point du détecteur
3. Au fil du temps, un motif d'interférence apparaît, comme si chaque particule passait simultanément par les deux fentes.
4. Si vous mesurez par quelle fente passe la particule, le motif d'interférence disparaît
**Conclusion :** Les objets quantiques ne sont ni purement des particules ni purement des ondes. Ils présentent un comportement semblable à celui d’une onde lorsqu’ils ne sont pas observés et d’un comportement semblable à celui d’une particule lorsqu’ils sont mesurés.
---

## La fonction d'onde
### Définition
La **fonction d'onde** ψ(x, t) décrit complètement un système quantique. C'est une fonction à valeurs complexes dont le module au carré donne la densité de probabilité :
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalisation
La probabilité totale doit être égale à 1 :
∫ |ψ(x)|² dx = 1 (sur tout l'espace)
### Règle née
La probabilité de trouver la particule entre x et x + dx :
P(x à x+dx) = |ψ(x)|² dx
Pour un observable général avec états propres φₙ :
P(mesurant la valeur propre aₙ) = |⟨φₙ|ψ⟩|²
---

## L'équation de Schrödinger
### Équation de Schrödinger dépendant du temps
jeℏ ∂ψ/∂t = Ĥψ
où Ĥ est le **opérateur hamiltonien** (opérateur d'énergie totale).
### Équation de Schrödinger indépendante du temps
Pour les états stationnaires (états propres énergétiques) :
Ĥψ = Eψ
Il s'agit d'une équation aux valeurs propres : les énergies autorisées E sont les valeurs propres de Ĥ.
### Particule dans une boîte (puits carré infini)
Le système quantique le plus simple : particule confinée à 0 < x < L.
| Quantité | Résultat |
|--------------|--------|
| Fonctions d'onde | ψₙ(x) = √(2/L) sin(nπx/L) |
| Niveaux d'énergie | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| État fondamental | n = 1, E₁ = h²/(8 ml²) |
| Énergie du point zéro | E₁ > 0 (la particule ne peut pas être parfaitement immobile) |
| Nombre quantique | n = 1, 2, 3, ... (entiers positifs uniquement) |
### Oscillateur harmonique quantique
V(x) = ½mω²x²
| Quantité | Résultat |
|--------------|--------|
| Niveaux d'énergie | Eₙ = (n + ½)ℏω |
| Énergie du point zéro | E₀ = ½ℏω |
| Espacement | ΔE = ℏω (uniforme) |
| Fonctions d'onde | Polynômes d'Hermite × Gaussien |
---

## Opérateurs et observables
En mécanique quantique, chaque observable physique correspond à un **opérateur hermitien**.
### Opérateurs clés
| Observables | Opérateur (espace de position) | Valeurs propres |
|-----------|----------------|-------------|
| Poste | x = x | Tout réel x |
| Élan | p̂ = −iℏ ∂/∂x | Tout vrai p |
| Énergie (Hamiltonien) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (discret pour les états liés) |
| Moment angulaire | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Tourner | Ŝ = (ℏ/2)σ (matrices de Pauli) | ±ℏ/2 (pour spin-½) |
### Valeurs attendues
Le résultat moyen de la mesure de l'observable A sur l'état ψ :
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Relations de trajet
[Â, B̂] = ÂB̂ − B̂Â
| Commutateur | Résultat | Importance |
|---------------|--------|-------------|
| [x̂, p̂] | jeℏ | La position et l'élan sont incompatibles |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Les composants du moment angulaire sont incompatibles |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Matrices de Pauli (composantes de spin) |
Si [Â, B̂] = 0, les observables peuvent être mesurés simultanément (partager les états propres).
---

## Principe d'incertitude
### Principe d'incertitude de Heisenberg
Δx · Δp ≥ ℏ/2
Plus généralement, pour deux observables A et B quelconques :
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Relations d'incertitude
| Paire | Relation | Interprétation |
|------|----------|----------------|
| Position-élan | ΔxΔp ≥ ℏ/2 | Je ne peux pas connaître les deux avec précision |
| Énergie-temps | ΔEΔt ≥ ℏ/2 | Les États éphémères ont une énergie incertaine |
| Moment angulaire | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Impossible de connaître tous les composants simultanément |
**Important :** L'incertitude ne concerne pas la perturbation des mesures : il s'agit d'une propriété fondamentale des états quantiques. Une particule n’a pas simultanément une position et un élan définis.
---

## États quantiques et superposition
### Notation de Dirac (Bra-Ket)
| Symbole | Nom | Signification |
|--------|------|---------|
| \|ψ⟩ | Ket | Vecteur d'état (vecteur de colonne) |
| ⟨ψ\| | Soutien-gorge | Transposition conjuguée (vecteur ligne) |
| ⟨φ\|ψ⟩ | Produit intérieur | Amplitude pour ψ à trouver dans l'état φ |
| \|ψ\|² | Norme au carré | Probabilité |
### Principe de superposition
Si \|ψ₁⟩ et \|ψ₂⟩ sont des états quantiques valides, alors toute combinaison linéaire est également valide :
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

où |α|² + |β|² = 1 (normalisation).
**Mesure :** Une fois mesuré, le système « s'effondre » en \|ψ₁⟩ avec une probabilité |α|² ou \|ψ₂⟩ avec une probabilité |β|².
###Qubits
Un **qubit** est un bit quantique : un système quantique à deux niveaux.
\|ψ⟩ = α\|0⟩ + β\|1⟩, où |α|² + |β|² = 1
| Représentation | \|0⟩ | \|1⟩ |
|---------------|------|------|
| Tourner | Faites tourner ↑ | Ralentissez ↓ |
| Polarisation des photons | horizontale | verticale |
| Niveau d'énergie | État fondamental | État excité |
| Circuit | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Sphère de Bloch :** Tout état de qubit peut s'écrire comme :
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
où θ ∈ [0, π] et φ ∈ [0, 2π). L'espace d'état est une sphère.
---

## Enchevêtrement
Deux qubits sont **intriqués** lorsque leur état commun ne peut pas être écrit comme un produit d'états individuels.
### États de cloche (enchevêtrés au maximum)
| État | Expressions | Nom |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | État de la cloche |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | État de la cloche |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | État de la cloche |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | État du singulet |
### Propriétés de l'enchevêtrement
| Propriété | Descriptif |
|--------------|-------------|
| Corrélation | La mesure d'un qubit détermine instantanément l'autre, quelle que soit la distance |
| Aucune communication | Impossible d'utiliser l'intrication seule pour envoyer des informations plus rapidement que la lumière |
| Monogamie | Si A est intriqué au maximum avec B, il ne peut pas être intriqué avec C |
| Fragilité | L'interaction avec l'environnement détruit l'intrication (décohérence) |
### Paradoxe EPR et théorème de Bell
Einstein, Podolsky et Rosen affirmaient que la mécanique quantique devait être incomplète (variables cachées). Bell a montré que toute théorie locale des variables cachées satisfait certaines inégalités. Les expériences violent les inégalités de Bell, confirmant la mécanique quantique et excluant les variables locales cachées.
---

## Portes quantiques
Les portes quantiques sont des opérations unitaires sur des qubits.
### Portes à un seul qubit
| Porte | Matrice | Effet |
|------|--------|--------|
| **Pauli-X** (PAS) | [[0,1],[1,0]] | Retournement de bits : \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + retournement de phase |
| **Pauli-Z** | [[1,0],[0,−1]] | Inversion de phase : \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Crée une superposition : \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Phase** (S) | [[1,0],[0,i]] | rotation π/2 autour de Z |
| **Porte en T** | [[1,0],[0,e^{iπ/4}]] | rotation π/4 autour de Z |
| **Rotation** Rₓ(θ) | cos(θ/2)I − je sin(θ/2)σₓ | Rotation de θ autour de l'axe X |
### Portes à deux qubits
| Porte | Descriptif | Effet |
|------|-------------|--------|
| **CNOT** | Contrôlé-NON | Retourne la cible si le contrôle est \|1⟩ |
| **CZ** | Contrôlé-Z | Applique Z à la cible si le contrôle est \|1⟩ |
| **ÉCHANGE** | Échanger des qubits | \|ab⟩ → \|ba⟩ |
### Créer un enchevêtrement
Appliquez H au qubit 1, puis CNOT avec le qubit 1 comme contrôle :
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Algorithmes quantiques
| Algorithme | Accélération | Demande |
|-----------|---------|-------------|
| **Shor** | Exponentiel (factorisation) | Brise le cryptage RSA |
| **Grover** | Quadratique (recherche) | Recherche non structurée dans O(√N) |
| **VQE** | Heuristique | Trouver les énergies fondamentales (chimie, matériaux) |
| **QAOA** | Heuristique | Optimisation combinatoire |
| **HHL** | Exponentiel (sous conditions) | Résolution de systèmes linéaires |
| **Simulation quantique** | Exponentiel | Simulation de systèmes quantiques (la motivation originale de Feynman) |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept quantique | Demande |
|----------------|-------------|
| Qubits et superpositions | Apprentissage automatique quantique, échantillonnage amélioré quantique |
| Enchevêtrement | Communication quantique, distribution de clés quantiques (QKD) |
| Portes quantiques | Conception de circuits quantiques pour les sous-programmes ML |
| L'algorithme de Grover | Accélération quadratique pour l'optimisation basée sur la recherche |
| L'algorithme de Shor | Menace pour la cryptographie actuelle ; motive la crypto post-quantique |
| Simulation quantique | Découverte de médicaments, science des matériaux, simulation chimique |
| Algorithmes variationnels (VQE, QAOA) | ML quantique à court terme sur les appareils NISQ |
| Règle née | Résultats probabilistes analogues à l'échantillonnage à partir de distributions |
| Produits tenseurs | Systèmes multi-qubits (espace d'état exponentiel — mêmes mathématiques que l'algèbre multilinéaire en ML) |
| Matrices unitaires | Analogues quantiques des transformations orthogonales |
---

## Résumé
| Concepts | Idée de base | Équation clé |
|---------|-----------|-------------|
| Dualité onde-particule | La matière a des propriétés ondulatoires | λ = h/p |
| Fonction d'onde | Description complète de l'état quantique | P(x) = \|ψ(x)\|² |
| Équation de Schrödinger | Comment évoluent les états quantiques | jeℏ ∂ψ/∂t = Ĥψ |
| Opérateurs | Les observables sont des opérateurs hermitiens | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Incertitude | Limites fondamentales de la connaissance simultanée | ΔxΔp ≥ ℏ/2 |
| Superpositions | Des états peuvent être ajoutés | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Enchevêtrement | États communs non séparables | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Portes quantiques | Opérations unitaires sur les qubits | Ensembles de portails H, CNOT et universels |
La mécanique quantique remet en question nos intuitions les plus profondes sur la réalité : des particules qui sont des ondes, des objets situés à deux endroits à la fois, des corrélations qui défient toute explication classique. Pourtant, ses mathématiques sont précises et ses prédictions sont d’une précision inégalée. Pour les data scientists, la mécanique quantique devient directement pertinente grâce à l’informatique quantique, qui promet de transformer l’optimisation, la cryptographie, la simulation et potentiellement l’apprentissage automatique lui-même.