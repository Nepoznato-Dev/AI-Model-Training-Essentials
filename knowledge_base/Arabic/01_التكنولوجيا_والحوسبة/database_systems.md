<!-- 
This file was automatically translated from English to Arabic.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# قاعدة البيانات الأنظمة

## قاعدة البيانات الأساسيات

### What is a قاعدة البيانات?
A قاعدة البيانات is an organized collection من structured information stored electronically, designed لأجل efficient retrieval, insertion, updating, و deletion من البيانات.

### قاعدة البيانات الإدارة الأنظمة (DBMS)
Software that interacts مع end users, applications, و ال قاعدة البيانات itself to capture و analyze البيانات. أمثلة: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization من قاعدة البيانات (tables, fields, relationships)
- **Instance**: Actual البيانات stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing البيانات to reduce redundancy
- **Denormalization**: Adding redundancy to improve read الأداء

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) و columns (fields)
- **Primary Key**: Unique identifier لأجل each row
- **Foreign Key**: مرجع to primary key في another table
- **Indexes**: البيانات structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on البيانات changes

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
- **CROSS JOIN**: Cartesian product من both tables
- **SELF JOIN**: Table joined مع itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: متقدم features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, الويب applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types من NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **حالات الاستخدام**: Content الإدارة, catalogs, user profiles
- **أمثلة**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **حالات الاستخدام**: Caching, sessions, shopping carts
- **أمثلة**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **حالات الاستخدام**: Big البيانات, analytics, time-series
- **أمثلة**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **حالات الاستخدام**: Social networks, fraud detection, recommendations
- **أمثلة**: Neo4j, Amazon Neptune, ArangoDB
- **Query اللغة**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested البيانات
- Distributed الأنظمة
- Real-time applications

## قاعدة البيانات Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties من entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number من instances في relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types في one table مع type discriminator
- **Class Table Inheritance**: Separate tables لأجل base و subclasses
- **Concrete Table Inheritance**: Separate table لأجل each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic البيانات (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed لأجل query

## Query Optimization

### Execution Plans
- Understanding how قاعدة البيانات executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types و order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common الأداء Issues
- **N+1 Query Problem**: Fetching related البيانات inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting لأجل locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions و Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed البيانات visible (default في most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions من rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait لأجل each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication و Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split البيانات across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same البيانات at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup و Recovery

### Backup Strategies
- **Full Backup**: مكتمل قاعدة البيانات copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-في-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable البيانات loss
- **Disaster Recovery Plan**: Documented procedures لأجل failures
- **الاختبار**: Regular recovery drills

## الأمان

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions لأجل easier الإدارة
- **Principle من Least Privilege**: Minimum necessary access

### البيانات Protection
- **Encryption at Rest**: Encrypt stored البيانات
- **Encryption في Transit**: TLS/SSL لأجل connections
- **Masking**: Hide sensitive البيانات في non-production
- **Tokenization**: Replace sensitive البيانات مع tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL في user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all قاعدة البيانات activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern قاعدة البيانات Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL قاعدة البيانات, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency مع NoSQL scalability
- **أمثلة**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized لأجل timestamped البيانات
- **أمثلة**: InfluxDB, TimescaleDB, Prometheus
- **حالات الاستخدام**: IoT, monitoring, financial البيانات

### Vector Databases
- Store و query embedding vectors
- **أمثلة**: Pinecone, Milvus, Weaviate, Qdrant
- **حالات الاستخدام**: Semantic search, recommendation الأنظمة, AI applications

### Multi-Model Databases
- الدعم multiple البيانات models في single system
- **أمثلة**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs و البيانات Access

### Object-Relational Mapping
- **Purpose**: Map قاعدة البيانات tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration الإدارة
- Query building واجهات البرمجة

### Drawbacks
- الأداء overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## قاعدة البيانات Administration

### DBA Responsibilities
- Installation و configuration
- الأداء tuning
- Backup و recovery
- الأمان الإدارة
- Capacity planning
- Monitoring و alerting
- Patch الإدارة

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update إحصائيات, reclaim space
- **Index Rebuilding**: Defragment indexes
- **إحصائيات Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
