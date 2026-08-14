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
# SQL — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe bazy danych, narzędzia i infrastrukturę w ekosystemie SQL.
---

## Systemy baz danych
### Relacyjny (OLTP)
| Baza danych | Wpisz | Najlepsze dla |
|---------|------|---------|
| **PostgreSQL** | Otwarte oprogramowanie | Najbardziej bogate w funkcje, rozszerzalne |
| **MySQL / MariaDB** | Otwarte oprogramowanie | Aplikacje internetowe |
| **SQLite** | Wbudowany | Mobilne, stacjonarne, małe aplikacje |
| **Serwer SQL** | Komercyjne | Przedsiębiorstwo (Microsoft) |
| **Wyrocznia** | Komercyjne | Duże przedsiębiorstwo |
| **DB2** | Komercyjne | Przedsiębiorstwo IBM |
| **KaraluchDB** | Rozproszone | Natywny dla chmury, kompatybilny z PostgreSQL |
| **TiDB** | Rozproszone | Kompatybilny z MySQL, HTAP |
| **YugabyteDB** | Rozproszone | Kompatybilny z PostgreSQL |
### Analityczne (OLAP)
| Baza danych | Wpisz | Najlepsze dla |
|---------|------|---------|
| **KliknijDom** | Kolumnowy | Analityka w czasie rzeczywistym |
| **DuckDB** | Wbudowany | Analityka wewnątrzprocesowa |
| **Płatek śniegu** | Chmura | Hurtownia danych |
| **BigQuery** | Chmura | Analityka Google |
| **Przesunięcie ku czerwieni** | Chmura | Analityka AWS |
| **Druid Apaczów** | Kolumnowy | Analiza szeregów czasowych |
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

## Narzędzia do migracji
| Narzędzie | Wpisz | Notatki |
|------|------|------|
| **Trasa przelotowa** | oparty na Javie | Proste, migracje SQL |
| **Likwibaza** | XML/SQL/YAML | Klasy korporacyjnej |
| **Alembik** | Pythona | Migracje SQLAlchemy |
| **Migracja Prisma** | TypeScript | Migracje bezpieczne dla typów |
| **golang-migracja** | Idź | Migracje baz danych |
| **Atlas** | Nowoczesne | Schemat jako kod |
| **dbmate** | Wielu DB | Prosty interfejs wiersza polecenia |
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

## Konstruktorzy zapytań i ORM
| Narzędzie | Język | Wpisz |
|------|----------|------|
| **Prisma** | TypeScript | Bezpieczny typ ORM |
| **Mżawka** | TypeScript | Bezpieczny typ SQL |
| **Sekwencja** | JavaScript | Pełny ORM |
| **Knex.js** | JavaScript | Kreator zapytań |
| **SQLAlchemia** | Pythona | Pełny ORM + rdzeń |
| **Django ORM** | Pythona | Pełny ORM |
| **peeee** | Pythona | Lekki ORM |
| **Wymowny** | PHP (Laravel) | Aktywny rekord ORM |
| **Doktryna** | PHP (Symfony) | ORM mapowania danych |
| **Struktura jednostki** | C# | Pełny ORM |
| **Wytworny** | C# | Mikro-ORM |
| **Hibernacja** | Jawa | Pełny ORM |
| **jOOQ** | Jawa | Bezpieczny typ SQL |
| **GORM** | Idź | Pełny ORM |
| **sqlc** | Idź | Wygeneruj Go z SQL |
| **Diesel** | Rdza | Bezpieczny typ ORM |
| **SQLx** | Rdza | Asynchroniczny SQL |
| **SeaORM** | Rdza | Asynchroniczny ORM |
---

