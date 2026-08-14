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
SQL (لغة الاستعلام الهيكلية) هي لغة خاصة بالمجال مصممة لإدارة البيانات والاستعلام عنها في قواعد البيانات العلائقية. تم تطوير SQL لأول مرة في IBM في السبعينيات وتم توحيده في عام 1987، ويظل SQL هو الواجهة الأساسية بين التطبيقات وبياناتها. كل نظام رئيسي لإدارة قواعد البيانات العلائقية (RDBMS) - PostgreSQL، وMySQL، وSQL Server، وOracle، وSQLite - يستخدم SQL كلغة استعلام خاصة به.
SQL ليست لغة برمجة للأغراض العامة. لن تكتب تطبيق ويب في SQL. ولكن إذا كان تطبيقك يقوم بتخزين البيانات - وجميع التطبيقات تقريبًا تقوم بذلك - فإن لغة SQL هي اللغة التي تستخدمها لاسترداد تلك البيانات وتحويلها وإدارتها. يمكن القول إنها المهارة التقنية الأكثر فائدة عالميًا بعد البرمجة العامة.
---

## لماذا يهم SQL
- **عالمي**: كل قاعدة بيانات علائقية تتحدث لغة SQL. تعلمها مرة واحدة، واستخدمها في كل مكان.
- **التصريح**: أنت تصف *ما* البيانات التي تريدها، وليس *كيفية* الحصول عليها. يعمل محرك قاعدة البيانات على تحسين التنفيذ.
- **ضروري لأي مطور**: الواجهة الخلفية، وعلوم البيانات، وDevOps، والتحليلات — كلها تتطلب SQL.
- **قوية**: تتيح لك وظائف النافذة وCTEs والاستعلامات الفرعية والتجميعات التعبير عن المنطق المعقد في بضعة أسطر.
- **الأداء**: يمكن لاستعلام SQL مكتوب بشكل جيد على قاعدة بيانات مفهرسة بشكل صحيح معالجة ملايين الصفوف بالمللي ثانية.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** ليست لغة للأغراض العامة ** | لا يمكن إنشاء تطبيقات أو واجهات برمجة تطبيقات أو خوارزميات في SQL | ادمجها مع Python وJava وJavaScript وما إلى ذلك |
| **اختلافات اللهجات** | كل RDBMS له نكهة SQL الخاصة به مع ملحقات غير متوافقة | التزم بـ ANSI SQL حيثما أمكن ذلك؛ اختلافات اللهجة المجردة في تطبيقك |
| **صلابة المخطط** | يمكن أن يكون تغيير بنية الجدول على الجداول الكبيرة بطيئًا ومزعجًا | استخدام أدوات الترحيل؛ مخططات التصميم بعناية مقدما |
| **مشكلة استعلام N+1** | يمكن أن تكون الاستعلامات التي تم إنشاؤها بواسطة ORM غير فعالة للغاية | كتابة SQL مخصصة للاستعلامات المعقدة؛ الملف الشخصي مع شرح التحليل |
| **تعقيد القياس** | من الصعب توسيع نطاق قواعد بيانات SQL أفقيًا مقارنة بـ NoSQL | استخدم قراءة النسخ المتماثلة أو التقسيم أو فكر في NoSQL لحالات استخدام محددة |
---

## المفاهيم الأساسية
### النموذج العلائقي
يتم تخزين البيانات في **الجداول** (العلاقات)، والتي تتكون من **الصفوف** (السجلات/الصفوف) و **الأعمدة** (السمات/الحقول). يمكن ربط الجداول ببعضها البعض من خلال **المفاتيح**.
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

## أساسيات بناء الجملة
### استرداد البيانات (SELECT)
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

### التجميع
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

### الانضمام إلى الجداول
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

### تعديل البيانات
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

## بناء الجملة والأنماط المتقدمة
### وظائف النافذة — نظرة عميقة
تقوم وظائف النافذة بإجراء عمليات حسابية عبر مجموعة من الصفوف المرتبطة بالصف الحالي - دون طيها في صف إخراج واحد كما تفعل GROUP BY.
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

