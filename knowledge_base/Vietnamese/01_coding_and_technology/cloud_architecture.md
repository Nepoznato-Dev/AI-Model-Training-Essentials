<!--
---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
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
tags: [cloud, architecture, coding-and-technology]
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
# Kiến trúc đám mây
Điện toán đám mây đã thay đổi căn bản cách các tổ chức xây dựng, triển khai và mở rộng quy mô phần mềm. Thay vì mua và bảo trì máy chủ vật lý, bạn có thể cung cấp tài nguyên máy tính theo yêu cầu, thanh toán cho những gì bạn sử dụng và mở rộng quy mô trên toàn cầu chỉ trong vài phút. Tệp này bao gồm các khái niệm cốt lõi, mẫu kiến ​​trúc, dịch vụ và các phương pháp hay nhất mà bạn cần biết.
---

## Nguyên tắc cơ bản về điện toán đám mây
### Điện toán đám mây là gì?
Cung cấp tài nguyên máy tính theo yêu cầu — máy chủ, bộ lưu trữ, cơ sở dữ liệu, mạng, phần mềm — qua internet với mức giá thanh toán theo mức sử dụng.
### Đặc điểm cơ bản của NIST
| Đặc trưng | Ý nghĩa |
|--------------|----------|
| **Tự phục vụ theo yêu cầu** | Cung cấp tài nguyên mà không cần sự tương tác của con người |
| **Truy cập mạng rộng** | Có sẵn trên mạng thông qua các cơ chế tiêu chuẩn |
| **Tổng hợp tài nguyên** | Mô hình nhiều người thuê; tài nguyên được gán động |
| **Đàn hồi nhanh** | Mở rộng quy mô ra ngoài và vào trong một cách nhanh chóng |
| **Dịch vụ được đo lường** | Việc sử dụng được theo dõi và lập hoá đơn |
### Mô hình triển khai
| Người mẫu | Mô tả | Khi nào nên sử dụng |
|-------|-------------|-------------|
| **Đám mây công cộng** | Thuộc sở hữu của nhà cung cấp; cơ sở hạ tầng dùng chung (AWS, Azure, GCP) | Khối lượng công việc lớn nhất; tiết kiệm chi phí |
| **Đám mây riêng** | Dành riêng cho một tổ chức | Yêu cầu pháp lý, dữ liệu nhạy cảm |
| **Đám mây lai** | Sự kết hợp giữa công và tư | Tính linh hoạt + tuân thủ |
| **Đa đám mây** | Sử dụng nhiều nhà cung cấp đám mây công cộng | Tránh bị khóa nhà cung cấp, loại tốt nhất |
###Mô hình dịch vụ
| Người mẫu | Cung cấp | Ví dụ | Trường hợp sử dụng |
|-------|----------|----------|----------|
| **IaaS** | VM, lưu trữ, mạng, HĐH | AWS EC2, máy ảo Azure, Công cụ tính toán GCP | Di chuyển thang máy, kiểm soát hoàn toàn |
| **PaaS** | Nền tảng phát triển, cơ sở dữ liệu, phần mềm trung gian | Heroku, Google App Engine, Cây đậu đàn hồi AWS | Phát triển ứng dụng, triển khai API |
| **SaaS** | Hoàn thành các ứng dụng qua internet | Lực lượng bán hàng, Google Workspace, Microsoft 365 | Email, CRM, cộng tác |
| **FaaS / Không có máy chủ** | Thực thi hàm hướng sự kiện | AWS Lambda, Chức năng Azure, Chức năng đám mây GCP | API, xử lý sự kiện, tác vụ theo lịch trình |
---

## Nhà cung cấp đám mây lớn
| Nhà cung cấp | Thị phần | Điểm mạnh |
|----------|-------------|----------|
| **AWS** | ~32% | Danh mục dịch vụ rộng nhất, hệ sinh thái lớn nhất |
| **Azure** | ~23% | Tích hợp doanh nghiệp, đám mây lai, Microsoft stack |
| **GCP** | ~10% | Phân tích dữ liệu, AI/ML, Kubernetes |
| **Đám mây Alibaba** | ~4% | Thống trị ở Châu Á - Thái Bình Dương |
| **Đám mây Oracle** | ~2% | Khối lượng công việc cơ sở dữ liệu, ứng dụng doanh nghiệp |
| **Đám mây IBM** | ~2% | Tập trung vào doanh nghiệp, Watson AI |
| **Đại dương kỹ thuật số** | Ngách | Các dịch vụ đơn giản, thân thiện với nhà phát triển |
### So sánh dịch vụ (Top 3 nhà cung cấp)
| Danh mục | AWS | Azure | GCP |
|----------|------|-------|------|
| **Tính** | EC2, Lambda, ECS | VM, Chức năng, AKS | Công cụ tính toán, Chức năng đám mây, GKE |
| **Lưu trữ** | S3, EBS, Sông băng | Lưu trữ Blob, Lưu trữ đĩa | Lưu trữ đám mây, Đĩa liên tục |
| **Cơ sở dữ liệu** | RDS, DynamoDB, Aurora | Cơ sở dữ liệu SQL, Cosmos DB | Đám mây SQL, Firestore, Bigtable |
| **Phân tích** | Dịch chuyển đỏ, EMR | Synapse, Databricks | BigQuery, Luồng dữ liệu |
| **AI/ML** | SageMaker, Nhận thức | Azure ML, Dịch vụ nhận thức | Vertex AI, AutoML |
| **Kết nối mạng** | VPC, Tuyến 53, CloudFront | VNet, Quản lý giao thông | VPC, DNS đám mây, CDN đám mây |
---

