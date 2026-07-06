# Kiến trúc đám mây

## Nguyên tắc cơ bản về điện toán đám mây

### Điện toán đám mây là gì?
Cung cấp tài nguyên máy tính theo yêu cầu (máy chủ, bộ lưu trữ, cơ sở dữ liệu, mạng, phần mềm) qua internet với mức giá thanh toán theo mức sử dụng.

### Đặc điểm cơ bản (Định nghĩa của NIST)
- **Tự phục vụ theo yêu cầu**: Cung cấp tài nguyên mà không cần sự tương tác của con người
- **Truy cập mạng rộng**: Có sẵn qua mạng thông qua các cơ chế tiêu chuẩn
- **Tổng hợp tài nguyên**: Mô hình nhiều người thuê với sự phân công động
- **Độ co giãn nhanh**: Mở rộng ra ngoài và vào trong nhanh chóng
- **Dịch vụ được đo lường**: Việc sử dụng tài nguyên được theo dõi và lập hóa đơn

### Mô hình triển khai trên đám mây
- **Đám mây công cộng**: Thuộc sở hữu của nhà cung cấp, cơ sở hạ tầng dùng chung (AWS, Azure, GCP)
- **Đám mây riêng**: Dành riêng cho một tổ chức (tại chỗ hoặc được lưu trữ trên máy chủ)
- **Đám mây lai**: Kết hợp giữa đám mây công cộng và đám mây riêng
- **Đa đám mây**: Sử dụng nhiều nhà cung cấp đám mây công cộng
- **Community Cloud**: Được chia sẻ bởi các tổ chức có chung mối quan tâm

###Mô hình dịch vụ

#### Cơ sở hạ tầng dưới dạng dịch vụ (IaaS)
- **Cung cấp**: Máy ảo, lưu trữ, mạng, hệ điều hành
- **Ví dụ**: AWS EC2, Google Computer Engine, máy ảo Azure
- **Trường hợp sử dụng**: Di chuyển theo kiểu nâng và chuyển đổi, môi trường phát triển, nhu cầu kiểm soát cao

#### Nền tảng dưới dạng dịch vụ (PaaS)
- **Cung cấp**: Nền tảng phát triển, cơ sở dữ liệu, phần mềm trung gian
- **Ví dụ**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Trường hợp sử dụng**: Phát triển ứng dụng, triển khai API, vi dịch vụ

#### Phần mềm dưới dạng dịch vụ (SaaS)
- **Cung cấp**: Hoàn thiện hồ sơ qua internet
- **Ví dụ**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Trường hợp sử dụng**: Email, CRM, ứng dụng cộng tác, kinh doanh

#### Chức năng như một dịch vụ (FaaS) / Serverless
- **Cung cấp**: Thực thi hàm theo sự kiện
- **Ví dụ**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Trường hợp sử dụng**: Xử lý sự kiện, API, tác vụ theo lịch trình, xử lý theo thời gian thực

## Nhà cung cấp đám mây lớn

### Dịch vụ web của Amazon (AWS)
- **Thị phần**: ~32% (nhà cung cấp lớn nhất)
- **Dịch vụ chính**:
  - Tính toán: EC2, Lambda, ECS, EKS
  - Lưu trữ: S3, EBS, Glacier
  - Cơ sở dữ liệu: RDS, DynamoDB, Aurora
  - Kết nối mạng: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Nhận diện, Hiểu rõ

### Microsoft Azure
- **Thị phần**: ~23%
- **Điểm mạnh**: Tích hợp doanh nghiệp, đám mây lai, hệ sinh thái Microsoft
- **Dịch vụ chính**:
  - Tính toán: Máy ảo, Hàm Azure, AKS
  - Lưu trữ: Lưu trữ Blob, Lưu trữ đĩa
  - Cơ sở dữ liệu: Cơ sở dữ liệu SQL, Cosmos DB
  - Kết nối mạng: Mạng ảo, Quản lý lưu lượng
  - AI/ML: Azure ML, Dịch vụ nhận thức

### Nền tảng đám mây của Google (GCP)
- **Thị phần**: ~10%
- **Điểm mạnh**: Phân tích dữ liệu, AI/ML, Kubernetes
- **Dịch vụ chính**:
  - Tính toán: Công cụ tính toán, Chức năng đám mây, GKE
  - Lưu trữ: Lưu trữ đám mây, Đĩa liên tục
  - Cơ sở dữ liệu: Cloud SQL, Firestore, Bigtable
  - Phân tích: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Nhà cung cấp khác
