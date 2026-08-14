<!--
---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# DevOps và CI/CD
DevOps là sự kết hợp giữa triết lý văn hóa, thực tiễn và công cụ cho phép các nhóm cung cấp phần mềm nhanh hơn và đáng tin cậy hơn. Nó phá vỡ bức tường giữa các nhà phát triển (những người muốn thực hiện các thay đổi) và các hoạt động (những người muốn sự ổn định). CI/CD — Tích hợp liên tục và Phân phối liên tục — là xương sống tự động hóa giúp điều này trở nên khả thi.
---

## Đường ống CI/CD
### CI/CD thực sự có nghĩa là gì
| Kỳ hạn | Nó làm gì |
|------|-------------|
| **Tích hợp liên tục (CI)** | Các nhà phát triển thường xuyên hợp nhất mã; mỗi lần hợp nhất sẽ kích hoạt các bản dựng và thử nghiệm tự động |
| **Giao hàng liên tục (CD)** | Mã luôn ở trạng thái có thể triển khai được; phát hành vào sản xuất là một quyết định thủ công |
| **Triển khai liên tục** | Mọi thay đổi vượt qua thử nghiệm sẽ tự động được đưa vào sản xuất — không cần cổng thủ công |
### Các giai đoạn đường ống điển hình
| Sân khấu | Điều gì xảy ra | Công cụ |
|-------|-------------|-------|
| **Nguồn** | Nhà phát triển đẩy mã tới Git | GitHub, GitLab, Bitbucket |
| **Xây dựng** | Biên dịch mã, cài đặt phụ thuộc | Maven, Gradle, npm, pip |
| **Kiểm tra** | Chạy đơn vị, tích hợp, kiểm tra lỗi mã nguồn | Jest, pytest, JUnit |
| **Gói** | Xây dựng hình ảnh hoặc tạo tác Docker | Docker, Gói xây dựng |
| **Triển khai (dàn dựng)** | Triển khai vào môi trường dàn dựng | Kubernetes, ECS, VM |
| **Thử nghiệm (dàn dựng)** | Kiểm tra tích hợp, kiểm tra khói | Selenium, Người đưa thư |
| **Triển khai (sản xuất)** | Phát hành để sản xuất | Xanh lam, hoàng yến, lăn |
| **Giám sát** | Quan sát tình trạng, lỗi, hiệu suất | Prometheus, Grafana, Datadog |
### So sánh các công cụ CI/CD
| Công cụ | Loại | Sức mạnh |
|------|------|----------|
| **Hành động GitHub** | CI/CD đám mây | Tích hợp sâu với GitHub; Quy trình công việc YAML |
| **CI GitLab** | CI/CD tích hợp | Nền tảng duy nhất cho repo + đường ống |
| **Jenkins** | CI/CD tự lưu trữ | Cấu hình cao; hệ sinh thái plugin lớn |
| **CircleCI** | CI/CD đám mây | Nhanh; tốt cho quy trình công việc được chứa trong container |
| **ArgoCD** | GitOps cho Kubernetes | Triển khai khai báo, dựa trên Git |
---

