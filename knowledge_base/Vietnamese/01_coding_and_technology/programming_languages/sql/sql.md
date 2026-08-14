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
SQL (Ngôn ngữ truy vấn có cấu trúc) là ngôn ngữ dành riêng cho miền được thiết kế để quản lý và truy vấn dữ liệu trong cơ sở dữ liệu quan hệ. Được phát triển lần đầu tiên tại IBM vào những năm 1970 và được tiêu chuẩn hóa vào năm 1987, SQL vẫn là giao diện chính giữa các ứng dụng và dữ liệu của chúng. Mọi Hệ thống quản lý cơ sở dữ liệu quan hệ chính (RDBMS) - PostgreSQL, MySQL, SQL Server, Oracle, SQLite - đều sử dụng SQL làm ngôn ngữ truy vấn.
SQL không phải là ngôn ngữ lập trình có mục đích chung. Bạn sẽ không viết một ứng dụng web bằng SQL. Nhưng nếu ứng dụng của bạn lưu trữ dữ liệu — và gần như tất cả các ứng dụng đều lưu trữ — thì SQL là ngôn ngữ bạn sử dụng để truy xuất, chuyển đổi và quản lý dữ liệu đó. Nó được cho là kỹ năng kỹ thuật hữu ích nhất sau lập trình chung.
---

## Tại sao SQL lại quan trọng
- **Universal**: Mọi cơ sở dữ liệu quan hệ đều sử dụng SQL. Học nó một lần, sử dụng nó ở mọi nơi.
- **Khai báo**: Bạn mô tả *dữ liệu* bạn muốn chứ không phải *làm thế nào* để có được dữ liệu đó. Công cụ cơ sở dữ liệu tối ưu hóa việc thực thi.
- **Cần thiết cho bất kỳ nhà phát triển nào**: Phần phụ trợ, khoa học dữ liệu, DevOps, phân tích - tất cả đều yêu cầu SQL.
- **Mạnh mẽ**: Các hàm cửa sổ, CTE, truy vấn phụ và tập hợp cho phép bạn diễn đạt logic phức tạp trong một vài dòng.
- **Hiệu suất**: Một truy vấn SQL được viết tốt trên cơ sở dữ liệu được lập chỉ mục chính xác có thể xử lý hàng triệu hàng trong một phần nghìn giây.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Không phải ngôn ngữ có mục đích chung** | Không thể xây dựng ứng dụng, API hoặc thuật toán trong SQL | Kết hợp với Python, Java, JavaScript, v.v. |
| **Sự khác biệt về phương ngữ** | Mỗi RDBMS có hương vị SQL riêng với các phần mở rộng không tương thích | Bám sát ANSI SQL nếu có thể; sự khác biệt phương ngữ trừu tượng trong ứng dụng của bạn |
| **Độ cứng của lược đồ** | Việc thay đổi cấu trúc bảng trên các bảng lớn có thể chậm và gây rối | Sử dụng các công cụ di chuyển; lược đồ thiết kế trả trước cẩn thận |
| **Vấn đề truy vấn N+1** | Các truy vấn do ORM tạo có thể cực kỳ kém hiệu quả | Viết SQL tùy chỉnh cho các truy vấn phức tạp; hồ sơ với GIẢI THÍCH PHÂN TÍCH |
| **Độ phức tạp khi mở rộng quy mô** | Cơ sở dữ liệu SQL khó mở rộng theo chiều ngang hơn NoSQL | Sử dụng bản sao đọc, phân đoạn hoặc xem xét NoSQL cho các trường hợp sử dụng cụ thể |
---

## Khái niệm cốt lõi
### Mô hình quan hệ
Dữ liệu được lưu trữ trong **bảng** (quan hệ), bao gồm **hàng** (bản ghi/bộ dữ liệu) và **cột** (thuộc tính/trường). Các bảng có thể liên kết với nhau thông qua **phím**.
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

##Cơ bản về cú pháp
### Truy xuất dữ liệu (CHỌN)
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

### Tổng hợp
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

### Tham gia các bảng
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

### Sửa đổi dữ liệu
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

