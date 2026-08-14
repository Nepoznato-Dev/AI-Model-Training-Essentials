<!--
---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# Sistema ng Database
## Mga Pangunahing Kaalaman sa Database
### Ano ang isang Database?
Ang database ay isang organisadong koleksyon ng nakabalangkas na impormasyon na nakaimbak sa elektronikong paraan, na idinisenyo para sa mahusay na pagkuha, pagpasok, pag-update, at pagtanggal ng data.
### Database Management System (DBMS)
Software na nakikipag-ugnayan sa mga end user, application, at ang database mismo upang makuha at suriin ang data. Mga halimbawa: MySQL, PostgreSQL, Oracle, MongoDB.
### Mga Pangunahing Konsepto
- **Schema**: Istraktura/organisasyon ng database (mga talahanayan, field, relasyon)
- **Instance**: Aktwal na data na nakaimbak sa isang partikular na sandali
- **Mga Katangian ng ACID**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (piliin ang 2)
- **Normalization**: Pag-aayos ng data para mabawasan ang redundancy
- **Denormalization**: Pagdaragdag ng redundancy para mapahusay ang performance ng pagbabasa
## Mga Relational Database (SQL)
### Mga Pangunahing Konsepto
- **Tables**: Mga row (record) at column (fields)
- **Pangunahing Key**: Natatanging identifier para sa bawat row
- **Foreign Key**: Reference sa primary key sa ibang table
- **Mga Index**: Ang mga istruktura ng data ay nagpapahusay sa bilis ng query
- **Mga Pagtingin**: Mga virtual na talahanayan batay sa mga resulta ng query
- **Mga Naka-imbak na Pamamaraan**: Naka-precompiled na mga bloke ng SQL code
- **Mga Pag-trigger**: Mga awtomatikong pagkilos sa mga pagbabago sa data
### SQL Operations (CRUD)```sql
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

