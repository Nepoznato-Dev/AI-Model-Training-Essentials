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
# এসকিউএল
এসকিউএল (স্ট্রাকচার্ড কোয়েরি ল্যাঙ্গুয়েজ) একটি ডোমেন-নির্দিষ্ট ভাষা যা রিলেশনাল ডাটাবেসে ডেটা পরিচালনা এবং অনুসন্ধানের জন্য ডিজাইন করা হয়েছে। প্রথম 1970-এর দশকে IBM-এ বিকশিত হয়েছিল এবং 1987 সালে প্রমিত, এসকিউএল অ্যাপ্লিকেশন এবং তাদের ডেটার মধ্যে প্রাথমিক ইন্টারফেস হিসাবে রয়ে গেছে। প্রতিটি প্রধান রিলেশনাল ডাটাবেস ম্যানেজমেন্ট সিস্টেম (RDBMS) — PostgreSQL, MySQL, SQL সার্ভার, Oracle, SQLite — তার ক্যোয়ারী ভাষা হিসেবে SQL ব্যবহার করে।
SQL একটি সাধারণ-উদ্দেশ্য প্রোগ্রামিং ভাষা নয়। আপনি SQL এ একটি ওয়েব অ্যাপ্লিকেশন লিখবেন না। কিন্তু যদি আপনার অ্যাপ্লিকেশান ডেটা সঞ্চয় করে — এবং প্রায় সব অ্যাপ্লিকেশানই করে — তাহলে SQL হল সেই ভাষা যা আপনি ডেটা পুনরুদ্ধার, রূপান্তর এবং পরিচালনা করতে ব্যবহার করেন৷ সাধারণ প্রোগ্রামিংয়ের পরে এটি তর্কযোগ্যভাবে সর্বজনীনভাবে দরকারী প্রযুক্তিগত দক্ষতা।
---

## কেন এসকিউএল গুরুত্বপূর্ণ
- **ইউনিভার্সাল**: প্রতিটি রিলেশনাল ডাটাবেস SQL বলে। একবার শিখুন, সর্বত্র ব্যবহার করুন।
- **ঘোষণামূলক**: আপনি *কী* ডেটা চান তা বর্ণনা করেন, *কীভাবে* পাবেন তা নয়। ডাটাবেস ইঞ্জিন এক্সিকিউশনকে অপ্টিমাইজ করে।
- **যেকোন ডেভেলপারের জন্য অপরিহার্য**: ব্যাকএন্ড, ডেটা সায়েন্স, DevOps, অ্যানালিটিক্স — সবগুলোর জন্য SQL প্রয়োজন।
- **শক্তিশালী**: উইন্ডো ফাংশন, CTE, সাবকোয়েরি এবং সমষ্টি আপনাকে কয়েকটি লাইনে জটিল যুক্তি প্রকাশ করতে দেয়।
- **পারফরম্যান্স**: একটি সঠিকভাবে সূচীকৃত ডাটাবেসে একটি সুলিখিত SQL কোয়েরি মিলিসেকেন্ডে লক্ষ লক্ষ সারি প্রক্রিয়া করতে পারে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **একটি সাধারণ-উদ্দেশ্যের ভাষা নয়** | SQL এ অ্যাপ্লিকেশন, API, বা অ্যালগরিদম তৈরি করা যাবে না | পাইথন, জাভা, জাভাস্ক্রিপ্ট ইত্যাদির সাথে একত্রিত করুন |
| **উপভাষা পার্থক্য** | বেমানান এক্সটেনশন সহ প্রতিটি RDBMS এর নিজস্ব SQL স্বাদ আছে | যেখানে সম্ভব ANSI SQL এ লেগে থাকুন; আপনার অ্যাপ্লিকেশনে বিমূর্ত উপভাষা পার্থক্য |
| **স্কিমা অনমনীয়তা** | বড় টেবিলে টেবিলের কাঠামো পরিবর্তন করা ধীর এবং বিঘ্নিত হতে পারে | মাইগ্রেশন টুল ব্যবহার করুন; ডিজাইন স্কিমা সাবধানে আগাম |
| **N+1 ক্যোয়ারী সমস্যা** | ORM-উত্পন্ন প্রশ্নগুলি অত্যন্ত অদক্ষ হতে পারে | জটিল প্রশ্নের জন্য কাস্টম SQL লিখুন; ব্যাখ্যা বিশ্লেষণ সহ প্রোফাইল |
| **স্কেলিং জটিলতা** | এসকিউএল ডাটাবেসগুলি NoSQL এর চেয়ে অনুভূমিকভাবে স্কেল করা কঠিন রিড রেপ্লিকা, শার্ডিং ব্যবহার করুন বা নির্দিষ্ট ব্যবহারের ক্ষেত্রে NoSQL বিবেচনা করুন |
---

