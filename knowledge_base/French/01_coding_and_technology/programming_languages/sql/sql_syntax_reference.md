---
# Metadata
title: "SQL — Syntax Reference"
description: "Detailed syntax reference for SQL covering queries, joins, window functions, CTEs, indexes, and database design patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [sql, syntax-reference, queries, joins, window-functions, cte, database, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# SQL — Référence de syntaxe
Ce document fournit une référence de syntaxe complète et structurée pour SQL (ANSI SQL avec des notes sur les différences de dialecte PostgreSQL/MySQL/SQLite). Il complète la référence SQL principale en se concentrant sur les modèles de requête exhaustifs, les fonctions de fenêtre, les CTE et la conception de bases de données.
---

## Syntaxe de requête principale
### SÉLECTIONNER
```sql
-- Basic query
SELECT name, email, age
FROM users
WHERE age >= 18
ORDER BY name ASC
LIMIT 10 OFFSET 20;

-- DISTINCT
SELECT DISTINCT department FROM employees;

-- Aliases
SELECT u.name AS username, o.total AS order_total
FROM users u
JOIN orders o ON u.id = o.user_id;

-- Expressions
SELECT
    first_name || ' ' || last_name AS full_name,
    COALESCE(nickname, first_name, 'Anonymous') AS display_name,
    CASE
        WHEN age < 18 THEN 'minor'
        WHEN age < 65 THEN 'adult'
        ELSE 'senior'
    END AS age_group,
    salary * 12 AS annual_salary
FROM employees;

-- NULL handling
SELECT * FROM users WHERE email IS NOT NULL;
SELECT COALESCE(phone, 'N/A') AS phone FROM contacts;
SELECT NULLIF(status, '') AS status FROM orders;
```

### OÙ
```sql
-- Comparison
WHERE age > 18
WHERE status = 'active'
WHERE created_at >= '2024-01-01'

-- Logical
WHERE age >= 18 AND status = 'active'
WHERE department = 'IT' OR department = 'Engineering'
WHERE NOT is_deleted

-- IN / NOT IN
WHERE department IN ('IT', 'Engineering', 'Sales')
WHERE id NOT IN (SELECT user_id FROM banned_users)

-- BETWEEN
WHERE salary BETWEEN 50000 AND 100000
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31'

-- LIKE / ILIKE (pattern matching)
WHERE name LIKE 'A%'           -- starts with A
WHERE name LIKE '%smith%'      -- contains smith
WHERE name ILIKE '%SMITH%'     -- case-insensitive (PostgreSQL)

-- EXISTS
WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id)

-- IS NULL / IS NOT NULL
WHERE email IS NULL
WHERE phone IS NOT NULL
```

---

## Rejoint
```sql
-- INNER JOIN (matching rows in both)
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN (all from left, matching from right)
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN (all from right, matching from left)
SELECT u.name, o.total
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- FULL OUTER JOIN (all from both)
SELECT u.name, o.total
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;

-- CROSS JOIN (cartesian product)
SELECT d.name AS department, r.name AS role
FROM departments d
CROSS JOIN roles r;

-- Self join
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Multiple joins
SELECT u.name, o.id AS order_id, p.name AS product
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

---

## Agrégation et regroupement
```sql
-- Aggregate functions
SELECT
    department,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_salary,
    SUM(salary) AS total_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median
FROM employees
GROUP BY department
HAVING COUNT(*) > 5
ORDER BY avg_salary DESC;

-- GROUPING SETS (multiple grouping levels)
SELECT department, role, COUNT(*)
FROM employees
GROUP BY GROUPING SETS (
    (department, role),  -- by dept and role
    (department),        -- by dept only
    ()                   -- grand total
);

-- ROLLUP (hierarchical grouping)
SELECT department, role, COUNT(*)
FROM employees
GROUP BY ROLLUP (department, role);

-- STRING_AGG / GROUP_CONCAT
SELECT department,
       STRING_AGG(name, ', ' ORDER BY name) AS employees
FROM employees
GROUP BY department;
```

---

## Fonctions de la fenêtre
```sql
-- ROW_NUMBER, RANK, DENSE_RANK
SELECT name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
    RANK()       OVER (PARTITION BY department ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Running totals
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) AS running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7d
FROM daily_sales;

-- LAG / LEAD (compare with previous/next row)
SELECT month, revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month,
    LEAD(revenue, 1) OVER (ORDER BY month) AS next_month,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS month_over_month
FROM monthly_revenue;

-- NTILE (percentiles/buckets)
SELECT name, salary,
    NTILE(4) OVER (ORDER BY salary) AS quartile,
    NTILE(100) OVER (ORDER BY salary) AS percentile
FROM employees;

-- FIRST_VALUE / LAST_VALUE
SELECT name, department, salary,
    FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) AS highest_paid,
    LAST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS lowest_paid
FROM employees;
```

---

## CTE et sous-requêtes
```sql
-- Common Table Expression
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS total
    FROM orders
    GROUP BY 1
)
SELECT month, total,
    SUM(total) OVER (ORDER BY month) AS cumulative
FROM monthly_sales;

-- Recursive CTE
WITH RECURSIVE hierarchy AS (
    -- Base case
    SELECT id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e
    JOIN hierarchy h ON e.manager_id = h.id
)
SELECT * FROM hierarchy ORDER BY level, name;

-- Correlated subquery
SELECT name, salary,
    (SELECT AVG(salary) FROM employees e2
     WHERE e2.department = e1.department) AS dept_avg
FROM employees e1
WHERE salary > (
    SELECT AVG(salary) FROM employees
    WHERE department = e1.department
);

-- EXISTS vs IN
-- EXISTS is often faster for large datasets
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.total > 1000
);
```

---

## Modification des données
```sql
-- INSERT
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

INSERT INTO users (name, email)
SELECT first_name || ' ' || last_name, email
FROM temp_users WHERE status = 'verified';

-- UPDATE
UPDATE employees
SET salary = salary * 1.1,
    updated_at = NOW()
WHERE department = 'Engineering';

-- DELETE
DELETE FROM sessions WHERE expires_at < NOW();

-- UPSERT (dialect-specific)
-- PostgreSQL:
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON CONFLICT (id) DO UPDATE
SET name = EXCLUDED.name, email = EXCLUDED.email;

-- Transaction
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

---

## Indices et performances
```sql
-- Create indexes
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_orders_user_date ON orders (user_id, order_date);
CREATE UNIQUE INDEX idx_users_username ON users (LOWER(username));

-- Partial index (PostgreSQL)
CREATE INDEX idx_active_users ON users (email) WHERE is_active = true;

-- Check query plan
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 42 AND order_date > '2024-01-01';

-- View
CREATE VIEW active_orders AS
SELECT o.*, u.name AS user_name
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.status != 'cancelled';
```

---

## Résumé
La syntaxe de SQL est restée stable pendant 50 ans tout en évoluant continuellement. Les requêtes principales (SELECT, JOIN, WHERE, GROUP BY) sont standard dans toutes les bases de données. Les fonctions de fenêtre, les CTE et la prise en charge de JSON représentent les capacités du SQL moderne. L'utilisation efficace de SQL bénéficie de la compréhension de la manière dont le moteur de base de données traite les requêtes : lecture des plans d'exécution, compréhension des index et écriture d'opérations basées sur des ensembles au lieu de boucles procédurales. De solides compétences SQL sont précieuses pour toute personne travaillant avec des données.