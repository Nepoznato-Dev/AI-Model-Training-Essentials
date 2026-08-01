<!-- 
This file was automatically translated from English to French.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Systèmes de base de données

## Fondamentaux des bases de données

### Qu'est-ce qu'une base de données ?
Une base de données est un ensemble organisé d'informations structurées, stockées électroniquement et conçues pour permettre la récupération, l'insertion, la mise à jour et la suppression efficaces des données.

### Systèmes de gestion de base de données (DBMS)
Il s'agit de logiciels qui interagissent avec les utilisateurs finaux, les applications et la base de données elle-même afin de collecter et d'analyser les données. Exemples : MySQL, PostgreSQL, Oracle, MongoDB.

### Concepts clés
- **Schéma** : structure et organisation de la base de données (tables, champs, relations)
- **Instance** : données réellement stockées à un instant donné
- **Propriétés ACID** : atomicité, cohérence, isolation, durabilité
- **Théorème CAP** : cohérence, disponibilité, tolérance au partitionnement (on en choisit 2)
- **Normalisation** : organisation des données pour réduire la redondance
- **Dénormalisation** : ajout de redondance pour améliorer les performances de lecture

## Bases de données relationnelles (SQL)

### Concepts de base
- **Tables** : lignes (enregistrements) et colonnes (champs)
- **Clé primaire** : identifiant unique pour chaque ligne
- **Clé étrangère** : référence à la clé primaire d'une autre table
- **Index** : structures de données qui accélèrent les requêtes
- **Vues** : tables virtuelles basées sur les résultats d'une requête
- **Procédures stockées** : blocs de code SQL précompilés
- **Déclencheurs** : actions automatiques lors des changements de données

