---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
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

# Ingénierie des données et pipelines
L'ingénierie des données est la discipline qui consiste à créer des systèmes qui déplacent, transforment et stockent des données à grande échelle. Sans pipelines de données fiables, les modèles d'apprentissage automatique ne peuvent pas être formés, les tableaux de bord affichent des chiffres obsolètes et les décisions commerciales sont basées sur des conjectures. Ce fichier couvre l'architecture, les outils et les pratiques permettant de créer une infrastructure de données qui fonctionne.
---

## ETL contre ELT
| Approche | Comment ça marche | Idéal pour | Outils |
|--------------|-------------|--------------|-------|
| **ETL** (Extraire → Transformer → Charger) | Transformer les données *avant* le chargement dans l'entrepôt | Entrepôts traditionnels avec calcul limité | Informatica, Talend, Apache NiFi |
| **ELT** (Extraire → Charger → Transformer) | Chargez d'abord les données brutes ; transformer *à l'intérieur* de l'entrepôt | Entrepôts cloud modernes avec calcul élastique | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
Le passage de l'ETL à l'ELT a été motivé par les entrepôts de données cloud (BigQuery, Snowflake, Redshift) qui peuvent faire évoluer le calcul indépendamment du stockage. Il n'est plus nécessaire de tout prétraiter avant le chargement.
---

## Lacs de données vs entrepôts de données
| Fonctionnalité | Lac de données | Entrepôt de données |
|--------------|-----------|---------------|
| **Format des données** | Format brut natif (schéma à la lecture) | Structuré, traité (schéma sur écriture) |
| **Schéma** | Défini au moment de la requête | Défini avant le chargement |
| **Types de données** | Structuré, semi-structuré, non structuré | Principalement structuré |
| **Utilisateurs** | Data scientists, ingénieurs | Analystes d'affaires, outils BI |
| **Coût** | Stockage moins cher (stockage objet) | Plus cher (optimisé pour les requêtes) |
| **Exemples** | AWS S3, Azure Data Lake, GCS | Flocon de neige, BigQuery, Redshift |
L'approche moderne est le **lakehouse** : combinez le stockage flexible et bon marché d'un lac avec les fonctionnalités de gestion et de performance d'un entrepôt. Delta Lake, Apache Iceberg et Apache Hudi sont les technologies clés ici.
---

## Architecture des pipelines
### Lot ou streaming
| Mode | Descriptif | Latence | Cas d'utilisation |
|------|-------------|---------|--------------|
| **Lot** | Traiter les données en gros morceaux à intervalles planifiés | Minutes en heures | Rapports quotidiens, tâches ETL, enrichissement des données |
| **Diffusion** | Traiter les données en continu dès leur arrivée | Millisecondes en secondes | Tableaux de bord en temps réel, détection de fraude, alertes |
| **Micro-lot** | Petits lots à intervalles très courts | Secondes | Temps quasi réel avec simplicité par lots |
### Composants du pipeline
Un pipeline de données typique comporte ces étapes :
| Scène | Descriptif | Outils |
|-------|-------------|-------|
| **Ingestion** | Recueillir des données à partir de sources | Kafka, Airbyte, Fivetran, Debezium |
| **Transformation** | Nettoyer, enrichir, agréger | dbt, Spark, Pandas |
| **Stockage** | Conserver les données traitées | BigQuery, flocon de neige, S3, Delta Lake |
| **Servir** | Mettre les données à disposition des consommateurs | API, tableaux de bord, magasins de fonctionnalités ML |
| **Orchestration** | Planifier et gérer les dépendances | Flux d'air, préfet, Dagster |
| **Surveillance** | Suivre l’état du pipeline et la qualité des données | Grandes attentes, Monte Carlo, alertes personnalisées |
---

## Outils d'orchestration
| Outil | Approche | Force |
|------|----------|--------------|
| **Apache Airflow** | DAG basés sur Python ; norme de l'industrie | Immense écosystème, mature, flexible |
| **Préfet** | Natif Python ; API plus propre qu'Airflow | Design moderne, excellente gestion des erreurs |
| **Dague** | Centré sur les actifs ; approche du génie logiciel | Système de types, tests, observabilité |
| **Luigi** | L'outil de pipeline original de Spotify | Simple, mais moins activement développé |
### Exemple de flux d'air
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

##ApacheKafka
Kafka est l'épine dorsale de nombreux systèmes de données en temps réel. Il s'agit d'un journal d'événements distribué qui fournit une messagerie à haut débit et tolérante aux pannes.
### Concepts de base
| Concepts | Descriptif |
|---------|-------------|
| **Sujet** | Une catégorie de messages (par exemple,`orders`,`user-events`) |
| **Partition** | Les sujets sont divisés en partitions pour le parallélisme |
| **Producteur** | Application qui écrit des messages dans des sujets |
| **Consommateur** | Application qui lit les messages des sujets |
| **Groupe de consommateurs** | Groupe de consommateurs qui partagent la charge de lire un sujet |
| **Décalage** | Position d'un consommateur au sein d'une partition |
| **Courtier** | Un nœud de serveur Kafka |
### Quand utiliser Kafka
- **Diffusion d'événements** : traitement des événements en temps réel à grande échelle.
- **Services de découplage** : les producteurs et les consommateurs n'ont pas besoin de se connaître.
- **Replay** : les messages sont conservés ; les consommateurs peuvent relire à partir de n’importe quel décalage.
- **Contre-pression** : Kafka gère naturellement les différences de vitesse entre les producteurs et les consommateurs.
---

