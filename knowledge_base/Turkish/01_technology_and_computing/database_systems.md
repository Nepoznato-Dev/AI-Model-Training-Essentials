# Veritabanı Sistemleri

## Veritabanı Temelleri

### Veritabanı Nedir?
Veritabanı, verinin verimli şekilde alınması, eklenmesi, güncellenmesi ve silinmesi için tasarlanmış, elektronik olarak saklanan yapılandırılmış bilgilerin organize edilmiş bir koleksiyonudur.

### Database Management Systems (DBMS)
Son kullanıcılar, uygulamalar ve veritabanının kendisiyle etkileşime girerek veriyi toplamak ve analiz etmek için kullanılan yazılımlardır. Örnekler: MySQL, PostgreSQL, Oracle, MongoDB.

### Temel Kavramlar
- **Schema**: Veritabanının yapısı/organizasyonu (tablolar, alanlar, ilişkiler)
- **Instance**: Belirli bir andaki gerçek veri
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance (2'si seçilir)
- **Normalization**: Fazlalığı azaltmak için veriyi düzenleme
- **Denormalization**: Okuma performansını artırmak için fazlalık ekleme

## Relational Databases (SQL)

### Temel Kavramlar
- **Tables**: Satırlar (records) ve sütunlar (fields)
- **Primary Key**: Her satır için benzersiz tanımlayıcı
- **Foreign Key**: Başka bir tablodaki primary key'e referans
- **Indexes**: Sorgu hızını artıran veri yapıları
- **Views**: Sorgu sonuçlarına dayalı sanal tablolar
- **Stored Procedures**: Önceden derlenmiş SQL kod blokları
- **Triggers**: Veri değişikliklerinde otomatik çalışan işlemler

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
- **INNER JOIN**: Her iki tablodaki eşleşen satırları döndürür
- **LEFT JOIN**: Sol tablodaki tüm satırlar, sağdan eşleşenler
- **RIGHT JOIN**: Sağ tablodaki tüm satırlar, soldan eşleşenler
- **FULL OUTER JOIN**: Her iki tablodaki tüm satırlar
- **CROSS JOIN**: Her iki tablonun Kartezyen çarpımı
- **SELF JOIN**: Tabloyun kendisiyle join edilmesi

### Normalization Forms
- **1NF**: Atomik değerler, tekrar eden grup yok
- **2NF**: 1NF + kısmi bağımlılık yok (tüm non-key öznitelikler tam primary key'e bağlıdır)
- **3NF**: 2NF + geçişli bağımlılık yok (non-key öznitelikler başka non-key özniteliklere bağlı değildir)
- **BCNF**: 3NF'in daha güçlü hali, her determinant bir candidate key'dir
- **4NF**: Çok değerli bağımlılık yok
- **5NF**: Join bağımlılığı yok

### Popüler RDBMS'ler
- **PostgreSQL**: Gelişmiş özellikler, genişletilebilirlik, ACID uyumluluğu
- **MySQL**: Yaygın kullanım, hızlı okumalar, web uygulamaları
- **Oracle**: Kurumsal özellikler, ölçeklenebilirlik, yüksek maliyet
- **SQL Server**: Microsoft ekosistemi, entegre araçlar
- **SQLite**: Embedded, serverless, hafif
- **MariaDB**: MySQL fork'u, open-source

## NoSQL Databases

### NoSQL Veritabanı Türleri

#### Document Stores
- **Structure**: JSON benzeri belgeler (BSON)
- **Use Cases**: İçerik yönetimi, kataloglar, kullanıcı profilleri
- **Examples**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Key-Value Stores
- **Structure**: Basit anahtar-değer çiftleri
- **Use Cases**: Caching, session'lar, alışveriş sepetleri
- **Examples**: Redis, DynamoDB, Riak
- **Characteristics**: Hızlı, basit, sınırlı sorgulama

#### Column-Family Stores
- **Structure**: Family'ler halinde gruplanmış sütunlar
- **Use Cases**: Büyük veri, analitik, time-series
- **Examples**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Yazma odaklı, dağıtık, ölçeklenebilir

#### Graph Databases
- **Structure**: Düğümler, kenarlar, özellikler
- **Use Cases**: Sosyal ağlar, dolandırıcılık tespiti, öneriler
- **Examples**: Neo4j, Amazon Neptune, ArangoDB
- **Query Language**: Cypher (Neo4j), Gremlin

### NoSQL Ne Zaman Kullanılır?
- Esnek/gelişen schema
- Yatay ölçekleme gereksinimleri
- Yüksek yazma hacmi
- Hiyerarşik/iç içe veri
- Dağıtık sistemler
- Gerçek zamanlı uygulamalar

## Veritabanı Tasarımı

### Entity-Relationship Modeling
- **Entities**: Nesneler/kavramlar (Customer, Product, Order)
- **Attributes**: Varlıkların özellikleri (name, price, date)
- **Relationships**: Varlıklar arası bağlantılar (one-to-one, one-to-many, many-to-many)
- **Cardinality**: İlişkideki örnek sayısı

### Schema Design Patterns
- **Single Table Inheritance**: Tür ayracıyla tüm tiplerin tek tabloda tutulması
- **Class Table Inheritance**: Base ve alt sınıflar için ayrı tablolar
- **Concrete Table Inheritance**: Her somut sınıf için ayrı tablo
- **Junction Tables**: Many-to-many ilişkileri çözme
- **Audit Tables**: Değişiklikleri izleme (created_at, updated_at, deleted_at)

### Indexing Strategies
- **B-Tree**: Varsayılan, aralık sorguları, sıralama
- **Hash**: Tam eşleşme aramaları
- **Bitmap**: Düşük kardinaliteli sütunlar (gender, status)
- **Full-Text**: Metin arama yetenekleri
- **Spatial**: Coğrafi veri (GIS)
- **Composite**: Birleştirilmiş çoklu sütunlar
- **Covering**: Sorgunun ihtiyaç duyduğu tüm sütunları içerir

## Query Optimization

### Execution Plans
- Veritabanının sorguları nasıl çalıştırdığını anlamak
- Darboğazları belirlemek (full table scan, eksik index)
- Araçlar: EXPLAIN, EXPLAIN ANALYZE

### Optimization Techniques
- **Index Usage**: Sorguların uygun index'leri kullandığından emin olma
- **Query Rewriting**: Karmaşık sorguları sadeleştirme
- **Join Optimization**: Doğru join türlerini ve sırasını seçme
- **Partitioning**: Büyük tabloları bölme (range, hash, list)
- **Materialized Views**: Önceden hesaplanmış sorgu sonuçları
- **Query Caching**: Sık kullanılan sorgu sonuçlarını saklama

### Yaygın Performans Sorunları
- **N+1 Query Problem**: İlişkili veriyi verimsiz şekilde çekme
- **Missing Indexes**: Büyük tablolarda full table scan
- **Over-indexing**: Çok fazla index nedeniyle yavaş yazma
- **Lock Contention**: Transaction'ların lock beklemesi
- **Inefficient Queries**: SELECT *, gereksiz join'ler

## Transactions ve Concurrency

### Transaction Isolation Levels
- **READ UNCOMMITTED**: En düşük izolasyon, dirty read mümkün
- **READ COMMITTED**: Yalnızca commit edilmiş veri görünür (çoğu DB'de varsayılan)
- **REPEATABLE READ**: Aynı transaction içinde aynı sorgu aynı sonucu döndürür
- **SERIALIZABLE**: En yüksek izolasyon, transaction'lar sıralı yürür

### Concurrency Control
- **Pessimistic Locking**: Erişimden önce kaynakları kilitleme
- **Optimistic Locking**: Commit'ten önce sürüm kontrolü
- **MVCC (Multi-Version Concurrency Control)**: Satırların birden fazla sürümünü tutma
- **Row-Level Locking**: Belirli satırları kilitleme
- **Table-Level Locking**: Tüm tabloyu kilitleme

### Deadlocks
- Transaction'ların birbirini beklediği döngüsel bağımlılık durumu
- Önleme: Tutarlı kilit sıralaması, timeout'lar, deadlock tespiti
- Çözüm: Bir transaction'ı iptal etme

## Replication ve Scaling

### Replication Types
- **Master-Slave**: Bir primary, birden çok read replica
- **Master-Master**: Birden çok primary, çift yönlü çoğaltma
- **Multi-Master**: N adet primary, çatışma çözümü gerekir
- **Chain Replication**: Düğümler üzerinden sıralı çoğaltma

### Scaling Approaches
- **Vertical Scaling**: Sunucu kaynaklarını artırma (CPU, RAM, storage)
- **Horizontal Scaling**: Daha fazla sunucu ekleme (sharding, partitioning)
- **Read Replicas**: Okuma trafiğini başka düğümlere aktarma
- **Sharding**: Veriyi key/range/hash'e göre sunuculara bölme
- **Federation**: İşleve/hizmete göre ayırma

### Consistency Models
- **Strong Consistency**: Tüm düğümler aynı anda aynı veriyi görür
- **Eventual Consistency**: Düğümler zaman içinde yakınsar
- **Causal Consistency**: Neden-sonuç ilişkileri korunur
- **Read-Your-Writes**: Kullanıcı kendi güncellemelerini hemen görür

## Backup ve Recovery

### Backup Strategies
- **Full Backup**: Veritabanının tam kopyası
- **Incremental Backup**: Son yedekten beri değişenler
- **Differential Backup**: Son full backup'tan beri değişenler
- **Point-in-Time Recovery**: Belirli bir ana geri dönme
- **Continuous Backup**: Yedek ortama gerçek zamanlı çoğaltma

### Recovery Procedures
- **RTO (Recovery Time Objective)**: Kabul edilebilir azami kesinti süresi
- **RPO (Recovery Point Objective)**: Kabul edilebilir azami veri kaybı
- **Disaster Recovery Plan**: Arızalar için belgelenmiş prosedürler
- **Testing**: Düzenli kurtarma tatbikatları

## Güvenlik

### Access Control
- **Authentication**: Kullanıcı kimliğini doğrulama
- **Authorization**: Yetki verme (GRANT, REVOKE)
- **Roles**: Yönetimi kolaylaştırmak için izinleri gruplama
- **Principle of Least Privilege**: Gereken en düşük erişim seviyesi

### Veri Koruma
- **Encryption at Rest**: Saklanan veriyi şifreleme
- **Encryption in Transit**: Bağlantılar için TLS/SSL
- **Masking**: Production dışı ortamlarda hassas veriyi gizleme
- **Tokenization**: Hassas veriyi token'larla değiştirme

### Yaygın Açıklar
- **SQL Injection**: Kullanıcı girdisindeki kötü amaçlı SQL
- **Privilege Escalation**: Yetkisiz erişim elde etme
- **Audit Logging**: Tüm veritabanı etkinliklerini izleme
- **Compliance**: GDPR, HIPAA, PCI-DSS gereksinimleri

## Modern Veritabanı Teknolojileri

### Cloud Databases
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Benefits**: Managed service, auto-scaling, dahil yedekleme

### NewSQL Databases
- SQL tutarlılığını NoSQL ölçeklenebilirliğiyle birleştirir
- **Examples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Dağıtık yapı, ACID transaction'lar, yatay ölçekleme

### Time-Series Databases
- Zaman damgalı veri için optimize edilmiştir
- **Examples**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, izleme, finansal veri

### Vector Databases
- Embedding vektörlerini saklar ve sorgular
- **Examples**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Semantic search, öneri sistemleri, AI uygulamaları

### Multi-Model Databases
- Tek sistem içinde birden fazla veri modelini destekler
- **Examples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Birden fazla veritabanı olmadan esneklik

## ORMs ve Veri Erişimi

### Object-Relational Mapping
- **Purpose**: Veritabanı tablolarını programlama nesnelerine eşleme
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Faydalar
- SQL'den soyutlama
- Tür güvenliği
- Migration yönetimi
- Query building API'leri

### Dezavantajlar
- Performans ek yükü
- Karmaşık sorguların daha zor yazılması
- N+1 query problemleri
- Öğrenme eğrisi

## Veritabanı Yönetimi

### DBA Sorumlulukları
- Kurulum ve yapılandırma
- Performans ayarı
- Yedekleme ve kurtarma
- Güvenlik yönetimi
- Kapasite planlama
- İzleme ve uyarı yönetimi
- Yama yönetimi

### Monitoring Metrics
- Sorgu yanıt süresi
- Throughput (saniye başına transaction)
- Bağlantı sayısı
- Cache hit ratio
- Disk I/O
- Lock bekleme süresi
- Replication gecikmesi

### Maintenance Tasks
- **Vacuum/Analyze**: İstatistikleri güncelleme, alan geri kazanımı
- **Index Rebuilding**: Index parçalanmasını giderme
- **Statistics Updates**: Sorgu optimizer'ını güncel tutma
- **Log Rotation**: Log dosyası boyutlarını yönetme
- **Capacity Planning**: Büyümeyi öngörme, yükseltmeleri planlama
