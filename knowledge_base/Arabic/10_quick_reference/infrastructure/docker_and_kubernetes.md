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
# ورقة الغش لـ Docker وKubernetes
مرجع عملي لحاويات التطبيقات مع Docker وتنسيقها مع Kubernetes. يفترض الإلمام الأساسي بسطر الأوامر.
---

## أساسيات عامل الميناء
| المفهوم | الوصف |
|---------|------------|
| **صورة** | قالب للقراءة فقط مع رمز التطبيق + التبعيات + مكتبات نظام التشغيل |
| **حاوية** | تشغيل مثيل الصورة؛ عملية معزولة |
| **ملف الإرساء** | وصفة لبناء الصورة |
| ** التسجيل ** | تخزين الصور (Docker Hub، ECR، GCR، GHCR) |
| **الحجم** | تخزين مستمر ينجو من إعادة تشغيل الحاوية |
| **الشبكة** | شبكة افتراضية تربط الحاويات |
---

## أوامر عامل الميناء الأساسية
### الصور
| الأمر | الوصف |
|---------|------------|
| `docker build -t myapp:1.0 .`| قم ببناء صورة من ملف Dockerfile |
| `docker images`| قائمة الصور المحلية |
| `docker pull nginx:latest`| سحب صورة من التسجيل |
| `docker push myrepo/myapp:1.0`| دفع صورة إلى التسجيل |
| `docker rmi myapp:1.0`| إزالة صورة محلية |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| وضع علامة على صورة للتسجيل |
| `docker image prune -a`| إزالة كافة الصور غير المستخدمة |
###حاويات
| الأمر | الوصف |
|---------|------------|
| `docker run -d -p 8080:80 nginx`| قم بتشغيل حاوية في الخلفية، قم بتعيين المنفذ 8080→80 |
| `docker run -it ubuntu bash`| تشغيل تفاعلي باستخدام Shell |
| `docker run --name web -e DB_HOST=db nginx`| قم بتعيين اسم الحاوية ومتغير البيئة |
| `docker ps`| قائمة تشغيل الحاويات |
| `docker ps -a`| قائمة بجميع الحاويات (بما في ذلك المتوقفة) |
| `docker stop web`| إيقاف تشغيل حاوية |
| `docker start web`| بدء حاوية متوقفة |
| `docker rm web`| إزالة حاوية متوقفة |
| `docker exec -it web bash`| فتح قذيفة داخل حاوية قيد التشغيل |
| `docker logs -f web`| اتبع سجلات الحاوية |
| `docker inspect web`| بيانات تعريف الحاوية التفصيلية (JSON) |
| `docker stats`| الاستخدام المباشر للموارد لجميع الحاويات |
### تنظيف
| الأمر | الوصف |
|---------|------------|
| `docker system prune -a`| قم بإزالة جميع الحاويات والصور والشبكات غير المستخدمة، وقم بإنشاء ذاكرة تخزين مؤقت |
| `docker volume prune`| إزالة كافة وحدات التخزين غير المستخدمة |
| `docker container prune`| إزالة كافة الحاويات المتوقفة |
---