## মূল ধারণা
### রিলেশনাল মডেল
ডেটা **টেবিল** (সম্পর্ক) এ সংরক্ষণ করা হয়, যা **সারি** (রেকর্ড/টুপল) এবং **কলাম** (বিশিষ্ট/ক্ষেত্র) নিয়ে গঠিত। টেবিল **কী** এর মাধ্যমে একে অপরের সাথে সম্পর্কিত হতে পারে।
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

## সিনট্যাক্স মৌলিক
### ডেটা পুনরুদ্ধার করা হচ্ছে (নির্বাচন করুন)
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

### সমষ্টি
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

### টেবিলে যোগদান
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

### ডেটা পরিবর্তন করা
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### উইন্ডো ফাংশন — ডিপ ডাইভ
উইন্ডো ফাংশনগুলি বর্তমান সারির সাথে সম্পর্কিত সারিগুলির একটি সেট জুড়ে গণনা সম্পাদন করে — GROUP BY এর মতো একটি একক আউটপুট সারিতে তাদের ভেঙে না দিয়ে।
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

### কমন টেবিল এক্সপ্রেশন (CTEs) — উন্নত ব্যবহার
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

### JSON অপারেশন
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

### সঞ্চিত পদ্ধতি এবং ট্রিগার
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

## মূল বৈশিষ্ট্যগুলিতে গভীরভাবে ডুব দিন
### ক্যোয়ারী অপ্টিমাইজেশান
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

**অপ্টিমাইজেশন চেকলিস্ট:**
| ইস্যু | উপসর্গ | ঠিক করুন |
|-------|---------|------|
| বড় টেবিলে অনুক্রমিক স্ক্যান | `Seq Scan`ব্যাখ্যা করুন | উপযুক্ত সূচক যোগ করুন |
| WHERE কলামে অনুপস্থিত সূচক | সম্পূর্ণ টেবিল স্ক্যান | ফিল্টার করা কলামে সূচক তৈরি করুন |
| SELECT * অপচয় | অপ্রয়োজনীয় কলাম আনা হচ্ছে | শুধুমাত্র প্রয়োজনীয় কলাম নির্বাচন করুন |
| অন্তর্নিহিত প্রকার রূপান্তর | সূচক ব্যবহার করা হয়নি | তুলনার ধরন |
| ইন্ডেক্সড কলামে ফাংশন | সূচক অব্যবহারযোগ্য (অ-সার্জেবল) | পুনরায় লিখুন:`WHERE date >= '2024-01-01'``WHERE YEAR(date) = 2024` নয় |
### ইন্ডেক্সিং কৌশল
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

### লেনদেন বিচ্ছিন্নতা স্তর
| বিচ্ছিন্নতা স্তর | নোংরা পড়া | অ-পুনরাবৃত্ত পঠন | ফ্যান্টম রিড |
|-----------------|:---------:|:------:|:------------:|
| নিঃসন্দেহে পড়ুন | হ্যাঁ | হ্যাঁ | হ্যাঁ |
| প্রতিশ্রুতিবদ্ধ পড়ুন | না | হ্যাঁ | হ্যাঁ |
| পুনরাবৃত্তিযোগ্য পঠন | না | না | হ্যাঁ* |
| ক্রমিক | না | না | না |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### স্বাভাবিকীকরণ
| সাধারণ ফর্ম | নিয়ম | উদাহরণ লঙ্ঘন |
|---------------|------|---------|
| **1NF** | পারমাণবিক মান, কোন পুনরাবৃত্ত গ্রুপ | "123,456" হিসাবে একটি কলামে একাধিক ফোন সংরক্ষণ করা হচ্ছে |
| **2NF** | 1NF + কোন আংশিক নির্ভরতা নেই | অর্ডারের বিশদ অর্ডার_আইডির উপর নির্ভর করে কিন্তু পণ্য_আইডি নয় |
| **3NF** | 2NF + কোন ট্রানজিটিভ নির্ভরতা নেই | কর্মচারী বিভাগের নাম dept_id এর উপর নির্ভর করে, কর্মচারী নয় |
---

