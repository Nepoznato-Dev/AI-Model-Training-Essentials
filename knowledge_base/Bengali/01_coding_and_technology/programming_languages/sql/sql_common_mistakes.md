<!--
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

-->
# SQL — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ SQL-এ সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. প্রোডাকশনে * নির্বাচন করুন
```sql
-- ❌ WRONG — returns all columns, breaks on schema change
SELECT * FROM users WHERE active = true;

-- ✅ CORRECT — specify columns
SELECT id, name, email FROM users WHERE active = true;
```

---

## 2. NULL তুলনা
```sql
-- ❌ WRONG — NULL = NULL is NULL, not TRUE
SELECT * FROM users WHERE email = NULL;  -- returns nothing

-- ✅ CORRECT — use IS NULL
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 3. এসকিউএল ইনজেকশন
```sql
-- ❌ WRONG — string concatenation
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- ✅ CORRECT — parameterized queries
-- SELECT * FROM users WHERE name = ?;
-- Then bind userInput to the parameter
```

---

## 4. সূচী ব্যবহার না করা (SARGable Query)
```sql
-- ❌ WRONG — function on column prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- ✅ CORRECT — range condition (SARGable)
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01';
```

---

## 5. অন্তর্নিহিত প্রকার রূপান্তর
```sql
-- ❌ WRONG — comparing string to number
SELECT * FROM users WHERE phone = 1234567890;
-- phone is VARCHAR, implicit conversion may skip index

-- ✅ CORRECT — match types
SELECT * FROM users WHERE phone = '1234567890';
```

---

## 6. কার্টেসিয়ান পণ্য
```sql
-- ❌ WRONG — missing JOIN condition
SELECT * FROM users, orders;  -- every user × every order!

-- ✅ CORRECT — explicit JOIN with condition
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 7. সমস্ত অ-একত্রিত কলাম ছাড়াই গ্রুপ করুন
```sql
-- ❌ WRONG — non-aggregated column not in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name;
-- email is ambiguous!

-- ✅ CORRECT — all non-aggregated columns in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name, email;
```

---

## সারাংশ
এসকিউএল-এর ঘোষণামূলক প্রকৃতি পারফরম্যান্সের ফাঁদগুলিকে লুকিয়ে রাখে: সর্বদা কলামগুলি নির্দিষ্ট করুন (`SELECT *` নয়), শূন্য চেকের জন্য`IS NULL`ব্যবহার করুন, ইনজেকশন প্রতিরোধ করার জন্য প্রশ্নগুলিকে প্যারামিটারাইজ করুন, সূচক ব্যবহারের জন্য সার্গেবল শর্ত লিখুন, তুলনামূলকভাবে মিলের ধরনগুলি ব্যবহার করুন, সমস্ত নন-গ্রুপ-সংযোজন এবং সহ-সম্মিলিত সহ-সম্মিলিত অংশগুলি ব্যবহার করুন৷ ভালো এসকিউএল হল সেটে চিন্তা করা, সারি নয়।