<!-- 
This file was automatically translated from English to Turkish.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Veritabanı Sistemler

## Veritabanı Temeller

### What is a Veritabanı?
A Veritabanı is an organized collection içinde structured information stored electronically, designed için efficient retrieval, insertion, updating, ve deletion içinde Veri.

### Veritabanı Yönetim Sistemler (DBMS)
Software that interacts ile end users, applications, ve bu Veritabanı itself to capture ve analyze Veri. Örnekler: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization içinde Veritabanı (tables, fields, relationships)
- **Instance**: Actual Veri stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing Veri to reduce redundancy
- **Denormalization**: Adding redundancy to improve read Performans

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) ve columns (fields)
- **Primary Key**: Unique identifier için each row
- **Foreign Key**: Referans to primary key içinde another table
- **Indexes**: Veri structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on Veri changes

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
- **CROSS JOIN**: Cartesian product içinde both tables
- **SELF JOIN**: Table joined ile itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: İleri Düzey features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, Web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types içinde NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content Yönetim, catalogs, user profiles
- **Örnekler**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Örnekler**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big Veri, analytics, time-series
- **Örnekler**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Örnekler**: Neo4j, Amazon Neptune, ArangoDB
- **Query Dil**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested Veri
- Distributed Sistemler
- Real-time applications

## Veritabanı Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties içinde entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number içinde instances içinde relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types içinde one table ile type discriminator
- **Class Table Inheritance**: Separate tables için base ve subclasses
- **Concrete Table Inheritance**: Separate table için each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic Veri (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed için query

## Query Optimization

### Execution Plans
- Understanding how Veritabanı executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types ve order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common Performans Issues
- **N+1 Query Problem**: Fetching related Veri inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting için locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions ve Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed Veri visible (default içinde most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions içinde rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait için each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication ve Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split Veri across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same Veri at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup ve Recovery

### Backup Strategies
- **Full Backup**: Tam Veritabanı copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-içinde-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable Veri loss
- **Disaster Recovery Plan**: Documented procedures için failures
- **Test Etme**: Regular recovery drills

## Güvenlik

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions için easier Yönetim
- **Principle içinde Least Privilege**: Minimum necessary access

### Veri Protection
- **Encryption at Rest**: Encrypt stored Veri
- **Encryption içinde Transit**: TLS/SSL için connections
- **Masking**: Hide sensitive Veri içinde non-production
- **Tokenization**: Replace sensitive Veri ile tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL içinde user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all Veritabanı activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern Veritabanı Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Veritabanı, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency ile NoSQL scalability
- **Örnekler**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized için timestamped Veri
- **Örnekler**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial Veri

### Vector Databases
- Store ve query embedding vectors
- **Örnekler**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation Sistemler, AI applications

### Multi-Model Databases
- Destek multiple Veri models içinde single system
- **Örnekler**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs ve Veri Access

### Object-Relational Mapping
- **Purpose**: Map Veritabanı tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration Yönetim
- Query building APIs

### Drawbacks
- Performans overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## Veritabanı Administration

### DBA Responsibilities
- Installation ve configuration
- Performans tuning
- Backup ve recovery
- Güvenlik Yönetim
- Capacity planning
- Monitoring ve alerting
- Patch Yönetim

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update İstatistikler, reclaim space
- **Index Rebuilding**: Defragment indexes
- **İstatistikler Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
