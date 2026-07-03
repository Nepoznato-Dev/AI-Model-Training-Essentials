<!-- 
This file was automatically translated from English to Korean.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이터베이스 시스템

## 데이터베이스 기초

### What is a 데이터베이스?
A 데이터베이스 is an organized collection 의 structured information stored electronically, designed 위한 efficient retrieval, insertion, updating, 와 deletion 의 데이터.

### 데이터베이스 관리 시스템 (DBMS)
Software that interacts 와 함께 end users, applications, 와 그 데이터베이스 itself to capture 와 analyze 데이터. 예시: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization 의 데이터베이스 (tables, fields, relationships)
- **Instance**: Actual 데이터 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing 데이터 to reduce redundancy
- **Denormalization**: Adding redundancy to improve read 성능

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) 와 columns (fields)
- **Primary Key**: Unique identifier 위한 each row
- **Foreign Key**: 참조 to primary key 에서 another table
- **Indexes**: 데이터 structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on 데이터 changes

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
- **CROSS JOIN**: Cartesian product 의 both tables
- **SELF JOIN**: Table joined 와 함께 itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: 고급 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 웹 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types 의 NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 관리, catalogs, user profiles
- **예시**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **예시**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big 데이터, analytics, time-series
- **예시**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **예시**: Neo4j, Amazon Neptune, ArangoDB
- **Query 언어**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested 데이터
- Distributed 시스템
- Real-time applications

## 데이터베이스 Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 의 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number 의 instances 에서 relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types 에서 one table 와 함께 type discriminator
- **Class Table Inheritance**: Separate tables 위한 base 와 subclasses
- **Concrete Table Inheritance**: Separate table 위한 each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 데이터 (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed 위한 query

## Query Optimization

### Execution Plans
- Understanding how 데이터베이스 executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types 와 order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common 성능 Issues
- **N+1 Query Problem**: Fetching related 데이터 inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting 위한 locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions 와 Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 데이터 visible (default 에서 most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions 의 rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait 위한 each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication 와 Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split 데이터 across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same 데이터 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup 와 Recovery

### Backup Strategies
- **Full Backup**: 완전한 데이터베이스 copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-에서-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable 데이터 loss
- **Disaster Recovery Plan**: Documented procedures 위한 failures
- **테스트**: Regular recovery drills

## 보안

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions 위한 easier 관리
- **Principle 의 Least Privilege**: Minimum necessary access

### 데이터 Protection
- **Encryption at Rest**: Encrypt stored 데이터
- **Encryption 에서 Transit**: TLS/SSL 위한 connections
- **Masking**: Hide sensitive 데이터 에서 non-production
- **Tokenization**: Replace sensitive 데이터 와 함께 tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL 에서 user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all 데이터베이스 activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern 데이터베이스 Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 데이터베이스, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency 와 함께 NoSQL scalability
- **예시**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized 위한 timestamped 데이터
- **예시**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial 데이터

### Vector Databases
- Store 와 query embedding vectors
- **예시**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 시스템, AI applications

### Multi-Model Databases
- 지원 multiple 데이터 models 에서 single system
- **예시**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs 와 데이터 Access

### Object-Relational Mapping
- **Purpose**: Map 데이터베이스 tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration 관리
- Query building APIs

### Drawbacks
- 성능 overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## 데이터베이스 Administration

### DBA Responsibilities
- Installation 와 configuration
- 성능 tuning
- Backup 와 recovery
- 보안 관리
- Capacity planning
- Monitoring 와 alerting
- Patch 관리

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update 통계, reclaim space
- **Index Rebuilding**: Defragment indexes
- **통계 Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
