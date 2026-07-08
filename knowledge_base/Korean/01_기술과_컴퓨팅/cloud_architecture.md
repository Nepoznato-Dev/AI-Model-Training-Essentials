<!-- 
This file was automatically translated from English to Korean.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 클라우드 아키텍처

## 클라우드 컴퓨팅 기초

### 클라우드 컴퓨팅이란 무엇인가?
온디맨드 컴퓨팅 리소스 제공 (서버, 스토리지, 데이터베이스, 네트워킹, 소프트웨어) 을 인터넷을 통해 종량제 가격 책정으로 제공.

### 기본 특성 (NIST 정의)
- **온디맨드 셀프서비스**: 사람과의 상호작용 없이 리소스 프로비저닝
- **광범위한 네트워크 액세스**: 표준 메커니즘을 통해 네트워크를 통해 이용 가능
- **리소스 풀링**: 멀티테넌트 모델 및 동적 할당
- **신속한 탄력성**: 빠르게 스케일아웃 및 스케일인
- **측정된 서비스**: 리소스 사용량 모니터링 및 과금

### 클라우드 배포 모델
- **퍼블릭 클라우드**: 제공자가 소유, 공유 인프라 (AWS, Azure, GCP)
- **프라이빗 클라우드**: 단일 조직 전용 (온프레미스 또는 호스팅)
- **하이브리드 클라우드**: 퍼블릭 클라우드와 프라이빗 클라우드의 조합
- **멀티클라우드**: 여러 퍼블릭 클라우드 제공자 사용
- **커뮤니티 클라우드**: 공통 관심사를 가진 조직 간 공유

### 서비스 모델

#### Infrastructure as a Service (IaaS)
- **제공 내용**: 가상 머신, 스토리지, 네트워크, 운영 체제
- **예시**: AWS EC2, Google Compute Engine, Azure VMs
- **사용 사례**: 리프트앤시프트 마이그레이션, 개발 환경, 높은 제어 필요

#### Platform as a Service (PaaS)
- **제공 내용**: 개발 플랫폼, 데이터베이스, 미들웨어
- **예시**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **사용 사례**: 애플리케이션 개발, API 배포, 마이크로서비스

#### Software as a Service (SaaS)
- **제공 내용**: 완전한 애플리케이션을 인터넷을 통해 제공
- **예시**: Salesforce, Google Workspace, Microsoft 365, Slack
- **사용 사례**: 이메일, CRM, 협업, 비즈니스 애플리케이션

#### Function as a Service (FaaS) / 서버리스
- **제공 내용**: 이벤트 기반 함수 실행
- **예시**: AWS Lambda, Azure Functions, Google Cloud Functions
- **사용 사례**: 이벤트 처리, API, 예약 작업, 실시간 처리

## 주요 클라우드 제공자

### Amazon Web Services (AWS)
- **시장 점유율**: 약 32% (최대 제공자)
- **주요 서비스**:
  - 컴퓨트: EC2, Lambda, ECS, EKS
  - 스토리지: S3, EBS, Glacier
  - 데이터베이스: RDS, DynamoDB, Aurora
  - 네트워킹: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **시장 점유율**: 약 23%
- **강점**: 엔터프라이즈 통합, 하이브리드 클라우드, Microsoft 생태계
- **주요 서비스**:
  - 컴퓨트: Virtual Machines, Azure Functions, AKS
  - 스토리지: Blob Storage, Disk Storage
  - 데이터베이스: SQL Database, Cosmos DB
  - 네트워킹: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **시장 점유율**: 약 10%
- **강점**: 데이터 분석, AI/ML, Kubernetes
- **주요 서비스**:
  - 컴퓨트: Compute Engine, Cloud Functions, GKE
  - 스토리지: Cloud Storage, Persistent Disk
  - 데이터베이스: Cloud SQL, Firestore, Bigtable
  - 분석: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### 기타 제공자
- **IBM Cloud**: 엔터프라이즈 중심, Watson AI
- **Oracle Cloud**: 데이터베이스 워크로드, 엔터프라이즈 애플리케이션
- **Alibaba Cloud**: 아시아 태평양 지역에서 지배적
- **DigitalOcean**: 개발자 친화적, 단순화된 제품

## 클라우드 아키텍처 패턴

### Well-Architected Framework 원칙

#### 운영 우수성
- 운영 자동화
- 빈번하고 가역적인 변경 수행
- 절차 지속적 개선
- 장애 예측

