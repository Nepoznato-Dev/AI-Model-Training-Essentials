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

#เอสแอลแอล
SQL (Structured Query Language) เป็นภาษาเฉพาะโดเมนที่ออกแบบมาเพื่อการจัดการและการสืบค้นข้อมูลในฐานข้อมูลเชิงสัมพันธ์ พัฒนาขึ้นครั้งแรกที่ IBM ในปี 1970 และได้รับมาตรฐานในปี 1987 SQL ยังคงเป็นอินเทอร์เฟซหลักระหว่างแอปพลิเคชันและข้อมูล ระบบจัดการฐานข้อมูลเชิงสัมพันธ์หลักทุกระบบ (RDBMS) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — ใช้ SQL เป็นภาษาในการสืบค้น
SQL ไม่ใช่ภาษาโปรแกรมทั่วไป คุณจะไม่เขียนเว็บแอปพลิเคชันใน SQL แต่ถ้าแอปพลิเคชันของคุณจัดเก็บข้อมูล และแอปพลิเคชันเกือบทั้งหมดเก็บข้อมูลไว้ SQL ก็เป็นภาษาที่คุณใช้เพื่อดึงข้อมูล แปลง และจัดการข้อมูลนั้น ถือเป็นทักษะทางเทคนิคที่มีประโยชน์ในระดับสากลมากที่สุดหลังจากการเขียนโปรแกรมทั่วไป
---

## ทำไม SQL จึงมีความสำคัญ
- **สากล**: ทุกฐานข้อมูลเชิงสัมพันธ์พูด SQL เรียนรู้เพียงครั้งเดียว นำไปใช้ได้ทุกที่
- **ประกาศ**: คุณอธิบายว่า *ข้อมูลอะไร* ที่คุณต้องการ ไม่ใช่ *วิธี* เพื่อให้ได้มา เอ็นจิ้นฐานข้อมูลปรับการดำเนินการให้เหมาะสม
- **จำเป็นสำหรับนักพัฒนาทุกคน**: แบ็กเอนด์, วิทยาศาสตร์ข้อมูล, DevOps, การวิเคราะห์ — ทั้งหมดนี้ต้องใช้ SQL
- **ทรงพลัง**: ฟังก์ชันหน้าต่าง, CTE, แบบสอบถามย่อย และการรวมกลุ่มช่วยให้คุณแสดงตรรกะที่ซับซ้อนได้ในไม่กี่บรรทัด
- **ประสิทธิภาพ**: การสืบค้น SQL ที่เขียนอย่างดีบนฐานข้อมูลที่ได้รับการจัดทำดัชนีอย่างเหมาะสมสามารถประมวลผลแถวนับล้านแถวในหน่วยมิลลิวินาที
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ไม่ใช่ภาษาวัตถุประสงค์ทั่วไป** | ไม่สามารถสร้างแอปพลิเคชัน API หรืออัลกอริทึมใน SQL | รวมกับ Python, Java, JavaScript ฯลฯ |
| **ความแตกต่างของภาษาถิ่น** | RDBMS แต่ละตัวมีรสชาติ SQL ของตัวเองพร้อมส่วนขยายที่เข้ากันไม่ได้ | ยึดติดกับ ANSI SQL หากเป็นไปได้ ความแตกต่างทางภาษาเชิงนามธรรมในแอปพลิเคชันของคุณ |
| **ความแข็งแกร่งของสคีมา** | การเปลี่ยนโครงสร้างตารางบนโต๊ะขนาดใหญ่อาจทำได้ช้าและก่อกวน | ใช้เครื่องมือการโยกย้าย ออกแบบสคีมาอย่างระมัดระวังล่วงหน้า |
| **ปัญหาแบบสอบถาม N+1** | ข้อความค้นหาที่สร้างโดย ORM อาจไม่มีประสิทธิภาพอย่างยิ่ง | เขียน SQL แบบกำหนดเองสำหรับการสืบค้นที่ซับซ้อน โปรไฟล์พร้อมอธิบายการวิเคราะห์ |
| **ความซับซ้อนในการปรับขนาด** | ฐานข้อมูล SQL นั้นปรับขนาดในแนวนอนได้ยากกว่า NoSQL | ใช้การจำลองการอ่าน การแบ่งส่วน หรือพิจารณา NoSQL สำหรับกรณีการใช้งานเฉพาะ |
---

