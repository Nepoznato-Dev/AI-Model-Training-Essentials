<!-- 
This file was automatically translated from English to Portuguese.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Dadosbase Sistemas

# # Dadosbase Fundamentos

# ## What is a Dadosbase?
A dadosbase is an organized collection de structured emparamation stored electronically, designed para efficient retrieval, emsertion, updatemg, e deletion de dados.

# ## Dadosbase Gerenciamento Sistemas (DBMS)
Sdetware that emteracts com end users, applications, e o/a dadosbase itself to capture e analyze dados. Exemplos: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization de dadosbase (tables, fields, relationships)
- **Instance**: Actual dados stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizemg dados to reduce redundancy
- **Denormalization**: Addemg redundancy to improve read perparamance

# # Relational Dadosbases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) e columns (fields)
- **Primary Key**: Unique identifier para each row
- **Foreign Key**: Referência to primary key em anoo/ar table
- **Indexes**: Dados structures improvemg query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on dados changes

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

# ## Joems
- **EMNER JOEM**: Returns matchemg rows from both tables
- **LEFT JOEM**: All rows from left table, matches from right
- **RIGHT JOEM**: All rows from right table, matches from left
- **FULL OUTER JOEM**: All rows from both tables
- **CROSS JOEM**: Cartesian product de both tables
- **SELF JOEM**: Table joemed com itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeatemg groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on oo/ar non-key attributes)
- **BCNF**: Stronger 3NF, every determemant is a ceidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No joem dependencies

# ## Popular RDBMS
- **PostgreSQL**: Avançado features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsdet ecosystem, emtegrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL parak, open-source

# # NoSQL Dadosbases

# ## Types de NoSQL Dadosbases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content gerenciamento, catalogs, user prdeiles
- **Exemplos**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Cachemg, sessions, shoppemg cartes
- **Exemplos**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited queryemg

# ### Column-Family Stores
- **Structure**: Columns grouped emto families
- **Use Cases**: Big dados, analytics, time-series
- **Exemplos**: Cassera, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Dadosbases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social redes, fraud detection, recommendations
- **Exemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Query Idioma**: Cypher (Neo4j), Gremlem

# ## When to Use NoSQL
- Flexible/evolvemg schema
- Horizontal scalemg requirements
- High write throughput
- Hierarchical/nested dados
- Distributed sistemas
- Real-time applications

# # Dadosbase Design

# ## Entity-Relationship Modelemg
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties de entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardemality**: Number de emstances em relationship

# ## Schema Design Patterns
- **Semgle Table Inheritance**: All types em one table com type discrimemator
- **Class Table Inheritance**: Separate tables para base e subclasses
- **Concrete Table Inheritance**: Separate table para each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexemg Strategies
- **B-Tree**: Default, range queries, sortemg
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardemality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic dados (GIS)
- **Composite**: Multiple columns combemed
- **Coveremg**: Includes all columns needed para query

# # Query Optimization

# ## Execution Plans
- Understeemg how dadosbase executes queries
- Identifyemg bottlenecks (full table scans, missemg emdexes)
- Tools: EXPLAEM, EXPLAEM ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate emdexes
- **Query Rewritemg**: Simplify complex queries
- **Joem Optimization**: Choose correct joem types e order
- **Partitionemg**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Cachemg**: Store frequent query results

# ## Common Perparamance Issues
- **N+1 Query Problem**: Fetchemg related dados emefficiently
- **Missemg Indexes**: Full table scans on large tables
- **Over-emdexemg**: Slow writes due to too many emdexes
- **Lock Contention**: Transactions waitemg para locks
- **Inefficient Queries**: SELECT *, unnecessary joems

# # Transactions e Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed dados visible (default em most DBs)
- **REPEATABLE READ**: Same query returns same results comem transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Lockemg**: Lock resources beparae access
- **Optimistic Lockemg**: Check version beparae commit
- **MVCC (Multi-Version Concurrency Control)**: Maemtaem multiple versions de rows
- **Row-Level Lockemg**: Lock specific rows
- **Table-Level Lockemg**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait para each oo/ar
- Prevention: Consistent lock orderemg, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication e Scalemg

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chaem Replication**: Sequential replication through nodes

# ## Scalemg Approaches
- **Vertical Scalemg**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scalemg**: Add more servers (shardemg, partitionemg)
- **Read Replicas**: Offload read traffic
- **Shardemg**: Split dados across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same dados at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees o/air own updates immediately

# # Backup e Recovery

# ## Backup Strategies
- **Full Backup**: Complete dadosbase copy
- **Incremental Backup**: Changes semce last backup
- **Differential Backup**: Changes semce last full backup
- **Poemt-em-Time Recovery**: Restore to specific moment
- **Contemuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Poemt Objective)**: Maximum acceptable dados loss
- **Disaster Recovery Plan**: Documented procedures para failures
- **Testemg**: Regular recovery drills

# # Segurança

# ## Access Control
- **Auo/antication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions para easier gerenciamento
- **Premciple de Least Privilege**: Memimum necessary access

# ## Dados Protection
- **Encryption at Rest**: Encrypt stored dados
- **Encryption em Transit**: TLS/SSL para connections
- **Maskemg**: Hide sensitive dados em non-production
- **Tokenization**: Replace sensitive dados com tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL em user emput
- **Privilege Escalation**: Gaememg unauthorized access
- **Audit Loggemg**: Track all dadosbase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Dadosbase Technologies

# ## Cloud Dadosbases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Dadosbase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scalemg, backups emcluded

# ## NewSQL Dadosbases
- Combeme SQL consistency com NoSQL scalability
- **Exemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scalemg

# ## Time-Series Dadosbases
- Optimized para timestamped dados
- **Exemplos**: InfluxDB, TimescaleDB, Promeo/aus
- **Use Cases**: IoT, monitoremg, femancial dados

# ## Vector Dadosbases
- Store e query embeddemg vectors
- **Exemplos**: Pemecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation sistemas, AI applications

# ## Multi-Model Dadosbases
- Support multiple dados models em semgle system
- **Exemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility comout multiple dadosbases

# # ORMs e Dados Access

# ## Object-Relational Mappemg
- **Purpose**: Map dadosbase tables to programmemg objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type seguroty
- Migration gerenciamento
- Query buildemg APIs

# ## Drawbacks
- Perparamance overhead
- Complex queries harder to write
- N+1 query problems
- Learnemg curve

# # Dadosbase Admemistration

# ## DBA Responsibilities
- Installation e configuration
- Perparamance tunemg
- Backup e recovery
- Segurança gerenciamento
- Capacity plannemg
- Monitoremg e alertemg
- Patch gerenciamento

# ## Monitoremg Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maemtenance Tasks
- **Vacuum/Analyze**: Update estatísticas, reclaim space
- **Index Rebuildemg**: Defragment emdexes
- **Estatísticas Updates**: Keep query optimizer emparamed
- **Log Rotation**: Manage log file sizes
- **Capacity Plannemg**: Predict growth, plan upgrades
