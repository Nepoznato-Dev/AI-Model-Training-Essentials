# دليل مرجعي سريع لـ SQL

أوامر SQL الأساسية لعمليات قواعد البيانات.

---

## بنية الاستعلام الأساسية

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

## استرجاع البيانات (SELECT)

### التحديد الأساسي
```sql
-- تحديد جميع الأعمدة
SELECT * FROM users;

-- تحديد أعمدة معينة
SELECT id, name, email FROM users;

-- التحديد مع اسم مستعار (alias)
SELECT name AS user_name, email AS contact FROM users;

-- تحديد القيم الفريدة
SELECT DISTINCT country FROM users;
```

### التصفية (WHERE)
```sql
-- عوامل المقارنة
SELECT * FROM products WHERE price > 100;
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE name IN ('Alice', 'Bob', 'Charlie');
SELECT * FROM users WHERE name LIKE 'A%';      -- تبدأ بحرف A
SELECT * FROM users WHERE name LIKE '%son';    -- تنتهي بـ son
SELECT * FROM users WHERE name LIKE '%test%';  -- تحتوي على test
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- العوامل المنطقية
SELECT * FROM users WHERE age >= 18 AND country = 'USA';
SELECT * FROM users WHERE age < 18 OR guardian IS NOT NULL;
SELECT * FROM products WHERE NOT discontinued;
```

### الترتيب والتحديد
```sql
-- الترتيب حسب عمود واحد
SELECT * FROM products ORDER BY price DESC;

-- الترتيب حسب أعمدة متعددة
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- تحديد عدد النتائج
SELECT * FROM users LIMIT 10;

-- الإزاحة (للتقسيم على صفحات)
SELECT * FROM users LIMIT 10 OFFSET 20;  -- تخطي 20، أخذ 10
```

---

## دوال التجميع

```sql
-- عد الصفوف
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- المجموع، المتوسط، الأصغر، الأكبر
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

-- التجميع حسب (Group by)
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Having (تصفية المجموعات)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## الدمج (Joins)

### الدمج الداخلي (Inner Join)
```sql
SELECT u.name, o.order_date, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### الدمج الأيسر/الأيمن (Left/Right Join)
```sql
-- جميع المستخدمين، حتى من ليس لديهم طلبات
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- جميع الطلبات، حتى تلك بدون مستخدمين (حالة نادرة)
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### الدمج الخارجي الكامل (Full Outer Join)
```sql
-- جميع المستخدمين وجميع الطلبات (MySQL لا يدعم FULL OUTER)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### الدمج التقاطعي (Cross Join)
```sql
-- الضرب الديكارتي (جميع التركيبات الممكنة)
SELECT * FROM colors CROSS JOIN sizes;
```

### الدمج الذاتي (Self Join)
```sql
-- إيجاد الموظفين ومديريهم
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## الاستعلامات الفرعية (Subqueries)

```sql
-- في جملة WHERE
SELECT name FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- في جملة SELECT
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE user_id = users.id) AS order_count
FROM users;

