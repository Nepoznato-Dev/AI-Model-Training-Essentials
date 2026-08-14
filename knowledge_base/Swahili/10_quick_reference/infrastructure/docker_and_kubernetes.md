<!--
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

-->
# Docker na Kubernetes Karatasi ya Kudanganya
Rejeleo la vitendo la kuweka programu na Docker na kuzipanga kwa Kubernetes. Inachukua ujuzi wa kimsingi na mstari wa amri.
---

## Misingi ya Docker
| Dhana | Maelezo |
|---------|-------------|
| **Picha** | Kiolezo cha kusoma pekee chenye msimbo wa programu + vitegemezi + maktaba za Mfumo wa Uendeshaji |
| **Kontena** | Mfano wa kukimbia wa picha; mchakato pekee |
| **Dockerfile** | Kichocheo cha kujenga picha |
| **Msajili** | Hifadhi ya picha (Docker Hub, ECR, GCR, GHCR) |
| **Kiasi** | Hifadhi ya kudumu ambayo itasalia kwenye kontena kuanzishwa upya |
| **Mtandao** | Vyombo pepe vya kuunganisha mtandao |
---

## Amri Muhimu za Docker
### Picha
| Amri | Maelezo |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Unda picha kutoka kwa Dockerfile |
| `docker images`| Orodhesha picha za ndani |
| `docker pull nginx:latest`| Vuta picha kutoka kwa sajili |
| `docker push myrepo/myapp:1.0`| Sukuma picha kwenye sajili |
| `docker rmi myapp:1.0`| Ondoa picha ya ndani |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Weka tagi kwa sajili |
| `docker image prune -a`| Ondoa picha zote ambazo hazijatumika |
### Vyombo
| Amri | Maelezo |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Endesha kontena chinichini, bandari ya ramani 8080→80 |
| `docker run -it ubuntu bash`| Endesha kwa maingiliano na ganda |
| `docker run --name web -e DB_HOST=db nginx`| Weka jina la kontena na utofauti wa mazingira |
| `docker ps`| Orodhesha vyombo vinavyoendesha |
| `docker ps -a`| Orodhesha vyombo vyote (pamoja na vilivyosimamishwa) |
| `docker stop web`| Acha kontena inayoendesha |
| `docker start web`| Anzisha chombo kilichosimamishwa |
| `docker rm web`| Ondoa kontena iliyosimamishwa |
| `docker exec -it web bash`| Fungua ganda ndani ya chombo kinachoendesha |
| `docker logs -f web`| Fuata kumbukumbu za kontena |
| `docker inspect web`| Metadata ya kina ya chombo (JSON) |
| `docker stats`| Matumizi ya rasilimali moja kwa moja kwa vyombo vyote |
### Kusafisha
| Amri | Maelezo |
|---------|-------------|
| `docker system prune -a`| Ondoa kontena zote ambazo hazijatumika, picha, mitandao, na kache ya ujenzi |
| `docker volume prune`| Ondoa majuzuu yote ambayo hayajatumika |
| `docker container prune`| Ondoa vyombo vyote vilivyosimamishwa |
---

## Marejeleo ya faili ya Docker
### Maagizo ya Kawaida
| Maelekezo | Kusudi | Mfano |
|----------------------------------|
| `FROM`| Picha ya msingi | `FROM python:3.12-slim`|
| `WORKDIR`| Weka saraka ya kufanya kazi ndani ya picha | `WORKDIR /app`|
| `COPY`| Nakili faili kutoka kwa seva pangishi hadi kwenye picha | `COPY requirements.txt .`|
| `ADD`| Kama COPY, lakini pia hutoa tar na kuauni URL | `ADD app.tar.gz /app/`|
| `RUN`| Tekeleza amri wakati wa kujenga | `RUN pip install -r requirements.txt`|
| `CMD`| Amri chaguo-msingi wakati kontena inapoanza | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Amri zisizohamishika; CMD inakuwa hoja | `ENTRYPOINT ["python"]`|
| `ENV`| Weka mabadiliko ya mazingira | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Hati ambayo programu inasikiliza kwenye | `EXPOSE 8000`|
| `ARG`| Tofauti ya wakati wa ujenzi | `ARG VERSION=1.0`|
| `USER`| Badili hadi mtumiaji asiye mzizi | `USER appuser`|
| `HEALTHCHECK`| Bainisha amri ya ukaguzi wa afya | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Unda sehemu ya kupanda | `VOLUME /data`|
### Mbinu Bora
| Mazoezi | Kwa nini |
|----------|-----|
| Tumia picha ndogo/msingi | Picha ndogo = kuvuta kwa kasi, sehemu ndogo ya mashambulizi |
| Changanya amri za RUN na`&&`| Hupunguza tabaka za picha |
| Nakili faili za utegemezi kwanza, kisha msimbo | Inaongeza kashe ya ujenzi ya Docker |
| Tumia`.dockerignore`| Usijumuishe`node_modules`,`.git`,`__pycache__`|
| Endesha kama mtumiaji asiye na mizizi | Mbinu bora za usalama |
| Tumia miundo ya hatua nyingi | Tenganisha ujenzi na wakati wa kukimbia; picha ndogo ya mwisho |
| Bandika matoleo ya picha za msingi | Miundo inayoweza kuzaa tena ( `python:3.12.1-slim`, si`python:latest`) |
### Mfano wa Ujenzi wa Hatua Mbalimbali
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

