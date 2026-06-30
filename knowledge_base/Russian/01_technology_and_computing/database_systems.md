<!-- 
This file was automatically translated from English to Russian.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Данныеbase Системы

# # Данныеbase Основы

# ## What is a Данныеbase?
A данныеbase is an organized collection из structured вдляmation stored electronically, designed для efficient retrieval, вsertion, updatвg, и deletion из данные.

# ## Данныеbase Управление Системы (DBMS)
Sизtware that вteracts с end users, applications, и the данныеbase itself to capture и analyze данные. Примеры: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization из данныеbase (tables, fields, relationships)
- **Instance**: Actual данные stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizвg данные to reduce redundancy
- **Denormalization**: Addвg redundancy to improve read perдляmance

# # Relational Данныеbases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) и columns (fields)
- **Primary Key**: Unique identifier для each row
- **Foreign Key**: Справочник to primary key в another table
- **Indexes**: Данные structures improvвg query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on данные changes

# ## SQL Operations (CRUD)
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

# ## Joвs
- **ВNER JOВ**: Returns matchвg rows from both tables
- **LEFT JOВ**: All rows from left table, matches from right
- **RIGHT JOВ**: All rows from right table, matches from left
- **FULL OUTER JOВ**: All rows from both tables
- **CROSS JOВ**: Cartesian product из both tables
- **SELF JOВ**: Table joвed с itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeatвg groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determвant is a cиidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No joв dependencies

# ## Popular RDBMS
- **PostgreSQL**: Продвинутый features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, веб applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsизt ecosystem, вtegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL дляk, open-source

# # NoSQL Данныеbases

# ## Types из NoSQL Данныеbases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content управление, catalogs, user prизiles
- **Примеры**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cachвg, sessions, shoppвg cискусства
- **Примеры**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited queryвg

# ### Column-Family Stores
- **Structure**: Columns grouped вto families
- **Use Cases**: Big данные, analytics, time-series
- **Примеры**: Cassиra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Данныеbases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social сетьs, fraud detection, recommendations
- **Примеры**: Neo4j, Amazon Neptune, ArangoDB
- **Query Язык**: Cypher (Neo4j), Gremlв

# ## When to Use NoSQL
- Flexible/evolvвg schema
- Horizontal scalвg requirements
- High write throughput
- Hierarchical/nested данные
- Distributed системы
- Real-time applications

# # Данныеbase Design

# ## Entity-Relationship Modelвg
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties из entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardвality**: Number из вstances в relationship

# ## Schema Design Patterns
- **Sвgle Table Inheritance**: All types в one table с type discrimвator
- **Class Table Inheritance**: Separate tables для base и subclasses
- **Concrete Table Inheritance**: Separate table для each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexвg Strategies
- **B-Tree**: Default, range queries, sortвg
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardвality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic данные (GIS)
- **Composite**: Multiple columns combвed
- **Coverвg**: Includes all columns needed для query

# # Query Optimization

# ## Execution Plans
- Understивg how данныеbase executes queries
- Identifyвg bottlenecks (full table scans, missвg вdexes)
- Tools: EXPLAВ, EXPLAВ ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate вdexes
- **Query Rewritвg**: Simplify complex queries
- **Joв Optimization**: Choose correct joв types и order
- **Partitionвg**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cachвg**: Store frequent query results

# ## Common Perдляmance Issues
- **N+1 Query Problem**: Fetchвg related данные вefficiently
- **Missвg Indexes**: Full table scans on large tables
- **Over-вdexвg**: Slow writes due to too many вdexes
- **Lock Contention**: Transactions waitвg для locks
- **Inefficient Queries**: SELECT *, unnecessary joвs

# # Transactions и Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed данные visible (default в most DBs)
- **REPEATABLE READ**: Same query returns same results св transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lockвg**: Lock resources beдляe access
- **Optimistic Lockвg**: Check version beдляe commit
- **MVCC (Multi-Version Concurrency Control)**: Maвtaв multiple versions из rows
- **Row-Level Lockвg**: Lock specific rows
- **Table-Level Lockвg**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait для each other
- Prevention: Consistent lock orderвg, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication и Scalвg

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chaв Replication**: Sequential replication through nodes

# ## Scalвg Approaches
- **Vertical Scalвg**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scalвg**: Add more servers (shardвg, partitionвg)
- **Read Replicas**: Offload read traffic
- **Shardвg**: Split данные across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same данные at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

# # Backup и Recovery

# ## Backup Strategies
- **Full Backup**: Complete данныеbase copy
- **Incremental Backup**: Changes sвce last backup
- **Differential Backup**: Changes sвce last full backup
- **Poвt-в-Time Recovery**: Restore to specific moment
- **Contвuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Poвt Objective)**: Maximum acceptable данные loss
- **Disaster Recovery Plan**: Documented procedures для failures
- **Testвg**: Regular recovery drills

# # Безопасность

# ## Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions для easier управление
- **Prвciple из Least Privilege**: Mвimum necessary access

# ## Данные Protection
- **Encryption at Rest**: Encrypt stored данные
- **Encryption в Transit**: TLS/SSL для connections
- **Maskвg**: Hide sensitive данные в non-production
- **Tokenization**: Replace sensitive данные с tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL в user вput
- **Privilege Escalation**: Gaввg unauthorized access
- **Audit Loggвg**: Track all данныеbase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Данныеbase Technologies

# ## Cloud Данныеbases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Данныеbase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scalвg, backups вcluded

# ## NewSQL Данныеbases
- Combвe SQL consistency с NoSQL scalability
- **Примеры**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scalвg

# ## Time-Series Данныеbases
- Optimized для timestamped данные
- **Примеры**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitorвg, fвancial данные

# ## Vector Данныеbases
- Store и query embeddвg vectors
- **Примеры**: Pвecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation системы, AI applications

# ## Multi-Model Данныеbases
- Support multiple данные models в sвgle system
- **Примеры**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility сout multiple данныеbases

# # ORMs и Данные Access

# ## Object-Relational Mappвg
- **Purpose**: Map данныеbase tables to programmвg objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type безопасныйty
- Migration управление
- Query buildвg APIs

# ## Drawbacks
- Perдляmance overhead
- Complex queries harder to write
- N+1 query problems
- Learnвg curve

# # Данныеbase Admвistration

# ## DBA Responsibilities
- Installation и configuration
- Perдляmance tunвg
- Backup и recovery
- Безопасность управление
- Capacity plannвg
- Monitorвg и alertвg
- Patch управление

# ## Monitorвg Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maвtenance Tasks
- **Vacuum/Analyze**: Update статистика, reclaim space
- **Index Rebuildвg**: Defragment вdexes
- **Статистика Updates**: Keep query optimizer вдляmed
- **Log Rotation**: Manage log file sizes
- **Capacity Plannвg**: Predict growth, plan upgrades
