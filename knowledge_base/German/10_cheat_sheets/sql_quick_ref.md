# SQL-Kurzübersicht

Wesentliche SQL-Befehle für Datenbankoperationen.

---

## Grundlegende Abfragestruktur

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

## Datenabruf (SELECT)

### Grundauswahl
```sql
-- Alle Spalten auswählen
SELECT * FROM users;

-- Bestimmte Spalten auswählen
SELECT id, name, email FROM users;

-- Auswahl mit Alias
SELECT name AS user_name, email AS contact FROM users;

-- Eindeutige Werte auswählen
SELECT DISTINCT country FROM users;
```

### Filtern (WHERE)
```sql
-- Vergleichsoperatoren
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- Beginnt mit A
SELECT * FROM users WHERE name LIKE '%son';    -- Endet mit son
SELECT * FROM users WHERE name LIKE '%test%';  -- Enthält test
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- Logische Operatoren
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### Sortieren und Begrenzen
```sql
-- Nach einzelner Spalte sortieren
SELECT * FROM products ORDER BY price DESC;

-- Nach mehreren Spalten sortieren
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- Ergebnisse begrenzen
SELECT * FROM users LIMIT 10;

-- Offset (für Paginierung)
SELECT * FROM users LIMIT 10 OFFSET 20;  -- 20 überspringen, 10 nehmen
```

---

## Aggregatfunktionen

```sql
-- Zeilen zählen
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- Summe, Durchschnitt, Minimum, Maximum
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- Gruppieren nach
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having (Gruppen filtern)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## Joins

### Inner Join
```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### Left/Right Join
```sql
-- Alle Nutzer, auch ohne Bestellungen
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Alle Bestellungen, auch ohne Nutzer (selten)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Full Outer Join
```sql
-- Alle Nutzer und alle Bestellungen (MySQL unterstützt FULL OUTER nicht)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Cross Join
```sql
-- Kartesisches Produkt (alle Kombinationen)
SELECT * FROM colors CROSS JOIN sizes;
```

### Self Join
```sql
-- Mitarbeiter und ihre Manager finden
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## Unterabfragen

```sql
-- In der WHERE-Klausel
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- In der SELECT-Klausel
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- In der FROM-Klausel
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- Mit EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## Mengenoperationen

```sql
-- UNION (Duplikate entfernen)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (Duplikate behalten)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT (gemeinsame Zeilen)
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2024;

-- EXCEPT/MINUS (Zeilen in der ersten, aber nicht in der zweiten Menge)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## Datenänderung

### INSERT
```sql
-- Einzelne Zeile einfügen
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- Mehrere Zeilen einfügen
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- Aus SELECT einfügen
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### UPDATE
```sql
-- Einzelne Zeile aktualisieren
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- Mehrere Spalten aktualisieren
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- Mit JOIN aktualisieren
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### DELETE
```sql
-- Bestimmte Zeilen löschen
DELETE FROM users WHERE id = 1;

-- Mit Bedingung löschen
DELETE FROM orders WHERE order_date < '2023-01-01';

-- Mit JOIN löschen
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- Tabelle leeren (schneller, setzt auto-increment zurück)
TRUNCATE TABLE temp_data;
```

---

## Tabellenoperationen

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
-- Spalte hinzufügen
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Spalte ändern
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- Spalte umbenennen
ALTER TABLE users RENAME COLUMN username TO user_name;

-- Spalte löschen
ALTER TABLE users DROP COLUMN phone;

-- Constraint hinzufügen
ALTER TABLE orders ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) REFERENCES users(id);

-- Constraint löschen
ALTER TABLE orders DROP FOREIGN KEY fk_user;

-- Tabelle umbenennen
ALTER TABLE old_name RENAME TO new_name;
```

### DROP Table
```sql
DROP TABLE IF EXISTS temp_table;
```

---

## Constraints

```sql
-- PRIMARY KEY: Eindeutiger Bezeichner
CREATE TABLE users (
    id INT PRIMARY KEY
);

-- FOREIGN KEY: Verweis auf eine andere Tabelle
CREATE TABLE orders (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- UNIQUE: Keine doppelten Werte
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- NOT NULL: Pflichtfeld
CREATE TABLE users (
    name VARCHAR(50) NOT NULL
);

-- CHECK: Werte validieren
CREATE TABLE products (
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0)
);

-- DEFAULT: Standardwert
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Indizes

```sql
-- Index erstellen
CREATE INDEX idx_email ON users(email);

-- Zusammengesetzten Index erstellen
CREATE INDEX idx_name_age ON users(last_name, first_name);

-- Eindeutigen Index erstellen
CREATE UNIQUE INDEX idx_username ON users(username);

-- Index löschen
DROP INDEX idx_email ON users;

-- Indizes anzeigen
SHOW INDEX FROM users;
```

---

## Views

```sql
-- View erstellen
CREATE VIEW active_users AS
SELECT id, name, email, country
FROM users
WHERE status = 'active';

-- View verwenden
SELECT * FROM active_users WHERE country = 'USA';

-- View aktualisieren (falls aktualisierbar)
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, country, created_at
FROM users
WHERE status = 'active';

-- View löschen
DROP VIEW IF EXISTS active_users;
```

---

## Common Table Expressions (CTEs)

