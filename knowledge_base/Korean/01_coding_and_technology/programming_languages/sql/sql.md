<!--
---
# Metadata
title: "SQL"
description: "Comprehensive reference for the SQL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [sql, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "26 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# SQL
SQL(Structured Query Language)은 관계형 데이터베이스의 데이터를 관리하고 쿼리하기 위해 설계된 도메인별 언어입니다. 1970년대 IBM에서 처음 개발되어 1987년에 표준화된 SQL은 여전히 ​​애플리케이션과 해당 데이터 간의 기본 인터페이스로 남아 있습니다. PostgreSQL, MySQL, SQL Server, Oracle, SQLite 등 모든 주요 관계형 데이터베이스 관리 시스템(RDBMS)은 SQL을 쿼리 언어로 사용합니다.
SQL은 범용 프로그래밍 언어가 아닙니다. SQL로 웹 애플리케이션을 작성하지 않을 것입니다. 그러나 애플리케이션이 데이터를 저장하고 거의 모든 애플리케이션이 데이터를 저장한다면 SQL은 해당 데이터를 검색, 변환 및 관리하는 데 사용하는 언어입니다. 이는 틀림없이 일반 프로그래밍 다음으로 가장 보편적으로 유용한 기술입니다.
---

## SQL이 중요한 이유
- **범용**: 모든 관계형 데이터베이스는 SQL을 사용합니다. 한 번 배워서 어디에서나 사용하세요.
- **선언적**: *어떻게* 얻는 것이 아니라 원하는 *무엇* 데이터를 설명합니다. 데이터베이스 엔진은 실행을 최적화합니다.
- **모든 개발자에게 필수**: 백엔드, 데이터 과학, DevOps, 분석 — 모두 SQL이 필요합니다.
- **강력함**: 창 함수, CTE, 하위 쿼리 및 집계를 사용하면 복잡한 논리를 몇 줄로 표현할 수 있습니다.
- **성능**: 적절하게 인덱싱된 데이터베이스에서 잘 작성된 SQL 쿼리는 밀리초 안에 수백만 개의 행을 처리할 수 있습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **범용 언어가 아님** | SQL에서 애플리케이션, API 또는 알고리즘을 구축할 수 없습니다. | Python, Java, JavaScript 등과 결합 |
| **방언의 차이** | 각 RDBMS에는 호환되지 않는 확장이 포함된 고유한 SQL 특성이 있습니다. | 가능하면 ANSI SQL을 사용하세요. 응용 프로그램의 추상 방언 차이점 |
| **스키마 견고성** | 큰 테이블에서 테이블 구조를 변경하면 속도가 느리고 중단될 수 있습니다. | 마이그레이션 도구를 사용하십시오. 설계 스키마를 신중하게 사전에 |
| **N+1 쿼리 문제** | ORM 생성 쿼리는 매우 비효율적일 수 있습니다 | 복잡한 쿼리를 위한 사용자 정의 SQL을 작성합니다. EXPLAIN ANALYZE를 사용한 프로필 |
| **복잡성 확장** | SQL 데이터베이스는 NoSQL보다 수평 확장이 더 어렵습니다 | 특정 사용 사례에 대해 읽기 복제본, 샤딩을 사용하거나 NoSQL을 고려 |
---

## 핵심 개념
### 관계형 모델
데이터는 **행**(레코드/튜플)과 **열**(속성/필드)로 구성된 **테이블**(관계)에 저장됩니다. 테이블은 **키**를 통해 서로 연결될 수 있습니다.
```
+---------------------------------+     +----------------------------------+
|            users                |     |            orders                |
+------+----------+---------------+     +------+----------+----------------+
|  id  |   name   |    email      |     |  id  | user_id  |   total        |
+------+----------+---------------+     +------+----------+----------------+
|  1   | Alice    | alice@mail.com|<----|  1   |    1     |   99.99        |
|  2   | Bob      | bob@mail.com  |<----|  2   |    1     |   49.50        |
|  3   | Charlie  | charlie@mail  |     |  3   |    2     |  150.00        |
+------+----------+---------------+     |  4   |    3     |   75.25        |
  PRIMARY KEY                           |  5   |    3     |   30.00        |
                                        +------+----------+----------------+
                                                  FOREIGN KEY -> users.id
```

