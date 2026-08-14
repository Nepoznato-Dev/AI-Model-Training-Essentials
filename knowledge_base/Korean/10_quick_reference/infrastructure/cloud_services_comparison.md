<!--
---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
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

-->
# 클라우드 서비스 비교
컴퓨팅, 스토리지, 데이터베이스, AI/ML, 네트워킹, 모니터링, 코드형 인프라 등 세 가지 주요 클라우드 제공업체(AWS, Azure, Google Cloud)를 나란히 비교합니다. 사용할 플랫폼을 결정하거나 한 클라우드에서 다른 클라우드로 서비스를 매핑하는 설계자에게 유용합니다.
---

## 공급자 개요
| | AWS | 아주르 | 구글 클라우드(GCP) |
|---|------|-------|---------|
| **시장점유율** | ~31%(최대) | ~25%(초) | ~11%(세번째, 가장 빠르게 성장) |
| **강점** | 광범위한 서비스; 성숙함; 생태계 | 엔터프라이즈 통합; 하이브리드 클라우드; 마이크로소프트 스택 | 데이터/AI; 쿠버네티스; 글로벌 네트워크 |
| **최고의 대상** | 스타트업에서 기업으로; 가장 광범위한 서비스 카탈로그 | Microsoft/Active Directory를 사용하는 기업 하이브리드 | 데이터 집약적인 워크로드 Kubernetes 기반; AI/ML |
| **지역** | 33개 지역, 105개 AZ | 60개 이상의 지역 | 40개 이상의 지역, 100개 이상의 영역 |
| **무료 등급** | 12개월 무료 등급 + 상시 무료 | 12개월 무료 + $200 크레딧 | 90일 동안 $300 크레딧 + 상시 무료 |
---

## 컴퓨팅
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **가상 머신** | EC2(탄력적 컴퓨팅 클라우드) | 가상 머신 | 컴퓨팅 엔진 |
| **자동 확장** | Auto Scaling 그룹 | 가상 머신 확장 세트 | 인스턴스 그룹 |
| **서버리스 기능** | 람다 | 애저 함수 | 클라우드 기능 |
| **컨테이너 레지스트리** | ECR(탄력적 컨테이너 레지스트리) | Azure 컨테이너 레지스트리 | 유물 등록소 |
| **컨테이너 오케스트레이션** | ECS / EKS | ACS / AKS | GKE/클라우드 실행 |
| **서버리스 컨테이너** | 파게이트 | 컨테이너 앱 | 클라우드런 |
| **앱 플랫폼(PaaS)** | Elastic Beanstalk, 앱 실행자 | 앱 서비스 | 앱 엔진 |
| **일괄 처리** | AWS 배치 | Azure 배치 | 클라우드 배치 |
| **GPU/AI 컴퓨팅** | EC2(P4d, P5 인스턴스) | NC/ND 시리즈 VM | A2/A3 VM; TPU |
### VM 가격 모델
| 모델 | AWS | 아주르 | GCP |
|-------|------|-------|------|
| **주문형** | 온디맨드 인스턴스 | 종량제 | 주문형 |
| **예약됨/확정됨** | 예약 인스턴스(1~3년) | 예약된 VM(1~3년) | 약정 사용 할인(1~3년) |
| **스팟/인터럽트** | 스팟 인스턴스 | 스팟 VM | 선점형/스팟 VM |
| **저축 계획** | 저축 계획 | 저축 계획 | 약정 사용 할인 |
---

## 저장
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **객체 스토리지** | S3 | Blob 저장소 | 클라우드 스토리지 |
| **블록 스토리지** | EBS | 관리 디스크 | 영구 디스크 |
| **파일 저장소** | EFS, FSx | Azure 파일 | 파일 저장소 |
| **아카이브/콜드** | S3 빙하, 딥 아카이브 | Blob Cool/보관 계층 | 클라우드 스토리지 콜드라인/아카이브 |
| **데이터 전송** | 눈덩이, DataSync | 데이터 박스 | 트랜스퍼 어플라이언스 |
### 스토리지 클래스 비교
| 사용 사례 | AWS S3 | Azure 블롭 | GCP 클라우드 스토리지 |
|----------|---------|------------|------|
| **자주 접속** | S3 표준 | 핫 | 표준 |
| **빈번한 액세스** | S3 스탠다드-IA | 멋지다 | 니어라인 |
| **드문 액세스** | S3 One Zone-IA | — | 콜드라인 |
| **아카이브** | S3 빙하/딥 아카이브 | 아카이브 | 아카이브 |
---

