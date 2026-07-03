<!-- 
This file was automatically translated from English to Japanese.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# データベース システム

## データベース 基礎

### What is a データベース?
A データベース is an organized collection の structured information stored electronically, designed のために efficient retrieval, insertion, updating, と deletion の データ.

### データベース 管理 システム (DBMS)
Software that interacts と end users, applications, と その データベース itself to capture と analyze データ. 例: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization の データベース (tables, fields, relationships)
- **Instance**: Actual データ stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing データ to reduce redundancy
- **Denormalization**: Adding redundancy to improve read パフォーマンス

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) と columns (fields)
- **Primary Key**: Unique identifier のために each row
- **Foreign Key**: リファレンス to primary key で another table
- **Indexes**: データ structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on データ changes

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
- **CROSS JOIN**: Cartesian product の both tables
- **SELF JOIN**: Table joined と itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: 上級 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, ウェブ applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types の NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 管理, catalogs, user profiles
- **例**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **例**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big データ, analytics, time-series
- **例**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **例**: Neo4j, Amazon Neptune, ArangoDB
- **Query 言語**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested データ
- Distributed システム
- Real-time applications

## データベース Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties の entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number の instances で relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types で one table と type discriminator
- **Class Table Inheritance**: Separate tables のために base と subclasses
- **Concrete Table Inheritance**: Separate table のために each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic データ (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed のために query

## Query Optimization

### Execution Plans
- Understanding how データベース executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types と order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common パフォーマンス Issues
- **N+1 Query Problem**: Fetching related データ inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting のために locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions と Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed データ visible (default で most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions の rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait のために each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication と Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split データ across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same データ at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup と Recovery

### Backup Strategies
- **Full Backup**: 完全 データベース copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-で-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable データ loss
- **Disaster Recovery Plan**: Documented procedures のために failures
- **テスト**: Regular recovery drills

## セキュリティ

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions のために easier 管理
- **Principle の Least Privilege**: Minimum necessary access

### データ Protection
- **Encryption at Rest**: Encrypt stored データ
- **Encryption で Transit**: TLS/SSL のために connections
- **Masking**: Hide sensitive データ で non-production
- **Tokenization**: Replace sensitive データ と tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL で user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all データベース activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern データベース Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL データベース, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency と NoSQL scalability
- **例**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized のために timestamped データ
- **例**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial データ

### Vector Databases
- Store と query embedding vectors
- **例**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation システム, AI applications

### Multi-Model Databases
- サポート multiple データ models で single system
- **例**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs と データ Access

### Object-Relational Mapping
- **Purpose**: Map データベース tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration 管理
- Query building APIs

### Drawbacks
- パフォーマンス overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## データベース Administration

### DBA Responsibilities
- Installation と configuration
- パフォーマンス tuning
- Backup と recovery
- セキュリティ 管理
- Capacity planning
- Monitoring と alerting
- Patch 管理

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update 統計, reclaim space
- **Index Rebuilding**: Defragment indexes
- **統計 Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