## ডেটাবেস স্ট্রাকচার সংজ্ঞায়িত করা
### টেবিল তৈরি করা
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

### টেবিল পরিবর্তন
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### মাইগ্রেশন টুল
| টুল | ভাষা/স্ট্যাক | দৃষ্টিভঙ্গি |
|------|---------------|---------|
| **ফ্লাইওয়ে** | জাভা / সাধারণ | এসকিউএল-ভিত্তিক মাইগ্রেশন, সহজ নামকরণ কনভেনশন |
| **লিকুইবেস** | জাভা / সাধারণ | XML, YAML, JSON, বা SQL চেঞ্জলগ |
| **অ্যালেম্বিক** | পাইথন (SQLAlchemy) | মডেল পরিবর্তন থেকে স্বয়ংক্রিয়ভাবে মাইগ্রেশন তৈরি করে |
| **প্রিজমা মাইগ্রেট** | Node.js / TypeScript | স্কিমা-প্রথম, স্বয়ংক্রিয়ভাবে এসকিউএল তৈরি করে |
| **গোলাং-মাইগ্রেট** | যান | SQL-ভিত্তিক, আপ/ডাউন মাইগ্রেশন সমর্থন করে |
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

## পরীক্ষা
### টেস্ট ডেটা জেনারেশন
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

| ফ্রেমওয়ার্ক | ডাটাবেস | বর্ণনা |
|------------|----------|---------------|
| **pgTAP** | PostgreSQL | ইউনিট টেস্টিং ফ্রেমওয়ার্ক |
| **tSQLt** | SQL সার্ভার | SQL সার্ভারের জন্য ইউনিট টেস্টিং |
| **utPLSQL** | ওরাকল | Oracle PL/SQL এর জন্য টেস্টিং ফ্রেমওয়ার্ক |
---

## ইন্টারঅপারেবিলিটি
### ভাষা বাঁধাই
| ইন্টারফেস | ভাষা | বর্ণনা |
|------------|----------|---------------|
| **JDBC** | জাভা | স্ট্যান্ডার্ড ডাটাবেস API |
| **ODBC** | একাধিক | ইউনিভার্সাল ডাটাবেস API |
| **psycopg2/3** | পাইথন | PostgreSQL অ্যাডাপ্টার |
| **ডাটাবেস/sql** | যান | ড্রাইভার ইন্টারফেস সহ স্ট্যান্ডার্ড লাইব্রেরি |
| **sqlite3** | পাইথন | অন্তর্নির্মিত SQLite সমর্থন |
| **pg** | Node.js | PostgreSQL ক্লায়েন্ট |
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: পিভট/ক্রসট্যাব
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### প্যাটার্ন 2: টপ-এন প্রতি গ্রুপ
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### প্যাটার্ন 3: ফাঁক এবং দ্বীপপুঞ্জ
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

### প্যাটার্ন 4: ধীরে ধীরে পরিবর্তিত হচ্ছে (SCD টাইপ 2)
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

## কর্মক্ষমতা: সূচী এবং প্রশ্ন পরিকল্পনা
### কিভাবে ইনডেক্স কাজ করে
একটি সূচক হল একটি ডেটা স্ট্রাকচার (সাধারণত একটি বি-ট্রি) যা ডাটাবেসকে পুরো টেবিলটি স্ক্যান না করেই সারি খুঁজে পেতে দেয়।
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| সূচক প্রকার | জন্য সেরা | উদাহরণ |
|------------|----------|---------|
| **বি-ট্রি** (ডিফল্ট) | সমতা এবং পরিসীমা প্রশ্ন | `WHERE age > 25 AND age < 35`|
| **হ্যাশ** | সঠিক সমতা শুধুমাত্র | `WHERE email = 'x@y.com'`|
| **জিন** | পূর্ণ-পাঠ্য অনুসন্ধান, অ্যারে, JSON | `WHERE description @@ 'search term'`|
| **উদ্দেশ্য** | জ্যামিতিক/স্থানিক ডেটা | `WHERE location <-> point(x,y) < 1000`|
### কোয়েরি প্ল্যান পড়া
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

