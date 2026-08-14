---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
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
# Phương pháp tập hợp
Các phương pháp tập hợp kết hợp nhiều mô hình học máy để tạo ra dự đoán tốt hơn bất kỳ mô hình đơn lẻ nào có thể đạt được nếu sử dụng riêng lẻ. Trực giác rất đơn giản: nếu bạn có một số mô hình, mỗi mô hình đều có phần chính xác nhưng lại mắc các lỗi khác nhau, thì việc kết hợp các dự đoán của chúng sẽ loại bỏ các lỗi riêng lẻ và tạo ra kết quả chắc chắn hơn. Ensembles đứng đằng sau hầu hết các giải pháp học máy cạnh tranh và vẫn là một trong những kỹ thuật đáng tin cậy nhất trong hệ thống sản xuất.
---

## Tại sao Ensembles lại hoạt động
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Trí tuệ của đám đông** | Nhiều ước tính không hoàn hảo, được tính trung bình, tốt hơn bất kỳ ước tính đơn lẻ nào |
| **Đánh đổi độ lệch-phương sai** | Các tập hợp có thể giảm phương sai (đóng bao) hoặc sai lệch (tăng cường) mà không phải hy sinh cái kia |
| **Lỗi đa dạng** | Nếu các mô hình mắc các lỗi khác nhau, việc kết hợp chúng sẽ loại bỏ các lỗi riêng lẻ |
| **Làm mịn ranh giới quyết định** | Nhiều mô hình tạo ra bề mặt quyết định mạnh mẽ hơn một mô hình |
---

## Đóng gói (Tổng hợp Bootstrap)
### Cách thức hoạt động
| Bước | Mô tả |
|------|-------------|
| **1. Lấy mẫu Bootstrap** | Vẽ nhiều mẫu ngẫu nhiên (có thể thay thế) từ dữ liệu huấn luyện |
| **2. Mô hình cơ sở xe lửa** | Huấn luyện một mô hình trên mỗi mẫu bootstrap (thường là cây quyết định) |
| **3. Tổng hợp** | Đối với hồi quy: dự đoán trung bình. Để phân loại: bỏ phiếu theo đa số |
### Đặc điểm chính
| Đặc trưng | Mô tả |
|---------------|-------------|
| **Giảm phương sai** | Tính trung bình làm giảm bớt các biến động của mô hình riêng lẻ |
| **Đào tạo song song** | Mỗi mô hình cơ sở đều độc lập; có thể được đào tạo đồng thời |
| **Đánh giá thực tế** | Mỗi mẫu bị loại khỏi một số mẫu bootstrap; sử dụng chúng để xác nhận |
| **Giải trí** | Lựa chọn tính năng ngẫu nhiên ở mỗi lần phân chia làm giảm mối tương quan giữa các cây |
### Rừng ngẫu nhiên
| Khía cạnh | Mô tả |
|--------|-------------|
| **Người học cơ bản** | Cây quyết định |
| **Bổ sung khóa** | Tại mỗi lần phân chia, chỉ xem xét một tập hợp con các tính năng ngẫu nhiên (thường là sqrt(n_features)) |
| **Tại sao nó hoạt động** | Lựa chọn tính năng ngẫu nhiên làm mất liên kết giữa các cây, làm cho quần thể trở nên mạnh mẽ hơn |
| **Siêu tham số** | Số lượng cây; độ sâu tối đa; mẫu tối thiểu trên mỗi lá; tính năng tối đa |
| **Điểm mạnh** | Xử lý dữ liệu nhiều chiều; mạnh mẽ đến các ngoại lệ; cung cấp tầm quan trọng của tính năng |
| **Điểm yếu** | Khó hiểu hơn so với cây đơn lẻ; có thể phù hợp với các nhiệm vụ hồi quy ồn ào |
---

