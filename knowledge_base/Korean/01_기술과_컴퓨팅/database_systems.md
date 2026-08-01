<!-- 
This file was automatically translated from English to Korean.
Source: database_systems.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이터베이스 시스템

## 데이터베이스 기초

### 데이터베이스란?
데이터베이스는 구조화된 정보를 전자적으로 저장해 두고, 데이터를 효율적으로 조회·삽입·수정·삭제할 수 있도록 구성한 체계적인 집합입니다.

### 데이터베이스 관리 시스템 (DBMS)
DBMS는 최종 사용자, 애플리케이션, 데이터베이스 자체와 상호작용하며 데이터를 수집하고 분석하는 소프트웨어입니다. 예시: MySQL, PostgreSQL, Oracle, MongoDB.

### 핵심 개념
- **Schema**: 데이터베이스의 구조와 조직 방식(테이블, 필드, 관계)
- **Instance**: 특정 시점에 실제로 저장되어 있는 데이터
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability
- **CAP Theorem**: Consistency, Availability, Partition Tolerance 중 세 가지를 모두 동시에 완벽히 만족할 수 없다는 정리
- **Normalization**: 중복을 줄이기 위해 데이터를 체계적으로 조직하는 작업
- **Denormalization**: 읽기 성능 향상을 위해 일부 중복을 허용하는 작업

## 관계형 데이터베이스 (SQL)

### 핵심 개념
- **Tables**: 행(records)과 열(fields)로 구성된 구조
- **Primary Key**: 각 행을 고유하게 식별하는 키
- **Foreign Key**: 다른 테이블의 기본 키를 참조하는 키
- **Indexes**: 쿼리 속도를 높이는 데이터 구조
- **Views**: 쿼리 결과를 바탕으로 만든 가상 테이블
- **Stored Procedures**: 미리 컴파일된 SQL 코드 블록
- **Triggers**: 데이터 변경에 반응해 자동으로 실행되는 동작

