---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [ml, engineering, mlops, ai-and-machine-learning]
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
# Kỹ thuật ML và MLOps
Xây dựng mô hình học máy mới chỉ là một nửa trận chiến. Đưa nó vào sản xuất, giữ cho nó chạy ổn định, theo dõi độ lệch và lặp lại nó - đó là lúc kỹ thuật ML và MLOps xuất hiện. Tệp này bao gồm toàn bộ vòng đời từ hệ thống thử nghiệm đến hệ thống sản xuất.
---

## Vòng đời ML
| Giai đoạn | Mô tả | Hoạt động chính |
|-------|-------------|---------------|
| **1. Định nghĩa vấn đề** | Đóng khung vấn đề kinh doanh như một nhiệm vụ ML | Xác định số liệu, ràng buộc, tiêu chí thành công |
| **2. Thu thập dữ liệu** | Thu thập và gắn nhãn dữ liệu đào tạo | ETL, ghi nhãn, tăng cường |
| **3. Thử nghiệm** | Đào tạo và đánh giá mô hình | Kỹ thuật tính năng, điều chỉnh siêu tham số |
| **4. Lựa chọn mẫu** | Chọn mẫu tốt nhất | So sánh số liệu, đánh giá sự cân bằng |
| **5. Triển khai** | Đưa mô hình đi sản xuất | Phục vụ cơ sở hạ tầng, API, hàng loạt |
| **6. Giám sát** | Theo dõi sự trôi dạt và xuống cấp | Trôi dạt dữ liệu, trôi dạt khái niệm, hiệu suất |
| **7. Đào tạo lại** | Cập nhật mô hình với dữ liệu mới | Đào tạo lại theo lịch trình hoặc kích hoạt |
Hầu hết giá trị (và độ khó) nằm ở giai đoạn 5–7. Một mô hình ngồi trong sổ tay Jupyter không tạo ra giá trị kinh doanh.
---

## Mẫu phục vụ mẫu
| Mẫu | Mô tả | Độ trễ | Trường hợp sử dụng |
|----------|-------------|----------|----------|
| **Suy luận hàng loạt** | Chạy mô hình trên một loạt dữ liệu theo lịch trình | Giờ | Đề xuất hàng ngày, chấm điểm gian lận |
| **Suy luận trực tuyến** | Dự đoán thời gian thực theo yêu cầu | Mili giây | Xếp hạng tìm kiếm, phân loại theo thời gian thực |
| **Suy luận trực tuyến** | Xử lý dự đoán trên luồng dữ liệu | Giây | Phát hiện bất thường, xử lý sự kiện |
### Phục vụ cơ sở hạ tầng
| Công cụ | Loại | Tốt nhất cho |
|------|------|----------|
| **Phục vụ TensorFlow** | Máy chủ mẫu | Mô hình TensorFlow |
| **Phục vụ ngọn đuốc** | Máy chủ mẫu | Mô hình PyTorch |
| **Máy chủ suy luận Triton** | Đa khung | Suy luận GPU, nhiều khung |
| **vLLM** | LLM phục vụ | Suy luận LLM thông lượng cao |
| **BentoML** | Phục vụ thống nhất | Triển khai theo khung bất khả tri |
| **Seldon** | K8s-bản địa | Triển khai mô hình Kubernetes |
| **Ray Phục vụ** | Phục vụ có thể mở rộng | Mô hình lớn, suy luận phân tán |
---

## Sổ đăng ký mẫu
Cơ quan đăng ký mô hình là một kho lưu trữ tập trung để quản lý các mô hình ML - phiên bản, siêu dữ liệu, số liệu và trạng thái triển khai của chúng.
| Năng lực | Mô tả |
|----------||-------------|
| **Phiên bản** | Theo dõi mọi phiên bản mô hình bằng ID duy nhất |
| **Siêu dữ liệu** | Dữ liệu đào tạo, siêu tham số, số liệu, tác giả |
| **Chuyển tiếp giai đoạn** | Di chuyển mô hình qua các giai đoạn: Giai đoạn → Sản xuất → Đã lưu trữ |
| **Dòng dõi** | Theo dõi dữ liệu và mã nào được tạo ra từng mô hình |
| Công cụ | Mô tả |
|------|-------------|
| **MLflow** | Nguồn mở; đăng ký mô hình + theo dõi thử nghiệm |
| **Trọng lượng & Xu hướng (W&B)** | Thuộc về thương mại; theo dõi thử nghiệm + đăng ký mô hình |
| **DVC** | Phiên bản dữ liệu và mô hình với Git |
| **Azure ML / SageMaker** | Quản lý mô hình gốc trên nền tảng đám mây |
---

