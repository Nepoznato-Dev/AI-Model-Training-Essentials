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
SQL（結構化查詢語言）是一種特定於領域的語言，旨在管理和查詢關係資料庫中的資料。 SQL 最初由 IBM 於 20 世紀 70 年代開發，並於 1987 年標準化，至今仍然是應用程式與其資料之間的主要介面。每個主要的關聯式資料庫管理系統 (RDBMS) — PostgreSQL、MySQL、SQL Server、Oracle、SQLite — 都使用 SQL 作為其查詢語言。
SQL 不是通用程式語言。您不會用 SQL 編寫 Web 應用程式。但是，如果您的應用程式儲存資料（幾乎所有應用程式都這樣做），那麼 SQL 就是您用來檢索、轉換和管理該資料的語言。它可以說是繼通用程式設計之後最普遍有用的技術技能。
---

## 為什麼 SQL 很重要
- **通用**：每個關聯式資料庫都使用 SQL。一次學習，隨處使用。
- **聲明性**：您描述您想要「什麼」數據，而不是「如何」取得它。資料庫引擎優化執行。
- **對於任何開發人員來說都是必不可少的**：後端、資料科學、DevOps、分析 - 都需要 SQL。
- **強大**：視窗函數、CTE、子查詢和聚合讓您可以用幾行程式碼表達複雜的邏輯。
- **效能**：在正確索引的資料庫上編寫良好的 SQL 查詢可以在幾毫秒內處理數百萬行。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **不是通用語言** |無法在 SQL 中建立應用程式、API 或演算法 |與Python、Java、JavaScript等結合 |
| **方言差異** |每個 RDBMS 都有自己的 SQL 風格，且擴展不相容 |盡可能堅持使用 ANSI SQL；應用程式中的抽象方言差異|
| **模式剛性** |更改大型表上的表結構可能會很慢且具有破壞性 |使用遷移工具；預先仔細設計架構|
| **N+1查詢問題** | ORM 產生的查詢效率極低 |為複雜查詢編寫自訂 SQL；使用 EXPLAIN ANALYZE | 進行設定文件
| **擴展複雜性** | SQL 資料庫比 NoSQL 更難水平擴展 |針對特定用例使用唯讀副本、分片或考慮 NoSQL |
---

## 核心概念
### 關係模型
資料儲存在**表**（關係）中，由**行**（記錄/元組）和**列**（屬性/欄位）組成。表可以透過**鍵**相互關聯。
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

## 文法基礎知識
### 檢索資料（選擇）
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

### 聚合
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

### 連接表
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

### 修改數據
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

## 進階語法和模式
### 視窗函數 — 深入探討
視窗函數對與目前行相關的一組行執行計算，而不是像 GROUP BY 那樣將它們折疊成單一輸出行。
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

### 公用表格運算式 (CTE) — 進階用法
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

### JSON 操作
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

### 預存程序和觸發器
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

## 深入探討核心功能
### 查詢最佳化
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

**優化清單：**
|問題 |症狀|修復|
|--------|---------|-----|
|大表順序掃描 | 解釋 | `Seq Scan`新增適當的索引 |
| WHERE 欄位上缺少索引 |全表掃描 |在篩選列上建立索引 |
|選擇 * 浪費 |取得不必要的列 |只選擇需要的列 |
|隱式類型轉換 |未使用索引 |比較中的符合類型 |
|索引列上的函數 |索引不可用（不可控制）|重寫：`WHERE date >= '2024-01-01'` 不是`WHERE YEAR(date) = 2024`|
### 索引策略
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

