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
# Bảng cheat Docker và Kubernetes
Tài liệu tham khảo thực tế về việc chứa các ứng dụng bằng Docker và sắp xếp chúng với Kubernetes. Giả sử sự quen thuộc cơ bản với dòng lệnh.
---

## Nguyên tắc cơ bản về Docker
| Khái niệm | Mô tả |
|----------|-------------|
| **Hình ảnh** | Mẫu chỉ đọc có mã ứng dụng + phần phụ thuộc + thư viện hệ điều hành |
| **Bình chứa** | Phiên bản đang chạy của một hình ảnh; quá trình cô lập |
| **Tệp Docker** | Công thức xây dựng hình ảnh |
| **Đăng ký** | Lưu trữ hình ảnh (Docker Hub, ECR, GCR, GHCR) |
| **Khối lượng** | Bộ lưu trữ liên tục vẫn tồn tại khi khởi động lại vùng chứa |
| **Mạng** | Container kết nối mạng ảo |
---

## Các lệnh Docker cần thiết
### Hình ảnh
| Lệnh | Mô tả |
|----------|-------------|
| `docker build -t myapp:1.0 .`| Xây dựng hình ảnh từ Dockerfile |
| `docker images`| Liệt kê hình ảnh địa phương |
| `docker pull nginx:latest`| Kéo hình ảnh từ sổ đăng ký |
| `docker push myrepo/myapp:1.0`| Đẩy hình ảnh vào sổ đăng ký |
| `docker rmi myapp:1.0`| Xóa hình ảnh cục bộ |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Gắn thẻ hình ảnh cho sổ đăng ký |
| `docker image prune -a`| Xóa tất cả hình ảnh không sử dụng |
### Thùng chứa
| Lệnh | Mô tả |
|----------|-------------|
| `docker run -d -p 8080:80 nginx`| Chạy vùng chứa ở chế độ nền, cổng bản đồ 8080→80 |
| `docker run -it ubuntu bash`| Chạy tương tác với shell |
| `docker run --name web -e DB_HOST=db nginx`| Đặt tên vùng chứa và biến môi trường |
| `docker ps`| Danh sách các container đang chạy |
| `docker ps -a`| Liệt kê tất cả các container (bao gồm cả đã dừng) |
| `docker stop web`| Dừng một container đang chạy |
| `docker start web`| Bắt đầu một container đã dừng |
| `docker rm web`| Loại bỏ một container đã dừng |
| `docker exec -it web bash`| Mở shell bên trong container đang chạy |
| `docker logs -f web`| Theo dõi nhật ký container |
| `docker inspect web`| Siêu dữ liệu vùng chứa chi tiết (JSON) |
| `docker stats`| Sử dụng tài nguyên trực tiếp cho tất cả các vùng chứa |
### Dọn dẹp
| Lệnh | Mô tả |
|----------|-------------|
| `docker system prune -a`| Xóa tất cả các vùng chứa, hình ảnh, mạng không sử dụng và xây dựng bộ đệm |
| `docker volume prune`| Xóa tất cả các tập không sử dụng |
| `docker container prune`| Loại bỏ tất cả các container đã dừng |
---

