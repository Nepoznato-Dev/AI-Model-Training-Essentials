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
SQL (Structured Query Language) é uma linguagem específica de domínio projetada para gerenciar e consultar dados em bancos de dados relacionais. Desenvolvido pela primeira vez na IBM na década de 1970 e padronizado em 1987, o SQL continua sendo a principal interface entre aplicativos e seus dados. Todos os principais sistemas de gerenciamento de banco de dados relacional (RDBMS) – PostgreSQL, MySQL, SQL Server, Oracle, SQLite – usam SQL como linguagem de consulta.
SQL não é uma linguagem de programação de uso geral. Você não escreveria uma aplicação web em SQL. Mas se seu aplicativo armazena dados — e quase todos os aplicativos o fazem — então SQL é a linguagem que você usa para recuperar, transformar e gerenciar esses dados. É sem dúvida a habilidade técnica mais universalmente útil depois da programação geral.
---

## Por que o SQL é importante
- **Universal**: Todo banco de dados relacional fala SQL. Aprenda uma vez, use em qualquer lugar.
- **Declarativo**: você descreve *quais* dados deseja, não *como* obtê-los. O mecanismo de banco de dados otimiza a execução.
- **Essencial para qualquer desenvolvedor**: back-end, ciência de dados, DevOps, análise — todos exigem SQL.
- **Poderoso**: funções de janela, CTEs, subconsultas e agregações permitem expressar lógica complexa em poucas linhas.
- **Desempenho**: uma consulta SQL bem escrita em um banco de dados indexado corretamente pode processar milhões de linhas em milissegundos.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Não é uma linguagem de uso geral** | Não é possível construir aplicativos, APIs ou algoritmos em SQL | Combine com Python, Java, JavaScript, etc. |
| **Diferenças de dialeto** | Cada RDBMS possui seu próprio tipo de SQL com extensões incompatíveis | Atenha-se ao ANSI SQL sempre que possível; diferenças de dialeto abstrato em sua aplicação |
| **Rigidez do esquema** | Alterar estruturas de tabelas em tabelas grandes pode ser lento e perturbador | Utilize ferramentas de migração; projetar esquemas com cuidado antecipadamente |
| **Problema de consulta N+1** | Consultas geradas por ORM podem ser extremamente ineficientes | Escreva SQL personalizado para consultas complexas; perfil com EXPLAIN ANALYZE |
| **Complexidade de escalonamento** | Os bancos de dados SQL são mais difíceis de escalar horizontalmente do que o NoSQL | Use réplicas de leitura, fragmentação ou considere NoSQL para casos de uso específicos |
---

## Conceitos Básicos
### O modelo relacional
Os dados são armazenados em **tabelas** (relações), que consistem em **linhas** (registros/tuplas) e **colunas** (atributos/campos). As tabelas podem ser relacionadas entre si por meio de **chaves**.
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

## Fundamentos de sintaxe
### Recuperando Dados (SELECT)
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

### Agregação
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

### Unindo Tabelas
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

### Modificando dados
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

## Sintaxe e padrões avançados
### Funções da janela — Aprofundamento
As funções de janela executam cálculos em um conjunto de linhas relacionadas à linha atual — sem recolhê-las em uma única linha de saída, como faz GROUP BY.
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

### Expressões de Tabela Comuns (CTEs) — Uso Avançado
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

### Operações JSON
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

### Procedimentos armazenados e gatilhos
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

## Aprofunde-se nos principais recursos
### Otimização de consulta
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

**Lista de verificação de otimização:**
| Edição | Sintoma | Correção |
|-------|---------|-----|
| Varredura sequencial em mesa grande | `Seq Scan`em EXPLICAR | Adicione o índice apropriado |
| Índice ausente na coluna WHERE | Verificação completa da tabela | Crie índice em colunas filtradas |
| SELECIONE *resíduos | Buscando colunas desnecessárias | Selecione apenas as colunas necessárias |
| Conversão de tipo implícita | Índice não utilizado | Tipos de correspondência em comparações |
| Funções em colunas indexadas | Índice inutilizável (não sargável) | Reescrever:`WHERE date >= '2024-01-01'`e não`WHERE YEAR(date) = 2024`|
### Estratégias de Indexação
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

### Níveis de isolamento de transação
| Nível de isolamento | Leitura Suja | Leitura não repetível | Leitura Fantasma |
|-----------------|:----------:|:-------------------:|:------------:|
| LEIA NÃO COMPROMETIDO | Sim | Sim | Sim |
| LEIA COMPROMETIDO | Não | Sim | Sim |
| LEITURA REPETÍVEL | Não | Não | Sim* |
| SERIALIZÁVEL | Não | Não | Não |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Normalização
| Forma normal | Regra | Exemplo de violação |
|------------|------|-------------------|
| **1NF** | Valores atômicos, sem grupos repetidos | Armazenando vários telefones em uma coluna como "123.456" |
| **2NF** | 1NF + sem dependências parciais | Os detalhes do pedido dependem de order_id, mas não de product_id |
| **3NF** | 2NF + sem dependências transitivas | O nome do departamento do funcionário depende de dept_id, não de funcionário |
---

## Definindo a estrutura do banco de dados
### Criando Tabelas
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

