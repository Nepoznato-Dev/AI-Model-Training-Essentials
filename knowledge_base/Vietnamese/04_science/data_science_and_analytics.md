# Khoa học Dữ liệu và Phân tích

## Các Khái niệm Cốt lõi

### Khoa học Dữ liệu là gì?
Khoa học dữ liệu là một lĩnh vực liên ngành sử dụng các phương pháp khoa học, quy trình, thuật toán và hệ thống để trích xuất kiến thức và thông tin chi tiết từ dữ liệu có cấu trúc và không có cấu trúc. Nó kết hợp:
- **Thống kê**: Nền tảng toán học cho phân tích
- **Khoa học Máy tính**: Lập trình, thuật toán, cấu trúc dữ liệu
- **Chuyên môn Lĩnh vực**: Kiến thức về chủ đề
- **Trực quan hóa Dữ liệu**: Truyền đạt hiệu quả các phát hiện

### Các Loại Dữ liệu
- **Dữ liệu Có cấu trúc**: Được tổ chức thành hàng/cột (cơ sở dữ liệu, bảng tính)
- **Dữ liệu Không có cấu trúc**: Không có định dạng xác định trước (văn bản, hình ảnh, âm thanh, video)
- **Dữ liệu Bán cấu trúc**: Có một số tổ chức nhưng không cứng nhắc (JSON, XML, HTML)
- **Dữ liệu Chuỗi Thời gian**: Các điểm dữ liệu tuần tự được lập chỉ mục theo thứ tự thời gian
- **Dữ liệu Không gian**: Thông tin dựa trên địa lý/vị trí
- **Dữ liệu Đồ thị**: Các nút và cạnh biểu diễn mối quan hệ

### Quy trình Khoa học Dữ liệu (CRISP-DM)
1. **Hiểu biết Kinh doanh**: Xác định mục tiêu và yêu cầu
2. **Hiểu biết Dữ liệu**: Thu thập và khám phá dữ liệu ban đầu
3. **Chuẩn bị Dữ liệu**: Làm sạch, biến đổi và định dạng dữ liệu (80% công việc)
4. **Mô hình hóa**: Lựa chọn và áp dụng các kỹ thuật mô hình hóa
5. **Đánh giá**: Đánh giá hiệu suất mô hình so với mục tiêu
6. **Triển khai**: Triển khai mô hình trong môi trường sản xuất

## Nền tảng Thống kê

### Thống kê Mô tả
- **Các thước đo Xu hướng Trung tâm**: Trung bình, trung vị, mốt
- **Các thước đo Độ phân tán**: Khoảng biến thiên, phương sai, độ lệch chuẩn, khoảng tứ phân vị
- **Hình dạng Phân phối**: Độ bất đối xứng (skewness), độ nhọn (kurtosis)
- **Phần trăm và Tứ phân vị**: Vị trí trong phân phối

### Thống kê Suy luận
- **Kiểm định Giả thuyết**: Giả thuyết không, giả thuyết thay thế, giá trị p
- **Khoảng Tin cậy**: Dải giá trị có khả năng chứa tham số tổng thể
- **Ý nghĩa Thống kê**: Khả năng kết quả xảy ra do ngẫu nhiên
- **Sai số Loại I**: Dương tính giả (bác bỏ giả thuyết không đúng)
- **Sai số Loại II**: Âm tính giả (không bác bỏ giả thuyết không sai)
- **Lực kiểm định (Power)**: Xác suất bác bỏ chính xác giả thuyết không sai

### Các Phân phối Xác suất
- **Phân phối Chuẩn**: Đường cong chuông, trung bình = trung vị = mốt
- **Phân phối Nhị thức**: Kết quả thành công/thất bại
- **Phân phối Poisson**: Số lượng sự kiện trong khoảng cố định
- **Phân phối Đều**: Tất cả kết quả có khả năng như nhau
- **Phân phối Mũ**: Thời gian giữa các sự kiện
- **Phân phối t**: Cỡ mẫu nhỏ, phương sai tổng thể chưa biết
- **Phân phối Chi-Bình phương**: Phân tích dữ liệu phân loại

