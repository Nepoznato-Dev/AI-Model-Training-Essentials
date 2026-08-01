<!-- 
This file was automatically translated from English to French.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Architecture du cloud

## Fondamentaux de l'informatique en nuage

### Qu'est-ce que l'informatique en nuage ?
L'informatique en nuage désigne la fourniture à la demande de ressources informatiques (serveurs, stockage, bases de données, réseau, logiciels) via Internet, avec une facturation à l'usage.

### Caractéristiques essentielles (définition du NIST)
- **Libre-service à la demande** : provisionner des ressources sans intervention humaine
- **Large accès réseau** : accès via le réseau au moyen de mécanismes standard
- **Mutualisation des ressources** : modèle multi-locataire avec attribution dynamique
- **Élasticité rapide** : montée en charge et réduction rapides des ressources
- **Service mesuré** : utilisation des ressources surveillée et facturée

### Modèles de déploiement du cloud
- **Cloud public** : exploité par des fournisseurs, avec une infrastructure partagée (AWS, Azure, GCP)
- **Cloud privé** : dédié à une seule organisation (sur site ou hébergé)
- **Cloud hybride** : combinaison de clouds publics et privés
- **Multi-cloud** : utilisation de plusieurs fournisseurs de cloud public
- **Cloud communautaire** : partagé par des organisations ayant des préoccupations communes

### Modèles de service

#### Infrastructure en tant que service (IaaS)
- **Fournit** : machines virtuelles, stockage, réseaux, systèmes d'exploitation
- **Exemples** : AWS EC2, Google Compute Engine, Azure VMs
- **Cas d'utilisation** : migrations lift-and-shift, environnements de développement, besoins de contrôle élevés

#### Plateforme en tant que service (PaaS)
- **Fournit** : plateformes de développement, bases de données, middleware
- **Exemples** : Heroku, Google App Engine, AWS Elastic Beanstalk
- **Cas d'utilisation** : développement d'applications, déploiement d'API, microservices

#### Logiciel en tant que service (SaaS)
- **Fournit** : applications complètes accessibles via Internet
- **Exemples** : Salesforce, Google Workspace, Microsoft 365, Slack
- **Cas d'utilisation** : messagerie, CRM, collaboration, applications d'entreprise

#### Fonction en tant que service (FaaS) / sans serveur
- **Fournit** : exécution de fonctions déclenchée par des événements
- **Exemples** : AWS Lambda, Azure Functions, Google Cloud Functions
- **Cas d'utilisation** : traitement d'événements, API, tâches planifiées, traitement en temps réel

## Principaux fournisseurs de cloud

### Amazon Web Services (AWS)
- **Part de marché** : ~32 % (plus grand fournisseur)
- **Services clés** :
  - Calcul : EC2, Lambda, ECS, EKS
  - Stockage : S3, EBS, Glacier
  - Bases de données : RDS, DynamoDB, Aurora
  - Réseau : VPC, Route 53, CloudFront
  - IA/ML : SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Part de marché** : ~23 %
- **Points forts** : intégration en entreprise, cloud hybride, écosystème Microsoft
- **Services clés** :
  - Calcul : Virtual Machines, Azure Functions, AKS
  - Stockage : Blob Storage, Disk Storage
  - Bases de données : SQL Database, Cosmos DB
  - Réseau : Virtual Network, Traffic Manager
  - IA/ML : Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Part de marché** : ~10 %
- **Points forts** : analytique de données, IA/ML, Kubernetes
- **Services clés** :
  - Calcul : Compute Engine, Cloud Functions, GKE
  - Stockage : Cloud Storage, Persistent Disk
  - Bases de données : Cloud SQL, Firestore, Bigtable
  - Analytique : BigQuery, Dataflow, Pub/Sub
  - IA/ML : Vertex AI, AutoML

### Autres fournisseurs
- **IBM Cloud** : orientation entreprise, Watson AI
- **Oracle Cloud** : charges de travail de bases de données, applications d'entreprise
- **Alibaba Cloud** : leader en Asie-Pacifique
- **DigitalOcean** : convivial pour les développeurs, offres simplifiées

## Modèles d'architecture cloud

### Principes du cadre Well-Architected

#### Excellence opérationnelle
- Automatiser les opérations
- Apporter des changements fréquents et réversibles
- Affiner continuellement les procédures
- Anticiper les défaillances

#### Sécurité
- Mettre en place une base d'identité solide
- Activer la traçabilité
- Appliquer la sécurité à toutes les couches
- Automatiser les bonnes pratiques de sécurité
- Protéger les données en transit et au repos