## Mẫu kiến ​​trúc
### Khung được kiến ​​trúc tốt
Tất cả ba nhà cung cấp chính đều xuất bản các khuôn khổ có kiến ​​trúc tốt được xây dựng dựa trên năm trụ cột:
| Trụ cột | Nguyên tắc chính |
|--------|--------------|
| **Hoạt động xuất sắc** | Tự động hóa hoạt động; thực hiện những thay đổi thường xuyên, có thể đảo ngược; lường trước thất bại |
| **An ninh** | Nền tảng bản sắc vững chắc; áp dụng bảo mật ở mọi lớp; bảo vệ dữ liệu đang di chuyển và ở trạng thái nghỉ ngơi |
| **Độ tin cậy** | Thủ tục phục hồi thử nghiệm; tự động phục hồi sau thất bại; quy mô theo chiều ngang |
| **Hiệu quả hoạt động** | Sử dụng không có máy chủ; đi toàn cầu trong vài phút; thử nghiệm thường xuyên |
| **Tối ưu hóa chi phí** | Áp dụng mô hình tiêu dùng; sử dụng các dịch vụ được quản lý; ngừng chi tiêu vào công việc không phân biệt |
### Các mẫu phổ biến
| Mẫu | Mô tả | Lợi ích | Thử thách |
|----------|-------------|----------|----------||
| **Dịch vụ vi mô** | Phân tách ứng dụng thành các dịch vụ nhỏ, độc lập | Khả năng mở rộng, cách ly lỗi, triển khai độc lập | Độ phức tạp phân tán, tính nhất quán của dữ liệu |
| **Theo hướng sự kiện** | Các thành phần giao tiếp thông qua các sự kiện | Khớp nối lỏng lẻo, xử lý thời gian thực | Gỡ lỗi phức tạp, tính nhất quán cuối cùng |
| **Không có máy chủ** | Không quản lý máy chủ; trả tiền cho mỗi lần thực hiện | Hiệu quả chi phí, triển khai nhanh chóng | Khởi động nguội, khóa nhà cung cấp, giới hạn thực thi |
| **Lớp (N-Tier)** | Trình bày → Logic nghiệp vụ → Truy cập dữ liệu → Cơ sở dữ liệu | Tách biệt mối quan tâm, khả năng bảo trì | Có thể trở thành nguyên khối |
| **Dựa trên không gian** | Dữ liệu được phân phối trên các nút bộ nhớ ảo hóa | Xử lý đồng thời cao, độ trễ thấp | Phức tạp để thiết kế và quản lý |
---

