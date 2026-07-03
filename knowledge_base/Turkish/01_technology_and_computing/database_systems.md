# Veritabanı Sistemleri

## Veritabanı Temelleri

### Veritabanı Nedir?
Veritabanı, verinin verimli biçimde alınması, eklenmesi, güncellenmesi ve silinmesi için tasarlanmış; elektronik olarak saklanan yapılandırılmış bilgilerin düzenli bir koleksiyonudur.

### Veritabanı Yönetim Sistemleri (DBMS)
Son kullanıcılar, uygulamalar ve veritabanının kendisiyle etkileşime girerek veriyi toplamak ve analiz etmek için kullanılan yazılımlardır. Örnekler: MySQL, PostgreSQL, Oracle, MongoDB.

### Temel Kavramlar
- **Şema (Schema)**: Veritabanının yapısı/organizasyonu (tablolar, alanlar, ilişkiler)
- **Anlık Durum (Instance)**: Belirli bir andaki gerçek veri
- **ACID Özellikleri**: Atomicity, Consistency, Isolation, Durability
- **CAP Teoremi**: Consistency, Availability, Partition Tolerance (2'si seçilir)
- **Normalizasyon**: Fazlalığı azaltmak için veriyi düzenleme
- **Denormalizasyon**: Okuma performansını artırmak için fazlalık ekleme

## İlişkisel Veritabanları (SQL)

### Temel Kavramlar
- **Tablolar**: Satırlar (records) ve sütunlar (fields)
- **Birincil Anahtar (Primary Key)**: Her satır için benzersiz tanımlayıcı
- **Yabancı Anahtar (Foreign Key)**: Başka bir tablodaki birincil anahtara referans
- **İndeksler**: Sorgu hızını artıran veri yapıları
- **Görünümler**: Sorgu sonuçlarına dayalı sanal tablolar
- **Saklı Yordamlar**: Önceden derlenmiş SQL kod blokları
- **Tetikleyiciler**: Veri değişikliklerinde otomatik çalışan işlemler

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

### Join İşlemleri
- **INNER JOIN**: Her iki tablodaki eşleşen satırları döndürür
- **LEFT JOIN**: Sol tablodaki tüm satırlar, sağdan eşleşenler
- **RIGHT JOIN**: Sağ tablodaki tüm satırlar, soldan eşleşenler
- **FULL OUTER JOIN**: Her iki tablodaki tüm satırlar
- **CROSS JOIN**: Her iki tablonun Kartezyen çarpımı
- **SELF JOIN**: Tablonun kendisiyle birleştirilmesi

### Normalizasyon Biçimleri
- **1NF**: Atomik değerler, tekrar eden grup yok
- **2NF**: 1NF + kısmi bağımlılık yok (tüm non-key öznitelikler tam primary key'e bağlıdır)
- **3NF**: 2NF + geçişli bağımlılık yok (non-key öznitelikler başka non-key özniteliklere bağlı değildir)
- **BCNF**: 3NF'in daha güçlü hâli, her determinant bir candidate key'dir
- **4NF**: Çok değerli bağımlılık yok
- **5NF**: Join bağımlılığı yok

### Popüler RDBMS'ler
- **PostgreSQL**: Gelişmiş özellikler, genişletilebilirlik, ACID uyumluluğu
- **MySQL**: Yaygın kullanım, hızlı okumalar, web uygulamaları
- **Oracle**: Kurumsal özellikler, ölçeklenebilirlik, yüksek maliyet
- **SQL Server**: Microsoft ekosistemi, entegre araçlar
- **SQLite**: Embedded, serverless, hafif
- **MariaDB**: MySQL fork'u, açık kaynak

## NoSQL Veritabanları

### NoSQL Veritabanı Türleri

#### Belge Depoları
- **Yapı**: JSON benzeri belgeler (BSON)
- **Kullanım Alanları**: İçerik yönetimi, kataloglar, kullanıcı profilleri
- **Örnekler**: MongoDB, CouchDB, DocumentDB
- **Sorgu Örneği** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Anahtar-Değer Depoları
- **Yapı**: Basit anahtar-değer çiftleri
- **Kullanım Alanları**: Önbellekleme, oturumlar, alışveriş sepetleri
- **Örnekler**: Redis, DynamoDB, Riak
- **Özellikler**: Hızlı, basit, sınırlı sorgulama

#### Sütun Ailesi Depoları
- **Yapı**: Aileler hâlinde gruplanmış sütunlar
- **Kullanım Alanları**: Büyük veri, analitik, time-series
- **Örnekler**: Cassandra, HBase, ScyllaDB
- **Özellikler**: Yazma odaklı, dağıtık, ölçeklenebilir

#### Grafik Veritabanları
- **Yapı**: Düğümler, kenarlar, özellikler
- **Kullanım Alanları**: Sosyal ağlar, dolandırıcılık tespiti, öneriler
- **Örnekler**: Neo4j, Amazon Neptune, ArangoDB
- **Sorgu Dili**: Cypher (Neo4j), Gremlin

### NoSQL Ne Zaman Kullanılır?
- Esnek/gelişen şema
- Yatay ölçekleme gereksinimleri
- Yüksek yazma hacmi
- Hiyerarşik/iç içe veri
- Dağıtık sistemler
- Gerçek zamanlı uygulamalar

## Veritabanı Tasarımı

### Varlık-İlişki Modelleme
- **Varlıklar**: Nesneler/kavramlar (Customer, Product, Order)
- **Öznitelikler**: Varlıkların özellikleri (name, price, date)
- **İlişkiler**: Varlıklar arası bağlantılar (one-to-one, one-to-many, many-to-many)
- **Kardinalite**: İlişkideki örnek sayısı

### Şema Tasarım Kalıpları
- **Single Table Inheritance**: Tür ayracıyla tüm tiplerin tek tabloda tutulması
- **Class Table Inheritance**: Temel sınıf ve alt sınıflar için ayrı tablolar
- **Concrete Table Inheritance**: Her somut sınıf için ayrı tablo
- **Junction Tables**: Many-to-many ilişkileri çözme
- **Audit Tables**: Değişiklikleri izleme (created_at, updated_at, deleted_at)

### İndeksleme Stratejileri
- **B-Tree**: Varsayılan, aralık sorguları, sıralama
- **Hash**: Tam eşleşme aramaları
- **Bitmap**: Düşük kardinaliteli sütunlar (gender, status)
- **Tam Metin**: Metin arama yetenekleri
- **Mekânsal**: Coğrafi veri (GIS)
- **Bileşik**: Birden çok sütunun birleştirilmesi
- **Kapsayıcı**: Sorgunun ihtiyaç duyduğu tüm sütunları içerir

## Sorgu Optimizasyonu

### Çalıştırma Planları
- Veritabanının sorguları nasıl çalıştırdığını anlamak
- Darboğazları belirlemek (full table scan, eksik index)
- Araçlar: EXPLAIN, EXPLAIN ANALYZE

### Optimizasyon Teknikleri
- **İndeks Kullanımı**: Sorguların uygun index'leri kullandığından emin olma
- **Sorgu Yeniden Yazımı**: Karmaşık sorguları sadeleştirme
- **Join Optimizasyonu**: Doğru join türlerini ve sırasını seçme
- **Bölümleme**: Büyük tabloları bölme (range, hash, list)
- **Materyalize Görünümler**: Önceden hesaplanmış sorgu sonuçları
- **Sorgu Önbellekleme**: Sık kullanılan sorgu sonuçlarını saklama

### Yaygın Performans Sorunları
- **N+1 Sorgu Problemi**: İlişkili veriyi verimsiz biçimde çekme
- **Eksik İndeksler**: Büyük tablolarda full table scan yapılması
- **Aşırı İndeksleme**: Çok fazla index nedeniyle yavaş yazma
- **Kilit Çakışması**: Transaction'ların kilit beklemesi
- **Verimsiz Sorgular**: SELECT *, gereksiz join'ler

## İşlemler ve Eşzamanlılık

### Transaction Isolation Levels
- **READ UNCOMMITTED**: En düşük izolasyon, dirty read mümkün
- **READ COMMITTED**: Yalnızca commit edilmiş veri görünür (çoğu DB'de varsayılan)
- **REPEATABLE READ**: Aynı transaction içinde aynı sorgu aynı sonucu döndürür
- **SERIALIZABLE**: En yüksek izolasyon, transaction'lar sıralı yürür

### Eşzamanlılık Kontrolü
- **Kötümser Kilitleme**: Erişimden önce kaynakları kilitleme
- **İyimser Kilitleme**: Commit'ten önce sürüm kontrolü
- **MVCC (Multi-Version Concurrency Control)**: Satırların birden fazla sürümünü tutma
- **Satır Düzeyinde Kilitleme**: Belirli satırları kilitleme
- **Tablo Düzeyinde Kilitleme**: Tüm tabloyu kilitleme

### Deadlock'lar
- Transaction'ların birbirini beklediği döngüsel bağımlılık durumu
- Önleme: Tutarlı kilit sıralaması, timeout'lar, deadlock tespiti
- Çözüm: Bir transaction'ı iptal etme

## Çoğaltma ve Ölçekleme

### Çoğaltma Türleri
- **Master-Slave**: Bir primary, birden çok read replica
- **Master-Master**: Birden çok primary, çift yönlü çoğaltma
- **Multi-Master**: N adet primary, çatışma çözümü gerekir
- **Chain Replication**: Düğümler üzerinden sıralı çoğaltma

### Ölçekleme Yaklaşımları
- **Dikey Ölçekleme**: Sunucu kaynaklarını artırma (CPU, RAM, storage)
- **Yatay Ölçekleme**: Daha fazla sunucu ekleme (sharding, partitioning)
- **Read Replicas**: Okuma trafiğini başka düğümlere aktarma
- **Sharding**: Veriyi key/range/hash'e göre sunuculara bölme
- **Federation**: İşleve/hizmete göre ayırma

### Tutarlılık Modelleri
- **Güçlü Tutarlılık**: Tüm düğümler aynı anda aynı veriyi görür
- **Nihai Tutarlılık**: Düğümler zaman içinde yakınsar
- **Nedensel Tutarlılık**: Neden-sonuç ilişkileri korunur
- **Read-Your-Writes**: Kullanıcı kendi güncellemelerini hemen görür

## Yedekleme ve Kurtarma

### Yedekleme Stratejileri
- **Tam Yedek**: Veritabanının tam kopyası
- **Artımlı Yedek**: Son yedekten beri değişenler
- **Fark Yedeği**: Son full backup'tan beri değişenler
- **Point-in-Time Recovery**: Belirli bir ana geri dönme
- **Sürekli Yedekleme**: Yedek ortama gerçek zamanlı çoğaltma

### Kurtarma Prosedürleri
- **RTO (Recovery Time Objective)**: Kabul edilebilir azami kesinti süresi
- **RPO (Recovery Point Objective)**: Kabul edilebilir azami veri kaybı
- **Felaket Kurtarma Planı**: Arızalar için belgelenmiş prosedürler
- **Test**: Düzenli kurtarma tatbikatları

## Güvenlik

### Erişim Kontrolü
- **Kimlik Doğrulama**: Kullanıcı kimliğini doğrulama
- **Yetkilendirme**: Yetki verme (GRANT, REVOKE)
- **Roller**: Yönetimi kolaylaştırmak için izinleri gruplama
- **En Az Ayrıcalık İlkesi**: Gereken en düşük erişim seviyesi

### Veri Koruma
- **Beklemedeki Şifreleme**: Saklanan veriyi şifreleme
- **Aktarım Sırasında Şifreleme**: Bağlantılar için TLS/SSL
- **Maskeleme**: Production dışı ortamlarda hassas veriyi gizleme
- **Tokenizasyon**: Hassas veriyi token'larla değiştirme

### Yaygın Açıklar
- **SQL Injection**: Kullanıcı girdisindeki kötü amaçlı SQL
- **Yetki Yükseltme**: Yetkisiz erişim elde etme
- **Denetim Günlükleme**: Tüm veritabanı etkinliklerini izleme
- **Uyumluluk**: GDPR, HIPAA, PCI-DSS gereksinimleri

## Modern Veritabanı Teknolojileri

### Bulut Veritabanları
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Avantajlar**: Yönetilen hizmet, otomatik ölçekleme, dâhil yedekleme

### NewSQL Veritabanları
- SQL tutarlılığını NoSQL ölçeklenebilirliğiyle birleştirir
- **Örnekler**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Özellikler**: Dağıtık yapı, ACID transaction'lar, yatay ölçekleme

### Time-Series Veritabanları
- Zaman damgalı veri için optimize edilmiştir
- **Örnekler**: InfluxDB, TimescaleDB, Prometheus
- **Kullanım Alanları**: IoT, izleme, finansal veri

### Vektör Veritabanları
- Embedding vektörlerini saklar ve sorgular
- **Örnekler**: Pinecone, Milvus, Weaviate, Qdrant
- **Kullanım Alanları**: Anlamsal arama, öneri sistemleri, AI uygulamaları

### Çok Modelli Veritabanları
- Tek sistem içinde birden fazla veri modelini destekler
- **Örnekler**: ArangoDB, OrientDB, Azure Cosmos DB
- **Avantajı**: Birden fazla veritabanı olmadan esneklik

## ORMs ve Veri Erişimi

### Object-Relational Mapping
- **Amacı**: Veritabanı tablolarını programlama nesnelerine eşlemek
- **Popüler ORM'ler**:
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

### İzleme Metrikleri
- Sorgu yanıt süresi
- Throughput (saniye başına transaction)
- Bağlantı sayısı
- Cache hit ratio
- Disk I/O
- Kilit bekleme süresi
- Replication gecikmesi

### Bakım Görevleri
- **Vacuum/Analyze**: İstatistikleri güncelleme, alan geri kazanımı
- **Index Rebuilding**: Index parçalanmasını giderme
- **Statistics Updates**: Sorgu optimizer'ını güncel tutma
- **Log Rotation**: Log dosyası boyutlarını yönetme
- **Capacity Planning**: Büyümeyi öngörme, yükseltmeleri planlama
