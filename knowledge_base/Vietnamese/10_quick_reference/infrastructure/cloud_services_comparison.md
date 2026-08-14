---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
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
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# So sánh dịch vụ đám mây
Bảng so sánh song song của ba nhà cung cấp đám mây lớn — AWS, Azure và Google Cloud — trên các lĩnh vực điện toán, lưu trữ, cơ sở dữ liệu, AI/ML, kết nối mạng, giám sát và cơ sở hạ tầng dưới dạng mã. Hữu ích cho các kiến ​​trúc sư quyết định nên sử dụng nền tảng nào hoặc ánh xạ các dịch vụ từ đám mây này sang đám mây khác.
---

## Tổng quan về nhà cung cấp
| | AWS | Azure | Đám mây của Google (GCP) |
|---|------|-------|----------------------|
| **Thị phần** | ~31% (lớn nhất) | ~25% (giây) | ~11% (thứ ba, tăng trưởng nhanh nhất) |
| **Điểm mạnh** | Bề rộng của dịch vụ; trưởng thành; hệ sinh thái | Tích hợp doanh nghiệp; đám mây lai; ngăn xếp của Microsoft | Dữ liệu/AI; Kubernetes; mạng lưới toàn cầu |
| **Tốt nhất cho** | Khởi nghiệp cho doanh nghiệp; danh mục dịch vụ rộng nhất | Doanh nghiệp có Microsoft/Active Directory; lai | Khối lượng công việc sử dụng nhiều dữ liệu; Kubernetes-bản địa; AI/ML |
| **Khu vực** | 33 vùng, 105 AZ | Hơn 60 khu vực | Hơn 40 khu vực, hơn 100 khu vực |
| **Cấp miễn phí** | Bậc miễn phí 12 tháng + luôn miễn phí | 12 tháng miễn phí + tín dụng $200 | Khoản tín dụng $300 trong 90 ngày + luôn miễn phí |
---

## Tính toán
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **Máy ảo** | EC2 (Đám mây điện toán đàn hồi) | Máy ảo | Công cụ tính toán |
| **Tự động mở rộng quy mô** | Nhóm tự động chia tỷ lệ | Bộ cân máy ảo | Nhóm phiên bản |
| **Chức năng phi máy chủ** | Lambda | Chức năng Azure | Chức năng đám mây |
| **Đăng ký vùng chứa** | ECR (Đăng ký vùng chứa đàn hồi) | Đăng ký vùng chứa Azure | Đăng ký hiện vật |
| **Dàn nhạc vùng chứa** | ECS / EKS | ACS / AKS | GKE / Chạy trên nền tảng đám mây |
| **Vùng chứa không có máy chủ** | Cổng xa | Ứng dụng vùng chứa | Chạy trên đám mây |
| **Nền tảng ứng dụng (PaaS)** | Cây đậu đàn hồi, Người chạy ứng dụng | Dịch vụ ứng dụng | Công cụ ứng dụng |
| **Xử lý hàng loạt** | Lô AWS | Lô Azure | Lô đám mây |
| **Tính toán GPU / AI** | EC2 (phiên bản P4d, P5) | Máy ảo dòng NC/ND | Máy ảo A2/A3; TPU |
### Mô hình định giá VM
| Người mẫu | AWS | Azure | GCP |
|-------|------|-------|------|
| **Theo yêu cầu** | Phiên bản theo yêu cầu | Trả tiền khi bạn sử dụng | Theo yêu cầu |
| **Dành riêng / Đã cam kết** | Phiên bản dự trữ (1–3 năm) | Máy ảo dự trữ (1–3 năm) | Cam kết giảm giá sử dụng (1–3 năm) |
| **Tại chỗ / Gián đoạn** | Phiên bản Spot | Máy ảo tại chỗ | Máy ảo ưu tiên / Spot |
| **Kế hoạch tiết kiệm** | Kế hoạch tiết kiệm | Kế hoạch tiết kiệm | Cam kết giảm giá sử dụng |
---

## Kho
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **Lưu trữ đối tượng** | S3 | Lưu trữ Blob | Lưu trữ đám mây |
| **Khối lưu trữ** | EBS | Đĩa được quản lý | Đĩa liên tục |
| **Lưu trữ tệp** | EFS, FSx | Tệp Azure | Kho tập tin |
| **Lưu trữ / Lạnh** | Sông băng S3, Kho lưu trữ sâu | Cấp độ Blob Cool/Lưu trữ | Đường dây lạnh lưu trữ đám mây/Lưu trữ |
| **Truyền dữ liệu** | Quả cầu tuyết, DataSync | Hộp dữ liệu | Chuyển Thiết bị |
### So sánh các lớp lưu trữ
| Trường hợp sử dụng | AWS S3 | Azure Blob | Lưu trữ đám mây GCP |
|----------|--------|-------------|-------------------|
| **Truy cập thường xuyên** | Tiêu chuẩn S3 | Nóng | Tiêu chuẩn |
| **Truy cập không thường xuyên** | Tiêu chuẩn S3-IA | Tuyệt vời | Gần tuyến |
| **Quyền truy cập hiếm** | S3 Một Vùng-IA | — | Đường dây lạnh |
| **Lưu trữ** | Sông băng S3 / Lưu trữ sâu | Lưu trữ | Lưu trữ |
---

