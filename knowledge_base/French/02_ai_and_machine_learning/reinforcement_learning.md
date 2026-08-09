---
# Métadonnées
titre : "Apprentissage par renforcement"
description : "MDP, Q-learning, gradients politiques, RLHF, systèmes multi-agents"
catégorie : "IA et Machine Learning"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances sur l'IA et l'apprentissage automatique"
next_review : "2027-08-05"
#Classement
tags : [renforcement, apprentissage, IA et apprentissage automatique]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "9 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Apprentissage par renforcement
L'apprentissage par renforcement (RL) est la façon dont les machines apprennent à prendre des séquences de décisions par essais et erreurs. Contrairement à l’apprentissage supervisé, où la bonne réponse est fournie pour chaque exemple, RL ne donne à un agent qu’un signal de récompense – et l’agent doit déterminer quelles actions conduisent aux meilleurs résultats au fil du temps. C'est l'approche derrière AlphaGo, le contrôle robotique, l'IA de jeu et, surtout, RLHF, la technique utilisée pour aligner les grands modèles de langage modernes sur les préférences humaines.
---

## Concepts de base
RL présente la prise de décision comme une boucle entre un **agent** et un **environnement**.
| Composant | Rôle | Exemple |
|---------------|------|--------------|
| **Agent** | Le décideur | Un programme d'échecs, un robot, un modèle de langage |
| **Environnement** | Le monde avec lequel l'agent interagit | L'échiquier, un entrepôt, une conversation |
| **État** | La situation actuelle | Position du tableau, lectures des capteurs du robot, historique des discussions |
| **Action** | Ce que l'agent peut faire | Déplacez une pièce, tournez à gauche, générez un jeton |
| **Récompense** | Signal de rétroaction (nombre scalaire) | +1 pour gagner, -1 pour planter, score de préférence humaine |
| **Politique** | Stratégie mappant les états aux actions | "Si le roi est menacé, déplacez-le" |
| **Fonction valeur** | Récompense cumulée attendue d'un État | "Cette position au conseil d'administration vaut environ +3 points" |
### La boucle RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

L'objectif de l'agent est de maximiser la **récompense cumulative** au fil du temps, et pas seulement la récompense immédiate. C’est ce qui différencie fondamentalement l’apprentissage réel de l’apprentissage supervisé.
---

## Différences clés par rapport aux autres paradigmes d'apprentissage
| Aspects | Apprentissage supervisé | Apprentissage non supervisé | Apprentissage par renforcement |
|--------|---------|-----------|----------------------|
| **Signal** | Corriger les étiquettes pour chaque exemple | Aucune étiquette ; trouver une structure | Récompense scalaire, souvent retardée |
| **Commentaires** | Immédiat | Aucun | Retardé et clairsemé |
| **Séquence** | Chaque exemple est indépendant | Chaque exemple est indépendant | Les actions affectent les états futurs |
| **Objectif** | Minimiser l'erreur de prédiction | Découvrez les modèles | Maximiser la récompense cumulée |
---

