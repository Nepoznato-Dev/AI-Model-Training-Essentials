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
# SQL — 생태계 및 도구 가이드
이 가이드에서는 SQL 생태계의 필수 데이터베이스, 도구 및 인프라를 다룹니다.
---

## 데이터베이스 시스템
### 관계형(OLTP)
| 데이터베이스 | 유형 | 최고의 대상 |
|----------|------|----------|
| **PostgreSQL** | 오픈 소스 | 기능이 가장 풍부하고 확장 가능 |
| **MySQL/마리아DB** | 오픈 소스 | 웹 애플리케이션 |
| **SQLite** | 임베디드 | 모바일, 데스크탑, 소형 앱 |
| **SQL 서버** | 상업용 | 엔터프라이즈(마이크로소프트) |
| **오라클** | 상업용 | 대기업 |
| **DB2** | 상업용 | IBM 엔터프라이즈 |
| **바퀴벌레DB** | 분산 | 클라우드 네이티브, PostgreSQL 호환 |
| **TiDB** | 분산 | MySQL 호환, HTAP |
| **유가바이트DB** | 분산 | PostgreSQL 호환 |
### 분석(OLAP)
| 데이터베이스 | 유형 | 최고의 대상 |
|----------|------|----------|
| **클릭하우스** | 기둥형 | 실시간 분석 |
| **DuckDB** | 임베디드 | 진행 중인 분석 |
| **눈송이** | 클라우드 | 데이터 웨어하우스 |
| **빅쿼리** | 클라우드 | 구글 분석 |
| **적색편이** | 클라우드 | AWS 분석 |
| **아파치 드루이드** | 기둥형 | 시계열 분석 |
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

## 마이그레이션 도구
| 도구 | 유형 | 메모 |
|------|------|-------|
| **이동 경로** | 자바 기반 | 간단한 SQL 마이그레이션 |
| **리퀴베이스** | XML/SQL/YAML | 엔터프라이즈급 |
| **알렘빅** | 파이썬 | SQLAlchemy 마이그레이션 |
| **Prisma 마이그레이션** | 타입스크립트 | 유형이 안전한 마이그레이션 |
| **golang-마이그레이션** | 이동 | 데이터베이스 마이그레이션 |
| **아틀라스** | 현대 | 코드형 스키마 |
| **DB메이트** | 다중DB | 간단한 CLI |
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

## 쿼리 빌더 및 ORM
| 도구 | 언어 | 유형 |
|------|----------|------|
| **프리즈마** | 타입스크립트 | 유형이 안전한 ORM |
| **이슬비** | 타입스크립트 | 유형이 안전한 SQL |
| **시퀀라이즈** | 자바스크립트 | 전체 ORM |
| **Knex.js** | 자바스크립트 | 쿼리 빌더 |
| **SQLAlchemy** | 파이썬 | 전체 ORM + 코어 |
| **장고 ORM** | 파이썬 | 전체 ORM |
| **오줌** | 파이썬 | 경량 ORM |
| **웅변** | PHP(라라벨) | 액티브 레코드 ORM |
| **교리** | PHP(심포니) | 데이터 매퍼 ORM |
| **엔티티 프레임워크** | C# | 전체 ORM |
| **멋쟁이** | C# | 마이크로ORM |
| **최대 절전 모드** | 자바 | 전체 ORM |
| **jOOQ** | 자바 | 유형이 안전한 SQL |
| **고름** | 이동 | 전체 ORM |
| **sqlc** | 이동 | SQL에서 Go 생성 |
| **디젤** | 녹 | 유형이 안전한 ORM |
| **SQLx** | 녹 | 비동기 SQL |
| **SeaORM** | 녹 | 비동기 ORM |
---

