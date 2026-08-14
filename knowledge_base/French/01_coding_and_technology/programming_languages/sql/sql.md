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
SQL (Structured Query Language) est un langage spécifique à un domaine conçu pour gérer et interroger des données dans des bases de données relationnelles. Développé pour la première fois chez IBM dans les années 1970 et standardisé en 1987, SQL reste la principale interface entre les applications et leurs données. Tous les principaux systèmes de gestion de bases de données relationnelles (SGBDR) — PostgreSQL, MySQL, SQL Server, Oracle, SQLite — utilisent SQL comme langage de requête.
SQL n'est pas un langage de programmation à usage général. Vous n’écririez pas une application Web en SQL. Mais si votre application stocke des données (et presque toutes les applications le font), alors SQL est le langage que vous utilisez pour récupérer, transformer et gérer ces données. Il s’agit sans doute de la compétence technique la plus universellement utile après la programmation générale.
---

## Pourquoi SQL est important
- **Universel** : chaque base de données relationnelle parle SQL. Apprenez-le une fois, utilisez-le partout.
- **Déclaratif** : vous décrivez *quelles* données vous souhaitez, et non *comment* les obtenir. Le moteur de base de données optimise l'exécution.
- **Indispensable pour tout développeur** : backend, science des données, DevOps, analytique : tous nécessitent SQL.
- **Puissant** : les fonctions de fenêtre, les CTE, les sous-requêtes et les agrégations vous permettent d'exprimer une logique complexe en quelques lignes.
- **Performances** : une requête SQL bien écrite sur une base de données correctement indexée peut traiter des millions de lignes en millisecondes.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Pas un langage à usage général** | Impossible de créer des applications, des API ou des algorithmes dans SQL | Combinez avec Python, Java, JavaScript, etc. |
| **Différences dialectales** | Chaque SGBDR a sa propre version SQL avec des extensions incompatibles | Tenez-vous-en à ANSI SQL lorsque cela est possible ; différences dialectales abstraites dans votre application |
| **Ridicité du schéma** | Changer la structure des tables sur de grandes tables peut être lent et perturbateur | Utiliser des outils de migration ; concevoir des schémas avec soin dès le départ |
| **Problème de requête N+1** | Les requêtes générées par ORM peuvent être extrêmement inefficaces | Écrivez du SQL personnalisé pour les requêtes complexes ; profil avec EXPLIQUER ANALYSER |
| **Mise à l'échelle de la complexité** | Les bases de données SQL sont plus difficiles à mettre à l'échelle horizontalement que NoSQL | Utilisez des réplicas en lecture, le partitionnement ou envisagez NoSQL pour des cas d'utilisation spécifiques |
---

## Concepts de base
### Le modèle relationnel
Les données sont stockées dans des **tables** (relations), qui se composent de **lignes** (enregistrements/tuples) et de **colonnes** (attributs/champs). Les tables peuvent être liées les unes aux autres via des **clés**.
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

## Fondamentaux de la syntaxe
### Récupération de données (SELECT)
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

### Agrégation
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

### Joindre des tables
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

### Modification des données
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

## Syntaxe et modèles avancés
### Fonctions de la fenêtre – Analyse approfondie
Les fonctions de fenêtre effectuent des calculs sur un ensemble de lignes liées à la ligne actuelle, sans les regrouper en une seule ligne de sortie comme le fait GROUP BY.
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

### Expressions de table communes (CTE) — Utilisation avancée
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

### Opérations JSON
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

### Procédures stockées et déclencheurs
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

## Plongée en profondeur dans les fonctionnalités de base
### Optimisation des requêtes
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

**Liste de contrôle d'optimisation :**
| Problème | Symptôme | Corriger |
|-------|---------|-----|
| Balayage séquentiel sur grande table | `Seq Scan`dans EXPLIQUER | Ajouter un index approprié |
| Index manquant sur la colonne WHERE | Analyse complète du tableau | Créer un index sur les colonnes filtrées |
| SELECT * déchets | Récupérer les colonnes inutiles | Sélectionnez uniquement les colonnes nécessaires |
| Conversion de type implicite | Index non utilisé | Types de correspondance dans les comparaisons |
| Fonctions sur les colonnes indexées | Index inutilisable (non sargable) | Réécriture :`WHERE date >= '2024-01-01'`et non`WHERE YEAR(date) = 2024`|
### Stratégies d'indexation
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

