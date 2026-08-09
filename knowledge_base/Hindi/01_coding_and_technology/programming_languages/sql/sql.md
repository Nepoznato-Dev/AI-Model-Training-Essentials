---
# मेटाडेटा
शीर्षक: "एसक्यूएल"
विवरण: "एसक्यूएल प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
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
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [एसक्यूएल, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "26 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
#एसक्यूएल
SQL (स्ट्रक्चर्ड क्वेरी लैंग्वेज) एक डोमेन-विशिष्ट भाषा है जिसे रिलेशनल डेटाबेस में डेटा को प्रबंधित और क्वेरी करने के लिए डिज़ाइन किया गया है। पहली बार 1970 के दशक में IBM में विकसित किया गया और 1987 में मानकीकृत किया गया, SQL अनुप्रयोगों और उनके डेटा के बीच प्राथमिक इंटरफ़ेस बना हुआ है। प्रत्येक प्रमुख रिलेशनल डेटाबेस मैनेजमेंट सिस्टम (RDBMS) - PostgreSQL, MySQL, SQL सर्वर, Oracle, SQLite - अपनी क्वेरी भाषा के रूप में SQL का उपयोग करता है।
SQL एक सामान्य-उद्देश्य वाली प्रोग्रामिंग भाषा नहीं है। आप SQL में वेब एप्लिकेशन नहीं लिखेंगे. लेकिन यदि आपका एप्लिकेशन डेटा संग्रहीत करता है - और लगभग सभी एप्लिकेशन ऐसा करते हैं - तो SQL वह भाषा है जिसका उपयोग आप उस डेटा को पुनः प्राप्त करने, बदलने और प्रबंधित करने के लिए करते हैं। सामान्य प्रोग्रामिंग के बाद यह यकीनन सबसे सार्वभौमिक रूप से उपयोगी तकनीकी कौशल है।
---

## SQL क्यों मायने रखता है
- **यूनिवर्सल**: प्रत्येक रिलेशनल डेटाबेस SQL ​​बोलता है। इसे एक बार सीखें, हर जगह इसका उपयोग करें।
- **घोषणात्मक**: आप वर्णन करते हैं कि आप *क्या* डेटा चाहते हैं, न कि इसे *कैसे* प्राप्त करें। डेटाबेस इंजन निष्पादन को अनुकूलित करता है।
- **किसी भी डेवलपर के लिए आवश्यक**: बैकएंड, डेटा साइंस, DevOps, एनालिटिक्स - सभी के लिए SQL की आवश्यकता होती है।
- **शक्तिशाली**: विंडो फ़ंक्शंस, सीटीई, सबक्वेरीज़ और एकत्रीकरण आपको जटिल तर्क को कुछ पंक्तियों में व्यक्त करने देते हैं।
- **प्रदर्शन**: उचित रूप से अनुक्रमित डेटाबेस पर एक अच्छी तरह से लिखी गई SQL क्वेरी मिलीसेकंड में लाखों पंक्तियों को संसाधित कर सकती है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सामान्य प्रयोजन वाली भाषा नहीं** | SQL में एप्लिकेशन, एपीआई या एल्गोरिदम नहीं बना सकते | पायथन, जावा, जावास्क्रिप्ट, आदि के साथ संयोजन करें
| **बोली अंतर** | असंगत एक्सटेंशन के साथ प्रत्येक आरडीबीएमएस का अपना एसक्यूएल फ्लेवर होता है जहां संभव हो एएनएसआई एसक्यूएल पर टिके रहें; आपके आवेदन में अमूर्त बोली अंतर |
| **स्कीमा कठोरता** | बड़ी टेबलों पर टेबल संरचनाओं को बदलना धीमा और विघटनकारी हो सकता है | माइग्रेशन टूल का उपयोग करें; स्कीमा को पहले से सावधानीपूर्वक डिज़ाइन करें |
| **एन+1 क्वेरी समस्या** | ORM-जनरेटेड क्वेरीज़ बेहद अकुशल हो सकती हैं | जटिल प्रश्नों के लिए कस्टम SQL लिखें; व्याख्या विश्लेषण के साथ प्रोफ़ाइल |
| **स्केलिंग जटिलता** | NoSQL | की तुलना में SQL डेटाबेस को क्षैतिज रूप से स्केल करना कठिन है विशिष्ट उपयोग के मामलों के लिए रीड प्रतिकृतियां, शार्डिंग का उपयोग करें, या NoSQL पर विचार करें |
---

## मूल अवधारणाएँ
### रिलेशनल मॉडल
डेटा **टेबल** (संबंध) में संग्रहीत किया जाता है, जिसमें **पंक्तियाँ** (रिकॉर्ड/ट्यूपल्स) और **कॉलम** (विशेषताएं/फ़ील्ड) शामिल होते हैं। तालिकाओं को **कुंजियों** के माध्यम से एक दूसरे से संबंधित किया जा सकता है।
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

## सिंटेक्स बुनियादी बातें
### डेटा पुनर्प्राप्त करना (चयन करें)
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

### एकत्रीकरण
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

### तालिकाओं को जोड़ना
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

### डेटा संशोधित करना
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

## उन्नत सिंटैक्स और पैटर्न
### विंडो फ़ंक्शंस - डीप डाइव
विंडो फ़ंक्शंस वर्तमान पंक्ति से संबंधित पंक्तियों के एक सेट में गणना करते हैं - उन्हें GROUP BY की तरह एकल आउटपुट पंक्ति में संक्षिप्त किए बिना।
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

### सामान्य टेबल एक्सप्रेशन (सीटीई) - उन्नत उपयोग
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

### JSON संचालन
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

### संग्रहित प्रक्रियाएं और ट्रिगर
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

## मुख्य विशेषताओं में गहराई से उतरें
### क्वेरी अनुकूलन
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

**अनुकूलन चेकलिस्ट:**
| अंक | लक्षण | ठीक करें |
|-------|---------|-----|
| बड़ी मेज पर अनुक्रमिक स्कैन |  व्याख्या में __संरक्षित_0__ | उचित अनुक्रमणिका जोड़ें |
| WHERE कॉलम पर अनुपलब्ध अनुक्रमणिका | पूर्ण टेबल स्कैन | फ़िल्टर किए गए कॉलम पर इंडेक्स बनाएं |
| चयन करें *अपशिष्ट | अनावश्यक कॉलम लाये जा रहे हैं | केवल आवश्यक कॉलम चुनें |
| निहित प्रकार रूपांतरण | सूचकांक का उपयोग नहीं किया गया | तुलना में मिलान प्रकार |
| अनुक्रमित स्तंभों पर कार्य | सूचकांक अनुपयोगी (नॉन-सारगेबल) | पुनः लिखें:`WHERE date >= '2024-01-01'`नहीं`WHERE YEAR(date) = 2024`|
### अनुक्रमण रणनीतियाँ
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

### लेनदेन अलगाव स्तर
| अलगाव स्तर | गंदा पढ़ें | गैर-दोहराने योग्य पढ़ें | प्रेत पढ़ें |
|-----------------|:----------:|:-------------------:|:----------------:|
| अनकमिटेड पढ़ें | हाँ | हाँ | हाँ |
| पढ़ें प्रतिबद्ध | नहीं | हाँ | हाँ |
| दोहराने योग्य पढ़ें | नहीं | नहीं | हाँ* |
| क्रमबद्ध | नहीं | नहीं | नहीं |
```sql
-- Setting isolation level (PostgreSQL)
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### सामान्यीकरण
| सामान्य रूप | नियम | उदाहरण उल्लंघन |
|---|------|-------------------|
| **1NF** | परमाणु मान, कोई दोहराव वाला समूह नहीं | एक कॉलम में एकाधिक फ़ोन को "123,456" के रूप में संग्रहित करना |
| **2NF** | 1NF + कोई आंशिक निर्भरता नहीं | ऑर्डर विवरण ऑर्डर_आईडी पर निर्भर करता है, लेकिन उत्पाद_आईडी पर नहीं |
| **3NF** | 2NF + कोई सकर्मक निर्भरता नहीं | कर्मचारी विभाग का नाम विभाग आईडी पर निर्भर करता है, कर्मचारी पर नहीं |
---

## डेटाबेस संरचना को परिभाषित करना
### तालिकाएँ बनाना
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

### तालिकाएँ बदलना
```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;
ALTER TABLE users RENAME COLUMN phone TO phone_number;
ALTER TABLE users DROP COLUMN phone_number;
```
---

## परियोजना विन्यास एवं निर्माण प्रणाली
### प्रवासन उपकरण
| उपकरण | भाषा/स्टैक | दृष्टिकोण |
|------|----------------------|----------|
| **फ्लाईवे** | जावा / सामान्य | SQL-आधारित माइग्रेशन, सरल नामकरण परंपरा |
| **लिक्विबेस** | जावा / सामान्य | XML, YAML, JSON, या SQL चेंजलॉग |
| **एलेम्बिक** | पायथन (SQLAlchemy) | मॉडल परिवर्तनों से स्वत: माइग्रेशन उत्पन्न होता है |
| **प्रिज्मा माइग्रेट** | Node.js / टाइपस्क्रिप्ट | स्कीमा-प्रथम, स्वचालित रूप से SQL उत्पन्न करता है |
| **गोलंग-माइग्रेट** | जाओ | SQL-आधारित, अप/डाउन माइग्रेशन का समर्थन करता है |
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

## परीक्षण
### डेटा जनरेशन का परीक्षण करें
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

| ढाँचा | डेटाबेस | विवरण |
|----|-------|----|
| **pgTAP** | पोस्टग्रेएसक्यूएल | इकाई परीक्षण रूपरेखा |
| **tSQLt** | एसक्यूएल सर्वर | SQL सर्वर के लिए यूनिट परीक्षण |
| **utPLSQL** | ओरेकल | Oracle PL/SQL के लिए परीक्षण ढाँचा |
---

## अंतरसंचालनीयता
### भाषा बंधन
| इंटरफ़ेस | भाषा | विवरण |
|----|-------|----|
| **जेडीबीसी** | जावा | मानक डेटाबेस एपीआई |
| **ओडीबीसी** | एकाधिक | यूनिवर्सल डेटाबेस एपीआई |
| **psycopg2/3** | पायथन | PostgreSQL एडाप्टर |
| **डेटाबेस/एसक्यूएल** | जाओ | ड्राइवर इंटरफ़ेस के साथ मानक पुस्तकालय |
| **sqlite3** | पायथन | अंतर्निहित SQLite समर्थन |
| **पृष्ठ** | नोड.जेएस | PostgreSQL क्लाइंट |
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

## डिज़ाइन पैटर्न
### पैटर्न 1: धुरी/क्रॉसटैब
```sql
SELECT product_name,
    COALESCE(SUM(CASE WHEN month = 'Jan' THEN revenue END), 0) AS jan,
    COALESCE(SUM(CASE WHEN month = 'Feb' THEN revenue END), 0) AS feb,
    COALESCE(SUM(CASE WHEN month = 'Mar' THEN revenue END), 0) AS mar
FROM monthly_sales WHERE year = 2024 GROUP BY product_name;
```

### पैटर्न 2: प्रति समूह टॉप-एन
```sql
SELECT * FROM (
    SELECT o.*, u.name,
        ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.created_at DESC) AS rn
    FROM orders o JOIN users u ON o.user_id = u.id
) ranked WHERE rn <= 3;
```

### पैटर्न 3: अंतराल और द्वीप
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

### पैटर्न 4: धीरे-धीरे बदलते आयाम (एससीडी प्रकार 2)
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

## प्रदर्शन: सूचकांक और क्वेरी योजना
### इंडेक्स कैसे काम करते हैं
इंडेक्स एक डेटा संरचना (आमतौर पर एक बी-ट्री) है जो डेटाबेस को संपूर्ण तालिका को स्कैन किए बिना पंक्तियां ढूंढने देता है।
```sql
-- Without index: database scans every row (slow for large tables)
SELECT * FROM users WHERE email = 'alice@mail.com';

