<!--
---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mathématiques
Les mathématiques ne sont pas seulement une matière étudiée à l’école : elles sous-tendent presque tous les domaines techniques. La physique l'utilise pour décrire l'univers. L'informatique l'utilise pour concevoir des algorithmes. L'apprentissage automatique l'utilise pour optimiser les poids. La finance l’utilise pour évaluer le risque. La maîtrise de chaque branche n’est pas nécessaire, mais comprendre le paysage – et savoir où chaque branche s’applique – facilite la compréhension d’autres sujets.
---

## Systèmes numériques
Avant toute chose, il est utile de comprendre les types de chiffres avec lesquels vous travaillez. Chaque couche étend la précédente pour résoudre un problème que l'ancienne couche ne pouvait pas résoudre.
| Type de numéro | Ce qu'il comprend | Pourquoi il a été inventé | Exemple |
|---|---|---|---|
| Nombres naturels | 1, 2, 3, 4, ... | Compter les choses | 5 pommes |
| Nombres entiers | 0, 1, 2, 3, ... | Représentant « rien » | 0 degrés |
| Entiers | ..., −2, −1, 0, 1, 2, ... | Dette, température en dessous de zéro | −15°C |
| Nombres rationnels | p/q où q ≠ 0 | Diviser les choses de manière inégale | 1/3, 0,75 |
| Nombres irrationnels | Ne peut pas être exprimé sous forme de fractions | Diagonales, cercles, croissance | √2, π, e |
| Chiffres réels | Tout rationnel + irrationnel | La droite numérique complète | 3.14159... |
| Nombres imaginaires | Multiples de i = √(−1) | Résolution de x² + 1 = 0 | 3i |
| Nombres complexes | a + bi (réel + imaginaire) | Génie électrique, mécanique quantique | 2 + 3i |
---

## Arithmétique et théorie des nombres
Les bases : l'addition, la soustraction, la multiplication, la division et les règles régissant leur ordre.
**Ordre des opérations** (PEMDAS/BODMAS) : Parenthèses → Exposants → Multiplication/Division (de gauche à droite) → Addition/Soustraction (de gauche à droite).
**Les nombres premiers** — nombres entiers supérieurs à 1 sans diviseur autre que 1 et eux-mêmes — sont les atomes de la théorie des nombres. Les premiers : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Pourquoi les nombres premiers sont importants au-delà des cours de mathématiques : le chiffrement moderne (RSA) repose sur le fait que multiplier deux grands nombres premiers est facile, mais la prise en compte du résultat est brutale sur le plan informatique.
**Opérations utiles :**
- Factorisation première : 84 = 2² × 3 × 7
- Plus grand diviseur commun (PGCD) de 24 et 36 : 12
- Le Plus Petit Commun Multiple (LCM) de 4 et 6 : 12
---

