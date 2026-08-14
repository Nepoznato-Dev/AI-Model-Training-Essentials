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
SQL (lenguaje de consulta estructurado) es un lenguaje de dominio específico diseñado para administrar y consultar datos en bases de datos relacionales. Desarrollado por primera vez en IBM en la década de 1970 y estandarizado en 1987, SQL sigue siendo la interfaz principal entre las aplicaciones y sus datos. Todos los principales sistemas de gestión de bases de datos relacionales (RDBMS) (PostgreSQL, MySQL, SQL Server, Oracle, SQLite) utilizan SQL como lenguaje de consulta.
SQL no es un lenguaje de programación de propósito general. No escribirías una aplicación web en SQL. Pero si su aplicación almacena datos (y casi todas las aplicaciones lo hacen), entonces SQL es el lenguaje que utiliza para recuperar, transformar y administrar esos datos. Podría decirse que es la habilidad técnica más útil universalmente después de la programación general.
---

## Por qué es importante SQL
- **Universal**: Cada base de datos relacional habla SQL. Aprendalo una vez, utilícelo en todas partes.
- **Declarativo**: usted describe *qué* datos desea, no *cómo* obtenerlos. El motor de base de datos optimiza la ejecución.
- **Esencial para cualquier desarrollador**: backend, ciencia de datos, DevOps, análisis: todos requieren SQL.
- **Potente**: las funciones de ventana, CTE, subconsultas y agregaciones le permiten expresar una lógica compleja en unas pocas líneas.
- **Rendimiento**: una consulta SQL bien escrita en una base de datos indexada correctamente puede procesar millones de filas en milisegundos.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **No es un lenguaje de propósito general** | No se pueden crear aplicaciones, API o algoritmos en SQL | Combinar con Python, Java, JavaScript, etc. |
| **Diferencias dialectales** | Cada RDBMS tiene su propio tipo SQL con extensiones incompatibles | Cíñete a ANSI SQL siempre que sea posible; diferencias dialectales abstractas en su aplicación |
| **Rigidez del esquema** | Cambiar las estructuras de las mesas en mesas grandes puede ser lento y perturbador | Utilice herramientas de migración; esquemas de diseño cuidadosamente por adelantado |
| **N+1 problema de consulta** | Las consultas generadas por ORM pueden ser extremadamente ineficientes | Escriba SQL personalizado para consultas complejas; perfil con EXPLICAR ANALIZAR |
| **Complejidad de escala** | Las bases de datos SQL son más difíciles de escalar horizontalmente que NoSQL | Utilice réplicas de lectura, fragmentación o considere NoSQL para casos de uso específicos |
---

## Conceptos básicos
### El modelo relacional
Los datos se almacenan en **tablas** (relaciones), que constan de **filas** (registros/tuplas) y **columnas** (atributos/campos). Las tablas se pueden relacionar entre sí mediante **claves**.
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

## Fundamentos de sintaxis
### Recuperando datos (SELECCIONAR)
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

### Agregación
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

### Unir mesas
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

### Modificación de datos
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

## Sintaxis y patrones avanzados
### Funciones de ventana: análisis profundo
Las funciones de ventana realizan cálculos en un conjunto de filas relacionadas con la fila actual, sin colapsarlas en una sola fila de salida como lo hace GROUP BY.
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

### Expresiones de tabla comunes (CTE): uso avanzado
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

### Operaciones JSON
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

### Procedimientos almacenados y desencadenadores
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

## Profundice en las funciones principales
### Optimización de consultas
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

**Lista de verificación de optimización:**
| Problema | Síntoma | Arreglar |
|-------|---------|-----|
| Escaneo secuencial en mesa grande | `Seq Scan`en EXPLICAR | Agregue el índice apropiado |
| Falta índice en la columna DONDE | Escaneo completo de la tabla | Crear índice en columnas filtradas |
| SELECCIONAR * residuos | Recuperando columnas innecesarias | Seleccione solo las columnas necesarias |
| Conversión de tipo implícita | Índice no utilizado | Tipos de coincidencias en comparaciones |
| Funciones en columnas indexadas | Índice inutilizable (no sargable) | Reescribir:`WHERE date >= '2024-01-01'`no`WHERE YEAR(date) = 2024`|
### Estrategias de indexación
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