## Dịch vụ cốt lõi
### Tính toán
| Loại dịch vụ | Chi tiết |
|-------------|----------|
| **Máy ảo** | Mục đích chung, tối ưu hóa tính toán, tối ưu hóa bộ nhớ, GPU. Giá cả: theo yêu cầu, đặt trước, giao ngay. |
| **Hộp chứa** | Thời gian chạy Docker; phối hợp thông qua Kubernetes (EKS, AKS, GKE). Cơ quan đăng ký: ECR, GCR, ACR. |
| **Chức năng phi máy chủ** | Sự kiện kích hoạt, không trạng thái. Giới hạn về thời gian thực hiện, bộ nhớ, đồng thời. |
### Kho
| Loại | Đặc điểm | Ví dụ | Tốt nhất cho |
|------|-------|----------|----------|
| **Đối tượng** | Cấu trúc phẳng, truy cập HTTP, giàu siêu dữ liệu | S3, Lưu trữ đám mây, Azure Blob | Tài sản tĩnh, bản sao lưu, hồ dữ liệu |
| **Chặn** | Khối lượng thô được gắn vào máy ảo | EBS, Đĩa liên tục, Đĩa Azure | Cơ sở dữ liệu, khối lượng khởi động |
| **Tệp** | Hệ thống tệp dùng chung (NFS/SMB) | EFS, Filestore, Tệp Azure | Quản lý nội dung, cấu hình chia sẻ |
| **Lưu trữ** | Chi phí thấp nhất, thời gian truy xuất chậm | S3 Glacier, Lưu trữ Azure | Tuân thủ, sao lưu dài hạn |
### Cơ sở dữ liệu
| Danh mục | Dịch vụ | Trường hợp sử dụng |
|----------|----------|----------|
| **Quan hệ được quản lý** | RDS, Đám mây SQL, Azure SQL | Ứng dụng truyền thống, giao dịch ACID |
| **NoSQL — Tài liệu** | DocumentDB, Firestore, Cosmos DB | Lược đồ linh hoạt, dữ liệu JSON |
| **NoSQL — Khóa-Giá trị** | DynamoDB, Bộ nhớ đệm Redis | Bộ nhớ đệm, phiên, tra cứu đơn giản |
| **NoSQL — Cột rộng** | Bàn lớn, Cassandra | Viết nhiều, chuỗi thời gian |
| **NoSQL — Đồ thị** | Sao Hải Vương, Cosmos DB (API đồ thị) | Các mối quan hệ, mạng xã hội |
| **Kho dữ liệu** | Bông tuyết, Redshift, BigQuery, Synapse | Phân tích, BI |
| **Bộ nhớ đệm** | ElastiCache, Kho lưu trữ đám mây | Lưu trữ phiên, bộ nhớ đệm truy vấn |
---

