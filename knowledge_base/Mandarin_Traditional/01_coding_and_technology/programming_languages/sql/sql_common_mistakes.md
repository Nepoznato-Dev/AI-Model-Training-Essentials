---
# Metadata
title: "SQL — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in SQL with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [sql, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# SQL — 常見錯誤與反模式
本文檔列出了 SQL 中最常見的錯誤、陷阱和反模式，並進行了修正。
---

## 1. 在生產中選擇 *
```sql
-- ❌ WRONG — returns all columns, breaks on schema change
SELECT * FROM users WHERE active = true;

-- ✅ CORRECT — specify columns
SELECT id, name, email FROM users WHERE active = true;
```

---

## 2. NULL 比較
```sql
-- ❌ WRONG — NULL = NULL is NULL, not TRUE
SELECT * FROM users WHERE email = NULL;  -- returns nothing

-- ✅ CORRECT — use IS NULL
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 3. SQL注入
```sql
-- ❌ WRONG — string concatenation
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- ✅ CORRECT — parameterized queries
-- SELECT * FROM users WHERE name = ?;
-- Then bind userInput to the parameter
```

---

## 4. 不使用索引（SARGable 查詢）
```sql
-- ❌ WRONG — function on column prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- ✅ CORRECT — range condition (SARGable)
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01';
```

---

## 5. 隱式型別轉換
```sql
-- ❌ WRONG — comparing string to number
SELECT * FROM users WHERE phone = 1234567890;
-- phone is VARCHAR, implicit conversion may skip index

-- ✅ CORRECT — match types
SELECT * FROM users WHERE phone = '1234567890';
```

---

## 6.笛卡兒積
```sql
-- ❌ WRONG — missing JOIN condition
SELECT * FROM users, orders;  -- every user × every order!

-- ✅ CORRECT — explicit JOIN with condition
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 7. 沒有所有非聚合列的 GROUP BY
```sql
-- ❌ WRONG — non-aggregated column not in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name;
-- email is ambiguous!

-- ✅ CORRECT — all non-aggregated columns in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name, email;
```

---

＃＃ 概括
SQL 的聲明性本質隱藏了效能陷阱：始終指定列（而不是`SELECT *`）、使用`IS NULL`進行 null 檢查、參數化查詢以防止注入、為索引使用編寫 SARGable 條件、比較中的匹配類型、使用顯式 JOIN 以及在 GROUP BY 中包含所有非聚合列。好的 SQL 是在集合中思考，而不是在行中思考。