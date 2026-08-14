---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Chuỗi thời gian và dự báo
Dữ liệu chuỗi thời gian là bất kỳ dữ liệu nào được thu thập theo thời gian: giá cổ phiếu, chỉ số nhiệt độ, lưu lượng truy cập trang web, số liệu bán hàng, máy đo nhịp tim, mức tiêu thụ năng lượng. Dự báo có nghĩa là dự đoán các giá trị trong tương lai dựa trên các mẫu trong quá khứ. Đây là một trong những ứng dụng có giá trị thực tế nhất của khoa học dữ liệu — và là một trong những ứng dụng khó nhất, bởi vì tương lai thực sự không chắc chắn và chuỗi thời gian trong thế giới thực đầy rẫy những nhiễu loạn, tính thời vụ và sự phá vỡ cấu trúc.
---

## Đặc điểm của chuỗi thời gian
| Thành phần | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Xu hướng** | Tăng hoặc giảm dài hạn | Nhiệt độ toàn cầu tăng trong nhiều thập kỷ |
| **Tính thời vụ** | Các mẫu đều đặn, có thể dự đoán được ở những khoảng thời gian cố định | Doanh số bán lẻ tăng đột biến vào tháng 12 |
| **Tính chu kỳ** | Biến động theo khoảng thời gian không cố định (thường là kinh tế) | Suy thoái cứ sau 5-10 năm |
| **Tiếng ồn (dư lượng)** | Biến thể ngẫu nhiên không thể giải thích được | Biến động giá cổ phiếu hàng ngày |
| **Tự tương quan** | Giá trị hiện tại phụ thuộc vào giá trị trong quá khứ | Nhiệt độ hôm nay giống hôm qua |
###Tính cố định
Một chuỗi thời gian **đứng yên** nếu các thuộc tính thống kê (trung bình, phương sai) của nó không thay đổi theo thời gian. Hầu hết các phương pháp dự báo đều giả định tính dừng.
| Kiểm tra | Mục đích |
|------|----------|
| **Tăng cường Dickey-Fuller (ADF)** | Kiểm tra xem có tồn tại nghiệm đơn vị hay không (không cố định) |
| **Kiểm tra KPSS** | Kiểm tra xem chuỗi có xu hướng dừng hay không |
| Chuyển đổi | Khi nào nên sử dụng |
|---------------|-------------|
| **Khác biệt** | Xóa xu hướng: y'(t) = y(t) - y(t-1) |
| **Biến đổi nhật ký** | Ổn định phương sai (để tăng trưởng theo cấp số nhân) |
| **Sự khác biệt theo mùa** | Loại bỏ tính thời vụ: y'(t) = y(t) - y(t-s) trong đó s là độ dài mùa |
---

## Phương pháp dự báo cổ điển
### Đường trung bình động
| Phương pháp | Mô tả | Tốt nhất cho |
|--------|-------------|----------|
| **Đường trung bình động đơn giản (SMA)** | Trung bình của N quan sát cuối cùng | Làm mịn dữ liệu nhiễu |
| **Trung bình trượt có trọng số** | Những quan sát gần đây hơn có trọng số cao hơn | Khi dữ liệu gần đây quan trọng hơn |
| **Đường trung bình động hàm mũ (EMA)** | Trọng lượng giảm theo cấp số nhân | Theo dõi xu hướng với độ trễ ít hơn |
### Làm mịn theo cấp số nhân
| Phương pháp | Linh kiện | Trường hợp sử dụng |
|--------|-------------|----------|
| **Đơn giản (SES)** | Chỉ cấp độ | Không có xu hướng, không có tính thời vụ |
| **Holt's (Đôi)** | Cấp độ + xu hướng | Dữ liệu có xu hướng nhưng không có tính thời vụ |
| **Holt-Winters (Ba)** | Cấp độ + xu hướng + tính thời vụ | Dữ liệu có cả xu hướng và tính thời vụ |
### ARIMA và các biến thể
ARIMA (Trung bình di chuyển tích hợp tự động hồi quy) là công cụ dự báo chuỗi thời gian cổ điển.
| Thành phần | Ý nghĩa | Tham số |
|----------||----------|----------|
| **AR (p)** | Hồi quy các giá trị p trước đó | Sử dụng bao nhiêu giá trị trong quá khứ |
| **Tôi (d)** | Số bước khác nhau để tạo ra sự cố định | Bao nhiêu lần chênh lệch |
| **MA (q)** | Lập mô hình lỗi dưới dạng sự kết hợp của các lỗi trong quá khứ | Sử dụng bao nhiêu lỗi trong quá khứ |
| Biến thể | Gia hạn | Trường hợp sử dụng |
|----------|-------------|----------|
| **SARIMA** | Thêm các thành phần theo mùa (P, D, Q, s) | Dữ liệu có tính thời vụ mạnh mẽ |
| **ARIMAX** | Thêm các biến bên ngoài | Khi bạn biết về các sự kiện sắp tới |
| **VAR** | ARIMA đa biến; nhiều chuỗi phụ thuộc lẫn nhau | Khi các biến ảnh hưởng lẫn nhau |
---

