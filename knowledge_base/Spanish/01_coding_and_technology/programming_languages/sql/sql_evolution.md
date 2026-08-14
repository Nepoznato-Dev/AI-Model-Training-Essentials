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
# SQL: historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| SECUELA | 1974 | Lenguaje de investigación original de IBM (Chamberlin & Boyce) |
| SQL-86 | 1986 | **Primer estándar ANSI** (SQL-86) |
| SQL-89 | 1989 | Revisión menor (restricciones de integridad) |
| SQL-92 | 1992 | **Principal**: `JOIN`, subconsultas, `CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Expresiones regulares**, consultas recursivas, desencadenadores, BLOB |
| SQL:2003 | 2003 | **Funciones de ventana**, XML, columnas`GENERATED`|
| SQL:2006 | 2006 | Soporte XML,`MERGE`|
| SQL:2008 | 2008 |  Activadores `INSTEAD OF`, `TRUNCATE`,`ORDER BY`en vistas |
| SQL:2011 | 2011 | **Datos temporales** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **Soporte JSON**, reconocimiento de patrones de filas |
| SQL:2019 | 2019 | **Funciones de tabla polimórfica**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**, operaciones `SET`, mejoras de matriz |
## Hitos importantes
### SECUELA y SQL temprano (1974-1986)
- **1974**: Donald Chamberlin y Raymond Boyce crean SEQUEL en IBM Research
- **Objetivo**: Manipulación de consultas para System R (base de datos relacional)
- Renombrado a SQL (lenguaje de consulta estructurado) debido a un conflicto de marcas comerciales
- **1986**: Primer estándar ANSI (SQL-86)
- **1987**: ISO adopta SQL-87
### SQL-92 — La Fundación (1992)
- **El estándar más importante**: todo SQL moderno desciende de este
- `INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`
- Subconsultas (`SELECT` anidadas)
- Expresión `CASE`
- `COALESCE`,`NULLIF`
- Restricciones `UNIQUE`, `CHECK`
- Definición del esquema (`CREATE SCHEMA`)
### SQL:1999 — Comienza el SQL moderno (1999)
- Expresiones regulares (`LIKE`, `SIMILAR TO`)
- Consultas recursivas (`WITH RECURSIVE`)
- Desencadenantes
- BLOB/CLOB (objetos binarios/de caracteres grandes)
- Tipos definidos por el usuario (UDT)
-`ORDER BY`en subconsultas
### SQL:2003 — Revolución analítica (2003)
- **Funciones de ventana**: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`,`SUM() OVER()`
- Tipo de datos XML y funciones.
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(control de transacciones)
- Funciones hash
### SQL:2011 — Datos temporales (2011)
- **Tablas temporales**: `FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(estándar `LIMIT`)
- Paginación`OFFSET`/ `FETCH`
### SQL:2016–2023: JSON y más allá (2016-presente)
- **2016**: tipo de datos JSON, `JSON_VALUE`, `JSON_QUERY`,`JSON_EXISTS`
- **2019**: Funciones de tabla polimórficas,`LISTAGG`
- **2023**:`JSON_TABLE`(vista relacional de JSON), operaciones `SET`, mejoras de matriz
## Evolución de la sintaxis
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

## Evolución de funciones
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

## Principios clave de diseño
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Evolución del dialecto principal
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Crecimiento del ecosistema
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