## Tham khảo tệp Docker
### Hướng dẫn chung
| Hướng dẫn | Mục đích | Ví dụ |
|-------------|----------|----------|
| `FROM`| Hình ảnh cơ sở | `FROM python:3.12-slim`|
| `WORKDIR`| Đặt thư mục làm việc bên trong hình ảnh | `WORKDIR /app`|
| `COPY`| Sao chép tập tin từ máy chủ vào hình ảnh | `COPY requirements.txt .`|
| `ADD`| Giống như COPY, nhưng cũng trích xuất tars và hỗ trợ URL | `ADD app.tar.gz /app/`|
| `RUN`| Thực thi lệnh trong quá trình xây dựng | `RUN pip install -r requirements.txt`|
| `CMD`| Lệnh mặc định khi container khởi động | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Lệnh cố định; CMD trở thành đối số | `ENTRYPOINT ["python"]`|
| `ENV`| Đặt biến môi trường | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Tài liệu ứng dụng sẽ nghe trên cổng nào | `EXPOSE 8000`|
| `ARG`| Biến thời gian xây dựng | `ARG VERSION=1.0`|
| `USER`| Chuyển sang người dùng không root | `USER appuser`|
| `HEALTHCHECK`| Xác định lệnh kiểm tra tình trạng | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Tạo điểm gắn kết | `VOLUME /data`|
### Các phương pháp hay nhất
| Thực hành | Tại sao |
|----------|------|
| Sử dụng hình ảnh mỏng/cơ bản | Hình ảnh nhỏ hơn = kéo nhanh hơn, bề mặt tấn công nhỏ hơn |
| Kết hợp lệnh RUN với`&&`| Giảm lớp hình ảnh |
| Sao chép các tệp phụ thuộc trước, sau đó mã | Tận dụng bộ đệm xây dựng của Docker |
| Sử dụng`.dockerignore`| Loại trừ`node_modules`,`.git`,`__pycache__`|
| Chạy với tư cách người dùng không phải root | Thực hành tốt nhất về bảo mật |
| Sử dụng các bản dựng nhiều giai đoạn | Xây dựng và thời gian chạy riêng biệt; hình ảnh cuối cùng nhỏ hơn |
| Pin phiên bản hình ảnh cơ sở | Các bản dựng có thể tái tạo (`python:3.12.1-slim`, không phải`python:latest`) |
### Ví dụ về bản dựng nhiều giai đoạn
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

## Soạn Docker
Docker Compose xác định các ứng dụng nhiều vùng chứa trong một tệp YAML duy nhất.
### Các lệnh chính
| Lệnh | Mô tả |
|----------|-------------|
| `docker compose up -d`| Bắt đầu tất cả các dịch vụ ở chế độ nền |
| `docker compose down`| Dừng và loại bỏ các container, mạng |
| `docker compose down -v`| Đồng thời loại bỏ khối lượng |
| `docker compose logs -f`| Theo dõi nhật ký từ tất cả các dịch vụ |
| `docker compose ps`| Liệt kê các dịch vụ đang chạy |
| `docker compose build`| Xây dựng lại hình ảnh |
| `docker compose exec web bash`| Chạy lệnh trong một dịch vụ đang chạy |
| `docker compose pull`| Kéo hình ảnh mới nhất |
### Ví dụ soạn tập tin
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

## Kiến trúc Kubernetes
| Thành phần | Vai trò |
|----------||------|
| **Cụm** | Một tập hợp các nút (máy) chạy các ứng dụng được đóng gói |
| **Mặt phẳng điều khiển** | Máy chủ API, bộ lập lịch, trình quản lý bộ điều khiển, v.v. (trạng thái cụm) |
| **Nút** | Một máy công nhân (VM hoặc vật lý) chạy nhóm |
| **Pod** | Đơn vị nhỏ nhất; một hoặc nhiều thùng chứa được liên kết chặt chẽ |
| **Triển khai** | Quản lý bản sao của một nhóm; xử lý các bản cập nhật luân phiên |
| **Dịch vụ** | Điểm cuối mạng ổn định cho một nhóm nhóm |
| **Xâm nhập** | Định tuyến HTTP từ bên ngoài cụm đến các dịch vụ |
| **Bản đồ cấu hình** | Dữ liệu cấu hình không bí mật |
| **Bí mật** | Dữ liệu nhạy cảm (được mã hóa base64) |
| **Không gian tên** | Cách ly logic trong một cụm |
| **Khối lượng liên tục (PV)** | Tài nguyên lưu trữ cấp cụm |
| **Yêu cầu khối lượng liên tục (PVC)** | Yêu cầu lưu trữ theo nhóm |
---

