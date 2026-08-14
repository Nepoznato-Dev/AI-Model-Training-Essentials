<!--
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

-->
#SQL
SQL (Bahasa Kueri Terstruktur) adalah bahasa khusus domain yang dirancang untuk mengelola dan menanyakan data dalam database relasional. Pertama kali dikembangkan di IBM pada tahun 1970an dan distandarisasi pada tahun 1987, SQL tetap menjadi antarmuka utama antara aplikasi dan datanya. Setiap Sistem Manajemen Basis Data Relasional (RDBMS) utama — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — menggunakan SQL sebagai bahasa kuerinya.
SQL bukanlah bahasa pemrograman tujuan umum. Anda tidak akan menulis aplikasi web dalam SQL. Namun jika aplikasi Anda menyimpan data — dan hampir semua aplikasi menyimpan data — maka SQL adalah bahasa yang Anda gunakan untuk mengambil, mengubah, dan mengelola data tersebut. Ini bisa dibilang merupakan keterampilan teknis yang paling berguna secara universal setelah pemrograman umum.
---

## Mengapa SQL Penting
- **Universal**: Setiap database relasional menggunakan SQL. Pelajari sekali, gunakan di mana saja.
- **Deklaratif**: Anda menjelaskan *data apa* yang Anda inginkan, bukan *bagaimana* mendapatkannya. Mesin database mengoptimalkan eksekusi.
- **Penting bagi pengembang mana pun**: Backend, ilmu data, DevOps, analitik — semuanya memerlukan SQL.
- **Kuat**: Fungsi jendela, CTE, subkueri, dan agregasi memungkinkan Anda mengekspresikan logika kompleks dalam beberapa baris.
- **Kinerja**: Kueri SQL yang ditulis dengan baik pada database yang diindeks dengan benar dapat memproses jutaan baris dalam milidetik.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Bukan bahasa tujuan umum** | Tidak dapat membangun aplikasi, API, atau algoritma dalam SQL | Kombinasikan dengan Python, Java, JavaScript, dll |
| **Perbedaan dialek** | Setiap RDBMS memiliki ragam SQL sendiri dengan ekstensi yang tidak kompatibel | Tetap berpegang pada ANSI SQL jika memungkinkan; perbedaan dialek abstrak dalam aplikasi Anda |
| **Kekakuan skema** | Mengubah struktur tabel pada tabel besar bisa lambat dan mengganggu | Gunakan alat migrasi; desain skema dengan hati-hati di muka |
| **Masalah kueri N+1** | Kueri yang dihasilkan ORM bisa sangat tidak efisien | Tulis SQL khusus untuk kueri kompleks; profil dengan JELASKAN ANALISIS |
| **Penskalaan kompleksitas** | Database SQL lebih sulit untuk diskalakan secara horizontal dibandingkan NoSQL | Gunakan replika baca, sharding, atau pertimbangkan NoSQL untuk kasus penggunaan tertentu |
---

## Konsep Inti
### Model Relasional
Data disimpan dalam **tabel** (relasi), yang terdiri dari **baris** (catatan/tupel) dan **kolom** (atribut/bidang). Tabel dapat dihubungkan satu sama lain melalui **kunci**.
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

## Dasar Sintaks
### Mengambil Data (PILIH)
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

### Agregasi
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

### Menggabungkan Tabel
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

### Memodifikasi Data
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

## Sintaks & Pola Tingkat Lanjut
### Fungsi Jendela — Menyelami Lebih Dalam
Fungsi jendela melakukan penghitungan pada sekumpulan baris yang terkait dengan baris saat ini — tanpa mengelompokkannya menjadi satu baris keluaran seperti yang dilakukan GROUP BY.
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

### Ekspresi Tabel Umum (CTE) — Penggunaan Tingkat Lanjut
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

### Operasi JSON
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

### Prosedur dan Pemicu Tersimpan
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

## Selidiki Lebih Dalam Fitur Inti
### Optimasi Kueri
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

**Daftar periksa pengoptimalan:**
| Edisi | Gejala | Perbaiki |
|-------|---------|-----|
| Pemindaian berurutan pada tabel besar | `Seq Scan`dalam JELASKAN | Tambahkan indeks |
| Indeks tidak ada pada kolom WHERE | Pemindaian tabel lengkap | Buat indeks pada kolom yang difilter |
| PILIH * buang | Mengambil kolom yang tidak diperlukan | Pilih hanya kolom yang diperlukan |
| Konversi tipe implisit | Indeks tidak digunakan | Jenis pencocokan dalam perbandingan |
| Fungsi pada kolom yang diindeks | Indeks tidak dapat digunakan (tidak dapat disargable) | Tulis ulang:`WHERE date >= '2024-01-01'`bukan`WHERE YEAR(date) = 2024`|
### Strategi Pengindeksan
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

