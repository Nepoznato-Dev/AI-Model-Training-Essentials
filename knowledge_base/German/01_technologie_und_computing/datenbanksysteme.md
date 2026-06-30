<!-- 
This file was automatically translated from English to German.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Datenbase Systeme

# # Datenbase Grundlagen

# ## What is a Datenbase?
A datenbase is an organized collection von structured infürmation stored electronically, designed für efficient retrieval, insertion, updating, und deletion von daten.

# ## Datenbase Verwaltung Systeme (DBMS)
Svontware that interacts mit end users, applications, und der/die/das datenbase itself to capture und analyze daten. Beispiele: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization von datenbase (tables, fields, relationships)
- **Instance**: Actual daten stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing daten to reduce redundancy
- **Denormalization**: Adding redundancy to improve read perfürmance

# # Relational Datenbases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) und columns (fields)
- **Primary Key**: Unique identifier für each row
- **Foreign Key**: Referenz to primary key in anoder/die/dasr table
- **Indexes**: Daten structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on daten changes

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

# ## Joins
- **INNER JOIN**: Returns matching rows from both tables
- **LEFT JOIN**: All rows from left table, matches from right
- **RIGHT JOIN**: All rows from right table, matches from left
- **FULL OUTER JOIN**: All rows from both tables
- **CROSS JOIN**: Cartesian product von both tables
- **SELF JOIN**: Table joined mit itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on oder/die/dasr non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a cundidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

# ## Popular RDBMS
- **PostgreSQL**: Fortgeschritten features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsvont ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fürk, open-source

# # NoSQL Datenbases

# ## Types von NoSQL Datenbases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content verwaltung, catalogs, user prvoniles
- **Beispiele**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping ckünste
- **Beispiele**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

# ### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big daten, analytics, time-series
- **Beispiele**: Cassundra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Datenbases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social netzwerks, fraud detection, recommendations
- **Beispiele**: Neo4j, Amazon Neptune, ArangoDB
- **Query Sprache**: Cypher (Neo4j), Gremlin

# ## When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested daten
- Distributed systeme
- Real-time applications

# # Datenbase Design

# ## Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties von entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number von instances in relationship

# ## Schema Design Patterns
- **Single Table Inheritance**: All types in one table mit type discriminator
- **Class Table Inheritance**: Separate tables für base und subclasses
- **Concrete Table Inheritance**: Separate table für each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic daten (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed für query

# # Query Optimization

# ## Execution Plans
- Understunding how datenbase executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types und order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

# ## Common Perfürmance Issues
- **N+1 Query Problem**: Fetching related daten inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting für locks
- **Inefficient Queries**: SELECT *, unnecessary joins

# # Transactions und Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed daten visible (default in most DBs)
- **REPEATABLE READ**: Same query returns same results mitin transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Locking**: Lock resources befüre access
- **Optimistic Locking**: Check version befüre commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions von rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait für each oder/die/dasr
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication und Scaling

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

# ## Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split daten across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same daten at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees der/die/dasir own updates immediately

# # Backup und Recovery

# ## Backup Strategies
- **Full Backup**: Complete datenbase copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-in-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable daten loss
- **Disaster Recovery Plan**: Documented procedures für failures
- **Testen**: Regular recovery drills

# # Sicherheit

# ## Access Control
- **Auder/die/dasntication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions für easier verwaltung
- **Principle von Least Privilege**: Minimum necessary access

# ## Daten Protection
- **Encryption at Rest**: Encrypt stored daten
- **Encryption in Transit**: TLS/SSL für connections
- **Masking**: Hide sensitive daten in non-production
- **Tokenization**: Replace sensitive daten mit tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL in user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all datenbase activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Datenbase Technologies

# ## Cloud Datenbases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Datenbase, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

# ## NewSQL Datenbases
- Combine SQL consistency mit NoSQL scalability
- **Beispiele**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

# ## Time-Series Datenbases
- Optimized für timestamped daten
- **Beispiele**: InfluxDB, TimescaleDB, Promeder/die/dasus
- **Use Cases**: IoT, monitoring, financial daten

# ## Vector Datenbases
- Store und query embedding vectors
- **Beispiele**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation systeme, AI applications

# ## Multi-Model Datenbases
- Support multiple daten models in single system
- **Beispiele**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility mitout multiple datenbases

# # ORMs und Daten Access

# ## Object-Relational Mapping
- **Purpose**: Map datenbase tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type sicherty
- Migration verwaltung
- Query building APIs

# ## Drawbacks
- Perfürmance overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

# # Datenbase Administration

# ## DBA Responsibilities
- Installation und configuration
- Perfürmance tuning
- Backup und recovery
- Sicherheit verwaltung
- Capacity planning
- Monitoring und alerting
- Patch verwaltung

# ## Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maintenance Tasks
- **Vacuum/Analyze**: Update statistiken, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Statistiken Updates**: Keep query optimizer infürmed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