## Cơ sở dữ liệu
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **Quan hệ (được quản lý)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Cơ sở dữ liệu Azure (MySQL, PostgreSQL); Azure SQL | Đám mây SQL (MySQL, PostgreSQL) |
| **Quan hệ (bản địa trên nền tảng đám mây)** | Aurora (tương thích với MySQL/PostgreSQL) | Cơ sở dữ liệu Azure SQL (nhóm đàn hồi) | Cloud Spanner (phân phối toàn cầu) |
| **NoSQL (tài liệu)** | DynamoDB | Cosmos DB (API MongoDB, API SQL) | Cửa hàng cứu hỏa; Kho dữ liệu |
| **NoSQL (cột rộng)** | DynamoDB (cũng) | Cosmos DB (API Cassandra) | Bàn lớn |
| **NoSQL (khóa-giá trị)** | DynamoDB, ElastiCache | Bộ đệm Azure cho Redis | Kho lưu trữ bộ nhớ (Redis) |
| **Biểu đồ** | Sao Hải Vương | Cosmos DB (API Gremlin) | — |
| **Dòng thời gian** | Dòng thời gian | Trình khám phá dữ liệu Azure | — |
| **Sổ cái** | QLDB | Sổ cái bí mật Azure | — |
| **Bộ nhớ đệm trong bộ nhớ** | ElastiCache (Redis, Memcached) | Bộ đệm Azure cho Redis | Kho ký ức |
| **Tìm kiếm** | Dịch vụ tìm kiếm mở | Tìm kiếm AI Azure | Tìm kiếm trên đám mây; Tìm kiếm AI của Vertex |
| **Kho dữ liệu** | Dịch chuyển đỏ | Phân tích khớp thần kinh | BigQuery |
---

## AI và học máy
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **Nền tảng ML** | SageMaker | Học máy Azure | AI đỉnh |
| **API được đào tạo trước** | Nhận thức (tầm nhìn), Polly (TTS), Hiểu (NLP), Ghi chép | Dịch vụ nhận thức (Tầm nhìn, Lời nói, Ngôn ngữ, Quyết định) | Vision AI, Chuyển giọng nói thành văn bản, API ngôn ngữ tự nhiên |
| **LLM / AI sáng tạo** | Bedrock (Claude, Llama, Titan) | Dịch vụ Azure OpenAI (GPT-4, DALL-E) | Vertex AI (Song Tử); Vườn Mẫu |
| **Vector / Phần nhúng** | OpenSearch (k-NN), Cơ sở Kiến thức Bedrock | Tìm kiếm AI Azure (vector) | Tìm kiếm vectơ AI của Vertex, AlloyDB |
| **MLOps** | Quy trình SageMaker, Đăng ký mô hình | Đường ống Azure ML, Sổ đăng ký mẫu | Đường ống AI của Vertex, Đăng ký mô hình |
| **Ghi nhãn dữ liệu** | Sự thật cơ bản của SageMaker | Ghi nhãn dữ liệu Azure ML | Ghi nhãn dữ liệu AI của Vertex |
| **AI đàm thoại** | Lex | Dịch vụ Bot Azure | Hộp thoại CX/ES |
| **Dịch** | Dịch | Người phiên dịch | API dịch |
---

## Kết nối mạng
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **Mạng ảo** | VPC | Mạng ảo (VNet) | VPC |
| **Cân bằng tải** | ELB/ALB/NLB/CLB | Cân bằng tải (Ứng dụng, Mạng, Cổng) | Cân bằng tải trên đám mây |
| **DNS** | Tuyến 53 | DNS Azure | DNS đám mây |
| **CDN** | CloudFront | Cửa trước Azure | CDN đám mây |
| **Cổng API** | Cổng API | Quản lý API | Cổng API |
| **VPN** | VPN site-to-site, VPN máy khách | Cổng VPN | VPN đám mây |
| **Kết nối trực tiếp / ExpressRoute** | Kết nối trực tiếp | ExpressRoute | Kết nối đám mây |
| **Liên kết riêng** | Liên kết riêng tư, Điểm cuối VPC | Liên kết riêng tư, Điểm cuối riêng tư | Kết nối dịch vụ riêng |
| **Tường lửa** | WAF, Tường lửa mạng | Tường lửa Azure, WAF | Áo giáp đám mây, Tường lửa |
| **Bảo vệ DDoS** | Khiên Tiêu chuẩn / Nâng cao | Bảo vệ DDoS | Giáp Mây |
---

