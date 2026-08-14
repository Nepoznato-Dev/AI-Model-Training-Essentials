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
# SQL
Ang SQL (Structured Query Language) ay isang domain-specific na wika na idinisenyo para sa pamamahala at pag-query ng data sa mga relational na database. Unang binuo sa IBM noong 1970s at na-standardize noong 1987, ang SQL ay nananatiling pangunahing interface sa pagitan ng mga application at ng kanilang data. Ang bawat pangunahing Relational Database Management System (RDBMS) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — ay gumagamit ng SQL bilang query language nito.
Ang SQL ay hindi isang pangkalahatang layunin na programming language. Hindi ka magsulat ng isang web application sa SQL. Ngunit kung ang iyong application ay nag-iimbak ng data - at halos lahat ng mga application ay nag-iimbak - kung gayon ang SQL ay ang wikang ginagamit mo upang kunin, baguhin, at pamahalaan ang data na iyon. Ito ay arguably ang pinaka-unibersal na kapaki-pakinabang na teknikal na kasanayan pagkatapos ng pangkalahatang programming.
---

## Bakit Mahalaga ang SQL
- **Universal**: Ang bawat relational database ay nagsasalita ng SQL. Matuto nang isang beses, gamitin ito kahit saan.
- **Declarative**: Inilalarawan mo *anong* data ang gusto mo, hindi *paano* ito makukuha. Ang database engine ay nag-optimize ng pagpapatupad.
- **Mahalaga para sa sinumang developer**: Backend, data science, DevOps, analytics — lahat ay nangangailangan ng SQL.
- **Makapangyarihan**: Hinahayaan ka ng mga function ng window, CTE, subquery, at aggregation na magpahayag ng kumplikadong lohika sa ilang linya.
- **Pagganap**: Ang isang mahusay na nakasulat na SQL query sa isang maayos na na-index na database ay maaaring magproseso ng milyun-milyong row sa millisecond.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Hindi isang pangkalahatang layunin na wika** | Hindi makabuo ng mga application, API, o algorithm sa SQL | Pagsamahin sa Python, Java, JavaScript, atbp. |
| **Mga pagkakaiba sa diyalekto** | Ang bawat RDBMS ay may sariling SQL flavor na may mga hindi tugmang extension | Manatili sa ANSI SQL kung posible; abstract na mga pagkakaiba sa diyalekto sa iyong aplikasyon |
| **Katigasan ng schema** | Ang pagpapalit ng mga istruktura ng talahanayan sa malalaking talahanayan ay maaaring maging mabagal at nakakagambala | Gumamit ng mga tool sa paglipat; disenyo ng mga schema nang maingat sa harap |
| **N+1 query problem** | Ang mga query na binuo ng ORM ay maaaring maging lubhang hindi mahusay | Sumulat ng custom na SQL para sa mga kumplikadong query; profile na may EXPLAIN ANALYZE |
| **Pagiging kumplikado ng scaling** | Ang mga database ng SQL ay mas mahirap sukatin nang pahalang kaysa sa NoSQL | Gumamit ng mga read replicas, sharding, o isaalang-alang ang NoSQL para sa mga partikular na kaso ng paggamit |
---

## Mga Pangunahing Konsepto
### Ang Relational Model
Naka-store ang data sa **tables** (relasyon), na binubuo ng **rows** (records/tuples) at **column** (attribute/fields). Maaaring iugnay ang mga talahanayan sa isa't isa sa pamamagitan ng **mga key**.
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

## Syntax Fundamentals
### Pagbawi ng Data (PUMILI)
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

### Pagsasama-sama
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

### Sumasali sa mga Table
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

### Pagbabago ng Data
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

## Advanced na Syntax at Mga Pattern
### Mga Function ng Window — Deep Dive
Ang mga function ng window ay nagsasagawa ng mga kalkulasyon sa isang hanay ng mga row na nauugnay sa kasalukuyang row — nang hindi ibinabagsak ang mga ito sa iisang output row tulad ng ginagawa ng GROUP BY.
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

