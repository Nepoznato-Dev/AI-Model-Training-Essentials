---
# Metadata
title: "SQL"
description: "Comprehensive reference for the SQL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# SQL
SQL (Structured Query Language) は、リレーショナル データベース内のデータの管理とクエリを行うために設計されたドメイン固有の言語です。 1970 年代に IBM で最初に開発され、1987 年に標準化された SQL は、今でもアプリケーションとそのデータの間の主要なインターフェイスです。 PostgreSQL、MySQL、SQL Server、Oracle、SQLite などの主要なリレーショナル データベース管理システム (RDBMS) はすべて、クエリ言語として SQL を使用します。
SQL は汎用プログラミング言語ではありません。 SQL で Web アプリケーションを作成することはありません。しかし、アプリケーションがデータを保存する場合 (ほとんどすべてのアプリケーションがそうします)、そのデータを取得、変換、管理するために使用する言語は SQL です。これはおそらく、一般的なプログラミングに次いで最も普遍的に役立つ技術スキルです。
---

## SQL が重要な理由
- **ユニバーサル**: すべてのリレーショナル データベースは SQL を話します。一度学習すれば、どこでも使用できます。
- **宣言型**: データを*取得する方法*ではなく、必要なデータを*説明します。データベース エンジンは実行を最適化します。
- **すべての開発者にとって必須**: バックエンド、データ サイエンス、DevOps、分析 - すべてに SQL が必要です。
- **強力**: ウィンドウ関数、CTE、サブクエリ、集計を使用すると、複雑なロジックを数行で表現できます。
- **パフォーマンス**: 適切にインデックス付けされたデータベース上で適切に作成された SQL クエリは、数百万行をミリ秒で処理できます。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **汎用言語ではありません** | SQL でアプリケーション、API、またはアルゴリズムを構築できない | Python、Java、JavaScriptなどと組み合わせる |
| **方言の違い** |各 RDBMS には、互換性のない拡張子を持つ独自の SQL フレーバーがあります。可能な限り ANSI SQL を使用してください。アプリケーション内の抽象的な方言の違い |
| **スキーマの剛性** |大きなテーブルでテーブル構造を変更すると、時間がかかり、中断が生じる可能性があります。移行ツールを使用します。スキーマを事前に慎重に設計する |
| **N+1 クエリの問題** | ORM で生成されたクエリは非常に非効率になる可能性があります。複雑なクエリ用のカスタム SQL を作成します。 EXPLAIN ANALYZE を使用したプロファイル |
| **スケーリングの複雑さ** | SQL データベースは NoSQL よりも水平方向に拡張するのが困難です。特定のユースケースでは、リードレプリカ、シャーディングを使用するか、NoSQL を検討してください。
---

## コアコンセプト
### リレーショナル モデル
データは **テーブル** (リレーション) に保存され、**行** (レコード/タプル) と **列** (属性/フィールド) で構成されます。テーブルは **キー** を使用して相互に関連付けることができます。
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

## 構文の基礎
### データの取得 (SELECT)
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

### 集計
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

### テーブルの結合
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

### データの変更
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

## 高度な構文とパターン
### ウィンドウ関数 — 詳細
ウィンドウ関数は、GROUP BY のように行を 1 つの出力行に折りたたむことなく、現在の行に関連する一連の行に対して計算を実行します。
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

### 共通テーブル式 (CTE) — 高度な使用法
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

### JSON 操作
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

### ストアド プロシージャとトリガー
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

## コア機能の詳細
### クエリの最適化
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

**最適化チェックリスト:**
|問題 |症状 |修正 |
|------|-----------|-----|
|大きなテーブルでの順次スキャン |  EXPLAIN の`Seq Scan`|適切なインデックスを追加します |
| WHERE 列にインデックスがありません |フルテーブルスキャン |フィルタリングされた列にインデックスを作成する |
| SELECT * 無駄 |不要な列を取得する |必要な列のみを選択 |
|暗黙的な型変換 |インデックスは使用されていません |比較における一致タイプ |
|インデックス付き列の関数 |インデックスは使用できません (検索可能ではありません) |書き換え:`WHERE YEAR(date) = 2024`ではなく`WHERE date >= '2024-01-01'`|
### インデックス作成戦略
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

