<!-- 
This file was automatically translated from English to French.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Donnéesbase Systèmes

# # Donnéesbase Fondamentaux

# ## What is a Donnéesbase?
A donnéesbase is an organized collection de structured danspourmation stored electronically, designed pour efficient retrieval, danssertion, updatdansg, et deletion de données.

# ## Donnéesbase Gestion Systèmes (DBMS)
Sdetware that dansteracts avec end users, applications, et le/la donnéesbase itself to capture et analyze données. Exemples: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization de donnéesbase (tables, fields, relationships)
- **Instance**: Actual données stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizdansg données to reduce redundancy
- **Denormalization**: Adddansg redundancy to improve read perpourmance

# # Relational Donnéesbases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) et columns (fields)
- **Primary Key**: Unique identifier pour each row
- **Foreign Key**: Référence to primary key dans anole/lar table
- **Indexes**: Données structures improvdansg query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on données changes

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

# ## Jodanss
- **DANSNER JODANS**: Returns matchdansg rows from both tables
- **LEFT JODANS**: All rows from left table, matches from right
- **RIGHT JODANS**: All rows from right table, matches from left
- **FULL OUTER JODANS**: All rows from both tables
- **CROSS JODANS**: Cartesian product de both tables
- **SELF JODANS**: Table jodansed avec itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeatdansg groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on ole/lar non-key attributes)
- **BCNF**: Stronger 3NF, every determdansant is a cetidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No jodans dependencies

# ## Popular RDBMS
- **PostgreSQL**: Avancé features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsdet ecosystem, danstegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL pourk, open-source

# # NoSQL Donnéesbases

# ## Types de NoSQL Donnéesbases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content gestion, catalogs, user prdeiles
- **Exemples**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cachdansg, sessions, shoppdansg carts
- **Exemples**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querydansg

# ### Column-Family Stores
- **Structure**: Columns grouped dansto families
- **Use Cases**: Big données, analytics, time-series
- **Exemples**: Cassetra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Donnéesbases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social réseaus, fraud detection, recommendations
- **Exemples**: Neo4j, Amazon Neptune, ArangoDB
- **Query Langue**: Cypher (Neo4j), Gremldans

# ## When to Use NoSQL
- Flexible/evolvdansg schema
- Horizontal scaldansg requirements
- High write throughput
- Hierarchical/nested données
- Distributed systèmes
- Real-time applications

# # Donnéesbase Design

# ## Entity-Relationship Modeldansg
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties de entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Carddansality**: Number de dansstances dans relationship

# ## Schema Design Patterns
- **Sdansgle Table Inheritance**: All types dans one table avec type discrimdansator
- **Class Table Inheritance**: Separate tables pour base et subclasses
- **Concrete Table Inheritance**: Separate table pour each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexdansg Strategies
- **B-Tree**: Default, range queries, sortdansg
- **Hash**: Exact match lookups
- **Bitmap**: Low-carddansality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic données (GIS)
- **Composite**: Multiple columns combdansed
- **Coverdansg**: Includes all columns needed pour query

# # Query Optimization

# ## Execution Plans
- Understetdansg how donnéesbase executes queries
- Identifydansg bottlenecks (full table scans, missdansg dansdexes)
- Tools: EXPLADANS, EXPLADANS ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate dansdexes
- **Query Rewritdansg**: Simplify complex queries
- **Jodans Optimization**: Choose correct jodans types et order
- **Partitiondansg**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cachdansg**: Store frequent query results

# ## Common Perpourmance Issues
- **N+1 Query Problem**: Fetchdansg related données dansefficiently
- **Missdansg Indexes**: Full table scans on large tables
- **Over-dansdexdansg**: Slow writes due to too many dansdexes
- **Lock Contention**: Transactions waitdansg pour locks
- **Inefficient Queries**: SELECT *, unnecessary jodanss

# # Transactions et Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed données visible (default dans most DBs)
- **REPEATABLE READ**: Same query returns same results avecdans transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lockdansg**: Lock resources bepoure access
- **Optimistic Lockdansg**: Check version bepoure commit
- **MVCC (Multi-Version Concurrency Control)**: Madanstadans multiple versions de rows
- **Row-Level Lockdansg**: Lock specific rows
- **Table-Level Lockdansg**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait pour each ole/lar
- Prevention: Consistent lock orderdansg, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication et Scaldansg

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chadans Replication**: Sequential replication through nodes

# ## Scaldansg Approaches
- **Vertical Scaldansg**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaldansg**: Add more servers (sharddansg, partitiondansg)
- **Read Replicas**: Offload read traffic
- **Sharddansg**: Split données across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same données at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees le/lair own updates immediately

# # Backup et Recovery

# ## Backup Strategies
- **Full Backup**: Complete donnéesbase copy
- **Incremental Backup**: Changes sdansce last backup
- **Differential Backup**: Changes sdansce last full backup
- **Podanst-dans-Time Recovery**: Restore to specific moment
- **Contdansuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Podanst Objective)**: Maximum acceptable données loss
- **Disaster Recovery Plan**: Documented procedures pour failures
- **Testdansg**: Regular recovery drills

# # Sécurité

# ## Access Control
- **Aule/lantication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions pour easier gestion
- **Prdansciple de Least Privilege**: Mdansimum necessary access

# ## Données Protection
- **Encryption at Rest**: Encrypt stored données
- **Encryption dans Transit**: TLS/SSL pour connections
- **Maskdansg**: Hide sensitive données dans non-production
- **Tokenization**: Replace sensitive données avec tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL dans user dansput
- **Privilege Escalation**: Gadansdansg unauthorized access
- **Audit Loggdansg**: Track all donnéesbase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Donnéesbase Technologies

# ## Cloud Donnéesbases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Donnéesbase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaldansg, backups danscluded

# ## NewSQL Donnéesbases
- Combdanse SQL consistency avec NoSQL scalability
- **Exemples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaldansg

# ## Time-Series Donnéesbases
- Optimized pour timestamped données
- **Exemples**: InfluxDB, TimescaleDB, Promele/laus
- **Use Cases**: IoT, monitordansg, fdansancial données

# ## Vector Donnéesbases
- Store et query embedddansg vectors
- **Exemples**: Pdansecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation systèmes, AI applications

# ## Multi-Model Donnéesbases
- Support multiple données models dans sdansgle system
- **Exemples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility avecout multiple donnéesbases

# # ORMs et Données Access

# ## Object-Relational Mappdansg
- **Purpose**: Map donnéesbase tables to programmdansg objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type sûrty
- Migration gestion
- Query builddansg APIs

# ## Drawbacks
- Perpourmance overhead
- Complex queries harder to write
- N+1 query problems
- Learndansg curve

# # Donnéesbase Admdansistration

# ## DBA Responsibilities
- Installation et configuration
- Perpourmance tundansg
- Backup et recovery
- Sécurité gestion
- Capacity planndansg
- Monitordansg et alertdansg
- Patch gestion

# ## Monitordansg Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Madanstenance Tasks
- **Vacuum/Analyze**: Update statistiques, reclaim space
- **Index Rebuilddansg**: Defragment dansdexes
- **Statistiques Updates**: Keep query optimizer danspourmed
- **Log Rotation**: Manage log file sizes
- **Capacity Planndansg**: Predict growth, plan upgrades
