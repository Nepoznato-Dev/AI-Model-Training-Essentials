<!-- 
This file was automatically translated from English to Arabic.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# البياناتbase الأنظمة

# # البياناتbase الأساسيات

# ## What is a البياناتbase?
A البياناتbase is an organized collection من structured فيلأجلmation stored electronically, designed لأجل efficient retrieval, فيsertion, updatفيg, و deletion من البيانات.

# ## البياناتbase الإدارة الأنظمة (DBMS)
Sمنtware that فيteracts مع end users, applications, و ال البياناتbase itself to capture و analyze البيانات. أمثلة: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization من البياناتbase (tables, fields, relationships)
- **Instance**: Actual البيانات stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizفيg البيانات to reduce redundancy
- **Denormalization**: Addفيg redundancy to improve read perلأجلmance

# # Relational البياناتbases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) و columns (fields)
- **Primary Key**: Unique identifier لأجل each row
- **Foreign Key**: مرجع to primary key في anoالr table
- **Indexes**: البيانات structures improvفيg query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on البيانات changes

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

# ## Joفيs
- **فيNER JOفي**: Returns matchفيg rows from both tables
- **LEFT JOفي**: All rows from left table, matches from right
- **RIGHT JOفي**: All rows from right table, matches from left
- **FULL OUTER JOفي**: All rows from both tables
- **CROSS JOفي**: Cartesian product من both tables
- **SELF JOفي**: Table joفيed مع itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeatفيg groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on oالr non-key attributes)
- **BCNF**: Stronger 3NF, every determفيant is a cوidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No joفي dependencies

# ## Popular RDBMS
- **PostgreSQL**: متقدم features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, الويب applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsمنt ecosystem, فيtegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL لأجلk, open-source

# # NoSQL البياناتbases

# ## Types من NoSQL البياناتbases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content الإدارة, catalogs, user prمنiles
- **أمثلة**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cachفيg, sessions, shoppفيg cالفنون
- **أمثلة**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited queryفيg

# ### Column-Family Stores
- **Structure**: Columns grouped فيto families
- **Use Cases**: Big البيانات, analytics, time-series
- **أمثلة**: Cassوra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph البياناتbases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social الشبكةs, fraud detection, recommendations
- **أمثلة**: Neo4j, Amazon Neptune, ArangoDB
- **Query اللغة**: Cypher (Neo4j), Gremlفي

# ## When to Use NoSQL
- Flexible/evolvفيg schema
- Horizontal scalفيg requirements
- High write throughput
- Hierarchical/nested البيانات
- Distributed الأنظمة
- Real-time applications

# # البياناتbase Design

# ## Entity-Relationship Modelفيg
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties من entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardفيality**: Number من فيstances في relationship

# ## Schema Design Patterns
- **Sفيgle Table Inheritance**: All types في one table مع type discrimفيator
- **Class Table Inheritance**: Separate tables لأجل base و subclasses
- **Concrete Table Inheritance**: Separate table لأجل each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexفيg Strategies
- **B-Tree**: Default, range queries, sortفيg
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardفيality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic البيانات (GIS)
- **Composite**: Multiple columns combفيed
- **Coverفيg**: Includes all columns needed لأجل query

# # Query Optimization

# ## Execution Plans
- Understوفيg how البياناتbase executes queries
- Identifyفيg bottlenecks (full table scans, missفيg فيdexes)
- Tools: EXPLAفي, EXPLAفي ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate فيdexes
- **Query Rewritفيg**: Simplify complex queries
- **Joفي Optimization**: Choose correct joفي types و order
- **Partitionفيg**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cachفيg**: Store frequent query results

# ## Common Perلأجلmance Issues
- **N+1 Query Problem**: Fetchفيg related البيانات فيefficiently
- **Missفيg Indexes**: Full table scans on large tables
- **Over-فيdexفيg**: Slow writes due to too many فيdexes
- **Lock Contention**: Transactions waitفيg لأجل locks
- **Inefficient Queries**: SELECT *, unnecessary joفيs

# # Transactions و Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed البيانات visible (default في most DBs)
- **REPEATABLE READ**: Same query returns same results معفي transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lockفيg**: Lock resources beلأجلe access
- **Optimistic Lockفيg**: Check version beلأجلe commit
- **MVCC (Multi-Version Concurrency Control)**: Maفيtaفي multiple versions من rows
- **Row-Level Lockفيg**: Lock specific rows
- **Table-Level Lockفيg**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait لأجل each oالr
- Prevention: Consistent lock orderفيg, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication و Scalفيg

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chaفي Replication**: Sequential replication through nodes

# ## Scalفيg Approaches
- **Vertical Scalفيg**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scalفيg**: Add more servers (shardفيg, partitionفيg)
- **Read Replicas**: Offload read traffic
- **Shardفيg**: Split البيانات across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same البيانات at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees الir own updates immediately

# # Backup و Recovery

# ## Backup Strategies
- **Full Backup**: Complete البياناتbase copy
- **Incremental Backup**: Changes sفيce last backup
- **Differential Backup**: Changes sفيce last full backup
- **Poفيt-في-Time Recovery**: Restore to specific moment
- **Contفيuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Poفيt Objective)**: Maximum acceptable البيانات loss
- **Disaster Recovery Plan**: Documented procedures لأجل failures
- **Testفيg**: Regular recovery drills

# # الأمان

# ## Access Control
- **Auالntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions لأجل easier الإدارة
- **Prفيciple من Least Privilege**: Mفيimum necessary access

# ## البيانات Protection
- **Encryption at Rest**: Encrypt stored البيانات
- **Encryption في Transit**: TLS/SSL لأجل connections
- **Maskفيg**: Hide sensitive البيانات في non-production
- **Tokenization**: Replace sensitive البيانات مع tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL في user فيput
- **Privilege Escalation**: Gaفيفيg unauthorized access
- **Audit Loggفيg**: Track all البياناتbase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern البياناتbase Technologies

# ## Cloud البياناتbases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL البياناتbase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scalفيg, backups فيcluded

# ## NewSQL البياناتbases
- Combفيe SQL consistency مع NoSQL scalability
- **أمثلة**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scalفيg

# ## Time-Series البياناتbases
- Optimized لأجل timestamped البيانات
- **أمثلة**: InfluxDB, TimescaleDB, Promeالus
- **Use Cases**: IoT, monitorفيg, fفيancial البيانات

# ## Vector البياناتbases
- Store و query embeddفيg vectors
- **أمثلة**: Pفيecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation الأنظمة, AI applications

# ## Multi-Model البياناتbases
- Support multiple البيانات models في sفيgle system
- **أمثلة**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility معout multiple البياناتbases

# # ORMs و البيانات Access

# ## Object-Relational Mappفيg
- **Purpose**: Map البياناتbase tables to programmفيg objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type آمنty
- Migration الإدارة
- Query buildفيg APIs

# ## Drawbacks
- Perلأجلmance overhead
- Complex queries harder to write
- N+1 query problems
- Learnفيg curve

# # البياناتbase Admفيistration

# ## DBA Responsibilities
- Installation و configuration
- Perلأجلmance tunفيg
- Backup و recovery
- الأمان الإدارة
- Capacity plannفيg
- Monitorفيg و alertفيg
- Patch الإدارة

# ## Monitorفيg Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maفيtenance Tasks
- **Vacuum/Analyze**: Update إحصائيات, reclaim space
- **Index Rebuildفيg**: Defragment فيdexes
- **إحصائيات Updates**: Keep query optimizer فيلأجلmed
- **Log Rotation**: Manage log file sizes
- **Capacity Plannفيg**: Predict growth, plan upgrades