### Niveaux d'isolement des transactions
| Niveau d'isolement | Lecture sale | Lecture non répétable | Lecture fantôme |
|-----------------|:--------------:|:-------------------:|:------------:|
| LIRE NON ENGAGÉ | Oui | Oui | Oui |
| LIRE ENGAGÉ | Non | Oui | Oui |
| LECTURE RÉPÉTABLE | Non | Non | Oui* |
| SÉRIALISABLE | Non | Non | Non |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalisation
| Forme normale | Règle | Exemple de violation |
|-------------|------|---------|
| **1NF** | Valeurs atomiques, pas de groupes répétitifs | Stockage de plusieurs téléphones dans une colonne sous « 123 456 » |
| **2NF** | 1NF + pas de dépendances partielles | Les détails de la commande dépendent de order_id mais pas de product_id |
| **3NF** | 2NF + pas de dépendances transitives | Le nom du service de l'employé dépend de dept_id et non de l'employé |
---

## Définition de la structure de la base de données
### Création de tableaux
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

### Modification des tableaux
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Configuration du projet et système de construction
### Outils de migration
| Outil | Langue/Pile | Approche |
|------|---------------|--------------|
| **Voie de migration** | Java / général | Migrations basées sur SQL, convention de dénomination simple |
| **Liquibase** | Java / général | Journaux des modifications XML, YAML, JSON ou SQL |
| **Alambic** | Python (SQLAlchimie) | Génère automatiquement des migrations à partir des modifications du modèle |
| **Prisma Migrer** | Node.js/TypeScript | Le schéma d'abord, génère automatiquement du SQL |
| **golang-migrate** | Aller | Basé sur SQL, prend en charge les migrations ascendantes/descendantes |
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

## Tests
### Génération de données de test
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

| Cadre | Base de données | Descriptif |
|-----------|----------|-------------|
| **pgTAP** | PostgreSQL | Cadre de tests unitaires |
| **tSQLt** | Serveur SQL | Tests unitaires pour SQL Server |
| **utPLSQL** | Oracle | Cadre de test pour Oracle PL/SQL |
---

## Interopérabilité
### Liaisons linguistiques
| Interfaces | Langue | Descriptif |
|-----------|----------|-------------|
| **JDBC** | Java | API de base de données standard |
| **ODBC** | Plusieurs | API de base de données universelle |
| **psycopg2/3** | Python | Adaptateur PostgreSQL |
| **base de données/sql** | Aller | Bibliothèque standard avec interface pilote |
| **sqlite3** | Python | Prise en charge SQLite intégrée |
| **page** | Noeud.js | Client PostgreSQL |
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

## Modèles de conception
### Modèle 1 : Pivot / Tableau croisé
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Modèle 2 : Top-N par groupe
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Modèle 3 : Lacunes et îles
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

### Modèle 4 : Dimensions qui changent lentement (SCD Type 2)
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

## Performance : index et planification des requêtes
### Comment fonctionnent les index
Un index est une structure de données (généralement un arbre B) qui permet à la base de données de trouver des lignes sans analyser la table entière.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Type d'index | Idéal pour | Exemple |
|-----------|----------|---------|
| **B-tree** (par défaut) | Requêtes d'égalité et de plage | `WHERE age > 25 AND age < 35`|
| **Hachage** | Égalité exacte uniquement | `WHERE email = 'x@y.com'`|
| **GIN** | Recherche en texte intégral, tableaux, JSON | `WHERE description @@ 'search term'`|
| **Gist** | Données géométriques/spatiales | `WHERE location <-> point(x,y) < 1000`|
### Lecture des plans de requête
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

## Dialectes SQL
| Fonctionnalité | PostgreSQL | MySQL | Serveur SQL | SQLite |
|--------|-----------|-------|------------|--------|
| Incrémentation automatique | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Concatération de chaînes | `\|\|`| `CONCAT()`| `+`ou`CONCAT()`| `\|\|`|
| Fonctions de dates | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Prise en charge JSON | Excellent (`jsonb`) | Bon (`JSON`) | Bon (`JSON`) | De base (`JSON1`) |
| Recherche en texte intégral | Intégré (`tsvector`) | Intégré | Intégré | Limité |
| Fonctions de fenêtre | Oui | Oui (8,0+) | Oui | Oui |
---

## Déploiement
### Stratégies de déploiement de bases de données
| Stratégie | Descriptif | Niveau de risque |
|--------------|-------------|------------|
| **Fichiers de migration** | Scripts SQL versionnés appliqués dans l'ordre | Faible |
| **Déploiement bleu-vert** | Deux bases de données identiques ; changer de trafic | Faible |
| **Contrat élargi** | Ajouter une nouvelle colonne, double écriture, migrer, supprimer l'ancienne | Faible |
| **DDL direct** | Exécuter ALTER TABLE directement en production | Élevé |
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

