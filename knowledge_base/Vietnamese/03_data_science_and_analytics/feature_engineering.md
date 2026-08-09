---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Kỹ thuật tính năng
Kỹ thuật tính năng là quá trình chuyển đổi dữ liệu thô thành các biểu diễn giúp mô hình học máy hiệu quả hơn. Đây thường được mô tả là bước quan trọng nhất trong quy trình ML — các tính năng bạn cung cấp cho mô hình quan trọng hơn thuật toán bạn chọn. Một mô hình đơn giản với các tính năng được thiết kế tốt thường sẽ hoạt động tốt hơn một mô hình phức tạp có đầu vào thô, chưa được xử lý. Nghệ thuật nằm ở việc hiểu rõ cả miền và dữ liệu để tạo ra các tín hiệu mà mô hình có thể học hỏi.
---

## Tại sao kỹ thuật tính năng lại quan trọng
| Yếu tố | Tác động |
|--------|--------|
| **Chất lượng tín hiệu** | Các tính năng tốt hơn = mô hình rõ ràng hơn để mô hình học hỏi |
| **Mô hình đơn giản** | Các tính năng tốt cho phép các mô hình đơn giản hơn hoạt động tốt; ít cần kiến ​​trúc phức tạp |
| **Tốc độ luyện tập** | Các tính năng có liên quan, có quy mô tốt sẽ hội tụ nhanh hơn |
| **Tổng quát hóa** | Các tính năng được thông tin về miền giúp các mô hình hoạt động trên dữ liệu chưa được nhìn thấy |
| **Có thể hiểu được** | Các đặc điểm có ý nghĩa dễ giải thích hơn cho các bên liên quan |
---

## Các loại chuyển đổi tính năng
### Phép biến đổi số
| Chuyển đổi | Công thức / Mô tả | Khi nào nên sử dụng |
|--------------|----------------------|-------------|
| **Biến đổi nhật ký** | log(x) hoặc log(x + 1) | Phân bố lệch phải; giá trị tiền tệ |
| **Căn bậc hai** | sqrt(x) | Độ lệch vừa phải; đếm dữ liệu |
| **Box-Cox** | Biến đổi tham số tìm ra phép biến đổi công suất tốt nhất | Làm cho dữ liệu được phân phối bình thường hơn |
| **Yeo-Johnson** | Giống như Box-Cox nhưng xử lý các giá trị âm | Dữ liệu lệch có giá trị âm |
| **Tiêu chuẩn hóa** | (x - trung bình) / std | Các tính năng với quy mô khác nhau; thuật toán giả định tính chuẩn |
| **Tỷ lệ tối thiểu-tối đa** | (x - phút) / (tối đa - phút) | Giới hạn các tính năng thành [0, 1]; giá trị pixel hình ảnh |
| **Mở rộng quy mô mạnh mẽ** | (x - trung vị) / IQR | Dữ liệu có giá trị ngoại lệ |
| **Nhóm** | Chuyển đổi liên tục sang phân loại | mối quan hệ phi tuyến tính; cây quyết định |
| **Tính chất đa thức** | x², x³, x₁×x₂ | Nắm bắt các mối quan hệ phi tuyến tính trong các mô hình tuyến tính |
### Mã hóa phân loại
| Mã hóa | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Mã hóa một lần** | Tạo cột nhị phân cho từng danh mục | Các danh mục có số lượng thẻ thấp; mô hình dựa trên cây xử lý nguyên bản |
| **Mã hóa nhãn** | Gán số nguyên cho từng danh mục | Các loại thứ tự; mô hình dựa trên cây |
| **Mã hóa mục tiêu** | Thay thế danh mục bằng giá trị trung bình của biến mục tiêu | Các hạng mục có số lượng thẻ cao; tránh trang bị quá mức bằng cách làm mịn |
| **Mã hóa tần số** | Thay thế danh mục bằng số lượng hoặc tần suất của nó | Khi tần số mang tính thông tin |
| **Mã hóa nhị phân** | Chuyển đổi các danh mục được mã hóa số nguyên thành chữ số nhị phân | Số lượng thẻ cao; giảm chiều so với một nóng |
| **Nhúng** | Tìm hiểu biểu diễn vector dày đặc | Cardinality rất cao; NLP; hệ thống gợi ý |
| **Mã hóa băm** | Băm các danh mục thành một số tính năng cố định | Cardinality rất cao; học trực tuyến |
### Tính năng ngày và giờ
| Tính năng | Mô tả |
|----------|-------------|
| **Giờ trong ngày** | Chụp các mẫu hàng ngày (giờ cao điểm, ban đêm) |
| **Ngày trong tuần** | Hiệu ứng ngày trong tuần và cuối tuần |
| **Tháng/quý** | Mẫu theo mùa |
| **Là cuối tuần** | Cờ nhị phân cho cuối tuần |
| **Là kỳ nghỉ** | Cờ nhị phân cho ngày lễ |
| **Thời gian kể từ sự kiện** | Số ngày kể từ lần mua cuối cùng; giờ kể từ lần đăng nhập cuối cùng |
| **Mã hóa theo chu kỳ** | sin(2π × giờ / 24), cos(2π × giờ / 24) — bảo toàn tính chất tuần hoàn của thời gian |
---