#### 보안
- 강력한 ID 기반 구현
- 추적 가능성 활성화
- 모든 계층에서 보안 적용
- 보안 모범 사례 자동화
- 전송 중 및 저장 시 데이터 보호

#### 신뢰성
- 복구 절차 테스트
- 장애 시 자동 복구
- 가용성을 위한 수평 확장
- 용량 추측 중지
- 자동화로 변경 관리

#### 성능 효율성
- 고급 기술 민주화
- 몇 분 안에 글로벌 확장
- 서버리스 아키텍처 사용
- 더 자주 실험
- 기계적 공감 고려

#### 비용 최적화
- 소비 모델 채택
- 전체 효율성 측정
- 차별화되지 않은 작업에 지출 중지
- 지출 분석 및 귀속
- 관리 서비스 사용

### 일반적인 아키텍처 패턴

#### 마이크로서비스 아키텍처
- 애플리케이션을 작고 독립적인 서비스로 분해
- 각 서비스는 자체 데이터와 로직 소유
- API(REST, gRPC, 메시징) 를 통해 통신
- 독립적으로 배포
- **장점**: 확장성, 장애 격리, 기술 다양성
- **과제**: 분산 복잡성, 데이터 일관성, 모니터링

#### 이벤트 기반 아키텍처
- 구성 요소는 이벤트를 통해 통신
- 프로듀서는 이벤트 발행, 컨슈머는 반응
- **패턴**: 이벤트 소싱, CQRS, pub/sub
- **기술**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **장점**: 느슨한 결합, 확장성, 실시간 처리

#### 서버리스 아키텍처
- 서버 관리 불필요
- 실행 단위 과금
- 자동 확장
- **구성 요소**: 함수, API Gateway, 관리 서비스
- **장점**: 비용 효율성, 운영 감소, 빠른 배포
- **고려 사항**: 콜드 스타트, 벤더 락인, 실행 제한

#### 레이어드 아키텍처 (N-Tier)
- 프레젠테이션 계층 (UI)
- 애플리케이션/비즈니스 로직 계층
- 데이터 액세스 계층
- 데이터베이스 계층
- **장점**: 관심사 분리, 유지보수성
- **일반적**: 3 티어 웹 애플리케이션

#### 스페이스 기반 아키텍처
- 고동시성 및 분산 데이터 처리
- 서버 간 가상화 메모리
- 처리 노드는 독립적으로 확장
- **사용 사례**: 대용량, 저지연 애플리케이션

## 컴퓨트 서비스

### 가상 머신
- **유형**: 범용, 컴퓨트 최적화, 메모리 최적화, GPU
- **가격 책정**: 온디맨드, 리저브드 인스턴스, 스팟 인스턴스
- **관리**: 오토스케일링 그룹, 로드 밸런서
- **모범 사례**: 적절한 사이징, 태깅, 모니터링, 패치 적용

### 컨테이너
- **Docker**: 컨테이너 런타임 표준
- **오케스트레이션**: Kubernetes(EKS, AKS, GKE), ECS, Fargate
- **장점**: 이식성, 효율성, 일관성
- **레지스트리**: ECR, GCR, ACR, Docker Hub

### 서버리스 함수
- **실행 모델**: 이벤트 트리거, 상태 없음
- **제한**: 실행 시간, 메모리, 동시 실행
- **사용 사례**: API, 파일 처리, 예약 작업, IoT 백엔드
- **모니터링**: 호출 횟수, 오류, 기간, 콜드 스타트

## 스토리지 솔루션

### 객체 스토리지
- **특징**: 플랫 구조, 메타데이터, HTTP 액세스
- **예시**: AWS S3, Google Cloud Storage, Azure Blob
- **사용 사례**: 정적 자산, 백업, 데이터 레이크, 아카이브
- **스토리지 클래스**: 핫, 쿨, 콜드, 아카이브 (비용/액세스 다름)

### 블록 스토리지
- **특징**: RAW 볼륨, VM 에 연결
- **예시**: AWS EBS, Google Persistent Disk, Azure Disks
- **사용 사례**: 데이터베이스, 부트 볼륨, 고성능 요구
- **유형**: SSD, HDD, 프로비저닝 IOPS

### 파일 스토리지
- **특징**: 공유 파일 시스템, NFS/SMB 프로토콜
- **예시**: AWS EFS, Google Filestore, Azure Files
- **사용 사례**: 콘텐츠 관리, 공유 구성, 리프트앤시프트

