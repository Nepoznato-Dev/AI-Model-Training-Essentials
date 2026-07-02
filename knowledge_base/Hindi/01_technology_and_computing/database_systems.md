# डेटाबेस सिस्टम्स

## डेटाबेस की बुनियाद

### डेटाबेस क्या है?
डेटाबेस संरचित जानकारी का एक सुव्यवस्थित संग्रह है, जिसे इलेक्ट्रॉनिक रूप से संग्रहीत किया जाता है और जिसे data की कुशल retrieval, insertion, updating, और deletion के लिए डिज़ाइन किया गया है।

### Database Management Systems (DBMS)
ऐसा software जो end users, applications, और स्वयं database के साथ इंटरैक्ट करके data को capture और analyze करता है। उदाहरण: MySQL, PostgreSQL, Oracle, MongoDB.

### मुख्य अवधारणाएँ
- **Schema**: डेटाबेस की संरचना/व्यवस्था (tables, fields, relationships)
- **Instance**: किसी विशेष समय पर संग्रहीत वास्तविक data
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (3 में से 2 चुनें)
- **Normalization**: redundancy कम करने के लिए data को व्यवस्थित करना
- **Denormalization**: read performance बेहतर करने के लिए redundancy जोड़ना

## Relational Databases (SQL)

### मुख्य अवधारणाएँ
- **Tables**: rows (records) और columns (fields)
- **Primary Key**: प्रत्येक row के लिए unique identifier
- **Foreign Key**: दूसरी table की primary key का reference
- **Indexes**: query speed बेहतर करने वाली data structures
- **Views**: query results पर आधारित virtual tables
- **Stored Procedures**: पूर्व-संकलित SQL कोड ब्लॉक
- **Triggers**: data changes पर होने वाली automatic actions

### SQL संचालन (CRUD)
```sql
-- बनाएँ
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- पढ़ें
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- अपडेट करें
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- हटाएँ
DELETE FROM users WHERE id = 1;
```

### Joins
- **INNER JOIN**: दोनों tables से matching rows लौटाता है
- **LEFT JOIN**: बाईं table की सभी rows, दाईं से matches
- **RIGHT JOIN**: दाईं table की सभी rows, बाईं से matches
- **FULL OUTER JOIN**: दोनों tables की सभी rows
- **CROSS JOIN**: दोनों tables का Cartesian product
- **SELF JOIN**: table को स्वयं के साथ join करना

### Normalization forms
- **1NF**: atomic values, कोई repeating groups नहीं
- **2NF**: 1NF + कोई partial dependencies नहीं (सभी non-key attributes पूरी primary key पर निर्भर हों)
- **3NF**: 2NF + कोई transitive dependencies नहीं (non-key attributes अन्य non-key attributes पर निर्भर न हों)
- **BCNF**: 3NF का अधिक मजबूत रूप, हर determinant एक candidate key होता है
- **4NF**: कोई multi-valued dependencies नहीं
- **5NF**: कोई join dependencies नहीं

### लोकप्रिय RDBMS
- **PostgreSQL**: उन्नत सुविधाएँ, extensible, ACID-compliant
- **MySQL**: व्यापक रूप से उपयोग किया जाता है, तेज़ reads, web applications
- **Oracle**: enterprise features, scalability, महँगा
- **SQL Server**: Microsoft ecosystem, integrated tools
- **SQLite**: embedded, serverless, lightweight
- **MariaDB**: MySQL fork, open-source

## NoSQL Databases

### NoSQL Databases के प्रकार

#### Document stores
- **Structure**: JSON-जैसे documents (BSON)
- **Use Cases**: content management, catalogs, user profiles
- **Examples**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-value stores
- **Structure**: simple key-value pairs
- **Use Cases**: caching, sessions, shopping carts
- **Examples**: Redis, DynamoDB, Riak
- **Characteristics**: fast, simple, limited querying

#### Column-family stores
- **Structure**: columns को families में समूहित किया जाता है
- **Use Cases**: big data, analytics, time-series
- **Examples**: Cassandra, HBase, ScyllaDB
- **Characteristics**: write-optimized, distributed, scalable

