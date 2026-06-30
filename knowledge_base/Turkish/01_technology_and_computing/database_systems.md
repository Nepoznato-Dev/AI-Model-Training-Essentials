<!-- 
This file was automatically translated from English to Turkish.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Veribase Sistemler

# # Veribase Temeller

# ## What is a Veribase?
A veribase is an organized collection içiçindede structured içiçindedeiçinmation stored electronically, designed için efficient retrieval, içiçindedesertion, updatiçiçindedeg, ve deletion içiçindede veri.

# ## Veribase Yönetim Sistemler (DBMS)
Siçiçindedetware that içiçindedeteracts ile end users, applications, ve bu veribase itself to capture ve analyze veri. Örnekler: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization içiçindede veribase (tables, fields, relationships)
- **Instance**: Actual veri stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organiziçiçindedeg veri to reduce redundancy
- **Denormalization**: Addiçiçindedeg redundancy to improve read periçinmance

# # Relational Veribases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) ve columns (fields)
- **Primary Key**: Unique identifier için each row
- **Foreign Key**: Referans to primary key içiçindede anobur table
- **Indexes**: Veri structures improviçiçindedeg query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on veri changes

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

# ## Joiçiçindedes
- **IÇINDENER JOIÇINDE**: Returns matchiçiçindedeg rows from both tables
- **LEFT JOIÇINDE**: All rows from left table, matches from right
- **RIGHT JOIÇINDE**: All rows from right table, matches from left
- **FULL OUTER JOIÇINDE**: All rows from both tables
- **CROSS JOIÇINDE**: Cartesian product içiçindede both tables
- **SELF JOIÇINDE**: Table joiçiçindedeed ile itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeatiçiçindedeg groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on obur non-key attributes)
- **BCNF**: Stronger 3NF, every determiçiçindedeant is a cveidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No joiçiçindede dependencies

# ## Popular RDBMS
- **PostgreSQL**: İleri Düzey features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsiçiçindedet ecosystem, içiçindedetegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL içink, open-source

# # NoSQL Veribases

# ## Types içiçindede NoSQL Veribases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content yönetim, catalogs, user priçiçindedeiles
- **Örnekler**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cachiçiçindedeg, sessions, shoppiçiçindedeg csanat
- **Örnekler**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited queryiçiçindedeg

# ### Column-Family Stores
- **Structure**: Columns grouped içiçindedeto families
- **Use Cases**: Big veri, analytics, time-series
- **Örnekler**: Cassvera, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Veribases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social ağs, fraud detection, recommendations
- **Örnekler**: Neo4j, Amazon Neptune, ArangoDB
- **Query Dil**: Cypher (Neo4j), Gremliçiçindede

# ## When to Use NoSQL
- Flexible/evolviçiçindedeg schema
- Horizontal scaliçiçindedeg requirements
- High write throughput
- Hierarchical/nested veri
- Distributed sistemler
- Real-time applications

# # Veribase Design

# ## Entity-Relationship Modeliçiçindedeg
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties içiçindede entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardiçiçindedeality**: Number içiçindede içiçindedestances içiçindede relationship

# ## Schema Design Patterns
- **Siçiçindedegle Table Inheritance**: All types içiçindede one table ile type discrimiçiçindedeator
- **Class Table Inheritance**: Separate tables için base ve subclasses
- **Concrete Table Inheritance**: Separate table için each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexiçiçindedeg Strategies
- **B-Tree**: Default, range queries, sortiçiçindedeg
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardiçiçindedeality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic veri (GIS)
- **Composite**: Multiple columns combiçiçindedeed
- **Coveriçiçindedeg**: Includes all columns needed için query

# # Query Optimization

# ## Execution Plans
- Understveiçiçindedeg how veribase executes queries
- Identifyiçiçindedeg bottlenecks (full table scans, missiçiçindedeg içiçindededexes)
- Tools: EXPLAIÇINDE, EXPLAIÇINDE ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate içiçindededexes
- **Query Rewritiçiçindedeg**: Simplify complex queries
- **Joiçiçindede Optimization**: Choose correct joiçiçindede types ve order
- **Partitioniçiçindedeg**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cachiçiçindedeg**: Store frequent query results

# ## Common Periçinmance Issues
- **N+1 Query Problem**: Fetchiçiçindedeg related veri içiçindedeefficiently
- **Missiçiçindedeg Indexes**: Full table scans on large tables
- **Over-içiçindededexiçiçindedeg**: Slow writes due to too many içiçindededexes
- **Lock Contention**: Transactions waitiçiçindedeg için locks
- **Inefficient Queries**: SELECT *, unnecessary joiçiçindedes