### Alterando Tabelas
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## Configuração do projeto e sistema de construção
### Ferramentas de migração
| Ferramenta | Idioma/Pilha | Abordagem |
|------|---------------|----------|
| **Via aérea** | Java/geral | Migrações baseadas em SQL, convenção de nomenclatura simples |
| **Liquibase** | Java/geral | Registros de alterações XML, YAML, JSON ou SQL |
| **Alambique** | Python (SQLAlchemy) | Gera migrações automaticamente a partir de alterações de modelo |
| **Migração Prisma** | Node.js/TypeScript | Esquema primeiro, gera SQL automaticamente |
| **golang-migrar** | Vá | Baseado em SQL, suporta migrações up/down |
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

## Teste
### Geração de dados de teste
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

| Estrutura | Banco de dados | Descrição |
|-----------|----------|------------|
| **pgTAP** | PostgreSQL | Estrutura de testes unitários |
| **tSQLt** | Servidor SQL | Teste de unidade para SQL Server |
| **outPLSQL** | Oráculo | Estrutura de teste para Oracle PL/SQL |
---

## Interoperabilidade
### Ligações de linguagem
| Interface | Idioma | Descrição |
|-----------|----------|------------|
| **JDBC** | Java | API de banco de dados padrão |
| **ODBC** | Múltiplo | API de banco de dados universal |
| **psicopg2/3** | Pitão | Adaptador PostgreSQL |
| **banco de dados/sql** | Vá | Biblioteca padrão com interface de driver |
| **sqlite3** | Pitão | Suporte SQLite integrado |
| **pág.** | Node.js | Cliente PostgreSQL |
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

## Padrões de Projeto
### Padrão 1: Tabela Dinâmica / Tabela Cruzada
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### Padrão 2: N principais por grupo
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### Padrão 3: Lacunas e Ilhas
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

### Padrão 4: Dimensões de mudança lenta (SCD tipo 2)
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

## Desempenho: índices e planejamento de consultas
### Como funcionam os índices
Um índice é uma estrutura de dados (geralmente uma árvore B) que permite ao banco de dados encontrar linhas sem verificar a tabela inteira.
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| Tipo de índice | Melhor para | Exemplo |
|----------|----------|--------|
| **Árvore B** (padrão) | Consultas de igualdade e intervalo | `WHERE age > 25 AND age < 35`|
| **Hash** | Apenas igualdade exata | `WHERE email = 'x@y.com'`|
| **GIN** | Pesquisa de texto completo, matrizes, JSON | `WHERE description @@ 'search term'`|
| **GiST** | Dados geométricos/espaciais | `WHERE location <-> point(x,y) < 1000`|
### Lendo planos de consulta
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

## Dialetos SQL
| Recurso | PostgreSQL | MySQL | Servidor SQL | SQLite |
|---------|-----------|-------|------------|--------|
| Incremento automático | `BIGSERIAL`/`GENERATED ALWAYS`| `AUTO_INCREMENT`| `IDENTITY`| `INTEGER PRIMARY KEY AUTOINCREMENT`|
| String concat | `\|\|`| `CONCAT()`| `+`ou`CONCAT()`| `\|\|`|
| Funções de data | `NOW()`,`AGE()`| `NOW()`,`DATEDIFF()`| `GETDATE()`,`DATEDIFF()`| `DATE('now')`|
| Suporte JSON | Excelente (`jsonb`) | Bom (`JSON`) | Bom (`JSON`) | Básico (`JSON1`) |
| Pesquisa de texto completo | Integrado (`tsvector`) | Integrado | Integrado | Limitado |
| Funções de janela | Sim | Sim (8,0+) | Sim | Sim |
---

## Implantação
### Estratégias de implantação de banco de dados
| Estratégia | Descrição | Nível de risco |
|----------|------------|-----------|
| **Arquivos de migração** | Scripts SQL versionados aplicados em ordem | Baixo |
| **Implantação azul esverdeado** | Dois bancos de dados idênticos; mudar o tráfego | Baixo |
| **Expandir contrato** | Adicionar nova coluna, gravação dupla, migrar, descartar a antiga | Baixo |
| **DDL direto** | Executando ALTER TABLE diretamente na produção | Alto |
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

## Quando usar SQL
| Cenário | Por que SQL | Alternativa |
|----------|------------|-------------|
| Dados relacionais com consultas complexas | É para isso que o SQL foi projetado | --- |
| Integridade transacional (ACID) | Bancos de dados SQL garantem consistência | --- |
| Relatórios e análises | Agregações, funções de janela, CTEs | Python (Pandas) para análises muito complexas |
| Restrições de integridade de dados | Chaves estrangeiras, CHECK, UNIQUE, NOT NULL | Validação em nível de aplicativo (mais fraca) |
| Armazenamento simples de valores-chave | Exagero para este caso de uso | Redis, DynamoDB |
| Dados altamente não estruturados | A rigidez do esquema é um problema | MongoDB, bancos de dados de documentos |
| Escala horizontal massiva | Bancos de dados SQL difíceis de fragmentar | Cassandra, DynamoDB, BarataDB |
---

## Resumo
SQL é uma linguagem de 50 anos que continua essencial. Todo desenvolvedor, cientista de dados e analista precisa saber disso. A linguagem principal é padronizada e portátil; as diferenças de dialeto são administráveis. O SQL moderno (com funções de janela, CTEs e suporte a JSON) é expressivo o suficiente para a maioria das tarefas de dados. As principais habilidades são: escrever consultas eficientes, compreender índices, ler planos de consulta e projetar bons esquemas. Se você trabalha com dados, o SQL não é negociável.