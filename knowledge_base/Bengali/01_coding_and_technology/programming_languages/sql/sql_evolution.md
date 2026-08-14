---
# Metadata
title: "SQL — Version History & Evolution"
description: "Comprehensive version history and evolution of SQL from SEQUEL to modern SQL."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [sql, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# SQL — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| সিক্যুয়েল | 1974 | আসল আইবিএম গবেষণা ভাষা (চেম্বারলিন এবং বয়েস) |
| SQL-86 | 1986 | **প্রথম ANSI মান** (SQL-86) |
| SQL-89 | 1989 | ছোটখাট সংশোধন (অখণ্ডতার সীমাবদ্ধতা) |
| SQL-92 | 1992 | **মেজর**:`JOIN`, subqueries,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **নিয়মিত অভিব্যক্তি**, পুনরাবৃত্তিমূলক প্রশ্ন, ট্রিগার, BLOBs |
| SQL:2003 | 2003 | **উইন্ডো ফাংশন**, XML,`GENERATED`কলাম |
| SQL:2006 | 2006 | XML সমর্থন,`MERGE`|
| SQL:2008 | 2008 | `INSTEAD OF`ট্রিগার,`TRUNCATE`,`ORDER BY`ভিউ |
| SQL:2011 | 2011 | **টেম্পোরাল ডেটা** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **JSON সমর্থন**, সারি প্যাটার্ন স্বীকৃতি |
| SQL:2019 | 2019 | **পলিমরফিক টেবিল ফাংশন**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**,`SET`অপারেশন, অ্যারে বর্ধিতকরণ |
## প্রধান মাইলফলক
### সিক্যুয়েল এবং আর্লি এসকিউএল (1974-1986)
- **1974**: ডোনাল্ড চেম্বারলিন এবং রেমন্ড বয়েস আইবিএম রিসার্চে সিক্যুয়েল তৈরি করেন
- **লক্ষ্য**: সিস্টেম R (রিলেশনাল ডাটাবেস) এর জন্য ক্যোয়ারী ম্যানিপুলেশন
- ট্রেডমার্ক বিরোধের কারণে SQL (স্ট্রাকচার্ড কোয়েরি ল্যাঙ্গুয়েজ) নামকরণ করা হয়েছে
- **1986**: প্রথম ANSI মান (SQL-86)
- **1987**: ISO SQL-87 গ্রহণ করে
### SQL-92 — দ্য ফাউন্ডেশন (1992)
- **সবচেয়ে গুরুত্বপূর্ণ মান** — সমস্ত আধুনিক এসকিউএল এর থেকে এসেছে
- `INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`
- সাবকোয়ারি (নেস্টেড `SELECT`)
-`CASE`অভিব্যক্তি
- `COALESCE`,`NULLIF`
-`UNIQUE`,`CHECK`সীমাবদ্ধতা৷
- স্কিমা সংজ্ঞা (`CREATE SCHEMA`)
### SQL:1999 — আধুনিক SQL শুরু হয় (1999)
- রেগুলার এক্সপ্রেশন (`LIKE`,`SIMILAR TO`)
- পুনরাবৃত্তিমূলক প্রশ্ন (`WITH RECURSIVE`)
- ট্রিগার
- BLOB/CLOB (বাইনারী/অক্ষর বড় বস্তু)
- ব্যবহারকারী-সংজ্ঞায়িত প্রকার (UDTs)
- সাবকোয়েরিতে `ORDER BY`৷
### SQL:2003 — বিশ্লেষণ বিপ্লব (2003)
- **উইন্ডো ফাংশন**: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`,`SUM() OVER()`
- XML ডাটা টাইপ এবং ফাংশন
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(লেনদেন নিয়ন্ত্রণ)
- হ্যাশ ফাংশন
### SQL:2011 — টেম্পোরাল ডেটা (2011)
- **টেম্পোরাল টেবিল**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(স্ট্যান্ডার্ড `LIMIT`)
-`OFFSET`/`FETCH`পেজিনেশন
### SQL:2016–2023 — JSON & Beyond (2016–বর্তমান)
- **2016**: JSON ডেটা টাইপ,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: পলিমরফিক টেবিল ফাংশন,`LISTAGG`
- **2023**:`JSON_TABLE`(JSON-এর রিলেশনাল ভিউ),`SET`অপারেশন, অ্যারে বর্ধিতকরণ
## সিনট্যাক্স বিবর্তন
```sql
-- SQL-86: Basic queries
SELECT name, salary FROM employees WHERE salary > 50000;

-- SQL-92: JOINs, subqueries, CASE
SELECT e.name, d.department_name,
  CASE WHEN e.salary > 100000 THEN 'High'
       WHEN e.salary > 50000 THEN 'Medium'
       ELSE 'Low'
  END AS salary_band
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
WHERE e.hire_date > '2020-01-01';

-- SQL:1999: Recursive CTE
WITH RECURSIVE hierarchy AS (
  SELECT id, name, manager_id, 1 AS level
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, h.level + 1
  FROM employees e JOIN hierarchy h ON e.manager_id = h.id
)
SELECT * FROM hierarchy;

-- SQL:2003: Window functions
SELECT name, department_id, salary,
  RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank,
  SUM(salary) OVER (PARTITION BY department_id) AS dept_total
FROM employees;

-- SQL:2011: Temporal queries
SELECT * FROM employees
FOR SYSTEM_TIME AS OF '2024-01-01'
WHERE department_id = 5;

-- SQL:2016: JSON
SELECT JSON_VALUE(data, '$.name') AS name
FROM users
WHERE JSON_EXISTS(data, '$.address.zipcode');

-- SQL:2023: JSON_TABLE
SELECT jt.*
FROM users
CROSS JOIN JSON_TABLE(
  data, '$.orders[*]'
  COLUMNS (
    order_id INT PATH '$.id',
    amount DECIMAL(10,2) PATH '$.amount'
  )
) AS jt;
```

## বৈশিষ্ট্য বিবর্তন
```
SQL-86:   SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, basic WHERE
SQL-89:   Integrity constraints, GRANT/REVOKE
SQL-92:   JOIN, subqueries, CASE, COALESCE, CHECK, UNIQUE
SQL:1999: Regular expressions, recursive CTE, triggers, BLOB/CLOB, UDTs
SQL:2003: Window functions, XML, IDENTITY, SAVEPOINT
SQL:2006: XML functions, MERGE
SQL:2008: INSTEAD OF triggers, TRUNCATE, ORDER BY in views
SQL:2011: Temporal tables, FETCH FIRST/OFFSET
SQL:2016: JSON data type, JSON_VALUE/QUERY/EXISTS
SQL:2019: Polymorphic table functions, LISTAGG
SQL:2023: JSON_TABLE, SET operations, arrays
```

## মূল ডিজাইনের নীতি
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## প্রধান উপভাষা বিবর্তন
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## ইকোসিস্টেম বৃদ্ধি
```
1974: SEQUEL created at IBM Research
1986: SQL-86 — first ANSI standard
1992: SQL-92 — the foundation of modern SQL
1995: MySQL released — open source SQL
1996: PostgreSQL released — advanced open source SQL
2000: SQLite — embedded SQL (now in every phone)
2010: Cloud data warehouses (BigQuery, Redshift)
2020: DuckDB — analytical SQL in a single binary
2025: SQL is the universal language of data
       Every RDBMS, every cloud, every phone — SQL is everywhere
       50+ years old and still growing
```
