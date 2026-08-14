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
SQL (زبان پرس و جو ساختاریافته) یک زبان دامنه خاص است که برای مدیریت و جستجوی داده ها در پایگاه های داده رابطه ای طراحی شده است. SQL اولین بار در IBM در دهه 1970 توسعه یافت و در سال 1987 استاندارد شد، SQL رابط اصلی بین برنامه‌ها و داده‌های آنها باقی می‌ماند. هر سیستم اصلی مدیریت پایگاه داده رابطه ای (RDBMS) - PostgreSQL، MySQL، SQL Server، Oracle، SQLite - از SQL به عنوان زبان پرس و جو استفاده می کند.
SQL یک زبان برنامه نویسی همه منظوره نیست. شما نمی توانید یک برنامه وب در SQL بنویسید. اما اگر برنامه شما داده ها را ذخیره می کند - و تقریباً همه برنامه ها این کار را انجام می دهند - SQL زبانی است که برای بازیابی، تبدیل و مدیریت آن داده ها استفاده می کنید. مسلماً این مهارت فنی پس از برنامه نویسی عمومی مفیدترین مهارت فنی است.
---

## چرا SQL مهم است
- **Universal**: هر پایگاه داده رابطه ای SQL صحبت می کند. یک بار یاد بگیرید، همه جا از آن استفاده کنید.
- **اعلامی**: شما *چه* داده هایی را که می خواهید، توصیف می کنید، نه *چگونه* را دریافت کنید. موتور پایگاه داده اجرا را بهینه می کند.
- ** ضروری برای هر توسعه دهنده **: Backend، علم داده، DevOps، تجزیه و تحلیل - همه به SQL نیاز دارند.
- **قدرتمند**: توابع پنجره، CTEها، سوالات فرعی، و تجمیع به شما امکان می دهند منطق پیچیده را در چند خط بیان کنید.
- **عملکرد**: یک پرس و جوی SQL به خوبی نوشته شده بر روی یک پایگاه داده به درستی نمایه شده می تواند میلیون ها ردیف را در میلی ثانیه پردازش کند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **زبان همه منظوره نیست** | نمی توان برنامه ها، API ها یا الگوریتم ها را در SQL | ساخت ترکیب با پایتون، جاوا، جاوا اسکریپت و غیره |
| **تفاوت گویش** | هر RDBMS طعم SQL خاص خود را با پسوندهای ناسازگار دارد | در صورت امکان به ANSI SQL بچسبید. تفاوت های انتزاعی گویش در برنامه شما |
| **سختی طرحواره** | تغییر ساختار جدول روی میزهای بزرگ می تواند کند و مخرب باشد | از ابزارهای مهاجرت استفاده کنید. طرحواره ها را با دقت از قبل طراحی کنید |
| **مشکل پرس و جو N+1** | پرس و جوهای تولید شده توسط ORM می توانند بسیار ناکارآمد باشند | نوشتن SQL سفارشی برای پرس و جوهای پیچیده. نمایه با EXPLAIN ANALYZE |
| **پیچیدگی مقیاس بندی** | مقیاس افقی پایگاه داده های SQL سخت تر از NoSQL | است از replica های خواندنی، اشتراک گذاری استفاده کنید یا NoSQL را برای موارد استفاده خاص در نظر بگیرید |
---

## مفاهیم اصلی
### مدل رابطه ای
داده‌ها در **جدول** (روابط) ذخیره می‌شوند که از **ردیف** (رکوردها/مقدارها) و**ستون**ها (ویژگیها/فیلدها) تشکیل شده است. جداول را می توان از طریق **کلیدها** به یکدیگر مرتبط کرد.
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

## اصول نحو
### بازیابی داده ها (SELECT)
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

### تجمیع
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

### پیوستن به جداول
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

### تغییر داده ها
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

## نحو و الگوهای پیشرفته
### توابع پنجره - شیرجه عمیق
توابع پنجره محاسبات را در میان مجموعه‌ای از ردیف‌های مربوط به ردیف فعلی انجام می‌دهند - بدون اینکه آنها را در یک ردیف خروجی واحد مانند GROUP BY جمع کنند.
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

### عبارات جدول رایج (CTEs) - استفاده پیشرفته
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

### عملیات JSON
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

### رویه ها و محرک های ذخیره شده
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

## به ویژگی های اصلی شیرجه بزنید
### بهینه سازی پرس و جو
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

**چک لیست بهینه سازی:**
| شماره | علامت | رفع |
|-------|---------|-----|
| اسکن متوالی روی میز بزرگ | `Seq Scan`در توضیح | افزودن نمایه مناسب |
| فهرست موجود در ستون WHERE | اسکن کامل جدول | ایجاد نمایه در ستون های فیلتر شده |
| انتخاب * زباله | واکشی ستون های غیر ضروری | فقط ستون های مورد نیاز را انتخاب کنید |
| تبدیل نوع ضمنی | فهرست استفاده نشده | انواع مطابقت در مقایسه |
| توابع در ستون های نمایه شده | ایندکس غیرقابل استفاده (غیر قابل استفاده) | بازنویسی:`WHERE date >= '2024-01-01'`نه`WHERE YEAR(date) = 2024`|
### استراتژی های نمایه سازی
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