## Docker và Container
### Tại sao lại là Container?
Trước các container, vấn đề kinh điển là "nó hoạt động trên máy của tôi". Bộ chứa giải quyết vấn đề này bằng cách đóng gói một ứng dụng với tất cả các phần phụ thuộc của nó — thư viện, thời gian chạy, cấu hình — vào một thiết bị di động duy nhất chạy giống hệt nhau ở mọi nơi.
### Những điều cơ bản về Docker
| Khái niệm | Mô tả |
|----------|-------------|
| **Hình ảnh** | Mẫu chỉ đọc có ứng dụng + phần phụ thuộc |
| **Bình chứa** | Phiên bản đang chạy của một hình ảnh |
| **Tệp Docker** | Công thức xây dựng hình ảnh |
| **Đăng ký** | Lưu trữ hình ảnh (Docker Hub, ECR, GCR) |
| **Khối lượng** | Bộ lưu trữ liên tục vẫn tồn tại khi khởi động lại vùng chứa |
| **Mạng** | Lớp mạng biệt lập cho container |
### Các phương pháp hay nhất về Dockerfile
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Các phương pháp chính: sử dụng hình ảnh cơ sở mỏng/alpine, chạy dưới dạng không phải root, tận dụng bộ nhớ đệm lớp, sử dụng`.dockerignore`, quét hình ảnh để tìm lỗ hổng (`trivy`,`docker scan`) và đặt giới hạn tài nguyên.
### Soạn Docker
Để chạy nhiều container cùng nhau (ứng dụng + cơ sở dữ liệu + bộ đệm):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8)
Kubernetes là bộ điều phối container tiêu chuẩn công nghiệp. Nó quản lý việc triển khai, mở rộng quy mô và vận hành các ứng dụng được đóng gói.
### Kiến trúc cốt lõi
| Thành phần | Vai trò |
|----------||------|
| **Mặt phẳng điều khiển** | Quản lý cụm (máy chủ API, bộ lập lịch, etcd, trình quản lý bộ điều khiển) |
| **Nút** | Máy công nhân (VM hoặc vật lý) chạy container |
| **Pod** | Đơn vị có thể triển khai nhỏ nhất; một hoặc nhiều container chia sẻ mạng |
| **Dịch vụ** | Điểm cuối mạng ổn định định tuyến lưu lượng truy cập đến nhóm |
| **Triển khai** | Định nghĩa khai báo về trạng thái nhóm mong muốn (bản sao, hình ảnh, v.v.) |
| **Xâm nhập** | Quy tắc định tuyến HTTP cho lưu lượng truy cập bên ngoài |
| **Bản đồ cấu hình / Bí mật** | Cấu hình và dữ liệu nhạy cảm được đưa vào nhóm |
### Các lệnh kubectl cần thiết
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Mũ bảo hiểm
Helm là người quản lý gói cho Kubernetes. **biểu đồ** là một gói tài nguyên Kubernetes được định cấu hình sẵn. Hãy nghĩ về nó như`apt`hoặc`brew`cho K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Cơ sở hạ tầng dưới dạng mã (IaC)
IaC xử lý cấu hình cơ sở hạ tầng giống như cách bạn xử lý mã ứng dụng: được kiểm soát phiên bản, thử nghiệm và triển khai thông qua quy trình.
### Terraform vs Ansible
| Công cụ | Loại | Tiếp cận | Tốt nhất cho |
|------|------|----------|----------|
| **Địa hình** | Cung cấp | Khai báo (HCL); dựa trên nhà nước | Tạo tài nguyên đám mây (VPC, VM, cơ sở dữ liệu) |
| **Ansible** | Cấu hình | Khai báo (YAML); vô dụng | Cấu hình server, cài đặt phần mềm |
| **Pulumi** | Cung cấp | Bắt buộc (Python, Go, TS) | Các nhóm thích ngôn ngữ lập trình thực tế |
| **CloudFormation** | Cung cấp | Khai báo (YAML/JSON); Bản địa AWS | Cơ sở hạ tầng chỉ dành cho AWS |
### Ví dụ về địa hình
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Cách thực hành tốt nhất: sử dụng mô-đun để có thể sử dụng lại, lưu trữ trạng thái từ xa (S3 + DynamoDB để khóa), không bao giờ mã hóa bí mật và kiểm soát phiên bản mọi thứ.
---

