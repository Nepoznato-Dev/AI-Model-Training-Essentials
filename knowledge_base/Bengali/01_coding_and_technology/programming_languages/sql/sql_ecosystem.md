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
# SQL — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকা এসকিউএল ইকোসিস্টেমের প্রয়োজনীয় ডাটাবেস, টুলস এবং অবকাঠামো কভার করে।
---

## ডাটাবেস সিস্টেম
### রিলেশনাল (OLTP)
| ডাটাবেস | প্রকার | জন্য সেরা |
|----------|------|----------|
| **PostgreSQL** | ওপেন সোর্স | সর্বাধিক বৈশিষ্ট্য সমৃদ্ধ, এক্সটেনসিবল |
| **MySQL / MariaDB** | ওপেন সোর্স | ওয়েব অ্যাপ্লিকেশন |
| **SQLite** | এমবেডেড | মোবাইল, ডেস্কটপ, ছোট অ্যাপস |
| **এসকিউএল সার্ভার** | বাণিজ্যিক | এন্টারপ্রাইজ (মাইক্রোসফ্ট) |
| **ওরাকল** | বাণিজ্যিক | বড় এন্টারপ্রাইজ |
| **DB2** | বাণিজ্যিক | IBM এন্টারপ্রাইজ |
| **তেলাপোকাDB** | বিতরণ করা | ক্লাউড-নেটিভ, PostgreSQL-সামঞ্জস্যপূর্ণ |
| **TiDB** | বিতরণ করা | MySQL- সামঞ্জস্যপূর্ণ, HTAP |
| **ইউগাবাইটডিবি** | বিতরণ করা | PostgreSQL-সামঞ্জস্যপূর্ণ |
### বিশ্লেষণাত্মক (OLAP)
| ডাটাবেস | প্রকার | জন্য সেরা |
|----------|------|----------|
| **ক্লিক হাউস** | কলামার | রিয়েল-টাইম বিশ্লেষণ |
| **ডাকডিবি** | এমবেডেড | ইন-প্রসেস বিশ্লেষণ |
| **তুষারকণা** | মেঘ | তথ্য গুদাম |
| **BigQuery** | মেঘ | Google বিশ্লেষণ |
| **রেডশিফ্ট** | মেঘ | AWS বিশ্লেষণ |
| **Apache Druid** | কলামার | সময়-সিরিজ বিশ্লেষণ |
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

## মাইগ্রেশন টুল
| টুল | প্রকার | নোট |
|------|------|-------|
| **ফ্লাইওয়ে** | জাভা ভিত্তিক | সহজ, SQL মাইগ্রেশন |
| **লিকুইবেস** | XML/SQL/YAML | এন্টারপ্রাইজ-গ্রেড |
| **অ্যালেম্বিক** | পাইথন | SQLAlchemy মাইগ্রেশন |
| **প্রিজমা মাইগ্রেট** | টাইপস্ক্রিপ্ট | টাইপ-নিরাপদ মাইগ্রেশন |
| **গোলাং-মাইগ্রেট** | যান | ডাটাবেস মাইগ্রেশন |
| **এটলাস** | আধুনিক | কোড হিসাবে স্কিমা |
| **dbmate** | মাল্টি-ডিবি | সহজ CLI |
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

## ক্যোয়ারী নির্মাতা এবং ORMs
| টুল | ভাষা | প্রকার |
|------|------------|------|
| **প্রিজমা** | টাইপস্ক্রিপ্ট | টাইপ-সেফ ORM |
| **গুঁড়ি গুঁড়ি* | টাইপস্ক্রিপ্ট | টাইপ-নিরাপদ SQL |
| **সিক্যুয়ালাইজ** | জাভাস্ক্রিপ্ট | সম্পূর্ণ ORM |
| **Knex.js** | জাভাস্ক্রিপ্ট | কোয়েরি নির্মাতা |
| **এসকিউএলকেমি** | পাইথন | সম্পূর্ণ ORM + কোর |
| **জ্যাঙ্গো ওআরএম** | পাইথন | সম্পূর্ণ ORM |
| **পিউই** | পাইথন | লাইটওয়েট ORM |
| **বক্তা** | পিএইচপি (লারাভেল) | সক্রিয় রেকর্ড ORM |
| ** মতবাদ** | পিএইচপি (সিমফনি) | ডেটা ম্যাপার ORM |
| **সত্তা ফ্রেমওয়ার্ক** | C# | সম্পূর্ণ ORM |
| **ডপার** | C# | মাইক্রো-ORM |
| **হাইবারনেট** | জাভা | সম্পূর্ণ ORM |
| **jOOQ** | জাভা | টাইপ-নিরাপদ SQL |
| **GORM** | যান | সম্পূর্ণ ORM |
| **sqlc** | যান | এসকিউএল থেকে গো জেনারেট করুন |
| **ডিজেল** | মরিচা | টাইপ-সেফ ORM |
| **SQLx** | মরিচা | Async SQL |
| **SeaORM** | মরিচা | Async ORM |
---

## GUI এবং IDE টুল
| টুল | প্রকার | নোট |
|------|------|-------|
| **DBeaver** | সর্বজনীন | বিনামূল্যে, মাল্টি-ডাটাবেস |
| **ডেটাগ্রিপ** | JetBrains | সেরা SQL IDE |
| **পিজিএডমিন** | PostgreSQL | ওয়েব ভিত্তিক অ্যাডমিন |
| **মাইএসকিউএল ওয়ার্কবেঞ্চ** | মাইএসকিউএল | অফিসিয়াল টুল |
| **হেইডিএসকিউএল** | উইন্ডোজ | লাইটওয়েট |
| **টেবিলপ্লাস** | আধুনিক | সুন্দর UI |
| **মৌমাছি পালন স্টুডিও** | ওপেন সোর্স | ইলেকট্রন ভিত্তিক |
| **psql** | CLI | PostgreSQL টার্মিনাল |
| **mysql** | CLI | মাইএসকিউএল টার্মিনাল |
| **sqlite3** | CLI | SQLite টার্মিনাল |
---

