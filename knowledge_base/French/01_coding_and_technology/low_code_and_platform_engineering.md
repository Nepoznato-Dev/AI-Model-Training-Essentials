<!--
---
# Metadata
title: "Low-Code and Platform Engineering"
description: "Low-code platforms, internal developer platforms, golden paths"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [low, code, platform, engineering, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Ingénierie Low-Code et Plateforme
Les plates-formes low-code permettent aux utilisateurs de créer des applications avec un minimum de code écrit à la main, généralement via des interfaces glisser-déposer, des flux de travail visuels et des connecteurs prédéfinis. L'ingénierie de plate-forme est la discipline consistant à créer des plates-formes de développement internes (IDP) qui permettent aux équipes produit de mettre facilement en place une infrastructure, un CI/CD et des outils opérationnels en libre-service. Les deux tendances sont des réponses au même problème : l’écart entre la demande de logiciels et l’offre de développeurs capables de les créer.
---

## Plateformes Low-Code
### Ce que signifie réellement le Low-Code
| Aspects | Descriptif |
|--------|-------------|
| **Développement visuel** | Générateurs d'interface utilisateur par glisser-déposer ; éditeurs de flux de travail visuels ; concepteurs de formulaires |
| **Composants pré-construits** | Widgets, connecteurs, modèles et intégrations prêts à l'emploi |
| **Logique déclarative** | Configurer le comportement via des règles et des conditions plutôt que d'écrire du code |
| **Extensibilité** | Possibilité d'ajouter du code personnalisé lorsque les capacités intégrées de la plateforme ne suffisent pas |
| **Infrastructure gérée** | La plate-forme gère l'hébergement, la mise à l'échelle et les correctifs de sécurité |
### Plateformes Low-Code populaires
| Plateforme | Force | Cas d'utilisation typique |
|----------|----------|------------------|
| **Plateforme Microsoft Power** | Intégration approfondie de Microsoft 365/Azure ; Power Apps, Power Automate, Power BI | Flux de travail d'entreprise ; outils internes |
| **Plateforme Salesforce** | CRM natif ; Apex pour les extensions ; Générateur de flux | Applications destinées aux clients ; flux de travail de vente |
| **ServiceMaintenant** | Gestion des services informatiques ; automatisation du flux de travail | Opérations informatiques ; HEURE; installations |
| **Appien** | Extraction de processus ; gestion de cas | Processus commerciaux complexes ; conformité |
| **OutSystems** | Web et mobile complets ; de niveau entreprise | Portails clients ; applications mobiles |
| **Réoutiller** | Constructeur d'outils internes ; se connecte aux bases de données et aux API | Panneaux d'administration ; tableaux de bord ; outils opérationnels |
| **Airtable** | Hybride tableur-base de données ; automatisations | Suivi de projet ; CRM léger |
### Quand le Low-Code fonctionne bien
| Scénario | Pourquoi le Low-Code s'adapte |
|----------|---------|
| **Outils internes** | Rapide à construire ; les utilisateurs sont internes, donc la flexibilité de l'interface utilisateur compte moins |
| **Formulaires et approbations** | Les créateurs de flux de travail visuels excellent dans ce domaine |
| **Applications CRUD** | La plupart des plates-formes low-code sont optimisées pour les modèles de création-lecture-mise à jour-suppression |
| **Prototypage** | Validez une idée en heures au lieu de semaines |
| **Développement citoyen** | Les analystes métier peuvent créer leurs propres solutions grâce à la gouvernance informatique |
### Quand le Low-Code échoue
| Limitation | Impact |
|------------|--------|
| **Verrouillage du fournisseur** | Les applications ne peuvent pas être facilement migrées hors de la plateforme |
| **Plafonds de performance** | Ne convient pas aux applications à haut débit ou sensibles à la latence |
| **Contraintes de l'interface utilisateur** | Les conceptions personnalisées sont difficiles ; vous êtes limité à ce que la plateforme prend en charge |
| **Complexité d'intégration** | La connexion à des API inhabituelles ou à des systèmes existants peut de toute façon nécessiter un code personnalisé |
| **Coût à grande échelle** | La tarification par utilisateur ou par application peut devenir coûteuse à mesure que l'utilisation augmente |
| **Difficulté de débogage** | Les abstractions visuelles rendent difficile le diagnostic de problèmes complexes |
---

## Ingénierie de plateforme
### Le problème que l'ingénierie de plate-forme résout
| Sans ingénierie de plateforme | Avec l'ingénierie de plate-forme |
|------------------------------|--------------------------------|
| Chaque équipe gère sa propre infrastructure | Infrastructure de résumés de plateforme libre-service |
| Outils incohérents entre les équipes | Chaîne d'outils standardisée ; chemins d'or |
| Les développeurs attendent que les opérations provisionnent les ressources | Les développeurs mettent à disposition des ressources à la demande |
| Silos de connaissances ; connaissances tribales | Documenté; automatisé; découvrable |
| Intégration lente des nouveaux ingénieurs | Les nouveaux ingénieurs peuvent être déployés dès le premier jour |
### Composants de base d'une plate-forme de développement interne
| Composant | Objectif | Exemples d'outils |
|-----------|---------|---------------|
| **Catalogue de services** | Registre central de tous les services et de leurs propriétaires | Dans les coulisses ; Port; Cortex |
| **Échafaudage modèle** | Générer de nouveaux services à partir de modèles approuvés | Modèles de logiciels en coulisses ; Emporte-pièce |
| **Infrastructure libre-service** | Les développeurs mettent à disposition des ressources cloud sans déposer de tickets | Modules Terraform ; Pulumi ; Plan croisé |
| **Pipelines CI/CD** | Construction, test et déploiement de pipelines standardisés | Actions GitHub ; GitLabCI ; CD Argo |
| **Gestion de l'environnement** | Environnements de développement/staging éphémères à la demande | Vcluster ; Espace de noms ; Gitpod |
| **Observabilité** | Journalisation, métriques et traçage intégrés à chaque service | Prométhée; Grafana; OpenTélémétrie ; Chien de données |
| **Gestion secrète** | Stockage sécurisé et rotation des informations d'identification | Sauter; Gestionnaire de secrets AWS ; POS |
| **Identité et accès** | authentification unique ; accès basé sur les rôles ; authentification de service à service | Okta; Porte-clés ; SPIFFE |
### Chemins d'or
Une voie dorée est une manière soutenue et opiniâtre de faire quelque chose. C'est la voie de moindre résistance : si vous la suivez, tout fonctionne. Vous pouvez sortir du chemin, mais vous êtes seul.
| Chemin d'Or | Ce qu'il fournit |
|-------------|-----------------|
| **Nouveau service** | Dépôt de modèles ; CI/CD ; surveillance; enregistrement; configuration de déploiement |
| **Nouvelle base de données** | Instance provisionnée ; chaînes de connexion dans les secrets ; sauvegarde configurée |
| **Nouvelle interface** | Construire un pipeline ; RDC ; environnements de prévisualisation ; contrôles de phare |
| **Pipeline de données** | Orchestration; validation du schéma ; surveillance; alerte |
### Décisions de construction ou d'achat
| Facteur | Construire sur mesure | Utiliser l'outil existant |
|--------|-------------|---------|
| **Compétence de base** | Unique à votre entreprise ; avantage concurrentiel | Marchandise; chaque entreprise en a besoin |
| **Fardeau d'entretien** | Vous avez la capacité de le maintenir | L'outil est bien entretenu par le fournisseur/la communauté |
| **Besoins d'intégration** | Intégration approfondie avec les systèmes internes requise | Les API et connecteurs standards suffisent |
| **Coût** | Moins cher à construire qu'une licence | Moins cher à obtenir une licence qu'à construire |
---

## La relation entre le Low-Code et l'ingénierie de plateforme
| Dimensions | Low-Code | Ingénierie de plateforme |
|-----------|----------|---------------|
| **Utilisateur cible** | Utilisateurs professionnels ; développeurs citoyens | Ingénieurs logiciels professionnels |
| **Objectif** | Réduire le code ; augmenter la vitesse | Réduire la charge cognitive ; augmenter l'autonomie |
| **Niveau d'abstraction** | Très élevé ; visuel | Moyen; basé sur du code mais simplifié |
| **Flexibilité** | Limité par les capacités de la plateforme | Flexibilité totale ; vous pouvez écrire n'importe quel code |
| **Gouvernance** | La plateforme applique les règles | Plateforme offre des chemins dorés |
Ils sont complémentaires : l'ingénierie de plate-forme rend les développeurs professionnels plus rapides, tandis que le low-code permet aux non-développeurs de créer des applications simples. Ensemble, ils comblent les lacunes en matière de fourniture de logiciels sous différents angles.
---

## Résumé
Les plateformes low-code et les plateformes de développeurs internes visent toutes deux à augmenter le nombre de personnes capables de fournir des logiciels. Pour ce faire, le low-code élimine entièrement le code : constructeurs visuels, connecteurs prédéfinis, logique déclarative. L'ingénierie de plate-forme fait cela pour les développeurs professionnels en fournissant une infrastructure en libre-service, des chemins d'accès privilégiés et des outils standardisés afin qu'ils passent moins de temps sur le travail opérationnel et plus de temps sur les fonctionnalités du produit. Ce n’est pas non plus une solution miracle : le low-code présente des contraintes de dépendance envers un fournisseur et des limites de performances, et l’ingénierie de la plate-forme nécessite un investissement continu pour sa maintenance. Mais lorsqu'ils sont appliqués aux bons problèmes (outils internes, applications CRUD, prestation de services standardisés), les deux peuvent réduire considérablement le délai entre l'idée et la production.