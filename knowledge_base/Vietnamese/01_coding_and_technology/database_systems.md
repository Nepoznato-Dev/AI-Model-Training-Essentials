<!--
---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#Hệ thống cơ sở dữ liệu
## Cơ sở dữ liệu cơ bản
### Cơ sở dữ liệu là gì?
Cơ sở dữ liệu là một tập hợp có tổ chức các thông tin có cấu trúc được lưu trữ điện tử, được thiết kế để truy xuất, chèn, cập nhật và xóa dữ liệu một cách hiệu quả.
### Hệ thống quản lý cơ sở dữ liệu (DBMS)
Phần mềm tương tác với người dùng cuối, ứng dụng và cơ sở dữ liệu để thu thập và phân tích dữ liệu. Ví dụ: MySQL, PostgreSQL, Oracle, MongoDB.
### Các khái niệm chính
- **Lược đồ**: Cấu trúc/tổ chức cơ sở dữ liệu (bảng, trường, mối quan hệ)
- **Instance**: Dữ liệu thực tế được lưu trữ tại một thời điểm cụ thể
- **Thuộc tính axit**: Tính nguyên tử, tính nhất quán, tính cô lập, độ bền
- **Định lý CAP**: Tính nhất quán, Tính sẵn có, Dung sai phân vùng (chọn 2)
- **Chuẩn hóa**: Sắp xếp dữ liệu để giảm sự dư thừa
- **Không chuẩn hóa**: Thêm dự phòng để cải thiện hiệu suất đọc
## Cơ sở dữ liệu quan hệ (SQL)
### Khái niệm cốt lõi
- **Bảng**: Hàng (bản ghi) và cột (trường)
- **Khóa chính**: Mã định danh duy nhất cho mỗi hàng
- **Khóa ngoại**: Tham chiếu đến khóa chính trong bảng khác
- **Chỉ mục**: Cấu trúc dữ liệu cải thiện tốc độ truy vấn
- **Chế độ xem**: Bảng ảo dựa trên kết quả truy vấn
- **Thủ tục lưu trữ**: Các khối mã SQL được biên dịch trước
- **Kích hoạt**: Hành động tự động khi thay đổi dữ liệu
### Hoạt động SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Tham gia
- **INNER JOIN**: Trả về các hàng khớp từ cả hai bảng
- **THAM GIA TRÁI**: Tất cả các hàng từ bảng bên trái, khớp từ bảng bên phải
- **RIGHT THAM GIA**: Tất cả các hàng từ bảng bên phải, khớp từ bên trái
- **THAM GIA NGOÀI ĐẦY ĐỦ**: Tất cả các hàng từ cả hai bảng
- **Tham gia chéo**: Tích Descartes của cả hai bảng
- **SELF JOIN**: Bảng được nối với chính nó
### Biểu mẫu chuẩn hóa
- **1NF**: Giá trị nguyên tử, không có nhóm lặp lại
- **2NF**: 1NF + không phụ thuộc một phần (tất cả các thuộc tính không khóa đều phụ thuộc vào toàn bộ khóa chính)
- **3NF**: 2NF + không có phụ thuộc bắc cầu (thuộc tính không khóa không phụ thuộc vào các thuộc tính không khóa khác)
- **BCNF**: 3NF mạnh hơn, mọi định thức đều là khóa dự tuyển
- **4NF**: Không có phần phụ thuộc nhiều giá trị
- **5NF**: Không phụ thuộc vào việc tham gia
### RDBMS phổ biến
- **PostgreSQL**: Các tính năng nâng cao, có thể mở rộng, tuân thủ ACID
- **MySQL**: Ứng dụng web được sử dụng rộng rãi, đọc nhanh
- **Oracle**: Tính năng dành cho doanh nghiệp, khả năng mở rộng, đắt tiền
- **SQL Server**: Hệ sinh thái Microsoft, các công cụ tích hợp
- **SQLite**: Được nhúng, không cần máy chủ, nhẹ
- **MariaDB**: Phân nhánh MySQL, mã nguồn mở
## Cơ sở dữ liệu NoSQL
### Các loại cơ sở dữ liệu NoSQL
#### Kho tài liệu
- **Cấu trúc**: Tài liệu giống JSON (BSON)
- **Trường hợp sử dụng**: Quản lý nội dung, danh mục, hồ sơ người dùng
- **Ví dụ**: MongoDB, CouchDB, DocumentDB
- **Ví dụ truy vấn** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Cửa hàng khóa-giá trị
- **Cấu trúc**: Cặp khóa-giá trị đơn giản
- **Trường hợp sử dụng**: Bộ nhớ đệm, phiên, giỏ hàng
- **Ví dụ**: Redis, DynamoDB, Riak
- **Đặc điểm**: Truy vấn nhanh, đơn giản, hạn chế
#### Cửa hàng cột-Gia đình
- **Cấu trúc**: Các cột được nhóm thành các họ
- **Trường hợp sử dụng**: Dữ liệu lớn, phân tích, chuỗi thời gian
- **Ví dụ**: Cassandra, HBase, ScyllaDB
- **Đặc điểm**: Tối ưu hóa ghi, phân tán, có thể mở rộng
#### Cơ sở dữ liệu đồ thị
- **Cấu trúc**: Nút, cạnh, thuộc tính
- **Trường hợp sử dụng**: Mạng xã hội, phát hiện gian lận, đề xuất
- **Ví dụ**: Neo4j, Amazon Neptune, ArangoDB
- **Ngôn ngữ truy vấn**: Cypher (Neo4j), Gremlin
### Khi nào nên sử dụng NoSQL
- Lược đồ linh hoạt/phát triển
- Yêu cầu chia tỷ lệ theo chiều ngang
- Thông lượng ghi cao
- Dữ liệu phân cấp/lồng nhau
- Hệ thống phân tán
- Ứng dụng thời gian thực
## Thiết kế cơ sở dữ liệu
### Mô hình hóa mối quan hệ thực thể
- **Thực thể**: Đối tượng/khái niệm (Khách hàng, Sản phẩm, Đơn hàng)
- **Thuộc tính**: Thuộc tính của thực thể (tên, giá, ngày)
- **Mối quan hệ**: Kết nối giữa các thực thể (một-một, một-nhiều, nhiều-nhiều)
- **Cardinality**: Số lượng phiên bản trong mối quan hệ
### Mẫu thiết kế lược đồ
- **Kế thừa bảng đơn**: Tất cả các loại trong một bảng có bộ phân biệt loại
- **Kế thừa bảng lớp**: Các bảng riêng biệt cho lớp cơ sở và lớp con
- **Kế thừa bảng cụ thể**: Bảng riêng cho từng lớp cụ thể
- **Bảng nối**: Giải quyết mối quan hệ nhiều-nhiều
- **Bảng kiểm tra**: Theo dõi các thay đổi (created_at,update_at, đã xóa_at)
### Chiến lược lập chỉ mục
- **B-Tree**: Mặc định, truy vấn phạm vi, sắp xếp
- **Băm**: Tra cứu kết quả khớp chính xác
- **Bitmap**: Cột số lượng thấp (giới tính, trạng thái)
- **Toàn văn**: Khả năng tìm kiếm văn bản
- **Không gian**: Dữ liệu địa lý (GIS)
- **Composite**: Kết hợp nhiều cột
- **Bao phủ**: Bao gồm tất cả các cột cần thiết cho truy vấn
## Tối ưu hóa truy vấn
### Kế hoạch thực hiện
- Hiểu cách cơ sở dữ liệu thực hiện các truy vấn
- Xác định các điểm nghẽn (quét toàn bộ bảng, thiếu chỉ mục)
- Công cụ: GIẢI THÍCH, GIẢI THÍCH PHÂN TÍCH
### Kỹ thuật tối ưu hóa
- **Sử dụng chỉ mục**: Đảm bảo truy vấn sử dụng chỉ mục thích hợp
- **Viết lại truy vấn**: Đơn giản hóa các truy vấn phức tạp
- **Tối ưu hóa tham gia**: Chọn đúng loại và thứ tự tham gia
- **Phân vùng**: Chia các bảng lớn (phạm vi, hàm băm, danh sách)
- **Chế độ xem được cụ thể hóa**: Kết quả truy vấn được tính toán trước
- **Bộ nhớ đệm truy vấn**: Lưu trữ kết quả truy vấn thường xuyên
### Các vấn đề thường gặp về hiệu suất
- **Vấn đề truy vấn N+1**: Tìm nạp dữ liệu liên quan không hiệu quả
- **Thiếu chỉ mục**: Quét toàn bộ bảng trên các bảng lớn
- **Lập chỉ mục quá mức**: Ghi chậm do có quá nhiều chỉ mục
- **Chống tranh chấp khóa**: Giao dịch chờ khóa
- **Truy vấn không hiệu quả**: CHỌN *, các phép nối không cần thiết
## Giao dịch và đồng thời
### Mức độ cô lập giao dịch
- **ĐỌC KHÔNG CAM KẾT**: Khả năng cách ly thấp nhất, có thể đọc sai
- **ĐỌC CAM KẾT**: Chỉ hiển thị dữ liệu đã cam kết (mặc định trong hầu hết các DB)
- **ĐỌC LẶP LẠI**: Cùng một truy vấn trả về cùng một kết quả trong giao dịch
- **SERIALIZABLE**: Cách ly cao nhất, giao dịch thực hiện tuần tự
### Kiểm soát đồng thời
- **Khóa bi quan**: Khóa tài nguyên trước khi truy cập
- **Khóa lạc quan**: Kiểm tra phiên bản trước khi cam kết
- **MVCC (Kiểm soát đồng thời nhiều phiên bản)**: Duy trì nhiều phiên bản của hàng
- **Khóa cấp hàng**: Khóa các hàng cụ thể
- **Khóa cấp độ bảng**: Khóa toàn bộ bảng
### Bế tắc
- Phụ thuộc vòng tròn nơi các giao dịch chờ đợi lẫn nhau
- Phòng ngừa: Thứ tự khóa nhất quán, hết thời gian chờ, phát hiện bế tắc
- Giải pháp: Hủy một giao dịch
## Sao chép và nhân rộng
### Các kiểu sao chép
- **Master-Slave**: Một bản sao chính, nhiều bản sao đọc
- **Master-Master**: Nhiều cuộc bầu cử sơ bộ, sao chép hai chiều
- **Multi-Master**: N bầu cử sơ bộ, cần giải quyết xung đột
- **Sao chép chuỗi**: Sao chép tuần tự thông qua các nút
### Phương pháp mở rộng quy mô
- **Tỷ lệ theo chiều dọc**: Tăng tài nguyên máy chủ (CPU, RAM, bộ nhớ)
- **Chia tỷ lệ theo chiều ngang**: Thêm nhiều máy chủ hơn (phân mảnh, phân vùng)
- **Bản sao đọc**: Giảm tải lưu lượng đọc
- **Sharding**: Chia dữ liệu giữa các máy chủ theo khóa/phạm vi/băm
- **Liên đoàn**: Chia theo chức năng/dịch vụ
### Mô hình nhất quán
- **Tính nhất quán cao**: Tất cả các nút đều xem cùng một dữ liệu tại cùng một thời điểm
- **Tính nhất quán cuối cùng**: Các nút hội tụ theo thời gian
- **Tính nhất quán nhân quả**: Duy trì mối quan hệ nhân quả
- **Đọc-Viết của bạn**: Người dùng thấy ngay các cập nhật của chính họ
## Sao lưu và phục hồi
### Chiến lược dự phòng
- **Sao lưu đầy đủ**: Bản sao cơ sở dữ liệu hoàn chỉnh
- **Sao lưu gia tăng**: Những thay đổi kể từ lần sao lưu cuối cùng
- **Sao lưu vi sai**: Những thay đổi kể từ lần sao lưu đầy đủ gần đây nhất
- **Phục hồi tại thời điểm**: Khôi phục về thời điểm cụ thể
- **Sao lưu liên tục**: Sao chép thời gian thực để sao lưu
### Quy trình khôi phục
- **RTO (Mục tiêu về thời gian phục hồi)**: Thời gian ngừng hoạt động tối đa có thể chấp nhận được
- **RPO (Mục tiêu điểm khôi phục)**: Mất dữ liệu tối đa có thể chấp nhận được
- **Kế hoạch khắc phục thảm họa**: Thủ tục được ghi lại đối với các lỗi
- **Kiểm tra**: Luyện tập phục hồi thường xuyên
## Bảo vệ
### Kiểm soát truy cập
- **Xác thực**: Xác minh danh tính người dùng
- **Ủy quyền**: Cấp quyền (CẤP, THU HỒI)
- **Vai trò**: Quyền nhóm để quản lý dễ dàng hơn
- **Nguyên tắc đặc quyền tối thiểu**: Quyền truy cập cần thiết ở mức tối thiểu
### Bảo vệ dữ liệu
- **Encryption at Rest**: Mã hóa dữ liệu được lưu trữ
- **Mã hóa khi chuyển tuyến**: TLS/SSL cho các kết nối
- **Masking**: Ẩn dữ liệu nhạy cảm trong phiên bản không sản xuất
- **Mã thông báo**: Thay thế dữ liệu nhạy cảm bằng mã thông báo
### Các lỗ hổng phổ biến
- **Tội lỗi SQL**: SQL độc hại trong đầu vào của người dùng
- **Nâng cao đặc quyền**: Đạt được quyền truy cập trái phép
- **Ghi nhật ký kiểm tra**: Theo dõi tất cả các hoạt động cơ sở dữ liệu
- **Tuân thủ**: Yêu cầu GDPR, HIPAA, PCI-DSS
## Công nghệ cơ sở dữ liệu hiện đại
### Cơ sở dữ liệu đám mây
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: Cơ sở dữ liệu SQL, Cosmos DB, Synapse
- **Lợi ích**: Dịch vụ được quản lý, tự động mở rộng quy mô, bao gồm sao lưu
### Cơ sở dữ liệu NewSQL
- Kết hợp tính nhất quán của SQL với khả năng mở rộng NoSQL
- **Ví dụ**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Tính năng**: Giao dịch phân tán, ACID, chia tỷ lệ theo chiều ngang
### Cơ sở dữ liệu chuỗi thời gian
- Tối ưu hóa cho dữ liệu được đánh dấu thời gian
- **Ví dụ**: InfluxDB, TimescaleDB, Prometheus
- **Trường hợp sử dụng**: IoT, giám sát, dữ liệu tài chính
### Cơ sở dữ liệu vectơ
- Lưu trữ và truy vấn các vectơ nhúng
- **Ví dụ**: Quả thông, Milvus, Weaviate, Qdrant
- **Trường hợp sử dụng**: Tìm kiếm ngữ nghĩa, hệ thống đề xuất, ứng dụng AI
### Cơ sở dữ liệu đa mô hình
- Hỗ trợ nhiều mô hình dữ liệu trong một hệ thống
- **Ví dụ**: ArangoDB, OrientDB, Azure Cosmos DB
- **Lợi ích**: Tính linh hoạt mà không cần nhiều cơ sở dữ liệu
## ORM và quyền truy cập dữ liệu
### Ánh xạ quan hệ đối tượng
- **Mục đích**: Ánh xạ các bảng cơ sở dữ liệu tới các đối tượng lập trình
- **ORM phổ biến**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Phần tiếp theo, Prisma, TypeORM
  - Java: Ngủ đông, JPA
  - Ruby: ActiveRecord
  - .NET: Khung thực thể
