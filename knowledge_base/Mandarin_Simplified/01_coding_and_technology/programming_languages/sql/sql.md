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
SQL（结构化查询语言）是一种特定于领域的语言，旨在管理和查询关系数据库中的数据。 SQL 最初于 20 世纪 70 年代由 IBM 开发，并于 1987 年标准化，至今仍然是应用程序与其数据之间的主要接口。每个主要的关系数据库管理系统 (RDBMS) — PostgreSQL、MySQL、SQL Server、Oracle、SQLite — 都使用 SQL 作为其查询语言。
SQL 不是通用编程语言。您不会用 SQL 编写 Web 应用程序。但是，如果您的应用程序存储数据（几乎所有应用程序都这样做），那么 SQL 就是您用来检索、转换和管理该数据的语言。它可以说是继通用编程之后最普遍有用的技术技能。
---

## 为什么 SQL 很重要
- **通用**：每个关系数据库都使用 SQL。一次学习，随处使用。
- **声明性**：您描述您想要“什么”数据，而不是“如何”获取它。数据库引擎优化执行。
- **对于任何开发人员来说都是必不可少的**：后端、数据科学、DevOps、分析 - 都需要 SQL。
- **强大**：窗口函数、CTE、子查询和聚合让您可以用几行代码表达复杂的逻辑。
- **性能**：在正确索引的数据库上编写良好的 SQL 查询可以在几毫秒内处理数百万行。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **不是通用语言** |无法在 SQL 中构建应用程序、API 或算法 |与Python、Java、JavaScript等结合|
| **方言差异** |每个 RDBMS 都有自己的 SQL 风格，且扩展不兼容 |尽可能坚持使用 ANSI SQL；应用程序中的抽象方言差异|
| **模式刚性** |更改大型表上的表结构可能会很慢且具有破坏性 |使用迁移工具；预先仔细设计架构|
| **N+1查询问题** | ORM 生成的查询效率极低 |为复杂查询编写自定义 SQL；使用 EXPLAIN ANALYZE | 进行配置文件
| **扩展复杂性** | SQL 数据库比 NoSQL 更难水平扩展 |针对特定用例使用只读副本、分片或考虑 NoSQL |
---

## 核心概念
### 关系模型
数据存储在**表**（关系）中，由**行**（记录/元组）和**列**（属性/字段）组成。表可以通过**键**相互关联。
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

## 语法基础知识
### 检索数据（选择）
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

### 连接表
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

### 修改数据
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

## 高级语法和模式
### 窗口函数 — 深入探讨
窗口函数对与当前行相关的一组行执行计算，而不是像 GROUP BY 那样将它们折叠成单个输出行。
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

### 公用表表达式 (CTE) — 高级用法
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

### 存储过程和触发器
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

## 深入探讨核心功能
### 查询优化
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

**优化清单：**
|问题 |症状|修复 |
|--------|---------|-----|
|大表顺序扫描 |  解释 | `Seq Scan`添加适当的索引 |
| WHERE 列上缺少索引 |全表扫描 |在过滤列上创建索引 |
|选择 * 浪费 |获取不必要的列 |仅选择需要的列 |
|隐式类型转换 |未使用索引 |比较中的匹配类型 |
|索引列上的函数 |索引不可用（不可控制）|重写：`WHERE date >= '2024-01-01'` 不是`WHERE YEAR(date) = 2024`|
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

### 事务隔离级别
|隔离级别|脏读 |不可重复阅读 |幻读|
|-----------------|:----------:|:--------------------:|:------------:|
|阅读未提交 |是的 |是的 |是的 |
|已提交读 |没有 |是的 |是的 |
|可重复阅读|没有 |没有 |是* |
|可串行化|没有 |没有 |没有 |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 标准化
|范式 |规则|违规示例 |
|------------|------|--------------------|
| **1NF** |原子值，无重复基团 |将多个电话存储在一列中，如“123,456” |
| **2NF** | 1NF + 无部分依赖 |订单详细信息取决于 order_id 而不是 Product_id |
| **3NF** | 2NF + 无传递依赖 |员工部门名称取决于 dept_id，而不是员工 |
---

## 定义数据库结构
### 创建表
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

