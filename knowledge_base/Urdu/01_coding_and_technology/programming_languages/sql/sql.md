---
# Metadata
title: "SQL"
description: "Comprehensive reference for the SQL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
SQL (Structured Query Language) ایک ڈومین کے لیے مخصوص زبان ہے جسے متعلقہ ڈیٹا بیس میں ڈیٹا کے انتظام اور استفسار کے لیے ڈیزائن کیا گیا ہے۔ سب سے پہلے 1970 کی دہائی میں IBM میں تیار کیا گیا اور 1987 میں معیاری بنایا گیا، SQL ایپلی کیشنز اور ان کے ڈیٹا کے درمیان بنیادی انٹرفیس ہے۔ ہر بڑا رشتہ دار ڈیٹا بیس مینجمنٹ سسٹم (RDBMS) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — SQL کو اپنی استفسار کی زبان کے طور پر استعمال کرتا ہے۔
SQL ایک عام مقصد کی پروگرامنگ زبان نہیں ہے۔ آپ ایس کیو ایل میں ویب ایپلیکیشن نہیں لکھیں گے۔ لیکن اگر آپ کی ایپلی کیشن ڈیٹا کو اسٹور کرتی ہے — اور تقریباً تمام ایپلیکیشنز کرتی ہیں — تو SQL وہ زبان ہے جسے آپ ڈیٹا کو بازیافت کرنے، تبدیل کرنے اور اس کا نظم کرنے کے لیے استعمال کرتے ہیں۔ یہ عام پروگرامنگ کے بعد سب سے زیادہ عالمی طور پر مفید تکنیکی مہارت ہے۔
---

## ایس کیو ایل کیوں اہمیت رکھتا ہے۔
- **یونیورسل**: ہر متعلقہ ڈیٹا بیس SQL بولتا ہے۔ اسے ایک بار سیکھیں، اسے ہر جگہ استعمال کریں۔
- **اعلانیہ**: آپ بیان کرتے ہیں کہ آپ *کونسا* ڈیٹا چاہتے ہیں، اسے *کیسے* حاصل کرنا ہے۔ ڈیٹا بیس انجن عملدرآمد کو بہتر بناتا ہے۔
- **کسی بھی ڈویلپر کے لیے ضروری**: بیک اینڈ، ڈیٹا سائنس، ڈی او اوپس، اینالیٹکس — سبھی کے لیے SQL درکار ہے۔
- **طاقتور**: ونڈو فنکشنز، CTEs، ذیلی سوالات، اور جمع آپ کو چند سطروں میں پیچیدہ منطق کا اظہار کرنے دیتے ہیں۔
- **کارکردگی**: مناسب طریقے سے انڈیکس شدہ ڈیٹا بیس پر ایک اچھی طرح سے لکھا ہوا SQL سوال ملی سیکنڈ میں لاکھوں قطاروں پر کارروائی کرسکتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **عام مقصد کی زبان نہیں** | SQL میں ایپلیکیشنز، APIs، یا الگورتھم نہیں بنا سکتے ازگر، جاوا، جاوا اسکرپٹ، وغیرہ کے ساتھ جوڑیں۔
| **بولی کے فرق** | ہر RDBMS کا اپنا ایس کیو ایل ذائقہ ہے جس میں غیر مطابقت پذیر ایکسٹینشنز ہیں | جہاں ممکن ہو ANSI SQL پر قائم رہیں۔ آپ کی درخواست میں خلاصہ بولی کے فرق |
| **اسکیما کی سختی** | بڑی میزوں پر ٹیبل کے ڈھانچے کو تبدیل کرنا سست اور خلل ڈالنے والا ہو سکتا ہے۔ نقل مکانی کے اوزار استعمال کریں؛ ڈیزائن سکیموں کو احتیاط سے پیشگی |
| **N+1 استفسار کا مسئلہ** | ORM سے تیار کردہ سوالات انتہائی ناکارہ ہو سکتے ہیں۔ پیچیدہ سوالات کے لیے حسب ضرورت SQL لکھیں؛ EXPLAIN NALYZE کے ساتھ پروفائل |
| **پیمانے کی پیچیدگی** | ایس کیو ایل ڈیٹا بیسز کو NoSQL | کے مقابلے افقی طور پر پیمانہ کرنا مشکل ہے۔ استعمال کے مخصوص کیسز کے لیے پڑھی ہوئی نقلیں، شارڈنگ، یا NoSQL پر غور کریں۔
---

