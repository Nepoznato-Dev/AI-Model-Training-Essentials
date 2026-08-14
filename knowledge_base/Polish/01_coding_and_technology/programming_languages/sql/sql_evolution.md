---
# Metadata
title: "SQL — Version History & Evolution"
description: "Comprehensive version history and evolution of SQL from SEQUEL to modern SQL."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# SQL — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| KONTYNUACJA | 1974 | Oryginalny język badawczy IBM (Chamberlin & Boyce) |
| SQL-86 | 1986 | **Pierwszy standard ANSI** (SQL-86) |
| SQL-89 | 1989 | Drobna rewizja (ograniczenia integralności) |
| SQL-92 | 1992 | **Główne**:`JOIN`, podzapytania,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Wyrażenia regularne**, zapytania rekurencyjne, wyzwalacze, obiekty BLOB |
| SQL:2003 | 2003 | **Funkcje okna**, kolumny XML,`GENERATED`|
| SQL:2006 | 2006 | Obsługa XML,`MERGE`|
| SQL:2008 | 2008 |  Wyzwalacze `INSTEAD OF`,`TRUNCATE`,`ORDER BY`w widokach |
| SQL:2011 | 2011 | **Dane tymczasowe** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **Obsługa JSON**, rozpoznawanie wzorców wierszy |
| SQL:2019 | 2019 | **Funkcje tabel polimorficznych**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**, operacje `SET`, udoskonalenia tablicowe |
## Główne kamienie milowe
### SEQUEL i wczesny SQL (1974–1986)
- **1974**: Donald Chamberlin i Raymond Boyce tworzą SEQUEL w IBM Research
- **Cel**: Manipulacja zapytaniami dla Systemu R (relacyjna baza danych)
- Zmieniono nazwę na SQL (Structured Query Language) ze względu na konflikt znaków towarowych
- **1986**: Pierwszy standard ANSI (SQL-86)
- **1987**: ISO przyjmuje SQL-87
### SQL-92 — Fundacja (1992)
- **Najważniejszy standard** – od niego wywodzi się cały współczesny SQL
- `INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`
- Podzapytania (zagnieżdżone`SELECT`)
- Wyrażenie `CASE`
- `COALESCE`,`NULLIF`
- Ograniczenia`UNIQUE`, `CHECK`
- Definicja schematu (`CREATE SCHEMA`)
### SQL:1999 — początek nowoczesnego SQL (1999)
- Wyrażenia regularne (`LIKE`,`SIMILAR TO`)
- Zapytania rekurencyjne (`WITH RECURSIVE`)
- Wyzwalacze
- BLOB/CLOB (duże obiekty binarne/znakowe)
- Typy zdefiniowane przez użytkownika (UDT)
-`ORDER BY`w podzapytaniach
### SQL:2003 — rewolucja analityczna (2003)
- **Funkcje okna**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- Typ danych XML i funkcje
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(kontrola transakcji)
- Funkcje mieszające
### SQL:2011 — dane tymczasowe (2011)
- **Tabele czasowe**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(standardowy `LIMIT`)
- Paginacja`OFFSET`/ `FETCH`
### SQL:2016–2023 — JSON i nie tylko (2016 – obecnie)
- **2016**: typ danych JSON,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: Polimorficzne funkcje tabelowe,`LISTAGG`
- **2023**:`JSON_TABLE`(relacyjny widok JSON), operacje `SET`, ulepszenia tablicowe
## Ewolucja składni
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

## Ewolucja funkcji
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

## Kluczowe zasady projektowania
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Główna ewolucja dialektu
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Rozwój ekosystemu
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
