---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
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
# Docker 和 Kubernetes 備忘單
使用 Docker 容器化應用程式並使用 Kubernetes 編排它們的實用參考。假設對命令列有基本的熟悉。
---

## Docker 基礎知識
|概念 |描述 |
|---------|-------------|
| **圖片** |具有應用程式程式碼 + 依賴項 + 作業系統庫的唯讀範本 |
| **集裝箱** |運行映像實例；隔離進程|
| **Dockerfile** |建構映像的秘訣|
| **註冊表** |映像儲存（Docker Hub、ECR、GCR、GHCR）|
| **成交量** |容器重新啟動後仍然存在的持久存儲 |
| **網路** |虛擬網路連線容器|
---

## 基本 Docker 指令
### 圖片
|命令 |描述 |
|---------|-------------|
|`docker build -t myapp:1.0 .`|從 Dockerfile 建立映像 |
|`docker images`|列出本地圖像 |
|`docker pull nginx:latest`|從登錄中擷取鏡像 |
|`docker push myrepo/myapp:1.0`|將映像推送到註冊表 |
|`docker rmi myapp:1.0`|刪除本機鏡像 |
|`docker tag myapp:1.0 myrepo/myapp:1.0`|為登錄標記圖片 |
|`docker image prune -a`|刪除所有未使用的影像 |
### 容器
|命令 |描述 |
|---------|-------------|
|`docker run -d -p 8080:80 nginx`|後台運行容器，映射埠8080→80 |
|`docker run -it ubuntu bash`|與 shell 互動運作 |
|`docker run --name web -e DB_HOST=db nginx`|設定容器名稱與環境變數 |
|`docker ps`|列出正在運行的容器 |
|`docker ps -a`|列出所有容器（包括已停止的容器） |
|`docker stop web`|停止正在運作的容器 |
|`docker start web`|啟動已停止的容器 |
|`docker rm web`|刪除停止的容器 |
|`docker exec -it web bash`|在正在運作的容器內開啟 shell |
|`docker logs -f web`|關注容器日誌 |
|`docker inspect web`|詳細的容器元資料 (JSON) |
|`docker stats`|所有容器的即時資源使用情況 |
＃＃＃ 清理
|命令 |描述 |
|---------|-------------|
|`docker system prune -a`|刪除所有未使用的容器、映像、網路和建置快取 |
|`docker volume prune`|刪除所有未使用的磁碟區 |
|`docker container prune`|刪除所有停止的容器 |
---

## Dockerfile 參考
### 常用說明
|說明 |目的|範例|
|-------------|---------|---------|
|`FROM`|基礎圖像 |`FROM python:3.12-slim`|
|`WORKDIR`|設定影像內的工作目錄 |`WORKDIR /app`|
|`COPY`|將檔案從主機複製到鏡像 |`COPY requirements.txt .`|
|`ADD`|與 COPY 類似，但也提取 tars 並支援 URL |`ADD app.tar.gz /app/`|
|`RUN`|在建置期間執行指令 |`RUN pip install -r requirements.txt`|
|`CMD`|容器啟動時的預設指令 |`CMD ["python", "app.py"]`|
|`ENTRYPOINT`|固定指令；CMD 成為參數 |`ENTRYPOINT ["python"]`|
|`ENV`|設定環境變數 |`ENV DATABASE_URL=postgres://...`|
|`EXPOSE`|記錄應用程式偵聽的連接埠 |`EXPOSE 8000`|
|`ARG`|建置時變數 |`ARG VERSION=1.0`|
|`USER`|切換到非root用戶|`USER appuser`|
|`HEALTHCHECK`|定義健康檢查指令 |`HEALTHCHECK CMD curl -f http://localhost:8000/health`|
|`VOLUME`|建立掛載點 |`VOLUME /data`|
### 最佳實踐
|實踐|為什麼 |
|----------|-----|
|使用精簡/基礎鏡像 |較小的影像 = 更快的拉取、更小的攻擊面 |
|將 RUN 指令與`&&`組合 |減少影像圖層 |
|先複製依賴文件，再編碼 |利用 Docker 的建置快取 |
|使用`.dockerignore` |排除`node_modules`、`.git`、`__pycache__`|
|以非 root 使用者身分執行 |安全最佳實務 |
|使用多階段建置 |獨立的建置和運行時；較小的最終映像 |
| Pin 基礎鏡像版本 |可重現的建置（`python:3.12.1-slim`，而非`python:latest`）|
### 多階段建置範例
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

## Docker 組合
Docker Compose 在單一 YAML 檔案中定義多容器應用程式。
### 按鍵命令
|命令 |描述 |
|---------|-------------|
|`docker compose up -d`|在背景啟動所有服務 |
|`docker compose down`|停止並刪除容器、網路 |
|`docker compose down -v`|同時刪除磁碟區 |
|`docker compose logs -f`|關注所有服務的日誌 |
|`docker compose ps`|列出正在運行的服務 |
|`docker compose build`|重建影像 |
|`docker compose exec web bash`|在正在運行的服務中執行命令 |
|`docker compose pull`|拉取最新鏡像 |
### 撰寫文件範例
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