## بنیادی تصورات
### رشتہ دار ماڈل
ڈیٹا کو **ٹیبلز** (تعلقات) میں محفوظ کیا جاتا ہے، جو **قطاروں** (ریکارڈز/ٹیپلز) اور **کالم** (صفات/فیلڈز) پر مشتمل ہوتا ہے۔ میزیں **کیز** کے ذریعے ایک دوسرے سے متعلق ہوسکتی ہیں۔
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

## نحوی بنیادی باتیں
### ڈیٹا بازیافت کرنا (SELECT)
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

### جمع
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

### ٹیبلز میں شامل ہونا
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

### ڈیٹا میں ترمیم کرنا
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

## اعلی درجے کی نحو اور نمونے۔
### ونڈو فنکشنز - گہرا غوطہ
ونڈو فنکشنز موجودہ قطار سے متعلق قطاروں کے ایک سیٹ پر کیلکولیشن کرتے ہیں — انہیں کسی ایک آؤٹ پٹ قطار میں سمیٹے بغیر جیسے GROUP BY کرتا ہے۔
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

### کامن ٹیبل ایکسپریشنز (CTEs) — ایڈوانسڈ استعمال
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

### JSON آپریشنز
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

### ذخیرہ شدہ طریقہ کار اور محرکات
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

## بنیادی خصوصیات میں گہرا غوطہ لگائیں۔
### استفسار کی اصلاح
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

**آپٹمائزیشن چیک لسٹ:**
| مسئلہ | علامت | درست کریں |
|---------|---------|------|
| بڑی میز پر ترتیب وار اسکین | `Seq Scan`وضاحت میں | مناسب انڈیکس شامل کریں |
| WHERE کالم پر انڈیکس غائب ہے | مکمل ٹیبل اسکین | فلٹر شدہ کالموں پر انڈیکس بنائیں |
| منتخب کریں * فضلہ | غیر ضروری کالموں کی بازیافت | صرف مطلوبہ کالم منتخب کریں |
| مضمر قسم کی تبدیلی | انڈیکس استعمال نہیں کیا گیا | موازنے میں قسمیں |
| انڈیکسڈ کالمز پر فنکشنز | انڈیکس ناقابل استعمال (نا قابل استعمال) | دوبارہ لکھیں:`WHERE date >= '2024-01-01'`نہیں`WHERE YEAR(date) = 2024`|
### اشاریہ سازی کی حکمت عملی
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

### ٹرانزیکشن آئسولیشن لیولز
| تنہائی کی سطح | گندا پڑھیں | غیر مکرر پڑھیں | پریت پڑھیں |
|-----------------|:---------:|:------:|:------------:|
| غیر ذمہ دار پڑھیں | جی ہاں | جی ہاں | جی ہاں |
| پرعزم پڑھیں | نہیں | جی ہاں | جی ہاں |
| دوبارہ پڑھنے کے قابل نہیں | نہیں | ہاں* |
| سیریلائزیبل | نہیں | نہیں | نہیں |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### معمول بنانا
| عام شکل | اصول | مثال کی خلاف ورزی |
|---------------|------|-------------------|
| **1NF** | جوہری اقدار، کوئی دہرانے والے گروپ نہیں | ایک کالم میں ایک سے زیادہ فونز کو "123,456" کے بطور اسٹور کرنا |
| **2NF** | 1NF + کوئی جزوی انحصار نہیں | آرڈر کی تفصیل آرڈر_آئی ڈی پر منحصر ہے لیکن پروڈکٹ_آئی ڈی پر نہیں۔
| **3NF** | 2NF + کوئی عبوری انحصار نہیں | ملازم محکمہ کا نام dept_id پر منحصر ہے، ملازم پر نہیں۔
---