## Tunga Docker
Docker Compose inafafanua programu za vyombo vingi katika faili moja ya YAML.
### Amri Muhimu
| Amri | Maelezo |
|---------|-------------|
| `docker compose up -d`| Anzisha huduma zote chinichini |
| `docker compose down`| Simamisha na uondoe vyombo, mitandao |
| `docker compose down -v`| Pia ondoa majuzuu |
| `docker compose logs -f`| Fuata kumbukumbu kutoka kwa huduma zote |
| `docker compose ps`| Orodhesha huduma zinazoendeshwa |
| `docker compose build`| Jenga upya picha |
| `docker compose exec web bash`| Endesha amri katika huduma inayoendesha |
| `docker compose pull`| Vuta picha za hivi punde |
### Mfano Tunga Faili
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

## Usanifu wa Kubernetes
| Sehemu | Jukumu |
|-----------|------|
| **Kikundi** | Seti ya nodi (mashine) zinazoendesha programu zilizo na kontena |
| **Ndege ya Kudhibiti** | Seva ya API, kipanga ratiba, kidhibiti kidhibiti, nk (hali ya nguzo) |
| **Njia** | Mashine ya mfanyakazi (VM au ya kimwili) inayoendesha maganda |
| **Pod** | Kitengo kidogo zaidi; chombo kimoja au zaidi kilichounganishwa vizuri |
| **Usambazaji** | Inasimamia nakala za ganda; Hushughulikia masasisho |
| **Huduma** | Mwisho wa mtandao thabiti kwa seti ya maganda |
| **Ingress** | Uelekezaji wa HTTP kutoka nje ya nguzo hadi kwa huduma |
| **ConfigMap** | Data ya usanidi isiyo ya siri |
| **Siri** | Data nyeti (base64-iliyosimbwa) |
| **Nafasi ya majina** | Kutengwa kimantiki ndani ya kundi |
| **Volume Persistent (PV)** | Nyenzo ya hifadhi ya kiwango cha nguzo |
| **PersistentVolumeClaim (PVC)** | Ombi la kuhifadhi kwa ganda |
---

## kubectl Amri
### Maelezo ya Nguzo
| Amri | Maelezo |
|---------|-------------|
| `kubectl cluster-info`| Maelezo ya mwisho wa nguzo |
| `kubectl get nodes`| Orodhesha nodi zote |
| `kubectl get namespaces`| Orodhesha nafasi za majina |
| `kubectl config current-context`| Onyesha muktadha wa sasa wa nguzo |
| `kubectl config use-context prod`| Badilisha muktadha |
### Mizigo ya kazi
| Amri | Maelezo |
|---------|-------------|
| `kubectl get pods`| Orodhesha maganda katika nafasi ya sasa ya majina |
| `kubectl get pods -A`| Orodhesha maganda kwenye nafasi zote za majina |
| `kubectl get deployments`| Orodha ya uwekaji |
| `kubectl get services`| Orodhesha huduma |
| `kubectl get ingress`| Orodhesha rasilimali za ingress |
| `kubectl describe pod <name>`| Maelezo ya kina ya ganda (matukio, hali, vipimo) |
| `kubectl logs <pod>`| Tazama kumbukumbu za ganda |
| `kubectl logs -f <pod>`| Fuata kumbukumbu za pod |
| `kubectl logs <pod> -c <container>`| Kumbukumbu kutoka kwa chombo maalum katika ganda la vyombo vingi |
| `kubectl exec -it <pod> -- bash`| Shell ndani ya ganda |
| `kubectl delete pod <name>`| Futa ganda (itaundwa upya na mtawala wake) |
| `kubectl rollout status deployment/<name>`| Angalia maendeleo ya uchapishaji |
| `kubectl rollout undo deployment/<name>`| Rudi kwenye toleo la awali |
### Inaweka Usanidi
| Amri | Maelezo |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Tumia faili ya maelezo ya YAML |
| `kubectl apply -f ./dir/`| Tumia faili zote za YAML kwenye saraka |
| `kubectl delete -f deployment.yaml`| Futa rasilimali zilizobainishwa katika faili ya YAML |
| `kubectl scale deployment/web --replicas=5`| Ongeza kiwango cha upelekaji |
| `kubectl set image deployment/web web=myapp:2.0`| Sasisha picha ya kontena |
---

## Maonyesho ya Kawaida ya Kubernetes
### Usambazaji
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

### Huduma
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

## Misingi ya Helm
Helm ndiye msimamizi wa kifurushi cha Kubernetes. Inafunga rasilimali za Kubernetes katika chati zinazoweza kutumika tena.
| Amri | Maelezo |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Ongeza hazina ya chati |
| `helm repo update`| Sasisha faharasa ya chati ya ndani |
| `helm search repo nginx`| Tafuta chati |
| `helm install my-release bitnami/nginx`| Sakinisha chati |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Sakinisha kwa kutumia thamani maalum |
| `helm install my-release bitnami/nginx -f values.yaml`| Sakinisha ukitumia faili ya maadili |
| `helm list`| Orodhesha matoleo yaliyosakinishwa |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Boresha toleo |
| `helm rollback my-release 1`| Rudi kwenye masahihisho ya awali |
| `helm uninstall my-release`| Sanidua toleo |
| `helm status my-release`| Onyesha hali ya toleo |
---

## Kutatua Marejeleo ya Haraka
| Tatizo | Amri za Kujaribu |
|---------|----------------|
| Pod haijaanza | `kubectl describe pod <name>`→ angalia Matukio |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ tazama kwa nini ilianguka |
| Hitilafu ya kuvuta picha | Angalia jina la picha, lebo, na vitambulisho vya usajili |
| Huduma haipatikani | `kubectl get endpoints <service>`→ je, maganda yamechaguliwa? |
| OOMKilled | Ongeza vikomo vya kumbukumbu au uboresha matumizi ya kumbukumbu ya programu |
| Maganda yanayosubiri | `kubectl describe pod`→ angalia rasilimali za nodi, uchafu, mshikamano |
| Masuala ya DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|