---

## 구문 기본 사항
### 데이터 검색(SELECT)
```sql
-- Basic query
SELECT name, email FROM users;

-- With filtering (WHERE)
SELECT name, email FROM users WHERE id = 1;

-- Multiple conditions
SELECT name, email FROM users WHERE id > 1 AND email LIKE '%@mail.com';

-- Sorting (ORDER BY)
SELECT name, email FROM users ORDER BY name ASC, id DESC;

-- Limiting results
SELECT name FROM users ORDER BY id LIMIT 10;
```

### 집계
```sql
-- Count, sum, average, min, max
SELECT 
    COUNT(*) AS total_users,
    AVG(age) AS average_age,
    MIN(created_at) AS earliest_user,
    MAX(created_at) AS latest_user
FROM users;

-- Group by (aggregate per group)
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS average_salary
FROM employees GROUP BY department;

-- Filter groups (HAVING)
SELECT department, COUNT(*) AS employee_count
FROM employees GROUP BY department HAVING COUNT(*) > 5;
```

### 테이블 조인
```sql
-- INNER JOIN — only matching rows from both tables
SELECT u.name, o.total FROM users u INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN — all rows from left table, matching rows from right
SELECT u.name, o.total FROM users u LEFT JOIN orders o ON u.id = o.user_id;

-- Multiple joins
SELECT u.name, o.id AS order_id, p.name AS product_name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;

-- Self join (employees and their managers)
SELECT e.name AS employee, m.name AS manager
FROM employees e LEFT JOIN employees m ON e.manager_id = m.id;
```

### 데이터 수정
```sql
-- Insert
INSERT INTO users (name, email, age) VALUES ('Diana', 'diana@mail.com', 28);

-- Insert multiple rows
INSERT INTO users (name, email, age) VALUES
    ('Eve', 'eve@mail.com', 32),
    ('Frank', 'frank@mail.com', 45);

-- Update
UPDATE users SET age = 31, email = 'alice.new@mail.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 3;

-- Upsert (PostgreSQL)
INSERT INTO users (id, name, email) VALUES (1, 'Alice Updated', 'alice@mail.com')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;
```
---

## 고급 구문 및 패턴
### 창 기능 — 심층 분석
창 함수는 GROUP BY처럼 단일 출력 행으로 축소하지 않고 현재 행과 관련된 일련의 행에 걸쳐 계산을 수행합니다.
```sql
-- ROW_NUMBER: unique sequential number within a partition
SELECT name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

-- RANK vs DENSE_RANK: handling ties differently
SELECT name, score,
    RANK()       OVER (ORDER BY score DESC) AS rank,        -- 1, 2, 2, 4
    DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank,  -- 1, 2, 2, 3
    ROW_NUMBER() OVER (ORDER BY score DESC) AS row_num      -- 1, 2, 3, 4
FROM students;

-- LAG and LEAD: access previous and next rows
SELECT month, revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month,
    LEAD(revenue, 1) OVER (ORDER BY month) AS next_month,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS month_change
FROM monthly_revenue;

-- Running total with frame specification
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) AS running_total,
    AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7day
FROM daily_sales;

-- NTILE: divide rows into N roughly equal buckets
SELECT name, salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile,
    NTILE(10) OVER (ORDER BY salary DESC) AS decile
FROM employees;

-- Percentage of total using window functions
SELECT department, salary,
    ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY department), 2) AS pct_of_dept,
    ROUND(salary * 100.0 / SUM(salary) OVER (), 2) AS pct_of_company
FROM employees;
```

