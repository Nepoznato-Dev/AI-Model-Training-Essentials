---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Théorie du contrôle
La théorie du contrôle consiste à faire en sorte que les systèmes se comportent comme vous le souhaitez. Des thermostats aux pilotes automatiques, des bras robotiques aux réacteurs chimiques, les systèmes de contrôle détectent, décident et agissent pour maintenir le comportement souhaité. Le domaine fournit des outils rigoureux pour analyser la stabilité, les performances et la robustesse – des concepts qui ont migré vers l'apprentissage par renforcement, le réglage des hyperparamètres et les systèmes adaptatifs.
---

## Concepts fondamentaux
### Boucle ouverte vs boucle fermée
| Tapez | Descriptif | Exemple | Avantage |
|------|-------------|---------|---------------|
| **Boucle ouverte** | Action de contrôle indépendante de la sortie | Minuterie machine à laver | Simple, aucun capteur nécessaire |
| **Boucle fermée (retour d'information)** | L'action de contrôle dépend du résultat | Thermostat, régulateur de vitesse | Rejette les perturbations, robuste |
### Éléments du diagramme
| Élément | Symbole | Fonction |
|---------|--------|--------------|
| **Plante** | G(s) | Le système contrôlé |
| **Contrôleur** | C(s) | Calcule l'action de contrôle |
| **Capteur** | H(s) | Mesure la sortie |
| ** Jonction sommatrice ** | ⊕ | Erreur de calcul : r − y |
| **Référence** | r(t) | Sortie souhaitée |
| **Erreur** | e(t) = r(t) − y(t) | Différence entre souhaité et réel |
| **Perturbation** | ré(t) | Apports indésirables affectant l'installation |
### Fonction de transfert en boucle fermée
Pour un système de rétroaction négative standard :
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Quantité | Formule |
|--------------|---------|
| Fonction de transfert en boucle ouverte | L(s) = C(s)G(s)H(s) |
| Fonction de transfert en boucle fermée | T(s) = L(s)/H(s) / (1 + L(s)) |
| Fonction de transfert d'erreur | E(s)/R(s) = 1 / (1 + L(s)) |
| Sensibilité | S(s) = 1 / (1 + L(s)) |
---

## Fonctions de transfert
Une **fonction de transfert** H(s) = Y(s)/X(s) décrit la relation entrée-sortie d'un système linéaire invariant dans le temps (LTI) dans le domaine de Laplace.
### Formulaires standards
| Système | Fonction de transfert | Paramètres |
|--------|---------|------------|
| **Premier ordre** | K/(τs + 1) | K = gain, τ = constante de temps |
| **Deuxième ordre** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = fréquence propre, ζ = taux d'amortissement |
| **Intégrateur** | K/s | — |
| **Différentiateur** | Ks | — |
| **Retard** | e^{−sT_d} | T_d = temporisation |
### Comportement du système de second ordre
| Rapport d'amortissement ζ | Comportement | Emplacements des pôles |
|-----------------|-----------|---------------|
| ζ = 0 | Oscillation non amortie | Pur imaginaire |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Suramorti (lent, pas d'oscillation) | Réel, distinct |
### Mesures de performances (réponse par étapes)
| Métrique | Formule (2ème ordre, sous-amorti) | Descriptif |
|--------|------------------------|-------------|
| Temps de montée (t_r) | ≈ 1,8/ωₙ | Il est temps de passer de 10 % à 90 % |
| Heure de pointe (t_p) | π/(ωₙ√(1−ζ²)) | Temps jusqu'au premier maximum |
| Dépassement (M_p) | e^{−πζ/√(1−ζ²)} × 100 % | Pic maximum au-dessus de la valeur finale |
| Temps de stabilisation (t_s) | ≈ 4/(ζωₙ) | Il est temps de rester à moins de 2% de la finale |
| Erreur en régime permanent | Dépend du type de système | Différence entre souhaité et réel lorsque t → ∞ |
---

## Contrôleurs PID
Le **régulateur PID** est le régulateur le plus utilisé dans l'industrie (plus de 90 % des régulateurs industriels).
### Formule PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Dans le domaine de Laplace : C(s) = K_p + K_i/s + K_d s
| Terme | Effet | Trop | Trop peu |
|------|--------|----------|------------|
| **Proportionnel (K_p)** | Réagit à l'erreur actuelle | Oscillation, instabilité | Réponse lente, erreur importante |
| **Intégrale (K_i)** | Élimine l'erreur d'état stable | Dépassement, oscillation | Décalage persistant |
| **Dérivé (K_d)** | Prédit les erreurs futures (amortissement) | Amplification du bruit | Mauvais rejet des perturbations |
### Méthodes de réglage PID
| Méthode | Approche |
|--------|----------|
| **Ziegler-Nichols** | Augmentez K_u jusqu'à l'oscillation ; utiliser K_u et la période P_u pour définir les gains |
| **Cohen-Coon** | Basé sur des paramètres de réponse échelonnée (gain, constante de temps, temps mort) |
| **IMC (Contrôle du modèle interne)** | Basé sur un modèle de processus ; offre une bonne robustesse |
| **Réglage automatique** | Identification + réglage en ligne (de nombreux contrôleurs modernes) |
| **Manuel** | Commencez par K_p uniquement, ajoutez K_i pour supprimer le décalage, ajoutez K_d pour l'amortissement |
### Règles de Ziegler-Nichols
1. Définir K_i = K_d = 0
2. Augmenter K_p jusqu'à oscillation soutenue : gain ultime K_u, période P_u
3. Définir les gains :
| Contrôleur | K_p | K_i | K_d |
|-----------|-----|-----|-----|
| P | 0,5K_u | — | — |
| PI | 0,45K_u | 1,2K_u/P_u | — |
| PID | 0,6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Analyse de stabilité
Un système est **stable** si sa sortie reste limitée pour des entrées limitées (stabilité BIBO).
### Stabilité basée sur les pôles
| État | Stabilité |
|-----------|---------------|
| Tous les pôles dans le demi-plan gauche (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Instable |
| Pôles sur un axe imaginaire (Re(s) = 0) | Marginalement stable (ou instable en cas de répétition) |
### Critère de Routh-Hurwitz
Détermine la stabilité sans calculer explicitement les pôles. Construit le tableau de Routh à partir des coefficients polynomiaux caractéristiques.
**Règle :** Le nombre de changements de signe dans la première colonne est égal au nombre de pôles du demi-plan droit.
### Critère de stabilité de Nyquist
Trace la réponse en fréquence en boucle ouverte L(jω) dans le plan complexe.
**Règle :** Le système en boucle fermée est stable si le tracé de Nyquist encercle le point (−1, 0) dans le sens inverse des aiguilles d'une montre un nombre de fois égal au nombre de pôles instables en boucle ouverte.
**Marge de gain :** Quel gain peut augmenter avant l'instabilité (distance du tracé à −1 sur l'axe réel).
**Marge de phase :** Quel est le décalage de phase qui peut augmenter avant l'instabilité (angle entre le tracé et le cercle unitaire au croisement du gain).
### Analyse du tracé de Bode
Trace le gain (dB) et la phase (degrés) en fonction de la fréquence (échelle logarithmique).
| Métrique | Définition | Valeur souhaitée |
|--------|-----------|---------------|
| **Gain de marge (GM)** | Augmentation du gain pour atteindre 0 dB en phase = −180° | > 6 dB |
| **Marge de phase (PM)** | Phase au croisement du gain (0 dB) + 180° | > 45° |
| **Gagnez le crossover** | Fréquence où gain = 0 dB | — |
| **Croisement de phases** | Fréquence où phase = −180° | — |
---

## Représentation espace-état
Pour les systèmes multi-entrées multi-sorties (MIMO), la forme espace d’états est plus naturelle que les fonctions de transfert.
### Formulaire standard
ẋ(t) = Ax(t) + Bu(t) (équation d'état)
y(t) = Cx(t) + Du(t) (équation de sortie)
| Matrice | Nom | Dimensions |
|--------|------|---------------|
| Un | Matrice système/état | n × n |
| B | Matrice d'entrée | n × m |
| C | Matrice de sortie | p × n |
| D | Matrice de traversée | p × m |
### Fonction de transfert depuis l'espace d'état
G(s) = C(sI − A)⁻¹B + D
### Contrôlabilité et observabilité
| Propriété | Test | Signification |
|--------------|------|---------|
| **Contrôlable** | Rang[C_B] = n (où C_B = [B, AB, A²B, ...]) | Peut se diriger vers n'importe quel état |
| **Observables** | Rang[O_B] = n (où O_B = [C; CA; CA²; ...]) | Peut déterminer l'état à partir de la sortie |
Un système doit être contrôlable pour être stabilisable par rétroaction et observable pour l'estimation de l'état.
### Commentaires sur l'état
u = −Kx + r (retour d'état complet)
Boucle fermée : ẋ = (A − BK)x + Br
**Placement des pôles :** Choisissez K tel que A − BK ait les valeurs propres (pôles) souhaitées.
---

## Contrôle optimal
### Régulateur quadratique linéaire (LQR)
Minimiser : J = ∫₀^∞ (xᵀQx + uᵀRu) dt
où Q ≥ 0 (coût de l’état) et R > 0 (coût de contrôle).
**Solution :** u = −Kx où K = R⁻¹BᵀP et P résout l'**équation algébrique de Riccati :**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Réglage | Effet |
|--------|--------|
| Augmenter Q | Réponse plus rapide, plus d'effort de contrôle |
| Augmenter R | Réponse plus lente, moins d'effort de contrôle |
| Q ≫ R | Contrôle agressif (comme un K_p élevé) |
### Filtre de Kalman
L'estimateur d'état optimal pour les systèmes linéaires avec bruit gaussien.
**Modèle du système :**
ẋ = Ax + Bu + w (bruit de processus w ~ N(0, Q))
y = Cx + v (bruit de mesure v ~ N(0, R))
**Équations du filtre de Kalman :**
- Prédire : x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Mise à jour : K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Le filtre de Kalman est le double LQR : il minimise la variance de l'erreur d'estimation.
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept de théorie du contrôle | Demande |
|----------------------|-------------|
| Contrôle des commentaires | Taux d'apprentissage adaptatifs, stabilisation de la formation |
| Contrôleurs PID | Réglage des hyperparamètres, contrôle de la température dans les centres de données |
| Modèles d'espace d'état | Modélisation de séries chronologiques, réseaux de neurones récurrents |
| Filtre de Kalman | Suivi, fusion de capteurs, estimation d'état, prévision de séries chronologiques |
| LQR / contrôle optimal | Apprentissage par renforcement (contrôle LQG), robotique |
| Analyse de stabilité | Dynamique de formation des GAN, convergence des algorithmes RL |
| Contrôlabilité/observabilité | Comprendre l'expressivité RNN, identification du système |
| Fonctions de transfert | Comprendre les CNN en tant que filtres linéaires, analyse du domaine fréquentiel |
| Nyquist/Bode | Analyse de robustesse pour les systèmes adaptatifs |
| Placement des poteaux | Concevoir la dynamique des systèmes appris (Neural ODE) |
---

## Résumé
| Concepts | Idée de base | Outil clé |
|---------|-----------|--------------|
| Commentaires | Utiliser la sortie pour corriger l'entrée | Fonction de transfert en boucle fermée |
| Fonction de transfert | Relation entrée-sortie dans le domaine s | G(s) = Y(s)/X(s) |
| Contrôle PID | Proportionnelle + Intégrale + Dérivée | Contrôleur industriel le plus utilisé |
| Stabilité | Sortie limitée pour entrée limitée | Routh-Hurwitz, Nyquist, Bode |
| Espace d'état | Représentation interne de l'État | ẋ = Hache + Bu, y = Cx + Du |
| Contrôlabilité | Pouvons-nous atteindre n’importe quel état ? | Test de classement sur la matrice de contrôlabilité |
| Observabilité | Peut-on en déduire l’État ? | Test de classement sur matrice d'observabilité |
| LQR | Retour d'information sur l'état optimal | Équation de Riccati |
| Filtre de Kalman | Estimation de l'état optimal | Cycle de prévision-mise à jour |
La théorie du contrôle consiste à faire en sorte que les systèmes fassent ce que vous voulez : de manière fiable, robuste et efficace. Ses principes de rétroaction, de stabilité et d’optimalité se sont révélés universels, apparaissant dans des domaines allant de la robotique à l’apprentissage par renforcement, de l’économie à la biologie. Pour les data scientists, la théorie du contrôle fournit le langage nécessaire pour comprendre les systèmes adaptatifs, concevoir des procédures de formation stables et créer des agents intelligents qui interagissent avec des environnements dynamiques.