## Kết nối mạng
### Mạng ảo
Mọi hoạt động triển khai trên đám mây đều nằm trong Đám mây riêng ảo (VPC / VNet) — một mạng biệt lập mà bạn xác định bằng các khối CIDR, mạng con (công khai hoặc riêng tư), bảng định tuyến và cổng.
### Cân bằng tải và CDN
| Dịch vụ | Mục đích |
|----------|----------|
| **Cân bằng tải** | Phân phối lưu lượng trên các phiên bản (mạng L4, ứng dụng L7) |
| **CDN** | Nội dung được lưu vào bộ đệm ở các vị trí biên để có độ trễ thấp hơn (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Đăng ký tên miền, chính sách định tuyến, kiểm tra tình trạng (Tuyến 53, Cloud DNS, Azure DNS) |
### Tùy chọn kết nối
| Tùy chọn | Mô tả |
|--------|-------------|
| **Cổng Internet** | Truy cập internet công cộng cho VPC |
| **Cổng NAT** | Truy cập ra mạng con riêng |
| **VPN** | Đường hầm được mã hóa đến tại chỗ |
| **Kết nối trực tiếp / ExpressRoute** | Kết nối riêng tư chuyên dụng |
| **VPC ngang hàng** | Kết nối các VPC trong hoặc giữa các tài khoản |
---

## Bảo vệ
### Mô hình chia sẻ trách nhiệm
| Lớp | Nhà cung cấp | Khách hàng |
|-------|----------|----------|
| **Cơ sở hạ tầng** (phần cứng, cơ sở vật chất) | ✅ | |
| **Tính toán, lưu trữ, kết nối mạng** | ✅ (được quản lý) | ✅ (tự quản lý) |
| **Dữ liệu, Ứng dụng, Nhận dạng** | | ✅ |
Dịch vụ càng được quản lý nhiều thì nhà cung cấp càng xử lý được nhiều việc hơn. Với IaaS bạn quản lý hầu hết mọi thứ; với SaaS, nhà cung cấp xử lý gần như toàn bộ việc đó.
### Quản lý danh tính và quyền truy cập (IAM)
| Khái niệm | Mô tả |
|----------|-------------|
| **Người dùng** | Danh tính cá nhân |
| **Nhóm** | Bộ sưu tập của người dùng |
| **Vai trò** | Thông tin xác thực tạm thời cho dịch vụ hoặc người dùng |
| **Chính sách** | Tài liệu xác định quyền |
| **Nguyên tắc** | Đặc quyền tối thiểu, phân chia nhiệm vụ |
### Bảo vệ dữ liệu
- **Mã hóa ở trạng thái lưu trữ**: KMS, khóa do khách hàng quản lý, HSM.
- **Mã hóa khi truyền**: TLS/SSL, HTTPS.
- **Quản lý bí mật**: Trình quản lý bí mật, Key Vault — không bao giờ mã hóa bí mật.
---

## DevOps trên đám mây
### Cơ sở hạ tầng dưới dạng mã (IaC)
| Công cụ | Mô tả |
|------|-------------|
| **Địa hình** | Đa đám mây, khai báo HCL, quản lý trạng thái |
| **CloudFormation** | Mẫu gốc AWS, YAML/JSON |
| **Mẫu ARM / Bắp tay** | Azure-bản địa |
| **Pulumi** | Cơ sở hạ tầng sử dụng ngôn ngữ lập trình (Python, Go, v.v.) |
### Dịch vụ CI/CD
| Nhà cung cấp | Công cụ |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azure** | Azure DevOps, Hành động GitHub |
| **GCP** | Xây dựng đám mây, Triển khai đám mây |
| **Bên thứ ba** | Jenkins, CircleCI, GitLab CI |
### Giám sát và quan sát
| Năng lực | AWS | Azure | GCP |
|----------||------|-------|------|
| **Số liệu** | CloudWatch | Màn hình Azure | Giám sát đám mây |
| **Ghi nhật ký** | Nhật ký CloudWatch | Phân tích nhật ký | Ghi nhật ký trên đám mây |
| **Truy tìm** | Tia X | Thông tin chi tiết về ứng dụng | Dấu vết đám mây |
---

##Quản lý chi phí
### Mô hình định giá
| Người mẫu | Mô tả | Tốt nhất cho |
|-------|-------------|----------|
| **Theo yêu cầu** | Trả tiền cho những gì bạn sử dụng, theo giây/giờ | Khối lượng công việc ngắn hạn, có thể thay đổi |
| **Phiên bản dự trữ** | Cam kết 1–3 năm, chiết khấu đáng kể | Khối lượng công việc ở trạng thái ổn định |
| **Phiên bản Spot** | Đấu thầu công suất chưa sử dụng; có thể bị gián đoạn | Công việc linh hoạt, có khả năng chịu lỗi |
| **Kế hoạch tiết kiệm** | Giá cam kết linh hoạt | Mô hình sử dụng hỗn hợp |
| **Cấp miễn phí** | Sử dụng miễn phí có giới hạn cho tài khoản mới | Học tập, tạo mẫu |
### Chiến lược tối ưu hóa
Phiên bản có kích thước phù hợp để phù hợp với khối lượng công việc. Sử dụng tính năng tự động mở rộng quy mô để xử lý nhu cầu tăng đột biến. Dự trữ công suất cho các tải có thể dự đoán được. Sử dụng các phiên bản tại chỗ cho các công việc hàng loạt. Di chuyển dữ liệu được truy cập không thường xuyên sang các tầng lưu trữ rẻ hơn. Xóa các tài nguyên không sử dụng (ảnh chụp nhanh mồ côi, bộ cân bằng tải nhàn rỗi, IP không được đính kèm).
---

## Tính sẵn sàng cao và khắc phục thảm họa
### Khái niệm về tính sẵn có
| Khái niệm | Mô tả |
|----------|-------------|
| **Vùng sẵn có (AZ)** | Các trung tâm dữ liệu riêng biệt về mặt vật lý trong một khu vực |
| **Vùng** | Khu vực địa lý có nhiều AZ |
| **Vị trí cạnh** | Vị trí bộ đệm CDN để phân phối nội dung |
### Chiến lược khắc phục thảm họa
| Chiến lược | Chi phí | RTO | RPO | Mô tả |
|----------|------|-----|------|-------------|
| **Sao lưu và khôi phục** | Thấp nhất | Giờ | Giờ-ngày | Sao lưu định kỳ, khôi phục khi cần |
| **Đèn hoa tiêu** | Thấp | Phút–giờ | Phút | Yếu tố cốt lõi luôn chạy, mở rộng quy mô khi có thảm họa |
| **Chế độ chờ ấm áp** | Trung bình | Phút | Giây–phút | Phiên bản thu nhỏ luôn chạy |
| **Đang hoạt động/Đang hoạt động trên nhiều trang** | Cao nhất | Gần bằng không | Không | Sản xuất đầy đủ ở nhiều vùng |
**RTO** (Mục tiêu về thời gian phục hồi) = thời gian ngừng hoạt động tối đa có thể chấp nhận được. **RPO** (Mục tiêu điểm khôi phục) = mức độ mất dữ liệu tối đa có thể chấp nhận được.
---

## Xu hướng mới nổi
| Xu hướng | Chuyện gì đang xảy ra |
|-------|-------------------|
| **Điện toán biên** | Xử lý dữ liệu gần nguồn hơn (AWS Outposts, Wavelength, Azure Edge) |
| **Đa đám mây** | Tránh bị khóa nhà cung cấp; tận dụng những sản phẩm tốt nhất của các nhà cung cấp |
| **Dịch vụ AI/ML** | Các mô hình được đào tạo trước (tầm nhìn, lời nói, ngôn ngữ) + đào tạo tùy chỉnh (SageMaker, Vertex AI) |
| **Tính toán lượng tử** | Dịch vụ thử nghiệm giai đoạn đầu (AWS Braket, Azure Quantum) |
| **Đám mây bền vững** | Theo dõi lượng khí thải carbon, cam kết năng lượng tái tạo, kiến ​​trúc xanh |