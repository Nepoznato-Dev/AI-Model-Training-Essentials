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
# SQL - دليل النظام البيئي والأدوات
يغطي هذا الدليل قواعد البيانات والأدوات والبنية التحتية الأساسية في نظام SQL البيئي.
---

## أنظمة قواعد البيانات
### العلائقية (OLTP)
| قاعدة بيانات | اكتب | الأفضل لـ |
|----------|------|---------|
| ** بوستجريس كيو ال ** | مفتوح المصدر | الأكثر ثراءً بالميزات، وقابلة للتوسيع |
| ** ماي إس كيو إل / ماريا دي بي ** | مفتوح المصدر | تطبيقات الويب |
| ** سكليتي ** | مضمن | تطبيقات الهاتف المحمول وسطح المكتب والتطبيقات الصغيرة |
| **خادم SQL** | تجاري | إنتربرايز (مايكروسوفت) |
| ** أوراكل ** | تجاري | مؤسسة كبيرة |
| **DB2** | تجاري | مؤسسة آي بي إم |
| ** صرصور دي بي ** | وزعت | سحابي أصلي، متوافق مع PostgreSQL |
| **تيدب** | وزعت | متوافق مع MySQL، HTAP |
| **يوغا بايت دي بي** | وزعت | متوافق مع PostgreSQL |
### التحليلية (OLAP)
| قاعدة بيانات | اكتب | الأفضل لـ |
|----------|------|---------|
| ** كليك هاوس ** | عمودي | تحليلات في الوقت الحقيقي |
| **داك دي بي** | مضمن | التحليلات الجارية |
| **ندفة الثلج** | سحابة | مستودع البيانات |
| **بيج كويري** | سحابة | تحليلات جوجل |
| **التحول نحو الأحمر** | سحابة | تحليلات AWS |
| **اباتشي درويد** | عمودي | تحليلات السلاسل الزمنية |
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

## أدوات الهجرة
| أداة | اكتب | ملاحظات |
|------|------|-------|
| **مسار الهجرة** | القائم على جافا | عمليات ترحيل بسيطة لـ SQL |
| **ليكويبيز** | XML/SQL/YAML | على مستوى المؤسسات |
| **الإلبيك** | بايثون | ترحيلات SQLAlchemy |
| **ترحيل بريزما** | تايب سكريبت | عمليات الترحيل الآمنة من النوع |
| **جولانج-هاجر** | اذهب | ترحيل قاعدة البيانات |
| **أطلس** | حديث | المخطط كرمز |
| ** دي بي ميت ** | متعدد ديسيبل | سطر الأوامر البسيط |
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

## منشئو الاستعلامات وORMs
| أداة | اللغة | اكتب |
|------|----------|------|
| **بريزما** | تايب سكريبت | ORM من النوع الآمن |
| ** رذاذ ** | تايب سكريبت | نوع SQL آمن |
| ** تكملة ** | جافا سكريبت | ORM كامل |
| **Knex.js** | جافا سكريبت | منشئ الاستعلام |
| **SQLAlchemy** | بايثون | ORM كامل + كور |
| ** جانغو أورم ** | بايثون | ORM كامل |
| ** بيوي ** | بايثون | ORM خفيف الوزن |
| **بليغ** | PHP (لارافيل) | السجل النشط ORM |
| **العقيدة** | PHP (سيمفوني) | مخطط البيانات ORM |
| **إطار الكيان** | ج # | ORM كامل |
| ** دابر ** | ج # | مايكرو أورم |
| ** السبات ** | جافا | ORM كامل |
| **جوك** | جافا | نوع SQL آمن |
| ** جورم ** | اذهب | ORM كامل |
| ** sqlc ** | اذهب | توليد الذهاب من SQL |
| **ديزل** | الصدأ | ORM من النوع الآمن |
| **SQLx** | الصدأ | SQL غير المتزامن |
| **SeaORM** | الصدأ | ORM غير متزامن |
---

