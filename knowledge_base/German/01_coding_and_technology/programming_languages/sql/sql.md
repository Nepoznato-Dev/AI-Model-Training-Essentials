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
# SQL
SQL (Structured Query Language) ist eine domänenspezifische Sprache zur Verwaltung und Abfrage von Daten in relationalen Datenbanken. SQL wurde erstmals in den 1970er Jahren bei IBM entwickelt und 1987 standardisiert und ist nach wie vor die primäre Schnittstelle zwischen Anwendungen und ihren Daten. Jedes große relationale Datenbankmanagementsystem (RDBMS) – PostgreSQL, MySQL, SQL Server, Oracle, SQLite – verwendet SQL als Abfragesprache.
SQL ist keine Allzweck-Programmiersprache. Sie würden keine Webanwendung in SQL schreiben. Wenn Ihre Anwendung jedoch Daten speichert – und das tun fast alle Anwendungen –, dann ist SQL die Sprache, die Sie zum Abrufen, Transformieren und Verwalten dieser Daten verwenden. Nach der allgemeinen Programmierung handelt es sich wohl um die allgemein nützlichste technische Fähigkeit.
---

## Warum SQL wichtig ist
- **Universell**: Jede relationale Datenbank spricht SQL. Einmal lernen, überall nutzen.
- **Deklarativ**: Sie beschreiben, *welche* Daten Sie benötigen, nicht *wie* Sie diese erhalten. Die Datenbank-Engine optimiert die Ausführung.
- **Unverzichtbar für jeden Entwickler**: Backend, Datenwissenschaft, DevOps, Analysen – alle erfordern SQL.
- **Leistungsstark**: Mit Fensterfunktionen, CTEs, Unterabfragen und Aggregationen können Sie komplexe Logik in wenigen Zeilen ausdrücken.
- **Leistung**: Eine gut geschriebene SQL-Abfrage in einer ordnungsgemäß indizierten Datenbank kann Millionen von Zeilen in Millisekunden verarbeiten.
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Keine Allzwecksprache** | Anwendungen, APIs oder Algorithmen können nicht in SQL | erstellt werden Kombinieren Sie mit Python, Java, JavaScript usw. |
| **Dialektunterschiede** | Jedes RDBMS hat seine eigene SQL-Variante mit inkompatiblen Erweiterungen | Bleiben Sie nach Möglichkeit bei ANSI SQL. abstrakte Dialektunterschiede in Ihrer Anwendung |
| **Schemasteifigkeit** | Das Ändern von Tabellenstrukturen bei großen Tischen kann langsam und störend sein | Verwenden Sie Migrationstools. Entwerfen Sie Schemata sorgfältig im Voraus |
| **N+1-Abfrageproblem** | ORM-generierte Abfragen können äußerst ineffizient sein | Schreiben Sie benutzerdefiniertes SQL für komplexe Abfragen. Profil mit EXPLAIN ANALYZE |
| **Skalierung der Komplexität** | SQL-Datenbanken sind schwerer horizontal zu skalieren als NoSQL | Verwenden Sie Lesereplikate, Sharding oder erwägen Sie NoSQL für bestimmte Anwendungsfälle |
---

## Kernkonzepte
### Das relationale Modell
Daten werden in **Tabellen** (Beziehungen) gespeichert, die aus **Zeilen** (Datensätze/Tupel) und **Spalten** (Attribute/Felder) bestehen. Tabellen können über **Schlüssel** miteinander verknüpft werden.
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

## Syntax-Grundlagen
### Daten abrufen (SELECT)
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

### Aggregation
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

### Tabellen zusammenfügen
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

### Daten ändern
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

## Erweiterte Syntax und Muster
### Fensterfunktionen – Deep Dive
Fensterfunktionen führen Berechnungen über eine Reihe von Zeilen durch, die sich auf die aktuelle Zeile beziehen – ohne sie wie bei GROUP BY in einer einzigen Ausgabezeile zusammenzufassen.
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

