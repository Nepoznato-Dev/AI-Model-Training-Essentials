<!-- 
This file was automatically translated from English to German.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Datenbank Systeme

# # Datenbank Grundlagen

# ## What is a Datenbank?
A Datenbank is an organized collection von structured information stored electronically, designed für efficient retrieval, insertion, updating, und deletion von Daten.

# ## Datenbank Verwaltung Systeme (DBMS)
Software that interacts mit end users, applications, und der/die/das Datenbank itself to capture und analyze Daten. Beispiele: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization von Datenbank (tables, fields, relationships)
- **Instance**: Actual Daten stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing Daten to reduce redundancy
- **Denormalization**: Adding redundancy to improve read Leistung

# # Relational Databases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) und columns (fields)
- **Primary Key**: Unique identifier für each row
- **Foreign Key**: Referenz to primary key in another table
- **Indexes**: Daten structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on Daten changes

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
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

# ## Popular RDBMS
- **PostgreSQL**: Fortgeschritten features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, Web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

# # NoSQL Databases

# ## Types von NoSQL Databases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content Verwaltung, catalogs, user profiles
- **Beispiele**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Beispiele**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

# ### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big Daten, analytics, time-series
- **Beispiele**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Beispiele**: Neo4j, Amazon Neptune, ArangoDB
- **Query Sprache**: Cypher (Neo4j), Gremlin

# ## When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested Daten
- Distributed Systeme
- Real-time applications

# # Datenbank Design

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
- **Spatial**: Geographic Daten (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed für query

# # Query Optimization

# ## Execution Plans
- Understanding how Datenbank executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types und order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

# ## Common Leistung Issues
- **N+1 Query Problem**: Fetching related Daten inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting für locks
- **Inefficient Queries**: SELECT *, unnecessary joins

# # Transactions und Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed Daten visible (default in most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions von rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait für each other
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
- **Sharding**: Split Daten across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same Daten at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

# # Backup und Recovery

# ## Backup Strategies
- **Full Backup**: Complete Datenbank copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-in-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable Daten loss
- **Disaster Recovery Plan**: Documented procedures für failures
- **Testen**: Regular recovery drills

# # Sicherheit

# ## Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions für easier Verwaltung
- **Principle von Least Privilege**: Minimum necessary access

# ## Daten Protection
- **Encryption at Rest**: Encrypt stored Daten
- **Encryption in Transit**: TLS/SSL für connections
- **Masking**: Hide sensitive Daten in non-production
- **Tokenization**: Replace sensitive Daten mit tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL in user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all Datenbank activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Datenbank Technologies

# ## Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Datenbank, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

# ## NewSQL Databases
- Combine SQL consistency mit NoSQL scalability
- **Beispiele**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

# ## Time-Series Databases
- Optimized für timestamped Daten
- **Beispiele**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial Daten

# ## Vector Databases
- Store und query embedding vectors
- **Beispiele**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation Systeme, AI applications

# ## Multi-Model Databases
- Support multiple Daten models in single system
- **Beispiele**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

# # ORMs und Daten Access

# ## Object-Relational Mapping
- **Purpose**: Map Datenbank tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type safety
- Migration Verwaltung
- Query building APIs

# ## Drawbacks
- Leistung overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

# # Datenbank Administration

# ## DBA Responsibilities
- Installation und configuration
- Leistung tuning
- Backup und recovery
- Sicherheit Verwaltung
- Capacity planning
- Monitoring und alerting
- Patch Verwaltung

# ## Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maintenance Tasks
- **Vacuum/Analyze**: Update Statistiken, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Statistiken Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
