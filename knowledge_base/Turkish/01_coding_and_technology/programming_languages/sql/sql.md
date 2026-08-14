---
# Metadata
title: "SQL"
description: "Comprehensive reference for the SQL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [sql, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "26 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#SQL
SQL (Yapısal Sorgulama Dili), ilişkisel veritabanlarındaki verileri yönetmek ve sorgulamak için tasarlanmış, alana özgü bir dildir. İlk olarak 1970'lerde IBM'de geliştirilen ve 1987'de standartlaştırılan SQL, uygulamalar ve veriler arasındaki birincil arayüz olmaya devam ediyor. Her büyük İlişkisel Veritabanı Yönetim Sistemi (RDBMS) (PostgreSQL, MySQL, SQL Server, Oracle, SQLite) sorgulama dili olarak SQL'i kullanır.
SQL genel amaçlı bir programlama dili değildir. SQL'de bir web uygulaması yazmazsınız. Ancak uygulamanız verileri depoluyorsa (ve neredeyse tüm uygulamalarda depolanır), o zaman SQL, bu verileri almak, dönüştürmek ve yönetmek için kullandığınız dildir. Genel programlamadan sonra tartışmasız evrensel olarak en yararlı teknik beceridir.
---

## SQL Neden Önemlidir
- **Evrensel**: Her ilişkisel veritabanı SQL konuşur. Bir kez öğrenin, her yerde kullanın.
- **Bildirimsel**: *Nasıl* elde edeceğinizi değil, *ne* veriyi istediğinizi açıklarsınız. Veritabanı motoru yürütmeyi optimize eder.
- **Her geliştirici için gereklidir**: Arka uç, veri bilimi, DevOps, analitik — hepsi SQL gerektirir.
- **Güçlü**: Pencere işlevleri, CTE'ler, alt sorgular ve toplamalar, karmaşık mantığı birkaç satırda ifade etmenize olanak tanır.
- **Performans**: Düzgün şekilde indekslenmiş bir veritabanında iyi yazılmış bir SQL sorgusu, milisaniyeler içinde milyonlarca satırı işleyebilir.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Genel amaçlı bir dil değildir** | SQL'de uygulamalar, API'ler veya algoritmalar oluşturulamıyor | Python, Java, JavaScript vb. ile birleştirin. |
| **Lehçe farklılıkları** | Her RDBMS'nin uyumsuz uzantılara sahip kendi SQL tadı vardır | Mümkün olduğunda ANSI SQL'e sadık kalın; uygulamanızdaki soyut lehçe farklılıkları |
| **Şema katılığı** | Büyük masalarda masa yapılarını değiştirmek yavaş ve işleri aksatabilir | Geçiş araçlarını kullanın; şemaları dikkatlice önceden tasarlayın |
| **N+1 sorgu sorunu** | ORM tarafından oluşturulan sorgular son derece verimsiz olabilir | Karmaşık sorgular için özel SQL yazın; AÇIKLAMA ANALİZİ içeren profil |
| **Ölçeklendirme karmaşıklığı** | SQL veritabanlarının yatay olarak ölçeklendirilmesi NoSQL'e göre daha zordur | Okuma replikalarını, parçalamayı kullanın veya belirli kullanım durumları için NoSQL'i düşünün |
---

## Temel Kavramlar
### İlişkisel Model
Veriler, **satırlar** (kayıtlar/demetler) ve **sütunlardan** (öznitelikler/alanlar) oluşan **tablolarda** (ilişkiler) depolanır. Tablolar **tuşlar** aracılığıyla birbirleriyle ilişkilendirilebilir.
```
+---------------------------------+     +----------------------------------+
|            users                |     |            orders                |
+------+----------+---------------+     +------+----------+----------------+
|  id  |   name   |    email      |     |  id  | user_id  |   total        |
+------+----------+---------------+     +------+----------+----------------+
|  1   | Alice    | alice@mail.com|<----|  1   |    1     |   99.99        |
|  2   | Bob      | bob@mail.com  |<----|  2   |    1     |   49.50        |
|  3   | Charlie  | charlie@mail  |     |  3   |    2     |  150.00        |
+------+----------+---------------+     |  4   |    3     |   75.25        |
  PRIMARY KEY                           |  5   |    3     |   30.00        |
                                        +------+----------+----------------+
                                                  FOREIGN KEY -> users.id
```

