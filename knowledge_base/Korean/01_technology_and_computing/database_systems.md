<!-- 
This file was automatically translated from English to Korean.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이 터base 시스템

# # 데이 터base 기초

# ## What is a 데이 터base?
A 데이 터base is an organized collection 구조화된 mation stored electronically, designed efficient retrieval, sertion, updat, deletion 데이 터.

# ## 데이 터base 관리 시스템 (DBMS)
Stware that teracts 함께 end users, applications, 데이 터base itself to capture analyze 데이 터. 예시: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization 데이 터base (표, fields, relationships)
- **Instance**: Actual 데이 터 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organiz 데이 터 to reduce redundancy
- **Denormalization**: Add redundancy to improve read permance

# # Relational 데이 터bases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) columns (fields)
- **Primary Key**: Unique identifier each row
- **Foreign Key**: 참조 to primary key anor table
- **Indexes**: 데이 터 structures improv query speed
- **Views**: Virtual 표 based on query results
- **Stored Procedures**: Precompiled SQL 코드 블록
- **Triggers**: Automatic actions on 데이 터 changes

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
- **NER JO**: Returns match rows from both 표
- **LEFT JO**: All rows from left table, matches from right
- **RIGHT JO**: All rows from right table, matches from left
- **FULL OUTER JO**: All rows from both 표
- **CROSS JO**: Cartesian product both 표
- **SELF JO**: Table joed 함께 itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeat groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on or non-key attributes)
- **BCNF**: Stronger 3NF, every determant is a cidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No jo dependencies

# ## Popular RDBMS
- **PostgreSQL**: 고급 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 웹 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microst ecosystem, tegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL k, open-source

# # NoSQL 데이 터bases

# ## Types NoSQL 데이 터bases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 관리, catalogs, user priles
- **예시**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cach, sessions, shopp c예술
- **예시**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited query

# ### Column-Family Stores
- **Structure**: Columns grouped 로 families
- **Use Cases**: Big 데이 터, analytics, time-series
- **예시**: Cassra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph 데이 터bases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social 네트워크s, fraud detection, recommendations
- **예시**: Neo4j, Amazon Neptune, ArangoDB
- **Query 언어**: Cypher (Neo4j), Greml

# ## When to Use NoSQL
- Flexible/evolv schema
- Horizontal scal requirements
- High write throughput
- Hierarchical/nested 데이 터
- Distributed 시스템
- Real-time applications

# # 데이 터base Design

# ## Entity-Relationship Model
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardality**: Number stances relationship

# ## Schema Design Patterns
- **Sle Table Inheritance**: All types one table 함께 type discrimator
- **Class Table Inheritance**: Separate 표 base subclasses
- **Concrete Table Inheritance**: Separate table each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Index Strategies
- **B-Tree**: Default, range queries, sort
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 데이 터 (GIS)
- **Composite**: Multiple columns combed
- **Cover**: Includes all columns needed query

# # Query Optimization

# ## Execution Plans
- Underst how 데이 터base executes queries
- Identify bottlenecks (full table scans, miss dexes)
- Tools: EXPLA, EXPLA ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate dexes
- **Query Rewrit**: Simplify complex queries
- **Jo Optimization**: Choose correct jo types order
- **Partition**: Split large 표 (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cach**: Store frequent query results

# ## Common Permance Issues
- **N+1 Query Problem**: Fetch related 데이 터 efficiently
- **Miss Indexes**: Full table scans on large 표
- **Over-dex**: Slow writes due to too many dexes
- **Lock Contention**: Transactions wait locks
- **Inefficient Queries**: SELECT *, unnecessary jos

# # Transactions Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 데이 터 visible (default most DBs)
- **REPEATABLE READ**: Same query returns same results 함께 transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lock**: Lock resources 전에 access
- **Optimistic Lock**: Check version 전에 commit
- **MVCC (Multi-Version Concurrency Control)**: Mata multiple versions rows
- **Row-Level Lock**: Lock specific rows
- **Table-Level Lock**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait each or
- Prevention: Consistent lock order, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication Scal

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Cha Replication**: Sequential replication through nodes

# ## Scal Approaches
- **Vertical Scal**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scal**: Add more servers (shard, partition)
- **Read Replicas**: Offload read traffic
- **Shard**: Split 데이 터 across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same 데이 터 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees ir own updates immediately

# # Backup Recovery

# ## Backup Strategies
- **Full Backup**: Complete 데이 터base copy
- **Incremental Backup**: Changes sce last backup
- **Differential Backup**: Changes sce last full backup
- **Pot--Time Recovery**: Restore to specific moment
- **Contuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Pot Objective)**: Maximum acceptable 데이 터 loss
- **Disaster Recovery Plan**: Documented procedures failures
- **Test**: Regular recovery drills

# # 보안

# ## Access Control
- **Auntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions easier 관리
- **Prciple Least Privilege**: Mimum necessary access

# ## 데이 터 Protection
- **Encryption at Rest**: Encrypt stored 데이 터
- **Encryption Transit**: TLS/SSL connections
- **Mask**: Hide sensitive 데이 터 non-production
- **Tokenization**: Replace sensitive 데이 터 함께 tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL user put
- **Privilege Escalation**: Ga unauthorized access
- **Audit Logg**: Track all 데이 터base activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern 데이 터base Technologies

# ## Cloud 데이 터bases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 데이 터base, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scal, backups 포함하다d

# ## NewSQL 데이 터bases
- Combe SQL consistency 함께 NoSQL scalability
- **예시**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scal

# ## Time-Series 데이 터bases
- Optimized timestamped 데이 터
- **예시**: InfluxDB, TimescaleDB, Promeus
- **Use Cases**: IoT, monitor, fancial 데이 터

# ## Vector 데이 터bases
- Store query embedd vectors
- **예시**: Pecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 시스템, 인공 지능 applications

# ## Multi-Model 데이 터bases
- Support multiple 데이 터 models sle system
- **예시**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility 함께out multiple 데이 터bases

# # ORMs 데이 터 Access

# ## Object-Relational Mapp
- **Purpose**: Map 데이 터base 표 to programm objects
- **Popular ORMs**:
 - Python: SQLAlchemy, Django ORM, Peewee
 - JavaScript: Sequelize, Prisma, TypeORM
 - Java: Hibernate, JPA
 - Ruby: ActiveRecord
 - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type 안전한ty
- Migration 관리
- Query build APIs

# ## Drawbacks
- Permance overhead
- Complex queries harder to write
- N+1 query problems
- Learn curve

# # 데이 터base Admistration

# ## DBA Responsibilities
- Installation configuration
- Permance tun
- Backup recovery
- 보안 관리
- Capacity plann
- Monitor alert
- Patch 관리

# ## Monitor Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Matenance Tasks
- **Vacuum/Analyze**: Update 통계, reclaim space
- **Index Rebuild**: Defragment dexes
- **통계 Updates**: Keep query optimizer med
- **Log Rotation**: Manage log file sizes
- **Capacity Plann**: Predict growth, plan upgrades