## Narzędzia GUI i IDE
| Narzędzie | Wpisz | Notatki |
|------|------|------|
| **DBeaver** | Uniwersalny | Bezpłatny, wielobazowy |
| **Uchwyt danych** | JetBrains | Najlepsze IDE SQL |
| **pgAdmin** | PostgreSQL | Administrator sieciowy |
| **Środowisko pracy MySQL** | MySQL | Oficjalne narzędzie |
| **HeidiSQL** | Okna | Lekki |
| **StółPlus** | Nowoczesne | Piękny interfejs użytkownika |
| **Pszczelarnia** | Otwarte oprogramowanie | Oparte na elektronach |
| **psql** | Interfejs wiersza polecenia | Terminal PostgreSQL |
| **mysql** | Interfejs wiersza polecenia | Terminal MySQL |
| **sqlite3** | Interfejs wiersza polecenia | Terminal SQLite |
---

## Wydajność i analiza
| Narzędzie | Cel |
|------|-------------|
| **WYJAŚNIJ ANALIZĘ** | Plan wykonania zapytania |
| **pg_stat_statements** | Statystyki zapytań PostgreSQL |
| **WYJAŚNIJ** | Plan wykonania (MySQL) |
| **POKAŻ PROFIL** | Profilowanie MySQL |
| **Profil serwera SQL** | Profilowanie SQL Server |
| **pgBadger** | Analizator logów PostgreSQL |
| **streszczenie-pt-query** | Analiza zapytań MySQL |
| **widoki systemowe** | Widoki systemu MySQL |
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

## Testowanie
| Narzędzie | Cel |
|------|-------------|
| **tSQLt** | Testowanie jednostkowe SQL Server |
| **pgTAP** | Testowanie PostgreSQL |
| **utPLSQL** | Testowanie Oracle |
| **test db** | Testowanie baz danych |
| **kontenery testowe** | Testy DB oparte na Dockerze |
| **sqlfluff** | Linting SQL |
| **schemat** | Schemat lintingu |
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

## Linting i formatowanie SQL
| Narzędzie | Cel |
|------|-------------|
| **SQLFluff** | Linter i formater |
| **formatator sql** | Formatowanie SQL |
| **skrzeczenie** | Linter migracji PostgreSQL |
| **psql2go** | Konwerter SQL na Go |
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

## Kluczowe pojęcia SQL
| Koncepcja | Opis |
|--------|------------|
| **KWAS** | Atomowość, spójność, izolacja, trwałość |
| **Normalizacja** | 1NF, 2NF, 3NF, BCNF |
| **Indeksy** | B-drzewo, Hash, GIN, GiST, BRIN |
| **Transakcje** | ROZPOCZNIJ, ZATWIERDŹ, WYCOFNIJ |
| **Dołącza** | WEWNĘTRZNA, LEWA, PRAWA, PEŁNA, KRZYŻOWA |
| **Funkcje okna** | ROW_NUMBER, RANK, LAG, LEAD |
| **CTE** | Z, zapytania rekurencyjne |
| **Wyświetlenia** | Wirtualne stoły |
| **Wyzwalacze** | Akcje automatyczne |
| **Procedury składowane** | Kod SQL wielokrotnego użytku |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Doker** | Oficjalne obrazy (postgres, mysql) |
| **Usługi zarządzane** | RDS, Cloud SQL, Azure SQL |
| **Flyway / Liquibase** | Migracje schematów |
| **pg_dump / mysqldump** | Kopie zapasowe |
| **WAL-E / pgBackRest** | Kopie zapasowe PostgreSQL |
| **Operatorzy Kubernetes** | CloudNativePG, Vitess |
---

## Streszczenie
Ekosystem SQL obejmuje dziesiątki silników baz danych i setki narzędzi. Standardowy stos to: **PostgreSQL** jako domyślna baza danych (najbogatsza w funkcje open source), **MySQL** dla aplikacji internetowych, **SQLite** do zastosowań osadzonych, **Flyway** lub **Liquibase** do migracji, **DBeaver** lub **DataGrip** jako GUI, **SQLFluff** do lintingu i **EXPLAIN ANALYZE** do dostrajania wydajności. Współczesny rozwój języka SQL wykorzystuje bezpieczne typy ORM, takie jak **Prisma** (TypeScript), **SQLAlchemy** (Python) lub **sqlc** (Go), aby wygenerować kod z SQL. SQL pozostaje uniwersalnym językiem danych, niezbędnym w każdym stosie technologicznym.