### トランザクション分離レベル
|分離レベル |ダーティリード |反復不可能な読み取り |ファントムリード |
|-----------------|:----------:|:---------------------:|:------------:|
|コミットされていない読み取り |はい |はい |はい |
|コミット済みの読み取り |いいえ |はい |はい |
|繰り返し読み取り |いいえ |いいえ |はい* |
|シリアル化可能 |いいえ |いいえ |いいえ |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 正規化
|標準形 |ルール |違反例 |
|-----------|------|--------|
| **1NF** |原子値、繰り返しグループなし |複数の電話機を 1 つの列に「123,456」として保存する |
| **2NF** | 1NF + 部分的な依存関係なし |注文の詳細は order_id に依存しますが、product_id には依存しません。
| **3NF** | 2NF + 推移的な依存関係なし |従業員の部門名は、employee ではなく dept_id に依存します。
---

## データベース構造の定義
### テーブルの作成
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

### テーブルの変更
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## プロジェクトの構成とシステムの構築
### 移行ツール
|ツール |言語/スタック |アプローチ |
|------|---------------|----------|
| **フライウェイ** | Java / 一般 | SQL ベースの移行、単純な命名規則 |
| **リキベース** | Java / 一般 | XML、YAML、JSON、または SQL 変更ログ |
| **アレンビック** | Python (SQLAlchemy) |モデル変更から移行を自動生成 |
| **Prisma Migrate** | Node.js / TypeScript |スキーマファースト、SQL を自動生成 |
| **golang-移行** |行く | SQL ベース、アップ/ダウン移行をサポート |
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

## テスト
### テストデータの生成
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

|フレームワーク |データベース |説明 |
|----------|----------|---------------|
| **pgTAP** |ポストグレSQL |単体テストフレームワーク |
| **tSQLt** | SQLサーバー | SQL Server の単体テスト |
| **utPLSQL** |オラクル | Oracle PL/SQL のテスト フレームワーク |
---

## 相互運用性
### 言語バインディング
|インターフェース |言語 |説明 |
|----------|----------|---------------|
| **JDBC** |ジャワ |標準データベース API |
| **ODBC** |複数 |ユニバーサルデータベースAPI |
| **psycopg2/3** |パイソン | PostgreSQLアダプター |
| **データベース/SQL** |行く |ドライバーインターフェイスを備えた標準ライブラリ |
| **sqlite3** |パイソン |組み込みの SQLite サポート |
| **ページ** | Node.js | PostgreSQL クライアント |
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

## デザインパターン
### パターン 1: ピボット / クロス集計
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### パターン 2: グループごとの上位 N
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### パターン 3: ギャップとアイランド
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

### パターン 4: ゆっくりと変化する寸法 (SCD タイプ 2)
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

## パフォーマンス: インデックスとクエリ プランニング
### インデックスの仕組み
インデックスは、データベースがテーブル全体をスキャンせずに行を検索できるようにするデータ構造 (通常は B ツリー) です。
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

|インデックスの種類 |最適な用途 |例 |
|----------|----------|----------|
| **B ツリー** (デフォルト) |等価性クエリと範囲クエリ | `WHERE age > 25 AND age < 35`|
| **ハッシュ** |完全に等しい場合のみ | `WHERE email = 'x@y.com'`|
| **ジン** |全文検索、配列、JSON | `WHERE description @@ 'search term'`|
| **GiST** |幾何学・空間データ | `WHERE location <-> point(x,y) < 1000`|
### クエリプランの読み取り
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

## SQL の方言
|特集 |ポストグレSQL | MySQL | SQLサーバー | SQLite |
|-----------|-----------|----------|------------|--------|
|自動インクリメント | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
|文字列連結 | `\|\|`| `CONCAT()`| `+`または`CONCAT()`| `\|\|`|
|日付関数 |  `NOW()`、`AGE()` |  `NOW()`、`DATEDIFF()` |  `GETDATE()`、`DATEDIFF()` | `DATE('now')`|
| JSON のサポート |素晴らしい (`jsonb`) |良い (`JSON`) |良い (`JSON`) |基本 (`JSON1`) |
|全文検索 |内蔵 (`tsvector`) |内蔵 |内蔵 |限定 |
|ウィンドウ関数 |はい |はい (8.0 以降) |はい |はい |
---

## デプロイメント
### データベース導入戦略
|戦略 |説明 |リスクレベル |
|----------|---------------|---------------|
| **移行ファイル** |バージョン管理された SQL スクリプトが順番に適用される |低い |
| **ブルーグリーンデプロイ** | 2 つの同一のデータベース。スイッチトラフィック |低い |
| **契約の展開** |新しい列の追加、二重書き込み、移行、古い列の削除 |低い |
| **直接 DDL** |本番環境で ALTER TABLE を直接実行する |高 |
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