## কর্মক্ষমতা এবং বিশ্লেষণ
| টুল | উদ্দেশ্য |
|------|---------|
| **বিশ্লেষণ ব্যাখ্যা করুন** | ক্যোয়ারী এক্সিকিউশন প্ল্যান |
| **pg_stat_statements** | PostgreSQL ক্যোয়ারী পরিসংখ্যান |
| **ব্যাখ্যা করুন** | এক্সিকিউশন প্ল্যান (MySQL) |
| **প্রোফাইল দেখান** | MySQL প্রোফাইলিং |
| **এসকিউএল সার্ভার প্রোফাইলার** | SQL সার্ভার প্রোফাইলিং |
| **pgBadger** | PostgreSQL লগ বিশ্লেষক |
| **pt-query-digest** | MySQL ক্যোয়ারী বিশ্লেষণ |
| **sys ভিউ** | মাইএসকিউএল সিস্টেম ভিউ |
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

## পরীক্ষা
| টুল | উদ্দেশ্য |
|------|---------|
| **tSQLt** | SQL সার্ভার ইউনিট টেস্টিং |
| **pgTAP** | PostgreSQL পরীক্ষা |
| **utPLSQL** | ওরাকল টেস্টিং |
| **dbtest** | ডাটাবেস টেস্টিং |
| **পরীক্ষার পাত্র** | ডকার-ভিত্তিক ডিবি পরীক্ষা |
| **sqlfluff** | এসকিউএল লিন্টিং |
| **স্কিমলিন্ট** | স্কিমা লিন্টিং |
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

## এসকিউএল লিন্টিং এবং ফরম্যাটিং
| টুল | উদ্দেশ্য |
|------|---------|
| **SQLFluff** | লিন্টার এবং ফরম্যাটার |
| **sql-ফরম্যাটার** | এসকিউএল ফরম্যাটিং |
| **স্কোয়াক** | PostgreSQL মাইগ্রেশন লিন্টার |
| **psql2go** | এসকিউএল টু গো কনভার্টার |
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

## মূল এসকিউএল ধারণা
| ধারণা | বর্ণনা |
|---------|---------------|
| **এসিড** | পারমাণবিকতা, ধারাবাহিকতা, বিচ্ছিন্নতা, স্থায়িত্ব |
| **স্বাভাবিককরণ** | 1NF, 2NF, 3NF, BCNF |
| **সূচী** | বি-ট্রি, হ্যাশ, জিআইএন, জিএসটি, ব্রিন |
| **লেনদেন** | শুরু করুন, কমিট করুন, রোলব্যাক করুন |
| **যোগ দেয়** | ভিতরের, বাম, ডান, পূর্ণ, ক্রস |
| **উইন্ডো ফাংশন** | ROW_NUMBER, RANK, LAG, LEAD |
| **CTEs** | সঙ্গে, পুনরাবৃত্তিমূলক প্রশ্ন |
| **দর্শন** | ভার্চুয়াল টেবিল |
| **ট্রিগার** | স্বয়ংক্রিয় ক্রিয়া |
| **সংরক্ষিত পদ্ধতি** | পুনঃব্যবহারযোগ্য SQL কোড |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **ডকার** | অফিসিয়াল ছবি (পোস্টগ্রেস, মাইএসকিউএল) |
| **পরিচালিত পরিষেবা** | RDS, ক্লাউড SQL, Azure SQL |
| **ফ্লাইওয়ে / লিকুইবেস** | স্কিমা মাইগ্রেশন |
| **pg_dump / mysqldump** | ব্যাকআপ |
| **WAL-E / pgBackRest** | PostgreSQL ব্যাকআপ |
| **কুবারনেটস অপারেটর** | CloudNativePG, Vitess |
---

## সারাংশ
এসকিউএল-এর ইকোসিস্টেম কয়েক ডজন ডাটাবেস ইঞ্জিন এবং শত শত টুল বিস্তৃত। স্ট্যান্ডার্ড স্ট্যাক হল: **PostgreSQL** ডিফল্ট ডাটাবেস হিসেবে (সবচেয়ে বৈশিষ্ট্য সমৃদ্ধ ওপেন সোর্স), **MySQL** ওয়েব অ্যাপ্লিকেশনের জন্য, **SQLite** এমবেডেড ব্যবহারের জন্য, **ফ্লাইওয়ে** বা **লিকুইবেস** মাইগ্রেশনের জন্য, **DBeaver** বা **ডেটাগ্রিপ**, GUILT** এবং GUILT** এর জন্য পারফরম্যান্স টিউনিংয়ের জন্য **বিশ্লেষণ ব্যাখ্যা করুন। আধুনিক SQL ডেভেলপমেন্ট SQL থেকে কোড তৈরি করতে **প্রিজমা** (টাইপস্ক্রিপ্ট), **SQLAlchemy** (পাইথন), বা **sqlc** (Go) এর মতো টাইপ-সেফ ORM ব্যবহার করে। এসকিউএল ডেটার জন্য সার্বজনীন ভাষা হিসাবে রয়ে গেছে, প্রতিটি প্রযুক্তি স্ট্যাকের জন্য অপরিহার্য।