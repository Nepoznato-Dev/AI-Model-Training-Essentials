---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
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

# Comparaison des services cloud
Une comparaison côte à côte des trois principaux fournisseurs de cloud (AWS, Azure et Google Cloud) en matière de calcul, de stockage, de bases de données, d'IA/ML, de mise en réseau, de surveillance et d'infrastructure en tant que code. Utile pour les architectes qui décident quelle plate-forme utiliser ou pour mapper les services d'un cloud à un autre.
---

## Présentation du fournisseur
| | AWS | Azur | Google Cloud (GCP) |
|---|-----|-------|-----------|
| **Part de marché** | ~31% (le plus grand) | ~25 % (seconde) | ~11 % (troisième, croissance la plus rapide) |
| **Forces** | Étendue des services ; maturité; écosystème | Intégration d'entreprise ; cloud hybride ; Pile Microsoft | Données/IA ; Kubernetes ; réseau mondial |
| **Idéal pour** | Des startups aux entreprises ; catalogue de services le plus large | Entreprises avec Microsoft/Active Directory ; hybride | Charges de travail gourmandes en données ; Natif de Kubernetes ; IA/ML |
| **Régions** | 33 régions, 105 AZ | 60+ régions | Plus de 40 régions, plus de 100 zones |
| **Niveau gratuit** | 12 mois de niveau gratuit + toujours gratuit | 12 mois gratuits + 200$ de crédit | Crédit de 300 $ pendant 90 jours + toujours gratuit |
---

## Calculer
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **Machines virtuelles** | EC2 (Elastic Compute Cloud) | Machines virtuelles | Moteur de calcul |
| **Mise à l'échelle automatique** | Groupes de mise à l'échelle automatique | Ensembles de machines virtuelles identiques | Groupes d'instances |
| **Fonctions sans serveur** | Lambda | Fonctions Azure | Fonctions cloud |
| **Registre de conteneurs** | ECR (Registre de conteneurs élastiques) | Registre de conteneurs Azure | Registre des artefacts |
| **Orchestration de conteneurs** | ECS/EKS | ACS/AKS | GKE/Cloud Run |
| **Conteneurs sans serveur** | Fargate | Applications de conteneur | Exécution en nuage |
| **Plateforme d'applications (PaaS)** | Elastic Beanstalk, App Runner | Service d'application | Moteur d'application |
| **Traitement par lots** | Lot AWS | Lot Azure | Lot de nuages ​​|
| **Calcul GPU/IA** | EC2 (instances P4d, P5) | Machines virtuelles série NC/ND | Machines virtuelles A2/A3 ; TPU |
### Modèles de tarification des VM
| Modèle | AWS | Azur | GCP |
|-------|-----|-------|-----|
| **À la demande** | Instances à la demande | Paiement à l'utilisation | À la demande |
| **Réservé / Engagé** | Instances réservées (1 à 3 ans) | VM réservées (1 à 3 ans) | Remises sur engagement d'utilisation (1 à 3 ans) |
| **Spot / Interruptible** | Instances ponctuelles | Spot VM | Machines virtuelles préemptives/Spot |
| **Plans d'épargne** | Plans d'épargne | Plans d'épargne | Remises sur engagement d'utilisation |
---

## Stockage
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **Stockage d'objets** | S3 | Stockage d’objets blob | Stockage en nuage |
| **Stockage en bloc** | EBS | Disques gérés | Disque persistant |
| **Stockage de fichiers** | EFS, FSx | Fichiers Azure | Magasin de fichiers |
| **Archiver / Froid** | Glacier S3, archives profondes | Niveaux Blob Cool/Archive | Stockage Cloud Coldline/Archives |
| **Transfert de données** | Boule de neige, DataSync | Boîte de données | Appareil de transfert |
### Comparaison des classes de stockage
| Cas d'utilisation | AWS S3 | Blob azur | Stockage cloud GCP |
|--------------|--------|------------|------------------------|
| **Accès fréquent** | Norme S3 | Chaud | Norme |
| **Accès peu fréquent** | S3 Standard-IA | Frais | Près de ligne |
| **Accès rare** | S3 One Zone-IA | — | Ligne froide |
| **Archiver** | Glacier S3 / Archives profondes | Archives | Archives |
---

