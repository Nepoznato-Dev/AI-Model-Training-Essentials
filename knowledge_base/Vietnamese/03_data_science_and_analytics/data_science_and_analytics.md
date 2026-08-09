---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
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
# Khoa học dữ liệu và phân tích
Khoa học dữ liệu là môn học biến dữ liệu thô thành thông tin chi tiết có thể hành động được. Nó nằm ở giao điểm của thống kê, khoa học máy tính và kiến ​​thức chuyên môn về lĩnh vực — và nó đã trở nên thiết yếu trong mọi lĩnh vực từ tài chính đến chăm sóc sức khỏe. Tệp này trình bày các khái niệm, công cụ và quy trình công việc cốt lõi mà mọi người hành nghề nên biết.
---

## Quy trình khoa học dữ liệu
Hầu hết các dự án đều tuân theo một số biến thể của **CRISP-DM**, vòng đời tiêu chuẩn ngành:
| Giai đoạn | Điều gì xảy ra | Giờ điển hình |
|-------|-----------------|--------------|
| **Hiểu biết về kinh doanh** | Xác định mục tiêu, số liệu thành công và các ràng buộc | 10–15% |
| **Hiểu dữ liệu** | Thu thập, khám phá và lập hồ sơ dữ liệu | 10–15% |
| **Chuẩn bị dữ liệu** | Tính năng làm sạch, biến đổi, kỹ sư | ~50–60% |
| **Làm người mẫu** | Lựa chọn và đào tạo mô hình | 10–15% |
| **Đánh giá** | Đánh giá hiệu quả hoạt động so với mục tiêu kinh doanh | 5–10% |
| **Triển khai** | Đưa mô hình đi sản xuất | 5–10% |
Trò đùa cũ là 80% khoa học dữ liệu đang làm sạch dữ liệu. Nó không xa sự thật.
---

## Sơ lược về các kiểu dữ liệu
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Có cấu trúc** | Được tổ chức theo hàng và cột | Bảng, bảng tính SQL |
| **Không có cấu trúc** | Không có định dạng được xác định trước | Văn bản, hình ảnh, âm thanh, video |
| **Bán cấu trúc** | Một số tổ chức nhưng linh hoạt | JSON, XML, HTML |
| **Chuỗi thời gian** | Dữ liệu tuần tự được lập chỉ mục theo thời gian | Giá cổ phiếu, bài đọc cảm biến |
| **Không gian** | Dựa trên địa lý hoặc vị trí | Tọa độ GPS, dữ liệu bản đồ |
| **Biểu đồ** | Các nút và cạnh thể hiện mối quan hệ | Mạng xã hội, đồ thị tri thức |
---

## Nguyên tắc cơ bản về thống kê
### Thống kê mô tả và suy luận
Thống kê mô tả tóm tắt những gì bạn *có*; thống kê suy luận cho phép bạn đưa ra kết luận về những gì bạn *không* có (dân số rộng hơn).
| Khái niệm | Ý tưởng chính |
|----------|----------|
| **Khuynh hướng trung tâm** | Trung bình (nhạy cảm với các ngoại lệ), trung vị (mạnh), chế độ (thường xuyên nhất) |
| **Phân tán** | Phạm vi, phương sai, độ lệch chuẩn, phạm vi liên vùng |
| **Hình dạng phân phối** | Độ lệch (không đối xứng), độ nhọn (độ nặng của đuôi) |
| **Kiểm tra giả thuyết** | Giả thuyết không và giả thuyết thay thế, giá trị p, mức ý nghĩa (α) |
| **Khoảng tin cậy** | Phạm vi có khả năng chứa tham số dân số thực sự |
| **Lỗi Loại I / Loại II** | Dương tính giả (từ chối giá trị rỗng đúng) / âm tính giả (thiếu hiệu ứng thực) |
### Kiểm tra thống kê thông thường
| Kiểm tra | Khi nào nên sử dụng |
|------|-------------|
| **t-kiểm tra** | So sánh phương tiện giữa hai nhóm |
| **ANOVA** | So sánh các phương tiện giữa ba nhóm trở lên |
| **Chi-vuông** | Kiểm tra tính độc lập của các biến phân loại |
| **Mann-Whitney U** | Thay thế phi tham số cho t-test (không có giả định về tính quy phạm) |
| **Tương quan Pearson** | Mối quan hệ tuyến tính giữa hai biến liên tục |
| **Tương quan Spearman** | Mối quan hệ đơn điệu (dựa trên cấp bậc, mạnh mẽ hơn) |
### Phân phối xác suất đáng biết
| Phân phối | Trường hợp sử dụng |
|-------------|----------|
| **Bình thường** | Hiện tượng tự nhiên, sai số đo lường — đường cong hình chuông cổ điển |
| **Nhị thức** | Số lượng thành công/thất bại (lật xu, tỷ lệ chuyển đổi) |
| **Poisson** | Số sự kiện được tính trong một khoảng thời gian cố định (cuộc gọi mỗi giờ, lỗi mỗi đợt) |
| **Số mũ** | Thời gian giữa các sự kiện (thời gian chờ, khoảng thời gian lỗi) |
| **t-Phân phối** | Mẫu nhỏ hoặc phương sai tổng thể chưa biết |
| **Chi-vuông** | Phân tích dữ liệu phân loại, kiểm tra mức độ phù hợp |
---