## Modélisation des données
### Schéma en étoile vs schéma en flocon de neige
| Schéma | Structure | Avantages | Inconvénients |
|--------|-----------|------|------|
| **Étoile** | Table de faits centrale entourée de tables de dimensions dénormalisées | Requêtes simples, lectures rapides | Redondance des données |
| **Flocon de neige** | Les tableaux de dimensions sont normalisés (divisés en sous-tableaux) | Moins de redondance | Plus de jointures, des requêtes plus lentes |
### Tableaux de faits et de dimensions
| Type de tableau | Contient | Exemple |
|-----------|----------|---------|
| **Fait** | Événements mesurables (métriques) | `orders`(order_id, product_id, customer_id, montant, date) |
| **Dimensions** | Attributs descriptifs | `products`(product_id, nom, catégorie, prix),`customers`(customer_id, nom, ville) |
---

## Magasins de fonctionnalités
Un magasin de fonctionnalités est un référentiel centralisé de fonctionnalités ML — les valeurs dérivées utilisées comme entrée dans les modèles (par exemple, « valeur moyenne des commandes de l'utilisateur au cours des 30 derniers jours »).
| Capacité | Descriptif |
|---------------|-------------|
| **Registre des fonctionnalités** | Catalogue des fonctionnalités disponibles avec métadonnées |
| **Boutique hors ligne** | Fonctionnalités historiques pour la formation de modèles (batch) |
| **Boutique en ligne** | Fonctionnalité à faible latence servant à l'inférence en temps réel |
| **Surveillance des fonctionnalités** | Détecter les dérives, les valeurs manquantes, les changements de distribution |
| Outil | Descriptif |
|------|-------------|
| **Fête** | Source ouverte ; fonctionne avec n'importe quel framework ML |
| **Tecton** | Commercial; plateforme de fonctionnalités en temps réel |
| **Hopsworks** | Source ouverte ; plateforme ML complète avec magasin de fonctionnalités |
| **Magasin de fonctionnalités Databricks** | Intégré à Databricks/Spark |
---

## Qualité des données
La qualité des données est le tueur silencieux des projets ML. Déchets entrants, déchets sortants.
### Dimensions de la qualité
| Dimensions | Question |
|-----------|----------|
| **Précision** | Les données reflètent-elles la réalité ? |
| **Exhaustivité** | Les champs obligatoires sont-ils renseignés ? |
| **Cohérence** | Les valeurs concordent-elles entre les sources ? |
| **Rapidité** | Les données sont-elles à jour ? |
| **Validité** | Les valeurs sont-elles conformes aux règles définies ? |
| **Unicité** | Y a-t-il des enregistrements en double ? |
### Outils de qualité des données
| Outil | Approche |
|------|----------|
| **Grandes attentes** | Basé sur Python ; définir les « attentes » concernant les données |
| **Monte-Carlo** | Plateforme d'observabilité des données basée sur le ML |
| **tests de dbt** | Tests intégrés pour les données d'entrepôt (uniques, not_null, relations) |
| **Soude** | Analyse de la qualité des données open source |
---

## Gouvernance des données
La gouvernance des données garantit que les données sont gérées de manière responsable dans l’ensemble de l’organisation.
| Zone | Descriptif |
|------|-------------|
| **Catalogue de données** | Inventaire consultable d'ensembles de données avec métadonnées (Amundsen, DataHub, Atlan) |
| **Lignée des données** | Suivez l'origine des données et comment elles se transforment |
| **Contrôle d'accès** | Autorisations basées sur les rôles ; qui sait lire/écrire quoi |
| **Conformité** | Adhésion au RGPD, au CCPA et à la HIPAA |
| **Propriété des données** | Propriété claire pour chaque ensemble de données (intendance) |
| **Politiques de rétention** | Définir la durée de conservation des données et le moment où elles sont supprimées |
---

## La pile de données moderne
La « pile de données moderne » fait référence à la combinaison typique d'outils utilisés par les équipes de données aujourd'hui :
| Couche | Outils typiques |
|-------|--------------|
| **Ingestion** | Fivetran, Airbyte |
| **Entrepôt** | Flocon de neige, BigQuery, Redshift |
| **Transformation** | dette |
| **Orchestration** | Flux d'air, préfet, Dagster |
| **BI / Visualisation** | Looker, métabase, Tableau |
| **ETL inversé** | Recensement, Hightouch (synchroniser les données de l'entrepôt avec les outils) |
| **Qualité des données** | De grandes attentes, Monte Carlo |
La tendance est aux outils modulaires de pointe, connectés par des standards ouverts (SQL, modèles dbt, DAG Airflow) plutôt que par des plates-formes monolithiques.