### Gemeinsame Tabellenausdrücke (CTEs) – Erweiterte Verwendung
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

### JSON-Operationen
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

### Gespeicherte Prozeduren und Trigger
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

## Tauchen Sie tief in die Kernfunktionen ein
### Abfrageoptimierung
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

**Optimierungs-Checkliste:**
| Problem | Symptom | Fix |
|-------|---------|-----|
| Sequentielles Scannen auf einem großen Tisch | `Seq Scan`in EXPLAIN | Fügen Sie den entsprechenden Index hinzu |
| Fehlender Index für die WHERE-Spalte | Vollständiger Tabellenscan | Index für gefilterte Spalten erstellen |
| SELECT * Abfall | Unnötige Spalten abrufen | Wählen Sie nur die benötigten Spalten | aus
| Implizite Typkonvertierung | Index nicht verwendet | Übereinstimmungstypen in Vergleichen |
| Funktionen für indizierte Spalten | Index unbrauchbar (nicht sargable) | Umschreiben: `WHERE date >= '2024-01-01'`, nicht`WHERE YEAR(date) = 2024`|
### Indexierungsstrategien
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

### Transaktionsisolationsstufen
| Isolationsstufe | Schmutziges Lesen | Nicht wiederholbares Lesen | Phantom Read |
|-----------------|:----------:|:-------------------:|:------------:|
| UNVERPFLICHTET LESEN | Ja | Ja | Ja |
| LESEN SIE VERPFLICHTET | Nein | Ja | Ja |
| WIEDERHOLBARES LESEN | Nein | Nein | Ja* |
| SERIALISIERBAR | Nein | Nein | Nein |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalisierung
| Normalform | Regel | Beispielverstoß |
|-------------|------|-----|
| **1NF** | Atomare Werte, keine sich wiederholenden Gruppen | Mehrere Telefone in einer Spalte als „123.456“ speichern |
| **2NF** | 1NF + keine Teilabhängigkeiten | Die Bestelldetails hängen von der Bestell-ID ab, nicht jedoch von der Produkt-ID |
| **3NF** | 2NF + keine transitiven Abhängigkeiten | Der Abteilungsname des Mitarbeiters hängt von der Abteilungs-ID ab, nicht vom Mitarbeiter |
---

## Datenbankstruktur definieren
### Tabellen erstellen
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

### Tabellen ändern
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Projektkonfiguration und Build-System
### Migrationstools
| Werkzeug | Sprache/Stack | Ansatz |
|------|---------------|----------|
| **Flugbahn** | Java / allgemein | SQL-basierte Migrationen, einfache Namenskonvention |
| **Liquibase** | Java / allgemein | XML-, YAML-, JSON- oder SQL-Änderungsprotokolle |
| **Destillierkolben** | Python (SQLAlchemy) | Generiert automatisch Migrationen aus Modelländerungen |
| **Prisma migrieren** | Node.js / TypeScript | Schema-first, generiert automatisch SQL |
| **golang-migration** | Geh | SQL-basiert, unterstützt Up-/Down-Migrationen |
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

## Testen
### Testdatengenerierung
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

| Rahmen | Datenbank | Beschreibung |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Unit-Test-Framework |
| **tSQLt** | SQL-Server | Unit-Tests für SQL Server |
| **utPLSQL** | Orakel | Testframework für Oracle PL/SQL |
---

## Interoperabilität
### Sprachbindungen
| Schnittstelle | Sprache | Beschreibung |
|-----------|----------|-------------|
| **JDBC** | Java | Standard-Datenbank-API |
| **ODBC** | Mehrere | Universelle Datenbank-API |
| **psycopg2/3** | Python | PostgreSQL-Adapter |
| **Datenbank/SQL** | Geh | Standardbibliothek mit Treiberschnittstelle |
| **SQLite3** | Python | Integrierte SQLite-Unterstützung |
| **Seite** | Node.js | PostgreSQL-Client |
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