## แนวคิดหลัก
### โมเดลเชิงสัมพันธ์
ข้อมูลถูกจัดเก็บไว้ใน **ตาราง** (ความสัมพันธ์) ซึ่งประกอบด้วย **แถว** (บันทึก/สิ่งอันดับ) และ **คอลัมน์** (แอตทริบิวต์/ฟิลด์) ตารางสามารถเชื่อมโยงถึงกันผ่าน **คีย์**
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

## พื้นฐานไวยากรณ์
### การดึงข้อมูล (SELECT)
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

### การรวมกลุ่ม
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

### เข้าร่วมตาราง
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

### การแก้ไขข้อมูล
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ฟังก์ชั่นหน้าต่าง — เจาะลึก
ฟังก์ชันหน้าต่างจะทำการคำนวณข้ามชุดแถวที่เกี่ยวข้องกับแถวปัจจุบัน โดยไม่ยุบแถวเหล่านั้นให้เป็นแถวเอาต์พุตเดี่ยวเหมือนที่ GROUP BY ทำ
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

### Common Table Expressions (CTE) — การใช้งานขั้นสูง
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

### การดำเนินงาน JSON
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

### ขั้นตอนที่เก็บไว้และทริกเกอร์
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

## เจาะลึกคุณสมบัติหลัก
### การเพิ่มประสิทธิภาพแบบสอบถาม
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

**รายการตรวจสอบการเพิ่มประสิทธิภาพ:**
| ปัญหา | อาการ | แก้ไข |
|-------|---------|-----|
| การสแกนตามลำดับบนโต๊ะขนาดใหญ่ | `Seq Scan`ในอธิบาย | เพิ่มดัชนีที่เหมาะสม |
| ไม่มีดัชนีในคอลัมน์ WHERE | สแกนเต็มตาราง | สร้างดัชนีในคอลัมน์ที่ถูกกรอง |
| SELECT * เสีย | กำลังดึงคอลัมน์ที่ไม่จำเป็น | เลือกเฉพาะคอลัมน์ที่ต้องการ |
| การแปลงประเภทโดยนัย | ไม่ได้ใช้ดัชนี | ประเภทการจับคู่ในการเปรียบเทียบ |
| ฟังก์ชั่นในคอลัมน์ที่จัดทำดัชนี | ดัชนีใช้ไม่ได้ (ไม่ใช่ sargable) | เขียนใหม่:`WHERE date >= '2024-01-01'`ไม่ใช่`WHERE YEAR(date) = 2024`|
### กลยุทธ์การจัดทำดัชนี
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

### ระดับการแยกธุรกรรม
| ระดับการแยก | อ่านสกปรก | อ่านซ้ำไม่ได้ | ผีอ่าน |
|-----------------|:----------:|:-------------------:|:------------:|
| อ่านไม่มีข้อผูกมัด | ใช่ | ใช่ | ใช่ |
| อ่านมุ่งมั่น | ไม่ | ใช่ | ใช่ |
| อ่านซ้ำได้ | ไม่ | ไม่ | ใช่* |
| เรียงลำดับได้ | ไม่ | ไม่ | ไม่ |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### การทำให้เป็นมาตรฐาน
| แบบฟอร์มปกติ | กฎ | ตัวอย่างการละเมิด |
|-----------------|-|-------------------|
| **1NF** | ค่าอะตอมมิก ไม่มีหมู่ซ้ำ | การจัดเก็บโทรศัพท์หลายเครื่องในคอลัมน์เดียวเป็น "123,456" |
| **2NF** | 1NF + ไม่มีการพึ่งพาบางส่วน | รายละเอียดคำสั่งซื้อขึ้นอยู่กับ order_id แต่ไม่ใช่ product_id |
| **3NF** | 2NF + ไม่มีการพึ่งพาสกรรมกริยา | ชื่อแผนกพนักงานขึ้นอยู่กับ dept_id ไม่ใช่พนักงาน |
---