## Xử lý các giá trị bị thiếu
| Chiến lược | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Thả hàng** | Xóa các hàng có giá trị bị thiếu | Dữ liệu bị thiếu chỉ là một phần nhỏ; MCAR (thiếu hoàn toàn ngẫu nhiên) |
| **Thả cột** | Xóa các tính năng có quá nhiều giá trị bị thiếu | Tính năng hầu như bị thiếu; không quan trọng |
| **Sự cắt bỏ trung bình/trung bình** | Điền giá trị trung bình hoặc trung vị của đối tượng địa lý | Đơn giản; duy trì giá trị trung bình nhưng làm giảm phương sai |
| **Chế độ quy định** | Điền vào phân loại với giá trị thường xuyên nhất | Tính năng phân loại |
| **Cắt bỏ KNN** | Sử dụng k-hàng xóm gần nhất để ước tính giá trị còn thiếu | Khi các trường hợp tương tự giúp dự đoán giá trị còn thiếu |
| **Tính toán dựa trên mô hình** | Huấn luyện mô hình để dự đoán các giá trị còn thiếu | Chính xác hơn; tính toán đắt tiền |
| **Thiếu chỉ báo** | Thêm một cột nhị phân gắn cờ thiếu | Khi sự thiếu sót chính là thông tin |
| **Nội suy** | Điền các giá trị nội suy (tuyến tính, spline) | Chuỗi thời gian; dữ liệu đặt hàng |
---

## Lựa chọn tính năng
### Phương pháp lọc
| Phương pháp | Mô tả |
|--------|-------------|
| **Tương quan** | Loại bỏ các tính năng có mối tương quan cao với nhau |
| **Ngưỡng chênh lệch** | Loại bỏ các tính năng có phương sai gần như bằng 0 |
| **Thông tin lẫn nhau** | Đo lường thông tin mà mỗi tính năng cung cấp về mục tiêu |
| **Chi bình phương** | Kiểm tra tính độc lập giữa các tính năng phân loại và mục tiêu |
| **Kiểm tra F ANOVA** | Kiểm tra xem ý nghĩa của tính năng số có khác nhau giữa các lớp mục tiêu hay không |
### Phương thức bao bọc
| Phương pháp | Mô tả |
|--------|-------------|
| **Lựa chọn chuyển tiếp** | Bắt đầu trống rỗng; thêm từng tính năng tốt nhất |
| **Loại bỏ ngược** | Bắt đầu với tất cả; loại bỏ từng tính năng tồi tệ nhất |
| **Loại bỏ tính năng đệ quy (RFE)** | Mô hình đào tạo liên tục; loại bỏ các tính năng ít quan trọng nhất |
### Phương thức nhúng
| Phương pháp | Mô tả |
|--------|-------------|
| **Chính quy hóa L1 (Lasso)** | Thu gọn trọng số tính năng không liên quan về 0 |
| **Tầm quan trọng của cây** | Sử dụng tầm quan trọng của tính năng từ mô hình cây |
| **Giá trị SHAP** | Đo lường sự đóng góp của từng tính năng vào dự đoán |
---

