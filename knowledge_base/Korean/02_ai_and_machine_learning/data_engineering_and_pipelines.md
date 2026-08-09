---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 데이터 엔지니어링 및 파이프라인
데이터 엔지니어링은 대규모로 데이터를 이동, 변환, 저장하는 시스템을 구축하는 분야입니다. 신뢰할 수 있는 데이터 파이프라인이 없으면 기계 학습 모델을 훈련할 수 없고 대시보드에 오래된 숫자가 표시되며 비즈니스 결정은 추측에 기반합니다. 이 파일은 작동하는 데이터 인프라를 구축하기 위한 아키텍처, 도구 및 사례를 다루고 있습니다.
---

## ETL 대 ELT
| 접근 | 작동 원리 | 최고의 대상 | 도구 |
|----------|-------------|----------|-------|
| **ETL**(추출 → 변환 → 로드) | 창고에 로드하기 *전에* 데이터 변환 | 컴퓨팅이 제한된 기존 창고 | 인포매티카, Talend, Apache NiFi |
| **ELT**(추출 → 로드 → 변환) | 원시 데이터를 먼저 로드합니다. 창고 *내부* 변형 | 탄력적인 컴퓨팅을 갖춘 최신 클라우드 웨어하우스 | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
ETL에서 ELT로의 전환은 스토리지와 독립적으로 컴퓨팅을 확장할 수 있는 클라우드 데이터 웨어하우스(BigQuery, Snowflake, Redshift)에 의해 주도되었습니다. 더 이상 로드하기 전에 모든 것을 사전 처리할 필요가 없습니다.
---

## 데이터 레이크와 데이터 웨어하우스
| 기능 | 데이터 레이크 | 데이터 웨어하우스 |
|---------|------------|---------------|
| **데이터 형식** | 원시, 기본 형식(읽기 스키마) | 구조화되고 처리됨(쓰기 시 스키마) |
| **스키마** | 쿼리 시 정의됨 | 로드하기 전에 정의됨 |
| **데이터 유형** | 구조화, 반구조화, 비구조화 | 주로 구조화됨 |
| **사용자** | 데이터 과학자, 엔지니어 | 비즈니스 분석가, BI 도구 |
| **비용** | 저렴한 스토리지(오브젝트 스토리지) | 더 비쌉니다(쿼리에 최적화됨) |
| **예** | AWS S3, Azure 데이터 레이크, GCS | 스노우플레이크, BigQuery, Redshift |
현대적인 접근 방식은 **레이크하우스**입니다. 저렴하고 유연한 호수 저장 기능과 창고의 관리 및 성능 기능을 결합한 것입니다. Delta Lake, Apache Iceberg 및 Apache Hudi가 여기서 핵심 기술입니다.
---

## 파이프라인 아키텍처
### 일괄 처리와 스트리밍
| 모드 | 설명 | 대기 시간 | 사용 사례 |
|------|-------------|---------|----------|
| **일괄** | 예약된 간격으로 큰 청크의 데이터 처리 | 분에서 시간까지 | 일일 보고서, ETL 작업, 데이터 강화 |
| **스트리밍** | 데이터가 도착하면 지속적으로 처리 | 밀리초에서 초로 | 실시간 대시보드, 사기 탐지, 경고 |
| **마이크로배치** | 매우 짧은 간격으로 작은 배치 | 초 | 배치 단순성을 갖춘 거의 실시간 |
### 파이프라인 구성요소
일반적인 데이터 파이프라인에는 다음과 같은 단계가 있습니다.
| 무대 | 설명 | 도구 |
|-------|-------------|-------|
| **섭취** | 소스에서 데이터 수집 | 카프카, 에어바이트, Fivetran, Debezium |
| **변환** | 정리, 강화, 집계 | dbt, 스파크, 팬더 |
| **스토리지** | 처리된 데이터 유지 | BigQuery, 눈송이, S3, 델타 레이크 |
| **서빙** | 소비자에게 데이터 제공 | API, 대시보드, ML 기능 저장소 |
| **오케스트레이션** | 종속성 예약 및 관리 | 기류, 지사, Dagster |
| **모니터링** | 파이프라인 상태 및 데이터 품질 추적 | Great Expectations, Monte Carlo, 맞춤 알림 |
---

## 오케스트레이션 도구
| 도구 | 접근 | 힘 |
|------|----------|----------|
| **아파치 에어플로우** | Python 기반 DAG; 산업 표준 | 성숙하고 유연한 거대한 생태계 |
| **반장** | Python 기반; Airflow보다 더 깨끗한 API | 현대적인 디자인, 뛰어난 오류 처리 |
| **대그스터** | 자산 중심; 소프트웨어 공학적 접근 | 유형 시스템, 테스트, 관찰 가능성 |
| **루이지** | Spotify의 오리지널 파이프라인 도구 | 단순하지만 덜 활발하게 개발됨 |
### 공기 흐름 예시
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## 아파치 카프카
Kafka는 많은 실시간 데이터 시스템의 백본입니다. 높은 처리량과 내결함성 메시징을 제공하는 분산 이벤트 로그입니다.
### 핵심 개념
| 개념 | 설명 |
|---------|-------------|
| **주제** | 메시지 카테고리(예:`orders`,`user-events`) |
| **파티션** | 주제는 병렬 처리를 위해 파티션으로 분할됩니다. |
| **프로듀서** | 주제에 메시지를 쓰는 애플리케이션 |
| **소비자** | 주제의 메시지를 읽는 애플리케이션 |
| **소비자 그룹** | 주제를 읽는 부담을 공유하는 소비자 집단 |
| **오프셋** | 파티션 내 소비자의 위치 |
| **브로커** | Kafka 서버 노드 |
### Kafka를 사용해야 하는 경우
- **이벤트 스트리밍**: 대규모 실시간 이벤트 처리.
- **디커플링 서비스**: 생산자와 소비자는 서로에 대해 알 필요가 없습니다.
- **재생**: 메시지가 유지됩니다. 소비자는 모든 오프셋에서 다시 읽을 수 있습니다.
- **배압**: Kafka는 생산자와 소비자 간의 속도 차이를 자연스럽게 처리합니다.
---