### Niveles de aislamiento de transacciones
| Nivel de aislamiento | Lectura sucia | Lectura no repetible | Lectura fantasma |
|-----------------|:----------:|:-------------------:|:------------:|
| LEER SIN COMPROMISO | Sí | Sí | Sí |
| LEER COMPROMETIDO | No | Sí | Sí |
| LECTURA REPETIBLE | No | No | Sí* |
| SERIALIZABLE | No | No | No |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalización
| Forma normal | Regla | Ejemplo de infracción |
|-------------|------|-------------------|
| **1NF** | Valores atómicos, sin grupos repetidos | Almacenamiento de varios teléfonos en una columna como "123,456" |
| **2FN** | 1NF + sin dependencias parciales | Los detalles del pedido dependen de order_id pero no de product_id |
| **3NF** | 2NF + sin dependencias transitivas | El nombre del departamento del empleado depende de dept_id, no del empleado |
---

## Definición de la estructura de la base de datos
### Creando tablas
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

### Modificación de tablas
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Configuración del proyecto y sistema de construcción
### Herramientas de migración
| Herramienta | Idioma/Pila | Enfoque |
|------|---------------|----------|
| **Ruta migratoria** | Java/generales | Migraciones basadas en SQL, convención de nomenclatura sencilla |
| **Liquibase** | Java/generales | Registros de cambios XML, YAML, JSON o SQL |
| **Alambique** | Python (SQLAlchemy) | Genera automáticamente migraciones a partir de cambios de modelo |
| **Prisma Migrar** | Node.js / TypeScript | Primero el esquema, genera automáticamente SQL |
| **golang-migrar** | Ir | Basado en SQL, admite migraciones hacia arriba y hacia abajo |
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

## Pruebas
### Generación de datos de prueba
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

| Marco | Base de datos | Descripción |
|-----------|----------|-------------|
| **páginaTAP** | PostgreSQL | Marco de pruebas unitarias |
| **tSQLt** | Servidor SQL | Pruebas unitarias para SQL Server |
| **utPLSQL** | Oráculo | Marco de pruebas para Oracle PL/SQL |
---

## Interoperabilidad
### Enlaces de idiomas
| Interfaz | Idioma | Descripción |
|-----------|----------|-------------|
| **JDBC** | Java | API de base de datos estándar |
| **ODBC** | Múltiples | API de base de datos universal |
| **psycopg2/3** | Pitón | Adaptador PostgreSQL |
| **base de datos/sql** | Ir | Biblioteca estándar con interfaz de controlador |
| **sqlite3** | Pitón | Soporte SQLite incorporado |
| **página** | Nodo.js | Cliente PostgreSQL |
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

## Patrones de diseño
### Patrón 1: Pivote/Tabla cruzada
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Patrón 2: Top-N por grupo
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Patrón 3: Brechas e islas
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

### Patrón 4: Dimensiones que cambian lentamente (SCD tipo 2)
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

## Rendimiento: índices y planificación de consultas
### Cómo funcionan los índices
Un índice es una estructura de datos (generalmente un árbol B) que permite a la base de datos encontrar filas sin escanear toda la tabla.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Tipo de índice | Mejor para | Ejemplo |
|-----------|----------|---------|
| **árbol B** (predeterminado) | Consultas de igualdad y rango | `WHERE age > 25 AND age < 35`|
| **picadillo** | Sólo igualdad exacta | `WHERE email = 'x@y.com'`|
| **GINEBRA** | Búsqueda de texto completo, matrices, JSON | `WHERE description @@ 'search term'`|
| **GIST** | Datos geométricos/espaciales | `WHERE location <-> point(x,y) < 1000`|
### Lectura de planes de consulta
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

