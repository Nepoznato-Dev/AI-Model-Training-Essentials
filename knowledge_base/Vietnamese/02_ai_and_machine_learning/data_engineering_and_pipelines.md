---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Kỹ thuật dữ liệu và đường ống
Kỹ thuật dữ liệu là môn học xây dựng các hệ thống di chuyển, chuyển đổi và lưu trữ dữ liệu trên quy mô lớn. Nếu không có đường truyền dữ liệu đáng tin cậy, các mô hình học máy không thể được đào tạo, bảng thông tin hiển thị các con số cũ và các quyết định kinh doanh đều dựa trên phỏng đoán. Tệp này bao gồm kiến ​​trúc, công cụ và thực tiễn để xây dựng cơ sở hạ tầng dữ liệu hoạt động.
---

## ETL vs ELT
| Tiếp cận | Nó hoạt động như thế nào | Tốt nhất cho | Công cụ |
|----------|-------------|----------|-------|
| **ETL** (Trích xuất → Chuyển đổi → Tải) | Chuyển đổi dữ liệu *trước khi* tải vào kho | Kho truyền thống với khả năng tính toán hạn chế | Informatica, Talend, Apache NiFi |
| **ELT** (Trích xuất → Tải → Chuyển đổi) | Tải dữ liệu thô trước; biến đổi *bên trong* nhà kho | Kho đám mây hiện đại với khả năng tính toán đàn hồi | dbt, Fivetran, Airbyte + BigQuery/Bông tuyết |
Việc chuyển từ ETL sang ELT được thúc đẩy bởi các kho dữ liệu đám mây (BigQuery, Snowflake, Redshift) có thể mở rộng quy mô tính toán độc lập với bộ nhớ. Không còn cần phải xử lý trước mọi thứ trước khi tải.
---

## Hồ dữ liệu và Kho dữ liệu
| Tính năng | Hồ dữ liệu | Kho dữ liệu |
|----------|-------------|---------------|
| **Định dạng dữ liệu** | Định dạng thô, gốc (lược đồ khi đọc) | Có cấu trúc, được xử lý (lược đồ khi ghi) |
| **Lược đồ** | Được xác định tại thời điểm truy vấn | Được xác định trước khi tải |
| **Các loại dữ liệu** | Có cấu trúc, bán cấu trúc, không cấu trúc | Cấu trúc chủ yếu |
| **Người dùng** | Nhà khoa học dữ liệu, kỹ sư | Nhà phân tích kinh doanh, công cụ BI |
| **Chi phí** | Lưu trữ rẻ hơn (lưu trữ đối tượng) | Đắt hơn (được tối ưu hóa cho truy vấn) |
| **Ví dụ** | AWS S3, Hồ dữ liệu Azure, GCS | Bông tuyết, BigQuery, Dịch chuyển đỏ |
Cách tiếp cận hiện đại là **nhà hồ**: kết hợp việc lưu trữ hồ linh hoạt, giá rẻ với các tính năng quản lý và hiệu suất của nhà kho. Delta Lake, Apache Iceberg và Apache Hudi là những công nghệ chủ chốt ở đây.
---

## Kiến trúc đường ống
### Hàng loạt và Phát trực tuyến
| Chế độ | Mô tả | Độ trễ | Trường hợp sử dụng |
|------|-------------|----------|----------|
| **Đợt** | Xử lý dữ liệu theo khối lớn theo khoảng thời gian đã lên lịch | Phút đến giờ | Báo cáo hàng ngày, công việc ETL, làm giàu dữ liệu |
| **Truyền phát** | Xử lý dữ liệu liên tục khi nó đến | Mili giây sang giây | Bảng điều khiển thời gian thực, phát hiện gian lận, cảnh báo |
| **Micro-lô** | Lô nhỏ với khoảng thời gian rất ngắn | Giây | Gần thời gian thực với tính đơn giản hàng loạt |
### Thành phần đường ống
Một đường ống dữ liệu điển hình có các giai đoạn sau:
| Sân khấu | Mô tả | Công cụ |
|-------|-------------|-------|
| **Ăn vào** | Thu thập dữ liệu từ các nguồn | Kafka, Airbyte, Fivetran, Debezium |
| **Biến đổi** | Làm sạch, làm giàu, tổng hợp | dbt, Spark, Gấu trúc |
| **Lưu trữ** | Dữ liệu được xử lý liên tục | BigQuery, Bông tuyết, S3, Hồ Delta |
| **Phục vụ** | Cung cấp dữ liệu cho người tiêu dùng | API, trang tổng quan, cửa hàng tính năng ML |
| **Dàn nhạc** | Lên lịch và quản lý các phần phụ thuộc | Luồng không khí, Tỉnh trưởng, Dao găm |
| **Giám sát** | Theo dõi tình trạng đường ống và chất lượng dữ liệu | Kỳ vọng lớn, Monte Carlo, cảnh báo tùy chỉnh |
---