### سطوح جداسازی تراکنش
| سطح ایزوله | کثیف خواندن | غیر قابل تکرار خواندن | فانتوم خوانده شده |
|------------------|:----------:|:-------------------:|:------------:|
| خواندن غیرمتعهد | بله | بله | بله |
| خواندن متعهد | نه | بله | بله |
| تکراری خواندن | نه | نه | بله* |
| سریال سازی | نه | نه | نه |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### عادی سازی
| فرم معمولی | قانون | مثال نقض |
|-------------|------|-------------------|
| **1NF** | مقادیر اتمی، بدون گروه های تکراری | ذخیره چندین تلفن در یک ستون به عنوان "123,456" |
| **2NF** | 1NF + بدون وابستگی جزئی | جزئیات سفارش به order_id بستگی دارد اما نه product_id |
| **3NF** | 2NF + بدون وابستگی گذرا | نام گروه کارمند به dept_id بستگی دارد نه به کارمند |
---

## تعریف ساختار پایگاه داده
### ایجاد جداول
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

### تغییر جداول
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## پیکربندی پروژه و سیستم ساخت
### ابزارهای مهاجرت
| ابزار | زبان/پشته | رویکرد |
|------|---------------|----------|
| **فلای وی** | جاوا / عمومی | مهاجرت های مبتنی بر SQL، قرارداد نامگذاری ساده |
| **Liquibase** | جاوا / عمومی | تغییرات XML، YAML، JSON یا SQL |
| **آلمبیک** | پایتون (SQLAlchemy) | ایجاد خودکار مهاجرت از تغییرات مدل |
| **پریسما مهاجرت** | Node.js / TypeScript | طرحواره اول، SQL را به صورت خودکار تولید می کند |
| **گلانگ-مهاجرت** | برو | مبتنی بر SQL، از مهاجرت های بالا/پایین پشتیبانی می کند |
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

## تست
### تست تولید داده
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

| چارچوب | پایگاه داده | توضیحات |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | چارچوب تست واحد |
| **tSQLt** | SQL Server | تست واحد برای SQL Server |
| **utPLSQL** | اوراکل | چارچوب تست Oracle PL/SQL |
---

## قابلیت همکاری
### پیوندهای زبان
| رابط | زبان | توضیحات |
|-----------|----------|-------------|
| **JDBC** | جاوا | API پایگاه داده استاندارد |
| **ODBC** | چندگانه | API پایگاه داده جهانی |
| **psycopg2/3** | پایتون | آداپتور PostgreSQL |
| **پایگاه داده/sql** | برو | کتابخانه استاندارد با رابط درایور |
| **sqlite3** | پایتون | پشتیبانی داخلی SQLite |
| **صفحه** | Node.js | مشتری PostgreSQL |
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

## الگوهای طراحی
### الگوی 1: Pivot / Crosstab
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### الگوی 2: Top-N در هر گروه
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### الگوی 3: شکاف ها و جزایر
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

### الگوی 4: به آرامی تغییر ابعاد (SCD نوع 2)
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

## عملکرد: شاخص ها و برنامه ریزی پرس و جو
### چگونه شاخص ها کار می کنند
ایندکس یک ساختار داده است (معمولا یک درخت B) که به پایگاه داده اجازه می دهد بدون اسکن کل جدول، ردیف ها را پیدا کند.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| نوع شاخص | بهترین برای | مثال |
|-----------|----------|---------|
| **B-tree** (پیش فرض) | پرس و جوهای برابری و محدوده | `WHERE age > 25 AND age < 35`|
| **هش** | فقط برابری دقیق | `WHERE email = 'x@y.com'`|
| **GIN** | جستجوی متن کامل، آرایه ها، JSON | `WHERE description @@ 'search term'`|
| **GiST** | داده های هندسی/مکانی | `WHERE location <-> point(x,y) < 1000`|
### خواندن طرح های پرس و جو
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

## گویش های SQL
| ویژگی | PostgreSQL | MySQL | SQL Server | SQLite |
|---------|-----------|------|------------|--------|
| افزایش خودکار | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Concat رشته | `\|\|`| `CONCAT()`| `+`یا`CONCAT()`| `\|\|`|
| توابع تاریخ | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| پشتیبانی JSON | عالی (`jsonb`) | خوب (`JSON`) | خوب (`JSON`) | پایه (`JSON1`) |
| جستجوی متن کامل | داخلی (`tsvector`) | داخلی | داخلی | محدود |
| توابع پنجره | بله | بله (8.0+) | بله | بله |
---

## استقرار
### استراتژی های استقرار پایگاه داده
| استراتژی | توضیحات | سطح ریسک |
|----------|-------------|------------|
| **فایل های مهاجرت** | اسکریپت های SQL نسخه شده به ترتیب | کم |
| **استقرار سبز-آبی** | دو پایگاه داده یکسان؛ سوئیچ ترافیک | کم |
| **توسعه-قرارداد** | اضافه کردن ستون جدید، نوشتن دوگانه، مهاجرت، رها کردن قدیمی | کم |
| **DDL مستقیم** | اجرای ALTER TABLE به طور مستقیم در تولید | بالا |
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