## Giám sát và ghi nhật ký
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **Số liệu / Giám sát** | CloudWatch | Màn hình Azure | Giám sát đám mây (Stackdriver) |
| **Ghi nhật ký** | Nhật ký CloudWatch | Phân tích nhật ký (Nhật ký giám sát Azure) | Ghi nhật ký trên đám mây |
| **Truy tìm** | Tia X | Thông tin chi tiết về ứng dụng | Dấu vết đám mây |
| **Cảnh báo** | Cảnh báo CloudWatch | Cảnh báo màn hình Azure | Cảnh báo giám sát đám mây |
| **Bảng điều khiển** | Bảng thông tin CloudWatch | Sổ làm việc / Bảng thông tin Azure | Bảng điều khiển giám sát đám mây |
| **Theo dõi lỗi** | Tổng hợp CloudWatch | Thông tin chi tiết về ứng dụng | Báo cáo lỗi đám mây |
| **Bên thứ ba** | Datadog, Di tích mới, PagerDuty | Datadog, Di tích mới, PagerDuty | Datadog, Di tích mới, PagerDuty |
---

## Cơ sở hạ tầng dưới dạng Mã và DevOps
| Danh mục dịch vụ | AWS | Azure | GCP |
|-----------------|------|-------|------|
| **IaC (bản địa)** | CloudFormation | Mẫu ARM / Bắp tay | Giám đốc triển khai / Pulumi |
| **IaC (đám mây chéo)** | Địa hình, Pulumi, CDK | Địa hình, Pulumi, Bắp tay | Địa hình, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, Hành động GitHub | Xây dựng đám mây; Triển khai đám mây |
| **Đăng ký vùng chứa** | ECR | Đăng ký vùng chứa Azure | Đăng ký hiện vật |
| **GitOps** | Lưới ứng dụng + Flux/ArgoCD | Flux/ArgoCD trên AKS | Đồng bộ hóa cấu hình (Anthos) |
| **Quản lý bí mật** | Trình quản lý bí mật, Lưu trữ thông số SSM | Kho chìa khóa | Người quản lý bí mật |
---

## Cân nhắc về giá
| Yếu tố | AWS | Azure | GCP |
|--------|------|-------|------|
| **Chi tiết thanh toán** | Mỗi giây (sau giờ đầu tiên đối với một số người) | Mỗi giây | Mỗi giây |
| **Giảm giá sử dụng liên tục** | Phiên bản dự trữ/Gói tiết kiệm | Máy ảo dành riêng | Cam kết giảm giá sử dụng |
| **Các trường hợp tại chỗ** | Giảm giá tới 90% | Giảm giá tới 90% | Giảm giá tới 91% |
| **Đầu ra dữ liệu** | Tính phí (đắt) | Đã tính phí | Cùng một mức giá bất kể điểm đến (thường rẻ hơn) |
| **Cấp miễn phí** | 12 tháng + luôn miễn phí | 12 tháng + khoản tín dụng $200 | $300 trong 90 ngày + luôn miễn phí |
| **Giảm giá doanh nghiệp** | Chương trình chiết khấu doanh nghiệp (EDP) | MACC (Hợp đồng cam kết tiền tệ) | Cam kết sử dụng + CUD |
---

## Khi nào nên sử dụng cái nào
| Kịch bản | Được đề xuất | Tại sao |
|----------|-------------|------|
| **Lựa chọn dịch vụ rộng nhất; hệ sinh thái trưởng thành** | AWS | Danh mục lớn nhất; hầu hết các tích hợp của bên thứ ba |
| **Doanh nghiệp Microsoft; Thư mục hoạt động; lai** | Azure | Tích hợp AD gốc; dụng cụ lai mạnh mẽ |
| **Kho dữ liệu; BigQuery; phân tích nặng** | GCP | BigQuery là tốt nhất trong lớp; tích hợp dữ liệu liền mạch |
| **Phát triển dựa trên Kubernetes** | GCP | GKE là Kubernetes được quản lý bóng bẩy nhất |
| **Ứng dụng AI / LLM sáng tạo** | Azure hoặc GCP | Azure OpenAI cho các mô hình GPT; Vertex AI dành cho Song Tử |
| **Ứng dụng có quy mô toàn cầu, độ trễ thấp** | GCP | Mạng lưới toàn cầu của Google là một lợi thế thực sự |
| **Khối lượng công việc nặng về tuân thủ/chính phủ** | AWS hoặc Azure | Hầu hết các chứng nhận tuân thủ; Khu vực GovCloud |
| **Khởi nghiệp nhạy cảm với chi phí** | GCP hoặc AWS | Cấp miễn phí của GCP rất hào phóng; AWS có tín dụng khởi nghiệp |
| **Ngăn xếp Microsoft / .NET hiện có** | Azure | Tích hợp chặt chẽ với Visual Studio, .NET, Office 365 |
| **Chiến lược đa đám mây** | Terraform + cả ba | Sử dụng Terraform để quản lý tài nguyên trên các đám mây |
---

## Bản tóm tắt
Cả ba đám mây đều có khả năng, đáng tin cậy và không ngừng mở rộng. Sự lựa chọn thường phụ thuộc vào: nhóm của bạn đã biết gì, hợp đồng hiện tại của bạn trông như thế nào và dịch vụ cụ thể nào quan trọng đối với khối lượng công việc của bạn. Nhiều đám mây ngày càng phổ biến — hãy sử dụng Terraform hoặc Pulumi để tránh sự ràng buộc của nhà cung cấp ở lớp cơ sở hạ tầng và chọn từng đám mây để hoạt động tốt nhất.