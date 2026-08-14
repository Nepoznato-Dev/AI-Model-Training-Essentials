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
# ڈوکر اور کبرنیٹس چیٹ شیٹ
ڈوکر کے ساتھ ایپلی کیشنز کو کنٹینر کرنے اور کوبرنیٹس کے ساتھ آرکیسٹریٹنگ کے لیے ایک عملی حوالہ۔ کمانڈ لائن کے ساتھ بنیادی واقفیت فرض کرتا ہے۔
---

## ڈوکر کے بنیادی اصول
| تصور | تفصیل |
|---------|---------------|
| **تصویر** | ایپ کوڈ + انحصار + OS لائبریریوں کے ساتھ صرف پڑھنے کے لیے ٹیمپلیٹ |
| **کنٹینر** | ایک تصویر کی مثال چل رہی ہے؛ الگ تھلگ عمل |
| **ڈاکر فائل** | تصویر بنانے کا نسخہ |
| **رجسٹری** | تصاویر کے لیے ذخیرہ (Docker Hub, ECR, GCR, GHCR) |
| **حجم** | کنٹینر دوبارہ شروع ہونے سے بچ جانے والا مستقل ذخیرہ |
| **نیٹ ورک** | ورچوئل نیٹ ورک کنٹینرز |
---

## ضروری ڈوکر کمانڈز
### تصاویر
| کمانڈ | تفصیل |
|---------|---------------|
| `docker build -t myapp:1.0 .`| ڈاکر فائل سے ایک تصویر بنائیں |
| `docker images`| مقامی تصاویر کی فہرست بنائیں |
| `docker pull nginx:latest`| رجسٹری سے تصویر کھینچیں |
| `docker push myrepo/myapp:1.0`| ایک تصویر کو رجسٹری میں دھکیلیں |
| `docker rmi myapp:1.0`| ایک مقامی تصویر کو ہٹا دیں |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| رجسٹری کے لیے ایک تصویر کو ٹیگ کریں |
| `docker image prune -a`| تمام غیر استعمال شدہ تصاویر کو ہٹا دیں |
### کنٹینرز
| کمانڈ | تفصیل |
|---------|---------------|
| `docker run -d -p 8080:80 nginx`| پس منظر میں ایک کنٹینر چلائیں، نقشہ پورٹ 8080→80 |
| `docker run -it ubuntu bash`| ایک شیل کے ساتھ انٹرایکٹو چلائیں |
| `docker run --name web -e DB_HOST=db nginx`| کنٹینر کا نام اور ماحولیاتی متغیر سیٹ کریں |
| `docker ps`| چلانے والے کنٹینرز کی فہرست |
| `docker ps -a`| تمام کنٹینرز کی فہرست بنائیں (بشمول روکے گئے) |
| `docker stop web`| چلتے ہوئے کنٹینر کو روکیں |
| `docker start web`| روکا ہوا کنٹینر شروع کریں |
| `docker rm web`| رکے ہوئے کنٹینر کو ہٹا دیں |
| `docker exec -it web bash`| چلتے ہوئے کنٹینر کے اندر ایک شیل کھولیں |
| `docker logs -f web`| کنٹینر لاگز کی پیروی کریں |
| `docker inspect web`| تفصیلی کنٹینر میٹا ڈیٹا (JSON) |
| `docker stats`| تمام کنٹینرز کے لیے براہ راست وسائل کا استعمال |
### صفائی
| کمانڈ | تفصیل |
|---------|---------------|
| `docker system prune -a`| تمام غیر استعمال شدہ کنٹینرز، تصاویر، نیٹ ورکس کو ہٹا دیں اور کیش بنائیں |
| `docker volume prune`| تمام غیر استعمال شدہ جلدوں کو ہٹا دیں |
| `docker container prune`| تمام رکے ہوئے کنٹینرز کو ہٹا دیں |
---