## ڈیٹا بیس کی ساخت کی وضاحت
### میزیں بنانا
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

### ٹیبلز کو تبدیل کرنا
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### منتقلی کے اوزار
| ٹول | زبان/اسٹیک | نقطہ نظر |
|------|---------------|---------|
| **فلائی وے** | جاوا / جنرل | ایس کیو ایل پر مبنی ہجرت، سادہ نام دینے کا کنونشن |
| **لیکوبیس** | جاوا / جنرل | XML، YAML، JSON، یا SQL changelogs |
| **الیمبک** | Python (SQLAalchemy) | ماڈل کی تبدیلیوں سے خود بخود نقل مکانی پیدا کرتا ہے |
| **پریزما ہجرت** | Node.js / TypeScript | سکیما فرسٹ، ایس کیو ایل کو خود بخود تیار کرتا ہے۔
| **گولنگ-ہجرت** | جاؤ | SQL پر مبنی، اوپر/نیچے منتقلی کی حمایت کرتا ہے |
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

## ٹیسٹنگ
### ٹیسٹ ڈیٹا جنریشن
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

| فریم ورک | ڈیٹا بیس | تفصیل |
|------------|---------|------------|
| **pgTAP** | PostgreSQL | یونٹ ٹیسٹنگ فریم ورک |
| **tSQLt** | SQL سرور | ایس کیو ایل سرور کے لیے یونٹ ٹیسٹنگ |
| **utPLSQL** | اوریکل | اوریکل PL/SQL کے لیے ٹیسٹنگ فریم ورک |
---

## انٹرآپریبلٹی
### زبان کی پابندیاں
| انٹرفیس | زبان | تفصیل |
|------------|---------|------------|
| **JDBC** | جاوا | معیاری ڈیٹا بیس API |
| **ODBC** | متعدد | یونیورسل ڈیٹا بیس API |
| **psycopg2/3** | ازگر | PostgreSQL اڈاپٹر |
| **ڈیٹا بیس/sql** | جاؤ | ڈرائیور انٹرفیس کے ساتھ معیاری لائبریری |
| **sqlite3** | ازگر | بلٹ ان SQLite سپورٹ |
| **pg** | Node.js | PostgreSQL کلائنٹ |
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

## ڈیزائن پیٹرن
### پیٹرن 1: محور / کراس ٹیب
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### پیٹرن 2: ٹاپ-N فی گروپ
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### پیٹرن 3: خلا اور جزائر
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

### پیٹرن 4: آہستہ آہستہ بدلتے ہوئے طول و عرض (SCD قسم 2)
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

## کارکردگی: اشاریہ جات اور سوال کی منصوبہ بندی
### اشاریہ جات کیسے کام کرتے ہیں۔
ایک انڈیکس ڈیٹا کا ڈھانچہ ہے (عام طور پر ایک بی ٹری) جو ڈیٹا بیس کو پوری ٹیبل کو اسکین کیے بغیر قطاریں تلاش کرنے دیتا ہے۔
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| انڈیکس کی قسم | کے لیے بہترین | مثال |
|------------|---------|---------|
| **B-tree** (پہلے سے طے شدہ) | مساوات اور رینج کے سوالات | `WHERE age > 25 AND age < 35`|
| **ہیش** | صرف عین مطابق مساوات | `WHERE email = 'x@y.com'`|
| **GIN** | مکمل متن کی تلاش، صفوں، JSON | `WHERE description @@ 'search term'`|
| **GiST** | ہندسی/مقامی ڈیٹا | `WHERE location <-> point(x,y) < 1000`|
### سوالات کے منصوبے پڑھنا
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