### Các Kiểm định Thống kê
- **Kiểm định t**: So sánh trung bình giữa hai nhóm
- **ANOVA**: So sánh trung bình trên nhiều nhóm
- **Kiểm định Chi-Bình phương**: Kiểm tra tính độc lập của các biến phân loại
- **Mann-Whitney U**: Phương án phi tham số thay thế cho kiểm định t
- **Tương quan Pearson**: Mối quan hệ tuyến tính giữa các biến liên tục
- **Tương quan Spearman**: Mối quan hệ đơn điệu (dựa trên hạng)
- **Kolmogorov-Smirnov**: So sánh các phân phối

## Thu thập và Lưu trữ Dữ liệu

### Các Nguồn Dữ liệu
- **Cơ sở Dữ liệu**: SQL, NoSQL, quan hệ, kho lưu trữ tài liệu
- **APIs**: REST, GraphQL, thu thập dữ liệu web
- **Tệp**: CSV, JSON, XML, Parquet, Avro
- **Dữ liệu Luồng**: Kafka, Kinesis, nguồn cấp dữ liệu thời gian thực
- **Khảo sát và Thí nghiệm**: Thu thập dữ liệu sơ cấp
- **Bộ Dữ liệu Công cộng**: Dữ liệu chính phủ, Kaggle, kho lưu trữ học thuật

### Kho dữ liệu (Data Warehousing)
- **ETL**: Quy trình Trích xuất, Biến đổi, Tải
- **Hồ Dữ liệu (Data Lake)**: Lưu trữ dữ liệu thô ở định dạng gốc
- **Kho Dữ liệu (Data Warehouse)**: Dữ liệu có cấu trúc, đã xử lý để phân tích
- **Mart Dữ liệu (Data Mart)**: Tập con của kho dữ liệu cho phòng ban cụ thể
- **OLAP**: Xử lý Phân tích Trực tuyến, truy vấn đa chiều
- **Sơ đồ Hình sao**: Các bảng sự kiện được bao quanh bởi các bảng chiều
- **Sơ đồ Bông tuyết**: Các bảng chiều được chuẩn hóa