## مرجع ملف دوكر
### تعليمات مشتركة
| تعليمات | الغرض | مثال |
|-------------|---------|---------|
| `FROM`| الصورة الأساسية | `FROM python:3.12-slim`|
| `WORKDIR`| قم بتعيين دليل العمل داخل الصورة | `WORKDIR /app`|
| `COPY`| انسخ الملفات من المضيف إلى الصورة | `COPY requirements.txt .`|
| `ADD`| مثل COPY، ولكنه يستخرج أيضًا القطران ويدعم عناوين URL | `ADD app.tar.gz /app/`|
| `RUN`| تنفيذ أمر أثناء الإنشاء | `RUN pip install -r requirements.txt`|
| `CMD`| الأمر الافتراضي عند بدء تشغيل الحاوية | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| أمر ثابت؛ يصبح CMD وسيطات | `ENTRYPOINT ["python"]`|
| `ENV`| تعيين متغير البيئة | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| قم بتوثيق المنفذ الذي يستمع إليه التطبيق | `EXPOSE 8000`|
| `ARG`| متغير وقت البناء | `ARG VERSION=1.0`|
| `USER`| قم بالتبديل إلى مستخدم غير جذر | `USER appuser`|
| `HEALTHCHECK`| تحديد أمر فحص الصحة | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| قم بإنشاء نقطة تحميل | `VOLUME /data`|
### أفضل الممارسات
| ممارسة | لماذا |
|----------|-----|
| استخدم الصور الرفيعة/الأساسية | الصور الأصغر = عمليات سحب أسرع، وسطح هجوم أصغر |
| ادمج أوامر RUN مع`&&`| يقلل من طبقات الصورة |
| انسخ الملفات التابعة أولاً، ثم قم بنسخ الكود | الاستفادة من ذاكرة التخزين المؤقت لبناء Docker |
| استخدم`.dockerignore`| استبعاد `node_modules`، `.git`،`__pycache__`|
| تشغيل كمستخدم غير جذر | أفضل الممارسات الأمنية |
| استخدم بنيات متعددة المراحل | بناء منفصل ووقت التشغيل؛ الصورة النهائية الأصغر |
| دبوس إصدارات الصور الأساسية | النسخ القابلة للتكرار (`python:3.12.1-slim`، وليس `python:latest`) |
### مثال بناء متعدد المراحل
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

## إنشاء عامل الميناء
يحدد Docker Compose تطبيقات متعددة الحاويات في ملف YAML واحد.
### الأوامر الرئيسية
| الأمر | الوصف |
|---------|------------|
| `docker compose up -d`| بدء كافة الخدمات في الخلفية |
| `docker compose down`| إيقاف وإزالة الحاويات والشبكات |
| `docker compose down -v`| قم أيضًا بإزالة المجلدات |
| `docker compose logs -f`| متابعة السجلات من كافة الخدمات |
| `docker compose ps`| قائمة تشغيل الخدمات |
| `docker compose build`| إعادة بناء الصور |
| `docker compose exec web bash`| قم بتشغيل الأمر في خدمة قيد التشغيل |
| `docker compose pull`| سحب أحدث الصور |
### مثال لملف الإنشاء
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

## هندسة كوبيرنتس
| مكون | الدور |
|-----------|------|
| **الكتلة** | مجموعة من العقد (الأجهزة) التي تقوم بتشغيل التطبيقات الحاوية |
| **طائرة التحكم** | خادم واجهة برمجة التطبيقات، والمجدول، ومدير وحدة التحكم، وما إلى ذلك (حالة المجموعة) |
| **العقدة** | آلة عاملة (VM أو مادية) تقوم بتشغيل القرون |
| **جراب** | أصغر وحدة؛ واحدة أو أكثر من الحاويات المقترنة بإحكام |
| **النشر** | يدير النسخ المتماثلة من جراب. يعالج التحديثات المتداولة |
| **الخدمة** | نقطة نهاية شبكة مستقرة لمجموعة من القرون |
| **دخول** | توجيه HTTP من خارج المجموعة إلى الخدمات |
| **خريطة التكوين** | بيانات التكوين غير السرية |
| **سرى** | بيانات حساسة (بترميز Base64) |
| **مساحة الاسم** | العزلة المنطقية داخل كتلة |
| **الحجم المستمر (PV)** | مورد التخزين على مستوى المجموعة |
| ** المطالبة بالحجم المستمر (PVC) ** | طلب تخزين بواسطة جراب |
---

