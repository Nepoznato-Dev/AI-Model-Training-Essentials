---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
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
tags: [cicd, pipeline, config, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# CI/CD 파이프라인 구성
CI(지속적 통합) 및 CD(지속적 배포) 파이프라인은 소프트웨어 구축, 테스트 및 배포 프로세스를 자동화합니다. 이 참조 자료에서는 가장 널리 사용되는 CI/CD 플랫폼인 GitHub Actions, GitLab CI 및 일반 파이프라인 설계 원칙에 대한 구성 패턴을 다룹니다.
---

## GitHub 작업
### 워크플로 구조
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up language
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build
        run: python setup.py build
```

### 일반적인 트리거
| 트리거 | 설명 |
|---------|-------------|
| `on: push`| 푸시할 때마다 |
| `on: pull_request`| PR 오픈, 업데이트, 재개시 |
| `on: schedule`| Cron 기반 일정 |
| `on: workflow_dispatch`| 수동 트리거 |
| `on: release`| 릴리스 생성 시 |
| `on: workflow_call`| 다른 워크플로에서 호출됨(재사용 가능) |
### 주요 기능
| 기능 | 설명 |
|---------|-------------|
| **매트릭스 전략** | 다른 구성으로 동일한 작업 실행 |
| **비밀** | 암호화된 환경 변수(`${{ secrets.MY_SECRET }}`) |
| **환경** | 보호 규칙이 있는 배포 대상 |
| **캐싱** | 실행 간 캐시 종속성 |
| **아티팩트** | 작업(테스트 보고서, 빌드)에서 파일 업로드 |
| **재사용 가능한 워크플로** | 저장소 전체에서 워크플로 논리 공유 |
| **복합 작업** | 여러 단계를 하나의 작업으로 결합 |
### 매트릭스 전략
```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## GitLab CI
### 파이프라인 구조
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run myapp:$CI_COMMIT_SHA pytest

deploy:
  stage: deploy
  script:
    - deploy.sh $CI_COMMIT_SHA
  only:
    - main
  when: manual
```

### 핵심 키워드
| 키워드 | 설명 |
|---------|-------------|
| `stages`| 파이프라인 단계 및 순서 정의 |
| `stage`| 단계에 작업 할당 |
| `script`| 실행할 명령 |
| `before_script`| 기본 스크립트보다 먼저 실행되는 명령 |
| `after_script`| 기본 스크립트 이후에 명령 실행(실패 시에도) |
| `only / except`| 작업 실행 시기 제어(분기, 태그) |
| `rules`| only/exc의 보다 유연한 버전 |
| `variables`| CI/CD 변수 정의 |
| `cache`| 파이프라인 실행 간 파일 캐시 |
| `artifacts`| 작업 간에 전달할 파일 |
| `environment`| 배포 환경 |
| `when`| 작업 실행 제어(on_success, on_failure, 수동, 항상) |
| `needs`| 작업 종속성 지정(DAG 모드) |
| `extends`| 다른 작업에서 구성 상속 |
| `include`| 외부 YAML 파일 가져오기 |
### 사전 정의된 변수
| 변수 | 설명 |
|----------|-------------|
| `$CI_COMMIT_SHA`| 현재 커밋 해시 |
| `$CI_COMMIT_REF_NAME`| 분기 또는 태그 이름 |
| `$CI_PIPELINE_ID`| 파이프라인 ID |
| `$CI_JOB_ID`| 채용정보 |
| `$CI_PROJECT_DIR`| 프로젝트의 전체 경로 |
| `$CI_REGISTRY`| 컨테이너 레지스트리 URL |
| `$CI_DEFAULT_BRANCH`| 기본 지점 이름 |
---

## 파이프라인 디자인 패턴
### 일반적인 패턴
| 패턴 | 설명 |
|---------|-------------|
| **한 번 빌드하고 여러 번 배포** | 아티팩트를 한 번만 빌드하세요. 각 환경에 동일한 아티팩트 배포 |
| **게이트 체크** | 프로덕션 배포 전 수동 승인 |
| **기능 플래그** | 프로덕션에 배포하지만 기능 플래그 뒤에 숨어 있음 |
| **카나리아 배포** | 작은 비율로 배포합니다. 감시 장치; 롤아웃 |
| **블루-그린 배포** | 두 개의 동일한 환경; 트래픽 전환 |
| **병렬 테스트** | 테스트 스위트를 병렬로 실행하여 파이프라인 시간 단축 |
| **린트 우선** | 비용이 많이 드는 테스트 전에 린터를 실행하십시오. 빨리 실패 |
| **캐시 종속성** | node_modules, pip, Maven을 캐시하여 빌드 속도 향상 |
### 파이프라인 단계(일반)
| 무대 | 목적 |
|-------|---------|
| **린트** | 코드 스타일 및 정적 분석 |
| **빌드** | 엮다; 묶음; 아티팩트 생성 |
| **단위 테스트** | 빠른 테스트; 외부 종속성 없음 |
| **통합 테스트** | 데이터베이스로 테스트합니다. 아피스; 외부 서비스 |
| **보안 검사** | 종속성 취약점 비밀 스캐닝; SAST |
| **패키지** | Docker 이미지를 생성합니다. 빌드 릴리스 아티팩트 |
| **스테이징 배포** | 스테이징 환경에 배포 |
| **E2E 테스트** | 스테이징에 대한 전체 시스템 테스트 |
| **프로덕션 배포** | 프로덕션에 배포(수동 또는 자동) |
| **연기 테스트** | 배포가 정상인지 확인 |
---

## 캐싱 전략
| 언어/도구 | 캐시 경로 | 예 |
|---|------------|---------|
| **파이썬(핍)** | `~/.cache/pip`| `requirements.txt`해시의 키가 있는`actions/cache`|
| **Node.js(npm)** | `~/.npm`|  캐싱이 내장된`actions/setup-node`|
| **자바(메이븐)** | `~/.m2/repository`|`pom.xml`해시의 키가 있는 캐시 |
| **자바(Gradle)** | `~/.gradle/caches`|`build.gradle`해시의 키가 있는 캐시 |
| **가기** | `~/go/pkg/mod`|`go.sum`해시의 키가 있는 캐시 |
| **러스트(화물)** | `~/.cargo/registry`|`Cargo.lock`해시의 키가 있는 캐시 |
| **도커** | Docker 레이어 캐싱 |  캐시에서`docker/build-push-action`|
---

## 문제 해결
| 문제 | 솔루션 |
|---------|----------|
| **파이프라인이 느림** | 캐시 종속성 작업 병렬화; 더 작은 기본 이미지 사용 |
| **비밀정보를 사용할 수 없음** | 비밀 이름을 확인하세요. 환경 범위를 확인합니다. 포크 PR 제한 사항을 확인하세요 |
| **아티팩트가 너무 큼** | 불필요한 파일을 제외합니다. 압박 붕대; 더 짧은 보존 기간 사용 |
| **행렬이 너무 큼** | 조합을 줄입니다.`include`/`exclude`사용 |
| **불안정한 테스트** | 격리된 색다른 테스트; 근본 원인을 수정합니다. `retry:`로 다시 시도 |
| **권한이 거부되었습니다** | 토큰 범위를 확인하세요. 러너 권한 확인 |
---

## 요약
CI/CD 파이프라인은 소프트웨어 구축, 테스트 및 배포를 자동화합니다. GitHub Actions는 저장소 이벤트에 의해 트리거되는 YAML 워크플로를 사용합니다. GitLab CI는 유연한 규칙으로 스테이지와 작업을 사용합니다. 주요 패턴은 다음과 같습니다: 한 번 빌드하고 여러 개 배포; 생산 전 게이트 점검; 빠른 피드백을 위해 린트를 먼저 사용합니다. 빌드 속도를 높이기 위한 캐시 종속성; 테스트를 병렬화합니다. 파이프라인 단계는 일반적으로 린트 → 빌드 → 테스트 → 보안 → 패키지 → 배포 → 스모크 테스트로 진행됩니다. 캐싱 전략은 언어에 따라 다르지만 동일한 원칙을 따릅니다. 즉, 잠금 파일 해시로 키가 지정된 캐시 종속성 디렉터리입니다. 목표는 모든 변경 사항에 대한 빠르고 안정적인 피드백과 안전하고 반복 가능한 프로덕션 배포입니다.