## Cú pháp & Mẫu nâng cao
### Chức năng của cửa sổ — Tìm hiểu sâu
Các hàm cửa sổ thực hiện các phép tính trên một tập hợp các hàng liên quan đến hàng hiện tại — mà không thu gọn chúng thành một hàng đầu ra duy nhất như GROUP BY.
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

### Biểu thức bảng chung (CTE) - Cách sử dụng nâng cao
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

### Thao tác JSON
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

### Thủ tục lưu trữ và trình kích hoạt
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

## Đi sâu vào các tính năng cốt lõi
### Tối ưu hóa truy vấn
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

**Danh sách kiểm tra tối ưu hóa:**
| Vấn đề | Triệu chứng | Sửa chữa |
|-------|----------|------|
| Quét tuần tự trên bàn lớn | `Seq Scan`trong GIẢI THÍCH | Thêm chỉ mục thích hợp |
| Thiếu chỉ mục trên cột WHERE | Quét toàn bộ bảng | Tạo chỉ mục trên các cột được lọc |
| CHỌN * lãng phí | Tìm nạp các cột không cần thiết | Chỉ chọn các cột cần thiết |
| Chuyển đổi loại ngầm định | Chỉ mục không được sử dụng | Các loại kết hợp trong so sánh |
| Chức năng trên các cột được lập chỉ mục | Chỉ mục không thể sử dụng được (không thể mở rộng) | Viết lại:`WHERE date >= '2024-01-01'`không phải`WHERE YEAR(date) = 2024`|
### Chiến lược lập chỉ mục
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

### Mức độ cô lập giao dịch
| Mức độ cô lập | Đọc bẩn | Đọc không lặp lại | Đọc ma |
|-----------------|:----------:|:-------------------:|:----------:|
| ĐỌC KHÔNG CAM KẾT | Có | Có | Có |
| ĐỌC CAM KẾT | Không | Có | Có |
| ĐỌC LẶP LẠI | Không | Không | Có* |
| CÓ THỂ TUẦN TIẾP | Không | Không | Không |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Chuẩn hóa
| Mẫu bình thường | Quy tắc | Ví dụ vi phạm |
|-------------|------|-------------------|
| **1NF** | Giá trị nguyên tử, không có nhóm lặp lại | Lưu nhiều điện thoại vào một cột là "123,456" |
| **2NF** | 1NF + không phụ thuộc một phần | Chi tiết đơn hàng phụ thuộc vào order_id chứ không phụ thuộc vào Product_id |
| **3NF** | 2NF + không phụ thuộc bắc cầu | Tên phòng nhân viên phụ thuộc vào dept_id, không phải nhân viên |
---

## Xác định cấu trúc cơ sở dữ liệu
### Tạo bảng
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

### Thay đổi bảng
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Cấu hình dự án & xây dựng hệ thống
### Công cụ di chuyển
| Công cụ | Ngôn ngữ/Ngăn xếp | Tiếp cận |
|------|--------------||----------|
| **Đường bay** | Java / chung | Di chuyển dựa trên SQL, quy ước đặt tên đơn giản |
| **Liquibase** | Java / chung | Nhật ký thay đổi XML, YAML, JSON hoặc SQL |
| **Alembic** | Python (SQLAlchemy) | Tự động tạo di chuyển từ các thay đổi mô hình |
| **Di chuyển Prisma** | Node.js / TypeScript | Lược đồ đầu tiên, tự động tạo SQL |
| **golang-di chuyển** | Đi | Dựa trên SQL, hỗ trợ di chuyển lên/xuống |
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

##Thử nghiệm
### Tạo dữ liệu thử nghiệm
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

| Khung | Cơ sở dữ liệu | Mô tả |
|----------|----------|-------------|
| **pgTAP** | PostgreSQL | Khung kiểm tra đơn vị |
| **tSQLt** | Máy chủ SQL | Kiểm tra đơn vị cho SQL Server |
| **utPLSQL** | Oracle | Khung thử nghiệm cho Oracle PL/SQL |
---