### Common Table Expressions (CTEs) — Advanced na Paggamit
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

### JSON Operations
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

### Mga Naka-imbak na Pamamaraan at Trigger
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

## Malalim na Sumisid sa Mga Pangunahing Tampok
### Pag-optimize ng Query
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

**Checklist ng pag-optimize:**
| Isyu | Sintomas | Ayusin |
|-------|---------|-----|
| Sequential scan sa malaking table | `Seq Scan`sa EXPLAIN | Magdagdag ng naaangkop na index |
| Nawawalang index sa column na WHERE | Pag-scan ng buong talahanayan | Gumawa ng index sa mga na-filter na column |
| PUMILI * basura | Kinukuha ang mga hindi kinakailangang column | Piliin lamang ang mga kinakailangang column |
| Implicit na uri ng conversion | Hindi ginamit ang index | Mga uri ng pagtutugma sa mga paghahambing |
| Mga function sa mga na-index na column | Hindi nagagamit ang index (non-sargable) | Isulat muli:`WHERE date >= '2024-01-01'`hindi`WHERE YEAR(date) = 2024`|
### Mga Istratehiya sa Pag-index
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

### Mga Antas ng Paghihiwalay ng Transaksyon
| Antas ng Paghihiwalay | Dirty Read | Hindi nauulit na Basahin | Phantom Read |
|-----------------|:----------:|:-------------------:|:------------:|
| BASAHIN UNCOMMITTED | Oo | Oo | Oo |
| READ COMMITTED | Hindi | Oo | Oo |
| ULIT-ULIT NA BASAHIN | Hindi | Hindi | Oo* |
| SERIALIZABLE | Hindi | Hindi | Hindi |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalisasyon
| Normal na Anyo | Panuntunan | Halimbawa ng Paglabag |
|-------------|------|-------------------|
| **1NF** | Mga halaga ng atom, walang paulit-ulit na pangkat | Pag-iimbak ng maraming telepono sa isang column bilang "123,456" |
| **2NF** | 1NF + walang bahagyang dependencies | Ang detalye ng order ay nakadepende sa order_id ngunit hindi product_id |
| **3NF** | 2NF + walang transitive dependencies | Ang pangalan ng dept ng empleyado ay nakasalalay sa dept_id, hindi empleyado |
---

## Pagtukoy sa Istraktura ng Database
### Paggawa ng mga Table
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

### Binabago ang mga Table
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Project Configuration at Build System
### Mga Tool sa Paglipat
| Tool | Wika/Stack | Diskarte |
|------|--------------|----------|
| **Flyway** | Java / pangkalahatan | Mga paglilipat na batay sa SQL, simpleng kombensyon ng pagbibigay ng pangalan |
| **Liquibase** | Java / pangkalahatan | XML, YAML, JSON, o SQL changelogs |
| **Alembic** | Python (SQLAlchemy) | Awtomatikong bumubuo ng mga paglilipat mula sa mga pagbabago sa modelo |
| **Prisma Migrate** | Node.js / TypeScript | Schema-first, awtomatikong bumubuo ng SQL |
| **golang-migrate** | Pumunta | Nakabatay sa SQL, sumusuporta sa pataas/pababang paglilipat |
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

## Pagsubok
### Pagbuo ng Data ng Pagsubok
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

| Balangkas | Database | Paglalarawan |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Unit testing framework |
| **tSQLt** | SQL Server | Unit testing para sa SQL Server |
| **utPLSQL** | Oracle | Balangkas ng pagsubok para sa Oracle PL/SQL |
---

## Interoperability
### Mga Binding sa Wika
| Interface | Wika | Paglalarawan |
|-----------|----------|-------------|
| **JDBC** | Java | Standard database API |
| **ODBC** | Maramihang | Universal database API |
| **psycopg2/3** | Python | PostgreSQL adapter |
| **database/sql** | Pumunta | Karaniwang library na may driver interface |
| **sqlite3** | Python | Built-in na suporta sa SQLite |
| **pg** | Node.js | PostgreSQL client |
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

