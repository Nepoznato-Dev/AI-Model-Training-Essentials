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
# Docker 和 Kubernetes 备忘单
使用 Docker 容器化应用程序并使用 Kubernetes 编排它们的实用参考。假设对命令行有基本的熟悉。
---

## Docker 基础知识
|概念 |描述 |
|---------|-------------|
| **图片** |具有应用程序代码 + 依赖项 + 操作系统库的只读模板 |
| **集装箱** |运行图像实例；隔离进程|
| **Dockerfile** |构建图像的秘诀|
| **注册表** |图像存储（Docker Hub、ECR、GCR、GHCR）|
| **成交量** |容器重启后仍然存在的持久存储 |
| **网络** |虚拟网络连接容器|
---

## 基本 Docker 命令
### 图片
|命令 |描述 |
|---------|-------------|
| `docker build -t myapp:1.0 .`|从 Dockerfile 构建镜像 |
| `docker images`|列出本地图像 |
| `docker pull nginx:latest`|从注册表中提取镜像 |
| `docker push myrepo/myapp:1.0`|将图像推送到注册表 |
| `docker rmi myapp:1.0`|删除本地镜像 |
| `docker tag myapp:1.0 myrepo/myapp:1.0`|为注册表标记图像 |
| `docker image prune -a`|删除所有未使用的图像 |
### 容器
|命令 |描述 |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`|后台运行容器，映射端口8080→80 |
| `docker run -it ubuntu bash`|与 shell 交互运行 |
| `docker run --name web -e DB_HOST=db nginx`|设置容器名称和环境变量 |
| `docker ps`|列出正在运行的容器 |
| `docker ps -a`|列出所有容器（包括已停止的容器） |
| `docker stop web`|停止正在运行的容器 |
| `docker start web`|启动已停止的容器 |
| `docker rm web`|删除停止的容器 |
| `docker exec -it web bash`|在正在运行的容器内打开 shell |
| `docker logs -f web`|关注容器日志 |
| `docker inspect web`|详细的容器元数据 (JSON) |
| `docker stats`|所有容器的实时资源使用情况 |
＃＃＃ 清理
|命令 |描述 |
|---------|-------------|
| `docker system prune -a`|删除所有未使用的容器、图像、网络和构建缓存 |
| `docker volume prune`|删除所有未使用的卷 |
| `docker container prune`|删除所有停止的容器 |
---

## Dockerfile 参考
### 常用说明
|说明 |目的|示例|
|-------------|---------|---------|
| `FROM`|基础图像 | `FROM python:3.12-slim`|
| `WORKDIR`|设置图像内的工作目录 | `WORKDIR /app`|
| `COPY`|将文件从主机复制到镜像 | `COPY requirements.txt .`|
| `ADD`|与 COPY 类似，但也提取 tars 并支持 URL | `ADD app.tar.gz /app/`|
| `RUN`|在构建期间执行命令 | `RUN pip install -r requirements.txt`|
| `CMD`|容器启动时的默认命令 | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`|固定命令； CMD 成为参数 | `ENTRYPOINT ["python"]`|
| `ENV`|设置环境变量 | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`|记录应用程序侦听的端口 | `EXPOSE 8000`|
| `ARG`|构建时变量 | `ARG VERSION=1.0`|
| `USER`|切换到非root用户| `USER appuser`|
| `HEALTHCHECK`|定义健康检查命令 | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`|创建挂载点 | `VOLUME /data`|
### 最佳实践
|实践|为什么 |
|----------|-----|
|使用精简/基础镜像 |较小的图像 = 更快的拉取、更小的攻击面 |
|将 RUN 命令与`&&`组合 |减少图像层 |
|先复制依赖文件，再编码 |利用 Docker 的构建缓存 |
|使用`.dockerignore` |排除`node_modules`、`.git`、`__pycache__`|
|以非 root 用户身份运行 |安全最佳实践 |
|使用多阶段构建 |独立的构建和运行时；较小的最终图像 |
| Pin 基础镜像版本 |可重现的构建（`python:3.12.1-slim`，而不是`python:latest`）|
### 多阶段构建示例
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

## Docker 组合
Docker Compose 在单个 YAML 文件中定义多容器应用程序。
### 按键命令
|命令 |描述 |
|---------|-------------|
| `docker compose up -d`|在后台启动所有服务 |
| `docker compose down`|停止并删除容器、网络 |
| `docker compose down -v`|同时删除卷 |
| `docker compose logs -f`|关注所有服务的日志 |
| `docker compose ps`|列出正在运行的服务 |
| `docker compose build`|重建图像 |
| `docker compose exec web bash`|在正在运行的服务中运行命令 |
| `docker compose pull`|拉取最新镜像 |
### 撰写文件示例
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