### تعبيرات الجدول الشائعة (CTEs) — الاستخدام المتقدم
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

### عمليات JSON
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

### الإجراءات والمشغلات المخزنة
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

## الغوص العميق في الميزات الأساسية
### تحسين الاستعلام
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

**قائمة التحقق من التحسين:**
| العدد | العَرَض | إصلاح |
|-------|---------|-----|
| مسح متسلسل على طاولة كبيرة | `Seq Scan`في الشرح | أضف الفهرس المناسب |
| فهرس مفقود في عمود WHERE | مسح الجدول كاملا | إنشاء فهرس على الأعمدة التي تمت تصفيتها |
| اختر * النفايات | جلب الأعمدة غير الضرورية | حدد الأعمدة المطلوبة فقط |
| تحويل النوع الضمني | الفهرس غير مستخدم | أنواع المطابقة في المقارنات |
| وظائف على الأعمدة المفهرسة | الفهرس غير قابل للاستخدام (غير قابل للطرح) | أعد الكتابة:`WHERE date >= '2024-01-01'`وليس`WHERE YEAR(date) = 2024`|
### استراتيجيات الفهرسة
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

### مستويات عزل المعاملات
| مستوى العزل | قراءة قذرة | قراءة غير قابلة للتكرار | القراءة الوهمية |
|-----------------|:----------:|:-------------------:|:------------:|
| قراءة غير ملتزم بها | نعم | نعم | نعم |
| قراءة ملتزمة | لا | نعم | نعم |
| قراءة متكررة | لا | لا | نعم* |
| قابل للتسلسل | لا | لا | لا |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### التطبيع
| النموذج العادي | القاعدة | مثال على المخالفة |
|-------------|-----|------------------|
| **1NF** | القيم الذرية، لا توجد مجموعات مكررة | تخزين هواتف متعددة في عمود واحد كـ "123,456" |
| **2NF** | 1NF + لا توجد تبعيات جزئية | تعتمد تفاصيل الطلب على order_id وليس على Product_id |
| **3NF** | 2NF + لا توجد تبعيات متعدية | يعتمد اسم قسم الموظف على dept_id، وليس على الموظف |
---

## تعريف بنية قاعدة البيانات
### إنشاء الجداول
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

### تغيير الجداول
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## تكوين المشروع ونظام البناء
### أدوات الترحيل
| أداة | اللغة/المكدس | النهج |
|------|--------------|----------|
| **مسار الهجرة** | جافا / عام | عمليات الترحيل المستندة إلى SQL، اصطلاح تسمية بسيط |
| **ليكويبيز** | جافا / عام | سجلات تغيير XML أو YAML أو JSON أو SQL |
| **الإلبيك** | بايثون (SQLAlchemy) | يُنشئ عمليات الترحيل تلقائيًا من تغييرات النموذج |
| **ترحيل بريزما** | Node.js / تايب سكريبت | المخطط أولاً، يقوم بإنشاء SQL | تلقائيًا
| **جولانج-هاجر** | اذهب | يعتمد على SQL، ويدعم عمليات الترحيل لأعلى/لأسفل |
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

## الاختبار
### اختبار توليد البيانات
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

| الإطار | قاعدة بيانات | الوصف |
|-----------|---------|-------------|
| **ص.تاب** | بوستجرس كيو ال | إطار اختبار الوحدة |
| **تسكلت** | خادم SQL | اختبار الوحدة لـ SQL Server |
| **utPLSQL** | أوراكل | إطار اختبار لـ Oracle PL/SQL |
---

