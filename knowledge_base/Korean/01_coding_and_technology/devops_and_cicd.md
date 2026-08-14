---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# DevOps 및 CI/CD
DevOps는 팀이 소프트웨어를 더 빠르고 안정적으로 제공할 수 있도록 지원하는 문화 철학, 관행 및 도구의 조합입니다. 이는 개발자(변경 사항을 제공하려는)와 운영(안정성을 원하는) 사이의 벽을 허무는 것입니다. CI/CD(지속적 통합 및 지속적 전달)는 이를 가능하게 하는 자동화 백본입니다.
---

## CI/CD 파이프라인
### CI/CD의 실제 의미
| 기간 | 그것이 하는 일 |
|------|-------------|
| **지속적 통합(CI)** | 개발자는 코드를 자주 병합합니다. 각 병합은 자동화된 빌드 및 테스트를 트리거합니다 |
| **지속적 전달(CD)** | 코드는 항상 배포 가능한 상태입니다. 프로덕션 릴리스는 수동으로 결정됩니다 |
| **지속적 배포** | 테스트를 통과한 모든 변경 사항은 자동으로 프로덕션 단계로 이동합니다. 수동 게이트가 필요하지 않습니다. |
### 일반적인 파이프라인 단계
| 무대 | 무슨 일이 일어나는지 | 도구 |
|-------|-------------|-------|
| **출처** | 개발자가 코드를 Git에 푸시 | GitHub, GitLab, Bitbucket |
| **빌드** | 코드 컴파일, 종속성 설치 | 메이븐, 그래들, npm, pip |
| **테스트** | 실행 단위, 통합, 린트 검사 | Jest, pytest, JUnit |
| **패키지** | Docker 이미지 또는 아티팩트 빌드 | Docker, 빌드팩 |
| **배포(스테이징)** | 스테이징 환경에 배포 | 쿠버네티스, ECS, VM |
| **테스트(스테이징)** | 통합 테스트, 스모크 테스트 | 셀레늄, 우편 배달부 |
| **배포(프로덕션)** | 프로덕션으로 출시 | 청록색, 카나리아, 롤링 |
| **모니터** | 상태, 오류, 성능 관찰 | 프로메테우스, 그라파나, 데이터독 |
### CI/CD 도구 비교
| 도구 | 유형 | 힘 |
|------|------|----------|
| **GitHub 작업** | 클라우드 CI/CD | GitHub와 긴밀하게 통합되었습니다. YAML 워크플로 |
| **GitLab CI** | 내장 CI/CD | 저장소 + 파이프라인을 위한 단일 플랫폼 |
| **젠킨스** | 자체 호스팅 CI/CD | 고도로 구성 가능; 대규모 플러그인 생태계 |
| **서클CI** | 클라우드 CI/CD | 빠른; 컨테이너화된 워크플로에 적합 |
| **아르고CD** | Kubernetes용 GitOps | 선언적 Git 기반 배포 |
---

## 도커와 컨테이너
### 왜 컨테이너인가?
컨테이너 이전에는 "내 컴퓨터에서 작동한다"는 전형적인 문제가 있었습니다. 컨테이너는 라이브러리, 런타임, 구성 등 모든 종속성을 포함하는 애플리케이션을 어디서나 동일하게 실행되는 이식 가능한 단일 장치로 패키징하여 이 문제를 해결합니다.
### 도커 필수사항
| 개념 | 설명 |
|---------|-------------|
| **이미지** | 앱 + 종속성이 포함된 읽기 전용 템플릿 |
| **컨테이너** | 이미지 인스턴스 실행 |
| **도커파일** | 이미지 구축 레시피 |
| **레지스트리** | 이미지 저장소(Docker Hub, ECR, GCR) |
| **볼륨** | 컨테이너 재시작 후에도 유지되는 영구 스토리지 |
| **네트워크** | 컨테이너를 위한 격리된 네트워킹 계층 |
### Dockerfile 모범 사례
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

주요 사례: 슬림/알파인 기본 이미지 사용, 루트가 아닌 사용자로 실행, 레이어 캐싱 활용,`.dockerignore`사용, 이미지에서 취약점 스캔(`trivy`,`docker scan`), 리소스 제한 설정.
### 도커 작성
여러 컨테이너를 함께 실행하는 경우(앱 + 데이터베이스 + 캐시):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## 쿠버네티스(K8s)
Kubernetes는 업계 표준 컨테이너 오케스트레이터입니다. 컨테이너화된 애플리케이션의 배포, 확장 및 운영을 관리합니다.
### 핵심 아키텍처
| 구성요소 | 역할 |
|------------|------|
| **제어판** | 클러스터 관리(API 서버, 스케줄러, etcd, 컨트롤러 관리자) |
| **노드** | 컨테이너를 실행하는 작업자 머신(VM 또는 물리적) |
| **포드** | 배치 가능한 최소 단위; 네트워킹을 공유하는 하나 이상의 컨테이너 |
| **서비스** | 트래픽을 Pod로 라우팅하는 안정적인 네트워크 엔드포인트 |
| **배포** | 원하는 Pod 상태(복제본, 이미지 등)의 선언적 정의 |
| **인그레스** | 외부 트래픽에 대한 HTTP 라우팅 규칙 |
| **ConfigMap/비밀** | 포드에 주입된 구성 및 민감한 데이터 |
### 필수 kubectl 명령
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### 투구
Helm은 Kubernetes의 패키지 관리자입니다. **차트**는 사전 구성된 Kubernetes 리소스의 번들입니다. K8s의 경우`apt`또는 `brew`라고 생각하세요.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## 코드형 인프라(IaC)
IaC는 애플리케이션 코드를 처리하는 것과 동일한 방식으로 인프라 구성을 처리합니다(버전 관리, 테스트 및 파이프라인을 통한 배포).
### Terraform과 Ansible 비교
| 도구 | 유형 | 접근 | 최고의 대상 |
|------|------|----------|----------|
| **테라폼** | 프로비저닝 | 선언적(HCL); 주 기반 | 클라우드 리소스(VPC, VM, 데이터베이스) 생성 |
| **앤서블** | 구성 | 선언적(YAML); 에이전트 없는 | 서버 구성, 소프트웨어 설치 |
| **풀루미** | 프로비저닝 | 명령형(Python, Go, TS) | 실제 프로그래밍 언어를 선호하는 팀 |
| **클라우드 형성** | 프로비저닝 | 선언적(YAML/JSON); AWS 네이티브 | AWS 전용 인프라 |
### 테라폼 예시
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

