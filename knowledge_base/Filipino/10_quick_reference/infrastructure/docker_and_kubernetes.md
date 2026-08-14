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
# Docker at Kubernetes Cheat Sheet
Isang praktikal na sanggunian para sa paglalagay ng container ng mga application sa Docker at pag-orkestra sa mga ito gamit ang Kubernetes. Ipinapalagay ang pangunahing pamilyar sa command line.
---

## Docker Fundamentals
| Konsepto | Paglalarawan |
|---------|-------------|
| **Larawan** | Read-only na template na may app code + dependencies + OS library |
| **Lalagyan** | Running instance ng isang imahe; nakahiwalay na proseso |
| **Dockerfile** | Recipe para sa pagbuo ng isang imahe |
| **Registry** | Imbakan para sa mga larawan (Docker Hub, ECR, GCR, GHCR) |
| **Dami** | Ang tuluy-tuloy na storage na nananatili sa container ay nag-restart |
| **Network** | Virtual network na kumukonekta sa mga container |
---

## Mahahalagang Docker Command
### Mga larawan
| Utos | Paglalarawan |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Bumuo ng isang imahe mula sa isang Dockerfile |
| `docker images`| Maglista ng mga lokal na larawan |
| `docker pull nginx:latest`| Hilahin ang isang imahe mula sa isang registry |
| `docker push myrepo/myapp:1.0`| Itulak ang isang imahe sa isang registry |
| `docker rmi myapp:1.0`| Mag-alis ng lokal na larawan |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Mag-tag ng larawan para sa isang registry |
| `docker image prune -a`| Alisin ang lahat ng hindi nagamit na larawan |
### Mga lalagyan
| Utos | Paglalarawan |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Magpatakbo ng container sa background, mapa port 8080→80 |
| `docker run -it ubuntu bash`| Patakbuhin nang interactive na may shell |
| `docker run --name web -e DB_HOST=db nginx`| Itakda ang pangalan ng container at variable ng kapaligiran |
| `docker ps`| Maglista ng mga tumatakbong lalagyan |
| `docker ps -a`| Ilista ang lahat ng mga lalagyan (kabilang ang huminto) |
| `docker stop web`| Ihinto ang tumatakbong lalagyan |
| `docker start web`| Magsimula ng huminto na lalagyan |
| `docker rm web`| Mag-alis ng huminto na lalagyan |
| `docker exec -it web bash`| Magbukas ng shell sa loob ng tumatakbong lalagyan |
| `docker logs -f web`| Sundin ang mga log ng container |
| `docker inspect web`| Detalyadong container metadata (JSON) |
| `docker stats`| Live na paggamit ng mapagkukunan para sa lahat ng container |
### Paglilinis
| Utos | Paglalarawan |
|---------|-------------|
| `docker system prune -a`| Alisin ang lahat ng hindi nagamit na lalagyan, larawan, network, at bumuo ng cache |
| `docker volume prune`| Alisin ang lahat ng hindi nagamit na volume |
| `docker container prune`| Alisin ang lahat ng nakahintong container |
---

