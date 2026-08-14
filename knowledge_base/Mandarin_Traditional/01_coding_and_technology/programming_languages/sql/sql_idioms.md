---
# Metadata
title: "SQL — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, efficient SQL."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# SQL — 慣用模式與最佳實踐
本指南涵蓋了編寫乾淨、高效 SQL 的慣用模式和最佳實踐。
---

## 格式和樣式
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

## 連結和關係
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

## 視窗函數
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

## CTE 和子查詢
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

＃＃ 表現
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

＃＃ 概括
SQL 慣用法強調：明確列名、一致的格式、用於可讀性的 CTE、用於分析的視窗函數、用於效能的 SARGable 查詢以及用於調優的 `EXPLAIN ANALYZE`。遵循 SQLFluff 進行格式化，並始終使用參數化查詢來防止 SQL 注入。