## Processus décisionnels de Markov (MDP)
Les MDP sont le cadre mathématique du RL. Ils supposent que l'avenir dépend uniquement de l'état actuel, et non de l'histoire de la façon dont vous y êtes arrivé (la **propriété de Markov**).
| Composant | Notations | Signification |
|-----------|----------|---------|
| **États** | S | Toutes les situations possibles dans lesquelles l'agent peut se trouver |
| **Actions** | Un | Tout ce que l'agent peut faire |
| **Fonction de transition** | P(s' \| s, une) | Probabilité d'atteindre les états s' après avoir pris une mesure a dans l'état s |
| **Fonction de récompense** | R(s, une, s') | Récompense reçue pour la transition |
| **Facteur de remise** | γ (gamma) | Quelle valeur donner aux récompenses futures par rapport aux récompenses immédiates (0 à 1) |
Le **rendement** (récompense totale à prix réduit) est :
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Un facteur d’actualisation élevé (γ proche de 1) signifie que l’agent est prévoyant. Un faible signifie qu'il s'agit d'une vision à courte vue.
---

## Algorithmes RL classiques
### Méthodes basées sur la valeur
Ceux-ci apprennent à quel point chaque état (ou paire état-action) est bon.
| Algorithme | Idée clé | Limitation |
|-----------|----------|------------|
| **Q-Apprentissage** | Apprenez un tableau de valeurs Q : Q(état, action) = récompense attendue | Ne s'adapte pas aux grands espaces d'état |
| **Réseau Q profond (DQN)** | Utiliser un réseau neuronal pour approximer les valeurs Q | Ne gère que les actions discrètes ; peut être instable |
| **Double DQN** | Corriger le biais de surestimation de Q-learning | Encore limité à des actions discrètes |
Règle de mise à jour de Q-learning :
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Méthodes basées sur des politiques
Ceux-ci apprennent directement la politique (stratégie) sans estimer de valeurs.
| Algorithme | Idée clé | Avantage |
|-----------|----------|---------------|
| **RENFORCER** | gradient politique de Monte Carlo ; mettre à jour la politique en direction de bons résultats | Simple; fonctionne avec des actions continues |
| **PPO** (optimisation de la politique proximale) | Coupez les mises à jour des politiques pour éviter des changements importants et déstabilisants | Écurie; largement utilisé; bon défaut |
| **TRPO** | Méthode de région de confiance pour les mises à jour de stratégie | Plus fondé sur des principes que le PPO ; plus difficile à mettre en œuvre |
### Méthodes acteur-critique
Combinez le meilleur des deux : un **acteur** (politique) et un **critique** (fonction de valeur).
| Algorithme | Idée clé |
|-----------|----------|
| **A2C/A3C** | Avantage Acteur-Critique ; utilise l'estimation des avantages pour réduire la variance |
| **SAC** (Acteur-Critique Soft) | Maximiser la récompense tout en maintenant l'exploration (régularisation de l'entropie) |
| **TD3** (DDPG double retardé) | Aborder la surestimation dans les espaces d'action continue |
---

## RLHF : Apprentissage par renforcement à partir du feedback humain
RLHF est la technique qui a rendu ChatGPT possible. Il comble le fossé entre un modèle capable de prédire le texte et un modèle qui produit des résultats que les humains trouvent réellement utiles.
### Les trois étapes
| Étape | Que se passe-t-il | Sortie |
|------|-------------|--------|
| **1. Réglage fin supervisé (SFT)** | Affiner un modèle pré-entraîné sur des exemples écrits par des humains de haute qualité | Un modèle qui suit raisonnablement bien les instructions |
| **2. Formation de modèle de récompense** | Les humains comparent des paires de sorties de modèles ; former un modèle pour prédire les préférences humaines | Un modèle de récompense qui évalue la qualité du résultat |
| **3. Optimisation RL** | Utilisez PPO pour affiner le modèle SFT afin de maximiser les scores du modèle de récompense | Un modèle aligné sur les préférences humaines |
### Pourquoi la RLHF est importante
Sans RLHF, un modèle linguistique est comme un étudiant qui a lu tous les livres mais ne sait pas comment se comporter dans une conversation. Il peut générer du texte, mais celui-ci peut être inutile, toxique ou complètement passer à côté de l'essentiel. RLHF enseigne au modèle *ce que veulent les humains* – pas seulement à quoi ressemble le texte.
### Variantes et alternatives
| Méthode | Descriptif | Avantage |
|--------|-------------|---------------|
| **DPO** (Optimisation des préférences directes) | Évitez le modèle de récompense ; optimiser directement la politique à partir des préférences humaines | Plus simple ; pas de modèle de récompense distinct pour s'entraîner |
| **RLAIF** | Utilisez l'IA (plutôt que les humains) pour générer des étiquettes de préférence | Moins cher que l'étiquetage humain |
| **IA constitutionnelle** | Utiliser un ensemble de principes pour guider le comportement du modèle sans étiquettes humaines | Plus évolutif ; L'approche anthropique |
| **GRPO** (optimisation de la politique relative de groupe) | Comparez les résultats au sein d'un groupe plutôt qu'avec un modèle distinct | Utilisé dans DeepSeek-R1 ; réduit le besoin d'un réseau de valeur |
---

## Exploration vs Exploitation
C’est la tension centrale de RL. **Exploitation** signifie choisir des actions dont vous savez qu'elles fonctionnent bien. **Exploration** signifie essayer de nouvelles choses pour découvrir des stratégies potentiellement meilleures.
| Stratégie | Comment ça marche | Compromis |
|--------------|-------------|---------------|
| **ε-gourmand** | Choisissez la meilleure action la plupart du temps ; action aléatoire avec probabilité ε | Simple mais inefficace |
| **Exploration Boltzmann** | Choisir les actions de manière probabiliste en fonction de leurs valeurs estimées | Plus doux que ε-gourmand |
| **UCB** (limite de confiance supérieure) | Préférer les actions avec une forte incertitude (optimisme face à l'incertitude) | Bonnes garanties théoriques |
| **Régularisation de l'entropie** | Ajouter un bonus pour visiter divers États (utilisé dans SAC, PPO) | Encourage l'exploration naturelle |
---

## Apprentissage par renforcement multi-agents
Lorsque plusieurs agents apprennent simultanément, la dynamique devient bien plus complexe.
| Scénario | Défi | Exemple |
|----------|-----------|---------|
| **Coopérative** | Les agents doivent se coordonner ; l'attribution de crédit est difficile | Équipes de football robotisées ; réseaux de capteurs distribués |
| **Compétitif** | Les adversaires s’adaptent ; l'environnement n'est pas stationnaire | IA de jeu (poker, StarCraft) ; cybersécurité |
| **Mixte** | Certains agents coopèrent, d'autres rivalisent | Marchés aux enchères ; systèmes de circulation |
| Algorithme | Descriptif |
|---------------|-------------|
| **MADDPG** | Version multi-agents de DDPG ; critique centralisé, acteurs décentralisés |
| **MAPPO** | PPO multi-agents ; largement utilisé dans la pratique |
| **Auto-jeu** | Les agents s'entraînent contre des copies d'eux-mêmes (AlphaGo, AlphaStar) |
---

## Transfert Sim-vers-Réel
Entraîner des robots dans le monde réel est lent et dangereux. Au lieu de cela, les agents s’entraînent à la simulation et se transfèrent à la réalité.
| Défi | Solutions |
|-----------|----------|
| **Écart de réalité** (simulation ≠ monde réel) | Randomisation de domaine : faire varier les paramètres physiques pendant l'entraînement |
| **Échantillon d'inefficacité** | Utilisez le RL basé sur un modèle ou entraînez-vous sur de grandes simulations parallèles |
| **Sécurité** | RL contraint : pénaliser les actions à risque lors de l'entraînement |
| **Observabilité partielle** | Entraînez-vous avec des capteurs bruyants et des observations retardées |
Des entreprises comme Boston Dynamics et Tesla utilisent largement la simulation, mais l'écart entre les performances simulées et physiques reste l'un des plus grands défis du domaine.
---

## Outils et cadres
| Outil | Objectif | Idéal pour |
|------|---------|--------------|
| **Lignes de base stables3** | Implémentations Python propres de PPO, SAC, TD3, DQN | Apprentissage et prototypage |
| **RLlib** | Bibliothèque RL évolutive construite sur Ray | Formation distribuée à grande échelle |
| **CleanRL** | Implémentations de fichiers uniques pour la recherche | Comprendre les algorithmes en profondeur |
| **Gymnase (OpenAI)** | Interface d'environnement standardisée | Définir les problèmes RL |
| **Isaac Gym / Isaac Lab** | Simulation physique accélérée par GPU | Robotique, de la simulation au réel |
| **TRL** (Bibliothèque Transformer RL) | RLHF, DPO, PPO pour les modèles linguistiques | Aligner les LLM |
| **OpenRLHF** | Cadre RLHF distribué | Former de grands modèles avec RLHF |
---

## Conseils pratiques
- **Commencez par PPO.** C'est l'algorithme général le plus fiable. Si vous ne savez pas quoi utiliser, PPO est la valeur par défaut.
- **Normalisez vos récompenses.** La mise à l'échelle des récompenses affecte considérablement la stabilité de l'entraînement.
- **Utilisez des environnements vectorisés.** L'exécution de plusieurs environnements en parallèle (par exemple, 8 à 64) stabilise les estimations de gradient et accélère considérablement l'entraînement.
- **Surveillez à la fois la récompense et l'entropie.** Si l'entropie tombe à zéro, votre agent a arrêté l'exploration et peut être bloqué dans un optimal local.
- **La création de récompenses est un art.** Concevoir la bonne fonction de récompense est souvent la partie la plus difficile. Les récompenses rares (uniquement à la fin) rendent l'apprentissage extrêmement lent. Des récompenses denses et bien conçues guident l'agent mais peuvent introduire un comportement involontaire.
- **RLHF est fragile.** De petites modifications du modèle de récompense ou des hyperparamètres PPO peuvent entraîner d'importantes baisses de qualité. DPO est une alternative plus stable si vous n'avez pas besoin du pipeline RLHF complet.
---

## Résumé
L'apprentissage par renforcement est l'étude de la manière dont les agents apprennent à prendre des décisions par interaction. Cela va des algorithmes classiques comme Q-learning aux méthodes modernes de RL profondes comme PPO et SAC, et il sous-tend certaines des avancées récentes les plus importantes en matière d'IA - du jeu à l'alignement des modèles de langage. Le principal défi reste le même : comment apprendre un comportement optimal lorsque le feedback est retardé, clairsemé et bruyant ? La réponse – des essais et des erreurs, guidés par des mathématiques intelligentes – s’avère être l’une des idées les plus puissantes de toute l’intelligence artificielle.