## Kỹ thuật tính năng dành riêng cho miền
### Tính năng văn bản
| Tính năng | Mô tả |
|----------|-------------|
| **TF-IDF** | Tần suất thuật ngữ được tính theo tần số tài liệu nghịch đảo |
| **Nhúng từ** | Các vectơ dày đặc nắm bắt ý nghĩa ngữ nghĩa (Word2Vec, GloVe) |
| **N-gram ký tự** | Nắm bắt các mẫu từ phụ; hữu ích cho lỗi chính tả và hình thái |
| **Thống kê văn bản** | Chiều dài; số từ; số câu; độ dài từ trung bình |
| **Điểm dễ đọc** | Flesch-Kincaid; Chỉ số sương mù bắn súng |
### Tính năng của chuỗi thời gian
| Tính năng | Mô tả |
|----------|-------------|
| **Tính năng trễ** | Giá trị trước đó: y(t-1), y(t-7), y(t-30) |
| **Số liệu thống kê luân phiên** | Giá trị trung bình, tiêu chuẩn, tối thiểu, tối đa trên một cửa sổ |
| **Sự khác biệt** | y(t) - y(t-1); nắm bắt xu hướng |
| **Sự khác biệt theo mùa** | y(t) - y(t-12) cho dữ liệu hàng tháng có tính thời vụ hàng năm |
| **Thuật ngữ Fourier** | Thuật ngữ sin và cosin cho các mẫu theo mùa |
### Tính năng hình ảnh (Pre-Deep Learning)
| Tính năng | Mô tả |
|----------|-------------|
| **HOG** (Biểu đồ độ dốc định hướng) | Phân phối hướng cạnh |
| **LBP** (Mẫu nhị phân cục bộ) | Mô tả kết cấu |
| **SIFT** (Chuyển đổi tính năng bất biến tỷ lệ) | Mô tả điểm chính |
| **Biểu đồ màu** | Phân bổ màu sắc trong ảnh |
---

## Các phương pháp hay nhất về kỹ thuật tính năng
| Thực hành | Mô tả |
|----------|-------------|
| **Tránh rò rỉ dữ liệu** | Không bao giờ sử dụng thông tin từ tương lai hoặc bộ thử nghiệm để tạo tính năng |
| **Ghi lại mọi thứ** | Ghi lại những phép biến đổi nào đã được áp dụng và tại sao |
| **Phiên bản các tính năng của bạn** | Theo dõi các thay đổi về tính năng cùng với các thay đổi về kiểu máy |
| **Xác thực có và không có** | Kiểm tra xem tính năng mới có thực sự cải thiện hiệu suất của mô hình hay không |
| **Giữ cho nó có thể tái tạo** | Quy trình kỹ thuật tính năng phải mang tính xác định và có thể lặp lại |
| **Theo dõi tính năng trôi dạt** | Phân phối tính năng có thể thay đổi theo thời gian; theo dõi và đào tạo lại |
---

## Bản tóm tắt
Kỹ thuật tính năng là nơi kiến ​​thức miền gặp máy học. Đó là quá trình chuyển đổi dữ liệu thô - lộn xộn, không đầy đủ, nhiều chiều - thành các biểu diễn rõ ràng, giàu thông tin mà các mô hình có thể học hỏi. Các phép biến đổi số xử lý độ lệch và tỷ lệ. Mã hóa phân loại chuyển đổi nhãn thành số mà mô hình có thể sử dụng. Các tính năng ngày nắm bắt các mẫu thời gian. Chiến lược giá trị thiếu xử lý dữ liệu không đầy đủ. Lựa chọn tính năng sẽ loại bỏ tiếng ồn và sự dư thừa. Các kỹ sư tính năng giỏi nhất suy nghĩ giống như thám tử: họ hỏi những tín hiệu nào sẽ có trong dữ liệu, những tín hiệu đó có thể bị ẩn ở đâu và cách trích xuất chúng theo cách trung thực (không rò rỉ dữ liệu), có thể tái tạo và thay đổi mạnh mẽ theo thời gian.