## چه زمانی از SQL استفاده کنیم
| سناریو | چرا SQL | جایگزین |
|----------|---------|-------------|
| داده های رابطه ای با پرس و جوهای پیچیده | این همان چیزی است که SQL برای | طراحی شده است --- |
| یکپارچگی تراکنش (ACID) | پایگاه داده های SQL ثبات را تضمین می کنند | --- |
| گزارش و تحلیل | تجمعات، توابع پنجره، CTEs | پایتون (پاندا) برای تجزیه و تحلیل بسیار پیچیده |
| محدودیت های یکپارچگی داده ها | کلیدهای خارجی، چک، منحصر به فرد، NOT NULL | اعتبار سنجی در سطح برنامه (ضعیفتر) |
| ذخیره سازی ساده کلید-مقدار | Overkill برای این مورد استفاده | Redis، DynamoDB |
| داده های بسیار بدون ساختار | سختی طرحواره یک مشکل است | MongoDB، پایگاه داده اسناد |
| مقیاس افقی عظیم | سخت به خرد کردن پایگاه داده های SQL | Cassandra، DynamoDB، CockroachDB |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین`WHERE`و`HAVING`چیست؟
**A:**`WHERE`سطرها را قبل از گروه بندی فیلتر می کند. `HAVING`گروه ها را پس از تجمیع فیلتر می کند:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: عملکردهای پنجره چه تفاوتی با GROUP BY دارند؟
**A:** توابع پنجره بدون جمع کردن سطرها محاسبه می شوند:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: چگونه پرس و جوهای کند را بهینه کنم؟
**الف:** استراتژی های کلیدی:
- اضافه کردن فهرست به ستون های مورد استفاده در `WHERE`، `JOIN`، و`ORDER BY`
- اجتناب از`SELECT *`- فقط ستون های مورد نیاز را انتخاب کنید
- از`EXPLAIN`/`EXPLAIN ANALYZE`برای خواندن طرح های پرس و جو استفاده کنید
- در صورت امکان، درخواست های فرعی را با JOIN جایگزین کنید
- از CTE برای خوانایی استفاده کنید (معمولاً بدون جریمه عملکرد)
- اجتناب از توابع در ستون های نمایه شده در WHERE: از`WHERE date >= '2024-01-01'`استفاده کنید نه `WHERE YEAR(date) = 2024`
### Q4: CTE چیست و چه زمانی باید از آنها استفاده کنم؟
**A:** عبارات جدول مشترک مجموعه نتایج موقت نامگذاری شده را ایجاد می کنند:
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

### Q5: چگونه مقادیر NULL را به درستی مدیریت کنم؟
**A:** NULL نشان دهنده ناشناخته است - با هیچ چیز از جمله خودش برابر نیست:
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یافتن N برتر در هر گروه
**مرحله 1: مشکل را درک کنید**
3 کارمند پردرآمد در هر بخش را پیدا کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از یک تابع پنجره با`ROW_NUMBER()`پارتیشن بندی شده توسط بخش استفاده کنید.
**مرحله 3: پیاده سازی **```sql
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

**مرحله 4: تایید **
بررسی کنید که هر بخش حداکثر 3 ردیف داشته باشد. در صورت نیاز، اتصالات را با`DENSE_RANK()`انجام دهید.
### مشکل 2: ایجاد گزارش رشد سال به سال
**مرحله 1: مشکل را درک کنید**
درآمد ماهانه و درصد رشد سال به سال را محاسبه کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از`DATE_TRUNC`برای گروه بندی و از تابع پنجره`LAG()`برای مقایسه سال قبل استفاده کنید.
**مرحله 3: پیاده سازی **```sql
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

**مرحله 4: تایید **
بررسی کنید 12 ماه اول NULL برای سال قبل باشد. درصد رشد را در برابر ارقام شناخته شده تأیید کنید.
### مشکل 3: چرخش ردیف ها به ستون ها
**مرحله 1: مشکل را درک کنید**
شمارش وضعیت را از ردیف به ستون تبدیل کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از تجمیع شرطی استفاده کنید (`CASE` داخل `SUM`).
**مرحله 3: پیاده سازی **```sql
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

**مرحله 4: تمدید**
ستون های درصد و مجموع در حال اجرا را اضافه کنید.
---

## خلاصه
SQL یک زبان 50 ساله است که همچنان ضروری است. هر توسعه دهنده، دانشمند داده و تحلیلگر باید آن را بداند. زبان اصلی استاندارد و قابل حمل است. تفاوت های لهجه ای قابل کنترل است. SQL مدرن (با توابع پنجره، CTEها و پشتیبانی JSON) برای اکثر وظایف داده به اندازه کافی گویا است. مهارت های کلیدی عبارتند از: نوشتن پرس و جوهای کارآمد، درک نمایه ها، خواندن طرح های پرس و جو و طراحی طرحواره های خوب. اگر اصلاً با داده کار می کنید، SQL غیرقابل مذاکره است.