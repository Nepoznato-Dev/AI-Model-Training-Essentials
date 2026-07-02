# Architecture cloud

## Fondamentaux du cloud computing

### Qu'est-ce que le cloud computing ?
La fourniture à la demande de ressources informatiques (serveurs, stockage, bases de données, réseau, logiciels) via internet avec une tarification à l'usage.

### Caractéristiques essentielles (définition du NIST)
- **Libre-service à la demande** : Provisionner des ressources sans interaction humaine
- **Accès réseau étendu** : Disponible via le réseau à l'aide de mécanismes standard
- **Mutualisation des ressources** : Modèle multi-tenant avec attribution dynamique
- **Élasticité rapide** : Monter et descendre en capacité rapidement
- **Service mesuré** : Utilisation des ressources surveillée et facturée

### Modèles de déploiement cloud
- **Cloud public** : Possédé par des fournisseurs, infrastructure partagée (AWS, Azure, GCP)
- **Cloud privé** : Dédié à une seule organisation (sur site ou hébergé)
- **Cloud hybride** : Combinaison de clouds publics et privés
- **Multi-cloud** : Utilisation de plusieurs fournisseurs de cloud public
- **Cloud communautaire** : Partagé par des organisations ayant des préoccupations communes

### Modèles de service

#### Infrastructure as a Service (IaaS)
- **Fournit** : Machines virtuelles, stockage, réseaux, systèmes d'exploitation
- **Exemples** : AWS EC2, Google Compute Engine, Azure VMs
- **Cas d'usage** : Migrations lift-and-shift, environnements de développement, besoins de contrôle élevé

#### Platform as a Service (PaaS)
- **Fournit** : Plateformes de développement, bases de données, middleware
- **Exemples** : Heroku, Google App Engine, AWS Elastic Beanstalk
- **Cas d'usage** : Développement d'applications, déploiement d'API, microservices

#### Software as a Service (SaaS)
- **Fournit** : Applications complètes via internet
- **Exemples** : Salesforce, Google Workspace, Microsoft 365, Slack
- **Cas d'usage** : E-mail, CRM, collaboration, applications métier

#### Function as a Service (FaaS) / Serverless
- **Fournit** : Exécution de fonctions pilotée par événements
- **Exemples** : AWS Lambda, Azure Functions, Google Cloud Functions
- **Cas d'usage** : Traitement d'événements, API, tâches planifiées, traitement en temps réel

## Principaux fournisseurs cloud

### Amazon Web Services (AWS)
- **Part de marché** : ~32 % (plus grand fournisseur)
- **Services clés** :
  - Compute : EC2, Lambda, ECS, EKS
  - Storage : S3, EBS, Glacier
  - Database : RDS, DynamoDB, Aurora
  - Networking : VPC, Route 53, CloudFront
  - AI/ML : SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Part de marché** : ~23 %
- **Points forts** : Intégration entreprise, cloud hybride, écosystème Microsoft
- **Services clés** :
  - Compute : Virtual Machines, Azure Functions, AKS
  - Storage : Blob Storage, Disk Storage
  - Database : SQL Database, Cosmos DB
  - Networking : Virtual Network, Traffic Manager
  - AI/ML : Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Part de marché** : ~10 %
- **Points forts** : Analyse de données, AI/ML, Kubernetes
- **Services clés** :
  - Compute : Compute Engine, Cloud Functions, GKE
  - Storage : Cloud Storage, Persistent Disk
  - Database : Cloud SQL, Firestore, Bigtable
  - Analytics : BigQuery, Dataflow, Pub/Sub
  - AI/ML : Vertex AI, AutoML

### Autres fournisseurs
- **IBM Cloud** : Orientation entreprise, Watson AI
- **Oracle Cloud** : Charges de travail bases de données, applications d'entreprise
- **Alibaba Cloud** : Dominant en Asie-Pacifique
- **DigitalOcean** : Convivial pour les développeurs, offres simplifiées

## Modèles d'architecture cloud

### Principes du Well-Architected Framework

#### Excellence opérationnelle
- Automatiser les opérations
- Effectuer des changements fréquents et réversibles
- Améliorer les procédures en continu
- Anticiper les défaillances

#### Sécurité
- Mettre en place une base d'identité solide
- Assurer la traçabilité
- Appliquer la sécurité à toutes les couches
- Automatiser les bonnes pratiques de sécurité
- Protéger les données en transit et au repos