### 交易隔離級別
|隔離等級|髒讀 |不可重複閱讀 |幻讀|
|-----------------|:----------:|:--------------------:|:------------:|
|閱讀未提交 |是的 |是的 |是的 |
|已提交讀 |沒有 |是的 |是的 |
|可重複閱讀|沒有 |沒有 |是* |
|可串行化|沒有 |沒有 |沒有 |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 標準化
|範式|規則|違規範例 |
|------------|------|--------------------|
| **1NF** |原子值，無重複基團 |將多個電話儲存在一列中，如“123,456” |
| **2NF** | 1NF + 無部分依賴性 |訂單詳細資料取決於 order_id 而非 Product_id |
| **3NF** | 2NF + 無傳遞依賴 |員工部門名稱取決於 dept_id，而不是員工 |
---

## 定義資料庫結構
### 建立表
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

### 改變表
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## 專案配置與建置系統
### 遷移工具
|工具|語言/堆疊 |方法|
|------|----------------|----------|
| **飛行路線** | Java / 通用 |基於 SQL 的遷移，簡單的命名約定 |
| **液體鹼** | Java / 通用 | XML、YAML、JSON 或 SQL 變更日誌 |
| **蒸餾器** | Python（SQLAlchemy）|根據模型變更自動產生遷移 |
| **Prisma 遷移** | Node.js / TypeScript |模式優先，自動產生 SQL |
| **golang-遷移** |去 |基於SQL，支援上/下遷移 |
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

## 測試
### 測試資料生成
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

|框架|資料庫|描述 |
|------------|----------|-------------|
| **pgTAP** | PostgreSQL |單元測試框架|
| **tSQLt** | SQL Server | SQL Server 的單元測試 |
| **utPLSQL** |甲骨文 | Oracle PL/SQL 測試框架|
---

## 互通性
### 語言綁定
|介面|語言 |說明 |
|------------|----------|-------------|
| **JDBC** |爪哇 |標準資料庫API |
| **ODBC** |多|通用資料庫API |
| **psycopg2/3** |蟒蛇 | PostgreSQL 適配器 |
| **資料庫/sql** |去 |有驅動程式介面的標準函式庫 |
| **sqlite3** |蟒蛇 |內建 SQLite 支援 |
| **頁** | Node.js | PostgreSQL 用戶端 |
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

## 設計模式
### 模式 1：資料透視表/交叉表
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### 模式 2：每組前 N 個
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### 模式 3：間隙與孤島
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

### 模式 4：緩慢變化的維度（SCD 類型 2）
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

## 效能：索引與查詢規劃
### 索引如何運作
索引是一種資料結構（通常是 B 樹），可讓資料庫在不掃描整個資料表的情況下尋找行。
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

|指數類型 |最適合 |範例|
|------------|----------|---------|
| **B 樹**（預設） |相等與範圍查詢 |`WHERE age > 25 AND age < 35`|
| **哈希** |僅精確相等 |`WHERE email = 'x@y.com'`|
| **杜松子酒** |全文搜尋、陣列、JSON |`WHERE description @@ 'search term'`|
| **吉斯特** |幾何/空間資料|`WHERE location <-> point(x,y) < 1000`|
### 閱讀查詢計劃
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

## SQL 方言
|特色 | PostgreSQL | MySQL | SQL Server | SQLite |
|--------|---------|--------|------------|--------|
| 自動遞增 |`BIGSERIAL`/`GENERATED ALWAYS`|`AUTO_INCREMENT`|`IDENTITY`|`INTEGER PRIMARY KEY AUTOINCREMENT`|
|字串連線 |`\|\|`|`CONCAT()`|`+`或`CONCAT()`|`\|\|`|
|日期函數 | `NOW()`、`AGE()` | `NOW()`、`DATEDIFF()` | `GETDATE()`、`DATEDIFF()` |`DATE('now')`|
| JSON 支援 |優秀（`jsonb`）|好（`JSON`）|好 (`JSON`) |基本（`JSON1`）|
|全文檢索 |內建（`tsvector`）|內建|內建|有限公司|
|視窗函數 |是的 |是（8.0+）|是的 |是的 |
---

