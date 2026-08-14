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
#SQL
SQL (Structured Query Language) to język specyficzny dla domeny, przeznaczony do zarządzania danymi i wysyłania zapytań do danych w relacyjnych bazach danych. Język SQL, opracowany po raz pierwszy w IBM w latach 70. XX wieku i ustandaryzowany w 1987 r., pozostaje głównym interfejsem między aplikacjami i ich danymi. Każdy większy system zarządzania relacyjnymi bazami danych (RDBMS) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — używa języka SQL jako języka zapytań.
SQL nie jest językiem programowania ogólnego przeznaczenia. Nie napisałbyś aplikacji internetowej w SQL. Jeśli jednak Twoja aplikacja przechowuje dane — a prawie wszystkie aplikacje to robią — wówczas SQL jest językiem, którego używasz do pobierania, przekształcania i zarządzania tymi danymi. Jest to prawdopodobnie najbardziej uniwersalnie przydatna umiejętność techniczna po ogólnym programowaniu.
---

## Dlaczego SQL ma znaczenie
- **Uniwersalny**: Każda relacyjna baza danych mówi w języku SQL. Naucz się tego raz, używaj go wszędzie.
- **Deklaratywny**: Opisujesz *jakie* dane chcesz, a nie *jak* je zdobyć. Silnik bazy danych optymalizuje wykonanie.
- **Niezbędne dla każdego programisty**: Backend, analityka danych, DevOps, analityka — wszystkie wymagają SQL.
- **Potężne**: Funkcje okna, CTE, podzapytania i agregacje pozwalają wyrazić złożoną logikę w kilku wierszach.
- **Wydajność**: Dobrze napisane zapytanie SQL w odpowiednio zindeksowanej bazie danych może przetworzyć miliony wierszy w ciągu milisekund.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Nie jest to język ogólnego zastosowania** | Nie można tworzyć aplikacji, interfejsów API ani algorytmów w języku SQL | Połącz z Pythonem, Javą, JavaScriptem itp. |
| **Różnice w dialektach** | Każdy RDBMS ma swój własny SQL z niekompatybilnymi rozszerzeniami | Jeśli to możliwe, trzymaj się ANSI SQL; różnice w abstrakcyjnych dialektach w Twojej aplikacji |
| **Sztywność schematu** | Zmiana struktury tabel na dużych tabelach może być powolna i destrukcyjna | Korzystaj z narzędzi migracyjnych; starannie projektuj schematy |
| **Problem z zapytaniem N+1** | Zapytania generowane przez ORM mogą być wyjątkowo nieefektywne | Napisz niestandardowy kod SQL dla złożonych zapytań; profil z WYJAŚNIJ ANALIZĘ |
| **Skalowanie złożoności** | Bazy danych SQL są trudniejsze do skalowania w poziomie niż NoSQL | Używaj replik do odczytu, fragmentowania lub rozważ NoSQL w konkretnych przypadkach użycia |
---

## Podstawowe pojęcia
### Model relacyjny
Dane przechowywane są w **tabelach** (relacjach), które składają się z **wierszy** (rekordów/krotek) i **kolumn** (atrybutów/pól). Tabele można ze sobą powiązać za pomocą **kluczy**.
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

## Podstawy składni
### Pobieranie danych (WYBIERZ)
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

### Agregacja
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

### Łączenie tabel
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

### Modyfikowanie danych
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

## Zaawansowana składnia i wzorce
### Funkcje okna — Głębokie nurkowanie
Funkcje okna wykonują obliczenia na zestawie wierszy powiązanych z bieżącym wierszem — bez zwijania ich w jeden wiersz wyjściowy, jak ma to miejsce w przypadku GROUP BY.
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

### Typowe wyrażenia tabelowe (CTE) — użycie zaawansowane
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

### Operacje JSON
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

### Procedury składowane i wyzwalacze
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

## Zagłęb się w podstawowe funkcje
### Optymalizacja zapytań
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

**Lista kontrolna optymalizacji:**
| Wydanie | Objaw | Napraw |
|-------|---------|-----|
| Skanowanie sekwencyjne na dużym stole | `Seq Scan`w WYJAŚNIJ | Dodaj odpowiedni indeks |
| Brak indeksu w kolumnie WHERE | Pełny skan tabeli | Utwórz indeks na filtrowanych kolumnach |
| WYBIERZ * odpady | Pobieranie niepotrzebnych kolumn | Wybierz tylko potrzebne kolumny |
| Niejawna konwersja typów | Indeks nieużywany | Typy dopasowań w porównaniach |
| Funkcje na kolumnach indeksowanych | Indeks nie nadaje się do użytku (nie można go używać) | Przepisz:`WHERE date >= '2024-01-01'`nie`WHERE YEAR(date) = 2024`|
### Strategie indeksowania
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

