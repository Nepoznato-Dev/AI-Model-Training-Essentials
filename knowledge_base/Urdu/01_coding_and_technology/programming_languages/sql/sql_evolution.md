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
# SQL - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| SEQUEL | 1974 | اصل IBM تحقیقی زبان (چیمبرلن اور بوائس) |
| SQL-86 | 1986 | **پہلا ANSI معیار** (SQL-86) |
| SQL-89 | 1989 | معمولی نظرثانی (سالمیت کی پابندیاں) |
| SQL-92 | 1992 | **میجر**:`JOIN`, subqueries ,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **باقاعدہ اظہار**، تکراری سوالات، محرکات، BLOBs |
| SQL:2003 | 2003 | **ونڈو کے افعال**، XML،`GENERATED`کالم |
| SQL:2006 | 2006 | XML سپورٹ،`MERGE`|
| SQL:2008 | 2008 | `INSTEAD OF`ٹرگرز،`TRUNCATE`,`ORDER BY`مناظر میں |
| SQL:2011 | 2011 | **عارضی ڈیٹا** (`AS OF`,`FOR SYSTEM_TIME`) ,`FETCH FIRST`|
| SQL:2016 | 2016 | **JSON سپورٹ**، قطار پیٹرن کی شناخت |
| SQL: 2019 | 2019 | **پولیمورفک ٹیبل کے افعال**،`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**،`SET`آپریشنز، صفوں میں اضافہ |
## اہم سنگ میل
### سیکوئل اور ابتدائی ایس کیو ایل (1974–1986)
- **1974**: ڈونلڈ چیمبرلن اور ریمنڈ بوائس نے آئی بی ایم ریسرچ میں سیکوئل بنایا
- **مقصد**: سسٹم R (ریلیشنل ڈیٹا بیس) کے لیے استفسار کی ہیرا پھیری
- ٹریڈ مارک تنازعہ کی وجہ سے ایس کیو ایل (سٹرکچرڈ کوئوری لینگویج) کا نام تبدیل کر دیا گیا۔
- **1986**: پہلا ANSI معیار (SQL-86)
- **1987**: ISO SQL-87 کو اپناتا ہے۔
### SQL-92 - دی فاؤنڈیشن (1992)
- **سب سے اہم معیار** — تمام جدید ایس کیو ایل اس سے نکلتے ہیں۔
- `INNER JOIN`، `LEFT JOIN`،`RIGHT JOIN`
- ذیلی سوالات (نیسٹڈ`SELECT`)
-`CASE`اظہار
- `COALESCE`،`NULLIF`
- `UNIQUE`،`CHECK`رکاوٹیں۔
- اسکیما کی تعریف (`CREATE SCHEMA`)
### ایس کیو ایل: 1999 - ماڈرن ایس کیو ایل بیگنس (1999)
- باقاعدہ اظہار (`LIKE`، `SIMILAR TO`)
- تکراری سوالات (`WITH RECURSIVE`)
- محرکات
- BLOB/CLOB (بائنری/کریکٹر بڑی اشیاء)
- صارف کی وضاحت شدہ اقسام (UDTs)
- ذیلی سوالات میں `ORDER BY`
### SQL:2003 — تجزیاتی انقلاب (2003)
- **ونڈو کے افعال**: `ROW_NUMBER()`، `RANK()`، `DENSE_RANK()`، `LAG()`، `LEAD()`،`SUM() OVER()`
- XML ڈیٹا کی قسم اور افعال
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(لین دین کنٹرول)
- ہیش کے افعال
### SQL:2011 — عارضی ڈیٹا (2011)
- **عارضی میزیں**: `FOR SYSTEM_TIME AS OF`،`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(معیاری `LIMIT`)
-`OFFSET`/`FETCH`صفحہ بندی
### SQL:2016–2023 — JSON & Beyond (2016–موجودہ)
- **2016**: JSON ڈیٹا کی قسم، `JSON_VALUE`، `JSON_QUERY`،`JSON_EXISTS`
- **2019**: پولیمورفک ٹیبل کے افعال،`LISTAGG`
- **2023**:`JSON_TABLE`(JSON کا رشتہ دار منظر)،`SET`آپریشنز، صفوں میں اضافہ
## نحوی ارتقاء
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

## فیچر ارتقاء
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

## ڈیزائن کے کلیدی اصول
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## بڑی بولی کا ارتقا
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## ماحولیاتی نظام کی نمو
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
