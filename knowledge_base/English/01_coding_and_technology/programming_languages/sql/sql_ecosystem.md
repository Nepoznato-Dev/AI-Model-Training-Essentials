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
# SQL — Ecosystem & Tooling Guide

This guide covers the essential databases, tools, and infrastructure in the SQL ecosystem.

---

## Database Systems

### Relational (OLTP)

| Database | Type | Best For |
|----------|------|----------|
| **PostgreSQL** | Open-source | Most feature-rich, extensible |
| **MySQL / MariaDB** | Open-source | Web applications |
| **SQLite** | Embedded | Mobile, desktop, small apps |
| **SQL Server** | Commercial | Enterprise (Microsoft) |
| **Oracle** | Commercial | Large enterprise |
| **DB2** | Commercial | IBM enterprise |
| **CockroachDB** | Distributed | Cloud-native, PostgreSQL-compatible |
| **TiDB** | Distributed | MySQL-compatible, HTAP |
| **YugabyteDB** | Distributed | PostgreSQL-compatible |

### Analytical (OLAP)

| Database | Type | Best For |
|----------|------|----------|
| **ClickHouse** | Columnar | Real-time analytics |
| **DuckDB** | Embedded | In-process analytics |
| **Snowflake** | Cloud | Data warehouse |
| **BigQuery** | Cloud | Google analytics |
| **Redshift** | Cloud | AWS analytics |
| **Apache Druid** | Columnar | Time-series analytics |

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

## Migration Tools

| Tool | Type | Notes |
|------|------|-------|
| **Flyway** | Java-based | Simple, SQL migrations |
| **Liquibase** | XML/SQL/YAML | Enterprise-grade |
| **Alembic** | Python | SQLAlchemy migrations |
| **Prisma Migrate** | TypeScript | Type-safe migrations |
| **golang-migrate** | Go | Database migrations |
| **Atlas** | Modern | Schema-as-code |
| **dbmate** | Multi-DB | Simple CLI |

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

| Tool | Language | Type |
|------|----------|------|
| **Prisma** | TypeScript | Type-safe ORM |
| **Drizzle** | TypeScript | Type-safe SQL |
| **Sequelize** | JavaScript | Full ORM |
| **Knex.js** | JavaScript | Query builder |
| **SQLAlchemy** | Python | Full ORM + Core |
| **Django ORM** | Python | Full ORM |
| **peewee** | Python | Lightweight ORM |
| **Eloquent** | PHP (Laravel) | Active Record ORM |
| **Doctrine** | PHP (Symfony) | Data Mapper ORM |
| **Entity Framework** | C# | Full ORM |
| **Dapper** | C# | Micro-ORM |
| **Hibernate** | Java | Full ORM |
| **jOOQ** | Java | Type-safe SQL |
| **GORM** | Go | Full ORM |
| **sqlc** | Go | Generate Go from SQL |
| **Diesel** | Rust | Type-safe ORM |
| **SQLx** | Rust | Async SQL |
| **SeaORM** | Rust | Async ORM |

---

## GUI & IDE Tools

| Tool | Type | Notes |
|------|------|-------|
| **DBeaver** | Universal | Free, multi-database |
| **DataGrip** | JetBrains | Best SQL IDE |
| **pgAdmin** | PostgreSQL | Web-based admin |
| **MySQL Workbench** | MySQL | Official tool |
| **HeidiSQL** | Windows | Lightweight |
| **TablePlus** | Modern | Beautiful UI |
| **Beekeeper Studio** | Open-source | Electron-based |
| **psql** | CLI | PostgreSQL terminal |
| **mysql** | CLI | MySQL terminal |
| **sqlite3** | CLI | SQLite terminal |

---

## Performance & Analysis

| Tool | Purpose |
|------|---------|
| **EXPLAIN ANALYZE** | Query execution plan |
| **pg_stat_statements** | PostgreSQL query stats |
| **EXPLAIN** | Execution plan (MySQL) |
| **SHOW PROFILE** | MySQL profiling |
| **SQL Server Profiler** | SQL Server profiling |
| **pgBadger** | PostgreSQL log analyzer |
| **pt-query-digest** | MySQL query analysis |
| **sys views** | MySQL system views |

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

## Testing

| Tool | Purpose |
|------|---------|
| **tSQLt** | SQL Server unit testing |
| **pgTAP** | PostgreSQL testing |
| **utPLSQL** | Oracle testing |
| **dbtest** | Database testing |
| **testcontainers** | Docker-based DB tests |
| **sqlfluff** | SQL linting |
| **schemalint** | Schema linting |

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

| Tool | Purpose |
|------|---------|
| **SQLFluff** | Linter and formatter |
| **sql-formatter** | SQL formatting |
| **squawk** | PostgreSQL migration linter |
| **psql2go** | SQL to Go converter |

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

## Key SQL Concepts

| Concept | Description |
|---------|-------------|
| **ACID** | Atomicity, Consistency, Isolation, Durability |
| **Normalization** | 1NF, 2NF, 3NF, BCNF |
| **Indexes** | B-tree, Hash, GIN, GiST, BRIN |
| **Transactions** | BEGIN, COMMIT, ROLLBACK |
| **Joins** | INNER, LEFT, RIGHT, FULL, CROSS |
| **Window functions** | ROW_NUMBER, RANK, LAG, LEAD |
| **CTEs** | WITH, recursive queries |
| **Views** | Virtual tables |
| **Triggers** | Automatic actions |
| **Stored procedures** | Reusable SQL code |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Docker** | Official images (postgres, mysql) |
| **Managed services** | RDS, Cloud SQL, Azure SQL |
| **Flyway / Liquibase** | Schema migrations |
| **pg_dump / mysqldump** | Backups |
| **WAL-E / pgBackRest** | PostgreSQL backups |
| **Kubernetes operators** | CloudNativePG, Vitess |

---

## Summary

SQL's ecosystem spans dozens of database engines and hundreds of tools. The standard stack is: **PostgreSQL** as the default database (most feature-rich open-source), **MySQL** for web applications, **SQLite** for embedded use, **Flyway** or **Liquibase** for migrations, **DBeaver** or **DataGrip** as GUI, **SQLFluff** for linting, and **EXPLAIN ANALYZE** for performance tuning. Modern SQL development uses type-safe ORMs like **Prisma** (TypeScript), **SQLAlchemy** (Python), or **sqlc** (Go) to generate code from SQL. SQL remains the universal language for data, essential in every technology stack.
