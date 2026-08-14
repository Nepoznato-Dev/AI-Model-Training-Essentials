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
# SQL — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| SUITE | 1974 | Langage de recherche IBM original (Chamberlin & Boyce) |
| SQL-86 | 1986 | **Première norme ANSI** (SQL-86) |
| SQL-89 | 1989 | Révision mineure (contraintes d'intégrité) |
| SQL-92 | 1992 | **Majeur** :`JOIN`, sous-requêtes,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Expressions régulières**, requêtes récursives, déclencheurs, BLOB |
| SQL:2003 | 2003 | **Fonctions de fenêtre**, XML, colonnes`GENERATED`|
| SQL:2006 | 2006 | Prise en charge XML,`MERGE`|
| SQL:2008 | 2008 |  Déclencheurs `INSTEAD OF`, `TRUNCATE`,`ORDER BY`dans les vues |
| SQL:2011 | 2011 | **Données temporelles** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **Prise en charge JSON**, reconnaissance des modèles de lignes |
| SQL:2019 | 2019 | **Fonctions de table polymorphes**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**, opérations `SET`, améliorations du tableau |
## Étapes majeures
### SEQUEL et premiers SQL (1974-1986)
- **1974** : Donald Chamberlin et Raymond Boyce créent SEQUEL chez IBM Research
- **Objectif** : Manipulation de requêtes pour System R (base de données relationnelle)
- Renommé en SQL (Structured Query Language) en raison d'un conflit de marque
- **1986** : Première norme ANSI (SQL-86)
- **1987** : l'ISO adopte SQL-87
### SQL-92 — La Fondation (1992)
- **La norme la plus importante** — tout le SQL moderne en descend
-`INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`
- Sous-requêtes (`SELECT` imbriquées)
-Expression `CASE`
-`COALESCE`,`NULLIF`
- Contraintes`UNIQUE`, `CHECK`
- Définition du schéma (`CREATE SCHEMA`)
### SQL : 1999 — Début du SQL moderne (1999)
- Expressions régulières (`LIKE`,`SIMILAR TO`)
- Requêtes récursives (`WITH RECURSIVE`)
- Déclencheurs
- BLOB/CLOB (grands objets binaires/caractères)
- Types définis par l'utilisateur (UDT)
-`ORDER BY`dans les sous-requêtes
### SQL :2003 — Révolution analytique (2003)
- **Fonctions de fenêtre** :`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- Type de données XML et fonctions
-`GENERATED ALWAYS AS IDENTITY` 
-`SAVEPOINT`(contrôle des transactions)
- Fonctions de hachage
### SQL:2011 — Données temporelles (2011)
- **Tables temporelles** :`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(norme `LIMIT`)
- Pagination`OFFSET`/ `FETCH`
### SQL : 2016-2023 — JSON et au-delà (2016-présent)
- **2016** : type de données JSON,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019** : Fonctions de table polymorphe,`LISTAGG`
- **2023** :`JSON_TABLE`(vue relationnelle de JSON), opérations `SET`, améliorations des tableaux
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
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

## Principes de conception clés
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Évolution majeure des dialectes
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Croissance de l'écosystème
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
