---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.1"
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
# Docker and Kubernetes Cheat Sheet

A practical reference for containerising applications with Docker and orchestrating them with Kubernetes. Assumes basic familiarity with the command line.

---

## Docker Fundamentals

| Concept | Description |
|---------|-------------|
| **Image** | Read-only template with app code + dependencies + OS libraries |
| **Container** | Running instance of an image; isolated process |
| **Dockerfile** | Recipe for building an image |
| **Registry** | Storage for images (Docker Hub, ECR, GCR, GHCR) |
| **Volume** | Persistent storage that survives container restarts |
| **Network** | Virtual network connecting containers |

---

## Essential Docker Commands

### Images

| Command | Description |
|---------|-------------|
| `docker build -t myapp:1.0 .` | Build an image from a Dockerfile |
| `docker images` | List local images |
| `docker pull nginx:latest` | Pull an image from a registry |
| `docker push myrepo/myapp:1.0` | Push an image to a registry |
| `docker rmi myapp:1.0` | Remove a local image |
| `docker tag myapp:1.0 myrepo/myapp:1.0` | Tag an image for a registry |
| `docker image prune -a` | Remove all unused images |

### Containers

| Command | Description |
|---------|-------------|
| `docker run -d -p 8080:80 nginx` | Run a container in background, map port 8080→80 |
| `docker run -it ubuntu bash` | Run interactively with a shell |
| `docker run --name web -e DB_HOST=db nginx` | Set container name and environment variable |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker stop web` | Stop a running container |
| `docker start web` | Start a stopped container |
| `docker rm web` | Remove a stopped container |
| `docker exec -it web bash` | Open a shell inside a running container |
| `docker logs -f web` | Follow container logs |
| `docker inspect web` | Detailed container metadata (JSON) |
| `docker stats` | Live resource usage for all containers |

### Cleanup

| Command | Description |
|---------|-------------|
| `docker system prune -a` | Remove all unused containers, images, networks, and build cache |
| `docker volume prune` | Remove all unused volumes |
| `docker container prune` | Remove all stopped containers |

---

## Dockerfile Reference

### Common Instructions

| Instruction | Purpose | Example |
|-------------|---------|---------|
| `FROM` | Base image | `FROM python:3.12-slim` |
| `WORKDIR` | Set working directory inside the image | `WORKDIR /app` |
| `COPY` | Copy files from host into image | `COPY requirements.txt .` |
| `ADD` | Like COPY, but also extracts tars and supports URLs | `ADD app.tar.gz /app/` |
| `RUN` | Execute a command during build | `RUN pip install -r requirements.txt` |
| `CMD` | Default command when container starts | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | Fixed command; CMD becomes arguments | `ENTRYPOINT ["python"]` |
| `ENV` | Set environment variable | `ENV DATABASE_URL=postgres://...` |
| `EXPOSE` | Document which port the app listens on | `EXPOSE 8000` |
| `ARG` | Build-time variable | `ARG VERSION=1.0` |
| `USER` | Switch to non-root user | `USER appuser` |
| `HEALTHCHECK` | Define a health check command | `HEALTHCHECK CMD curl -f http://localhost:8000/health` |
| `VOLUME` | Create a mount point | `VOLUME /data` |

### Best Practices

| Practice | Why |
|----------|-----|
| Use slim/base images | Smaller images = faster pulls, smaller attack surface |
| Combine RUN commands with `&&` | Reduces image layers |
| Copy dependency files first, then code | Leverages Docker's build cache |
| Use `.dockerignore` | Exclude `node_modules`, `.git`, `__pycache__` |
| Run as non-root user | Security best practice |
| Use multi-stage builds | Separate build and runtime; smaller final image |
| Pin base image versions | Reproducible builds (`python:3.12.1-slim`, not `python:latest`) |

### Multi-Stage Build Example

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

## Docker Compose

Docker Compose defines multi-container applications in a single YAML file.

### Key Commands

| Command | Description |
|---------|-------------|
| `docker compose up -d` | Start all services in background |
| `docker compose down` | Stop and remove containers, networks |
| `docker compose down -v` | Also remove volumes |
| `docker compose logs -f` | Follow logs from all services |
| `docker compose ps` | List running services |
| `docker compose build` | Rebuild images |
| `docker compose exec web bash` | Run command in a running service |
| `docker compose pull` | Pull latest images |