## ڈاکر فائل حوالہ
### عام ہدایات
| ہدایات | مقصد | مثال |
|---------------|---------|---------|
| `FROM`| بنیادی تصویر | `FROM python:3.12-slim`|
| `WORKDIR`| تصویر کے اندر ورکنگ ڈائرکٹری سیٹ کریں | `WORKDIR /app`|
| `COPY`| فائلوں کو میزبان سے تصویر میں کاپی کریں | `COPY requirements.txt .`|
| `ADD`| کاپی کی طرح، لیکن ٹارز بھی نکالتا ہے اور یو آر ایل کو سپورٹ کرتا ہے۔ `ADD app.tar.gz /app/`|
| `RUN`| تعمیر کے دوران کمانڈ پر عمل کریں | `RUN pip install -r requirements.txt`|
| `CMD`| کنٹینر شروع ہونے پر پہلے سے طے شدہ کمانڈ | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| فکسڈ کمانڈ؛ سی ایم ڈی دلائل بن جاتا ہے | `ENTRYPOINT ["python"]`|
| `ENV`| ماحول متغیر سیٹ کریں | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| دستاویز جس پورٹ پر ایپ سنتی ہے | `EXPOSE 8000`|
| `ARG`| تعمیر وقت متغیر | `ARG VERSION=1.0`|
| `USER`| غیر جڑ صارف پر سوئچ کریں | `USER appuser`|
| `HEALTHCHECK`| ہیلتھ چیک کمانڈ کی وضاحت کریں | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| ایک ماؤنٹ پوائنٹ بنائیں | `VOLUME /data`|
### بہترین طرز عمل
| مشق | کیوں |
|------------|------|
| پتلی/بیس تصاویر کا استعمال کریں | چھوٹی تصاویر = تیزی سے کھینچنا، چھوٹی حملے کی سطح |
| RUN کمانڈز کو`&&`کے ساتھ جوڑیں۔ تصویر کی تہوں کو کم کرتا ہے |
| پہلے انحصار فائلوں کو کاپی کریں، پھر کوڈ | ڈوکر کے بلڈ کیشے کا فائدہ اٹھاتا ہے |
|`.dockerignore`استعمال کریں۔ خارج کریں`node_modules`,`.git`,`__pycache__`|
| غیر جڑ صارف کے طور پر چلائیں | سیکورٹی بہترین پریکٹس |
| ملٹی اسٹیج بلڈز استعمال کریں۔ علیحدہ تعمیر اور رن ٹائم؛ چھوٹی حتمی تصویر |
| پن بیس تصویری ورژن | دوبارہ پیدا کرنے والی تعمیرات ( `python:3.12.1-slim`،`python:latest`نہیں ) |
### ملٹی اسٹیج بلڈ کی مثال
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

## ڈوکر کمپوز
ڈوکر کمپوز ایک ہی YAML فائل میں ملٹی کنٹینر ایپلی کیشنز کی وضاحت کرتا ہے۔
### کلیدی کمانڈز
| کمانڈ | تفصیل |
|---------|---------------|
| `docker compose up -d`| تمام خدمات کو پس منظر میں شروع کریں |
| `docker compose down`| کنٹینرز، نیٹ ورکس کو روکیں اور ہٹا دیں۔
| `docker compose down -v`| جلدیں بھی ہٹا دیں |
| `docker compose logs -f`| تمام خدمات سے لاگز کی پیروی کریں |
| `docker compose ps`| فہرست چلانے والی خدمات |
| `docker compose build`| تصاویر کو دوبارہ بنائیں |
| `docker compose exec web bash`| رننگ سروس میں کمانڈ چلائیں |
| `docker compose pull`| تازہ ترین تصاویر ھیںچو |
### کمپوز فائل کی مثال
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

## کوبرنیٹس آرکیٹیکچر
| جزو | کردار |
|------------|------|
| **کلسٹر** | کنٹینرائزڈ ایپلی کیشنز چلانے والے نوڈس (مشینوں) کا ایک سیٹ |
| **کنٹرول طیارہ** | API سرور، شیڈولر، کنٹرولر مینیجر، وغیرہ (کلسٹر اسٹیٹ) |
| **نوڈ** | ایک ورکر مشین (VM یا فزیکل) جو پھلی چلاتی ہے۔
| **پوڈ** | سب سے چھوٹی یونٹ؛ ایک یا زیادہ مضبوطی سے جوڑے ہوئے کنٹینرز |
| **تعینات** | پوڈ کی نقلوں کا انتظام کرتا ہے۔ رولنگ اپ ڈیٹس ہینڈل |
| **سروس** | پوڈز کے سیٹ کے لیے مستحکم نیٹ ورک اینڈ پوائنٹ |
| **داخلہ** | کلسٹر کے باہر سے خدمات تک HTTP روٹنگ |
| **ConfigMap** | غیر خفیہ کنفیگریشن ڈیٹا |
| **خفیہ** | حساس ڈیٹا (base64-encoded) |
| **نام کی جگہ** | ایک کلسٹر کے اندر منطقی تنہائی |
| **مستقل حجم (PV)** | کلسٹر لیول اسٹوریج ریسورس |
| **پرسسٹنٹ والیوم کلیم (PVC)** | پوڈ کے ذریعہ ذخیرہ کرنے کی درخواست |
---