---

## Söz Diziminin Temelleri
### Veri Alma (SEÇ)
```sql
-- Basic query
SELECT name, email FROM users;

-- With filtering (WHERE)
SELECT name, email FROM users WHERE id = 1;

-- Multiple conditions
SELECT name, email FROM users WHERE id > 1 AND email LIKE '%@mail.com';

-- Sorting (ORDER BY)
SELECT name, email FROM users ORDER BY name ASC, id DESC;

-- Limiting results
SELECT name FROM users ORDER BY id LIMIT 10;
```

### Toplama
```sql
-- Count, sum, average, min, max
SELECT 
    COUNT(*) AS total_users,
    AVG(age) AS average_age,
    MIN(created_at) AS earliest_user,
    MAX(created_at) AS latest_user
FROM users;

-- Group by (aggregate per group)
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS average_salary
FROM employees GROUP BY department;

-- Filter groups (HAVING)
SELECT department, COUNT(*) AS employee_count
FROM employees GROUP BY department HAVING COUNT(*) > 5;
```

### Tabloları Birleştirme
```sql
-- INNER JOIN — only matching rows from both tables
SELECT u.name, o.total FROM users u INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN — all rows from left table, matching rows from right
SELECT u.name, o.total FROM users u LEFT JOIN orders o ON u.id = o.user_id;

-- Multiple joins
SELECT u.name, o.id AS order_id, p.name AS product_name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;

-- Self join (employees and their managers)
SELECT e.name AS employee, m.name AS manager
FROM employees e LEFT JOIN employees m ON e.manager_id = m.id;
```

### Verileri Değiştirme
```sql
-- Insert
INSERT INTO users (name, email, age) VALUES ('Diana', 'diana@mail.com', 28);

-- Insert multiple rows
INSERT INTO users (name, email, age) VALUES
    ('Eve', 'eve@mail.com', 32),
    ('Frank', 'frank@mail.com', 45);

-- Update
UPDATE users SET age = 31, email = 'alice.new@mail.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 3;

-- Upsert (PostgreSQL)
INSERT INTO users (id, name, email) VALUES (1, 'Alice Updated', 'alice@mail.com')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;
```
---

## Gelişmiş Sözdizimi ve Desenler
### Pencere İşlevleri — Ayrıntılı İnceleme
Pencere işlevleri, GROUP BY'nin yaptığı gibi bunları tek bir çıktı satırına daraltmadan, geçerli satırla ilgili bir dizi satır boyunca hesaplamalar gerçekleştirir.
```sql
-- ROW_NUMBER: unique sequential number within a partition
SELECT name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

-- RANK vs DENSE_RANK: handling ties differently
SELECT name, score,
    RANK()       OVER (ORDER BY score DESC) AS rank,        -- 1, 2, 2, 4
    DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank,  -- 1, 2, 2, 3
    ROW_NUMBER() OVER (ORDER BY score DESC) AS row_num      -- 1, 2, 3, 4
FROM students;

-- LAG and LEAD: access previous and next rows
SELECT month, revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month,
    LEAD(revenue, 1) OVER (ORDER BY month) AS next_month,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS month_change
FROM monthly_revenue;

-- Running total with frame specification
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) AS running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7day
FROM daily_sales;

-- NTILE: divide rows into N roughly equal buckets
SELECT name, salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile,
    NTILE(10) OVER (ORDER BY salary DESC) AS decile
FROM employees;

-- Percentage of total using window functions
SELECT department, salary,
    ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY department), 2) AS pct_of_dept,
    ROUND(salary * 100.0 / SUM(salary) OVER (), 2) AS pct_of_company
FROM employees;
```

