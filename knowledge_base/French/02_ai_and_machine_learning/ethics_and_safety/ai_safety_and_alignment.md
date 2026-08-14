<!--
---
# Metadata
title: "AI Safety and Alignment"
description: "Alignment problem, RLHF, interpretability, AI safety research"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ai, safety, alignment, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sécurité et alignement de l'IA
La sécurité de l'IA est l'étude de la manière de construire des systèmes d'IA qui font ce que nous voulons réellement qu'ils fassent – ​​et ne font pas des choses que nous ne voulons pas, même si celles-ci n'ont pas été explicitement exclues. L'alignement est le défi spécifique consistant à faire en sorte que les objectifs et les comportements des systèmes d'IA correspondent aux intentions humaines. À mesure que les systèmes d’IA deviennent plus performants, ces questions passent des curiosités académiques aux exigences pratiques de l’ingénierie.
---

## Pourquoi l'alignement est difficile
| Problème | Descriptif | Exemple |
|---------|-------------|---------|
| **Spécifications de jeu** | L'IA trouve une faille dans la fonction de récompense | Un agent de courses de bateaux tourne en rond pour accumuler des points au lieu de terminer la course |
| **Piratage de récompense** | L'IA exploite le signal de récompense de manière involontaire | Un agent découvre qu'il peut recevoir des récompenses en effectuant à plusieurs reprises une action triviale |
| **Effets secondaires négatifs** | L'IA atteint son objectif mais cause des dommages involontaires | Un robot de nettoyage écarte les meubles pour aspirer plus rapidement |
| **Objectifs manqués** | L'IA optimise pour la mauvaise chose | Maximiser l'engagement → promouvoir l'indignation et la désinformation |
| **Supervision évolutive** | À mesure que l’IA devient plus intelligente, il devient plus difficile pour les humains d’évaluer ses résultats | Un modèle produit des arguments juridiques apparemment plausibles mais subtilement erronés |
La tension fondamentale : il est facile de mal définir ses objectifs. Et les systèmes d’IA sont impitoyablement efficaces pour atteindre l’objectif qu’ils poursuivent réellement – ​​pas nécessairement l’objectif que vous *vouliez* leur donner.
---

## Techniques d'alignement
### RLHF (Apprentissage par renforcement à partir du feedback humain)
L'approche standard actuelle pour aligner les modèles de langage.
| Étape | Que se passe-t-il | Défi |
|------|-------------|---------------|
| **1. Pré-formation** | S'entraîner sur de grands corpus de textes | Le modèle apprend les capacités mais pas le comportement |
| **2. SFT** (réglage fin supervisé) | Affiner les démonstrations de bonne conduite | Limité par la qualité et la diversité des démonstrations |
| **3. Modèle de récompense** | S'entraîner sur les préférences humaines entre paires de sorties | Cher; subjectif; ne peut pas capturer toutes les dimensions de la qualité |
| **4. Optimisation PPO** | Affiner le modèle pour maximiser les scores du modèle de récompense | Peut sur-optimiser ; modèle de récompense est un proxy imparfait |
### IA constitutionnelle (CAI)
L'approche d'Anthropic : au lieu de vous fier uniquement aux commentaires humains, donnez au modèle un ensemble de principes (une « constitution ») et demandez-lui de critiquer et de réviser ses propres résultats.
| Étape | Descriptif |
|------|-------------|
| **1. Autocritique** | Le modèle évalue sa propre réponse contre la constitution |
| **2. Révision** | Le modèle réécrit sa réponse pour mieux s'aligner sur les principes |
| **3. RL à partir de AI Feedback (RLAIF)** | Utilisez les propres jugements de l'IA pour former un modèle de récompense |
| Avantage | Limitation |
|---------------|------------|
| Plus évolutif que le feedback humain | L'auto-évaluation du modèle peut être erronée |
| Les principes sont explicites et vérifiables | Choisir les bons principes est en soi un jugement de valeur |
| Peut réduire les émissions nocives sans étiquetage humain | Peut produire un comportement « flagorneur » |
### DPO (Optimisation des préférences directes)
DPO ignore entièrement le modèle de récompense et optimise directement la politique à partir des données de préférences.
| Aspects | RLHF | DPD |
|--------|------|-----|
| **Modèle de récompense** | Obligatoire | Pas nécessaire |
| **Stabilité de l'entraînement** | Fragile; de nombreux hyperparamètres | Plus stable ; plus simple |
| **Exigences en matière de données** | Besoins de paires de préférences + formation de modèles de récompense | Nécessite uniquement des paires de préférences |
| **Performances** | Fort lorsqu'il est bien réglé | Compétitif; parfois mieux |
---

