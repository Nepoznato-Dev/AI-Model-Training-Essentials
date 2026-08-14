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
# SQL – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| SEQUELA | 1974 | Linguagem de pesquisa original da IBM (Chamberlin & Boyce) |
| SQL-86 | 1986 | **Primeiro padrão ANSI** (SQL-86) |
| SQL-89 | 1989 | Pequena revisão (restrições de integridade) |
| SQL-92 | 1992 | **Principal**:`JOIN`, subconsultas,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Expressões regulares**, consultas recursivas, gatilhos, BLOBs |
| SQL:2003 | 2003 | **Funções de janela**, XML, colunas`GENERATED`|
| SQL:2006 | 2006 | Suporte XML,`MERGE`|
| SQL:2008 | 2008 |  Gatilhos `INSTEAD OF`,`TRUNCATE`,`ORDER BY`em visualizações |
| SQL:2011 | 2011 | **Dados temporais** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **Suporte JSON**, reconhecimento de padrão de linha |
| SQL:2019 | 2019 | **Funções de tabela polimórfica**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**, operações `SET`, melhorias de array |
## Marcos importantes
### SEQUEL e SQL antigo (1974–1986)
- **1974**: Donald Chamberlin e Raymond Boyce criam SEQUEL na IBM Research
- **Objetivo**: Manipulação de consultas para Sistema R (banco de dados relacional)
- Renomeado para SQL (Structured Query Language) devido a conflito de marca registrada
- **1986**: Primeiro padrão ANSI (SQL-86)
- **1987**: ISO adota SQL-87
### SQL-92 — A Fundação (1992)
- **O padrão mais importante** — todo SQL moderno descende deste
- `INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`
- Subconsultas (aninhadas `SELECT`)
- Expressão `CASE`
-`COALESCE`,`NULLIF`
- Restrições `UNIQUE`, `CHECK`
- Definição de esquema (`CREATE SCHEMA`)
### SQL:1999 — Começa o SQL moderno (1999)
- Expressões regulares (`LIKE`, `SIMILAR TO`)
- Consultas recursivas (`WITH RECURSIVE`)
- Gatilhos
- BLOB/CLOB (objetos binários/grandes caracteres)
- Tipos definidos pelo usuário (UDTs)
-`ORDER BY`em subconsultas
### SQL:2003 — Revolução Analítica (2003)
- **Funções de janela**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- Tipo de dados e funções XML
-`GENERATED ALWAYS AS IDENTITY` 
-`SAVEPOINT`(controle de transação)
- Funções hash
### SQL:2011 — Dados temporais (2011)
- **Tabelas temporais**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(padrão `LIMIT`)
- Paginação `OFFSET`/`FETCH`
### SQL:2016–2023 — JSON e além (2016–presente)
- **2016**: tipo de dados JSON,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: Funções de tabela polimórfica,`LISTAGG`
- **2023**:`JSON_TABLE`(visão relacional de JSON), operações `SET`, melhorias de array
## Evolução da Sintaxe
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

## Evolução de recursos
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

## Princípios-chave de design
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Evolução do Dialeto Principal
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Crescimento do Ecossistema
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
