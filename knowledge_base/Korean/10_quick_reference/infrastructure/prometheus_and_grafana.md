---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prometheus, grafana, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# 프로메테우스와 그라파나
Prometheus는 안정성과 확장성을 위해 설계된 오픈 소스 모니터링 및 경고 도구 키트입니다. Grafana는 시계열 데이터 시각화를 위한 최고의 오픈 소스 플랫폼입니다. 이 두 가지가 함께 현대 인프라 및 애플리케이션을 위한 가장 널리 사용되는 모니터링 스택을 형성합니다. Prometheus는 측정항목을 수집하고 저장합니다. Grafana는 이를 대시보드에 표시합니다.
---

## 프로메테우스 아키텍처
| 구성요소 | 설명 |
|------------|-------------|
| **프로메테우스 서버** | 대상에서 측정항목을 스크랩합니다. 시계열 데이터를 저장합니다. 경고 규칙을 평가합니다 |
| **수출업체** | 시스템(노드 내보내기, cAdvisor 등)에서 메트릭을 노출합니다. |
| **푸시게이트웨이** | 단기 작업(일괄 작업, CI)에서 지표 수신 |
| **경고 관리자** | 경고 처리: 그룹화, 침묵, 라우팅, 금지 |
| **서비스 검색** | 대상 자동 검색(Kubernetes, Consul, EC2 등) |
---

## 주요 개념
| 개념 | 설명 |
|---------|-------------|
| **측정항목** | 선택적 레이블과 값이 포함된 명명된 측정 |
| **시계열** | 특정 측정항목 + 라벨 조합에 대한 데이터 포인트 스트림 |
| **직업** | 같은 목적을 가진 대상들의 집합 |
| **인스턴스** | 스크래핑할 단일 대상(일반적으로 프로세스) |
| **스크래핑** | 정기적으로 대상에서 측정항목을 가져오는 Prometheus |
| **레이블** | 측정항목의 크기를 측정하는 키-값 쌍(예:`method="GET"`) |
| **샘플** | 특정 시점의 값: (타임스탬프, 값) |
---

## 측정항목 유형
| 유형 | 설명 | 사용 사례 |
|------|-------------|----------|
| **카운터** | 단조롭게 증가하는 값(오직 올라감) | 요청 횟수 오류; 완료된 작업 |
| **게이지** | 올라가거나 내려갈 수 있는 가치 | 온도; 메모리 사용량; 대기열 길이 |
| **히스토그램** | 값별로 분류된 관찰 | 요청 대기 시간 응답 크기 |
| **요약** | 히스토그램과 유사합니다. 클라이언트 측 분위수 계산 | 지연 시간 백분위수 |
---

## PromQL(쿼리 언어)
### 기본 쿼리
| 쿼리 | 설명 |
|-------|-------------|
| `http_requests_total`| 원시 시계열 |
| `http_requests_total{method="GET"}`| 라벨로 필터링 |
| `http_requests_total{method="GET", status="200"}`| 다중 라벨 필터 |
| `rate(http_requests_total[5m])`| 5분 이상 초당 속도 |
| `increase(http_requests_total[1h])`| 1시간 동안의 총 증가 |
| `sum(rate(http_requests_total[5m])) by (status)`| 상태별 누계비율 |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| 95번째 백분위수 대기 시간 |
| `avg(node_cpu_seconds_total{mode="idle"})`| 평균 CPU 유휴 |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| CPU 활용도 |
### 공통 기능
| 기능 | 설명 | 예 |
|----------|-------------|---------|
| `rate()`| 초당 평균 증가율 | `rate(requests_total[5m])`|
| `irate()`| 마지막 두 데이터 포인트를 기준으로 한 초당 비율 | `irate(requests_total[1m])`|
| `increase()`| 시간 범위에 따른 총 증가 | `increase(errors_total[1h])`|
| `sum()`| 계열 전체의 합계 | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| 시리즈 전체의 평균 | `avg(node_memory_usage)`|
| `histogram_quantile()`| 히스토그램에서 분위수 계산 | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| 가치별 상위 K 시리즈 | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| 선형 예측 | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| 측정항목이 누락되었는지 확인 | `absent(up{job="myapp"})`|
---