## 部署
### 資料庫部署策略
|戰略|描述 |風險等級|
|----------|-------------|------------|
| **遷移檔案** |依序套用版本化 SQL 腳本 |低|
| **藍綠部署** |兩個相同的資料庫；切換流量 |低|
| **擴大合約** |新增列、雙寫、遷移、刪除舊列 |低|
| **直接 DDL** |直接在生產環境中運行 ALTER TABLE |高|
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

## 何時使用 SQL
|場景|為什麼要使用 SQL |另類|
|----------|---------|-------------|
|具有複雜查詢的關聯式資料 |這就是 SQL 的設計目的 | --- |
|事務完整性（ACID）| SQL資料庫保證一致性| --- |
|報告與分析 |聚合、視窗函數、CTE | Python（Pandas）用於非常複雜的分析 |
|資料完整性限制|外鍵、CHECK、UNIQUE、NOT NULL |應用程式層級驗證（較弱）|
|簡單的鍵值儲存 |對於這個用例來說太過分了| Redis、DynamoDB |
|高度非結構化資料 |模式剛性是一個問題| MongoDB，文檔資料庫 |
|大規模水平擴展 | SQL資料庫難以分片|卡桑德拉、DynamoDB、CockroachDB |
---

## 綜合問答
### Q1：`WHERE` 和`HAVING`有什麼不同？
**A:**`WHERE`在分組之前過濾行；`HAVING`聚合後過濾組：
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2：視窗函數與 GROUP BY 有何不同？
**A:** 視窗函數跨行計算而不折疊它們：
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3：如何最佳化慢查詢？
**答：** 關鍵策略：
- 在`WHERE`、`JOIN`和`ORDER BY`中使用的欄位上新增索引
- 避免`SELECT *`— 僅選擇所需的列
- 使用`EXPLAIN`/`EXPLAIN ANALYZE`讀取查詢計劃
- 盡可能用 JOIN 取代子查詢
- 使用 CTE 提高可讀性（通常不會造成效能損失）
- 避免在 WHERE 中的索引列上使用函數：使用`WHERE date >= '2024-01-01'`而不是 `WHERE YEAR(date) = 2024`
### Q4：什麼是 CTE？何時應該使用它們？
**A:** 公用表格運算式建立命名暫存結果集：
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

### Q5：如何正確處理NULL值？
**A:** NULL 代表未知－它不等於任何東西，包括它自己：
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

## 解決問題的思路
### 問題 1：找出每組前 N 個
**第 1 步：了解問題**
找出每個部門中薪水最高的 3 名員工。
**第 2 步：確定方法**
使用按部門分區的`ROW_NUMBER()`視窗函數。
**步驟 3：實施**```sql
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

**第 4 步：驗證**
檢查每個部門最多有 3 行。如果需要，請使用`DENSE_RANK()`處理關聯式。
### 問題 2：建立年成長報告
**第 1 步：了解問題**
計算每月收入和年增率百分比。
**第 2 步：確定方法**
使用`DATE_TRUNC`進行分組，使用`LAG()`視窗函數進行上一年比較。
**步驟 3：實施**```sql
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

**第 4 步：驗證**
檢查上一年的前 12 個月是否為 NULL。根據已知數據驗證增長百分比。
### 問題 3：將行旋轉到列
**第 1 步：了解問題**
將狀態計數從行轉換為列。
**第 2 步：確定方法**
使用条件聚合（`SUM`内的`CASE`）。
**步驟 3：實施**```sql
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

**第 4 步：擴充**
新增百分比列和運行總計。
---

＃＃ 概括
SQL 是一門已有 50 年歷史的語言，至今仍然至關重要。每個開發人員、資料科學家和分析師都需要了解它。核心語言標準化、可移植；方言差異是可以控制的。現代 SQL（具有視窗函數、CTE 和 JSON 支援）對於大多數資料任務來說具有足夠的表達能力。關鍵技能是：編寫高效的查詢、理解索引、閱讀查詢計劃以及設計良好的模式。如果您確實需要處理數據，那麼 SQL 是不容協商的。