## Thu thập và lưu trữ dữ liệu
### Dữ liệu đến từ đâu
Dữ liệu trong thế giới thực đến từ nhiều nguồn: cơ sở dữ liệu quan hệ, API (REST, GraphQL), tệp phẳng (CSV, JSON, Parquet), nền tảng phát trực tuyến (Kafka, Kinesis), khảo sát và kho lưu trữ công cộng (Kaggle, cổng chính phủ). Định dạng bạn nhận được quyết định phần lớn chiến lược tiền xử lý của bạn.
### Khái niệm lưu trữ dữ liệu
| Khái niệm | Mô tả |
|----------|-------------|
| **ETL** | Trích xuất → Chuyển đổi → Tải — cách tiếp cận đường ống truyền thống |
| **ELT** | Trích xuất → Tải → Chuyển đổi — cách tiếp cận đám mây hiện đại (tải thô, chuyển đổi trong kho) |
| **Hồ dữ liệu** | Dữ liệu thô được lưu trữ ở định dạng gốc (lược đồ khi đọc) |
| **Kho dữ liệu** | Dữ liệu có cấu trúc, được xử lý được tối ưu hóa để phân tích (lược đồ khi ghi) |
| **Siêu thị dữ liệu** | Một tập hợp con của kho, nằm trong phạm vi một bộ phận hoặc miền |
| **Lược đồ sao** | Bảng dữ kiện trung tâm được bao quanh bởi các bảng thứ nguyên |
| **Sơ đồ bông tuyết** | Bảng kích thước được chuẩn hóa (ít dư thừa hơn, nhiều kết nối hơn) |
### Các loại cơ sở dữ liệu
| Loại | Ví dụ | Tốt nhất cho |
|------|----------|----------|
| **Quan hệ (SQL)** | PostgreSQL, MySQL, Oracle | Dữ liệu có cấu trúc, giao dịch ACID |
| **Tài liệu** | MongoDB, CouchDB | Lược đồ linh hoạt, dữ liệu giống JSON |
| **Khóa-Giá trị** | Redis, DynamoDB | Bộ nhớ đệm, phiên, tra cứu đơn giản |
| **Cột-Gia đình** | Cassandra, HBase | Khối lượng công việc ghi nhiều, chuỗi thời gian |
| **Biểu đồ** | Neo4j, Amazon Neptune | Các mối quan hệ, mạng xã hội |
| **Dòng thời gian** | InfluxDB, TimescaleDB | Số liệu, giám sát IoT |
| **Vectơ** | Quả thông, Milvus | Nhúng bộ nhớ để tìm kiếm ML/AI |
---

