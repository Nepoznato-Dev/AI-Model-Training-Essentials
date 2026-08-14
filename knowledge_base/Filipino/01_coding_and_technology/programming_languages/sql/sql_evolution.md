<!--
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

-->
# SQL — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| SEQUEL | 1974 | Orihinal na wika ng pananaliksik ng IBM (Chamberlin & Boyce) |
| SQL-86 | 1986 | **Unang pamantayan ng ANSI** (SQL-86) |
| SQL-89 | 1989 | Maliit na rebisyon (mga hadlang sa integridad) |
| SQL-92 | 1992 | **Major**:`JOIN`, mga subquery,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Mga regular na expression**, recursive query, trigger, BLOBs |
| SQL:2003 | 2003 | **Mga function ng window**, XML,`GENERATED`column |
| SQL:2006 | 2006 | Suporta sa XML,`MERGE`|
| SQL:2008 | 2008 | `INSTEAD OF`trigger,`TRUNCATE`,`ORDER BY`sa mga view |
| SQL:2011 | 2011 | **Temporal na data** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **JSON support**, row pattern recognition |
| SQL:2019 | 2019 | **Mga function ng polymorphic table**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**,`SET`na pagpapatakbo, mga pagpapahusay ng array |
## Mga Pangunahing Milestone
### SEQUEL at Early SQL (1974–1986)
- **1974**: Gumawa sina Donald Chamberlin at Raymond Boyce ng SEQUEL sa IBM Research
- **Layunin**: Pagmamanipula ng query para sa System R (relational database)
- Pinalitan ng pangalan sa SQL (Structured Query Language) dahil sa salungatan sa trademark
- **1986**: Unang pamantayan ng ANSI (SQL-86)
- **1987**: Pinagtibay ng ISO ang SQL-87
### SQL-92 — The Foundation (1992)
- **Ang pinakamahalagang pamantayan** — lahat ng modernong SQL ay nagmumula dito
-`INNER JOIN`,`LEFT JOIN`,`RIGHT JOIN`
- Mga Subquery (nakapugad`SELECT`)
-`CASE`expression
-`COALESCE`,`NULLIF`
-`UNIQUE`,`CHECK`hadlang
- Depinisyon ng schema (`CREATE SCHEMA`)
### SQL:1999 — Nagsisimula ang Modern SQL (1999)
- Mga regular na expression (`LIKE`,`SIMILAR TO`)
- Mga paulit-ulit na query (`WITH RECURSIVE`)
- Mga nag-trigger
- BLOB/CLOB (binary/character na malalaking bagay)
- Mga uri na tinukoy ng gumagamit (UDT)
-`ORDER BY`sa mga subquery
### SQL:2003 — Analytics Revolution (2003)
- **Mga function ng window**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- Uri ng data at mga function ng XML
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(kontrol sa transaksyon)
- Mga function ng hash
### SQL:2011 — Temporal na Data (2011)
- **Mga temporal na talahanayan**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(karaniwang`LIMIT`)
-`OFFSET`/`FETCH`pagination
### SQL:2016–2023 — JSON & Beyond (2016–kasalukuyan)
- **2016**: Uri ng data ng JSON,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: Mga function ng polymorphic table,`LISTAGG`
- **2023**:`JSON_TABLE`(relational view ng JSON),`SET`operations, array enhancements
## Syntax Evolution
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

## Ebolusyon ng Tampok
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Major Dialect Evolution
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Paglago ng Ecosystem
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