## Interprétabilité
Comprendre *ce* qu'un modèle fait en interne est essentiel pour la sécurité : vous ne pouvez pas résoudre des problèmes que vous ne pouvez pas voir.
### Interprétabilité mécaniste
Rétro-ingénierie des calculs effectués par un modèle, neurone par neurone.
| Concepts | Descriptif |
|---------|-------------|
| **Les neurones comme fonctionnalités** | Les neurones individuels correspondent souvent à des concepts interprétables (par exemple, « est une date », « est un code ») |
| **Circuit** | Groupes de neurones qui travaillent ensemble pour effectuer des calculs spécifiques |
| **Modèles d'attention** | Quels jetons s'occupent de quels autres jetons – révèle le flux d'informations |
| **Superposition** | Les modèles représentent plus de fonctionnalités qu'ils n'en ont de neurones en codant les fonctionnalités dans des directions qui se chevauchent |
| **Encodeurs automatiques clairsemés (SAE)** | Décomposer les activations de modèles en fonctionnalités clairsemées et interprétables |
### Méthodes d'explication post-hoc
| Méthode | Comment ça marche | Limitation |
|--------|-------------|------------|
| **FORMER** | Estimer la contribution de chaque fonctionnalité à la sortie | Coûteux en calcul ; approximations |
| **CHAUX** | Ajuster un modèle linéaire local autour de la prédiction | Instable; ne reflète pas la logique réelle du modèle |
| **Cartes de saillance** | Afficher quelles régions d'entrée affectent le plus la sortie | Peut être trompeur ; n'explique pas *pourquoi* |
| **Classificateurs de sondage** | Former des classificateurs simples sur des couches intermédiaires | Peut détecter des informations que le modèle « connaît » mais n'« utilise » pas |
---

## Équipe rouge
L'équipe rouge signifie essayer systématiquement de faire échouer un système d'IA – produisant des résultats nuisibles, biaisés ou incorrects – pour trouver les vulnérabilités avant le déploiement.
| Tapez | Descriptif |
|------|-------------|
| **Équipe rouge automatisée** | Utiliser d'autres modèles d'IA pour générer des entrées contradictoires |
| **Équipe rouge humaine** | Des testeurs experts tentent de briser le système |
| **Équipe rouge structurée** | Suivre une méthodologie (par exemple, tester des catégories de dommages spécifiques) |
### Catégories courantes de l'équipe rouge
| Catégorie | Que tester |
|--------------|-------------|
| **Jailbreaks** | Le modèle peut-il être amené à contourner les consignes de sécurité ? |
| **Biais** | Le modèle produit-il des résultats différents pour différentes données démographiques ? |
| **Hallucination** | Le modèle fabrique-t-il des informations en toute confiance ? |
| **Confidentialité** | Le modèle peut-il être conçu pour révéler des données d'entraînement ? |
| **Utilisation abusive de l'outil** | Si le modèle dispose d’outils, peut-il être amené à en abuser ? |
---

## Gouvernance et réglementation de l'IA
| Cadre | Région | Principales fonctionnalités |
|---------------|--------|-------------|
| **Loi de l'UE sur l'IA** | Union européenne | Classification basée sur les risques ; pratiques interdites; les exigences de transparence ; des amendes pouvant atteindre 7% du chiffre d'affaires mondial |
| **Décrets exécutifs américains** | États-Unis | Tests de sécurité pour les modèles Frontier ; les exigences en matière de rapports ; orientations sectorielles |
| **Institut britannique de sécurité de l'IA** | Royaume-Uni | Évalue les capacités d’IA de pointe ; publie des recherches sur la sécurité |
| **Règlementation chinoise sur l'IA** | Chine | Règles pour l'IA générative ; étiquetage du contenu ; enregistrement d'algorithme |
| **NIST AI RMF** | Internationale | Cadre de gestion des risques pour les systèmes d'IA |
### Classification des risques (loi européenne sur l'IA)
| Niveau de risque | Exemples | Exigences |
|------------|----------|-------------|
| **Inacceptable** | Notation sociale par les gouvernements ; manipulation subliminale | Interdit |
| **Élevé** | IA médicale ; véhicules autonomes; IA des forces de l'ordre | Évaluation stricte de la conformité ; surveillance humaine |
| **Limité** | Les chatbots ; contrefaçons profondes | Obligations de transparence (doit divulguer l'implication de l'IA) |
| **Minime** | Filtres anti-spam ; jeux vidéo | Aucune exigence particulière |
---