## Theo dõi thử nghiệm
Mọi thử nghiệm ML phải được theo dõi: dữ liệu nào đã được sử dụng, siêu tham số nào, kết quả là số liệu gì.
| Công cụ | Các tính năng chính |
|------|-------------|
| **MLflow** | Mã nguồn mở, tự lưu trữ, theo dõi các thông số/số liệu/tạo phẩm |
| **W&B** | Giao diện người dùng phong phú, quét, tạo phiên bản giả, báo cáo |
| **Sao Hải Vương** | Lưu trữ siêu dữ liệu cho MLOps |
| **TensorBoard** | Được tích hợp vào TensorFlow; hình dung đường cong đào tạo |
### Nội dung cần theo dõi
| Danh mục | Ví dụ |
|----------|----------|
| **Thông số** | Tốc độ học tập, kích thước lô, kiến ​​trúc mô hình, số kỷ nguyên |
| **Số liệu** | Độ chính xác, tổn thất, F1, AUC-ROC (mỗi kỷ nguyên và cuối cùng) |
| **Hiện vật** | Trọng lượng mô hình, ma trận nhầm lẫn, mẫu dự đoán |
| **Dữ liệu** | Phiên bản tập dữ liệu, tỷ lệ phân chia, các bước tiền xử lý |
| **Môi trường** | Phiên bản Python, phiên bản thư viện, phần cứng |
---

## Chiến lược triển khai mô hình
| Chiến lược | Nó hoạt động như thế nào | Rủi ro |
|----------|-------------|------|
| **Triển khai bóng** | Mô hình mới chạy song song với mô hình cũ; dự đoán được so sánh nhưng không được phục vụ | Không có rủi ro; xác thực trước khi phát trực tiếp |
| **Bản phát hành Canary** | Định tuyến % lưu lượng truy cập nhỏ đến mô hình mới; tăng dần | Rủi ro thấp; khôi phục nhanh |
| **Thử nghiệm A/B** | Phân chia người dùng cũ và mới; so sánh các số liệu kinh doanh | Đo lường tác động thực tế |
| **Xanh-Xanh** | Hai môi trường giống hệt nhau; chuyển đổi tất cả lưu lượng truy cập cùng một lúc | Khôi phục ngay lập tức; chi phí gấp đôi trong quá trình chuyển đổi |
| **Cờ tính năng** | Bật/tắt mô hình cho mỗi phân khúc người dùng | Kiểm soát chi tiết |
---

## Giám sát hệ thống ML
Hệ thống ML cần giám sát nhiều hơn phần mềm truyền thống vì bản thân dữ liệu có thể thay đổi.
### Các kiểu trôi dạt
| Loại Trôi | Những thay đổi gì | Ví dụ |
|----------|-------------|----------|
| **Dữ liệu trôi dạt** | Thay đổi phân phối đầu vào | Nhân khẩu học của khách hàng thay đổi sau một chiến dịch tiếp thị |
| **Khái niệm trôi dạt** | Mối quan hệ giữa thay đổi đầu vào và đầu ra | Hành vi của người tiêu dùng thay đổi trong thời kỳ suy thoái |
| **Nhãn trôi** | Thay đổi phân phối mục tiêu | Tỉ lệ lừa đảo tăng từ 1% lên 5% |
### Những gì cần theo dõi
| Danh mục | Số liệu |
|----------|----------|
| **Hiệu suất mẫu** | Độ chính xác, độ chính xác, thu hồi, F1, AUC (so với đường cơ sở) |
| **Chất lượng dữ liệu** | Thiếu giá trị, phân phối tính năng, ngoại lệ |
| **Phát hiện trôi dạt** | Kiểm tra thống kê (kiểm tra KS, PSI, phân kỳ KL) |
| **Cơ sở hạ tầng** | Độ trễ, thông lượng, mức sử dụng GPU, bộ nhớ |
| **Số liệu kinh doanh** | Tỷ lệ chuyển đổi, tác động đến doanh thu, sự hài lòng của người dùng |
### Công cụ giám sát
| Công cụ | Loại |
|------|------|
| **Rõ ràng là AI** | Giám sát hiệu suất mô hình và trôi dạt dữ liệu nguồn mở |
| **Grafana** | Trực quan hóa bảng điều khiển (hoạt động với Prometheus) |
| **Tại saoLabs** | Nền tảng quan sát dữ liệu |
| **Arize** | Khả năng quan sát ML và phân tích nguyên nhân gốc rễ |
| **Prometheus + Grafana** | Số liệu về cơ sở hạ tầng và ứng dụng |
---

