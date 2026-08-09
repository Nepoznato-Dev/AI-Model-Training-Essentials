---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Database Systems

## Database Fundamentals

### What is a Database?
A database is an organized collection of structured information stored electronically, designed for efficient retrieval, insertion, updating, and deletion of data.

### Database Management Systems (DBMS)
Software that interacts with end users, applications, and the database itself to capture and analyze data. Examples: MySQL, PostgreSQL, Oracle, MongoDB.

### Key Concepts
- **Schema**: Structure/organization of database (tables, fields, relationships)
- **Instance**: Actual data stored at a particular moment
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (choose 2)
- **Normalization**: Organizing data to reduce redundancy
- **Denormalization**: Adding redundancy to improve read performance

## Relational Databases (SQL)

### Core Concepts
- **Tables**: Rows (records) and columns (fields)
- **Primary Key**: Unique identifier for each row
- **Foreign Key**: Reference to primary key in another table
- **Indexes**: Data structures improving query speed
- **Views**: Virtual tables based on query results
- **Stored Procedures**: Precompiled SQL code blocks
- **Triggers**: Automatic actions on data changes

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
- **CROSS JOIN**: Cartesian product of both tables
- **SELF JOIN**: Table joined with itself

### Normalization Forms
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies (all non-key attributes depend on whole primary key)
- **3NF**: 2NF + no transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Stronger 3NF, every determinant is a candidate key
- **4NF**: No multi-valued dependencies
- **5NF**: No join dependencies

### Popular RDBMS
- **PostgreSQL**: Advanced features, extensible, ACID-compliant
- **MySQL**: Widely used, fast reads, web applications
- **Oracle**: Enterprise features, scalability, expensive
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: Embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### Types of NoSQL Databases

#### Document Stores
- **Structure**: JSON-like documents (BSON)
- **Use Cases**: Content management, catalogs, user profiles
- **Examples**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Simple key-value pairs
- **Use Cases**: Caching, sessions, shopping carts
- **Examples**: Redis, DynamoDB, Riak
- **Characteristics**: Fast, simple, limited querying

#### Column-Family Stores
- **Structure**: Columns grouped into families
- **Use Cases**: Big data, analytics, time-series
- **Examples**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Write-optimized, distributed, scalable

#### Graph Databases
- **Structure**: Nodes, edges, properties
- **Use Cases**: Social networks, fraud detection, recommendations
- **Examples**: Neo4j, Amazon Neptune, ArangoDB
- **Query Language**: Cypher (Neo4j), Gremlin

### When to Use NoSQL
- Flexible/evolving schema
- Horizontal scaling requirements
- High write throughput
- Hierarchical/nested data
- Distributed systems
- Real-time applications

## Database Design

### Entity-Relationship Modeling
- **Entities**: Objects/concepts (Customer, Product, Order)
- **Attributes**: Properties of entities (name, price, date)
- **Relationships**: Connections between entities (one-to-one, one-to-many, many-to-many)
- **Cardinality**: Number of instances in relationship