### Poziomy izolacji transakcji
| Poziom izolacji | Brudna lektura | Niepowtarzalny odczyt | Odczyt fantomowy |
|-----------------|:--------------:|:--------------------------------:|:------------:|
| CZYTAJ NIEZOBOWIĄZANE | Tak | Tak | Tak |
| CZYTAJ ZOBOWIĄZANE | Nie | Tak | Tak |
| POWTARZALNE CZYTANIE | Nie | Nie | Tak* |
| SERIALIZOWALNE | Nie | Nie | Nie |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalizacja
| Normalna forma | Zasada | Przykładowe naruszenie |
|------------|------|----------------------|
| **1NF** | Wartości atomowe, brak powtarzających się grup | Przechowywanie wielu telefonów w jednej kolumnie jako „123 456” |
| **2NF** | 1NF + brak częściowych zależności | Szczegóły zamówienia zależą od identyfikatora zamówienia, ale nie identyfikatora produktu |
| **3NF** | 2NF + brak zależności przechodnich | Nazwa działu pracownika zależy od identyfikatora działu, a nie pracownika |
---

## Definiowanie struktury bazy danych
### Tworzenie tabel
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

### Zmiana tabel
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Konfiguracja projektu i budowanie systemu
### Narzędzia do migracji
| Narzędzie | Język/stos | Podejście |
|------|-------------------|--------------|
| **Trasa przelotowa** | Java / ogólne | Migracje w oparciu o SQL, prosta konwencja nazewnictwa |
| **Likwibaza** | Java / ogólne | Dzienniki zmian XML, YAML, JSON lub SQL |
| **Alembik** | Python (SQLAlchemy) | Automatycznie generuje migracje na podstawie zmian w modelu |
| **Migracja Prisma** | Node.js / TypeScript | Najpierw schemat, automatycznie generuje SQL |
| **golang-migracja** | Idź | Oparty na SQL, obsługuje migracje w górę/w dół |
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

## Testowanie
### Testuj generowanie danych
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

| Ramy | Baza danych | Opis |
|----------|----------|------------|
| **pgTAP** | PostgreSQL | Struktura testów jednostkowych |
| **tSQLt** | Serwer SQL | Testowanie jednostkowe dla SQL Server |
| **utPLSQL** | Wyrocznia | Framework testowy dla Oracle PL/SQL |
---

## Interoperacyjność
### Powiązania językowe
| Interfejs | Język | Opis |
|----------|----------|------------|
| **JDBC** | Jawa | Standardowe API bazy danych |
| **ODBC** | Wiele | Uniwersalne API baz danych |
| **psycopg2/3** | Pythona | Adapter PostgreSQL |
| **baza danych/sql** | Idź | Standardowa biblioteka z interfejsem sterownika |
| **sqlite3** | Pythona | Wbudowana obsługa SQLite |
| **str.** | Node.js | Klient PostgreSQL |
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

## Wzorce projektowe
### Wzór 1: Tabela przestawna/przestawna
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Wzór 2: Top-N na grupę
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Wzór 3: Luki i wyspy
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

### Wzór 4: Powolna zmiana wymiarów (SCD typ 2)
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

## Wydajność: Indeksy i planowanie zapytań
### Jak działają indeksy
Indeks to struktura danych (zwykle drzewo B), która umożliwia bazie danych znajdowanie wierszy bez skanowania całej tabeli.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Typ indeksu | Najlepsze dla | Przykład |
|----------|----------|---------|
| **B-drzewo** (domyślnie) | Zapytania o równość i zakres | `WHERE age > 25 AND age < 35`|
| **Hasz** | Tylko dokładna równość | `WHERE email = 'x@y.com'`|
| **GIN** | Wyszukiwanie pełnotekstowe, tablice, JSON | `WHERE description @@ 'search term'`|
| **GIST** | Dane geometryczne/przestrzenne | `WHERE location <-> point(x,y) < 1000`|
### Czytanie planów zapytań
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

## Dialekty SQL
| Funkcja | PostgreSQL | MySQL | Serwer SQL | SQLite |
|--------|-----------|-------|------------|--------|
| Automatyczny przyrost | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Połączenie ciągu | `\|\|`| `CONCAT()`| `+`lub`CONCAT()`| `\|\|`|
| Funkcje daty | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Obsługa JSON | Znakomity (`jsonb`) | Dobry (`JSON`) | Dobry (`JSON`) | Podstawowy (`JSON1`) |
| Wyszukiwanie pełnotekstowe | Wbudowany (`tsvector`) | Wbudowany | Wbudowany | ograniczona |
| Funkcje okna | Tak | Tak (8.0+) | Tak | Tak |
---

## Zastosowanie
### Strategie wdrażania baz danych
| Strategia | Opis | Poziom ryzyka |
|---------|------------|------------|
| **Pliki migracji** | Wersjonowane skrypty SQL zastosowane w kolejności | Niski |
| **Niebiesko-zielone wdrożenie** | Dwie identyczne bazy danych; przełączyć ruch | Niski |
| **Rozszerz umowę** | Dodaj nową kolumnę, zapisz podwójnie, migruj, usuń stare | Niski |
| **Bezpośredni DDL** | Uruchamianie ALTER TABLE bezpośrednio na produkcji | Wysoki |
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