#### Fiabilité
- Tester les procédures de reprise
- Se rétablir automatiquement après une défaillance
- Mettre à l'échelle pour assurer la disponibilité
- Cesser d'estimer la capacité au hasard
- Gérer les changements par l'automatisation

#### Efficacité des performances
- Démocratiser les technologies avancées
- Passer à l'échelle mondiale en quelques minutes
- Utiliser des architectures serverless
- Expérimenter plus souvent
- Tenir compte de la « sympathie mécanique » (compréhension du matériel sous-jacent)

#### Optimisation des coûts
- Adopter un modèle de consommation
- Mesurer l'efficacité globale
- Cesser de dépenser pour un travail sans valeur différenciante
- Analyser et attribuer les dépenses
- Utiliser des services gérés

### Modèles d'architecture courants

#### Architecture microservices
- Décomposer les applications en petits services indépendants
- Chaque service possède ses propres données et sa propre logique
- Communiquer via des API (REST, gRPC, messagerie)
- Déployer indépendamment
- **Avantages** : évolutivité, isolation des pannes, diversité technologique
- **Défis** : complexité distribuée, cohérence des données, supervision

#### Architecture pilotée par les événements
- Les composants communiquent par des événements
- Les producteurs émettent des événements, les consommateurs réagissent
- **Modèles** : event sourcing, CQRS, pub/sub
- **Technologies** : Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Avantages** : faible couplage, évolutivité, traitement en temps réel

#### Architecture sans serveur
- Aucune gestion de serveur requise
- Paiement à l'exécution
- Mise à l'échelle automatique
- **Composants** : fonctions, API Gateway, services gérés
- **Avantages** : efficacité des coûts, opérations réduites, déploiement rapide
- **Considérations** : démarrages à froid, dépendance au fournisseur, limites d'exécution

#### Architecture en couches (N-tier)
- Couche de présentation (UI)
- Couche logique applicative et métier
- Couche d'accès aux données
- Couche de base de données
- **Avantages** : séparation des responsabilités, maintenabilité
- **Courant** : applications web à 3 niveaux

#### Architecture orientée espace
- Gérer une forte concurrence avec des données distribuées
- Mémoire virtualisée sur plusieurs serveurs
- Les nœuds de traitement s'adaptent indépendamment
- **Cas d'utilisation** : applications à fort volume et faible latence

## Services de calcul

### Machines virtuelles
- **Types** : usage général, optimisé pour le calcul, optimisé pour la mémoire, GPU
- **Tarification** : à la demande, instances réservées, instances spot
- **Gestion** : groupes de mise à l'échelle automatique, équilibreurs de charge
- **Meilleures pratiques** : dimensionnement adapté, étiquetage, surveillance, correctifs

### Conteneurs
- **Docker** : standard d'exécution des conteneurs
- **Orchestration** : Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Avantages** : portabilité, efficacité, cohérence
- **Registre** : ECR, GCR, ACR, Docker Hub

### Fonctions sans serveur
- **Modèle d'exécution** : déclenché par des événements, sans état
- **Limites** : temps d'exécution, mémoire, exécutions simultanées
- **Cas d'utilisation** : API, traitement de fichiers, tâches planifiées, backends IoT
- **Surveillance** : nombre d'invocations, erreurs, durée, démarrages à froid

## Solutions de stockage

### Stockage objet
- **Caractéristiques** : structure plate, métadonnées, accès HTTP
- **Exemples** : AWS S3, Google Cloud Storage, Azure Blob
- **Cas d'utilisation** : ressources statiques, sauvegardes, lacs de données, archives
- **Classes de stockage** : chaud, froid, très froid, archive (coût/accès variable)

### Stockage par blocs
- **Caractéristiques** : volumes bruts, attachés aux VM
- **Exemples** : AWS EBS, Google Persistent Disk, Azure Disks
- **Cas d'utilisation** : bases de données, volumes de démarrage, besoins de hautes performances
- **Types** : SSD, HDD, IOPS provisionnés

### Stockage de fichiers
- **Caractéristiques** : systèmes de fichiers partagés, protocoles NFS/SMB
- **Exemples** : AWS EFS, Google Filestore, Azure Files
- **Cas d'utilisation** : gestion de contenu, configurations partagées, lift-and-shift

### Stockage d'archives
- **Caractéristiques** : coût minimal, délais de récupération
- **Exemples** : S3 Glacier, Azure Archive Storage
- **Cas d'utilisation** : conformité, sauvegardes à long terme, données historiques

## Services de base de données

