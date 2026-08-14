---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Théorie des jeux
La théorie des jeux est la mathématique de l’interaction stratégique – des situations dans lesquelles votre résultat dépend non seulement de vos propres choix, mais aussi de ceux des autres. Des guerres de prix entre entreprises aux courses aux armements nucléaires, des enchères en ligne à la biologie évolutionniste, la théorie des jeux fournit les outils nécessaires à l’analyse des conflits et de la coopération. Il est devenu de plus en plus pertinent pour l'apprentissage automatique grâce à l'apprentissage par renforcement multi-agents, aux réseaux contradictoires génératifs (GAN) et à la conception de mécanismes pour les plateformes en ligne.
---

## Jeux de forme stratégique
### Définition
Un **jeu de forme stratégique (forme normale)** se compose de :
- Un ensemble de joueurs N = {1, 2, ..., n}
- Ensembles de stratégie S₁, S₂, ..., Sₙ pour chaque joueur
- Fonctions de paiement u₁, u₂, ..., uₙ mappant les profils de stratégie en nombres réels
### Exemple : le dilemme du prisonnier
| | Coopérer (C) | Défaut (D) |
|---|---------------|------------|
| **Coopérer (C)** | (−1, −1) | (−3, 0) |
| **Défaut (D)** | (0, −3) | (−2, −2) |
| Analyse | Résultat |
|--------------|--------|
| Stratégie dominante | Défaut (D domine C pour les deux joueurs) |
| Équilibre de Nash | (D, D) avec gain (−2, −2) |
| Optimale sociale | (C, C) avec gain (−1, −1) |
| Dilemme | La rationalité individuelle mène à l'irrationalité collective |
### Plus de jeux classiques
**Bataille des sexes :**
| | Opéra | Football |
|---|-------|----------|
| Opéra | (2, 1) | (0, 0) |
| Football | (0, 0) | (1, 2) |
Deux équilibres de Nash : (Opéra, Opéra) et (Football, Football).
**Poulet (faucon-colombe) :**
| | Faucon | Colombe |
|---|------|------|
| Faucon | (−10, −10) | (5, 0) |
| Colombe | (0, 5) | (1, 1) |
Deux équilibres de Nash : (Hawk, Dove) et (Dove, Hawk).
---

## Stratégies dominantes
| Concepts | Définition |
|--------------|------------|
| **Strictement dominant** | La stratégie sᵢ offre des gains plus élevés que toute autre stratégie, quels que soient les choix des adversaires |
| **Faiblement dominant** | La stratégie sᵢ offre un gain au moins aussi élevé que n'importe quel autre, et strictement plus élevé pour certains profils d'adversaires |
| **Stratégie dominée** | Une stratégie qui n'est jamais la meilleure réponse |
**Élimination itérative des stratégies dominées :**
1. Supprimez toutes les stratégies strictement dominées
2. Répétez jusqu'à ce qu'il n'y ait plus rien à retirer
3. S’il reste un profil de stratégie, c’est celui de l’équilibre de Nash unique
---

## Équilibre de Nash
Un **équilibre de Nash** est un profil stratégique dans lequel aucun joueur ne peut améliorer ses gains en modifiant unilatéralement sa stratégie.
### Définition
(s₁*, s₂*, ..., sₙ*) est un équilibre de Nash si pour chaque joueur i :
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) pour tout sᵢ ∈ Sᵢ
### Trouver les équilibres de Nash (jeux 2 × 2)
**Meilleure méthode de réponse :**
1. Pour chaque colonne, soulignez la meilleure réponse du joueur 1
2. Pour chaque ligne, soulignez la meilleure réponse du joueur 2
3. Les cellules où les deux sont soulignées sont des équilibres de Nash
### Existence (théorème de Nash)
Tout jeu fini possède au moins un équilibre de Nash (éventuellement dans le cadre de stratégies mixtes).
### Stratégies mixtes
Une **stratégie mixte** est une distribution de probabilité sur des stratégies pures.
| Concepts | Définition |
|--------------|------------|
| Stratégie mixte σᵢ | Distribution de probabilité sur Sᵢ |
| Stratégie mixte NE | Aucun joueur ne peut améliorer les gains attendus en modifiant sa combinaison |
| Assistance | Ensemble de stratégies pures jouées avec une probabilité positive |
**Exemple pratique : pièces de monnaie correspondantes**
| | Têtes | Queues |
|---|-------|-------|
| Têtes | (1, −1) | (−1, 1) |
| Queues | (−1, 1) | (1, −1) |
Pas de stratégie pure NE. NE mixte : les deux jouent H et T avec une probabilité de ½ chacun.
---

