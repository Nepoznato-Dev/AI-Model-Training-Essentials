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

# SQL — عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز ایس کیو ایل میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کو تصحیح کے ساتھ کیٹلاگ کرتا ہے۔
---

## 1. پروڈکشن میں * منتخب کریں۔
```sql
-- ❌ WRONG — returns all columns, breaks on schema change
SELECT * FROM users WHERE active = true;

-- ✅ CORRECT — specify columns
SELECT id, name, email FROM users WHERE active = true;
```

---

## 2. NULL موازنہ
```sql
-- ❌ WRONG — NULL = NULL is NULL, not TRUE
SELECT * FROM users WHERE email = NULL;  -- returns nothing

-- ✅ CORRECT — use IS NULL
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 3. ایس کیو ایل انجیکشن
```sql
-- ❌ WRONG — string concatenation
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- ✅ CORRECT — parameterized queries
-- SELECT * FROM users WHERE name = ?;
-- Then bind userInput to the parameter
```

---

## 4. اشاریہ جات کا استعمال نہیں کرنا (سارگیبل سوالات)
```sql
-- ❌ WRONG — function on column prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- ✅ CORRECT — range condition (SARGable)
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01';
```

---

## 5. مضمر قسم کی تبدیلی
```sql
-- ❌ WRONG — comparing string to number
SELECT * FROM users WHERE phone = 1234567890;
-- phone is VARCHAR, implicit conversion may skip index

-- ✅ CORRECT — match types
SELECT * FROM users WHERE phone = '1234567890';
```

---

## 6. کارٹیشین مصنوعات
```sql
-- ❌ WRONG — missing JOIN condition
SELECT * FROM users, orders;  -- every user × every order!

-- ✅ CORRECT — explicit JOIN with condition
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 7. تمام غیر جمع شدہ کالموں کے بغیر گروپ بنائیں
```sql
-- ❌ WRONG — non-aggregated column not in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name;
-- email is ambiguous!

-- ✅ CORRECT — all non-aggregated columns in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name, email;
```

---

## خلاصہ
ایس کیو ایل کی وضاحتی نوعیت کارکردگی کے جال کو چھپاتی ہے: ہمیشہ کالم کی وضاحت کریں (`SELECT *` نہیں)، null چیکس کے لیے`IS NULL`استعمال کریں، انجیکشن کو روکنے کے لیے سوالات کو پیرامیٹرائز کریں، انڈیکس کے استعمال کے لیے سارگیبل شرائط لکھیں، موازنہ میں میچ کی قسمیں، واضح استعمال کریں شامل کریں BONGRUP اور تمام Nonregglums. اچھا SQL سیٹوں میں سوچنے کے بارے میں ہے، قطاروں میں نہیں۔