## إمكانية التشغيل البيني
### روابط اللغة
| الواجهة | اللغة | الوصف |
|-----------|---------|-------------|
| **JDBC** | جافا | واجهة برمجة تطبيقات قاعدة البيانات القياسية |
| **ODBC** | متعددة | قاعدة بيانات عالمية API |
| **psycopg2/3** | بايثون | محول PostgreSQL |
| ** قاعدة البيانات / SQL ** | اذهب | مكتبة قياسية مع واجهة برنامج التشغيل |
| **سكليت3** | بايثون | دعم SQLite المدمج |
| **صفحة** | نود.جي إس | عميل PostgreSQL |
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

## أنماط التصميم
### النموذج 1: محوري / جدولي
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### النمط 2: Top-N لكل مجموعة
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### النموذج 3: الفجوات والجزر
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

### النموذج 4: الأبعاد المتغيرة ببطء (SCD النوع 2)
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

## الأداء: الفهارس وتخطيط الاستعلام
### كيف تعمل الفهارس
الفهرس عبارة عن بنية بيانات (عادةً ما تكون شجرة B) تتيح لقاعدة البيانات العثور على الصفوف دون فحص الجدول بأكمله.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| نوع الفهرس | الأفضل لـ | مثال |
|-----------|---------|---------|
| **B-tree** (افتراضي) | استعلامات المساواة والمدى | `WHERE age > 25 AND age < 35`|
| ** التجزئة ** | المساواة التامة فقط | `WHERE email = 'x@y.com'`|
| **جين** | البحث عن النص الكامل، المصفوفات، JSON | `WHERE description @@ 'search term'`|
| **GiST** | بيانات هندسية/مكانية | `WHERE location <-> point(x,y) < 1000`|
### قراءة خطط الاستعلام
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

## لهجات SQL
| ميزة | بوستجرس كيو ال | ماي إس كيو إل | خادم SQL | سكليتي |
|---------|----------|------|------------|--------|
| الزيادة التلقائية | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| سلسلة متسلسلة | `\|\|`| `CONCAT()`| `+`أو`CONCAT()`| `\|\|`|
| وظائف التاريخ | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| دعم JSON | ممتاز (`jsonb`) | جيد (`JSON`) | جيد (`JSON`) | الأساسية (`JSON1`) |
| البحث عن النص الكامل | مدمج (`tsvector`) | مدمج | مدمج | محدودة |
| وظائف النافذة | نعم | نعم (8.0+) | نعم | نعم |
---

## النشر
### استراتيجيات نشر قاعدة البيانات
| استراتيجية | الوصف | مستوى المخاطر |
|----------|------------|------------|
| **ملفات الهجرة** | تم تطبيق البرامج النصية SQL ذات الإصدار بالترتيب | منخفض |
| ** نشر الأزرق والأخضر ** | قاعدتي بيانات متطابقتين؛ تبديل حركة المرور | منخفض |
| **توسيع العقد** | إضافة عمود جديد، كتابة مزدوجة، ترحيل، إسقاط القديم | منخفض |
| ** DDL المباشر ** | تشغيل ALTER TABLE مباشرة على الإنتاج | عالية |
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

