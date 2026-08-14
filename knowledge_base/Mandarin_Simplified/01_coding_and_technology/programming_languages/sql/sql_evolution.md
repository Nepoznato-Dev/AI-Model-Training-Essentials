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
# SQL — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|续集 | 1974 | IBM 原创研究语言 (Chamberlin & Boyce) |
| SQL-86 | 1986 | **第一个 ANSI 标准** (SQL-86) |
| SQL-89 | 1989 |小修改（完整性约束）|
| SQL-92 | 1992 | **主要**：`JOIN`、子查询、`CASE` 、`COALESCE`|
| SQL：1999 | 1999 | **正则表达式**、递归查询、触发器、BLOB |
| SQL：2003 | 2003 | **窗口函数**、XML、`GENERATED` 列 |
| SQL：2006 | 2006 | XML 支持，`MERGE` |
| SQL：2008 | 2008 |  视图中的`INSTEAD OF`触发器、`TRUNCATE` 、`ORDER BY`|
| SQL：2011 | 2011 | **时间数据** (`AS OF`、`FOR SYSTEM_TIME`)、`FETCH FIRST` |
| SQL：2016 | 2016 | 2016 **JSON 支持**，行模式识别 |
| SQL：2019 | 2019 | 2019 **多态表函数**，`LISTAGG` |
| SQL：2023 | 2023 | **`JSON_TABLE`**、`SET` 操作、数组增强 |
## 主要里程碑
### SEQUEL 和早期 SQL (1974–1986)
- **1974**：Donald Chamberlin 和 Raymond Boyce 在 IBM 研究中心创建了 SEQUEL
- **目标**：System R（关系数据库）的查询操作
- 由于商标冲突而更名为 SQL（结构化查询语言）
- **1986**：第一个 ANSI 标准 (SQL-86)
- **1987**：ISO 采用 SQL-87
### SQL-92 — 基金会 (1992)
- **最重要的标准** — 所有现代 SQL 都源于此
- `INNER JOIN`、`LEFT JOIN`、`RIGHT JOIN` 
- 子查询（嵌套`SELECT`）
-`CASE`表达式
-`COALESCE`,`NULLIF`
-`UNIQUE`、`CHECK`约束
- 模式定义 (`CREATE SCHEMA`)
### SQL:1999 — 现代 SQL 开始 (1999)
- 正则表达式（`LIKE`，`SIMILAR TO`）
- 递归查询（`WITH RECURSIVE`）
- 触发器
- BLOB/CLOB（二进制/字符大对象）
- 用户定义类型（UDT）
- 子查询中的 `ORDER BY`
### SQL:2003 — 分析革命 (2003)
- **窗口函数**：`ROW_NUMBER()`、`RANK()`、`DENSE_RANK()`、`LAG()`、`LEAD()`、`SUM() OVER()`
- XML数据类型和函数
-`GENERATED ALWAYS AS IDENTITY`
- `SAVEPOINT`（事务控制）
- 哈希函数
### SQL:2011 — 时态数据 (2011)
- **时态表**：`FOR SYSTEM_TIME AS OF`、`VERSIONING`
- `FETCH FIRST n ROWS ONLY`（标准`LIMIT`）
-`OFFSET`/`FETCH`分页
### SQL:2016–2023 — JSON 及其他（2016 年至今）
- **2016**：JSON 数据类型，`JSON_VALUE`、`JSON_QUERY`、`JSON_EXISTS`
- **2019**：多态表函数，`LISTAGG` 
- **2023**：`JSON_TABLE`（JSON 的关系视图）、`SET` 操作、数组增强
## 语法演变
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

## 功能演变
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

## 关键设计原则
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## 主要方言的演变
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## 生态系统增长
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