## Reference ng Dockerfile
### Mga Karaniwang Tagubilin
| Tagubilin | Layunin | Halimbawa |
|-------------|---------|---------|
| `FROM`| Batayang larawan | `FROM python:3.12-slim`|
| `WORKDIR`| Itakda ang gumaganang direktoryo sa loob ng larawan | `WORKDIR /app`|
| `COPY`| Kopyahin ang mga file mula sa host patungo sa larawan | `COPY requirements.txt .`|
| `ADD`| Tulad ng COPY, ngunit nag-extract din ng mga tar at sumusuporta sa mga URL | `ADD app.tar.gz /app/`|
| `RUN`| Magsagawa ng utos sa panahon ng build | `RUN pip install -r requirements.txt`|
| `CMD`| Default na command kapag nagsimula ang container | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Nakapirming utos; Nagiging argumento ang CMD | `ENTRYPOINT ["python"]`|
| `ENV`| Itakda ang variable ng kapaligiran | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Idokumento kung aling port ang pinapakinggan ng app sa | `EXPOSE 8000`|
| `ARG`| Variable ng Build-time | `ARG VERSION=1.0`|
| `USER`| Lumipat sa non-root user | `USER appuser`|
| `HEALTHCHECK`| Tukuyin ang isang utos ng pagsusuri sa kalusugan | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Gumawa ng mount point | `VOLUME /data`|
### Pinakamahuhusay na Kasanayan
| Magsanay | Bakit |
|----------|-----|
| Gumamit ng mga slim/base na larawan | Mas maliliit na larawan = mas mabilis na paghila, mas maliit na atake sa ibabaw |
| Pagsamahin ang mga RUN command sa`&&`| Binabawasan ang mga layer ng larawan |
| Kopyahin muna ang mga dependency file, pagkatapos ay code | Pinakikinabangan ang build cache ng Docker |
| Gamitin ang`.dockerignore`| Ibukod ang`node_modules`,`.git`,`__pycache__`|
| Patakbuhin bilang non-root user | Pinakamahusay na kasanayan sa seguridad |
| Gumamit ng mga multi-stage na build | Paghiwalayin ang build at runtime; mas maliit na huling larawan |
| I-pin ang base na mga bersyon ng imahe | Reproducible build (`python:3.12.1-slim`, hindi`python:latest`) |
### Halimbawa ng Multi-Stage Build
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
Tinutukoy ng Docker Compose ang mga multi-container na application sa iisang YAML file.
### Mga Pangunahing Utos
| Utos | Paglalarawan |
|---------|-------------|
| `docker compose up -d`| Simulan ang lahat ng serbisyo sa background |
| `docker compose down`| Ihinto at alisin ang mga lalagyan, mga network |
| `docker compose down -v`| Alisin din ang mga volume |
| `docker compose logs -f`| Sundin ang mga log mula sa lahat ng serbisyo |
| `docker compose ps`| Listahan ng mga tumatakbong serbisyo |
| `docker compose build`| Muling buuin ang mga larawan |
| `docker compose exec web bash`| Patakbuhin ang command sa isang tumatakbong serbisyo |
| `docker compose pull`| Hilahin ang pinakabagong mga larawan |
### Halimbawang Compose File
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

## Arkitektura ng Kubernetes
| Bahagi | Tungkulin |
|-----------|------|
| **Cluster** | Isang set ng mga node (machine) na nagpapatakbo ng mga containerized na application |
| **Control Plane** | API server, scheduler, controller manager, etcd (cluster state) |
| **Node** | Isang worker machine (VM o pisikal) na nagpapatakbo ng mga pod |
| **Pod** | Pinakamaliit na yunit; isa o higit pang mahigpit na pinagsamang lalagyan |
| **Deployment** | Namamahala ng mga replika ng isang pod; pinangangasiwaan ang mga rolling update |
| **Serbisyo** | Matatag na endpoint ng network para sa isang hanay ng mga pod |
| **Pagpasok** | Pagruruta ng HTTP mula sa labas ng cluster patungo sa mga serbisyo |
| **ConfigMap** | Hindi lihim na data ng pagsasaayos |
| **Lihim** | Sensitibong data (base64-encoded) |
| **Namespace** | Lohikal na paghihiwalay sa loob ng isang kumpol |
| **PersistentVolume (PV)** | Cluster-level na mapagkukunan ng storage |
| **PersistentVolumeClaim (PVC)** | Kahilingan para sa imbakan ng isang pod |
---

