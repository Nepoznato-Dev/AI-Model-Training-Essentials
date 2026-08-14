---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [computer, vision, ai-and-machine-learning]
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
# Nguyên tắc cơ bản về thị giác máy tính
Thị giác máy tính mang lại cho máy móc khả năng diễn giải và hiểu thông tin hình ảnh từ thế giới - hình ảnh, video và dữ liệu 3D. Nó hỗ trợ mọi thứ, từ nhận dạng khuôn mặt trên điện thoại đến ô tô tự lái, phân tích hình ảnh y tế và kiểm soát chất lượng công nghiệp. Tệp này bao gồm các khái niệm, kiến ​​trúc và kỹ thuật cốt lõi.
---

## Cách máy tính xem hình ảnh
### Pixel và kênh
Hình ảnh kỹ thuật số là một mạng lưới các pixel. Mỗi pixel có các giá trị số biểu thị cường độ màu.
| Loại hình ảnh | Kênh | Giá trị trên mỗi pixel | Ví dụ |
|----------|----------|--------|---------|
| **Thang độ xám** | 1 | 0 (đen) đến 255 (trắng) | Chụp X-quang y tế |
| **RGB** | 3 | Đỏ, Xanh lục, Xanh lam (mỗi 0–255) | Ảnh màu chuẩn |
| **RGBA** | 4 | RGB + Alpha (trong suốt) | Hình ảnh có nền trong suốt |
| **HSV** | 3 | Huế, Độ bão hòa, Giá trị | Phân khúc dựa trên màu sắc |
Hình ảnh 1920×1080 RGB là một tenxơ có hình dạng`(1080, 1920, 3)`— tức là 6,2 triệu pixel, mỗi pixel có 3 giá trị.
### Thao tác chính
| Hoạt động | Mô tả |
|----------||-------------|
| **Thay đổi kích thước** | Chia tỷ lệ hình ảnh theo kích thước mục tiêu (nội suy song tuyến, lân cận gần nhất) |
| **Cắt xén** | Trích xuất một vùng quan tâm |
| **Bình thường hóa** | Chia tỷ lệ giá trị pixel thành [0,1] hoặc [-1,1] cho mạng thần kinh |
| **Tăng cường** | Mở rộng dữ liệu huấn luyện một cách giả tạo (xoay, lật, giật màu, cắt) |
---

## Tích chập: Hoạt động cốt lõi
Một tích chập trượt một bộ lọc nhỏ (hạt nhân) trên hình ảnh, tính toán tích số chấm tại mỗi vị trí. Đây là cách CNN phát hiện các cạnh, kết cấu và kiểu mẫu.
### Tham số tích chập
| Tham số | Hiệu ứng |
|----------||--------|
| **Kích thước hạt** | 3×3, 5×5, 7×7 — hạt nhân lớn hơn chụp được các mẫu lớn hơn |
| **Sải bước** | Kích thước bước; sải chân = 2 giảm một nửa kích thước đầu ra |
| **Đệm** | Thêm số không xung quanh đường viền để bảo toàn kích thước không gian |
| **Số lượng bộ lọc** | Mỗi bộ lọc tìm hiểu một tính năng khác nhau (cạnh, kết cấu, mẫu màu) |
### Học những gì về sự kết hợp
| Độ sâu lớp | Tính năng được phát hiện |
|-------------|-------------------|
| **Lớp đầu** | Các cạnh, góc, họa tiết đơn giản |
| **Lớp giữa** | Hình dạng, bộ phận đồ vật (bánh xe, mắt, lá) |
| **Lớp sâu** | Khái niệm cấp cao (khuôn mặt, ô tô, động vật) |
---

