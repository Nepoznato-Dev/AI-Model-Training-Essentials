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
SQL (Lugha ya Maswali Iliyoundwa) ni lugha mahususi ya kikoa iliyoundwa kwa ajili ya kudhibiti na kuuliza data katika hifadhidata za uhusiano. Iliyoundwa kwa mara ya kwanza katika IBM katika miaka ya 1970 na kusawazishwa mnamo 1987, SQL inabaki kuwa kiolesura cha msingi kati ya programu na data zao. Kila Mfumo mkuu wa Usimamizi wa Hifadhidata ya Uhusiano (RDBMS) - PostgreSQL, MySQL, Seva ya SQL, Oracle, SQLite - hutumia SQL kama lugha yake ya kuuliza.
SQL sio lugha ya programu ya kusudi la jumla. Hungeandika programu ya wavuti katika SQL. Lakini ikiwa programu yako itahifadhi data - na karibu programu zote hufanya hivyo - basi SQL ndiyo lugha unayotumia kupata, kubadilisha, na kudhibiti data hiyo. Bila shaka ni ujuzi wa kiufundi muhimu zaidi ulimwenguni baada ya upangaji programu wa jumla.
---

## Kwa nini SQL Ni Muhimu
- **Universal**: Kila hifadhidata ya uhusiano inazungumza SQL. Jifunze mara moja, itumie kila mahali.
- **Taarifa**: Unaelezea *data* unayotaka, sio *jinsi* ya kuipata. Injini ya hifadhidata inaboresha utekelezaji.
- **Muhimu kwa msanidi yeyote**: Mazingira ya nyuma, sayansi ya data, DevOps, uchanganuzi - zote zinahitaji SQL.
- **Nye nguvu**: Vitendaji vya dirisha, CTE, hoja ndogo, na mijumuisho hukuruhusu ueleze mantiki changamano katika mistari michache.
- **Utendaji**: Hoja iliyoandikwa vizuri ya SQL kwenye hifadhidata iliyoonyeshwa vizuri inaweza kuchakata mamilioni ya safu mlalo katika milisekunde.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Si lugha ya kusudi la jumla** | Haiwezi kuunda programu, API, au kanuni katika SQL | Changanya na Python, Java, JavaScript, n.k. |
| **Tofauti za lahaja** | Kila RDBMS ina ladha yake ya SQL na viendelezi visivyoendana | Shikilia ANSI SQL inapowezekana; tofauti za lahaja dhahania katika programu yako |
| **Ugumu wa schema** | Kubadilisha miundo ya jedwali kwenye jedwali kubwa kunaweza kuwa polepole na kutatiza | Tumia zana za uhamiaji; kubuni schemas kwa makini mbele |
| **Tatizo la swali la N+1** | Hoja zinazozalishwa na ORM zinaweza kuwa zisizofaa sana | Andika SQL maalum kwa maswali magumu; wasifu ulio na ELEZA CHAMBUA |
| **Kuongeza utata** | Hifadhidata za SQL ni ngumu kuorodhesha mlalo kuliko NoSQL | Tumia nakala za kusoma, kugawa, au zingatia NoSQL kwa hali mahususi za utumiaji |
---

## Dhana za Msingi
### Mfano wa Uhusiano
Data huhifadhiwa katika **meza** (mahusiano), ambayo yanajumuisha **safu mlalo** (rekodi/nakala) na **safu** (sifa/nyuga). Majedwali yanaweza kuhusishwa kwa kila mmoja kupitia **funguo**.
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

## Misingi ya Sintaksia
### Kurejesha Data (CHAGUA)
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

### Kujumlisha
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

### Majedwali ya Kujiunga
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

### Kurekebisha Data
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

## Sintaksia na Miundo ya Kina
### Kazi za Dirisha — Kupiga mbizi kwa kina
Vitendaji vya dirisha hufanya hesabu katika safu mlalo mbalimbali zinazohusiana na safu mlalo ya sasa - bila kuzikunja kuwa safu mlalo ya towe kama vile GROUP BY inavyofanya.
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

### Maneno ya Kawaida ya Jedwali (CTEs) — Matumizi ya Hali ya Juu
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