## Tăng cường
### Cách thức hoạt động
| Bước | Mô tả |
|------|-------------|
| **1. Đào tạo mô hình đầu tiên** | Huấn luyện mô hình cơ sở (thường là cây nông / "gốc") trên dữ liệu |
| **2. Xác định lỗi** | Tìm những trường hợp mô hình sai |
| **3. Đào tạo mô hình tiếp theo** | Đào tạo một mô hình mới tập trung vào những sai lầm (tái trọng số hoặc trang bị dư) |
| **4. Kết hợp tuần tự** | Mỗi mẫu mới sẽ sửa các lỗi tích lũy của tất cả các mẫu trước đó |
| **5. Lặp lại** | Tiếp tục với số vòng xác định |
### Thuật toán tăng cường
| Thuật toán | Hàm mất mát | Tính năng chính |
|----------||--------------|-------------|
| **AdaBoost** | Hàm mũ | Cân nhắc lại các trường hợp bị phân loại sai; đơn giản; nhạy cảm với tiếng ồn |
| **Tăng cường độ dốc** | Bất kỳ tổn thất nào có thể phân biệt được | Phù hợp với phần dư (độ dốc mất mát); linh hoạt hơn |
| **XGBoost** | Tăng cường độ dốc thường xuyên | Chính quy hóa L1/L2; độ dốc bậc hai; tối ưu hóa phần cứng |
| **LightGBM** | Lấy mẫu một phía dựa trên gradient | Tăng trưởng theo lá; dựa trên biểu đồ; nhanh trên tập dữ liệu lớn |
| **CatBoost** | Ra lệnh tăng cường | Xử lý các tính năng phân loại nguyên bản; giảm trang bị quá mức |
### Tăng tốc và Đóng bao
| Kích thước | Đóng bao | Tăng cường |
|----------|----------|----------|
| **Đào tạo** | Song song | Tuần tự |
| **Tập trung** | Giảm phương sai | Giảm sự thiên vị |
| **Mô hình cơ sở** | Phương sai cao, độ lệch thấp (cây sâu) | Phương sai thấp, độ lệch cao (cây nông / gốc cây) |
| **Kết hợp** | Trọng lượng bằng nhau | Trọng số theo hiệu suất |
| **Trang bị quá mức** | Ít bị ảnh hưởng | Có thể overfit nếu quá nhiều vòng |
| **Độ nhạy tiếng ồn** | Mạnh mẽ | Nhạy cảm với dữ liệu ồn ào |
---

## Xếp chồng
### Cách thức hoạt động
| Bước | Mô tả |
|------|-------------|
| **1. Mô hình cơ sở xe lửa** | Đào tạo các mô hình đa dạng (ví dụ: rừng ngẫu nhiên, SVM, mạng lưới thần kinh, tăng cường độ dốc) |
| **2. Tạo dự đoán** | Sử dụng các dự đoán ngoài màn hình (xác thực chéo) làm tính năng đầu vào |
| **3. Đào tạo siêu mô hình** | Huấn luyện mô hình cấp hai dựa trên dự đoán của mô hình cơ sở |
| **4. Dự đoán cuối cùng** | Mô hình cơ sở dự đoán; siêu mô hình kết hợp dự đoán của họ |
### Các phương pháp hay nhất về xếp chồng
| Thực hành | Lý do |
|----------|--------|
| **Sử dụng các mẫu cơ sở đa dạng** | Các thuật toán khác nhau tạo ra các lỗi khác nhau; sự đa dạng là toàn bộ vấn đề |
| **Sử dụng xác thực chéo cho các dự đoán cơ sở** | Ngăn chặn siêu mô hình học cách khai thác các mô hình cơ sở overfit |
| **Giữ siêu mô hình đơn giản** | Hồi quy logistic hoặc cây nông; các mô hình cơ sở thực hiện công việc nặng nhọc |
| **Bao gồm các tính năng thô trong siêu mô hình** | Đôi khi cũng hữu ích khi cấp cho siêu mô hình quyền truy cập vào các tính năng gốc |
---