## Kiến trúc CNN
Sự phát triển của kiến ​​trúc CNN kể câu chuyện về sự tiến bộ của deep learning trong thị giác máy tính.
| Kiến trúc | Năm | Đổi mới quan trọng |
|-------------|------|---------------|
| **LeNet-5** | 1998 | CNN thực tế đầu tiên; nhận dạng chữ số |
| **AlexNet** | 2012 | CNN sâu thắng ImageNet; ReLU, bỏ học, đào tạo GPU |
| **VGGNet** | 2014 | Tích chập 3×3 xếp chồng lên nhau (sâu hơn = tốt hơn) |
| **GoogLeNet (Khởi đầu)** | 2014 | Mô-đun khởi động (kích thước bộ lọc song song); 22 lớp |
| **ResNet** | 2015 | Bỏ qua kết nối (học tập còn lại); Hơn 152 lớp |
| **Mạng hiệu quả** | 2019 | Chia tỷ lệ tổng hợp (độ sâu + chiều rộng + độ phân giải) |
| **ConvNeXt** | 2022 | ResNet hiện đại hóa; cạnh tranh với Transformers |
### Tại sao ResNet lại thay đổi mọi thứ
Trước ResNet, việc đào tạo các mạng rất sâu gần như không thể do vấn đề độ dốc biến mất. ResNet đã giới thiệu **bỏ qua kết nối** (còn gọi là kết nối dư): đầu vào của một lớp được thêm vào đầu ra của nó.
```
output = F(x) + x    # Skip connection
```

Ý tưởng đơn giản này cho phép các mạng có hơn 152 lớp được đào tạo một cách hiệu quả và giờ đây nó trở thành tiêu chuẩn trong hầu hết tất cả các kiến ​​trúc sâu.
---

## Nhiệm vụ tầm nhìn cốt lõi
### Phân loại hình ảnh
Gán nhãn cho toàn bộ hình ảnh.
| Người mẫu | Tiếp cận |
|-------|----------|
| CNN (ResNet, EfficiencyNet) | Cách tiếp cận truyền thống; độ chính xác tuyệt vời |
| Máy biến áp tầm nhìn (ViT) | Coi hình ảnh như một chuỗi các bản vá; Bộ mã hóa máy biến áp |
| Chuyển tiếp học tập | Tinh chỉnh mô hình được đào tạo trước trên tập dữ liệu của bạn |
### Phát hiện đối tượng
Tìm và phân loại nhiều đối tượng trong một hình ảnh bằng các hộp giới hạn.
| Người mẫu | Loại | Tốc độ |
|-------|------|-------|
| **R-CNN** | Hai giai đoạn (đề xuất + phân loại) | Chậm |
| **R-CNN nhanh** | Cải tiến hai giai đoạn | Trung bình |
| **R-CNN nhanh hơn** | Mạng đề xuất khu vực + máy dò | Trung bình |
| **YOLO** (v1–v10) | Một giai đoạn; hộp dự đoán + lớp học trong một lần | Rất nhanh |
| **DETR** | Dựa trên máy biến áp; không có hộp neo | Trung bình |
**YOLO** (You Only Look Once) là công cụ phát hiện theo thời gian thực. **R-CNN nhanh hơn** được ưu tiên khi độ chính xác quan trọng hơn tốc độ.
### Phân đoạn hình ảnh
Phân loại từng pixel trong một hình ảnh.
| Loại | Mô tả | Trường hợp sử dụng |
|------|-------------|----------|
| **Phân đoạn ngữ nghĩa** | Mỗi pixel có một nhãn lớp | Lái xe tự động (đường bộ, ô tô, người đi bộ) |
| **Phân đoạn phiên bản** | Mỗi pixel + ID phiên bản đối tượng | Đếm đồ vật, hình ảnh y tế |
| **Phân đoạn toàn cảnh** | Kết hợp ngữ nghĩa + ví dụ | Hiểu biết toàn diện về cảnh |
Các mô hình chính: U-Net (hình ảnh y tế), Mask R-CNN (ví dụ), DeepLab (ngữ nghĩa), Mô hình phân đoạn bất kỳ (SAM - phân đoạn phổ quát).
### Tạo hình ảnh
| Tiếp cận | Mô tả | Ví dụ |
|----------|-------------|----------|
| **GAN** | Đào tạo đối lập giữa người tạo và người phân biệt đối xử | StyleGAN, CycleGAN |
| **VAE** | Tìm hiểu phân phối tiềm ẩn; mẫu để tạo | Bộ mã hóa tự động biến thể |
| **Mô hình khuếch tán** | Khử nhiễu ngẫu nhiên lặp đi lặp lại | Khuếch tán ổn định, DALL-E, Giữa hành trình |
Các mô hình khuếch tán phần lớn đã vượt qua GAN về chất lượng tạo hình ảnh.
---

