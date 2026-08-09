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

#SQL
SQL (Structured Query Language) è un linguaggio specifico del dominio progettato per la gestione e l'interrogazione dei dati nei database relazionali. Sviluppato per la prima volta da IBM negli anni '70 e standardizzato nel 1987, SQL rimane l'interfaccia principale tra le applicazioni e i relativi dati. Tutti i principali sistemi di gestione di database relazionali (RDBMS) – PostgreSQL, MySQL, SQL Server, Oracle, SQLite – utilizzano SQL come linguaggio di query.
SQL non è un linguaggio di programmazione generico. Non scriveresti un'applicazione web in SQL. Ma se la tua applicazione archivia dati, e quasi tutte le applicazioni lo fanno, allora SQL è il linguaggio che utilizzi per recuperare, trasformare e gestire tali dati. È probabilmente l'abilità tecnica più universalmente utile dopo la programmazione generale.
---

## Perché SQL è importante
- **Universale**: ogni database relazionale parla SQL. Imparalo una volta, usalo ovunque.
- **Dichiarativo**: descrivi *quali* dati desideri, non *come* ottenerli. Il motore del database ottimizza l'esecuzione.
- **Essenziale per qualsiasi sviluppatore**: backend, data science, DevOps, analisi: tutto richiede SQL.
- **Potente**: funzioni finestra, CTE, sottoquery e aggregazioni ti consentono di esprimere una logica complessa in poche righe.
- **Prestazioni**: una query SQL ben scritta su un database correttamente indicizzato può elaborare milioni di righe in millisecondi.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Non è un linguaggio generico** | Impossibile creare applicazioni, API o algoritmi in SQL | Combinalo con Python, Java, JavaScript, ecc. |
| **Differenze dialettali** | Ogni RDBMS ha il proprio sapore SQL con estensioni incompatibili | Attenersi ad ANSI SQL ove possibile; differenze dialettali astratte nella tua applicazione |
| **Rigidità dello schema** | Cambiare la struttura dei tavoli su tavoli di grandi dimensioni può essere lento e disturbante | Utilizzare strumenti di migrazione; progettare attentamente gli schemi in anticipo |
| **Problema di query N+1** | Le query generate da ORM possono essere estremamente inefficienti | Scrivi SQL personalizzato per query complesse; profilo con SPIEGARE ANALIZZA |
| **Ridimensionamento della complessità** | I database SQL sono più difficili da scalare orizzontalmente rispetto a NoSQL | Utilizza repliche di lettura, partizionamento orizzontale o considera NoSQL per casi d'uso specifici |
---

## Concetti fondamentali
### Il modello relazionale
I dati vengono archiviati in **tabelle** (relazioni), costituite da **righe** (record/tuple) e **colonne** (attributi/campi). Le tabelle possono essere messe in relazione tra loro tramite **chiavi**.
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

## Fondamenti di sintassi
### Recupero dei dati (SELEZIONE)
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

### Aggregazione
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

### Unione di tabelle
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

### Modifica dei dati
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

## Sintassi e modelli avanzati
### Funzioni della finestra: approfondimento
Le funzioni della finestra eseguono calcoli su un insieme di righe correlate alla riga corrente, senza comprimerle in un'unica riga di output come fa GROUP BY.
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

### Espressioni di tabella comuni (CTE): utilizzo avanzato
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

### Operazioni JSON
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

### Procedure memorizzate e trigger
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

## Approfondimento sulle funzionalità principali
### Ottimizzazione delle query
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

**Elenco di controllo per l'ottimizzazione:**
| Problema | Sintomo | Correzione |
|-------|---------|-----|
| Scansione sequenziale su tavolo grande | `Seq Scan`in SPIEGARE | Aggiungi l'indice appropriato |
| Indice mancante nella colonna WHERE | Scansione completa della tabella | Crea indice su colonne filtrate |
| SELEZIONA * rifiuti | Recupero colonne non necessarie | Seleziona solo le colonne necessarie |
| Conversione implicita del tipo | Indice non utilizzato | Tipi di corrispondenza nei confronti |
| Funzioni su colonne indicizzate | Indice inutilizzabile (non sargabile) | Riscrivi:`WHERE date >= '2024-01-01'`non`WHERE YEAR(date) = 2024`|
### Strategie di indicizzazione
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

### Livelli di isolamento delle transazioni
| Livello di isolamento | Lettura sporca | Lettura non ripetibile | Lettura fantasma |
|-----------------|:----------:|:-----:|:------------:|
| LEGGI SENZA IMPEGNO | Sì | Sì | Sì |
| LEGGI IMPEGNO | No | Sì | Sì |
| LEGGERE RIPETIBILE | No | No | Sì* |
| SERIALIZZABILE | No | No | No |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalizzazione
| Forma normale | Regola | Esempio di violazione |
|-------------|------|-------------|
| **1NF** | Valori atomici, nessun gruppo ripetitivo | Memorizzazione di più telefoni in una colonna come "123.456" |
| **2NF** | 1NF + nessuna dipendenza parziale | I dettagli dell'ordine dipendono da order_id ma non da product_id |
| **3NF** | 2NF + nessuna dipendenza transitiva | Il nome del reparto del dipendente dipende da dept_id, non da dipendente |
---

