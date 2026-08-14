<!--
---
# Metadata
title: "SQL — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the SQL ecosystem including databases, tools, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [sql, ecosystem, tooling, databases, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# SQL - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ SQL ایکو سسٹم میں ضروری ڈیٹا بیس، ٹولز اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## ڈیٹا بیس سسٹم
### رشتہ دار (OLTP)
| ڈیٹا بیس | قسم | کے لیے بہترین |
|------------|------|---------|
| **پوسٹگری ایس کیو ایل** | اوپن سورس | سب سے زیادہ خصوصیت سے بھرپور، قابل توسیع |
| **MySQL / MariaDB** | اوپن سورس | ویب ایپلیکیشنز |
| **SQLite** | ایمبیڈڈ | موبائل، ڈیسک ٹاپ، چھوٹی ایپس |
| **SQL سرور** | کمرشل | انٹرپرائز (مائیکروسافٹ) |
| **اوریکل** | کمرشل | بڑی انٹرپرائز |
| **DB2** | کمرشل | IBM انٹرپرائز |
| **کاکروچ ڈی بی** | تقسیم شدہ | کلاؤڈ-آبائی، PostgreSQL- موافق |
| **TiDB** | تقسیم شدہ | MySQL کے موافق، HTAP |
| **یوگا بائٹ ڈی بی** | تقسیم شدہ | PostgreSQL- ہم آہنگ |
### تجزیاتی (OLAP)
| ڈیٹا بیس | قسم | کے لیے بہترین |
|------------|------|---------|
| **کلک ہاؤس** | کالم | ریئل ٹائم تجزیات |
| **DuckDB** | ایمبیڈڈ | درون عمل تجزیات |
| **برف کی تہہ** | بادل | ڈیٹا گودام |
| **BigQuery** | بادل | گوگل تجزیات |
| **ریڈ شفٹ** | بادل | AWS تجزیات |
| **Apache Druid** | کالم | ٹائم سیریز کے تجزیات |
```sql
-- PostgreSQL example
CREATE TABLE users (
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    age         INTEGER CHECK (age > 0),
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created ON users(created_at);
```

---

## منتقلی کے اوزار
| ٹول | قسم | نوٹس |
|------|------|------|
| **فلائی وے** | جاوا پر مبنی | سادہ، SQL منتقلی |
| **لیکوبیس** | XML/SQL/YAML | انٹرپرائز گریڈ |
| **الیمبک** | ازگر | SQLAlchemy منتقلی |
| **پریزما ہجرت** | TypeScript | قسم سے محفوظ ہجرتیں |
| **گولنگ-ہجرت** | جاؤ | ڈیٹا بیس کی منتقلی |
| **اٹلس** | جدید | کوڈ کے طور پر سکیما |
| **dbmate** | ملٹی ڈی بی | سادہ سی ایل آئی |
```sql
-- Flyway migration: V1__create_users.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- V2__add_age_column.sql
ALTER TABLE users ADD COLUMN age INTEGER CHECK (age > 0);
CREATE INDEX idx_users_age ON users(age);
```

```bash
flyway migrate -url=jdbc:postgresql://localhost/mydb -user=postgres
```

---

## استفسار کرنے والے اور ORMs
| ٹول | زبان | قسم |
|------|------------|------|
| **پرزم** | TypeScript | ٹائپ سیف ORM |
| **بوندا باندی** | TypeScript | ٹائپ سیف ایس کیو ایل |
| **سیکوئلائز** | جاوا اسکرپٹ | مکمل ORM |
| **Knex.js** | جاوا اسکرپٹ | سوال بلڈر |
| **SQLA کیمیا** | ازگر | مکمل ORM + کور |
| **جیانگو ORM** | ازگر | مکمل ORM |
| **پیوی** | ازگر | ہلکا پھلکا ORM |
| **فصیح** | PHP (Laravel) | فعال ریکارڈ ORM |
| **نظریہ** | پی ایچ پی (سیمفونی) | ڈیٹا میپر ORM |
| **ہستی کا فریم ورک** | C# | مکمل ORM |
| **ڈیپر** | C# | مائیکرو-ORM |
| **ہائبرنیٹ** | جاوا | مکمل ORM |
| **jOOQ** | جاوا | ٹائپ سیف ایس کیو ایل |
| **گورم** | جاؤ | مکمل ORM |
| **sqlc** | جاؤ | ایس کیو ایل سے گو پیدا کریں۔
| **ڈیزل** | مورچا | ٹائپ سیف ORM |
| **SQLx** | مورچا | Async SQL |
| **SeaORM** | مورچا | Async ORM |
---

## GUI اور IDE ٹولز
| ٹول | قسم | نوٹس |
|------|------|------|
| **DBeaver** | یونیورسل | مفت، کثیر ڈیٹا بیس |
| **ڈیٹا گرپ** | جیٹ برینز | بہترین SQL IDE |
| **pgAdmin** | PostgreSQL | ویب پر مبنی ایڈمن |
| **MySQL ورک بینچ** | MySQL | سرکاری ٹول |
| **HeidiSQL** | ونڈوز | ہلکا پھلکا |
| **ٹیبل پلس** | جدید | خوبصورت UI |
| **مکھی پالنے والا اسٹوڈیو** | اوپن سورس | الیکٹران پر مبنی |
| **psql** | CLI | PostgreSQL ٹرمینل |
| **mysql** | CLI | MySQL ٹرمینل |
| **sqlite3** | CLI | SQLite ٹرمینل |
---

