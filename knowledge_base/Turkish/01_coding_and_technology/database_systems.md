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
# Veritabanı Sistemleri
## Veritabanı Temelleri
### Veritabanı Nedir?
Veritabanı, verilerin verimli bir şekilde alınması, eklenmesi, güncellenmesi ve silinmesi için tasarlanmış, elektronik olarak depolanan yapılandırılmış bilgilerin düzenli bir koleksiyonudur.
### Veritabanı Yönetim Sistemleri (DBMS)
Verileri yakalamak ve analiz etmek için son kullanıcılarla, uygulamalarla ve veritabanının kendisiyle etkileşime giren yazılım. Örnekler: MySQL, PostgreSQL, Oracle, MongoDB.
### Temel Kavramlar
- **Şema**: Veritabanının yapısı/organizasyonu (tablolar, alanlar, ilişkiler)
- **Örnek**: Belirli bir anda depolanan gerçek veriler
- **ASİT Özellikleri**: Atomiklik, Tutarlılık, Yalıtım, Dayanıklılık
- **CAP Teoremi**: Tutarlılık, Kullanılabilirlik, Bölüm Toleransı (2'yi seçin)
- **Normalleştirme**: Artıklığı azaltmak için verilerin düzenlenmesi
- **Denormalizasyon**: Okuma performansını iyileştirmek için artıklık ekleme
## İlişkisel Veritabanları (SQL)
### Temel Kavramlar
- **Tablolar**: Satırlar (kayıtlar) ve sütunlar (alanlar)
- **Birincil Anahtar**: Her satır için benzersiz tanımlayıcı
- **Yabancı Anahtar**: Başka bir tablodaki birincil anahtara referans
- **Dizinler**: Sorgu hızını artıran veri yapıları
- **Görünümler**: Sorgu sonuçlarına dayalı sanal tablolar
- **Saklı Prosedürler**: Önceden derlenmiş SQL kod blokları
- **Tetikleyiciler**: Veri değişikliklerinde otomatik işlemler
### SQL İşlemleri (CRUD)```sql
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

### Katılma
- **INNER JOIN**: Her iki tablodan eşleşen satırları döndürür
- **LEFT JOIN**: Soldaki tablodaki tüm satırlar, sağdaki eşleşmeler
- **RIGHT JOIN**: Tablonun sağındaki tüm satırlar, soldaki eşleşmeler
- **FULL OUTER JOIN**: Her iki tablodaki tüm satırlar
- **CROSS JOIN**: Her iki tablonun kartezyen çarpımı
- **SELF JOIN**: Kendisiyle birleştirilmiş tablo
### Normalleştirme Formları
- **1NF**: Atomik değerler, tekrarlanan gruplar yok
- **2NF**: 1NF + kısmi bağımlılık yok (anahtar olmayan tüm özellikler birincil anahtarın tamamına bağlıdır)
- **3NF**: 2NF + geçişli bağımlılık yok (anahtar olmayan nitelikler diğer anahtar olmayan niteliklere bağlı değildir)
- **BCNF**: Daha güçlü 3NF, her belirleyici bir aday anahtardır
- **4NF**: Çok değerli bağımlılık yok
- **5NF**: Birleştirme bağımlılığı yok
### Popüler RDBMS
- **PostgreSQL**: Gelişmiş özellikler, genişletilebilir, ACID uyumlu
- **MySQL**: Yaygın olarak kullanılan, hızlı okunan, web uygulamaları
- **Oracle**: Kurumsal özellikler, ölçeklenebilirlik, pahalı
- **SQL Server**: Microsoft ekosistemi, entegre araçlar
- **SQLite**: Gömülü, sunucusuz, hafif
- **MariaDB**: MySQL çatalı, açık kaynak
## NoSQL Veritabanları
### NoSQL Veritabanlarının Türleri
#### Belge Depoları
- **Yapı**: JSON benzeri belgeler (BSON)
- **Kullanım Örnekleri**: İçerik yönetimi, kataloglar, kullanıcı profilleri
- **Örnekler**: MongoDB, CouchDB, DocumentDB
- **Sorgu Örneği** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Anahtar-Değer Depoları
- **Yapı**: Basit anahtar/değer çiftleri
- **Kullanım Örnekleri**: Önbelleğe alma, oturumlar, alışveriş sepetleri
- **Örnekler**: Redis, DynamoDB, Riak
- **Özellikler**: Hızlı, basit, sınırlı sorgulama
#### Sütun-Aile Mağazaları
- **Yapı**: Aileler halinde gruplandırılmış sütunlar
- **Kullanım Örnekleri**: Büyük veri, analiz, zaman serisi
- **Örnekler**: Cassandra, HBase, ScyllaDB
- **Özellikler**: Yazma için optimize edilmiş, dağıtılmış, ölçeklenebilir
#### Grafik Veritabanları
- **Yapı**: Düğümler, kenarlar, özellikler
- **Kullanım Örnekleri**: Sosyal ağlar, dolandırıcılık tespiti, öneriler
- **Örnekler**: Neo4j, Amazon Neptune, ArangoDB
- **Sorgu Dili**: Cypher (Neo4j), Gremlin
### NoSQL Ne Zaman Kullanılmalı
- Esnek/gelişen şema
- Yatay ölçeklendirme gereksinimleri
- Yüksek yazma verimi
- Hiyerarşik/iç içe geçmiş veriler
- Dağıtık sistemler
- Gerçek zamanlı uygulamalar
## Veritabanı Tasarımı
### Varlık-İlişki Modellemesi
- **Varlıklar**: Nesneler/kavramlar (Müşteri, Ürün, Sipariş)
- **Nitelikler**: Varlıkların özellikleri (isim, fiyat, tarih)
- **İlişkiler**: Varlıklar arasındaki bağlantılar (bire bir, bire çok, çoktan çoğa)
- **Önemlilik**: İlişkideki örneklerin sayısı
### Şema Tasarım Desenleri
- **Tek Tablo Mirası**: Tür ayırıcıyla birlikte tüm türler tek bir tabloda
- **Sınıf Tablosu Mirası**: Temel ve alt sınıflar için ayrı tablolar
- **Beton Tablo Mirası**: Her beton sınıfı için ayrı tablo
- **Bağlantı Tabloları**: Çoka çok ilişkileri çözme
- **Denetim Tabloları**: Değişiklikleri takip edin (created_at, güncellendi_at, silindi_at)
### Dizin Oluşturma Stratejileri
- **B-Tree**: Varsayılan, aralık sorguları, sıralama
- **Hash**: Tam eşleşme aramaları
- **Bitmap**: Düşük kardinaliteli sütunlar (cinsiyet, durum)
- **Tam Metin**: Metin arama özellikleri
- **Uzamsal**: Coğrafi veriler (GIS)
- **Bileşik**: Birden çok sütun birleştirildi
- **Kapsama**: Sorgu için gereken tüm sütunları içerir
## Sorgu Optimizasyonu
### Uygulama Planları
- Veritabanının sorguları nasıl yürüttüğünü anlamak
- Darboğazların belirlenmesi (tam tablo taramaları, eksik indeksler)
- Araçlar: AÇIKLAMA, AÇIKLAMA ANALİZİ
### Optimizasyon Teknikleri
- **Dizin Kullanımı**: Sorguların uygun dizinleri kullandığından emin olun
- **Sorgu Yeniden Yazma**: Karmaşık sorguları basitleştirin
- **Katılım Optimizasyonu**: Doğru birleştirme türlerini ve sırasını seçin
- **Bölümlendirme**: Büyük tabloları bölme (aralık, karma, liste)
- **Gerçekleştirilmiş Görünümler**: Önceden hesaplanmış sorgu sonuçları
- **Sorgu Önbelleğe Alma**: Sık yapılan sorgu sonuçlarını saklayın
### Yaygın Performans Sorunları
- **N+1 Sorgu Sorunu**: İlgili verilerin verimsiz bir şekilde getirilmesi
- **Eksik Dizinler**: Büyük tablolarda tam tablo taramaları
- **Aşırı indeksleme**: Çok fazla indeks nedeniyle yavaş yazma
- **Kilit Çekişmesi**: Kilitlenmeyi bekleyen işlemler
- **Verimsiz Sorgular**: SELECT *, gereksiz birleştirmeler
## İşlemler ve Eşzamanlılık
### İşlem Yalıtım Düzeyleri
- **TAMAMLANMAMIŞ OKUYUN**: En düşük izolasyon, kirli okumalar mümkün
- **KABUL EDİLEN OKUMA**: Yalnızca taahhüt edilen veriler görünür (çoğu veritabanında varsayılan)
- **TEKRARLANABİLİR OKUMA**: Aynı sorgu, işlem içinde aynı sonuçları döndürür
- **SERİ hale getirilebilir**: En yüksek izolasyon, işlemler sırayla yürütülür
### Eşzamanlılık Kontrolü
- **Kötümser Kilitleme**: Kaynakları erişimden önce kilitleyin
- **İyimser Kilitleme**: Kaydetmeden önce sürümü kontrol edin
- **MVCC (Çok Sürümlü Eşzamanlılık Kontrolü)**: Satırların birden çok sürümünü koruyun
- **Satır Düzeyinde Kilitleme**: Belirli satırları kilitle
- **Tablo Düzeyinde Kilitleme**: Tüm tabloyu kilitle
### Kilitlenmeler
- İşlemlerin birbirini beklediği döngüsel bağımlılık
- Önleme: Tutarlı kilit sıralaması, zaman aşımları, kilitlenme tespiti
- Çözüm: Bir işlemi iptal edin
## Çoğaltma ve Ölçeklendirme
### Çoğaltma Türleri
- **Master-Slave**: Bir birincil, birden fazla okuma kopyası
- **Master-Master**: Çoklu birinciller, çift yönlü çoğaltma
- **Multi-Master**: N ön seçim, çatışma çözümü gerekiyor
- **Zincir Çoğaltma**: Düğümler aracılığıyla sıralı çoğaltma
### Ölçeklendirme Yaklaşımları
- **Dikey Ölçeklendirme**: Sunucu kaynaklarını artırın (CPU, RAM, depolama)
- **Yatay Ölçeklendirme**: Daha fazla sunucu ekleme (parçalama, bölümleme)
- **Okuma Kopyaları**: Okuma trafiğini boşaltın
- **Parçalama**: Verileri anahtara/aralığa/karmaya göre sunucular arasında bölme
- **Federasyon**: İşleve/hizmete göre bölme
### Tutarlılık Modelleri
- **Güçlü Tutarlılık**: Tüm düğümler aynı anda aynı verileri görür
- **Nihai Tutarlılık**: Düğümler zamanla birleşir
- **Nedensel Tutarlılık**: Neden-sonuç ilişkileri korunur
- **Yazdıklarınızı Okuyun**: Kullanıcı kendi güncellemelerini anında görür
## Yedekleme ve Kurtarma
### Yedekleme Stratejileri
- **Tam Yedekleme**: Tam veritabanı kopyası
- **Artımlı Yedekleme**: Son yedeklemeden bu yana yapılan değişiklikler
- **Diferansiyel Yedekleme**: Son tam yedeklemeden bu yana yapılan değişiklikler
- **Belirli Bir Noktaya Kurtarma**: Belirli bir ana geri yükleme
- **Sürekli Yedekleme**: Yedeklemeye gerçek zamanlı çoğaltma
### Kurtarma Prosedürleri
- **RTO (Kurtarma Süresi Hedefi)**: Kabul edilebilir maksimum kesinti süresi
- **RPO (Kurtarma Noktası Hedefi)**: Kabul edilebilir maksimum veri kaybı
- **Felaket Kurtarma Planı**: Arızalar için belgelenmiş prosedürler
- **Test**: Düzenli kurtarma tatbikatları
## Güvenlik
### Erişim Kontrolü
- **Kimlik doğrulama**: Kullanıcı kimliğini doğrulayın
- **Yetkilendirme**: İzin verme (HİBE, İPTAL)
- **Roller**: Daha kolay yönetim için grup izinleri
- **En Az Ayrıcalık Prensibi**: Gerekli minimum erişim
### Veri Koruma
- **Kullanılmayan Şifreleme**: Depolanan verileri şifreleyin
- **Transit Halinde Şifreleme**: Bağlantılar için TLS/SSL
- **Maskeleme**: Üretim dışı ortamlardaki hassas verileri gizleyin
- **Belirteçleştirme**: Hassas verileri belirteçlerle değiştirin
### Yaygın Güvenlik Açıkları
- **SQL Enjeksiyonu**: Kullanıcı girişinde kötü amaçlı SQL
- **Ayrıcalık Artışı**: Yetkisiz erişim elde etme
- **Denetim Günlüğü**: Tüm veritabanı etkinliklerini izleyin
- **Uyumluluk**: GDPR, HIPAA, PCI-DSS gereksinimleri
## Modern Veritabanı Teknolojileri
### Bulut Veritabanları
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Veritabanı, Cosmos DB, Synapse
- **Avantajlar**: Yönetilen hizmet, otomatik ölçeklendirme, yedeklemeler dahildir
### YeniSQL Veritabanları
- SQL tutarlılığını NoSQL ölçeklenebilirliğiyle birleştirin
- **Örnekler**: HamamböceğiDB, TiDB, YugabyteDB, Google Spanner
- **Özellikler**: Dağıtılmış, ACID işlemleri, yatay ölçeklendirme
### Zaman Serisi Veritabanları
- Zaman damgalı veriler için optimize edildi
- **Örnekler**: InfluxDB, TimescaleDB, Prometheus
- **Kullanım Örnekleri**: Nesnelerin İnterneti, izleme, finansal veriler
### Vektör Veritabanları
- Gömme vektörlerini saklayın ve sorgulayın
- **Örnekler**: Çam kozalağı, Milvus, Weaviate, Qdrant
- **Kullanım Örnekleri**: Semantik arama, öneri sistemleri, yapay zeka uygulamaları
### Çok Modelli Veritabanları
- Tek sistemde birden fazla veri modelini destekleyin
- **Örnekler**: ArangoDB, OrientDB, Azure Cosmos DB
- **Avantajı**: Birden fazla veritabanı olmadan esneklik
## ORM'ler ve Veri Erişimi
### Nesne-İlişkisel Haritalama
- **Amaç**: Veritabanı tablolarını programlama nesnelerine eşleme
- **Popüler ORM'ler**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hazırda Beklet, JPA
  - Ruby: Aktif Kayıt
  - .NET: Varlık Çerçevesi
### Faydaları
- SQL'den soyutlama
- Tip güvenliği
- Göç yönetimi
- Sorgu oluşturma API'leri
### Dezavantajları
- Performans ek yükü
- Karmaşık sorguların yazılması daha zordur
- N+1 sorgu problemi
- Öğrenme eğrisi
## Veritabanı Yönetimi
### DBA Sorumlulukları
- Kurulum ve konfigürasyon
- Performans ayarı
- Yedekleme ve kurtarma
- Güvenlik yönetimi
- Kapasite planlaması
- İzleme ve uyarı
- Yama yönetimi
### İzleme Metrikleri
- Sorgu yanıt süresi
- Verim (saniye başına işlem sayısı)
- Bağlantı sayısı
- Önbellek isabet oranı
- Disk G/Ç
- Bekleme süresini kilitle
- Çoğaltma gecikmesi
### Bakım Görevleri
- **Vakum/Analiz**: İstatistikleri güncelleyin, alanı geri kazanın
- **Dizin Yeniden Oluşturulması**: Dizinleri birleştirme
- **İstatistik Güncellemeleri**: Sorgu iyileştiriciyi bilgilendirin
- **Günlük Döndürme**: Günlük dosyası boyutlarını yönetin
- **Kapasite Planlama**: Büyümeyi tahmin edin, yükseltmeleri planlayın