### Schema Design Patterns
- **Single Table Inheritance**: All types in one table with type discriminator
- **Class Table Inheritance**: Separate tables for base and subclasses
- **Concrete Table Inheritance**: Separate table for each concrete class
- **Junction Tables**: Resolve many-to-many relationships
- **Audit Tables**: Track changes (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Default, range queries, sorting
- **Hash**: Exact match lookups
- **Bitmap**: Low-cardinality columns (gender, status)
- **Full-Text**: Text search capabilities
- **Spatial**: Geographic data (GIS)
- **Composite**: Multiple columns combined
- **Covering**: Includes all columns needed for query

## Query Optimization

### Execution Plans
- Understanding how database executes queries
- Identifying bottlenecks (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Ensure queries use appropriate indexes
- **Query Rewriting**: Simplify complex queries
- **Join Optimization**: Choose correct join types and order
- **Partitioning**: Split large tables (range, hash, list)
- **Materialized Views**: Pre-computed query results
- **Query Caching**: Store frequent query results

### Common Performance Issues
- **N+1 Query Problem**: Fetching related data inefficiently
- **Missing Indexes**: Full table scans on large tables
- **Over-indexing**: Slow writes due to too many indexes
- **Lock Contention**: Transactions waiting for locks
- **Inefficient Queries**: SELECT *, unnecessary joins

## Transactions and Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: Lowest isolation, dirty reads possible
- **READ COMMITTED**: Only committed data visible (default in most DBs)
- **REPEATABLE READ**: Same query returns same results within transaction
- **SERIALIZABLE**: Highest isolation, transactions execute sequentially

### Concurrency Control
- **Pessimistic Locking**: Lock resources before access
- **Optimistic Locking**: Check version before commit
- **MVCC (Multi-Version Concurrency Control)**: Maintain multiple versions of rows
- **Row-Level Locking**: Lock specific rows
- **Table-Level Locking**: Lock entire table

### Deadlocks
- Circular dependency where transactions wait for each other
- Prevention: Consistent lock ordering, timeouts, deadlock detection
- Resolution: Abort one transaction

## Replication and Scaling

### Replication Types
- **Master-Slave**: One primary, multiple read replicas
- **Master-Master**: Multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution needed
- **Chain Replication**: Sequential replication through nodes

### Scaling Approaches
- **Vertical Scaling**: Increase server resources (CPU, RAM, storage)
- **Horizontal Scaling**: Add more servers (sharding, partitioning)
- **Read Replicas**: Offload read traffic
- **Sharding**: Split data across servers by key/range/hash
- **Federation**: Split by function/service

### Consistency Models
- **Strong Consistency**: All nodes see same data at same time
- **Eventual Consistency**: Nodes converge over time
- **Causal Consistency**: Cause-effect relationships preserved
- **Read-Your-Writes**: User sees their own updates immediately

## Backup and Recovery

### Backup Strategies
- **Full Backup**: Complete database copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup
- **Point-in-Time Recovery**: Restore to specific moment
- **Continuous Backup**: Real-time replication to backup

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable data loss
- **Disaster Recovery Plan**: Documented procedures for failures
- **Testing**: Regular recovery drills

## Security

### Access Control
- **Authentication**: Verify user identity
- **Authorization**: Grant permissions (GRANT, REVOKE)
- **Roles**: Group permissions for easier management
- **Principle of Least Privilege**: Minimum necessary access

### Data Protection
- **Encryption at Rest**: Encrypt stored data
- **Encryption in Transit**: TLS/SSL for connections
- **Masking**: Hide sensitive data in non-production
- **Tokenization**: Replace sensitive data with tokens

### Common Vulnerabilities
- **SQL Injection**: Malicious SQL in user input
- **Privilege Escalation**: Gaining unauthorized access
- **Audit Logging**: Track all database activities
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## Modern Database Technologies

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, backups included

### NewSQL Databases
- Combine SQL consistency with NoSQL scalability
- **Examples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distributed, ACID transactions, horizontal scaling

### Time-Series Databases
- Optimized for timestamped data
- **Examples**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial data

### Vector Databases
- Store and query embedding vectors
- **Examples**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, recommendation systems, AI applications

### Multi-Model Databases
- Support multiple data models in single system
- **Examples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility without multiple databases

## ORMs and Data Access

### Object-Relational Mapping
- **Purpose**: Map database tables to programming objects
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- Abstraction from SQL
- Type safety
- Migration management
- Query building APIs

### Drawbacks
- Performance overhead
- Complex queries harder to write
- N+1 query problems
- Learning curve

## Database Administration

### DBA Responsibilities
- Installation and configuration
- Performance tuning
- Backup and recovery
- Security management
- Capacity planning
- Monitoring and alerting
- Patch management

### Monitoring Metrics
- Query response time
- Throughput (transactions per second)
- Connection count
- Cache hit ratio
- Disk I/O
- Lock wait time
- Replication lag

### Maintenance Tasks
- **Vacuum/Analyze**: Update statistics, reclaim space
- **Index Rebuilding**: Defragment indexes
- **Statistics Updates**: Keep query optimizer informed
- **Log Rotation**: Manage log file sizes
- **Capacity Planning**: Predict growth, plan upgrades