## Kiedy używać SQL
| Scenariusz | Dlaczego SQL | Alternatywa |
|---------|---------|------------|
| Dane relacyjne ze złożonymi zapytaniami | Właśnie do tego przeznaczony jest SQL | --- |
| Integralność transakcyjna (ACID) | Bazy danych SQL gwarantują spójność | --- |
| Raportowanie i analityka | Agregacje, funkcje okienkowe, CTE | Python (Pandas) do bardzo złożonych analiz |
| Ograniczenia integralności danych | Klucze obce, SPRAWDŹ, UNIKALNE, NIE NULL | Walidacja na poziomie aplikacji (słabsza) |
| Proste przechowywanie klucz-wartość | Przesada w tym przypadku użycia | Redis, DynamoDB |
| Dane wysoce nieustrukturyzowane | Sztywność schematu jest problemem | MongoDB, bazy dokumentów |
| Ogromne skalowanie poziome | Trudno podzielić bazy danych SQL | Cassandra, DynamoDB, KaraluchDB |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między`WHERE`a `HAVING`?
**A:**`WHERE`filtruje wiersze przed grupowaniem; `HAVING`filtruje grupy po agregacji:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### P2: Czym różnią się funkcje okna od funkcji GROUP BY?
**A:** Funkcje okna wykonują obliczenia w wierszach bez ich zwijania:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### P3: Jak zoptymalizować wolne zapytania?
**O:** Kluczowe strategie:
- Dodaj indeksy do kolumn używanych w`WHERE`,`JOIN`i`ORDER BY`
- Unikaj`SELECT *`— wybierz tylko potrzebne kolumny
- Użyj`EXPLAIN`/ `EXPLAIN ANALYZE`, aby odczytać plany zapytań
- Jeśli to możliwe, zamień podzapytania na JOIN
- Używaj CTE dla czytelności (zwykle nie ma to wpływu na wydajność)
- Unikaj funkcji w kolumnach indeksowanych w WHERE: użyj `WHERE date >= '2024-01-01'`, a nie `WHERE YEAR(date) = 2024`
### P4: Co to są współczynniki CTE i kiedy należy ich używać?
**A:** Typowe wyrażenia tabelowe tworzą nazwane tymczasowe zestawy wyników:
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

### P5: Jak poprawnie obsługiwać wartości NULL?
**A:** NULL oznacza nieznaną — nie jest równa niczemu, łącznie z samą sobą:
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

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Znajdowanie N pierwszych grup
**Krok 1: Zrozum problem**
Znajdź 3 najlepiej opłacanych pracowników w każdym dziale.
**Krok 2: Zidentyfikuj podejście**
Użyj funkcji okna z`ROW_NUMBER()`podzielonym według działów.
**Krok 3: Wdróż**```sql
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

**Krok 4: Zweryfikuj**
Sprawdź, czy każdy dział ma co najwyżej 3 wiersze. Jeśli to konieczne, obsłuż powiązania za pomocą `DENSE_RANK()`.
### Problem 2: Tworzenie raportu o wzroście rocznym
**Krok 1: Zrozum problem**
Oblicz miesięczne przychody i procent wzrostu rok do roku.
**Krok 2: Zidentyfikuj podejście**
Użyj`DATE_TRUNC`do grupowania i funkcji okna`LAG()`do porównania z poprzednim rokiem.
**Krok 3: Wdróż**```sql
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

**Krok 4: Zweryfikuj**
Sprawdź, czy pierwsze 12 miesięcy ma NULL dla poprzedniego roku. Porównaj procent wzrostu ze znanymi liczbami.
### Problem 3: Przesuwanie wierszy do kolumn
**Krok 1: Zrozum problem**
Przekształć liczniki stanu z wierszy na kolumny.
**Krok 2: Zidentyfikuj podejście**
Użyj agregacji warunkowej (`CASE`wewnątrz`SUM`).
**Krok 3: Wdróż**```sql
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

**Krok 4: Przedłuż**
Dodaj kolumny procentowe i sumy bieżące.
---

## Streszczenie
SQL to język mający 50 lat, który pozostaje niezbędny. Każdy programista, analityk danych i analityk musi to wiedzieć. Podstawowy język jest ustandaryzowany i przenośny; różnice w dialektach są do opanowania. Nowoczesny SQL (z funkcjami okiennymi, CTE i obsługą JSON) jest wystarczająco wyrazisty dla większości zadań związanych z danymi. Kluczowe umiejętności to: pisanie wydajnych zapytań, zrozumienie indeksów, czytanie planów zapytań i projektowanie dobrych schematów. Jeśli w ogóle pracujesz z danymi, SQL nie podlega negocjacjom.