#### Fiabilité
- Tester les procédures de reprise
- Récupérer automatiquement après une défaillance
- Monter horizontalement en charge pour la disponibilité
- Arrêter de deviner la capacité nécessaire
- Gérer le changement par l'automatisation

#### Efficacité des performances
- Démocratiser les technologies avancées
- Se déployer à l'échelle mondiale en quelques minutes
- Utiliser des architectures serverless
- Expérimenter plus souvent
- Tenir compte de la compatibilité mécanique

#### Optimisation des coûts
- Adopter un modèle de consommation
- Mesurer l'efficacité globale
- Éviter de dépenser pour du travail sans valeur différenciante
- Analyser et attribuer les dépenses
- Utiliser des services managés

### Modèles d'architecture courants

#### Architecture microservices
- Décomposer les applications en services petits et indépendants
- Chaque service possède ses données et sa logique
- Communiquer via des API (REST, gRPC, messaging)
- Déployer indépendamment
- **Avantages** : Scalabilité, isolation des pannes, diversité technologique
- **Défis** : Complexité distribuée, cohérence des données, supervision

#### Architecture pilotée par événements
- Les composants communiquent par événements
- Les producteurs émettent des événements, les consommateurs réagissent
- **Modèles** : Event sourcing, CQRS, pub/sub
- **Technologies** : Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Avantages** : Couplage faible, scalabilité, traitement en temps réel

#### Architecture serverless
- Aucune gestion de serveur requise
- Paiement par exécution
- Scalabilité automatique
- **Composants** : Fonctions, API Gateway, services managés
- **Avantages** : Efficacité des coûts, opérations réduites, déploiement rapide
- **Points à considérer** : Démarrages à froid, verrouillage fournisseur, limites d'exécution

#### Architecture en couches (N-Tier)
- Couche de présentation (UI)
- Couche de logique applicative / métier
- Couche d'accès aux données
- Couche base de données
- **Avantages** : Séparation des responsabilités, maintenabilité
- **Courant** : Applications web 3-tiers

#### Space-Based Architecture
- Gérer une forte concurrence avec des données distribuées
- Mémoire virtualisée entre les serveurs
- Les nœuds de traitement montent en charge indépendamment
- **Cas d'usage** : Applications à fort volume et faible latence

## Services de calcul

### Machines virtuelles
- **Types** : Usage général, optimisées calcul, optimisées mémoire, GPU
- **Tarification** : On-demand, instances réservées, instances spot
- **Gestion** : Groupes d'auto-scaling, load balancers
- **Bonnes pratiques** : Dimensionnement adapté, étiquetage, supervision, correctifs

### Conteneurs
- **Docker** : Standard d'exécution de conteneurs
- **Orchestration** : Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Avantages** : Portabilité, efficacité, cohérence
- **Registry** : ECR, GCR, ACR, Docker Hub

### Fonctions serverless
- **Modèle d'exécution** : Déclenché par événements, sans état
- **Limites** : Temps d'exécution, mémoire, exécutions simultanées
- **Cas d'usage** : API, traitement de fichiers, tâches planifiées, backends IoT
- **Supervision** : Nombre d'invocations, erreurs, durée, démarrages à froid

## Solutions de stockage

### Object Storage
- **Caractéristiques** : Structure plate, métadonnées, accès HTTP
- **Exemples** : AWS S3, Google Cloud Storage, Azure Blob
- **Cas d'usage** : Ressources statiques, sauvegardes, data lakes, archives
- **Classes de stockage** : Hot, cool, cold, archive (coût/accès variables)

### Block Storage
- **Caractéristiques** : Volumes bruts, attachés aux VMs
- **Exemples** : AWS EBS, Google Persistent Disk, Azure Disks
- **Cas d'usage** : Bases de données, volumes de démarrage, besoins haute performance
- **Types** : SSD, HDD, IOPS provisionnées

### File Storage
- **Caractéristiques** : Systèmes de fichiers partagés, protocoles NFS/SMB
- **Exemples** : AWS EFS, Google Filestore, Azure Files
- **Cas d'usage** : Gestion de contenu, configurations partagées, lift-and-shift

### Archive Storage
- **Caractéristiques** : Coût le plus faible, délais de récupération
- **Exemples** : S3 Glacier, Azure Archive Storage
- **Cas d'usage** : Conformité, sauvegardes long terme, données historiques

