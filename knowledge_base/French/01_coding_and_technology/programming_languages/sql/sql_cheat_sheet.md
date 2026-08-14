<!--
---
# Metadata
title: "SQL — Cheat Sheet"
description: "Quick-reference cheat sheet for SQL queries, DDL, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [sql, database, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# SQL — Aide-mémoire
## SÉLECTIONNER les bases
```sql
-- Basic query
SELECT * FROM users;
SELECT name, email FROM users;
SELECT name AS user_name FROM users;

-- WHERE clause
SELECT * FROM users WHERE age >= 18;
SELECT * FROM users WHERE status IN ('active', 'pending');
SELECT * FROM users WHERE name LIKE 'A%';
SELECT * FROM users WHERE name LIKE '%son';
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
SELECT * FROM users WHERE email IS NOT NULL;
SELECT * FROM users WHERE age > 18 AND status = 'active';

-- DISTINCT
SELECT DISTINCT department FROM employees;
SELECT DISTINCT department, role FROM employees;

-- ORDER BY
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY age DESC, name ASC;

-- LIMIT / OFFSET
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;
```

## Agrégation
```sql
-- Aggregate functions
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT department) FROM employees;
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(age), MAX(age) FROM users;

-- GROUP BY
SELECT department, COUNT(*) AS cnt
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- GROUP BY with multiple columns
SELECT department, role, COUNT(*) AS cnt
FROM employees
GROUP BY department, role;
```

## Rejoint
```sql
-- INNER JOIN
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN
SELECT u.name, o.total
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- FULL OUTER JOIN
SELECT u.name, o.total
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;

-- CROSS JOIN
SELECT u.name, d.name
FROM users u
CROSS JOIN departments d;

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

## Sous-requêtes
```sql
-- Scalar subquery
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- IN subquery
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- EXISTS
SELECT name FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);

-- Derived table
SELECT dept.avg_sal, d.name
FROM (SELECT department_id, AVG(salary) AS avg_sal
      FROM employees GROUP BY department_id) dept
JOIN departments d ON dept.department_id = d.id;

-- Correlated subquery
SELECT name, salary
FROM employees e1
WHERE salary = (SELECT MAX(salary) FROM employees WHERE department = e1.department);
```

## Fonctions de la fenêtre
```sql
-- ROW_NUMBER, RANK, DENSE_RANK
SELECT name, department, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
    RANK() OVER (ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Partition by
SELECT name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- Running total
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- Moving average
SELECT date, amount,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM transactions;

-- LAG / LEAD
SELECT date, amount,
    LAG(amount, 1) OVER (ORDER BY date) AS prev_amount,
    LEAD(amount, 1) OVER (ORDER BY date) AS next_amount
FROM transactions;

-- NTILE
SELECT name, salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

##DDL
```sql
-- Create table
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    age         INTEGER CHECK (age >= 0),
    status      VARCHAR(20) DEFAULT 'active',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alter table
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users ALTER COLUMN name SET NOT NULL;
ALTER TABLE users RENAME COLUMN name TO full_name;

-- Index
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_name_age ON users(name, age);
CREATE UNIQUE INDEX idx_users_email_unique ON users(LOWER(email));

-- Drop
DROP TABLE IF EXISTS users;
DROP INDEX IF EXISTS idx_users_email;

-- Constraints
ALTER TABLE orders ADD CONSTRAINT fk_user
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
```

##LML
```sql
-- Insert
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email) VALUES ('Alice', 'a@b.com'), ('Bob', 'b@c.com');

-- Update
UPDATE users SET name = 'Bob' WHERE id = 1;
UPDATE users SET status = 'inactive', updated_at = NOW() WHERE last_login < '2024-01-01';

-- Delete
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE status = 'inactive' AND last_login < '2023-01-01';

-- Upsert (PostgreSQL)
INSERT INTO users (name, email) VALUES ('Alice', 'a@b.com')
ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name;

-- Upsert (MySQL)
INSERT INTO users (name, email) VALUES ('Alice', 'a@b.com')
ON DUPLICATE KEY UPDATE name = VALUES(name);
```

## CTE et avancé
```sql
-- CTE (Common Table Expression)
WITH active_users AS (
    SELECT id, name FROM users WHERE status = 'active'
)
SELECT au.name, COUNT(o.id) AS order_count
FROM active_users au
LEFT JOIN orders o ON au.id = o.user_id
GROUP BY au.name;

-- Recursive CTE
WITH RECURSIVE hierarchy AS (
    SELECT id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e
    JOIN hierarchy h ON e.manager_id = h.id
)
SELECT * FROM hierarchy;

-- CASE expression
SELECT name,
    CASE
        WHEN age >= 65 THEN 'senior'
        WHEN age >= 18 THEN 'adult'
        ELSE 'minor'
    END AS age_group
FROM users;

-- COALESCE / NULLIF
SELECT COALESCE(phone, email, 'N/A') AS contact FROM users;
SELECT NULLIF(status, 'unknown') AS real_status FROM users;

-- PIVOT (using CASE)
SELECT department,
    SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male,
    SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female
FROM employees
GROUP BY department;
```