## ایس کیو ایل بولیاں
| خصوصیت | PostgreSQL | MySQL | SQL سرور | SQLite |
|---------|------------|-------|------------|---------|
| آٹو انکریمنٹ | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| سٹرنگ concat | `\|\|`| `CONCAT()`| `+`یا`CONCAT()`| `\|\|`|
| تاریخ کے افعال | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| JSON سپورٹ | بہترین (`jsonb`) | اچھا (`JSON`) | اچھا (`JSON`) | بنیادی (`JSON1`) |
| مکمل متن کی تلاش | بلٹ ان (`tsvector`) | بلٹ ان | بلٹ ان | محدود |
| ونڈو کے افعال | جی ہاں | ہاں (8.0+) | جی ہاں | جی ہاں |
---

## تعیناتی۔
### ڈیٹا بیس کی تعیناتی کی حکمت عملی
| حکمت عملی | تفصیل | خطرے کی سطح |
|------------|------------|------------|
| **مائیگریشن فائلیں** | ورژن شدہ SQL اسکرپٹس ترتیب میں لاگو کم |
| **نیلا سبز تعینات** | دو ایک جیسے ڈیٹا بیس؛ ٹریفک کو تبدیل کریں | کم |
| **توسیع معاہدہ** | نیا کالم شامل کریں، دوہری لکھیں، منتقل کریں، پرانا چھوڑیں | کم |
| **براہ راست DDL** | ALTER TABLE کو براہ راست پروڈکشن پر چلانا | ہائی |
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

## SQL کب استعمال کریں۔
| منظر نامہ | کیوں SQL | متبادل |
|------------|---------|------------|
| پیچیدہ سوالات کے ساتھ متعلقہ ڈیٹا | اسی کے لیے ایس کیو ایل ڈیزائن کیا گیا ہے | --- |
| ٹرانزیکشنل انٹیگریٹی (ACID) | SQL ڈیٹا بیس مستقل مزاجی کی ضمانت | --- |
| رپورٹنگ اور تجزیات | جمع، ونڈو کے افعال، CTEs | بہت پیچیدہ تجزیہ کے لیے ازگر (پانڈا) |
| ڈیٹا کی سالمیت کی رکاوٹیں | غیر ملکی چابیاں، چیک کریں، منفرد، خالی نہیں | درخواست کی سطح کی توثیق (کمزور) |
| سادہ کلیدی قدر ذخیرہ | اس استعمال کے کیس کے لیے اوور کِل | Redis, DynamoDB |
| انتہائی غیر ساختہ ڈیٹا | سکیما کی سختی ایک مسئلہ ہے | MongoDB، دستاویز ڈیٹا بیس |
| بڑے پیمانے پر افقی اسکیلنگ | ایس کیو ایل ڈیٹا بیس کو شارڈ کرنا مشکل | Cassandra، DynamoDB، CockroachDB |
---

## مصنوعی سوال و جواب
### Q1:`WHERE`اور`HAVING`میں کیا فرق ہے؟
**A:**`WHERE`گروپ بندی سے پہلے قطاروں کو فلٹر کرتا ہے۔ `HAVING`جمع کرنے کے بعد گروپوں کو فلٹر کرتا ہے:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: ونڈو کے فنکشن گروپ BY سے کیسے مختلف ہیں؟
**A:** ونڈو فنکشنز ان کو گرائے بغیر قطاروں میں گنتی کرتے ہیں:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: میں سست سوالات کو کیسے بہتر بنا سکتا ہوں؟
**A:** اہم حکمت عملی:
- `WHERE`، `JOIN`، اور`ORDER BY`میں استعمال ہونے والے کالموں پر اشاریہ جات شامل کریں 
-`SELECT *`سے بچیں - صرف مطلوبہ کالم منتخب کریں۔
- استفسار کے منصوبوں کو پڑھنے کے لیے`EXPLAIN`/`EXPLAIN ANALYZE`استعمال کریں
- جہاں ممکن ہو سبکوریز کو JOIN سے تبدیل کریں۔
- پڑھنے کی اہلیت کے لیے CTEs کا استعمال کریں (عام طور پر کارکردگی کا کوئی جرمانہ نہیں)
- جہاں میں انڈیکس شدہ کالموں پر فنکشن سے بچیں:`WHERE date >= '2024-01-01'`استعمال کریں`WHERE YEAR(date) = 2024`نہیں
### Q4: CTEs کیا ہیں اور مجھے انہیں کب استعمال کرنا چاہیے؟
**A:** کامن ٹیبل ایکسپریشنز نامی عارضی نتائج سیٹ بناتے ہیں:
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

