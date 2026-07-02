# Systèmes de bases de données

## Fondamentaux des bases de données

### Qu'est-ce qu'une base de données ?
Une base de données est une collection organisée d'informations structurées stockées électroniquement, conçue pour permettre la récupération, l'insertion, la mise à jour et la suppression efficaces des données.

### Systèmes de gestion de bases de données (DBMS)
Logiciels qui interagissent avec les utilisateurs finaux, les applications et la base de données elle-même afin de capturer et d'analyser les données. Exemples : MySQL, PostgreSQL, Oracle, MongoDB.

### Concepts clés
- **Schema** : Structure/organisation de la base de données (tables, champs, relations)
- **Instance** : Données réellement stockées à un instant donné
- **ACID Properties** : Atomicité, Cohérence, Isolation, Durabilité
- **CAP Theorem** : Consistency, Availability, Partition Tolerance (en choisir 2)
- **Normalization** : Organisation des données pour réduire la redondance
- **Denormalization** : Ajout de redondance pour améliorer les performances en lecture

## Bases de données relationnelles (SQL)

### Concepts fondamentaux
- **Tables** : Lignes (records) et colonnes (fields)
- **Primary Key** : Identifiant unique pour chaque ligne
- **Foreign Key** : Référence à la clé primaire d'une autre table
- **Indexes** : Structures de données améliorant la vitesse des requêtes
- **Views** : Tables virtuelles basées sur les résultats d'une requête
- **Stored Procedures** : Blocs de code SQL précompilés
- **Triggers** : Actions automatiques lors de modifications de données

### Opérations SQL (CRUD)
```sql
-- Créer
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Lire
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Mettre à jour
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Supprimer
DELETE FROM users WHERE id = 1;
```

### Joins
- **INNER JOIN** : Renvoie les lignes correspondantes des deux tables
- **LEFT JOIN** : Toutes les lignes de la table de gauche, correspondances à droite
- **RIGHT JOIN** : Toutes les lignes de la table de droite, correspondances à gauche
- **FULL OUTER JOIN** : Toutes les lignes des deux tables
- **CROSS JOIN** : Produit cartésien des deux tables
- **SELF JOIN** : Table jointe avec elle-même