### Ortak Tablo İfadeleri (CTE'ler) — Gelişmiş Kullanım
```sql
-- Multiple CTEs in a single query
WITH department_stats AS (
    SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
    FROM employees GROUP BY department
),
high_earners AS (
    SELECT e.name, e.department, e.salary
    FROM employees e
    JOIN department_stats ds ON e.department = ds.department
    WHERE e.salary > ds.avg_salary * 1.5
)
SELECT * FROM high_earners ORDER BY department, salary DESC;

-- Recursive CTE: traverse a hierarchy (org chart)
WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 1 AS level, name AS path
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, oc.level + 1, oc.path || ' > ' || e.name
    FROM employees e JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT level, path FROM org_chart ORDER BY path;

-- Recursive CTE: generate a date series
WITH RECURSIVE date_series AS (
    SELECT DATE '2024-01-01' AS dt
    UNION ALL
    SELECT dt + INTERVAL '1 day' FROM date_series WHERE dt < DATE '2024-12-31'
)
SELECT dt FROM date_series WHERE EXTRACT(DOW FROM dt) BETWEEN 1 AND 5;
```

### JSON İşlemleri
```sql
-- PostgreSQL: JSONB operations
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    attributes JSONB NOT NULL DEFAULT '{}'
);

INSERT INTO products (name, attributes) VALUES
('Laptop', '{"brand": "Dell", "ram_gb": 16, "storage": {"type": "SSD", "size_gb": 512}}'),
('Phone',  '{"brand": "Apple", "ram_gb": 6, "storage": {"type": "NVMe", "size_gb": 128}}');

-- Query JSON fields
SELECT name, attributes->>'brand' AS brand FROM products WHERE attributes->>'brand' = 'Dell';

-- Nested JSON access
SELECT name, attributes->'storage'->>'type' AS storage_type FROM products;

-- Check if JSON contains a key/value
SELECT name FROM products WHERE attributes @> '{"brand": "Apple"}';

-- Update a JSON field
UPDATE products SET attributes = jsonb_set(attributes, '{ram_gb}', '32') WHERE name = 'Laptop';
```

### Saklı Prosedürler ve Tetikleyiciler
```sql
-- PostgreSQL: function that returns a table
CREATE OR REPLACE FUNCTION get_top_customers(min_orders INTEGER DEFAULT 5)
RETURNS TABLE(customer_name TEXT, order_count BIGINT, total_spent NUMERIC)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT u.name, COUNT(o.id), SUM(o.total)
    FROM users u JOIN orders o ON u.id = o.user_id
    GROUP BY u.name HAVING COUNT(o.id) >= min_orders
    ORDER BY SUM(o.total) DESC;
END; $$;

-- Trigger: automatically audit changes
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY, table_name TEXT, operation TEXT,
    old_data JSONB, new_data JSONB, changed_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION audit_trigger_func() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (table_name, operation, old_data, new_data)
    VALUES (TG_TABLE_NAME, TG_OP, to_jsonb(OLD), to_jsonb(NEW));
    RETURN COALESCE(NEW, OLD);
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER users_audit
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();
```
---

## Temel Özelliklere Derinlemesine Bakış
### Sorgu Optimizasyonu
```sql
-- EXPLAIN ANALYSE: see the actual execution plan with real timings
EXPLAIN ANALYSE
SELECT u.name, COUNT(o.id) AS order_count
FROM users u LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.name HAVING COUNT(o.id) > 3
ORDER BY order_count DESC;

-- Typical output interpretation:
-- "Seq Scan" = scanning every row (slow for large tables)
-- "Index Scan" = using an index (fast)
-- "Hash Join" = joining with a hash table (usually fast)
-- "Nested Loop" = joining with a loop (can be slow)
```