- **IBM Cloud**: Trọng tâm doanh nghiệp, Watson AI
- **Oracle Cloud**: Khối lượng công việc cơ sở dữ liệu, ứng dụng doanh nghiệp
- **Đám mây Alibaba**: Thống trị ở Châu Á - Thái Bình Dương
- **DigitalOcean**: Các dịch vụ đơn giản, thân thiện với nhà phát triển

## Các mẫu kiến trúc đám mây

### Nguyên tắc khung kiến trúc tốt

#### Hoạt động xuất sắc
- Tự động hóa các hoạt động
- Thực hiện những thay đổi thường xuyên, có thể đảo ngược
- Tinh chỉnh thủ tục liên tục
- Dự đoán sự thất bại

#### Bảo mật
- Triển khai nền tảng nhận diện mạnh mẽ
- Cho phép truy xuất nguồn gốc
- Áp dụng bảo mật ở tất cả các lớp
- Tự động thực hành bảo mật tốt nhất
- Bảo vệ dữ liệu trong quá trình vận chuyển và khi nghỉ ngơi

#### Độ tin cậy
- Quy trình phục hồi thử nghiệm
- Tự động phục hồi sau thất bại
- Quy mô theo chiều ngang cho sẵn có
- Dừng khả năng đoán
- Quản lý sự thay đổi trong tự động hóa

#### Hiệu quả hoạt động
- Dân chủ hóa công nghệ tiên tiến
- Đi toàn cầu trong vài phút
- Sử dụng kiến trúc serverless
- Thử nghiệm thường xuyên hơn
- Xem xét sự đồng cảm máy móc

#### Tối ưu hóa chi phí
- Áp dụng mô hình tiêu dùng
- Đo lường hiệu quả tổng thể
- Đừng tiêu tiền vào những công việc không có tính phân biệt
- Phân tích và phân bổ chi tiêu
- Sử dụng các dịch vụ được quản lý

### Các mẫu kiến trúc phổ biến

#### Kiến trúc microservice
- Phân tách các ứng dụng thành các dịch vụ nhỏ, độc lập
- Mỗi dịch vụ sở hữu dữ liệu và logic của nó
- Giao tiếp qua API (REST, gRPC, nhắn tin)
- Triển khai độc lập
- **Lợi ích**: Khả năng mở rộng, cách ly lỗi, đa dạng công nghệ
- **Thách thức**: Độ phức tạp phân tán, tính nhất quán của dữ liệu, giám sát

#### Kiến trúc hướng sự kiện
- Các thành phần giao tiếp thông qua các sự kiện
- Nhà sản xuất phát ra sự kiện, người tiêu dùng phản ứng
- **Mẫu**: Tìm nguồn cung ứng sự kiện, CQRS, pub/sub
- **Công nghệ**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Lợi ích**: Khớp nối lỏng lẻo, khả năng mở rộng, xử lý thời gian thực#### Kiến trúc không máy chủ
- Không cần quản lý máy chủ
- Trả tiền cho mỗi lần thực hiện
- Tự động chia tỷ lệ
- **Thành phần**: Chức năng, Cổng API, dịch vụ được quản lý
- **Lợi ích**: Hiệu quả chi phí, giảm hoạt động, triển khai nhanh chóng
- **Cân nhắc**: Khởi động nguội, khóa nhà cung cấp, giới hạn thực thi

#### Kiến trúc phân lớp (N-Tier)
- Lớp trình bày (UI)
- Lớp logic ứng dụng/kinh doanh
- Lớp truy cập dữ liệu
- Lớp cơ sở dữ liệu
- **Lợi ích**: Tách biệt các mối quan tâm, khả năng bảo trì
- **Thông thường**: Ứng dụng web 3 tầng

#### Kiến trúc dựa trên không gian
- Xử lý đồng thời cao với dữ liệu phân tán
- Bộ nhớ ảo hóa trên các máy chủ
- Xử lý các nút có quy mô độc lập
- **Trường hợp sử dụng**: Ứng dụng có khối lượng lớn, độ trễ thấp

## Dịch vụ điện toán

### Máy ảo
- **Các loại**: Mục đích chung, tối ưu hóa điện toán, tối ưu hóa bộ nhớ, GPU
- **Giá**: Phiên bản theo yêu cầu, phiên bản dự trữ, phiên bản giao ngay
- **Quản lý**: Nhóm tự động mở rộng quy mô, bộ cân bằng tải
- **Các phương pháp hay nhất**: Định cỡ phù hợp, gắn thẻ, giám sát, vá lỗi

