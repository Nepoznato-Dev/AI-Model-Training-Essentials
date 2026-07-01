<!-- 
Ce fichier a été traduit automatiquement de l'anglais vers le français.
Source : database_systems.md
Note : Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer avec des modifications via des pull requests.
-->

# Systèmes de Base de Données

## Fondamentaux des Bases de Données

### Qu'est-ce qu'une Base de Données?
Une base de données est une collection organisée de données structurées stockées électroniquement, conçue pour une récupération, insertion, mise à jour et suppression efficaces des données.

### Systèmes de Gestion de Base de Données (SGBD)
Logiciel qui interagit avec les utilisateurs finaux, les applications et la base de données elle-même pour capturer et analyser les données. Exemples: MySQL, PostgreSQL, Oracle, MongoDB.

### Concepts Clés
- **Schéma**: Structure/organisation de la base de données (tables, champs, relations)
- **Instance**: Données réelles stockées à un moment donné
- **Propriétés ACID**: Atomicité, Cohérence, Isolation, Durabilité
- **Théorème CAP**: Cohérence, Disponibilité, Tolérance au Partitionnement (choisir 2)
- **Normalisation**: Organisation des données pour réduire la redondance
- **Dénormalisation**: Ajout de redondance pour améliorer les performances de lecture

## Bases de Données Relationnelles (SQL)

### Concepts de Base
- **Tables**: Lignes (enregistrements) et colonnes (champs)
- **Clé Primaire**: Identifiant unique pour chaque ligne
- **Clé Étrangère**: Référence à la clé primaire dans une autre table
- **Index**: Structures de données améliorant la vitesse des requêtes
- **Vues**: Tables virtuelles basées sur des résultats de requêtes
- **Procédures Stockées**: Blocs de code SQL précompilés
- **Déclencheurs**: Actions automatiques lors des changements de données

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
- **INNER JOIN**: Retourne les lignes correspondantes des deux tables
- **LEFT JOIN**: Toutes les lignes de la table gauche, correspondances de la droite
- **RIGHT JOIN**: Toutes les lignes de la table droite, correspondances de la gauche
- **FULL OUTER JOIN**: Toutes les lignes des deux tables
- **CROSS JOIN**: Produit cartésien des deux tables
- **SELF JOIN**: Table jointe avec elle-même