**Optimizasyon kontrol listesi:**
| Sayı | Belirti | Düzelt |
|----------|------------|-----|
| Büyük tabloda sıralı tarama |  AÇIKLAMA'da`Seq Scan`| Uygun dizini ekle |
| WHERE sütununda dizin eksik | Tam tablo taraması | Filtrelenen sütunlarda dizin oluşturun |
| SEÇİN * atık | Gereksiz sütunlar getiriliyor | Yalnızca gerekli sütunları seçin |
| Örtülü tür dönüştürme | Dizin kullanılmıyor | Karşılaştırmalarda eşleme türleri |
| İndekslenmiş sütunlardaki işlevler | Dizin kullanılamaz (sarglanamaz) | Yeniden yazın: `WHERE date >= '2024-01-01'`,`WHERE YEAR(date) = 2024`değil |
### Dizin Oluşturma Stratejileri
```sql
-- Composite index: order matters (leftmost prefix rule)
CREATE INDEX idx_orders_status_date ON orders(status, created_at);
-- Useful for: WHERE status = 'active' AND created_at > '2024-01-01'
-- Useful for: WHERE status = 'active' (leftmost prefix)
-- NOT useful for: WHERE created_at > '2024-01-01' (skips first column)

-- Covering index: includes all columns needed by the query
CREATE INDEX idx_orders_covering ON orders(user_id) INCLUDE (total, status);

-- Partial index: only index rows meeting a condition
CREATE INDEX idx_orders_pending ON orders(created_at) WHERE status = 'pending';

-- Expression index: index on a computed value
CREATE INDEX idx_users_lower_email ON users(LOWER(email));

-- GIN index for full-text search (PostgreSQL)
CREATE INDEX idx_products_search ON products USING GIN(to_tsvector('english', name));
SELECT * FROM products WHERE to_tsvector('english', name) @@ plainto_tsquery('laptop');
```

### İşlem Yalıtım Düzeyleri
| İzolasyon Seviyesi | Kirli Okuma | Tekrarlanamaz Okuma | Hayalet Okuma |
|----------------|:----------:|:----------------------:|:------------:|
| TAAHHÜTSİZ OKUYUN | Evet | Evet | Evet |
| TAAHHÜT OKUYUN | Hayır | Evet | Evet |
| TEKRARLANABİLİR OKUMA | Hayır | Hayır | Evet* |
| SERİ OLABİLİR | Hayır | Hayır | Hayır |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalleştirme
| Normal Form | Kural | Örnek İhlal |
|------------|----------|-------|
| **1NF** | Atomik değerler, yinelenen grup yok | Birden fazla telefonun tek sütunda "123,456" olarak saklanması |
| **2NF** | 1NF + kısmi bağımlılık yok | Sipariş ayrıntıları order_id'ye bağlıdır ancak ürün_id'sine bağlı değildir |
| **3NF** | 2NF + geçişli bağımlılık yok | Çalışan departmanı adı, çalışana değil departman_id'sine bağlıdır |
---

## Veritabanı Yapısını Tanımlama
### Tablo Oluşturma
```sql
CREATE TABLE users (
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    age         INTEGER CHECK (age >= 0 AND age <= 150),
    role        VARCHAR(20) DEFAULT 'viewer' CHECK (role IN ('admin', 'editor', 'viewer')),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP
);

CREATE TABLE orders (
    id          BIGSERIAL PRIMARY KEY,
    user_id     BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    total       DECIMAL(10, 2) NOT NULL CHECK (total >= 0),
    status      VARCHAR(20) DEFAULT 'pending',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
```

### Tabloları Değiştirmek
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Proje Yapılandırması ve Oluşturma Sistemi
### Taşıma Araçları
| Araç | Dil/Yığın | Yaklaşım |
|------|---------------|----------|
| **Geçiş yolu** | Java / genel | SQL tabanlı geçişler, basit adlandırma kuralı |
| **Sıvıbaz** | Java / genel | XML, YAML, JSON veya SQL değişiklik günlükleri |
| **Alembik** | Python (SQLAlchemy) | Model değişikliklerinden geçişleri otomatik olarak oluşturur |
| **Prizma Geçişi** | Node.js / TypeScript | Şema önceliklidir, SQL'i otomatik olarak oluşturur |
| **golang-göç** | Git | SQL tabanlı, yukarı/aşağı geçişleri destekler |
```sql
-- Migration file naming convention (Flyway):
-- V001__create_users_table.sql
-- V002__add_email_index.sql
-- V003__create_orders_table.sql

-- V001__create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Always use idempotent migrations where possible
DROP TABLE IF EXISTS legacy_data;
CREATE TABLE IF NOT EXISTS audit_log (id SERIAL PRIMARY KEY);
```

---

## Test etme
### Test Verisi Oluşturma
```sql
-- Generate test data with generate_series (PostgreSQL)
INSERT INTO users (name, email, age)
SELECT 'User_' || i, 'user' || i || '@test.com', 18 + (random() * 60)::INTEGER
FROM generate_series(1, 10000) AS i;

-- Assertion patterns for testing queries (PostgreSQL)
DO $$
DECLARE total_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO total_count FROM users;
    ASSERT total_count = 10000, 'Expected 10000 users, got ' || total_count;
    RAISE NOTICE 'All tests passed!';
END $$;
```