## Algèbre
L'algèbre est l'endroit où vous arrêtez de travailler avec des nombres spécifiques et commencez à travailler avec des *relations*. Une variable telle que`x`n'a pas de valeur fixe : elle représente tout ce qui rend l'équation vraie.
**La formule quadratique** résout ax² + bx + c = 0 :
x = (−b ± √(b² − 4ac)) / 2a
**Types de fonctions courants et où ils apparaissent :**
| Fonction | Formule | Forme | Exemple concret |
|---|---|---|---|
| Linéaire | y = mx + b | Ligne droite | Coût unitaire au forfait |
| Quadratique | y = ax² + bx + c | Parabole | Mouvement du projectile, distance de freinage |
| Exponentiel | y = une × b² | Croissance/décroissance rapide | Intérêts composés, croissance démographique, propagation virale |
| Logarithmique | y = log_b(x) | Croissance lente, inverse de l'exponentielle | Échelle de décibels, échelle de pH, complexité de l'algorithme |
**Vocabulaire clé :**
- **Domaine** : toutes les entrées valides (par exemple, ne peut pas diviser par zéro, ne peut pas prendre √ d'un négatif en réels)
- **Plage** : toutes les sorties possibles
- **Pente** (m) : taux de changement — "pour chaque unité de x, y change de m"
- **Intercept** : où la fonction traverse un axe
---

## Géométrie
La géométrie étudie les formes, les tailles et les relations spatiales. On le retrouve partout : les moteurs de jeux l'utilisent pour le rendu, la robotique l'utilise pour la planification des trajectoires, l'architecture l'utilise pour la conception structurelle.
**Formules essentielles :**
| Forme | Propriété | Formule |
|---|---|---|
| Triangle | Somme des angles | 180° |
| Quadrilatère | Somme des angles | 360° |
| Cercle | Circonférence | 2πr |
| Cercle | Zone | πr² |
| Sphère | Volume | (4/3)πr³ |
| Triangle rectangle | Théorème de Pythagore | a² + b² = c² |
**π (pi)** ≈ 3,14159 — le rapport entre la circonférence d'un cercle et son diamètre. Cela apparaît dans des endroits inattendus : probabilité (distribution normale), ingénierie (traitement du signal), même l'équation du principe d'incertitude de Heisenberg.
---

## Calcul
Études de calcul *changement* et *accumulation*. Si l’algèbre gère les instantanés, le calcul gère les films.
### Calcul différentiel
Taux de changement. La dérivée f'(x) vous indique à quelle vitesse f change à tout moment.
| Fonction f(x) | Dérivée f'(x) | Intuitions |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Règle de pouvoir |
| eˣ | eˣ | La seule fonction égale à sa propre dérivée |
| ln(x) | 1/x | Le taux de croissance ralentit à mesure que x augmente |
| péché(x) | cos(x) | Taux de changement d'oscillation |
**Pourquoi les dérivées sont importantes dans le ML :** la descente de gradient (l'algorithme qui entraîne la plupart des réseaux de neurones) fonctionne en calculant les dérivées de la fonction de perte et en allant dans la direction qui réduit les erreurs.
### Règles de différenciation clés
| Règle | Formule | Cas d'utilisation |
|------|---------|--------------|
| **Règle de chaîne** | (f∘g)' = f'(g(x)) · g'(x) | Fonctions imbriquées — rétropropagation dans les réseaux de neurones |
| **Règle du produit** | (fg)' = f'g + fg' | Multiplier deux fonctions de x |
| **Règle du quotient** | (f/g)' = (f'g − fg') / g² | Diviser deux fonctions de x |
### Calcul intégral
Accumulation. L'intégrale représente l'aire sous une courbe. Si les dérivées répondent « à quelle vitesse cela change-t-il ? », les intégrales répondent « combien s'est accumulé ?
Le **théorème fondamental du calcul** relie les deux : la différenciation et l'intégration sont des opérations inverses.
| Intégrale | Résultat | Cas d'utilisation |
|--------------|--------|--------------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Aire sous les courbes polynomiales |
| ∫ eˣ dx | eˣ + C | Croissance totale accumulée |
| ∫ 1/x dx | ln|x| + C | Accumulation logarithmique |
---

## Ensembles
Un **ensemble** est une collection d'objets distincts — le fondement des mathématiques modernes.
| Opération | Symbole | Signification | Exemple (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Syndicat | UNE ∪B | Éléments de l'un ou l'autre ensemble | {1, 2, 3, 4} |
| Intersection | UNE ∩B | Éléments des deux ensembles | {2} |
| Différence | A\B | Éléments dans A mais pas dans B | {1, 3} |
| Ensemble vide | ∅ | Ne contient rien | {} |
| Sous-ensemble | UNE ⊂ B | Tous les éléments de A sont dans B | {1,2} ⊂ {1,2,3} |
La théorie des ensembles apparaît dans les bases de données (les SQL JOIN sont essentiellement des opérations sur des ensembles), les probabilités (les événements sont des ensembles de résultats) et la programmation (ensembles, cartes de hachage).
---

## Bases binaires et numériques
Les ordinateurs pensent en binaire (base 2) : uniquement des 0 et des 1. Les humains pensent en décimal (base 10). Les programmeurs utilisent souvent l'hexadécimal (base 16) comme moyen compact de représenter le binaire.
| Socle | Chiffres utilisés | Exemple | Équivalent décimal |
|---|---|---|---|
| Binaire (base 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Décimal (base 10) | 0-9 | 11 | 11 |
| Hexadécimal (base 16) | 0-9, A-F | B | 11 |
| Hexadécimal | 0-9, A-F | A3 | 160 + 3 = 163 |
**Pourquoi c'est important :** chaque élément de données d'un ordinateur (texte, images, audio, vidéo) n'est en fin de compte que binaire. Un octet (8 bits) peut représenter 256 valeurs distinctes. Les couleurs en CSS (#FF5733), les adresses mémoire (0x7FFF) et les adresses IP utilisent toutes l'hexadécimal car elles compressent les longues chaînes binaires en quelque chose de lisible.
---

## Algèbre linéaire pour le ML et les graphiques
L'algèbre linéaire (vecteurs, matrices et transformations) est le moteur mathématique derrière l'apprentissage automatique, l'infographie, les simulations physiques et les moteurs de recherche.
### Vecteurs
Les **Vecteurs** sont des listes ordonnées de nombres. En ML, chaque point de données est un vecteur de fonctionnalités :
- [23, 1,8, 75] pourrait représenter l'âge, la taille en mètres et le poids d'une personne en kg.
| Opération vectorielle | Formule | Cas d'utilisation |
|-----------------|---------|--------------|
| **Ajout** | une + b = [une₁+b₁, une₂+b₂, ...] | Combinaison de vecteurs de caractéristiques |
| **Multiplication scalaire** | c·a = [c·a₁, c·a₂, ...] | Fonctionnalités de mise à l'échelle |
| **Produit scalaire** | a·b = Σ aᵢbᵢ | Similitude, projections |
| **Norme (ampleur)** | ||une|| = √(Σ aᵢ²) | Longueur du vecteur |
| **Produit croisé** | a × b (3D uniquement) | Vecteur perpendiculaire, aire |
### Matrices
Les **matrices** sont des tableaux de nombres 2D. Les poids d'un réseau neuronal sont stockés sous forme de matrices. Un lot de 100 images peut être une matrice de forme (100, 784) — 100 lignes, chacune avec 784 valeurs de pixels.
**Opérations clés :**
| Opération | Ce qu'il fait | Où il apparaît |
|---|---|---|
| Produit scalaire | Mesure la similarité entre deux vecteurs | Systèmes de recommandation, similarité cosinus |
| Multiplication matricielle | Combine des transformations linéaires | Chaque couche d'un réseau neuronal |
| Valeurs propres/vecteurs propres | Directions d'une matrice mise à l'échelle (pas de rotation) | Réduction de dimensionnalité PCA, PageRank |
| Rang matriciel | Quantité d'informations indépendantes | Compression, approximation de bas rang |
| Transposer | Inverse les lignes et les colonnes | Calcul du gradient |
| Inverse | A⁻¹ tel que A·A⁻¹ = I | Résolution de systèmes linéaires |
**Similitude cosinus** = (a·b) / (||a|| × ||b||) — va de −1 (opposé) à 1 (même direction). C’est ainsi que les moteurs de recherche mesurent si deux documents « concernent la même chose » et comment les modèles d’intégration comparent la similarité sémantique.
---

## Résumé
| Branche | Question fondamentale | Application clé |
|---|---|---|
| Arithmétique et théorie des nombres | Comment se comportent les chiffres ? | Cryptographie, hachage |
| Algèbre | Quel est le rapport entre les inconnues ? | Modélisation, équations |
| Géométrie | Comment fonctionnent les formes et les espaces ? | Graphique, robotique, architecture |
| Calcul | Comment les choses changent-elles ? | Formation aux réseaux de neurones, physique |
| Théorie des ensembles | Quel est le rapport entre les collections ? | Bases de données, probabilités |
| Algèbre linéaire | Comment fonctionnent les transformations ? | ML, graphiques, moteurs de recherche |
Tous ces sujets ne sont pas nécessaires immédiatement. Cependant, à mesure que l’on approfondit un domaine technique, ces fondements deviennent de plus en plus pertinents. Chaque branche devient plus claire une fois que le problème qu’elle est censée résoudre est compris.