## Bỏ phiếu và tính trung bình
### Bỏ phiếu cứng (Phân loại)
| Người mẫu | Dự đoán |
|-------|----------|
| Mẫu A | Lớp 1 |
| Mẫu B | Lớp 0 |
| Mẫu C | Lớp 1 |
| **Đa số phiếu** | **Lớp 1** |
### Bỏ phiếu mềm (Phân loại)
| Người mẫu | P(Lớp 0) | P(Lớp 1) |
|-------|--------------|----------|
| Mẫu A | 0,3 | 0,7 |
| Mẫu B | 0,6 | 0,4 |
| Mẫu C | 0,4 | 0,6 |
| **Trung bình** | **0,43** | **0,57** |
| **Dự đoán** | | **Lớp 1** |
### Tính trung bình có trọng số
| Người mẫu | Cân nặng | Dự đoán |
|-------|--------|----------|
| Mẫu A | 0,5 | 0,8 |
| Mẫu B | 0,3 | 0,6 |
| Mẫu C | 0,2 | 0,9 |
| **Trung bình có trọng số** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Hướng dẫn thực hành
### Khi nào nên sử dụng bản hòa tấu nào
| Kịch bản | Phương pháp được đề xuất |
|----------|-------------------|
| ** Đường cơ sở nhanh; dữ liệu dạng bảng** | Rừng ngẫu nhiên |
| ** Độ chính xác tối đa; dữ liệu dạng bảng** | XGBoost / LightGBM / CatBoost |
| **Dữ liệu ồn ào** | Đóng gói (tăng tốc sẽ vượt quá tiếng ồn) |
| **Cần có khả năng diễn giải** | Mô hình đơn lẻ hoặc quần thể nhỏ có tầm quan trọng về tính năng |
| **Các loại mô hình đa dạng** | Xếp chồng hoặc biểu quyết |
| **Học trực tuyến** | Truyền trực tuyến các phương pháp tập hợp; tăng cường thích ứng |
| **Dữ liệu mất cân bằng** | Rừng ngẫu nhiên cân bằng; tăng cường nhạy cảm với chi phí |
### Chiến lược đa dạng của tập thể
| Chiến lược | Mô tả |
|----------|-------------|
| **Các thuật toán khác nhau** | Kết hợp các mô hình dựa trên cây, tuyến tính và thần kinh |
| **Các tính năng khác nhau** | Đào tạo mô hình trên các tập hợp con tính năng khác nhau |
| **Các tập hợp con dữ liệu khác nhau** | Đóng bao; lấy mẫu con |
| **Siêu tham số khác nhau** | Cùng một thuật toán với các cấu hình khác nhau |
| **Các khoảng thời gian khác nhau** | Đào tạo vào các khung giờ khác nhau |
---

## Bản tóm tắt
Các phương pháp tập hợp hoạt động vì chúng kết hợp nhiều mô hình không hoàn hảo thành một công cụ dự báo mạnh mẽ duy nhất. Đóng bao (rừng ngẫu nhiên) làm giảm phương sai bằng cách huấn luyện các mô hình song song trên các mẫu bootstrap và tính trung bình. Việc tăng cường (XGBoost, LightGBM, CatBoost) làm giảm sai lệch bằng cách đào tạo các mô hình một cách tuần tự, mỗi mô hình sẽ sửa các lỗi trước đó. Xếp chồng sử dụng siêu mô hình để kết hợp các mô hình cơ sở đa dạng. Bỏ phiếu và tính trung bình là những cách kết hợp đơn giản nhất. Chủ đề chung là sự đa dạng: các nhóm hoạt động tốt nhất khi các mô hình thành phần của chúng hợp lý riêng lẻ nhưng mắc các lỗi khác nhau. Trong thực tế, việc tăng cường độ dốc trên dữ liệu dạng bảng thường là phương pháp đơn lẻ có hiệu suất cao nhất, trong khi việc xếp chồng các mô hình khác nhau sẽ đẩy độ chính xác cao hơn nữa trong các cuộc thi và ứng dụng có mức đặt cược cao.