## Xử lý trước dữ liệu và kỹ thuật tính năng
### Danh sách kiểm tra vệ sinh
Mọi tập dữ liệu thực đều có vấn đề. Đây là cách dọn dẹp tiêu chuẩn:
| Vấn đề | Tiếp cận |
|-------|----------|
| **Thiếu giá trị** | Sự thay đổi (trung bình, trung bình, dự đoán) hoặc xóa nếu thưa thớt |
| **Ngoại lệ** | Phát hiện thông qua IQR hoặc điểm Z; xử lý bằng giới hạn hoặc chuyển đổi |
| **Trùng lặp** | Xác định và loại bỏ |
| **Mâu thuẫn** | Chuẩn hóa định dạng, sửa lỗi chính tả, chuẩn hóa đơn vị |
### Kỹ thuật chuyển đổi
| Kỹ thuật | Nó làm gì |
|----------||-------------|
| **Bình thường hóa** | Chia tỷ lệ các giá trị thành phạm vi 0–1 |
| **Tiêu chuẩn hóa** | Điểm Z: trung bình = 0, std = 1 |
| **Mã hóa một lần** | Chuyển đổi danh mục thành cột nhị phân |
| **Mã hóa nhãn** | Gán nhãn số nguyên cho danh mục |
| **Chuyển đổi nhật ký** | Giảm độ lệch phải của dữ liệu |
| **Nhóm** | Nhóm các giá trị liên tục vào các nhóm riêng biệt |
### Kỹ thuật tính năng
Kỹ thuật tính năng thường là sự khác biệt giữa một mô hình tầm thường và một mô hình tuyệt vời. Các kỹ thuật chính bao gồm:
- **Tạo tính năng**: Lấy các cột mới từ các cột hiện có (ví dụ:`age_group`từ`age`).
- **Lựa chọn tính năng**: Phương thức lọc (tương quan), phương thức bao bọc (loại bỏ đệ quy), phương thức nhúng (LASSO, tầm quan trọng của cây).
- **Giảm kích thước**: PCA cho tuyến tính, t-SNE hoặc UMAP cho trực quan hóa.
- **Thuật ngữ tương tác**: Kết hợp các tính năng theo cấp số nhân để nắm bắt được hiệu ứng chung.
---

## Phân tích dữ liệu thăm dò (EDA)
EDA là nơi bạn phát triển trực giác về dữ liệu của mình trước khi lập mô hình. Mục tiêu là phát hiện các mô hình, sự bất thường và các mối quan hệ.
### Chọn biểu đồ phù hợp
| Loại biểu đồ | Tốt nhất cho |
|----------||----------|
| **Biểu đồ** | Phân phối một biến duy nhất |
| **Biểu đồ hộp** | Tóm tắt năm số, phát hiện ngoại lệ |
| **Biểu đồ phân tán** | Mối quan hệ giữa hai biến liên tục |
| **Bản đồ nhiệt** | Ma trận tương quan, trực quan hóa mật độ |
| **Biểu đồ thanh** | So sánh danh mục |
| **Biểu đồ đường** | Xu hướng theo thời gian |
| **Âm mưu vĩ cầm** | Mật độ phân phối + tóm tắt ô hộp |
| **Sơ đồ cặp** | Tổng quan nhanh về tất cả các cặp biến |
### Ngăn xếp EDA của Python
| Thư viện | Vai trò |
|----------|------|
| **gấu trúc** | Thao tác và phân tích dữ liệu |
| **bụi bặm** | Tính toán số |
| **matplotlib** | Vẽ móng |
| **sinh vật biển** | Trực quan hóa thống kê (được xây dựng trên matplotlib) |
| **âm mưu** | Trực quan hóa dựa trên web, tương tác |
| **scipy** | Tính toán khoa học và thống kê |
---

## Học máy trong khoa học dữ liệu
### Sơ lược về học tập có giám sát
| Nhiệm vụ | Thuật toán |
|------|-------------|
| **Hồi quy** (dự đoán một số) | Tuyến tính, Ridge/LASSO, Cây quyết định, Rừng ngẫu nhiên, Tăng cường độ dốc (XGBoost, LightGBM) |
| **Phân loại** (dự đoán một danh mục) | Hồi quy logistic, k-NN, Naive Bayes, SVM, Cây quyết định, Rừng ngẫu nhiên, Mạng thần kinh |
### Sơ lược về học tập không giám sát
| Nhiệm vụ | Thuật toán |
|------|-------------|
| **Phân cụm** | k-Means, Mô hình phân cấp, DBSCAN, Hỗn hợp Gaussian |
| **Giảm kích thước** | PCA, t-SNE, UMAP, Bộ mã hóa tự động |
| **Quy tắc kết hợp** | Apriori, FP-Tăng trưởng |
###Đánh giá mô hình
| Loại số liệu | Số liệu chính |
|-------------|-------------|
| **Phân loại** | Độ chính xác, độ chính xác, thu hồi, điểm F1, ROC-AUC, ma trận nhầm lẫn |
| **Hồi quy** | MAE, MSE, RMSE, R 2, R 2 đã điều chỉnh |
| **Xác thực** | xác thực chéo k-fold, phân tầng, phân chia chuỗi thời gian |
| **Điều chỉnh** | Tìm kiếm lưới, tìm kiếm ngẫu nhiên, tối ưu hóa Bayes |
---