## Dialectos SQL
| Característica | PostgreSQL | MySQL | Servidor SQL | SQLite |
|---------|-----------|-------|------------|--------|
| Incremento automático | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| Concatenación de cadenas | `\|\|`| `CONCAT()`| `+`o`CONCAT()`| `\|\|`|
| Funciones de fecha |  `NOW()`,`AGE()`|  `NOW()`,`DATEDIFF()`|  `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Soporte JSON | Excelente (`jsonb`) | Bueno (`JSON`) | Bueno (`JSON`) | Básico (`JSON1`) |
| Búsqueda de texto completo | Incorporado (`tsvector`) | Incorporado | Incorporado | Limitado |
| Funciones de ventana | Sí | Sí (8.0+) | Sí | Sí |
---

## Implementación
### Estrategias de implementación de bases de datos
| Estrategia | Descripción | Nivel de riesgo |
|----------|-------------|------------|
| **Archivos de migración** | Scripts SQL versionados aplicados en orden | Bajo |
| **Implementación azul-verde** | Dos bases de datos idénticas; cambiar el tráfico | Bajo |
| **Ampliar contrato** | Agregar nueva columna, escritura dual, migrar, eliminar la anterior | Bajo |
| **DDL directo** | Ejecutando ALTER TABLE directamente en producción | Alto |
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

## Cuándo utilizar SQL
| Escenario | ¿Por qué SQL? Alternativa |
|----------|---------|-------------|
| Datos relacionales con consultas complejas | Para eso está diseñado SQL | --- |
| Integridad transaccional (ACID) | Las bases de datos SQL garantizan coherencia | --- |
| Informes y análisis | Agregaciones, funciones de ventana, CTE | Python (Pandas) para análisis muy complejos |
| Restricciones de integridad de datos | Claves externas, CHECK, UNIQUE, NOT NULL | Validación a nivel de aplicación (más débil) |
| Almacenamiento simple de valores clave | Exceso para este caso de uso | Redis, DynamoDB |
| Datos altamente desestructurados | La rigidez del esquema es un problema | MongoDB, bases de datos documentales |
| Escalamiento horizontal masivo | Bases de datos SQL difíciles de fragmentar | Casandra, DynamoDB, CockroachDB |
---

## Preguntas y respuestas sintéticas
### P1: ¿Cuál es la diferencia entre`WHERE`y `HAVING`?
**R:**`WHERE`filtra filas antes de agruparlas; `HAVING`filtra grupos después de la agregación:
```sql
-- WHERE: filter individual rows
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE salary > 50000        -- filters rows first
GROUP BY department
HAVING COUNT(*) > 5;        -- filters groups after
```

### P2: ¿En qué se diferencian las funciones de ventana de GROUP BY?
**R:** Las funciones de ventana se calculan en filas sin contraerlas:
```sql
-- GROUP BY collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Window function preserves all rows
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### P3: ¿Cómo optimizo las consultas lentas?
**R:** Estrategias clave:
- Agregar índices en las columnas utilizadas en `WHERE`,`JOIN`y `ORDER BY`. 
- Evite `SELECT *`: seleccione solo las columnas necesarias
- Utilice`EXPLAIN`/`EXPLAIN ANALYZE`para leer planes de consulta
- Reemplace las subconsultas con JOIN siempre que sea posible
- Utilice CTE para mejorar la legibilidad (normalmente sin penalización de rendimiento)
- Evite funciones en columnas indexadas en DONDE: use `WHERE date >= '2024-01-01'`, no `WHERE YEAR(date) = 2024`
### P4: ¿Qué son los CTE y cuándo debo utilizarlos?
**R:** Las expresiones de tabla comunes crean conjuntos de resultados temporales con nombre:
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

### P5: ¿Cómo manejo los valores NULL correctamente?
**R:** NULL representa desconocido; no es igual a nada, ni siquiera a sí mismo:
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

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: Encontrar los N principales por grupo
**Paso 1: Comprenda el problema**
Encuentre los 3 empleados mejor pagados de cada departamento.
**Paso 2: Identificar el enfoque**
Utilice una función de ventana con`ROW_NUMBER()`particionada por departamento.
**Paso 3: Implementar**```sql
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

**Paso 4: Verificar**
Compruebe que cada departamento tenga como máximo 3 filas. Maneje las ataduras con`DENSE_RANK()`si es necesario.
### Problema 2: Elaboración de un informe de crecimiento año tras año
**Paso 1: Comprenda el problema**
Calcule los ingresos mensuales y el porcentaje de crecimiento año tras año.
**Paso 2: Identificar el enfoque**
Utilice`DATE_TRUNC`para agrupar y la función de ventana`LAG()`para comparar el año anterior.
**Paso 3: Implementar**```sql
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

**Paso 4: Verificar**
Verifique que los primeros 12 meses tengan NULL para el año anterior. Validar porcentajes de crecimiento contra cifras conocidas.
### Problema 3: Pivotar filas a columnas
**Paso 1: Comprenda el problema**
Transforme los recuentos de estado de filas a columnas.
**Paso 2: Identificar el enfoque**
Utilice agregación condicional (`CASE`dentro de`SUM`).
**Paso 3: Implementar**```sql
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

**Paso 4: Extender**
Agregue columnas de porcentajes y totales acumulados.
---

## Resumen
SQL es un lenguaje de 50 años que sigue siendo esencial. Todo desarrollador, científico de datos y analista debe saberlo. El lenguaje central está estandarizado y portátil; las diferencias dialectales son manejables. El SQL moderno (con funciones de ventana, CTE y compatibilidad con JSON) es lo suficientemente expresivo para la mayoría de las tareas de datos. Las habilidades clave son: escribir consultas eficientes, comprender índices, leer planes de consultas y diseñar buenos esquemas. Si trabaja con datos, SQL no es negociable.