```sql
-- Einfache CTE
WITH high_value_users AS (
    SELECT id, name, total_spent
    FROM users
    WHERE total_spent > 1000
)
SELECT * FROM high_value_users ORDER BY total_spent DESC;

-- Rekursive CTE (hierarchische Daten)
WITH RECURSIVE org_chart AS (
    -- Basisfall
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Rekursiver Fall
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## Fensterfunktionen

```sql
-- ROW_NUMBER
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK und DENSE_RANK
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Laufende Summe
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- Partitioniertes Fenster
SELECT department, name, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- LAG und LEAD
SELECT date, sales,
       LAG(sales, 1) OVER (ORDER BY date) AS prev_day_sales,
       LEAD(sales, 1) OVER (ORDER BY date) AS next_day_sales
FROM daily_sales;
```

---

## Datentypen

### Numerisch
- `INT` - Ganzzahl
- `BIGINT` - Große Ganzzahl
- `DECIMAL(p,s)` - Exakte Dezimalzahl (Präzision, Skala)
- `FLOAT` - Ungefähre Gleitkommazahl
- `DOUBLE` - Gleitkommazahl mit doppelter Genauigkeit

### String
- `CHAR(n)` - String mit fester Länge
- `VARCHAR(n)` - String mit variabler Länge
- `TEXT` - Großer Text
- `ENUM` - Aufgezählte Werte

### Datum/Zeit
- `DATE` - Datum (YYYY-MM-DD)
- `TIME` - Uhrzeit (HH:MM:SS)
- `DATETIME` - Datum und Uhrzeit
- `TIMESTAMP` - Unix-Zeitstempel
- `YEAR` - Jahreswert

### Boolean
- `BOOLEAN` oder `BOOL` - True/False

### Binär
- `BLOB` - Großes binäres Objekt
- `BINARY` - Feste Binärdaten
- `VARBINARY` - Variable Binärdaten

---

## Nützliche Funktionen

### String-Funktionen
```sql
CONCAT(first_name, ' ', last_name)  -- Strings verketten
UPPER(name)                          -- In Großbuchstaben umwandeln
LOWER(name)                          -- In Kleinbuchstaben umwandeln
SUBSTRING(name, 1, 3)                -- Teilstring extrahieren
LENGTH(name)                         -- Stringlänge
TRIM(name)                           -- Leerraum entfernen
REPLACE(text, 'old', 'new')          -- Teilstring ersetzen
```

### Datumsfunktionen
```sql
NOW()                                -- Aktuelles Datum/Uhrzeit
CURDATE()                            -- Aktuelles Datum
CURTIME()                            -- Aktuelle Uhrzeit
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- Intervall hinzufügen
DATEDIFF(end_date, start_date)       -- Differenz in Tagen
YEAR(date_column)                    -- Jahr extrahieren
MONTH(date_column)                   -- Monat extrahieren
DAY(date_column)                     -- Tag extrahieren
```

### Numerische Funktionen
```sql
ROUND(value, 2)                      -- Auf Dezimalstellen runden
CEIL(value)                          -- Aufrunden
FLOOR(value)                         -- Abrunden
ABS(value)                           -- Absolutwert
POWER(base, exp)                     -- Potenzierung
SQRT(value)                          -- Quadratwurzel
RAND()                               -- Zufallszahl
```

### Bedingte Funktionen
```sql
-- CASE-Anweisung
SELECT name,
       CASE 
            WHEN age < 18 THEN 'Minor'
            WHEN age < 65 THEN 'Adult'
            ELSE 'Senior'
       END AS age_group
FROM users;

-- IF-Funktion (MySQL)
SELECT IF(age >= 18, 'Adult', 'Minor') AS status FROM users;

-- COALESCE (ersten Nicht-Null-Wert zurückgeben)
SELECT COALESCE(phone, email, 'No contact') AS contact FROM users;

-- NULLIF (NULL zurückgeben, wenn gleich)
SELECT NULLIF(value, 0) AS safe_value FROM data;
```

---

## Performance-Tipps

✅ **Tun:**
- Verwenden Sie Indizes für häufig abgefragte Spalten
- Wählen Sie nur benötigte Spalten aus (vermeiden Sie `SELECT *`)
- Verwenden Sie `EXPLAIN`, um die Abfrageleistung zu analysieren
- Normalisieren Sie Daten angemessen
- Verwenden Sie vorbereitete Anweisungen, um SQL-Injection zu verhindern

❌ **Nicht tun:**
- Funktionen auf indizierten Spalten in WHERE-Klauseln verwenden
- Zu viele Indizes erstellen (verlangsamt Schreibvorgänge)
- `SELECT DISTINCT` unnötig verwenden
- Ausführungspläne von Abfragen ignorieren
- Berechnete Werte speichern, wenn sie berechnet werden können

---

## Sicherheits-Best-Practices

```sql
-- Parametrisierte Abfragen verwenden (im Anwendungscode)
-- Benutzereingaben NIEMALS direkt verketten

-- Minimale Berechtigungen vergeben
GRANT SELECT, INSERT ON database.table TO 'user'@'localhost';
REVOKE DELETE ON database.table FROM 'user'@'localhost';

-- Starke Passwörter verwenden
-- SSL-Verbindungen aktivieren
-- Regelmäßige Sicherheitsaudits
```

---

*Zuletzt aktualisiert: Juni 2025 | SQL Standard (MySQL/PostgreSQL-kompatibel)*