## Công nghệ dữ liệu lớn
Khi các tập dữ liệu vượt quá những gì một máy có thể xử lý, tính toán phân tán sẽ xuất hiện.
| Khung | Sức mạnh |
|----------||----------|
| **Tia lửa Apache** | Xử lý trong bộ nhớ; Spark SQL, Phát trực tuyến, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — ngăn xếp dữ liệu lớn ban đầu |
| **Liên kết Apache** | Xử lý luồng có độ trễ thấp |
| **Tia Apache** | Mô hình phát trực tuyến và hàng loạt thống nhất |
### Nền tảng dữ liệu đám mây
| Nhà cung cấp | Dịch vụ chính |
|----------|-------------|
| **AWS** | S3, EMR, Dịch chuyển đỏ, SageMaker, Keo |
| **Đám mây của Google** | BigQuery, Dataproc, Nền tảng AI, Lưu trữ đám mây |
| **Azure** | Phân tích khớp thần kinh, Databricks, Học máy, Hồ dữ liệu |
| **Bông tuyết** | Kho dữ liệu gốc trên nền tảng đám mây (nhà cung cấp bất khả tri) |
### Điều phối đường ống
| Công cụ | Ghi chú |
|------|-------|
| **Luồng khí Apache** | Tiêu chuẩn ngành; DAG dựa trên Python |
| **Quận trưởng** | Thay thế hiện đại với API sạch hơn |
| **Dao găm** | Điều phối tài sản làm trung tâm |
| **dbt** | Chuyển đổi dữ liệu SQL đầu tiên trong kho |
---

## Phân tích và thông minh kinh doanh
### So sánh các công cụ BI
| Công cụ | Loại | Sức mạnh |
|------|------|----------|
| **Hoạt cảnh** | Thương mại | Phân tích hình ảnh phong phú, kéo và thả |
| **Power BI** | Thương mại (Microsoft) | Tích hợp Deep Office/Azure |
| **Người nhìn** | Thương mại (Google) | Khám phá dữ liệu, lập mô hình LookML |
| **Siêu dữ liệu** | Mã nguồn mở | Dễ dàng thiết lập, có nguồn gốc SQL |
| **Siêu bộ** | Mã nguồn mở (Apache) | Có thể mở rộng, ưu tiên SQL |
### Nguyên tắc thiết kế bảng điều khiển
Trang tổng quan tốt tuân theo một số quy tắc: hiểu đối tượng của bạn, chọn hình ảnh trực quan phù hợp cho từng số liệu, sử dụng màu sắc một cách chiến lược (không mang tính trang trí), duy trì tỷ lệ nhất quán và bật tính tương tác (bộ lọc, thông tin chi tiết). Hiệu suất cũng quan trọng — không ai chờ đợi một bảng điều khiển chậm.
### Các hạng mục KPI phổ biến
| Danh mục | Ví dụ |
|----------|----------|
| **Tài chính** | Doanh thu, tỷ suất lợi nhuận, ROI, giá trị trọn đời của khách hàng |
| **Khách hàng** | Chi phí mua lại (CAC), tỷ lệ rời bỏ, NPS, điểm hài lòng |
| **Hoạt động** | Tỷ lệ hiệu quả, thời gian chu kỳ, tỷ lệ lỗi |
| **Tiếp thị** | Tỷ lệ chuyển đổi, tỷ lệ nhấp, ROAS, phân bổ |
| **Sản phẩm** | Người dùng hoạt động hàng ngày, mức độ tương tác, tỷ lệ giữ chân, áp dụng tính năng |
---

