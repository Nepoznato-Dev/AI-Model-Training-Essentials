<!-- 
This file was automatically translated from English to French.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Architecture Cloud

## Fondamentaux du Cloud Computing

### Qu'est-ce que le Cloud Computing ?
Livraison à la demande de ressources informatiques (serveurs, stockage, bases de données, réseau, logiciels) via Internet avec une tarification à l'usage.

### Caractéristiques Essentielles (Définition NIST)
- **Auto-service à la demande**: Provisionner les ressources sans interaction humaine
- **Accès réseau large**: Disponible via le réseau via des mécanismes standard
- **Mise en commun des ressources**: Modèle multi-locataire avec attribution dynamique
- **Élasticité rapide**: Mise à l'échelle horizontale rapide dans les deux sens
- **Service mesuré**: Utilisation des ressources surveillée et facturée

### Modèles de Déploiement Cloud
- **Cloud Public**: Possédé par des fournisseurs, infrastructure partagée (AWS, Azure, GCP)
- **Cloud Privé**: Dédié à une seule organisation (sur site ou hébergé)
- **Cloud Hybride**: Combinaison de clouds publics et privés
- **Multi-Cloud**: Utilisation de plusieurs fournisseurs de cloud public
- **Cloud Communautaire**: Partagé par des organisations avec des préoccupations communes

### Modèles de Service

#### Infrastructure as a Service (IaaS)
- **Fournit**: Machines virtuelles, stockage, réseaux, systèmes d'exploitation
- **Exemples**: AWS EC2, Google Compute Engine, Azure VMs
- **Cas d'utilisation**: Migrations lift-and-shift, environnements de développement, besoins de contrôle élevé

#### Platform as a Service (PaaS)
- **Fournit**: Plateformes de développement, bases de données, middleware
- **Exemples**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Cas d'utilisation**: Développement d'applications, déploiement d'API, microservices

#### Software as a Service (SaaS)
- **Fournit**: Applications complètes via Internet
- **Exemples**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Cas d'utilisation**: Messagerie, CRM, collaboration, applications d'entreprise

#### Function as a Service (FaaS) / Serverless
- **Fournit**: Exécution de fonctions pilotée par les événements
- **Exemples**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Cas d'utilisation**: Traitement d'événements, API, tâches planifiées, traitement en temps réel

## Principaux Fournisseurs de Cloud

### Amazon Web Services (AWS)
- **Part de marché**: ~32% (plus grand fournisseur)
- **Services clés**:
  - Calcul: EC2, Lambda, ECS, EKS
  - Stockage: S3, EBS, Glacier
  - Bases de données: RDS, DynamoDB, Aurora
  - Réseau: VPC, Route 53, CloudFront
  - IA/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Part de marché**: ~23%
- **Points forts**: Intégration entreprise, cloud hybride, écosystème Microsoft
- **Services clés**:
  - Calcul: Virtual Machines, Azure Functions, AKS
  - Stockage: Blob Storage, Disk Storage
  - Bases de données: SQL Database, Cosmos DB
  - Réseau: Virtual Network, Traffic Manager
  - IA/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Part de marché**: ~10%
- **Points forts**: Analytique de données, IA/ML, Kubernetes
- **Services clés**:
  - Calcul: Compute Engine, Cloud Functions, GKE
  - Stockage: Cloud Storage, Persistent Disk
  - Bases de données: Cloud SQL, Firestore, Bigtable
  - Analytique: BigQuery, Dataflow, Pub/Sub
  - IA/ML: Vertex AI, AutoML

### Autres Fournisseurs
- **IBM Cloud**: Concentration entreprise, Watson AI
- **Oracle Cloud**: Charges de travail de base de données, applications d'entreprise
- **Alibaba Cloud**: Dominant en Asie-Pacifique
- **DigitalOcean**: Convivial pour les développeurs, offres simplifiées

## Modèles d'Architecture Cloud

### Principes du Cadre Well-Architected

#### Excellence Opérationnelle
- Automatiser les opérations
- Apporter des changements fréquents et réversibles
- Affiner continuellement les procédures
- Anticiper les défaillances

#### Sécurité
- Mettre en œuvre une base d'identité forte
- Activer la traçabilité
- Appliquer la sécurité à toutes les couches
- Automatiser les meilleures pratiques de sécurité
- Protéger les données en transit et au repos