## Kubernetes 架構
|組件|角色 |
|------------|------|
| **叢集** |一組運行容器化應用程式的節點（機器）
| **控制平面** | API 伺服器、排程器、控制器管理器、etcd（叢集狀態）|
| **節點** |執行 Pod 的工作機器（VM 或實體）|
| **吊艙** |最小單位；一個或多個緊密耦合的容器|
| **部署** |管理 Pod 的副本；處理滾動更新|
| **服务** |一组 Pod 的稳定网络端点 |
| **入口** |從叢集外部到服務的 HTTP 路由
| **配置映射** |非秘密配置数据 |
| **秘密** |敏感数据（base64 编码）|
| **命名空间** |集群内逻辑隔离|
| **持續成交量 (PV)** |叢集級儲存資源|
| **持久性成交量聲明 (PVC)** | pod 的儲存請求 |
---

## kubectl 指令
### 叢集資訊
|命令 |描述 |
|---------|-------------|
|`kubectl cluster-info`|叢集端點詳細資料 |
|`kubectl get nodes`|列出所有節點 |
|`kubectl get namespaces`|列出命名空間 |
|`kubectl config current-context`|顯示目前叢集上下文 |
|`kubectl config use-context prod`|切換上下文 |
### 工作負載
|命令 |描述 |
|---------|-------------|
|`kubectl get pods`|列出目前命名空間中的 Pod |
|`kubectl get pods -A`|列出所有命名空間中的 pod |
|`kubectl get deployments`|列出部署 |
|`kubectl get services`|列出服務 |
|`kubectl get ingress`|列出入口資源 |
|`kubectl describe pod <name>`|詳細的 Pod 資訊（事件、狀態、規格）|
|`kubectl logs <pod>`|查看 Pod 日誌 |
|`kubectl logs -f <pod>`|關注 pod 日誌 |
|`kubectl logs <pod> -c <container>`|來自多容器 Pod 中特定容器的日誌 |
|`kubectl exec -it <pod> -- bash`|殼成豆莢 |
|`kubectl delete pod <name>`|刪除 Pod（它將由其控制器重新建立）|
|`kubectl rollout status deployment/<name>`|檢查推出進度 |
|`kubectl rollout undo deployment/<name>`|回滾到之前的版本 |
### 應用程式配置
|命令 |描述 |
|---------|-------------|
|`kubectl apply -f deployment.yaml`|應用 YAML 清單 |
|`kubectl apply -f ./dir/`|應用目錄中的所有 YAML 檔案 |
|`kubectl delete -f deployment.yaml`|刪除 YAML 檔案中定義的資源 |
|`kubectl scale deployment/web --replicas=5`|擴充部署 |
|`kubectl set image deployment/web web=myapp:2.0`|更新容器鏡像 |
---

## 常見的 Kubernetes 清單
### 部署
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

＃＃＃ 服務
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

### 入口
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

## 頭盔基礎知識
Helm 是 Kubernetes 的套件管理器。它將 Kubernetes 資源打包成可重複使用的圖表。
|命令 |描述 |
|---------|-------------|
|`helm repo add bitnami https://charts.bitnami.com/bitnami`|新增圖表儲存庫 |
|`helm repo update`|更新本機圖表索引 |
|`helm search repo nginx`|搜尋圖表 |
|`helm install my-release bitnami/nginx`|安裝圖表 |
|`helm install my-release bitnami/nginx --set replicaCount=3`|使用自訂值安裝 |
|`helm install my-release bitnami/nginx -f values.yaml`|使用值檔安裝 |
|`helm list`|列出已安裝的版本 |
|`helm upgrade my-release bitnami/nginx --set image.tag=2.0`|升級版本 |
|`helm rollback my-release 1`|回滾到以前的修訂版 |
|`helm uninstall my-release`|卸載版本 |
|`helm status my-release`|顯示發佈狀態 |
---

## 故障排除快速參考
|問題 |嘗試的命令 |
|---------|----------------|
| Pod 未啟動 |`kubectl describe pod <name>`→ 檢視活動 |
|崩潰環回關閉 |`kubectl logs <pod> --previous`→ 看看它崩潰的原因 |
|圖片拉取錯誤 |檢查映像名稱、標籤和登錄憑證 |
|服務無法存取 |`kubectl get endpoints <service>`→ 是否選擇了 Pod？ |
| OOM 被殺 |增加記憶體限製或優化應用記憶體使用 |
|待處理的豆莢 |`kubectl describe pod`→ 檢查節點資源、污點、關聯性 |
| DNS 問題 |`kubectl exec <pod> -- nslookup kubernetes.default`|