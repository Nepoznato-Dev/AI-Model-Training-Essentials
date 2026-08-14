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
# SQL — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 속편 | 1974년 | 원래 IBM 연구 언어(Chamberlin & Boyce) |
| SQL-86 | 1986 | **최초의 ANSI 표준**(SQL-86) |
| SQL-89 | 1989 | 사소한 개정(무결성 제약) |
| SQL-92 | 1992 | **주요**:`JOIN`, 하위 쿼리,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **정규식**, 재귀 쿼리, 트리거, BLOB |
| SQL:2003 | 2003년 | **창 함수**, XML,`GENERATED`열 |
| SQL:2006 | 2006년 | XML 지원,`MERGE`|
| SQL:2008 | 2008 | `INSTEAD OF`트리거,`TRUNCATE`,`ORDER BY`보기 |
| SQL:2011 | 2011 | **임시 데이터** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **JSON 지원**, 행 패턴 인식 |
| SQL:2019 | 2019 | **다형성 테이블 함수**,`LISTAGG`|
| SQL:2023 | 2023년 | **`JSON_TABLE`**,`SET`작업, 배열 개선 |
## 주요 이정표
### SEQUEL 및 초기 SQL(1974~1986)
- **1974**: Donald Chamberlin과 Raymond Boyce가 IBM Research에서 속편 제작
- **목표**: System R(관계형 데이터베이스)에 대한 쿼리 조작
- 상표권 충돌로 인해 SQL(Structured Query Language)로 이름이 변경되었습니다.
- **1986**: 최초의 ANSI 표준(SQL-86)
- **1987**: ISO가 SQL-87을 채택함
### SQL-92 — 재단(1992)
- **가장 중요한 표준** — 모든 최신 SQL은 이 표준에서 파생되었습니다.
- `INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`
- 하위 쿼리(중첩`SELECT`)
-`CASE`표현
- `COALESCE`,`NULLIF`
-`UNIQUE`,`CHECK`제약 조건
- 스키마 정의(`CREATE SCHEMA`)
### SQL:1999 — 최신 SQL 시작(1999)
- 정규 표현식(`LIKE`,`SIMILAR TO`)
- 재귀 쿼리(`WITH RECURSIVE`)
- 트리거
- BLOB/CLOB(바이너리/문자 대형 객체)
- 사용자 정의 유형(UDT)
- 하위 쿼리의 `ORDER BY`
### SQL:2003 — 분석 혁명(2003)
- **창 기능**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- XML 데이터 유형 및 기능
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(트랜잭션 제어)
- 해시 함수
### SQL:2011 — 임시 데이터(2011)
- **임시 테이블**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(표준 `LIMIT`)
-`OFFSET`/`FETCH`페이지 매김
### SQL:2016~2023 — JSON 및 그 이후(2016~현재)
- **2016**: JSON 데이터 유형,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: 다형성 테이블 함수,`LISTAGG`
- **2023**: `JSON_TABLE`(JSON의 관계형 보기),`SET`작업, 배열 개선
## 구문 진화
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

## 기능 진화
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

## 주요 디자인 원칙
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## 주요 방언의 진화
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## 생태계 성장
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