## Services de base de données

### Bases de données relationnelles managées
- **Services** : AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Fonctionnalités** : Sauvegardes automatisées, correctifs, mise à l'échelle, réplication
- **Moteurs** : MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bases de données NoSQL
- **Document** : DocumentDB, Firestore, Cosmos DB
- **Key-Value** : DynamoDB, Redis Cache
- **Wide-Column** : Bigtable, Cassandra (managed)
- **Graph** : Neptune, Cosmos DB (graph API)

### Data Warehousing
- **Services** : Snowflake, Redshift, BigQuery, Synapse
- **Caractéristiques** : Stockage colonnaire, architecture MPP
- **Cas d'usage** : Analytics, BI, analyse de données à grande échelle

### Services de cache
- **In-Memory** : ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching** : CloudFront, Cloud CDN, Azure CDN
- **Cas d'usage** : Stockage de sessions, cache de requêtes, diffusion de contenu

## Réseau

### Réseaux virtuels
- **VPC/VNet** : Environnements réseau isolés
- **Subnets** : Publics (exposés à internet), privés (internes uniquement)
- **Adressage IP** : Blocs CIDR, IPv4/IPv6
- **Tables de routage** : Contrôlent les flux réseau

### Répartition de charge
- **Types** : Application (L7), Network (L4), Gateway
- **Fonctionnalités** : Contrôles d'état, terminaison SSL, sticky sessions
- **Services** : ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Réseaux de diffusion de contenu (CDN)
- **Objectif** : Mettre le contenu en cache en périphérie
- **Avantages** : Latence réduite, charge moindre sur l'origine, distribution mondiale
- **Services** : CloudFront, Cloud CDN, Azure CDN, Akamai

### Services DNS
- **Fonctions** : Enregistrement de domaines, routage, contrôles d'état
- **Services** : Route 53, Cloud DNS, Azure DNS
- **Politiques de routage** : Simple, pondéré, basé sur la latence, géolocalisation, basculement

### Options de connectivité
- **Internet Gateway** : Accès public à internet
- **NAT Gateway** : Accès sortant depuis un subnet privé
- **VPN** : Tunnels chiffrés vers l'on-premises
- **Direct Connect/ExpressRoute** : Connexions privées dédiées
- **VPC Peering** : Connecter des VPC dans/entre des comptes

## Sécurité dans le cloud

### Modèle de responsabilité partagée
- **Responsabilité du fournisseur** : Sécurité DU cloud (infrastructure)
- **Responsabilité du client** : Sécurité DANS le cloud (données, applications, accès)
- **Varie selon le service** : Plus c'est managé, plus la responsabilité du fournisseur augmente

### Identity and Access Management (IAM)
- **Users** : Identités individuelles
- **Groups** : Groupes d'utilisateurs
- **Roles** : Identifiants temporaires pour services/utilisateurs
- **Policies** : Documents JSON définissant les permissions
- **Principes** : Moindre privilège, séparation des tâches

### Sécurité réseau
- **Security Groups** : Pare-feu à états pour les instances
- **Network ACLs** : Pare-feu sans état pour les subnets
- **Web Application Firewall (WAF)** : Protection contre les attaques web
- **DDoS Protection** : Shield, Cloud Armor, DDoS Protection

### Protection des données
- **Encryption at Rest** : KMS, clés gérées par le client
- **Encryption in Transit** : TLS/SSL, HTTPS
- **Gestion des clés** : HSM, rotation des clés, pistes d'audit
- **Secrets Management** : Secrets Manager, Key Vault

### Conformité et gouvernance
- **Certifications** : SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Outils** : Application des politiques, rapports de conformité, journaux d'audit
- **Référentiels** : Cloud Security Alliance, NIST CSF

## DevOps dans le cloud

### Services CI/CD
- **AWS** : CodePipeline, CodeBuild, CodeDeploy
- **Azure** : Azure DevOps, GitHub Actions
- **GCP** : Cloud Build, Cloud Deploy
- **Tiers** : Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform** : Multi-cloud, déclaratif, gestion d'état
- **CloudFormation** : Natif AWS, templates YAML/JSON
- **ARM Templates** : Natif Azure
- **Deployment Manager** : Natif GCP
- **Pulumi** : Infrastructure avec des langages de programmation
- **Avantages** : Contrôle de version, répétabilité, documentation

