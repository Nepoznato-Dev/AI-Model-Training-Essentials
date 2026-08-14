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
# SQL – Häufige Fehler und Anti-Patterns
Dieses Dokument katalogisiert die häufigsten Fehler, Fallstricke und Anti-Patterns in SQL mit Korrekturen.
---

## 1. SELECT * in Produktion
```sql
-- ❌ WRONG — returns all columns, breaks on schema change
SELECT * FROM users WHERE active = true;

-- ✅ CORRECT — specify columns
SELECT id, name, email FROM users WHERE active = true;
```

---

## 2. NULL-Vergleich
```sql
-- ❌ WRONG — NULL = NULL is NULL, not TRUE
SELECT * FROM users WHERE email = NULL;  -- returns nothing

-- ✅ CORRECT — use IS NULL
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 3. SQL-Injection
```sql
-- ❌ WRONG — string concatenation
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- ✅ CORRECT — parameterized queries
-- SELECT * FROM users WHERE name = ?;
-- Then bind userInput to the parameter
```

---

## 4. Keine Indizes verwenden (SARGable-Abfragen)
```sql
-- ❌ WRONG — function on column prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- ✅ CORRECT — range condition (SARGable)
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01';
```

---

## 5. Implizite Typkonvertierung
```sql
-- ❌ WRONG — comparing string to number
SELECT * FROM users WHERE phone = 1234567890;
-- phone is VARCHAR, implicit conversion may skip index

-- ✅ CORRECT — match types
SELECT * FROM users WHERE phone = '1234567890';
```

---

## 6. Kartesische Produkte
```sql
-- ❌ WRONG — missing JOIN condition
SELECT * FROM users, orders;  -- every user × every order!

-- ✅ CORRECT — explicit JOIN with condition
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 7. GROUP BY ohne alle nicht aggregierten Spalten
```sql
-- ❌ WRONG — non-aggregated column not in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name;
-- email is ambiguous!

-- ✅ CORRECT — all non-aggregated columns in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name, email;
```

---

## Zusammenfassung
Die deklarative Natur von SQL verbirgt Leistungsfallen: Geben Sie immer Spalten an (nicht `SELECT *`), verwenden Sie`IS NULL`für Nullprüfungen, parametrisieren Sie Abfragen, um eine Injektion zu verhindern, schreiben Sie SARGable-Bedingungen für die Indexverwendung, gleichen Sie Typen in Vergleichen ab, verwenden Sie explizite JOINs und schließen Sie alle nicht aggregierten Spalten in GROUP BY ein. Bei gutem SQL geht es darum, in Mengen zu denken, nicht in Zeilen.