## Lệnh kubectl
### Thông tin cụm
| Lệnh | Mô tả |
|----------|-------------|
| `kubectl cluster-info`| Chi tiết điểm cuối cụm |
| `kubectl get nodes`| Liệt kê tất cả các nút |
| `kubectl get namespaces`| Liệt kê các không gian tên |
| `kubectl config current-context`| Hiển thị bối cảnh cụm hiện tại |
| `kubectl config use-context prod`| Chuyển ngữ cảnh |
### Khối lượng công việc
| Lệnh | Mô tả |
|----------|-------------|
| `kubectl get pods`| Liệt kê các nhóm trong không gian tên hiện tại |
| `kubectl get pods -A`| Liệt kê các nhóm trên tất cả các không gian tên |
| `kubectl get deployments`| Liệt kê triển khai |
| `kubectl get services`| Liệt kê dịch vụ |
| `kubectl get ingress`| Liệt kê tài nguyên xâm nhập |
| `kubectl describe pod <name>`| Thông tin chi tiết về nhóm (sự kiện, trạng thái, thông số kỹ thuật) |
| `kubectl logs <pod>`| Xem nhật ký nhóm |
| `kubectl logs -f <pod>`| Theo dõi nhật ký nhóm |
| `kubectl logs <pod> -c <container>`| Nhật ký từ một vùng chứa cụ thể trong nhóm nhiều vùng chứa |
| `kubectl exec -it <pod> -- bash`| Vỏ thành một cái vỏ |
| `kubectl delete pod <name>`| Xóa một nhóm (nó sẽ được bộ điều khiển của nó tạo lại) |
| `kubectl rollout status deployment/<name>`| Kiểm tra tiến độ triển khai |
| `kubectl rollout undo deployment/<name>`| Quay lại phiên bản trước |
### Áp dụng cấu hình
| Lệnh | Mô tả |
|----------|-------------|
| `kubectl apply -f deployment.yaml`| Áp dụng bảng kê khai YAML |
| `kubectl apply -f ./dir/`| Áp dụng tất cả các tệp YAML trong một thư mục |
| `kubectl delete -f deployment.yaml`| Xóa tài nguyên được xác định trong tệp YAML |
| `kubectl scale deployment/web --replicas=5`| Quy mô triển khai |
| `kubectl set image deployment/web web=myapp:2.0`| Cập nhật hình ảnh container |
---

## Bản kê khai Kubernetes phổ biến
### Triển khai
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

### Dịch vụ
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

### Xâm nhập
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

## Thông tin cơ bản về mũ bảo hiểm
Helm là người quản lý gói cho Kubernetes. Nó đóng gói tài nguyên Kubernetes vào các biểu đồ có thể tái sử dụng.
| Lệnh | Mô tả |
|----------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Thêm kho lưu trữ biểu đồ |
| `helm repo update`| Cập nhật chỉ số biểu đồ địa phương |
| `helm search repo nginx`| Tìm kiếm biểu đồ |
| `helm install my-release bitnami/nginx`| Cài đặt biểu đồ |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Cài đặt với các giá trị tùy chỉnh |
| `helm install my-release bitnami/nginx -f values.yaml`| Cài đặt bằng tệp giá trị |
| `helm list`| Liệt kê các bản phát hành đã cài đặt |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Nâng cấp một bản phát hành |
| `helm rollback my-release 1`| Quay lại bản sửa đổi trước |
| `helm uninstall my-release`| Gỡ cài đặt một bản phát hành |
| `helm status my-release`| Hiển thị trạng thái phát hành |
---

## Khắc phục sự cố Tham khảo nhanh
| Vấn đề | Các lệnh cần thử |
|----------|----------------|
| Pod không bắt đầu | `kubectl describe pod <name>`→ kiểm tra Sự kiện |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ xem tại sao nó bị lỗi |
| Lỗi kéo ảnh | Kiểm tra tên hình ảnh, thẻ và thông tin đăng ký |
| Dịch vụ không thể truy cập | `kubectl get endpoints <service>`→ nhóm có được chọn không? |
| OOMGiết | Tăng giới hạn bộ nhớ hoặc tối ưu hóa việc sử dụng bộ nhớ ứng dụng |
| Nhóm đang chờ xử lý | `kubectl describe pod`→ kiểm tra tài nguyên nút, vết bẩn, mối quan hệ |
| Vấn đề về DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|