## Designmuster
### Muster 1: Pivot / Kreuztabelle
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Muster 2: Top-N pro Gruppe
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Muster 3: Lücken und Inseln
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

### Muster 4: Sich langsam ändernde Dimensionen (SCD-Typ 2)
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

## Leistung: Indizes und Abfrageplanung
### Wie Indizes funktionieren
Ein Index ist eine Datenstruktur (normalerweise ein B-Baum), die es der Datenbank ermöglicht, Zeilen zu finden, ohne die gesamte Tabelle zu durchsuchen.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Indextyp | Am besten für | Beispiel |
|-----------|----------|---------|
| **B-Baum** (Standard) | Gleichheits- und Bereichsabfragen | `WHERE age > 25 AND age < 35`|
| **Hash** | Nur exakte Gleichheit | `WHERE email = 'x@y.com'`|
| **GIN** | Volltextsuche, Arrays, JSON | `WHERE description @@ 'search term'`|
| **GiST** | Geometrische/räumliche Daten | `WHERE location <-> point(x,y) < 1000`|
### Abfragepläne lesen
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

## SQL-Dialekte
| Funktion | PostgreSQL | MySQL | SQL-Server | SQLite |
|---------|-----------|-------|------------|--------|
| Automatisches Inkrementieren | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| String-Verknüpfung | `\|\|`| `CONCAT()`| `+`oder`CONCAT()`| `\|\|`|
| Datumsfunktionen | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| JSON-Unterstützung | Ausgezeichnet (`jsonb`) | Gut (`JSON`) | Gut (`JSON`) | Basic (`JSON1`) |
| Volltextsuche | Eingebaut (`tsvector`) | Eingebaut | Eingebaut | Begrenzt |
| Fensterfunktionen | Ja | Ja (8.0+) | Ja | Ja |
---

## Bereitstellung
### Datenbankbereitstellungsstrategien
| Strategie | Beschreibung | Risikostufe |
|----------|-------------|------------|
| **Migrationsdateien** | Versionierte SQL-Skripte werden in der Reihenfolge | angewendet Niedrig |
| **Blau-grüner Einsatz** | Zwei identische Datenbanken; Verkehr wechseln | Niedrig |
| **Vertrag erweitern** | Neue Spalte hinzufügen, Dual-Write, migrieren, alte löschen | Niedrig |
| **Direktes DDL** | ALTER TABLE direkt in der Produktion ausführen | Hoch |
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

## Wann man SQL verwenden sollte
| Szenario | Warum SQL | Alternative |
|----------|---------|-------------|
| Relationale Daten mit komplexen Abfragen | Dafür ist SQL konzipiert | --- |
| Transaktionsintegrität (ACID) | SQL-Datenbanken garantieren Konsistenz | --- |
| Reporting und Analysen | Aggregationen, Fensterfunktionen, CTEs | Python (Pandas) für sehr komplexe Analysen |
| Einschränkungen der Datenintegrität | Fremdschlüssel, CHECK, UNIQUE, NOT NULL | Validierung auf Anwendungsebene (schwächer) |
| Einfache Schlüsselwertspeicherung | Overkill für diesen Anwendungsfall | Redis, DynamoDB |
| Stark unstrukturierte Daten | Schemastarrheit ist ein Problem | MongoDB, Dokumentendatenbanken |
| Massive horizontale Skalierung | Schwer zu teilende SQL-Datenbanken | Cassandra, DynamoDB, CockroachDB |
---