## Phương pháp tiếp cận ML hiện đại
### Mô hình dựa trên LSTM và RNN
| Người mẫu | Kiến trúc | Lợi thế |
|-------|-------------|----------|
| **LSTM** | Mạng bộ nhớ ngắn hạn dài | Nắm bắt sự phụ thuộc thời gian tầm xa |
| **GRU** | Đơn vị định kỳ có kiểm soát (LSTM đơn giản hơn) | Đào tạo nhanh hơn; hiệu suất tương tự |
| **Seq2Seq** | Bộ mã hóa-giải mã cho chuỗi thời gian | Độ dài đầu vào/đầu ra linh hoạt |
| **Mạng tích chập tạm thời (TCN)** | Nhân quả giãn nở | Đào tạo song song; trường tiếp nhận dài |
### Tiên tri (Meta)
Một công cụ dự báo thực tế được thiết kế cho chuỗi thời gian kinh doanh.
| Tính năng | Mô tả |
|----------|-------------|
| **Phân hủy** | Xu hướng + tính thời vụ + ngày lễ |
| **Linh hoạt** | Xử lý dữ liệu bị thiếu, ngoại lệ và phá vỡ cấu trúc |
| **Có thể hiểu được** | Các thành phần có thể đọc được |
| **Tự động** | Mặc định hợp lý; yêu cầu điều chỉnh tối thiểu |
| Sức mạnh | Hạn chế |
|----------|-------------|
| Tuyệt vời cho các số liệu kinh doanh (doanh số, người dùng) | Không lý tưởng cho dữ liệu tần số rất cao |
| Xử lý các ngày lễ và sự kiện đặc biệt | Giả sử tính thời vụ cộng hoặc nhân |
| Mạnh mẽ đến mức ngoại lệ | Kém chính xác hơn học sâu đối với các mẫu phức tạp |
### Mô hình dựa trên máy biến áp
| Người mẫu | Tính năng chính |
|-------|-------------|
| **Người cung cấp thông tin** | Vấn đềSự chú ý thưa thớt đối với các chuỗi dài |
| **Tự động hóa** | Cơ chế tự tương quan để phân tách chuỗi |
| **PatchTST** | Vá chuỗi thời gian; kênh độc lập |
| **TimeFM** (Google) | Mô hình nền tảng cho chuỗi thời gian; được đào tạo trước về dữ liệu đa dạng |
| **Chronos** (Amazon) | Chuỗi thời gian mã hóa; sử dụng kiến ​​trúc kiểu LLM |
---

## Phát hiện bất thường trong chuỗi thời gian
Phát hiện các mẫu bất thường đi chệch khỏi hành vi dự kiến.
| Phương pháp | Tiếp cận | Trường hợp sử dụng |
|--------|----------|----------|
| **Thống kê** | Điểm Z, IQR, biểu đồ kiểm soát | Đơn giản, dễ hiểu |
| **Rừng Cô Lập** | Dựa trên cây; cô lập các dị thường bằng cách phân vùng ngẫu nhiên | Phát hiện dị thường đa biến |
| **LOF** (Yếu tố ngoại lệ cục bộ) | Dựa trên mật độ; so sánh mật độ địa phương với hàng xóm | Khi dị thường ở vùng mật độ thấp |
| **Bộ mã hóa tự động** | Lỗi tái thiết; lỗi cao = bất thường | Các mẫu phức tạp, phi tuyến tính |
| **Dựa trên LSTM** | Dự đoán bước tiếp theo; lỗi dự đoán lớn = dị thường | Sự bất thường tuần tự |
### Ứng dụng
| Tên miền | Ý nghĩa của sự bất thường |
|--------|-------------------|
| **Tài chính** | Lừa đảo, sụp đổ thị trường, sụp đổ chớp nhoáng |
| **Chăm sóc sức khỏe** | Nhịp tim bất thường, khởi phát cơn động kinh |
| **Sản xuất** | Lỗi thiết bị, lỗi chất lượng |
| **An ninh mạng** | Các nỗ lực xâm nhập, tấn công DDoS |
| **Cơ sở hạ tầng** | Server quá tải, lỗi mạng |
---