### 공통 테이블 표현식(CTE) - 고급 사용법
```sql
-- Multiple CTEs in a single query
WITH department_stats AS (
    SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
    FROM employees GROUP BY department
),
high_earners AS (
    SELECT e.name, e.department, e.salary
    FROM employees e
    JOIN department_stats ds ON e.department = ds.department
    WHERE e.salary > ds.avg_salary * 1.5
)
SELECT * FROM high_earners ORDER BY department, salary DESC;

-- Recursive CTE: traverse a hierarchy (org chart)
WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 1 AS level, name AS path
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, oc.level + 1, oc.path || ' > ' || e.name
    FROM employees e JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT level, path FROM org_chart ORDER BY path;

-- Recursive CTE: generate a date series
WITH RECURSIVE date_series AS (
    SELECT DATE '2024-01-01' AS dt
    UNION ALL
    SELECT dt + INTERVAL '1 day' FROM date_series WHERE dt < DATE '2024-12-31'
)
SELECT dt FROM date_series WHERE EXTRACT(DOW FROM dt) BETWEEN 1 AND 5;
```

### JSON 작업
```sql
-- PostgreSQL: JSONB operations
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    attributes JSONB NOT NULL DEFAULT '{}'
);

INSERT INTO products (name, attributes) VALUES
('Laptop', '{"brand": "Dell", "ram_gb": 16, "storage": {"type": "SSD", "size_gb": 512}}'),
('Phone',  '{"brand": "Apple", "ram_gb": 6, "storage": {"type": "NVMe", "size_gb": 128}}');

-- Query JSON fields
SELECT name, attributes->>'brand' AS brand FROM products WHERE attributes->>'brand' = 'Dell';

-- Nested JSON access
SELECT name, attributes->'storage'->>'type' AS storage_type FROM products;

-- Check if JSON contains a key/value
SELECT name FROM products WHERE attributes @> '{"brand": "Apple"}';

-- Update a JSON field
UPDATE products SET attributes = jsonb_set(attributes, '{ram_gb}', '32') WHERE name = 'Laptop';
```

### 저장 프로시저 및 트리거
```sql
-- PostgreSQL: function that returns a table
CREATE OR REPLACE FUNCTION get_top_customers(min_orders INTEGER DEFAULT 5)
RETURNS TABLE(customer_name TEXT, order_count BIGINT, total_spent NUMERIC)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT u.name, COUNT(o.id), SUM(o.total)
    FROM users u JOIN orders o ON u.id = o.user_id
    GROUP BY u.name HAVING COUNT(o.id) >= min_orders
    ORDER BY SUM(o.total) DESC;
END; $$;

-- Trigger: automatically audit changes
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY, table_name TEXT, operation TEXT,
    old_data JSONB, new_data JSONB, changed_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION audit_trigger_func() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (table_name, operation, old_data, new_data)
    VALUES (TG_TABLE_NAME, TG_OP, to_jsonb(OLD), to_jsonb(NEW));
    RETURN COALESCE(NEW, OLD);
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER users_audit
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();
```
---

## 핵심 기능 심층 분석
### 쿼리 최적화
```sql
-- EXPLAIN ANALYSE: see the actual execution plan with real timings
EXPLAIN ANALYSE
SELECT u.name, COUNT(o.id) AS order_count
FROM users u LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.name HAVING COUNT(o.id) > 3
ORDER BY order_count DESC;

-- Typical output interpretation:
-- "Seq Scan" = scanning every row (slow for large tables)
-- "Index Scan" = using an index (fast)
-- "Hash Join" = joining with a hash table (usually fast)
-- "Nested Loop" = joining with a loop (can be slow)
```

**최적화 체크리스트:**
| 이슈 | 증상 | 수정 |
|-------|---------|-----|
| 대형 테이블의 순차 스캔 |  EXPLAIN의`Seq Scan`| 적절한 색인 추가 |
| WHERE 열에 인덱스가 누락되었습니다. | 전체 테이블 스캔 | 필터링된 열에 인덱스 만들기 |
| SELECT * 폐기물 | 불필요한 열 가져오기 | 필요한 열만 선택 |
| 암시적 유형 변환 | 인덱스가 사용되지 않음 | 비교의 일치 유형 |
| 인덱싱된 열의 함수 | 인덱스를 사용할 수 없음(선택할 수 없음) | 재작성: `WHERE YEAR(date) = 2024`가 아닌`WHERE date >= '2024-01-01'`|
### 색인 전략
```sql
-- Composite index: order matters (leftmost prefix rule)
CREATE INDEX idx_orders_status_date ON orders(status, created_at);
-- Useful for: WHERE status = 'active' AND created_at > '2024-01-01'
-- Useful for: WHERE status = 'active' (leftmost prefix)
-- NOT useful for: WHERE created_at > '2024-01-01' (skips first column)

-- Covering index: includes all columns needed by the query
CREATE INDEX idx_orders_covering ON orders(user_id) INCLUDE (total, status);

-- Partial index: only index rows meeting a condition
CREATE INDEX idx_orders_pending ON orders(created_at) WHERE status = 'pending';

-- Expression index: index on a computed value
CREATE INDEX idx_users_lower_email ON users(LOWER(email));

-- GIN index for full-text search (PostgreSQL)
CREATE INDEX idx_products_search ON products USING GIN(to_tsvector('english', name));
SELECT * FROM products WHERE to_tsvector('english', name) @@ plainto_tsquery('laptop');
```