-- في جملة FROM
SELECT dept, avg_salary
FROM (
    SELECT department AS dept, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 60000;

-- باستخدام EXISTS
SELECT name FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

---

## عمليات المجموعات (Set Operations)

```sql
-- UNION (إزالة التكرارات)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (الاحتفاظ بالتكرارات)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;

-- INTERSECT (الصفوف المشتركة)
SELECT product_id FROM orders_2023
INTERSECT
SELECT product_id FROM orders_2024;

-- EXCEPT/MINUS (الصفوف الموجودة في الأول وليست في الثاني)
SELECT user_id FROM active_users
EXCEPT
SELECT user_id FROM banned_users;
```

---

## تعديل البيانات

### INSERT
```sql
-- إدراج صف واحد
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@example.com', 30);

-- إدراج عدة صفوف
INSERT INTO users (name, email, age)
VALUES 
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35);

-- الإدراج من SELECT
INSERT INTO archived_users
SELECT * FROM users WHERE last_login < '2023-01-01';
```

### UPDATE
```sql
-- تحديث صف واحد
UPDATE users 
SET email = 'newemail@example.com'
WHERE id = 1;

-- تحديث أعمدة متعددة
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'Electronics';

-- التحديث مع JOIN
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'processed'
WHERE u.country = 'USA';
```

### DELETE
```sql
-- حذف صفوف معينة
DELETE FROM users WHERE id = 1;

-- الحذف مع شرط
DELETE FROM orders WHERE order_date < '2023-01-01';

-- الحذف مع JOIN
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.status = 'deleted';

-- تفريغ الجدول (أسرع، يعيد تعيين الترقيم التلقائي)
TRUNCATE TABLE temp_data;
```

---

## عمليات الجداول

### إنشاء جدول (CREATE)
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

### تعديل جدول (ALTER)
```sql
-- إضافة عمود
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- تعديل عمود
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) NOT NULL;

-- إعادة تسمية عمود
ALTER TABLE users RENAME COLUMN username TO user_name;

-- حذف عمود
ALTER TABLE users DROP COLUMN phone;

-- إضافة قيد (constraint)
ALTER TABLE orders ADD CONSTRAINT fk_user 
FOREIGN KEY (user_id) REFERENCES users(id);

-- حذف قيد
ALTER TABLE orders DROP FOREIGN KEY fk_user;

-- إعادة تسمية جدول
ALTER TABLE old_name RENAME TO new_name;
```

### حذف جدول (DROP)
```sql
DROP TABLE IF EXISTS temp_table;
```

---

## القيود (Constraints)

```sql
-- PRIMARY KEY: معرّف فريد
CREATE TABLE users (
    id INT PRIMARY KEY
);

-- FOREIGN KEY: إشارة إلى جدول آخر
CREATE TABLE orders (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- UNIQUE: لا قيم مكررة
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- NOT NULL: حقل مطلوب
CREATE TABLE users (
    name VARCHAR(50) NOT NULL
);

-- CHECK: التحقق من صحة القيم
CREATE TABLE products (
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0)
);

-- DEFAULT: قيمة افتراضية
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## الفهارس (Indexes)

```sql
-- إنشاء فهرس
CREATE INDEX idx_email ON users(email);

-- إنشاء فهرس مركب
CREATE INDEX idx_name_age ON users(last_name, first_name);

-- إنشاء فهرس فريد
CREATE UNIQUE INDEX idx_username ON users(username);

-- حذف فهرس
DROP INDEX idx_email ON users;

-- عرض الفهارس
SHOW INDEX FROM users;
```

---

## طرق العرض (Views)

```sql
-- إنشاء طريقة عرض
CREATE VIEW active_users AS
SELECT id, name, email, country
FROM users
WHERE status = 'active';

-- استخدام طريقة العرض
SELECT * FROM active_users WHERE country = 'USA';

-- تحديث طريقة العرض (إن كانت قابلة للتحديث)
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, country, created_at
FROM users
WHERE status = 'active';

-- حذف طريقة عرض
DROP VIEW IF EXISTS active_users;
```

---

## تعبيرات الجداول الشائعة (CTEs)

```sql
-- CTE بسيط
WITH high_value_users AS (
    SELECT id, name, total_spent
    FROM users
    WHERE total_spent > 1000
)
SELECT * FROM high_value_users ORDER BY total_spent DESC;

-- CTE تكراري (بيانات هرمية)
WITH RECURSIVE org_chart AS (
    -- الحالة الأساسية
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- الحالة التكرارية
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## دوال النافذة (Window Functions)

```sql
-- ROW_NUMBER
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK و DENSE_RANK
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- المجموع التراكمي
SELECT date, amount,
       SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- نافذة مقسّمة (Partitioned)
SELECT department, name, salary,
       AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;

-- LAG و LEAD
SELECT date, sales,
       LAG(sales, 1) OVER (ORDER BY date) AS prev_day_sales,
       LEAD(sales, 1) OVER (ORDER BY date) AS next_day_sales
FROM daily_sales;
```

---

## أنواع البيانات

### الأنواع الرقمية
- `INT` - عدد صحيح
- `BIGINT` - عدد صحيح كبير
- `DECIMAL(p,s)` - عدد عشري دقيق (الدقة، المقياس)
- `FLOAT` - عدد عشري تقريبي
- `DOUBLE` - عدد عشري بدقة مضاعفة

### الأنواع النصية
- `CHAR(n)` - سلسلة نصية بطول ثابت
- `VARCHAR(n)` - سلسلة نصية بطول متغير
- `TEXT` - نص كبير
- `ENUM` - قيم معدودة (Enumerated)

### التاريخ/الوقت
- `DATE` - التاريخ (YYYY-MM-DD)
- `TIME` - الوقت (HH:MM:SS)
- `DATETIME` - التاريخ والوقت
- `TIMESTAMP` - طابع زمني Unix
- `YEAR` - قيمة السنة

### القيم المنطقية
- `BOOLEAN` أو `BOOL` - صحيح/خطأ

### الأنواع الثنائية
- `BLOB` - كائن ثنائي كبير
- `BINARY` - ثنائي بطول ثابت
- `VARBINARY` - ثنائي بطول متغير

---

## دوال مفيدة

### دوال السلاسل النصية
```sql
CONCAT(first_name, ' ', last_name)  -- دمج السلاسل النصية
UPPER(name)                          -- تحويل إلى أحرف كبيرة
LOWER(name)                          -- تحويل إلى أحرف صغيرة
SUBSTRING(name, 1, 3)                -- استخراج سلسلة فرعية
LENGTH(name)                         -- طول السلسلة النصية
TRIM(name)                           -- إزالة المسافات البيضاء
REPLACE(text, 'old', 'new')          -- استبدال سلسلة فرعية
```

### دوال التاريخ
```sql
NOW()                                -- التاريخ/الوقت الحالي
CURDATE()                            -- التاريخ الحالي
CURTIME()                            -- الوقت الحالي
DATE_ADD(NOW(), INTERVAL 7 DAY)      -- إضافة فترة زمنية
DATEDIFF(end_date, start_date)       -- الفرق بالأيام
YEAR(date_column)                    -- استخراج السنة
MONTH(date_column)                   -- استخراج الشهر
DAY(date_column)                     -- استخراج اليوم
```

### الدوال الرقمية
```sql
ROUND(value, 2)                      -- التقريب إلى منازل عشرية
CEIL(value)                          -- التقريب للأعلى
FLOOR(value)                         -- التقريب للأسفل
ABS(value)                           -- القيمة المطلقة
POWER(base, exp)                     -- الأس (Exponentiation)
SQRT(value)                          -- الجذر التربيعي
RAND()                               -- رقم عشوائي
```

### الدوال الشرطية
```sql
-- جملة CASE
SELECT name,
       CASE 
           WHEN age < 18 THEN 'Minor'
           WHEN age < 65 THEN 'Adult'
           ELSE 'Senior'
       END AS age_group
FROM users;

-- دالة IF (خاصة بـ MySQL)
SELECT IF(age >= 18, 'Adult', 'Minor') AS status FROM users;

-- COALESCE (إرجاع أول قيمة غير فارغة)
SELECT COALESCE(phone, email, 'No contact') AS contact FROM users;

-- NULLIF (إرجاع NULL إذا كانت القيمتان متساويتين)
SELECT NULLIF(value, 0) AS safe_value FROM data;
```

---

## نصائح لتحسين الأداء

✅ **افعل:**
- استخدم الفهارس على الأعمدة التي يتكرر الاستعلام عنها
- حدّد الأعمدة المطلوبة فقط (تجنب `SELECT *`)
- استخدم `EXPLAIN` لتحليل أداء الاستعلام
- طبّع (Normalize) البيانات بشكل مناسب
- استخدم الجمل التحضيرية (prepared statements) لمنع حقن SQL

❌ **لا تفعل:**
- استخدام الدوال على الأعمدة المفهرسة داخل جمل WHERE
- إنشاء عدد كبير جداً من الفهارس (يبطئ الكتابة)
- استخدام `SELECT DISTINCT` بلا داعٍ
- تجاهل خطط تنفيذ الاستعلام
- تخزين قيم محسوبة يمكن حسابها عند الطلب

---

## أفضل ممارسات الأمان

```sql
-- استخدم الاستعلامات ذات المعاملات (في كود التطبيق)
-- لا تقم أبداً بدمج مدخلات المستخدم مباشرة

-- امنح الصلاحيات الدنيا اللازمة فقط
GRANT SELECT, INSERT ON database.table TO 'user'@'localhost';
REVOKE DELETE ON database.table FROM 'user'@'localhost';

-- استخدم كلمات مرور قوية
-- فعّل اتصالات SSL
-- أجرِ مراجعات أمنية دورية
```

---

*آخر تحديث: يونيو 2025 | معيار SQL (متوافق مع MySQL/PostgreSQL)*
