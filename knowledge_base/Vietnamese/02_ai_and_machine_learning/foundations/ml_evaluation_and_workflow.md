<!--
---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, evaluation, workflow, ai-and-machine-learning]
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

-->
# Đánh giá và quy trình làm việc của Machine Learning
Hướng dẫn thực tế về vòng đời ML — từ việc định khung vấn đề đến giám sát sản xuất — tập trung vào số liệu, xác thực và gỡ lỗi.
---

## Quy trình làm việc ML (CRISP-ML)
1. **Hiểu biết về kinh doanh**: Xác định mục tiêu và tiêu chí thành công.
2. **Hiểu biết về dữ liệu**: Khám phá dữ liệu có sẵn, xác định các vấn đề về chất lượng.
3. **Chuẩn bị dữ liệu**: Làm sạch, chuyển đổi và phân chia dữ liệu.
4. **Lập mô hình**: Đào tạo mô hình, điều chỉnh siêu tham số.
5. **Đánh giá**: Đánh giá hiệu suất theo số liệu.
6. **Triển khai**: Phục vụ mô hình trong sản xuất.
7. **Giám sát**: Theo dõi độ lệch, hiệu suất và các điểm bất thường.
Đây là một vòng lặp - bạn sẽ xem lại các bước trước đó dựa trên kết quả đánh giá.
---

## Tách dữ liệu
### Đào tạo / Xác thực / Tách thử nghiệm
- **Tập huấn luyện** (~70%): Được sử dụng để phù hợp với các tham số của mô hình.
- **Bộ xác thực** (~15%): Được sử dụng để điều chỉnh siêu tham số và chọn các biến thể mô hình.
- **Bộ kiểm tra** (~15%): Chỉ sử dụng một lần ở cuối để ước tính hiệu suất khái quát hóa.
**Quan trọng:** Bộ thử nghiệm phải được giữ nguyên hoàn toàn cho đến lần đánh giá cuối cùng để tránh rò rỉ dữ liệu.
### Xác thực chéo (k-fold)
Đối với các tập dữ liệu nhỏ, hãy sử dụng xác thực chéo k-fold: chia dữ liệu thành k lần, huấn luyện trên k-1, xác thực phần còn lại và lặp lại k lần. Hiệu suất trung bình. k=5 hoặc k=10 là phổ biến.
### Phân chia theo tầng
Để phân loại với các lớp không cân bằng, hãy sử dụng phân chia phân tầng để duy trì tỷ lệ lớp trong mỗi tập hợp con.
### Chia theo thời gian
Đối với dữ liệu chuỗi thời gian, hãy phân chia theo trình tự thời gian (huấn luyện trong quá khứ, kiểm tra trong tương lai) thay vì ngẫu nhiên.
---

## Số liệu đánh giá
### Số liệu phân loại
| Số liệu | Nó đo lường những gì | Được sử dụng tốt nhất cho |
|--------|-------------------|---------------|
| **Độ chính xác** | (TP + TN) / (TP + TN + FP + FN) | Bộ dữ liệu cân bằng |
| **Chính xác** | TP / (TP + FP) | Khi kết quả dương tính giả gây tốn kém (ví dụ: phát hiện thư rác) |
| **Nhớ lại** | TP / (TP + FN) | Khi kết quả âm tính giả tốn kém (ví dụ: sàng lọc ung thư) |
| **Điểm F1** | Phương tiện hài hòa của độ chính xác và thu hồi | Bộ dữ liệu không cân bằng, số liệu đơn |
| **AUC-ROC** | Diện tích dưới đường cong ROC; cân bằng giữa TPR và FPR | Hiệu suất phân loại chung không phụ thuộc vào ngưỡng |
| **AUC-PR** | Khu vực dưới đường cong Precision-Recall | Bộ dữ liệu mất cân bằng cao |
**Định nghĩa:**
- TP = Thực Dương
- TN = Đúng Âm tính
- FP = Dương tính giả (Lỗi loại I)
- FN = Âm tính giả (Lỗi loại II)
### Số liệu hồi quy
| Số liệu | Nó đo lường những gì | Nhạy cảm với các ngoại lệ |
|--------|-------------------|--------------------------|
| **MSE** (Lỗi bình phương trung bình) | Chênh lệch bình phương trung bình | Cao |
| **RMSE** (Lỗi bình phương trung bình gốc) | Căn bậc hai của MSE (cùng đơn vị với mục tiêu) | Cao |
| **MAE** (Lỗi tuyệt đối trung bình) | Chênh lệch tuyệt đối trung bình | Thấp |
| **R²** (Hệ số xác định) | Tỷ lệ phương sai được giải thích | Không trực tiếp, nhưng nhạy cảm với các ngoại lệ một cách gián tiếp |
### Số liệu xếp hạng và truy xuất
- **Precision@k**: Tỷ lệ các mục có liên quan trong số đề xuất hàng đầu.
- **Recall@k**: Phần của tất cả các mục có liên quan xuất hiện trong top-k.
- **NDCG** (Lợi nhuận tích lũy chiết khấu chuẩn hóa): Tính đến mức độ liên quan của vị thế.
- **Tỷ lệ truy cập**: Liệu một mục có liên quan có xuất hiện trong top-k hay không.
### Số liệu sáng tạo / LLM
- **Sự bối rối**: Mức độ "ngạc nhiên" của mô hình trước một văn bản bị kéo dài ra (càng thấp càng tốt).
- **BLEU**: n-gram trùng lặp với các bản dịch tham chiếu (tập trung vào độ chính xác).
- **ROUGE**: Chồng chéo theo định hướng thu hồi để tóm tắt.
- **BERTScore**: Sự tương đồng về ngữ nghĩa bằng cách sử dụng các phần nhúng theo ngữ cảnh (mạnh hơn BLEU).
- **METEOR**: Căn chỉnh theo các từ đồng nghĩa và gốc của WordNet.
---