### 트랜잭션 격리 수준
| 격리 수준 | 더티 읽기 | 반복 불가능 읽기 | 팬텀 읽기 |
|----|:----------:|:------:|:------------:|
| 커밋되지 않은 읽기 | 예 | 예 | 예 |
| 커밋됨 읽기 | 아니요 | 예 | 예 |
| 반복 읽기 | 아니요 | 아니요 | 예* |
| 직렬화 가능 | 아니요 | 아니요 | 아니요 |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 정규화
| 정규형 | 규칙 | 위반 사례 |
|-------------|------|------|
| **1NF** | 원자 값, 반복 그룹 없음 | 여러 전화기를 하나의 열에 "123,456"으로 저장 |
| **2NF** | 1NF + 부분 종속성 없음 | 주문 세부정보는 order_id에 따라 달라지지만 product_id에는 따라 다릅니다. |
| **3NF** | 2NF + 전이적 종속성 없음 | 직원 부서 이름은 직원이 아닌 부서 ID에 따라 다릅니다. |
---

## 데이터베이스 구조 정의
### 테이블 생성
```sql
CREATE TABLE users (
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    age         INTEGER CHECK (age >= 0 AND age <= 150),
    role        VARCHAR(20) DEFAULT 'viewer' CHECK (role IN ('admin', 'editor', 'viewer')),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP
);

CREATE TABLE orders (
    id          BIGSERIAL PRIMARY KEY,
    user_id     BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    total       DECIMAL(10, 2) NOT NULL CHECK (total >= 0),
    status      VARCHAR(20) DEFAULT 'pending',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
```

### 테이블 변경
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## 프로젝트 구성 및 빌드 시스템
### 마이그레이션 도구
| 도구 | 언어/스택 | 접근 |
|------|---------------|----------|
| **이동 경로** | 자바/일반 | SQL 기반 마이그레이션, 간단한 명명 규칙 |
| **리퀴베이스** | 자바/일반 | XML, YAML, JSON 또는 SQL 변경 로그 |
| **알렘빅** | 파이썬(SQLAlchemy) | 모델 변경으로 인한 마이그레이션 자동 생성 |
| **Prisma 마이그레이션** | Node.js/타입스크립트 | 스키마 우선, SQL 자동 생성 |
| **golang-마이그레이션** | 이동 | SQL 기반, Up/Down 마이그레이션 지원 |
```sql
-- Migration file naming convention (Flyway):
-- V001__create_users_table.sql
-- V002__add_email_index.sql
-- V003__create_orders_table.sql

-- V001__create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Always use idempotent migrations where possible
DROP TABLE IF EXISTS legacy_data;
CREATE TABLE IF NOT EXISTS audit_log (id SERIAL PRIMARY KEY);
```

---

## 테스트
### 테스트 데이터 생성
```sql
-- Generate test data with generate_series (PostgreSQL)
INSERT INTO users (name, email, age)
SELECT 'User_' || i, 'user' || i || '@test.com', 18 + (random() * 60)::INTEGER
FROM generate_series(1, 10000) AS i;

-- Assertion patterns for testing queries (PostgreSQL)
DO $$
DECLARE total_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO total_count FROM users;
    ASSERT total_count = 10000, 'Expected 10000 users, got ' || total_count;
    RAISE NOTICE 'All tests passed!';
END $$;
```

