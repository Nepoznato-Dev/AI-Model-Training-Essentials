---
# فراداده
عنوان: "برگ تقلب داکر و کوبرنتس"
توضیحات: "Docker, Docker Compose, Kubernetes, Helm Cheat Sheet"
دسته بندی: "مرجع سریع"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش مرجع سریع"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [docker، kubernetes، مرجع سریع]
سطح سختی: "مبتدی"
پیش نیاز: []
تخمینی_زمان_خواندن: "15 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
# برگه تقلب Docker و Kubernetes
یک مرجع کاربردی برای کانتینری کردن برنامه ها با Docker و هماهنگ کردن آنها با Kubernetes. آشنایی اولیه با خط فرمان را فرض می کند.
---

## اصول داکر
| مفهوم | توضیحات |
|---------|-------------|
| **تصویر** | الگوی فقط خواندنی با کد برنامه + وابستگی ها + کتابخانه های سیستم عامل |
| **ظرف** | نمونه در حال اجرا یک تصویر؛ فرآیند ایزوله |
| **Dockerfile** | دستور ساخت تصویر |
| **رجیستری** | ذخیره سازی برای تصاویر (Docker Hub، ECR، GCR، GHCR) |
| **حجم** | ذخیره سازی پایدار که در کانتینر باقی می ماند دوباره راه اندازی می شود |
| **شبکه** | کانتینرهای اتصال شبکه مجازی |
---

## دستورات ضروری Docker
### تصاویر
| فرمان | توضیحات |
|---------|-------------|
| `docker build -t myapp:1.0 .`| ساخت یک تصویر از Dockerfile |
|  __محافظت شده_1__ | فهرست تصاویر محلی |
| `docker pull nginx:latest`| یک تصویر را از رجیستری بکشید |
|  __محافظت شده_3__ | یک تصویر را به یک رجیستری فشار دهید |
| `docker rmi myapp:1.0`| حذف یک تصویر محلی |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| یک تصویر را برای یک رجیستری تگ کنید |
|  __محافظت شده_6__ | حذف تمام تصاویر استفاده نشده |
### ظروف
| فرمان | توضیحات |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| یک کانتینر را در پس زمینه اجرا کنید، پورت نقشه 8080→80 |
|  __محافظت شده_1__ | اجرای تعاملی با یک پوسته |
| `docker run --name web -e DB_HOST=db nginx`| تنظیم نام کانتینر و متغیر محیط |
|  __محافظت شده_3__ | فهرست کانتینرهای در حال اجرا |
| `docker ps -a`| فهرست همه ظروف (از جمله توقف) |
| `docker stop web`| توقف یک ظرف در حال اجرا |
|  __محافظت شده_6__ | شروع یک ظرف متوقف شده |
| `docker rm web`| یک ظرف متوقف شده را بردارید |
| `docker exec -it web bash`| باز کردن یک پوسته در داخل یک ظرف در حال اجرا |
|  __محافظت شده_9__ | سیاهههای مربوط به کانتینر را دنبال کنید |
| `docker inspect web`| فراداده کانتینر تفصیلی (JSON) |
| `docker stats`| استفاده از منابع زنده برای همه کانتینرها |
### پاکسازی
| فرمان | توضیحات |
|---------|-------------|
| `docker system prune -a`| همه کانتینرها، تصاویر، شبکه‌ها، استفاده نشده را حذف کنید و حافظه پنهان را بسازید |
|  __محافظت شده_1__ | حذف تمام جلدهای استفاده نشده |
| `docker container prune`| تمام ظروف متوقف شده را بردارید |
---