### Các Loại Cơ sở Dữ liệu
- **Quan hệ (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Tài liệu**: MongoDB, CouchDB (tài liệu giống JSON)
- **Khóa-Giá trị**: Redis, DynamoDB (cặp khóa-giá trị đơn giản)
- **Họ Cột**: Cassandra, HBase (tối ưu hóa cho cột)
- **Đồ thị**: Neo4j, Amazon Neptune (nút và mối quan hệ)
- **Chuỗi Thời gian**: InfluxDB, TimescaleDB (dữ liệu có dấu thời gian)
- **Vector**: Pinecone, Milvus (lưu trữ embedding cho ML)

## Tiền xử lý Dữ liệu

### Làm sạch Dữ liệu
- **Giá trị Thiếu**: Imputation (trung bình, trung vị, mốt, dự đoán), xóa
- **Ngoại lai**: Phát hiện (IQR, điểm Z), xử lý (giới hạn, biến đổi)
- **Trùng lặp**: Nhận diện và loại bỏ
- **Không nhất quán**: Chuẩn hóa định dạng, sửa lỗi chính tả
- **Xác thực Dữ liệu**: Kiểm tra ràng buộc, phạm vi, kiểu

### Biến đổi Dữ liệu
- **Chuẩn hóa (Normalization)**: Thuỷ tỉ lệ về khoảng 0-1
- **Tiêu chuẩn hóa (Standardization)**: Chuẩn hóa điểm Z (trung bình=0, std=1)
- **Mã hóa**: One-hot, label, ordinal, target encoding
- **Phân nhóm (Binning)**: Nhóm các giá trị liên tục thành danh mục
- **Biến đổi Log**: Giảm độ bất đối xứng
- **Thuỷ tỉ lệ Đặc trưng**: Làm cho các đặc trưng có thể so sánh được

### Kỹ thuật Đặc trưng (Feature Engineering)
- **Tạo Đặc trưng**: Dẫn xuất các đặc trưng mới từ các đặc trưng hiện có
- **Lựa chọn Đặc trưng**: Chọn các đặc trưng phù hợp nhất
  - Phương pháp lọc (tương quan, chi-bình phương)
  - Phương pháp wrapper (loại bỏ đặc trưng đệ quy)
  - Phương pháp embedded (LASSO, tầm quan trọng dựa trên cây)
- **Giảm Chiều**: PCA, t-SNE, UMAP
- **Số hạng Tương tác**: Kết hợp các đặc trưng theo phép nhân
- **Đặc trưng Đa thức**: Tạo các số hạng bậc cao hơn

## Phân tích Dữ liệu Khám phá (EDA)

### Kỹ thuật EDA
- **Thống kê Tóm tắt**: Mô tả xu hướng trung tâm, độ phân tán, hình dạng
- **Phân tích Đơn biến**: Phân phối biến đơn lẻ
- **Phân tích Song biến**: Mối quan hệ giữa hai biến
- **Phân tích Đa biến**: Tương tác nhiều biến
- **Phân tích Tương quan**: Xác định mối quan hệ và đa cộng tuyến
- **Phân khúc**: Nhóm các quan sát tương tự

### Công cụ Trực quan hóa
- **Biểu đồ Histogram**: Phân phối của biến đơn
- **Biểu đồ Hộp (Box Plot)**: Tóm tắt năm số, phát hiện ngoại lai
- **Biểu đồ Phân tán (Scatter Plot)**: Mối quan hệ giữa hai biến liên tục
- **Biểu đồ Nhiệt (Heatmap)**: Ma trận tương quan, mật độ
- **Biểu đồ Cột**: So sánh phân loại
- **Biểu đồ Đường**: Xu hướng theo thời gian
- **Biểu đồ Violin**: Mật độ phân phối với các yếu tố biểu đồ hộp
- **Biểu đồ Pair**: Nhiều biểu đồ phân tán cho các cặp biến

### Thư viện Python cho EDA
- **pandas**: Thao tác và phân tích dữ liệu
- **numpy**: Tính toán số
- **matplotlib**: Vẽ đồ thị cơ bản
- **seaborn**: Trực quan hóa thống kê
- **plotly**: Trực quan hóa tương tác
- **scipy**: Tính toán khoa học và thống kê

## Học máy trong Khoa học Dữ liệu

### Học có Giám sát
- **Hồi quy**: Dự đoán giá trị liên tục
  - Hồi quy Tuyến tính
  - Hồi quy Đa thức
  - Ridge/LASSO/Elastic Net
  - Cây Quyết định Hồi quy
  - Rừng Ngẫu nhiên Hồi quy
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Phân loại**: Dự đoán nhãn phân loại
  - Hồi quy Logistic
  - k-Láng giềng Gần nhất
  - Naive Bayes
  - Máy Vectơ Hỗ trợ
  - Cây Quyết định
  - Rừng Ngẫu nhiên
  - Gradient Boosting
  - Mạng Nơ-ron

### Học không Giám sát
- **Phân cụm**: Nhóm các quan sát tương tự
  - k-Means
  - Phân cụm Phân cấp
  - DBSCAN (dựa trên mật độ)
  - Mô hình Hỗn hợp Gaussian
  - Phân cụm Phổ
  
- **Giảm Chiều**: Giảm số lượng đặc trưng
  - Phân tích Thành phần Chính (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Luật Kết hợp**: Tìm các mục cùng xuất hiện
  - Thuật toán Apriori
  - FP-Growth

### Đánh giá Mô hình
- **Chỉ số Phân loại**: Độ chính xác, precision, recall, F1-score, ROC-AUC, ma trận nhầm lẫn
- **Chỉ số Hồi quy**: MAE, MSE, RMSE, R², R² Hiệu chỉnh
- **Kiểm định Chéo**: k-fold, stratified, leave-one-out, chia chuỗi thời gian
- **Điều chỉnh Siêu tham số**: Tìm kiếm lưới, tìm kiếm ngẫu nhiên, tối ưu hóa Bayesian
- **Đường cong Học tập**: Chẩn đoán sự đánh đổi bias-variance

## Công nghệ Dữ liệu Lớn

### Framework Tính toán Phân tán
- **Apache Hadoop**: MapReduce, HDFS (Hệ thống Tệp Phân tán Hadoop)
- **Apache Spark**: Xử lý trong bộ nhớ, nhanh hơn Hadoop
  - Spark SQL: Xử lý dữ liệu có cấu trúc
  - Spark Streaming: Dữ liệu thời gian thực
  - MLlib: Thư viện học máy
  - GraphX: Xử lý đồ thị
- **Apache Flink**: Xử lý luồng với độ trễ thấp
- **Apache Beam**: Batch và streaming thống nhất

### Nền tảng Đám mây
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Kho dữ liệu đám mây

### Công cụ Pipeline Dữ liệu
- **Apache Airflow**: Điều phối quy trình làm việc
- **Luigi**: Quản lý pipeline (Spotify)
- **Prefect**: Điều phối quy trình làm việc hiện đại
- **Dagster**: Bộ điều phối dữ liệu với trọng tâm tài sản
- **dbt**: Biến đổi dữ liệu trong kho dữ liệu

## Business Intelligence và Phân tích

### Công cụ BI
- **Tableau**: Nền tảng phân tích trực quan
- **Power BI**: Phân tích kinh doanh Microsoft
- **Looker**: Khám phá dữ liệu và thông tin chi tiết (Google)
- **Qlik Sense**: Phân tích liên kết
- **Metabase**: BI mã nguồn mở
- **Superset**: BI mã nguồn mở Apache

### Nguyên tắc Thiết kế Dashboard
- **Hiểu Đối tượng của bạn**: Tùy chỉnh theo nhu cầu người dùng
- **Chọn Trực quan hóa Phù hợp**: Ghép biểu đồ với loại dữ liệu
- **Sử dụng Màu chiến lược**: Làm nổi bật thông tin quan trọng
- **Duy trì Tính nhất quán**: Chuẩn hóa định dạng và thang đo
- **Cho phép Tương tác**: Bộ lọc, drill-downs, tooltips
- **Tối ưu Hiệu suất**: Tải nhanh, truy vấn hiệu quả
- **Cân nhắc Di động**: Thiết kế đáp ứng

### Chỉ số Hiệu suất Chính (KPIs)
- **Tài chính**: Doanh thu, biên lợi nhuận, ROI, giá trị vòng đời khách hàng
- **Khách hàng**: Chi phí mua lại, tỷ lệ rời bỏ, điểm hài lòng, NPS
- **Vận hành**: Tỷ lệ hiệu quả, thời gian chu kỳ, tỷ lệ lỗi
- **Marketing**: Tỷ lệ chuyển đổi, tỷ lệ nhấp, phân bổ
- **Sản phẩm**: Người dùng hoạt động, tương tác, giữ chân, áp dụng tính năng

## Phân tích Nâng cao

### Phân tích Dự đoán
- **Dự báo**: Dự đoán chuỗi thời gian (ARIMA, Prophet, LSTM)
- **Mô hình hóa Rủi ro**: Chấm điểm tín dụng, phát hiện gian lận, bảo hiểm
- **Phân tích Khách hàng**: Dự đoán rời bỏ, mô hình hóa khuynh hướng
- **Dự báo Nhu cầu**: Tối ưu hóa tồn kho, chuỗi cung ứng
- **Dự đoán Bảo trì**: Dự đoán hỏng hóc thiết bị

### Phân tích Đề xuất
- **Tối ưu hóa**: Quy hoạch tuyến tính, quy hoạch nguyên
- **Mô phỏng**: Phương pháp Monte Carlo, mô phỏng sự kiện rời rạc
- **Phân tích Quyết định**: Cây quyết định, sơ đồ ảnh hưởng
- **Kiểm định A/B**: Thiết kế thử nghiệm, ý nghĩa thống kê
- **Multi-Armed Bandits**: Thử nghiệm thích ứng

### Phân tích Văn bản (NLP)
- **Tiền xử lý Văn bản**: Tokenization, stemming, lemmatization
- **Phân tích Cảm xúc**: Phân loại tích cực/tiêu cực/trung tính
- **Mô hình hóa Chủ đề**: LDA, NMF để khám phá chủ đề
- **Nhận diện Thực thể Có tên**: Xác định người, địa điểm, tổ chức
- **Phân loại Văn bản**: Phát hiện spam, phân loại
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Đạo đức Dữ liệu và Quản trị

### Quyền riêng tư Dữ liệu
- **GDPR**: Quy định Bảo vệ Dữ liệu Chung của EU
- **CCPA**: Đạo luật Quyền riêng tư Người tiêu dùng California
- **HIPAA**: Đạo luật Portability và Accountability Bảo hiểm Y tế (chăm sóc sức khỏe Hoa Kỳ)
- **Ẩn danh**: Xóa thông tin nhận dạng cá nhân
- **Quyền riêng tư Vi sai**: Thêm nhiễu để bảo vệ cá nhân
- **Quản lý Sự đồng ý**: Cơ chế opt-in/opt-out

### Chất lượng Dữ liệu
- **Độ chính xác**: Tính đúng đắn của dữ liệu
- **Tính đầy đủ**: Tất cả dữ liệu cần thiết đều có mặt
- **Tính nhất quán**: Không có mâu thuẫn giữa các nguồn
- **Tính kịp thời**: Dữ liệu có sẵn khi cần
- **Tính hợp lệ**: Tuân thủ các quy tắc xác định
- **Tính duy nhất**: Không trùng lặp

### Thiên kiến và Công bằng
- **Thiên kiến Lấy mẫu**: Thu thập dữ liệu không đại diện
- **Thiên kiến Đo lường**: Công cụ thu thập dữ liệu bị lỗi
- **Thiên kiến Thuật toán**: Dự đoán mô hình phân biệt đối xử
- **Chỉ số Công bằng**: Ngang bằng nhân khẩu học, cơ hội bình đẳng
- **Giảm thiểu Thiên kiến**: Tiền xử lý, trong xử lý, hậu xử lý

### Khung Quản trị Dữ liệu
- **Giám sát Dữ liệu**: Trách nhiệm đối với tài sản dữ liệu
- **Quản lý Siêu dữ liệu**: Tài liệu về dữ liệu
- **Nguồn gốc Dữ liệu**: Theo dõi luồng dữ liệu và biến đổi
- **Kiểm soát Truy cập**: Quyền dựa trên vai trò
- **Nhật ký Kiểm toán**: Ghi nhật ký truy cập và thay đổi dữ liệu
- **Tuân thủ**: Tuân thủ quy định

## Con đường Sự nghiệp trong Khoa học Dữ liệu

### Vai trò
- **Nhà Phân tích Dữ liệu**: Tập trung vào phân tích mô tả, dashboard, báo cáo
- **Nhà Khoa học Dữ liệu**: Mô hình hóa thống kê, học máy, phân tích nâng cao
- **Kỹ sư ML**: Hệ thống ML sản xuất, triển khai mô hình, MLOps
- **Kỹ sư Dữ liệu**: Pipeline dữ liệu, cơ sở hạ tầng, quy trình ETL
- **Quản lý Phân tích**: Lãnh đạo nhóm, chiến lược, quản lý bên liên quan
- **Nhà phát triển BI**: Tạo dashboard, phát triển báo cáo
- **Nhà Khoa học Nghiên cứu**: Thuật toán mới, ấn phẩm, nghiên cứu nâng cao

### Ma trận Kỹ năng
- **Kỹ thuật**: Python/R, SQL, thống kê, framework ML, nền tảng đám mây
- **Phân tích**: Giải quyết vấn đề, tư duy phản biện, thiết kế thử nghiệm
- **Giao tiếp**: Kể chuyện, trực quan hóa, kỹ năng trình bày
- **Kinh doanh**: Kiến thức lĩnh vực, quản lý bên liên quan, phân tích ROI
- **Công cụ**: Git, Jupyter, Docker, CI/CD, kiểm soát phiên bản cho mô hình

## Xu hướng Mới nổi

### Phát triển Hiện tại
- **AutoML**: Tự động hóa tạo pipeline học máy
- **MLOps**: Thực hành DevOps cho học máy
- **Kho Đặc trưng**: Quản lý đặc trưng tập trung
- **Data Mesh**: Kiến trúc dữ liệu phi tập trung
- **LLM và AI Tạo sinh**: Mô hình ngôn ngữ lớn, tạo nội dung
- **Phân tích Biên**: Xử lý dữ liệu tại thiết bị nguồn
- **Phân tích Thời gian Thực**: Phân tích dữ liệu luồng
- **Phân tích Tăng cường**: Chuẩn bị dữ liệu và thông tin chi tiết hỗ trợ bởi AI

### Hướng đi Tương lai
- **Học máy Lượng tử**: Tính toán lượng tử cho ML
- **Học Liên bang**: Huấn luyện mô hình trên dữ liệu phi tập trung
- **Suy luận Nhân quả**: Vượt qua tương quan đến nhân quả
- **AI Có trách nhiệm**: Đạo đức, khả năng giải thích, minh bạch
- **Data Fabric**: Quản lý dữ liệu tích hợp trên các môi trường