| 프레임워크 | 데이터베이스 | 설명 |
|------------|----------|-------------|
| **pgTAP** | 포스트그레SQL | 단위 테스트 프레임워크 |
| **tSQLt** | SQL 서버 | SQL Server에 대한 단위 테스트 |
| **utPLSQL** | 오라클 | Oracle PL/SQL용 테스트 프레임워크 |
---

## 상호 운용성
### 언어 바인딩
| 인터페이스 | 언어 | 설명 |
|------------|----------|-------------|
| **JDBC** | 자바 | 표준 데이터베이스 API |
| **ODBC** | 다중 | 범용 데이터베이스 API |
| **psycopg2/3** | 파이썬 | PostgreSQL 어댑터 |
| **데이터베이스/SQL** | 이동 | 드라이버 인터페이스가 포함된 표준 라이브러리 |
| **sqlite3** | 파이썬 | 내장된 SQLite 지원 |
| **pg** | Node.js | PostgreSQL 클라이언트 |
```python
# Python: connecting to PostgreSQL
import psycopg2
conn = psycopg2.connect(host="localhost", database="myapp", user="app_user", password="secret")
cur = conn.cursor()
# Parameterized query (NEVER use string concatenation — SQL injection risk!)
cur.execute("SELECT name, email FROM users WHERE id = %s", (user_id,))
rows = cur.fetchall()
```

---

## 디자인 패턴
### 패턴 1: 피벗/크로스탭
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### 패턴 2: 그룹당 상위 N개
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### 패턴 3: 틈과 섬
```sql
WITH numbered AS (
    SELECT login_date,
           login_date - ROW_NUMBER() OVER (ORDER BY login_date) AS grp
    FROM (SELECT DISTINCT login_date FROM user_logins WHERE user_id = 1) t
)
SELECT MIN(login_date) AS start_date, MAX(login_date) AS end_date,
       COUNT(*) AS consecutive_days
FROM numbered GROUP BY grp;
```

### 패턴 4: 천천히 변화하는 치수(SCD 유형 2)
```sql
CREATE TABLE dim_customer (
    id SERIAL PRIMARY KEY, customer_key INTEGER NOT NULL,
    name TEXT, address TEXT,
    valid_from DATE NOT NULL DEFAULT CURRENT_DATE,
    valid_to DATE, is_current BOOLEAN NOT NULL DEFAULT TRUE
);

-- Query current state:
SELECT * FROM dim_customer WHERE is_current = TRUE;

-- Query historical state:
SELECT * FROM dim_customer
WHERE '2024-06-15' BETWEEN valid_from AND COALESCE(valid_to, '9999-12-31');
```
---

## 성능: 인덱스 및 쿼리 계획
### 인덱스 작동 방식
인덱스는 데이터베이스가 전체 테이블을 스캔하지 않고 행을 찾을 수 있게 해주는 데이터 구조(일반적으로 B-트리)입니다.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| 지수 유형 | 최고의 대상 | 예 |
|------------|----------|---------|
| **B-트리**(기본값) | 같음 및 범위 쿼리 | `WHERE age > 25 AND age < 35`|
| **해시** | 정확한 평등만 | `WHERE email = 'x@y.com'`|
| **진** | 전체 텍스트 검색, 배열, JSON | `WHERE description @@ 'search term'`|
| **지스트** | 기하학적/공간 데이터 | `WHERE location <-> point(x,y) < 1000`|
### 쿼리 계획 읽기
```sql
-- PostgreSQL: see how the database plans to execute your query
EXPLAIN ANALYSE SELECT * FROM users WHERE email = 'alice@mail.com';

-- Look for:
-- "Seq Scan" = scanning every row (slow for large tables)
-- "Index Scan" = using an index (fast)
-- "Nested Loop" = joining with a loop (can be slow)
-- "Hash Join" = joining with a hash table (usually fast)
```

---