## Mga Pattern ng Disenyo
### Pattern 1: Pivot / Crosstab
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Pattern 2: Top-N Bawat Grupo
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Pattern 3: Mga Gaps at Isla
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

### Pattern 4: Dahan-dahang Nagbabago ng Mga Dimensyon (SCD Type 2)
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

## Pagganap: Mga Index at Pagpaplano ng Query
### Paano Gumagana ang Mga Index
Ang index ay isang istraktura ng data (karaniwan ay isang B-tree) na nagbibigay-daan sa database na makahanap ng mga hilera nang hindi ini-scan ang buong talahanayan.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Uri ng Index | Pinakamahusay Para sa | Halimbawa |
|-----------|----------|---------|
| **B-tree** (default) | Mga query sa pagkakapantay-pantay at saklaw | `WHERE age > 25 AND age < 35`|
| **Hash** | Eksaktong pagkakapantay-pantay lamang | `WHERE email = 'x@y.com'`|
| **GIN** | Full-text na paghahanap, mga array, JSON | `WHERE description @@ 'search term'`|
| **GiST** | Geometric/spatial na data | `WHERE location <-> point(x,y) < 1000`|
### Pagbabasa ng Mga Plano sa Query
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

## Mga Diyalekto ng SQL
| Tampok | PostgreSQL | MySQL | SQL Server | SQLite |
|---------|-----------|-------|------------|--------|
| Auto-increment | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| String concat | `\|\|`| `CONCAT()`| `+`o`CONCAT()`| `\|\|`|
| Mga function ng petsa | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Suporta sa JSON | Napakahusay (`jsonb`) | Maganda (`JSON`) | Maganda (`JSON`) | Basic (`JSON1`) |
| Full-text na paghahanap | Built-in (`tsvector`) | Built-in | Built-in | Limitado |
| Mga function ng window | Oo | Oo (8.0+) | Oo | Oo |
---

## Deployment
### Mga Istratehiya sa Pag-deploy ng Database
| Diskarte | Paglalarawan | Antas ng Panganib |
|----------|-------------|------------|
| **Migration file** | Inilapat ang mga bersyon ng SQL script sa pagkakasunud-sunod | Mababa |
| **Asul-berde na pag-deploy** | Dalawang magkaparehong database; lumipat ng trapiko | Mababa |
| **Palawakin-kontrata** | Magdagdag ng bagong column, dual-write, migrate, drop old | Mababa |
| **Direktang DDL** | Direktang tumatakbo ang ALTER TABLE sa produksyon | Mataas |
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

