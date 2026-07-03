<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 資料庫 系統

## 資料庫 基礎

### What is a 資料庫?
A 資料庫 is an organized collection 的 structured information stored electronically, designed 為 efficient retrieval, insertion, updating, 和 deletion 的 資料.

### 資料庫 管理 系統 (DBMS)
Software that interacts 與 end users, applications, 和 這 資料庫 itself to capture 和 analyze 資料. 範例: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization 的 資料庫 (tables, fields, relationships)
- **Instance**: Actual 資料 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing 資料 to reduce redundancy
- **Denormalization**: Adding redundancy to improve read 效能

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) 和 columns (fields)
- **Primary Key**: Unique identifier 為 each row
- **Foreign Key**: 參考 to primary key 在 another table
- **Indexes**: 資料 structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on 資料 changes

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
- **CROSS JOIN**: Cartesian product 的 both tables
- **SELF JOIN**: Table joined 與 itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: 高級 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 網路 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types 的 NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 管理, catalogs, user profiles
- **範例**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **範例**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big 資料, analytics, time-series
- **範例**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **範例**: Neo4j, Amazon Neptune, ArangoDB
- **Query 語言**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested 資料
- Distributed 系統
- Real-time applications

## 資料庫 Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 的 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number 的 instances 在 relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types 在 one table 與 type discriminator
- **Class Table Inheritance**: Separate tables 為 base 和 subclasses
- **Concrete Table Inheritance**: Separate table 為 each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 資料 (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed 為 query

## Query Optimization

### Execution Plans
- Understanding how 資料庫 executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types 和 order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common 效能 Issues
- **N+1 Query Problem**: Fetching related 資料 inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting 為 locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions 和 Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 資料 visible (default 在 most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions 的 rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait 為 each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication 和 Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split 資料 across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same 資料 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup 和 Recovery

### Backup Strategies
- **Full Backup**: 完整 資料庫 copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-在-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable 資料 loss
- **Disaster Recovery Plan**: Documented procedures 為 failures
- **測試**: Regular recovery drills

## 安全

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions 為 easier 管理
- **Principle 的 Least Privilege**: Minimum necessary access

### 資料 Protection
- **Encryption at Rest**: Encrypt stored 資料
- **Encryption 在 Transit**: TLS/SSL 為 connections
- **Masking**: Hide sensitive 資料 在 non-production
- **Tokenization**: Replace sensitive 資料 與 tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL 在 user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all 資料庫 activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern 資料庫 Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 資料庫, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency 與 NoSQL scalability
- **範例**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized 為 timestamped 資料
- **範例**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial 資料

### Vector Databases
- Store 和 query embedding vectors
- **範例**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 系統, AI applications

### Multi-Model Databases
- 支援 multiple 資料 models 在 single system
- **範例**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs 和 資料 Access

### Object-Relational Mapping
- **Purpose**: Map 資料庫 tables to programming objects
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
- 效能 overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## 資料庫 Administration

### DBA Responsibilities
- Installation 和 configuration
- 效能 tuning
- Backup 和 recovery
- 安全 管理
- Capacity planning
- Monitoring 和 alerting
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
