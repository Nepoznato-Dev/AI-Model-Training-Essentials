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

SQL (Structured Query Language) is a domain-specific language designed for managing and querying data in relational databases. First developed at IBM in the 1970s and standardised in 1987, SQL remains the primary interface between applications and their data. Every major Relational Database Management System (RDBMS) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — uses SQL as its query language.

SQL is not a general-purpose programming language. You would not write a web application in SQL. But if your application stores data — and nearly all applications do — then SQL is the language you use to retrieve, transform, and manage that data. It is arguably the most universally useful technical skill after general programming.

---

## Why SQL Matters

- **Universal**: Every relational database speaks SQL. Learn it once, use it everywhere.
- **Declarative**: You describe *what* data you want, not *how* to get it. The database engine optimises the execution.
- **Essential for any developer**: Backend, data science, DevOps, analytics — all require SQL.
- **Powerful**: Window functions, CTEs, subqueries, and aggregations let you express complex logic in a few lines.
- **Performance**: A well-written SQL query on a properly indexed database can process millions of rows in milliseconds.

## The Trade-offs

| Limitation | Details | Typical Workaround |
|-----------|---------|-------------------|
| **Not a general-purpose language** | Cannot build applications, APIs, or algorithms in SQL | Combine with Python, Java, JavaScript, etc. |
| **Dialect differences** | Each RDBMS has its own SQL flavour with incompatible extensions | Stick to ANSI SQL where possible; abstract dialect differences in your application |
| **Schema rigidity** | Changing table structures on large tables can be slow and disruptive | Use migration tools; design schemas carefully upfront |
| **N+1 query problem** | ORM-generated queries can be extremely inefficient | Write custom SQL for complex queries; profile with EXPLAIN ANALYSE |
| **Scaling complexity** | SQL databases are harder to scale horizontally than NoSQL | Use read replicas, sharding, or consider NoSQL for specific use cases |

---

## Core Concepts

### The Relational Model

Data is stored in **tables** (relations), which consist of **rows** (records/tuples) and **columns** (attributes/fields). Tables can be related to each other through **keys**.

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

## Syntax Fundamentals

### Retrieving Data (SELECT)

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

### Aggregation

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

### Joining Tables

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

### Modifying Data

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

## Advanced Syntax & Patterns

### Window Functions — Deep Dive

Window functions perform calculations across a set of rows related to the current row — without collapsing them into a single output row like GROUP BY does.

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

### Common Table Expressions (CTEs) — Advanced Usage

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

### JSON Operations

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

### Stored Procedures and Triggers

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

## Deep Dive into Core Features

### Query Optimization

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

**Optimization checklist:**

| Issue | Symptom | Fix |
|-------|---------|-----|
| Sequential scan on large table | `Seq Scan` in EXPLAIN | Add appropriate index |
| Missing index on WHERE column | Full table scan | Create index on filtered columns |
| SELECT * waste | Fetching unnecessary columns | Select only needed columns |
| Implicit type conversion | Index not used | Match types in comparisons |
| Functions on indexed columns | Index unusable (non-sargable) | Rewrite: `WHERE date >= '2024-01-01'` not `WHERE YEAR(date) = 2024` |

### Indexing Strategies

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

### Transaction Isolation Levels

| Isolation Level | Dirty Read | Non-repeatable Read | Phantom Read |
|-----------------|:----------:|:-------------------:|:------------:|
| READ UNCOMMITTED | Yes | Yes | Yes |
| READ COMMITTED | No | Yes | Yes |
| REPEATABLE READ | No | No | Yes* |
| SERIALIZABLE | No | No | No |

```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalization

| Normal Form | Rule | Example Violation |
|-------------|------|-------------------|
| **1NF** | Atomic values, no repeating groups | Storing multiple phones in one column as "123,456" |
| **2NF** | 1NF + no partial dependencies | Order detail depends on order_id but not product_id |
| **3NF** | 2NF + no transitive dependencies | Employee dept name depends on dept_id, not employee |

---

## Defining Database Structure

### Creating Tables

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

### Altering Tables

```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Project Configuration & Build System

### Migration Tools

| Tool | Language/Stack | Approach |
|------|---------------|----------|
| **Flyway** | Java / general | SQL-based migrations, simple naming convention |
| **Liquibase** | Java / general | XML, YAML, JSON, or SQL changelogs |
| **Alembic** | Python (SQLAlchemy) | Auto-generates migrations from model changes |
| **Prisma Migrate** | Node.js / TypeScript | Schema-first, auto-generates SQL |
| **golang-migrate** | Go | SQL-based, supports up/down migrations |

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

## Testing

### Test Data Generation

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

| Framework | Database | Description |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Unit testing framework |
| **tSQLt** | SQL Server | Unit testing for SQL Server |
| **utPLSQL** | Oracle | Testing framework for Oracle PL/SQL |

---

## Interoperability

### Language Bindings

| Interface | Language | Description |
|-----------|----------|-------------|
| **JDBC** | Java | Standard database API |
| **ODBC** | Multiple | Universal database API |
| **psycopg2/3** | Python | PostgreSQL adapter |
| **database/sql** | Go | Standard library with driver interface |
| **sqlite3** | Python | Built-in SQLite support |
| **pg** | Node.js | PostgreSQL client |

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

## Design Patterns

### Pattern 1: Pivot / Crosstab

