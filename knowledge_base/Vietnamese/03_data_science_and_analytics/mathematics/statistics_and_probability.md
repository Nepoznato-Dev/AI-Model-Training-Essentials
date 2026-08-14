---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Thống kê và xác suất
Xác suất và thống kê là nền tảng toán học của khoa học dữ liệu, học máy và nghiên cứu khoa học. Xác suất cho bạn biết các sự kiện có thể xảy ra như thế nào; số liệu thống kê cho bạn biết cách rút ra kết luận từ dữ liệu. Cùng nhau, họ biến sự không chắc chắn thành kiến ​​thức có thể định lượng và quản lý được.
---

##Lý thuyết xác suất
### Khái niệm cốt lõi
| Khái niệm | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Không gian mẫu** | Tập hợp tất cả các kết quả có thể xảy ra | Đổ xúc xắc: {1, 2, 3, 4, 5, 6} |
| **Sự kiện** | Một tập con của không gian mẫu | Cán một số chẵn: {2, 4, 6} |
| **Xác suất** | Số từ 0 đến 1 đo khả năng | P(cán 6) = 1/6 |
| **Xác suất có điều kiện** | P(A|B): xác suất xảy ra A cho B | P(mưa | nhiều mây) |
| **Độc lập** | Sự kiện mà cái này không ảnh hưởng đến cái kia | Việc lật đồng xu là độc lập |
### Quy tắc xác suất
| Quy tắc | Công thức | Trường hợp sử dụng |
|------|----------|----------|
| **Quy tắc bổ sung** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Xác suất của A hoặc B |
| **Quy tắc nhân** | P(A ∩ B) = P(A) × P(B|A) | Xác suất của A và B |
| **Quy tắc bổ sung** | P(không phải A) = 1 − P(A) | Xác suất xảy ra sự kiện |
| **Định luật tổng xác suất** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Phân vùng theo các sự kiện loại trừ lẫn nhau |
| **Định lý Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Cập nhật niềm tin bằng bằng chứng |
### Phân phối xác suất
| Phân phối | Loại | Thông số chính | Trường hợp sử dụng |
|-------------|------|-------|----------|
| **Bình thường (Gaussian)** | Liên tục | Giá trị trung bình (μ), Độ lệch chuẩn (σ) | Hiện tượng tự nhiên, sai số đo lường |
| **Nhị thức** | Rời Rạc | n (thử nghiệm), p (xác suất) | Số lượng thành công/thất bại |
| **Poisson** | Rời Rạc | λ (tỷ lệ) | Sự kiện hiếm hoi theo thời gian/không gian |
| **Số mũ** | Liên tục | λ (tỷ lệ) | Thời gian giữa các sự kiện |
| **Đồng phục** | Cả hai | a, b (giới hạn) | Kết quả có khả năng xảy ra như nhau |
| **Chi-Square** | Liên tục | k (bậc tự do) | Các bài kiểm tra mức độ phù hợp |
| **t-Phân phối** | Liên tục | ν (bậc tự do) | Suy luận mẫu nhỏ |
### Thuộc tính chính của phân phối
| Tài sản | Mô tả |
|----------|-------------|
| **Trung bình (Giá trị mong đợi)** | Tâm khối lượng phân bố: E[X] = Σ xᵢ × P(xᵢ) |
| **Phương sai** | Trải rộng xung quanh giá trị trung bình: Var(X) = E[(X − μ)²] |
| **Độ lệch chuẩn** | Căn bậc hai của phương sai; cùng đơn vị với dữ liệu |
| **Độ lệch** | Sự bất đối xứng của phân phối |
| **Đột ngột** | "Tailedness" — cái đuôi nặng đến mức nào |
---