## Công cụ điều phối
| Công cụ | Tiếp cận | Sức mạnh |
|------|----------|----------|
| **Luồng khí Apache** | DAG dựa trên Python; tiêu chuẩn ngành | Hệ sinh thái khổng lồ, trưởng thành, linh hoạt |
| **Quận trưởng** | Python-bản địa; API sạch hơn Airflow | Thiết kế hiện đại, xử lý lỗi tốt |
| **Dao găm** | Lấy tài sản làm trung tâm; phương pháp công nghệ phần mềm | Hệ thống loại, thử nghiệm, khả năng quan sát |
| **Luigi** | Công cụ đường dẫn ban đầu của Spotify | Đơn giản nhưng ít phát triển tích cực |
### Ví dụ về luồng không khí
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## Apache Kafka
Kafka là xương sống của nhiều hệ thống dữ liệu thời gian thực. Đó là nhật ký sự kiện được phân phối cung cấp thông báo có thông lượng cao, có khả năng chịu lỗi.
### Khái niệm cốt lõi
| Khái niệm | Mô tả |
|----------|-------------|
| **Chủ đề** | Một danh mục tin nhắn (ví dụ:`orders`,`user-events`) |
| **Phân vùng** | Các chủ đề được chia thành các phân vùng để song song |
| **Nhà sản xuất** | Ứng dụng viết tin nhắn theo chủ đề |
| **Người tiêu dùng** | Ứng dụng đọc tin nhắn theo chủ đề |
| **Nhóm người tiêu dùng** | Nhóm người tiêu dùng chia sẻ gánh nặng đọc một chủ đề |
| **Bù đắp** | Vị trí của người tiêu dùng trong một phân vùng |
| **Nhà môi giới** | Nút máy chủ Kafka |
### Khi nào nên sử dụng Kafka
- **Truyền phát sự kiện**: Xử lý sự kiện theo thời gian thực trên quy mô lớn.
- **Dịch vụ tách rời**: Nhà sản xuất và người tiêu dùng không cần biết về nhau.
- **Phát lại**: Tin nhắn được giữ lại; người tiêu dùng có thể đọc lại từ bất kỳ phần bù nào.
- **Back Pressure**: Kafka xử lý một cách tự nhiên sự khác biệt về tốc độ giữa nhà sản xuất và người tiêu dùng.
---

## Mô hình hóa dữ liệu
### Lược đồ sao và Lược đồ bông tuyết
| Lược đồ | Cấu trúc | Ưu điểm | Nhược điểm |
|--------|-------------|------|------|
| **Sao** | Bảng dữ kiện trung tâm được bao quanh bởi các bảng thứ nguyên không chuẩn hóa | Truy vấn đơn giản, đọc nhanh | Dự phòng dữ liệu |
| **Bông tuyết** | Các bảng thứ nguyên được chuẩn hóa (chia thành các bảng con) | Ít dư thừa | Tham gia nhiều hơn, truy vấn chậm hơn |
### Bảng sự kiện và thứ nguyên
| Loại bảng | Chứa | Ví dụ |
|----------|----------|----------|
| **Sự thật** | Các sự kiện có thể đo lường được (số liệu) | `orders`(id_đơn hàng, id_sản phẩm, id khách hàng, số tiền, ngày) |
| **Kích thước** | Thuộc tính mô tả | `products`(product_id, tên, danh mục, giá),`customers`(customer_id, tên, thành phố) |
---

