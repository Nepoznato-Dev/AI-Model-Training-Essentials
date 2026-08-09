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
SQL (язык структурированных запросов) — это предметно-ориентированный язык, предназначенный для управления данными и запроса данных в реляционных базах данных. SQL, впервые разработанный в IBM в 1970-х годах и стандартизированный в 1987 году, остается основным интерфейсом между приложениями и их данными. Каждая крупная система управления реляционными базами данных (СУБД) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — использует SQL в качестве языка запросов.
SQL не является языком программирования общего назначения. Вы бы не стали писать веб-приложение на SQL. Но если ваше приложение хранит данные (а это делают почти все приложения), то SQL — это язык, который вы используете для извлечения, преобразования и управления этими данными. Это, возможно, самый универсальный технический навык после общего программирования.
---

## Почему SQL важен
- **Универсальность**: каждая реляционная база данных использует SQL. Выучите один раз и используйте везде.
- **Декларативный**: вы описываете, *какие* данные вам нужны, а не *как* их получить. Ядро базы данных оптимизирует выполнение.
- **Необходимо для любого разработчика**: серверная часть, обработка данных, DevOps, аналитика — для всего требуется SQL.
- **Мощность**: оконные функции, CTE, подзапросы и агрегаты позволяют выражать сложную логику в нескольких строках.
- **Производительность**. Хорошо написанный SQL-запрос к правильно индексированной базе данных может обрабатывать миллионы строк за миллисекунды.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Не является языком общего назначения** | Невозможно создавать приложения, API или алгоритмы на SQL | Комбинируйте с Python, Java, JavaScript и т. д. |
| **Диалектные различия** | Каждая СУБД имеет свой собственный вариант SQL с несовместимыми расширениями | По возможности придерживайтесь ANSI SQL; абстрактные диалектные различия в вашем приложении |
| **Жесткость схемы** | Изменение структуры таблиц в больших таблицах может быть медленным и разрушительным | Используйте инструменты миграции; тщательно разрабатывайте схемы заранее |
| **Проблема запроса N+1** | Запросы, генерируемые ORM, могут быть крайне неэффективными | Написание собственного SQL для сложных запросов; профиль с EXPLAIN ANALYZE |
| **Масштабирование сложности** | Базы данных SQL труднее масштабировать по горизонтали, чем NoSQL | Используйте реплики чтения, сегментирование или рассмотрите NoSQL для конкретных случаев использования |
---

## Основные понятия
### Реляционная модель
Данные хранятся в **таблицах** (отношениях), которые состоят из **строк** (записей/кортежей) и **столбцов** (атрибутов/полей). Таблицы могут быть связаны друг с другом посредством **ключей**.
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

## Основы синтаксиса
### Получение данных (ВЫБРАТЬ)
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

### Агрегация
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

### Соединение таблиц
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

### Изменение данных
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

## Расширенный синтаксис и шаблоны
### Оконные функции — подробное описание
Оконные функции выполняют вычисления над набором строк, связанных с текущей строкой, не сжимая их в одну выходную строку, как это делает GROUP BY.
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

### Общие табличные выражения (CTE) — расширенное использование
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

### Операции JSON
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

### Хранимые процедуры и триггеры
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

## Глубокое погружение в основные функции
### Оптимизация запросов
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

**Контрольный список оптимизации:**
| Выпуск | Симптом | Исправить |
|-------|---------|-----|
| Последовательное сканирование на большом столе | `Seq Scan`в EXPLAIN | Добавьте соответствующий индекс |
| Отсутствует индекс в столбце WHERE | Полное сканирование таблицы | Создать индекс по отфильтрованным столбцам |
| ВЫБЕРИТЕ * отходы | Получение ненужных столбцов | Выберите только необходимые столбцы |
| Неявное преобразование типов | Индекс не используется | Типы совпадений в сравнениях |
| Функции для индексированных столбцов | Индекс непригоден для использования (не подлежит записи) | Перепишите:`WHERE date >= '2024-01-01'`вместо`WHERE YEAR(date) = 2024`|
### Стратегии индексирования
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

### Уровни изоляции транзакций
| Уровень изоляции | Грязное чтение | Неповторяемый Читать | Фантомное чтение |
|-----------------|:----------:|:-------------------:|:------------:|
| ПРОЧИТАТЬ НЕПРЕРЫВНО | Да | Да | Да |
| ПРОЧИТАТЬ СОВЕРШЕНО | Нет | Да | Да |
| ПОВТОРНОЕ ЧТЕНИЕ | Нет | Нет | Да* |
| СЕРИАЛИЗУЕМЫЙ | Нет | Нет | Нет |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Нормализация
| Нормальная форма | Правило | Пример нарушения |
|-------------|------|-------------------|
| **1НФ** | Атомарные значения, без повторяющихся групп | Сохранение нескольких телефонов в одном столбце как «123,456» |
| **2НФ** | 1NF + нет частичных зависимостей | Детализация заказа зависит от order_id, но не от Product_id |
| **3НФ** | 2НФ + отсутствие транзитивных зависимостей | Имя отдела сотрудника зависит от dept_id, а не от сотрудника |
---

## Определение структуры базы данных
### Создание таблиц
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

