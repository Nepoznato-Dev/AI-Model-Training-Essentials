---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Théorie des jeux et réflexion stratégique
La théorie des jeux est l'étude mathématique des interactions stratégiques, c'est-à-dire des situations dans lesquelles votre résultat dépend non seulement de ce que vous faites, mais aussi de ce que font les autres. Cela s’applique partout : concurrence commerciale, relations internationales, enchères, négociations, biologie évolutive et décisions quotidiennes comme le choix d’un itinéraire dans la circulation. L'idée centrale est que les acteurs rationnels dans des situations stratégiques ne se contentent pas d'optimiser leur propre stratégie : ils anticipent ce que les autres feront, et d'autres font de même.
---

## Concepts fondamentaux
### Terminologie clé
| Terme | Définition |
|------|-----------|
| **Jeu** | Toute situation avec deux ou plusieurs décideurs (acteurs) dont les choix affectent les résultats de chacun |
| **Joueur** | Un décideur dans le jeu |
| **Stratégie** | Un plan d'action complet pour chaque situation qui pourrait survenir |
| **Récompense** | Le résultat qu'un joueur reçoit d'une combinaison particulière de stratégies |
| **Équilibre de Nash** | Un ensemble de stratégies où aucun joueur ne peut améliorer ses gains en changeant unilatéralement sa stratégie |
| **Stratégie dominante** | Une stratégie qui est la meilleure indépendamment de ce que font les autres joueurs |
| **Jeu à somme nulle** | Le gain d'un joueur est exactement la perte d'un autre |
| **Jeu à somme non nulle** | Les joueurs peuvent potentiellement tous gagner ou tous perdre |
| **Jeu coopératif** | Les joueurs peuvent conclure des accords contraignants |
| **Jeu non coopératif** | Aucun accord contraignant ; chaque joueur agit dans son propre intérêt |
---