#### Graph databases
- **Structure**: nodes, edges, properties
- **Use Cases**: social networks, fraud detection, recommendations
- **Examples**: Neo4j, Amazon Neptune, ArangoDB
- **Query Language**: Cypher (Neo4j), Gremlin

### NoSQL कब उपयोग करें
- flexible/evolving schema
- horizontal scaling requirements
- high write throughput
- hierarchical/nested data
- distributed systems
- real-time applications

## Database design

### Entity-Relationship modeling
- **Entities**: objects/concepts (Customer, Product, Order)
- **Attributes**: entities की properties (name, price, date)
- **Relationships**: entities के बीच connections (one-to-one, one-to-many, many-to-many)
- **Cardinality**: relationship में instances की संख्या

### Schema design patterns
- **Single Table Inheritance**: type discriminator के साथ सभी types एक table में
- **Class Table Inheritance**: base और subclasses के लिए अलग tables
- **Concrete Table Inheritance**: प्रत्येक concrete class के लिए अलग table
- **Junction Tables**: many-to-many relationships को resolve करना
- **Audit Tables**: changes को track करना (`created_at`, `updated_at`, `deleted_at`)

### Indexing strategies
- **B-Tree**: default, range queries, sorting
- **Hash**: exact match lookups
- **Bitmap**: low-cardinality columns (gender, status)
- **Full-Text**: text search capabilities
- **Spatial**: geographic data (GIS)
- **Composite**: multiple columns combined
- **Covering**: query के लिए आवश्यक सभी columns शामिल

## Query optimization

### Execution plans
- यह समझना कि database queries को कैसे execute करता है
- bottlenecks की पहचान करना (full table scans, missing indexes)
- Tools: EXPLAIN, EXPLAIN ANALYZE

### Optimization techniques
- **Index Usage**: सुनिश्चित करें कि queries उचित indexes का उपयोग करें
- **Query Rewriting**: complex queries को सरल बनाना
- **Join Optimization**: सही join types और order चुनना
- **Partitioning**: बड़ी tables को विभाजित करना (range, hash, list)
- **Materialized Views**: पहले से computed query results
- **Query Caching**: बार-बार आने वाले query results को store करना

### सामान्य performance समस्याएँ
- **N+1 Query Problem**: related data को अक्षम तरीके से fetch करना
- **Missing Indexes**: बड़ी tables पर full table scans
- **Over-indexing**: बहुत अधिक indexes के कारण writes धीमी होना
- **Lock Contention**: locks के लिए प्रतीक्षा करती transactions
- **Inefficient Queries**: `SELECT *`, अनावश्यक joins

## Transactions और Concurrency

### Transaction isolation levels
- **READ UNCOMMITTED**: सबसे कम isolation, dirty reads संभव
- **READ COMMITTED**: केवल committed data दिखता है (अधिकांश DBs में default)
- **REPEATABLE READ**: transaction के भीतर वही query समान results लौटाती है
- **SERIALIZABLE**: सबसे उच्च isolation, transactions क्रमिक रूप से execute होती हैं

### Concurrency control
- **Pessimistic Locking**: access से पहले resources को lock करना
- **Optimistic Locking**: commit से पहले version की जाँच करना
- **MVCC (Multi-Version Concurrency Control)**: rows के कई versions बनाए रखना
- **Row-Level Locking**: specific rows को lock करना
- **Table-Level Locking**: पूरी table को lock करना

### Deadlocks
- ऐसी circular dependency जहाँ transactions एक-दूसरे की प्रतीक्षा करती हैं
- Prevention: consistent lock ordering, timeouts, deadlock detection
- Resolution: एक transaction को abort करना

## Replication और scaling

### Replication types
- **Master-Slave**: एक primary, multiple read replicas
- **Master-Master**: multiple primaries, bidirectional replication
- **Multi-Master**: N primaries, conflict resolution आवश्यक
- **Chain Replication**: nodes के माध्यम से क्रमिक replication

