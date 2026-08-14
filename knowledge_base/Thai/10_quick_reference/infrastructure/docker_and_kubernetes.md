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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# เอกสารโกง Docker และ Kubernetes
ข้อมูลอ้างอิงที่เป็นประโยชน์สำหรับการจัดแอปพลิเคชันคอนเทนเนอร์ด้วย Docker และการเรียบเรียงแอปพลิเคชันด้วย Kubernetes ถือว่ามีความคุ้นเคยพื้นฐานกับบรรทัดคำสั่ง
---

## พื้นฐานนักเทียบท่า
| แนวคิด | คำอธิบาย |
|---------|-------------|
| **รูปภาพ** | เทมเพลตแบบอ่านอย่างเดียวพร้อมโค้ดแอป + การขึ้นต่อกัน + ไลบรารีระบบปฏิบัติการ |
| **ตู้คอนเทนเนอร์** | เรียกใช้อินสแตนซ์ของรูปภาพ กระบวนการแยก |
| **ไฟล์นักเทียบท่า** | สูตรสร้างภาพ |
| **ทะเบียน** | พื้นที่จัดเก็บรูปภาพ (Docker Hub, ECR, GCR, GHCR) |
| **ปริมาณ** | ที่เก็บข้อมูลถาวรที่รอดจากการรีสตาร์ทคอนเทนเนอร์ |
| **เครือข่าย** | เครือข่ายเสมือนที่เชื่อมต่อคอนเทนเนอร์ |
---

## คำสั่งนักเทียบท่าที่จำเป็น
### รูปภาพ
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `docker build -t myapp:1.0 .`| สร้างภาพจาก Dockerfile |
| `docker images`| แสดงรายการภาพท้องถิ่น |
| `docker pull nginx:latest`| ดึงรูปภาพจากรีจิสตรี |
| `docker push myrepo/myapp:1.0`| พุชรูปภาพไปที่รีจิสตรี |
| `docker rmi myapp:1.0`| ลบรูปภาพในเครื่อง |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| แท็กรูปภาพสำหรับการลงทะเบียน |
| `docker image prune -a`| ลบภาพที่ไม่ได้ใช้ทั้งหมด |
### คอนเทนเนอร์
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| เรียกใช้คอนเทนเนอร์ในพื้นหลัง แมปพอร์ต 8080→80 |
| `docker run -it ubuntu bash`| รันแบบโต้ตอบกับเชลล์ |
| `docker run --name web -e DB_HOST=db nginx`| ตั้งชื่อคอนเทนเนอร์และตัวแปรสภาพแวดล้อม |
| `docker ps`| แสดงรายการคอนเทนเนอร์ที่ทำงานอยู่ |
| `docker ps -a`| แสดงรายการคอนเทนเนอร์ทั้งหมด (รวมถึงการหยุดทำงาน) |
| `docker stop web`| หยุดคอนเทนเนอร์ที่ทำงานอยู่ |
| `docker start web`| เริ่มคอนเทนเนอร์ที่หยุดทำงาน |
| `docker rm web`| ลบคอนเทนเนอร์ที่หยุดทำงาน |
| `docker exec -it web bash`| เปิดเชลล์ภายในคอนเทนเนอร์ที่ทำงานอยู่ |
| `docker logs -f web`| ติดตามบันทึกคอนเทนเนอร์ |
| `docker inspect web`| ข้อมูลเมตาคอนเทนเนอร์โดยละเอียด (JSON) |
| `docker stats`| การใช้ทรัพยากรแบบสดสำหรับคอนเทนเนอร์ทั้งหมด |
### ทำความสะอาด
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `docker system prune -a`| ลบคอนเทนเนอร์ รูปภาพ เครือข่าย และบิลด์แคชที่ไม่ได้ใช้ทั้งหมด |
| `docker volume prune`| ลบวอลุ่มที่ไม่ได้ใช้ทั้งหมด |
| `docker container prune`| ลบคอนเทนเนอร์ที่หยุดทำงานทั้งหมด |
---