모범 사례: 재사용성을 위해 모듈을 사용하고, 상태를 원격으로 저장하고(잠금을 위한 S3 + DynamoDB), 비밀을 하드코딩하지 않으며, 모든 것을 버전 제어합니다.
---

## 모니터링 및 관찰 가능성
### 세 개의 기둥
| 기둥 | 그것이 당신에게 말하는 것 | 도구 |
|---------|------|-------|
| **측정항목** | 시간에 따른 수치 측정(CPU, 요청률, 오류율) | 프로메테우스, CloudWatch, Datadog |
| **로그** | 컨텍스트가 포함된 개별 이벤트(오류, 요청, 상태 변경) | ELK 스택, Loki, CloudWatch 로그 |
| **추적** | 서비스 전반에 걸친 엔드투엔드 요청 여정 | 예거, 엑스레이, 집킨 |
### 프로메테우스 + 그라파나 스택
표준 오픈 소스 모니터링 스택:
| 구성요소 | 역할 |
|------------|------|
| **프로메테우스** | 시계열 데이터베이스; 서비스에서 측정항목을 가져옵니다 |
| **그라파나** | 시각화 및 대시보드 |
| **경고 관리자** | Slack, PagerDuty, 이메일로 경고 라우팅 |
| **노드 내보내기** | 시스템 수준 지표(CPU, RAM, 디스크) 노출 |
| **블랙박스 수출업체** | 프로브 엔드포인트(HTTP, TCP, ICMP) |
### 추적할 주요 지표
| 카테고리 | 측정항목 |
|------------|---------|
| **인프라** | CPU, RAM, 디스크 사용량, 네트워크 I/O |
| **신청** | 요청률, 지연 시간(p50, p95, p99), 오류율 |
| **데이터베이스** | 쿼리 횟수, 느린 쿼리, 연결 풀 사용량 |
| **비즈니스** | 가입, 전환, 수익 |
---

## 배포 전략
| 전략 | 작동 원리 | 위험 | 롤백 |
|----------|-------------|------|----------|
| **지속적 업데이트** | 기존 인스턴스를 새 인스턴스로 점진적으로 교체 | 이전 버전의 일부 사용자, 새 버전의 일부 사용자 | 이전 이미지로 되돌리기 |
| **청록색** | 두 개의 동일한 환경을 실행합니다. 트래픽 전환 | 전환 중 인프라 비용이 두 배로 증가 | 즉시 다시 전환 |
| **카나리** | 적은 양의 트래픽을 새 버전으로 라우팅합니다. 점진적으로 증가 | 복잡한 교통관리 | 안정적인 트래픽을 다시 라우팅 |
| **기능 플래그** | 코드를 배포하지만 토글 뒤에 기능을 숨깁니다 | 조건부 논리로 인한 코드 복잡성 | 끄기 |
---

## 깃옵스
GitOps는 IaC를 논리적인 결론으로 ​​이끌어냅니다. 즉, Git 저장소는 원하는 인프라 및 애플리케이션 상태에 대한 단일 정보 소스입니다.
| 원리 | 설명 |
|------------|-------------|
| **선언적** | 코드(YAML, HCL)로 설명된 모든 것 |
| **버전 있음** | Git은 진실의 원천입니다 |
| **자동** | 도구는 원하는 상태를 실제 상태와 지속적으로 조정합니다 |
| **감사 가능** | 모든 변경 사항은 Git 커밋입니다 |
**ArgoCD** 및 **Flux**는 Kubernetes를 위한 최고의 GitOps 도구입니다. Git 저장소에 변경 사항을 푸시하면 도구가 자동으로 이를 클러스터에 배포합니다.
---

## 사고 대응
오전 3시에 문제가 발생하는 경우:
1. 경고를 **확인**합니다.
2. **범위 평가**: 어떤 서비스, 사용자, 데이터가 영향을 받나요?
3. 근본 원인을 **식별**하세요. 로그, 지표, 최근 배포를 확인하세요.
4. 가능한 경우 **포함** — 회로 차단기, 기능 플래그, 트래픽 이동.
5. **수정** — 롤백 또는 패치 전달.
6. **의사소통** — 이해관계자 및 사용자를 업데이트합니다(상태 페이지).
7. **사후 조사** — 24~48시간 이내에 근본 원인과 조치 항목을 문서화합니다.
단순히 사고를 해결하는 것이 아니라 동일한 사고가 재발하지 않도록 하는 것이 목표입니다.