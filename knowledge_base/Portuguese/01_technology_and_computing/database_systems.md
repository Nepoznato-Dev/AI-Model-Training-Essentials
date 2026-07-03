<!-- 
This file was automatically translated from English to Portuguese.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Banco de dados Sistemas

## Banco de dados Fundamentos

### What is a Banco de dados?
A Banco de dados is an organized collection de structured information stored electronically, designed para efficient retrieval, insertion, updating, e deletion de Dados.

### Banco de dados Gerenciamento Sistemas (DBMS)
Software that interacts com end users, applications, e o/a Banco de dados itself to capture e analyze Dados. Exemplos: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization de Banco de dados (tables, fields, relationships)
- **Instance**: Actual Dados stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing Dados to reduce redundancy
- **Denormalization**: Adding redundancy to improve read Desempenho

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) e columns (fields)
- **Primary Key**: Unique identifier para each row
- **Foreign Key**: Referência to primary key em another table
- **Indexes**: Dados structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on Dados changes

### SQL Operations (CRUD)
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

### Joins
- **INNER JOIN**: Returns matching rows from both tables
- **LEFT JOIN**: All rows from left table, matches from right
- **RIGHT JOIN**: All rows from right table, matches from left
- **FULL OUTER JOIN**: All rows from both tables
- **CROSS JOIN**: Cartesian product de both tables
- **SELF JOIN**: Table joined com itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: Avançado features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, Web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types de NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content Gerenciamento, catalogs, user profiles
- **Exemplos**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Exemplos**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big Dados, analytics, time-series
- **Exemplos**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Exemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Query Idioma**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested Dados
- Distributed Sistemas
- Real-time applications

## Banco de dados Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties de entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number de instances em relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types em one table com type discriminator
- **Class Table Inheritance**: Separate tables para base e subclasses
- **Concrete Table Inheritance**: Separate table para each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic Dados (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed para query

## Query Optimization

### Execution Plans
- Understanding how Banco de dados executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types e order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common Desempenho Issues
- **N+1 Query Problem**: Fetching related Dados inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting para locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions e Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed Dados visible (default em most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions de rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait para each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication e Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split Dados across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same Dados at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup e Recovery

### Backup Strategies
- **Full Backup**: Completo Banco de dados copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-em-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable Dados loss
- **Disaster Recovery Plan**: Documented procedures para failures
- **Teste**: Regular recovery drills

## Segurança

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions para easier Gerenciamento
- **Principle de Least Privilege**: Minimum necessary access

### Dados Protection
- **Encryption at Rest**: Encrypt stored Dados
- **Encryption em Transit**: TLS/SSL para connections
- **Masking**: Hide sensitive Dados em non-production
- **Tokenization**: Replace sensitive Dados com tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL em user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all Banco de dados activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern Banco de dados Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Banco de dados, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency com NoSQL scalability
- **Exemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized para timestamped Dados
- **Exemplos**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial Dados

### Vector Databases
- Store e query embedding vectors
- **Exemplos**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation Sistemas, AI applications

### Multi-Model Databases
- Suporte multiple Dados models em single system
- **Exemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs e Dados Access

### Object-Relational Mapping
- **Purpose**: Map Banco de dados tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration Gerenciamento
- Query building APIs

### Drawbacks
- Desempenho overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## Banco de dados Administration

### DBA Responsibilities
- Installation e configuration
- Desempenho tuning
- Backup e recovery
- Segurança Gerenciamento
- Capacity planning
- Monitoring e alerting
- Patch Gerenciamento

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update Estatísticas, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Estatísticas Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