## การกำหนดโครงสร้างฐานข้อมูล
### การสร้างตาราง
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

### การเปลี่ยนแปลงตาราง
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## การกำหนดค่าโครงการ & ระบบการสร้าง
### เครื่องมือการย้ายข้อมูล
| เครื่องมือ | ภาษา/สแต็ก | วิธีการ |
|------|---------------|----------|
| **ทางบิน** | ชวา / ทั่วไป | การโยกย้ายที่ใช้ SQL แบบแผนการตั้งชื่ออย่างง่าย |
| **ลิควิเบส** | ชวา / ทั่วไป | บันทึกการเปลี่ยนแปลง XML, YAML, JSON หรือ SQL |
| **แอลเลมบิก** | Python (SQLAlchemy) | สร้างการโยกย้ายอัตโนมัติจากการเปลี่ยนแปลงโมเดล |
| **พริสม่าไมเกรต** | Node.js / TypeScript | Schema-first สร้าง SQL | โดยอัตโนมัติ
| **golang-migrate** | ไป | อิง SQL รองรับการโยกย้ายขึ้น/ลง |
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

## การทดสอบ
### ทดสอบการสร้างข้อมูล
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

| กรอบ | ฐานข้อมูล | คำอธิบาย |
|----------|----------|-------------|
| **pgTAP** | PostgreSQL | กรอบการทดสอบหน่วย |
| **tSQLt** | เซิร์ฟเวอร์ SQL | การทดสอบหน่วยสำหรับ SQL Server |
| **utPLSQL** | ออราเคิล | กรอบการทดสอบสำหรับ Oracle PL/SQL |
---

## การทำงานร่วมกัน
### การผูกภาษา
| อินเตอร์เฟซ | ภาษา | คำอธิบาย |
|----------|----------|-------------|
| **เจดีบีซี** | ชวา | API ฐานข้อมูลมาตรฐาน |
| **ODBC** | หลาย | API ฐานข้อมูลสากล |
| **psycopg2/3** | หลาม | อะแดปเตอร์ PostgreSQL |
| **ฐานข้อมูล/sql** | ไป | ไลบรารีมาตรฐานพร้อมอินเทอร์เฟซไดรเวอร์ |
| **sqlite3** | หลาม | รองรับ SQLite ในตัว |
| **หน้า** | โหนด js | ไคลเอนต์ PostgreSQL |
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

## รูปแบบการออกแบบ
### รูปแบบ 1: Pivot / Crosstab
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### รูปแบบ 2: Top-N ต่อกลุ่ม
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### รูปแบบ 3: ช่องว่างและหมู่เกาะ
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

### รูปแบบ 4: ขนาดที่เปลี่ยนแปลงอย่างช้าๆ (SCD ประเภท 2)
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

## ประสิทธิภาพ: ดัชนีและการวางแผนแบบสอบถาม
### ดัชนีทำงานอย่างไร
ดัชนีคือโครงสร้างข้อมูล (โดยปกติจะเป็น B-tree) ที่ช่วยให้ฐานข้อมูลค้นหาแถวโดยไม่ต้องสแกนทั้งตาราง
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| ประเภทดัชนี | ดีที่สุดสำหรับ | ตัวอย่าง |
|----------|----------|---------|
| **B-tree** (ค่าเริ่มต้น) | แบบสอบถามความเท่าเทียมกันและช่วง | `WHERE age > 25 AND age < 35`|
| **แฮช** | ความเท่าเทียมกันที่แน่นอนเท่านั้น | `WHERE email = 'x@y.com'`|
| **จิน** | การค้นหาข้อความแบบเต็ม อาร์เรย์ JSON | `WHERE description @@ 'search term'`|
| **จีเอสที** | ข้อมูลเรขาคณิต/เชิงพื้นที่ | `WHERE location <-> point(x,y) < 1000`|
### แผนการอ่านแบบสอบถาม
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