### Scaling approaches
- **Vertical Scaling**: server resources बढ़ाना (CPU, RAM, storage)
- **Horizontal Scaling**: अधिक servers जोड़ना (sharding, partitioning)
- **Read Replicas**: read traffic को offload करना
- **Sharding**: key/range/hash के आधार पर data को servers में बाँटना
- **Federation**: function/service के आधार पर विभाजन

### Consistency models
- **Strong Consistency**: सभी nodes एक ही समय पर समान data देखते हैं
- **Eventual Consistency**: समय के साथ nodes एक जैसी स्थिति में पहुँचते हैं
- **Causal Consistency**: cause-effect relationships सुरक्षित रहती हैं
- **Read-Your-Writes**: user अपने updates तुरंत देखता है

## Backup और recovery

### Backup strategies
- **Full Backup**: database की पूर्ण copy
- **Incremental Backup**: पिछली backup के बाद हुए changes
- **Differential Backup**: पिछली full backup के बाद हुए changes
- **Point-in-Time Recovery**: किसी विशेष समय बिंदु तक restore करना
- **Continuous Backup**: backup के लिए real-time प्रतिकृति

### Recovery procedures
- **RTO (Recovery Time Objective)**: अधिकतम स्वीकार्य सेवा-विराम समय
- **RPO (Recovery Point Objective)**: अधिकतम स्वीकार्य डेटा हानि
- **Disaster Recovery Plan**: failures के लिए प्रलेखित प्रक्रियाएँ
- **Testing**: नियमित recovery drills

## सुरक्षा

### Access control
- **Authentication**: user identity की पुष्टि करना
- **Authorization**: permissions देना (`GRANT`, `REVOKE`)
- **Roles**: आसान management के लिए permissions का समूह
- **Principle of Least Privilege**: न्यूनतम आवश्यक access

### Data protection
- **Encryption at Rest**: संग्रहीत data को encrypt करना
- **Encryption in Transit**: connections के लिए TLS/SSL
- **Masking**: non-production में sensitive data छिपाना
- **Tokenization**: sensitive data को tokens से बदलना

### सामान्य vulnerabilities
- **SQL Injection**: user input में malicious SQL
- **Privilege Escalation**: अनधिकृत access प्राप्त करना
- **Audit Logging**: सभी database activities को track करना
- **Compliance**: GDPR, HIPAA, PCI-DSS requirements

## आधुनिक डेटाबेस तकनीकें

### Cloud databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Benefits**: managed service, auto-scaling, backups included

### NewSQL databases
- SQL consistency को NoSQL scalability के साथ संयोजित करते हैं
- **Examples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: distributed, ACID transactions, horizontal scaling

### Time-series databases
- timestamped data के लिए optimized
- **Examples**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoring, financial data

### Vector databases
- embedding vectors को store और query करना
- **Examples**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: semantic search, recommendation systems, AI applications

### Multi-model databases
- एक ही system में multiple data models का समर्थन
- **Examples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: multiple databases के बिना flexibility

## ORMs और data access

### Object-Relational Mapping
- **Purpose**: database tables को programming objects से map करना
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefits
- SQL से abstraction
- type safety
- migration management
- query building APIs

### Drawbacks
- performance overhead
- complex queries लिखना कठिन
- N+1 query problems
- learning curve

## Database administration

### DBA responsibilities
- installation और configuration
- performance tuning
- backup और recovery
- security management
- capacity planning
- monitoring और alerting
- patch management

### Monitoring metrics
- query response time
- throughput (transactions per second)
- connection count
- cache hit ratio
- disk I/O
- lock wait time
- replication lag

### Maintenance tasks
- **Vacuum/Analyze**: statistics update करना, space reclaim करना
- **Index Rebuilding**: indexes को defragment करना
- **Statistics Updates**: query optimizer को सूचित रखना
- **Log Rotation**: log file sizes को manage करना
- **Capacity Planning**: growth का अनुमान लगाना, upgrades की योजना बनाना