## Cạm bẫy đánh giá
### Rò rỉ dữ liệu
Xảy ra khi thông tin từ bộ kiểm tra vô tình ảnh hưởng đến việc huấn luyện.
- **Ngăn chặn:** Không bao giờ sử dụng dữ liệu thử nghiệm cho kỹ thuật tính năng, chuẩn hóa hoặc điều chỉnh siêu tham số.
- **Phát hiện:** Nếu mô hình của bạn đạt điểm cao đáng ngờ, nghi ngờ có rò rỉ.
### Trang bị quá mức
Mô hình hoạt động tốt trên dữ liệu huấn luyện nhưng kém về xác nhận/kiểm tra.
- **Giảm nhẹ:** Sử dụng tính năng chính quy hóa, dừng sớm, đơn giản hóa kiến ​​trúc hoặc thu thập thêm dữ liệu.
### Không phù hợp
Mô hình hoạt động kém cả về đào tạo và xác nhận.
- **Giảm thiểu:** Sử dụng mô hình phức tạp hơn, thêm tính năng hoặc giảm tính chính quy.
### Dữ liệu mất cân bằng
- **Giảm nhẹ:** Sử dụng trọng số lớp, mẫu thừa (SMOTE), mẫu dưới hoặc sử dụng số liệu thích hợp (F1, AUC-PR) thay vì độ chính xác.
### Trôi theo thời gian (Trôi theo khái niệm)
Mối quan hệ giữa các tính năng và mục tiêu thay đổi theo thời gian.
- **Giảm thiểu:** Đào tạo lại định kỳ, theo dõi hiệu suất, sử dụng thuật toán phát hiện sai lệch.
---

## Điều chỉnh siêu tham số
- **Tìm kiếm lưới**: Thử triệt để tất cả các kết hợp của một tập hợp siêu tham số được xác định trước. Đơn giản nhưng tốn kém về mặt tính toán.
- **Tìm kiếm ngẫu nhiên**: Mẫu kết hợp ngẫu nhiên từ các bản phân phối. Hiệu quả hơn tìm kiếm dạng lưới cho không gian nhiều chiều.
- **Tối ưu hóa Bayes**: Xây dựng mô hình xác suất của hàm mục tiêu và chọn siêu tham số một cách thông minh. Thư viện: Optuna, Hyperopt, tối ưu hóa scikit.
- **Điều chỉnh tự động**: Sử dụng các công cụ như Optuna, Ray Tune hoặc Weights & Biases Sweeps để điều chỉnh phân tán.
**Phạm vi tìm kiếm được đề xuất cho các siêu tham số phổ biến:**
| Tham số | Phạm vi được đề xuất (thang log) |
|----------||------------------------------------------|
| Tỷ lệ học tập | 1e-5 đến 1e-1 |
| Kích thước lô | 16, 32, 64, 128, 256 |
| Số lớp (NN) | 2 đến 6 |
| Số lượng tế bào thần kinh (NN) | 32 đến 1024 |
| Chính quy hóa (L2) | 1e-6 đến 1e-2 |
| Độ sâu cây (XGBoost) | 3 đến 12 |
---