### Bases de données relationnelles gérées
- **Services** : AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Fonctionnalités** : sauvegardes automatisées, correctifs, mise à l'échelle, réplication
- **Moteurs** : MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bases de données NoSQL
- **Document** : DocumentDB, Firestore, Cosmos DB
- **Clé-valeur** : DynamoDB, Redis Cache
- **Colonne large** : Bigtable, Cassandra (géré)
- **Graphe** : Neptune, Cosmos DB (API graphe)

### Entrepôts de données
- **Services** : Snowflake, Redshift, BigQuery, Synapse
- **Caractéristiques** : stockage colonnaire, architecture MPP
- **Cas d'utilisation** : analytique, BI, analyse de données à grande échelle

### Services de mise en cache
- **En mémoire** : ElastiCache (Redis/Memcached), Cloud Memorystore
- **Cache CDN** : CloudFront, Cloud CDN, Azure CDN
- **Cas d'utilisation** : stockage de session, cache de requêtes, diffusion de contenu

## Réseau

### Réseaux virtuels
- **VPC/VNet** : environnements réseau isolés
- **Sous-réseaux** : public (exposé à Internet), privé (interne uniquement)
- **Adressage IP** : blocs CIDR, IPv4/IPv6
- **Tables de routage** : contrôler les flux de trafic

### Équilibrage de charge
- **Types** : applicatif (L7), réseau (L4), passerelle
- **Fonctionnalités** : contrôles d'état, terminaison SSL, persistance de session
- **Services** : ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Réseaux de diffusion de contenu (CDN)
- **Objectif** : mettre en cache le contenu sur des points de présence en périphérie
- **Avantages** : latence réduite, charge moindre sur l'origine, distribution mondiale
- **Services** : CloudFront, Cloud CDN, Azure CDN, Akamai

### Services DNS
- **Fonctions** : enregistrement de domaine, routage, contrôles d'état
- **Services** : Route 53, Cloud DNS, Azure DNS
- **Politiques de routage** : simple, pondéré, basé sur la latence, géolocalisation, basculement

### Options de connectivité
- **Passerelle Internet** : accès public à Internet
- **Passerelle NAT** : accès sortant pour le sous-réseau privé
- **VPN** : tunnels chiffrés vers les locaux de l'entreprise
- **Direct Connect/ExpressRoute** : connexions privées dédiées
- **VPC Peering** : connecter des VPC au sein d'un même compte ou entre plusieurs comptes

## Sécurité dans le cloud

### Modèle de responsabilité partagée
- **Responsabilité du fournisseur** : sécurité du cloud (infrastructure)
- **Responsabilité du client** : sécurité dans le cloud (données, applications, accès)
- **Varie selon le service** : plus le service est géré, plus la responsabilité du fournisseur est importante

### Gestion des identités et des accès (IAM)
- **Utilisateurs** : identités individuelles
- **Groupes** : ensembles d'utilisateurs
- **Rôles** : identifiants temporaires pour les services et les utilisateurs
- **Stratégies** : documents JSON définissant les autorisations
- **Principes** : moindre privilège, séparation des tâches

### Sécurité réseau
- **Groupes de sécurité** : pare-feu avec état pour les instances
- **ACL réseau** : pare-feu sans état pour les sous-réseaux
- **Pare-feu applicatif web (WAF)** : protection contre les exploits web
- **Protection DDoS** : Shield, Cloud Armor, DDoS Protection

### Protection des données
- **Chiffrement au repos** : KMS, clés gérées par le client
- **Chiffrement en transit** : TLS/SSL, HTTPS
- **Gestion des clés** : HSM, rotation des clés, pistes d'audit
- **Gestion des secrets** : Secrets Manager, Key Vault

### Conformité et gouvernance
- **Certifications** : SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Outils** : application des politiques, rapports de conformité, journaux d'audit
- **Cadres** : Cloud Security Alliance, NIST CSF

## DevOps dans le cloud

### Services CI/CD
- **AWS** : CodePipeline, CodeBuild, CodeDeploy
- **Azure** : Azure DevOps, GitHub Actions
- **GCP** : Cloud Build, Cloud Deploy
- **Tiers** : Jenkins, CircleCI, GitLab CI

### Infrastructure en tant que code (IaC)
- **Terraform** : multi-cloud, déclaratif, gestion d'état
- **CloudFormation** : natif AWS, modèles YAML/JSON
- **ARM Templates** : natif Azure
- **Deployment Manager** : natif GCP
- **Pulumi** : infrastructure définie avec des langages de programmation
- **Avantages** : contrôle de version, reproductibilité, documentation