## مرجع Dockerfile
### دستورالعمل های رایج
| دستورالعمل | هدف | مثال |
|-------------|---------|---------|
| `FROM`| تصویر پایه |  __محافظت شده_1__ |
| `WORKDIR`| تنظیم دایرکتوری کاری در داخل تصویر |  __محافظت شده_3__ |
| `COPY`| کپی فایل ها از میزبان به تصویر | `COPY requirements.txt .`|
|  __محافظت شده_6__ | مانند COPY، اما تارها را استخراج می کند و URL ها را پشتیبانی می کند | `ADD app.tar.gz /app/`|
| `RUN`| اجرای دستور در حین ساخت |  __محافظت شده_9__ |
| `CMD`| فرمان پیش‌فرض هنگام شروع کانتینر | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| دستور ثابت؛ CMD تبدیل به آرگومان می شود | `ENTRYPOINT ["python"]`|
| `ENV`| تنظیم متغیر محیطی | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| سندی که برنامه به کدام پورت گوش می دهد | `EXPOSE 8000`|
| `ARG`| متغیر زمان ساخت | `ARG VERSION=1.0`|
| `USER`| تغییر به کاربر غیر ریشه | `USER appuser`|
| `HEALTHCHECK`| تعریف دستور بررسی سلامت | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| ایجاد نقطه اتصال | `VOLUME /data`|
### بهترین شیوه ها
| تمرین | چرا |
|----------|-----|
| استفاده از تصاویر باریک/پایه | تصاویر کوچکتر = کشش سریعتر، سطح حمله کوچکتر |
| دستورات RUN را با`&&`| ترکیب کنید لایه های تصویر را کاهش می دهد |
| ابتدا فایل های وابستگی را کپی کنید، سپس کد | اهرم کش ساخت Docker's |
| استفاده از`.dockerignore`| استثناء `node_modules`، `.git`،`__pycache__`|
| اجرا به عنوان کاربر غیر ریشه | بهترین روش امنیتی |
| استفاده از ساخت های چند مرحله ای | ساخت و زمان اجرا جداگانه؛ تصویر نهایی کوچکتر |
| پین کردن نسخه های تصویر پایه | سازه های قابل تکرار (`python:3.12.1-slim`, نه`python:latest`) |
### مثال ساخت چند مرحله ای
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
Docker Compose برنامه های کاربردی چند کانتینری را در یک فایل YAML تعریف می کند.
### دستورات کلیدی
| فرمان | توضیحات |
|---------|-------------|
| `docker compose up -d`| شروع تمام خدمات در پس زمینه |
|  __محافظت شده_1__ | توقف و حذف کانتینرها، شبکه ها |
| `docker compose down -v`| همچنین حجم ها را حذف کنید |
|  __محافظت شده_3__ | سیاهههای مربوط به همه خدمات را دنبال کنید |
| `docker compose ps`| فهرست خدمات در حال اجرا |
| `docker compose build`| بازسازی تصاویر |
|  __محافظت شده_6__ | اجرای دستور در یک سرویس در حال اجرا |
| `docker compose pull`| کشیدن آخرین تصاویر |
### مثال نوشتن فایل
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

## معماری Kubernetes
| جزء | نقش |
|-----------|------|
| **خوشه** | مجموعه ای از گره ها (ماشین ها) که برنامه های کاربردی کانتینری را اجرا می کنند |
| **هواپیمای کنترل** | سرور API، زمانبندی، مدیریت کنترلر، etcd (وضعیت خوشه) |
| **گره** | یک ماشین کارگر (VM یا فیزیکی) که pods |
| **پاد** | کوچکترین واحد؛ یک یا چند ظرف محکم جفت شده |
| **استقرار** | کپی های یک غلاف را مدیریت می کند. مدیریت به روز رسانی های چرخشی |
| **سرویس** | نقطه پایانی شبکه پایدار برای مجموعه ای از pods |
| **ورود** | مسیریابی HTTP از خارج از خوشه به خدمات |
| **ConfigMap** | داده های پیکربندی غیر محرمانه |
| **راز** | داده های حساس (با پایه 64 رمزگذاری شده) |
| ** فضای نام ** | جداسازی منطقی در یک خوشه |
| **حجم پایدار (PV)** | منبع ذخیره سازی در سطح خوشه |
| **PersistentVolumeClaim (PVC)** | درخواست ذخیره توسط غلاف |
---

