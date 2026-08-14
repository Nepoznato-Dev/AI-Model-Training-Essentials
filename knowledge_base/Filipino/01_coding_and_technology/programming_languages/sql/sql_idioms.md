---
# Metadata
title: "SQL — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, efficient SQL."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [sql, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# SQL — Mga Idiomatic Pattern at Pinakamahuhusay na Kasanayan
Sinasaklaw ng gabay na ito ang mga idiomatic pattern at pinakamahuhusay na kagawian para sa pagsusulat ng malinis, mahusay na SQL.
---

## Pag-format at Estilo
```sql
-- ✅ Consistent formatting
SELECT
    u.id,
    u.name,
    u.email,
    COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.created_at >= '2024-01-01'
  AND u.status = 'active'
GROUP BY u.id, u.name, u.email
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC
LIMIT 20;

-- ✅ Use aliases
SELECT u.name, o.total
FROM users AS u
JOIN orders AS o ON o.user_id = u.id;

-- ✅ Explicit column names (never SELECT *)
SELECT id, name, email FROM users;
```

---

## Sumali at Relasyon
```sql
-- ✅ Explicit JOIN syntax
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON o.user_id = u.id;

-- ✅ LEFT JOIN for optional relationships
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON o.user_id = u.id;

-- ✅ Self-join
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;
```

---

## Mga Pag-andar ng Window
```sql
-- ✅ ROW_NUMBER for ranking
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- ✅ Running total
SELECT
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- ✅ Partition by group
SELECT
    department,
    name,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

---

## Mga CTE at Subquery
```sql
-- ✅ CTEs for readability
WITH active_users AS (
    SELECT id, name, email
    FROM users
    WHERE status = 'active'
),
user_orders AS (
    SELECT user_id, COUNT(*) AS order_count, SUM(total) AS total_spent
    FROM orders
    GROUP BY user_id
)
SELECT u.name, COALESCE(o.order_count, 0) AS orders
FROM active_users u
LEFT JOIN user_orders o ON o.user_id = u.id;

-- ✅ Recursive CTE
WITH RECURSIVE hierarchy AS (
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e
    JOIN hierarchy h ON h.id = e.manager_id
)
SELECT * FROM hierarchy;
```

---

## Pagganap
```sql
-- ✅ SARGable queries
-- ❌
WHERE YEAR(created_at) = 2024
-- ✅
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'

-- ✅ Use EXISTS instead of IN for subqueries
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);

-- ✅ Covering indexes
CREATE INDEX idx_users_active ON users(status, created_at) INCLUDE (name, email);

-- ✅ EXPLAIN ANALYZE for tuning
EXPLAIN ANALYZE SELECT ...;
```

---

## Buod
Binibigyang-diin ng mga SQL idiom ang: tahasang mga pangalan ng column, pare-parehong pag-format, mga CTE para sa pagiging madaling mabasa, mga function ng window para sa analytics, SARGable na mga query para sa pagganap, at`EXPLAIN ANALYZE`para sa pag-tune. Sundin ang SQLFluff para sa pag-format at palaging gumamit ng mga parameterized na query para maiwasan ang SQL injection.