## أوامر كوبيكتل
### معلومات المجموعة
| الأمر | الوصف |
|---------|------------|
| `kubectl cluster-info`| تفاصيل نقطة نهاية الكتلة |
| `kubectl get nodes`| قائمة بجميع العقد |
| `kubectl get namespaces`| قائمة مساحات الأسماء |
| `kubectl config current-context`| إظهار سياق المجموعة الحالية |
| `kubectl config use-context prod`| تبديل السياق |
### أعباء العمل
| الأمر | الوصف |
|---------|------------|
| `kubectl get pods`| قائمة القرون في مساحة الاسم الحالية |
| `kubectl get pods -A`| سرد القرون عبر كافة مساحات الأسماء |
| `kubectl get deployments`| قائمة النشر |
| `kubectl get services`| قائمة الخدمات |
| `kubectl get ingress`| قائمة موارد الدخول |
| `kubectl describe pod <name>`| معلومات مفصلة عن الكبسولة (الأحداث، الحالة، المواصفات) |
| `kubectl logs <pod>`| عرض سجلات جراب |
| `kubectl logs -f <pod>`| اتبع سجلات جراب |
| `kubectl logs <pod> -c <container>`| سجلات من حاوية محددة في حاوية متعددة الحاويات |
| `kubectl exec -it <pod> -- bash`| قذيفة في جراب |
| `kubectl delete pod <name>`| حذف جراب (سيتم إعادة إنشائه بواسطة وحدة التحكم الخاصة به) |
| `kubectl rollout status deployment/<name>`| تحقق من تقدم عملية الطرح |
| `kubectl rollout undo deployment/<name>`| العودة إلى الإصدار السابق |
### تطبيق التكوين
| الأمر | الوصف |
|---------|------------|
| `kubectl apply -f deployment.yaml`| تطبيق بيان YAML |
| `kubectl apply -f ./dir/`| قم بتطبيق جميع ملفات YAML في الدليل |
| `kubectl delete -f deployment.yaml`| حذف الموارد المحددة في ملف YAML |
| `kubectl scale deployment/web --replicas=5`| مقياس النشر |
| `kubectl set image deployment/web web=myapp:2.0`| تحديث صورة الحاوية |
---

## بيانات Kubernetes الشائعة
### النشر
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

### خدمة
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

### دخول
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

## أساسيات الخوذة
Helm هو مدير الحزم في Kubernetes. يقوم بتجميع موارد Kubernetes في مخططات قابلة لإعادة الاستخدام.
| الأمر | الوصف |
|---------|------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| إضافة مستودع الرسم البياني |
| `helm repo update`| تحديث مؤشر الرسم البياني المحلي |
| `helm search repo nginx`| ابحث عن مخطط |
| `helm install my-release bitnami/nginx`| تثبيت مخطط |
| `helm install my-release bitnami/nginx --set replicaCount=3`| التثبيت باستخدام القيم المخصصة |
| `helm install my-release bitnami/nginx -f values.yaml`| التثبيت باستخدام ملف القيم |
| `helm list`| قائمة الإصدارات المثبتة |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| ترقية الإصدار |
| `helm rollback my-release 1`| العودة إلى المراجعة السابقة |
| `helm uninstall my-release`| إلغاء تثبيت الإصدار |
| `helm status my-release`| عرض حالة الإصدار |
---

## استكشاف أخطاء المرجع السريع وإصلاحها
| مشكلة | أوامر للمحاولة |
|---------|----------------|
| جراب لا يبدأ | `kubectl describe pod <name>`→ تحقق من الأحداث |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ تعرف على سبب تعطلها |
| خطأ في سحب الصورة | تحقق من اسم الصورة والعلامة وبيانات اعتماد التسجيل |
| الخدمة غير قابلة للوصول | `kubectl get endpoints <service>`→ هل تم تحديد القرون؟ |
| أومقتل | زيادة حدود الذاكرة أو تحسين استخدام ذاكرة التطبيق |
| القرون المعلقة | `kubectl describe pod`→ التحقق من موارد العقدة والعيوب والتقارب |
| قضايا DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|