## 일반 수출업체
| 수출 | 모니터링 대상 |
|------------|----|
| **노드 내보내기** | Linux/Unix 호스트 지표(CPU, 메모리, 디스크, 네트워크) |
| **c어드바이저** | 컨테이너 지표(CPU, 메모리, 네트워크, 파일 시스템) |
| **MySQL 내보내기** | MySQL 데이터베이스 지표 |
| **PostgreSQL 내보내기** | PostgreSQL 데이터베이스 지표 |
| **Redis 내보내기** | Redis 측정항목 |
| **블랙박스 수출업체** | HTTP, HTTPS, DNS, TCP, ICMP를 통한 엔드포인트 프로브 |
| **SNMP 내보내기** | SNMP를 통한 네트워크 장치 메트릭 |
| **JSON 내보내기** | JSON API의 사용자 정의 측정항목 |
---

## 그라파나
### 주요 개념
| 개념 | 설명 |
|---------|-------------|
| **데이터 소스** | Prometheus(또는 기타 백엔드)에 대한 연결 |
| **대시보드** | 레이아웃으로 배열된 패널 모음 |
| **패널** | 단일 시각화(그래프, 게이지, 테이블, 히트맵) |
| **변수** | 대시보드용 동적 필터(예: 인스턴스 선택) |
| **주석** | 그래프에 이벤트 표시(배포, 사건) |
| **경고 규칙** | Grafana 내 임계값 기반 알림 |
| **템플릿** | 변수가 포함된 재사용 가능한 대시보드 패턴 |
### 유용한 대시보드 패턴
| 패턴 | 설명 |
|---------|-------------|
| **개요 행** | 주요 지표 요약: 오류율, 대기 시간, 처리량 |
| **드릴다운** | 변수를 이용하여 요약에서 상세보기로 클릭 |
| **RED 방법** | 비율, 오류, 기간 — 세 가지 주요 서비스 지표 |
| **사용방법** | 활용도, 포화도, 오류 - 인프라용 |
| **황금 신호** | 지연 시간, 트래픽, 오류, 포화도(Google의 SRE 도서) |
---

## 경고
### 경고 규칙 구조
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Alertmanager 라우팅
| 개념 | 설명 |
|---------|-------------|
| **그룹** | 유사한 경고를 하나의 알림으로 결합 |
| **경로** | 경고가 어디로 갈지 결정하는 매처 트리 |
| **수신자** | 경고를 보낼 위치(이메일, Slack, PagerDuty, webhook) |
| **금지** | 다른 경고가 실행될 때 경고 억제 |
| **침묵** | 라벨 일치자에 의한 알림을 일시적으로 음소거 |
---

## 문제 해결
| 문제 | 솔루션 |
|---------|----------|
| **타겟 다운** | 내보내기가 실행 중인지 확인하세요. 네트워크/방화벽을 확인하세요. 스크랩 구성 확인 |
| **데이터 없음** | 측정항목 이름 철자를 확인하세요. 라벨 필터를 확인하세요. 시간 범위 확인 |
| **높은 카디널리티** | 라벨 조합이 너무 많습니다. 라벨 값을 줄입니다. 녹음 규칙 사용 |
| **느린 쿼리** | 복잡한 쿼리에는 기록 규칙을 사용하세요. 긁힘 간격 증가 |
| **경고 피로** | 임계값 조정`for`기간을 추가합니다. 그룹 관련 알림 |
| **다시 시작한 후 측정항목 누락** | Prometheus는 데이터를 로컬에 저장합니다. 보존 설정 확인 |
---

## 요약
Prometheus는 정기적으로 내보내기 업체로부터 측정항목을 수집하여 시스템을 모니터링합니다. 측정항목은 카운터(위로만 이동), 게이지(위 및 아래로), 히스토그램(버킷 관측), 요약(분위수)의 네 가지 유형으로 제공됩니다. PromQL은 쿼리 언어입니다.`rate()`,`increase()`,`histogram_quantile()`및 집계 함수(`sum`,`avg`)가 가장 일반적인 작업입니다. Grafana는 패널, 변수 및 주석을 사용하여 대시보드에서 Prometheus 데이터를 시각화합니다. 경고는 경고를 그룹화, 라우팅, 음소거 및 금지하기 위해 Alertmanager를 사용합니다. 주요 모니터링 패턴은 서비스에 대한 Google의 골든 신호(지연 시간, 트래픽, 오류, 포화도)와 RED 방법(속도, 오류, 기간), 인프라에 대한 USE 방법(사용률, 포화도, 오류)입니다.