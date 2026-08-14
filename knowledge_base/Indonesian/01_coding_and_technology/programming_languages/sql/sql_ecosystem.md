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
# SQL — Panduan Ekosistem & Peralatan
Panduan ini mencakup database, alat, dan infrastruktur penting dalam ekosistem SQL.
---

## Sistem Basis Data
### Relasional (OLTP)
| Basis Data | Ketik | Terbaik Untuk |
|----------|------|----------|
| **PostgreSQL** | Sumber terbuka | Paling kaya fitur, dapat diperluas |
| **MySQL/MariaDB** | Sumber terbuka | Aplikasi web |
| **SQLite** | Tertanam | Seluler, desktop, aplikasi kecil |
| **Server SQL** | Komersial | Perusahaan (Microsoft) |
| **Peramal** | Komersial | Perusahaan besar |
| **DB2** | Komersial | Perusahaan IBM |
| **KecoaDB** | Didistribusikan | Cloud-native, kompatibel dengan PostgreSQL |
| **TiDB** | Didistribusikan | Kompatibel dengan MySQL, HTAP |
| **YugabyteDB** | Didistribusikan | Kompatibel dengan PostgreSQL |
### Analitis (OLAP)
| Basis Data | Ketik | Terbaik Untuk |
|----------|------|----------|
| **KlikRumah** | Kolom | Analisis waktu nyata |
| **BebekDB** | Tertanam | Analisis dalam proses |
| **Kepingan Salju** | Awan | Gudang data |
| **BigQuery** | Awan | Analisis Google |
| **Pergeseran Merah** | Awan | Analisis AWS |
| **Apache Druid** | Kolom | Analisis deret waktu |
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

## Alat Migrasi
| Alat | Ketik | Catatan |
|------|------|-------|
| **Jalur Terbang** | Berbasis Java | Sederhana, migrasi SQL |
| **Liquibase** | XML/SQL/YAML | Tingkat perusahaan |
| **Alembik** | ular piton | Migrasi SQLAlchemy |
| **Prisma Bermigrasi** | Skrip Ketik | Migrasi tipe-aman |
| **golang-migrasi** | Pergi | Migrasi basis data |
| **Atlas** | Modern | Skema-sebagai-kode |
| **teman db** | Multi-DB | CLI sederhana |
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

## Pembuat Kueri & ORM
| Alat | Bahasa | Ketik |
|------|----------|------|
| **Prisma** | Skrip Ketik | ORM yang aman untuk tipe |
| **Gerimis** | Skrip Ketik | SQL yang aman untuk mengetik |
| **Sekuel** | JavaScript | ORM penuh |
| **Knex.js** | JavaScript | Pembuat kueri |
| **SQLAlkimia** | ular piton | ORM Penuh + Inti |
| **Django ORM** | ular piton | ORM penuh |
| **peewee** | ular piton | ORM Ringan |
| **Fasih** | PHP (Laravel) | Catatan Aktif ORM |
| **Doktrin** | PHP (Simfoni) | ORM Pemeta Data |
| **Kerangka Entitas** | C#| ORM penuh |
| **Necis** | C#| Mikro-ORM |
| **Hibernasi** | Jawa | ORM penuh |
| **jOOQ** | Jawa | SQL yang aman untuk mengetik |
| **GORM** | Pergi | ORM penuh |
| **sqlc** | Pergi | Hasilkan Go dari SQL |
| **Diesel** | Karat | ORM yang aman untuk tipe |
| **SQLx** | Karat | SQL asinkron |
| **ORM Laut** | Karat | ORM Asinkron |
---