## এসকিউএল উপভাষা
| বৈশিষ্ট্য | PostgreSQL | মাইএসকিউএল | SQL সার্ভার | SQLite |
|---------|------------|-------|------------|---------|
| স্বয়ংক্রিয় বৃদ্ধি | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| স্ট্রিং কনক্যাট | `\|\|`| `CONCAT()`| `+`বা`CONCAT()`| `\|\|`|
| তারিখ ফাংশন | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| JSON সমর্থন | চমৎকার (`jsonb`) | ভাল (`JSON`) | ভাল (`JSON`) | মৌলিক (`JSON1`) |
| পূর্ণ-পাঠ্য অনুসন্ধান | অন্তর্নির্মিত (`tsvector`) | অন্তর্নির্মিত | অন্তর্নির্মিত | লিমিটেড |
| উইন্ডো ফাংশন | হ্যাঁ | হ্যাঁ (8.0+) | হ্যাঁ | হ্যাঁ |
---

## স্থাপনা
### ডাটাবেস স্থাপনার কৌশল
| কৌশল | বর্ণনা | ঝুঁকির স্তর |
|------------|-------------|------------|
| **মাইগ্রেশন ফাইল** | ক্রমানুসারে প্রয়োগ করা সংস্করণযুক্ত SQL স্ক্রিপ্ট | কম |
| **নীল-সবুজ স্থাপন** | দুটি অভিন্ন ডাটাবেস; ট্রাফিক পরিবর্তন করুন | কম |
| **সম্প্রসারণ-চুক্তি** | নতুন কলাম যোগ করুন, ডুয়েল-রাইট করুন, মাইগ্রেট করুন, পুরানো বাদ দিন | কম |
| **সরাসরি DDL** | সরাসরি উৎপাদনে ALTER TABLE চালানো হচ্ছে | উচ্চ |
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

## কখন SQL ব্যবহার করবেন
| দৃশ্যকল্প | কেন এসকিউএল | বিকল্প |
|------------|---------|---------------|
| জটিল প্রশ্নের সাথে রিলেশনাল ডেটা | যে SQL এর জন্য ডিজাইন করা হয়েছে | --- |
| লেনদেনের অখণ্ডতা (ACID) | এসকিউএল ডাটাবেস ধারাবাহিকতার গ্যারান্টি | --- |
| রিপোর্টিং এবং বিশ্লেষণ | সমষ্টি, উইন্ডো ফাংশন, CTEs | খুব জটিল বিশ্লেষণের জন্য পাইথন (পান্ডা) |
| ডেটা অখণ্ডতার সীমাবদ্ধতা | বিদেশী কী, চেক করুন, অনন্য, শূন্য নয় | আবেদন-স্তরের বৈধতা (দুর্বল) |
| সরল কী-মানের সঞ্চয়স্থান | এই ব্যবহারের ক্ষেত্রে ওভারকিল | Redis, DynamoDB |
| অত্যন্ত অসংগঠিত তথ্য | স্কিমা অনমনীয়তা একটি সমস্যা | MongoDB, নথি ডাটাবেস |
| ব্যাপক অনুভূমিক স্কেলিং | এসকিউএল ডাটাবেস শার্ড করা কঠিন | Cassandra, DynamoDB, CockroachDB |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1:`WHERE`এবং`HAVING`এর মধ্যে পার্থক্য কী?
**A:**`WHERE`গ্রুপ করার আগে সারি ফিল্টার করে; `HAVING`সমষ্টির পরে গোষ্ঠীগুলি ফিল্টার করে:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### প্রশ্ন 2: কিভাবে উইন্ডো ফাংশন GROUP BY থেকে আলাদা?
**A:** উইন্ডো ফাংশনগুলিকে ভেঙে না দিয়ে সারি জুড়ে গণনা করে:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### প্রশ্ন 3: আমি কীভাবে ধীরগতির প্রশ্নগুলি অপ্টিমাইজ করব?
**A:** মূল কৌশল:
- `WHERE`, `JOIN`, এবং `ORDER BY`-এ ব্যবহৃত কলামগুলিতে সূচী যোগ করুন 
-`SELECT *`এড়িয়ে চলুন - শুধুমাত্র প্রয়োজনীয় কলাম নির্বাচন করুন
- ক্যোয়ারী প্ল্যান পড়তে`EXPLAIN`/`EXPLAIN ANALYZE`ব্যবহার করুন
- যেখানে সম্ভব সাবকোয়ারিগুলিকে JOIN দিয়ে প্রতিস্থাপন করুন
- পঠনযোগ্যতার জন্য CTE ব্যবহার করুন (সাধারণত কোন পারফরম্যান্স পেনাল্টি নেই)
- যেখানে ইন্ডেক্স করা কলামগুলিতে ফাংশন এড়িয়ে চলুন:`WHERE date >= '2024-01-01'`ব্যবহার করুন`WHERE YEAR(date) = 2024`ব্যবহার করুন
### প্রশ্ন 4: CTE কি এবং আমার কখন ব্যবহার করা উচিত?
**A:** সাধারণ সারণী অভিব্যক্তিগুলি নামের অস্থায়ী ফলাফল সেট তৈরি করে:
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