## Lựa chọn và xác thực mô hình
1. **Mô hình cơ sở**: Bắt đầu bằng mô hình phỏng đoán đơn giản hoặc mô hình đơn giản (ví dụ: hồi quy logistic, chỉ số dự đoán trung bình) để thiết lập giới hạn dưới.
2. **Mô hình ứng cử viên**: Đào tạo nhiều nhóm mô hình (ví dụ: Rừng ngẫu nhiên, XGBoost, Mạng thần kinh).
3. **Xác thực chéo** từng ứng viên trên bộ xác thực.
4. **So sánh số liệu** (với khoảng tin cậy) và chọn ứng viên tốt nhất.
5. **Đánh giá cuối cùng** trên bộ bài kiểm tra được tổ chức.
6. **Phân tích lỗi**: Xem các ví dụ mà mô hình sai. Xác định các mẫu (ví dụ: các lớp hiếm, đầu vào không rõ ràng) và cung cấp thông tin chuyên sâu về quá trình chuẩn bị dữ liệu hoặc kỹ thuật tính năng.
---

## Triển khai và giám sát
### Mẫu phục vụ
- **Suy luận hàng loạt**: Xử lý khối lượng lớn dữ liệu ngoại tuyến (ví dụ: đề xuất hàng đêm).
- **Suy luận trực tuyến**: Dự đoán theo thời gian thực thông qua API (ví dụ: chấm điểm tín dụng, phát hiện gian lận).
- **Suy luận trực tuyến**: Theo sự kiện, theo thời gian thực với độ trễ thấp (ví dụ: cảnh báo cảm biến IoT).
### Giám sát mô hình
- **Giám sát hiệu suất**: Theo dõi độ chính xác/F1 theo thời gian trên dữ liệu trực tiếp (khi có thông tin cơ bản).
- **Trôi dạt dữ liệu**: Theo dõi những thay đổi trong phân bổ tính năng đầu vào (ví dụ: sử dụng PSI – Chỉ số ổn định dân số).
- **Trôi khái niệm**: Theo dõi những thay đổi trong mối quan hệ giữa đầu vào và đầu ra.
- **Độ lệch dự đoán**: Theo dõi sự phân bổ của các kết quả đầu ra được dự đoán.
- **Độ trễ và thông lượng**: Đảm bảo đáp ứng SLA (Thỏa thuận cấp độ dịch vụ).
### Ghi nhật ký và cảnh báo
- Ghi lại tất cả các yêu cầu và phản hồi dự đoán (có tính năng ẩn danh).
- Đặt cảnh báo cho:
  - Hiệu suất giảm đáng kể.
  - Tỷ lệ đầu vào bị thiếu hoặc không hợp lệ cao.
  - Kết quả đầu ra của mô hình nằm ngoài giới hạn dự kiến.
### Lập phiên bản và đăng ký mô hình
- Sử dụng sổ đăng ký mô hình (ví dụ: MLflow, Trọng lượng & Xu hướng, Sổ đăng ký mô hình Sagemaker) để lưu trữ và phiên bản mô hình, siêu dữ liệu và kết quả đánh giá.
- Lưu trữ mã huấn luyện và phiên bản dữ liệu (thông qua DVC hoặc Git LFS) bên cạnh mô hình.
---

## Danh sách kiểm tra quy trình làm việc thực tế
- [ ] Vấn đề được đóng khung và xác định số liệu thành công.
- [ ] Đã thực hiện khám phá dữ liệu (thiếu giá trị, giá trị ngoại lệ, phân phối).
- [ ] Đã tạo phần tách đào tạo/xác thực/kiểm tra (phân tầng nếu cần).
- [ ] Mô hình cơ sở được thiết lập.
- [ ] Các mô hình ứng viên được đào tạo và xác nhận.
- [ ] Điều chỉnh siêu tham số.
- [ ] Mô hình tốt nhất được lựa chọn thông qua xác thực chéo.
- [ ] Đánh giá cuối cùng trên tập kiểm tra.
- [ ] Thực hiện phân tích lỗi.
- [ ] Đã sẵn sàng kế hoạch triển khai (phục vụ cơ sở hạ tầng).
- [ ] Thiết lập bảng điều khiển giám sát.
- [ ] Tài liệu (thẻ dữ liệu, thẻ mẫu) đã hoàn thành.