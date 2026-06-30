<!-- 
This file was automatically translated from English to Korean.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이터base 시스템

# # 데이터base 기초

# ## What is a 데이터base?
A 데이터base is an organized collection 의 structured 에서위한mation stored electronically, designed 위한 efficient retrieval, 에서sertion, updat에서g, 와 deletion 의 데이터.

# ## 데이터base 관리 시스템 (DBMS)
S의tware that 에서teracts 와 함께 end users, applications, 와 그 데이터base itself to capture 와 analyze 데이터. 예시: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization 의 데이터base (tables, fields, relationships)
- **Instance**: Actual 데이터 stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organiz에서g 데이터 to reduce redundancy
- **Denormalization**: Add에서g redundancy to improve read per위한mance

# # Relational 데이터bases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) 와 columns (fields)
- **Primary Key**: Unique identifier 위한 each row
- **Foreign Key**: 참조 to primary key 에서 ano그r table
- **Indexes**: 데이터 structures improv에서g query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on 데이터 changes

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

# ## Jo에서s
- **에서NER JO에서**: Returns match에서g rows from both tables
- **LEFT JO에서**: All rows from left table, matches from right
- **RIGHT JO에서**: All rows from right table, matches from left
- **FULL OUTER JO에서**: All rows from both tables
- **CROSS JO에서**: Cartesian product 의 both tables
- **SELF JO에서**: Table jo에서ed 와 함께 itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeat에서g groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on o그r non-key attributes)
- **BCNF**: Stronger 3NF, every determ에서ant is a c와idate key
- **4NF**: No multi-valued dependencies
- **5NF**: No jo에서 dependencies

# ## Popular RDBMS
- **PostgreSQL**: 고급 features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, 웹 applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Micros의t ecosystem, 에서tegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL 위한k, open-source

# # NoSQL 데이터bases

# ## Types 의 NoSQL 데이터bases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content 관리, catalogs, user pr의iles
- **예시**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cach에서g, sessions, shopp에서g c예술
- **예시**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited query에서g

# ### Column-Family Stores
- **Structure**: Columns grouped 에서to families
- **Use Cases**: Big 데이터, analytics, time-series
- **예시**: Cass와ra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph 데이터bases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social 네트워크s, fraud detection, recommendations
- **예시**: Neo4j, Amazon Neptune, ArangoDB
- **Query 언어**: Cypher (Neo4j), Greml에서

# ## When to Use NoSQL
- Flexible/evolv에서g schema
- Horizontal scal에서g requirements
- High write throughput
- Hierarchical/nested 데이터
- Distributed 시스템
- Real-time applications

# # 데이터base Design

# ## Entity-Relationship Model에서g
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties 의 entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Card에서ality**: Number 의 에서stances 에서 relationship

# ## Schema Design Patterns
- **S에서gle Table Inheritance**: All types 에서 one table 와 함께 type discrim에서ator
- **Class Table Inheritance**: Separate tables 위한 base 와 subclasses
- **Concrete Table Inheritance**: Separate table 위한 each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Index에서g Strategies
- **B-Tree**: Default, range queries, sort에서g
- **Hash**: Exact match lookups
- **Bitmap**: Low-card에서ality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic 데이터 (GIS)
- **Composite**: Multiple columns comb에서ed
- **Cover에서g**: Includes all columns needed 위한 query

# # Query Optimization

# ## Execution Plans
- Underst와에서g how 데이터base executes queries
- Identify에서g bottlenecks (full table scans, miss에서g 에서dexes)
- Tools: EXPLA에서, EXPLA에서 ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate 에서dexes
- **Query Rewrit에서g**: Simplify complex queries
- **Jo에서 Optimization**: Choose correct jo에서 types 와 order
- **Partition에서g**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cach에서g**: Store frequent query results