### Thùng chứa
- **Docker**: Tiêu chuẩn thời gian chạy của vùng chứa
- **Dàn nhạc**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Lợi ích**: Tính di động, hiệu quả, tính nhất quán
- **Đăng ký**: ECR, GCR, ACR, Docker Hub

### Chức năng không có máy chủ
- **Mô hình thực thi**: Kích hoạt sự kiện, không trạng thái
- **Giới hạn**: Thời gian thực thi, bộ nhớ, thực thi đồng thời
- **Trường hợp sử dụng**: API, xử lý tệp, công việc đã lên lịch, chương trình phụ trợ IoT
- **Giám sát**: Số lần gọi, lỗi, thời lượng, khởi động nguội

## Giải pháp lưu trữ

### Lưu trữ đối tượng
- **Đặc điểm**: Cấu trúc phẳng, siêu dữ liệu, truy cập HTTP
- **Ví dụ**: AWS S3, Google Cloud Storage, Azure Blob
- **Trường hợp sử dụng**: Nội dung tĩnh, bản sao lưu, hồ dữ liệu, kho lưu trữ
- **Các lớp lưu trữ**: Nóng, mát, lạnh, lưu trữ (chi phí/quyền truy cập khác nhau)

### Khối lưu trữ
- **Đặc điểm**: Khối lượng thô, được đính kèm với VM
- **Ví dụ**: AWS EBS, Google Persistent Disk, Azure Disks
- **Trường hợp sử dụng**: Cơ sở dữ liệu, khối lượng khởi động, nhu cầu hiệu năng cao
- **Các loại**: SSD, HDD, IOPS được cung cấp

### Lưu trữ tệp
- **Đặc điểm**: Hệ thống tệp dùng chung, giao thức NFS/SMB
- **Ví dụ**: AWS EFS, Google Filestore, Azure Files
- **Trường hợp sử dụng**: Quản lý nội dung, cấu hình dùng chung, nâng và chuyển

### Lưu trữ lưu trữ
- **Đặc điểm**: Chi phí thấp nhất, độ trễ truy xuất
- **Ví dụ**: S3 Glacier, Bộ lưu trữ lưu trữ Azure
- **Trường hợp sử dụng**: Tuân thủ, sao lưu dài hạn, dữ liệu lịch sử

## Dịch vụ cơ sở dữ liệu

### Cơ sở dữ liệu quan hệ được quản lý
- **Dịch vụ**: AWS RDS/Aurora, Google Cloud SQL, Cơ sở dữ liệu SQL Azure
- **Tính năng**: Tự động sao lưu, vá lỗi, mở rộng quy mô, sao chép
- **Công cụ**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Cơ sở dữ liệu NoSQL
- **Tài liệu**: DocumentDB, Firestore, Cosmos DB
- **Khóa-giá trị**: DynamoDB, Redis Cache
- **Cột rộng**: Bigtable, Cassandra (được quản lý)
- **Đồ thị**: Neptune, Cosmos DB (API đồ thị)

### Kho dữ liệu
- **Dịch vụ**: Snowflake, Redshift, BigQuery, Synapse
- **Đặc điểm**: Lưu trữ dạng cột, kiến trúc MPP
- **Trường hợp sử dụng**: Analytics, BI, phân tích dữ liệu quy mô lớn

### Dịch vụ bộ nhớ đệm
- **Trong bộ nhớ**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Bộ nhớ đệm CDN**: CloudFront, Cloud CDN, Azure CDN
- **Trường hợp sử dụng**: Lưu trữ phiên, bộ nhớ đệm truy vấn, phân phối nội dung

## Kết nối mạng

### Mạng ảo
- **VPC/VNet**: Môi trường mạng biệt lập
- **Mạng con**: Công khai (kết nối internet), riêng tư (chỉ nội bộ)
- **Địa chỉ IP**: Khối CIDR, IPv4/IPv6
- **Bảng lộ trình**: Kiểm soát luồng giao thông

### Cân bằng tải
- **Các loại**: Ứng dụng (L7), Mạng (L4), Cổng
- **Tính năng**: Kiểm tra tình trạng, chấm dứt SSL, phiên dính
- **Dịch vụ**: ELB/ALB/NLB, Cân bằng tải đám mây, Cân bằng tải Azure