## Khả năng tương tác
### Ràng buộc ngôn ngữ
| Giao diện | Ngôn ngữ | Mô tả |
|----------|----------|-------------|
| **JDBC** | Java | API cơ sở dữ liệu tiêu chuẩn |
| **ODBC** | Nhiều | API cơ sở dữ liệu phổ quát |
| **psycopg2/3** | Python | Bộ điều hợp PostgreSQL |
| **cơ sở dữ liệu/sql** | Đi | Thư viện chuẩn với giao diện trình điều khiển |
| **sqlite3** | Python | Hỗ trợ SQLite tích hợp |
| **trang** | Node.js | Máy khách PostgreSQL |
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

## Mẫu thiết kế
### Mẫu 1: Pivot/crosstab
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Mẫu 2: Top-N mỗi nhóm
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Mẫu 3: Khoảng trống và Đảo
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

### Mẫu 4: Kích thước thay đổi từ từ (SCD Loại 2)
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

## Hiệu suất: Lập chỉ mục và lập kế hoạch truy vấn
### Cách hoạt động của chỉ mục
Chỉ mục là một cấu trúc dữ liệu (thường là cây B) cho phép cơ sở dữ liệu tìm các hàng mà không cần quét toàn bộ bảng.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Loại chỉ mục | Tốt nhất cho | Ví dụ |
|----------|----------|----------|
| **B-cây** (mặc định) | Truy vấn đẳng thức và phạm vi | `WHERE age > 25 AND age < 35`|
| **Băm** | Chỉ bình đẳng chính xác | `WHERE email = 'x@y.com'`|
| **GIN** | Tìm kiếm toàn văn, mảng, JSON | `WHERE description @@ 'search term'`|
| **GiST** | Dữ liệu hình học/không gian | `WHERE location <-> point(x,y) < 1000`|
### Đọc kế hoạch truy vấn
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

## Phương ngữ SQL
| Tính năng | PostgreSQL | MySQL | Máy chủ SQL | SQLite |
|----------|-------------|-------|-------------|--------|
| Tự động tăng | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Nối chuỗi | `\|\|`| `CONCAT()`| `+`hoặc`CONCAT()`| `\|\|`|
| Hàm ngày | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Hỗ trợ JSON | Xuất sắc (`jsonb`) | Tốt (`JSON`) | Tốt (`JSON`) | Cơ bản (`JSON1`) |
| Tìm kiếm toàn văn | Tích hợp (`tsvector`) | Tích hợp | Tích hợp | Hạn chế |
| Chức năng cửa sổ | Có | Có (8.0+) | Có | Có |
---

## Triển khai
### Chiến lược triển khai cơ sở dữ liệu
| Chiến lược | Mô tả | Mức độ rủi ro |
|----------|-------------|-------------|
| **Tệp di chuyển** | Các tập lệnh SQL được phiên bản được áp dụng theo thứ tự | Thấp |
| **Triển khai xanh lam** | Hai cơ sở dữ liệu giống hệt nhau; chuyển giao thông | Thấp |
| **Mở rộng hợp đồng** | Thêm cột mới, ghi kép, di chuyển, bỏ cột cũ | Thấp |
| **DDL trực tiếp** | Chạy ALTER TABLE trực tiếp trên sản xuất | Cao |
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

