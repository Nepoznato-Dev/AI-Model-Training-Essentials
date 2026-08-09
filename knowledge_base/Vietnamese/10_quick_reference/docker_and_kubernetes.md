---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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
|  __BẢO VỆ_0__ | Xây dựng hình ảnh từ Dockerfile |
|  __BẢO VỆ_1__ | Liệt kê hình ảnh địa phương |
|  __BẢO VỆ_2__ | Kéo hình ảnh từ sổ đăng ký |
|  __BẢO VỆ_3__ | Đẩy hình ảnh vào sổ đăng ký |
|  __BẢO VỆ_4__ | Xóa hình ảnh cục bộ |
|  __BẢO VỆ_5__ | Gắn thẻ hình ảnh cho sổ đăng ký |
|  __BẢO VỆ_6__ | Xóa tất cả hình ảnh không sử dụng |
### Thùng chứa
| Lệnh | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Chạy vùng chứa ở chế độ nền, cổng bản đồ 8080→80 |
|  __BẢO VỆ_1__ | Chạy tương tác với shell |
|  __BẢO VỆ_2__ | Đặt tên vùng chứa và biến môi trường |
|  __BẢO VỆ_3__ | Danh sách các container đang chạy |
|  __BẢO VỆ_4__ | Liệt kê tất cả các container (bao gồm cả đã dừng) |
|  __BẢO VỆ_5__ | Dừng một container đang chạy |
|  __BẢO VỆ_6__ | Bắt đầu một container đã dừng |
|  __BẢO VỆ_7__ | Loại bỏ một container đã dừng |
|  __BẢO VỆ_8__ | Mở shell bên trong container đang chạy |
|  __BẢO VỆ_9__ | Theo dõi nhật ký container |
|  __BẢO VỆ_10__ | Siêu dữ liệu vùng chứa chi tiết (JSON) |
|  __BẢO VỆ_11__ | Sử dụng tài nguyên trực tiếp cho tất cả các vùng chứa |
### Dọn dẹp
| Lệnh | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Xóa tất cả các vùng chứa, hình ảnh, mạng không sử dụng và xây dựng bộ đệm |
|  __BẢO VỆ_1__ | Xóa tất cả các tập không sử dụng |
|  __BẢO VỆ_2__ | Loại bỏ tất cả các container đã dừng |
---