## ภาษาถิ่น SQL
| คุณสมบัติ | PostgreSQL | MySQL | เซิร์ฟเวอร์ SQL | SQLite |
|---------|-----------|--------|------------|--------|
| เพิ่มอัตโนมัติ | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| เชื่อมต่อสตริง | `\|\|`| `CONCAT()`| `+`หรือ`CONCAT()`| `\|\|`|
| ฟังก์ชันวันที่ | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| รองรับ JSON | ยอดเยี่ยม (`jsonb`) | ดี (`JSON`) | ดี (`JSON`) | พื้นฐาน (`JSON1`) |
| ค้นหาข้อความแบบเต็ม | บิวท์อิน (`tsvector`) | ในตัว | ในตัว | จำกัด |
| ฟังก์ชั่นหน้าต่าง | ใช่ | ใช่ (8.0+) | ใช่ | ใช่ |
---

## การปรับใช้
### กลยุทธ์การปรับใช้ฐานข้อมูล
| กลยุทธ์ | คำอธิบาย | ระดับความเสี่ยง |
|----------|-------------|------------|
| **ไฟล์การโยกย้าย** | สคริปต์ SQL เวอร์ชันที่ใช้ตามลำดับ | ต่ำ |
| **ปรับใช้สีน้ำเงิน-เขียว** | สองฐานข้อมูลที่เหมือนกัน สลับการรับส่งข้อมูล | ต่ำ |
| **ขยายสัญญา** | เพิ่มคอลัมน์ใหม่ เขียนคู่ ย้าย ปล่อยเก่า | ต่ำ |
| **DDL โดยตรง** | การรัน ALTER TABLE โดยตรงกับการผลิต | สูง |
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

## เมื่อใดจึงควรใช้ SQL
| สถานการณ์ | ทำไมต้อง SQL | ทางเลือก |
|----------|---------|-------------|
| ข้อมูลเชิงสัมพันธ์ที่มีการสืบค้นที่ซับซ้อน | นั่นคือสิ่งที่ SQL ได้รับการออกแบบมาสำหรับ | --- |
| ความสมบูรณ์ของธุรกรรม (ACID) | ฐานข้อมูล SQL รับประกันความสอดคล้อง | --- |
| การรายงานและการวิเคราะห์ | การรวมตัว ฟังก์ชันหน้าต่าง CTEs | Python (Pandas) สำหรับการวิเคราะห์ที่ซับซ้อนมาก |
| ข้อจำกัดด้านความสมบูรณ์ของข้อมูล | คีย์ต่างประเทศ ตรวจสอบ ไม่ซ้ำกัน ไม่ใช่ NULL | การตรวจสอบระดับแอปพลิเคชัน (อ่อนแอกว่า) |
| การจัดเก็บคีย์-ค่าอย่างง่าย | เกินกำลังสำหรับกรณีการใช้งานนี้ | เรดดิส, DynamoDB |
| ข้อมูลที่ไม่มีโครงสร้างสูง | ความแข็งแกร่งของสคีมาเป็นปัญหา | MongoDB ฐานข้อมูลเอกสาร |
| มาตราส่วนแนวนอนขนาดใหญ่ | ฐานข้อมูล SQL ยากที่จะแยกส่วน | คาสซานดรา, DynamoDB, CockroachDB |
---