### Изменение таблиц
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Конфигурация проекта и система сборки
### Инструменты миграции
| Инструмент | Язык/Стек | Подход |
|------|---------------|----------|
| **Пролетный путь** | Java / общее | Миграция на основе SQL, простое соглашение об именах |
| **Ликибаза** | Java / общее | Журналы изменений XML, YAML, JSON или SQL |
| **Алембик** | Питон (SQLAlchemy) | Автоматически генерирует миграции на основе изменений модели |
| **Присма Миграция** | Node.js/TypeScript | Схема сначала автоматически генерирует SQL |
| **голанг-мигрировать** | Перейти | На основе SQL, поддерживает миграцию вверх/вниз |
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

## Тестирование
### Генерация тестовых данных
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

| Рамочная | База данных | Описание |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Платформа модульного тестирования |
| **tSQLt** | SQL-сервер | Модульное тестирование для SQL Server |
| **utPLSQL** | Оракул | Среда тестирования для Oracle PL/SQL |
---

## Совместимость
### Языковые привязки
| Интерфейс | Язык | Описание |
|-----------|----------|-------------|
| **JDBC** | Ява | Стандартный API базы данных |
| **ODBC** | Несколько | Универсальный API базы данных |
| **псикопг2/3** | Питон | Адаптер PostgreSQL |
| **база данных/sql** | Перейти | Стандартная библиотека с интерфейсом драйвера |
| **sqlite3** | Питон | Встроенная поддержка SQLite |
| **стр** | Node.js | Клиент PostgreSQL |
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

## Шаблоны проектирования
### Шаблон 1: сводная таблица/перекрестная таблица
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Схема 2: Топ-N на группу
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Схема 3: Пробелы и острова
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

### Схема 4: Медленное изменение размеров (SCD типа 2)
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

## Производительность: индексы и планирование запросов
### Как работают индексы
Индекс — это структура данных (обычно B-дерево), которая позволяет базе данных находить строки без сканирования всей таблицы.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Тип индекса | Лучшее для | Пример |
|-----------|----------|---------|
| **B-дерево** (по умолчанию) | Запросы на равенство и диапазон | `WHERE age > 25 AND age < 35`|
| **Хеш** | Только точное равенство | `WHERE email = 'x@y.com'`|
| **ДЖИН** | Полнотекстовый поиск, массивы, JSON | `WHERE description @@ 'search term'`|
| **ГиСТ** | Геометрические/пространственные данные |  __ЗАЩИЩЕНО_3__ |
### Чтение планов запросов
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

## Диалекты SQL
| Особенность | PostgreSQL | MySQL | SQL-сервер | SQLite |
|---------|-----------|-------|------------|--------|
| Автоинкремент | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`|  __ЗАЩИЩЕНО_3__ | `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Конкат строк | `\|\|`| `CONCAT()`| `+`или`CONCAT()`| `\|\|`|
| Функции даты | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Поддержка JSON | Отлично (`jsonb`) | Хорошо (`JSON`) | Хорошо (`JSON`) | Базовый (`JSON1`) |
| Полнотекстовый поиск | Встроенный (`tsvector`) | Встроенный | Встроенный | Ограниченная |
| Оконные функции | Да | Да (8.0+) | Да | Да |
---

## Развертывание
### Стратегии развертывания базы данных
| Стратегия | Описание | Уровень риска |
|----------|-------------|------------|
| **Файлы миграции** | Версионные сценарии SQL применяются по порядку | Низкий |
| **Сине-зеленое развертывание** | Две идентичные базы данных; переключить трафик | Низкий |
| **Расширенный контракт** | Добавить новый столбец, двойную запись, перенести, удалить старый | Низкий |
| **Прямой DDL** | Запуск ALTER TABLE непосредственно в рабочей среде | Высокий |
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

## Когда использовать SQL
| Сценарий | Почему SQL | Альтернатива |
|----------|---------|-------------|
| Реляционные данные со сложными запросами | Именно для этого создан SQL | --- |
| Транзакционная целостность (ACID) | Базы данных SQL гарантируют согласованность | --- |
| Отчетность и аналитика | Агрегации, оконные функции, CTE | Python (Pandas) для очень сложного анализа |
| Ограничения целостности данных | Внешние ключи, CHECK, UNIQUE, NOT NULL | Проверка на уровне приложения (более слабая) |
| Простое хранилище ключей и значений | Избыток для этого варианта использования | Редис, DynamoDB |
| Сильно неструктурированные данные | Жесткость схемы — проблема | MongoDB, базы данных документов |
| Массивное горизонтальное масштабирование | Трудно сегментировать базы данных SQL | Кассандра, DynamoDB, CockroachDB |
---

## Краткое содержание
SQL — это язык с 50-летней историей, который по-прежнему важен. Это должен знать каждый разработчик, специалист по данным и аналитик. Основной язык стандартизирован и переносим; диалектные различия преодолимы. Современный SQL (с оконными функциями, CTE и поддержкой JSON) достаточно выразителен для большинства задач с данными. Ключевые навыки: написание эффективных запросов, понимание индексов, чтение планов запросов и проектирование хороших схем. Если вы вообще работаете с данными, SQL не подлежит обсуждению.