## kubectl کمانڈز
### کلسٹر کی معلومات
| کمانڈ | تفصیل |
|---------|---------------|
| `kubectl cluster-info`| کلسٹر اینڈ پوائنٹ کی تفصیلات |
| `kubectl get nodes`| تمام نوڈس کی فہرست بنائیں |
| `kubectl get namespaces`| نام کی جگہوں کی فہرست |
| `kubectl config current-context`| موجودہ کلسٹر سیاق و سباق دکھائیں |
| `kubectl config use-context prod`| سیاق و سباق کو تبدیل کریں |
### کام کا بوجھ
| کمانڈ | تفصیل |
|---------|---------------|
| `kubectl get pods`| موجودہ نام کی جگہ میں پھلیوں کی فہرست |
| `kubectl get pods -A`| تمام نام کی جگہوں پر پوڈز کی فہرست بنائیں |
| `kubectl get deployments`| فہرست تعیناتیوں |
| `kubectl get services`| فہرست خدمات |
| `kubectl get ingress`| داخل ہونے والے وسائل کی فہرست |
| `kubectl describe pod <name>`| پوڈ کی تفصیلی معلومات (واقعات، حیثیت، چشمی) |
| `kubectl logs <pod>`| پوڈ لاگز دیکھیں |
| `kubectl logs -f <pod>`| پوڈ لاگز کی پیروی کریں |
| `kubectl logs <pod> -c <container>`| ملٹی کنٹینر پوڈ میں مخصوص کنٹینر سے لاگز |
| `kubectl exec -it <pod> -- bash`| ایک پھلی میں شیل |
| `kubectl delete pod <name>`| ایک پوڈ کو حذف کریں (اسے اپنے کنٹرولر کے ذریعہ دوبارہ بنایا جائے گا) |
| `kubectl rollout status deployment/<name>`| رول آؤٹ کی پیشرفت چیک کریں |
| `kubectl rollout undo deployment/<name>`| پچھلے ورژن پر واپس جائیں |
### کنفیگریشن کا اطلاق کرنا
| کمانڈ | تفصیل |
|---------|---------------|
| `kubectl apply -f deployment.yaml`| YAML مینی فیسٹ لگائیں |
| `kubectl apply -f ./dir/`| تمام YAML فائلوں کو ڈائریکٹری میں لاگو کریں |
| `kubectl delete -f deployment.yaml`| YAML فائل میں بیان کردہ وسائل کو حذف کریں |
| `kubectl scale deployment/web --replicas=5`| تعیناتی کی پیمائش کریں |
| `kubectl set image deployment/web web=myapp:2.0`| کنٹینر کی تصویر کو اپ ڈیٹ کریں |
---

## عام کبرنیٹس ظاہر ہوتا ہے۔
### تعیناتی۔
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

### سروس
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

### داخل ہونا
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

## ہیلم کی بنیادی باتیں
ہیلم Kubernetes کے لیے پیکیج مینیجر ہے۔ یہ کبرنیٹس کے وسائل کو دوبارہ قابل استعمال چارٹس میں پیک کرتا ہے۔
| کمانڈ | تفصیل |
|---------|---------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| ایک چارٹ ذخیرہ شامل کریں |
| `helm repo update`| مقامی چارٹ انڈیکس کو اپ ڈیٹ کریں |
| `helm search repo nginx`| چارٹ تلاش کریں |
| `helm install my-release bitnami/nginx`| چارٹ انسٹال کریں |
| `helm install my-release bitnami/nginx --set replicaCount=3`| حسب ضرورت اقدار کے ساتھ انسٹال کریں |
| `helm install my-release bitnami/nginx -f values.yaml`| ویلیوز فائل کے ساتھ انسٹال کریں |
| `helm list`| انسٹال کردہ ریلیز کی فہرست |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| ایک ریلیز کو اپ گریڈ کریں |
| `helm rollback my-release 1`| پچھلی نظرثانی پر واپس جائیں |
| `helm uninstall my-release`| ریلیز کو ان انسٹال کریں |
| `helm status my-release`| ریلیز کی حیثیت دکھائیں |
---

## فوری حوالہ کا ازالہ کرنا
| مسئلہ | کوشش کرنے کے احکامات |
|---------|----------------|
| پھلی شروع نہیں ہو رہی | `kubectl describe pod <name>`→ واقعات چیک کریں |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ دیکھیں کہ یہ کیوں کریش ہوا |
| تصویر کھینچنے کی خرابی | تصویر کا نام، ٹیگ، اور رجسٹری کی اسناد چیک کریں |
| سروس قابل رسائی نہیں ہے | `kubectl get endpoints <service>`→ کیا پوڈز منتخب ہیں؟ |
| OOMKilled | میموری کی حدود میں اضافہ کریں یا ایپ میموری کے استعمال کو بہتر بنائیں |
| زیر التواء پھلی | `kubectl describe pod`→ چیک نوڈ وسائل، داغ، تعلق |
| DNS مسائل | `kubectl exec <pod> -- nslookup kubernetes.default`|