### 아카이브 스토리지
- **특징**: 최저 비용, 검색 지연
- **예시**: S3 Glacier, Azure Archive Storage
- **사용 사례**: 규정 준수, 장기 백업, 역사적 데이터

## 데이터베이스 서비스

### 관리형 관계형 데이터베이스
- **서비스**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **기능**: 자동 백업, 패치 적용, 확장, 복제
- **엔진**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### NoSQL 데이터베이스
- **문서**: DocumentDB, Firestore, Cosmos DB
- **키 - 값**: DynamoDB, Redis Cache
- **와이드 컬럼**: Bigtable, Cassandra(관리형)
- **그래프**: Neptune, Cosmos DB(그래프 API)

### 데이터 웨어하우징
- **서비스**: Snowflake, Redshift, BigQuery, Synapse
- **특징**: 컬럼나 스토리지, MPP 아키텍처
- **사용 사례**: 분석, BI, 대규모 데이터 분석

### 캐싱 서비스
- **인메모리**: ElastiCache(Redis/Memcached), Cloud Memorystore
- **CDN 캐싱**: CloudFront, Cloud CDN, Azure CDN
- **사용 사례**: 세션 스토리지, 쿼리 캐싱, 콘텐츠 전송

## 네트워킹

### 가상 네트워크
- **VPC/VNet**: 격리된 네트워크 환경
- **서브넷**: 퍼블릭 (인터넷 연결), 프라이빗 (내부만)
- **IP 주소 지정**: CIDR 블록, IPv4/IPv6
- **라우트 테이블**: 트래픽 흐름 제어

### 로드 밸런싱
- **유형**: 애플리케이션 (L7), 네트워크 (L4), 게이트웨이
- **기능**: 헬스 체크, SSL 종료, 스티키 세션
- **서비스**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### 콘텐츠 전송 네트워크 (CDN)
- **목적**: 엣지 위치에서 콘텐츠 캐싱
- **장점**: 지연 시간 감소, 오리진 부하 감소, 글로벌 배포
- **서비스**: CloudFront, Cloud CDN, Azure CDN, Akamai

### DNS 서비스
- **기능**: 도메인 등록, 라우팅, 헬스 체크
- **서비스**: Route 53, Cloud DNS, Azure DNS
- **라우팅 정책**: 심플, 가중치, 지연 시간 기반, 지리적 위치, 페일오버

### 연결 옵션
- **인터넷 게이트웨이**: 퍼블릭 인터넷 액세스
- **NAT 게이트웨이**: 프라이빗 서브넷 아웃바운드 액세스
- **VPN**: 온프레미스로 암호화 터널
- **Direct Connect/ExpressRoute**: 전용 프라이빗 연결
- **VPC 피어링**: 계정 내/간 VPC 연결

## 클라우드 보안

### 공유 책임 모델
- **제공자 책임**: 클라우드의 보안 (인프라)
- **고객 책임**: 클라우드 내 보안 (데이터, 애플리케이션, 액세스)
- **서비스별 차이**: 관리형이 많을수록 제공자 책임 증가

### ID 및 액세스 관리 (IAM)
- **사용자**: 개별 ID
- **그룹**: 사용자 컬렉션
- **롤**: 서비스/사용자를 위한 임시 자격 증명
- **정책**: 권한을 정의하는 JSON 문서
- **원칙**: 최소 권한, 직무 분리

### 네트워크 보안
- **보안 그룹**: 인스턴스용 상태 방화벽
- **네트워크 ACL**: 서브넷용 무상태 방화벽
- **웹 애플리케이션 방화벽 (WAF)**: 웹 익스플로잇으로부터 보호
- **DDoS 보호**: Shield, Cloud Armor, DDoS Protection

### 데이터 보호
- **저장 시 암호화**: KMS, 고객 관리 키
- **전송 중 암호화**: TLS/SSL, HTTPS
- **키 관리**: HSM, 키 회전, 감사 로그
- **비밀 관리**: Secrets Manager, Key Vault

### 규정 준수 및 거버넌스
- **인증**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **도구**: 정책 시행, 규정 준수 보고, 감사 로그
- **프레임워크**: Cloud Security Alliance, NIST CSF

## 클라우드 DevOps

