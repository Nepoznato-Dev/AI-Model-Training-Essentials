<!-- 
This file was automatically translated from English to French.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Base de données Systèmes

## Base de données Fondamentaux

### What is a Base de données?
A Base de données is an organized collection de structured information stored electronically, designed pour efficient retrieval, insertion, updating, et deletion de Données.

### Base de données gestion Systèmes (DBMS)
Software that interacts avec end users, applications, et le/la Base de données itself to capture et analyze Données. Exemples: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization de Base de données (tables, fields, relationships)
- **Instance**: Actual Données stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing Données to reduce redundancy
- **Denormalization**: Adding redundancy to improve read Performance

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) et columns (fields)
- **Primary Key**: Unique identifier pour each row
- **Foreign Key**: Référence to primary key dans another table
- **Indexes**: Données structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on Données changes

### SQL Operations (CRUD)
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

### Joins
- **INNER JOIN**: Returns matching rows from both tables
- **LEFT JOIN**: All rows from left table, matches from right
- **RIGHT JOIN**: All rows from right table, matches from left
- **FULL OUTER JOIN**: All rows from both tables
- **CROSS JOIN**: Cartesian product de both tables
- **SELF JOIN**: Table joined avec itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: Avancé features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, Web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types de NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content gestion, catalogs, user profiles
- **Exemples**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Exemples**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big Données, analytics, time-series
- **Exemples**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Exemples**: Neo4j, Amazon Neptune, ArangoDB
- **Query Langue**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested Données
- Distributed Systèmes
- Real-time applications

## Base de données Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties de entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number de instances dans relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types dans one table avec type discriminator
- **Class Table Inheritance**: Separate tables pour base et subclasses
- **Concrete Table Inheritance**: Separate table pour each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic Données (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed pour query

## Query Optimization

### Execution Plans
- Understanding how Base de données executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types et order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common Performance Issues
- **N+1 Query Problem**: Fetching related Données inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting pour locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions et Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed Données visible (default dans most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions de rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait pour each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication et Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split Données across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same Données at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup et Recovery

### Backup Strategies
- **Full Backup**: Complet Base de données copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-dans-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable Données loss
- **Disaster Recovery Plan**: Documented procedures pour failures
- **Test**: Regular recovery drills

## Sécurité

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions pour easier gestion
- **Principle de Least Privilege**: Minimum necessary access

### Données Protection
- **Encryption at Rest**: Encrypt stored Données
- **Encryption dans Transit**: TLS/SSL pour connections
- **Masking**: Hide sensitive Données dans non-production
- **Tokenization**: Replace sensitive Données avec tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL dans user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all Base de données activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern Base de données Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Base de données, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency avec NoSQL scalability
- **Exemples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized pour timestamped Données
- **Exemples**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial Données

### Vector Databases
- Store et query embedding vectors
- **Exemples**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation Systèmes, AI applications

### Multi-Model Databases
- Assistance multiple Données models dans single system
- **Exemples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs et Données Access

### Object-Relational Mapping
- **Purpose**: Map Base de données tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration gestion
- Query building APIs

### Drawbacks
- Performance overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## Base de données Administration

### DBA Responsibilities
- Installation et configuration
- Performance tuning
- Backup et recovery
- Sécurité gestion
- Capacity planning
- Monitoring et alerting
- Patch gestion

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update Statistiques, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Statistiques Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