## Definizione della struttura del database
### Creazione di tabelle
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

### Modifica delle tabelle
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Configurazione del progetto e sistema di creazione
### Strumenti di migrazione
| Strumento | Lingua/Stack | Avvicinamento |
|------|---------------|----------|
| **Volo** | Java / generale | Migrazioni basate su SQL, convenzione di denominazione semplice |
| **Liquibase** | Java / generale | Log delle modifiche XML, YAML, JSON o SQL |
| **Alambicco** | Python (SQLAlchemy) | Genera automaticamente le migrazioni dalle modifiche del modello |
| **Prisma Migrare** | Node.js/TypeScript | Prima lo schema, genera automaticamente SQL |
| **golang-migrare** | Vai | Basato su SQL, supporta le migrazioni su/giù |
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

## Test
### Generazione dei dati di prova
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

| Quadro | Banca dati | Descrizione |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Quadro di test unitario |
| **tSQLt** | SQLServer | Test unitari per SQL Server |
| **utPLSQL** | Oracolo | Framework di test per Oracle PL/SQL |
---

## Interoperabilità
### Vincoli linguistici
| Interfaccia | Lingua | Descrizione |
|-----------|----------|-------------|
| **JDBC** | Giava | API del database standard |
| **ODBC** | Molteplici | API del database universale |
| **psicopg2/3** | Pitone | Adattatore PostgreSQL |
| **database/sql** | Vai | Libreria standard con interfaccia driver |
| **sqlite3** | Pitone | Supporto SQLite integrato |
| **pag** | Node.js | Client PostgreSQL |
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

## Modelli di progettazione
### Modello 1: pivot/tabella incrociata
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Modello 2: Primi N per gruppo
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Modello 3: Lacune e isole
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

### Modello 4: Dimensioni a cambiamento lento (SCD tipo 2)
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

## Prestazioni: indici e pianificazione delle query
### Come funzionano gli indici
Un indice è una struttura dati (solitamente un albero B) che consente al database di trovare righe senza scansionare l'intera tabella.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Tipo indice | Ideale per | Esempio |
|-----------|----------|---------|
| **B-albero** (predefinito) | Query di uguaglianza e intervallo | `WHERE age > 25 AND age < 35`|
| **Hash** | Solo uguaglianza esatta | `WHERE email = 'x@y.com'`|
| **GIN** | Ricerca full-text, array, JSON | `WHERE description @@ 'search term'`|
| **GiST** | Dati geometrici/spaziali | `WHERE location <-> point(x,y) < 1000`|
### Lettura dei piani di query
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

## Dialetti SQL
| Caratteristica | PostgreSQL | MySQL | SQLServer | SQLite |
|---------|-----------|-------|------------|--------|
| Incremento automatico | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Stringa concat | `\|\|`| `CONCAT()`| `+`o`CONCAT()`| `\|\|`|
| Funzioni data | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Supporto JSON | Eccellente (`jsonb`) | Buono (`JSON`) | Buono (`JSON`) | Base (`JSON1`) |
| Ricerca nel testo completo | Integrato (`tsvector`) | Integrato | Integrato | Limitato |
| Funzioni della finestra | Sì | Sì (8.0+) | Sì | Sì |
---

## Distribuzione
### Strategie di distribuzione del database
| Strategia | Descrizione | Livello di rischio |
|----------|-------------|------------|
| **File di migrazione** | Script SQL con versione applicati nell'ordine | Basso |
| **Spiegamento blu-verde** | Due database identici; cambiare traffico | Basso |
| **Espandere il contratto** | Aggiungi nuova colonna, doppia scrittura, migrazione, elimina vecchia | Basso |
| **DDL diretto** | Esecuzione di ALTER TABLE direttamente sulla produzione | Alto |
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

## Quando utilizzare SQL
| Scenario | Perché SQL | Alternativa |
|----------|---------|-----|
| Dati relazionali con query complesse | Questo è lo scopo per cui SQL è stato progettato | --- |
| Integrità transazionale (ACID) | I database SQL garantiscono la coerenza | --- |
| Reporting e analisi | Aggregazioni, funzioni finestra, CTE | Python (Panda) per analisi molto complesse |
| Vincoli di integrità dei dati | Chiavi esterne, CHECK, UNIQUE, NOT NULL | Convalida a livello di applicazione (più debole) |
| Memorizzazione semplice di valori-chiave | Eccessivo per questo caso d'uso | Redis, DynamoDB |
| Dati altamente non strutturati | La rigidità dello schema è un problema | MongoDB, banche dati documentali |
| Enorme ridimensionamento orizzontale | Difficile partizionare i database SQL | Cassandra, DynamoDB, CockroachDB |
---

## Riepilogo
SQL è un linguaggio vecchio di 50 anni che rimane essenziale. Ogni sviluppatore, data scientist e analista deve saperlo. Il linguaggio principale è standardizzato e portabile; le differenze dialettali sono gestibili. L'SQL moderno (con funzioni finestra, CTE e supporto JSON) è sufficientemente espressivo per la maggior parte delle attività relative ai dati. Le competenze chiave sono: scrivere query efficienti, comprendere gli indici, leggere i piani di query e progettare buoni schemi. Se lavori con i dati, SQL non è negoziabile.