## Suy luận thống kê
### Thống kê mô tả và thống kê suy luận
| | Mô tả | Suy luận |
|---|-------------|-------------|
| **Mục đích** | Tóm tắt và mô tả dữ liệu | Rút ra kết luận về dân số từ một mẫu |
| **Công cụ** | Giá trị trung bình, trung vị, mode, độ lệch chuẩn, biểu đồ | Kiểm tra giả thuyết, khoảng tin cậy, hồi quy |
| **Phạm vi** | Chỉ dữ liệu bạn có | Khái quát hóa ngoài mẫu của bạn |
### Khung kiểm tra giả thuyết
| Bước | Mô tả |
|------|-------------|
| 1. **Giả thuyết trạng thái** | Giả thuyết không (H₀): không có hiệu lực; Thay thế (H₁): có hiệu lực |
| 2. **Chọn mức ý nghĩa** | α = 0,05 (thông thường) |
| 3. **Chọn bài kiểm tra** | Dựa trên loại dữ liệu, cỡ mẫu và các giả định |
| 4. **Tính toán thống kê kiểm tra** | Phụ thuộc vào bài kiểm tra được chọn |
| 5. **Tìm giá trị p** | Xác suất quan sát dữ liệu nếu H₀ đúng |
| 6. **Đưa ra quyết định** | Nếu p < α, hãy bác bỏ H₀; nếu không thì không bác bỏ H₀ |
### Kiểm tra thống kê thông thường
| Kiểm tra | Khi nào nên sử dụng | Nó so sánh những gì |
|------|-------------|-----------------|
| **t-kiểm tra** | So sánh phương tiện của 1–2 nhóm | Nhóm ý nghĩa của một giá trị hoặc với nhau |
| **Kiểm tra chi bình phương** | Dữ liệu phân loại | Tần suất quan sát được so với dự kiến ​​|
| **ANOVA** | So sánh phương tiện của hơn 3 nhóm | Phương sai giữa nhóm và trong nhóm |
| **Mann-Whitney U** | Thay thế phi tham số cho t-test | Xếp hạng phân bố của hai nhóm |
| **Tương quan Pearson** | Mối quan hệ tuyến tính giữa hai biến liên tục | giá trị r từ −1 đến +1 |
| **Tương quan Spearman** | Mối quan hệ đơn điệu (dựa trên cấp bậc) | ρ giá trị cho dữ liệu thứ tự hoặc không chuẩn hóa |
### Khoảng tin cậy
Khoảng tin cậy đưa ra một loạt các giá trị hợp lý cho tham số tổng thể:
- **KTC 95% cho giá trị trung bình** (đã biết σ): x̄ ± 1,96 × (σ / √n)
- **Giải thích**: "Chúng tôi tin chắc 95% giá trị trung bình thực sự của tổng thể nằm trong khoảng này"
- **CI rộng hơn** = độ không chắc chắn cao hơn (mẫu nhỏ hơn, độ biến thiên cao hơn hoặc mức độ tin cậy cao hơn)
---