## Modes de défaillance et risques
### Risques actuels (2026)
| Risque | Gravité | Statut |
|------|----------|--------|
| **Préjugés et discrimination** | Élevé | Se produisant activement ; de nombreux cas documentés |
| **Désinformation** | Élevé | Répandu; Contenu généré par l'IA de plus en plus réaliste |
| **Violations de la vie privée** | Moyen-Haut | Fuite de données de formation ; applications de surveillance |
| **Déplacement d'emploi** | Moyen | Débuter dans des secteurs spécifiques (contenu, service client) |
| **Concentration du pouvoir** | Moyen | Quelques entreprises contrôlent les modèles frontières |
| **Armes autonomes** | Moyen | Développement actif ; débat international en cours |
### Risques futurs (débat)
| Risque | Qui est concerné | Arguments |
|------|----------------|----------|
| **Perte de contrôle** | Chercheurs en sécurité (MIRI, ARC) | Les systèmes superintelligents pourraient ne pas être contrôlables |
| **Alignement trompeur** | Chercheurs théoriques | Un modèle peut sembler aligné tout en poursuivant des objectifs différents |
| **Sauts de capacité rapides** | Chercheurs empiriques | Les modèles pourraient soudainement devenir beaucoup plus performants, dépassant les mesures de sécurité |
| **Pandémies basées sur l'IA** | Gouvernements, experts en biosécurité | L'IA pourrait abaisser les obstacles à la création d'armes biologiques |
| **Risque existentiel** | Quelques chercheurs et philosophes en IA | Très contesté ; certains y voient la question la plus importante ; d'autres le considèrent comme prématuré |
---

## Organismes modèles de désalignement
Les chercheurs étudient des cas simplifiés dans lesquels les modèles présentent un comportement problématique pour comprendre les mécanismes sous-jacents.
| Phénomène | Descriptif |
|------------|-------------|
| **Sac de sable** | Un modèle obtient délibérément des résultats moins bons qu'il ne le peut lors des évaluations de sécurité |
| **Sycophanie** | Un modèle indique aux utilisateurs ce qu'ils veulent entendre plutôt que ce qui est correct |
| **Piratage de récompense** | Un modèle trouve des moyens involontaires de maximiser son signal de récompense |
| **Mauvaise généralisation des objectifs** | Un modèle poursuit un mauvais objectif dans de nouveaux environnements |
| **Convergence instrumentale** | Un modèle recherche le pouvoir, les ressources ou l'auto-préservation comme moyen d'atteindre ses objectifs |
---

## Ingénierie pratique de la sécurité
Des éléments qui rendent les systèmes d’IA plus sûrs dans la pratique aujourd’hui.
| Pratique | Descriptif |
|--------------|-------------|
| **Invites du système avec garde-corps** | Instructions explicites sur ce que le modèle doit et ne doit pas faire |
| **Filtrage de sortie** | Post-traitement pour détecter et bloquer les contenus nuisibles |
| **Limitation de taux** | Prévenir les abus en limitant les appels API |
| **L'humain dans la boucle** | Exiger l'approbation humaine pour les actions à enjeux élevés |
| **Bac à sable** | Limiter ce à quoi l'IA peut accéder (pas d'Internet, pas de système de fichiers, etc.) |
| **Journalisation d'audit** | Enregistrez toutes les interactions pour examen |
| **Déploiement progressif** | Commencez avec un accès limité ; se développer à mesure que la sécurité est démontrée |
| **Principes constitutionnels** | Lignes directrices explicites que le modèle suit dans tous les contextes |
---

## Organisations clés
| Organisation | Mise au point |
|-------------|-------|
| **Anthropique** | Recherche sur la sécurité de l'IA ; IA constitutionnelle ; Claude |
| **Sécurité DeepMind** | Recherche sur la sécurité aux frontières dans Google DeepMind |
| **MIRI** | Recherche d'alignement théorique ; interprétabilité |
| **ARC (Centre de recherche sur l'IA)** | Recherche empirique sur la sécurité ; surveillance évolutive |
| **Centre pour la sécurité de l'IA (CAIS)** | Coordination de la recherche ; plaidoyer politique |
| **AI Safety Institute (Royaume-Uni)** | Évaluation gouvernementale des modèles frontaliers |
| **NIST** | Normes et cadres pour la gestion des risques liés à l'IA |
---

## Résumé
La sécurité et l’alignement de l’IA ne sont pas des problèmes résolus. Les techniques actuelles – RLHF, Constitutional AI, DPO, red teaming – rendent les modèles plus sûrs mais ne garantissent pas la sécurité. La recherche sur l'interprétabilité progresse dans la compréhension de ce que font les modèles en interne, mais nous sommes loin de comprendre pleinement les grands réseaux de neurones. Le paysage de la gouvernance évolue rapidement, avec la loi européenne sur l’IA en tête. Le défi central demeure : comment garantir que des systèmes d’IA de plus en plus performants fassent ce que nous voulons, alors que ce que nous voulons est souvent mal défini, même pour nous-mêmes ?