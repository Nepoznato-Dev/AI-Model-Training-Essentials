# SQL त्वरित संदर्भ मार्गदर्शिका

डेटाबेस ऑपरेशनों के लिए आवश्यक SQL कमांड।

---

## मूल क्वेरी संरचना

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

## डेटा प्राप्ति (SELECT)

### मूल चयन
```sql
-- सभी कॉलम चुनें
SELECT * FROM users;

-- विशिष्ट कॉलम चुनें
SELECT id, name, email FROM users;

-- उपनाम के साथ चुनें
SELECT name AS user_name, email AS contact FROM users;

-- अलग-अलग मान चुनें
SELECT DISTINCT country FROM users;
```

### फ़िल्टरिंग (WHERE)
```sql
-- तुलना ऑपरेटर
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- A से शुरू होता है
SELECT * FROM users WHERE name LIKE '%son';    -- son पर समाप्त होता है
SELECT * FROM users WHERE name LIKE '%test%';  -- test शामिल है
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- लॉजिकल ऑपरेटर
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### क्रमबद्ध करना और सीमा निर्धारित करना
```sql
-- एकल कॉलम के अनुसार क्रमबद्ध करें
SELECT * FROM products ORDER BY price DESC;

-- कई कॉलमों के अनुसार क्रमबद्ध करें
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- परिणामों की सीमा निर्धारित करें
SELECT * FROM users LIMIT 10;

-- Offset (पृष्ठांकन के लिए)
SELECT * FROM users LIMIT 10 OFFSET 20;  -- 20 छोड़ें, 10 लें
```

---

## एग्रीगेशन फ़ंक्शन

```sql
-- पंक्तियों की गिनती करें
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- योग, औसत, न्यूनतम, अधिकतम
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- समूह बनाएँ
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having (समूहों को फ़िल्टर करें)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## जॉइन

### इनर जॉइन
```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### लेफ्ट/राइट जॉइन
```sql
-- सभी users, यहाँ तक कि वे भी जिनके orders नहीं हैं
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- सभी orders, यहाँ तक कि वे भी जिनके users नहीं हैं (दुर्लभ)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### फुल आउटर जॉइन
```sql
-- सभी users और सभी orders (MySQL FULL OUTER का समर्थन नहीं करता)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### क्रॉस जॉइन
```sql
-- कार्टेशियन प्रोडक्ट (सभी संयोजन)
SELECT * FROM colors CROSS JOIN sizes;
```

### सेल्फ जॉइन
```sql
-- employees और उनके managers खोजें
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## सबक्वेरी

```sql
-- WHERE खंड में
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- SELECT खंड में
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- FROM खंड में
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- EXISTS के साथ
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## सेट ऑपरेशन्स

```sql
-- UNION (डुप्लिकेट्स हटाता है)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (डुप्लिकेट्स बनाए रखता है)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT (सामान्य पंक्तियाँ)
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2024;

-- EXCEPT/MINUS (पहले में मौजूद, लेकिन दूसरे में नहीं)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## डेटा संशोधन

### INSERT
```sql
-- एकल पंक्ति जोड़ें
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- कई पंक्तियाँ जोड़ें
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- SELECT से जोड़ें
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### UPDATE
```sql
-- एकल पंक्ति अपडेट करें
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- कई कॉलम अपडेट करें
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- JOIN के साथ अपडेट करें
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### DELETE
```sql
-- विशिष्ट पंक्तियाँ हटाएँ
DELETE FROM users WHERE id = 1;

-- शर्त के साथ हटाएँ
DELETE FROM orders WHERE order_date < '2023-01-01';

-- JOIN के साथ हटाएँ
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- टेबल खाली करें (तेज़, auto-increment रीसेट करता है)
TRUNCATE TABLE temp_data;
```
