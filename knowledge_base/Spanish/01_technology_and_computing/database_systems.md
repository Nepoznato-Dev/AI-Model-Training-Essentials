<!-- 
This file was automatically translated from English to Spanish.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Base de datos Sistemas

# # Base de datos Fundamentos

# ## What is a Base de datos?
A Base de datos is an organized collection de structured information stored electronically, designed para efficient retrieval, insertion, updating, y deletion de Datos.

# ## Base de datos Gestión Sistemas (DBMS)
Software that interacts con end users, applications, y el/la Base de datos itself to capture y analyze Datos. Ejemplos: MySQL, PostgreSQL, Oracle, MongoDB.

# ## Key Concepts
- **Schema**: Structure/organization de Base de datos (tables, fields, relationships)
- **Instance**: Actual Datos stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing Datos to reduce redundancy
- **Denormalization**: Adding redundancy to improve read Rendimiento

# # Relational Databases (SQL)

# ## Core Concepts
- **Tables**: Rows (records) y columns (fields)
- **Primary Key**: Unique identifier para each row
- **Foreign Key**: Referencia to primary key en another table
- **Indexes**: Datos structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on Datos changes

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
- **CROSS JOIN**: Cartesian product de both tables
- **SELF JOIN**: Table joined con itself

# ## Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

# ## Popular RDBMS
- **PostgreSQL**: Avanzado features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, Web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

# # NoSQL Databases

# ## Types de NoSQL Databases

# ### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content Gestión, catalogs, user profiles
- **Ejemplos**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

# ### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Ejemplos**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

# ### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big Datos, analytics, time-series
- **Ejemplos**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

# ### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Ejemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Query Idioma**: Cypher (Neo4j), Gremlin

# ## When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested Datos
- Distributed Sistemas
- Real-time applications

# # Base de datos Design

# ## Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties de entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number de instances en relationship

# ## Schema Design Patterns
- **Single Table Inheritance**: All types en one table con type discriminator
- **Class Table Inheritance**: Separate tables para base y subclasses
- **Concrete Table Inheritance**: Separate table para each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

# ## Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic Datos (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed para query

# # Query Optimization

# ## Execution Plans
- Understanding how Base de datos executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

# ## Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types y order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

# ## Common Rendimiento Issues
- **N+1 Query Problem**: Fetching related Datos inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting para locks
- **Inefficient Queries**: SELECT *, unnecessary joins

# # Transactions y Concurrency

# ## Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed Datos visible (default en most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

# ## Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions de rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

# ## Deadlocks
- Circular dependency where transactions wait para each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

# # Replication y Scaling

# ## Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

# ## Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split Datos across servers by key/range/hash
- **Federation**: Split by function/service

# ## Consistency Models
- **Strong Consistency**: All nodes see same Datos at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

# # Backup y Recovery

# ## Backup Strategies
- **Full Backup**: Complete Base de datos copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-en-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

# ## Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable Datos loss
- **Disaster Recovery Plan**: Documented procedures para failures
- **Pruebas**: Regular recovery drills

# # Seguridad

# ## Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions para easier Gestión
- **Principle de Least Privilege**: Minimum necessary access

# ## Datos Protection
- **Encryption at Rest**: Encrypt stored Datos
- **Encryption en Transit**: TLS/SSL para connections
- **Masking**: Hide sensitive Datos en non-production
- **Tokenization**: Replace sensitive Datos con tokens

# ## Common Vulnerabilities
- **SQL Injection**: Malicious SQL en user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all Base de datos activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

# # Modern Base de datos Technologies

# ## Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Base de datos, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

# ## NewSQL Databases
- Combine SQL consistency con NoSQL scalability
- **Ejemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

# ## Time-Series Databases
- Optimized para timestamped Datos
- **Ejemplos**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial Datos

# ## Vector Databases
- Store y query embedding vectors
- **Ejemplos**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation Sistemas, AI applications

# ## Multi-Model Databases
- Support multiple Datos models en single system
- **Ejemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

# # ORMs y Datos Access

# ## Object-Relational Mapping
- **Purpose**: Map Base de datos tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

# ## Benefits
- Abstraction from SQL
- Type safety
- Migration Gestión
- Query building APIs

# ## Drawbacks
- Rendimiento overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

# # Base de datos Administration

# ## DBA Responsibilities
- Installation y configuration
- Rendimiento tuning
- Backup y recovery
- Seguridad Gestión
- Capacity planning
- Monitoring y alerting
- Patch Gestión

# ## Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

# ## Maintenance Tasks
- **Vacuum/Analyze**: Update Estadísticas, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Estadísticas Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
