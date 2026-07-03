<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 数据库 系统

## 数据库 基础

### What is a 数据库?
A 数据库 is an organized collection 的 structured information stored electronically, designed 为 efficient retrieval, insertion, updating, 和 deletion 的 数据.

### 数据库 管理 系统 (DBMS)
Software that interacts 与 end users, applications, 和 这 数据库 itself to capture 和 analyze 数据. 示例: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization 的 数据库 (tables, fields, relationships)
- **Instance**: Actual 数据 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing 数据 to reduce redundancy
- **Denormalization**: Adding redundancy to improve read 性能

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) 和 columns (fields)
- **Primary Key**: Unique identifier 为 each row
- **Foreign Key**: 参考 to primary key 在 another table
- **Indexes**: 数据 structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on 数据 changes

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
- **SELF JOIN**: Table joined 与 itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: 高级 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 网络 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types 的 NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 管理, catalogs, user profiles
- **示例**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **示例**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big 数据, analytics, time-series
- **示例**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **示例**: Neo4j, Amazon Neptune, ArangoDB
- **Query 语言**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested 数据
- Distributed 系统
- Real-time applications

## 数据库 Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 的 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number 的 instances 在 relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types 在 one table 与 type discriminator
- **Class Table Inheritance**: Separate tables 为 base 和 subclasses
- **Concrete Table Inheritance**: Separate table 为 each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 数据 (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed 为 query

## Query Optimization

### Execution Plans
- Understanding how 数据库 executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types 和 order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common 性能 Issues
- **N+1 Query Problem**: Fetching related 数据 inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting 为 locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions 和 Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 数据 visible (default 在 most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions 的 rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait 为 each other
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
- **Sharding**: Split 数据 across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same 数据 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup 和 Recovery

### Backup Strategies
- **Full Backup**: 完整 数据库 copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-在-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable 数据 loss
- **Disaster Recovery Plan**: Documented procedures 为 failures
- **测试**: Regular recovery drills

## 安全

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions 为 easier 管理
- **Principle 的 Least Privilege**: Minimum necessary access

### 数据 Protection
- **Encryption at Rest**: Encrypt stored 数据
- **Encryption 在 Transit**: TLS/SSL 为 connections
- **Masking**: Hide sensitive 数据 在 non-production
- **Tokenization**: Replace sensitive 数据 与 tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL 在 user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all 数据库 activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern 数据库 Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 数据库, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency 与 NoSQL scalability
- **示例**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized 为 timestamped 数据
- **示例**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial 数据

### Vector Databases
- Store 和 query embedding vectors
- **示例**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 系统, AI applications

### Multi-Model Databases
- 支持 multiple 数据 models 在 single system
- **示例**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs 和 数据 Access

### Object-Relational Mapping
- **Purpose**: Map 数据库 tables to programming objects
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
- 性能 overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## 数据库 Administration

### DBA Responsibilities
- Installation 和 configuration
- 性能 tuning
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
- **Vacuum/Analyze**: Update 统计, reclaim space
- **Index Rebuilding**: Defragment indexes
- **统计 Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
