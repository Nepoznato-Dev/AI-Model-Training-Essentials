---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
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

# Học tập liên kết và quyền riêng tư
Học liên kết là một kỹ thuật đào tạo các mô hình học máy trên nhiều thiết bị hoặc tổ chức mà không chia sẻ dữ liệu thô. Thay vì gửi dữ liệu đến máy chủ trung tâm, mỗi thiết bị sẽ huấn luyện một mô hình cục bộ và chỉ chia sẻ các bản cập nhật mô hình (độ dốc hoặc trọng lượng). Máy chủ trung tâm tổng hợp những cập nhật này để tạo ra một mô hình toàn cầu. Nó được Google thiết kế để đào tạo các mô hình ngôn ngữ bàn phím trên điện thoại Android - và từ đó nó đã trở thành một kỹ thuật quan trọng để bảo vệ quyền riêng tư của AI.
---

## Tại sao phải học liên kết?
| Động lực | Mô tả | Ví dụ |
|----------||-------------|----------|
| **Quyền riêng tư dữ liệu** | Dữ liệu thô không bao giờ rời khỏi thiết bị | Hồ sơ bệnh án lưu tại bệnh viện; ảnh lưu lại trên điện thoại |
| **Tuân thủ quy định** | GDPR, HIPAA và các quy định khác hạn chế việc chia sẻ dữ liệu | Ngân hàng có thể cộng tác mà không cần chia sẻ dữ liệu khách hàng |
| **Khối lượng dữ liệu** | Di chuyển dữ liệu tốn kém và chậm | Việc đào tạo trên hàng tỷ điện thoại là không thực tế nếu dữ liệu phải được tải lên |
| **Độ nhạy dữ liệu** | Một số dữ liệu quá nhạy cảm để chia sẻ, ngay cả khi có sự đồng ý | Tình báo chính phủ; dữ liệu sức khỏe cá nhân |
---

## Học liên kết hoạt động như thế nào
### Giao thức cơ bản (FedAvg)
| Bước | Điều gì xảy ra |
|------|-------------|
| **1. Khởi tạo** | Máy chủ trung tâm tạo mô hình toàn cầu với trọng số ngẫu nhiên |
| **2. Phân phối** | Máy chủ gửi mô hình toàn cầu hiện tại tới các thiết bị được chọn |
| **3. Đào tạo địa phương** | Mỗi thiết bị huấn luyện mô hình trên dữ liệu cục bộ của nó trong nhiều kỷ nguyên |
| **4. Tải lên** | Thiết bị gửi trọng lượng mô hình đã cập nhật (không phải dữ liệu) trở lại máy chủ |
| **5. Tổng hợp** | Máy chủ tính trung bình các trọng số (Trung bình Liên kết) để tạo mô hình toàn cầu mới |
| **6. Lặp lại** | Quay lại bước 2 cho đến khi mô hình hội tụ |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Thuộc tính chính
| Bất động sản | Mô tả |
|----------|-------------|
| **Dữ liệu không phải IID** | Mỗi thiết bị có các bản phân phối dữ liệu khác nhau (không độc lập và được phân phối giống hệt nhau) |
| **Dữ liệu không cân bằng** | Một số thiết bị có nhiều dữ liệu, số khác có rất ít |
| **Tham gia một phần** | Không phải tất cả các thiết bị đều có sẵn trong mỗi vòng |
| **Hiệu quả truyền thông** | Nút thắt là giao tiếp chứ không phải tính toán |
---

## Các biến thể học tập liên kết
| Biến thể | Mô tả | Lợi thế |
|----------|-------------|----------|
| **Trung bình của Fed** | Trọng lượng mô hình trung bình trên các thiết bị | Đơn giản; hoạt động tốt với dữ liệu IID |
| **FedProx** | Thêm một thuật ngữ gần vào đào tạo địa phương | Tốt hơn cho dữ liệu không phải IID |
| **Giàn giáo** | Sử dụng các biến thể kiểm soát để điều chỉnh tính không đồng nhất của dữ liệu | Hội tụ nhanh hơn trên dữ liệu không phải IID |
| **FedSGD** | Giống như FedAvg nhưng có một bước chuyển màu mỗi vòng | Chi phí liên lạc mỗi vòng thấp hơn |
| **FL được cá nhân hóa** | Mỗi thiết bị duy trì một mô hình được cá nhân hóa cùng với mô hình toàn cầu | Hiệu suất trên mỗi thiết bị tốt hơn |
| **FL dọc** | Các tính năng khác nhau (không phải mẫu khác nhau) giữa các bên | Khi các bên nắm giữ các khía cạnh khác nhau của cùng một dữ liệu |
---

