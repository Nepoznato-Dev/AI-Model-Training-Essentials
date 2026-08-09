---
# मेटाडेटा
शीर्षक: "एसक्यूएल त्वरित संदर्भ गाइड"
विवरण: "एसक्यूएल क्वेरी संदर्भ"
श्रेणी: "त्वरित संदर्भ"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
review_by: "त्वरित संदर्भ नॉलेज बेस टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [एसक्यूएल, त्वरित-संदर्भ]
कठिनाई_स्तर: "शुरुआती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "24 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# SQL त्वरित संदर्भ मार्गदर्शिका
डेटाबेस संचालन के लिए आवश्यक SQL कमांड।
---

## बुनियादी क्वेरी संरचना
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

## डेटा पुनर्प्राप्ति (चयन करें)
### मूल चयन```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, name, email FROM users;

-- Select with alias
SELECT name AS user_name, email AS contact FROM users;

-- Select distinct values
SELECT DISTINCT country FROM users;
```

### फ़िल्टरिंग (कहां)```sql
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

### छंटाई और सीमित करना```sql
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

## एकत्रीकरण कार्य
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

## जुड़ता है
### आंतरिक रूप से जुड़ा```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### बाएँ/दाएँ जुड़ें```sql
-- All users, even those without orders
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- All orders, even those without users (rare)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### पूर्ण बाहरी जुड़ाव```sql
-- All users and all orders (MySQL doesn't support FULL OUTER)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### क्रॉस जॉइन```sql
-- Cartesian product (all combinations)
SELECT * FROM colors CROSS JOIN sizes;
```

### स्वयं जुड़ें```sql
-- Find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## उपश्रेणियाँ
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

## सेट ऑपरेशन
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
SELECT product_id FROM orders_2026;

-- EXCEPT/MINUS (rows in first but not second)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## डेटा संशोधन
### डालना```sql
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

### अद्यतन```sql
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

### मिटाना```sql
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

## टेबल संचालन
### तालिका बनाएं```sql
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

### तालिका बदलें```sql
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

### ड्रॉप तालिका```sql
DROP TABLE IF EXISTS temp_table;
```

---

## प्रतिबंध
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

## अनुक्रमणिका
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

## दृश्य
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

## सामान्य तालिका अभिव्यक्तियाँ (सीटीई)
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

## विंडो फ़ंक्शंस
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

## डेटा के प्रकार
### संख्यात्मक
-`INT`- पूर्णांक
- __संरक्षित_1__ - बड़ा पूर्णांक
- __संरक्षित_2__ - सटीक दशमलव (सटीकता, पैमाना)
-`FLOAT`- अनुमानित फ़्लोटिंग पॉइंट
-`DOUBLE`- डबल प्रिसिजन फ्लोट
### स्ट्रिंग
-`CHAR(n)`- निश्चित लंबाई वाली स्ट्रिंग
-`VARCHAR(n)`- परिवर्तनीय लंबाई वाली स्ट्रिंग
- __संरक्षित_2__ - बड़ा पाठ
- __संरक्षित_3__ - प्रगणित मान
### दिनांक/समय
- __संरक्षित_0__ - दिनांक (YYYY-MM-DD)
- __संरक्षित_1__ - समय (एचएच:एमएम:एसएस)
- __संरक्षित_2__ - दिनांक और समय
-`TIMESTAMP`- यूनिक्स टाइमस्टैम्प
- __संरक्षित_4__ - वर्ष मान
### बूलियन
-`BOOLEAN`या`BOOL`- सही/गलत
### बाइनरी
-`BLOB`- बाइनरी बड़ी वस्तु
- __संरक्षित_1__ - निश्चित बाइनरी
- __संरक्षित_2__ - परिवर्तनीय बाइनरी
---

## उपयोगी कार्य
### स्ट्रिंग फ़ंक्शंस```sql
CONCAT(first_name, ' ', last_name)  -- Concatenate strings
UPPER(name)                          -- Convert to uppercase
LOWER(name)                          -- Convert to lowercase
SUBSTRING(name, 1, 3)                -- Extract substring
LENGTH(name)                         -- String length
TRIM(name)                           -- Remove whitespace
REPLACE(text, 'old', 'new')          -- Replace substring
```

### दिनांक फ़ंक्शन```sql
NOW()                                -- Current date/time
CURDATE()                            -- Current date
CURTIME()                            -- Current time
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- Add interval
DATEDIFF(end_date, start_date)       -- Difference in days
YEAR(date_column)                    -- Extract year
MONTH(date_column)                   -- Extract month
DAY(date_column)                     -- Extract day
```

### संख्यात्मक कार्य```sql
ROUND(value, 2)                      -- Round to decimals
CEIL(value)                          -- Round up
FLOOR(value)                         -- Round down
ABS(value)                           -- Absolute value
POWER(base, exp)                     -- Exponentiation
SQRT(value)                          -- Square root
RAND()                               -- Random number
```

### सशर्त कार्य```sql
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

## प्रदर्शन युक्तियाँ
✅ **करें:**
- अक्सर पूछे जाने वाले कॉलम पर इंडेक्स का उपयोग करें
- केवल आवश्यक कॉलम चुनें (`SELECT *` से बचें)
- क्वेरी प्रदर्शन का विश्लेषण करने के लिए`EXPLAIN`का उपयोग करें
- डेटा को उचित रूप से सामान्यीकृत करें
- SQL इंजेक्शन को रोकने के लिए तैयार कथनों का उपयोग करें
❌ **नहीं करें:**
- WHERE क्लॉज में अनुक्रमित कॉलम पर फ़ंक्शन का उपयोग करें
- बहुत सारे इंडेक्स बनाएं (धीमे गति से लिखें)
- अनावश्यक रूप से`SELECT DISTINCT`का प्रयोग करें
- क्वेरी निष्पादन योजनाओं पर ध्यान न दें
- गणना किए गए मानों को तब संग्रहीत करें जब उनकी गणना की जा सके
---

## सुरक्षा सर्वोत्तम प्रथाएँ
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

*अंतिम अद्यतन: जुलाई 2026 | SQL मानक (MySQL/PostgreSQL संगत)*