## Phân tích hồi quy
### Các loại hồi quy
| Loại | Biến phụ thuộc | Trường hợp sử dụng |
|------|-------------------|----------|
| **Hồi quy tuyến tính** | Liên tục | Dự đoán giá nhà, doanh số |
| **Hồi quy logistic** | Nhị phân (0/1) | Phân loại: phát hiện thư rác, chẩn đoán bệnh |
| **Hồi quy đa thức** | Liên tục (cong) | Đường cong tăng trưởng, xu hướng phi tuyến tính |
| **Hồi quy bội** | Liên tục (2+ yếu tố dự đoán) | Kiểm soát các yếu tố gây nhiễu |
| **Sườn núi / Lasso** | Liên tục (chính quy) | Ngăn chặn trang bị quá mức, lựa chọn tính năng |
### Khái niệm cơ bản về hồi quy tuyến tính
Mô hình: **y = β₀ + β₁x + ε**
| Thành phần | Ý nghĩa |
|----------||----------|
| β₀ (đánh chặn) | Giá trị của y khi x = 0 |
| β₁ (độ dốc) | Thay đổi y để thay đổi một đơn vị trong x |
| ε (thuật ngữ lỗi) | Biến thể không giải thích được |
**Chỉ số chính:**
- **R² (hệ số xác định)**: Tỷ lệ phương sai được mô hình giải thích (0 đến 1)
- **R² đã điều chỉnh**: R² bị phạt vì số lượng yếu tố dự đoán
- **RMSE**: Sai số bình phương trung bình gốc — sai số dự đoán trung bình ở cùng đơn vị với y
### Giả định về hồi quy tuyến tính
| Giả định | Ý nghĩa của nó | Cách kiểm tra |
|----------|--------------|--------------|
| **Tính tuyến tính** | Mối quan hệ giữa X và Y là tuyến tính | Lô phân tán |
| **Độc lập** | Các quan sát là độc lập | Thiết kế nghiên cứu |
| **Tính đồng nhất** | Phương sai không đổi của phần dư | Lô đất dư |
| **Bình thường** | Phần dư được phân phối chuẩn | Biểu đồ Q-Q, bài kiểm tra Shapiro-Wilk |
| **Không có đa cộng tuyến** | Các yếu tố dự đoán không có mối tương quan cao | VIF (Hệ số lạm phát phương sai) |
---

## Thống kê Bayes
### Người thường xuyên so với Bayesian
| | Người thường xuyên | Bayes |
|---|-------------|----------|
| **Xác suất có nghĩa** | Tần số dài hạn | Mức độ niềm tin |
| **Thông số là** | Đã sửa nhưng chưa biết | Biến ngẫu nhiên có phân phối |
| **Công dụng** | giá trị p, khoảng tin cậy | Phân phối sau, khoảng tin cậy |
| **Điểm mạnh** | Khách quan, có cơ sở | Kết hợp kiến ​​thức sẵn có, diễn giải trực quan |
### Định lý Bayes trong thực tế
**Sau = (Khả năng × Trước) / Bằng chứng**
Ví dụ - xét nghiệm y tế:
- Tỷ lệ mắc bệnh: 1% (trước đó)
- Độ nhạy xét nghiệm: 95% (tỷ lệ dương tính thật)
- Độ đặc hiệu xét nghiệm: 90% (tỷ lệ âm tính thật)
- Nếu bạn xét nghiệm dương tính: P(bệnh | dương tính) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8%
Kết quả phản trực giác này — hầu hết các kết quả dương tính đều là dương tính giả khi bệnh hiếm gặp — là **sai lầm về tỷ lệ cơ sở** và nó cho thấy lý do tại sao tư duy Bayesian lại quan trọng.
---

## Lời khuyên thiết thực
- **Luôn trực quan hóa dữ liệu của bạn** trước khi chạy bất kỳ thử nghiệm thống kê nào
- **Kiểm tra các giả định** — vi phạm có thể làm mất hiệu lực kết quả
- **Quy mô hiệu ứng quan trọng** — một kết quả có ý nghĩa thống kê có thể thực tế vô nghĩa
- **Mối tương quan không phải là quan hệ nhân quả** — ngay cả mối tương quan chặt chẽ cũng có thể có yếu tố gây nhiễu
- **So sánh nhiều** làm tăng tỷ lệ dương tính giả — áp dụng các chỉnh sửa (Bonferroni, FDR)
- **Báo cáo khoảng tin cậy**, không chỉ giá trị p
---

## Tại sao điều này lại quan trọng
Thống kê là xương sống của nghiên cứu khoa học, phân tích kinh doanh và học máy. Không có nó, bạn không thể phân biệt tín hiệu với nhiễu, xác định tác động thực sự từ những biến động ngẫu nhiên hoặc đưa ra dự đoán với độ không chắc chắn được định lượng. Cho dù bạn đang phân tích các bài kiểm tra A/B, đào tạo mô hình ML hay đọc tài liệu nghiên cứu, hiểu biết về thống kê là điều cần thiết.