## Đào tạo có thể tái tạo
Khả năng tái tạo có nghĩa là bạn có thể chạy lại thử nghiệm và nhận được kết quả tương tự. Nó cần thiết cho việc gỡ lỗi, kiểm tra và tuân thủ.
### Yêu cầu
| Yêu cầu | Làm thế nào để đạt được nó |
|-------------|-------------------|
| **Phiên bản dữ liệu** | Ảnh chụp nhanh DVC, Delta Lake hoặc tập dữ liệu có hàm băm |
| **Phiên bản mã** | Git cho tất cả mã đào tạo |
| **Ghim môi trường** | `requirements.txt`,`conda env`, Hình ảnh Docker với các phiên bản chính xác |
| **Cài đặt hạt giống** | Sửa các hạt giống ngẫu nhiên cho numpy, torch, tensorflow |
| **Quản lý cấu hình** | Cấu hình Hydra, OmegaConf hoặc YAML cho tất cả các siêu tham số |
| **Theo dõi hiện vật** | MLflow hoặc W&B để ghi lại mọi thử nghiệm |
---

## Suy luận tỷ lệ
Khi một mô hình cần phục vụ hàng triệu yêu cầu mỗi ngày thì hiệu suất sẽ rất quan trọng.
| Kỹ thuật | Mô tả |
|----------||-------------|
| **Phân khối** | Nhóm nhiều yêu cầu thành một lượt chuyển tiếp duy nhất |
| **Lượng tử hóa** | Giảm độ chính xác của mô hình (FP32 → INT8 hoặc INT4) để suy luận nhanh hơn |
| **Chưng cất mẫu** | Huấn luyện một mô hình nhỏ hơn để bắt chước một mô hình lớn hơn |
| **Cắt tỉa** | Loại bỏ trọng lượng hoặc tế bào thần kinh không quan trọng |
| **Bộ nhớ đệm** | Lưu trữ các dự đoán thường xuyên để tránh tính toán lại |
| **Tối ưu hóa GPU** | TensorRT, ONNX Thời gian chạy, Chú ý Flash |
| **Tỷ lệ theo chiều ngang** | Chạy nhiều bản sao mô hình đằng sau bộ cân bằng tải |
---

## Cờ tính năng cho ML
Cờ tính năng cho phép bạn kiểm soát phiên bản mô hình nào phục vụ người dùng nào mà không cần triển khai lại.
| Trường hợp sử dụng | Mô tả |
|----------|-------------|
| **Triển khai dần dần** | Phục vụ mô hình mới cho 5% người dùng, sau đó tăng |
| ** Công tắc tắt ** | Hoàn nguyên ngay lập tức về mô hình trước đó nếu phát hiện sự cố |
| **Dựa trên phân khúc** | Các mẫu mã khác nhau cho các phân khúc người dùng khác nhau |
| **Thử nghiệm** | Các biến thể mô hình thử nghiệm A/B với số liệu kinh doanh |
Công cụ: LaunchDarkly, Unleash, Flagsmith hoặc các cờ tính năng được cơ sở dữ liệu hỗ trợ đơn giản.
---

## Đường cong trưởng thành MLOps
| Cấp độ | Đặc điểm |
|-------|-------|
| **Cấp 0 — Thủ công** | Đào tạo thủ công, triển khai thủ công, không giám sát |
| **Cấp 1 — Thử nghiệm** | Theo dõi thử nghiệm, đăng ký mô hình, CI cơ bản |
| **Cấp 2 — Tự động hóa** | Đào tạo lại tự động, CI/CD cho mô hình, kiểm tra tự động |
| **Cấp 3 — Đường dẫn đầy đủ** | Quy trình tự động hóa từ đầu đến cuối với tính năng giám sát, phát hiện sai lệch và tự động đào tạo lại |
Hầu hết các tổ chức đều ở giữa Cấp 0 và Cấp 1. Mục tiêu là Cấp 2–3, trong đó vòng đời ML được tự động hóa và tự phục hồi.