| Çerçeve | Veritabanı | Açıklama |
|-----------|----------|------------|
| **pgTAP** | PostgreSQL | Birim test çerçevesi |
| **tSQLt** | SQL Sunucusu | SQL Server için birim testi |
| **utPLSQL** | Kahin | Oracle PL/SQL için çerçeveyi test etme |
---

## Birlikte Çalışabilirlik
### Dil Bağları
| Arayüz | Dil | Açıklama |
|-----------|----------|------------|
| **JDBC** | Java | Standart veritabanı API'si |
| **ODBC** | Çoklu | Evrensel veritabanı API'si |
| **psycopg2/3** | Python | PostgreSQL bağdaştırıcısı |
| **veritabanı/sql** | Git | Sürücü arayüzlü standart kütüphane |
| **sqlite3** | Python | Yerleşik SQLite desteği |
| **sayfa** | Node.js | PostgreSQL istemcisi |
```python
# Python: connecting to PostgreSQL
import psycopg2
conn = psycopg2.connect(host="localhost", database="myapp", user="app_user", password="secret")
cur = conn.cursor()
# Parameterized query (NEVER use string concatenation — SQL injection risk!)
cur.execute("SELECT name, email FROM users WHERE id = %s", (user_id,))
rows = cur.fetchall()
```

---

## Tasarım Desenleri
### Desen 1: Pivot / Çapraz Tablo
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Desen 2: Grup Başına En İyi N
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Desen 3: Boşluklar ve Adalar
```sql
WITH numbered AS (
    SELECT login_date,
           login_date - ROW_NUMBER() OVER (ORDER BY login_date) AS grp
    FROM (SELECT DISTINCT login_date FROM user_logins WHERE user_id = 1) t
)
SELECT MIN(login_date) AS start_date, MAX(login_date) AS end_date,
       COUNT(*) AS consecutive_days
FROM numbered GROUP BY grp;
```

### Desen 4: Yavaşça Değişen Boyutlar (SCD Tip 2)
```sql
CREATE TABLE dim_customer (
    id SERIAL PRIMARY KEY, customer_key INTEGER NOT NULL,
    name TEXT, address TEXT,
    valid_from DATE NOT NULL DEFAULT CURRENT_DATE,
    valid_to DATE, is_current BOOLEAN NOT NULL DEFAULT TRUE
);

-- Query current state:
SELECT * FROM dim_customer WHERE is_current = TRUE;

-- Query historical state:
SELECT * FROM dim_customer
WHERE '2024-06-15' BETWEEN valid_from AND COALESCE(valid_to, '9999-12-31');
```
---

## Performans: Dizinler ve Sorgu Planlama
### Dizinler Nasıl Çalışır?
Dizin, veritabanının tüm tabloyu taramadan satırları bulmasını sağlayan bir veri yapısıdır (genellikle bir B ağacı).
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Dizin Türü | En İyisi | Örnek |
|-----------|----------|-----------|
| **B-ağacı** (varsayılan) | Eşitlik ve aralık sorguları | `WHERE age > 25 AND age < 35`|
| **Hash** | Yalnızca tam eşitlik | `WHERE email = 'x@y.com'`|
| **CİN** | Tam metin araması, diziler, JSON | `WHERE description @@ 'search term'`|
| **GiST** | Geometrik/uzaysal veriler | `WHERE location <-> point(x,y) < 1000`|
### Sorgu Planlarını Okumak
```sql
-- PostgreSQL: see how the database plans to execute your query
EXPLAIN ANALYSE SELECT * FROM users WHERE email = 'alice@mail.com';

-- Look for:
-- "Seq Scan" = scanning every row (slow for large tables)
-- "Index Scan" = using an index (fast)
-- "Nested Loop" = joining with a loop (can be slow)
-- "Hash Join" = joining with a hash table (usually fast)
```

---