## Kubernetes 架构
|组件|角色 |
|------------|------|
| **集群** |一组运行容器化应用程序的节点（机器）
| **控制平面** | API 服务器、调度程序、控制器管理器、etcd（集群状态）|
| **节点** |运行 Pod 的工作机器（VM 或物理）|
| **吊舱** |最小单位；一个或多个紧密耦合的容器|
| **部署** |管理 Pod 的副本；处理滚动更新|
| **服务** |一组 Pod 的稳定网络端点 |
| **入口** |从集群外部到服务的 HTTP 路由
| **配置映射** |非秘密配置数据 |
| **秘密** |敏感数据（base64 编码）|
| **命名空间** |集群内逻辑隔离|
| **持续成交量 (PV)** |集群级存储资源|
| **持久成交量声明 (PVC)** | pod 的存储请求 |
---

## kubectl 命令
### 集群信息
|命令 |描述 |
|---------|-------------|
| `kubectl cluster-info`|集群端点详细信息 |
| `kubectl get nodes`|列出所有节点 |
| `kubectl get namespaces`|列出命名空间 |
| `kubectl config current-context`|显示当前集群上下文 |
| `kubectl config use-context prod`|切换上下文 |
### 工作负载
|命令 |描述 |
|---------|-------------|
| `kubectl get pods`|列出当前命名空间中的 Pod |
| `kubectl get pods -A`|列出所有命名空间中的 pod |
| `kubectl get deployments`|列出部署 |
| `kubectl get services`|列出服务 |
| `kubectl get ingress`|列出入口资源 |
| `kubectl describe pod <name>`|详细的 Pod 信息（事件、状态、规格）|
| `kubectl logs <pod>`|查看 Pod 日志 |
| `kubectl logs -f <pod>`|关注 pod 日志 |
| `kubectl logs <pod> -c <container>`|来自多容器 Pod 中特定容器的日志 |
| `kubectl exec -it <pod> -- bash`|壳成豆荚 |
| `kubectl delete pod <name>`|删除 Pod（它将由其控制器重新创建）|
| `kubectl rollout status deployment/<name>`|检查推出进度 |
| `kubectl rollout undo deployment/<name>`|回滚到之前的版本 |
### 应用配置
|命令 |描述 |
|---------|-------------|
| `kubectl apply -f deployment.yaml`|应用 YAML 清单 |
| `kubectl apply -f ./dir/`|应用目录中的所有 YAML 文件 |
| `kubectl delete -f deployment.yaml`|删除 YAML 文件中定义的资源 |
| `kubectl scale deployment/web --replicas=5`|扩展部署 |
| `kubectl set image deployment/web web=myapp:2.0`|更新容器镜像 |
---

## 常见的 Kubernetes 清单
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

＃＃＃ 服务
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

## 头盔基础知识
Helm 是 Kubernetes 的包管理器。它将 Kubernetes 资源打包成可重用的图表。
|命令 |描述 |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`|添加图表存储库 |
| `helm repo update`|更新本地图表索引 |
| `helm search repo nginx`|搜索图表 |
| `helm install my-release bitnami/nginx`|安装图表 |
| `helm install my-release bitnami/nginx --set replicaCount=3`|使用自定义值安装 |
| `helm install my-release bitnami/nginx -f values.yaml`|使用值文件安装 |
| `helm list`|列出已安装的版本 |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`|升级版本 |
| `helm rollback my-release 1`|回滚到以前的修订版 |
| `helm uninstall my-release`|卸载版本 |
| `helm status my-release`|显示发布状态 |
---

## 故障排除快速参考
|问题 |尝试的命令 |
|---------|----------------|
| Pod 未启动 | `kubectl describe pod <name>`→ 查看活动 |
|崩溃环回关闭 | `kubectl logs <pod> --previous`→ 看看它崩溃的原因 |
|图片拉取错误 |检查映像名称、标签和注册表凭据 |
|服务无法访问 | `kubectl get endpoints <service>`→ 是否选择了 Pod？ |
| OOM 被杀 |增加内存限制或优化应用内存使用 |
|待处理的豆荚 | `kubectl describe pod`→ 检查节点资源、污点、关联性 |
| DNS 问题 | `kubectl exec <pod> -- nslookup kubernetes.default`|