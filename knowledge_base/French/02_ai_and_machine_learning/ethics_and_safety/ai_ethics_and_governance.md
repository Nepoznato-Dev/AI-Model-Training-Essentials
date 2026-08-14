<!--
---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
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
tags: [ai, ethics, governance, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Éthique et gouvernance de l'IA
Les systèmes d’IA ne sont pas neutres. Ils reflètent les données sur lesquelles ils ont été formés, les valeurs de leurs créateurs et les incitations des organisations qui les déploient. L’éthique ne consiste pas seulement à se demander « pouvons-nous construire cela ? » mais "devrions-nous?" La gouvernance consiste à créer des structures – lois, normes, organismes de surveillance – qui garantissent que l’IA soit développée et utilisée de manière responsable. Ce dossier couvre les principales dimensions éthiques de l’IA et les cadres de gouvernance émergents pour y répondre.
---

## Principes éthiques fondamentaux pour l'IA
La plupart des cadres éthiques de l’IA convergent vers un ensemble de principes partagés.
| Principe | Ce que cela signifie | Défi |
|-----------|--------------|---------------|
| **Équité** | L'IA ne devrait pas discriminer les groupes protégés | Définir mathématiquement l’équité est difficile ; différentes définitions de l'équité peuvent entrer en conflit |
| **Transparence** | Les utilisateurs doivent savoir quand ils interagissent avec l'IA et comment elle fonctionne | Une transparence totale peut permettre le jeu ; les systèmes propriétaires résistent à la divulgation |
| **Responsabilité** | Quelqu’un doit être responsable lorsque l’IA cause du tort | Responsabilité diffuse entre les développeurs, les déployeurs et les utilisateurs |
| **Confidentialité** | L'IA doit respecter les données personnelles et l'autonomie | Les données de formation incluent souvent des informations personnelles ; Conflit entre confidentialité et utilité |
| **Sécurité** | L'IA ne devrait pas causer de dommages physiques ou psychologiques | La définition du préjudice dépend du contexte ; les cas extrêmes sont imprévisibles |
| **Contrôle humain** | Les humains devraient conserver un contrôle significatif | Le biais d’automatisation signifie que les humains s’en remettent à l’IA ; la surveillance devient une approbation automatique |
---

## Biais dans les systèmes d'IA
### D'où vient le biais
| Source | Descriptif | Exemple |
|--------|-------------|---------|
| **Données de formation** | Biais historiques codés dans les données | Les données d'embauche reflètent la discrimination passée → le modèle discrimine |
| **Biais d'étiquette** | Les annotateurs humains imposent leurs préjugés | CV avec des noms « féminins » moins bien notés par les annotateurs |
| **Biais de sélection** | Les données ne représentent pas la population cible | La reconnaissance faciale s'entraîne principalement sur les visages à la peau claire |
| **Biais de mesure** | Fonctionnalités proxy pour les attributs protégés | Le code postal est en corrélation avec la race |
| **Biais algorithmique** | L'optimisation amplifie les petits biais | Un petit écart dans les données d'entraînement devient un grand écart dans les prédictions |
### Mesures d'équité
| Métrique | Définition | Quand utiliser |
|--------|-----------|-------------|
| **Parité démographique** | Le taux de positivité est égal dans tous les groupes | Quand vous voulez des résultats égaux |
| **Cotes égalisées** | Le taux de vrais positifs et le taux de faux positifs sont égaux dans tous les groupes | Quand vous voulez des taux d'erreur égaux |
| **Parité prédictive** | La précision est égale dans tous les groupes | Quand vous voulez que les prédictions signifient la même chose pour tous les groupes |
| **Équité individuelle** | Des individus similaires sont traités de la même manière | Quand vous voulez de la cohérence |
**Théorème d'impossibilité** : vous ne pouvez généralement pas satisfaire simultanément plusieurs définitions d'équité. Choisir quelle mesure d’équité utiliser est en soi un jugement de valeur.
### Atténuation des biais
| Scène | Techniques |
|-------|---------------|
| **Prétraitement** | Rééquilibrer les données d'entraînement ; supprimer les fonctionnalités biaisées ; suréchantillonnage synthétique |
| **En cours de traitement** | Ajouter des contraintes d'équité à la fonction de perte ; débiaisation contradictoire |
| **Post-traitement** | Ajuster les seuils par groupe ; calibrer les prédictions |
| **Évaluation** | Audits d'équité réguliers ; mesures de performance désagrégées |
---

## Explicabilité
### Pourquoi l'explicabilité est importante
| Raison | Descriptif |
|--------|-------------|
| **Confiance** | Les utilisateurs doivent comprendre pourquoi une décision a été prise |
| **Débogage** | Les développeurs doivent rechercher et corriger les erreurs de modèle |
| **Règlement** | le « droit à l’explication » du RGPD ; Exigences de la loi européenne sur l’IA |
| **Équité** | Vous ne pouvez pas détecter les biais sans comprendre le comportement du modèle |
| **Responsabilité** | Les organisations doivent justifier les décisions automatisées |
### Méthodes d'explication
| Méthode | Tapez | Comment ça marche | Limitation |
|--------|------|-------------|------------|
| **FORMER** | Importance des fonctionnalités | Estimation de la contribution de chaque fonctionnalité à l'aide de la théorie des jeux | Coûteux en calcul ; approximations |
| **CHAUX** | Substitut local | Ajuste un modèle simple autour de la prédiction | Instable; ne reflète pas la logique réelle du modèle |
| **Visualisation de l'attention** | Mécanisme interne | Montrer à quelles entrées le modèle s'occupe | Attention ≠ importance ; peut être trompeur |
| **Contrefactuels** | Analyse de simulation | « Si cette fonctionnalité était différente, la prédiction changerait-elle ? » | Dépend de scénarios contrefactuels réalistes |
| **Attribution des fonctionnalités** | Scores d'importance | Cartes de saillance, dégradés intégrés | N'explique pas *pourquoi* ; juste *où* |
---

## Réglementation IA
### Loi européenne sur l'IA (2026)
La première loi globale sur l'IA au monde.
| Niveau de risque | Exemples | Exigences |
|------------|----------|-------------|
| **Risque inacceptable** | Notation sociale ; manipulation subliminale ; surveillance biométrique en temps réel (sauf exceptions) | Interdit |
| **Risque élevé** | IA médicale ; véhicules autonomes; application de la loi; infrastructures critiques | Évaluation de la conformité ; surveillance humaine; transparence |
| **Risque limité** | Les chatbots ; contrefaçons profondes ; systèmes de recommandation | Doit divulguer l’implication de l’IA |
| **Risque minimal** | Filtres anti-spam ; jeux vidéo; la plupart des applications d'IA | Aucune exigence particulière |
### Autres approches réglementaires
| Région | Approche | Statut |
|--------|----------|--------|
| **États-Unis** | Spécifique au secteur ; décrets; engagements volontaires | Fragmenté ; pas de loi fédérale globale |
| **Royaume-Uni** | Basé sur des principes ; régulateurs du secteur | Institut de sécurité de l'IA ; démarche pro-innovation |
| **Chine** | Réglementation spécifique à l'IA générative, deepfakes, recommandations | Application active ; exigences de contenu |
| **Canada** | AIDA (Loi sur l'intelligence artificielle et les données) | Proposé; similaire à l'approche de l'UE |
| **Brésil** | Cadre de réglementation de l'IA | En cours |
---

## Impact environnemental
La formation et l’exécution de modèles d’IA consomment de l’énergie et génèrent des émissions de carbone.
| Activité | Émissions estimées | Comparaison |
|--------------|---------|------------|
| **Formation GPT-4** | Estimation de plus de 50 tonnes de CO₂ | Equivalent aux émissions annuelles de plusieurs voitures |
| **Formation d'un grand transformateur** | 280-620 tonnes de CO₂ | 5x les émissions d'une voiture pendant toute sa durée de vie |
| **Inférence quotidienne (1 million d'utilisateurs)** | En cours; dépend de la taille du modèle et du matériel | Peut dépasser les émissions de formation au fil du temps |
| **Peaufiner un modèle 7B** | 1 à 5 tonnes de CO₂ | Important mais bien moins que la pré-formation |
### Atténuation
| Stratégie | Impact |
|--------------|--------|
| **Matériel efficace** | Les nouveaux GPU sont plus économes en énergie par calcul |
| **Optimisation du modèle** | Des modèles plus petits et quantifiés consomment moins d'énergie |
| **Énergie verte** | Alimenter les centres de données avec des énergies renouvelables |
| **Architectures efficaces** | Mélange d'experts ; modèles clairsemés; distillation |
| **Planification respectueuse du carbone** | Exécutez l'entraînement lorsque la grille est la plus propre |
---

## Propriété intellectuelle et droit d'auteur
| Problème | Descriptif | Statut |
|-------|-------------|--------|
| **Formation sur les œuvres protégées** | Modèles formés sur des livres, articles, images sans autorisation | Poursuites actives ; débat sur l'utilisation équitable |
| **Sortie générée par l'IA** | À qui appartient le contenu généré par l’IA ? | Bureau américain du droit d'auteur : le contenu généré par l'IA n'est pas protégé par le droit d'auteur sans une paternité humaine suffisante |
| **Imitation de style** | L'IA peut imiter le style d'un artiste | Légalement gris ; préoccupations éthiques |
| **Mécanismes de désinscription** | Certains fournisseurs permettent aux créateurs de se désinscrire de la formation | robots.txt ; filtrage de contenu |
---

## Divulgation responsable
| Principe | Descriptif |
|---------------|-------------|
| **Tests préalables au déploiement** | Équipe rouge, audits de biais, évaluations de sécurité avant la publication |
| **Déploiement progressif** | Commencez avec un accès limité ; se développer à mesure que la sécurité est démontrée |
| **Rapport d'incident** | Documenter et partager des informations sur les échecs et les préjudices |
| **Contrats de bugs** | Récompenser les chercheurs externes qui ont découvert des vulnérabilités |
| **Cartes modèles** | Capacités, limites et utilisation prévue du modèle de document |
---

## Provenance des données
| Préoccupation | Descriptif |
|---------|-------------|
| **Transparence des données de formation** | La plupart des modèles frontières ne divulguent pas leurs données d'entraînement |
| **Consentement** | Les données des individus ont-elles été utilisées à leur connaissance et avec leur permission ? |
| **Empoisonnement des données** | Les attaquants peuvent-ils injecter des données malveillantes dans des ensembles de formation ? |
| **Cartes d'ensemble de données** | Documentation de la composition des ensembles de données, des méthodes de collecte et des limites |
| **Filigrane** | Intégrer des marqueurs invisibles dans le contenu généré par l'IA pour l'identifier |
---

## Cadres d'éthique pratiques
### Pour les développeurs d'IA
| Question | Pourquoi c'est important |
|--------------|--------------------|
| **Qui pourrait être lésé par ce système ?** | Identifie les parties prenantes concernées |
| **Que se passe-t-il si le modèle est erroné ?** | Évalue le coût des erreurs |
| **Les décisions du modèle peuvent-elles être expliquées ?** | Détermine les exigences d'explicabilité |
| **Les données d'entraînement sont-elles représentatives ?** | Vérifie les biais de sélection et de mesure |
| **Quels sont les modes de défaillance ?** | Anticipe les cas extrêmes et les abus |
| **Comment le système sera-t-il surveillé ?** | Plans de surveillance continue |
### Pour les organisations déployant l'IA
| Pratique | Descriptif |
|--------------|-------------|
| **Conseil de gouvernance de l'IA** | Équipe interfonctionnelle examinant les déploiements d'IA |
| **Analyses d'impact** | Évaluer les dommages potentiels avant le déploiement |
| **Processus de surveillance humaine** | Effacer les chemins d'escalade lorsque l'IA commet des erreurs |
| **Audits réguliers** | Vérifiez les biais, les dérives et les conséquences imprévues |
| **Canaux de commentaires des utilisateurs** | Autoriser les personnes concernées à signaler les problèmes |
| **Documentation** | Tenir des registres des décisions et des justifications du modèle |
---

## Résumé
L’éthique et la gouvernance de l’IA sont des exigences techniques. Les préjugés, l’opacité, le coût environnemental et les violations de la vie privée ne sont pas seulement des préoccupations éthiques ; ce sont des défauts qui causent un préjudice réel. Le paysage de la gouvernance évolue rapidement, la loi de l’UE sur l’IA établissant la norme mondiale. La réglementation à elle seule est insuffisante : l’équité, l’explicabilité et la responsabilité doivent être intégrées dans le travail quotidien de chaque développeur d’IA. La question centrale est de savoir comment construire des systèmes dignes de confiance.