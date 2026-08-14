---
# Metadata
title: "SQL — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the SQL ecosystem including databases, tools, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [sql, ecosystem, tooling, databases, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# SQL — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz, SQL ekosistemindeki temel veritabanlarını, araçları ve altyapıyı kapsar.
---

## Veritabanı Sistemleri
### İlişkisel (OLTP)
| Veritabanı | Tür | En İyisi |
|----------|----------|----------|
| **PostgreSQL** | Açık kaynak | En zengin özelliklere sahip, genişletilebilir |
| **MySQL / MariaDB** | Açık kaynak | Web uygulamaları |
| **SQLite** | Gömülü | Mobil, masaüstü, küçük uygulamalar |
| **SQL Sunucusu** | Ticari | Kurumsal (Microsoft) |
| **Oracle** | Ticari | Büyük işletme |
| **DB2** | Ticari | IBM kuruluşu |
| **HamamböceğiDB** | Dağıtıldı | Bulutta yerel, PostgreSQL uyumlu |
| **TiDB** | Dağıtıldı | MySQL uyumlu, HTAP |
| **YugabyteDB** | Dağıtıldı | PostgreSQL uyumlu |
### Analitik (OLAP)
| Veritabanı | Tür | En İyisi |
|----------|----------|----------|
| **ClickHouse** | Sütunlu | Gerçek zamanlı analiz |
| **ÖrdekDB** | Gömülü | Süreç içi analitik |
| **Kar tanesi** | Bulut | Veri ambarı |
| **BigQuery** | Bulut | Google analitiği |
| **Kırmızıya kayma** | Bulut | AWS analitiği |
| **Apache Druid** | Sütunlu | Zaman serisi analitiği |
```sql
-- PostgreSQL example
CREATE TABLE users (
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    age         INTEGER CHECK (age > 0),
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created ON users(created_at);
```

---

## Taşıma Araçları
| Araç | Tür | Notlar |
|------|------|----------|
| **Geçiş yolu** | Java tabanlı | Basit, SQL geçişleri |
| **Sıvıbaz** | XML/SQL/YAML | Kurumsal düzeyde |
| **Alembik** | Python | SQLAlchemy geçişleri |
| **Prizma Geçişi** | TypeScript | Tür uyumlu geçişler |
| **golang-göç** | Git | Veritabanı geçişleri |
| **Atlas** | Modern | Kod olarak şema |
| **dbmate** | Çoklu Veritabanı | Basit CLI |
```sql
-- Flyway migration: V1__create_users.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- V2__add_age_column.sql
ALTER TABLE users ADD COLUMN age INTEGER CHECK (age > 0);
CREATE INDEX idx_users_age ON users(age);
```

```bash
flyway migrate -url=jdbc:postgresql://localhost/mydb -user=postgres
```

---

## Sorgu Oluşturucular ve ORM'ler
| Araç | Dil | Tür |
|------|----------|------|
| **Prizma** | TypeScript | Tür açısından güvenli ORM |
| **Çiseleyen yağmur** | TypeScript | Tür açısından güvenli SQL |
| **Sekelleştir** | JavaScript | Tam ORM |
| **Knex.js** | JavaScript | Sorgu oluşturucu |
| **SQLAlchemy** | Python | Tam ORM + Çekirdek |
| **Django ORM** | Python | Tam ORM |
| **peeee** | Python | Hafif ORM |
| **Belagatli** | PHP (Laravel) | Aktif Kayıt ORM |
| **Doktrin** | PHP (Symfony) | Veri Eşleyici ORM |
| **Varlık Çerçevesi** | C# | Tam ORM |
| **Şık** | C# | Mikro-ORM |
| **Hazırda Bekletme** | Java | Tam ORM |
| **jOOQ** | Java | Tür açısından güvenli SQL |
| **GORM** | Git | Tam ORM |
| **sqlc** | Git | SQL'den Go Oluştur |
| **Dizel** | Pas | Tür açısından güvenli ORM |
| **SQLx** | Pas | Zaman uyumsuz SQL |
| **DenizORM** | Pas | Zaman uyumsuz ORM |
---

## GUI ve IDE Araçları
| Araç | Tür | Notlar |
|------|------|----------|
| **DBeaver** | Evrensel | Ücretsiz, çoklu veritabanı |
| **DataGrip** | JetBrains | En İyi SQL IDE'si |
| **pgAdmin** | PostgreSQL | Web tabanlı yönetici |
| **MySQL Çalışma Tezgahı** | MySQL | Resmi araç |
| **HeidiSQL** | Windows | Hafif |
| **TablePlus** | Modern | Güzel kullanıcı arayüzü |
| **Arıcı Stüdyosu** | Açık kaynak | Elektron bazlı |
| **psql** | CLI | PostgreSQL terminali |
| **mysql** | CLI | MySQL terminali |
| **sqlite3** | CLI | SQLite terminali |
---

