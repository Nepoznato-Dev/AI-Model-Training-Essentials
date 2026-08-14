<!--
---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Systèmes de bases de données
## Fondamentaux de la base de données
### Qu'est-ce qu'une base de données ?
Une base de données est une collection organisée d'informations structurées stockées électroniquement, conçues pour une récupération, une insertion, une mise à jour et une suppression efficaces des données.
### Systèmes de gestion de bases de données (SGBD)
Logiciel qui interagit avec les utilisateurs finaux, les applications et la base de données elle-même pour capturer et analyser les données. Exemples : MySQL, PostgreSQL, Oracle, MongoDB.
### Concepts clés
- **Schéma** : Structure/organisation de la base de données (tables, champs, relations)
- **Instance** : données réelles stockées à un moment donné
- **Propriétés ACIDE** : Atomicité, Cohérence, Isolation, Durabilité
- **Théorème CAP** : Cohérence, Disponibilité, Tolérance de partition (choisissez 2)
- **Normalisation** : organisation des données pour réduire la redondance
- **Dénormalisation** : ajout de redondance pour améliorer les performances de lecture
## Bases de données relationnelles (SQL)
### Concepts de base
- **Tableaux** : lignes (enregistrements) et colonnes (champs)
- **Clé primaire** : identifiant unique pour chaque ligne
- **Foreign Key** : Référence à la clé primaire dans une autre table
- **Index** : structures de données améliorant la vitesse des requêtes
- **Vues** : tables virtuelles basées sur les résultats de requêtes
- **Procédures stockées** : blocs de code SQL précompilés
- **Déclencheurs** : actions automatiques sur les modifications de données
### Opérations SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Rejoint
- **INNER JOIN** : renvoie les lignes correspondantes des deux tables
- **LEFT JOIN** : toutes les lignes du tableau de gauche, correspondances à droite
- **RIGHT JOIN** : toutes les lignes du tableau de droite, correspondances à gauche
- **FULL OUTER JOIN** : toutes les lignes des deux tables
- **CROSS JOIN** : produit cartésien des deux tables
- **SELF JOIN** : Table jointe à elle-même
### Formulaires de normalisation
- **1NF** : valeurs atomiques, pas de groupes répétitifs
- **2NF** : 1NF + aucune dépendance partielle (tous les attributs non clés dépendent de la clé primaire entière)
- **3NF** : 2NF + pas de dépendances transitives (les attributs non clés ne dépendent pas d'autres attributs non clés)
- **BCNF** : 3NF plus fort, chaque déterminant est une clé candidate
- **4NF** : Aucune dépendance à valeurs multiples
- **5NF** : Aucune dépendance de jointure
### SGBDR populaires
- **PostgreSQL** : fonctionnalités avancées, extensibles, conformes à ACID
- **MySQL** : applications Web largement utilisées et rapides à lire
- **Oracle** : fonctionnalités d'entreprise, évolutivité, coût élevé
- **SQL Server** : écosystème Microsoft, outils intégrés
- **SQLite** : Embarqué, sans serveur, léger
- **MariaDB** : fork MySQL, open-source
## Bases de données NoSQL
### Types de bases de données NoSQL
#### Magasins de documents
- **Structure** : documents de type JSON (BSON)
- **Cas d'utilisation** : gestion de contenu, catalogues, profils utilisateurs
- **Exemples** : MongoDB, CouchDB, DocumentDB
- **Exemple de requête** (MongoDB) :```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Magasins de valeurs-clés
- **Structure** : paires clé-valeur simples
- **Cas d'utilisation** : mise en cache, sessions, paniers d'achat
- **Exemples** : Redis, DynamoDB, Riak
- **Caractéristiques** : Requêtes rapides, simples et limitées
#### Magasins de la famille de colonnes
- **Structure** : Colonnes regroupées en familles
- **Cas d'utilisation** : Big data, analyses, séries chronologiques
- **Exemples** : Cassandra, HBase, ScyllaDB
- **Caractéristiques** : optimisé pour l'écriture, distribué, évolutif
#### Bases de données graphiques
- **Structure** : Nœuds, arêtes, propriétés
- **Use Cases** : Réseaux sociaux, détection de fraude, recommandations
- **Exemples** : Neo4j, Amazon Neptune, ArangoDB
- **Langage de requête** : Cypher (Neo4j), Gremlin
### Quand utiliser NoSQL
- Schéma flexible/évolutif
- Exigences de mise à l'échelle horizontale
- Débit d'écriture élevé
- Données hiérarchiques/imbriquées
- Systèmes distribués
-Applications en temps réel
## Conception de base de données
### Modélisation entité-relation
- **Entités** : Objets/concepts (Client, Produit, Commande)
- **Attributs** : Propriétés des entités (nom, prix, date)
- **Relations** : connexions entre entités (un-à-un, un-à-plusieurs, plusieurs-à-plusieurs)
- **Cardinalité** : Nombre d'instances en relation
### Modèles de conception de schéma
- **Héritage de table unique** : tous les types dans une seule table avec discriminateur de type
- **Héritage des tables de classes** : tables séparées pour la base et les sous-classes
- **Héritage de la table concrète** : table séparée pour chaque classe concrète
- **Tables de jonction** : résolvez les relations plusieurs-à-plusieurs
- **Tables d'audit** : suivez les modifications (created_at, update_at, delete_at)
### Stratégies d'indexation
- **B-Tree** : par défaut, requêtes de plage, tri
- **Hash** : recherches de correspondances exactes
- **Bitmap** : colonnes à faible cardinalité (sexe, statut)
- **Full-Text** : capacités de recherche de texte
- **Spatial** : Données géographiques (SIG)
- **Composite** : plusieurs colonnes combinées
- **Couvrant** : inclut toutes les colonnes nécessaires à la requête
## Optimisation des requêtes
### Plans d'exécution
- Comprendre comment la base de données exécute les requêtes
- Identifier les goulots d'étranglement (analyses complètes des tables, index manquants)
- Outils : EXPLIQUER, EXPLIQUER ANALYSER
### Techniques d'optimisation
- **Utilisation de l'index** : assurez-vous que les requêtes utilisent les index appropriés
- **Réécriture de requêtes** : simplifiez les requêtes complexes
- **Optimisation des jointures** : choisissez les types et l'ordre de jointure corrects
- **Partitionnement** : diviser les grandes tables (plage, hachage, liste)
- **Vues matérialisées** : résultats de requête pré-calculés
- **Mise en cache des requêtes** : stockez les résultats des requêtes fréquentes
### Problèmes de performances courants
- **Problème de requête N+1** : récupération inefficace des données associées
- **Index manquants** : analyses de tables complètes sur de grandes tables
- **Sur-indexation** : écritures lentes en raison d'un trop grand nombre d'index
- **Lock Contention** : transactions en attente de verrous
- **Requêtes inefficaces** : SELECT *, jointures inutiles
## Transactions et concurrence
### Niveaux d'isolement des transactions
- **READ UNCOMMITTED** : isolement le plus bas, lectures sales possibles
- **READ COMMITTED** : Seules les données validées sont visibles (par défaut dans la plupart des bases de données)
- **LECTURE RÉPÉTABLE** : la même requête renvoie les mêmes résultats dans la transaction
- **SERIALIZABLE** : isolation la plus élevée, les transactions s'exécutent de manière séquentielle
### Contrôle de concurrence
- **Verrouillage pessimiste** : verrouillez les ressources avant l'accès
- **Verrouillage optimiste** : Vérifiez la version avant de valider
- **MVCC (Multi-Version Concurrency Control)** : conserver plusieurs versions de lignes
- **Verrouillage au niveau des lignes** : verrouillez des lignes spécifiques
- **Verrouillage au niveau de la table** : verrouille la table entière
### Impasses
- Dépendance circulaire où les transactions s'attendent
- Prévention : ordre cohérent des verrous, délais d'attente, détection des interblocages
- Résolution : Abandonner une transaction
## Réplication et mise à l'échelle
### Types de réplication
- **Maître-Esclave** : un réplica principal et plusieurs réplicas en lecture
- **Master-Master** : Primaires multiples, réplication bidirectionnelle
- **Multi-Master** : N primaires, résolution de conflit nécessaire
- **Réplication en chaîne** : réplication séquentielle via des nœuds
### Approches de mise à l'échelle
- **Vertical Scaling** : augmentez les ressources du serveur (CPU, RAM, stockage)
- **Mise à l'échelle horizontale** : ajoutez plus de serveurs (sharding, partitionnement)
- **Répliques en lecture** : décharger le trafic de lecture
- **Partage** : divisez les données entre les serveurs par clé/plage/hachage
- **Fédération** : Répartition par fonction/service
### Modèles de cohérence
- **Forte cohérence** : tous les nœuds voient les mêmes données en même temps
- **Cohérence éventuelle** : les nœuds convergent au fil du temps
- **Cohérence causale** : relations de cause à effet préservées
- **Read-Your-Writes** : l'utilisateur voit immédiatement ses propres mises à jour
## Sauvegarde et récupération
### Stratégies de sauvegarde
- **Sauvegarde complète** : copie complète de la base de données
- **Sauvegarde incrémentielle** : modifications depuis la dernière sauvegarde
- **Sauvegarde différentielle** : modifications depuis la dernière sauvegarde complète
- **Récupération ponctuelle** : restauration à un moment spécifique
- **Sauvegarde continue** : réplication en temps réel vers la sauvegarde
### Procédures de récupération
- **RTO (Recovery Time Objective)** : temps d'arrêt maximum acceptable
- **RPO (Recovery Point Objective)** : perte de données maximale acceptable
- **Plan de reprise après sinistre** : procédures documentées en cas de panne
- **Tests** : exercices de récupération réguliers
## Sécurité
### Contrôle d'accès
- **Authentification** : vérifier l'identité de l'utilisateur
- **Autorisation** : Accorder des autorisations (GRANT, REVOKE)
- **Rôles** : autorisations de groupe pour une gestion plus facile
- **Principe du moindre privilège** : accès minimum nécessaire
### Protection des données
- **Chiffrement au repos** : chiffrer les données stockées
- **Chiffrement en transit** : TLS/SSL pour les connexions
- **Masquage** : masquer les données sensibles en dehors de la production
- **Tokenisation** : remplacez les données sensibles par des jetons
### Vulnérabilités courantes
- **Injection SQL** : SQL malveillant dans la saisie utilisateur
- **Élévation de privilèges** : obtention d'un accès non autorisé
- **Journalisation d'audit** : suivez toutes les activités de la base de données
- **Conformité** : exigences RGPD, HIPAA, PCI-DSS
## Technologies de bases de données modernes
### Bases de données cloud
- **AWS** : RDS, Aurora, DynamoDB, Redshift
- **Google Cloud** : Cloud SQL, Spanner, Bigtable, Firestore
- **Azure** : base de données SQL, Cosmos DB, Synapse
- **Avantages** : service géré, mise à l'échelle automatique, sauvegardes incluses
### Nouvelles bases de données SQL
- Combinez la cohérence SQL avec l'évolutivité NoSQL
- **Exemples** : CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Caractéristiques** : transactions distribuées, ACID, mise à l'échelle horizontale
### Bases de données de séries chronologiques
- Optimisé pour les données horodatées
- **Exemples** : InfluxDB, TimescaleDB, Prometheus
- **Cas d'utilisation** : IoT, surveillance, données financières
### Bases de données vectorielles
- Stocker et interroger les vecteurs d'intégration
- **Exemples** : Pinecone, Milvus, Weaviate, Qdrant
- **Cas d'utilisation** : recherche sémantique, systèmes de recommandation, applications d'IA
### Bases de données multimodèles
- Prise en charge de plusieurs modèles de données dans un seul système
- **Exemples** : ArangoDB, OrientDB, Azure Cosmos DB
- **Avantage** : Flexibilité sans plusieurs bases de données
## ORM et accès aux données
### Mappage objet-relationnel
- **Objectif** : mapper les tables de base de données aux objets de programmation
- **ORM populaires** :
  - Python : SQLAlchemy, Django ORM, Peewee
  - JavaScript : Sequelize, Prisma, TypeORM
  - Java : Mise en veille prolongée, JPA
  - Ruby : ActiveRecord
  - .NET : Entity Framework
### Avantages
- Abstraction de SQL
- Tapez la sécurité
- Gestion des migrations
- API de création de requêtes
### Inconvénients
- Frais généraux de performances
- Requêtes complexes plus difficiles à écrire
- Problèmes de requêtes N+1
- Courbe d'apprentissage
##Administration de la base de données
### Responsabilités de l'administrateur de base de données
-Installation et configuration
- Optimisation des performances
- Sauvegarde et récupération
- Gestion de la sécurité
- Planification des capacités
- Surveillance et alerte
- Gestion des correctifs
### Métriques de surveillance
- Temps de réponse aux requêtes
- Débit (transactions par seconde)
- Nombre de connexions
- Taux de réussite du cache
- E/S disque
- Verrouiller le temps d'attente
- Retard de réplication
### Tâches de maintenance
- **Vacuum/Analyze** : Mettre à jour les statistiques, récupérer de l'espace
- **Reconstruction d'index** : défragmenter les index
- **Mises à jour des statistiques** : Tenez l'optimiseur de requêtes informé
- **Rotation des journaux** : gérer la taille des fichiers journaux
- **Planification des capacités** : prédire la croissance et planifier les mises à niveau