### Formes normales
- **1NF** : Valeurs atomiques, aucun groupe répétitif
- **2NF** : 1NF + aucune dépendance partielle (tous les attributs non-clé dépendent de la clé primaire entière)
- **3NF** : 2NF + aucune dépendance transitive (les attributs non-clé ne dépendent pas d'autres attributs non-clé)
- **BCNF** : 3NF renforcée, chaque déterminant est une clé candidate
- **4NF** : Aucune dépendance multivaluée
- **5NF** : Aucune dépendance de jointure

### SGBDR populaires
- **PostgreSQL** : Fonctionnalités avancées, extensible, conforme ACID
- **MySQL** : Très utilisé, lectures rapides, applications web
- **Oracle** : Fonctionnalités d'entreprise, scalabilité, coûteux
- **SQL Server** : Écosystème Microsoft, outils intégrés
- **SQLite** : Embarqué, serverless, léger
- **MariaDB** : Fork de MySQL, open-source

## Bases de données NoSQL

### Types de bases de données NoSQL

#### Document Stores
- **Structure** : Documents de type JSON (BSON)
- **Cas d'usage** : Gestion de contenu, catalogues, profils utilisateur
- **Exemples** : MongoDB, CouchDB, DocumentDB
- **Exemple de requête** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure** : Paires clé-valeur simples
- **Cas d'usage** : Cache, sessions, paniers d'achat
- **Exemples** : Redis, DynamoDB, Riak
- **Caractéristiques** : Rapides, simples, capacités de requête limitées

#### Column-Family Stores
- **Structure** : Colonnes regroupées en familles
- **Cas d'usage** : Big data, analytics, séries temporelles
- **Exemples** : Cassandra, HBase, ScyllaDB
- **Caractéristiques** : Optimisées pour l'écriture, distribuées, scalables

#### Graph Databases
- **Structure** : Nœuds, arêtes, propriétés
- **Cas d'usage** : Réseaux sociaux, détection de fraude, recommandations
- **Exemples** : Neo4j, Amazon Neptune, ArangoDB
- **Langage de requête** : Cypher (Neo4j), Gremlin

### Quand utiliser NoSQL
- Schéma flexible/évolutif
- Besoins de scalabilité horizontale
- Débit d'écriture élevé
- Données hiérarchiques/imbriquées
- Systèmes distribués
- Applications en temps réel

## Conception de base de données

### Modélisation entité-relation
- **Entities** : Objets/concepts (Customer, Product, Order)
- **Attributes** : Propriétés des entités (name, price, date)
- **Relationships** : Connexions entre entités (one-to-one, one-to-many, many-to-many)
- **Cardinality** : Nombre d'instances dans la relation

### Modèles de conception de schéma
- **Single Table Inheritance** : Tous les types dans une seule table avec discriminateur de type
- **Class Table Inheritance** : Tables séparées pour la base et les sous-classes
- **Concrete Table Inheritance** : Table séparée pour chaque classe concrète
- **Junction Tables** : Résolvent les relations many-to-many
- **Audit Tables** : Suivent les changements (`created_at`, `updated_at`, `deleted_at`)

### Stratégies d'indexation
- **B-Tree** : Par défaut, requêtes de plage, tri
- **Hash** : Recherches par correspondance exacte
- **Bitmap** : Colonnes à faible cardinalité (gender, status)
- **Full-Text** : Capacités de recherche textuelle
- **Spatial** : Données géographiques (GIS)
- **Composite** : Plusieurs colonnes combinées
- **Covering** : Inclut toutes les colonnes nécessaires à la requête

## Optimisation des requêtes

### Plans d'exécution
- Comprendre comment la base de données exécute les requêtes
- Identifier les goulots d'étranglement (scans complets de table, index manquants)
- Outils : EXPLAIN, EXPLAIN ANALYZE

### Techniques d'optimisation
- **Index Usage** : S'assurer que les requêtes utilisent les index appropriés
- **Query Rewriting** : Simplifier les requêtes complexes
- **Join Optimization** : Choisir les bons types et l'ordre des joins
- **Partitioning** : Découper les grandes tables (range, hash, list)
- **Materialized Views** : Résultats de requêtes pré-calculés
- **Query Caching** : Stocker les résultats de requêtes fréquentes

### Problèmes de performance courants
- **N+1 Query Problem** : Récupération inefficace de données liées
- **Missing Indexes** : Scans complets de grandes tables
- **Over-indexing** : Écritures ralenties par trop d'index
- **Lock Contention** : Transactions en attente de verrous
- **Inefficient Queries** : SELECT *, joins inutiles

## Transactions et concurrence

### Niveaux d'isolation des transactions
- **READ UNCOMMITTED** : Isolation minimale, dirty reads possibles
- **READ COMMITTED** : Seules les données validées sont visibles (par défaut dans la plupart des DB)
- **REPEATABLE READ** : La même requête renvoie les mêmes résultats dans la transaction
- **SERIALIZABLE** : Isolation maximale, transactions exécutées séquentiellement

### Contrôle de concurrence
- **Pessimistic Locking** : Verrouiller les ressources avant l'accès
- **Optimistic Locking** : Vérifier la version avant le commit
- **MVCC (Multi-Version Concurrency Control)** : Maintenir plusieurs versions des lignes
- **Row-Level Locking** : Verrouiller des lignes spécifiques
- **Table-Level Locking** : Verrouiller toute la table

### Deadlocks
- Dépendance circulaire où les transactions s'attendent mutuellement
- Prévention : Ordre de verrouillage cohérent, timeouts, détection de deadlock
- Résolution : Annuler une transaction

## Réplication et scalabilité

### Types de réplication
- **Master-Slave** : Un primaire, plusieurs read replicas
- **Master-Master** : Plusieurs primaires, réplication bidirectionnelle
- **Multi-Master** : N primaires, résolution de conflits nécessaire
- **Chain Replication** : Réplication séquentielle via des nœuds

### Approches de mise à l'échelle
- **Vertical Scaling** : Augmenter les ressources du serveur (CPU, RAM, stockage)
- **Horizontal Scaling** : Ajouter plus de serveurs (sharding, partitioning)
- **Read Replicas** : Décharger le trafic de lecture
- **Sharding** : Répartir les données entre les serveurs par clé/plage/hash
- **Federation** : Répartition par fonction/service

### Modèles de cohérence
- **Strong Consistency** : Tous les nœuds voient les mêmes données au même moment
- **Eventual Consistency** : Les nœuds convergent avec le temps
- **Causal Consistency** : Les relations de cause à effet sont préservées
- **Read-Your-Writes** : L'utilisateur voit immédiatement ses propres mises à jour

## Sauvegarde et restauration

### Stratégies de sauvegarde
- **Full Backup** : Copie complète de la base de données
- **Incremental Backup** : Changements depuis la dernière sauvegarde
- **Differential Backup** : Changements depuis la dernière sauvegarde complète
- **Point-in-Time Recovery** : Restauration à un instant précis
- **Continuous Backup** : Réplication en temps réel vers une sauvegarde

### Procédures de reprise
- **RTO (Recovery Time Objective)** : Durée maximale d'indisponibilité acceptable
- **RPO (Recovery Point Objective)** : Perte de données maximale acceptable
- **Disaster Recovery Plan** : Procédures documentées pour les défaillances
- **Testing** : Exercices de reprise réguliers

## Sécurité

### Contrôle d'accès
- **Authentication** : Vérifier l'identité de l'utilisateur
- **Authorization** : Accorder des permissions (GRANT, REVOKE)
- **Roles** : Regrouper les permissions pour une gestion plus simple
- **Principle of Least Privilege** : Accès minimal nécessaire

### Protection des données
- **Encryption at Rest** : Chiffrer les données stockées
- **Encryption in Transit** : TLS/SSL pour les connexions
- **Masking** : Masquer les données sensibles hors production
- **Tokenization** : Remplacer les données sensibles par des tokens

### Vulnérabilités courantes
- **SQL Injection** : SQL malveillant dans les entrées utilisateur
- **Privilege Escalation** : Obtention d'un accès non autorisé
- **Audit Logging** : Suivre toutes les activités de base de données
- **Compliance** : Exigences GDPR, HIPAA, PCI-DSS

## Technologies modernes de base de données

### Cloud Databases
- **AWS** : RDS, Aurora, DynamoDB, Redshift
- **Google Cloud** : Cloud SQL, Spanner, Bigtable, Firestore
- **Azure** : SQL Database, Cosmos DB, Synapse
- **Avantages** : Service managé, auto-scaling, sauvegardes incluses

### NewSQL Databases
- Combiner la cohérence SQL avec la scalabilité NoSQL
- **Exemples** : CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Fonctionnalités** : Distribuées, transactions ACID, scalabilité horizontale

### Bases de données de séries temporelles
- Optimisées pour les données horodatées
- **Exemples** : InfluxDB, TimescaleDB, Prometheus
- **Cas d'usage** : IoT, supervision, données financières

### Bases de données vectorielles
- Stocker et interroger des vecteurs d'embedding
- **Exemples** : Pinecone, Milvus, Weaviate, Qdrant
- **Cas d'usage** : Recherche sémantique, systèmes de recommandation, applications d'IA

### Bases de données multi-modèles
- Prennent en charge plusieurs modèles de données dans un seul système
- **Exemples** : ArangoDB, OrientDB, Azure Cosmos DB
- **Avantage** : Flexibilité sans multiplier les bases de données

## ORMs et accès aux données

### Object-Relational Mapping
- **Objectif** : Mapper les tables de base de données sur des objets du langage
- **ORMs populaires** :
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Avantages
- Abstraction par rapport au SQL
- Sûreté des types
- Gestion des migrations
- API de construction de requêtes

### Inconvénients
- Surcoût en performance
- Requêtes complexes plus difficiles à écrire
- Problèmes de requêtes N+1
- Courbe d'apprentissage

## Administration de bases de données

### Responsabilités du DBA
- Installation et configuration
- Réglage des performances
- Sauvegarde et restauration
- Gestion de la sécurité
- Planification de capacité
- Supervision et alerting
- Gestion des correctifs

### Métriques de supervision
- Temps de réponse des requêtes
- Débit (transactions par seconde)
- Nombre de connexions
- Taux de succès du cache
- Disk I/O
- Temps d'attente sur les verrous
- Retard de réplication

### Tâches de maintenance
- **Vacuum/Analyze** : Mettre à jour les statistiques, récupérer de l'espace
- **Index Rebuilding** : Défragmenter les index
- **Statistics Updates** : Maintenir l'optimiseur de requêtes informé
- **Log Rotation** : Gérer la taille des fichiers log
- **Capacity Planning** : Prévoir la croissance, planifier les mises à niveau