## Synthetische Fragen und Antworten
### F1: Was ist der Unterschied zwischen`WHERE`und `HAVING`?
**A:**`WHERE`filtert Zeilen vor der Gruppierung; `HAVING`filtert Gruppen nach der Aggregation:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### F2: Wie unterscheiden sich Fensterfunktionen von GROUP BY?
**A:** Fensterfunktionen berechnen zeilenübergreifend, ohne sie zu reduzieren:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### F3: Wie optimiere ich langsame Abfragen?
**A:** Schlüsselstrategien:
– Fügen Sie Indizes für Spalten hinzu, die in `WHERE`,`JOIN`und`ORDER BY`verwendet werden 
- Vermeiden Sie`SELECT *`– wählen Sie nur benötigte Spalten aus
- Verwenden Sie`EXPLAIN`/ `EXPLAIN ANALYZE`, um Abfragepläne zu lesen
- Ersetzen Sie Unterabfragen nach Möglichkeit durch JOINs
- Verwenden Sie CTEs zur besseren Lesbarkeit (normalerweise keine Leistungseinbußen).
- Vermeiden Sie Funktionen für indizierte Spalten in WHERE: Verwenden Sie `WHERE date >= '2024-01-01'`, nicht `WHERE YEAR(date) = 2024`
### F4: Was sind CTEs und wann sollte ich sie verwenden?
**A:** Gemeinsame Tabellenausdrücke erstellen benannte temporäre Ergebnismengen:
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

### F5: Wie gehe ich richtig mit NULL-Werten um?
**A:** NULL steht für unbekannt – es ist mit nichts gleich, auch nicht mit sich selbst:
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

## Problemlösung in der Gedankenkette
### Problem 1: Die Top N pro Gruppe finden
**Schritt 1: Verstehen Sie das Problem**
Finden Sie die 3 bestbezahlten Mitarbeiter in jeder Abteilung.
**Schritt 2: Identifizieren Sie den Ansatz**
Verwenden Sie eine Fensterfunktion mit `ROW_NUMBER()`, aufgeteilt nach Abteilung.
**Schritt 3: Implementieren**```sql
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

**Schritt 4: Überprüfen**
Stellen Sie sicher, dass jede Abteilung höchstens 3 Zeilen hat. Behandeln Sie Bindungen bei Bedarf mit `DENSE_RANK()`.
### Problem 2: Erstellen eines Jahreswachstumsberichts
**Schritt 1: Verstehen Sie das Problem**
Berechnen Sie den monatlichen Umsatz und den Wachstumsprozentsatz im Jahresvergleich.
**Schritt 2: Identifizieren Sie den Ansatz**
Verwenden Sie`DATE_TRUNC`zum Gruppieren und die Fensterfunktion`LAG()`für den Vorjahresvergleich.
**Schritt 3: Implementieren**```sql
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

**Schritt 4: Überprüfen**
Überprüfen Sie, ob die ersten 12 Monate NULL für das Vorjahr haben. Validieren Sie Wachstumsprozentsätze anhand bekannter Zahlen.
### Problem 3: Zeilen in Spalten umwandeln
**Schritt 1: Verstehen Sie das Problem**
Der Transformationsstatus zählt von Zeilen zu Spalten.
**Schritt 2: Identifizieren Sie den Ansatz**
Verwenden Sie die bedingte Aggregation (`CASE`innerhalb von`SUM`).
**Schritt 3: Implementieren**```sql
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

**Schritt 4: Erweitern**
Fügen Sie Prozentspalten und laufende Summen hinzu.
---

## Zusammenfassung
SQL ist eine 50 Jahre alte Sprache, die nach wie vor unverzichtbar ist. Jeder Entwickler, Datenwissenschaftler und Analyst muss es wissen. Die Kernsprache ist standardisiert und portierbar; Die Dialektunterschiede sind überschaubar. Modernes SQL (mit Fensterfunktionen, CTEs und JSON-Unterstützung) ist für die meisten Datenaufgaben ausdrucksstark genug. Die Schlüsselkompetenzen sind: effiziente Abfragen schreiben, Indizes verstehen, Abfragepläne lesen und gute Schemata entwerfen. Wenn Sie überhaupt mit Daten arbeiten, ist SQL nicht verhandelbar.