## 데이터베이스
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **관계형(관리형)** | RDS(MySQL, PostgreSQL, Oracle, SQL Server) | Azure 데이터베이스(MySQL, PostgreSQL); 애저 SQL | 클라우드 SQL(MySQL, PostgreSQL) |
| **관계형(클라우드 기반)** | Aurora(MySQL/PostgreSQL 호환) | Azure SQL Database(탄력적 풀) | Cloud Spanner(전 세계적으로 분산됨) |
| **NoSQL(문서)** | 다이나모DB | 코스모스 DB(MongoDB API, SQL API) | 소방서; 데이터스토어 |
| **NoSQL(와이드 컬럼)** | DynamoDB(또한) | 코스모스 DB(카산드라 API) | 빅테이블 |
| **NoSQL(키-값)** | DynamoDB, ElastiCache | Redis용 Azure 캐시 | 메모리스토어(Redis) |
| **그래프** | 해왕성 | 코스모스 DB(그렘린 API) | — |
| **시계열** | 타임스트림 | Azure 데이터 탐색기 | — |
| **원장** | QLDB | Azure 기밀 원장 | — |
| **인메모리 캐시** | ElastiCache(Redis, Memcached) | Redis용 Azure 캐시 | 메모리스토어 |
| **검색** | 오픈서치 서비스 | Azure AI 검색 | 클라우드 검색; Vertex AI 검색 |
| **데이터 웨어하우스** | 적색편이 | 시냅스 분석 | 빅쿼리 |
---

## AI와 머신러닝
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **ML 플랫폼** | 세이지메이커 | Azure 기계 학습 | 버텍스 AI |
| **사전 학습된 API** | Rekognition(비전), Polly(TTS), Comprehend(NLP), Transcribe | 인지 서비스(시각, 말하기, 언어, 결정) | Vision AI, 음성 텍스트 변환, 자연어 API |
| **LLM / 생성 AI** | 기반암(클로드, 라마, 타이탄) | Azure OpenAI 서비스(GPT-4, DALL-E) | Vertex AI(제미니); 모델정원 |
| **벡터/임베딩** | OpenSearch(k-NN), Bedrock 기술 자료 | Azure AI 검색(벡터) | Vertex AI 벡터 검색, AlloyDB |
| **MLOps** | SageMaker 파이프라인, 모델 레지스트리 | Azure ML 파이프라인, 모델 레지스트리 | Vertex AI 파이프라인, 모델 레지스트리 |
| **데이터 라벨링** | SageMaker 실제 정보 | Azure ML 데이터 레이블 지정 | Vertex AI 데이터 라벨링 |
| **대화형 AI** | 렉스 | Azure 봇 서비스 | Dialogflow CX/ES |
| **번역** | 번역 | 번역가 | 번역 API |
---

## 네트워킹
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **가상 네트워크** | VPC | 가상 네트워크(VNet) | VPC |
| **로드 밸런싱** | ELB/ALB/NLB/CLB | 로드 밸런서(애플리케이션, 네트워크, 게이트웨이) | 클라우드 로드 밸런싱 |
| **DNS** | 53번 국도 | Azure DNS | 클라우드 DNS |
| **CDN** | 클라우드프론트 | 푸른 정문 | 클라우드 CDN |
| **API 게이트웨이** | API 게이트웨이 | API 관리 | API 게이트웨이 |
| **VPN** | 사이트 간 VPN, 클라이언트 VPN | VPN 게이트웨이 | 클라우드 VPN |
| **직접 연결/ExpressRoute** | 직접 연결 | 익스프레스루트 | 클라우드 인터커넥트 |
| **비공개 링크** | PrivateLink, VPC 엔드포인트 | 개인 링크, 개인 끝점 | 개인 서비스 연결 |
| **방화벽** | WAF, 네트워크 방화벽 | Azure 방화벽, WAF | 클라우드 아머, 방화벽 |
| **DDoS 보호** | 쉴드 표준 / 고급 | DDoS 보호 | 클라우드 아머 |
---