### CI/CD 서비스
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **서드파티**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: 멀티클라우드, 선언적, 상태 관리
- **CloudFormation**: AWS 네이티브, YAML/JSON 템플릿
- **ARM 템플릿**: Azure 네이티브
- **Deployment Manager**: GCP 네이티브
- **Pulumi**: 프로그래밍 언어를 사용한 인프라
- **장점**: 버전 관리, 재현성, 문서화

### 구성 관리
- **Ansible**: 에이전트리스, YAML 플레이북
- **Chef**: Ruby 기반, 성숙한 생태계
- **Puppet**: 선언적, 강력한 보고 기능
- **SaltStack**: 빠름, Python 기반

### 모니터링 및 관찰 가능성
- **메트릭**: CloudWatch, Cloud Monitoring, Azure Monitor
- **로깅**: CloudWatch Logs, Cloud Logging, Log Analytics
- **추적**: X-Ray, Cloud Trace, Application Insights
- **대시보드**: CloudWatch Dashboards, Cloud Console
- **알림**: SNS, Cloud Monitoring 알림, Action Groups

### 컨테이너 오케스트레이션
- **Kubernetes**: 업계 표준 오케스트레이션
- **관리 서비스**: EKS, AKS, GKE
- **서비스 메시**: Istio, Linkerd(트래픽 관리, 보안)
- **GitOps**: ArgoCD, Flux(선언적 배포)

## 비용 관리

### 가격 모델
- **종량제**: 사용한 만큼 지불
- **리저브드 인스턴스**: 1-3 년 약정, 상당한 할인
- **스팟 인스턴스**: 미사용 용량 입찰, 중단 가능
- **세이빙스 플랜**: 유연한 약정 가격
- **무료 티어**: 새 계정을 위한 제한된 무료 사용

### 비용 최적화 전략
- **적절한 사이징**: 인스턴스 유형을 워크로드 요구에 일치
- **오토스케일링**: 수요에 따라 확장
- **리저브드 용량**: 안정적 워크로드에 약정
- **스팟 사용**: 내결함성 있고 유연한 워크로드에 사용
- **스토리지 티어**: 저빈도 데이터를 저렴한 티어로 이동
- **정리**: 미사용 리소스, 스냅샷, AMI 삭제

### 비용 관리 도구
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Billing 보고서, Recommender
- **서드파티**: CloudHealth, CloudCheckr, Datadog

## 고가용성 및 재해 복구

### 가용성 개념
- **가용 영역**: 리전 내 물리적으로 분리된 데이터 센터
- **리전**: 여러 AZ 를 가진 지리적 영역
- **엣지 위치**: 전 세계 CDN 캐시 위치

### HA 전략
- **멀티 AZ**: 가용 영역 전체에 배포
- **자동 복구**: 실패한 인스턴스 자동 교체
- **로드 밸런싱**: 트래픽을 정상 인스턴스에 분산
- **데이터베이스 복제**: 멀티 AZ 배포, 읽기 복제본

### 재해 복구 전략
- **백업 및 복원**: 정기 백업, 필요시 복원 (최저 비용)
- **파일럿 라이트**: 핵심 요소 실행, 재해시 확장
- **웜 스탠바이**: 축소 버전 항상 실행
- **멀티사이트 액티브/액티브**: 여러 리전에서 전체 운영 (최고 비용)

### RTO 및 RPO
- **목표 복구 시간 (RTO)**: 허용 가능한 최대 다운타임
- **목표 복구 시점 (RPO)**: 허용 가능한 최대 데이터 손실
- **전략 선택**: 비즈니스 요구 및 예산 기반

## 신흥 트렌드

### 엣지 컴퓨팅
- 데이터 소스 근처에서 처리
- **서비스**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **사용 사례**: IoT, 실시간 분석, 저지연 애플리케이션

### 멀티클라우드 및 하이브리드 클라우드
- 벤더 락인 회피
- 최고 품종 서비스 활용
- **도구**: Terraform, Anthos, Arc, CloudHealth

### AI/ML 서비스
- 사전 훈련된 모델: 비전, 음성, 언어
- 커스텀 모델 훈련: SageMaker, Vertex AI, Azure ML
- MLOps: 모델 배포, 모니터링, 거버넌스

### 양자 컴퓨팅
- **서비스**: AWS Braket, Azure Quantum
- **상태**: 초기 단계, 실험적
- **가능성**: 암호학, 최적화, 신약 발견

### 지속 가능한 클라우드
- 탄소 발자국 추적
- 재생 에너지 약속
- 효율적인 리소스 활용
- 그린 아키텍처 패턴
