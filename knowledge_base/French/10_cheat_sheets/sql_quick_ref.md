# Guide de référence rapide SQL

Commandes SQL essentielles pour les opérations sur les bases de données.

---

## Structure de requête de base

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

## Récupération des données (SELECT)

### Sélection de base
```sql
-- Sélectionner toutes les colonnes
SELECT * FROM users;

-- Sélectionner des colonnes spécifiques
SELECT id, name, email FROM users;

-- Sélectionner avec alias
SELECT name AS user_name, email AS contact FROM users;

-- Sélectionner des valeurs distinctes
SELECT DISTINCT country FROM users;
```

### Filtrage (WHERE)
```sql
-- Opérateurs de comparaison
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- Commence par A
SELECT * FROM users WHERE name LIKE '%son';    -- Se termine par son
SELECT * FROM users WHERE name LIKE '%test%';  -- Contient test
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- Opérateurs logiques
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### Tri et limitation
```sql
-- Trier par une seule colonne
SELECT * FROM products ORDER BY price DESC;

-- Trier par plusieurs colonnes
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- Limiter les résultats
SELECT * FROM users LIMIT 10;

-- Offset (pour la pagination)
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Ignorer 20, prendre 10
```

---

## Fonctions d'agrégation

```sql
-- Compter les lignes
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- Somme, moyenne, min, max
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- Grouper par
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having (filtrer les groupes)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## Jointures

### Jointure interne
```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### Jointure gauche/droite
```sql
-- Tous les utilisateurs, même ceux sans commandes
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Toutes les commandes, même celles sans utilisateurs (rare)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Jointure externe complète
```sql
-- Tous les utilisateurs et toutes les commandes (MySQL ne prend pas en charge FULL OUTER)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### Jointure croisée
```sql
-- Produit cartésien (toutes les combinaisons)
SELECT * FROM colors CROSS JOIN sizes;
```

### Auto-jointure
```sql
-- Trouver les employés et leurs responsables
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## Sous-requêtes

```sql
-- Dans la clause WHERE
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- Dans la clause SELECT
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- Dans la clause FROM
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- Avec EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## Opérations ensemblistes

```sql
-- UNION (supprimer les doublons)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (conserver les doublons)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT (lignes communes)
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2024;

-- EXCEPT/MINUS (lignes présentes dans le premier mais pas dans le second)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## Modification des données

### INSERT
```sql
-- Insérer une seule ligne
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- Insérer plusieurs lignes
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- Insérer depuis SELECT
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### UPDATE
```sql
-- Mettre à jour une seule ligne
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- Mettre à jour plusieurs colonnes
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- Mettre à jour avec JOIN
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### DELETE
```sql
-- Supprimer des lignes spécifiques
DELETE FROM users WHERE id = 1;

-- Supprimer avec condition
DELETE FROM orders WHERE order_date < '2023-01-01';

-- Supprimer avec JOIN
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- Tronquer une table (plus rapide, réinitialise l'auto-incrément)
TRUNCATE TABLE temp_data;
```

---

## Opérations sur les tables

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
-- Ajouter une colonne
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Modifier une colonne
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- Renommer une colonne
ALTER TABLE users RENAME COLUMN username TO user_name;

-- Supprimer une colonne
ALTER TABLE users DROP COLUMN phone;

-- Ajouter une contrainte
ALTER TABLE orders ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) REFERENCES users(id);

-- Supprimer une contrainte
ALTER TABLE orders DROP FOREIGN KEY fk_user;

-- Renommer une table
ALTER TABLE old_name RENAME TO new_name;
```

### DROP Table
```sql
DROP TABLE IF EXISTS temp_table;
```

---

## Contraintes

```sql
-- PRIMARY KEY : identifiant unique
CREATE TABLE users (
    id INT PRIMARY KEY
);

-- FOREIGN KEY : référence à une autre table
CREATE TABLE orders (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- UNIQUE : pas de valeurs en double
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- NOT NULL : champ obligatoire
CREATE TABLE users (
    name VARCHAR(50) NOT NULL
);

-- CHECK : valider les valeurs
CREATE TABLE products (
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0)
);

-- DEFAULT : valeur par défaut
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Index

```sql
-- Créer un index
CREATE INDEX idx_email ON users(email);

-- Créer un index composite
CREATE INDEX idx_name_age ON users(last_name, first_name);

-- Créer un index unique
CREATE UNIQUE INDEX idx_username ON users(username);

-- Supprimer un index
DROP INDEX idx_email ON users;

-- Afficher les index
SHOW INDEX FROM users;
```

---

## Vues

```sql
-- Créer une vue
CREATE VIEW active_users AS
SELECT id, name, email, country
FROM users
WHERE status = 'active';

-- Utiliser la vue
SELECT * FROM active_users WHERE country = 'USA';

-- Mettre à jour la vue (si elle est modifiable)
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, country, created_at
FROM users
WHERE status = 'active';

-- Supprimer la vue
DROP VIEW IF EXISTS active_users;
```

---

## Expressions de table communes (CTEs)

