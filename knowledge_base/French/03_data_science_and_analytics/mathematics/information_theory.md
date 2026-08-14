---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Théorie de l'information
La théorie de l'information, fondée par Claude Shannon en 1948, quantifie l'information elle-même. Que vous dit un message ? Dans quelle mesure pouvez-vous compresser les données ? À quelle vitesse pouvez-vous communiquer sur un canal bruyant ? Ces questions ont des réponses mathématiques précises. Au-delà de la communication, la théorie de l'information est devenue fondamentale pour l'apprentissage automatique : l'entropie croisée est la fonction de perte par défaut pour la classification, la divergence KL mesure la similarité de la distribution et les informations mutuelles déterminent la sélection des fonctionnalités.
---

## Entropie
**L'entropie** mesure l'incertitude moyenne ou la « surprise » d'une variable aléatoire.
### Entropie de Shannon (discrète)
Pour une variable aléatoire discrète X avec fonction de masse de probabilité p(x) :
H(X) = −Σₓ p(x) log₂ p(x)
Unités : **bits** (lors de l'utilisation de log₂) ou **nats** (lors de l'utilisation de ln).
| Distribution | Entropie | Intuitions |
|-------------|---------|---------------|
| Pièce équitable (p = 0,5, 0,5) | 1 bit | Incertitude maximale pour le résultat binaire |
| Pièce biaisée (p = 0,9, 0,1) | 0,469 bits | Moins surprenant — principalement des têtes |
| Déterministe (p = 1, 0) | 0 bit | Aucune incertitude |
| Dé équitable (6 faces) | 2,585 bits | Plus de résultats = plus d'incertitude |
| Uniforme sur n résultats | log₂(n) bits | Entropie maximale pour n résultats |
### Propriétés de l'entropie
| Propriété | Déclaration |
|--------------|---------------|
| Non-négativité | H(X) ≥ 0 |
| Maximale | H(X) ≤ log₂(\|X\|) avec égalité pour une distribution uniforme |
| Règle de chaîne | H(X, Oui) = H(X) + H(Oui \| X) |
| Le conditionnement réduit | H(X \| Oui) ≤ H(X) |
| Concavité | H est une fonction concave de la distribution de probabilité |
### Entropie différentielle (continue)
Pour une variable aléatoire continue X de densité p(x) :
h(X) = −∫ p(x) log p(x) dx
Contrairement à l'entropie discrète, l'entropie différentielle peut être **négative**.
| Distribution | Entropie différentielle |
|-------------|-----------|
| Uniforme sur [a,b] | journal(b - une) |
| Normale N(μ, σ²) | (1/2) log(2πeσ²) |
| Exponentiel(λ) | 1 − ln(λ) |
---

## Informations conjointes, conditionnelles et mutuelles
### Entropie conjointe
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Mesure l'incertitude totale de la paire (X, Y).
### Entropie conditionnelle
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Mesure l'incertitude restante sur Y après avoir observé X.
### Informations mutuelles
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Mesure ce que la connaissance de X vous apprend sur Y (et vice versa).
| Propriété | Déclaration |
|--------------|---------------|
| Non-négativité | je(X; Oui) ≥ 0 |
| Symétrie | Je(X; Oui) = Je(Oui; X) |
| Relation avec l'entropie | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Relation avec l'articulation | je(X; Oui) = H(X) + H(Oui) − H(X, Oui) |
| Indépendance | I(X; Y) = 0 si X et Y sont indépendants |
| Auto-information | je(X; X) = H(X) |
### Visuel : Le diagramme d'entropie
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## Divergence de Kuala Lumpur
La **divergence Kullback-Leibler (KL)** mesure la différence entre une distribution et une autre.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Propriété | Déclaration |
|--------------|---------------|
| Non-négativité | D_KL(P \|\| Q) ≥ 0 (inégalité de Gibbs) |
| Identité | D_KL(P \|\| Q) = 0 si P = Q |
| Asymétrie | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) en général |
| Pas une métrique | Échoue la symétrie et l'inégalité triangulaire |
**Interprétation :** D_KL(P || Q) est le nombre supplémentaire de bits nécessaire pour coder les données de P à l'aide d'un code optimisé pour Q.
### Relation avec d'autres quantités
| Relation | Formule |
|-------------|---------|
| Entropie croisée | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Information mutuelle | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL conditionnel | D_KL(P(Y\|X) \|\| Q(Y\|X)) en moyenne sur X |
---

## Entropie croisée
**Entropie croisée** entre les distributions P et Q :
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Entropie croisée comme fonction de perte
En classification, P est la vraie distribution (étiquette codée à chaud) et Q est la distribution prédite du modèle.
**Entropie croisée binaire (BCE) :**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Entropie croisée catégorique :**
L = −Σᵢ yᵢ log(ŷᵢ)
| Scénario | y (vrai) | ŷ (prédit) | Perte |
|--------------|----------|---------------|------|
| Correct, confiant | 1 | 0,95 | 0,051 |
| Correct, incertain | 1 | 0,55 | 0,598 |
| Faux, confiant | 1 | 0,05 | 2,996 |
| Faux, incertain | 1 | 0,45 | 0,799 |
Minimiser l'entropie croisée équivaut à minimiser la divergence KL par rapport à la vraie distribution - c'est pourquoi elle fonctionne si bien comme fonction de perte.
---

## Capacité de canal
### Modèle de canal de communication
```
X → [Channel] → Y
```