## Giám sát và quan sát
###Ba trụ cột
| Trụ cột | Nó nói gì với bạn | Công cụ |
|--------|------------------------|-------|
| **Số liệu** | Đo lường số theo thời gian (CPU, tỷ lệ yêu cầu, tỷ lệ lỗi) | Prometheus, CloudWatch, Datadog |
| **Nhật ký** | Các sự kiện riêng biệt có ngữ cảnh (lỗi, yêu cầu, thay đổi trạng thái) | Ngăn xếp ELK, Loki, Nhật ký CloudWatch |
| **Dấu vết** | Hành trình yêu cầu từ đầu đến cuối trên các dịch vụ | Jaeger, X-Ray, Zipkin |
### Prometheus + Grafana Stack
Ngăn xếp giám sát nguồn mở tiêu chuẩn:
| Thành phần | Vai trò |
|----------||------|
| **Prometheus** | Cơ sở dữ liệu chuỗi thời gian; lấy số liệu từ dịch vụ |
| **Grafana** | Trực quan hóa và bảng điều khiển |
| **Quản lý cảnh báo** | Định tuyến cảnh báo tới Slack, PagerDuty, email |
| **Trình xuất nút** | Hiển thị các số liệu cấp hệ thống (CPU, RAM, đĩa) |
| **Nhà xuất khẩu hộp đen** | Thăm dò điểm cuối (HTTP, TCP, ICMP) |
### Các số liệu chính cần theo dõi
| Danh mục | Số liệu |
|----------|----------|
| **Cơ sở hạ tầng** | CPU, RAM, mức sử dụng ổ đĩa, I/O mạng |
| **Ứng tuyển** | Tỷ lệ yêu cầu, độ trễ (p50, p95, p99), tỷ lệ lỗi |
| **Cơ sở dữ liệu** | Số lượng truy vấn, truy vấn chậm, mức sử dụng nhóm kết nối |
| **Kinh doanh** | Đăng ký, chuyển đổi, doanh thu |
---

## Chiến lược triển khai
| Chiến lược | Nó hoạt động như thế nào | Rủi ro | Khôi phục |
|----------|-------------|------|----------|
| **Cập nhật liên tục** | Thay thế dần phiên bản cũ bằng phiên bản mới | Một số người dùng cũ, một số người dùng phiên bản mới | Hoàn nguyên về hình ảnh trước đó |
| **Xanh-Xanh** | Chạy hai môi trường giống hệt nhau; chuyển giao thông | Chi phí cơ sở hạ tầng tăng gấp đôi trong quá trình chuyển đổi | Chuyển trở lại ngay lập tức |
| **Chim hoàng yến** | Định tuyến % lưu lượng truy cập nhỏ sang phiên bản mới; tăng dần | Quản lý giao thông phức tạp | Tuyến đường giao thông trở lại ổn định |
| **Cờ tính năng** | Triển khai mã nhưng ẩn các tính năng đằng sau nút chuyển đổi | Độ phức tạp của mã từ logic có điều kiện | Tắt |
---

## GitOps
GitOps đưa IaC đến kết luận hợp lý: kho lưu trữ Git là nguồn thông tin chính xác duy nhất về trạng thái mong muốn của cơ sở hạ tầng và ứng dụng của bạn.
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Khai báo** | Mọi thứ được mô tả dưới dạng mã (YAML, HCL) |
| **Đã phiên bản** | Git là nguồn gốc của sự thật |
| **Tự động** | Công cụ liên tục đối chiếu trạng thái mong muốn với trạng thái thực tế |
| **Có thể kiểm toán** | Mọi thay đổi đều là một cam kết Git |
**ArgoCD** và **Flux** là những công cụ GitOps hàng đầu dành cho Kubernetes. Bạn đẩy một thay đổi vào kho lưu trữ Git của mình và công cụ sẽ tự động triển khai thay đổi đó vào cụm.
---

## Ứng phó sự cố
Khi có thứ gì đó bị hỏng lúc 3 giờ sáng:
1. **Xác nhận** cảnh báo.
2. **Đánh giá phạm vi**: dịch vụ, người dùng và dữ liệu nào bị ảnh hưởng?
3. **Xác định** nguyên nhân gốc rễ — kiểm tra nhật ký, số liệu, hoạt động triển khai gần đây.
4. **Chứa** nếu có thể — bộ ngắt mạch, cờ tính năng, dịch chuyển giao thông.
5. **Khắc phục** — khôi phục hoặc vá tiếp.
6. **Giao tiếp** — cập nhật các bên liên quan và người dùng (trang trạng thái).
7. **Sau khi khám nghiệm tử thi** — trong vòng 24–48 giờ, ghi lại nguyên nhân gốc rễ và các mục hành động.
Mục tiêu không chỉ là giải quyết sự cố mà còn đảm bảo sự cố tương tự không thể tái diễn.