## 모니터링 및 로깅
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **측정항목/모니터링** | 클라우드워치 | Azure 모니터 | 클라우드 모니터링(Stackdriver) |
| **로깅** | CloudWatch 로그 | 로그 분석(Azure Monitor 로그) | 클라우드 로깅 |
| **추적** | 엑스레이 | 애플리케이션 인사이트 | 클라우드 추적 |
| **경고** | CloudWatch 경보 | Azure Monitor 경고 | 클라우드 모니터링 알림 |
| **대시보드** | CloudWatch 대시보드 | Azure 통합 문서/대시보드 | 클라우드 모니터링 대시보드 |
| **오류 추적** | CloudWatch 합성 | 애플리케이션 인사이트 | 클라우드 오류 보고 |
| **타사** | Datadog, 뉴렐릭, PagerDuty | Datadog, 뉴렐릭, PagerDuty | Datadog, 뉴렐릭, PagerDuty |
---

## 코드 및 DevOps로서의 인프라
| 서비스 카테고리 | AWS | 아주르 | GCP |
|----|------|-------|------|
| **IaC(네이티브)** | 클라우드 형성 | ARM 템플릿/Bicep | 배포 관리자 / Pulumi |
| **IaC(교차 클라우드)** | Terraform, 풀루미, CDK | Terraform, 풀루미, Bicep | 테라폼, 풀루미 |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, GitHub 작업 | 클라우드 구축; 클라우드 배포 |
| **컨테이너 레지스트리** | ECR | Azure 컨테이너 레지스트리 | 유물 등록소 |
| **GitOps** | 앱 메시 + Flux/ArgoCD | AKS의 Flux/ArgoCD | 구성 동기화(Anthos) |
| **비밀 관리** | Secrets Manager, SSM 매개변수 저장소 | 키 볼트 | 비밀 관리자 |
---

## 가격 고려 사항
| 요인 | AWS | 아주르 | GCP |
|---------|-------|-------|------|
| **청구 세부사항** | 초당(일부 경우 첫 1시간 이후) | 초당 | 초당 |
| **지속 사용 할인** | 예약 인스턴스 / Savings Plan | 예약된 VM | 약정 사용 할인 |
| **스팟 인스턴스** | 최대 90% 할인 | 최대 90% 할인 | 최대 91% 할인 |
| **데이터 송신** | 유료(비싼) | 청구됨 | 목적지에 관계없이 동일한 가격(종종 더 저렴함) |
| **무료 등급** | 12개월 + 상시 무료 | 12개월 + $200 크레딧 | 90일 동안 $300 + 상시 무료 |
| **기업 할인** | 기업 할인 프로그램(EDP) | MACC(금전약정계약) | 약정 사용 + CUD |
---

## 언제 사용할 것인가?
| 시나리오 | 추천 | 왜 |
|----------|-------------|-----|
| **가장 광범위한 서비스 선택; 성숙한 생태계** | AWS | 가장 큰 카탈로그; 대부분의 타사 통합 |
| **Microsoft 기업; 액티브 디렉토리; 하이브리드** | 아주르 | 기본 AD 통합; 강력한 하이브리드 툴링 |
| **데이터 웨어하우징; 빅쿼리; 분석 중심** | GCP | BigQuery는 동급 최고입니다. 원활한 데이터 통합 ​​|
| **Kubernetes 네이티브 개발** | GCP | GKE는 가장 세련된 관리형 Kubernetes입니다 |
| **생성 AI/LLM 애플리케이션** | Azure 또는 GCP | GPT 모델용 Azure OpenAI; Gemini용 Vertex AI |
| **글로벌 규모의 지연 시간이 짧은 애플리케이션** | GCP | Google의 글로벌 네트워크는 진정한 장점입니다 |
| **정부/규정 준수가 많은 워크로드** | AWS 또는 Azure | 대부분의 규정 준수 인증; GovCloud 지역 |
| **비용에 민감한 스타트업** | GCP 또는 AWS | GCP의 무료 등급은 넉넉합니다. AWS에는 스타트업 크레딧이 있습니다 |
| **기존 Microsoft/.NET 스택** | 아주르 | Visual Studio, .NET, Office 365와의 긴밀한 통합 |
| **멀티 클라우드 전략** | Terraform + 세 가지 모두 | Terraform을 사용하여 클라우드 전반에서 리소스 관리 |
---

## 요약
세 가지 클라우드 모두 유능하고 안정적이며 지속적으로 확장됩니다. 선택은 일반적으로 팀이 이미 알고 있는 것, 기존 계약의 모양, 워크로드에 중요한 특정 서비스에 따라 결정됩니다. 멀티 클라우드가 점점 보편화되고 있습니다. Terraform 또는 Pulumi를 사용하여 인프라 계층에서 벤더 종속을 피하고 가장 잘하는 클라우드를 선택하세요.