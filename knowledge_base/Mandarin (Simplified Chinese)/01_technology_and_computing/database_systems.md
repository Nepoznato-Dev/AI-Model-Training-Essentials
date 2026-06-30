<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 数据base 系统

# # 数据base 基础

# ## What is a 数据base?
A 数据base is an organized collection 的 结构化 mation stored electronically, designed efficient retrieval, sertion, updat, 和 deletion 的 数据.

# ## 数据base 管理 系统 (DBMS)
S的tware that teracts 与 end users, applications, 和 数据base itself to capture 和 analyze 数据. 示例: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization 的 数据base (表格, fields, relationships)
- **Instance**: Actual 数据 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organiz 数据 to reduce redundancy
- **Denormalization**: Add redundancy to improve read permance

# # Relational 数据bases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) 和 columns (fields)
- **Primary Key**: Unique identifier each row
- **Foreign Key**: 参考 to primary key anor table
- **Indexes**: 数据 structures improv query speed
- **Views**: Virtual 表格 based on query results
- **Stored Procedures**: Precompiled SQL 代码块
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

# ## Jos
- **NER JO**: Returns match rows from both 表格
- **LEFT JO**: All rows from left table, matches from right
- **RIGHT JO**: All rows from right table, matches from left
- **FULL OUTER JO**: All rows from both 表格
- **CROSS JO**: Cartesian product 的 both 表格
- **SELF JO**: Table joed 与 itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeat groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on or non-key attributes)
- **BCNF**: Stronger 3NF, every determant is a c和idate key
- **4NF**: No multi-valued dependencies
- **5NF**: No jo dependencies

# ## Popular RDBMS
- **PostgreSQL**: 高级 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 网络 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Micros的t ecosystem, tegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL k, open-source

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
- **Use Cases**: Cach, sessions, shopp c艺术
- **示例**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited query

# ### Column-Family Stores
- **Structure**: Columns grouped 到 families
- **Use Cases**: Big 数据, analytics, time-series
- **示例**: Cass和ra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph 数据bases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social 网络s, fraud detection, recommendations
- **示例**: Neo4j, Amazon Neptune, ArangoDB
- **Query 语言**: Cypher (Neo4j), Greml

# ## When to Use NoSQL
- Flexible/evolv schema
- Horizontal scal requirements
- High write throughput
- Hierarchical/nested 数据
- Distributed 系统
- Real-time applications

# # 数据base Design

# ## Entity-Relationship Model
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 的 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardality**: Number 的 stances relationship

# ## Schema Design Patterns
- **Sle Table Inheritance**: All types one table 与 type discrimator
- **Class Table Inheritance**: Separate 表格 base 和 subclasses
- **Concrete Table Inheritance**: Separate table each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Index Strategies
- **B-Tree**: Default, range queries, sort
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 数据 (GIS)
- **Composite**: Multiple columns combed
- **Cover**: Includes all columns needed query

# # Query Optimization

# ## Execution Plans
- Underst和 how 数据base executes queries
- Identify bottlenecks (full table scans, miss dexes)
- Tools: EXPLA, EXPLA ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate dexes
- **Query Rewrit**: Simplify complex queries
- **Jo Optimization**: Choose correct jo types 和 order
- **Partition**: Split large 表格 (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cach**: Store frequent query results

# ## Common Permance Issues
- **N+1 Query Problem**: Fetch related 数据 efficiently
- **Miss Indexes**: Full table scans on large 表格
- **Over-dex**: Slow writes due to too many dexes
- **Lock Contention**: Transactions wait locks
- **Inefficient Queries**: SELECT *, unnecessary jos

# # Transactions 和 Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 数据 visible (default most DBs)
- **REPEATABLE READ**: Same query returns same results 与 transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lock**: Lock resources ...之前 access
- **Optimistic Lock**: Check version ...之前 commit
- **MVCC (Multi-Version Concurrency Control)**: Mata multiple versions 的 rows
- **Row-Level Lock**: Lock specific rows
- **Table-Level Lock**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait each or
- Prevention: Consistent lock order, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication 和 Scal

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Cha Replication**: Sequential replication through nodes

# ## Scal Approaches
- **Vertical Scal**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scal**: Add more servers (shard, partition)
- **Read Replicas**: Offload read traffic
- **Shard**: Split 数据 across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same 数据 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees ir own updates immediately

# # Backup 和 Recovery

# ## Backup Strategies
- **Full Backup**: Complete 数据base copy
- **Incremental Backup**: Changes sce last backup
- **Differential Backup**: Changes sce last full backup
- **Pot--Time Recovery**: Restore to specific moment
- **Contuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Pot Objective)**: Maximum acceptable 数据 loss
- **Disaster Recovery Plan**: Documented procedures failures
- **Test**: Regular recovery drills

# # 安全

# ## Access Control
- **Auntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions easier 管理
- **Prciple 的 Least Privilege**: Mimum necessary access

# ## 数据 Protection
- **Encryption at Rest**: Encrypt stored 数据
- **Encryption Transit**: TLS/SSL connections
- **Mask**: Hide sensitive 数据 non-production
- **Tokenization**: Replace sensitive 数据 与 tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL user put
- **Privilege Escalation**: Ga unauthorized access
- **Audit Logg**: Track all 数据base activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern 数据base Technologies

# ## Cloud 数据bases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 数据base, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scal, backups 包含d

# ## NewSQL 数据bases
- Combe SQL consistency 与 NoSQL scalability
- **示例**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scal

# ## Time-Series 数据bases
- Optimized timestamped 数据
- **示例**: InfluxDB, TimescaleDB, Promeus
- **Use Cases**: IoT, monitor, 金融 数据

# ## Vector 数据bases
- Store 和 query embedd vectors
- **示例**: Pecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 系统, 人工智能 applications

# ## Multi-Model 数据bases
- Support multiple 数据 models sle system
- **示例**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility 与out multiple 数据bases

# # ORMs 和 数据 Access

# ## Object-Relational Mapp
- **Purpose**: Map 数据base 表格 to programm objects
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
- Query build APIs

# ## Drawbacks
- Permance overhead
- Complex queries harder to write
- N+1 query problems
- Learn curve

# # 数据base Admistration

# ## DBA Responsibilities
- Installation 和 configuration
- Permance tun
- Backup 和 recovery
- 安全 管理
- Capacity plann
- Monitor 和 alert
- Patch 管理

# ## Monitor Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Matenance Tasks
- **Vacuum/Analyze**: Update 统计, reclaim space
- **Index Rebuild**: Defragment dexes
- **统计 Updates**: Keep query optimizer med
- **Log Rotation**: Manage log file sizes
- **Capacity Plann**: Predict growth, plan upgrades