### Lợi ích
- Trừu tượng hóa từ SQL
- Loại an toàn
- Quản lý di chuyển
- API xây dựng truy vấn
### Nhược điểm
- Chi phí hiệu suất
- Truy vấn phức tạp khó viết hơn
- Vấn đề truy vấn N+1
- Đường cong học tập
##Quản trị cơ sở dữ liệu
### Trách nhiệm của DBA
- Cài đặt và cấu hình
- Điều chỉnh hiệu suất
- Sao lưu và phục hồi
- Quản lý an ninh
- Quy hoạch năng lực
- Giám sát và cảnh báo
- Quản lý bản vá
### Số liệu giám sát
- Thời gian phản hồi truy vấn
- Thông lượng (giao dịch mỗi giây)
- Số lượng kết nối
- Tỷ lệ trúng bộ đệm
- Vào/ra đĩa
- Khóa thời gian chờ
- Độ trễ sao chép
### Nhiệm vụ bảo trì
- **Chân không/Phân tích**: Cập nhật số liệu thống kê, lấy lại dung lượng
- **Xây dựng lại chỉ mục**: Chống phân mảnh chỉ mục
- **Cập nhật số liệu thống kê**: Luôn thông báo cho trình tối ưu hóa truy vấn
- **Xoay vòng nhật ký**: Quản lý kích thước tệp nhật ký
- **Lập kế hoạch năng lực**: Dự đoán tăng trưởng, lên kế hoạch nâng cấp