## Kubectl Command
### Impormasyon ng Cluster
| Utos | Paglalarawan |
|---------|-------------|
| `kubectl cluster-info`| Mga detalye ng endpoint ng cluster |
| `kubectl get nodes`| Ilista ang lahat ng node |
| `kubectl get namespaces`| Maglista ng mga namespace |
| `kubectl config current-context`| Ipakita ang kasalukuyang konteksto ng cluster |
| `kubectl config use-context prod`| Lumipat ng konteksto |
### Mga workload
| Utos | Paglalarawan |
|---------|-------------|
| `kubectl get pods`| Maglista ng mga pod sa kasalukuyang namespace |
| `kubectl get pods -A`| Maglista ng mga pod sa lahat ng namespaces |
| `kubectl get deployments`| Listahan ng mga deployment |
| `kubectl get services`| Listahan ng mga serbisyo |
| `kubectl get ingress`| Listahan ng mga mapagkukunan ng pagpasok |
| `kubectl describe pod <name>`| Detalyadong impormasyon ng pod (mga kaganapan, katayuan, mga detalye) |
| `kubectl logs <pod>`| Tingnan ang mga pod log |
| `kubectl logs -f <pod>`| Sundin ang mga pod log |
| `kubectl logs <pod> -c <container>`| Mga log mula sa isang partikular na container sa isang multi-container pod |
| `kubectl exec -it <pod> -- bash`| Shell sa isang pod |
| `kubectl delete pod <name>`| Magtanggal ng pod (ito ay gagawa muli ng controller nito) |
| `kubectl rollout status deployment/<name>`| Suriin ang pag-usad ng rollout |
| `kubectl rollout undo deployment/<name>`| Bumalik sa nakaraang bersyon |
### Paglalapat ng Configuration
| Utos | Paglalarawan |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Maglapat ng YAML manifest |
| `kubectl apply -f ./dir/`| Ilapat ang lahat ng YAML file sa isang direktoryo |
| `kubectl delete -f deployment.yaml`| Tanggalin ang mga mapagkukunang tinukoy sa isang YAML file |
| `kubectl scale deployment/web --replicas=5`| Mag-scale ng deployment |
| `kubectl set image deployment/web web=myapp:2.0`| I-update ang larawan ng lalagyan |
---

## Mga Karaniwang Manipes ng Kubernetes
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

### Serbisyo
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

### Pagpasok
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

## Mga Pangunahing Kaalaman sa Helm
Si Helm ang package manager para sa Kubernetes. Pinapakete nito ang mga mapagkukunan ng Kubernetes sa mga reusable na chart.
| Utos | Paglalarawan |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Magdagdag ng imbakan ng tsart |
| `helm repo update`| I-update ang lokal na index ng tsart |
| `helm search repo nginx`| Maghanap ng tsart |
| `helm install my-release bitnami/nginx`| Mag-install ng chart |
| `helm install my-release bitnami/nginx --set replicaCount=3`| I-install gamit ang mga custom na halaga |
| `helm install my-release bitnami/nginx -f values.yaml`| I-install gamit ang isang values ​​file |
| `helm list`| Ilista ang mga naka-install na release |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Mag-upgrade ng release |
| `helm rollback my-release 1`| Bumalik sa isang nakaraang rebisyon |
| `helm uninstall my-release`| Mag-uninstall ng release |
| `helm status my-release`| Ipakita ang katayuan ng paglabas |
---

## Mabilis na Sanggunian sa Pag-troubleshoot
| Problema | Mga Utos na Subukan |
|---------|----------------|
| Hindi nagsisimula ang pod | `kubectl describe pod <name>`→ suriin ang Mga Kaganapan |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ tingnan kung bakit ito nag-crash |
| Error sa paghila ng larawan | Suriin ang pangalan ng larawan, tag, at mga kredensyal sa pagpapatala |
| Hindi maabot ang serbisyo | `kubectl get endpoints <service>`→ napili ba ang mga pod? |
| OOMKilled | Dagdagan ang mga limitasyon sa memorya o i-optimize ang paggamit ng memorya ng app |
| Mga nakabinbing pod | `kubectl describe pod`→ suriin ang mga mapagkukunan ng node, mga bahid, affinity |
| Mga isyu sa DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|