## Chuyển giao học tập cho tầm nhìn
Đào tạo CNN từ đầu đòi hỏi dữ liệu và tính toán lớn. Học chuyển giao cho phép bạn bắt đầu với một mô hình đã được đào tạo trên hàng triệu hình ảnh (ImageNet) và tinh chỉnh mô hình đó cho nhiệm vụ cụ thể của bạn.
### bước
1. **Chọn mô hình được đào tạo trước** (ResNet50, EfficiencyNet-B0, ViT).
2. **Thay thế đầu phân loại** bằng đầu phân loại của riêng bạn (phù hợp với số lớp của bạn).
3. **Đóng băng các lớp đầu** (chúng nắm bắt các đặc điểm chung như các cạnh).
4. **Tinh chỉnh** trên tập dữ liệu của bạn với tỷ lệ học tập thấp.
5. **Giải phóng dần dần** nếu bạn cần thích ứng nhiều hơn.
Cách tiếp cận này thường xuyên đạt được độ chính xác cao chỉ với 1.000–10.000 hình ảnh được dán nhãn.
---

## Tăng cường dữ liệu
Việc tăng cường mở rộng tập dữ liệu huấn luyện của bạn một cách giả tạo bằng cách áp dụng các phép biến đổi.
| Tăng cường | Hiệu ứng | Khi nào nên sử dụng |
|-------------|--------|-------------|
| **Cắt ngẫu nhiên** | Cắt theo vùng ngẫu nhiên | Hầu như luôn luôn |
| **Lật ngang** | Hình ảnh phản chiếu | Khi định hướng không quan trọng |
| **Xoay** | Xoay theo góc ngẫu nhiên | Khi vật thể xuất hiện ở mọi góc độ |
| **Giật màu** | Điều chỉnh ngẫu nhiên độ sáng, độ tương phản, độ bão hòa | Khi ánh sáng thay đổi |
| **Xóa ngẫu nhiên** | Mặt nạ vùng ngẫu nhiên | Cải thiện độ bền |
| **Trộn / CắtMix** | Trộn hai hình ảnh và nhãn | Chính quy hóa |
Thư viện:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Công cụ và Khung
| Công cụ | Mục đích |
|------|----------|
| **OpenCV** | Hoạt động CV cổ điển (lọc, phát hiện cạnh, biến đổi hình học) |
| **ngọn đuốc** | Mô hình tầm nhìn, biến đổi, bộ dữ liệu PyTorch |
| **tf.keras.applications** | Các mô hình được đào tạo trước trong TensorFlow/Keras |
| **Siêu phân tích (YOLOv8/v11)** | Phát hiện, phân đoạn, phân loại đối tượng |
| **Ôm Mặt (Transformers)** | Máy biến áp tầm nhìn, SegFormer, DETR |
| **Phân khúc mọi thứ (SAM)** | Phân đoạn hình ảnh phổ quát từ Meta |
| **Albumation** | Thư viện tăng cường hình ảnh nhanh chóng, linh hoạt |
---

## Lời khuyên thiết thực
- **Bắt đầu bằng phương pháp học chuyển tiếp.** Tinh chỉnh mô hình được đào tạo trước sẽ đánh bại việc đào tạo từ đầu trong hầu hết mọi trường hợp.
- **Chuẩn hóa thông tin đầu vào của bạn.** Khớp mức chuẩn hóa mà mô hình được đào tạo trước mong đợi (thường là giá trị trung bình/tiêu chuẩn của ImageNet).
- **Sử dụng số liệu thích hợp.** Độ chính xác cho bộ dữ liệu cân bằng; F1, mAP hoặc IoU cho các tác vụ phát hiện hoặc mất cân bằng.
- **Trực quan hóa dữ liệu của bạn.** Xem hình ảnh mẫu, kiểm tra phân bổ lớp, kiểm tra dự đoán mô hình.
- **Tăng cường một cách khôn ngoan.** Chỉ áp dụng các phép biến đổi có ý nghĩa cho miền của bạn (không lật hình ảnh y tế theo chiều dọc).
- **Giám sát quá mức.** Nếu độ chính xác của quá trình đào tạo cao nhưng xác thực thấp, hãy tăng cường hoặc thêm bỏ học.