## 데이터 모델링
### 스타 스키마와 눈송이 스키마 비교
| 스키마 | 구조 | 장점 | 단점 |
|---------|------------|------|------|
| **스타** | 비정규화된 차원 테이블로 둘러싸인 중앙 팩트 테이블 | 간단한 쿼리, 빠른 읽기 | 데이터 중복성 |
| **눈송이** | 차원 테이블이 정규화됨(하위 테이블로 분할됨) | 중복성 감소 | 더 많은 조인, 더 느린 쿼리 |
### 사실 및 차원 테이블
| 테이블 유형 | 포함 | 예 |
|------------|----------|---------|
| **사실** | 측정 가능한 이벤트(메트릭) |  `orders`(주문_ID, 제품_ID, 고객_ID, 금액, 날짜) |
| **차원** | 설명 속성 |  `products`(제품_ID, 이름, 카테고리, 가격), `customers`(고객_ID, 이름, 도시) |
---

## 피처 스토어
특성 저장소는 모델에 대한 입력으로 사용되는 파생 값(예: '지난 30일 동안 사용자의 평균 주문 값')인 ML 특성의 중앙 집중식 저장소입니다.
| 능력 | 설명 |
|------------|-------------|
| **기능 레지스트리** | 메타데이터와 함께 사용 가능한 기능 카탈로그 |
| **오프라인 매장** | 모델 훈련을 위한 과거 특징(일괄) |
| **온라인 스토어** | 실시간 추론을 위한 저지연 기능 제공 |
| **기능 모니터링** | 드리프트, 결측값, 분포 변화 감지 |
| 도구 | 설명 |
|------|-------------|
| **잔치** | 오픈 소스; 모든 ML 프레임워크에서 작동 |
| **텍톤** | 광고; 실시간 기능 플랫폼 |
| **홉스웍스** | 오픈 소스; 특성 저장소가 포함된 전체 ML 플랫폼 |
| **Databricks 피처 스토어** | Databricks/Spark와 통합 |
---

## 데이터 품질
데이터 품질은 ML 프로젝트의 조용한 살인자입니다. 쓰레기는 들어가고 쓰레기는 나옵니다.
### 품질 차원
| 차원 | 질문 |
|------------|----------|
| **정확성** | 데이터가 현실을 반영하는가? |
| **완전성** | 필수 필드가 채워져 있습니까? |
| **일관성** | 가치는 소스 전반에 걸쳐 일치합니까? |
| **적시성** | 데이터가 최신인가요? |
| **유효성** | 가치는 정의된 규칙을 준수합니까? |
| **독창성** | 중복된 기록이 있나요? |
### 데이터 품질 도구
| 도구 | 접근 |
|------|----------|
| **큰 기대** | Python 기반; 데이터에 대한 "기대"를 정의 |
| **몬테카를로** | ML 기반 데이터 관측 플랫폼 |
| **dbt 테스트** | 웨어하우스 데이터에 대한 내장 테스트(고유, not_null, 관계) |
| **소다** | 오픈소스 데이터 품질 스캐닝 |
---

## 데이터 거버넌스
데이터 거버넌스는 조직 전체에서 데이터가 책임감 있게 관리되도록 보장합니다.
| 면적 | 설명 |
|------|-------------|
| **데이터 카탈로그** | 메타데이터가 포함된 검색 가능한 데이터 세트 인벤토리(Amundsen, DataHub, Atlan) |
| **데이터 계보** | 데이터의 출처와 데이터가 어떻게 변환되는지 추적 |
| **접근 제어** | 역할 기반 권한; 누가 무엇을 읽고 쓸 수 있나요 |
| **규정 준수** | GDPR, CCPA, HIPAA 준수 |
| **데이터 소유권** | 각 데이터 세트에 대한 명확한 소유권(관리) |
| **보존 정책** | 데이터 보관 기간과 삭제 시기 정의 |
---

## 최신 데이터 스택
"최신 데이터 스택"은 오늘날 데이터 팀이 사용하는 일반적인 도구 조합을 의미합니다.
| 레이어 | 일반적인 도구 |
|-------|---------------|
| **섭취** | Fivetran, 에어바이트 |
| **창고** | 스노우플레이크, BigQuery, Redshift |
| **변환** | DBT |
| **오케스트레이션** | 기류, 지사, Dagster |
| **BI/시각화** | Looker, 메타베이스, Tableau |
| **역방향 ETL** | 인구조사, 하이터치(창고 데이터를 도구에 다시 동기화) |
| **데이터 품질** | 위대한 유산, 몬테카를로 |
모놀리식 플랫폼보다는 개방형 표준(SQL, dbt 모델, Airflow DAG)으로 연결된 동종 최고의 모듈식 도구를 지향하는 추세입니다.