- X : variable aléatoire d'entrée
- Y : variable aléatoire de sortie
- Canal : défini par des probabilités conditionnelles p(y|x)
### Théorème de codage des canaux bruyants de Shannon
Pour un canal de capacité C, si le débit de transmission R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, une communication fiable est impossible.
**Capacité du canal :**
C = max_{p(x)} I(X; Oui)
### Exemples de chaînes importantes
| Chaîne | Descriptif | Capacité |
|---------|-------------|--------------|
| **Binaire symétrique (BSC)** | Retourne chaque bit avec une probabilité p | 1 - H(p) bits |
| **Effacement binaire (BEC)** | Efface chaque bit avec une probabilité ε | 1 - ε bits |
| **Gaussien (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bits |
| **Binaire silencieux** | Transmission parfaite | 1 bit |
---

## Codage source et compression
### Théorème du codage source
Le nombre moyen de bits nécessaires pour coder une source est limité ci-dessous par son entropie :
L ≥ H(X)
Un code optimal atteint L ≈ H(X).
### Codage de Huffman
Un code **sans préfixe** qui attribue des codes plus courts à des symboles plus probables.
| Symbole | Probabilité | Code Huffman | Longueur |
|--------|-------------|-------------|--------|
| Un | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Longueur moyenne : 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bits/symbole
Entropie : H = 1,75 bits/symbole (optimal dans ce cas !)
### Compression sans perte ou avec perte
| Tapez | Principe | Exemples | Limite |
|------|-----------|--------------|-------|
| **Sans perte** | Supprimer la redondance statistique | ZIP, PNG, FLAC | Taux d'entropie H(X) |
| **Avec perte** | Supprimer les informations perceptuellement non pertinentes | JPEG, MP3, H.264 | Fonction taux-distorsion R(D) |
**Théorie débit-distorsion :** Pour une compression avec perte avec distorsion maximale D, le débit minimum est R(D) = min I(X; X̂) sous réserve de E[d(X, X̂)] ≤ D.
---

## Connexions à d'autres champs
### Théorie de l'information et thermodynamique
| Concepts | Théorie de l'information | Thermodynamique |
|---------|---------|----------------|
| Entropie | Entropie de Shannon H(X) | Entropie de Boltzmann S = k_B ln W |
| Entropie maximale | Distribution uniforme | Equilibre thermique |
| divergence KL | Différence de distribution | Différence d'énergie gratuite |
| Information mutuelle | Informations partagées | Corrélations dans les systèmes physiques |
Les formes mathématiques sont identiques : Shannon a délibérément emprunté le terme « entropie » à la mécanique statistique.
### Théorie de l'information et statistiques
| Concepts | Demande |
|---------|-------------|
| Maximum de vraisemblance | Équivalent à minimiser la divergence KL de la distribution empirique à la distribution modèle |
| Informations sur les pêcheurs | Courbure de la divergence KL ; borne inférieure de la variance de l'estimateur (Cramér-Rao) |
| Longueur minimale de description (MDL) | Sélection de modèle en minimisant la longueur totale de codage |
| AIC/BIC | Critères approximatifs de sélection du modèle basé sur KL |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept informatique | Application ML |
|---------------|----------------|
| Perte d'entropie croisée | Perte de classification par défaut (binaire et multi-classes) |
| divergence KL | Perte VAE (terme de régularisation), appariement de répartition, distillation |
| Information mutuelle | Sélection de fonctionnalités (MIFS), apprentissage des représentations (InfoMax), démêlage |
| Entropie | Critère de découpage de l'arbre de décision (gain d'information), exploration en RL (entropie maximale RL) |
| Capacité de canal | Complexité de la communication, compréhension des limites de la généralisation |
| Codage source | Compression des données pour le stockage et la transmission, encodage efficace |
| Entropie maximale | Classificateurs MaxEnt, sélection préalable dans l'inférence bayésienne |
| Distorsion de taux | Comprendre les compromis en matière de compression avec perte et de quantification dans les réseaux de neurones |
| Informations sur les pêcheurs | Descente de gradient naturel, compréhension de la sensibilité des paramètres |
| MDL/AIC/BIC | Sélection de modèle, empêchant le surapprentissage |
---

## Résumé
| Quantité | Formule (discrète) | Signification |
|----------|---------|---------|
| Entropie H(X) | −Σ p(x) log p(x) | Incertitude moyenne |
| Entropie conjointe H(X,Y) | −Σ p(x,y) logp(x,y) | Incertitude totale de la paire |
| Entropie conditionnelle H(Y\|X) | H(X,Oui) − H(X) | Incertitude restante concernant Y étant donné X |
| Informations mutuelles I(X;Y) | H(X) − H(X\|Y) | Informations partagées entre X et Y |
| Divergence KL D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | "Distance" entre les distributions |
| Entropie croisée H(P,Q) | −Σ P(x) log Q(x) | Coût d'encodage utilisant une mauvaise distribution |
| Capacité de canal C | maximum I(X;Y) | Taux de communication fiable maximal |
La théorie de l’information expose les limites fondamentales de ce qui peut être appris, compressé et communiqué. Pour les praticiens de l'apprentissage automatique, il explique pourquoi l'entropie croisée fonctionne comme une fonction de perte, comment mesurer la qualité des représentations apprises et comment réfléchir au compromis entre la complexité du modèle et l'ajustement des données. Les idées de Shannon datant de 1948 restent aussi pertinentes pour l’IA moderne que pour les télécommunications.