## การอ้างอิง Dockerfile
### คำแนะนำทั่วไป
| คำแนะนำ | วัตถุประสงค์ | ตัวอย่าง |
|-------------|---------|---------|
| `FROM`| ภาพฐาน | `FROM python:3.12-slim`|
| `WORKDIR`| ตั้งค่าไดเร็กทอรีการทำงานภายในรูปภาพ | `WORKDIR /app`|
| `COPY`| คัดลอกไฟล์จากโฮสต์ไปยังรูปภาพ | `COPY requirements.txt .`|
| `ADD`| เช่นเดียวกับ COPY แต่ยังแยก tars และรองรับ URL | `ADD app.tar.gz /app/`|
| `RUN`| ดำเนินการคำสั่งระหว่าง build | `RUN pip install -r requirements.txt`|
| `CMD`| คำสั่งเริ่มต้นเมื่อคอนเทนเนอร์เริ่มต้น | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| คำสั่งคงที่; CMD กลายเป็นอาร์กิวเมนต์ | `ENTRYPOINT ["python"]`|
| `ENV`| ตั้งค่าตัวแปรสภาพแวดล้อม | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| เอกสารที่พอร์ตที่แอปฟังบน | `EXPOSE 8000`|
| `ARG`| ตัวแปรเวลาบิวด์ | `ARG VERSION=1.0`|
| `USER`| สลับไปใช้ผู้ใช้ที่ไม่ใช่รูท | `USER appuser`|
| `HEALTHCHECK`| กำหนดคำสั่งตรวจสุขภาพ | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| สร้างจุดเมานต์ | `VOLUME /data`|
### แนวทางปฏิบัติที่ดีที่สุด
| การปฏิบัติ | ทำไม |
|----------|-----|
| ใช้รูปภาพแบบบาง/ฐาน | ภาพที่เล็กลง = ดึงเร็วขึ้น พื้นผิวการโจมตีเล็กลง |
| รวมคำสั่ง RUN เข้ากับ`&&`| ลดเลเยอร์รูปภาพ |
| คัดลอกไฟล์อ้างอิงก่อน จากนั้นจึงโค้ด | ใช้ประโยชน์จากแคชบิลด์ของ Docker |
| ใช้`.dockerignore`| ไม่รวม`node_modules`,`.git`,`__pycache__`|
| ทำงานในฐานะผู้ใช้ที่ไม่ใช่รูท | แนวปฏิบัติที่ดีที่สุดด้านความปลอดภัย |
| ใช้บิลด์แบบหลายขั้นตอน | แยกบิลด์และรันไทม์ ภาพสุดท้ายเล็กลง |
| ปักหมุดเวอร์ชันรูปภาพฐาน | บิลด์ที่ทำซ้ำได้ (`python:3.12.1-slim`ไม่ใช่`python:latest`) |
### ตัวอย่างการสร้างแบบหลายขั้นตอน
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

## นักเทียบท่าเขียน
Docker Compose กำหนดแอปพลิเคชันหลายคอนเทนเนอร์ในไฟล์ YAML ไฟล์เดียว
### คำสั่งที่สำคัญ
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `docker compose up -d`| เริ่มบริการทั้งหมดในพื้นหลัง |
| `docker compose down`| หยุดและถอดคอนเทนเนอร์, เครือข่าย |
| `docker compose down -v`| ลบโวลุ่มด้วย |
| `docker compose logs -f`| ติดตามบันทึกจากบริการทั้งหมด |
| `docker compose ps`| รายการบริการที่ทำงานอยู่ |
| `docker compose build`| สร้างภาพใหม่ |
| `docker compose exec web bash`| เรียกใช้คำสั่งในบริการที่ทำงานอยู่ |
| `docker compose pull`| ดึงภาพล่าสุด |
### ตัวอย่างไฟล์เขียน
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

## สถาปัตยกรรม Kubernetes
| ส่วนประกอบ | บทบาท |
|-----------|-|
| **คลัสเตอร์** | ชุดของโหนด (เครื่องจักร) ที่ใช้งานแอปพลิเคชันแบบคอนเทนเนอร์ |
| **เครื่องบินควบคุม** | เซิร์ฟเวอร์ API, ตัวกำหนดเวลา, ตัวจัดการคอนโทรลเลอร์, ฯลฯ (สถานะคลัสเตอร์) |
| **โหนด** | เครื่องของผู้ปฏิบัติงาน (VM หรือฟิสิคัล) ที่รันพ็อด |
| **พ็อด** | หน่วยที่เล็กที่สุด ภาชนะหนึ่งหรือหลายชิ้นที่ต่อกันอย่างแน่นหนา |
| **การปรับใช้** | จัดการการจำลองพ็อด จัดการการอัปเดตแบบกลิ้ง |
| **การบริการ** | จุดสิ้นสุดเครือข่ายที่เสถียรสำหรับชุดพ็อด |
| **ทางเข้า** | การกำหนดเส้นทาง HTTP จากภายนอกคลัสเตอร์ไปยังบริการ |
| **ConfigMap** | ข้อมูลการกำหนดค่าที่ไม่เป็นความลับ |
| **ความลับ** | ข้อมูลที่ละเอียดอ่อน (เข้ารหัส base64) |
| **เนมสเปซ** | การแยกเชิงตรรกะภายในคลัสเตอร์ |
| **ปริมาณถาวร (PV)** | ทรัพยากรการจัดเก็บข้อมูลระดับคลัสเตอร์ |
| **PersistentVolumeClaim (PVC)** | ขอพื้นที่จัดเก็บโดยพ็อด |
---

