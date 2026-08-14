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

# SQL — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|続編 | 1974年 |オリジナルの IBM 研究言語 (Chamberlin & Boyce) |
| SQL-86 | 1986年 | **最初の ANSI 標準** (SQL-86) |
| SQL-89 | 1989年 |マイナー リビジョン (整合性制約) |
| SQL-92 | 1992年 | **主要**:`JOIN`、サブクエリ、`CASE`、`COALESCE`|
| SQL:1999 | 1999年 | **正規表現**、再帰クエリ、トリガー、BLOB |
| SQL:2003 | 2003年 | **ウィンドウ関数**、XML、`GENERATED` 列 |
| SQL:2006 | 2006年 | XML サポート、`MERGE` |
| SQL:2008 | 2008年 | `INSTEAD OF`トリガー、ビュー内の`TRUNCATE`、`ORDER BY`|
| SQL:2011 | 2011年 | **時間データ** (`AS OF`、`FOR SYSTEM_TIME`)、`FETCH FIRST`|
| SQL:2016 | 2016年 | **JSON サポート**、行パターン認識 |
| SQL:2019 | 2019年 | **多態性テーブル関数**、`LISTAGG` |
| SQL:2023 | 2023年 | **`JSON_TABLE`**、`SET` 操作、配列の機能強化 |
## 主要なマイルストーン
### SEQUEL と初期の SQL (1974 ～ 1986 年)
- **1974**: ドナルド・チェンバリンとレイモンド・ボイスがIBM ResearchでSEQUELを作成
- **目標**: System R (リレーショナル データベース) のクエリ操作
- 商標権の競合のため、SQL (Structured Query Language) に名前変更されました。
- **1986**: 最初の ANSI 標準 (SQL-86)
- **1987**: ISO が SQL-87 を採用
### SQL-92 — 財団 (1992)
- **最も重要な標準** — すべての最新の SQL はこの標準から派生しています。
- `INNER JOIN`、`LEFT JOIN`、`RIGHT JOIN` 
- サブクエリ (ネストされた`SELECT`)
- `CASE`式
- `COALESCE`、`NULLIF` 
-`UNIQUE`、`CHECK`制約
- スキーマ定義 (`CREATE SCHEMA`)
### SQL:1999 — モダン SQL の始まり (1999)
- 正規表現 (`LIKE`、`SIMILAR TO`)
- 再帰クエリ (`WITH RECURSIVE`)
- トリガー
- BLOB/CLOB (バイナリ/文字ラージ オブジェクト)
- ユーザー定義型 (UDT)
- サブクエリ内の `ORDER BY`
### SQL:2003 — 分析革命 (2003)
- **ウィンドウ関数**:`ROW_NUMBER()`、`RANK()`、`DENSE_RANK()`、`LAG()`、`LEAD()`、`SUM() OVER()`
- XMLのデータ型と関数
- XQZマーカー6XQZ 
-`SAVEPOINT`(トランザクション制御)
- ハッシュ関数
### SQL:2011 — 一時データ (2011)
- **テンポラル テーブル**:`FOR SYSTEM_TIME AS OF`、`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(標準`LIMIT`)
-`OFFSET`/`FETCH`ページネーション
### SQL:2016–2023 — JSON 以降 (2016 年から現在)
- **2016**: JSON データ型、`JSON_VALUE`、`JSON_QUERY`、`JSON_EXISTS`
- **2019**: ポリモーフィック テーブル関数、`LISTAGG` 
- **2023**:`JSON_TABLE`(JSON のリレーショナル ビュー)、`SET` 操作、配列の機能強化
## 構文の進化
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

## 機能の進化
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

## 主要な設計原則
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## 方言の主な進化
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## エコシステムの成長
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