### প্রশ্ন 5: আমি কিভাবে NULL মান সঠিকভাবে পরিচালনা করব?
**A:** NULL অজানা প্রতিনিধিত্ব করে — এটি নিজে সহ কোনো কিছুর সমান নয়:
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: প্রতি গ্রুপে শীর্ষ N খুঁজে বের করা
**ধাপ 1: সমস্যাটি বুঝুন**
প্রতিটি বিভাগে 3 জন সর্বোচ্চ বেতনপ্রাপ্ত কর্মচারী খুঁজুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
বিভাগ দ্বারা বিভক্ত`ROW_NUMBER()`সহ একটি উইন্ডো ফাংশন ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```sql
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

**পদক্ষেপ 4: যাচাই করুন**
প্রতিটি বিভাগে সর্বোচ্চ 3টি সারি রয়েছে তা পরীক্ষা করুন। প্রয়োজনে`DENSE_RANK()`এর সাথে সম্পর্কগুলি পরিচালনা করুন৷
### সমস্যা 2: বছরের পর বছর বৃদ্ধির প্রতিবেদন তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
মাসিক রাজস্ব এবং বছরের পর বছর বৃদ্ধির শতাংশ গণনা করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
গ্রুপ করার জন্য`DATE_TRUNC`এবং আগের বছরের তুলনার জন্য`LAG()`উইন্ডো ফাংশন ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```sql
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

**পদক্ষেপ 4: যাচাই করুন**
প্রথম 12 মাসে আগের বছরের জন্য NULL আছে চেক করুন। পরিচিত পরিসংখ্যানের বিপরীতে বৃদ্ধির শতাংশ যাচাই করুন।
### সমস্যা 3: কলামে সারি পিভট করা
**ধাপ 1: সমস্যাটি বুঝুন**
সারি থেকে কলামে স্থিতি গণনা রূপান্তর করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
শর্তসাপেক্ষ একত্রীকরণ ব্যবহার করুন (`SUM` এর ভিতরে `CASE`)।
**ধাপ 3: প্রয়োগ করুন**```sql
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

**ধাপ 4: প্রসারিত করুন**
শতাংশ কলাম এবং চলমান মোট যোগ করুন।
---

## সারাংশ
এসকিউএল একটি 50 বছর বয়সী ভাষা যা অপরিহার্য। প্রতিটি বিকাশকারী, ডেটা সায়েন্টিস্ট এবং বিশ্লেষকের এটি জানা দরকার। মূল ভাষা প্রমিত এবং বহনযোগ্য; উপভাষা পার্থক্য পরিচালনাযোগ্য. আধুনিক SQL (উইন্ডো ফাংশন, CTE, এবং JSON সমর্থন সহ) বেশিরভাগ ডেটা কাজের জন্য যথেষ্ট অভিব্যক্তিপূর্ণ। মূল দক্ষতাগুলি হল: দক্ষ প্রশ্ন লেখা, সূচী বোঝা, ক্যোয়ারী পরিকল্পনা পড়া এবং ভাল স্কিমা ডিজাইন করা। আপনি যদি ডেটা নিয়ে কাজ করেন তবে এসকিউএল অ-আলোচনাযোগ্য।