### 改变表
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## 项目配置和构建系统
### 迁移工具
|工具|语言/堆栈 |方法|
|------|----------------|----------|
| **飞行路线** | Java / 通用 |基于 SQL 的迁移，简单的命名约定 |
| **液体碱** | Java / 通用 | XML、YAML、JSON 或 SQL 变更日志 |
| **蒸馏器** | Python（SQLAlchemy）|根据模型更改自动生成迁移 |
| **Prisma 迁移** | Node.js / TypeScript |模式优先，自动生成 SQL |
| **golang-迁移** |去 |基于SQL，支持上/下迁移 |
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

## 测试
### 测试数据生成
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

|框架|数据库|描述 |
|------------|----------|-------------|
| **pgTAP** | PostgreSQL |单元测试框架|
| **tSQLt** | SQL Server | SQL Server 的单元测试 |
| **utPLSQL** |甲骨文 | Oracle PL/SQL 测试框架|
---

## 互操作性
### 语言绑定
|接口 |语言 |描述 |
|------------|----------|-------------|
| **JDBC** |爪哇 |标准数据库API |
| **ODBC** |多个|通用数据库API |
| **psycopg2/3** |蟒蛇 | PostgreSQL 适配器 |
| **数据库/sql** |去 |带有驱动程序接口的标准库 |
| **sqlite3** |蟒蛇 |内置 SQLite 支持 |
| **页** | Node.js | PostgreSQL 客户端 |
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

## 设计模式
### 模式 1：数据透视表/交叉表
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### 模式 2：每组前 N 个
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### 模式 3：间隙和孤岛
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

### 模式 4：缓慢变化的维度（SCD 类型 2）
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

## 性能：索引和查询规划
### 索引如何工作
索引是一种数据结构（通常是 B 树），可让数据库在不扫描整个表的情况下查找行。
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

|指数类型 |最适合 |示例|
|------------|----------|---------|
| **B 树**（默认） |相等和范围查询 | `WHERE age > 25 AND age < 35`|
| **哈希** |仅精确相等 | `WHERE email = 'x@y.com'`|
| **杜松子酒** |全文搜索、数组、JSON | `WHERE description @@ 'search term'`|
| **吉斯特** |几何/空间数据| `WHERE location <-> point(x,y) < 1000`|
### 阅读查询计划
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
|自动递增 | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
|字符串连接 | `\|\|`| `CONCAT()`| `+`或`CONCAT()`| `\|\|`|
|日期函数 |  `NOW()`、`AGE()` |  `NOW()`、`DATEDIFF()` |  `GETDATE()`、`DATEDIFF()` | `DATE('now')`|
| JSON 支持 |优秀（`jsonb`）|好（`JSON`）|好 (`JSON`) |基本（`JSON1`）|
|全文检索 |内置（`tsvector`）|内置|内置|有限公司|
|窗口函数 |是的 |是（8.0+）|是的 |是的 |
---

## 部署
### 数据库部署策略
|战略|描述 |风险等级|
|----------|-------------|------------|
| **迁移文件** |按顺序应用版本化 SQL 脚本 |低|
| **蓝绿部署** |两个相同的数据库；切换流量 |低|
| **扩大合同** |添加新列、双写、迁移、删除旧列 |低|
| **直接 DDL** |直接在生产环境中运行 ALTER TABLE |高|
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

## 何时使用 SQL
|场景 |为什么使用 SQL |另类|
|----------|---------|-------------|
|具有复杂查询的关系数据 |这就是 SQL 的设计目的 | --- |
|事务完整性（ACID）| SQL数据库保证一致性| --- |
|报告和分析 |聚合、窗口函数、CTE | Python（Pandas）用于非常复杂的分析 |
|数据完整性约束|外键、CHECK、UNIQUE、NOT NULL |应用程序级验证（较弱） |
|简单的键值存储 |对于这个用例来说太过分了| Redis、DynamoDB |
|高度非结构化数据 |模式刚性是一个问题| MongoDB，文档数据库 |
|大规模水平扩展 | SQL数据库难以分片|卡桑德拉、DynamoDB、CockroachDB |
---

＃＃ 概括
SQL 是一门已有 50 年历史的语言，至今仍然至关重要。每个开发人员、数据科学家和分析师都需要了解它。核心语言标准化、可移植；方言差异是可以控制的。现代 SQL（具有窗口函数、CTE 和 JSON 支持）对于大多数数据任务来说具有足够的表达能力。关键技能是：编写高效的查询、理解索引、阅读查询计划以及设计良好的模式。如果您确实需要处理数据，那么 SQL 是不容协商的。