## Khi nào nên sử dụng SQL
| Kịch bản | Tại sao SQL | Thay thế |
|----------|----------|-------------|
| Dữ liệu quan hệ với các truy vấn phức tạp | Đó chính là mục đích của SQL | --- |
| Tính toàn vẹn giao dịch (ACID) | Cơ sở dữ liệu SQL đảm bảo tính nhất quán | --- |
| Báo cáo và phân tích | Tập hợp, chức năng cửa sổ, CTE | Python (Pandas) để phân tích rất phức tạp |
| Ràng buộc toàn vẹn dữ liệu | Khóa ngoại, KIỂM TRA, ĐỘC ĐÁO, KHÔNG NULL | Xác thực cấp ứng dụng (yếu hơn) |
| Lưu trữ khóa-giá trị đơn giản | Quá mức cần thiết cho trường hợp sử dụng này | Redis, DynamoDB |
| Dữ liệu phi cấu trúc cao | Độ cứng của lược đồ là một vấn đề | MongoDB, cơ sở dữ liệu tài liệu |
| Chia tỷ lệ ngang lớn | Khó phân chia cơ sở dữ liệu SQL | Cassandra, DynamoDB, CockroachDB |
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`WHERE`và`HAVING`là gì?
**A:**`WHERE`lọc các hàng trước khi nhóm; `HAVING`lọc các nhóm sau khi tổng hợp:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Câu 2: Các chức năng của cửa sổ khác với GROUP BY như thế nào?
**A:** Các hàm cửa sổ tính toán trên các hàng mà không thu gọn chúng:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Câu 3: Làm cách nào để tối ưu hóa các truy vấn chậm?
**Đ:** Các chiến lược chính:
- Thêm chỉ mục trên các cột sử dụng trong`WHERE`,`JOIN`, và`ORDER BY`
- Tránh`SELECT *`- chỉ chọn các cột cần thiết
- Sử dụng `EXPLAIN`/`EXPLAIN ANALYZE` để đọc kế hoạch truy vấn
- Thay thế các truy vấn con bằng THAM GIA nếu có thể
- Sử dụng CTE để dễ đọc (thường không bị phạt hiệu suất)
- Tránh các hàm trên các cột được lập chỉ mục trong WHERE: sử dụng`WHERE date >= '2024-01-01'`không sử dụng `WHERE YEAR(date) = 2024`
### Q4: CTE là gì và khi nào tôi nên sử dụng chúng?
**A:** Biểu thức bảng chung tạo các tập kết quả tạm thời được đặt tên:
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

### Câu hỏi 5: Làm cách nào để xử lý chính xác các giá trị NULL?
**A:** NULL đại diện cho ẩn số — nó không bằng bất cứ thứ gì, kể cả chính nó:
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Bài 1: Tìm N Top mỗi nhóm
**Bước 1: Tìm hiểu vấn đề**
Tìm 3 nhân viên được trả lương cao nhất trong mỗi bộ phận.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng chức năng cửa sổ với`ROW_NUMBER()`được phân vùng theo bộ phận.
**Bước 3: Thực hiện**```sql
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

**Bước 4: Xác minh**
Kiểm tra xem mỗi bộ phận có tối đa 3 hàng hay không. Xử lý các mối quan hệ bằng`DENSE_RANK()`nếu cần.
### Bài toán 2: Xây dựng Báo cáo tăng trưởng hàng năm
**Bước 1: Tìm hiểu vấn đề**
Tính toán doanh thu hàng tháng và tỷ lệ tăng trưởng hàng năm.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`DATE_TRUNC`để nhóm và chức năng cửa sổ`LAG()`để so sánh năm trước.
**Bước 3: Thực hiện**```sql
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

**Bước 4: Xác minh**
Kiểm tra 12 tháng đầu có NULL của năm trước không. Xác nhận tỷ lệ phần trăm tăng trưởng so với các số liệu đã biết.
### Vấn đề 3: Xoay hàng thành cột
**Bước 1: Tìm hiểu vấn đề**
Chuyển đổi số lượng trạng thái từ hàng sang cột.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng tổng hợp có điều kiện (`CASE`bên trong`SUM`).
**Bước 3: Thực hiện**```sql
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

**Bước 4: Gia hạn**
Thêm cột phần trăm và tổng số đang chạy.
---

## Bản tóm tắt
SQL là một ngôn ngữ 50 năm tuổi vẫn rất cần thiết. Mọi nhà phát triển, nhà khoa học dữ liệu và nhà phân tích đều cần biết điều đó. Ngôn ngữ cốt lõi được chuẩn hóa và di động; sự khác biệt về phương ngữ có thể quản lý được. SQL hiện đại (với các hàm cửa sổ, CTE và hỗ trợ JSON) đủ biểu cảm cho hầu hết các tác vụ dữ liệu. Các kỹ năng chính là: viết truy vấn hiệu quả, hiểu chỉ mục, đọc kế hoạch truy vấn và thiết kế các lược đồ tốt. Nếu bạn làm việc với dữ liệu, SQL là không thể thương lượng được.