## GUI 및 IDE 도구
| 도구 | 유형 | 메모 |
|------|------|-------|
| **디비버** | 유니버설 | 무료 다중 데이터베이스 |
| **DataGrip** | 제트브레인즈 | 최고의 SQL IDE |
| **pgAdmin** | 포스트그레SQL | 웹 기반 관리자 |
| **MySQL 워크벤치** | MySQL | 공식 도구 |
| **하이디SQL** | 윈도우 | 경량 |
| **테이블플러스** | 현대 | 아름다운 UI |
| **양봉 스튜디오** | 오픈 소스 | 전자 기반 |
| **psql** | CLI | PostgreSQL 터미널 |
| **mysql** | CLI | MySQL 터미널 |
| **sqlite3** | CLI | SQLite 터미널 |
---

## 성능 및 분석
| 도구 | 목적 |
|------|---------|
| **분석 설명** | 쿼리 실행 계획 |
| **pg_stat_statements** | PostgreSQL 쿼리 통계 |
| **설명** | 실행 계획(MySQL) |
| **프로필 보기** | MySQL 프로파일링 |
| **SQL Server 프로파일러** | SQL Server 프로파일링 |
| **pgBadger** | PostgreSQL 로그 분석기 |
| **pt-쿼리-다이제스트** | MySQL 쿼리 분석 |
| **sys 조회수** | MySQL 시스템 보기 |
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

## 테스트
| 도구 | 목적 |
|------|---------|
| **tSQLt** | SQL Server 단위 테스트 |
| **pgTAP** | PostgreSQL 테스트 |
| **utPLSQL** | 오라클 테스트 |
| **db테스트** | 데이터베이스 테스트 |
| **테스트컨테이너** | Docker 기반 DB 테스트 |
| **sqlfluff** | SQL 린팅 |
| **스키마린트** | 스키마 린트 |
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

## SQL 린팅 및 서식 지정
| 도구 | 목적 |
|------|---------|
| **SQL플러프** | 린터 및 포맷터 |
| **SQL 포맷터** | SQL 형식화 |
| **삐걱거리는 소리** | PostgreSQL 마이그레이션 린터 |
| **psql2go** | SQL-Go 변환기 |
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

## 주요 SQL 개념
| 개념 | 설명 |
|---------|-------------|
| **산** | 원자성, 일관성, 격리성, 내구성 |
| **정규화** | 1NF, 2NF, 3NF, BCNF |
| **색인** | B-트리, 해시, GIN, GiST, BRIN |
| **거래** | 시작, 커밋, 롤백 |
| **조인** | 내부, 왼쪽, 오른쪽, 전체, 십자가 |
| **창 기능** | ROW_NUMBER, 순위, LAG, 리드 |
| **CTE** | WITH, 재귀 쿼리 |
| **조회수** | 가상 테이블 |
| **트리거** | 자동 조치 |
| **저장 프로시저** | 재사용 가능한 SQL 코드 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **도커** | 공식 이미지(postgres, mysql) |
| **관리형 서비스** | RDS, 클라우드 SQL, Azure SQL |
| **이동경로/Liquibase** | 스키마 마이그레이션 |
| **pg_dump / mysqldump** | 백업 |
| **WAL-E / pgBackRest** | PostgreSQL 백업 |
| **Kubernetes 운영자** | CloudNativePG, 비테스 |
---

## 요약
SQL 생태계는 수십 개의 데이터베이스 엔진과 수백 개의 도구로 구성되어 있습니다. 표준 스택은 기본 데이터베이스(가장 풍부한 기능을 갖춘 오픈 소스)인 **PostgreSQL**, 웹 애플리케이션용 **MySQL**, 임베디드용 **SQLite**, 마이그레이션용 **Flyway** 또는 **Liquibase**, GUI용 **DBeaver** 또는 **DataGrip**, Linting용 **SQLFluff**, 성능 튜닝용 **EXPLAIN ANALYZE**입니다. 최신 SQL 개발에서는 **Prisma**(TypeScript), **SQLAlchemy**(Python) 또는 **sqlc**(Go)와 같은 유형이 안전한 ORM을 사용하여 SQL에서 코드를 생성합니다. SQL은 모든 기술 스택에 필수적인 데이터의 범용 언어로 남아 있습니다.