---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Thermodynamique et mécanique statistique
La thermodynamique décrit le comportement macroscopique des systèmes en termes de température, de pression et d'entropie, sans savoir à quoi ressemblent les atomes. La mécanique statistique explique la thermodynamique de bas en haut : elle dérive les propriétés macroscopiques du comportement microscopique d'un grand nombre de particules. Ensemble, ils fournissent la compréhension la plus approfondie de l’énergie, de l’entropie et de l’équilibre – des concepts qui ont migré vers la théorie de l’information, l’apprentissage automatique et au-delà.
---

## Variables et état thermodynamiques
### Variables d'état
| Variables | Tapez | Unité | Descriptif |
|--------------|------|------|-------------|
| Température (T) | Intensif | Kelvin (K) | Énergie cinétique moyenne par particule |
| Pression (P) | Intensif | Pascal (Pa) | Force par unité de surface |
| Tome (V) | Vaste | m³ | Espace occupé |
| Énergie interne (U) | Vaste | Joule (J) | Énergie microscopique totale |
| Entropie (S) | Vaste | J/K | Mesure du désordre/microétats |
| Nombre de particules (N) | Vaste | taupes ou compte | Quantité de substance |
Les variables **intensives** ne dépendent pas de la taille du système ; **de nombreuses** variables le font.
### Équation d'état
Pour un gaz parfait : PV = nRT = Nk_BT
| Constante | Valeur |
|--------------|-------|
| R (constante du gaz) | 8,314 J/(mol·K) |
| k_B (constante de Boltzmann) | 1,381 × 10⁻²³ J/K |
| N_A (numéro d'Avogadro) | 6,022 × 10²³ /mole |
---

## Les lois de la thermodynamique
### Loi Zéroth
Si A est en équilibre thermique avec B et B avec C, alors A est en équilibre thermique avec C.
**Signification :** La température est bien définie et mesurable.
### Première loi (économie d'énergie)
ΔU = Q − W
| Symbole | Signification |
|--------|---------|
| ΔU | Changement d'énergie interne |
| Q | Chaleur ajoutée au système |
| W | Travail effectué par le système |
**Forme différentielle :** dU = δQ − δW = δQ − PdV
| Processus | Contrainte | Conséquence |
|---------|-----------|-------------|
| Isochore | dV = 0 | W = 0, ΔU = Q |
| Isobare | dP = 0 | W = PΔV |
| Isotherme | dT = 0 | ΔU = 0 (gaz parfait), Q = W |
| Adiabatique | δQ = 0 | ΔU = −W |
### Deuxième loi (Entropie)
**Déclaration de Clausius :** La chaleur ne peut pas passer spontanément du froid au chaud.
**Déclaration Kelvin-Planck :** Aucun moteur ne peut convertir toute la chaleur en travail.
**Déclaration d'entropie :** Pour tout processus : ΔS_universe ≥ 0
| Type de processus | ΔS_univers |
|-------------|-------------|
| Réversible | = 0 |
| Irréversible (réel) | > 0 |
**Changement d'entropie :** dS = δQ_rev / T
### Troisième loi
Lorsque T → 0 K, l'entropie d'un cristal parfait s'approche de zéro : lim_{T→0} S = 0
**Signification :** Le zéro absolu est inaccessible en étapes finies.
---

## Entropie en profondeur
### Entropie thermodynamique
S est une fonction d'état. Pour un processus réversible entre les états A et B :
ΔS = ∫_A^B δQ_rev / T
**Exemple concret :** Changement d'entropie lors du chauffage de l'eau de T₁ à T₂ à pression constante.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropie statistique (Boltzmann)
S = k_B ln Ω
où Ω est le nombre de microétats cohérents avec le macroétat.
| Macroétat | Microétats (Ω) | Entropie |
|-----------|---|---------|
| Tout le gaz dans une moitié de boîte | Petit | Faible |
| Gaz uniformément réparti | Très grand | Élevé |
| Cristal parfait à 0 K | 1 | 0 |
**Connexion :** La deuxième loi devient statistique : les systèmes évoluent vers des macro-états avec plus de micro-états simplement parce qu'ils sont extrêmement plus probables.
---

## Enthalpie et énergie libre
### Enthalpie
H = U + PV
Utile pour les processus à pression constante (la plupart des produits chimiques et biologiques).
ΔH = Q_p (chaleur à pression constante)
### Énergie gratuite Helmholtz
F = U − TS
| Propriété | Déclaration |
|--------------|---------------|
| Signification | Travail maximum extractible à T, V constant |
| Équilibre | Le système minimise F à T, V constant |
| Relation avec la fonction de partition | F = −k_BT ln Z |
### Énergie gratuite Gibbs
G = H − TS = U + PV − TS
| Propriété | Déclaration |
|--------------|---------------|
| Signification | Travail maximal de non-expansion à T, P constant |
| Équilibre | Le système minimise G à T constant, P |
| Spontanéité | ΔG < 0 → spontané ; ΔG = 0 → équilibre |
| Réactions chimiques | ΔG = ΔH − TΔS détermine la direction |
### Résumé des potentiels thermodynamiques
| Potentiel | Variables naturelles | Différentiel | Réduit quand |
|---------------|---------|-------------|----------------|
| U (énergie interne) | S, V | dU = TdS − PdV | Système isolé |
| H (enthalpie) | S, P | dH = TdS + VdP | Constante P, adiabatique |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Constante T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Constante T, P |
---

## Le cycle de Carnot
Le **cycle Carnot** est le moteur thermique le plus efficace possible, fonctionnant entre les températures T_H (chaud) et T_C (froid).
### Quatre étapes
| Scène | Processus | Que se passe-t-il |
|-------|---------|-------------|
| 1 → 2 | Expansion isotherme | Absorber la chaleur Q_H du réservoir chaud à T_H |
| 2 → 3 | Expansion adiabatique | Le gaz se refroidit de T_H à T_C |
| 3 → 4 | Compression isotherme | Rejeter la chaleur Q_C vers le réservoir froid à T_C |
| 4 → 1 | Compression adiabatique | Le gaz chauffe de T_C à T_H |
### Efficacité Carnot
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500 K | 300 K | 40% |
| 1000K | 300 K | 70% |
| 300 K | 299 Ko | 0,33% |
**Aucun moteur réel ne peut dépasser l'efficacité Carnot.** Les vrais moteurs sont toujours irréversibles (frottements, turbulences, différences finies de température).
---

## Mécanique statistique
### La distribution Boltzmann
Pour un système en équilibre thermique à température T, la probabilité d'être dans un microétat d'énergie E_i :
P(E_i) = (1/Z) e^{−E_i / k_BT}
où Z est la **fonction de partition** :
Z = Σᵢ e^{−E_i / k_BT}
### La fonction de partition
Z code toutes les informations thermodynamiques sur le système.
| Quantité | Formule |
|--------------|---------|
| Énergie libre de Helmholtz | F = −k_BT ln Z |
| Énergie moyenne | ⟨E⟩ = −∂(ln Z)/∂β où β = 1/(k_BT) |
| Entropie | S = k_B(ln Z + β⟨E⟩) |
| Capacité thermique | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Pression | P = (1/β) ∂(lnZ)/∂V |
### Exemple concret : système à deux États
Une particule peut être dans l’état 0 (énergie 0) ou dans l’état 1 (énergie ε).
Z = 1 + e^{−βε}
| Quantité | Résultat |
|--------------|--------|
| P(état 0) | 1/(1 + e^{−βε}) |
| P(état 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Limite T haute (β→0) | ⟨E⟩ → ε/2 (probabilité égale) |
| Limite T basse (β→∞) | ⟨E⟩ → 0 (état fondamental) |
### Théorème d'équipartition
Chaque degré de liberté quadratique contribue ½k_BT à l'énergie moyenne.
| Système | Degrés de liberté | ⟨E⟩ |
|--------|---------|------|
| Gaz monoatomique (He) | Traduction 3 | (3/2)k_BT |
| Gaz diatomique (N₂) dans la pièce T | 3 trans + 2 pourris | (5/2)k_BT |
| Gaz diatomique à haute T | 3 trans + 2 rot + 1 vib | (7/2)k_BT |
| Solide (modèle Einstein) | 3 vibrationnel (par atome) | 3k_BT |
---

## Connexion à la théorie de l'information
### Entropie de Shannon vs entropie thermodynamique
| Aspects | Entropie de Shannon H(X) | Entropie thermodynamique S |
|--------|-----------|------------------------|
| Définition | −Σ pᵢ log pᵢ | k_B ln Ω (ou −k_B Σ pᵢ ln pᵢ) |
| Maximum lorsque | Distribution uniforme | Equilibre thermique |
| Mesures | Incertitude / contenu informationnel | Nombre de micro-états accessibles |
| Unités | Bits ou nats | J/K |
**Formule d'entropie de Gibbs :** S = −k_B Σᵢ pᵢ ln pᵢ (forme identique à l'entropie de Shannon)
### Principe d'entropie maximale
Les deux domaines utilisent le même principe : la distribution qui représente le mieux notre état de connaissances est celle qui maximise l'entropie sous réserve de contraintes connues.
| Contrainte | Distribution résultante |
|---------------|----------------------|
| Moyenne connue | Distribution exponentielle |
| Moyenne et variance connues | Distribution gaussienne |
| Énergie connue ⟨E⟩ | Distribution Boltzmann |
| Aucune contrainte | Distribution uniforme |
### Principe de Landauer
L'effacement d'un bit d'information dissipe au moins k_BT ln 2 d'énergie sous forme de chaleur. Cela relie directement le traitement de l’information à la thermodynamique – le calcul a un coût énergétique fondamental.
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept Thermo/StatMech | Demande |
|-----------------------------|-------------|
| Distribution Boltzmann | Fonction Softmax, modèles basés sur l'énergie, recuit simulé |
| Fonction de partition | Constante de normalisation dans les modèles probabilistes, intraitable en général |
| Énergie gratuite | Inférence variationnelle (minimiser l'énergie libre variationnelle = minimiser la divergence KL) |
| Entropie | Régularisation, exploration en RL (maximum entropy RL), arbres de décision |
| Principe d'entropie maximale | Classificateurs MaxEnt, sélection préalable, estimation de distribution |
| Recuit simulé | Optimisation globale en réduisant progressivement la « température » |
| Mécanique statistique | Comprendre les transitions de phases dans l'apprentissage (grokking, double descente) |
| Equipartition | Comprendre la distribution d'énergie dans les simulations physiques |
| Principe de Landauer | Limites fondamentales du calcul, calcul réversible |
| Échantillonnage Gibbs | Méthode MCMC directement inspirée de la mécanique statistique |
| Température (en softmax) | Contrôle le caractère aléatoire des prédictions : P(i) ∝ exp(z_i/T) |
---

## Résumé
| Loi/Concept | Idée de base | Formule |
|------------|-----------|---------|
| Loi zéro | La température est bien définie | Transitivité de l'équilibre thermique |
| Première loi | L'énergie est conservée | ΔU = Q − W |
| Deuxième loi | L'entropie de l'univers augmente | ΔS ≥ 0 |
| Troisième loi | Le zéro absolu est inaccessible | S → 0 comme T → 0 |
| Entropie de Boltzmann | L'entropie compte les microétats | S = k_B ln Ω |
| Distribution Boltzmann | Probabilité des états énergétiques | P ∝ e^{−E/k_BT} |
| Fonction de partition | Encode toutes les informations thermodynamiques | Z = Σ e^{−E_i/k_BT} |
| Énergie gratuite | Travaux utiles disponibles | F = U − TS, G = H − TS |
| Efficacité Carnot | Efficacité maximale du moteur thermique | η = 1 − T_C/T_H |
La thermodynamique et la mécanique statistique sont le point où la physique rencontre la théorie de l'information. La même entropie qui régit les moteurs thermiques régit la compression des données. La même distribution de Boltzmann qui décrit les molécules de gaz alimente la couche softmax de chaque classificateur. Comprendre ces connexions vous donne une vue unifiée de la physique, des probabilités et de l'apprentissage automatique.