## Jeux classiques
### Le dilemme du prisonnier
Deux suspects sont arrêtés. Chacun peut coopérer (garder le silence) ou faire défaut (avouer).
| | B coopère | Défauts B |
|---|-------------|---------------|
| **A coopère** | A : 1 an, B : 1 an | A : 10 ans, B : gratuit |
| **A Défauts** | A : gratuit, B : 10 ans | A : 5 ans, B : 5 ans |
| Aperçu | Descriptif |
|---------|-------------|
| **Stratégie dominante** | Le défaut est dominant pour les deux joueurs |
| **Équilibre de Nash** | Les deux défauts (5 ans chacun) |
| **Pareto optimal** | Les deux coopèrent (1 an chacun) |
| **Leçon** | Des décisions individuelles rationnelles peuvent conduire à des résultats collectivement pires |
### Autres jeux classiques
| Jeu | Descriptif | Équilibre de Nash | Leçon |
|------|-------------|-------|--------|
| **Poulet (Faucon-Tourterelle)** | Deux conducteurs se dirigent l'un vers l'autre ; faire un écart ou aller tout droit | On fait un écart, on va tout droit | Maîtrise de la corde raide ; crédibilité de l'engagement |
| **Chasse au cerf** | Chasser un cerf ensemble (gain élevé) ou chasser un lièvre seul (gain faible) | Les deux cerfs ou les deux lièvres | Coordination; confiance |
| **Bataille des sexes** | Deux joueurs préfèrent des résultats différents mais souhaitent se coordonner | Les deux vont au même événement | Équilibres multiples ; qui bouge en premier a l'avantage |
| **Jeu de l'ultimatum** | Le proposant divise l'argent ; le répondeur accepte ou rejette (les deux n'obtiennent rien) | Le proposant offre un minimum ; le répondeur accepte | Les gens rejettent les offres injustes (irrationnelles mais courantes) |
| **Jeu de biens publics** | Contribuer à une cagnotte partagée ou free-ride | Tout le monde fait des free-rides | Tragédie des biens communs ; besoin d'application |
---

## Types de jeux
### Par timing
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Simultané** | Les joueurs bougent en même temps (ou sans connaître les mouvements des autres) | Pierre-papier-ciseaux ; enchères sous pli cacheté |
| **Séquentiel** | Les joueurs se déplacent les uns après les autres ; les joueurs ultérieurs observent les mouvements antérieurs | Échecs; décisions d'entrée sur le marché |
| **Répété** | Même jeu joué plusieurs fois | Le dilemme répété du prisonnier ; concurrence commerciale en cours |
### Par informations
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Informations parfaites** | Tous les joueurs connaissent tous les mouvements précédents | Échecs; dames |
| **Informations imparfaites** | Certains mouvements sont masqués | Poker; concurrence commerciale |
| **Informations complètes** | Tous les joueurs connaissent tous les gains et stratégies | La plupart des jeux manuels |
| **Informations incomplètes** | Certains gains ou types sont inconnus | Ventes aux enchères ; négociations |
---

## Concepts de solutions
### Équilibre de Nash
| Aspects | Descriptif |
|--------|-------------|
| **Définition** | Aucun joueur ne peut améliorer ses gains en changeant seul sa stratégie |
| **Comment trouver** | Pour chaque joueur, trouver la meilleure réponse aux stratégies des autres ; où ils se croisent tous est l'équilibre de Nash |
| **Existence** | Tout jeu fini a au moins un équilibre de Nash (éventuellement dans des stratégies mixtes) |
| **Unicité** | Les jeux peuvent avoir plusieurs équilibres de Nash ; des problèmes de coordination surviennent |
| **Limitation** | L'équilibre de Nash ne vous indique pas quel équilibre sera sélectionné ; ne tient pas compte de l'équité |
### Équilibre stratégique dominant
| Étape | Descriptif |
|------|-------------|
| **1. Identifier les stratégies** | Liste toutes les stratégies disponibles pour chaque joueur |
| **2. Trouver des stratégies dominantes** | Une stratégie qui est la meilleure indépendamment de ce que font les autres |
| **3. Si tous les joueurs en ont un** | La combinaison est l'équilibre de stratégie dominante |
| **4. Sinon** | Utiliser l'élimination itérative des stratégies dominées ou l'équilibre de Nash |
### Induction vers l'arrière (jeux séquentiels)
| Étape | Descriptif |
|------|-------------|
| **1. Dessinez l'arbre du jeu** | Nœuds = points de décision ; branches = actions |
| **2. Commencez par la fin** | Identifier le choix optimal du dernier joueur à chaque nœud terminal |
| **3. Travailler à rebours** | À chaque nœud précédent, choisissez l'action qui mène au meilleur résultat |
| **4. Résultat** | Équilibre parfait du sous-jeu — stratégie optimale à chaque point de décision |
---

## Concepts avancés
### Stratégies mixtes
| Concepts | Descriptif | Exemple |
|---------|-------------|---------|
| **Stratégie mixte** | Randomiser les actions selon les probabilités | Pierre-papier-ciseaux : jouez chacun avec 1/3 de probabilité |
| **Pourquoi randomiser ?** | Empêche les adversaires de prédire votre mouvement | Les tirs au but dans le football ; contrôles fiscaux |
| **Équilibre de Nash à stratégie mixte** | Chaque joueur est indifférent entre ses stratégies pures | Aucun joueur ne peut exploiter l'autre |
### Jeux répétés et théorème populaire
| Concepts | Descriptif |
|---------|-------------|
| **Infiniment répété** | L’induction à rebours défait la coopération ; identique au jeu one-shot | La défection du dernier tour se propage à rebours |
| **Infiniment répété** | La coopération peut être soutenue par des menaces de sanctions futures | Du tac au tac ; stratégies de déclenchement sinistres |
| **Théorème populaire** | Tout gain individuellement rationnel peut être un équilibre de Nash dans un jeu répété à l'infini | La coopération est possible si l'avenir compte suffisamment |
| **Facteur de remise** | Dans quelle mesure les joueurs apprécient les gains futurs ; plus élevé = plus de coopération | Les joueurs patients coopèrent davantage |
### Conception de mécanismes (théorie des jeux inversés)
| Concepts | Descriptif |
|---------|-------------|
| **Objectif** | Concevoir les règles d'un jeu pour atteindre le résultat souhaité |
| **Demandes** | Ventes aux enchères ; systèmes de vote; conception de contrats ; conception du marché |
| **Principe de révélation** | Tout résultat réalisable par n'importe quel mécanisme peut être obtenu par un mécanisme direct véridique |
| **Exemple** | Enchères Vickrey (offre scellée au deuxième prix) — enchérir sur votre vraie valeur est une stratégie dominante |
---

## Candidatures
### Entreprise
| Demande | Concept de théorie des jeux | Aperçu |
|-------------|---------|---------|
| **Concurrence sur les prix** | Le dilemme du prisonnier | Les guerres des prix nuisent aux deux entreprises ; collusion tacite dans des jeux répétés |
| **Entrée sur le marché** | Jeu séquentiel ; engagement | La menace des opérateurs historiques de lutter contre l'entrée n'est crédible que s'ils ont investi dans leurs capacités |
| **Enchères** | Conception de mécanismes | Les enchères au deuxième prix révèlent de vraies valeurs ; les enchères du spectre rapportent des milliards |
| **Négociation** | Jeu de négociation ; Équilibre de Nash | Divisez le surplus ; avantage du premier arrivé dans les jeux d'ultimatum |
| **Signalisation** | Le modèle éducatif de Spence | Les signaux coûteux sont crédibles parce que les types de mauvaise qualité ne peuvent pas se les permettre |
### Relations internationales
| Demande | Concept de théorie des jeux | Aperçu |
|-------------|---------|---------|
| **Courses aux armements** | Le dilemme du prisonnier | Les deux camps feraient mieux de désarmer mais ne peuvent pas se faire confiance |
| **Guerres commerciales** | Jeu répété | Du tac au tac : coopérer jusqu'à ce que les autres défauts soient détectés, puis riposter |
| **Accords climatiques** | Jeu de biens publics | Le free-riding est rationnel ; mécanismes d'application nécessaires |
| **Dissuasion** | Poulet; engagement crédible | La destruction mutuelle assurée est un équilibre de Nash |
---

## Résumé
La théorie des jeux étudie les interactions stratégiques où votre résultat dépend des actions des autres. L’équilibre de Nash – dans lequel aucun acteur ne bénéficie du seul changement de stratégie – est le concept central de la solution. Des jeux classiques comme le dilemme du prisonnier montrent que des décisions individuelles rationnelles peuvent produire de mauvais résultats collectivement. Les jeux séquentiels sont résolus par induction rétrospective. Les jeux répétés peuvent soutenir la coopération malgré la menace de sanctions futures. Les stratégies mixtes impliquent la randomisation pour rester imprévisible. La conception des mécanismes inverse la question : au lieu de prédire les résultats, elle conçoit des règles pour atteindre les résultats souhaités (comme dans les enchères). Les applications couvrent les affaires (tarification, entrée, enchères), la politique (vote, traités), la biologie (stratégies évolutives stables) et la vie quotidienne. La leçon fondamentale est que la stratégie ne se limite pas à ce que vous faites : il s'agit également d'anticiper ce que feront les autres, en sachant qu'ils font de même.