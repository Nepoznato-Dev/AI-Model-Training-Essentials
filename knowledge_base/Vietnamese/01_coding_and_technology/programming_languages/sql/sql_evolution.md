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
# SQL — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| PHẦN TIẾP THEO | 1974 | Ngôn ngữ nghiên cứu gốc của IBM (Chamberlin & Boyce) |
| SQL-86 | 1986 | **Tiêu chuẩn ANSI đầu tiên** (SQL-86) |
| SQL-89 | 1989 | Sửa đổi nhỏ (ràng buộc về tính toàn vẹn) |
| SQL-92 | 1992 | **Chính**:`JOIN`, truy vấn phụ,`CASE`,`COALESCE`|
| SQL:1999 | 1999 | **Biểu thức chính quy**, truy vấn đệ quy, trình kích hoạt, BLOB |
| SQL:2003 | 2003 | **Các hàm cửa sổ**, cột XML,`GENERATED`|
| SQL:2006 | 2006 | Hỗ trợ XML,`MERGE`|
| SQL:2008 | 2008 |  Trình kích hoạt `INSTEAD OF`,`TRUNCATE`,`ORDER BY`trong lượt xem |
| SQL:2011 | 2011 | **Dữ liệu tạm thời** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| SQL:2016 | 2016 | **Hỗ trợ JSON**, nhận dạng mẫu hàng |
| SQL:2019 | 2019 | **Các hàm bảng đa hình**,`LISTAGG`|
| SQL:2023 | 2023 | **`JSON_TABLE`**, hoạt động `SET`, cải tiến mảng |
## Các cột mốc quan trọng
### SEQUEL và SQL sơ khai (1974–1986)
- **1974**: Donald Chamberlin & Raymond Boyce tạo ra SEQUEL tại IBM Research
- **Mục tiêu**: Thao tác truy vấn cho System R (cơ sở dữ liệu quan hệ)
- Đổi tên thành SQL (Ngôn ngữ truy vấn có cấu trúc) do xung đột nhãn hiệu
- **1986**: Tiêu chuẩn ANSI đầu tiên (SQL-86)
- **1987**: ISO áp dụng SQL-87
### SQL-92 — Nền tảng (1992)
- **Tiêu chuẩn quan trọng nhất** — tất cả SQL hiện đại đều bắt nguồn từ tiêu chuẩn này
-`INNER JOIN`,`LEFT JOIN`,`RIGHT JOIN`
- Truy vấn con (`SELECT` lồng nhau)
- Biểu thức `CASE`
-`COALESCE`,`NULLIF`
- Ràng buộc `UNIQUE`, `CHECK`
- Định nghĩa lược đồ (`CREATE SCHEMA`)
### SQL:1999 — SQL hiện đại bắt đầu (1999)
- Biểu thức chính quy (`LIKE`,`SIMILAR TO`)
- Truy vấn đệ quy (`WITH RECURSIVE`)
- Kích hoạt
- BLOB/CLOB (đối tượng lớn nhị phân/ký tự)
- Các loại do người dùng xác định (UDT)
-`ORDER BY`trong truy vấn con
### SQL:2003 — Cuộc cách mạng phân tích (2003)
- **Chức năng cửa sổ**:`ROW_NUMBER()`,`RANK()`,`DENSE_RANK()`,`LAG()`,`LEAD()`,`SUM() OVER()`
- Kiểu dữ liệu XML và các hàm
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(kiểm soát giao dịch)
- Hàm băm
### SQL:2011 — Dữ liệu tạm thời (2011)
- **Bảng tạm thời**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(chuẩn `LIMIT`)
- Phân trang`OFFSET`/ `FETCH`
### SQL:2016–2023 — JSON & Beyond (2016–nay)
- **2016**: Kiểu dữ liệu JSON,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: Hàm bảng đa hình,`LISTAGG`
- **2023**:`JSON_TABLE`(chế độ xem quan hệ của JSON), hoạt động `SET`, cải tiến mảng
## Tiến hóa cú pháp
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

## Tiến hóa tính năng
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

## Nguyên tắc thiết kế chính
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## Tiến hóa phương ngữ chính
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## Tăng trưởng hệ sinh thái
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