## SQL 방언
| 기능 | 포스트그레SQL | MySQL | SQL 서버 | SQLite |
|---------|------------|-------|------------|-------|
| 자동 증가 | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| 문자열 연결 | `\|\|`| `CONCAT()`| `+`또는`CONCAT()`| `\|\|`|
| 날짜 기능 | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| JSON 지원 | 우수 (`jsonb`) | 양호 (`JSON`) | 양호 (`JSON`) | 기본(`JSON1`) |
| 전체 텍스트 검색 | 내장 (`tsvector`) | 내장 | 내장 | 한정 |
| 창 기능 | 예 | 예(8.0+) | 예 | 예 |
---

## 배포
### 데이터베이스 배포 전략
| 전략 | 설명 | 위험 수준 |
|------------|-------------|------------|
| **마이그레이션 파일** | 버전이 지정된 SQL 스크립트가 순서대로 적용됨 | 낮음 |
| **블루-그린 배포** | 두 개의 동일한 데이터베이스 트래픽 전환 | 낮음 |
| **확장계약** | 새 열 추가, 이중 쓰기, 마이그레이션, 기존 삭제 | 낮음 |
| **직접 DDL** | 프로덕션에서 직접 ALTER TABLE 실행 | 높음 |
```sql
-- Expand-contract pattern: renaming a column safely
-- Phase 1: EXPAND - add new column alongside old
ALTER TABLE users ADD COLUMN full_name TEXT;

-- Phase 2: MIGRATE - backfill existing data
UPDATE users SET full_name = name WHERE full_name IS NULL;

-- Phase 3: CONTRACT - remove old column after verification
ALTER TABLE users DROP COLUMN name;
ALTER TABLE users RENAME COLUMN full_name TO name;
```

---

## SQL을 사용해야 하는 경우
| 시나리오 | 왜 SQL인가 | 대안 |
|------------|---------|-------------|
| 복잡한 쿼리가 포함된 관계형 데이터 | 이것이 바로 SQL이 설계된 이유입니다. | --- |
| 트랜잭션 무결성(ACID) | SQL 데이터베이스는 일관성을 보장합니다 | --- |
| 보고 및 분석 | 집계, 창 함수, CTE | 매우 복잡한 분석을 위한 Python(Pandas) |
| 데이터 무결성 제약 | 외래 키, CHECK, UNIQUE, NOT NULL | 애플리케이션 수준 검증(약함) |
| 간단한 키-값 저장 | 이 사용 사례에 대한 과잉 | Redis, DynamoDB |
| 고도로 구조화되지 않은 데이터 | 스키마 강성이 문제입니다 | MongoDB, 문서 데이터베이스 |
| 대규모 수평 확장 | SQL 데이터베이스를 샤딩하기 어려움 | 카산드라, DynamoDB, CockroachDB |
---

## 종합 Q&A
### Q1: `WHERE`와 `HAVING`의 차이점은 무엇인가요?
**A:** `WHERE`는 그룹화하기 전에 행을 필터링합니다.  `HAVING`는 집계 후 그룹을 필터링합니다.
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: 창 기능은 GROUP BY와 어떻게 다릅니까?
**A:** 창 함수는 행을 축소하지 않고 행 전체를 계산합니다.
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: 느린 쿼리를 어떻게 최적화합니까?
**답:** 주요 전략:
-`WHERE`,`JOIN`및`ORDER BY`에서 사용되는 열에 인덱스를 추가합니다. 
-`SELECT *`피하기 — 필요한 열만 선택
-`EXPLAIN`/ `EXPLAIN ANALYZE`를 사용하여 쿼리 계획 읽기
- 가능한 경우 하위 쿼리를 JOIN으로 대체합니다.
- 가독성을 위해 CTE를 사용합니다(일반적으로 성능 저하 없음).
- WHERE의 인덱스 열에 대한 함수 방지: `WHERE YEAR(date) = 2024`가 아닌 `WHERE date >= '2024-01-01'`를 사용하세요.
### Q4: CTE란 무엇이며 언제 사용해야 합니까?
**A:** 공통 테이블 표현식은 명명된 임시 결과 세트를 생성합니다.
```sql
-- CTE for readability
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS total
    FROM orders
    GROUP BY 1
),
running_total AS (
    SELECT month, total,
           SUM(total) OVER (ORDER BY month) AS cumulative
    FROM monthly_sales
)
SELECT * FROM running_total;
```