### Mạng phân phối nội dung (CDN)
- **Mục đích**: Nội dung được lưu vào bộ nhớ đệm tại các vị trí biên
- **Lợi ích**: Giảm độ trễ, tải gốc thấp hơn, phân phối toàn cầu
- **Dịch vụ**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Dịch vụ DNS
- **Chức năng**: Đăng ký tên miền, định tuyến, kiểm tra tình trạng
- **Dịch vụ**: Route 53, Cloud DNS, Azure DNS
- **Chính sách định tuyến**: Đơn giản, có trọng số, dựa trên độ trễ, định vị địa lý, chuyển đổi dự phòng

### Tùy chọn kết nối
- **Cổng Internet**: Truy cập internet công cộng
- **Cổng NAT**: Truy cập ra bên ngoài mạng con riêng
- **VPN**: Đường hầm được mã hóa tới cơ sở
- **Direct Connect/ExpressRoute**: Kết nối riêng tư chuyên dụng
- **VPC Peering**: Kết nối các VPC trong/giữa các tài khoản

## Bảo mật trên đám mây

### Mô hình chia sẻ trách nhiệm
- **Trách nhiệm của nhà cung cấp**: Bảo mật của đám mây (cơ sở hạ tầng)
- **Trách nhiệm của khách hàng**: Bảo mật TRÊN đám mây (dữ liệu, ứng dụng, quyền truy cập)
- **Thay đổi theo dịch vụ**: Được quản lý nhiều hơn = trách nhiệm của nhà cung cấp nhiều hơn

### Quản lý danh tính và quyền truy cập (IAM)
- **Người dùng**: Danh tính cá nhân
- **Nhóm**: Tập hợp người dùng
- **Vai trò**: Thông tin xác thực tạm thời cho dịch vụ/người dùng
- **Chính sách**: Tài liệu JSON xác định quyền
- **Nguyên tắc**: Đặc quyền tối thiểu, phân chia nhiệm vụ### An ninh mạng
- **Nhóm bảo mật**: Tường lửa trạng thái cho các phiên bản
- **Network ACL**: Tường lửa không trạng thái cho mạng con
- **Tường lửa ứng dụng web (WAF)**: Bảo vệ khỏi việc khai thác web
- **Bảo vệ DDoS**: Khiên, Áo giáp đám mây, Bảo vệ DDoS

### Bảo vệ dữ liệu
- **Mã hóa ở trạng thái lưu trữ**: KMS, khóa do khách hàng quản lý
- **Mã hóa khi chuyển tuyến**: TLS/SSL, HTTPS
- **Quản lý khóa**: HSM, xoay vòng khóa, theo dõi kiểm tra
- **Quản lý bí mật**: Trình quản lý bí mật, Key Vault

### Tuân thủ và Quản trị
- **Chứng nhận**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Công cụ**: Thực thi chính sách, báo cáo tuân thủ, nhật ký kiểm tra
- **Khung**: Liên minh bảo mật đám mây, NIST CSF

## DevOps trên đám mây

### Dịch vụ CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Hành động Azure DevOps, GitHub
- **GCP**: Xây dựng đám mây, Triển khai đám mây
- **Bên thứ ba**: Jenkins, CircleCI, GitLab CI

### Cơ sở hạ tầng dưới dạng mã (IaC)
- **Terraform**: Quản lý trạng thái, khai báo, đa đám mây
- **CloudFormation**: mẫu gốc AWS, mẫu YAML/JSON
- **Mẫu ARM**: Azure gốc
- **Trình quản lý triển khai**: GCP gốc
- **Pulumi**: Cơ sở hạ tầng sử dụng ngôn ngữ lập trình
- **Lợi ích**: Kiểm soát phiên bản, độ lặp lại, tài liệu

###Quản lý cấu hình
- **Ansible**: Sách hướng dẫn về Agentless, YAML
- **Chef**: Hệ sinh thái trưởng thành, dựa trên Ruby
- **Con rối**: Mang tính tuyên bố, báo cáo mạnh mẽ
- **SaltStack**: Nhanh, dựa trên Python

### Giám sát và quan sát
- **Số liệu**: CloudWatch, Giám sát đám mây, Azure Monitor
- **Ghi nhật ký**: Nhật ký CloudWatch, Nhật ký đám mây, Phân tích nhật ký
- **Theo dõi**: X-Ray, Cloud Trace, Thông tin chi tiết về ứng dụng
- **Trang tổng quan**: Bảng thông tin CloudWatch, Bảng điều khiển đám mây
- **Cảnh báo**: SNS, Cảnh báo giám sát đám mây, Nhóm hành động

### Điều phối vùng chứa
- **Kubernetes**: Điều phối tiêu chuẩn ngành
- **Dịch vụ được quản lý**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (quản lý lưu lượng, bảo mật)
- **GitOps**: ArgoCD, Flux (triển khai khai báo)