## کارکردگی اور تجزیہ
| ٹول | مقصد |
|------|---------|
| **تجزیہ کی وضاحت کریں** | استفسار پر عمل درآمد کا منصوبہ |
| **pg_stat_statements** | PostgreSQL استفسار کے اعدادوشمار |
| **وضاحت** | عمل درآمد کا منصوبہ (MySQL) |
| **پروفائل دکھائیں** | MySQL پروفائلنگ |
| **SQL سرور پروفائلر** | SQL سرور پروفائلنگ |
| **pgBadger** | PostgreSQL لاگ تجزیہ کار |
| **pt-query-digest** | MySQL استفسار کا تجزیہ |
| **sys views** | MySQL سسٹم کے نظارے |
```sql
-- Analyze query performance
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.created_at > '2024-01-01'
GROUP BY u.name
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC;

-- PostgreSQL: check indexes
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'users';
```

---

## ٹیسٹنگ
| ٹول | مقصد |
|------|---------|
| **tSQLt** | ایس کیو ایل سرور یونٹ ٹیسٹنگ |
| **pgTAP** | PostgreSQL ٹیسٹنگ |
| **utPLSQL** | اوریکل ٹیسٹنگ |
| **dbtest** | ڈیٹا بیس ٹیسٹنگ |
| **ٹیسٹ کنٹینرز** | ڈوکر پر مبنی DB ٹیسٹ |
| **sqlfluff** | SQL linting |
| **سکیملنٹ** ​​| سکیما لنٹنگ |
```sql
-- pgTAP example
BEGIN;
SELECT plan(3);

SELECT has_table('public', 'users', 'users table exists');
SELECT has_column('users', 'email', 'email column exists');
SELECT col_is_unique('users', 'email', 'email is unique');

SELECT * FROM finish();
ROLLBACK;
```

---

## ایس کیو ایل لنٹنگ اور فارمیٹنگ
| ٹول | مقصد |
|------|---------|
| **SQLFluff** | لنٹر اور فارمیٹر |
| **sql-formatter** | SQL فارمیٹنگ |
| **اسکواک** | PostgreSQL منتقلی لنٹر |
| **psql2go** | ایس کیو ایل ٹو گو کنورٹر |
```ini
# .sqlfluff
[sqlfluff]
dialect = postgres
max_line_length = 120

[sqlfluff:rules]
capitalisation_policy = upper
```

```bash
sqlfluff lint migrations/
sqlfluff fix migrations/
```

---

## کلیدی SQL تصورات
| تصور | تفصیل |
|---------|---------------|
| **ACID** | جوہری، مستقل مزاجی، تنہائی، استحکام |
| **نارملائزیشن** | 1NF، 2NF، 3NF، BCNF |
| **اشاریہ جات** | B-tree, Hash, GIN, GiST, BRIN |
| **لین دین** | شروع کریں، کمٹ کریں، رول بیک کریں |
| **شامل ہوتا ہے** | اندرونی، بائیں، دائیں، مکمل، کراس |
| **ونڈو کے افعال** | ROW_NUMBER، RANK، LAG، LEAD |
| **CTEs** | کے ساتھ، تکراری سوالات |
| **منظر** | ورچوئل ٹیبلز |
| **متحرکات** | خودکار کارروائیاں |
| **ذخیرہ شدہ طریقہ کار** | دوبارہ قابل استعمال SQL کوڈ |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **ڈوکر** | سرکاری تصاویر (پوسٹگریس، ایس کیو ایل) |
| **منظم خدمات** | RDS، Cloud SQL، Azure SQL |
| **فلائی وے / لیکوبیس** | سکیما منتقلی |
| **pg_dump / mysqldump** | بیک اپ |
| **WAL-E / pgBackRest** | PostgreSQL بیک اپ |
| **Kubernetes آپریٹرز** | CloudNativePG، Vitess |
---

## خلاصہ
SQL کا ماحولیاتی نظام درجنوں ڈیٹا بیس انجنوں اور سینکڑوں ٹولز پر محیط ہے۔ معیاری اسٹیک یہ ہے: **PostgreSQL** بطور ڈیفالٹ ڈیٹا بیس (سب سے زیادہ خصوصیت سے بھرپور اوپن سورس)، **MySQL** ویب ایپلیکیشنز کے لیے، **SQLite** ایمبیڈڈ استعمال کے لیے، **Flyway** یا **Liquibase** منتقلی کے لیے، **DBeaver** یا **DataGrip** کے لیے، **DataGrip** اور GUITGrip** کے لیے پرفارمنس ٹیوننگ کے لیے **تجزیہ کی وضاحت کریں**۔ ایس کیو ایل سے کوڈ بنانے کے لیے جدید SQL ڈیولپمنٹ ٹائپ سیف ORMs جیسے **Prisma** (TypeScript)، **SQLAlchemy** (Python) یا **sqlc** (Go) کا استعمال کرتی ہے۔ ایس کیو ایل ڈیٹا کے لیے آفاقی زبان بنی ہوئی ہے، ہر ٹیکنالوجی اسٹیک میں ضروری ہے۔