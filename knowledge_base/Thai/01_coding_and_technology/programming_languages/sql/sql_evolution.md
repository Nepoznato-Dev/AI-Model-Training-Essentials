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
# SQL - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| ภาคต่อ | 1974 | ภาษาการวิจัยดั้งเดิมของ IBM (Chamberlin & Boyce) |
| SQL-86 | 1986 | **มาตรฐาน ANSI แรก** (SQL-86) |
| SQL-89 | 1989 | การแก้ไขเล็กน้อย (ข้อจำกัดด้านความสมบูรณ์) |
| SQL-92 | 1992 | **หลัก**:`JOIN`, แบบสอบถามย่อย,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **นิพจน์ทั่วไป** การสืบค้นแบบเรียกซ้ำ ทริกเกอร์ BLOBs |
| SQL:2003 | 2546 | **ฟังก์ชันหน้าต่าง**, XML, คอลัมน์`GENERATED`|
| SQL:2006 | 2549 | รองรับ XML,`MERGE`|
| SQL:2008 | 2551 | `INSTEAD OF`ทริกเกอร์,`TRUNCATE`,`ORDER BY`ในมุมมอง |
| SQL:2011 | 2554 | **ข้อมูลชั่วคราว** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2559 | **รองรับ JSON** การจดจำรูปแบบแถว |
| SQL:2019 | 2019 | **ฟังก์ชันตารางโพลีมอร์ฟิก**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**, การดำเนินการ `SET`, การปรับปรุงอาร์เรย์ |
## เหตุการณ์สำคัญที่สำคัญ
### ผลสืบเนื่องและ SQL ยุคแรก (พ.ศ. 2517-2529)
- **1974**: Donald Chamberlin และ Raymond Boyce สร้าง SEQUEL ที่ IBM Research
- **เป้าหมาย**: การจัดการแบบสอบถามสำหรับ System R (ฐานข้อมูลเชิงสัมพันธ์)
- เปลี่ยนชื่อเป็น SQL (Structured Query Language) เนื่องจากข้อขัดแย้งด้านเครื่องหมายการค้า
- **1986**: มาตรฐาน ANSI แรก (SQL-86)
- **1987**: ISO ใช้ SQL-87
### SQL-92 - มูลนิธิ (1992)
- **มาตรฐานที่สำคัญที่สุด** — SQL สมัยใหม่ทั้งหมดสืบทอดมาจากสิ่งนี้
-`INNER JOIN`,`LEFT JOIN`,`RIGHT JOIN`
- แบบสอบถามย่อย (ซ้อน`SELECT`)
- การแสดงออก `CASE`
-`COALESCE`,`NULLIF`
-`UNIQUE`,`CHECK`ข้อจำกัด
- คำจำกัดความของสคีมา (`CREATE SCHEMA`)
### SQL:1999 — SQL สมัยใหม่เริ่มต้น (1999)
- นิพจน์ทั่วไป (`LIKE`,`SIMILAR TO`)
- ข้อความค้นหาแบบเรียกซ้ำ (`WITH RECURSIVE`)
- ทริกเกอร์
- BLOB/CLOB (วัตถุขนาดใหญ่ไบนารี/อักขระ)
- ประเภทที่ผู้ใช้กำหนด (UDT)
-`ORDER BY`ในแบบสอบถามย่อย
### SQL:2003 — การปฏิวัติของการวิเคราะห์ (2003)
- **ฟังก์ชันหน้าต่าง**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- ชนิดข้อมูล XML และฟังก์ชัน
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(ควบคุมธุรกรรม)
- ฟังก์ชั่นแฮช
### SQL:2011 — ข้อมูลชั่วคราว (2011)
- **ตารางชั่วคราว**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(มาตรฐาน`LIMIT`)
-`OFFSET`/`FETCH`การแบ่งหน้า
### SQL:2016–2023 — JSON & Beyond (2016–ปัจจุบัน)
- **2016**: ประเภทข้อมูล JSON,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: ฟังก์ชันตารางโพลีมอร์ฟิก`LISTAGG`
- **2023**:`JSON_TABLE`(มุมมองเชิงสัมพันธ์ของ JSON), การดำเนินการ `SET`, การปรับปรุงอาร์เรย์
## วิวัฒนาการไวยากรณ์
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

## วิวัฒนาการคุณสมบัติ
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

## หลักการออกแบบที่สำคัญ
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## วิวัฒนาการภาษาถิ่นที่สำคัญ
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## การเติบโตของระบบนิเวศ
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