##Quản lý chi phí

### Mô hình định giá
- **Trả tiền theo nhu cầu**: Trả tiền cho những gì bạn sử dụng
- **Phiên bản dự trữ**: Cam kết 1-3 năm, chiết khấu đáng kể
- **Phiên bản Spot**: Đấu thầu cho dung lượng chưa sử dụng, có thể bị gián đoạn
- **Gói tiết kiệm**: Giá cam kết linh hoạt
- **Cấp miễn phí**: Mức sử dụng miễn phí có giới hạn cho tài khoản mới

### Chiến lược tối ưu hóa chi phí
- **Định cỡ phù hợp**: Khớp loại phiên bản với nhu cầu khối lượng công việc
- **Tự động chia tỷ lệ**: Chia tỷ lệ theo nhu cầu
- **Công suất dự trữ**: Cam kết khối lượng công việc ở trạng thái ổn định
- **Sử dụng tại chỗ**: Sử dụng cho khối lượng công việc linh hoạt, có khả năng chịu lỗi
- **Cấp lưu trữ**: Di chuyển dữ liệu không thường xuyên sang cấp rẻ hơn
- **Dọn dẹp**: Xóa các tài nguyên, ảnh chụp nhanh, AMI không sử dụng

### Công cụ quản lý chi phí
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Quản lý chi phí, Cố vấn
- **GCP**: Báo cáo thanh toán, Người giới thiệu
- **Bên thứ ba**: CloudHealth, CloudCheckr, Datadog

## Tính sẵn sàng cao và khắc phục thảm họa

### Khái niệm về tính sẵn có
- **Vùng sẵn sàng**: Các trung tâm dữ liệu tách biệt về mặt vật lý trong khu vực
- **Khu vực**: Khu vực địa lý có nhiều AZ
- **Vị trí biên**: Vị trí bộ đệm CDN trên toàn cầu

### Chiến lược HA
- **Multi-AZ**: Triển khai trên các vùng sẵn sàng
- **Tự động sửa chữa**: Tự động thay thế các trường hợp bị lỗi
- **Cân bằng tải**: Phân phối lưu lượng truy cập trên các phiên bản lành mạnh
- **Sao chép cơ sở dữ liệu**: Triển khai Multi-AZ, đọc bản sao

### Chiến lược khắc phục thảm họa
- **Backup and Restore**: Backup định kỳ, khôi phục khi cần (chi phí thấp nhất)
- **Đèn thí điểm**: Các yếu tố cốt lõi đang chạy, mở rộng quy mô trong thảm họa
- **Chế độ chờ ấm**: Phiên bản thu nhỏ luôn chạy
- **Đang hoạt động/Đang hoạt động nhiều địa điểm**: Sản xuất đầy đủ ở nhiều vùng (chi phí cao nhất)

### RTO và RPO
- **Mục tiêu về thời gian phục hồi (RTO)**: Thời gian ngừng hoạt động tối đa có thể chấp nhận được
- **Mục tiêu điểm khôi phục (RPO)**: Mất dữ liệu tối đa có thể chấp nhận được
- **Lựa chọn chiến lược**: Dựa trên yêu cầu kinh doanh và ngân sách

## Xu hướng mới nổi

### Điện toán biên
- Xử lý dữ liệu gần nguồn hơn
- **Dịch vụ**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Trường hợp sử dụng**: IoT, phân tích thời gian thực, ứng dụng có độ trễ thấp

### Đám mây đa đám mây và đám mây lai
- Tránh bị khóa nhà cung cấp
- Tận dụng các dịch vụ tốt nhất
- **Công cụ**: Terraform, Anthos, Arc, CloudHealth

### Dịch vụ AI/ML
- Các mô hình được đào tạo trước: Thị giác, lời nói, ngôn ngữ
- Đào tạo mô hình tùy chỉnh: SageMaker, Vertex AI, Azure ML
- MLOps: Triển khai mô hình, giám sát, quản trị

### Điện toán lượng tử
- **Dịch vụ**: AWS Braket, Azure Quantum
- **Trạng thái**: Giai đoạn đầu, thử nghiệm
- **Tiềm năng**: Mật mã, tối ưu hóa, khám phá thuốc

### Đám mây bền vững
- Theo dõi lượng khí thải carbon
- Cam kết năng lượng tái tạo
- Sử dụng tài nguyên hiệu quả
- Mẫu kiến trúc xanh