### Tingkat Isolasi Transaksi
| Tingkat Isolasi | Bacaan Kotor | Bacaan yang tidak dapat diulang | Bacaan Hantu |
|-----------------|:----------:|:-------------------:|:------------:|
| BACA TANPA KOMITMEN | Ya | Ya | Ya |
| BACA BERKOMITMEN | Tidak | Ya | Ya |
| BACA BERULANG | Tidak | Tidak | Ya* |
| DAPAT DISERIALKAN | Tidak | Tidak | Tidak |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalisasi
| Bentuk Biasa | Aturan | Contoh Pelanggaran |
|-------------|------|-------------------|
| **1NF** | Nilai atom, tidak ada grup berulang | Menyimpan beberapa ponsel dalam satu kolom sebagai "123.456" |
| **2NF** | 1NF + tidak ada ketergantungan parsial | Detail pesanan bergantung pada order_id tetapi tidak product_id |
| **3NF** | 2NF + tidak ada ketergantungan transitif | Nama departemen karyawan bergantung pada dept_id, bukan karyawan |
---

## Mendefinisikan Struktur Basis Data
### Membuat Tabel
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

### Mengubah Tabel
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Konfigurasi Proyek & Sistem Pembangunan
### Alat Migrasi
| Alat | Bahasa/Tumpukan | Pendekatan |
|------|---------------|----------|
| **Jalur Terbang** | Jawa / umum | Migrasi berbasis SQL, konvensi penamaan sederhana |
| **Liquibase** | Jawa / umum | Log perubahan XML, YAML, JSON, atau SQL |
| **Alembik** | Python (SQLAlkimia) | Menghasilkan migrasi secara otomatis dari perubahan model |
| **Prisma Bermigrasi** | Node.js / TypeScript | Skema-pertama, menghasilkan SQL |
| **golang-migrasi** | Pergi | Berbasis SQL, mendukung migrasi atas/bawah |
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

## Pengujian
### Uji Pembuatan Data
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

| Kerangka | Basis Data | Deskripsi |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Kerangka pengujian unit |
| **tSQLt** | SQLServer | Pengujian unit untuk SQL Server |
| **utPLSQL** | Peramal | Kerangka pengujian untuk Oracle PL/SQL |
---

## Interoperabilitas
### Pengikatan Bahasa
| Antarmuka | Bahasa | Deskripsi |
|-----------|----------|-------------|
| **JDBC** | Jawa | API basis data standar |
| **ODBC** | Banyak | API basis data universal |
| **psikopg2/3** | ular piton | Adaptor PostgreSQL |
| **basis data/sql** | Pergi | Pustaka standar dengan antarmuka driver |
| **sqlite3** | ular piton | Dukungan SQLite bawaan |
| **hal** | Node.js | Klien PostgreSQL |
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

## Pola Desain
### Pola 1: Pivot / Tab Silang
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Pola 2: Top-N Per Grup
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Pola 3: Kesenjangan dan Pulau
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

### Pola 4: Dimensi Berubah Secara Perlahan (SCD Tipe 2)
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

## Kinerja: Indeks dan Perencanaan Kueri
### Cara Kerja Indeks
Indeks adalah struktur data (biasanya pohon B) yang memungkinkan database menemukan baris tanpa memindai seluruh tabel.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Jenis Indeks | Terbaik Untuk | Contoh |
|-----------|----------|---------|
| **B-pohon** (default) | Kueri kesetaraan dan jangkauan | `WHERE age > 25 AND age < 35`|
| **hash** | Hanya kesetaraan yang tepat | `WHERE email = 'x@y.com'`|
| **GI** | Pencarian teks lengkap, array, JSON | `WHERE description @@ 'search term'`|
| **Intinya** | Data geometris/spasial | `WHERE location <-> point(x,y) < 1000`|
### Membaca Rencana Kueri
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

## Dialek SQL
| Fitur | PostgreSQL | MySQL | SQLServer | SQLite |
|---------|-----------|-------|------------|--------|
| Peningkatan otomatis | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Rangkaian string | `\|\|`| `CONCAT()`| `+`atau`CONCAT()`| `\|\|`|
| Fungsi tanggal | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| dukungan JSON | Luar Biasa (`jsonb`) | Bagus (`JSON`) | Bagus (`JSON`) | Dasar (`JSON1`) |
| Pencarian teks lengkap | Bawaan (`tsvector`) | Bawaan | Bawaan | Terbatas |
| Fungsi jendela | Ya | Ya (8.0+) | Ya | Ya |
---

## Penerapan
### Strategi Penerapan Basis Data
| Strategi | Deskripsi | Tingkat Risiko |
|----------|-------------|------------|
| **File migrasi** | Skrip SQL berversi diterapkan secara berurutan | Rendah |
| **Penyebaran biru-hijau** | Dua database identik; beralih lalu lintas | Rendah |
| **Perluas Kontrak** | Tambahkan kolom baru, tulis ganda, migrasi, hapus | Rendah |
| **DDL Langsung** | Menjalankan ALTER TABLE langsung pada produksi | Tinggi |
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