### Example Compose File

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

## Kubernetes Architecture

| Component | Role |
|-----------|------|
| **Cluster** | A set of nodes (machines) running containerised applications |
| **Control Plane** | API server, scheduler, controller manager, etcd (cluster state) |
| **Node** | A worker machine (VM or physical) that runs pods |
| **Pod** | Smallest unit; one or more tightly coupled containers |
| **Deployment** | Manages replicas of a pod; handles rolling updates |
| **Service** | Stable network endpoint for a set of pods |
| **Ingress** | HTTP routing from outside the cluster to services |
| **ConfigMap** | Non-secret configuration data |
| **Secret** | Sensitive data (base64-encoded) |
| **Namespace** | Logical isolation within a cluster |
| **PersistentVolume (PV)** | Cluster-level storage resource |
| **PersistentVolumeClaim (PVC)** | Request for storage by a pod |

---

## kubectl Commands

### Cluster Info

| Command | Description |
|---------|-------------|
| `kubectl cluster-info` | Cluster endpoint details |
| `kubectl get nodes` | List all nodes |
| `kubectl get namespaces` | List namespaces |
| `kubectl config current-context` | Show current cluster context |
| `kubectl config use-context prod` | Switch context |

### Workloads

| Command | Description |
|---------|-------------|
| `kubectl get pods` | List pods in current namespace |
| `kubectl get pods -A` | List pods across all namespaces |
| `kubectl get deployments` | List deployments |
| `kubectl get services` | List services |
| `kubectl get ingress` | List ingress resources |
| `kubectl describe pod <name>` | Detailed pod info (events, status, specs) |
| `kubectl logs <pod>` | View pod logs |
| `kubectl logs -f <pod>` | Follow pod logs |
| `kubectl logs <pod> -c <container>` | Logs from a specific container in a multi-container pod |
| `kubectl exec -it <pod> -- bash` | Shell into a pod |
| `kubectl delete pod <name>` | Delete a pod (it will be recreated by its controller) |
| `kubectl rollout status deployment/<name>` | Check rollout progress |
| `kubectl rollout undo deployment/<name>` | Roll back to previous version |

### Applying Configuration

| Command | Description |
|---------|-------------|
| `kubectl apply -f deployment.yaml` | Apply a YAML manifest |
| `kubectl apply -f ./dir/` | Apply all YAML files in a directory |
| `kubectl delete -f deployment.yaml` | Delete resources defined in a YAML file |
| `kubectl scale deployment/web --replicas=5` | Scale a deployment |
| `kubectl set image deployment/web web=myapp:2.0` | Update container image |

---

## Common Kubernetes Manifests

### Deployment

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

### Service

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

### Ingress

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

## Helm Basics

Helm is the package manager for Kubernetes. It packages Kubernetes resources into reusable charts.

| Command | Description |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami` | Add a chart repository |
| `helm repo update` | Update local chart index |
| `helm search repo nginx` | Search for a chart |
| `helm install my-release bitnami/nginx` | Install a chart |
| `helm install my-release bitnami/nginx --set replicaCount=3` | Install with custom values |
| `helm install my-release bitnami/nginx -f values.yaml` | Install with a values file |
| `helm list` | List installed releases |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0` | Upgrade a release |
| `helm rollback my-release 1` | Roll back to a previous revision |
| `helm uninstall my-release` | Uninstall a release |
| `helm status my-release` | Show release status |

---

## Troubleshooting Quick Reference

| Problem | Commands to Try |
|---------|----------------|
| Pod not starting | `kubectl describe pod <name>` → check Events |
| CrashLoopBackOff | `kubectl logs <pod> --previous` → see why it crashed |
| Image pull error | Check image name, tag, and registry credentials |
| Service not reachable | `kubectl get endpoints <service>` → are pods selected? |
| OOMKilled | Increase memory limits or optimise app memory usage |
| Pending pods | `kubectl describe pod` → check node resources, taints, affinity |
| DNS issues | `kubectl exec <pod> -- nslookup kubernetes.default` |