### Q5: NULL 값을 올바르게 처리하려면 어떻게 해야 합니까?
**A:** NULL은 알 수 없음을 나타냅니다. 자신을 포함하여 어떤 것과도 동일하지 않습니다.
```sql
-- NULL comparisons
NULL = NULL    -- NULL (not TRUE!)
NULL IS NULL   -- TRUE

-- COALESCE — first non-NULL
SELECT COALESCE(nickname, first_name, 'Anonymous') AS display_name
FROM users;

-- NULLIF — return NULL if equal
SELECT NULLIF(status, '') AS status;  -- '' becomes NULL

-- COUNT ignores NULLs
SELECT COUNT(completed_at) FROM tasks;  -- counts non-NULL only
```

---

## 사고 사슬 문제 해결
### 문제 1: 그룹당 상위 N개 찾기
**1단계: 문제 이해**
각 부서에서 가장 높은 급여를 받는 직원 3명을 찾아보세요.
**2단계: 접근 방식 파악**
부서별로 분할된 `ROW_NUMBER()`를 사용하여 윈도우 기능을 사용합니다.
**3단계: 구현**```sql
WITH ranked AS (
    SELECT name, department, salary,
           ROW_NUMBER() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rn
    FROM employees
)
SELECT name, department, salary
FROM ranked
WHERE rn <= 3
ORDER BY department, salary DESC;
```

**4단계: 확인**
각 부서에 최대 3개의 행이 있는지 확인하세요. 필요한 경우 `DENSE_RANK()`를 사용하여 연결을 처리합니다.
### 문제 2: 전년 대비 성장 보고서 작성
**1단계: 문제 이해**
월별 수익과 전년 대비 성장률을 계산합니다.
**2단계: 접근 방식 파악**
그룹화에는 `DATE_TRUNC`를 사용하고 전년도 비교에는`LAG()`창 기능을 사용합니다.
**3단계: 구현**```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date) AS month,
           SUM(amount) AS revenue
    FROM orders
    GROUP BY 1
)
SELECT month,
       revenue,
       LAG(revenue, 12) OVER (ORDER BY month) AS revenue_prev_year,
       ROUND(
           (revenue - LAG(revenue, 12) OVER (ORDER BY month))
           / NULLIF(LAG(revenue, 12) OVER (ORDER BY month), 0) * 100,
           2
       ) AS yoy_growth_pct
FROM monthly
ORDER BY month;
```

**4단계: 확인**
처음 12개월에 이전 연도에 대한 NULL이 있는지 확인하세요. 알려진 수치와 비교하여 성장률을 검증합니다.
### 문제 3: 행을 열로 피벗
**1단계: 문제 이해**
변환 상태는 행에서 열로 계산됩니다.
**2단계: 접근 방식 파악**
조건부 집계(`SUM`내부`CASE`)를 사용합니다.
**3단계: 구현**```sql
-- Input: orders table with status column
-- Output: one row per month with status counts as columns
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(CASE WHEN status = 'pending'   THEN 1 ELSE 0 END) AS pending,
       SUM(CASE WHEN status = 'shipped'   THEN 1 ELSE 0 END) AS shipped,
       SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS delivered,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
       COUNT(*) AS total
FROM orders
GROUP BY 1
ORDER BY 1;
```

**4단계: 확장**
백분율 열과 누계를 추가합니다.
---

## 요약
SQL은 50년이 된 지금도 여전히 필수적인 언어입니다. 모든 개발자, 데이터 과학자, 분석가는 이를 알아야 합니다. 핵심 언어는 표준화되어 있고 이식 가능합니다. 방언의 차이는 관리 가능합니다. 최신 SQL(창 함수, CTE 및 JSON 지원 포함)은 대부분의 데이터 작업에 충분한 표현력을 제공합니다. 핵심 기술은 효율적인 쿼리 작성, 인덱스 이해, 쿼리 계획 읽기, 좋은 스키마 설계입니다. 데이터로 작업하는 경우 SQL은 협상할 수 없습니다.