```sql
-- CTE simple
WITH high_value_users AS (
    SELECT id, name, total_spent
    FROM users
    WHERE total_spent > 1000
)
SELECT * FROM high_value_users ORDER BY total_spent DESC;

-- CTE récursive (données hiérarchiques)
WITH RECURSIVE org_chart AS (
    -- Cas de base
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Cas récursif
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## Fonctions de fenêtre

```sql
-- ROW_NUMBER
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK et DENSE_RANK
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Total cumulé
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- Fenêtre partitionnée
SELECT department, name, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- LAG et LEAD
SELECT date, sales,
       LAG(sales, 1) OVER (ORDER BY date) AS prev_day_sales,
       LEAD(sales, 1) OVER (ORDER BY date) AS next_day_sales
FROM daily_sales;
```

---

## Types de données

### Numériques
- `INT` - Entier
- `BIGINT` - Entier long
- `DECIMAL(p,s)` - Décimal exact (précision, échelle)
- `FLOAT` - Virgule flottante approximative
- `DOUBLE` - Flottant double précision

### Chaînes
- `CHAR(n)` - Chaîne de longueur fixe
- `VARCHAR(n)` - Chaîne de longueur variable
- `TEXT` - Texte volumineux
- `ENUM` - Valeurs énumérées

### Date/heure
- `DATE` - Date (YYYY-MM-DD)
- `TIME` - Heure (HH:MM:SS)
- `DATETIME` - Date et heure
- `TIMESTAMP` - Horodatage Unix
- `YEAR` - Valeur d'année

### Booléen
- `BOOLEAN` ou `BOOL` - Vrai/Faux

### Binaire
- `BLOB` - Objet binaire volumineux
- `BINARY` - Binaire fixe
- `VARBINARY` - Binaire variable

---

## Fonctions utiles

### Fonctions sur les chaînes
```sql
CONCAT(first_name, ' ', last_name)  -- Concaténer des chaînes
UPPER(name)                          -- Convertir en majuscules
LOWER(name)                          -- Convertir en minuscules
SUBSTRING(name, 1, 3)                -- Extraire une sous-chaîne
LENGTH(name)                         -- Longueur de la chaîne
TRIM(name)                           -- Supprimer les espaces
REPLACE(text, 'old', 'new')          -- Remplacer une sous-chaîne
```

### Fonctions de date
```sql
NOW()                                -- Date/heure actuelle
CURDATE()                            -- Date actuelle
CURTIME()                            -- Heure actuelle
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- Ajouter un intervalle
DATEDIFF(end_date, start_date)       -- Différence en jours
YEAR(date_column)                    -- Extraire l'année
MONTH(date_column)                   -- Extraire le mois
DAY(date_column)                     -- Extraire le jour
```

### Fonctions numériques
```sql
ROUND(value, 2)                      -- Arrondir aux décimales
CEIL(value)                          -- Arrondir au supérieur
FLOOR(value)                         -- Arrondir à l'inférieur
ABS(value)                           -- Valeur absolue
POWER(base, exp)                     -- Exponentiation
SQRT(value)                          -- Racine carrée
RAND()                               -- Nombre aléatoire
```

### Fonctions conditionnelles
```sql
-- Instruction CASE
SELECT name,
       CASE 
            WHEN age < 18 THEN 'Minor'
            WHEN age < 65 THEN 'Adult'
            ELSE 'Senior'
       END AS age_group
FROM users;

-- Fonction IF (MySQL)
SELECT IF(age >= 18, 'Adult', 'Minor') AS status FROM users;

-- COALESCE (renvoie la première valeur non nulle)
SELECT COALESCE(phone, email, 'No contact') AS contact FROM users;

-- NULLIF (renvoie NULL en cas d'égalité)
SELECT NULLIF(value, 0) AS safe_value FROM data;
```

---

## Conseils de performance

✅ **À faire :**
- Utiliser des index sur les colonnes fréquemment interrogées
- Sélectionner uniquement les colonnes nécessaires (éviter `SELECT *`)
- Utiliser `EXPLAIN` pour analyser les performances des requêtes
- Normaliser les données de façon appropriée
- Utiliser des requêtes préparées pour prévenir les injections SQL

❌ **À éviter :**
- Utiliser des fonctions sur des colonnes indexées dans les clauses WHERE
- Créer trop d'index (cela ralentit les écritures)
- Utiliser `SELECT DISTINCT` inutilement
- Ignorer les plans d'exécution des requêtes
- Stocker des valeurs calculées lorsqu'elles peuvent être dérivées

---

## Bonnes pratiques de sécurité

```sql
-- Utiliser des requêtes paramétrées (dans le code applicatif)
-- NE JAMAIS concaténer directement les entrées utilisateur

-- Accorder des privilèges minimaux
GRANT SELECT, INSERT ON database.table TO 'user'@'localhost';
REVOKE DELETE ON database.table FROM 'user'@'localhost';

-- Utiliser des mots de passe robustes
-- Activer les connexions SSL
-- Audits de sécurité réguliers
```

---

*Dernière mise à jour : juin 2025 | SQL Standard (compatible MySQL/PostgreSQL)*
