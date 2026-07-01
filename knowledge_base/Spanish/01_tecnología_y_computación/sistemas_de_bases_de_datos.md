<!-- 
This file was automatically translated from English to Spanish.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Datosbase Sistemas

# # Datosbase Fundamentos

# ## What is a Datosbase?
A datosbase is an organized collection de structured enparamation stored electronically, designed para efficient retrieval, ensertion, updateng, y deletion de datos.

# ## Datosbase Gestión Sistemas (DBMS)
Sdetware that enteracts con end users, applications, y el/la datosbase itself to capture y analyze datos. Ejemplos: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization de datosbase (tables, fields, relationships)
- **Instance**: Actual datos stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizeng datos to reduce redundancy
- **Denormalization**: Addeng redundancy to improve read perparamance

# # Relational Datosbases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) y columns (fields)
- **Primary Key**: Unique identifier para each row
- **Foreign Key**: Referencia to primary key en anoel/lar table
- **Indexes**: Datos structures improveng query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on datos changes

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

# ## Joens
- **ENNER JOEN**: Returns matcheng rows from both tables
- **LEFT JOEN**: All rows from left table, matches from right
- **RIGHT JOEN**: All rows from right table, matches from left
- **FULL OUTER JOEN**: All rows from both tables
- **CROSS JOEN**: Cartesian product de both tables
- **SELF JOEN**: Table joened con itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeateng groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on oel/lar non-key attributes)
- **BCNF**: Stronger 3NF, every determenant is a cyidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No joen dependencies

# ## Popular RDBMS
- **PostgreSQL**: Avanzado features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsdet ecosystem, entegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL parak, open-source

# # NoSQL Datosbases

# ## Types de NoSQL Datosbases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content gestión, catalogs, user prdeiles
- **Ejemplos**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cacheng, sessions, shoppeng cartes
- **Ejemplos**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited queryeng

# ### Column-Family Stores
- **Structure**: Columns grouped ento families
- **Use Cases**: Big datos, analytics, time-series
- **Ejemplos**: Cassyra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Datosbases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social reds, fraud detection, recommendations
- **Ejemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Query Idioma**: Cypher (Neo4j), Gremlen

# ## When to Use NoSQL
- Flexible/evolveng schema
- Horizontal scaleng requirements
- High write throughput
- Hierarchical/nested datos
- Distributed sistemas
- Real-time applications

# # Datosbase Design

# ## Entity-Relationship Modeleng
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties de entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardenality**: Number de enstances en relationship

# ## Schema Design Patterns
- **Sengle Table Inheritance**: All types en one table con type discrimenator
- **Class Table Inheritance**: Separate tables para base y subclasses
- **Concrete Table Inheritance**: Separate table para each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexeng Strategies
- **B-Tree**: Default, range queries, sorteng
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardenality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic datos (GIS)
- **Composite**: Multiple columns combened
- **Covereng**: Includes all columns needed para query

# # Query Optimization

# ## Execution Plans
- Understyeng how datosbase executes queries
- Identifyeng bottlenecks (full table scans, misseng endexes)
- Tools: EXPLAEN, EXPLAEN ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate endexes
- **Query Rewriteng**: Simplify complex queries
- **Joen Optimization**: Choose correct joen types y order
- **Partitioneng**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cacheng**: Store frequent query results

# ## Common Perparamance Issues
- **N+1 Query Problem**: Fetcheng related datos enefficiently
- **Misseng Indexes**: Full table scans on large tables
- **Over-endexeng**: Slow writes due to too many endexes
- **Lock Contention**: Transactions waiteng para locks
- **Inefficient Queries**: SELECT *, unnecessary joens

# # Transactions y Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed datos visible (default en most DBs)
- **REPEATABLE READ**: Same query returns same results conen transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lockeng**: Lock resources beparae access
- **Optimistic Lockeng**: Check version beparae commit
- **MVCC (Multi-Version Concurrency Control)**: Maentaen multiple versions de rows
- **Row-Level Lockeng**: Lock specific rows
- **Table-Level Lockeng**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait para each oel/lar
- Prevention: Consistent lock ordereng, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication y Scaleng

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chaen Replication**: Sequential replication through nodes

# ## Scaleng Approaches
- **Vertical Scaleng**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaleng**: Add more servers (shardeng, partitioneng)
- **Read Replicas**: Offload read traffic
- **Shardeng**: Split datos across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same datos at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees el/lair own updates immediately

# # Backup y Recovery

# ## Backup Strategies
- **Full Backup**: Complete datosbase copy
- **Incremental Backup**: Changes sence last backup
- **Differential Backup**: Changes sence last full backup
- **Poent-en-Time Recovery**: Restore to specific moment
- **Contenuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Poent Objective)**: Maximum acceptable datos loss
- **Disaster Recovery Plan**: Documented procedures para failures
- **Testeng**: Regular recovery drills

# # Seguridad

# ## Access Control
- **Auel/lantication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions para easier gestión
- **Prenciple de Least Privilege**: Menimum necessary access

# ## Datos Protection
- **Encryption at Rest**: Encrypt stored datos
- **Encryption en Transit**: TLS/SSL para connections
- **Maskeng**: Hide sensitive datos en non-production
- **Tokenization**: Replace sensitive datos con tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL en user enput
- **Privilege Escalation**: Gaeneng unauthorized access
- **Audit Loggeng**: Track all datosbase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Datosbase Technologies

# ## Cloud Datosbases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Datosbase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaleng, backups encluded

# ## NewSQL Datosbases
- Combene SQL consistency con NoSQL scalability
- **Ejemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaleng

# ## Time-Series Datosbases
- Optimized para timestamped datos
- **Ejemplos**: InfluxDB, TimescaleDB, Promeel/laus
- **Use Cases**: IoT, monitoreng, fenancial datos

# ## Vector Datosbases
- Store y query embeddeng vectors
- **Ejemplos**: Penecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation sistemas, AI applications

# ## Multi-Model Datosbases
- Support multiple datos models en sengle system
- **Ejemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility conout multiple datosbases

# # ORMs y Datos Access

# ## Object-Relational Mappeng
- **Purpose**: Mapear tablas de base de datos a objetos de programación
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type seguroty
- Migration gestión
- Query buildeng APIs

# ## Drawbacks
- Perparamance overhead
- Complex queries harder to write
- N+1 query problems
- Learneng curve

# # Datosbase Admenistration

# ## DBA Responsibilities
- Installation y configuration
- Perparamance tuneng
- Backup y recovery
- Seguridad gestión
- Capacity planneng
- Monitoreng y alerteng
- Patch gestión

# ## Monitoreng Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maentenance Tasks
- **Vacuum/Analyze**: Update estadísticas, reclaim space
- **Index Rebuildeng**: Defragment endexes
- **Estadísticas Updates**: Keep query optimizer enparamed
- **Log Rotation**: Manage log file sizes
- **Capacity Planneng**: Predict growth, plan upgrades