```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Pattern 2: Top-N Per Group

```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Pattern 3: Gaps and Islands

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

### Pattern 4: Slowly Changing Dimensions (SCD Type 2)

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

## Performance: Indexes and Query Planning

### How Indexes Work

An index is a data structure (usually a B-tree) that lets the database find rows without scanning the entire table.

```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Index Type | Best For | Example |
|-----------|----------|---------|
| **B-tree** (default) | Equality and range queries | `WHERE age > 25 AND age < 35` |
| **Hash** | Exact equality only | `WHERE email = 'x@y.com'` |
| **GIN** | Full-text search, arrays, JSON | `WHERE description @@ 'search term'` |
| **GiST** | Geometric/spatial data | `WHERE location <-> point(x,y) < 1000` |

### Reading Query Plans

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

## SQL Dialects

| Feature | PostgreSQL | MySQL | SQL Server | SQLite |
|---------|-----------|-------|------------|--------|
| Auto-increment | `BIGSERIAL` / `GENERATED ALWAYS` | `AUTO_INCREMENT` | `IDENTITY` | `INTEGER PRIMARY KEY AUTOINCREMENT` |
| String concat | `\|\|` | `CONCAT()` | `+` or `CONCAT()` | `\|\|` |
| Date functions | `NOW()`, `AGE()` | `NOW()`, `DATEDIFF()` | `GETDATE()`, `DATEDIFF()` | `DATE('now')` |
| JSON support | Excellent (`jsonb`) | Good (`JSON`) | Good (`JSON`) | Basic (`JSON1`) |
| Full-text search | Built-in (`tsvector`) | Built-in | Built-in | Limited |
| Window functions | Yes | Yes (8.0+) | Yes | Yes |

---

## Deployment

### Database Deployment Strategies

| Strategy | Description | Risk Level |
|----------|-------------|------------|
| **Migration files** | Versioned SQL scripts applied in order | Low |
| **Blue-green deploy** | Two identical databases; switch traffic | Low |
| **Expand-contract** | Add new column, dual-write, migrate, drop old | Low |
| **Direct DDL** | Running ALTER TABLE directly on production | High |

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

## When to Use SQL

| Scenario | Why SQL | Alternative |
|----------|---------|-------------|
| Relational data with complex queries | That is what SQL is designed for | --- |
| Transactional integrity (ACID) | SQL databases guarantee consistency | --- |
| Reporting and analytics | Aggregations, window functions, CTEs | Python (Pandas) for very complex analysis |
| Data integrity constraints | Foreign keys, CHECK, UNIQUE, NOT NULL | Application-level validation (weaker) |
| Simple key-value storage | Overkill for this use case | Redis, DynamoDB |
| Highly unstructured data | Schema rigidity is a problem | MongoDB, document databases |
| Massive horizontal scaling | Hard to shard SQL databases | Cassandra, DynamoDB, CockroachDB |

---

## Synthetic Q&A

### Q1: What is the difference between `WHERE` and `HAVING`?

**A:** `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation:

```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: How do window functions differ from GROUP BY?

**A:** Window functions compute across rows without collapsing them:

```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: How do I optimize slow queries?

**A:** Key strategies:
- Add indexes on columns used in `WHERE`, `JOIN`, and `ORDER BY`
- Avoid `SELECT *` — select only needed columns
- Use `EXPLAIN` / `EXPLAIN ANALYZE` to read query plans
- Replace subqueries with JOINs where possible
- Use CTEs for readability (usually no performance penalty)
- Avoid functions on indexed columns in WHERE: use `WHERE date >= '2024-01-01'` not `WHERE YEAR(date) = 2024`

### Q4: What are CTEs and when should I use them?

**A:** Common Table Expressions create named temporary result sets:

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

### Q5: How do I handle NULL values correctly?

**A:** NULL represents unknown — it is not equal to anything, including itself:

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

## Chain-of-Thought Problem Solving

### Problem 1: Finding the Top N per Group

**Step 1: Understand the Problem**
Find the 3 highest-paid employees in each department.

**Step 2: Identify the Approach**
Use a window function with `ROW_NUMBER()` partitioned by department.

**Step 3: Implement**
```sql
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

**Step 4: Verify**
Check that each department has at most 3 rows. Handle ties with `DENSE_RANK()` if needed.

### Problem 2: Building a Year-over-Year Growth Report

**Step 1: Understand the Problem**
Calculate monthly revenue and year-over-year growth percentage.

**Step 2: Identify the Approach**
Use `DATE_TRUNC` for grouping and `LAG()` window function for previous year comparison.

**Step 3: Implement**
```sql
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

**Step 4: Verify**
Check first 12 months have NULL for previous year. Validate growth percentages against known figures.

### Problem 3: Pivoting Rows to Columns

**Step 1: Understand the Problem**
Transform status counts from rows to columns.

**Step 2: Identify the Approach**
Use conditional aggregation (`CASE` inside `SUM`).

**Step 3: Implement**
```sql
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

**Step 4: Extend**
Add percentage columns and running totals.

---

## Summary

SQL is a 50-year-old language that remains essential. Every developer, data scientist, and analyst needs to know it. The core language is standardised and portable; the dialect differences are manageable. Modern SQL (with window functions, CTEs, and JSON support) is expressive enough for most data tasks. The key skills are: writing efficient queries, understanding indexes, reading query plans, and designing good schemas. If you work with data at all, SQL is non-negotiable.