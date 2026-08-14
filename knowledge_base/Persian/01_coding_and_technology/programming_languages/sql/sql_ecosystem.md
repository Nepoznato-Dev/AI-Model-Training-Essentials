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
# SQL - راهنمای اکوسیستم و ابزار
این راهنما پایگاه های داده، ابزارها و زیرساخت های ضروری در اکوسیستم SQL را پوشش می دهد.
---

## سیستم های پایگاه داده
### رابطه ای (OLTP)
| پایگاه داده | نوع | بهترین برای |
|----------|------|----------|
| **PostgreSQL** | منبع باز | دارای بیشترین ویژگی، قابل توسعه |
| **MySQL / MariaDB** | منبع باز | برنامه های کاربردی وب |
| **SQLite** | تعبیه شده | موبایل، دسکتاپ، اپلیکیشن های کوچک |
| **SQL Server** | تجاری | اینترپرایز (مایکروسافت) |
| **اوراکل** | تجاری | شرکت بزرگ |
| **DB2** | تجاری | شرکت IBM |
| **سوسکDB** | توزیع شده | Cloud-Native، سازگار با PostgreSQL |
| **TiDB** | توزیع شده | سازگار با MySQL، HTAP |
| **YugabyteDB** | توزیع شده | سازگار با PostgreSQL |
### تحلیلی (OLAP)
| پایگاه داده | نوع | بهترین برای |
|----------|------|----------|
| **ClickHouse** | ستونی | تجزیه و تحلیل بلادرنگ |
| **DuckDB** | تعبیه شده | تجزیه و تحلیل در فرآیند |
| **دانه برف** | ابر | انبار داده |
| **BigQuery** | ابر | گوگل آنالیتیک |
| **Redshift** | ابر | تجزیه و تحلیل AWS |
| **آپاچی دروید** | ستونی | تجزیه و تحلیل سری زمانی |
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

## ابزارهای مهاجرت
| ابزار | نوع | یادداشت ها |
|------|------|-------|
| **فلای وی** | مبتنی بر جاوا | مهاجرت های ساده و SQL |
| **Liquibase** | XML/SQL/YAML | درجه سازمانی |
| **آلمبیک** | پایتون | مهاجرت های SQLAlchemy |
| **پریسما مهاجرت** | TypeScript | مهاجرت های نوع ایمن |
| **گلانگ-مهاجرت** | برو | مهاجرت های پایگاه داده |
| **اطلس** | مدرن | طرحواره به عنوان کد |
| **dbmate** | چند دی بی | CLI ساده |
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

## Query Builders & ORMs
| ابزار | زبان | نوع |
|------|----------|------|
| **پریسما** | TypeScript | نوع ایمن ORM |
| **نم نم نم باران** | TypeScript | نوع ایمن SQL |
| **عاقبت ** | جاوا اسکریپت | ORM کامل |
| **Knex.js** | جاوا اسکریپت | سازنده پرس و جو |
| **SQLAlchemy** | پایتون | ORM کامل + هسته |
| **Django ORM** | پایتون | ORM کامل |
| **پیوی** | پایتون | ORM سبک |
| **فصیح** | پی اچ پی (لاراول) | Active Record ORM |
| **دکترین** | PHP (Symfony) | داده نگاشت ORM |
| **Entity Framework** | سی شارپ | ORM کامل |
| **دپر** | سی شارپ | Micro-ORM |
| **خواب زمستانی** | جاوا | ORM کامل |
| **jOOQ** | جاوا | نوع ایمن SQL |
| **GORM** | برو | ORM کامل |
| **sqlc** | برو | تولید Go از SQL |
| **دیزل** | زنگ زدگی | نوع ایمن ORM |
| **SQLx** | زنگ زدگی | Async SQL |
| **SeaORM** | زنگ زدگی | Async ORM |
---

