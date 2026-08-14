<!--
---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Électromagnétisme
L'électromagnétisme est l'étude des champs électriques et magnétiques et de leurs interactions. Unifié par Maxwell dans les années 1860, l'électromagnétisme explique la lumière, l'électricité, le magnétisme, les ondes radio et la structure des atomes. Ce fut la première force fondamentale à être entièrement comprise mathématiquement, et ses équations ont inspiré la relativité restreinte d'Einstein et la théorie moderne des champs.
---

## Champs électriques
### Loi de Coulomb
La force entre deux charges ponctuelles q₁ et q₂ séparées par la distance r :
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Constante | Valeur |
|--------------|-------|
| ε₀ (permittivité de l'espace libre) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (Constante coulombienne k) | 8,988 × 10⁹ N·m²/C² |
### Définition du champ électrique
**E** = **F**/q (force par unité de charge)
Pour une charge ponctuelle Q : **E** = (1/4πε₀) · (Q/r²) · r̂
### Lignes de champ électrique
| Propriété | Règle |
|--------------|------|
| Itinéraire | Dirigez-vous loin des charges positives vers les charges négatives |
| Densité | Lignes plus proches = champ plus fort |
| Traversée | Les lignes de terrain ne se croisent jamais |
| Chefs d'orchestre | Les lignes rencontrent la surface perpendiculairement |
### Potentiel électrique (tension)
V = −∫ **E** · d**l** (la différence de potentiel est l'intégrale de ligne négative de E)
**E** = −∇V (le champ est le gradient de potentiel négatif)
Pour une charge ponctuelle : V = (1/4πε₀) · Q/r
| Concepts | Formule | Unité |
|---------|---------|------|
| Énergie potentielle | U = qV | Joules |
| Électron-volt | 1 eV = 1,602 × 10⁻¹⁹ J | Unité énergétique |
| Surface équipotentielle | Surface où V est constant | E lui est perpendiculaire |
---

## Loi de Gauss
### Déclaration
Le flux électrique total à travers toute surface fermée est égal à la charge enfermée divisée par ε₀ :
∮ **E** · d**A** = Q_enc / ε₀
Sous forme différentielle : ∇ · **E** = ρ/ε₀
### Utiliser la loi de Gauss
La loi de Gauss est particulièrement utile lorsque la symétrie permet de sortir E de l'intégrale.
| Symétrie | Surface gaussienne | Résultat |
|--------------|-------|--------|
| Sphérique | Sphère | E = Q/(4πε₀r²) extérieur |
| Cylindrique (charge de ligne) | Cylindre | E = λ/(2πε₀r) |
| Planaire (feuille infinie) | Pilulier | E = σ/(2ε₀) |
| Entre plaques parallèles | Pilulier | E = σ/ε₀ |
---

## Conducteurs et condensateurs
### Conducteurs en équilibre électrostatique
| Propriété | Explication |
|--------------|-------------|
| E = 0 à l'intérieur | Les frais sont réorganisés pour annuler le champ interne |
| Toutes les charges sont en surface | Pas de frais nets à l'intérieur |
| E perpendiculaire à la surface | Aucune composante tangentielle (sinon les charges bougent) |
| Équipotentiel partout | Même V partout à l'intérieur et en surface |
### Condensateurs
Un **condensateur** stocke l'énergie dans un champ électrique entre deux conducteurs.
| Configuration | Capacité |
|--------------|-------------|
| Plaques parallèles | C = ε₀A/ré |
| Cylindrique | C = 2πε₀L / ln(b/une) |
| Sphérique | C = 4πε₀ab / (b−a) |
| Formule | Expressions |
|--------------|------------|
| Tension de charge | Q = CV |
| Énergie stockée | U = ½CV² = ½Q²/C |
| Densité énergétique | u = ½ε₀E² |
| Combinaison de séries | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Combinaison parallèle | C_total = C₁ + C₂ + ... |
### Diélectriques
L'insertion d'un diélectrique (matériau isolant) avec κ constant augmente la capacité : C = κC₀.
---

## Champs magnétiques
### Force magnétique
**F** = q(**v** × **B**) (force de Lorentz, composante magnétique)
| Propriété | Déclaration |
|--------------|---------------|
| Itinéraire | Perpendiculaire à v et B (règle de droite) |
| Travail effectué | Zéro (la force est perpendiculaire à la vitesse) |
| Mouvement circulaire | Rayon r = mv/(qB) dans un champ B uniforme |
### Loi Biot-Savart
Le champ magnétique dû à un petit élément de courant :
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Constante | Valeur |
|--------------|-------|
| μ₀ (perméabilité de l'espace libre) | 4π × 10⁻⁷ T·m/A |
### Loi d'Ampère
∮ **B** · d**l** = μ₀I_enc
Sous forme différentielle : ∇ × **B** = μ₀**J**
**Candidatures :**
| Configuration | Champ B |
|--------------|---------|
| Fil long et droit | B = μ₀I/(2πr) |
| Solénoïde (à l'intérieur) | B = μ₀nI |
| Tore (à l'intérieur) | B = μ₀NI/(2πr) |
---

## Induction électromagnétique
### Loi de Faraday
Un flux magnétique changeant induit une force électromotrice (FEM) :
FEM = −dΦ_B/dt
où Φ_B = ∫ **B** · d**A** est le flux magnétique.
Sous forme différentielle : ∇ × **E** = −∂**B**/∂t
**Loi de Lenz :** La CEM induite s'oppose au changement de flux (le signe moins).
### Applications de l'induction
| Demande | Principe |
|-------------|-----------|
| Générateur | Bobine tournante dans le champ B → FEM alternative |
| Transformateur | Changement de courant au primaire → FEM au secondaire |
| Inducteur | S'oppose aux changements de courant : EMF = −L(dI/dt) |
| Courants de Foucault | Courants induits dans les conducteurs massifs (freinage, chauffage) |
### Inducteurs
| Formule | Expressions |
|--------------|------------|
| Liaison de flux | Φ = LI |
| Énergie stockée | U = ½LI² |
| Combinaison de séries | L_total = L₁ + L₂ + ... |
| Combinaison parallèle | 1/L_total = 1/L₁ + 1/L₂ + ... |
---

## Les équations de Maxwell
Les équations de Maxwell unifient l'électricité et le magnétisme en une seule théorie.
### Sous forme intégrale
| Équation | Nom | Déclaration |
|--------------|------|---------------|
| ∮ **E** · d**A** = Q/ε₀ | Loi de Gauss (électrique) | Flux électrique = charge enfermée |
| ∮ **B** · d**A** = 0 | Loi de Gauss (magnétique) | Pas de monopôles magnétiques |
| ∮ **E** · d**l** = −dΦ_B/dt | Loi de Faraday | Changer B induit E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Loi Ampère-Maxwell | E actuel et changeant produit B |
### Sous forme différentielle
| Équation | Nom | Expressions |
|--------------|------|------------|
| Gauss (électrique) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnétique) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampère-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Le courant de déplacement
L'ajout clé de Maxwell : le terme μ₀ε₀ ∂**E**/∂t (courant de déplacement). Cela garantit la conservation des charges et prédit les ondes électromagnétiques.
---

## Ondes électromagnétiques
Dans le vide (pas de charges, pas de courants), les équations de Maxwell donnent des équations d'ondes :
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Vitesse de la lumière :** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Propriétés des ondes EM
| Propriété | Descriptif |
|--------------|-------------|
| Transversale | E et B sont perpendiculaires entre eux et à la direction de propagation |
| En phase | E et B atteignent des maxima simultanément |
| Rapport de grandeur | E = CB |
| Flux d'énergie | S = (1/μ₀)**E** × **B** (vecteur de Poynting) |
| Intensité | je = ⟨S⟩ = E₀²/(2μ₀c) |
### Le spectre électromagnétique
| Tapez | Longueur d'onde | Fréquence | Source |
|------|-----------|---------------|--------|
| Radio | > 1 m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 Hz | Procédés nucléaires |
---

## Circuits CA
### Composants du circuit RLC
| Composant | Relation tension-courant | Impédance |
|---------------|--------------|---------------|
| Résistance (R) | V = IR | Z_R = R |
| Inducteur (L) | V = L(dI/dt) | Z_L = jωL |
| Condensateur (C) | je = C(dV/dt) | Z_C = 1/(jωC) |
### Impédance et résonance
Impédance totale (série RLC) : Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Résonance :** Lorsque ωL = 1/ωC → ω₀ = 1/√(LC)
- A la résonance : l'impédance est minimale (= R), le courant est maximum
- **Facteur de qualité :** Q = ω₀L/R (netteté de résonance)
### Puissance dans les circuits CA
| Quantité | Formule |
|--------------|---------|
| Puissance moyenne | P_moy = V_rms · I_rms · cos φ |
| Facteur de puissance | cos φ = R/\|Z\| |
| Tension efficace | V_rms = V₀/√2 |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept EM | Demande |
|---------------|-------------|
| Les équations de Maxwell | Réseaux de neurones basés sur la physique, électromagnétisme informatique |
| Équation d'onde | Fondements du traitement du signal, motivation de l'analyse de Fourier |
| Spectre électromagnétique | Données de capteurs (caméras infrarouges, radar, imagerie satellite) |
| Circuits CA / impédance | Comprendre le matériel qui exécute le ML (alimentations électriques, intégrité du signal) |
| Vecteur de Poynting | Flux d'énergie dans la communication sans fil (pertinent pour l'IoT/Edge ML) |
| Loi de Gauss | Analogue à la divergence en calcul vectoriel, utilisée dans les simulations de dynamique des fluides |
| Condensateurs/inductances | Informatique analogique pour réseaux de neurones, matériel neuromorphique |
| Résonance | Conception de filtres, analyse du domaine fréquentiel, méthodes spectrales |
| Problèmes de valeurs limites | Méthodes éléments finis, simulations basées sur maillage |
| Calcul vectoriel (∇·, ∇×) | Outils mathématiques essentiels utilisés dans la théorie du ML |
---

## Résumé
| Droit | Ce qu'il dit | Forme différentielle |
|-----|-------------|---------|
| Gauss (électrique) | Les charges créent une divergence de champ électrique | ∇ · E = ρ/ε₀ |
| Gauss (magnétique) | Pas de monopôles magnétiques | ∇ · B = 0 |
| Faraday | Changer B crée un curling E | ∇ × E = −∂B/∂t |
| Ampère-Maxwell | Actuel et changeant E crée du curling B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
L'électromagnétisme est la théorie physique la plus complète et la mieux testée jamais construite. Ses équations – seulement quatre – décrivent tout, de l'électricité statique à la lumière en passant par le comportement de chaque appareil électronique jamais construit. Pour les data scientists, comprendre l’électromagnétisme fournit une intuition approfondie des phénomènes ondulatoires, du calcul vectoriel et de la physique qui sous-tend tout le matériel informatique moderne.