# ## Common Per위한mance Issues
- **N+1 Query Problem**: Fetch에서g related 데이터 에서efficiently
- **Miss에서g Indexes**: Full table scans on large tables
- **Over-에서dex에서g**: Slow writes due to too many 에서dexes
- **Lock Contention**: Transactions wait에서g 위한 locks
- **Inefficient Queries**: SELECT *, unnecessary jo에서s

# # Transactions 와 Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed 데이터 visible (default 에서 most DBs)
- **REPEATABLE READ**: Same query returns same results 와 함께에서 transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lock에서g**: Lock resources be위한e access
- **Optimistic Lock에서g**: Check version be위한e commit
- **MVCC (Multi-Version Concurrency Control)**: Ma에서ta에서 multiple versions 의 rows
- **Row-Level Lock에서g**: Lock specific rows
- **Table-Level Lock에서g**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait 위한 each o그r
- Prevention: Consistent lock order에서g, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication 와 Scal에서g

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Cha에서 Replication**: Sequential replication through nodes

# ## Scal에서g Approaches
- **Vertical Scal에서g**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scal에서g**: Add more servers (shard에서g, partition에서g)
- **Read Replicas**: Offload read traffic
- **Shard에서g**: Split 데이터 across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same 데이터 at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees 그ir own updates immediately

# # Backup 와 Recovery

# ## Backup Strategies
- **Full Backup**: Complete 데이터base copy
- **Incremental Backup**: Changes s에서ce last backup
- **Differential Backup**: Changes s에서ce last full backup
- **Po에서t-에서-Time Recovery**: Restore to specific moment
- **Cont에서uous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Po에서t Objective)**: Maximum acceptable 데이터 loss
- **Disaster Recovery Plan**: Documented procedures 위한 failures
- **Test에서g**: Regular recovery drills

# # 보안

# ## Access Control
- **Au그ntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions 위한 easier 관리
- **Pr에서ciple 의 Least Privilege**: M에서imum necessary access

# ## 데이터 Protection
- **Encryption at Rest**: Encrypt stored 데이터
- **Encryption 에서 Transit**: TLS/SSL 위한 connections
- **Mask에서g**: Hide sensitive 데이터 에서 non-production
- **Tokenization**: Replace sensitive 데이터 와 함께 tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL 에서 user 에서put
- **Privilege Escalation**: Ga에서에서g unauthorized access
- **Audit Logg에서g**: Track all 데이터base activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern 데이터base Technologies

# ## Cloud 데이터bases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL 데이터base, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scal에서g, backups 에서cluded

# ## NewSQL 데이터bases
- Comb에서e SQL consistency 와 함께 NoSQL scalability
- **예시**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scal에서g

# ## Time-Series 데이터bases
- Optimized 위한 timestamped 데이터
- **예시**: InfluxDB, TimescaleDB, Prome그us
- **Use Cases**: IoT, monitor에서g, f에서ancial 데이터

# ## Vector 데이터bases
- Store 와 query embedd에서g vectors
- **예시**: P에서econe, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation 시스템, AI applications

# ## Multi-Model 데이터bases
- Support multiple 데이터 models 에서 s에서gle system
- **예시**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility 와 함께out multiple 데이터bases

# # ORMs 와 데이터 Access

# ## Object-Relational Mapp에서g
- **Purpose**: Map 데이터base tables to programm에서g objects
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
- Query build에서g APIs

# ## Drawbacks
- Per위한mance overhead
- Complex queries harder to write
- N+1 query problems
- Learn에서g curve

# # 데이터base Adm에서istration

# ## DBA Responsibilities
- Installation 와 configuration
- Per위한mance tun에서g
- Backup 와 recovery
- 보안 관리
- Capacity plann에서g
- Monitor에서g 와 alert에서g
- Patch 관리

# ## Monitor에서g Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Ma에서tenance Tasks
- **Vacuum/Analyze**: Update 통계, reclaim space
- **Index Rebuild에서g**: Defragment 에서dexes
- **통계 Updates**: Keep query optimizer 에서위한med
- **Log Rotation**: Manage log file sizes
- **Capacity Plann에서g**: Predict growth, plan upgrades