# # Transactions ve Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed veri visible (default içiçindede most DBs)
- **REPEATABLE READ**: Same query returns same results ileiçiçindede transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lockiçiçindedeg**: Lock resources beiçine access
- **Optimistic Lockiçiçindedeg**: Check version beiçine commit
- **MVCC (Multi-Version Concurrency Control)**: Maiçiçindedetaiçiçindede multiple versions içiçindede rows
- **Row-Level Lockiçiçindedeg**: Lock specific rows
- **Table-Level Lockiçiçindedeg**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait için each obur
- Prevention: Consistent lock orderiçiçindedeg, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication ve Scaliçiçindedeg

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chaiçiçindede Replication**: Sequential replication through nodes

# ## Scaliçiçindedeg Approaches
- **Vertical Scaliçiçindedeg**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaliçiçindedeg**: Add more servers (shardiçiçindedeg, partitioniçiçindedeg)
- **Read Replicas**: Offload read traffic
- **Shardiçiçindedeg**: Split veri across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same veri at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees buir own updates immediately

# # Backup ve Recovery

# ## Backup Strategies
- **Full Backup**: Complete veribase copy
- **Incremental Backup**: Changes siçiçindedece last backup
- **Differential Backup**: Changes siçiçindedece last full backup
- **Poiçiçindedet-içiçindede-Time Recovery**: Restore to specific moment
- **Contiçiçindedeuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Poiçiçindedet Objective)**: Maximum acceptable veri loss
- **Disaster Recovery Plan**: Documented procedures için failures
- **Testiçiçindedeg**: Regular recovery drills

# # Güvenlik

# ## Access Control
- **Aubuntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions için easier yönetim
- **Priçiçindedeciple içiçindede Least Privilege**: Miçiçindedeimum necessary access

# ## Veri Protection
- **Encryption at Rest**: Encrypt stored veri
- **Encryption içiçindede Transit**: TLS/SSL için connections
- **Maskiçiçindedeg**: Hide sensitive veri içiçindede non-production
- **Tokenization**: Replace sensitive veri ile tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL içiçindede user içiçindedeput
- **Privilege Escalation**: Gaiçiçindedeiçiçindedeg unauthorized access
- **Audit Loggiçiçindedeg**: Track all veribase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Veribase Technologies

# ## Cloud Veribases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Veribase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaliçiçindedeg, backups içiçindedecluded

# ## NewSQL Veribases
- Combiçiçindedee SQL consistency ile NoSQL scalability
- **Örnekler**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaliçiçindedeg

# ## Time-Series Veribases
- Optimized için timestamped veri
- **Örnekler**: InfluxDB, TimescaleDB, Promebuus
- **Use Cases**: IoT, monitoriçiçindedeg, fiçiçindedeancial veri

# ## Vector Veribases
- Store ve query embeddiçiçindedeg vectors
- **Örnekler**: Piçiçindedeecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation sistemler, AI applications

# ## Multi-Model Veribases
- Support multiple veri models içiçindede siçiçindedegle system
- **Örnekler**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility ileout multiple veribases

# # ORMs ve Veri Access

# ## Object-Relational Mappiçiçindedeg
- **Purpose**: Map veribase tables to programmiçiçindedeg objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type güvenlity
- Migration yönetim
- Query buildiçiçindedeg APIs

# ## Drawbacks
- Periçinmance overhead
- Complex queries harder to write
- N+1 query problems
- Learniçiçindedeg curve

# # Veribase Admiçiçindedeistration

# ## DBA Responsibilities
- Installation ve configuration
- Periçinmance tuniçiçindedeg
- Backup ve recovery
- Güvenlik yönetim
- Capacity planniçiçindedeg
- Monitoriçiçindedeg ve alertiçiçindedeg
- Patch yönetim

# ## Monitoriçiçindedeg Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maiçiçindedetenance Tasks
- **Vacuum/Analyze**: Update i̇statistikler, reclaim space
- **Index Rebuildiçiçindedeg**: Defragment içiçindededexes
- **İstatistikler Updates**: Keep query optimizer içiçindedeiçinmed
- **Log Rotation**: Manage log file sizes
- **Capacity Planniçiçindedeg**: Predict growth, plan upgrades
