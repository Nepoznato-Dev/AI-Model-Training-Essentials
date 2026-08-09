---
# Metadata
title: "SQL Quick Reference Guide"
description: "SQL query reference"
category: "Quick Reference"
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
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [sql, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "24 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# คู่มืออ้างอิงด่วนของ SQL
คำสั่ง SQL ที่จำเป็นสำหรับการดำเนินการฐานข้อมูล
---

## โครงสร้างแบบสอบถามพื้นฐาน
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column(s)
HAVING condition
ORDER BY column [ASC|DESC]
LIMIT number;
```

---

## การดึงข้อมูล (SELECT)
### การเลือกพื้นฐาน```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, name, email FROM users;

-- Select with alias
SELECT name AS user_name, email AS contact FROM users;

-- Select distinct values
SELECT DISTINCT country FROM users;
```

### การกรอง (WHERE)```sql
-- Comparison operators
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- Starts with A
SELECT * FROM users WHERE name LIKE '%son';    -- Ends with son
SELECT * FROM users WHERE name LIKE '%test%';  -- Contains test
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- Logical operators
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### การเรียงลำดับและการจำกัด```sql
-- Order by single column
SELECT * FROM products ORDER BY price DESC;

-- Order by multiple columns
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- Limit results
SELECT * FROM users LIMIT 10;

-- Offset (for pagination)
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Skip 20, take 10
```

---

## ฟังก์ชั่นการรวมกลุ่ม
```sql
-- Count rows
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- Sum, Average, Min, Max
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- Group by
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having (filter groups)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## เข้าร่วม
### เข้าร่วมภายใน```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### ซ้าย/ขวาเข้าร่วม```sql
-- All users, even those without orders
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- All orders, even those without users (rare)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### เข้าร่วมภายนอกแบบเต็ม```sql
-- All users and all orders (MySQL doesn't support FULL OUTER)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### ข้ามเข้าร่วม```sql
-- Cartesian product (all combinations)
SELECT * FROM colors CROSS JOIN sizes;
```

### เข้าร่วมด้วยตนเอง```sql
-- Find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## คำถามย่อย
```sql
-- In WHERE clause
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- In SELECT clause
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- In FROM clause
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- With EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## ตั้งค่าการดำเนินการ
```sql
-- UNION (remove duplicates)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (keep duplicates)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT (common rows)
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2026;

-- EXCEPT/MINUS (rows in first but not second)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## การปรับเปลี่ยนข้อมูล
### แทรก```sql
-- Insert single row
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- Insert multiple rows
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- Insert from SELECT
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### อัปเดต```sql
-- Update single row
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- Update multiple columns
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- Update with JOIN
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### ลบ```sql
-- Delete specific rows
DELETE FROM users WHERE id = 1;

-- Delete with condition
DELETE FROM orders WHERE order_date < '2023-01-01';

-- Delete with JOIN
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- Truncate table (faster, resets auto-increment)
TRUNCATE TABLE temp_data;
```

---

## การดำเนินงานตาราง
### สร้างตาราง```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    age INT CHECK (age >= 18),
    country VARCHAR(50) DEFAULT 'USA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_country (country)
);
```

### แก้ไขตาราง```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Modify column
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- Rename column
ALTER TABLE users RENAME COLUMN username TO user_name;

-- Drop column
ALTER TABLE users DROP COLUMN phone;

-- Add constraint
ALTER TABLE orders ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) REFERENCES users(id);

-- Drop constraint
ALTER TABLE orders DROP FOREIGN KEY fk_user;

-- Rename table
ALTER TABLE old_name RENAME TO new_name;
```

### ตารางดร็อป```sql
DROP TABLE IF EXISTS temp_table;
```

---

## ข้อจำกัด
```sql
-- PRIMARY KEY: Unique identifier
CREATE TABLE users (
    id INT PRIMARY KEY
);

-- FOREIGN KEY: Reference to another table
CREATE TABLE orders (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- UNIQUE: No duplicate values
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- NOT NULL: Required field
CREATE TABLE users (
    name VARCHAR(50) NOT NULL
);

-- CHECK: Validate values
CREATE TABLE products (
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0)
);

-- DEFAULT: Default value
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ดัชนี
```sql
-- Create index
CREATE INDEX idx_email ON users(email);

-- Create composite index
CREATE INDEX idx_name_age ON users(last_name, first_name);

-- Create unique index
CREATE UNIQUE INDEX idx_username ON users(username);

-- Drop index
DROP INDEX idx_email ON users;

-- View indexes
SHOW INDEX FROM users;
```

---

## มุมมอง
```sql
-- Create view
CREATE VIEW active_users AS
SELECT id, name, email, country
FROM users
WHERE status = 'active';

-- Use view
SELECT * FROM active_users WHERE country = 'USA';

-- Update view (if updatable)
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, country, created_at
FROM users
WHERE status = 'active';

-- Drop view
DROP VIEW IF EXISTS active_users;
```

---

