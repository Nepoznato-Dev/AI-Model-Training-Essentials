<!-- 
Этот файл был автоматически переведён с английского на русский язык.
Источник: sql_quick_ref.md
Примечание: технические термины, примеры кода и имена собственные могут оставаться на английском языке.
Для повышения точности перевода вносите правки через pull request.
-->

# SQL: краткое руководство-справочник

Основные команды SQL для работы с базами данных.

---

## Базовая структура запроса

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

## Получение данных (SELECT)

### Базовая выборка
```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, name, email FROM users;

-- Select with alias
SELECT name AS user_name, email AS contact FROM users;

-- Select distinct values
SELECT DISTINCT country FROM users;
```

### Фильтрация (WHERE)
```sql
-- Comparison operators
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- Starts with A
SELECT * FROM users WHERE name LIKE '%son';    -- Ends with son
SELECT * FROM users WHERE name LIKE '%test%';  -- Contains test
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- Logical operators
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### Сортировка и ограничение
```sql
-- Order by single column
SELECT * FROM products ORDER BY price DESC;

-- Order by multiple columns
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- Limit results
SELECT * FROM users LIMIT 10;

-- Offset (for pagination)
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Skip 20, take 10
```

---

## Функции агрегирования

```sql
-- Count rows
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- Sum, Average, Min, Max
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- Group by
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having (filter groups)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## Соединения (Joins)

### Внутреннее соединение (Inner Join)
```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### Левое/правое соединение (Left/Right Join)
```sql
-- All users, even those without orders
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- All orders, even those without users (rare)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Полное внешнее соединение (Full Outer Join)
```sql
-- All users and all orders (MySQL doesn't support FULL OUTER)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Декартово соединение (Cross Join)
```sql
-- Cartesian product (all combinations)
SELECT * FROM colors CROSS JOIN sizes;
```

### Самосоединение (Self Join)
```sql
-- Find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## Подзапросы

```sql
-- In WHERE clause
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- In SELECT clause
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- In FROM clause
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- With EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## Операции над множествами

```sql
-- UNION (remove duplicates)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (keep duplicates)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT (common rows)
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2024;

-- EXCEPT/MINUS (rows in first but not second)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## Изменение данных

### INSERT
```sql
-- Insert single row
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- Insert multiple rows
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- Insert from SELECT
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### UPDATE
```sql
-- Update single row
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- Update multiple columns
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- Update with JOIN
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### DELETE
```sql
-- Delete specific rows
DELETE FROM users WHERE id = 1;

-- Delete with condition
DELETE FROM orders WHERE order_date < '2023-01-01';

-- Delete with JOIN
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- Truncate table (faster, resets auto-increment)
TRUNCATE TABLE temp_data;
```

---

## Операции с таблицами

### Создание таблицы (CREATE TABLE)
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

### Изменение таблицы (ALTER TABLE)
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Modify column
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- Rename column
ALTER TABLE users RENAME COLUMN username TO user_name;

-- Drop column
ALTER TABLE users DROP COLUMN phone;

-- Add constraint
ALTER TABLE orders ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) REFERENCES users(id);

-- Drop constraint
ALTER TABLE orders DROP FOREIGN KEY fk_user;

-- Rename table
ALTER TABLE old_name RENAME TO new_name;
```

### Удаление таблицы (DROP TABLE)
```sql
DROP TABLE IF EXISTS temp_table;
```

---

## Ограничения (Constraints)

```sql
-- PRIMARY KEY: Unique identifier
CREATE TABLE users (
    id INT PRIMARY KEY
);

-- FOREIGN KEY: Reference to another table
CREATE TABLE orders (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- UNIQUE: No duplicate values
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- NOT NULL: Required field
CREATE TABLE users (
    name VARCHAR(50) NOT NULL
);

-- CHECK: Validate values
CREATE TABLE products (
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0)
);

-- DEFAULT: Default value
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Индексы (Indexes)

```sql
-- Create index
CREATE INDEX idx_email ON users(email);

-- Create composite index
CREATE INDEX idx_name_age ON users(last_name, first_name);

-- Create unique index
CREATE UNIQUE INDEX idx_username ON users(username);

-- Drop index
DROP INDEX idx_email ON users;

-- View indexes
SHOW INDEX FROM users;
```

---

## Представления (Views)

```sql
-- Create view
CREATE VIEW active_users AS
SELECT id, name, email, country
FROM users
WHERE status = 'active';

-- Use view
SELECT * FROM active_users WHERE country = 'USA';

-- Update view (if updatable)
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, country, created_at
FROM users
WHERE status = 'active';

-- Drop view
DROP VIEW IF EXISTS active_users;
```

---

## Общие табличные выражения (CTE)