## Quyền riêng tư khác biệt
Quyền riêng tư khác biệt (DP) cung cấp sự đảm bảo về mặt toán học rằng đầu ra của thuật toán không tiết lộ liệu có bất kỳ dữ liệu cá nhân nào được đưa vào hay không.
### Định nghĩa cốt lõi
Cơ chế M thỏa mãn quyền riêng tư vi sai (ε, δ) nếu đối với hai tập dữ liệu D và D' bất kỳ khác nhau trong một bản ghi:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Tham số | Ý nghĩa |
|----------||----------|
| **ε (epsilon)** | Ngân sách bảo mật. Nhỏ hơn = riêng tư hơn. Giá trị tiêu biểu: 0,1–10. |
| **δ (đồng bằng)** | Xác suất đảm bảo quyền riêng tư không thành công. Thường được đặt thành 1/N (nghịch đảo với kích thước tập dữ liệu). |
### Cơ chế bổ sung quyền riêng tư
| Cơ chế | Nó hoạt động như thế nào | Trường hợp sử dụng |
|----------|-------------|----------|
| **Cơ chế Gaussian** | Thêm nhiễu Gaussian được hiệu chỉnh theo độ nhạy của truy vấn | Giá trị liên tục (trọng số mô hình) |
| **Cơ chế Laplace** | Thêm tiếng ồn Laplace | Đếm truy vấn |
| **Cơ chế hàm mũ** | Chọn đầu ra có xác suất tỷ lệ thuận với tiện ích của chúng | Lựa chọn rời rạc |
### DP-SGD (Giảm dần độ dốc ngẫu nhiên riêng tư khác nhau)
| Bước | Mô tả |
|------|-------------|
| 1. Tính độ dốc trên mỗi mẫu | Thay vì độ dốc hàng loạt |
| 2. Clip chuyển màu | Giới hạn định mức tối đa của từng gradient (giới hạn ảnh hưởng của bất kỳ mẫu đơn lẻ nào) |
| 3. Thêm tiếng ồn | Thêm nhiễu Gaussian đã hiệu chỉnh vào gradient tổng hợp |
| 4. Cập nhật thông số | Bước giảm độ dốc tiêu chuẩn |
| Đánh đổi | Mô tả |
|----------||-------------|
| **Quyền riêng tư và độ chính xác** | Quyền riêng tư mạnh hơn (ε thấp hơn) đòi hỏi nhiều tiếng ồn hơn, làm giảm độ chính xác của mô hình |
| **Quyền riêng tư và thời gian đào tạo** | Nhiều tiếng ồn hơn có nghĩa là hội tụ chậm hơn |
| **Theo dõi ngân sách bảo mật** | Mỗi bước đào tạo tiêu tốn một phần ngân sách về quyền riêng tư; đã tiêu rồi thì không lấy lại được |
---

## Kết hợp Học tập Liên kết với Quyền riêng tư Khác biệt
| Lớp | Bảo vệ |
|-------|----------|
| **Học tập liên kết** | Dữ liệu thô vẫn còn trên thiết bị |
| **Quyền riêng tư khác biệt** | Ngay cả các bản cập nhật mô hình cũng ồn ào, bảo vệ những đóng góp của cá nhân |
| **Tập hợp an toàn** | Máy chủ chỉ nhìn thấy tổng hợp tất cả các bản cập nhật chứ không nhìn thấy từng bản cập nhật |
Sự kết hợp này mang lại sự đảm bảo mạnh mẽ về quyền riêng tư: ngay cả khi máy chủ bị xâm phạm, nó không thể xác định liệu có dữ liệu của cá nhân cụ thể nào được sử dụng trong quá trình đào tạo hay không.
---

## Các kỹ thuật bảo vệ quyền riêng tư khác
### Tính toán an toàn cho nhiều bên (SMPC)
Nhiều bên tính toán một hàm trên dữ liệu kết hợp của họ mà không tiết lộ đầu vào riêng lẻ của họ.
| Tính năng | Mô tả |
|----------|-------------|
| **Cách thức hoạt động** | Dữ liệu được chia thành các phần chia sẻ cho các bên; tính toán xảy ra trên cổ phiếu |
| **Đảm bảo** | Không bên nào biết được điều gì về ý kiến ​​đóng góp của bên kia |
| **Chi phí chung** | Chi phí truyền thông và tính toán đáng kể |
| **Trường hợp sử dụng** | Ngân hàng tính toán mô hình rủi ro chung mà không chia sẻ dữ liệu khách hàng |
### Mã hóa đồng cấu (HE)
Thực hiện tính toán trực tiếp trên dữ liệu được mã hóa.
| Loại | Nó hỗ trợ những gì | Chi phí chung |
|------|-------------------|----------|
| **Một phần HE** | Một thao tác (cộng HOẶC nhân) | Thấp |
| **Hơi HE** | Số lượng có hạn của cả hai hoạt động | Trung bình |
| **Hoàn toàn HE** | Tính toán tùy ý | Rất cao (chậm 100-1000 lần) |
| Ứng dụng | Mô tả |
|-------------|-------------|
| **Suy luận riêng** | Chạy mô hình ML trên dữ liệu được mã hóa; trả lại dự đoán được mã hóa |
| **Đào tạo được mã hóa** | Đào tạo về dữ liệu được mã hóa (chủ yếu vẫn là lý thuyết cho deep learning) |
| **Truy vấn riêng tư** | Truy vấn cơ sở dữ liệu mà không tiết lộ truy vấn hoặc dữ liệu |
### Môi trường thực thi đáng tin cậy (TEE)
Cách ly dựa trên phần cứng (Intel SGX, ARM Trustzone) giúp bảo vệ dữ liệu ngay cả từ hệ điều hành.
| Lợi thế | Hạn chế |
|----------||-------------|
| Hiệu suất gần như bản địa | Yêu cầu phần cứng cụ thể |
| Đảm bảo an ninh mạnh mẽ | Bộ nhớ hạn chế (kích thước bao vây) |
| Không có chi phí về mật mã | Có thể tấn công kênh bên |
---

