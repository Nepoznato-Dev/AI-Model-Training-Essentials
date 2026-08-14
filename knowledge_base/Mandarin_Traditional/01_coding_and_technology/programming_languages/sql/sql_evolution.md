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
# SQL — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|續集 | 1974 | IBM 原創研究語言 (Chamberlin & Boyce) |
| SQL-86 | 1986 | **第一個 ANSI 標準** (SQL-86) |
| SQL-89 | 1989 |小修改（完整性限制）|
| SQL-92 | 1992 | **主要**：`JOIN`、子查詢、`CASE` 、`COALESCE`|
| SQL：1999 | 1999 | **正規表示式**、遞迴查詢、觸發器、BLOB |
| SQL：2003 | 2003 | **視窗函數**、XML、`GENERATED` 欄位 |
| SQL：2006 | 2006 | XML 支持，`MERGE` |
| SQL：2008 | 2008 | 視圖中的`INSTEAD OF`觸發器、`TRUNCATE` 、`ORDER BY`|
| SQL：2011 | 2011 | **時間資料** (`AS OF`、`FOR SYSTEM_TIME`)、`FETCH FIRST` |
| SQL：2016 | 2016 | 2016 **JSON 支援**，行模式識別 |
| SQL：2019 | 2019 | 2019 **多型表函數**，`LISTAGG` |
| SQL：2023 | 2023 | **`JSON_TABLE`**、`SET` 操作、陣列增強 |
## 主要里程碑
### SEQUEL 與早期 SQL (1974–1986)
- **1974**：Donald Chamberlin 和 Raymond Boyce 在 IBM 研究中心創建了 SEQUEL
- **目標**：System R（關聯式資料庫）的查詢操作
- 因商標衝突而更名為 SQL（結構化查詢語言）
- **1986**：第一個 ANSI 標準 (SQL-86)
- **1987**：ISO 採用 SQL-87
### SQL-92 — 基金會 (1992)
- **最重要的標準** — 所有現代 SQL 都源自於此
- `INNER JOIN`、`LEFT JOIN`、`RIGHT JOIN`
- 子查詢（嵌套`SELECT`）
-`CASE`表達式
-`COALESCE`, `NULLIF`
-`UNIQUE`、`CHECK`約束
- 模式定義 (`CREATE SCHEMA`)
### SQL:1999 — 現代 SQL 開始 (1999)
- 正規表示式（`LIKE`，`SIMILAR TO`）
- 遞迴查詢（`WITH RECURSIVE`）
- 觸發器
- BLOB/CLOB（二進位/字元大物件）
- 使用者定義類型（UDT）
- 子查詢中的 `ORDER BY`
### SQL:2003 — 分析革命 (2003)
- **視窗函數**：`ROW_NUMBER()`、`RANK()`、`DENSE_RANK()`、`LAG()`、`LEAD()`、 `SUM() OVER()`
- XML資料型別和函數
- `GENERATED ALWAYS AS IDENTITY`
- `SAVEPOINT`（事務控制）
- 哈希函數
### SQL:2011 — 時態資料 (2011)
- **時態表**：`FOR SYSTEM_TIME AS OF`、 `VERSIONING`
- `FETCH FIRST n ROWS ONLY`（標準`LIMIT`）
-`OFFSET`/`FETCH`分頁
### SQL:2016–2023 — JSON 及其他（2016 年至今）
- **2016**：JSON 資料型，`JSON_VALUE`、`JSON_QUERY`、 `JSON_EXISTS`
- **2019**：多型表函數，`LISTAGG`
- **2023**：`JSON_TABLE`（JSON 的關係視圖）、`SET` 操作、陣列增強
## 語法演變
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

## 功能演變
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

## 關鍵設計原則
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## 主要方言的演變
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## 生態系成長
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