### Operesheni za JSON
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

### Taratibu Zilizohifadhiwa na Vichochezi
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

## Dive kwa kina katika Vipengele vya Msingi
### Uboreshaji wa Hoja
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

**Orodha hakiki ya uboreshaji:**
| Suala | Dalili | Rekebisha |
|-------|----------|-----|
| Uchanganuzi mfuatano kwenye jedwali kubwa | `Seq Scan`katika EXPLAIN | Ongeza faharasa inayofaa |
| Faharasa haipo kwenye safu wima ya WHERE | Uchanganuzi kamili wa jedwali | Unda faharasa kwenye safu wima zilizochujwa |
| CHAGUA * taka | Inaleta safu wima zisizo za lazima | Chagua safu wima zinazohitajika pekee |
| Ubadilishaji wa aina isiyo wazi | Index haitumiki | Aina za mechi kwa kulinganisha |
| Kazi kwenye safu wima zilizowekwa kwenye faharasa | Fahirisi isiyoweza kutumika (isiyo sargable) | Andika tena:`WHERE date >= '2024-01-01'`sio`WHERE YEAR(date) = 2024`|
### Mikakati ya Kuorodhesha
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

### Viwango vya Kutengwa kwa Muamala
| Kiwango cha Kutengwa | Kusoma kwa Uchafu | Isiyorudiwa Soma | Phantom Soma |
|-----------------|:-----------:|:------------------:|:------------:|
| SOMA BILA KUJITOA | Ndiyo | Ndiyo | Ndiyo |
| SOMA UMEJITUMA | Hapana | Ndiyo | Ndiyo |
| INAYORUDIWA KUSOMA | Hapana | Hapana | Ndiyo* |
| SERIALIZABLE | Hapana | Hapana | Hapana |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Urekebishaji
| Fomu ya Kawaida | Kanuni | Ukiukaji wa Mfano |
|--------------------|-------------------|
| **1NF** | Thamani za atomiki, hakuna vikundi vinavyojirudia | Kuhifadhi simu nyingi katika safu wima moja kama "123,456" |
| **2NF** | 1NF + hakuna tegemezi kiasi | Maelezo ya agizo hutegemea order_id lakini si product_id |
| **3NF** | 2NF + hakuna tegemezi za mpito | Jina la idara ya mfanyakazi linategemea dept_id, si mfanyakazi |
---

## Kufafanua Muundo wa Hifadhidata
### Kuunda Majedwali
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

### Kubadilisha Majedwali
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Usanidi wa Mradi & Mfumo wa Kuunda
### Zana za Uhamiaji
| Zana | Lugha/Randi | Mbinu |
|------|---------------|-----------|
| **Njia ya ndege** | Java / ujumla | Uhamiaji unaotegemea SQL, mkataba rahisi wa kumtaja |
| **Liquibase** | Java / ujumla | Magogo ya mabadiliko ya XML, YAML, JSON, au SQL |
| **Alembiki** | Chatu (SQLAlchemy) | Huzalisha uhamishaji kiotomatiki kutoka kwa mabadiliko ya muundo |
| **Prisma Hamisha** | Node.js / TypeScript | Schema-kwanza, inazalisha SQL kiotomatiki |
| **golang-hamia** | Nenda | Kulingana na SQL, inasaidia uhamaji wa juu/chini |
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

##Upimaji
### Uzalishaji Data wa Jaribio
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

| Mfumo | Hifadhidata | Maelezo |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Mfumo wa upimaji wa kitengo |
| **tSQLt** | Seva ya SQL | Jaribio la kitengo cha Seva ya SQL |
| **utPLSQL** | Oracle | Mfumo wa majaribio wa Oracle PL/SQL |
---

## Kuingiliana
### Vifungo vya Lugha
| Kiolesura | Lugha | Maelezo |
|-----------|----------|-------------|
| **JDBC** | Java | API ya hifadhidata ya kawaida |
| **ODBC** | Nyingi | API ya hifadhidata ya jumla |
| **psycopg2/3** | Chatu | Adapta ya PostgreSQL |
| **database/sql** | Nenda | Maktaba ya kawaida yenye kiolesura cha kiendeshi |
| **sqlite3** | Chatu | Usaidizi wa SQLite uliojengwa ndani |
| **uk** | Node.js | Mteja wa PostgreSQL |
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