-- With index: database jumps directly to the matching row (fast)
CREATE INDEX idx_users_email ON users(email);
```

| सूचकांक प्रकार | के लिए सर्वश्रेष्ठ | उदाहरण |
|----|---|----|
| **बी-ट्री** (डिफ़ॉल्ट) | समानता और सीमा प्रश्न |  __संरक्षित_0__ |
| **हैश** | केवल सटीक समानता |  __संरक्षित_1__ |
| **जिन** | पूर्ण-पाठ खोज, सरणियाँ, JSON |  __संरक्षित_2__ |
| **गिस्ट** | ज्यामितीय/स्थानिक डेटा |  __संरक्षित_3__ |
### क्वेरी योजनाएं पढ़ना
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

## एसक्यूएल बोलियाँ
| फ़ीचर | पोस्टग्रेएसक्यूएल | MySQL | एसक्यूएल सर्वर | SQLite |
|---------|--------|-------|---|-------|
| स्वतः-वृद्धि |  __संरक्षित_0__ / __संरक्षित_1__ |  __संरक्षित_2__ |  __संरक्षित_3__ |  __संरक्षित_4__ |
| स्ट्रिंग कॉनकैट |  __संरक्षित_5__ |  __संरक्षित_6__ |  __संरक्षित_7__ या __संरक्षित_8__ |  __संरक्षित_9__ |
| दिनांक कार्य |  __संरक्षित_10__ , __संरक्षित_11__ |  __संरक्षित_12__ , __संरक्षित_13__ |  __संरक्षित_14__ , __संरक्षित_15__ |  __संरक्षित_16__ |
| JSON समर्थन | उत्कृष्ट (__प्रोटेक्टेड_17__) | अच्छा (__प्रोटेक्टेड_18__) | अच्छा (__प्रोटेक्टेड_19__) | बुनियादी (`JSON1`) |
| पूर्ण-पाठ खोज | बिल्ट-इन (__प्रोटेक्टेड_21__) | अंतर्निर्मित | अंतर्निर्मित | सीमित |
| विंडो फ़ंक्शंस | हाँ | हाँ (8.0+) | हाँ | हाँ |
---

## तैनाती
### डेटाबेस परिनियोजन रणनीतियाँ
| रणनीति | विवरण | जोखिम स्तर |
|---|----|----|
| **माइग्रेशन फ़ाइलें** | संस्करणबद्ध SQL स्क्रिप्ट क्रम में लागू | निम्न |
| **नीला-हरा परिनियोजन** | दो समान डेटाबेस; ट्रैफ़िक स्विच करें | निम्न |
| **विस्तार-अनुबंध** | नया कॉलम जोड़ें, दोहरा लिखें, माइग्रेट करें, पुराना छोड़ें | निम्न |
| **डायरेक्ट डीडीएल** | उत्पादन पर सीधे ALTER TABLE चलाना | उच्च |
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

## SQL का उपयोग कब करें
| परिदृश्य | एसक्यूएल क्यों | वैकल्पिक |
|---|---|---|
| जटिल प्रश्नों के साथ संबंधपरक डेटा | SQL को इसी लिए डिज़ाइन किया गया है | --- |
| लेनदेन संबंधी अखंडता (एसीआईडी) | SQL डेटाबेस स्थिरता की गारंटी देते हैं | --- |
| रिपोर्टिंग और विश्लेषण | एकत्रीकरण, विंडो फ़ंक्शन, सीटीई | बहुत जटिल विश्लेषण के लिए पायथन (पांडा) |
| डेटा अखंडता बाधाएं | विदेशी कुंजियाँ, चेक, अद्वितीय, शून्य नहीं | एप्लिकेशन-स्तरीय सत्यापन (कमजोर) |
| सरल कुंजी-मूल्य भंडारण | इस उपयोग के मामले में ओवरकिल | रेडिस, डायनेमोडीबी |
| अत्यधिक असंरचित डेटा | स्कीमा कठोरता एक समस्या है | MongoDB, दस्तावेज़ डेटाबेस |
| विशाल क्षैतिज स्केलिंग | SQL डेटाबेस को शार्प करना कठिन | कैसेंड्रा, डायनेमोडीबी, कॉकरोचडीबी |
---

## सारांश
SQL 50 साल पुरानी भाषा है जो आज भी आवश्यक है। प्रत्येक डेवलपर, डेटा वैज्ञानिक और विश्लेषक को इसे जानना आवश्यक है। मुख्य भाषा मानकीकृत और पोर्टेबल है; बोली संबंधी अंतर प्रबंधनीय हैं। आधुनिक एसक्यूएल (विंडो फ़ंक्शंस, सीटीई और जेएसओएन समर्थन के साथ) अधिकांश डेटा कार्यों के लिए पर्याप्त रूप से अभिव्यंजक है। प्रमुख कौशल हैं: कुशल क्वेरीज़ लिखना, इंडेक्स को समझना, क्वेरी प्लान पढ़ना और अच्छे स्कीमा डिज़ाइन करना। यदि आप डेटा के साथ बिल्कुल भी काम करते हैं, तो SQL पर समझौता नहीं किया जा सकता है।