#### Fiabilité
- Tester les procédures de récupération
- Récupérer automatiquement après une défaillance
- Mise à l'échelle horizontale pour la disponibilité
- Arrêter de deviner la capacité
- Gérer le changement dans l'automatisation

#### Efficacité des Performances
- Démocratiser les technologies avancées
- Aller à l'échelle mondiale en quelques minutes
- Utiliser des architectures serverless
- Expérimenter plus souvent
- Considérer la sympathie mécanique (compréhension du matériel sous-jacent)

#### Optimisation des Coûts
- Adopter un modèle de consommation
- Mesurer l'efficacité globale
- Arrêter de dépenser de l'argent pour un travail non différencié
- Analyser et attribuer les dépenses
- Utiliser des services gérés

### Modèles d'Architecture Courants

#### Architecture Microservices
- Décomposer les applications en petits services indépendants
- Chaque service possède ses données et sa logique
- Communiquer via des API (REST, gRPC, messagerie)
- Déployer indépendamment
- **Avantages**: Évolutivité, isolation des pannes, diversité technologique
- **Défis**: Complexité distribuée, cohérence des données, surveillance

#### Architecture Pilotée par les Événements
- Les composants communiquent via des événements
- Les producteurs émettent des événements, les consommateurs réagissent
- **Modèles**: Event sourcing, CQRS, pub/sub
- **Technologies**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Avantages**: Couplage lâche, évolutivité, traitement en temps réel

#### Architecture Serverless
- Aucune gestion de serveur requise
- Paiement à l'exécution
- Mise à l'échelle automatique
- **Composants**: Fonctions, API Gateway, services gérés
- **Avantages**: Efficacité des coûts, opérations réduites, déploiement rapide
- **Considérations**: Démarrages à froid, verrouillage fournisseur, limites d'exécution

#### Architecture en Couches (N-Tier)
- Couche de présentation (UI)
- Couche logique application/métier
- Couche d'accès aux données
- Couche de base de données
- **Avantages**: Séparation des préoccupations, maintenabilité
- **Courant**: Applications web à 3 niveaux

#### Architecture Spatiale
- Gérer la haute concurrence avec des données distribuées
- Mémoire virtualisée sur les serveurs
- Les nœuds de traitement s'adaptent indépendamment
- **Cas d'utilisation**: Applications à haut volume et faible latence

## Services de Calcul

### Machines Virtuelles
- **Types**: Usage général, optimisé pour le calcul, optimisé pour la mémoire, GPU
- **Tarification**: À la demande, instances réservées, instances spot
- **Gestion**: Groupes de mise à l'échelle automatique, équilibreurs de charge
- **Meilleures pratiques**: Dimensionnement correct, étiquetage, surveillance, correction

### Conteneurs
- **Docker**: Standard d'exécution de conteneurs
- **Orchestration**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Avantages**: Portabilité, efficacité, cohérence
- **Registre**: ECR, GCR, ACR, Docker Hub

### Fonctions Serverless
- **Modèle d'exécution**: Déclenché par événements, sans état
- **Limites**: Temps d'exécution, mémoire, exécutions simultanées
- **Cas d'utilisation**: API, traitement de fichiers, tâches planifiées, backends IoT
- **Surveillance**: Nombre d'invocations, erreurs, durée, démarrages à froid

## Solutions de Stockage

### Stockage Objet
- **Caractéristiques**: Structure plate, métadonnées, accès HTTP
- **Exemples**: AWS S3, Google Cloud Storage, Azure Blob
- **Cas d'utilisation**: Actifs statiques, sauvegardes, lacs de données, archives
- **Classes de stockage**: Chaud, froid, très froid, archive (coût/accès variable)

### Stockage par Blocs
- **Caractéristiques**: Volumes bruts, attachés aux VM
- **Exemples**: AWS EBS, Google Persistent Disk, Azure Disks
- **Cas d'utilisation**: Bases de données, volumes de démarrage, besoins de performance élevée
- **Types**: SSD, HDD, IOPS provisionnés

### Stockage de Fichiers
- **Caractéristiques**: Systèmes de fichiers partagés, protocoles NFS/SMB
- **Exemples**: AWS EFS, Google Filestore, Azure Files
- **Cas d'utilisation**: Gestion de contenu, configurations partagées, lift-and-shift