## Performans ve Analiz
| Araç | Amaç |
|------|------------|
| **ANALİZİ AÇIKLAYIN** | Sorgu yürütme planı |
| **pg_stat_statements** | PostgreSQL sorgu istatistikleri |
| **AÇIKLAYIN** | Yürütme planı (MySQL) |
| **PROFİLİ GÖSTER** | MySQL profili oluşturma |
| **SQL Server Profil Oluşturucu** | SQL Server profil oluşturma |
| **pgBadger** | PostgreSQL günlük analizörü |
| **pt-query-digest** | MySQL sorgu analizi |
| **sistem görünümleri** | MySQL sistem görünümleri |
```sql
-- Analyze query performance
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.created_at > '2024-01-01'
GROUP BY u.name
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC;

-- PostgreSQL: check indexes
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'users';
```

---

## Test etme
| Araç | Amaç |
|------|------------|
| **tSQLt** | SQL Server birim testi |
| **pgTAP** | PostgreSQL testi |
| **utPLSQL** | Oracle testi |
| **dbtest** | Veritabanı testi |
| **test kapsayıcıları** | Docker tabanlı veritabanı testleri |
| **sqlfluff** | SQL astarlama |
| **şemalin** | Şema astarlama |
```sql
-- pgTAP example
BEGIN;
SELECT plan(3);

SELECT has_table('public', 'users', 'users table exists');
SELECT has_column('users', 'email', 'email column exists');
SELECT col_is_unique('users', 'email', 'email is unique');

SELECT * FROM finish();
ROLLBACK;
```

---

## SQL Linting ve Formatlama
| Araç | Amaç |
|------|------------|
| **SQLFluff** | Linter ve biçimlendirici |
| **sql-biçimlendirici** | SQL biçimlendirme |
| **ciyaklama** | PostgreSQL geçiş linter'ı |
| **psql2go** | SQL'den Go'ya dönüştürücü |
```ini
# .sqlfluff
[sqlfluff]
dialect = postgres
max_line_length = 120

[sqlfluff:rules]
capitalisation_policy = upper
```

```bash
sqlfluff lint migrations/
sqlfluff fix migrations/
```

---

## Temel SQL Kavramları
| Konsept | Açıklama |
|-----------|------------|
| **ASİT** | Atomiklik, Tutarlılık, Yalıtım, Dayanıklılık |
| **Normalleşme** | 1NF, 2NF, 3NF, BCNF |
| **Dizinler** | B-ağacı, Hash, GIN, GiST, BRIN |
| **İşlemler** | BAŞLA, KABUL ET, GERİ DÖN |
| **Katılıyor** | İÇ, SOL, SAĞ, TAM, ÇAPRAZ |
| **Pencere işlevleri** | ROW_NUMBER, RANK, LAG, LEAD |
| **CTE'ler** | İLE, özyinelemeli sorgular |
| **Görüntülemeler** | Sanal tablolar |
| **Tetikleyiciler** | Otomatik eylemler |
| **Saklı prosedürler** | Yeniden kullanılabilir SQL kodu |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Docker** | Resmi görseller (postgres, mysql) |
| **Yönetilen hizmetler** | RDS, Bulut SQL, Azure SQL |
| **Geçiş Yolu / Liquibase** | Şema geçişleri |
| **pg_dump / mysqldump** | Yedeklemeler |
| **WAL-E / pgBackRest** | PostgreSQL yedeklemeleri |
| **Kubernetes operatörleri** | CloudNativePG, Vitess |
---

## Özet
SQL'in ekosistemi düzinelerce veritabanı motorunu ve yüzlerce aracı kapsar. Standart yığın şudur: Varsayılan veritabanı olarak **PostgreSQL** (en zengin özelliklere sahip açık kaynak), web uygulamaları için **MySQL**, gömülü kullanım için **SQLite**, geçişler için **Flyway** veya **Liquibase**, GUI olarak **DBeaver** veya **DataGrip**, linting için **SQLFluff** ve performans ayarlaması için **EXPLAIN ANALYZE**. Modern SQL geliştirme, SQL'den kod oluşturmak için **Prisma** (TypeScript), **SQLAlchemy** (Python) veya **sqlc** (Go) gibi tür uyumlu ORM'leri kullanır. SQL, her teknoloji yığınında gerekli olan veriler için evrensel dil olmaya devam ediyor.