## Phân tích nâng cao
| Tiếp cận | Kỹ thuật | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Dự đoán** | Chuỗi thời gian (ARIMA, Prophet, LSTM), mô hình hóa rủi ro, dự đoán tỷ lệ rời bỏ | Dự báo giá trị tương lai |
| **Quy định** | Lập trình tuyến tính, mô phỏng Monte Carlo, thử nghiệm A/B, kẻ cướp nhiều nhánh | Quyết định tối ưu hóa |
| **Phân tích văn bản** | Mã thông báo, phân tích tình cảm, mô hình hóa chủ đề (LDA), NER, nhúng từ (Word2Vec, BERT) | Trích xuất thông tin chi tiết từ văn bản |
---

## Đạo đức và quản trị dữ liệu
### Quy định về quyền riêng tư
| Quy định | Phạm vi |
|----------|-------|
| **GDPR** | chủ đề dữ liệu của EU; quyền xóa, đồng ý, di chuyển dữ liệu |
| **CCPA** | người tiêu dùng California; từ chối bán dữ liệu |
| **HIPAA** | Dữ liệu chăm sóc sức khỏe của Hoa Kỳ; quy tắc bảo mật nghiêm ngặt |
### Thứ nguyên chất lượng dữ liệu
| Kích thước | Câu hỏi |
|----------||----------|
| **Độ chính xác** | Dữ liệu có chính xác không? |
| **Sự hoàn thiện** | Có thiếu thứ gì không? |
| **Tính nhất quán** | Các nguồn có đồng ý không? |
| **Tính kịp thời** | Nó có hiện tại không? |
| **Hiệu lực** | Nó có phù hợp với các định dạng mong đợi không? |
| **Tính độc đáo** | Có trùng lặp không? |
### Thiên kiến ​​và Công bằng
Xu hướng có thể xuất hiện ở bất kỳ giai đoạn nào: sai lệch lấy mẫu (dữ liệu không mang tính đại diện), sai lệch đo lường (công cụ có sai sót) hoặc sai lệch thuật toán (dự đoán phân biệt đối xử). Các chiến lược giảm thiểu bao gồm tiền xử lý (sửa dữ liệu), xử lý trong (hạn chế mô hình) và xử lý hậu kỳ (điều chỉnh đầu ra). Các số liệu công bằng như sự bình đẳng về nhân khẩu học và cơ hội bình đẳng giúp định lượng vấn đề.
---

## Con đường sự nghiệp
| Vai trò | Tập trung |
|------|-------|
| **Nhà phân tích dữ liệu** | Phân tích mô tả, bảng thông tin, báo cáo |
| **Nhà khoa học dữ liệu** | Mô hình thống kê, ML, phân tích nâng cao |
| **Kỹ sư ML** | Hệ thống ML sản xuất, triển khai mô hình, MLOps |
| **Kỹ sư dữ liệu** | Đường ống dữ liệu, cơ sở hạ tầng, ETL |
| **Trình quản lý phân tích** | Lãnh đạo nhóm, chiến lược, quản lý các bên liên quan |
| **Nhà khoa học nghiên cứu** | Thuật toán mới, ấn phẩm |
---

## Xu hướng mới nổi
- **AutoML**: Tạo đường dẫn và lựa chọn mô hình tự động.
- **MLOps**: Thực tiễn DevOps áp dụng cho quản lý vòng đời ML.
- **Cửa hàng tính năng**: Quản lý tính năng tập trung để tái sử dụng giữa các nhóm.
- **Lưới dữ liệu**: Kiến trúc dữ liệu phi tập trung, thuộc sở hữu của miền.
- **LLM và AI sáng tạo**: Các mô hình ngôn ngữ lớn chuyển đổi quy trình làm việc bằng văn bản, mã và hình ảnh.
- **Edge Analytics**: Xử lý dữ liệu trên thiết bị thay vì trên đám mây.
- **Suy luận nhân quả**: Vượt ra ngoài mối tương quan để hiểu nguyên nhân và kết quả thực tế.
- **Học tập liên kết**: Đào tạo các mô hình trên dữ liệu phi tập trung mà không cần di chuyển nó.
- **AI có trách nhiệm**: Đạo đức, khả năng giải thích và tính minh bạch trở thành yêu cầu tiêu chuẩn.