## أدوات واجهة المستخدم الرسومية وIDE
| أداة | اكتب | ملاحظات |
|------|------|-------|
| **دي بيفر** | عالمي | قاعدة بيانات متعددة ومجانية |
| ** داتا جريب ** | جيت براينز | أفضل بيئة تطوير متكاملة SQL |
| **pgAdmin** | بوستجرس كيو ال | المشرف على شبكة الإنترنت |
| **منضدة MySQL** | ماي إس كيو إل | الأداة الرسمية |
| **هايدي إس كيو إل** | ويندوز | خفيف الوزن |
| ** تابل بلس ** | حديث | واجهة مستخدم جميلة |
| ** ستوديو النحال ** | مفتوح المصدر | القائم على الإلكترون |
| **بسقل** | سطر الأوامر | محطة PostgreSQL |
| ** الخلية ** | سطر الأوامر | محطة ماي إس كيو إل |
| **سكليت3** | سطر الأوامر | محطة سكليتي |
---

## الأداء والتحليل
| أداة | الغرض |
|------|---------|
| **شرح التحليل** | خطة تنفيذ الاستعلام |
| **pg_stat_statements** | إحصائيات استعلام PostgreSQL |
| **شرح** | خطة التنفيذ (MySQL) |
| **إظهار الملف الشخصي** | ملفات تعريف MySQL |
| **ملف تعريف خادم SQL** | ملف تعريف SQL Server |
| **pgBadger** | محلل سجل PostgreSQL |
| **pt-query-digest** | تحليل استعلام MySQL |
| **مشاهدات النظام** | طرق عرض نظام MySQL |
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

## الاختبار
| أداة | الغرض |
|------|---------|
| **تسكلت** | اختبار وحدة SQL Server |
| **ص.تاب** | اختبار PostgreSQL |
| **utPLSQL** | اختبار أوراكل |
| ** دي بي تيست ** | اختبار قاعدة البيانات |
| **حاويات الاختبار** | اختبارات قاعدة البيانات المستندة إلى Docker |
| **سقلفلوف** | فحص SQL |
| ** مخطط ** | فحص المخطط |
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

## فحص وتنسيق SQL
| أداة | الغرض |
|------|---------|
| **SQLFluff** | لينتر وفورماتر |
| **منسق SQL** | تنسيق SQL |
| ** نعيق ** | ترحيل PostgreSQL linter |
| **psql2go** | SQL لتحويل الذهاب |
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

## مفاهيم SQL الأساسية
| المفهوم | الوصف |
|---------|------------|
| **الحمض** | الذرية، الاتساق، العزلة، المتانة |
| **التطبيع** | 1NF، 2NF، 3NF، BCNF |
| **الفهارس** | بي تري، هاش، جين، جيست، برين |
| **المعاملات** | البدء والالتزام والتراجع |
| ** الانضمامات ** | الداخلية، اليسار، اليمين، الكامل، الصليب |
| ** وظائف النافذة ** | ROW_NUMBER، الرتبة، التأخر، الرصاص |
| ** CTEs ** | مع الاستعلامات العودية |
| **المشاهدات** | الجداول الافتراضية |
| **المشغلات** | الإجراءات التلقائية |
| **الإجراءات المخزنة** | كود SQL القابل لإعادة الاستخدام |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| ** عامل الميناء ** | الصور الرسمية (postgres، mysql) |
| **الخدمات المدارة** | RDS، Cloud SQL، Azure SQL |
| **Flyway / Liquibase** | ترحيل المخطط |
| **pg_dump / mysqldump** | النسخ الاحتياطية |
| **WAL-E / pgBackRest** | النسخ الاحتياطية PostgreSQL |
| ** مشغلي Kubernetes ** | CloudNativePG، فيتيس |
---

## ملخص
يمتد النظام البيئي لـ SQL إلى العشرات من محركات قواعد البيانات ومئات الأدوات. المكدس القياسي هو: **PostgreSQL** كقاعدة البيانات الافتراضية (مفتوحة المصدر الأكثر ثراءً بالميزات)، **MySQL** لتطبيقات الويب، **SQLite** للاستخدام المضمن، **Flyway** أو **Liquibase** لعمليات الترحيل، **DBeaver** أو **DataGrip** كواجهة مستخدم رسومية، **SQLFluff** للفحص، و**شرح التحليل** لضبط الأداء. يستخدم تطوير SQL الحديث أنظمة ORM آمنة للنوع مثل **Prisma** (TypeScript) أو **SQLAlchemy** (Python) أو **sqlc** (Go) لإنشاء تعليمات برمجية من SQL. تظل SQL هي اللغة العالمية للبيانات، وهي ضرورية في كل حزمة تقنية.