### Gestion de configuration
- **Ansible** : Sans agent, playbooks YAML
- **Chef** : Basé sur Ruby, écosystème mature
- **Puppet** : Déclaratif, rapports solides
- **SaltStack** : Rapide, basé sur Python

### Monitoring et observabilité
- **Metrics** : CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging** : CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing** : X-Ray, Cloud Trace, Application Insights
- **Dashboards** : CloudWatch Dashboards, Cloud Console
- **Alerting** : SNS, alertes Cloud Monitoring, Action Groups

### Orchestration de conteneurs
- **Kubernetes** : Standard de l'industrie pour l'orchestration
- **Services managés** : EKS, AKS, GKE
- **Service Mesh** : Istio, Linkerd (gestion du trafic, sécurité)
- **GitOps** : ArgoCD, Flux (déploiements déclaratifs)

## Gestion des coûts

### Modèles de tarification
- **Pay-as-you-go** : Payer ce que vous utilisez
- **Reserved Instances** : Engagements de 1 à 3 ans, remises importantes
- **Spot Instances** : Enchérir sur la capacité inutilisée, interruption possible
- **Savings Plans** : Tarification flexible avec engagement
- **Free Tier** : Usage gratuit limité pour les nouveaux comptes

### Stratégies d'optimisation des coûts
- **Right-sizing** : Adapter les types d'instances aux besoins de la charge
- **Auto-scaling** : Monter en charge selon la demande
- **Capacité réservée** : S'engager sur des charges stables
- **Usage du spot** : Pour des charges tolérantes aux pannes et flexibles
- **Paliers de stockage** : Déplacer les données peu consultées vers des niveaux moins chers
- **Nettoyage** : Supprimer ressources inutilisées, snapshots, AMIs

### Outils de gestion des coûts
- **AWS** : Cost Explorer, Budgets, Trusted Advisor
- **Azure** : Cost Management, Advisor
- **GCP** : Billing reports, Recommender
- **Tiers** : CloudHealth, CloudCheckr, Datadog

## Haute disponibilité et reprise après sinistre

### Concepts de disponibilité
- **Availability Zones** : Centres de données physiquement séparés dans une région
- **Regions** : Zones géographiques avec plusieurs AZ
- **Edge Locations** : Emplacements de cache CDN dans le monde

### Stratégies HA
- **Multi-AZ** : Déployer sur plusieurs zones de disponibilité
- **Auto-healing** : Remplacer automatiquement les instances défaillantes
- **Load Balancing** : Répartir le trafic sur les instances saines
- **Réplication de base de données** : Déploiements Multi-AZ, read replicas

### Stratégies de reprise après sinistre
- **Backup and Restore** : Sauvegardes périodiques, restauration en cas de besoin (coût minimal)
- **Pilot Light** : Éléments essentiels actifs, montée en charge pendant le sinistre
- **Warm Standby** : Version réduite toujours en fonctionnement
- **Multi-Site Active/Active** : Production complète dans plusieurs régions (coût maximal)

### RTO et RPO
- **Recovery Time Objective (RTO)** : Durée maximale d'indisponibilité acceptable
- **Recovery Point Objective (RPO)** : Perte de données maximale acceptable
- **Choix de stratégie** : Selon les exigences métier et le budget

## Tendances émergentes

### Edge Computing
- Traiter les données au plus près de la source
- **Services** : AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Cas d'usage** : IoT, analytics en temps réel, applications à faible latence

### Multi-Cloud et cloud hybride
- Éviter le verrouillage fournisseur
- Tirer parti des meilleurs services de chaque fournisseur
- **Outils** : Terraform, Anthos, Arc, CloudHealth

### Services AI/ML
- Modèles préentraînés : Vision, parole, langage
- Entraînement de modèles personnalisés : SageMaker, Vertex AI, Azure ML
- MLOps : Déploiement, supervision, gouvernance des modèles

### Informatique quantique
- **Services** : AWS Braket, Azure Quantum
- **Statut** : Stade précoce, expérimental
- **Potentiel** : Cryptographie, optimisation, découverte de médicaments

### Cloud durable
- Suivi de l'empreinte carbone
- Engagements en faveur des énergies renouvelables
- Utilisation efficace des ressources
- Modèles d'architecture verte
