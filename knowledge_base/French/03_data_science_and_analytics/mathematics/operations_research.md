---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Recherche Opérationnelle
La recherche opérationnelle (RO) est l'application de méthodes mathématiques à la prise de décision. Né pendant la Seconde Guerre mondiale pour la logistique militaire, il optimise désormais les chaînes d'approvisionnement, planifie les compagnies aériennes, achemine les flottes de livraison, gère les stocks et alloue les ressources dans tous les secteurs. OR fournit la boîte à outils mathématiques pour prendre les meilleures décisions possibles sous contraintes.
---

## Formulations de programmation linéaire
### Formulaire standard
Réduire cᵀx
Sous réserve de : Ax = b, x ≥ 0
### Formulations LP courantes
**Mélange de produits :**
- Variables de décision : xⱼ = quantité de produit j à produire
- Objectif : maximiser le profit Σ pⱼxⱼ
- Contraintes : limites de ressources Σ aᵢⱼxⱼ ≤ bᵢ
**Problème de régime :**
- Variables de décision : xⱼ = quantité de nourriture j à acheter
- Objectif : minimiser le coût Σ cⱼxⱼ
- Contraintes : besoins nutritionnels Σ nᵢⱼxⱼ ≥ rᵢ
**Problème de mélange :**
- Variables de décision : xⱼ = proportion de l'ingrédient j dans le mélange
- Objectif : minimiser les coûts
- Contraintes : exigences de qualité (indice d'octane, solidité, etc.)
### Exemple concret : Planification de la production
Une usine fabrique les produits A et B.
- A nécessite 2 heures de main d'œuvre, 1 kg de matière ; bénéfice 30 $
- B nécessite 1 heure de travail, 3 kg de matériel ; bénéfice 40 $
- Disponible : 40 heures de main d'œuvre, 30 kg de matériel
**Formulation :**
- Maximiser : 30x_A + 40x_B
- Sous réserve de : 2x_A + x_B ≤ 40 (main d'œuvre)
- x_A + 3x_B ≤ 30 (matériau)
- x_A, x_B ≥ 0
**Solution :** Sommets de la région réalisable : (0,0), (20,0), (18,4), (0,10)
- (0,0) : bénéfice = 0
- (20,0) : bénéfice = 600
- (18,4) : profit = 700 ← optimal
- (0,10) : bénéfice = 400
---

## Problème de transport
Déplacer des marchandises de m sources vers n destinations à un coût minimum.
###Formulation
- Variables de décision : xᵢⱼ = quantité expédiée de la source i à la destination j
- Objectif : minimiser Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Sous réserve de : Σⱼ xᵢⱼ = sᵢ (contraintes d'approvisionnement)
- Σᵢ xᵢⱼ = dⱼ (contraintes de demande)
- xᵢⱼ ≥ 0
### Méthodes de résolution
| Méthode | Descriptif | Qualité de la solution initiale |
|--------|-------------|--------------------------------|
| **Coin nord-ouest** | Commencez en haut à gauche, répartissez avec gourmandise | Faisable mais souvent médiocre |
| **Rapprochement de Vogel** | Considérez les coûts des pénalités | Meilleure solution initiale |
| **MODI / Tremplin** | Améliorer la solution initiale de manière itérative | Trouve optimal |
### Exemple concret
| | D1 | D2 | D3 | Approvisionnement |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Demande | 40 | 30 | 30 | 100 |
---

## Problème d'affectation
Affecter n travailleurs à n tâches (un à un) pour minimiser le coût total.
###Formulation
- Variables de décision : xᵢⱼ ∈ {0, 1} (1 si le travailleur i est affecté au travail j)
- Réduire : Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Sous réserve de : Σⱼ xᵢⱼ = 1 (chaque travailleur obtient un emploi)
- Σᵢ xᵢⱼ = 1 (chaque emploi reçoit un travailleur)
### Algorithme hongrois
| Propriété | Valeur |
|--------------|-------|
| Complexité temporelle | O(n³) |
| Optimale ? | Oui |
| Approche | Réduction matricielle + couverture minimale |
**Étapes :**
1. Soustrayez les minimums de ligne de chaque ligne
2. Soustrayez les minimums de colonne de chaque colonne
3. Couvrez tous les zéros avec un nombre minimum de lignes
4. Si lignes = n, affectation optimale trouvée parmi les zéros
5. Sinon, ajustez la matrice et répétez
---

## Optimisation du flux réseau
### Flux de coût minimum
Étant donné un réseau avec des capacités et des coûts en périphérie, trouvez le flux qui satisfait la demande au coût minimum.
**Formulation :**
- Réduire : Σ cᵢⱼxᵢⱼ
- Sous réserve de : conservation des flux à chaque nœud
- Contraintes de capacité : 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Chemin le plus court en tant que flux réseau
Le problème du chemin le plus court est un cas particulier de flux à coût minimum (envoyer 1 unité de s à t).
### Candidatures
| Demande | Modèle de réseau |
|-------------|--------------|
| Chaîne d'approvisionnement | Nœuds = entrepôts, bords = routes d'expédition |
| Communication | Nœuds = routeurs, bords = liens avec bande passante |
| Trafic | Nœuds = intersections, bords = routes avec capacité |
| Gestion de projet | Réseaux CPM/PERT |
---

## Programmation dynamique
La **programmation dynamique (DP)** résout des problèmes complexes en les divisant en sous-problèmes qui se chevauchent.
### Principe d'optimalité de Bellman
Une politique optimale a la propriété que quels que soient l’état et la décision initiale, les décisions restantes doivent constituer une politique optimale pour l’état résultant.
### Éléments clés
| Élément | Descriptif |
|---------|-------------|
| **Scène** | Point de décision (pas de temps, index d'élément) |
| **État** | Informations nécessaires pour prendre une décision |
| **Décision** | Choix fait à chaque étape |
| **Récurrence** | Valeur optimale à l'étape n en termes d'étape n−1 |
### Problèmes DP classiques
| Problème | Récurrence | Complexité |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) avec mémoïsation |
| **Sac à dos** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Chemin le plus court** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) ou O(E log V) |
| **Modifier la distance** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+coût) | O(mn) |
| **Sous-séquence commune la plus longue** | L(i,j) = L(i−1,j−1)+1 si correspond, sinon max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Multiplication de chaîne matricielle** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Exemple concret : 0/1 Sac à dos
Articles : {poids : valeur} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Capacité W = 7.
V(i, w) = valeur maximale utilisant les i premiers éléments avec une capacité w
| je\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Optimal : V(4, 7) = 23 (éléments 1 et 4 : poids 2+5=7, valeur 12+11=23).
---

## Théorie des files d'attente
La théorie des files d’attente étudie les files d’attente : leur durée, combien de temps vous attendez et comment les réduire.
### Notation de Kendall
A/B/c/K/N/D où :
- A = processus d'arrivée (M = Markovien/Poisson, D = déterministe, G = général)
- B = processus de service (mêmes options)
- c = nombre de serveurs
- K = capacité (par défaut ∞)
- N = population (par défaut ∞)
- D = discipline (FIFO, LIFO, Priorité)
### File d'attente M/M/1 (serveur unique)
| Métrique | Formule |
|--------|---------|
| Utilisation | ρ = λ/µ |
| Nombre moyen dans le système | L = ρ/(1−ρ) |
| Temps moyen dans le système | W = 1/(μ−λ) |
| Nombre moyen en file d'attente | L_q = ρ²/(1−ρ) |
| Temps d'attente moyen | W_q = ρ/(μ−λ) |
où λ = taux d'arrivée, μ = taux de service, ρ = utilisation.
### File d'attente M/M/c (plusieurs serveurs)
| Métrique | Formule |
|--------|---------|
| Utilisation | ρ = λ/(cμ) |
| Probabilité d'attente (Erlang C) | P_w = formule complexe impliquant ρ et c |
| Longueur moyenne de la file d'attente | L_q = P_w · ρ/(1−ρ) |
### La loi de Little
L = λW (nombre moyen dans le système = taux d'arrivée × temps moyen)
Cela s’applique à TOUT système de file d’attente, quelles que soient les distributions d’arrivées/services.
### Exemples d'applications
| Scénario | Modèle de file d'attente |
|--------------|-------------|
| Centre d'appels | M/M/c (agents c) |
| Requêtes du serveur Web | M/M/1 ou M/G/1 |
| Urgence hospitalière | M/G/c avec priorités |
| Ligne de fabrication | Réseau de files d'attente |
| Planification du processeur de l'ordinateur | Partage de processeur M/M/1 |
---

## Modèles d'inventaire
### Quantité de commande économique (EOQ)
La quantité de commande optimale qui minimise les coûts totaux de stock.
Q* = √(2DS/H)
| Variables | Signification |
|--------------|---------|
| D | Demande annuelle |
| S | Coût de commande par commande |
| H | Coût de détention par unité et par an |
| Q* | Quantité de commande optimale |
**Coût total à Q* :** TC = √(2DSH)
### Extensions
| Modèle | Rallonge |
|-------|---------------|
| **EOQ avec réductions** | Les remises sur quantité modifient la fonction de coût |
| **Quantité de la commande de production** | Articles produits progressivement et non livrés en une seule fois |
| **Modèle (s, Q)** | Réorganisez les unités Q lorsque l'inventaire tombe au niveau s |
| **Modèle (s, S)** | Commandez jusqu'à S lorsque l'inventaire tombe à s |
| **Modèle de vendeur de journaux** | Demande incertaine sur une seule période |
### Modèle de vendeur de journaux
Quantité de commande optimale pour les stocks de denrées périssables sur une seule période :
P(D ≤ Q*) = c_u / (c_u + c_o)
où c_u = coût de sous-utilisation (perte de profit) et c_o = coût de dépassement (gaspillage).
---

## Planification
### Planification de l'atelier d'emploi
| Notations | Signification |
|--------------|---------|
| n/m/J/C_max | n emplois, m machines, atelier d'emploi, minimiser le makespan |
| Boutique de flux | Tous les travaux visitent les machines dans le même ordre |
| Boutique d'emploi | Chaque tâche a sa propre séquence de machines |
| Boutique ouverte | Aucune contrainte de commande |
### Règles de priorité
| Règle | Descriptif | Effet |
|------|-------------|--------|
| FCFS | Premier arrivé, premier servi | Juste, mais pas optimal |
| SPT | Temps de traitement le plus court en premier | Minimise l'achèvement moyen |
| EDD | Date d'échéance la plus proche en premier | Minimise les retards maximum |
| CR | Ratio critique (échéance restante / temps de traitement) | Équilibré |
| LPT | Temps de traitement le plus long en premier | Bon pour le makespan sur les machines parallèles |
### Algorithme de Johnson (atelier de flux à 2 machines)
Pour n tâches sur 2 machines, en minimisant le makespan :
1. Trouvez l'emploi avec le temps de traitement le plus court
2. S'il se trouve sur la machine 1, planifiez-le d'abord ; si sur la machine 2, planifiez-le en dernier
3. Supprimez ce travail et répétez
Idéal pour 2 machines ; NP-difficile pour 3+ machines.
---

## Pertinence pour l'apprentissage automatique et la science des données
| OU Concept | Demande |
|---------------|-------------|
| Programmation linéaire | Allocation des ressources, optimisation du portefeuille, allocation du budget publicitaire |
| Transport/affectation | Logistique, mise en relation de covoiturage, attribution de tâches |
| Flux de réseau | Optimisation de la chaîne d'approvisionnement, routage du trafic des centres de données |
| Programmation dynamique | Alignement de séquences (bioinformatique), algorithme de Viterbi (HMM), RL (équation de Bellman) |
| Théorie des files d'attente | Planification de la capacité des serveurs, modélisation de la latence, allocation des ressources cloud |
| Modèles d'inventaire | Intégration de la prévision de la demande, ML de la chaîne d'approvisionnement |
| Planification | Orchestration de pipeline ML, planification de tâches GPU, planification de recherche d'hyperparamètres |
| Programmation entière | Sélection de fonctionnalités (binaire), sélection de modèle, conception de réseau |
---

## Résumé
| Sujet | Problème central | Méthode clé |
|-------|-------------|------------|
| Formulations LP | Optimiser l'objectif linéaire avec des contraintes | Simplex, point intérieur |
| Transport | Expédier des marchandises au coût minimum | MODI, tremplin |
| Affectation | Associer les travailleurs aux emplois | Algorithme hongrois |
| Flux de réseau | Flux de routes à travers un réseau | Algorithmes de flux à coût minimum |
| Programmation dynamique | Sous-problèmes qui se chevauchent | Principe de Bellman, mémoïsation |
| Théorie des files d'attente | Analyse de la file d'attente | M/M/1, loi de Little |
| Inventaire | Quand et combien commander | EOQ, vendeur de journaux |
| Planification | Séquencer les tâches sur les machines | Règles de priorité, algorithme de Johnson |
La recherche opérationnelle transforme la prise de décision de l’art à la science. En formulant mathématiquement des problèmes du monde réel, OR fournit des solutions prouvées optimales (ou presque optimales) aux problèmes de logistique, de planification, d'allocation des ressources et de planification qui affectent tous les secteurs. Pour les data scientists, les méthodes OR complètent l'apprentissage automatique : tandis que le ML prédit, OR prescrit - et ensemble, elles constituent la base des systèmes de décision intelligents.