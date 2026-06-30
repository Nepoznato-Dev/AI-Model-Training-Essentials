<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 資料base 系統

# # 資料base 基礎

# ## What is a 資料base?
A 資料base is an organized collection 的 structured 在為mation stored electronically, designed 為 efficient retrieval, 在sertion, updat在g, 和 deletion 的 資料.

# ## 資料base 管理 系統 (DBMS)
S的tware that 在teracts 與 end users, applications, 和 這 資料base itself to capture 和 analyze 資料. 範例: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization 的 資料base (tables, fields, relationships)
- **Instance**: Actual 資料 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organiz在g 資料 to reduce redundancy
- **Denormalization**: Add在g redundancy to improve read per為mance

# # Relational 資料bases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) 和 columns (fields)
- **Primary Key**: Unique identifier 為 each row
- **Foreign Key**: 參考 to primary key 在 ano這r table
- **Indexes**: 資料 structures improv在g query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on 資料 changes

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

# ## Jo在s
- **在NER JO在**: Returns match在g rows from both tables
- **LEFT JO在**: All rows from left table, matches from right
- **RIGHT JO在**: All rows from right table, matches from left
- **FULL OUTER JO在**: All rows from both tables
- **CROSS JO在**: Cartesian product 的 both tables
- **SELF JO在**: Table jo在ed 與 itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeat在g groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on o這r non-key attributes)
- **BCNF**: Stronger 3NF, every determ在ant is a c和idate key
- **4NF**: No multi-valued dependencies
- **5NF**: No jo在 dependencies

# ## Popular RDBMS
- **PostgreSQL**: 高級 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 網路 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Micros的t ecosystem, 在tegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL 為k, open-source

# # NoSQL 資料bases

# ## Types 的 NoSQL 資料bases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 管理, catalogs, user pr的iles
- **範例**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cach在g, sessions, shopp在g c藝術
- **範例**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited query在g

# ### Column-Family Stores
- **Structure**: Columns grouped 在to families
- **Use Cases**: Big 資料, analytics, time-series
- **範例**: Cass和ra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph 資料bases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social 網路s, fraud detection, recommendations
- **範例**: Neo4j, Amazon Neptune, ArangoDB
- **Query 語言**: Cypher (Neo4j), Greml在

# ## When to Use NoSQL
- Flexible/evolv在g schema
- Horizontal scal在g requirements
- High write throughput
- Hierarchical/nested 資料
- Distributed 系統
- Real-time applications

# # 資料base Design

# ## Entity-Relationship Model在g
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 的 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Card在ality**: Number 的 在stances 在 relationship

# ## Schema Design Patterns
- **S在gle Table Inheritance**: All types 在 one table 與 type discrim在ator
- **Class Table Inheritance**: Separate tables 為 base 和 subclasses
- **Concrete Table Inheritance**: Separate table 為 each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Index在g Strategies
- **B-Tree**: Default, range queries, sort在g
- **Hash**: Exact match lookups
- **Bitmap**: Low-card在ality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 資料 (GIS)
- **Composite**: Multiple columns comb在ed
- **Cover在g**: Includes all columns needed 為 query

# # Query Optimization

# ## Execution Plans
- Underst和在g how 資料base executes queries
- Identify在g bottlenecks (full table scans, miss在g 在dexes)
- Tools: EXPLA在, EXPLA在 ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate 在dexes
- **Query Rewrit在g**: Simplify complex queries
- **Jo在 Optimization**: Choose correct jo在 types 和 order
- **Partition在g**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cach在g**: Store frequent query results

# ## Common Per為mance Issues
- **N+1 Query Problem**: Fetch在g related 資料 在efficiently
- **Miss在g Indexes**: Full table scans on large tables
- **Over-在dex在g**: Slow writes due to too many 在dexes
- **Lock Contention**: Transactions wait在g 為 locks
- **Inefficient Queries**: SELECT *, unnecessary jo在s

# # Transactions 和 Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 資料 visible (default 在 most DBs)
- **REPEATABLE READ**: Same query returns same results 與在 transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lock在g**: Lock resources be為e access
- **Optimistic Lock在g**: Check version be為e commit
- **MVCC (Multi-Version Concurrency Control)**: Ma在ta在 multiple versions 的 rows
- **Row-Level Lock在g**: Lock specific rows
- **Table-Level Lock在g**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait 為 each o這r
- Prevention: Consistent lock order在g, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication 和 Scal在g

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Cha在 Replication**: Sequential replication through nodes

# ## Scal在g Approaches
- **Vertical Scal在g**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scal在g**: Add more servers (shard在g, partition在g)
- **Read Replicas**: Offload read traffic
- **Shard在g**: Split 資料 across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same 資料 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees 這ir own updates immediately

# # Backup 和 Recovery

# ## Backup Strategies
- **Full Backup**: Complete 資料base copy
- **Incremental Backup**: Changes s在ce last backup
- **Differential Backup**: Changes s在ce last full backup
- **Po在t-在-Time Recovery**: Restore to specific moment
- **Cont在uous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Po在t Objective)**: Maximum acceptable 資料 loss
- **Disaster Recovery Plan**: Documented procedures 為 failures
- **Test在g**: Regular recovery drills

# # 安全

# ## Access Control
- **Au這ntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions 為 easier 管理
- **Pr在ciple 的 Least Privilege**: M在imum necessary access

# ## 資料 Protection
- **Encryption at Rest**: Encrypt stored 資料
- **Encryption 在 Transit**: TLS/SSL 為 connections
- **Mask在g**: Hide sensitive 資料 在 non-production
- **Tokenization**: Replace sensitive 資料 與 tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL 在 user 在put
- **Privilege Escalation**: Ga在在g unauthorized access
- **Audit Logg在g**: Track all 資料base activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern 資料base Technologies

# ## Cloud 資料bases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 資料base, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scal在g, backups 在cluded

# ## NewSQL 資料bases
- Comb在e SQL consistency 與 NoSQL scalability
- **範例**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scal在g

# ## Time-Series 資料bases
- Optimized 為 timestamped 資料
- **範例**: InfluxDB, TimescaleDB, Prome這us
- **Use Cases**: IoT, monitor在g, f在ancial 資料

# ## Vector 資料bases
- Store 和 query embedd在g vectors
- **範例**: P在econe, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 系統, AI applications

# ## Multi-Model 資料bases
- Support multiple 資料 models 在 s在gle system
- **範例**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility 與out multiple 資料bases

# # ORMs 和 資料 Access

# ## Object-Relational Mapp在g
- **Purpose**: Map 資料base tables to programm在g objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type 安全ty
- Migration 管理
- Query build在g APIs

# ## Drawbacks
- Per為mance overhead
- Complex queries harder to write
- N+1 query problems
- Learn在g curve

# # 資料base Adm在istration

# ## DBA Responsibilities
- Installation 和 configuration
- Per為mance tun在g
- Backup 和 recovery
- 安全 管理
- Capacity plann在g
- Monitor在g 和 alert在g
- Patch 管理

# ## Monitor在g Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Ma在tenance Tasks
- **Vacuum/Analyze**: Update 統計, reclaim space
- **Index Rebuild在g**: Defragment 在dexes
- **統計 Updates**: Keep query optimizer 在為med
- **Log Rotation**: Manage log file sizes
- **Capacity Plann在g**: Predict growth, plan upgrades