### Stockage d'Archive
- **Caractéristiques**: Coût le plus bas, délais de récupération
- **Exemples**: S3 Glacier, Azure Archive Storage
- **Cas d'utilisation**: Conformité, sauvegardes à long terme, données historiques

## Services de Base de Données

### Bases de Données Relationnelles Gérées
- **Services**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Fonctionnalités**: Sauvegardes automatisées, correction, mise à l'échelle, réplication
- **Moteurs**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bases de Données NoSQL
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Clé-Valeur**: DynamoDB, Redis Cache
- **Colonne Large**: Bigtable, Cassandra (géré)
- **Graphe**: Neptune, Cosmos DB (API graphe)

### Entrepôts de Données
- **Services**: Snowflake, Redshift, BigQuery, Synapse
- **Caractéristiques**: Stockage colonnaire, architecture MPP
- **Cas d'utilisation**: Analytique, BI, analyse de données à grande échelle

### Services de Mise en Cache
- **En mémoire**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Cache CDN**: CloudFront, Cloud CDN, Azure CDN
- **Cas d'utilisation**: Stockage de session, cache de requêtes, diffusion de contenu

## Réseau

### Réseaux Virtuels
- **VPC/VNet**: Environnements réseau isolés
- **Sous-réseaux**: Public (face à Internet), privé (interne uniquement)
- **Adressage IP**: Blocs CIDR, IPv4/IPv6
- **Tables de routage**: Contrôler le flux du trafic

### Équilibrage de Charge
- **Types**: Application (L7), réseau (L4), passerelle
- **Fonctionnalités**: Contrôles de santé, terminaison SSL, sessions persistantes
- **Services**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Réseaux de Diffusion de Contenu (CDN)
- **Objectif**: Mettre en cache le contenu aux emplacements périphériques
- **Avantages**: Latence réduite, charge d'origine inférieure, distribution mondiale
- **Services**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Services DNS
- **Fonctions**: Enregistrement de domaine, routage, contrôles de santé
- **Services**: Route 53, Cloud DNS, Azure DNS
- **Politiques de routage**: Simple, pondéré, basé sur la latence, géolocalisation, basculement

### Options de Connectivité
- **Passerelle Internet**: Accès Internet public
- **Passerelle NAT**: Accès sortant au sous-réseau privé
- **VPN**: Tunneaux chiffrés vers les locaux
- **Direct Connect/ExpressRoute**: Connexions privées dédiées
- **VPC Peering**: Connecter des VPC au sein/entre comptes

## Sécurité dans le Cloud

### Modèle de Responsabilité Partagée
- **Responsabilité du fournisseur**: Sécurité du cloud (infrastructure)
- **Responsabilité du client**: Sécurité dans le cloud (données, applications, accès)
- **Varie selon le service**: Plus géré = plus de responsabilité du fournisseur

### Gestion des Identités et des Accès (IAM)
- **Utilisateurs**: Identités individuelles
- **Groupes**: Collections d'utilisateurs
- **Rôles**: Identifiants temporaires pour les services/utilisateurs
- **Stratégies**: Documents JSON définissant les autorisations
- **Principes**: Privilège minimum, séparation des tâches

### Sécurité Réseau
- **Groupes de sécurité**: Pare-feu avec état pour les instances
- **ACL réseau**: Pare-feu sans état pour les sous-réseaux
- **Pare-feu d'Applications Web (WAF)**: Protection contre les exploits web
- **Protection DDoS**: Shield, Cloud Armor, DDoS Protection

### Protection des Données
- **Chiffrement au repos**: KMS, clés gérées par le client
- **Chiffrement en transit**: TLS/SSL, HTTPS
- **Gestion des clés**: HSM, rotation des clés, pistes d'audit
- **Gestion des secrets**: Secrets Manager, Key Vault

### Conformité et Gouvernance
- **Certifications**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Outils**: Application des politiques, rapports de conformité, journaux d'audit
- **Cadres**: Cloud Security Alliance, NIST CSF

## DevOps dans le Cloud

### Services CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Tiers**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, déclaratif, gestion d'état
- **CloudFormation**: Natif AWS, modèles YAML/JSON
- **ARM Templates**: Natif Azure
- **Deployment Manager**: Natif GCP
- **Pulumi**: Infrastructure utilisant des langages de programmation
- **Avantages**: Contrôle de version, reproductibilité, documentation