## Bases de données
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **Relationnel (géré)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Base de données Azure (MySQL, PostgreSQL) ; Azure SQL | Cloud SQL (MySQL, PostgreSQL) |
| **Relationnel (cloud natif)** | Aurora (compatible MySQL/PostgreSQL) | Base de données Azure SQL (pools élastiques) | Cloud Spanner (distribué dans le monde entier) |
| **NoSQL (document)** | DynamoDB | Cosmos DB (API MongoDB, API SQL) | Magasin de feu ; Banque de données |
| **NoSQL (colonne large)** | DynamoDB (également) | Cosmos DB (API Cassandra) | Grande table |
| **NoSQL (clé-valeur)** | DynamoDB, ElastiCache | Cache Azure pour Redis | Mémoire (Redis) |
| **Graphique** | Neptune | Cosmos DB (API Gremlin) | — |
| **Série chronologique** | Flux temporel | Explorateur de données Azure | — |
| **Grand livre** | QLDB | Grand livre confidentiel Azure | — |
| **Cache en mémoire** | ElastiCache (Redis, Memcached) | Cache Azure pour Redis | Mémoire |
| **Recherche** | Service de recherche ouverte | Recherche Azure IA | Recherche dans le cloud ; Recherche Vertex AI |
| **Entrepôt de données** | Redshift | Analyse Synapse | BigQuery |
---

## IA et apprentissage automatique
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **Plateforme ML** | SageMaker | Apprentissage automatique Azure | Sommet AI |
| **API pré-entraînées** | Reconnaissance (vision), Polly (TTS), Compréhension (PNL), Transcription | Services cognitifs (vision, parole, langage, décision) | Vision AI, synthèse vocale, API de langage naturel |
| **LLM / IA Générative** | Substrat rocheux (Claude, Lama, Titan) | Service Azure OpenAI (GPT-4, DALL-E) | Sommet AI (Gémeaux) ; Jardin modèle |
| **Vecteur / Intégrations** | OpenSearch (k-NN), bases de connaissances Bedrock | Recherche Azure AI (vecteur) | Recherche de vecteurs Vertex AI, AlloyDB |
| **MLOps** | Pipelines SageMaker, registre de modèles | Pipelines Azure ML, registre de modèles | Pipelines Vertex AI, registre des modèles |
| **Étiquetage des données** | Vérité terrain SageMaker | Étiquetage des données Azure ML | Étiquetage des données Vertex AI |
| **IA conversationnelle** | Lex | Service de robots Azure | Dialogflow CX/ES |
| **Traduction** | Traduire | Traducteur | API de traduction |
---

## Réseautage
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **Réseau virtuel** | VPC | Réseau virtuel (VNet) | VPC |
| **Équilibrage de charge** | ELB/ALB/NLB/CLB | Équilibreur de charge (application, réseau, passerelle) | Équilibrage de charge cloud |
| **DNS** | Itinéraire 53 | DNS Azure | DNS en nuage |
| **CAN** | CloudFront | Porte d’entrée azur | CloudCDN |
| **Passerelle API** | Passerelle API | Gestion des API | Passerelle API |
| **VPN** | VPN site à site, VPN client | Passerelle VPN | VPN en nuage |
| **Connexion directe/ExpressRoute** | Connexion directe | ExpressRoute | Interconnexion cloud |
| **Lien privé** | PrivateLink, points de terminaison VPC | Lien privé, points de terminaison privés | Connexion au service privé |
| **Pare-feu** | WAF, pare-feu réseau | Pare-feu Azure, WAF | Armure cloud, pare-feu |
| **Protection DDoS** | Bouclier Standard / Avancé | Protection DDoS | Armure de nuage |
---