## Théorème du Minimax
### Jeux à somme nulle
Dans un **jeu à somme nulle**, le gain d'un joueur est exactement la perte de l'autre : u₁ + u₂ = 0.
### Théorème du Minimax de Von Neumann
Pour chaque jeu à somme nulle à deux joueurs fini :
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
Le **maximin** (meilleur pire des cas pour le joueur 1) est égal au **minimax** (meilleur pire des cas pour le joueur 2). Cette valeur commune est la **valeur du jeu**.
### Résoudre les jeux à somme nulle
Pour un jeu à somme nulle 2×2 avec matrice :
| | L | R |
|---|---|---|
| T | un | b |
| B | c | ré |
Stratégie mixte optimale du joueur 1 : jouer T avec probabilité p = (d−c)/((a−b)+(d−c))
Valeur du jeu : v = (ad−bc)/((a−b)+(d−c))
---

## Jeux de forme étendue
Les jeux avec des mouvements séquentiels sont représentés sous forme d'**arbres de jeu**.
### Concepts clés
| Concepts | Définition |
|--------------|------------|
| **Arbre de jeu** | Arbre montrant toutes les séquences de mouvements possibles |
| **Ensemble d'informations** | Ensemble de nœuds qu'un joueur ne peut pas distinguer |
| **Informations parfaites** | Chaque ensemble d'informations est un singleton (tous les mouvements sont observables) |
| **Sous-jeu parfait NE** | Équilibre de Nash dans chaque sous-jeu |
| **Induction en arrière** | Résoudre à partir de la fin de l'arbre vers l'arrière |
### Théorème de Zermelo
Dans les jeux à deux joueurs finis et à information parfaite, sans aucune chance : soit un joueur a une stratégie gagnante, soit les deux peuvent forcer un match nul (par exemple, les échecs).
---

## Jeux coopératifs
Dans les **jeux coopératifs**, les joueurs peuvent former des accords et des coalitions contraignants.
### Caractéristique Fonction
Un jeu coopératif est défini par une **fonction caractéristique** v : 2^N → ℝ, où v(S) est la valeur que la coalition S peut atteindre.
| Propriété | Définition |
|--------------|------------|
| **Superadditif** | v(S ∪ T) ≥ v(S) + v(T) pour disjoint S, T |
| **Convexe** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) pour S ⊂ T |
### Le noyau
Le **noyau** est l'ensemble des allocations qu'aucune coalition ne peut améliorer en se séparant :
Noyau = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) pour tout S ⊂ N}
Le noyau peut être vide, auquel cas aucune allocation stable n'existe.
### Valeur Shapley
La **valeur Shapley** offre une allocation équitable unique basée sur des contributions marginales :
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Propriété | Déclaration |
|--------------|---------------|
| Efficacité | Σ φᵢ = v(N) (toute la valeur est distribuée) |
| Symétrie | Des contributeurs égaux obtiennent des récompenses égales |
| Joueur factice | Les non-cotisants obtiennent zéro |
| Additivité | φ(v + w) = φ(v) + φ(w) |
**Interprétation :** La valeur Shapley de chaque joueur est sa contribution marginale moyenne dans tous les ordres possibles de formation de coalition.
### Exemple concret
Trois joueurs : v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Joueur | Contributions marginales (moyennes sur les commandes) | Valeur Shapley |
|--------|----------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27,5 |
| 3 | (100+70+60+70+60+0)/6 | 35,0 |
(Calculé précisément en utilisant la formule de Shapley pour chaque permutation.)
---