## Quand utiliser SQL
| Scénario | Pourquoi SQL | Alternatives |
|--------------|---------|-------------|
| Données relationnelles avec requêtes complexes | C'est pour cela que SQL est conçu | --- |
| Intégrité transactionnelle (ACID) | Les bases de données SQL garantissent la cohérence | --- |
| Rapports et analyses | Agrégations, fonctions de fenêtre, CTE | Python (Pandas) pour des analyses très complexes |
| Contraintes d'intégrité des données | Clés étrangères, CHECK, UNIQUE, NOT NULL | Validation au niveau de l'application (plus faible) |
| Stockage clé-valeur simple | Exagération pour ce cas d'utilisation | Redis, DynamoDB |
| Données hautement non structurées | La rigidité des schémas est un problème | MongoDB, bases de données documentaires |
| Mise à l'échelle horizontale massive | Bases de données SQL difficiles à partitionner | Cassandra, DynamoDB, CockroachDB |
---

## Questions et réponses synthétiques
### Q1 : Quelle est la différence entre`WHERE`et `HAVING` ?
**A :**`WHERE`filtre les lignes avant le regroupement ; `HAVING`filtre les groupes après agrégation :
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### Q2 : En quoi les fonctions de fenêtre diffèrent-elles de GROUP BY ?
**R :** Les fonctions de fenêtre calculent sur plusieurs lignes sans les réduire :
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Q3 : Comment optimiser les requêtes lentes ?
**A :** Stratégies clés :
- Ajouter des index sur les colonnes utilisées dans`WHERE`,`JOIN`et`ORDER BY`
- Évitez`SELECT *`- sélectionnez uniquement les colonnes nécessaires
- Utilisez`EXPLAIN`/`EXPLAIN ANALYZE`pour lire les plans de requête
- Remplacez les sous-requêtes par des JOIN lorsque cela est possible
- Utilisez les CTE pour plus de lisibilité (généralement aucune pénalité de performances)
- Évitez les fonctions sur les colonnes indexées dans WHERE : utilisez`WHERE date >= '2024-01-01'`et non `WHERE YEAR(date) = 2024`
### Q4 : Que sont les CTE et quand dois-je les utiliser ?
**A :** Les expressions de table communes créent des ensembles de résultats temporaires nommés :
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

### Q5 : Comment gérer correctement les valeurs NULL ?
**A :** NULL représente un inconnu — il n'est égal à rien, y compris lui-même :
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : Trouver les N premiers par groupe
**Étape 1 : Comprendre le problème**
Trouvez les 3 employés les mieux payés de chaque département.
**Étape 2 : Identifiez l'approche**
Utilisez une fonction de fenêtre avec`ROW_NUMBER()`partitionné par département.
**Étape 3 : Mettre en œuvre**```sql
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

**Étape 4 : Vérifier**
Vérifiez que chaque département comporte au maximum 3 lignes. Manipulez les attaches avec`DENSE_RANK()`si nécessaire.
### Problème 2 : Créer un rapport de croissance d'une année sur l'autre
**Étape 1 : Comprendre le problème**
Calculez les revenus mensuels et le pourcentage de croissance d’une année sur l’autre.
**Étape 2 : Identifiez l'approche**
Utilisez`DATE_TRUNC`pour le regroupement et la fonction de fenêtre`LAG()`pour la comparaison de l'année précédente.
**Étape 3 : Mettre en œuvre**```sql
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

**Étape 4 : Vérifier**
Vérifiez que les 12 premiers mois ont NULL pour l’année précédente. Validez les pourcentages de croissance par rapport aux chiffres connus.
### Problème 3 : Pivotement des lignes vers les colonnes
**Étape 1 : Comprendre le problème**
Transformez le nombre d'états des lignes en colonnes.
**Étape 2 : Identifiez l'approche**
Utilisez l'agrégation conditionnelle (`CASE`dans`SUM`).
**Étape 3 : Mettre en œuvre**```sql
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

**Étape 4 : Prolonger**
Ajoutez des colonnes de pourcentage et des totaux cumulés.
---

## Résumé
SQL est un langage vieux de 50 ans qui reste incontournable. Chaque développeur, data scientist et analyste doit le savoir. Le langage de base est standardisé et portable ; les différences dialectales sont gérables. Le SQL moderne (avec fonctions de fenêtre, CTE et prise en charge JSON) est suffisamment expressif pour la plupart des tâches de données. Les compétences clés sont : rédiger des requêtes efficaces, comprendre les index, lire des plans de requête et concevoir de bons schémas. Si vous travaillez avec des données, SQL n'est pas négociable.