## Surveillance et journalisation
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **Mesures/Surveillance** | CloudWatch | Moniteur Azure | Surveillance du cloud (Stackdriver) |
| **Journalisation** | Journaux CloudWatch | Analyse des journaux (journaux Azure Monitor) | Journalisation dans le cloud |
| **Traçage** | Radiographie | Informations sur les applications | Trace de nuage |
| **Alertes** | Alarmes CloudWatch | Alertes du moniteur Azure | Alertes de surveillance du cloud |
| **Tableaux de bord** | Tableaux de bord CloudWatch | Classeurs/tableaux de bord Azure | Tableaux de bord de surveillance du cloud |
| **Suivi des erreurs** | Synthétiques CloudWatch | Informations sur les applications | Rapport d'erreurs cloud |
| **Tiers** | Datadog, nouvelle relique, PagerDuty | Datadog, nouvelle relique, PagerDuty | Datadog, nouvelle relique, PagerDuty |
---

## Infrastructure en tant que Code et DevOps
| Catégorie de services | AWS | Azur | GCP |
|-----------------|-----|-------|-----|
| **IaC (natif)** | Formation Cloud | Modèles BRAS / Biceps | Responsable de déploiement / Pulumi |
| **IaC (cross-cloud)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Biceps | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, actions GitHub | Création de nuages ; Déploiement cloud |
| **Registre de conteneurs** | REC | Registre de conteneurs Azure | Registre des artefacts |
| **GitOps** | Application Mesh + Flux/ArgoCD | Flux/ArgoCD sur AKS | Synchronisation de configuration (Anthos) |
| **Gestion des secrets** | Gestionnaire de secrets, magasin de paramètres SSM | Coffre-fort de clés | Gestionnaire secret |
---

## Considérations tarifaires
| Facteur | AWS | Azur | GCP |
|--------|-----|-------|-----|
| **granularité de facturation** | Par seconde (après la première heure pour certains) | Par seconde | Par seconde |
| **Remises pour utilisation durable** | Instances réservées/Plans d'épargne | VM réservées | Remises sur engagement d'utilisation |
| **Instances ponctuelles** | Jusqu'à 90% de réduction | Jusqu'à 90% de réduction | Jusqu'à 91% de réduction |
| **Sortie de données** | Facturé (cher) | Facturé | Même prix quelle que soit la destination (souvent moins cher) |
| **Niveau gratuit** | 12 mois + toujours gratuit | 12 mois + crédit de 200$ | 300 $ pour 90 jours + toujours gratuit |
| **Remises d'entreprise** | Programme de remise aux entreprises (EDP) | MACC (Contrat d'engagement monétaire) | Utilisation engagée + CUD |
---

## Quand utiliser lequel
| Scénario | Recommandé | Pourquoi |
|----------|-------------|-----|
| **La plus large sélection de services ; écosystème mature** | AWS | Le plus grand catalogue ; la plupart des intégrations tierces |
| **Microsoft entreprise ; Active Directory ; hybride** | Azur | Intégration AD native ; outillage hybride solide |
| **Entreposage de données ; BigQuery ; à forte intensité d'analyse** | GCP | BigQuery est le meilleur de sa catégorie ; intégration transparente des données |
| **Développement natif Kubernetes** | GCP | GKE est le Kubernetes géré le plus abouti |
| **Applications IA génératives / LLM** | Azure ou GCP | Azure OpenAI pour les modèles GPT ; Vertex AI pour Gemini |
| **Applications à l'échelle mondiale et à faible latence** | GCP | Le réseau mondial de Google est un véritable avantage |
| **Charges de travail lourdes liées au gouvernement et à la conformité** | AWS ou Azure | La plupart des certifications de conformité ; Régions GovCloud |
| **Startups sensibles aux coûts** | GCP ou AWS | L'offre gratuite de GCP est généreuse ; AWS a des crédits de démarrage |
| **Pile Microsoft/.NET existante** | Azur | Intégration étroite avec Visual Studio, .NET, Office 365 |
| **Stratégie multi-cloud** | Terraform + les trois | Utilisez Terraform pour gérer les ressources dans les cloud |
---

## Résumé
Les trois cloud sont performants, fiables et en constante expansion. Le choix se résume généralement à : ce que votre équipe sait déjà, à quoi ressemblent vos contrats existants et quels services spécifiques sont importants pour votre charge de travail. Le multicloud est de plus en plus courant : utilisez Terraform ou Pulumi pour éviter de dépendre d'un fournisseur au niveau de la couche d'infrastructure et choisissez chaque cloud pour ce qu'il fait le mieux.