### Gestion de configuration
- **Ansible** : sans agent, playbooks YAML
- **Chef** : basé sur Ruby, écosystème mature
- **Puppet** : déclaratif, reporting solide
- **SaltStack** : rapide, basé sur Python

### Surveillance et observabilité
- **Métriques** : CloudWatch, Cloud Monitoring, Azure Monitor
- **Journalisation** : CloudWatch Logs, Cloud Logging, Log Analytics
- **Traçage** : X-Ray, Cloud Trace, Application Insights
- **Tableaux de bord** : CloudWatch Dashboards, Cloud Console
- **Alertes** : SNS, alertes Cloud Monitoring, Action Groups

### Orchestration des conteneurs
- **Kubernetes** : standard de l'industrie pour l'orchestration
- **Services gérés** : EKS, AKS, GKE
- **Service Mesh** : Istio, Linkerd (gestion du trafic, sécurité)
- **GitOps** : ArgoCD, Flux (déploiements déclaratifs)

## Gestion des coûts

### Modèles de tarification
- **Pay-as-you-go** : payez uniquement ce que vous utilisez
- **Instances réservées** : engagements de 1 à 3 ans, remises importantes
- **Instances spot** : enchérir sur la capacité inutilisée, avec risque d'interruption
- **Plans d'économie** : tarification flexible basée sur l'engagement
- **Niveau gratuit** : utilisation gratuite limitée pour les nouveaux comptes

### Stratégies d'optimisation des coûts
- **Dimensionnement adapté** : choisir les types d'instance selon les besoins de la charge de travail
- **Mise à l'échelle automatique** : ajuster les ressources en fonction de la demande
- **Capacité réservée** : s'engager pour des charges de travail stables
- **Utilisation des instances spot** : à privilégier pour des charges de travail tolérantes aux pannes et flexibles
- **Niveaux de stockage** : déplacer les données peu consultées vers des niveaux moins coûteux
- **Nettoyage** : supprimer les ressources inutilisées, instantanés et AMI

### Outils de gestion des coûts
- **AWS** : Cost Explorer, Budgets, Trusted Advisor
- **Azure** : Cost Management, Advisor
- **GCP** : rapports de facturation, Recommender
- **Tiers** : CloudHealth, CloudCheckr, Datadog

## Haute disponibilité et reprise d'activité

### Concepts de disponibilité
- **Zones de disponibilité** : centres de données physiquement séparés dans une région
- **Régions** : zones géographiques avec plusieurs AZ
- **Emplacements périphériques** : emplacements de cache CDN répartis dans le monde

### Stratégies HA
- **Multi-AZ** : déploiement sur plusieurs zones de disponibilité
- **Auto-réparation** : remplacement automatique des instances défaillantes
- **Équilibrage de charge** : répartir le trafic entre les instances saines
- **Réplication de base de données** : déploiements Multi-AZ, réplicas en lecture

### Stratégies de reprise d'activité
- **Sauvegarde et restauration** : sauvegardes périodiques, restauration si nécessaire (coût le plus faible)
- **Pilot Light** : composants essentiels actifs, montée en charge en cas de catastrophe
- **Standby chaud** : version réduite toujours en cours d'exécution
- **Multi-site actif/actif** : production complète dans plusieurs régions (coût le plus élevé)

### RTO et RPO
- **Objectif de temps de reprise (RTO)** : durée maximale d'interruption acceptable
- **Objectif de point de reprise (RPO)** : perte maximale de données acceptable
- **Choix de la stratégie** : basé sur les exigences métier et le budget

## Tendances émergentes

### Informatique en périphérie (edge computing)
- Traiter les données au plus près de la source
- **Services** : AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Cas d'utilisation** : IoT, analytique en temps réel, applications à faible latence

### Multi-cloud et cloud hybride
- Éviter la dépendance à un fournisseur unique
- Tirer parti des meilleurs services de chaque catégorie
- **Outils** : Terraform, Anthos, Arc, CloudHealth

### Services IA/ML
- Modèles préentraînés : vision, parole, langue
- Entraînement de modèles personnalisés : SageMaker, Vertex AI, Azure ML
- MLOps : déploiement de modèles, surveillance, gouvernance

### Informatique quantique
- **Services** : AWS Braket, Azure Quantum
- **Statut** : stade précoce, encore expérimental
- **Potentiel** : cryptographie, optimisation, découverte de médicaments

### Cloud durable
- Suivi de l'empreinte carbone
- Engagements en faveur des énergies renouvelables
- Utilisation efficace des ressources
- Modèles d'architecture sobres en énergie