## Conception du mécanisme
**La conception de mécanismes** est une « théorie des jeux inverses » : au lieu d'analyser des jeux donnés, concevez des jeux qui produisent les résultats souhaités.
### Le principe de révélation
Tout mécanisme qui permet d'obtenir un résultat souhaité peut être remplacé par un **mécanisme de révélation directe** où dire la vérité est un équilibre de Nash.
### Théorie des enchères
| Type d'enchère | Règles | Équivalence des revenus |
|-------------|-------|-----------|
| **Offre scellée au premier prix** | Le plus offrant gagne et paie son offre | Toutes les enchères standards génèrent les mêmes revenus attendus |
| **Offre scellée au deuxième prix (Vickrey)** | Le plus offrant gagne, paie la deuxième offre la plus élevée | (sous valeurs privées indépendantes) |
| **Anglais (croissant)** | Les prix augmentent ; premier à accepter les victoires | — |
| **Néerlandais (décroissant)** | Les prix baissent ; premier à accepter les victoires | — |
### Ventes aux enchères Vickrey (deuxième prix)
**Stratégie dominante :** Offrez votre vraie valeur.
| Propriété | Déclaration |
|--------------|---------------|
| Enchères véridiques | Stratégie faiblement dominante |
| Efficacité | L'article est attribué au plus offrant |
| Revenus | Mêmes revenus attendus que le premier prix (théorème d'équivalence des revenus) |
### Conception optimale des enchères (Myerson)
L’enchère maximisant les revenus :
- Attribue au soumissionnaire avec la **valorisation virtuelle** la plus élevée
- Fixe un prix de réserve
- Valorisation virtuelle : ψ(v) = v − (1−F(v))/f(v)
---

## Connexions à l'apprentissage automatique
### Réseaux contradictoires génératifs (GAN)
Les GAN sont un jeu à deux joueurs entre un générateur G et un discriminateur D :
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Concept de théorie des jeux | Équivalent GAN |
|----------------------------------|-----------------|
| Jeu à somme nulle à deux joueurs | Générateur vs discriminateur |
| Équilibre de Nash | G génère des données réelles, D en produit ½ partout |
| Minimax | La fonction objectif GAN |
| Mode effondrement | Incapacité d'atteindre l'équilibre |
### Apprentissage par renforcement multi-agents (MARL)
| Concepts | Demande MARL |
|---------|-----------------|
| Équilibre de Nash | Politiques stables dans les paramètres multi-agents |
| Minimax | Des politiques robustes contre les opposants |
| Jeux coopératifs | Formation de coalitions, répartition des tâches |
| Valeur Shapley | Cession de crédit (quel agent a contribué à quoi ?) |
| Conception de mécanismes | Concevoir des incitations dans des systèmes multi-agents |
| Jeu fictif | Algorithme d'apprentissage convergeant vers l'équilibre de Nash |
### Autres connexions ML
| Demande | Outil de théorie des jeux |
|-------------|-----------------|
| Conception d'enchères publicitaires (Google, Facebook) | Conception de mécanismes, théorie des enchères |
| Conception d'une place de marché (Uber, Airbnb) | Théorie de l'appariement, conception de mécanismes |
| Robustesse contradictoire | Jeux à somme nulle entre attaquant et défenseur |
| Division équitable | Valeur Shapley, allocation sans envie |
| Apprentissage fédéré | Théorie des jeux coopératifs pour la mesure des contributions |
| Systèmes de recommandation | Conception de mécanismes pour une élicitation véridique des préférences |
---

## Résumé
| Concepts | Idée de base | Résultat clé |
|---------|-----------|------------|
| Jeux de forme stratégique | Joueurs, stratégies, gains | Représentation matricielle du jeu |
| Stratégies dominantes | Meilleur indépendamment des autres | Élimination itérée |
| Équilibre de Nash | Pas de déviation unilatérale rentable | Existe dans chaque jeu fini |
| Stratégies mixtes | Randomiser les actions | Théorème d'existence de Nash |
| Minimax | Meilleur pire des cas (somme nulle) | Théorème du minimax de Von Neumann |
| Forme étendue | Mouvements séquentiels | Induction vers l'arrière, perfection du sous-jeu |
| Jeux coopératifs | Coalitions contraignantes | Noyau, valeur Shapley |
| Conception de mécanismes | Concevoir des jeux pour obtenir des résultats | Principe de révélation, enchères optimales |
| Théorie des enchères | Vendre via la concurrence | Équivalence des revenus, enchères Vickrey |
La théorie des jeux est la mathématique de la pensée stratégique. Dans un monde de plus en plus peuplé d’agents d’IA en interaction, de marchés automatisés et de systèmes contradictoires, la théorie des jeux fournit la boîte à outils essentielle pour prédire les comportements, concevoir des mécanismes et construire des systèmes multi-agents robustes. Pour les data scientists, il explique comment fonctionnent les GAN, comment les enchères en ligne génèrent des milliards de revenus et comment créer des systèmes d'IA qui fonctionnent bien dans des environnements concurrentiels.