## دستورات kubectl
### اطلاعات خوشه
| فرمان | توضیحات |
|---------|-------------|
| `kubectl cluster-info`| جزئیات نقطه پایانی خوشه |
|  __محافظت شده_1__ | لیست تمام گره ها |
| `kubectl get namespaces`| فهرست فضاهای نام |
|  __محافظت شده_3__ | نمایش بافت خوشه فعلی |
| `kubectl config use-context prod`| تغییر زمینه |
### بار کاری
| فرمان | توضیحات |
|---------|-------------|
| `kubectl get pods`| فهرست غلاف ها در فضای نام فعلی |
|  __محافظت شده_1__ | فهرست غلاف ها در همه فضاهای نام |
| `kubectl get deployments`| فهرست استقرار |
|  __محافظت شده_3__ | لیست خدمات |
| `kubectl get ingress`| فهرست منابع ورودی |
| `kubectl describe pod <name>`| اطلاعات غلاف مفصل (رویدادها، وضعیت، مشخصات) |
|  __محافظت شده_6__ | مشاهده گزارش های غلاف |
| `kubectl logs -f <pod>`| دنبال کردن گزارش های غلاف |
| `kubectl logs <pod> -c <container>`| سیاهههای مربوط از یک ظرف خاص در یک غلاف چند کانتینری |
|  __محافظت شده_9__ | پوسته به غلاف |
| `kubectl delete pod <name>`| یک پاد را حذف کنید (توسط کنترل کننده آن دوباره ایجاد می شود) |
| `kubectl rollout status deployment/<name>`| بررسی پیشرفت عرضه |
| `kubectl rollout undo deployment/<name>`| بازگشت به نسخه قبلی |
### اعمال پیکربندی
| فرمان | توضیحات |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| اعمال مانیفست YAML |
|  __محافظت شده_1__ | اعمال تمام فایل های YAML در یک فهرست |
| `kubectl delete -f deployment.yaml`| حذف منابع تعریف شده در فایل YAML |
|  __محافظت شده_3__ | مقیاس استقرار |
| `kubectl set image deployment/web web=myapp:2.0`| به روز رسانی تصویر ظرف |
---

## تظاهرات رایج Kubernetes
### استقرار
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

خدمات ###
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

### ورود
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

## اصول کلاه
Helm مدیر بسته Kubernetes است. منابع Kubernetes را در نمودارهای قابل استفاده مجدد بسته بندی می کند.
| فرمان | توضیحات |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| اضافه کردن یک مخزن نمودار |
|  __محافظت شده_1__ | به روز رسانی نمایه نمودار محلی |
| `helm search repo nginx`| جستجو برای نمودار |
|  __محافظت شده_3__ | نصب نمودار |
| `helm install my-release bitnami/nginx --set replicaCount=3`| نصب با مقادیر سفارشی |
| `helm install my-release bitnami/nginx -f values.yaml`| نصب با فایل مقادیر |
|  __محافظت شده_6__ | لیست نسخه های نصب شده |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| ارتقاء یک نسخه |
| `helm rollback my-release 1`| بازگشت به نسخه قبلی |
|  __محافظت شده_9__ | حذف نصب |
| `helm status my-release`| نمایش وضعیت انتشار |
---

## مرجع سریع عیب یابی
| مشکل | دستورات برای امتحان |
|---------|----------------|
| پاد شروع نمی شود | `kubectl describe pod <name>`→ رویدادها |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ ببینید چرا خراب شد |
| خطای کشش تصویر | نام تصویر، برچسب و اعتبار رجیستری |
| سرویس قابل دسترسی نیست | `kubectl get endpoints <service>`→ غلاف ها انتخاب شده اند؟ |
| OOMKilled | افزایش محدودیت حافظه یا بهینه سازی استفاده از حافظه برنامه |
| غلاف های معلق | `kubectl describe pod`→ بررسی منابع گره، لکه ها، وابستگی |
| مشکلات DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|