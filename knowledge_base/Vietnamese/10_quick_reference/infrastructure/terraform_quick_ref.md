<!--
---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
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
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Địa hình và cơ sở hạ tầng dưới dạng mã
Terraform là công cụ Cơ sở hạ tầng dưới dạng Mã (IaC) được sử dụng rộng rãi nhất — nó cho phép bạn xác định cơ sở hạ tầng đám mây (máy chủ, cơ sở dữ liệu, mạng, quyền) trong các tệp cấu hình khai báo có thể được phiên bản, xem xét, kiểm tra và tự động hóa. Thay vì nhấp qua bảng điều khiển đám mây, bạn viết mã mô tả trạng thái mong muốn của cơ sở hạ tầng và Terraform tìm ra những thay đổi cần thực hiện.
---

## Khái niệm cốt lõi
| Khái niệm | Mô tả |
|----------|-------------|
| **Nhà cung cấp** | Plugin quản lý nền tảng đám mây cụ thể (AWS, Azure, GCP, v.v.) |
| **Tài nguyên** | Đối tượng cơ sở hạ tầng (máy chủ, cơ sở dữ liệu, mạng) |
| **Tiểu bang** | Hồ sơ của Terraform về những cơ sở hạ tầng tồn tại; được lưu trữ trong một tập tin trạng thái |
| **Kế hoạch** | Xem trước những thay đổi mà Terraform sẽ thực hiện |
| **Áp dụng** | Thực hiện kế hoạch; tạo/cập nhật/hủy cơ sở hạ tầng |
| **Mô-đun** | Bộ sưu tập tài nguyên có thể tái sử dụng |
| **Biến** | Tham số đầu vào cho cấu hình |
| **Đầu ra** | Giá trị được xuất từ ​​mô-đun hoặc cấu hình |
| **Nguồn dữ liệu** | Đọc thông tin từ cơ sở hạ tầng hiện có |
---

## Quy trình làm việc cơ bản
| Bước | Lệnh | Mô tả |
|------|----------|-------------|
| **1. Viết cấu hình** | Tạo tập tin`.tf`| Xác định nhà cung cấp, tài nguyên, biến |
| **2. Khởi tạo** | `terraform init`| Tải xuống nhà cung cấp; thiết lập phụ trợ |
| **3. Định dạng** | `terraform fmt`| Chuẩn hóa định dạng |
| **4. Xác thực** | `terraform validate`| Kiểm tra cú pháp và cấu hình |
| **5. Kế hoạch** | `terraform plan`| Xem trước các thay đổi (chạy thử) |
| **6. Nộp đơn** | `terraform apply`| Tạo hoặc cập nhật cơ sở hạ tầng |
| **7. Tiêu diệt** | `terraform destroy`| Phá bỏ tất cả cơ sở hạ tầng được quản lý |
---

## Các lệnh chung
| Lệnh | Mô tả |
|----------|-------------|
| `terraform init`| Khởi tạo thư mục làm việc; tải xuống nhà cung cấp và mô-đun |
| `terraform plan`| Hiển thị những thay đổi sẽ được thực hiện |
| `terraform apply`| Áp dụng các thay đổi; thêm`-auto-approve`để bỏ qua xác nhận |
| `terraform destroy`| Phá hủy tất cả các tài nguyên được quản lý |
| `terraform fmt`| Định dạng tập tin cấu hình theo kiểu chuẩn |
| `terraform validate`| Xác thực cú pháp cấu hình |
| `terraform output`| Hiển thị giá trị đầu ra |
| `terraform state list`| Liệt kê tất cả các nguồn lực trong bang |
| `terraform state show <resource>`| Hiển thị chi tiết về một nguồn tài nguyên cụ thể |
| `terraform import <resource> <id>`| Nhập cơ sở hạ tầng hiện có vào trạng thái |
| `terraform taint <resource>`| Đánh dấu một nguồn tài nguyên để giải trí vào lần đăng ký tiếp theo |
| `terraform refresh`| Cập nhật trạng thái để phù hợp với cơ sở hạ tầng thực |
| `terraform graph`| Tạo biểu đồ phụ thuộc trực quan (định dạng DOT) |
| `terraform console`| Bảng điều khiển tương tác để kiểm tra biểu thức |
---