## ابزارهای رابط کاربری گرافیکی و IDE
| ابزار | نوع | یادداشت ها |
|------|------|-------|
| **دی بیور** | جهانی | رایگان، چند پایگاه داده |
| **DataGrip** | جت برینز | بهترین SQL IDE |
| **pgAdmin** | PostgreSQL | ادمین مبتنی بر وب |
| **MySQL Workbench** | MySQL | ابزار رسمی |
| **HeidiSQL** | ویندوز | سبک |
| **TablePlus** | مدرن | رابط کاربری زیبا |
| **استودیو زنبورداری** | منبع باز | مبتنی بر الکترون |
| **psql** | CLI | ترمینال PostgreSQL |
| **mysql** | CLI | ترمینال MySQL |
| **sqlite3** | CLI | ترمینال SQLite |
---

## عملکرد و تجزیه و تحلیل
| ابزار | هدف |
|------|---------|
| **توضیح تجزیه و تحلیل** | طرح اجرای پرس و جو |
| **pg_stat_statements** | آمار پرس و جو PostgreSQL |
| **توضیح ** | برنامه اجرایی (MySQL) |
| **نمایش نمایه** | پروفایل MySQL |
| **نمایه سرور SQL** | پروفایل SQL Server |
| **pgBadger** | تحلیلگر لاگ PostgreSQL |
| **pt-query-digest** | تجزیه و تحلیل پرس و جو MySQL |
| **sys views** | نمایش سیستم MySQL |
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

## تست
| ابزار | هدف |
|------|---------|
| **tSQLt** | تست واحد SQL Server |
| **pgTAP** | تست PostgreSQL |
| **utPLSQL** | تست اوراکل |
| **dbtest** | تست پایگاه داده |
| **تست ظروف** | تست های DB مبتنی بر داکر |
| **sqlfluff** | SQL linting |
| **schemalint** | لینتینگ طرحواره |
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

## SQL Linting & Formatting
| ابزار | هدف |
|------|---------|
| **SQLFluff** | لینتر و فرم دهنده |
| **sql-formater** | قالب بندی SQL |
| **صدا کردن** | لینتر مهاجرت PostgreSQL |
| **psql2go** | مبدل SQL به Go |
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

## مفاهیم کلیدی SQL
| مفهوم | توضیحات |
|---------|-------------|
| **اسید** | اتمی، سازگاری، انزوا، دوام |
| ** عادی سازی ** | 1NF، 2NF، 3NF، BCNF |
| **شاخص** | B-tree، Hash، GIN، GiST، BRIN |
| **معاملات** | شروع، تعهد، بازگشت |
| **پیوستن** | داخلی، چپ، راست، کامل، متقاطع |
| **توابع پنجره** | ROW_NUMBER، RANK، LAG، LEAD |
| **CTE** | WITH، پرس و جوهای بازگشتی |
| **نمایش** | جداول مجازی |
| **محرک** | اقدامات خودکار |
| **رویه های ذخیره شده** | کد SQL قابل استفاده مجدد |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **داکر** | تصاویر رسمی (postgres، mysql) |
| **سرویس های مدیریت شده** | RDS، Cloud SQL، Azure SQL |
| **Flyway / Liquibase** | مهاجرت های طرحواره |
| **pg_dump / mysqldump** | پشتیبان گیری |
| **WAL-E / pgBackRest** | پشتیبان گیری PostgreSQL |
| **اپراتورهای Kubernetes** | CloudNativePG، Vitess |
---

## خلاصه
اکوسیستم SQL ده ها موتور پایگاه داده و صدها ابزار را در بر می گیرد. پشته استاندارد عبارتند از: **PostgreSQL** به عنوان پایگاه داده پیش فرض (غنی ترین منبع باز)، **MySQL** برای برنامه های کاربردی وب، **SQLite** برای استفاده جاسازی شده، **Flyway** یا **Liquibase** برای مهاجرت، **DBeaver** یا **DataGrip**** به عنوان GUI، SQLPlu، و EXQ به عنوان رابط کاربری گرافیکی، SQLitting، GUI، SQ و LFIN تجزیه و تحلیل ** برای تنظیم عملکرد. توسعه SQL مدرن از ORMهای ایمن نوع مانند **Prisma** (TypeScript)، **SQLAlchemy** (Python) یا **sqlc** (Go) برای تولید کد از SQL استفاده می کند. SQL همچنان زبان جهانی برای داده ها است که در هر پشته فناوری ضروری است.