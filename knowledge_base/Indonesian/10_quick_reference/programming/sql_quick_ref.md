<!--
---
# Metadata
title: "SQL Quick Reference Guide"
description: "SQL query reference"
category: "Quick Reference"
subcategory: "Programming"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to programming/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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

-->
# Panduan Referensi Cepat SQL
Perintah SQL penting untuk operasi database.
---

## Struktur Kueri Dasar
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

## Pengambilan Data (PILIH)
### Seleksi Dasar```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, name, email FROM users;

-- Select with alias
SELECT name AS user_name, email AS contact FROM users;

-- Select distinct values
SELECT DISTINCT country FROM users;
```

### Pemfilteran (DI MANA)```sql
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

### Menyortir dan Membatasi```sql
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

## Fungsi Agregasi
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

## Bergabung
### Gabungan Dalam```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### Gabung Kiri/Kanan```sql
-- All users, even those without orders
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- All orders, even those without users (rare)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Gabung Luar Penuh```sql
-- All users and all orders (MySQL doesn't support FULL OUTER)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Gabung Silang```sql
-- Cartesian product (all combinations)
SELECT * FROM colors CROSS JOIN sizes;
```

### Bergabung Sendiri```sql
-- Find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## Subkueri
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

## Atur Operasi
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

## Modifikasi Data
### MENYISIPKAN```sql
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

### MEMPERBARUI```sql
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

### MENGHAPUS```sql
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

## Operasi Tabel
### BUAT Tabel```sql
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

### ALTER Tabel```sql
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

### JATUHKAN Tabel```sql
DROP TABLE IF EXISTS temp_table;
```

---

## Kendala
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

## Indeks
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

## Tampilan
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

## Ekspresi Tabel Umum (CTE)
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

## Fungsi Jendela
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

## Tipe Data
### Numerik
-`INT`- Bilangan Bulat
-`BIGINT`- Bilangan bulat besar
-`DECIMAL(p,s)`- Desimal tepat (presisi, skala)
-`FLOAT`- Perkiraan titik mengambang
-`DOUBLE`- Pelampung presisi ganda
### Tali
-`CHAR(n)`- Panjang string tetap
-`VARCHAR(n)`- String dengan panjang variabel
-`TEXT`- Teks besar
-`ENUM`- Nilai yang disebutkan
### Tanggal/Waktu
-`DATE`- Tanggal (YYYY-MM-DD)
-`TIME`- Waktu (JJ:MM:SS)
-`DATETIME`- Tanggal dan waktu
-`TIMESTAMP`- Stempel waktu Unix
-`YEAR`- Nilai tahun
### Boolean
-`BOOLEAN`atau`BOOL`- Benar/Salah
### Biner
-`BLOB`- Objek biner besar
-`BINARY`- Biner tetap
-`VARBINARY`- Biner variabel
---

## Fungsi Berguna
### Fungsi Tali```sql
CONCAT(first_name, ' ', last_name)  -- Concatenate strings
UPPER(name)                          -- Convert to uppercase
LOWER(name)                          -- Convert to lowercase
SUBSTRING(name, 1, 3)                -- Extract substring
LENGTH(name)                         -- String length
TRIM(name)                           -- Remove whitespace
REPLACE(text, 'old', 'new')          -- Replace substring
```

### Fungsi Tanggal```sql
NOW()                                -- Current date/time
CURDATE()                            -- Current date
CURTIME()                            -- Current time
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- Add interval
DATEDIFF(end_date, start_date)       -- Difference in days
YEAR(date_column)                    -- Extract year
MONTH(date_column)                   -- Extract month
DAY(date_column)                     -- Extract day
```

### Fungsi Numerik```sql
ROUND(value, 2)                      -- Round to decimals
CEIL(value)                          -- Round up
FLOOR(value)                         -- Round down
ABS(value)                           -- Absolute value
POWER(base, exp)                     -- Exponentiation
SQRT(value)                          -- Square root
RAND()                               -- Random number
```

### Fungsi Bersyarat```sql
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

## Kiat Kinerja
✅ **Lakukan:**
- Gunakan indeks pada kolom yang sering ditanyakan
- Pilih hanya kolom yang diperlukan (hindari`SELECT *`)
- Gunakan`EXPLAIN`untuk menganalisis kinerja kueri
- Normalisasikan data dengan tepat
- Gunakan pernyataan yang disiapkan untuk mencegah injeksi SQL
❌ **Jangan:**
- Gunakan fungsi pada kolom yang diindeks dalam klausa WHERE
- Membuat terlalu banyak indeks (memperlambat penulisan)
- Gunakan`SELECT DISTINCT`jika tidak perlu
- Abaikan rencana eksekusi kueri
- Menyimpan nilai yang dihitung saat dapat dihitung
---

## Praktik Terbaik Keamanan
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

*Terakhir diperbarui: Juli 2026 | SQL Standar (kompatibel dengan MySQL/PostgreSQL)*