## Số liệu đánh giá
| Số liệu | Công thức (khái niệm) | Khi nào nên sử dụng |
|--------|----------------------|-------------|
| **MAE** (Lỗi tuyệt đối trung bình) | Trung bình sai số tuyệt đối | Có thể giải thích được; cùng đơn vị với dữ liệu |
| **RMSE** (Lỗi bình phương trung bình gốc) | Căn bậc hai của sai số bình phương trung bình | Phạt lỗi lớn hơn |
| **MAPE** (Lỗi phần trăm tuyệt đối trung bình) | Trung bình các lỗi phần trăm tuyệt đối | Khi lỗi tương đối quan trọng |
| **SMAPE** (MAPE đối xứng) | Phiên bản đối xứng của MAPE | Xử lý các giá trị gần 0 tốt hơn |
| **MASE** (Lỗi tỷ lệ tuyệt đối trung bình) | MAE so với một dự báo ngây thơ | So sánh giữa các dòng khác nhau |
---

## Quy trình làm việc thực tế
| Bước | Mô tả |
|------|-------------|
| **1. Khám phá** | Vẽ chuỗi; xác định xu hướng, tính thời vụ, các ngoại lệ |
| **2. Phân hủy** | Tách thành các thành phần xu hướng, theo mùa và dư lượng |
| **3. Văn phòng phẩm** | Áp dụng sai phân hoặc biến đổi nếu cần |
| **4. Tách** | Phân chia dựa trên thời gian (không bao giờ phân chia ngẫu nhiên cho chuỗi thời gian) |
| **5. Đường cơ sở** | Bắt đầu với một dự báo ngây thơ (giá trị cuối cùng, ngây thơ theo mùa) |
| **6. Người mẫu** | Hãy thử các phương pháp cổ điển (ARIMA, Prophet), sau đó là các phương pháp ML |
| **7. Đánh giá** | Sử dụng số liệu thích hợp; so sánh với đường cơ sở |
| **8. Lặp lại** | Thêm tính năng, thử các mô hình khác nhau, điều chỉnh siêu tham số |
---

## Công cụ và Thư viện
| Công cụ | Mục đích |
|------|----------|
| **mô hình thống kê** | Chuỗi thời gian cổ điển (ARIMA, ETS, phân rã) |
| **Nhà tiên tri** (Meta) | Dự báo chuỗi thời gian kinh doanh |
| **sktime** | Giao diện ML hợp nhất cho chuỗi thời gian |
| **Phi tiêu** | Thư viện dự báo toàn diện (cổ điển + học sâu) |
| **GluonTS** (Amazon) | Mô hình chuỗi thời gian xác suất |
| **Tiên tri thần kinh** | Tiên tri với các thành phần mạng lưới thần kinh |
| **tsfresh** | Trích xuất tính năng chuỗi thời gian tự động |
| **gấu trúc** | Thao tác và lấy mẫu lại chuỗi thời gian |
---

## Bản tóm tắt
Dự báo chuỗi thời gian kết hợp thống kê cổ điển với học máy hiện đại. Các phương pháp cổ điển (ARIMA, làm mịn hàm mũ, Tiên tri) có thể hiểu được, nhanh chóng và thường chính xác. Các phương pháp học sâu (LSTM, Transformers) nắm bắt các mẫu phức tạp nhưng yêu cầu nhiều dữ liệu và điều chỉnh hơn. Các nguyên tắc chính vẫn giữ nguyên bất kể phương pháp nào: hiểu cấu trúc dữ liệu của bạn (xu hướng, tính thời vụ, độ nhiễu), so sánh với đường cơ sở đơn giản, đánh giá bằng số liệu phù hợp và tính đến thực tế là tương lai sẽ không sao chép chính xác quá khứ.