## คำถามและคำตอบสังเคราะห์
### Q1: อะไรคือความแตกต่างระหว่าง`WHERE`และ`HAVING`?
**A:**`WHERE`กรองแถวก่อนจัดกลุ่ม `HAVING`กรองกลุ่มหลังจากการรวมกลุ่ม:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: ฟังก์ชันหน้าต่างแตกต่างจาก GROUP BY อย่างไร
**A:** ฟังก์ชันหน้าต่างคำนวณข้ามแถวโดยไม่ยุบ:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: ฉันจะเพิ่มประสิทธิภาพการสืบค้นที่ช้าได้อย่างไร
**ก:** กลยุทธ์หลัก:
- เพิ่มดัชนีในคอลัมน์ที่ใช้ใน`WHERE`,`JOIN`และ`ORDER BY`
- หลีกเลี่ยง`SELECT *`— เลือกเฉพาะคอลัมน์ที่จำเป็นเท่านั้น
- ใช้`EXPLAIN`/`EXPLAIN ANALYZE`เพื่ออ่านแผนการสืบค้น
- แทนที่แบบสอบถามย่อยด้วย JOIN เมื่อเป็นไปได้
- ใช้ CTE เพื่อให้อ่านง่าย (โดยปกติจะไม่มีการลงโทษด้านประสิทธิภาพ)
- หลีกเลี่ยงฟังก์ชันบนคอลัมน์ที่จัดทำดัชนีไว้ใน WHERE: ใช้`WHERE date >= '2024-01-01'`ไม่ใช่ `WHERE YEAR(date) = 2024`
### คำถามที่ 4: CTE คืออะไร และฉันควรใช้เมื่อใด
**A:** นิพจน์ตารางทั่วไปจะสร้างชุดผลลัพธ์ชั่วคราวที่มีชื่อ:
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

### Q5: ฉันจะจัดการค่า NULL ได้อย่างถูกต้องได้อย่างไร
**A:** NULL หมายถึงไม่ทราบ — มันไม่เท่ากับสิ่งใดๆ เลย รวมถึงตัวมันเองด้วย:
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

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การค้นหา N อันดับแรกต่อกลุ่ม
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
ค้นหาพนักงานที่ได้รับค่าตอบแทนสูงสุด 3 คนในแต่ละแผนก
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ฟังก์ชันหน้าต่างโดย`ROW_NUMBER()`แบ่งพาร์ติชันตามแผนก
**ขั้นตอนที่ 3: นำไปใช้**```sql
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

**ขั้นตอนที่ 4: ยืนยัน**
ตรวจสอบว่าแต่ละแผนกมีไม่เกิน 3 แถว จัดการสายรัดด้วย`DENSE_RANK()`หากจำเป็น
### ปัญหาที่ 2: สร้างรายงานการเติบโตปีต่อปี
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
คำนวณรายได้ต่อเดือนและเปอร์เซ็นต์การเติบโตปีต่อปี
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้`DATE_TRUNC`สำหรับการจัดกลุ่มและฟังก์ชันหน้าต่าง`LAG()`สำหรับการเปรียบเทียบปีก่อนหน้า
**ขั้นตอนที่ 3: นำไปใช้**```sql
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

**ขั้นตอนที่ 4: ยืนยัน**
ตรวจสอบ 12 เดือนแรกมีค่า NULL สำหรับปีก่อน ตรวจสอบเปอร์เซ็นต์การเติบโตเทียบกับตัวเลขที่ทราบ
### ปัญหาที่ 3: การหมุนแถวเป็นคอลัมน์
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
เปลี่ยนสถานะนับจากแถวเป็นคอลัมน์
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้การรวมแบบมีเงื่อนไข (`CASE`ภายใน`SUM`)
**ขั้นตอนที่ 3: นำไปใช้**```sql
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

**ขั้นตอนที่ 4: ขยาย**
เพิ่มคอลัมน์เปอร์เซ็นต์และผลรวมที่กำลังดำเนินการ
---

## สรุป
SQL เป็นภาษาที่มีอายุ 50 ปีซึ่งยังคงมีความสำคัญ นักพัฒนา นักวิทยาศาสตร์ข้อมูล และนักวิเคราะห์ทุกคนจำเป็นต้องรู้สิ่งนี้ ภาษาหลักเป็นมาตรฐานและพกพาได้ ความแตกต่างของภาษาถิ่นสามารถจัดการได้ SQL สมัยใหม่ (พร้อมฟังก์ชันหน้าต่าง, CTE และการสนับสนุน JSON) แสดงออกเพียงพอสำหรับงานข้อมูลส่วนใหญ่ ทักษะที่สำคัญคือ: การเขียนแบบสอบถามที่มีประสิทธิภาพ การทำความเข้าใจดัชนี การอ่านแผนการสืบค้น และการออกแบบสคีมาที่ดี หากคุณทำงานกับข้อมูลเลย SQL จะไม่สามารถต่อรองได้