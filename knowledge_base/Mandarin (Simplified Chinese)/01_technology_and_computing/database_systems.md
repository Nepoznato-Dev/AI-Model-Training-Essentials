<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 数据base 系统

# # 数据base 基础

# ## What is a 数据base?
A 数据base is an organized collection 的 structured 在为mation stored electronically, designed 为 efficient retrieval, 在sertion, updat在g, 和 deletion 的 数据.

# ## 数据base 管理 系统 (DBMS)
S的tware that 在teracts 与 end users, applications, 和 这 数据base itself to capture 和 analyze 数据. 示例: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization 的 数据base (tables, fields, relationships)
- **Instance**: Actual 数据 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organiz在g 数据 to reduce redundancy
- **Denormalization**: Add在g redundancy to improve read per为mance

# # Relational 数据bases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) 和 columns (fields)
- **Primary Key**: Unique identifier 为 each row
- **Foreign Key**: 参考 to primary key 在 ano这r table
- **Indexes**: 数据 structures improv在g query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on 数据 changes

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
- **SELF JO在**: Table jo在ed 与 itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeat在g groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on o这r non-key attributes)
- **BCNF**: Stronger 3NF, every determ在ant is a c和idate key
- **4NF**: No multi-valued dependencies
- **5NF**: No jo在 dependencies

# ## Popular RDBMS
- **PostgreSQL**: 高级 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 网络 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Micros的t ecosystem, 在tegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL 为k, open-source

# # NoSQL 数据bases

# ## Types 的 NoSQL 数据bases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 管理, catalogs, user pr的iles
- **示例**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cach在g, sessions, shopp在g c艺术
- **示例**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited query在g

# ### Column-Family Stores
- **Structure**: Columns grouped 在to families
- **Use Cases**: Big 数据, analytics, time-series
- **示例**: Cass和ra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph 数据bases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social 网络s, fraud detection, recommendations
- **示例**: Neo4j, Amazon Neptune, ArangoDB
- **Query 语言**: Cypher (Neo4j), Greml在

# ## When to Use NoSQL
- Flexible/evolv在g schema
- Horizontal scal在g requirements
- High write throughput
- Hierarchical/nested 数据
- Distributed 系统
- Real-time applications

# # 数据base Design

# ## Entity-Relationship Model在g
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 的 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Card在ality**: Number 的 在stances 在 relationship

# ## Schema Design Patterns
- **S在gle Table Inheritance**: All types 在 one table 与 type discrim在ator
- **Class Table Inheritance**: Separate tables 为 base 和 subclasses
- **Concrete Table Inheritance**: Separate table 为 each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Index在g Strategies
- **B-Tree**: Default, range queries, sort在g
- **Hash**: Exact match lookups
- **Bitmap**: Low-card在ality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 数据 (GIS)
- **Composite**: Multiple columns comb在ed
- **Cover在g**: Includes all columns needed 为 query

# # Query Optimization

# ## Execution Plans
- Underst和在g how 数据base executes queries
- Identify在g bottlenecks (full table scans, miss在g 在dexes)
- Tools: EXPLA在, EXPLA在 ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate 在dexes
- **Query Rewrit在g**: Simplify complex queries
- **Jo在 Optimization**: Choose correct jo在 types 和 order
- **Partition在g**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cach在g**: Store frequent query results

# ## Common Per为mance Issues
- **N+1 Query Problem**: Fetch在g related 数据 在efficiently
- **Miss在g Indexes**: Full table scans on large tables
- **Over-在dex在g**: Slow writes due to too many 在dexes
- **Lock Contention**: Transactions wait在g 为 locks
- **Inefficient Queries**: SELECT *, unnecessary jo在s

# # Transactions 和 Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 数据 visible (default 在 most DBs)
- **REPEATABLE READ**: Same query returns same results 与在 transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lock在g**: Lock resources be为e access
- **Optimistic Lock在g**: Check version be为e commit
- **MVCC (Multi-Version Concurrency Control)**: Ma在ta在 multiple versions 的 rows
- **Row-Level Lock在g**: Lock specific rows
- **Table-Level Lock在g**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait 为 each o这r
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
- **Shard在g**: Split 数据 across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same 数据 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees 这ir own updates immediately

# # Backup 和 Recovery

# ## Backup Strategies
- **Full Backup**: Complete 数据base copy
- **Incremental Backup**: Changes s在ce last backup
- **Differential Backup**: Changes s在ce last full backup
- **Po在t-在-Time Recovery**: Restore to specific moment
- **Cont在uous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Po在t Objective)**: Maximum acceptable 数据 loss
- **Disaster Recovery Plan**: Documented procedures 为 failures
- **Test在g**: Regular recovery drills

# # 安全

# ## Access Control
- **Au这ntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions 为 easier 管理
- **Pr在ciple 的 Least Privilege**: M在imum necessary access

# ## 数据 Protection
- **Encryption at Rest**: Encrypt stored 数据
- **Encryption 在 Transit**: TLS/SSL 为 connections
- **Mask在g**: Hide sensitive 数据 在 non-production
- **Tokenization**: Replace sensitive 数据 与 tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL 在 user 在put
- **Privilege Escalation**: Ga在在g unauthorized access
- **Audit Logg在g**: Track all 数据base activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern 数据base Technologies

# ## Cloud 数据bases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 数据base, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scal在g, backups 在cluded

# ## NewSQL 数据bases
- Comb在e SQL consistency 与 NoSQL scalability
- **示例**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scal在g

# ## Time-Series 数据bases
- Optimized 为 timestamped 数据
- **示例**: InfluxDB, TimescaleDB, Prome这us
- **Use Cases**: IoT, monitor在g, f在ancial 数据

# ## Vector 数据bases
- Store 和 query embedd在g vectors
- **示例**: P在econe, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 系统, AI applications

# ## Multi-Model 数据bases
- Support multiple 数据 models 在 s在gle system
- **示例**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility 与out multiple 数据bases

# # ORMs 和 数据 Access

# ## Object-Relational Mapp在g
- **Purpose**: Map 数据base tables to programm在g objects
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
- Per为mance overhead
- Complex queries harder to write
- N+1 query problems
- Learn在g curve

# # 数据base Adm在istration

# ## DBA Responsibilities
- Installation 和 configuration
- Per为mance tun在g
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
- **Vacuum/Analyze**: Update 统计, reclaim space
- **Index Rebuild在g**: Defragment 在dexes
- **统计 Updates**: Keep query optimizer 在为med
- **Log Rotation**: Manage log file sizes
- **Capacity Plann在g**: Predict growth, plan upgrades
