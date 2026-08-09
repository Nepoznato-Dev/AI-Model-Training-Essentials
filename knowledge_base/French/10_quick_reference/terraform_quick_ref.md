---
# Métadonnées
titre : "Terraform et Infrastructure as Code"
description : "Concepts IaC, commandes Terraform, gestion des états, modules"
catégorie : "Référence rapide"
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
review_by : "Équipe de base de connaissances de référence rapide"
next_review : "2027-08-05"
#Classement
balises : [terraform, référence rapide]
niveau de difficulté : "débutant"
prérequis : []
estimate_reading_time : "6 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Terraform et infrastructure en tant que code
Terraform est l'outil Infrastructure as Code (IaC) le plus largement utilisé : il vous permet de définir l'infrastructure cloud (serveurs, bases de données, réseaux, autorisations) dans des fichiers de configuration déclaratifs qui peuvent être versionnés, révisés, testés et automatisés. Au lieu de cliquer sur une console cloud, vous écrivez du code qui décrit l'état souhaité de votre infrastructure, et Terraform détermine les modifications à apporter.
---

## Concepts de base
| Concepts | Descriptif |
|---------|-------------|
| **Fournisseur** | Plugin qui gère une plateforme cloud spécifique (AWS, Azure, GCP, etc.) |
| **Ressource** | Un objet d'infrastructure (serveur, base de données, réseau) |
| **État** | L'enregistrement Terraform de l'infrastructure existante ; stocké dans un fichier d'état |
| **Plan** | Aperçu des changements que Terraform apportera |
| **Postuler** | Exécuter le plan ; créer/mettre à jour/détruire l'infrastructure |
| **Module** | Collection de ressources réutilisables |
| **Variable** | Paramètre d'entrée pour les configurations |
| **Sortie** | Valeur exportée depuis un module ou une configuration |
| **Source de données** | Lire les informations de l'infrastructure existante |
---

## Flux de travail de base
| Étape | Commande | Descriptif |
|------|---------|-------------|
| **1. Écrire la configuration** | Créer des fichiers`.tf`| Définir les fournisseurs, les ressources, les variables |
| **2. Initialiser** | `terraform init`| Fournisseurs de téléchargement ; configurer le back-end |
| **3. Format** | `terraform fmt`| Standardiser le formatage |
| **4. Valider** | `terraform validate`| Vérifier la syntaxe et la configuration |
| **5. Forfait** | `terraform plan`| Aperçu des modifications (essai à sec) |
| **6. Postuler** | `terraform apply`| Créer ou mettre à jour une infrastructure |
| **7. Détruire** | `terraform destroy`| Démolir toutes les infrastructures gérées |
---

## Commandes communes
| Commande | Descriptif |
|---------|-------------|
| `terraform init`| Initialiser le répertoire de travail ; fournisseurs et modules de téléchargement |
| `terraform plan`| Montrer les modifications qui seront apportées |
| `terraform apply`| Appliquer les modifications ; ajoutez`-auto-approve`pour ignorer la confirmation |
| `terraform destroy`| Détruire toutes les ressources gérées |
| `terraform fmt`| Formater les fichiers de configuration au style standard |
| `terraform validate`| Valider la syntaxe de configuration |
| `terraform output`| Afficher les valeurs de sortie |
| `terraform state list`| Répertorier toutes les ressources dans l'état |
| `terraform state show <resource>`| Afficher les détails d'une ressource spécifique |
| `terraform import <resource> <id>`| Importer les infrastructures existantes dans l'État |
| `terraform taint <resource>`| Marquer une ressource pour les loisirs lors de la prochaine candidature |
| `terraform refresh`| Mettre à jour l'état pour correspondre à l'infrastructure réelle |
| `terraform graph`| Générer un graphique de dépendance visuel (format DOT) |
| `terraform console`| Console interactive pour tester les expressions |
---

## Gestion de l'état
| Meilleure pratique | Descriptif |
|--------------|-------------|
| **État distant** | Stocker l'état dans S3, GCS, Azure Blob ou Terraform Cloud – jamais localement |
| **Verrouillage d'état** | Utilisez DynamoDB (backend S3) ou le verrouillage natif pour empêcher les modifications simultanées |
| **Cryptage d'état** | Activer le chiffrement au repos pour les fichiers d'état (ils contiennent des données sensibles) |
| **Séparation d'État** | Utiliser des fichiers d'état distincts pour différents environnements ou équipes |
| **Sauvegarde d'état** | État de version automatique des backends distants ; garder ceci activé |
| **Ne modifiez jamais l'état manuellement** | Utilisez plutôt`terraform state mv`,`rm`,`import`|
---

## Structure des modules
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Types de variables
| Tapez | Exemple | Cas d'utilisation |
|------|---------|--------------|
| **chaîne** | `variable "region" { type = string }`| Valeur de texte unique |
| **numéro** | `variable "count" { type = number }`| Valeur numérique |
| **bool** | `variable "enable" { type = bool }`| Drapeau vrai/faux |
| **liste** | `variable "zones" { type = list(string) }`| Collecte commandée |
| **carte** | `variable "tags" { type = map(string) }`| Paires clé-valeur |
| **objet** | `variable "config" { type = object({...}) }`| Configuration structurée |
---

## Modèles courants
| Modèle | Descriptif |
|---------|-------------|
| **Comte** | `count = 3`crée plusieurs instances d'une ressource |
| **Pour chacun** | `for_each = var.items`itère sur une carte ou un ensemble |
| **Blocs dynamiques** | Générer des blocs imbriqués répétés (par exemple, règles d'entrée) |
| **Valeurs locales** | `locals { ... }`pour les valeurs calculées et réduisant les répétitions |
| **Sources de données** | Lire l'infrastructure existante (par exemple, rechercher un VPC existant) |
| **Fournisseurs** | Exécuter des scripts sur les ressources après la création (à utiliser avec parcimonie) |
| **Espaces de travail** | État séparé pour différents environnements au sein de la même configuration |
---

## Dépannage
| Problème | Solutions |
|---------|----------|
| **Dérive de l'état** | Exécutez`terraform plan`pour voir les différences ; `terraform apply`pour réconcilier |
| **État verrouillé** | Vérifiez qui a la serrure ; utilisez`terraform force-unlock`si cela est sûr |
| **Erreurs du fournisseur** | Vérifiez les informations d'identification ; mettre à jour la version du fournisseur ; vérifier les limites de l'API |
| **Conflits d'importation** | Ressource déjà en état ; utiliser`terraform state rm`en premier |
| **Dépendances circulaires** | Restructurer les ressources ; utilisez`depends_on`avec précaution |
| **Grand État** | Divisé en modules ; utiliser`-target`pour les opérations partielles |
---

## Résumé
Terraform gère l'infrastructure via des fichiers de configuration déclaratifs. Le flux de travail est le suivant : écrire la configuration → init → plan → appliquer. L'état suit ce qui existe et doit être stocké à distance avec verrouillage. Les modules permettent la réutilisation. Les variables paramétrent les configurations. Les principes clés sont les suivants : traiter l'infrastructure comme du code (contrôle de version ; révision ; test) ; ne modifiez jamais l'état manuellement ; planifier avant de postuler ; utiliser l'état distant avec verrouillage ; et des configurations de structure avec des modules pour la maintenabilité.