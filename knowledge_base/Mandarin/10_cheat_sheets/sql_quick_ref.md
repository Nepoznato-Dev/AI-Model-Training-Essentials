# SQL 快速參考指南

資料庫操作的必備 SQL 指令。

---

## 基本查詢結構

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column(s)
HAVING condition
ORDER BY column [ASC|DESC]
LIMIT number;
```

---

## 資料檢索（SELECT）

### 基本選擇
```sql
-- 選擇所有欄位
SELECT * FROM users;

-- 選擇特定欄位
SELECT id, name, email FROM users;

-- 使用別名選擇
SELECT name AS user_name, email AS contact FROM users;

-- 選擇不重複的值
SELECT DISTINCT country FROM users;
```

### 過濾（WHERE）
```sql
-- 比較運算子
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- 以 A 開頭
SELECT * FROM users WHERE name LIKE '%son';    -- 以 son 結尾
SELECT * FROM users WHERE name LIKE '%test%';  -- 包含 test
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- 邏輯運算子
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### 排序與限制
```sql
-- 按單一欄位排序
SELECT * FROM products ORDER BY price DESC;

-- 按多個欄位排序
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- 限制結果
SELECT * FROM users LIMIT 10;

-- 偏移量（用於分頁）
SELECT * FROM users LIMIT 10 OFFSET 20;  -- 跳過 20 筆，取 10 筆
```

---

## 聚合函式

```sql
-- 計算列數
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- 總和、平均、最小、最大
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- 分組
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having（過濾群組）
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## 連接（Joins）

### 內連接
```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### 左/右連接
```sql
-- 所有使用者，即使沒有訂單
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- 所有訂單，即使沒有使用者（罕見）
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### 完全外連接
```sql
-- 所有使用者和所有訂單（MySQL 不支援 FULL OUTER）
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### 交叉連接
```sql
-- 笛卡爾積（所有組合）
SELECT * FROM colors CROSS JOIN sizes;
```

### 自連接
```sql
-- 尋找員工及其主管
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## 子查詢

```sql
-- 在 WHERE 子句中
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- 在 SELECT 子句中
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- 在 FROM 子句中
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- 使用 EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## 集合操作

```sql
-- UNION（移除重複）
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL（保留重複）
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT（共同列）
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2024;

-- EXCEPT/MINUS（第一個中有但第二個中沒有的列）
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## 資料修改

### INSERT
```sql
-- 插入單列
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- 插入多列
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- 從 SELECT 插入
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### UPDATE
```sql
-- 更新單列
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- 更新多個欄位
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- 使用 JOIN 更新
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### DELETE
```sql
-- 刪除特定列
DELETE FROM users WHERE id = 1;

-- 使用條件刪除
DELETE FROM orders WHERE order_date < '2023-01-01';

-- 使用 JOIN 刪除
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- 截斷表格（更快，重設自動遞增）
TRUNCATE TABLE temp_data;
```

---

## 表格操作

### CREATE Table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    age INT CHECK (age >= 18),
    country VARCHAR(50) DEFAULT 'USA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_country (country)
);
```

### ALTER Table
```sql
-- 新增欄位
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- 修改欄位
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- 重新命名欄位
ALTER TABLE users RENAME COLUMN username TO user_name;

-- 刪除欄位
ALTER TABLE users DROP COLUMN phone;

-- 新增約束
ALTER TABLE orders ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) REFERENCES users(id);

-- 刪除約束
ALTER TABLE orders DROP FOREIGN KEY fk_user;

-- 重新命名表格
ALTER TABLE old_name RENAME TO new_name;
```

### DROP Table
```sql
DROP TABLE IF EXISTS temp_table;
```

---

## 約束

```sql
-- PRIMARY KEY：唯一識別符
CREATE TABLE users (
    id INT PRIMARY KEY
);

-- FOREIGN KEY：參照另一個表格
CREATE TABLE orders (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- UNIQUE：無重複值
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- NOT NULL：必填欄位
CREATE TABLE users (
    name VARCHAR(50) NOT NULL
);

-- CHECK：驗證值
CREATE TABLE products (
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0)
);

-- DEFAULT：預設值
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 索引

```sql
-- 建立索引
CREATE INDEX idx_email ON users(email);

-- 建立複合索引
CREATE INDEX idx_name_age ON users(last_name, first_name);

-- 建立唯一索引
CREATE UNIQUE INDEX idx_username ON users(username);

-- 刪除索引
DROP INDEX idx_email ON users;

-- 檢視索引
SHOW INDEX FROM users;
```

---

## 視圖

```sql
-- 建立視圖
CREATE VIEW active_users AS
SELECT id, name, email, country
FROM users
WHERE status = 'active';

-- 使用視圖
SELECT * FROM active_users WHERE country = 'USA';