##Quản lý nhà nước
| Thực hành tốt nhất | Mô tả |
|--------------|-------------|
| **Trạng thái từ xa** | Lưu trữ trạng thái trong S3, GCS, Azure Blob hoặc Terraform Cloud — không bao giờ cục bộ |
| **Khóa trạng thái** | Sử dụng DynamoDB (phụ trợ S3) hoặc khóa gốc để ngăn sửa đổi đồng thời |
| **Mã hóa trạng thái** | Kích hoạt tính năng mã hóa ở trạng thái lưu trữ cho các tệp trạng thái (chúng chứa dữ liệu nhạy cảm) |
| **Tách nhà nước** | Sử dụng các tệp trạng thái riêng biệt cho các môi trường hoặc nhóm khác nhau |
| **Sao lưu trạng thái** | Trạng thái phiên bản tự động phụ trợ từ xa; giữ tính năng này được kích hoạt |
| **Không bao giờ chỉnh sửa trạng thái theo cách thủ công** | Thay vào đó hãy sử dụng`terraform state mv`,`rm`,`import`|
---

## Cấu trúc mô-đun
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Các loại biến
| Loại | Ví dụ | Trường hợp sử dụng |
|------|----------|----------|
| **chuỗi** | `variable "region" { type = string }`| Giá trị văn bản đơn |
| **số** | `variable "count" { type = number }`| Giá trị số |
| **bool** | `variable "enable" { type = bool }`| Cờ đúng/sai |
| **danh sách** | `variable "zones" { type = list(string) }`| Bộ sưu tập đặt hàng |
| **bản đồ** | `variable "tags" { type = map(string) }`| Cặp khóa-giá trị |
| **đối tượng** | `variable "config" { type = object({...}) }`| Cấu hình có cấu trúc |
---

## Các mẫu phổ biến
| Mẫu | Mô tả |
|----------|-------------|
| **Đếm** | `count = 3`tạo nhiều phiên bản của một tài nguyên |
| **Đối với mỗi** | `for_each = var.items`lặp lại trên bản đồ hoặc tập hợp |
| **Khối động** | Tạo các khối lồng nhau lặp đi lặp lại (ví dụ: quy tắc xâm nhập) |
| **Giá trị cục bộ** | `locals { ... }`cho các giá trị được tính toán và giảm sự lặp lại |
| **Nguồn dữ liệu** | Đọc cơ sở hạ tầng hiện có (ví dụ: tìm VPC hiện có) |
| **Nhà cung cấp** | Chạy tập lệnh trên tài nguyên sau khi tạo (sử dụng tiết kiệm) |
| **Không gian làm việc** | Trạng thái riêng biệt cho các môi trường khác nhau trong cùng một cấu hình |
---

## Khắc phục sự cố
| Vấn đề | Giải pháp |
|----------|----------|
| **Trôi trôi trạng thái** | Chạy`terraform plan`để thấy sự khác biệt; `terraform apply`để hòa giải |
| **Trạng thái bị khóa** | Kiểm tra xem ai có khóa; sử dụng`terraform force-unlock`nếu an toàn |
| **Lỗi của nhà cung cấp** | Kiểm tra thông tin xác thực; cập nhật phiên bản nhà cung cấp; kiểm tra giới hạn API |
| **Xung đột nhập khẩu** | Tài nguyên đã ở trạng thái; sử dụng`terraform state rm`trước |
| **Phụ thuộc vòng tròn** | Tái cơ cấu nguồn lực; sử dụng`depends_on`cẩn thận |
| **Trạng thái lớn** | Chia thành các mô-đun; sử dụng`-target`cho các hoạt động một phần |
---

## Bản tóm tắt
Terraform quản lý cơ sở hạ tầng thông qua các tệp cấu hình khai báo. Quy trình làm việc là: viết cấu hình → init → plan → áp dụng. Trạng thái theo dõi những gì tồn tại và phải được lưu trữ từ xa bằng khóa. Các mô-đun cho phép tái sử dụng. Các biến tham số hóa cấu hình. Các nguyên tắc chính là: coi cơ sở hạ tầng như mã (kiểm soát phiên bản; đánh giá; kiểm tra); không bao giờ chỉnh sửa trạng thái theo cách thủ công; lập kế hoạch trước khi áp dụng; sử dụng trạng thái từ xa có khóa; và cấu hình cấu trúc với các mô-đun để bảo trì.