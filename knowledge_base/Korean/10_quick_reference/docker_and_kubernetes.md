---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
category: "Quick Reference"
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
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [docker, kubernetes, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Docker 및 Kubernetes 치트 시트
Docker를 사용하여 애플리케이션을 컨테이너화하고 Kubernetes를 사용하여 조정하는 데 대한 실제 참조입니다. 명령줄에 대한 기본적인 지식이 있다고 가정합니다.
---

## 도커 기초
| 개념 | 설명 |
|---------|-------------|
| **이미지** | 앱 코드 + 종속성 + OS 라이브러리가 포함된 읽기 전용 템플릿 |
| **컨테이너** | 이미지의 인스턴스를 실행 중입니다. 격리된 프로세스 |
| **도커파일** | 이미지 구축 레시피 |
| **레지스트리** | 이미지 저장소(Docker Hub, ECR, GCR, GHCR) |
| **볼륨** | 컨테이너 재시작 후에도 유지되는 영구 스토리지 |
| **네트워크** | 컨테이너를 연결하는 가상 네트워크 |
---

## 필수 Docker 명령
### 이미지
| 명령 | 설명 |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Dockerfile에서 이미지 빌드 |
| `docker images`| 로컬 이미지 나열 |
| `docker pull nginx:latest`| 레지스트리에서 이미지 가져오기 |
| `docker push myrepo/myapp:1.0`| 이미지를 레지스트리에 푸시 |
| `docker rmi myapp:1.0`| 로컬 이미지 제거 |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| 레지스트리 이미지에 태그 지정 |
| `docker image prune -a`| 사용하지 않는 이미지를 모두 제거 |
### 컨테이너
| 명령 | 설명 |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| 백그라운드에서 컨테이너를 실행하고 포트 8080→80을 매핑 |
| `docker run -it ubuntu bash`| 셸을 사용하여 대화형으로 실행 |
| `docker run --name web -e DB_HOST=db nginx`| 컨테이너 이름 및 환경 변수 설정 |
| `docker ps`| 실행 중인 컨테이너 나열 |
| `docker ps -a`| 모든 컨테이너 나열(중지된 컨테이너 포함) |
| `docker stop web`| 실행 중인 컨테이너 중지 |
| `docker start web`| 중지된 컨테이너 시작 |
| `docker rm web`| 중지된 컨테이너 제거 |
| `docker exec -it web bash`| 실행 중인 컨테이너 내에서 셸 열기 |
| `docker logs -f web`| 컨테이너 로그 따르기 |
| `docker inspect web`| 상세한 컨테이너 메타데이터(JSON) |
| `docker stats`| 모든 컨테이너의 실시간 리소스 사용량 |
### 정리
| 명령 | 설명 |
|---------|-------------|
| `docker system prune -a`| 사용하지 않는 모든 컨테이너, 이미지, 네트워크 및 빌드 캐시 제거 |
| `docker volume prune`| 사용하지 않는 모든 볼륨을 제거 |
| `docker container prune`| 중지된 모든 컨테이너 제거 |
---

## Dockerfile 참조
### 공통 지침
| 지시 | 목적 | 예 |
|-------------|---------|---------|
| `FROM`| 기본 이미지 | `FROM python:3.12-slim`|
| `WORKDIR`| 이미지 내부에 작업 디렉터리 설정 | `WORKDIR /app`|
| `COPY`| 호스트의 파일을 이미지로 복사 | `COPY requirements.txt .`|
| `ADD`| COPY와 유사하지만 tar도 추출하고 URL도 지원합니다 | `ADD app.tar.gz /app/`|
| `RUN`| 빌드 중에 명령 실행 | `RUN pip install -r requirements.txt`|
| `CMD`| 컨테이너 시작 시 기본 명령 | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| 고정 명령; CMD가 인수가 됨 | `ENTRYPOINT ["python"]`|
| `ENV`| 환경 변수 설정 | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| 앱이 수신 대기하는 포트를 문서화하세요 | `EXPOSE 8000`|
| `ARG`| 빌드타임 변수 | `ARG VERSION=1.0`|
| `USER`| 루트가 아닌 사용자로 전환 | `USER appuser`|
| `HEALTHCHECK`| 상태 확인 명령 정의 | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| 마운트 지점 생성 | `VOLUME /data`|
### 모범 사례
| 연습 | 왜 |
|------------|-----|
| 슬림/기본 이미지 사용 | 더 작은 이미지 = 더 빠른 풀, 더 작은 공격 표면 |
| RUN 명령을 `&&`와 결합 | 이미지 레이어 감소 |
| 종속성 파일을 먼저 복사한 다음 코드 | Docker의 빌드 캐시 활용 |
|`.dockerignore`사용 |`node_modules`,`.git`,`__pycache__`제외 |
| 루트가 아닌 사용자로 실행 | 보안 모범 사례 |
| 다단계 빌드 사용 | 빌드와 런타임을 분리하세요. 더 작은 최종 이미지 |
| 기본 이미지 버전 고정 | 재현 가능한 빌드(`python:3.12.1-slim`,`python:latest`아님) |
### 다단계 빌드 예
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

---

## 도커 작성
Docker Compose는 단일 YAML 파일에 다중 컨테이너 애플리케이션을 정의합니다.
### 주요 명령
| 명령 | 설명 |
|---------|-------------|
| `docker compose up -d`| 백그라운드에서 모든 서비스 시작 |
| `docker compose down`| 컨테이너, 네트워크 중지 및 제거 |
| `docker compose down -v`| 볼륨도 제거 |
| `docker compose logs -f`| 모든 서비스의 로그 팔로우 |
| `docker compose ps`| 실행 중인 서비스 나열 |
| `docker compose build`| 이미지 재구축 |
| `docker compose exec web bash`| 실행 중인 서비스에서 명령 실행 |
| `docker compose pull`| 최신 이미지 가져오기 |
### 작성 파일 예시
```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

---

## 쿠버네티스 아키텍처
| 구성요소 | 역할 |
|------------|------|
| **클러스터** | 컨테이너화된 애플리케이션을 실행하는 노드(머신) 세트 |
| **제어판** | API 서버, 스케줄러, 컨트롤러 관리자, etcd(클러스터 상태) |
| **노드** | 포드를 실행하는 작업자 머신(VM 또는 물리적) |
| **포드** | 최소단위; 하나 이상의 긴밀하게 결합된 컨테이너 |
| **배포** | Pod의 복제본을 관리합니다. 롤링 업데이트 처리 |
| **서비스** | 포드 세트에 대한 안정적인 네트워크 엔드포인트 |
| **인그레스** | 클러스터 외부에서 서비스로의 HTTP 라우팅 |
| **구성 맵** | 비밀이 아닌 구성 데이터 |
| **비밀** | 민감한 데이터(base64 인코딩) |
| **네임스페이스** | 클러스터 내 논리적 격리 |
| **영구 볼륨(PV)** | 클러스터 수준 스토리지 리소스 |
| **영구 볼륨 청구(PVC)** | 포드별 저장 요청 |
---

## kubectl 명령
### 클러스터 정보
| 명령 | 설명 |
|---------|-------------|
| `kubectl cluster-info`| 클러스터 엔드포인트 세부정보 |
| `kubectl get nodes`| 모든 노드 나열 |
| `kubectl get namespaces`| 네임스페이스 나열 |
| `kubectl config current-context`| 현재 클러스터 컨텍스트 표시 |
| `kubectl config use-context prod`| 컨텍스트 전환 |
### 워크로드
| 명령 | 설명 |
|---------|-------------|
| `kubectl get pods`| 현재 네임스페이스의 Pod 나열 |
| `kubectl get pods -A`| 모든 네임스페이스에 걸쳐 Pod 나열 |
| `kubectl get deployments`| 배포 나열 |
| `kubectl get services`| 서비스 나열 |
| `kubectl get ingress`| 수신 리소스 나열 |
| `kubectl describe pod <name>`| 자세한 포드 정보(이벤트, 상태, 사양) |
| `kubectl logs <pod>`| 포드 로그 보기 |
| `kubectl logs -f <pod>`| 포드 로그 팔로우 |
| `kubectl logs <pod> -c <container>`| 다중 컨테이너 포드에 있는 특정 컨테이너의 로그 |
| `kubectl exec -it <pod> -- bash`| 포드에 쉘 |
| `kubectl delete pod <name>`| 포드 삭제(컨트롤러에 의해 다시 생성됨) |
| `kubectl rollout status deployment/<name>`| 출시 진행 상황 확인 |
| `kubectl rollout undo deployment/<name>`| 이전 버전으로 롤백 |
### 구성 적용 중
| 명령 | 설명 |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| YAML 매니페스트 적용 |
| `kubectl apply -f ./dir/`| 디렉터리의 모든 YAML 파일 적용 |
| `kubectl delete -f deployment.yaml`| YAML 파일에 정의된 리소스 삭제 |
| `kubectl scale deployment/web --replicas=5`| 배포 확장 |
| `kubectl set image deployment/web web=myapp:2.0`| 컨테이너 이미지 업데이트 |
---

## 일반적인 Kubernetes 매니페스트
### 배포
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### 서비스
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP    # Internal only
  # type: LoadBalancer  # External (cloud provider)
  # type: NodePort      # External via node IP + port
```

### 인그레스
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
```

---

## 헬름 기본 사항
Helm은 Kubernetes의 패키지 관리자입니다. Kubernetes 리소스를 재사용 가능한 차트로 패키징합니다.
| 명령 | 설명 |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| 차트 저장소 추가 |
| `helm repo update`| 지역 차트 색인 업데이트 |
| `helm search repo nginx`| 차트 검색 |
| `helm install my-release bitnami/nginx`| 차트 설치 |
| `helm install my-release bitnami/nginx --set replicaCount=3`| 사용자 정의 값으로 설치 |
| `helm install my-release bitnami/nginx -f values.yaml`| 값 파일을 사용하여 설치 |
| `helm list`| 설치된 릴리스 나열 |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| 릴리스 업그레이드 |
| `helm rollback my-release 1`| 이전 버전으로 롤백 |
| `helm uninstall my-release`| 릴리스 제거 |
| `helm status my-release`| 릴리스 상태 표시 |
---

## 문제 해결 빠른 참조
| 문제 | 시도해 볼 명령 |
|---------|---|
| 포드가 시작되지 않음 | `kubectl describe pod <name>`→ 이벤트 확인 |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ 충돌 이유 확인 |
| 이미지 가져오기 오류 | 이미지 이름, 태그 및 레지스트리 자격 증명 확인 |
| 서비스에 연결할 수 없음 | `kubectl get endpoints <service>`→ 포드가 선택되었나요? |
| OOM킬드 | 메모리 제한 늘리기 또는 앱 메모리 사용량 최적화 |
| 보류 중인 포드 | `kubectl describe pod`→ 노드 리소스, 오염, 선호도 확인 |
| DNS 문제 | `kubectl exec <pod> -- nslookup kubernetes.default`|