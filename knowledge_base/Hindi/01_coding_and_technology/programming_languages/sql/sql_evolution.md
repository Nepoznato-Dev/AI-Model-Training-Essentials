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

# एसक्यूएल - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| अगली कड़ी | 1974 | मूल आईबीएम अनुसंधान भाषा (चेम्बरलिन और बॉयस) |
| एसक्यूएल-86 | 1986 | **पहला एएनएसआई मानक** (एसक्यूएल-86) |
| एसक्यूएल-89 | 1989 | मामूली संशोधन (अखंडता बाधाएं) |
| एसक्यूएल-92 | 1992 | **प्रमुख**:`JOIN`, उपश्रेणी,`CASE`,`COALESCE`|
| एसक्यूएल:1999 | 1999 | **नियमित अभिव्यक्ति**, पुनरावर्ती प्रश्न, ट्रिगर, बीएलओबी |
| एसक्यूएल:2003 | 2003 | **विंडो फ़ंक्शंस**, XML,`GENERATED`कॉलम |
| एसक्यूएल:2006 | 2006 | XML समर्थन,`MERGE`|
| एसक्यूएल:2008 | 2008 | `INSTEAD OF`ट्रिगर्स,`TRUNCATE`,`ORDER BY`व्यूज में |
| एसक्यूएल:2011 | 2011 | **अस्थायी डेटा** (`AS OF`,`FOR SYSTEM_TIME`),`FETCH FIRST`|
| एसक्यूएल:2016 | 2016 | **JSON समर्थन**, पंक्ति पैटर्न पहचान |
| एसक्यूएल:2019 | 2019 | **पॉलीमॉर्फिक टेबल फ़ंक्शंस**,`LISTAGG`|
| एसक्यूएल:2023 | 2023 | **`JSON_TABLE`**,`SET`संचालन, सरणी संवर्द्धन |
## प्रमुख मील के पत्थर
### सीक्वल और प्रारंभिक एसक्यूएल (1974-1986)
- **1974**: डोनाल्ड चेम्बरलिन और रेमंड बॉयस ने आईबीएम रिसर्च में सीक्वल बनाया
- **लक्ष्य**: सिस्टम आर के लिए क्वेरी हेरफेर (संबंधपरक डेटाबेस)
- ट्रेडमार्क विरोध के कारण इसका नाम बदलकर SQL (स्ट्रक्चर्ड क्वेरी लैंग्वेज) कर दिया गया
- **1986**: पहला एएनएसआई मानक (एसक्यूएल-86)
- **1987**: ISO ने SQL-87 को अपनाया
### SQL-92 - द फाउंडेशन (1992)
- **सबसे महत्वपूर्ण मानक** - सभी आधुनिक एसक्यूएल इसी पर आधारित हैं
-`INNER JOIN`,`LEFT JOIN`,`RIGHT JOIN`
- सबक्वेरीज़ (नेस्टेड `SELECT`)
-`CASE`अभिव्यक्ति
-`COALESCE`,`NULLIF`
-`UNIQUE`,`CHECK`बाधाएं
- स्कीमा परिभाषा (`CREATE SCHEMA`)
### SQL:1999 - आधुनिक SQL आरंभ (1999)
- नियमित अभिव्यक्ति (`LIKE`, `SIMILAR TO`)
- पुनरावर्ती प्रश्न (`WITH RECURSIVE`)
- ट्रिगर
- ब्लॉब/सीएलओबी (बाइनरी/कैरेक्टर बड़ी वस्तुएं)
- उपयोगकर्ता-परिभाषित प्रकार (यूडीटी)
- सबक्वेरीज़ में `ORDER BY`
### SQL:2003 — एनालिटिक्स रिवोल्यूशन (2003)
- **विंडो फ़ंक्शन**: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`,`SUM() OVER()`
- XML डेटा प्रकार और फ़ंक्शन
-`GENERATED ALWAYS AS IDENTITY`
-`SAVEPOINT`(लेनदेन नियंत्रण)
- हैश फ़ंक्शन
### SQL:2011 — अस्थायी डेटा (2011)
- **टेम्पोरल टेबल**:`FOR SYSTEM_TIME AS OF`,`VERSIONING`
-`FETCH FIRST n ROWS ONLY`(मानक `LIMIT`)
-`OFFSET`/`FETCH`पृष्ठांकन
### SQL:2016–2023 — JSON और परे (2016–वर्तमान)
- **2016**: JSON डेटा प्रकार,`JSON_VALUE`,`JSON_QUERY`,`JSON_EXISTS`
- **2019**: पॉलीमॉर्फिक टेबल फ़ंक्शन,`LISTAGG`
- **2023**:`JSON_TABLE`(JSON का संबंधपरक दृश्य),`SET`संचालन, सरणी संवर्द्धन
## सिंटेक्स इवोल्यूशन
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

## फ़ीचर इवोल्यूशन
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

## मुख्य डिज़ाइन सिद्धांत
```
1. "Declarative" — describe WHAT, not HOW
2. "Set-based" — operate on sets of rows, not individual rows
3. "Standardized" — ANSI/ISO standards ensure portability
4. "Relational" — based on relational algebra (Codd, 1970)
5. "Composable" — queries within queries, views of views
6. "ACID" — Atomicity, Consistency, Isolation, Durability
```

## प्रमुख बोली विकास
```
1970s: System R (IBM) — first SQL implementation
1980s: Oracle, DB2, SQL Server, Ingres
1990s: PostgreSQL (1996), MySQL (1995)
2000s: SQLite (2000), BigQuery, Redshift (cloud)
2010s: Snowflake, CockroachDB, TiDB (distributed SQL)
2020s: DuckDB (analytical), SQLite (ubiquitous), cloud-native SQL
```

## पारिस्थितिकी तंत्र का विकास
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