## Kapan Menggunakan SQL
| Skenario | Mengapa SQL | Alternatif |
|----------|---------|-------------|
| Data relasional dengan kueri kompleks | Untuk itulah SQL dirancang | --- |
| Integritas Transaksional (ACID) | Database SQL menjamin konsistensi | --- |
| Pelaporan dan analitik | Agregasi, fungsi jendela, CTE | Python (Pandas) untuk analisis yang sangat kompleks |
| Batasan integritas data | Kunci asing, PERIKSA, UNIK, BUKAN NULL | Validasi tingkat aplikasi (lebih lemah) |
| Penyimpanan nilai kunci sederhana | Berlebihan untuk kasus penggunaan ini | Redis, DynamoDB |
| Data yang sangat tidak terstruktur | Kekakuan skema adalah sebuah masalah | MongoDB, database dokumen |
| Penskalaan horizontal besar-besaran | Sulit untuk memecah database SQL | Cassandra, DynamoDB, CockroachDB |
---

## Tanya Jawab Sintetis
### Q1: Apa perbedaan antara`WHERE`dan`HAVING`?
**A:**`WHERE`memfilter baris sebelum dikelompokkan; `HAVING`memfilter grup setelah agregasi:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: Apa perbedaan fungsi jendela dengan GROUP BY?
**A:** Fungsi jendela menghitung seluruh baris tanpa menciutkannya:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: Bagaimana cara mengoptimalkan kueri yang lambat?
**A:** Strategi utama:
- Tambahkan indeks pada kolom yang digunakan di`WHERE`,`JOIN`, dan`ORDER BY`
- Hindari`SELECT *`— pilih kolom yang diperlukan saja
- Gunakan`EXPLAIN`/`EXPLAIN ANALYZE`untuk membaca rencana kueri
- Ganti subkueri dengan GABUNG jika memungkinkan
- Gunakan CTE agar mudah dibaca (biasanya tidak ada penalti kinerja)
- Hindari fungsi pada kolom yang diindeks di WHERE: gunakan`WHERE date >= '2024-01-01'`bukan `WHERE YEAR(date) = 2024`
### Q4: Apa itu CTE dan kapan saya harus menggunakannya?
**A:** Ekspresi Tabel Umum membuat kumpulan hasil sementara bernama:
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

### Q5: Bagaimana cara menangani nilai NULL dengan benar?
**A:** NULL melambangkan hal yang tidak diketahui — tidak sama dengan apa pun, termasuk dirinya sendiri:
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

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Menemukan N Teratas per Grup
**Langkah 1: Pahami Masalahnya**
Temukan 3 karyawan dengan bayaran tertinggi di setiap departemen.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan fungsi jendela dengan`ROW_NUMBER()`yang dipartisi berdasarkan departemen.
**Langkah 3: Terapkan**```sql
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

**Langkah 4: Verifikasi**
Pastikan setiap departemen mempunyai paling banyak 3 baris. Tangani ikatan dengan`DENSE_RANK()`jika diperlukan.
### Masalah 2: Membuat Laporan Pertumbuhan Tahun ke Tahun
**Langkah 1: Pahami Masalahnya**
Hitung pendapatan bulanan dan persentase pertumbuhan tahun ke tahun.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan`DATE_TRUNC`untuk pengelompokan dan fungsi jendela`LAG()`untuk perbandingan tahun sebelumnya.
**Langkah 3: Terapkan**```sql
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

**Langkah 4: Verifikasi**
Periksa 12 bulan pertama memiliki NULL untuk tahun sebelumnya. Validasi persentase pertumbuhan terhadap angka yang diketahui.
### Masalah 3: Memutar Baris ke Kolom
**Langkah 1: Pahami Masalahnya**
Ubah jumlah status dari baris ke kolom.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan agregasi bersyarat (`CASE`di dalam`SUM`).
**Langkah 3: Terapkan**```sql
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

**Langkah 4: Perpanjang**
Tambahkan kolom persentase dan total berjalan.
---

## Ringkasan
SQL adalah bahasa berusia 50 tahun yang tetap penting. Setiap pengembang, ilmuwan data, dan analis perlu mengetahuinya. Bahasa inti distandarisasi dan portabel; perbedaan dialek dapat dikelola. SQL modern (dengan fungsi jendela, CTE, dan dukungan JSON) cukup ekspresif untuk sebagian besar tugas data. Keterampilan utamanya adalah: menulis kueri yang efisien, memahami indeks, membaca rencana kueri, dan merancang skema yang baik. Jika Anda bekerja dengan data, SQL tidak dapat dinegosiasikan.