## Alat GUI & IDE
| Alat | Ketik | Catatan |
|------|------|-------|
| **Berang-berang** | Universal | Gratis, multi-database |
| **Pegangan Data** | Otak Jet | IDE SQL Terbaik |
| **pgAdmin** | PostgreSQL | Admin berbasis web |
| **Meja Kerja MySQL** | MySQL | Alat resmi |
| **HeidiSQL** | jendela | Ringan |
| **MejaPlus** | Modern | UI yang indah |
| **Studio Peternak Lebah** | Sumber terbuka | Berbasis elektron |
| **psql** | CLI | Terminal PostgreSQL |
| **mysql** | CLI | Terminal MySQL |
| **sqlite3** | CLI | Terminal SQLite |
---

## Performa & Analisis
| Alat | Tujuan |
|------|---------|
| **JELASKAN ANALISIS** | Rencana eksekusi kueri |
| **pg_stat_statement** | Statistik kueri PostgreSQL |
| **JELASKAN** | Rencana eksekusi (MySQL) |
| **TAMPILKAN PROFIL** | Pembuatan profil MySQL |
| **Profil Server SQL** | Pembuatan profil SQL Server |
| **pgBadger** | Penganalisis log PostgreSQL |
| **pt-query-digest** | Analisis kueri MySQL |
| **tampilan sistem** | Tampilan sistem MySQL |
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

## Pengujian
| Alat | Tujuan |
|------|---------|
| **tSQLt** | Pengujian unit SQL Server |
| **pgTAP** | Pengujian PostgreSQL |
| **utPLSQL** | Pengujian Oracle |
| **ujian terbaik** | Pengujian basis data |
| **wadah uji** | Tes DB berbasis Docker |
| **sqlfluff** | SQL linting |
| **skema** | Linting skema |
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

## SQL Linting & Pemformatan
| Alat | Tujuan |
|------|---------|
| **SQLFluff** | Linter dan pemformat |
| **pemformat sql** | Pemformatan SQL |
| **berkotek** | Linter migrasi PostgreSQL |
| **psql2pergi** | Konverter SQL ke Go |
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

## Konsep Kunci SQL
| Konsep | Deskripsi |
|---------|-------------|
| **ASAM** | Atomisitas, Konsistensi, Isolasi, Daya Tahan |
| **Normalisasi** | 1NF, 2NF, 3NF, BCNF |
| **Indeks** | B-pohon, Hash, GIN, GiST, BRIN |
| **Transaksi** | MULAI, KOMITMEN, KEMBALIKAN |
| **Bergabung** | DALAM, KIRI, KANAN, PENUH, SILANG |
| **Fungsi jendela** | ROW_NUMBER, PERINGKAT, LAG, LEAD |
| **CTE** | DENGAN, kueri rekursif |
| **Tampilan** | Tabel virtual |
| **Pemicu** | Tindakan otomatis |
| **Prosedur tersimpan** | Kode SQL yang dapat digunakan kembali |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Buruh pelabuhan** | Gambar resmi (postgres, mysql) |
| **Layanan terkelola** | RDS, Cloud SQL, Azure SQL |
| **Jalur Terbang / Liquibase** | Migrasi skema |
| **pg_dump / mysqldump** | Cadangan |
| **WAL-E / pgBackRest** | Pencadangan PostgreSQL |
| **Operator Kubernetes** | CloudNativePG, Vitess |
---

## Ringkasan
Ekosistem SQL mencakup lusinan mesin basis data dan ratusan alat. Tumpukan standarnya adalah: **PostgreSQL** sebagai database default (sumber terbuka paling kaya fitur), **MySQL** untuk aplikasi web, **SQLite** untuk penggunaan tertanam, **Flyway** atau **Liquibase** untuk migrasi, **DBeaver** atau **DataGrip** sebagai GUI, **SQLFluff** untuk linting, dan **EXPLAIN ANALYZE** untuk penyesuaian performa. Pengembangan SQL modern menggunakan ORM yang aman untuk tipe seperti **Prisma** (TypeScript), **SQLAlchemy** (Python), atau **sqlc** (Go) untuk menghasilkan kode dari SQL. SQL tetap menjadi bahasa universal untuk data, penting dalam setiap rangkaian teknologi.