### Sumasali
- **INNER JOIN**: Ibinabalik ang magkatugmang mga row mula sa parehong talahanayan
- **LEFT JOIN**: Lahat ng row mula sa kaliwang table, mga tugma mula sa kanan
- **RIGHT JOIN**: Lahat ng row mula sa kanang table, mga tugma mula sa kaliwa
- **FULL OUTER JOIN**: Lahat ng row mula sa parehong table
- **CROSS JOIN**: Cartesian na produkto ng parehong talahanayan
- **SELF JOIN**: Ang talahanayan ay pinagsama sa sarili nito
### Mga Form ng Normalization
- **1NF**: Mga halaga ng atom, walang paulit-ulit na pangkat
- **2NF**: 1NF + walang partial dependencies (lahat ng hindi key na attribute ay nakadepende sa buong primary key)
- **3NF**: 2NF + walang transitive dependencies (hindi nakadepende ang mga hindi pangunahing katangian sa iba pang hindi pangunahing katangian)
- **BCNF**: Mas malakas na 3NF, ang bawat determinant ay isang candidate key
- **4NF**: Walang multi-valued dependencies
- **5NF**: Walang sumali sa mga dependency
### Sikat na RDBMS
- **PostgreSQL**: Mga advanced na feature, extensible, ACID-compliant
- **MySQL**: Malawakang ginagamit, mabilis na pagbabasa, mga web application
- **Oracle**: Mga feature ng enterprise, scalability, mahal
- **SQL Server**: Microsoft ecosystem, pinagsamang mga tool
- **SQLite**: Naka-embed, walang server, magaan
- **MariaDB**: MySQL fork, open-source
## Mga Database ng NoSQL
### Mga Uri ng NoSQL Database
#### Mga Tindahan ng Dokumento
- **Istruktura**: Mga dokumentong tulad ng JSON (BSON)
- **Mga Kaso ng Paggamit**: Pamamahala ng nilalaman, mga katalogo, mga profile ng user
- **Mga Halimbawa**: MongoDB, CouchDB, DocumentDB
- **Halimbawa ng Query** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Mga Tindahan ng Key-Value
- **Istruktura**: Simpleng key-value pairs
- **Mga Kaso ng Paggamit**: Pag-cache, mga session, mga shopping cart
- **Mga Halimbawa**: Redis, DynamoDB, Riak
- **Mga Katangian**: Mabilis, simple, limitadong pagtatanong
#### Mga Tindahan ng Column-Family
- **Istruktura**: Ang mga column na nakapangkat sa mga pamilya
- **Mga Kaso ng Paggamit**: Big data, analytics, time-series
- **Mga Halimbawa**: Cassandra, HBase, ScyllaDB
- **Katangian**: Write-optimized, distributed, scalable
#### Mga Database ng Graph
- **Istruktura**: Mga node, gilid, katangian
- **Mga Kaso ng Paggamit**: Mga social network, pagtuklas ng panloloko, mga rekomendasyon
- **Mga Halimbawa**: Neo4j, Amazon Neptune, ArangoDB
- **Query Language**: Cypher (Neo4j), Gremlin
### Kailan Gamitin ang NoSQL
- Flexible/nagbabagong schema
- Mga kinakailangan sa pahalang na pag-scale
- Mataas na write throughput
- Hierarchical/nested na data
- Mga sistemang ipinamamahagi
- Mga real-time na application
## Disenyo ng Database
### Pagmomodelo ng Entity-Relationship
- **Entity**: Mga bagay/konsepto (Customer, Produkto, Order)
- **Mga Katangian**: Mga katangian ng mga entity (pangalan, presyo, petsa)
- **Mga Relasyon**: Mga koneksyon sa pagitan ng mga entity (isa-sa-isa, isa-sa-marami, marami-sa-marami)
- **Cardinality**: Bilang ng mga pagkakataon sa relasyon
### Mga Pattern ng Disenyo ng Schema
- **Pamana ng Single Table**: Lahat ng uri sa isang table na may uri ng discriminator
- **Pamana ng Class Table**: Paghiwalayin ang mga talahanayan para sa base at mga subclass
- **Concrete Table Inheritance**: Hiwalay na talahanayan para sa bawat kongkretong klase
- **Junction Tables**: Lutasin ang marami-sa-maraming relasyon
- **Mga Talahanayan ng Pag-audit**: Subaybayan ang mga pagbabago (nilikha_sa, na-update_sa, tinanggal_sa)
### Mga Istratehiya sa Pag-index
- **B-Tree**: Default, mga query sa hanay, pag-uuri
- **Hash**: Mga paghahanap ng eksaktong tugma
- **Bitmap**: Mga column na mababa ang cardinality (kasarian, katayuan)
- **Full-Text**: Mga kakayahan sa paghahanap ng teksto
- **Spatial**: Geographic na data (GIS)
- **Composite**: Pinagsama-sama ang maraming column
- **Patakpan**: Kasama ang lahat ng column na kailangan para sa query
## Pag-optimize ng Query
### Mga Plano sa Pagpapatupad
- Pag-unawa kung paano isinasagawa ng database ang mga query
- Pagkilala sa mga bottleneck (mga full table scan, nawawalang index)
- Mga Tool: Ipaliwanag, Ipaliwanag ang PAGSUSURI
### Mga Teknik sa Pag-optimize
- **Paggamit ng Index**: Tiyaking gumagamit ang mga query ng naaangkop na mga index
- **Rewriting ng Query**: Pasimplehin ang mga kumplikadong query
- **Sumali sa Optimization**: Pumili ng mga tamang uri ng pagsali at pagkakasunud-sunod
- **Paghahati**: Hatiin ang malalaking talahanayan (saklaw, hash, listahan)
- **Materialized Views**: Pre-computed na mga resulta ng query
- **Query Caching**: Mag-imbak ng madalas na mga resulta ng query
### Mga Karaniwang Isyu sa Pagganap
- **N+1 Query Problem**: Kinukuha ang nauugnay na data nang hindi mahusay
- **Nawawalang Mga Index**: Ang buong talahanayan ay nag-scan sa malalaking talahanayan
- **Over-indexing**: Mabagal ang pagsusulat dahil sa napakaraming index
- **Lock Contention**: Mga transaksyon na naghihintay ng mga kandado
- **Inefficient Query**: SELECT *, hindi kinakailangang mga pagsali
## Mga Transaksyon at Concurrency
### Mga Antas ng Paghihiwalay ng Transaksyon
- **READ UNCOMMITTED**: Pinakamababang paghihiwalay, posibleng maruruming pagbabasa
- **READ COMMITTED**: Ang naka-commit na data lang ang nakikita (default sa karamihan ng mga DB)
- **REPEATABLE READ**: Ang parehong query ay nagbabalik ng parehong mga resulta sa loob ng transaksyon
- **SERIALIZABLE**: Pinakamataas na paghihiwalay, ang mga transaksyon ay isinasagawa nang sunud-sunod
### Concurrency Control
- **Pessimistic Locking**: I-lock ang mga mapagkukunan bago ma-access
- **Optimistic Locking**: Suriin ang bersyon bago gumawa
- **MVCC (Multi-Version Concurrency Control)**: Panatilihin ang maraming bersyon ng mga row
- **Row-Level Locking**: I-lock ang mga partikular na row
- **Table-Level Locking**: I-lock ang buong talahanayan
### Mga deadlock
- Circular dependency kung saan naghihintay ang mga transaksyon sa isa't isa
- Pag-iwas: Pare-parehong pag-order ng lock, timeout, deadlock detection
- Resolusyon: I-abort ang isang transaksyon
## Pagtitiklop at Pagsusukat
### Mga Uri ng Pagtitiklop
- **Master-Slave**: Isang pangunahin, maramihang nabasang replika
- **Master-Master**: Maramihang primarya, bidirectional replication
- **Multi-Master**: N primarya, kailangan ng paglutas ng salungatan
- **Chain Replication**: Sequential replication sa pamamagitan ng mga node
### Mga Diskarte sa Pagsusukat
- **Vertical Scaling**: Dagdagan ang mga mapagkukunan ng server (CPU, RAM, storage)
- **Horizontal Scaling**: Magdagdag ng higit pang mga server (sharding, partitioning)
- **Read Replicas**: I-offload ang traffic sa pagbasa
- **Sharding**: Hatiin ang data sa mga server ayon sa key/range/hash
- **Federation**: Hatiin ayon sa function/serbisyo
### Consistency Models
- **Malakas na Consistency**: Ang lahat ng node ay nakakakita ng parehong data sa parehong oras
- **Eventual Consistency**: Ang mga node ay nagtatagpo sa paglipas ng panahon
- **Causal Consistency**: Napanatili ang mga ugnayang sanhi-epekto
- **Read-Your-Writes**: Nakikita kaagad ng user ang sarili nilang mga update
## Pag-backup at Pagbawi
### Mga Diskarte sa Pag-backup
- **Buong Backup**: Kumpletuhin ang kopya ng database
- **Incremental Backup**: Mga pagbabago mula noong huling backup
- **Differential Backup**: Mga pagbabago mula noong huling full backup
- **Point-in-Time Recovery**: Ibalik sa partikular na sandali
- **Patuloy na Pag-backup**: Real-time na pagtitiklop sa backup
### Mga Pamamaraan sa Pagbawi
- **RTO (Layunin ng Oras ng Pagbawi)**: Pinakamataas na katanggap-tanggap na downtime
- **RPO (Layunin ng Recovery Point)**: Pinakamataas na katanggap-tanggap na pagkawala ng data
- **Disaster Recovery Plan**: Mga dokumentadong pamamaraan para sa mga pagkabigo
- **Pagsubok**: Mga regular na pagsasanay sa pagbawi
## Seguridad
### Access Control
- **Authentication**: I-verify ang pagkakakilanlan ng user
- **Awtorisasyon**: Magbigay ng mga pahintulot (GRANT, REVOKE)
- **Mga Tungkulin**: Mga pahintulot sa pangkat para sa mas madaling pamamahala
- **Principle of Least Privilege**: Minimum na kinakailangang access
### Proteksyon ng Data
- **Encryption at Rest**: I-encrypt ang nakaimbak na data
- **Pag-encrypt sa Transit**: TLS/SSL para sa mga koneksyon
- **Masking**: Itago ang sensitibong data sa hindi produksyon
- **Tokenization**: Palitan ang sensitibong data ng mga token
### Mga Karaniwang Kahinaan
- **SQL Injection**: Nakakahamak na SQL sa input ng user
- **Pagtaas ng Pribilehiyo**: Pagkuha ng hindi awtorisadong pag-access
- **Pag-log sa Pag-audit**: Subaybayan ang lahat ng aktibidad sa database
- **Pagsunod**: Mga kinakailangan sa GDPR, HIPAA, PCI-DSS
## Modernong Database Technologies
### Mga Cloud Database
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Mga Benepisyo**: Pinamamahalaang serbisyo, auto-scaling, kasama ang mga backup
### Mga Database ng NewSQL
- Pagsamahin ang pagkakapare-pareho ng SQL sa NoSQL scalability
- **Mga Halimbawa**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Mga Tampok**: Ibinahagi, mga transaksyon sa ACID, pahalang na pag-scale
### Mga Database ng Serye ng Oras
- Na-optimize para sa timestamped data
- **Mga Halimbawa**: InfluxDB, TimescaleDB, Prometheus
- **Mga Kaso ng Paggamit**: IoT, pagsubaybay, data sa pananalapi
### Mga Vector Database
- Store at query sa pag-embed ng mga vectors
- **Mga Halimbawa**: Pinecone, Milvus, Weaviate, Qdrant
- **Mga Kaso ng Paggamit**: Semantic na paghahanap, mga sistema ng rekomendasyon, mga AI application
### Mga Multi-Model na Database
- Suportahan ang maramihang mga modelo ng data sa iisang sistema
- **Mga Halimbawa**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibility na walang maraming database
## Mga ORM at Data Access
### Object-Relational Mapping
- **Layunin**: I-map ang mga talahanayan ng database sa mga bagay sa programming
- **Mga sikat na ORM**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Framework ng Entity
### Mga benepisyo
- Abstraction mula sa SQL
- Uri ng kaligtasan
- Pamamahala ng migrasyon
- Mga API sa pagbuo ng query
### Mga Kakulangan
- Overhead ng pagganap
- Mas mahirap isulat ang mga kumplikadong query
- N+1 na mga problema sa query
- Learning curve
## Pangangasiwa ng Database
### Mga Responsibilidad ng DBA
- Pag-install at pagsasaayos
- Pag-tune ng pagganap
- Pag-backup at pagbawi
- Pamamahala ng seguridad
- Pagpaplano ng kapasidad
- Pagsubaybay at pag-alerto
- Pamamahala ng patch
### Mga Sukatan sa Pagsubaybay
- Oras ng pagtugon sa query
- Throughput (mga transaksyon sa bawat segundo)
- Bilang ng koneksyon
- Cache hit ratio
- Disk I/O
- I-lock ang oras ng paghihintay
- Lag ng pagtitiklop
### Mga Gawain sa Pagpapanatili
- **Vacuum/Analyze**: I-update ang mga istatistika, bawiin ang espasyo
- **Pagbuo muli ng Index**: Defragment index
- **Mga Update sa Istatistika**: Panatilihing alam ang query optimizer
- **Pag-ikot ng Log**: Pamahalaan ang mga laki ng log file
- **Pagpaplano ng Kapasidad**: Hulaan ang paglaki, pag-upgrade ng plano