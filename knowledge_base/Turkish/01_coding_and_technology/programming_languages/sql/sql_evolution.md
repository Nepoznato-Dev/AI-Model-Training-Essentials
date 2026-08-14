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

# SQL — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| DEVAMI | 1974 | Orijinal IBM araştırma dili (Chamberlin & Boyce) |
| SQL-86 | 1986 | **İlk ANSI standardı** (SQL-86) |
| SQL-89 | 1989 | Küçük düzeltme (bütünlük kısıtlamaları) |
| SQL-92 | 1992 | **Ana**:`JOIN`, alt sorgular,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Normal ifadeler**, özyinelemeli sorgular, tetikleyiciler, BLOB'lar |
| SQL:2003 | 2003 | **Pencere işlevleri**, XML,`GENERATED`sütunları |
| SQL:2006 | 2006 | XML desteği,`MERGE`|
| SQL:2008 | 2008 | `INSTEAD OF`tetikleyicileri,`TRUNCATE`,`ORDER BY`görünümlerde |
| SQL:2011 | 2011 | **Geçici veriler** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **JSON desteği**, satır deseni tanıma |
| SQL:2019 | 2019 | **Polimorfik tablo fonksiyonları**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**,`SET`işlemleri, dizi geliştirmeleri |
## Önemli Kilometre Taşları
### DEVAMI ve Erken SQL (1974–1986)
- **1974**: Donald Chamberlin ve Raymond Boyce, IBM Research'te SEQUEL'i yarattı
- **Hedef**: Sistem R için sorgu manipülasyonu (ilişkisel veritabanı)
- Ticari marka anlaşmazlığı nedeniyle SQL (Yapılandırılmış Sorgu Dili) olarak yeniden adlandırıldı
- **1986**: İlk ANSI standardı (SQL-86)
- **1987**: ISO, SQL-87'yi benimsiyor
### SQL-92 — Temel (1992)
- **En önemli standart** — tüm modern SQL'in kökeni bu standarttır
-`INNER JOIN`,`LEFT JOIN`,`RIGHT JOIN`
- Alt sorgular (yuvalanmış `SELECT`)
-`CASE`ifadesi
-`COALESCE`,`NULLIF`
-`UNIQUE`,`CHECK`kısıtlamaları
- Şema tanımı (`CREATE SCHEMA`)
### SQL:1999 — Modern SQL Başlıyor (1999)
- Düzenli ifadeler (`LIKE`,`SIMILAR TO`)
- Özyinelemeli sorgular (`WITH RECURSIVE`)
- Tetikleyiciler
- BLOB/CLOB (ikili/karakter büyük nesneler)
- Kullanıcı tanımlı türler (UDT'ler)
- Alt sorgularda `ORDER BY`
### SQL:2003 — Analitik Devrimi (2003)
- **Pencere işlevleri**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- XML veri türü ve işlevleri
-`GENERATED ALWAYS AS IDENTITY` 
-`SAVEPOINT`(işlem kontrolü)
- Hash fonksiyonları
### SQL:2011 — Geçici Veriler (2011)
- **Geçici tablolar**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(standart`LIMIT`)
-`OFFSET`/`FETCH`sayfalandırma
### SQL:2016–2023 — JSON ve Ötesi (2016–günümüz)
- **2016**: JSON veri türü,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: Polimorfik tablo işlevleri,`LISTAGG`
- **2023**:`JSON_TABLE`(JSON'un ilişkisel görünümü),`SET`işlemleri, dizi geliştirmeleri
## Söz Dizimi Gelişimi
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

## Özellik Gelişimi
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

## Temel Tasarım İlkeleri
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Başlıca Lehçe Evrimi
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Ekosistem Büyümesi
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