## Miundo ya Kubuni
### Mchoro wa 1: Pivot / Crosstab
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Mchoro wa 2: Juu-N Kwa Kila Kikundi
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Muundo wa 3: Mapungufu na Visiwa
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

### Mchoro wa 4: Kubadilisha Vipimo Polepole (Aina ya 2 ya SCD)
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

## Utendaji: Fahirisi na Upangaji wa Hoji
### Jinsi Fahirisi Hufanya Kazi
Faharasa ni muundo wa data (kawaida mti wa B) ambao huruhusu hifadhidata kupata safu mlalo bila kuchanganua jedwali zima.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Aina ya Kielezo | Bora Kwa | Mfano |
|-----------|----------|----------|
| **B-mti** (chaguo-msingi) | Usawa na maswali mbalimbali | `WHERE age > 25 AND age < 35`|
| **Hashi** | Usawa kamili pekee | `WHERE email = 'x@y.com'`|
| **GIN** | Utafutaji wa maandishi kamili, safu, JSON | `WHERE description @@ 'search term'`|
| **GIST** | Data ya kijiometri/ anga | `WHERE location <-> point(x,y) < 1000`|
### Mipango ya Maswali ya Kusoma
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

## Lahaja za SQL
| Kipengele | PostgreSQL | MySQL | Seva ya SQL | SQLite |
|---------|-----------|-------|-----------|--------|
| Kuongeza otomatiki | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Mshikamano wa kamba | `\|\|`| `CONCAT()`| `+`au`CONCAT()`| `\|\|`|
| Vitendaji vya tarehe | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Msaada wa JSON | Bora (`jsonb`) | Nzuri (`JSON`) | Nzuri (`JSON`) | Msingi (`JSON1`) |
| Utafutaji wa maandishi kamili | Imejengwa ndani (`tsvector`) | Imejengwa ndani | Imejengwa ndani | Kidogo |
| Vitendaji vya dirisha | Ndiyo | Ndiyo (8.0+) | Ndiyo | Ndiyo |
---

## Usambazaji
### Mikakati ya Usambazaji Hifadhidata
| Mkakati | Maelezo | Kiwango cha Hatari |
|----------|--------------------------|
| **Faili za uhamishaji** | Hati za SQL zilizotolewa zimetumika kwa mpangilio | Chini |
| **Bluu-kijani kupeleka** | Hifadhidata mbili zinazofanana; badilisha trafiki | Chini |
| **Panua-mkataba** | Ongeza safu wima mpya, andika-mbili, hamisha, acha zamani | Chini |
| **DDL ya moja kwa moja** | Inaendesha ALTER TABLE moja kwa moja kwenye uzalishaji | Juu |
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