## คำสั่ง kubectl
### ข้อมูลคลัสเตอร์
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `kubectl cluster-info`| รายละเอียดจุดสิ้นสุดของคลัสเตอร์ |
| `kubectl get nodes`| แสดงรายการโหนดทั้งหมด |
| `kubectl get namespaces`| แสดงรายการเนมสเปซ |
| `kubectl config current-context`| แสดงบริบทคลัสเตอร์ปัจจุบัน |
| `kubectl config use-context prod`| สลับบริบท |
### ปริมาณงาน
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `kubectl get pods`| แสดงรายการพ็อดในเนมสเปซปัจจุบัน |
| `kubectl get pods -A`| แสดงรายการพ็อดในเนมสเปซทั้งหมด |
| `kubectl get deployments`| แสดงรายการการปรับใช้ |
| `kubectl get services`| รายการบริการ |
| `kubectl get ingress`| แสดงรายการทรัพยากรทางเข้า |
| `kubectl describe pod <name>`| ข้อมูลพ็อดโดยละเอียด (เหตุการณ์ สถานะ ข้อมูลจำเพาะ) |
| `kubectl logs <pod>`| ดูบันทึกพ็อด |
| `kubectl logs -f <pod>`| ติดตามบันทึกของพ็อด |
| `kubectl logs <pod> -c <container>`| บันทึกจากคอนเทนเนอร์เฉพาะในพ็อดคอนเทนเนอร์หลายคอนเทนเนอร์ |
| `kubectl exec -it <pod> -- bash`| เปลือกเข้าฝัก |
| `kubectl delete pod <name>`| ลบพ็อด (มันจะถูกสร้างขึ้นใหม่โดยตัวควบคุม) |
| `kubectl rollout status deployment/<name>`| ตรวจสอบความคืบหน้าของการเปิดตัว |
| `kubectl rollout undo deployment/<name>`| ย้อนกลับไปยังเวอร์ชันก่อนหน้า |
### กำลังใช้การกำหนดค่า
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| ใช้รายการ YAML |
| `kubectl apply -f ./dir/`| ใช้ไฟล์ YAML ทั้งหมดในไดเร็กทอรี |
| `kubectl delete -f deployment.yaml`| ลบทรัพยากรที่กำหนดไว้ในไฟล์ YAML |
| `kubectl scale deployment/web --replicas=5`| ปรับขนาดการปรับใช้ |
| `kubectl set image deployment/web web=myapp:2.0`| อัปเดตอิมเมจคอนเทนเนอร์ |
---

## การแสดง Kubernetes ทั่วไป
### การปรับใช้
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

### บริการ
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

### ทางเข้า
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

## พื้นฐานหมวกกันน็อค
Helm เป็นตัวจัดการแพ็คเกจสำหรับ Kubernetes โดยจะรวมทรัพยากร Kubernetes ไว้ในแผนภูมิที่นำมาใช้ซ้ำได้
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| เพิ่มที่เก็บแผนภูมิ |
| `helm repo update`| อัปเดตดัชนีแผนภูมิท้องถิ่น |
| `helm search repo nginx`| ค้นหาแผนภูมิ |
| `helm install my-release bitnami/nginx`| ติดตั้งแผนภูมิ |
| `helm install my-release bitnami/nginx --set replicaCount=3`| ติดตั้งด้วยค่าที่กำหนดเอง |
| `helm install my-release bitnami/nginx -f values.yaml`| ติดตั้งด้วยไฟล์ค่า |
| `helm list`| รายการรุ่นที่ติดตั้ง |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| อัปเกรดรุ่น |
| `helm rollback my-release 1`| ย้อนกลับไปยังการแก้ไขก่อนหน้า |
| `helm uninstall my-release`| ถอนการติดตั้งรุ่น |
| `helm status my-release`| แสดงสถานะการเปิดตัว |
---

## การแก้ไขปัญหาการอ้างอิงด่วน
| ปัญหา | คำสั่งให้ลอง |
|---------|----------------|
| พ็อดไม่เริ่ม | `kubectl describe pod <name>`→ ตรวจสอบ เหตุการณ์ |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ ดูว่าทำไมมันขัดข้อง |
| ข้อผิดพลาดในการดึงรูปภาพ | ตรวจสอบชื่อรูปภาพ แท็ก และข้อมูลรับรองรีจิสทรี |
| ไม่สามารถเข้าถึงบริการได้ | `kubectl get endpoints <service>`→ มีการเลือกพ็อดหรือไม่ |
| OOMKilled | เพิ่มขีดจำกัดหน่วยความจำหรือเพิ่มประสิทธิภาพการใช้หน่วยความจำของแอป |
| พ็อดที่รอดำเนินการ | `kubectl describe pod`→ ตรวจสอบทรัพยากรโหนด, เทนต์, ความสัมพันธ์ |
| ปัญหา DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|