### Formes de Normalisation
- **1NF**: Valeurs atomiques, pas de groupes répétitifs
- **2NF**: 1NF + pas de dépendances partielles (tous les attributs non-clé dépendent de toute la clé primaire)
- **3NF**: 2NF + pas de dépendances transitives (les attributs non-clé ne dépendent pas d'autres attributs non-clé)
- **BCNF**: 3NF renforcée, chaque déterminant est une clé candidate
- **4NF**: Pas de dépendances multi-valuées
- **5NF**: Pas de dépendances de jointure

### SGBD Populaires
- **PostgreSQL**: Fonctionnalités avancées, extensible, conforme ACID
- **MySQL**: Largement utilisé, lectures rapides, applications web
- **Oracle**: Fonctionnalités entreprise, scalabilité, coûteux
- **SQL Server**: Écosystème Microsoft, outils intégrés
- **SQLite**: Embarqué, sans serveur, léger
- **MariaDB**: Fork MySQL, open-source

## Bases de Données NoSQL

### Types de Bases de Données NoSQL

#### Magasins de Documents
- **Structure**: Documents de type JSON (BSON)
- **Cas d'Usage**: Gestion de contenu, catalogues, profils utilisateurs
- **Exemples**: MongoDB, CouchDB, DocumentDB
- **Exemple de Requête** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Magasins Clé-Valeur
- **Structure**: Paires clé-valeur simples
- **Cas d'Usage**: Mise en cache, sessions, paniers d'achat
- **Exemples**: Redis, DynamoDB, Riak
- **Caractéristiques**: Rapide, simple, requêtes limitées

#### Magasins à Colonnes
- **Structure**: Colonnes regroupées en familles
- **Cas d'Usage**: Big Data, analytique, séries temporelles
- **Exemples**: Cassandra, HBase, ScyllaDB
- **Caractéristiques**: Optimisé pour l'écriture, distribué, scalable

#### Bases de Données Graphe
- **Structure**: Nœuds, arêtes, propriétés
- **Cas d'Usage**: Réseaux sociaux, détection de fraude, recommandations
- **Exemples**: Neo4j, Amazon Neptune, ArangoDB
- **Langage de Requête**: Cypher (Neo4j), Gremlin

### Quand Utiliser NoSQL
- Schéma flexible/évolutif
- Besoins de mise à l'échelle horizontale
- Débit d'écriture élevé
- Données hiérarchiques/imbriquées
- Systèmes distribués
- Applications en temps réel

## Conception de Base de Données

### Modélisation Entité-Relation
- **Entités**: Objets/concepts (Client, Produit, Commande)
- **Attributs**: Propriétés des entités (nom, prix, date)
- **Relations**: Connexions entre entités (un-à-un, un-à-plusieurs, plusieurs-à-plusieurs)
- **Cardinalité**: Nombre d'instances dans la relation

### Modèles de Conception de Schéma
- **Héritage Table Unique**: Tous les types dans une table avec discriminateur de type
- **Héritage par Table de Classe**: Tables séparées pour la base et les sous-classes
- **Héritage par Table Concrète**: Table séparée pour chaque classe concrète
- **Tables de Jonction**: Résoudre les relations plusieurs-à-plusieurs
- **Tables d'Audit**: Suivre les changements (created_at, updated_at, deleted_at)

### Stratégies d'Indexation
- **B-Tree**: Par défaut, requêtes de plage, tri
- **Hash**: Recherches par correspondance exacte
- **Bitmap**: Colonnes à faible cardinalité (genre, statut)
- **Full-Text**: Capacités de recherche textuelle
- **Spatial**: Données géographiques (GIS)
- **Composite**: Plusieurs colonnes combinées
- **Couvrant**: Inclut toutes les colonnes nécessaires pour la requête

## Optimisation des Requêtes

### Plans d'Exécution
- Comprendre comment la base de données exécute les requêtes
- Identifier les goulots d'étranglement (balayages complets de table, index manquants)
- Outils: EXPLAIN, EXPLAIN ANALYZE

### Techniques d'Optimisation
- **Utilisation des Index**: S'assurer que les requêtes utilisent les index appropriés
- **Réécriture de Requêtes**: Simplifier les requêtes complexes
- **Optimisation des Jointures**: Choisir les types et l'ordre de jointure corrects
- **Partitionnement**: Diviser les grandes tables (plage, hachage, liste)
- **Vues Matérialisées**: Résultats de requêtes pré-calculés
- **Mise en Cache des Requêtes**: Stocker les résultats de requêtes fréquentes

### Problèmes de Performance Courants
- **Problème de Requête N+1**: Récupération inefficace des données liées
- **Index Manquants**: Balayages complets de table sur les grandes tables
- **Sur-indexation**: Écritures lentes dues à trop d'index
- **Contention de Verrous**: Transactions attendant les verrous
- **Requêtes Inefficaces**: SELECT *, jointures inutiles

## Transactions et Concurrence

### Niveaux d'Isolation des Transactions
- **READ UNCOMMITTED**: Isolation la plus faible, lectures sales possibles
- **READ COMMITTED**: Seules les données validées sont visibles (par défaut dans la plupart des SGBD)
- **REPEATABLE READ**: La même requête retourne les mêmes résultats dans la transaction
- **SERIALIZABLE**: Isolation la plus élevée, les transactions s'exécutent séquentiellement

### Contrôle de Concurrence
- **Verrouillage Pessimiste**: Verrouiller les ressources avant l'accès
- **Verrouillage Optimiste**: Vérifier la version avant validation
- **MVCC (Multi-Version Concurrency Control)**: Maintenir plusieurs versions des lignes
- **Verrouillage au Niveau des Lignes**: Verrouiller des lignes spécifiques
- **Verrouillage au Niveau de la Table**: Verrouiller toute la table

### Interblocages (Deadlocks)
- Dépendance circulaire où les transactions s'attendent mutuellement
- Prévention: Ordre de verrouillage cohérent, délais d'attente, détection d'interblocage
- Résolution: Abandonner une transaction

## Réplication et Mise à l'Échelle

### Types de Réplication
- **Maître-Esclave**: Un primaire, plusieurs répliques en lecture
- **Maître-Maître**: Plusieurs primaires, réplication bidirectionnelle
- **Multi-Maîtres**: N primaires, résolution de conflits nécessaire
- **Réplication en Chaîne**: Réplication séquentielle à travers les nœuds

### Approches de Mise à l'Échelle
- **Mise à l'Échelle Verticale**: Augmenter les ressources du serveur (CPU, RAM, stockage)
- **Mise à l'Échelle Horizontale**: Ajouter plus de serveurs (sharding, partitionnement)
- **Répliques en Lecture**: Décharger le trafic de lecture
- **Sharding**: Diviser les données entre les serveurs par clé/plage/hachage
- **Fédération**: Diviser par fonction/service

### Modèles de Cohérence
- **Cohérence Forte**: Tous les nœuds voient les mêmes données en même temps
- **Cohérence à Terme**: Les nœuds convergent avec le temps
- **Cohérence Causale**: Relations cause-effet préservées
- **Read-Your-Writes**: L'utilisateur voit ses propres mises à jour immédiatement

## Sauvegarde et Récupération

### Stratégies de Sauvegarde
- **Sauvegarde Complète**: Copie complète de la base de données
- **Sauvegarde Incrémentielle**: Changements depuis la dernière sauvegarde
- **Sauvegarde Différentielle**: Changements depuis la dernière sauvegarde complète
- **Récupération à un Instant Donné**: Restaurer à un moment spécifique
- **Sauvegarde Continue**: Réplication en temps réel vers la sauvegarde

### Procédures de Récupération
- **RTO (Recovery Time Objective)**: Temps d'arrêt maximum acceptable
- **RPO (Recovery Point Objective)**: Perte de données maximum acceptable
- **Plan de Reprise après Sinistre**: Procédures documentées pour les pannes
- **Tests**: Exercices réguliers de récupération

## Sécurité

### Contrôle d'Accès
- **Authentification**: Vérifier l'identité de l'utilisateur
- **Autorisation**: Accorder des permissions (GRANT, REVOKE)
- **Rôles**: Regrouper les permissions pour une gestion plus facile
- **Principe du Moindre Privilège**: Accès minimum nécessaire

### Protection des Données
- **Chiffrement au Repos**: Chiffrer les données stockées
- **Chiffrement en Transit**: TLS/SSL pour les connexions
- **Masquage**: Cacher les données sensibles dans les environnements non-production
- **Tokenisation**: Remplacer les données sensibles par des jetons

### Vulnérabilités Courantes
- **Injection SQL**: SQL malveillant dans l'entrée utilisateur
- **Élévation de Privilèges**: Obtention d'un accès non autorisé
- **Journalisation d'Audit**: Suivre toutes les activités de la base de données
- **Conformité**: Exigences RGPD, HIPAA, PCI-DSS

## Technologies Modernes de Base de Données

### Bases de Données Cloud
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Avantages**: Service managé, mise à l'échelle automatique, sauvegardes incluses

### Bases de Données NewSQL
- Combine la cohérence SQL avec la scalabilité NoSQL
- **Exemples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Fonctionnalités**: Distribué, transactions ACID, mise à l'échelle horizontale

### Bases de Données de Séries Temporelles
- Optimisées pour les données horodatées
- **Exemples**: InfluxDB, TimescaleDB, Prometheus
- **Cas d'Usage**: IoT, surveillance, données financières

### Bases de Données Vectorielles
- Stocker et interroger des vecteurs d'embeddings
- **Exemples**: Pinecone, Milvus, Weaviate, Qdrant
- **Cas d'Usage**: Recherche sémantique, systèmes de recommandation, applications IA

### Bases de Données Multi-Modèles
- Prend en charge plusieurs modèles de données dans un seul système
- **Exemples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Avantage**: Flexibilité sans multiples bases de données

## ORMs et Accès aux Données

### Mappage Objet-Relationnel
- **Objectif**: Mapper les tables de base de données aux objets de programmation
- **ORMs Populaires**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Avantages
- Abstraction du SQL
- Sécurité de type
- Gestion des migrations
- APIs de construction de requêtes

### Inconvénients
- Surcharge de performance
- Requêtes complexes plus difficiles à écrire
- Problèmes de requête N+1
- Courbe d'apprentissage

## Administration de Base de Données

### Responsabilités du DBA
- Installation et configuration
- Réglage des performances
- Sauvegarde et récupération
- Gestion de la sécurité
- Planification de la capacité
- Surveillance et alertes
- Gestion des correctifs

### Métriques de Surveillance
- Temps de réponse des requêtes
- Débit (transactions par seconde)
- Nombre de connexions
- Taux de succès du cache
- E/S disque
- Temps d'attente des verrous
- Latence de réplication

### Tâches de Maintenance
- **Vacuum/Analyze**: Mettre à jour les statistiques, récupérer l'espace
- **Reconstruction d'Index**: Défragmenter les index
- **Mises à Jour des Statistiques**: Maintenir l'optimiseur de requêtes informé
- **Rotation des Journaux**: Gérer la taille des fichiers journaux
- **Planification de la Capacité**: Prédire la croissance, planifier les mises à niveau