### Gestion de Configuration
- **Ansible**: Sans agent, playbooks YAML
- **Chef**: Basé sur Ruby, écosystème mature
- **Puppet**: Déclaratif, reporting solide
- **SaltStack**: Rapide, basé sur Python

### Surveillance et Observabilité
- **Métriques**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Journalisation**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Traçage**: X-Ray, Cloud Trace, Application Insights
- **Tableaux de bord**: CloudWatch Dashboards, Cloud Console
- **Alertes**: SNS, alertes Cloud Monitoring, Action Groups

### Orchestration de Conteneurs
- **Kubernetes**: Standard industriel d'orchestration
- **Services gérés**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (gestion du trafic, sécurité)
- **GitOps**: ArgoCD, Flux (déploiements déclaratifs)

## Gestion des Coûts

### Modèles de Tarification
- **Pay-as-you-go**: Payez ce que vous utilisez
- **Instances réservées**: Engagements de 1 à 3 ans, remises importantes
- **Instances spot**: Enchérir pour la capacité inutilisée, peut être interrompu
- **Plans d'économie**: Tarification d'engagement flexible
- **Niveau gratuit**: Utilisation gratuite limitée pour les nouveaux comptes

### Stratégies d'Optimisation des Coûts
- **Dimensionnement correct**: Adapter les types d'instance aux besoins de charge de travail
- **Mise à l'échelle automatique**: Mettre à l'échelle en fonction de la demande
- **Capacité réservée**: S'engager pour des charges de travail stables
- **Utilisation spot**: Utiliser pour des charges de travail tolérantes aux pannes et flexibles
- **Niveaux de stockage**: Déplacer les données peu fréquentes vers des niveaux moins chers
- **Nettoyage**: Supprimer les ressources inutilisées, instantanés, AMI

### Outils de Gestion des Coûts
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Rapports de facturation, Recommender
- **Tiers**: CloudHealth, CloudCheckr, Datadog

## Haute Disponibilité et Reprise d'Activité

### Concepts de Disponibilité
- **Zones de disponibilité**: Centres de données physiquement séparés dans la région
- **Régions**: Zones géographiques avec plusieurs AZ
- **Emplacements périphériques**: Emplacements de cache CDN dans le monde entier

### Stratégies HA
- **Multi-AZ**: Déploiement sur les zones de disponibilité
- **Auto-guérison**: Remplacement automatique des instances défaillantes
- **Équilibrage de charge**: Distribuer le trafic sur les instances saines
- **Réplication de base de données**: Déploiements Multi-AZ, réplicas en lecture

### Stratégies de Reprise d'Activité
- **Sauvegarde et restauration**: Sauvegardes périodiques, restauration si nécessaire (coût le plus bas)
- **Pilot Light**: Éléments principaux en cours d'exécution, mise à l'échelle pendant la catastrophe
- **Standby chaud**: Version réduite toujours en cours d'exécution
- **Multi-site Actif/Actif**: Production complète dans plusieurs régions (coût le plus élevé)

### RTO et RPO
- **Objectif de Temps de Récupération (RTO)**: Temps d'arrêt maximum acceptable
- **Objectif de Point de Récupération (RPO)**: Perte de données maximale acceptable
- **Sélection de stratégie**: Basée sur les exigences métier et le budget

## Tendances Émergentes

### Informatique en Périphérie (Edge Computing)
- Traiter les données plus près de la source
- **Services**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Cas d'utilisation**: IoT, analytique en temps réel, applications à faible latence

### Multi-Cloud et Cloud Hybride
- Éviter le verrouillage fournisseur
- Tirer parti des meilleurs services de leur catégorie
- **Outils**: Terraform, Anthos, Arc, CloudHealth

### Services IA/ML
- Modèles pré-entraînés: Vision, parole, langue
- Entraînement de modèle personnalisé: SageMaker, Vertex AI, Azure ML
- MLOps: Déploiement de modèle, surveillance, gouvernance

### Informatique Quantique
- **Services**: AWS Braket, Azure Quantum
- **Statut**: Stade précoce, expérimental
- **Potentiel**: Cryptographie, optimisation, découverte de médicaments

### Cloud Durable
- Suivi de l'empreinte carbone
- Engagements en matière d'énergies renouvelables
- Utilisation efficace des ressources
- Modèles d'architecture verte