## Quy định về quyền riêng tư và ML
| Quy định | Vùng | Tác động đến ML |
|-------------|--------|-------------|
| **GDPR** | EU | Quyền giải thích; giảm thiểu dữ liệu; đồng ý xử lý; quyền xóa |
| **CCPA** | California | Quyền được biết, xóa và từ chối bán dữ liệu |
| **HIPAA** | Hoa Kỳ (chăm sóc sức khỏe) | Kiểm soát chặt chẽ dữ liệu sức khỏe; yêu cầu hủy nhận dạng |
| **PIPL** | Trung Quốc | Bản địa hóa dữ liệu; yêu cầu chấp thuận; quy định chuyển tiền xuyên biên giới |
| **Đạo luật AI** | EU | Yêu cầu minh bạch; phân loại rủi ro; hành vi bị cấm |
### Tác động đến quy trình làm việc ML
| Nguyên tắc GDPR | Ý nghĩa ML |
|-------|--------------|
| **Giảm thiểu dữ liệu** | Chỉ thu thập những gì cần thiết; giúp học tập liên kết |
| **Giới hạn mục đích** | Không thể sử dụng lại dữ liệu nếu không có sự đồng ý mới |
| **Quyền xóa** | Phải có khả năng xóa dữ liệu của một người khỏi mô hình đã được đào tạo (loại bỏ máy) |
| **Quyền giải thích** | Các mô hình phải đủ dễ hiểu để giải thích các dự đoán riêng lẻ |
| **Quyền riêng tư theo thiết kế** | Quyền riêng tư phải được tích hợp vào hệ thống ngay từ đầu |
---

## Thử thách
| Thử thách | Mô tả |
|----------||-------------|
| **Chi phí truyền thông** | Gửi thông tin cập nhật mẫu qua hàng triệu thiết bị rất tốn kém |
| **Dữ liệu không phải IID** | Các thiết bị có sự phân bố dữ liệu rất khác nhau, làm ảnh hưởng đến sự hội tụ |
| **Người đi lạc** | Thiết bị chậm trì hoãn toàn bộ vòng đấu |
| **Đánh đổi quyền riêng tư-tiện ích** | Quyền riêng tư mạnh hơn có nghĩa là hiệu suất mô hình kém hơn |
| **Tấn công ngộ độc** | Những người tham gia độc hại có thể làm hỏng mô hình toàn cầu |
| **Trích xuất mô hình** | Ngay cả các bản cập nhật mô hình được chia sẻ cũng có thể rò rỉ thông tin về dữ liệu đào tạo |
| **Tính không đồng nhất của phần cứng** | Các thiết bị khác nhau có khả năng tính toán khác nhau |
---

## Công cụ và Khung
| Công cụ | Mục đích |
|------|----------|
| **Hoa** | Khung học tập liên kết nguồn mở; khuôn khổ bất khả tri |
| **Liên kết TensorFlow** | Khung FL của Google dành cho các mô hình TensorFlow |
| **PySyft** (OpenMined) | ML bảo vệ quyền riêng tư trong PyTorch |
| **Số phận** (Webank) | Nền tảng học tập liên kết cấp công nghiệp |
| **LÁ** | Bộ điểm chuẩn cho nghiên cứu học tập liên kết |
| **Opacus** (Meta) | Quyền riêng tư khác biệt cho PyTorch |
| **Quyền riêng tư TF của Google** | Quyền riêng tư khác biệt cho TensorFlow |
---

## Bản tóm tắt
Các kỹ thuật học tập liên kết và bảo vệ quyền riêng tư giải quyết một vấn đề căng thẳng cơ bản: làm cách nào để bạn xây dựng các mô hình AI mạnh mẽ khi dữ liệu được phân phối, nhạy cảm hoặc được quản lý? Học tập liên kết lưu giữ dữ liệu trên thiết bị và chỉ chia sẻ các bản cập nhật mô hình. Quyền riêng tư khác biệt bổ sung thêm các đảm bảo về mặt toán học rằng những đóng góp của cá nhân không thể bị phát hiện. Tính toán an toàn và mã hóa đồng cấu tiến xa hơn, cho phép tính toán trên dữ liệu được mã hóa. Mỗi kỹ thuật đều có chi phí – chi phí liên lạc, giảm độ chính xác, chi phí tính toán – nhưng chúng cùng nhau tạo thành một bộ công cụ để xây dựng AI tôn trọng quyền riêng tư trong khi vẫn học hỏi từ dữ liệu của thế giới.