### Opérations SQL (CRUD)
```sql
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

### Jointures
- **INNER JOIN** : renvoie les lignes correspondantes des deux tables
- **LEFT JOIN** : toutes les lignes de la table de gauche, avec les correspondances de droite
- **RIGHT JOIN** : toutes les lignes de la table de droite, avec les correspondances de gauche
- **FULL OUTER JOIN** : toutes les lignes des deux tables
- **CROSS JOIN** : produit cartésien des deux tables
- **SELF JOIN** : table jointe avec elle-même

### Formes normales
- **1NF** : valeurs atomiques, aucun groupe répétitif
- **2NF** : 1NF + aucune dépendance partielle (tous les attributs non clés dépendent de toute la clé primaire)
- **3NF** : 2NF + aucune dépendance transitive (les attributs non clés ne dépendent pas d'autres attributs non clés)
- **BCNF** : version renforcée de la 3NF, chaque déterminant est une clé candidate
- **4NF** : aucune dépendance multivaluée
- **5NF** : aucune dépendance de jointure

### SGBDR populaires
- **PostgreSQL** : fonctionnalités avancées, extensible, conforme ACID
- **MySQL** : largement utilisé, lecture rapide, applications web
- **Oracle** : fonctionnalités d'entreprise, forte évolutivité, coûteux
- **SQL Server** : écosystème Microsoft, outils intégrés
- **SQLite** : embarqué, serverless, léger
- **MariaDB** : fork open source de MySQL

## Bases de données NoSQL

### Types de bases de données NoSQL

#### Bases documentaires
- **Structure** : documents de type JSON (BSON)
- **Cas d'utilisation** : gestion de contenu, catalogues, profils utilisateurs
- **Exemples** : MongoDB, CouchDB, DocumentDB
- **Exemple de requête** (MongoDB) :
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Bases clé-valeur
- **Structure** : paires clé-valeur simples
- **Cas d'utilisation** : mise en cache, sessions, paniers d'achat
- **Exemples** : Redis, DynamoDB, Riak
- **Caractéristiques** : rapides, simples, requêtage limité

#### Bases en familles de colonnes
- **Structure** : colonnes regroupées en familles
- **Cas d'utilisation** : Big Data, analytique, séries temporelles
- **Exemples** : Cassandra, HBase, ScyllaDB
- **Caractéristiques** : optimisées pour l'écriture, distribuées, évolutives

#### Bases de données graphe
- **Structure** : nœuds, arêtes, propriétés
- **Cas d'utilisation** : réseaux sociaux, détection de fraude, recommandations
- **Exemples** : Neo4j, Amazon Neptune, ArangoDB
- **Langages de requête** : Cypher (Neo4j), Gremlin

### Quand utiliser NoSQL
- Schéma flexible ou évolutif
- Besoin de scalabilité horizontale
- Débit d'écriture élevé
- Données hiérarchiques ou imbriquées
- Systèmes distribués
- Applications en temps réel

## Conception de base de données

### Modélisation entité-relation
- **Entités** : objets ou concepts (Customer, Product, Order)
- **Attributs** : propriétés des entités (name, price, date)
- **Relations** : liens entre les entités (un à un, un à plusieurs, plusieurs à plusieurs)
- **Cardinalité** : nombre d'instances dans une relation

### Modèles de conception de schéma
- **Héritage sur table unique** : tous les types dans une seule table avec discriminateur de type
- **Héritage par table de classe** : tables séparées pour la base et les sous-classes
- **Héritage par table concrète** : table distincte pour chaque classe concrète
- **Tables de jonction** : résolution des relations plusieurs-à-plusieurs
- **Tables d’audit** : suivi des changements (`created_at`, `updated_at`, `deleted_at`)

### Stratégies d'indexation
- **B-Tree** : par défaut, requêtes par plage, tri
- **Hash** : recherches par correspondance exacte
- **Bitmap** : colonnes à faible cardinalité (genre, statut)
- **Plein texte** : capacités de recherche textuelle
- **Spatial** : données géographiques (GIS)
- **Composite** : combinaison de plusieurs colonnes
- **Index couvrant** : inclut toutes les colonnes nécessaires à la requête

## Optimisation des requêtes

### Plans d'exécution
- Comprendre comment la base de données exécute les requêtes
- Identifier les goulots d'étranglement (scans complets de table, index manquants)
- Outils : EXPLAIN, EXPLAIN ANALYZE

### Techniques d'optimisation
- **Utilisation des index** : s'assurer que les requêtes utilisent les bons index
- **Réécriture des requêtes** : simplifier les requêtes complexes
- **Optimisation des jointures** : choisir les bons types et le bon ordre de jointure
- **Partitionnement** : découper les grandes tables (range, hash, list)
- **Vues matérialisées** : résultats de requête précalculés
- **Mise en cache des requêtes** : stocker les résultats fréquemment demandés

### Problèmes de performance courants
- **Problème de requête N+1** : récupération inefficace des données liées
- **Index manquants** : scans complets sur de grandes tables
- **Sur-indexation** : écritures ralenties par un trop grand nombre d'index
- **Contention de verrouillage** : transactions en attente de verrous
- **Requêtes inefficaces** : `SELECT *`, jointures inutiles

## Transactions et concurrence

### Niveaux d'isolation des transactions
- **READ UNCOMMITTED** : isolation la plus faible, lectures sales possibles
- **READ COMMITTED** : seules les données validées sont visibles (par défaut dans la plupart des DB)
- **REPEATABLE READ** : une même requête renvoie les mêmes résultats au sein d'une transaction
- **SERIALIZABLE** : isolation la plus forte, transactions exécutées de façon séquentielle

### Contrôle de la concurrence
- **Verrouillage pessimiste** : verrouiller les ressources avant l'accès
- **Verrouillage optimiste** : vérifier la version avant le commit
- **MVCC (Multi-Version Concurrency Control)** : conserver plusieurs versions des lignes
- **Verrouillage au niveau ligne** : verrouiller des lignes précises
- **Verrouillage au niveau table** : verrouiller la table entière

### Interblocages
- Dépendance circulaire où les transactions s'attendent mutuellement
- Prévention : ordre de verrouillage cohérent, timeouts, détection des deadlocks
- Résolution : annuler l'une des transactions

## Réplication et mise à l'échelle

### Types de réplication
- **Primaire-répliques** : un primaire, plusieurs réplicas de lecture
- **Primaire-primaire** : plusieurs primaires, réplication bidirectionnelle
- **Multi-primaire** : N primaires, avec résolution de conflits nécessaire
- **Réplication en chaîne** : réplication séquentielle à travers les nœuds

### Approches de mise à l'échelle
- **Mise à l’échelle verticale** : augmenter les ressources du serveur (CPU, RAM, stockage)
- **Mise à l’échelle horizontale** : ajouter davantage de serveurs (sharding, partitionnement)
- **Réplicas de lecture** : décharger le trafic de lecture
- **Sharding** : répartir les données entre serveurs selon une clé, une plage ou un hash
- **Fédération** : découpage par fonction ou par service

### Modèles de cohérence
- **Cohérence forte** : tous les nœuds voient les mêmes données au même moment
- **Cohérence éventuelle** : les nœuds convergent avec le temps
- **Cohérence causale** : les relations de cause à effet sont préservées
- **Lecture de ses propres écritures** : l'utilisateur voit immédiatement ses propres mises à jour

## Sauvegarde et restauration

### Stratégies de sauvegarde
- **Sauvegarde complète** : copie intégrale de la base de données
- **Sauvegarde incrémentielle** : changements depuis la dernière sauvegarde
- **Sauvegarde différentielle** : changements depuis la dernière sauvegarde complète
- **Restauration à un instant donné** : retour à un moment précis
- **Sauvegarde continue** : réplication en temps réel vers la sauvegarde

### Procédures de restauration
- **RTO (Recovery Time Objective)** : durée d'indisponibilité maximale acceptable
- **RPO (Recovery Point Objective)** : perte de données maximale acceptable
- **Plan de reprise d'activité** : procédures documentées pour les pannes
- **Test** : exercices de restauration réguliers

## Sécurité

### Contrôle d'accès
- **Authentification** : vérifier l'identité de l'utilisateur
- **Autorisation** : accorder des permissions (GRANT, REVOKE)
- **Rôles** : regrouper les permissions pour simplifier la gestion
- **Principe du moindre privilège** : accès minimum nécessaire

### Protection des données
- **Chiffrement au repos** : chiffrer les données stockées
- **Chiffrement en transit** : TLS/SSL pour les connexions
- **Masquage** : cacher les données sensibles en dehors de la production
- **Tokenisation** : remplacer les données sensibles par des jetons

### Vulnérabilités courantes
- **Injection SQL** : SQL malveillant dans les entrées utilisateur
- **Élévation de privilèges** : obtention d'un accès non autorisé
- **Journalisation d'audit** : suivre toutes les activités de la base de données
- **Conformité** : exigences GDPR, HIPAA, PCI-DSS

## Technologies modernes de base de données

### Bases de données cloud
- **AWS** : RDS, Aurora, DynamoDB, Redshift
- **Google Cloud** : Cloud SQL, Spanner, Bigtable, Firestore
- **Azure** : SQL Database, Cosmos DB, Synapse
- **Avantages** : service géré, mise à l'échelle automatique, sauvegardes incluses

### Bases de données NewSQL
- Combinent la cohérence de SQL avec la scalabilité de NoSQL
- **Exemples** : CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Fonctionnalités** : distribuées, transactions ACID, scalabilité horizontale

### Bases de données de séries temporelles
- Optimisées pour les données horodatées
- **Exemples** : InfluxDB, TimescaleDB, Prometheus
- **Cas d'utilisation** : IoT, monitoring, données financières

### Bases de données vectorielles
- Stockent et interrogent des vecteurs d'embeddings
- **Exemples** : Pinecone, Milvus, Weaviate, Qdrant
- **Cas d'utilisation** : recherche sémantique, systèmes de recommandation, applications d'IA

### Bases de données multi-modèles
- Prennent en charge plusieurs modèles de données dans un même système
- **Exemples** : ArangoDB, OrientDB, Azure Cosmos DB
- **Avantage** : flexibilité sans multiplier les bases de données

## ORMs et accès aux données

### Mapping objet-relationnel
- **Objectif** : mapper les tables de la base de données sur des objets du langage
- **ORM populaires** :
  - Python : SQLAlchemy, Django ORM, Peewee
  - JavaScript : Sequelize, Prisma, TypeORM
  - Java : Hibernate, JPA
  - Ruby : ActiveRecord
  - .NET : Entity Framework

### Avantages
- Abstraction par rapport au SQL
- Sûreté de type
- Gestion des migrations
- API de construction de requêtes

### Inconvénients
- Surcoût de performance
- Requêtes complexes plus difficiles à écrire
- Problèmes de requêtes N+1
- Courbe d'apprentissage

## Administration des bases de données

### Responsabilités du DBA
- Installation et configuration
- Réglage des performances
- Sauvegarde et restauration
- Gestion de la sécurité
- Planification de capacité
- Monitoring et alerting
- Gestion des correctifs

### Métriques de surveillance
- Temps de réponse des requêtes
- Débit (transactions par seconde)
- Nombre de connexions
- Taux de succès du cache
- E/S disque
- Temps d'attente sur les verrous
- Retard de réplication

### Tâches de maintenance
- **Vacuum/Analyze** : mettre à jour les statistiques, récupérer de l'espace
- **Reconstruction des index** : défragmenter les index
- **Mise à jour des statistiques** : informer l'optimiseur de requêtes
- **Rotation des logs** : gérer la taille des fichiers journaux
- **Planification de capacité** : prévoir la croissance, planifier les montées de version