## Cửa hàng tính năng
Cửa hàng tính năng là kho lưu trữ tập trung các tính năng ML — các giá trị dẫn xuất được sử dụng làm đầu vào cho mô hình (ví dụ: "giá trị đặt hàng trung bình của người dùng trong 30 ngày qua").
| Năng lực | Mô tả |
|----------||-------------|
| **Đăng ký tính năng** | Danh mục các tính năng có sẵn với siêu dữ liệu |
| **Cửa hàng ngoại tuyến** | Đặc điểm lịch sử cho đào tạo mô hình (đợt) |
| **Cửa hàng trực tuyến** | Tính năng có độ trễ thấp phục vụ suy luận theo thời gian thực |
| **Giám sát tính năng** | Phát hiện độ lệch, thiếu giá trị, thay đổi phân phối |
| Công cụ | Mô tả |
|------|-------------|
| **Tiệc** | Nguồn mở; hoạt động với mọi khung ML |
| **Tecton** | Thuộc về thương mại; nền tảng tính năng thời gian thực |
| **Hoa bia** | Nguồn mở; nền tảng ML đầy đủ với cửa hàng tính năng |
| **Cửa hàng tính năng Databricks** | Tích hợp với Databricks/Spark |
---

## Chất lượng dữ liệu
Chất lượng dữ liệu là kẻ giết người thầm lặng của các dự án ML. Rác vào, rác ra.
### Kích thước chất lượng
| Kích thước | Câu hỏi |
|----------||----------|
| **Độ chính xác** | Dữ liệu có phản ánh thực tế không? |
| **Sự hoàn thiện** | Các trường bắt buộc có được điền không? |
| **Tính nhất quán** | Các giá trị có đồng ý giữa các nguồn không? |
| **Tính kịp thời** | Dữ liệu có hiện tại không? |
| **Hiệu lực** | Các giá trị có tuân theo các quy tắc đã xác định không? |
| **Tính độc đáo** | Có hồ sơ trùng lặp? |
### Công cụ chất lượng dữ liệu
| Công cụ | Tiếp cận |
|------|----------|
| **Kỳ vọng lớn** | Dựa trên Python; xác định “kỳ vọng” về dữ liệu |
| **Mont Carlo** | Nền tảng quan sát dữ liệu được hỗ trợ bởi ML |
| **kiểm tra dbt** | Các thử nghiệm tích hợp cho dữ liệu kho (duy nhất, not_null, mối quan hệ) |
| **Soda** | Quét chất lượng dữ liệu nguồn mở |
---

## Quản trị dữ liệu
Quản trị dữ liệu đảm bảo rằng dữ liệu được quản lý một cách có trách nhiệm trong toàn tổ chức.
| Khu vực | Mô tả |
|------|-------------|
| **Danh mục dữ liệu** | Kho dữ liệu có thể tìm kiếm được với siêu dữ liệu (Amundsen, DataHub, Atlan) |
| **Dòng dữ liệu** | Theo dõi dữ liệu đến từ đâu và nó biến đổi như thế nào |
| **Kiểm soát truy cập** | Quyền dựa trên vai trò; ai có thể đọc/viết cái gì |
| **Tuân thủ** | Tuân thủ GDPR, CCPA, HIPAA |
| **Quyền sở hữu dữ liệu** | Xóa quyền sở hữu cho từng tập dữ liệu (quản lý) |
| **Chính sách lưu giữ** | Xác định thời gian lưu giữ dữ liệu và thời điểm xóa dữ liệu |
---

## Ngăn xếp dữ liệu hiện đại
"Ngăn xếp dữ liệu hiện đại" đề cập đến sự kết hợp điển hình của các công cụ được các nhóm dữ liệu sử dụng ngày nay:
| Lớp | Công cụ điển hình |
|-------|--------------|
| **Ăn vào** | Fivetran, Airbyte |
| **Kho** | Bông tuyết, BigQuery, Dịch chuyển đỏ |
| **Biến đổi** | dbt |
| **Dàn nhạc** | Luồng không khí, Tỉnh trưởng, Dao găm |
| **BI / Trực quan hóa** | Người xem, Metabase, Tableau |
| **Đảo ngược ETL** | Census, Hightouch (đồng bộ dữ liệu kho về công cụ) |
| **Chất lượng dữ liệu** | Kỳ vọng lớn, Monte Carlo |
Xu hướng hướng tới các công cụ mô-đun tốt nhất được kết nối bằng các tiêu chuẩn mở (SQL, mô hình dbt, Airflow DAG) thay vì các nền tảng nguyên khối.