## Wakati wa Kutumia SQL
| Hali | Kwa nini SQL | Mbadala |
|----------|---------|-------------|
| Data ya uhusiano yenye maswali changamano | Hiyo ndio SQL imeundwa kwa | --- |
| Uadilifu wa shughuli (ACID) | Hifadhidata za SQL zinahakikisha uthabiti | --- |
| Kuripoti na uchanganuzi | Majumuisho, utendakazi wa dirisha, CTEs | Python (Pandas) kwa uchambuzi mgumu sana |
| Vikwazo vya uadilifu wa data | Funguo za kigeni, ANGALIA, KIPEKEE, SI UFUPI | Uthibitishaji wa kiwango cha programu (dhaifu) |
| Hifadhi rahisi ya thamani ya ufunguo | Overkill kwa kesi hii ya matumizi | Redis, DynamoDB |
| Data isiyo na muundo | Ugumu wa schema ni tatizo | MongoDB, hifadhidata za hati |
| Kiwango kikubwa cha mlalo | Ni ngumu kuchambua hifadhidata za SQL | Cassandra, DynamoDB, CockroachDB |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`WHERE`na`HAVING`?
**J:**`WHERE`huchuja safu mlalo kabla ya kupanga; `HAVING`huchuja vikundi baada ya kujumlisha:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: Je, vitendaji vya dirisha vinatofautiana vipi na GROUP BY?
**J:** Vitendaji vya dirisha hukusanya safu mlalo bila kuzikunja:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: Je, ninawezaje kuboresha hoja za polepole?
**J:** Mikakati muhimu:
- Ongeza faharasa kwenye safu wima zinazotumika katika`WHERE`,`JOIN`, na`ORDER BY`
- Epuka`SELECT *`— chagua safu wima zinazohitajika pekee
- Tumia`EXPLAIN`/`EXPLAIN ANALYZE`kusoma mipango ya hoja
- Badilisha maswali madogo kwa JOIN inapowezekana
- Tumia CTE kwa usomaji (kawaida hakuna adhabu ya utendaji)
- Epuka utendakazi kwenye safu wima zilizoorodheshwa katika WHERE: tumia`WHERE date >= '2024-01-01'`sio `WHERE YEAR(date) = 2024`
### Q4: CTEs ni nini na ninapaswa kuzitumia lini?
**J:** Vielezi vya Jedwali la Kawaida huunda seti za matokeo ya muda zilizopewa majina:
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

### Q5: Ninawezaje kushughulikia maadili NULL kwa usahihi?
**J:** NULL inawakilisha haijulikani - si sawa na chochote, ikiwa ni pamoja na yenyewe:
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Kupata N ya Juu kwa kila Kikundi
**Hatua ya 1: Elewa Tatizo**
Tafuta wafanyikazi 3 wanaolipwa zaidi katika kila idara.
**Hatua ya 2: Tambua Mbinu**
Tumia kitendakazi cha dirisha na`ROW_NUMBER()`iliyogawanywa na idara.
**Hatua ya 3: Tekeleza**```sql
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

**Hatua ya 4: Thibitisha**
Hakikisha kuwa kila idara ina safu mlalo zisizozidi 3. Shughulikia uhusiano na`DENSE_RANK()`ikiwa inahitajika.
### Tatizo la 2: Kujenga Ripoti ya Ukuaji wa Mwaka kwa Mwaka
**Hatua ya 1: Elewa Tatizo**
Kukokotoa mapato ya kila mwezi na asilimia ya ukuaji wa mwaka baada ya mwaka.
**Hatua ya 2: Tambua Mbinu**
Tumia`DATE_TRUNC`kwa kupanga na`LAG()`chaguo za kukokotoa za dirisha kwa ulinganisho wa mwaka uliopita.
**Hatua ya 3: Tekeleza**```sql
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

**Hatua ya 4: Thibitisha**
Angalia miezi 12 ya kwanza ina NULL kwa mwaka uliopita. Thibitisha asilimia za ukuaji dhidi ya takwimu zinazojulikana.
### Tatizo la 3: Safu Mlalo Kuelekeza kwa Safu
**Hatua ya 1: Elewa Tatizo**
Badilisha hesabu za hali kutoka safu mlalo hadi safu wima.
**Hatua ya 2: Tambua Mbinu**
Tumia ujumlisho wa masharti (`CASE`ndani ya`SUM`).
**Hatua ya 3: Tekeleza**```sql
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

**Hatua ya 4: Panua**
Ongeza asilimia ya safu wima na jumla zinazoendeshwa.
---

## Muhtasari
SQL ni lugha ya miaka 50 ambayo bado ni muhimu. Kila msanidi programu, mwanasayansi wa data, na mchambuzi anahitaji kuijua. Lugha ya msingi ni sanifu na inabebeka; tofauti za lahaja zinaweza kudhibitiwa. SQL ya kisasa (iliyo na vitendaji vya dirisha, CTEs, na usaidizi wa JSON) inajieleza vya kutosha kwa kazi nyingi za data. Ujuzi muhimu ni: kuandika maswali kwa ufanisi, kuelewa faharasa, mipango ya hoja ya kusoma, na kubuni miundo mizuri. Ikiwa unafanya kazi na data kabisa, SQL haiwezi kujadiliwa.