## นิพจน์ตารางทั่วไป (CTE)
```sql
-- Simple CTE
WITH high_value_users AS (
    SELECT id, name, total_spent
    FROM users
    WHERE total_spent > 1000
)
SELECT * FROM high_value_users ORDER BY total_spent DESC;

-- Recursive CTE (hierarchical data)
WITH RECURSIVE org_chart AS (
    -- Base case
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## ฟังก์ชั่นหน้าต่าง
```sql
-- ROW_NUMBER
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK and DENSE_RANK
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Running total
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- Partitioned window
SELECT department, name, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- LAG and LEAD
SELECT date, sales,
       LAG(sales, 1) OVER (ORDER BY date) AS prev_day_sales,
       LEAD(sales, 1) OVER (ORDER BY date) AS next_day_sales
FROM daily_sales;
```

---

## ประเภทข้อมูล
### ตัวเลข
-`INT`- จำนวนเต็ม
-`BIGINT`- จำนวนเต็มขนาดใหญ่
-`DECIMAL(p,s)`- ทศนิยมที่แน่นอน (ความแม่นยำ สเกล)
-`FLOAT`- จุดลอยตัวโดยประมาณ
-`DOUBLE`- ทุ่นความแม่นยำสองเท่า
### สตริง
-`CHAR(n)`- สตริงความยาวคงที่
-`VARCHAR(n)`- สตริงความยาวผันแปรได้
-`TEXT`- ข้อความขนาดใหญ่
-`ENUM`- ค่าแจกแจง
### วันที่/เวลา
-`DATE`- วันที่ (ปปปป-ดด-วว)
-`TIME`- เวลา (ช:นน:เอสเอส)
-`DATETIME`- วันที่และเวลา
-`TIMESTAMP`- การประทับเวลา Unix
-`YEAR`- ค่าปี
### บูลีน
-`BOOLEAN`หรือ`BOOL`- จริง/เท็จ
### ไบนารี่
-`BLOB`- วัตถุไบนารีขนาดใหญ่
-`BINARY`- ไบนารีคงที่
-`VARBINARY`- ไบนารี่ตัวแปร
---

## ฟังก์ชั่นที่มีประโยชน์
### ฟังก์ชั่นสตริง```sql
CONCAT(first_name, ' ', last_name)  -- Concatenate strings
UPPER(name)                          -- Convert to uppercase
LOWER(name)                          -- Convert to lowercase
SUBSTRING(name, 1, 3)                -- Extract substring
LENGTH(name)                         -- String length
TRIM(name)                           -- Remove whitespace
REPLACE(text, 'old', 'new')          -- Replace substring
```

### ฟังก์ชั่นวันที่```sql
NOW()                                -- Current date/time
CURDATE()                            -- Current date
CURTIME()                            -- Current time
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- Add interval
DATEDIFF(end_date, start_date)       -- Difference in days
YEAR(date_column)                    -- Extract year
MONTH(date_column)                   -- Extract month
DAY(date_column)                     -- Extract day
```

### ฟังก์ชันตัวเลข```sql
ROUND(value, 2)                      -- Round to decimals
CEIL(value)                          -- Round up
FLOOR(value)                         -- Round down
ABS(value)                           -- Absolute value
POWER(base, exp)                     -- Exponentiation
SQRT(value)                          -- Square root
RAND()                               -- Random number
```

### ฟังก์ชั่นตามเงื่อนไข```sql
-- CASE statement
SELECT name,
       CASE 
           WHEN age < 18 THEN 'Minor'
           WHEN age < 65 THEN 'Adult'
           ELSE 'Senior'
       END AS age_group
FROM users;

-- IF function (MySQL)
SELECT IF(age >= 18, 'Adult', 'Minor') AS status FROM users;

-- COALESCE (return first non-null)
SELECT COALESCE(phone, email, 'No contact') AS contact FROM users;

-- NULLIF (return NULL if equal)
SELECT NULLIF(value, 0) AS safe_value FROM data;
```

---

## เคล็ดลับประสิทธิภาพ
✅ **ทำ:**
- ใช้ดัชนีในคอลัมน์ที่มีการสอบถามบ่อย
- เลือกเฉพาะคอลัมน์ที่จำเป็น (หลีกเลี่ยง`SELECT *`)
- ใช้`EXPLAIN`เพื่อวิเคราะห์ประสิทธิภาพการค้นหา
- ทำให้ข้อมูลเป็นมาตรฐานอย่างเหมาะสม
- ใช้คำสั่งที่เตรียมไว้เพื่อป้องกันการแทรก SQL
❌ **อย่า:**
- ใช้ฟังก์ชันบนคอลัมน์ที่จัดทำดัชนีในส่วนคำสั่ง WHERE
- สร้างดัชนีมากเกินไป (เขียนช้า)
- ใช้`SELECT DISTINCT`โดยไม่จำเป็น
- ละเว้นแผนการดำเนินการแบบสอบถาม
- เก็บค่าที่คำนวณไว้เมื่อสามารถคำนวณได้
---

## แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย
```sql
-- Use parameterized queries (in application code)
-- NEVER concatenate user input directly

-- Grant minimal privileges
GRANT SELECT, INSERT ON database.table TO 'user'@'localhost';
REVOKE DELETE ON database.table FROM 'user'@'localhost';

-- Use strong passwords
-- Enable SSL connections
-- Regular security audits
```

---

*อัปเดตล่าสุด: กรกฎาคม 2569 | มาตรฐาน SQL (รองรับ MySQL/PostgreSQL)*