### Q5: میں NULL اقدار کو صحیح طریقے سے کیسے ہینڈل کروں؟
**A:** NULL نامعلوم کی نمائندگی کرتا ہے — یہ کسی بھی چیز کے برابر نہیں ہے، بشمول خود:
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: فی گروپ ٹاپ N تلاش کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
ہر محکمے میں 3 سب سے زیادہ تنخواہ پانے والے ملازمین تلاش کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
محکمہ کے ذریعہ تقسیم کردہ`ROW_NUMBER()`کے ساتھ ونڈو فنکشن استعمال کریں۔
**مرحلہ 3: نافذ کریں**```sql
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

**مرحلہ 4: تصدیق کریں**
چیک کریں کہ ہر شعبہ میں زیادہ سے زیادہ 3 قطاریں ہیں۔ اگر ضرورت ہو تو`DENSE_RANK()`کے ساتھ تعلقات کو سنبھالیں۔
### مسئلہ 2: سال بہ سال ترقی کی رپورٹ بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ماہانہ آمدنی اور سال بہ سال نمو کا حساب لگائیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
گروپ بندی کے لیے`DATE_TRUNC`اور پچھلے سال کے مقابلے کے لیے`LAG()`ونڈو فنکشن استعمال کریں۔
**مرحلہ 3: نافذ کریں**```sql
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

**مرحلہ 4: تصدیق کریں**
چیک کریں کہ پہلے 12 مہینے پچھلے سال کے لیے NULL ہیں۔ معلوم اعداد و شمار کے مقابلہ میں شرح نمو کی توثیق کریں۔
### مسئلہ 3: قطاروں کو کالموں میں محور کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
قطاروں سے کالموں میں اسٹیٹس شمار کو تبدیل کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
مشروط جمع استعمال کریں (`CASE``SUM`کے اندر)۔
**مرحلہ 3: نافذ کریں**```sql
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

**مرحلہ 4: توسیع کریں**
فی صد کالم اور چلنے والے ٹوٹل شامل کریں۔
---

## خلاصہ
ایس کیو ایل ایک 50 سال پرانی زبان ہے جو ضروری رہتی ہے۔ ہر ڈویلپر، ڈیٹا سائنسدان، اور تجزیہ کار کو اسے جاننے کی ضرورت ہے۔ بنیادی زبان معیاری اور پورٹیبل ہے۔ بولی کے اختلافات قابل انتظام ہیں۔ جدید ایس کیو ایل (ونڈو فنکشنز، CTEs، اور JSON سپورٹ کے ساتھ) ڈیٹا کے زیادہ تر کاموں کے لیے کافی تاثراتی ہے۔ کلیدی مہارتیں ہیں: موثر سوالات لکھنا، اشاریہ جات کو سمجھنا، استفسار کے منصوبوں کو پڑھنا، اور اچھے اسکیموں کو ڈیزائن کرنا۔ اگر آپ ڈیٹا کے ساتھ بالکل بھی کام کرتے ہیں تو ایس کیو ایل غیر گفت و شنید ہے۔