## Tham khảo tệp Docker
### Hướng dẫn chung
| Hướng dẫn | Mục đích | Ví dụ |
|-------------|----------|----------|
|  __BẢO VỆ_0__ | Hình ảnh cơ sở |  __BẢO VỆ_1__ |
|  __BẢO VỆ_2__ | Đặt thư mục làm việc bên trong hình ảnh |  __BẢO VỆ_3__ |
|  __BẢO VỆ_4__ | Sao chép tập tin từ máy chủ vào hình ảnh |  __BẢO VỆ_5__ |
|  __BẢO VỆ_6__ | Giống như COPY, nhưng cũng trích xuất tars và hỗ trợ URL |  __BẢO VỆ_7__ |
|  __BẢO VỆ_8__ | Thực thi lệnh trong quá trình xây dựng |  __BẢO VỆ_9__ |
|  __BẢO VỆ_10__ | Lệnh mặc định khi container khởi động |  __BẢO VỆ_11__ |
|  __BẢO VỆ_12__ | Lệnh cố định; CMD trở thành đối số |  __BẢO VỆ_13__ |
|  __BẢO VỆ_14__ | Đặt biến môi trường |  __BẢO VỆ_15__ |
|  __BẢO VỆ_16__ | Tài liệu ứng dụng sẽ nghe trên cổng nào |  __BẢO VỆ_17__ |
|  __BẢO VỆ_18__ | Biến thời gian xây dựng |  __BẢO VỆ_19__ |
|  __BẢO VỆ_20__ | Chuyển sang người dùng không root |  __BẢO VỆ_21__ |
|  __BẢO VỆ_22__ | Xác định lệnh kiểm tra tình trạng |  __BẢO VỆ_23__ |
|  __BẢO VỆ_24__ | Tạo điểm gắn kết |  __BẢO VỆ_25__ |
### Các phương pháp hay nhất
| Thực hành | Tại sao |
|----------|------|
| Sử dụng hình ảnh mỏng/cơ bản | Hình ảnh nhỏ hơn = kéo nhanh hơn, bề mặt tấn công nhỏ hơn |
| Kết hợp các lệnh RUN với`&&`| Giảm lớp hình ảnh |
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
|  __BẢO VỆ_0__ | Bắt đầu tất cả các dịch vụ ở chế độ nền |
|  __BẢO VỆ_1__ | Dừng và loại bỏ các container, mạng |
|  __BẢO VỆ_2__ | Đồng thời loại bỏ khối lượng |
|  __BẢO VỆ_3__ | Theo dõi nhật ký từ tất cả các dịch vụ |
|  __BẢO VỆ_4__ | Liệt kê các dịch vụ đang chạy |
|  __BẢO VỆ_5__ | Xây dựng lại hình ảnh |
|  __BẢO VỆ_6__ | Chạy lệnh trong một dịch vụ đang chạy |
|  __BẢO VỆ_7__ | Kéo hình ảnh mới nhất |
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
| **Xâm nhập** | Định tuyến HTTP từ bên ngoài cụm tới các dịch vụ |
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
|  __BẢO VỆ_0__ | Chi tiết điểm cuối cụm |
|  __BẢO VỆ_1__ | Liệt kê tất cả các nút |
|  __BẢO VỆ_2__ | Liệt kê các không gian tên |
|  __BẢO VỆ_3__ | Hiển thị bối cảnh cụm hiện tại |
|  __BẢO VỆ_4__ | Chuyển ngữ cảnh |
### Khối lượng công việc
| Lệnh | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Liệt kê các nhóm trong không gian tên hiện tại |
|  __BẢO VỆ_1__ | Liệt kê các nhóm trên tất cả các không gian tên |
|  __BẢO VỆ_2__ | Liệt kê triển khai |
|  __BẢO VỆ_3__ | Liệt kê dịch vụ |
|  __BẢO VỆ_4__ | Liệt kê tài nguyên xâm nhập |
|  __BẢO VỆ_5__ | Thông tin chi tiết về nhóm (sự kiện, trạng thái, thông số kỹ thuật) |
|  __BẢO VỆ_6__ | Xem nhật ký nhóm |
|  __BẢO VỆ_7__ | Theo dõi nhật ký nhóm |
|  __BẢO VỆ_8__ | Nhật ký từ một vùng chứa cụ thể trong nhóm nhiều vùng chứa |
|  __BẢO VỆ_9__ | Vỏ thành một cái vỏ |
|  __BẢO VỆ_10__ | Xóa một nhóm (nó sẽ được bộ điều khiển của nó tạo lại) |
|  __BẢO VỆ_11__ | Kiểm tra tiến độ triển khai |
|  __BẢO VỆ_12__ | Quay lại phiên bản trước |
### Áp dụng cấu hình
| Lệnh | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Áp dụng bảng kê khai YAML |
|  __BẢO VỆ_1__ | Áp dụng tất cả các tệp YAML trong một thư mục |
|  __BẢO VỆ_2__ | Xóa tài nguyên được xác định trong tệp YAML |
|  __BẢO VỆ_3__ | Quy mô triển khai |
|  __BẢO VỆ_4__ | Cập nhật hình ảnh container |
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
|  __BẢO VỆ_0__ | Thêm kho lưu trữ biểu đồ |
|  __BẢO VỆ_1__ | Cập nhật chỉ mục biểu đồ địa phương |
|  __BẢO VỆ_2__ | Tìm kiếm biểu đồ |
|  __BẢO VỆ_3__ | Cài đặt biểu đồ |
|  __BẢO VỆ_4__ | Cài đặt với các giá trị tùy chỉnh |
|  __BẢO VỆ_5__ | Cài đặt bằng tệp giá trị |
|  __BẢO VỆ_6__ | Liệt kê các bản phát hành đã cài đặt |
|  __BẢO VỆ_7__ | Nâng cấp một bản phát hành |
|  __BẢO VỆ_8__ | Quay lại bản sửa đổi trước |
|  __BẢO VỆ_9__ | Gỡ cài đặt một bản phát hành |
|  __BẢO VỆ_10__ | Hiển thị trạng thái phát hành |
---

## Khắc phục sự cố Tham khảo nhanh
| Vấn đề | Các lệnh cần thử |
|----------|-------|
| Pod không bắt đầu | `kubectl describe pod <name>`→ kiểm tra Sự kiện |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ xem tại sao nó bị lỗi |
| Lỗi kéo ảnh | Kiểm tra tên hình ảnh, thẻ và thông tin đăng ký |
| Dịch vụ không thể truy cập | `kubectl get endpoints <service>`→ nhóm có được chọn không? |
| OOMGiết | Tăng giới hạn bộ nhớ hoặc tối ưu hóa việc sử dụng bộ nhớ ứng dụng |
| Nhóm đang chờ xử lý | `kubectl describe pod`→ kiểm tra tài nguyên nút, vết bẩn, mối quan hệ |
| Vấn đề về DNS |  __BẢO VỆ_4__ |