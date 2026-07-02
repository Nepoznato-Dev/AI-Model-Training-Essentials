<!-- 
This file was automatically translated from English to Russian.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# База данных Системы

## База данных Основы

### What is a База данных?
A База данных is an organized collection из structured information stored electronically, designed для efficient retrieval, insertion, updating, и deletion из Данные.

### База данных Управление Системы (DBMS)
Software that interacts с end users, applications, и the База данных itself to capture и analyze Данные. Примеры: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization из База данных (tables, fields, relationships)
- **Instance**: Actual Данные stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing Данные to reduce redundancy
- **Denormalization**: Adding redundancy to improve read Производительность

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) и columns (fields)
- **Primary Key**: Unique identifier для each row
- **Foreign Key**: Справочник to primary key в another table
- **Indexes**: Данные structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on Данные changes

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
- **CROSS JOIN**: Cartesian product из both tables
- **SELF JOIN**: Table joined с itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: Продвинутый features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, Веб applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types из NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content Управление, catalogs, user profiles
- **Примеры**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Примеры**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big Данные, analytics, time-series
- **Примеры**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Примеры**: Neo4j, Amazon Neptune, ArangoDB
- **Query Язык**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested Данные
- Distributed Системы
- Real-time applications

## База данных Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties из entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number из instances в relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types в one table с type discriminator
- **Class Table Inheritance**: Separate tables для base и subclasses
- **Concrete Table Inheritance**: Separate table для each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic Данные (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed для query

## Query Optimization

### Execution Plans
- Understanding how База данных executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types и order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common Производительность Issues
- **N+1 Query Problem**: Fetching related Данные inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting для locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions и Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed Данные visible (default в most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions из rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait для each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication и Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split Данные across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same Данные at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup и Recovery

### Backup Strategies
- **Full Backup**: Complete База данных copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-в-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable Данные loss
- **Disaster Recovery Plan**: Documented procedures для failures
- **Тестирование**: Regular recovery drills

## Безопасность

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions для easier Управление
- **Principle из Least Privilege**: Minimum necessary access

### Данные Protection
- **Encryption at Rest**: Encrypt stored Данные
- **Encryption в Transit**: TLS/SSL для connections
- **Masking**: Hide sensitive Данные в non-production
- **Tokenization**: Replace sensitive Данные с tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL в user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all База данных activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern База данных Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL База данных, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency с NoSQL scalability
- **Примеры**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized для timestamped Данные
- **Примеры**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial Данные

### Vector Databases
- Store и query embedding vectors
- **Примеры**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation Системы, AI applications

### Multi-Model Databases
- Support multiple Данные models в single system
- **Примеры**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs и Данные Access

### Object-Relational Mapping
- **Purpose**: Map База данных tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration Управление
- Query building APIs

### Drawbacks
- Производительность overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## База данных Administration

### DBA Responsibilities
- Installation и configuration
- Производительность tuning
- Backup и recovery
- Безопасность Управление
- Capacity planning
- Monitoring и alerting
- Patch Управление

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update Статистика, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Статистика Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