## SQL を使用する場合
|シナリオ | SQL を使用する理由 |代替案 |
|----------|-----------|---------------|
|複雑なクエリを含むリレーショナル データ | SQL はそのように設計されています。 --- |
|トランザクションの整合性 (ACID) | SQL データベースは一貫性を保証します | --- |
|レポートと分析 |集計、ウィンドウ関数、CTE |非常に複雑な分析のための Python (Pandas) |
|データ整合性の制約 |外部キー、CHECK、UNIQUE、NOT NULL |アプリケーションレベルの検証 (弱い) |
|シンプルなキーと値のストレージ |このユースケースには過剰です | Redis、DynamoDB |
|高度に非構造化されたデータ |スキーマの硬直性が問題です。 MongoDB、ドキュメント データベース |
|大規模な水平スケーリング | SQL データベースのシャード化が困難 | Cassandra、DynamoDB、CockroachDB |
---

## 総合的な Q&A
### Q1:`WHERE`と`HAVING`の違いは何ですか?
**A:**`WHERE`はグループ化する前に行をフィルタリングします。 `HAVING`は、集約後にグループをフィルタリングします。
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2: ウィンドウ関数は GROUP BY とどう違うのですか?
**A:** ウィンドウ関数は行を折りたたむことなく複数の行にわたって計算します。
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3: 遅いクエリを最適化するにはどうすればよいですか?
**A:** 主な戦略:
-`WHERE`、`JOIN`、および`ORDER BY`で使用される列にインデックスを追加します。 
-`SELECT *`を避ける — 必要な列のみを選択します
-`EXPLAIN`/`EXPLAIN ANALYZE`を使用してクエリ プランを読み取る
- 可能な場合はサブクエリを JOIN に置き換えます。
- 可読性を高めるために CTE を使用します (通常、パフォーマンスの低下はありません)
- WHERE 内のインデックス付き列の関数を回避します。`WHERE YEAR(date) = 2024` ではなく`WHERE date >= '2024-01-01'`を使用してください。
### Q4: CTE とは何ですか?いつ使用する必要がありますか?
**A:** 共通テーブル式は、名前付きの一時結果セットを作成します。
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

### Q5: NULL 値を正しく処理するにはどうすればよいですか?
**A:** NULL は不明を表します。それ自体を含め、何とも等しくありません。
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

## 思考連鎖による問題解決
### 問題 1: グループごとの上位 N を見つける
**ステップ 1: 問題を理解する**
各部門で最も給与の高い従業員 3 人を見つけます。
**ステップ 2: アプローチを特定する**
`ROW_NUMBER()` を部門ごとに分割したウィンドウ関数を使用します。
**ステップ 3: 実装**```sql
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

**ステップ 4: 確認**
各部門の行数が最大 3 行であることを確認してください。必要に応じて、`DENSE_RANK()` を使用してタイを処理します。
### 問題 2: 前年比成長レポートの作成
**ステップ 1: 問題を理解する**
月次収益と前年比成長率を計算します。
**ステップ 2: アプローチを特定する**
グループ化には`DATE_TRUNC`を使用し、前年度の比較には`LAG()`ウィンドウ関数を使用します。
**ステップ 3: 実装**```sql
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

**ステップ 4: 確認**
最初の 12 か月に前年の NULL があることを確認します。既知の数値と比較して成長率を検証します。
### 問題 3: 行を列にピボットする
**ステップ 1: 問題を理解する**
変換ステータスは行から列までカウントされます。
**ステップ 2: アプローチを特定する**
条件付き集計を使用します (`SUM`内の`CASE`)。
**ステップ 3: 実装**```sql
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

**ステップ 4: 延長**
パーセント列と累計を追加します。
---

＃＃ まとめ
SQL は 50 年の歴史を持つ言語であり、今でも不可欠な言語です。すべての開発者、データ サイエンティスト、アナリストはそれを知っておく必要があります。コア言語は標準化されており、移植可能です。方言の違いは管理可能です。最新の SQL (ウィンドウ関数、CTE、および JSON サポートを備えた) は、ほとんどのデータ タスクに十分な表現力を備えています。主なスキルは、効率的なクエリの作成、インデックスの理解、クエリ プランの読み取り、適切なスキーマの設計です。データを扱う場合、SQL は交渉の余地がありません。