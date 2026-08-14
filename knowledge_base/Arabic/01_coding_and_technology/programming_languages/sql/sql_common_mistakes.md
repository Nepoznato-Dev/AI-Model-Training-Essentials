---
# Metadata
title: "SQL — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in SQL with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# SQL — الأخطاء الشائعة والأنماط المضادة
يقوم هذا المستند بفهرسة الأخطاء والفخاخ والأنماط المضادة الأكثر شيوعًا في SQL مع التصحيحات.
---

## 1. اختر * في الإنتاج
```sql
-- ❌ WRONG — returns all columns, breaks on schema change
SELECT * FROM users WHERE active = true;

-- ✅ CORRECT — specify columns
SELECT id, name, email FROM users WHERE active = true;
```

---

## 2. مقارنة فارغة
```sql
-- ❌ WRONG — NULL = NULL is NULL, not TRUE
SELECT * FROM users WHERE email = NULL;  -- returns nothing

-- ✅ CORRECT — use IS NULL
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 3. حقن SQL
```sql
-- ❌ WRONG — string concatenation
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- ✅ CORRECT — parameterized queries
-- SELECT * FROM users WHERE name = ?;
-- Then bind userInput to the parameter
```

---

## 4. عدم استخدام الفهارس (استعلامات SARGable)
```sql
-- ❌ WRONG — function on column prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- ✅ CORRECT — range condition (SARGable)
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01';
```

---

## 5. تحويل النوع الضمني
```sql
-- ❌ WRONG — comparing string to number
SELECT * FROM users WHERE phone = 1234567890;
-- phone is VARCHAR, implicit conversion may skip index

-- ✅ CORRECT — match types
SELECT * FROM users WHERE phone = '1234567890';
```

---

## 6. المنتجات الديكارتية
```sql
-- ❌ WRONG — missing JOIN condition
SELECT * FROM users, orders;  -- every user × every order!

-- ✅ CORRECT — explicit JOIN with condition
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 7. التجميع حسب بدون كافة الأعمدة غير المجمعة
```sql
-- ❌ WRONG — non-aggregated column not in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name;
-- email is ambiguous!

-- ✅ CORRECT — all non-aggregated columns in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name, email;
```

---

## ملخص
تخفي الطبيعة التعريفية لـ SQL مصائد الأداء: حدد دائمًا الأعمدة (وليس `SELECT *`)، واستخدم`IS NULL`لعمليات التحقق من القيمة الفارغة، وحدد معلمات الاستعلامات لمنع الحقن، واكتب شروط SARGable لاستخدام الفهرس، وأنواع المطابقة في المقارنات، واستخدم الصلات الصريحة، وقم بتضمين جميع الأعمدة غير المجمعة في GROUP BY. لغة SQL الجيدة تدور حول التفكير في مجموعات، وليس في صفوف.