## SQL Lehçeleri
| Özellik | PostgreSQL | MySQL | SQL Sunucusu | SQLite |
|-----------|-----------|----------|------------|--------|
| Otomatik artış | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Dize birleşimi | `\|\|`| `CONCAT()`| `+`veya`CONCAT()`| `\|\|`|
| Tarih işlevleri | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| JSON desteği | Mükemmel (`jsonb`) | İyi (`JSON`) | İyi (`JSON`) | Temel (`JSON1`) |
| Tam metin araması | Dahili (`tsvector`) | Dahili | Dahili | Sınırlı |
| Pencere işlevleri | Evet | Evet (8.0+) | Evet | Evet |
---

## Dağıtım
### Veritabanı Dağıtım Stratejileri
| Strateji | Açıklama | Risk Düzeyi |
|----------|----------------|------------|
| **Taşıma dosyaları** | Sürümlendirilmiş SQL komut dosyaları sırayla uygulandı | Düşük |
| **Mavi-yeşil dağıtım** | İki özdeş veritabanı; trafiği değiştir | Düşük |
| **Sözleşmeyi genişlet** | Yeni sütun ekleyin, çift yazın, taşıyın, eskisini bırakın | Düşük |
| **Doğrudan DDL** | ALTER TABLE'ı doğrudan üretimde çalıştırmak | Yüksek |
```sql
-- Expand-contract pattern: renaming a column safely
-- Phase 1: EXPAND - add new column alongside old
ALTER TABLE users ADD COLUMN full_name TEXT;

-- Phase 2: MIGRATE - backfill existing data
UPDATE users SET full_name = name WHERE full_name IS NULL;

-- Phase 3: CONTRACT - remove old column after verification
ALTER TABLE users DROP COLUMN name;
ALTER TABLE users RENAME COLUMN full_name TO name;
```

---

## SQL Ne Zaman Kullanılmalı
| Senaryo | Neden SQL | Alternatif |
|----------|------------|------------|
| Karmaşık sorgulara sahip ilişkisel veriler | SQL bunun için tasarlandı | --- |
| İşlem bütünlüğü (ACID) | SQL veritabanları tutarlılığı garanti eder | --- |
| Raporlama ve analiz | Toplamalar, pencere işlevleri, CTE'ler | Çok karmaşık analizler için Python (Pandalar) |
| Veri bütünlüğü kısıtlamaları | Yabancı anahtarlar, KONTROL, BENZERSİZ, BOŞ DEĞİL | Uygulama düzeyinde doğrulama (zayıf) |
| Basit anahtar/değer depolama | Bu kullanım durumu için aşırıya kaçma | Redis, DynamoDB |
| Son derece yapılandırılmamış veriler | Şema katılığı bir sorundur | MongoDB, belge veritabanları |
| Büyük yatay ölçeklendirme | SQL veritabanlarını parçalamak zor | Cassandra, DynamoDB, HamamböceğiDB |
---

## Sentetik Soru-Cevap
### S1:`WHERE`ile`HAVING`arasındaki fark nedir?
**A:** `WHERE`, gruplandırmadan önce satırları filtreler; `HAVING`toplama sonrasında grupları filtreler:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### S2: Pencere işlevlerinin GROUP BY'den farkı nedir?
**C:** Pencere işlevleri, satırları daraltmadan satırlar arasında işlem yapar:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### S3: Yavaş sorguları nasıl optimize edebilirim?
**C:** Temel stratejiler:
- `WHERE`,`JOIN`ve `ORDER BY`'de kullanılan sütunlara dizinler ekleyin 
- `SELECT *`'den kaçının — yalnızca gerekli sütunları seçin
- Sorgu planlarını okumak için`EXPLAIN`/`EXPLAIN ANALYZE`kullanın
- Mümkün olduğunda alt sorguları JOIN'lerle değiştirin
- Okunabilirlik için CTE'leri kullanın (genellikle performans cezası yoktur)
- WHERE içindeki indekslenmiş sütunlardaki işlevlerden kaçının:`WHERE YEAR(date) = 2024`değil`WHERE date >= '2024-01-01'`kullanın
### S4: CTE'ler nedir ve bunları ne zaman kullanmalıyım?
**C:** Ortak Tablo İfadeleri adlandırılmış geçici sonuç kümeleri oluşturur:
```sql
-- CTE for readability
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS total
    FROM orders
    GROUP BY 1
),
running_total AS (
    SELECT month, total,
           SUM(total) OVER (ORDER BY month) AS cumulative
    FROM monthly_sales
)
SELECT * FROM running_total;
```