```sql
-- Simple CTE
WITH high_value_users AS (
    SELECT id, name, total_spent
    FROM users
    WHERE total_spent > 1000
)
SELECT * FROM high_value_users ORDER BY total_spent DESC;

-- Recursive CTE (hierarchical data)
WITH RECURSIVE org_chart AS (
    -- Base case
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## Оконные функции (Window Functions)

```sql
-- ROW_NUMBER
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK and DENSE_RANK
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Running total
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- Partitioned window
SELECT department, name, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- LAG and LEAD
SELECT date, sales,
       LAG(sales, 1) OVER (ORDER BY date) AS prev_day_sales,
       LEAD(sales, 1) OVER (ORDER BY date) AS next_day_sales
FROM daily_sales;
```

---

## Типы данных

### Числовые
- `INT` — целое число
- `BIGINT` — большое целое число
- `DECIMAL(p,s)` — точное десятичное число (точность, масштаб)
- `FLOAT` — приблизительное число с плавающей точкой
- `DOUBLE` — число с плавающей точкой двойной точности

### Строковые
- `CHAR(n)` — строка фиксированной длины
- `VARCHAR(n)` — строка переменной длины
- `TEXT` — большой текст
- `ENUM` — перечисляемые значения

### Дата/время
- `DATE` — дата (ГГГГ-ММ-ДД)
- `TIME` — время (ЧЧ:ММ:СС)
- `DATETIME` — дата и время
- `TIMESTAMP` — временная метка Unix
- `YEAR` — значение года

### Логический тип
- `BOOLEAN` или `BOOL` — логическое значение (истина/ложь)

### Двоичные
- `BLOB` — большой двоичный объект
- `BINARY` — фиксированный двоичный тип
- `VARBINARY` — двоичный тип переменной длины

---

## Полезные функции

### Строковые функции
```sql
CONCAT(first_name, ' ', last_name)  -- Concatenate strings
UPPER(name)                          -- Convert to uppercase
LOWER(name)                          -- Convert to lowercase
SUBSTRING(name, 1, 3)                -- Extract substring
LENGTH(name)                         -- String length
TRIM(name)                           -- Remove whitespace
REPLACE(text, 'old', 'new')          -- Replace substring
```

### Функции для работы с датами
```sql
NOW()                                -- Current date/time
CURDATE()                            -- Current date
CURTIME()                            -- Current time
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- Add interval
DATEDIFF(end_date, start_date)       -- Difference in days
YEAR(date_column)                    -- Extract year
MONTH(date_column)                   -- Extract month
DAY(date_column)                     -- Extract day
```

### Числовые функции
```sql
ROUND(value, 2)                      -- Round to decimals
CEIL(value)                          -- Round up
FLOOR(value)                         -- Round down
ABS(value)                           -- Absolute value
POWER(base, exp)                     -- Exponentiation
SQRT(value)                          -- Square root
RAND()                               -- Random number
```

### Условные функции
```sql
-- CASE statement
SELECT name,
       CASE 
           WHEN age < 18 THEN 'Minor'
           WHEN age < 65 THEN 'Adult'
           ELSE 'Senior'
       END AS age_group
FROM users;

-- IF function (MySQL)
SELECT IF(age >= 18, 'Adult', 'Minor') AS status FROM users;

-- COALESCE (return first non-null)
SELECT COALESCE(phone, email, 'No contact') AS contact FROM users;

-- NULLIF (return NULL if equal)
SELECT NULLIF(value, 0) AS safe_value FROM data;
```

---

## Советы по производительности

✅ **Стоит делать:**
- Используйте индексы для часто запрашиваемых столбцов
- Выбирайте только нужные столбцы (избегайте `SELECT *`)
- Используйте `EXPLAIN` для анализа производительности запроса
- Нормализуйте данные должным образом
- Используйте подготовленные выражения для защиты от SQL-инъекций

❌ **Не стоит делать:**
- Применять функции к индексированным столбцам в условиях WHERE
- Создавать слишком много индексов (замедляет запись)
- Использовать `SELECT DISTINCT` без необходимости
- Игнорировать планы выполнения запросов
- Хранить вычисляемые значения, которые можно рассчитать на лету

---

## Лучшие практики безопасности

```sql
-- Use parameterized queries (in application code)
-- NEVER concatenate user input directly

-- Grant minimal privileges
GRANT SELECT, INSERT ON database.table TO 'user'@'localhost';
REVOKE DELETE ON database.table FROM 'user'@'localhost';

-- Use strong passwords
-- Enable SSL connections
-- Regular security audits
```

---

*Последнее обновление: июнь 2025 | Стандарт SQL (совместим с MySQL/PostgreSQL)*