-- 更新視圖（如果可更新）
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, country, created_at
FROM users
WHERE status = 'active';

-- 刪除視圖
DROP VIEW IF EXISTS active_users;
```

---

## 共同表格運算式（CTE）

```sql
-- 簡單 CTE
WITH high_value_users AS (
    SELECT id, name, total_spent
    FROM users
    WHERE total_spent > 1000
)
SELECT * FROM high_value_users ORDER BY total_spent DESC;

-- 遞迴 CTE（階層資料）
WITH RECURSIVE org_chart AS (
    -- 基礎情況
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- 遞迴情況
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## 視窗函式

```sql
-- ROW_NUMBER
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK 和 DENSE_RANK
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- 累計總和
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- 分割視窗
SELECT department, name, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- LAG 和 LEAD
SELECT date, sales,
       LAG(sales, 1) OVER (ORDER BY date) AS prev_day_sales,
       LEAD(sales, 1) OVER (ORDER BY date) AS next_day_sales
FROM daily_sales;
```

---

## 資料型別

### 數值
- `INT` - 整數
- `BIGINT` - 大整數
- `DECIMAL(p,s)` - 精確小數（精度，刻度）
- `FLOAT` - 近似浮點數
- `DOUBLE` - 雙精度浮點數

### 字串
- `CHAR(n)` - 固定長度字串
- `VARCHAR(n)` - 可變長度字串
- `TEXT` - 大文字
- `ENUM` - 列舉值

### 日期/時間
- `DATE` - 日期（YYYY-MM-DD）
- `TIME` - 時間（HH:MM:SS）
- `DATETIME` - 日期和時間
- `TIMESTAMP` - Unix 時間戳記
- `YEAR` - 年份值

### 布林
- `BOOLEAN` 或 `BOOL` - True/False

### 二進位
- `BLOB` - 二進位大物件
- `BINARY` - 固定二進位
- `VARBINARY` - 可變二進位

---

## 實用函式

### 字串函式
```sql
CONCAT(first_name, ' ', last_name)  -- 連接字串
UPPER(name)                          -- 轉換為大寫
LOWER(name)                          -- 轉換為小寫
SUBSTRING(name, 1, 3)                -- 提取子字串
LENGTH(name)                         -- 字串長度
TRIM(name)                           -- 移除空白
REPLACE(text, 'old', 'new')          -- 替換子字串
```

### 日期函式
```sql
NOW()                                -- 目前日期/時間
CURDATE()                            -- 目前日期
CURTIME()                            -- 目前時間
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- 新增間隔
DATEDIFF(end_date, start_date)       -- 日期差異（天）
YEAR(date_column)                    -- 提取年份
MONTH(date_column)                   -- 提取月份
DAY(date_column)                     -- 提取日
```

### 數值函式
```sql
ROUND(value, 2)                      -- 四捨五入至小數位
CEIL(value)                          -- 無條件進位
FLOOR(value)                         -- 無條件捨去
ABS(value)                           -- 絕對值
POWER(base, exp)                     -- 指數運算
SQRT(value)                          -- 平方根
RAND()                               -- 隨機數
```

### 條件函式
```sql
-- CASE 陳述式
SELECT name,
       CASE 
           WHEN age < 18 THEN 'Minor'
           WHEN age < 65 THEN 'Adult'
           ELSE 'Senior'
       END AS age_group
FROM users;

-- IF 函式（MySQL）
SELECT IF(age >= 18, 'Adult', 'Minor') AS status FROM users;

-- COALESCE（返回第一個非 NULL）
SELECT COALESCE(phone, email, 'No contact') AS contact FROM users;

-- NULLIF（如果相等則返回 NULL）
SELECT NULLIF(value, 0) AS safe_value FROM data;
```

---

## 效能提示

✅ **應該做的：**
- 在經常查詢的欄位上使用索引
- 僅選擇需要的欄位（避免 `SELECT *`）
- 使用 `EXPLAIN` 分析查詢效能
- 適當地正規化資料
- 使用預備陳述式防止 SQL 注入

❌ **不應該做的：**
- 在 WHERE 子句中對索引欄位使用函式
- 建立太多索引（減慢寫入速度）
- 不必要地使用 `SELECT DISTINCT`
- 忽略查詢執行計劃
- 儲存可以計算的計算值

---

## 安全最佳實踐

```sql
-- 使用參數化查詢（在應用程式程式碼中）
-- 絕不直接串接使用者輸入

-- 授予最小權限
GRANT SELECT, INSERT ON database.table TO 'user'@'localhost';
REVOKE DELETE ON database.table FROM 'user'@'localhost';

-- 使用強密碼
-- 啟用 SSL 連線
-- 定期安全稽核
```

---

*最後更新：2025年6月 | SQL 標準（MySQL/PostgreSQL 相容）*