## متى يجب استخدام SQL
| السيناريو | لماذا SQL | البديل |
|----------|--------|-------------|
| البيانات العلائقية مع الاستعلامات المعقدة | هذا هو ما تم تصميم SQL من أجله | --- |
| سلامة المعاملات (ACID) | قواعد بيانات SQL تضمن الاتساق | --- |
| التقارير والتحليلات | التجميعات، وظائف النافذة، CTEs | بايثون (Pandas) للتحليل المعقد للغاية |
| قيود سلامة البيانات | المفاتيح الخارجية، تحقق، فريدة، وليست فارغة | التحقق من الصحة على مستوى التطبيق (أضعف) |
| تخزين بسيط للقيمة الرئيسية | مبالغة في حالة الاستخدام هذه | ريديس، دينامو دي بي |
| بيانات غير منظمة للغاية | صلابة المخطط مشكلة | MongoDB، قواعد بيانات المستندات |
| تحجيم أفقي هائل | من الصعب تقسيم قواعد بيانات SQL | كاساندرا، دينامو دي بي، كوكروتش دي بي |
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين`WHERE`و`HAVING`؟
**A:** يقوم`WHERE`بتصفية الصفوف قبل التجميع؛  يقوم`HAVING`بتصفية المجموعات بعد التجميع:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### السؤال الثاني: كيف تختلف وظائف النافذة عن GROUP BY؟
**أ:** تحسب وظائف النافذة عبر الصفوف دون طيها:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### س3: كيف يمكنني تحسين الاستعلامات البطيئة؟
**أ:** الاستراتيجيات الرئيسية:
- إضافة فهارس على الأعمدة المستخدمة في`WHERE`و`JOIN`و`ORDER BY`
- تجنب`SELECT *`- حدد الأعمدة المطلوبة فقط
- استخدم`EXPLAIN`/`EXPLAIN ANALYZE`لقراءة خطط الاستعلام
- استبدال الاستعلامات الفرعية بـ JOINs حيثما أمكن ذلك
- استخدم CTEs لسهولة القراءة (عادة لا توجد عقوبة على الأداء)
- تجنب الوظائف في الأعمدة المفهرسة في المكان: استخدم`WHERE date >= '2024-01-01'`وليس `WHERE YEAR(date) = 2024`
### س4: ما هي CTEs ومتى يجب أن أستخدمها؟
**أ:** تنشئ تعبيرات الجدول الشائعة مجموعات نتائج مؤقتة مسماة:
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

### س5: كيف أتعامل مع القيم الخالية بشكل صحيح؟
**A:** يمثل NULL غير معروف — فهو لا يساوي أي شيء، بما في ذلك نفسه:
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة 1: العثور على أعلى N لكل مجموعة
**الخطوة الأولى: فهم المشكلة**
ابحث عن أعلى 3 موظفين أجرًا في كل قسم.
**الخطوة 2: تحديد النهج**
استخدم وظيفة النافذة مع تقسيم`ROW_NUMBER()`حسب القسم.
**الخطوة 3: التنفيذ**```sql
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

**الخطوة 4: التحقق**
تأكد من أن كل قسم يحتوي على 3 صفوف على الأكثر. تعامل مع الروابط باستخدام`DENSE_RANK()`إذا لزم الأمر.
### المشكلة الثانية: إنشاء تقرير النمو على أساس سنوي
**الخطوة الأولى: فهم المشكلة**
حساب الإيرادات الشهرية ونسبة النمو على أساس سنوي.
**الخطوة 2: تحديد النهج**
استخدم`DATE_TRUNC`للتجميع ووظيفة النافذة`LAG()`لمقارنة العام السابق.
**الخطوة 3: التنفيذ**```sql
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

**الخطوة 4: التحقق**
تحقق من أن أول 12 شهرًا خالية من العام السابق. التحقق من صحة نسب النمو مقابل الأرقام المعروفة.
### المشكلة 3: تحويل الصفوف إلى الأعمدة
**الخطوة الأولى: فهم المشكلة**
تحويل أعداد الحالة من الصفوف إلى الأعمدة.
**الخطوة 2: تحديد النهج**
استخدم التجميع الشرطي (`CASE` داخل `SUM`).
**الخطوة 3: التنفيذ**```sql
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

**الخطوة 4: تمديد**
إضافة أعمدة النسبة المئوية والإجماليات الجارية.
---

## ملخص
SQL هي لغة عمرها 50 عامًا ولا تزال ضرورية. يحتاج كل مطور وعالم بيانات ومحلل إلى معرفتها. اللغة الأساسية موحدة ومحمولة؛ يمكن التحكم في اختلافات اللهجة. تعد لغة SQL الحديثة (مع وظائف النافذة وCTEs ودعم JSON) معبرة بدرجة كافية لمعظم مهام البيانات. المهارات الأساسية هي: كتابة استعلامات فعالة، وفهم الفهارس، وقراءة خطط الاستعلام، وتصميم مخططات جيدة. إذا كنت تتعامل مع البيانات على الإطلاق، فإن لغة SQL غير قابلة للتفاوض.