## Kailan Gamitin ang SQL
| Sitwasyon | Bakit SQL | Alternatibo |
|----------|---------|-------------|
| Relational data na may mga kumplikadong query | Iyon ay kung ano ang SQL ay dinisenyo para sa | --- |
| Transactional integrity (ACID) | Ginagarantiyahan ng mga database ng SQL ang pagkakapare-pareho | --- |
| Pag-uulat at analytics | Mga pagsasama-sama, mga function ng window, mga CTE | Python (Pandas) para sa napakakomplikadong pagsusuri |
| Mga hadlang sa integridad ng data | Mga dayuhang key, CHECK, NATATANGI, HINDI NULL | Pagpapatunay sa antas ng aplikasyon (mas mahina) |
| Simpleng key-value na storage | Overkill para sa use case na ito | Redis, DynamoDB |
| Highly unstructured data | Ang katigasan ng schema ay isang problema | MongoDB, mga database ng dokumento |
| Napakalaking pahalang na pag-scale | Mahirap i-shard ang mga database ng SQL | Cassandra, DynamoDB, CockroachDB |
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba ng`WHERE`at`HAVING`?
**A:** Ang`WHERE`ay nagsasala ng mga hilera bago ang pagpapangkat;  Ang`HAVING`ay nag-filter ng mga pangkat pagkatapos ng pagsasama-sama:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: Paano naiiba ang mga function ng window sa GROUP BY?
**A:** Ang mga function ng window ay nagko-compute sa mga row nang hindi kino-collapse ang mga ito:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: Paano ko i-optimize ang mabagal na query?
**S:** Mga pangunahing diskarte:
- Magdagdag ng mga index sa mga column na ginamit sa`WHERE`,`JOIN`, at`ORDER BY`
- Iwasan ang`SELECT *`— piliin lamang ang mga kinakailangang column
- Gamitin ang`EXPLAIN`/`EXPLAIN ANALYZE`upang basahin ang mga query plan
- Palitan ang mga subquery ng mga JOIN kung posible
- Gumamit ng mga CTE para sa pagiging madaling mabasa (karaniwan ay walang parusa sa pagganap)
- Iwasan ang mga function sa mga naka-index na column sa WHERE: gamitin ang`WHERE date >= '2024-01-01'`hindi `WHERE YEAR(date) = 2024`
### Q4: Ano ang mga CTE at kailan ko dapat gamitin ang mga ito?
**S:** Lumilikha ang Mga Karaniwang Ekspresyon ng Talahanayan na pinangalanang pansamantalang mga hanay ng resulta:
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

### Q5: Paano ko hahawakan nang tama ang mga NULL na halaga?
**A:** Ang NULL ay kumakatawan sa hindi alam — hindi ito katumbas ng anuman, kasama ang sarili nito:
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Paghahanap ng Nangungunang N bawat Grupo
**Hakbang 1: Unawain ang Problema**
Hanapin ang 3 pinakamataas na suweldong empleyado sa bawat departamento.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng window function na may`ROW_NUMBER()`na hinati ayon sa departamento.
**Hakbang 3: Ipatupad**```sql
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

**Hakbang 4: I-verify**
Suriin na ang bawat departamento ay may hindi hihigit sa 3 row. Pangasiwaan ang mga kurbatang gamit ang`DENSE_RANK()`kung kinakailangan.
### Problema 2: Pagbuo ng Year-over-Year Growth Report
**Hakbang 1: Unawain ang Problema**
Kalkulahin ang buwanang kita at taon-sa-taon na porsyento ng paglago.
**Hakbang 2: Tukuyin ang Diskarte**
Gamitin ang`DATE_TRUNC`para sa pagpapangkat at`LAG()`window function para sa nakaraang taon na paghahambing.
**Hakbang 3: Ipatupad**```sql
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

**Hakbang 4: I-verify**
Suriin ang unang 12 buwan ay may NULL para sa nakaraang taon. Patunayan ang mga porsyento ng paglago laban sa mga kilalang numero.
### Problema 3: Pag-pivote ng Mga Row sa Mga Column
**Hakbang 1: Unawain ang Problema**
Baguhin ang mga bilang ng katayuan mula sa mga hilera patungo sa mga hanay.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng conditional aggregation (`CASE`sa loob ng`SUM`).
**Hakbang 3: Ipatupad**```sql
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

**Hakbang 4: Palawakin**
Magdagdag ng mga column ng porsyento at mga kabuuang tumatakbo.
---

## Buod
Ang SQL ay isang 50 taong gulang na wika na nananatiling mahalaga. Kailangang malaman ito ng bawat developer, data scientist, at analyst. Ang pangunahing wika ay standardized at portable; ang mga pagkakaiba ng diyalekto ay mapapamahalaan. Ang modernong SQL (na may mga function ng window, CTE, at suporta sa JSON) ay sapat na nagpapahayag para sa karamihan ng mga gawain sa data. Ang mga pangunahing kasanayan ay: pagsulat ng mahusay na mga query, pag-unawa sa mga index, pagbabasa ng mga plano ng query, at pagdidisenyo ng magagandang schema. Kung nagtatrabaho ka sa data sa lahat, ang SQL ay hindi mapag-usapan.