### S5: NULL değerlerini doğru şekilde nasıl işleyebilirim?
**A:** NULL bilinmeyeni temsil eder — kendisi dahil hiçbir şeye eşit değildir:
```sql
-- NULL comparisons
NULL = NULL    -- NULL (not TRUE!)
NULL IS NULL   -- TRUE

-- COALESCE — first non-NULL
SELECT COALESCE(nickname, first_name, 'Anonymous') AS display_name
FROM users;

-- NULLIF — return NULL if equal
SELECT NULLIF(status, '') AS status;  -- '' becomes NULL

-- COUNT ignores NULLs
SELECT COUNT(completed_at) FROM tasks;  -- counts non-NULL only
```

---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Grup Başına En İyi N'yi Bulma
**1. Adım: Sorunu Anlayın**
Her departmandaki en yüksek maaşlı 3 çalışanı bulun.
**2. Adım: Yaklaşımı Belirleyin**
Departmana göre bölümlenmiş`ROW_NUMBER()`ile bir pencere işlevi kullanın.
**3. Adım: Uygulama**```sql
WITH ranked AS (
    SELECT name, department, salary,
           ROW_NUMBER() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rn
    FROM employees
)
SELECT name, department, salary
FROM ranked
WHERE rn <= 3
ORDER BY department, salary DESC;
```

**4. Adım: Doğrulayın**
Her departmanın en fazla 3 satırı olduğundan emin olun. Gerekirse`DENSE_RANK()`ile bağları kullanın.
### Sorun 2: Yıllık Büyüme Raporu Oluşturmak
**1. Adım: Sorunu Anlayın**
Aylık geliri ve yıldan yıla büyüme yüzdesini hesaplayın.
**2. Adım: Yaklaşımı Belirleyin**
Gruplama için `DATE_TRUNC`'yi ve önceki yıl karşılaştırması için`LAG()`pencere işlevini kullanın.
**3. Adım: Uygulama**```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS revenue
    FROM orders
    GROUP BY 1
)
SELECT month,
       revenue,
       LAG(revenue, 12) OVER (ORDER BY month) AS revenue_prev_year,
       ROUND(
           (revenue - LAG(revenue, 12) OVER (ORDER BY month))
           / NULLIF(LAG(revenue, 12) OVER (ORDER BY month), 0) * 100,
           2
       ) AS yoy_growth_pct
FROM monthly
ORDER BY month;
```

**4. Adım: Doğrulayın**
İlk 12 ayın önceki yıla ait NULL olup olmadığını kontrol edin. Büyüme yüzdelerini bilinen rakamlara göre doğrulayın.
### Sorun 3: Satırları Sütunlara Döndürme
**1. Adım: Sorunu Anlayın**
Durum sayılarını satırlardan sütunlara dönüştürün.
**2. Adım: Yaklaşımı Belirleyin**
Koşullu toplamayı kullanın (`SUM`içinde`CASE`).
**3. Adım: Uygulama**```sql
-- Input: orders table with status column
-- Output: one row per month with status counts as columns
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(CASE WHEN status = 'pending'   THEN 1 ELSE 0 END) AS pending,
       SUM(CASE WHEN status = 'shipped'   THEN 1 ELSE 0 END) AS shipped,
       SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS delivered,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
       COUNT(*) AS total
FROM orders
GROUP BY 1
ORDER BY 1;
```

**4. Adım: Genişletin**
Yüzde sütunlarını ve değişen toplamları ekleyin.
---

## Özet
SQL, hala önemini koruyan 50 yıllık bir dildir. Her geliştiricinin, veri bilimcinin ve analistin bunu bilmesi gerekir. Çekirdek dil standartlaştırılmış ve taşınabilirdir; lehçe farklılıkları yönetilebilir. Modern SQL (pencere işlevleri, CTE'ler ve JSON desteğiyle) çoğu veri görevi için yeterince anlamlıdır. Temel beceriler şunlardır: etkili sorgular yazmak, dizinleri anlamak, sorgu planlarını okumak ve iyi şemalar tasarlamak. Verilerle çalışıyorsanız SQL tartışılamaz.