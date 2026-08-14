---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
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
tags: [cloud, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#Architecture cloud
Le cloud computing a fondamentalement changé la façon dont les organisations créent, déploient et font évoluer leurs logiciels. Au lieu d'acheter et d'entretenir des serveurs physiques, vous pouvez provisionner des ressources informatiques à la demande, payer pour ce que vous utilisez et évoluer à l'échelle mondiale en quelques minutes. Ce fichier couvre les concepts de base, les modèles d'architecture, les services et les meilleures pratiques que vous devez connaître.
---

## Fondamentaux du cloud computing
### Qu'est-ce que le Cloud Computing ?
Livraison à la demande de ressources informatiques (serveurs, stockage, bases de données, réseaux, logiciels) sur Internet avec une tarification à l'utilisation.
### Caractéristiques essentielles du NIST
| Caractéristique | Signification |
|---------------|---------|
| **Libre-service à la demande** | Provisionner des ressources sans interaction humaine |
| **Large accès au réseau** | Disponible sur le réseau via des mécanismes standards |
| **Mise en commun des ressources** | Modèle multi-locataire ; ressources affectées dynamiquement |
| **Élasticité rapide** | Évoluez rapidement vers l’extérieur et l’intérieur |
| **Service mesuré** | L'utilisation est surveillée et facturée |
### Modèles de déploiement
| Modèle | Descriptif | Quand utiliser |
|-------|-------------|-------------|
| **Cloud public** | Propriété des fournisseurs ; infrastructure partagée (AWS, Azure, GCP) | La plupart des charges de travail ; rentable |
| **Cloud privé** | Dédié à une seule organisation | Exigences réglementaires, données sensibles |
| **Cloud hybride** | Combinaison du public et du privé | Flexibilité + conformité |
| **Multi-Cloud** | Utiliser plusieurs fournisseurs de cloud public | Évitez la dépendance vis-à-vis d'un fournisseur, le meilleur de sa catégorie |
### Modèles de services
| Modèle | Fournit | Exemples | Cas d'utilisation |
|-------|----------|--------------|---------------|
| **IaaS** | VM, stockage, réseaux, OS | AWS EC2, machines virtuelles Azure, GCP Compute Engine | Migrations lift-and-shift, contrôle total |
| **PaaS** | Plateformes de développement, bases de données, middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | Développement d'applications, déploiement d'API |
| **SaaS** | Candidatures complètes sur Internet | Salesforce, Google Workspace, Microsoft 365 | E-mail, CRM, collaboration |
| **FaaS / Sans serveur** | Exécution de fonctions pilotées par événements | AWS Lambda, Azure Functions, GCP Cloud Functions | API, traitement des événements, tâches planifiées |
---

## Principaux fournisseurs de cloud
| Fournisseur | Part de marché | Points forts |
|--------------|-------------|---------------|
| **AWS** | ~32% | Le plus grand catalogue de services, le plus grand écosystème |
| **Azur** | ~23% | Intégration d'entreprise, cloud hybride, pile Microsoft |
| **GCP** | ~10% | Analyse de données, IA/ML, Kubernetes |
| **Alibaba Nuage** | ~4% | Dominant en Asie-Pacifique |
| **Oracle Cloud** | ~2% | Charges de travail de base de données, applications d'entreprise |
| **IBM-Cloud** | ~2% | Orientation entreprise, Watson AI |
| **Océan numérique** | Niche | Offres simplifiées et conviviales pour les développeurs |
### Comparaison de services (3 meilleurs fournisseurs)
| Catégorie | AWS | Azur | GCP |
|----------|-----|-------|-----|
| **Calcul** | EC2, Lambda, ECS | VM, fonctions, AKS | Compute Engine, fonctions Cloud, GKE |
| **Stockage** | S3, EBS, Glacier | Stockage Blob, stockage sur disque | Stockage cloud, disque persistant |
| **Base de données** | RDS, DynamoDB, Aurore | Base de données SQL, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Analyses** | Redshift, DME | Synapse, Databricks | BigQuery, flux de données |
| **IA/ML** | SageMaker, reconnaissance | Azure ML, services cognitifs | Vertex AI, AutoML |
| **Réseau** | VPC, Route 53, CloudFront | Réseau virtuel, gestionnaire de trafic | VPC, Cloud DNS, Cloud CDN |
---

## Modèles d'architecture
### Cadre bien architecturé
Les trois principaux fournisseurs publient des frameworks bien architecturés, construits autour de cinq piliers :
| Pilier | Principes clés |
|--------|---------------|
| **Excellence opérationnelle** | Automatiser les opérations ; apporter des changements fréquents et réversibles ; anticiper l'échec |
| **Sécurité** | Fondement identitaire solide ; appliquer la sécurité à chaque couche ; protéger les données en transit et au repos |
| **Fiabilité** | Procédures de récupération des tests ; récupération automatique après un échec ; échelle horizontale |
| **Efficacité des performances** | Utilisez le sans serveur ; devenez mondial en quelques minutes ; expérimenter souvent |
| **Optimisation des coûts** | Adopter un modèle de consommation ; utiliser des services gérés ; arrêter de dépenser pour un travail indifférencié |
### Modèles courants
| Modèle | Descriptif | Avantages | Défis |
|---------|-------------|--------------|------------|
| **Microservices** | Décomposer l'application en petits services indépendants | Évolutivité, isolation des pannes, déploiement indépendant | Complexité distribuée, cohérence des données |
| ** Basé sur les événements ** | Les composants communiquent via des événements | Couplage lâche, traitement en temps réel | Complexité du débogage, cohérence éventuelle |
| **Sans serveur** | Aucune gestion de serveur ; paiement par exécution | Rentabilité, déploiement rapide | Démarrages à froid, verrouillage du fournisseur, limites d'exécution |
| **En couches (N-Tier)** | Présentation → Logique métier → Accès aux données → Base de données | Séparation des préoccupations, maintenabilité | Peut devenir monolithique |
| **Basé sur l'espace** | Données distribuées sur des nœuds de mémoire virtualisés | Gère une concurrence élevée et une faible latence | Complexe à concevoir et à gérer |
---

## Services de base
### Calculer
| Type de service | Détails |
|-------------|---------|
| **Machines virtuelles** | GPU à usage général, optimisé pour le calcul et la mémoire. Tarification : sur demande, réservé, spot. |
| **Conteneurs** | Exécution Docker ; orchestration via Kubernetes (EKS, AKS, GKE). Registres : ECR, GCR, ACR. |
| **Fonctions sans serveur** | Déclenché par un événement, sans état. Limites de temps d'exécution, de mémoire et de concurrence. |
### Stockage
| Tapez | Caractéristiques | Exemples | Idéal pour |
|------|----------------|----------|--------------|
| **Objet** | Structure plate, accès HTTP, riche en métadonnées | S3, stockage cloud, Azure Blob | Actifs statiques, sauvegardes, lacs de données |
| **Bloquer** | Volumes bruts attachés aux VM | EBS, disque persistant, disques Azure | Bases de données, volumes de démarrage |
| **Fichier** | Systèmes de fichiers partagés (NFS/SMB) | EFS, magasin de fichiers, fichiers Azure | Gestion de contenu, configurations partagées |
| **Archiver** | Coût le plus bas, délais de récupération | S3 Glacier, Archives Azure | Conformité, sauvegardes à long terme |
### Bases de données
| Catégorie | Prestations | Cas d'utilisation |
|----------|----------|---------------|
| **Relationnel Géré** | RDS, Cloud SQL, Azure SQL | Applications traditionnelles, transactions ACID |
| **NoSQL — Document** | DocumentDB, Firestore, Cosmos DB | Schémas flexibles, données JSON |
| **NoSQL — Valeur-clé** | DynamoDB, cache Redis | Mise en cache, sessions, recherches simples |
| **NoSQL — Colonnes larges** | Bigtable, Cassandre | Séries chronologiques à forte écriture |
| **NoSQL — Graphique** | Neptune, Cosmos DB (API Graph) | Relations, réseaux sociaux |
| **Entreposage de données** | Flocon de neige, Redshift, BigQuery, Synapse | Analyse, BI |
| **Mise en cache** | ElastiCache, Cloud Memorystore | Stockage de session, mise en cache des requêtes |
---

## Réseautage
### Réseaux virtuels
Chaque déploiement cloud réside dans un cloud privé virtuel (VPC/VNet) : un réseau isolé que vous définissez avec des blocs CIDR, des sous-réseaux (publics ou privés), des tables de routage et des passerelles.
### Équilibrage de charge et CDN
| Services | Objectif |
|---------|---------|
| **Équilibreurs de charge** | Répartir le trafic entre les instances (réseau L4, application L7) |
| **CAN** | Mettre en cache le contenu aux emplacements périphériques pour une latence plus faible (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Enregistrement de domaine, politiques de routage, vérifications de l'état (Route 53, Cloud DNS, Azure DNS) |
### Options de connectivité
| Options | Descriptif |
|--------|-------------|
| **Passerelle Internet** | Accès Internet public pour VPC |
| **Passerelle NAT** | Accès sortant au sous-réseau privé |
| **VPN** | Tunnels chiffrés vers le site |
| **Connexion directe/ExpressRoute** | Connexions privées dédiées |
| **Appairage VPC** | Connecter des VPC au sein ou entre des comptes |
---

## Sécurité
### Modèle de responsabilité partagée
| Couche | Fournisseur | Client |
|-------|----------|--------------|
| **Infrastructure** (matériel, installations) | ✅ | |
| **Calcul, stockage, mise en réseau** | ✅ (géré) | ✅ (autogéré) |
| **Données, Applications, Identité** | | ✅ |
Plus le service est géré, plus le fournisseur en gère. Avec IaaS, vous gérez presque tout ; avec le SaaS, le fournisseur gère presque tout.
### Gestion des identités et des accès (IAM)
| Concepts | Descriptif |
|---------|-------------|
| **Utilisateurs** | Identités individuelles |
| **Groupes** | Collections d'utilisateurs |
| **Rôles** | Identifiants temporaires pour les services ou les utilisateurs |
| **Politiques** | Documents définissant les autorisations |
| **Principe** | Moindre privilège, séparation des tâches |
### Protection des données
- **Chiffrement au repos** : KMS, clés gérées par le client, HSM.
- **Chiffrement en transit** : TLS/SSL, HTTPS.
- **Gestion des secrets** : Secrets Manager, Key Vault — ne codez jamais de secrets en dur.
---

## DevOps dans le cloud
### Infrastructure en tant que code (IaC)
| Outil | Descriptif |
|------|-------------|
| **Terraforme** | Multi-cloud, HCL déclaratif, gestion d'état |
| **CloudFormation** | Modèles YAML/JSON natifs AWS |
| **Modèles BRAS / Biceps** | Azure-natif |
| **Pulumi** | Infrastructure utilisant des langages de programmation (Python, Go, etc.) |
### Services CI/CD
| Fournisseur | Outils |
|--------------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azur** | Azure DevOps, actions GitHub |
| **GCP** | Création de cloud, déploiement de cloud |
| **Tiers** | Jenkins, CircleCI, GitLab CI |
### Surveillance et observabilité
| Capacité | AWS | Azur | GCP |
|-----------|-----|-------|-----|
| **Mesures** | CloudWatch | Moniteur Azure | Surveillance du cloud |
| **Journalisation** | Journaux CloudWatch | Analyse des journaux | Journalisation dans le cloud |
| **Traçage** | Radiographie | Informations sur les applications | Trace de nuage |
---

## Gestion des coûts
### Modèles de tarification
| Modèle | Descriptif | Idéal pour |
|-------|-------------|--------------|
| **À la demande** | Payez ce que vous utilisez, à la seconde/heure | Charges de travail variables à court terme |
| **Instances réservées** | Engagement de 1 à 3 ans, remise importante | Charges de travail en régime permanent |
| **Instances ponctuelles** | Enchérir sur la capacité inutilisée ; peut être interrompu | Des emplois flexibles et tolérants aux pannes |
| **Plans d'épargne** | Tarification d'engagement flexible | Modèles d'utilisation mixtes |
| **Niveau gratuit** | Utilisation gratuite limitée pour les nouveaux comptes | Apprentissage, prototypage |
### Stratégies d'optimisation
Adaptez la taille des instances aux charges de travail. Utilisez la mise à l’échelle automatique pour gérer les pics de demande. Réservez de la capacité pour des charges prévisibles. Utilisez des instances ponctuelles pour les tâches par lots. Déplacez les données rarement consultées vers des niveaux de stockage moins chers. Supprimez les ressources inutilisées (instantanés orphelins, équilibreurs de charge inactifs, adresses IP non connectées).
---

## Haute disponibilité et reprise après sinistre
### Concepts de disponibilité
| Concepts | Descriptif |
|---------|-------------|
| **Zone de disponibilité (AZ)** | Centres de données physiquement séparés au sein d'une région |
| **Région** | Zone géographique avec plusieurs AZ |
| **Emplacement périphérique** | Emplacement du cache CDN pour la diffusion de contenu |
### Stratégies de reprise après sinistre
| Stratégie | Coût | RTO | RPO | Descriptif |
|----------|------|-----|-----|-------------|
| **Sauvegarde et restauration** | Le plus bas | Horaires | Heures-jours | Sauvegardes périodiques, restauration si nécessaire |
| **Voyant lumineux** | Faible | Minutes–heures | Procès-verbal | Éléments de base toujours opérationnels, adaptables en cas de sinistre |
| **Veille chaude** | Moyen | Procès-verbal | Secondes–minutes | Version réduite toujours en cours d'exécution |
| **Multi-site Actif/Actif** | Le plus haut | Proche de zéro | Zéro | Production complète dans plusieurs régions |
**RTO** (Recovery Time Objective) = temps d'arrêt maximum acceptable. **RPO** (Recovery Point Objective) = perte de données maximale acceptable.
---

## Tendances émergentes
| Tendance | Que se passe-t-il |
|-------|-----------------|
| **Informatique de pointe** | Traitement des données au plus près de la source (AWS Outposts, Wavelength, Azure Edge) |
| **Multi-Cloud** | Éviter le verrouillage du fournisseur ; tirer parti des meilleurs fournisseurs |
| **Services IA/ML** | Modèles pré-entraînés (vision, parole, langage) + formation personnalisée (SageMaker, Vertex AI) |
| **Informatique quantique** | Services expérimentaux à un stade précoce (AWS Braket, Azure Quantum) |
| **Cloud durable** | Suivi de l'empreinte carbone, engagements en matière d'énergies renouvelables, architecture verte |