### SQL 작업 (CRUD)
```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### 조인
- **INNER JOIN**: 두 테이블에서 조건이 일치하는 행만 반환합니다.
- **LEFT JOIN**: 왼쪽 테이블의 모든 행과 오른쪽 테이블의 일치하는 행을 반환합니다.
- **RIGHT JOIN**: 오른쪽 테이블의 모든 행과 왼쪽 테이블의 일치하는 행을 반환합니다.
- **FULL OUTER JOIN**: 두 테이블의 모든 행을 반환합니다.
- **CROSS JOIN**: 두 테이블의 카테시안 곱을 만듭니다.
- **SELF JOIN**: 하나의 테이블을 자기 자신과 조인합니다.

### 정규화 단계
- **1NF**: 값이 원자적이며 반복 그룹이 없습니다.
- **2NF**: 1NF를 만족하고, 부분 함수 종속이 없습니다(모든 비주요 속성이 전체 기본 키에 종속).
- **3NF**: 2NF를 만족하고, 이행 종속이 없습니다(비주요 속성이 다른 비주요 속성에 종속되지 않음).
- **BCNF**: 3NF보다 더 엄격하며, 모든 결정자가 후보 키입니다.
- **4NF**: 다치 종속이 없습니다.
- **5NF**: 조인 종속이 없습니다.

### 대표적인 RDBMS
- **PostgreSQL**: 고급 기능이 풍부하고 확장성이 높으며 ACID를 준수합니다.
- **MySQL**: 널리 사용되며 읽기 성능이 빠르고 웹 애플리케이션에 적합합니다.
- **Oracle**: 엔터프라이즈 기능과 확장성이 강력하지만 비용이 높습니다.
- **SQL Server**: Microsoft 생태계와 통합 도구에 강점이 있습니다.
- **SQLite**: 임베디드 환경에 적합한 서버리스 경량 데이터베이스입니다.
- **MariaDB**: MySQL에서 파생된 오픈소스 데이터베이스입니다.

## NoSQL 데이터베이스

### NoSQL 데이터베이스의 유형

#### 문서 저장소
- **구조**: JSON과 유사한 문서(BSON) 중심 구조
- **활용 사례**: 콘텐츠 관리, 카탈로그, 사용자 프로필
- **예시**: MongoDB, CouchDB, DocumentDB
- **쿼리 예시** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### 키-값 저장소
- **구조**: 단순한 키-값 쌍
- **활용 사례**: 캐싱, 세션, 장바구니
- **예시**: Redis, DynamoDB, Riak
- **특징**: 빠르고 단순하지만 질의 기능은 제한적입니다.

#### 컬럼 패밀리 저장소
- **구조**: 열을 패밀리 단위로 묶는 구조
- **활용 사례**: 빅데이터, 분석, 시계열 데이터
- **예시**: Cassandra, HBase, ScyllaDB
- **특징**: 쓰기 최적화, 분산 처리, 높은 확장성

#### 그래프 데이터베이스
- **구조**: 노드, 엣지, 속성으로 구성
- **활용 사례**: 소셜 네트워크, 사기 탐지, 추천 시스템
- **예시**: Neo4j, Amazon Neptune, ArangoDB
- **쿼리 언어**: Cypher (Neo4j), Gremlin

### NoSQL을 사용하는 경우
- 유연하거나 계속 변화하는 스키마가 필요할 때
- 수평 확장이 중요할 때
- 높은 쓰기 처리량이 필요할 때
- 계층형 또는 중첩 데이터가 많을 때
- 분산 시스템을 운영할 때
- 실시간 애플리케이션이 필요할 때

## 데이터베이스 설계

### 개체-관계 모델링
- **개체**: 객체나 개념(Customer, Product, Order)
- **속성**: 개체의 속성(name, price, date)
- **관계**: 개체 간 연결(one-to-one, one-to-many, many-to-many)
- **카디널리티**: 관계에 참여하는 인스턴스의 수

### 스키마 설계 패턴
- **단일 테이블 상속**: 타입 구분자와 함께 모든 유형을 하나의 테이블에 저장합니다.
- **클래스 테이블 상속**: 기본 클래스와 하위 클래스를 별도 테이블로 나눕니다.
- **구체 테이블 상속**: 각 구체 클래스마다 별도 테이블을 둡니다.
- **연결 테이블**: 다대다 관계를 해소합니다.
- **감사 테이블**: 변경 이력을 추적합니다(created_at, updated_at, deleted_at).

### 인덱싱 전략
- **B-Tree**: 기본 인덱스 형태로 범위 쿼리와 정렬에 적합합니다.
- **Hash**: 정확히 일치하는 값 조회에 적합합니다.
- **Bitmap**: 카디널리티가 낮은 컬럼(gender, status 등)에 적합합니다.
- **Full-Text**: 텍스트 검색 기능을 제공합니다.
- **Spatial**: 지리 데이터(GIS)에 사용됩니다.
- **Composite**: 여러 컬럼을 결합한 인덱스입니다.
- **Covering**: 쿼리에 필요한 컬럼을 모두 포함하는 인덱스입니다.

## 쿼리 최적화

### 실행 계획
- 데이터베이스가 쿼리를 어떻게 실행하는지 이해합니다.
- 병목 지점(전체 테이블 스캔, 누락된 인덱스 등)을 찾아냅니다.
- 도구: EXPLAIN, EXPLAIN ANALYZE

### 최적화 기법
- **인덱스 활용**: 쿼리가 적절한 인덱스를 사용하도록 합니다.
- **쿼리 재작성**: 복잡한 쿼리를 더 단순하게 다시 작성합니다.
- **조인 최적화**: 올바른 조인 유형과 순서를 선택합니다.
- **파티셔닝**: 큰 테이블을 분할합니다(range, hash, list).
- **머티리얼라이즈드 뷰**: 미리 계산된 쿼리 결과를 저장합니다.
- **쿼리 캐싱**: 자주 쓰는 쿼리 결과를 캐시합니다.

### 흔한 성능 문제
- **N+1 쿼리 문제**: 관련 데이터를 비효율적으로 여러 번 조회하는 문제
- **누락된 인덱스**: 대용량 테이블에서 전체 스캔이 발생함
- **과도한 인덱싱**: 인덱스가 너무 많아 쓰기 속도가 느려짐
- **잠금 경합**: 여러 트랜잭션이 잠금을 기다리며 충돌함
- **비효율적 쿼리**: `SELECT *`, 불필요한 조인 등 비효율적인 쿼리

## 트랜잭션과 동시성

### 트랜잭션 격리 수준
- **READ UNCOMMITTED**: 가장 낮은 격리 수준으로, dirty read가 발생할 수 있습니다.
- **READ COMMITTED**: 커밋된 데이터만 보입니다(대부분의 DB 기본값).
- **REPEATABLE READ**: 같은 트랜잭션 안에서 동일한 쿼리가 같은 결과를 반환합니다.
- **SERIALIZABLE**: 가장 높은 격리 수준으로, 트랜잭션이 순차적으로 실행되는 것처럼 동작합니다.

### 동시성 제어
- **비관적 잠금**: 접근 전에 자원을 먼저 잠급니다.
- **낙관적 잠금**: 커밋 전에 버전을 확인합니다.
- **MVCC (Multi-Version Concurrency Control)**: 행의 여러 버전을 유지합니다.
- **행 수준 잠금**: 특정 행만 잠급니다.
- **테이블 수준 잠금**: 테이블 전체를 잠급니다.

### 데드락
- 트랜잭션들이 서로를 기다리며 순환 의존이 생기는 상태입니다.
- 예방 방법: 일관된 잠금 순서, 타임아웃, 데드락 감지
- 해결 방법: 한 트랜잭션을 중단합니다.

## 복제와 확장

### 복제 유형
- **Master-Slave**: 하나의 primary와 여러 read replica로 구성됩니다.
- **Master-Master**: 여러 primary가 양방향으로 복제합니다.
- **Multi-Master**: 여러 primary를 두며 충돌 해결이 필요합니다.
- **Chain Replication**: 노드를 따라 순차적으로 복제합니다.

### 확장 방식
- **Vertical Scaling**: 서버 자원(CPU, RAM, storage)을 늘립니다.
- **Horizontal Scaling**: 서버 수를 늘립니다(sharding, partitioning).
- **Read Replicas**: 읽기 트래픽을 분산합니다.
- **Sharding**: 키·범위·해시 기준으로 데이터를 여러 서버에 분산합니다.
- **Federation**: 기능이나 서비스별로 분리합니다.

### 일관성 모델
- **Strong Consistency**: 모든 노드가 같은 시점에 동일한 데이터를 봅니다.
- **Eventual Consistency**: 시간이 지나면 모든 노드의 상태가 수렴합니다.
- **Causal Consistency**: 인과 관계가 있는 작업 순서를 보존합니다.
- **Read-Your-Writes**: 사용자가 자신의 갱신 결과를 즉시 볼 수 있습니다.

## 백업과 복구

### 백업 전략
- **전체 백업**: 전체 데이터베이스 복사본을 만듭니다.
- **증분 백업**: 마지막 백업 이후 변경분만 저장합니다.
- **차등 백업**: 마지막 전체 백업 이후 변경분을 저장합니다.
- **시점 복구**: 특정 시점으로 복원합니다.
- **연속 백업**: 실시간으로 백업 복제를 유지합니다.

### 복구 절차
- **RTO (Recovery Time Objective)**: 허용 가능한 최대 다운타임
- **RPO (Recovery Point Objective)**: 허용 가능한 최대 데이터 손실량
- **Disaster Recovery Plan**: 장애 상황에 대비한 문서화된 절차
- **테스트**: 정기적으로 복구 훈련을 수행합니다.

## 보안

### 접근 제어
- **인증**: 사용자 신원을 확인합니다.
- **인가**: 권한을 부여합니다(GRANT, REVOKE).
- **역할**: 권한을 묶어 더 쉽게 관리합니다.
- **Principle of Least Privilege**: 필요한 최소한의 접근만 허용합니다.

### 데이터 보호
- **저장 데이터 암호화**: 저장된 데이터를 암호화합니다.
- **전송 중 암호화**: 전송 중 연결에 TLS/SSL을 사용합니다.
- **마스킹**: 비운영 환경에서 민감한 데이터를 가립니다.
- **토큰화**: 민감한 데이터를 토큰으로 대체합니다.

### 일반적인 취약점
- **SQL Injection**: 사용자 입력을 통해 악의적인 SQL이 실행되는 문제
- **권한 상승**: 허가되지 않은 더 높은 권한을 획득하는 문제
- **감사 로그**: 모든 데이터베이스 활동을 추적·기록하는 기능
- **Compliance**: GDPR, HIPAA, PCI-DSS 같은 규정 준수 요구사항

## 현대 데이터베이스 기술

### 클라우드 데이터베이스
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **장점**: 관리형 서비스, 자동 확장, 내장 백업

### NewSQL 데이터베이스
- SQL의 일관성과 NoSQL의 확장성을 결합합니다.
- **예시**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **특징**: 분산 구조, ACID 트랜잭션, 수평 확장

### 시계열 데이터베이스
- 타임스탬프 기반 데이터 처리에 최적화되어 있습니다.
- **예시**: InfluxDB, TimescaleDB, Prometheus
- **활용 사례**: IoT, 모니터링, 금융 데이터

### 벡터 데이터베이스
- 임베딩 벡터를 저장하고 질의합니다.
- **예시**: Pinecone, Milvus, Weaviate, Qdrant
- **활용 사례**: 시맨틱 검색, 추천 시스템, AI 애플리케이션

### 멀티모델 데이터베이스
- 하나의 시스템에서 여러 데이터 모델을 지원합니다.
- **예시**: ArangoDB, OrientDB, Azure Cosmos DB
- **장점**: 여러 데이터베이스를 따로 운영하지 않아도 되는 유연성

## ORM과 데이터 접근

### 객체-관계 매핑
- **목적**: 데이터베이스 테이블을 프로그래밍 객체에 매핑합니다.
- **대표적인 ORM**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### 장점
- SQL로부터의 추상화
- 타입 안정성
- 마이그레이션 관리
- 쿼리 빌딩 API

### 단점
- 성능 오버헤드
- 복잡한 쿼리를 작성하기 어려울 수 있음
- N+1 query 문제
- 학습 곡선

## 데이터베이스 운영 관리

### DBA의 책임
- 설치와 구성
- 성능 튜닝
- 백업과 복구
- 보안 관리
- 용량 계획
- 모니터링과 알림
- 패치 관리

### 모니터링 지표
- 쿼리 응답 시간
- 처리량(초당 트랜잭션 수)
- 연결 수
- 캐시 적중률
- 디스크 I/O
- 잠금 대기 시간
- 복제 지연

### 유지보수 작업
- **Vacuum/Analyze**: 통계를 갱신하고 공간을 회수합니다.
- **Index Rebuilding**: 인덱스 단편화를 정리합니다.
- **통계 업데이트**: 쿼리 최적화기가 최신 정보를 활용하도록 합니다.
- **Log Rotation**: 로그 파일 크기를 관리합니다.
- **Capacity Planning**: 성장 추세를 예측하고 업그레이드를 계획합니다.
