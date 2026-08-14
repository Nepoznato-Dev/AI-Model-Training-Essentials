---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [recommendation, systems, ai-and-machine-learning]
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
# Hệ thống khuyến nghị
Hệ thống đề xuất dự đoán những gì người dùng sẽ muốn xem, mua hoặc tương tác tiếp theo. Chúng cung cấp nguồn cấp dữ liệu nội dung trên mạng xã hội, đề xuất sản phẩm trên các trang thương mại điện tử, lựa chọn phim trên nền tảng phát trực tuyến và kết quả tìm kiếm. Mặc dù vô hình đối với hầu hết người dùng, nhưng chúng nằm trong số những hệ thống AI có tác động thương mại nhất trên thế giới - Netflix ước tính công cụ đề xuất của họ tiết kiệm hơn 1 tỷ USD mỗi năm bằng cách giảm tỷ lệ người đăng ký rời bỏ.
---

## Tại sao đề xuất lại khó
| Thử thách | Mô tả |
|----------||-------------|
| **Tỷ lệ** | Hàng triệu người dùng × hàng triệu mặt hàng = hàng tỷ cặp có thể có |
| **Sự thưa thớt** | Mỗi người dùng đã tương tác với một phần rất nhỏ các mặt hàng có sẵn |
| **Khởi động nguội** | Người dùng mới và vật phẩm mới không có lịch sử tương tác |
| **Tùy chọn động** | Thị hiếu người dùng thay đổi theo thời gian |
| **Ngoài độ chính xác** | Các đề xuất cũng phải đa dạng, mới lạ và tình cờ |
| **Mục tiêu kinh doanh** | Tối đa hóa mức độ tương tác ≠ tối đa hóa phúc lợi của người dùng |
---

## Phương pháp tiếp cận cốt lõi
### Lọc cộng tác
Ý tưởng: nếu người dùng A và B đã đồng ý trước đây thì có thể họ sẽ đồng ý trong tương lai.
| Loại | Nó hoạt động như thế nào | Ví dụ |
|------|-------------|----------|
| **Dựa trên người dùng** | Tìm người dùng tương tự; giới thiệu những gì họ thích | "Người dùng thích điều này cũng thích..." |
| **Dựa trên vật phẩm** | Tìm các mục tương tự với những gì người dùng đã thích | "Bởi vì bạn đã xem..." |
| **Nhân tử ma trận** | Phân tách ma trận tương tác giữa người dùng và mục thành các yếu tố tiềm ẩn | SVD, ALS (Bình phương nhỏ nhất xen kẽ) |
| Sức mạnh | Điểm yếu |
|----------|----------|
| Không cần phải hiểu bản thân các mục | Vấn đề khởi đầu nguội: không thể đề xuất mặt hàng mới |
| Nắm bắt các sở thích phức tạp, tiềm ẩn | Yêu cầu nhiều dữ liệu tương tác |
| Hoạt động trên mọi loại nội dung | Xu hướng phổ biến: đề xuất các mặt hàng đã phổ biến |
### Lọc dựa trên nội dung
Đề xuất các mặt hàng tương tự với những mặt hàng mà người dùng đã thích, dựa trên tính năng của mặt hàng.
| Loại tính năng | Ví dụ |
|-------------|----------|
| **Văn bản** | Thể loại, mô tả, từ khóa, diễn viên |
| **Âm thanh** | Nhịp độ, thể loại, tâm trạng (dành cho âm nhạc) |
| **Trực quan** | Bảng màu, phong cách (cho hình ảnh/thời trang) |
| **Siêu dữ liệu** | Giá, nhãn hiệu, chủng loại |
| Sức mạnh | Điểm yếu |
|----------|----------|
| Không có khởi động nguội cho các hạng mục (các tính năng đã được biết) | Không thể đề xuất các mặt hàng ngoài sở thích hiện có của người dùng |
| Hoạt động với ít dữ liệu tương tác hơn | Yêu cầu kỹ thuật tính năng tốt |
| Có thể giải thích ("được khuyến nghị vì nó tương tự như X") | Ít tình cờ hơn |
### Phương pháp tiếp cận kết hợp
Hầu hết các hệ thống sản xuất đều kết hợp các phương pháp hợp tác và dựa trên nội dung.
| Chiến lược lai | Mô tả |
|-------|-------------|
| **Có trọng số** | Kết hợp điểm số từ nhiều mô hình |
| **Chuyển đổi** | Sử dụng dựa trên nội dung cho người dùng mới, cộng tác cho những người đã thành lập |
| **Thác** | Trước tiên hãy sử dụng mô hình đơn giản, sau đó tinh chỉnh bằng mô hình phức tạp |
| **Kết hợp tính năng** | Hợp nhất các tính năng cộng tác và nội dung thành một mô hình duy nhất |
| **Siêu học tập** | Tìm hiểu cách kết hợp những người giới thiệu khác nhau |
---

## Phương pháp học sâu hiện đại
###Mô hình 2 tòa tháp
Kiến trúc chủ đạo dành cho đề xuất quy mô lớn (được YouTube, Pinterest, Spotify sử dụng).
| Thành phần | Vai trò |
|----------||------|
| **Tháp người dùng** | Mạng thần kinh mã hóa các tính năng và lịch sử của người dùng thành một phần nhúng |
| **Tháp vật phẩm** | Mạng thần kinh mã hóa các tính năng của vật phẩm thành một phần nhúng |
| **Sự tương đồng** | Điểm tương đồng của sản phẩm hoặc cosine giữa phần nhúng của người dùng và vật phẩm |
| Bước | Mô tả |
|------|-------------|
| 1 | Huấn luyện cả hai tòa tháp để tạo ra các phần nhúng tương tự cho các cặp vật phẩm người dùng tương tác |
| 2 | Tại thời điểm phân phát, hãy tính toán trước phần nhúng mục |
| 3 | Đối với yêu cầu của người dùng, hãy tính toán nhúng của người dùng |
| 4 | Sử dụng tìm kiếm hàng xóm gần nhất (ANN) gần đúng để tìm các mục tương tự nhất |
### Mô hình trình tự cho khuyến nghị
Hành vi của người dùng là tuần tự — nội dung bạn xem ngày hôm qua sẽ ảnh hưởng đến nội dung bạn sẽ xem hôm nay.
| Người mẫu | Tiếp cận |
|-------|----------|
| **GRU4Rec** | Mô hình dựa trên GRU cho các đề xuất dựa trên phiên |
| **SASRec** | Người giới thiệu tuần tự dựa trên sự chú ý |
| **BERT4Rec** | Biến áp hai chiều cho các khuyến nghị tuần tự |
| **YouTube DNN** | Mạng lưới thần kinh sâu xử lý lịch sử xem như một chuỗi |
### Truy xuất và xếp hạng
Các hệ thống hiện đại chia khuyến nghị thành hai giai đoạn:
| Sân khấu | Mục đích | Phương pháp |
|-------|----------|--------|
| **Truy xuất (tạo ứng viên)** | Thu hẹp hàng triệu mặt hàng xuống ~1.000 ứng viên | Mô hình hai tháp; tìm kiếm ANN; nhanh nhưng gần đúng |
| **Xếp hạng (ghi điểm)** | Chấm điểm và sắp xếp ứng viên chính xác | Mô hình sâu sắc với nhiều tính năng; chậm hơn nhưng chính xác |
| **Xếp hạng lại** | Điều chỉnh cho sự đa dạng, quy tắc kinh doanh, sự mới mẻ | Kẻ cướp theo ngữ cảnh; tối ưu hóa ràng buộc |
---

## Số liệu đánh giá
| Số liệu | Nó đo lường những gì | Khi nào nên sử dụng |
|--------|-------------------|-------------|
| **Độ chính xác@K** | Tỷ lệ đề xuất top-K có liên quan | Khi bạn quan tâm đến độ chính xác của các lựa chọn hàng đầu |
| **Nhớ lại@K** | Tỷ lệ các mục có liên quan được tìm thấy trong top-K | Khi bạn quan tâm không thiếu đồ tốt |
| **NDCG** (Mức tăng tích lũy chiết khấu chuẩn hóa) | Xếp hạng chất lượng; phần thưởng đưa các mặt hàng có liên quan cao hơn | Khi thứ tự xếp hạng quan trọng |
| **MAP** (Độ chính xác trung bình trung bình) | Độ chính xác trung bình trên tất cả người dùng | Chất lượng xếp hạng tổng thể |
| **Tỷ lệ truy cập@K** | Liệu có ít nhất một mục liên quan xuất hiện trong top-K | Kịch bản liên quan nhị phân |
| **Phạm vi bảo hiểm** | Tỷ lệ các mặt hàng được đề xuất | Đa dạng và công bằng |
| **Tình cờ** | Khuyến nghị bất ngờ nhưng có liên quan | Sự hài lòng của người dùng |
---

## Vấn đề khởi đầu nguội
| Kịch bản | Thử thách | Giải pháp |
|----------|--------------|----------|
| **Người dùng mới** | Không có lịch sử tương tác | Sử dụng nhân khẩu học; hiển thị các mặt hàng phổ biến; sử dụng tín hiệu theo ngữ cảnh (vị trí, thiết bị, thời gian) |
| **Hàng mới** | Chưa có ai tương tác với nó | Sử dụng các tính năng nội dung; chiến lược khám phá-khai thác; thuật toán cướp |
| **Hệ thống mới** | Không có dữ liệu nào cả | Chuyển giao việc học từ các lĩnh vực tương tự; quản lý nội dung ban đầu |
---

## Thăm dò và Khai thác
| Chiến lược | Mô tả | Đánh đổi |
|----------|-------------|----------|
| **ε-tham lam** | Hiển thị các mục ngẫu nhiên với xác suất ε | Đơn giản nhưng không hiệu quả |
| **Lấy mẫu Thompson** | Mẫu từ phân phối sau của chất lượng mặt hàng | Nguyên tắc; tính chất lý thuyết tốt |
| **Giới hạn niềm tin trên (UCB)** | Ưu tiên các mặt hàng có độ không chắc chắn cao | Cân bằng tốt giữa thăm dò và khai thác |
| **Kẻ cướp theo ngữ cảnh** | Khám phá dựa trên bối cảnh người dùng | Hiệu quả hơn thăm dò mù quáng |
| **Tiêm đa dạng** | Cố tình đưa vào các mặt hàng đa dạng hoặc mới lạ | Đơn giản; có thể làm giảm sự tham gia ngắn hạn |
---

## Thiên vị và Công bằng
| Loại thiên vị | Mô tả | Tác động |
|----------|-------------|--------|
| **Thành kiến ​​phổ biến** | Các mặt hàng phổ biến được đề xuất nhiều hơn, trở nên phổ biến hơn | Các mặt hàng đuôi dài không được phục vụ đầy đủ |
| **Thành kiến ​​lựa chọn** | Các mô hình học hỏi từ các tương tác được quan sát, không phải tất cả các tương tác có thể xảy ra | Nghiêng về phía người dùng tích cực |
| **Thành kiến ​​về vị trí** | Các mục hiển thị ở vị trí cao hơn nhận được nhiều nhấp chuột hơn bất kể chất lượng | Củng cố các vị trí hàng đầu |
| **Thành kiến ​​tiếp xúc** | Các mục đã được hiển thị nhận được nhiều tín hiệu đào tạo hơn | Vòng phản hồi |
| **Thành kiến ​​nhân khẩu học** | Các đề xuất khác nhau giữa các nhóm nhân khẩu học theo những cách không công bằng | Phân biệt; kinh nghiệm kém cho một số nhóm |
### Chiến lược giảm thiểu
| Chiến lược | Mô tả |
|----------|-------------|
| **Trọng số xu hướng nghịch đảo** | Vật dụng giảm cân phổ biến trong tập luyện |
| **Lớp khử thiên vị** | Thêm thành phần khử sai lệch vào mô hình |
| **Ràng buộc công bằng** | Thêm các ràng buộc để đảm bảo đối xử công bằng |
| **Khuyến nghị đa dạng** | Tối ưu hóa rõ ràng để đảm bảo tính đa dạng bên cạnh mức độ liên quan |
| **Kiểm toán và giám sát** | Thường xuyên kiểm tra các đề xuất về sự thiên vị giữa các nhóm |
---

## Ví dụ về ngành
| Công ty | Hệ thống | Tiếp cận |
|----------|--------|----------|
| **Netflix** | Đề xuất phim/truyền hình | Truy xuất hai tháp + xếp hạng sâu + kẻ cướp theo ngữ cảnh cho tác phẩm nghệ thuật |
| **YouTube** | Đề xuất video | Mạng lưới thần kinh sâu để tạo ứng viên; mô hình xếp hạng riêng biệt |
| **Spotify** | Đề xuất âm nhạc | Lọc cộng tác + NLP trên danh sách phát + phân tích âm thanh |
| **Amazon** | Khuyến nghị sản phẩm | Lọc cộng tác từng mục; được cá nhân hóa ở quy mô |
| **TikTok** | Nguồn cấp dữ liệu video ngắn | Học tăng cường; nhấn mạnh vào việc thăm dò |
| **Pinterest** | Khuyến nghị trực quan | Mô hình hai tháp; sự tương đồng về hình ảnh |
---

## Công cụ và Khung
| Công cụ | Mục đích |
|------|----------|
| **Công cụ đề xuất TensorFlow (TFRS)** | Mô hình hai tháp, thu hồi, xếp hạng |
| **PyTorch RecSys** | Mô hình khuyến nghị theo định hướng nghiên cứu |
| **Bất ngờ** | Lọc cộng tác cổ điển (SVD, NMF, KNN) |
| **Ngầm** | Lọc cộng tác nhanh cho phản hồi ngầm (ALS, BPR) |
| **Faiss** (Meta) | Tìm kiếm hàng xóm gần nhất ở quy mô lớn |
| **Milvus / Pinecone / Weaviate** | Cơ sở dữ liệu vector để tìm kiếm sự tương đồng |
| **Recbole** | Thư viện nghiên cứu đề xuất toàn diện |
| **Merlin** (NVIDIA) | Đường dẫn đề xuất tăng tốc GPU |
---

## Bản tóm tắt
Hệ thống khuyến nghị là một trong những ứng dụng AI có ảnh hưởng nhất trong ngành. Lĩnh vực này đã phát triển từ lọc cộng tác đơn giản đến kiến ​​trúc học sâu kết hợp lịch sử người dùng, nội dung mục, tín hiệu theo ngữ cảnh và mục tiêu kinh doanh. Các hệ thống hiện đại sử dụng quy trình truy xuất-xếp hạng-tái xếp hạng, với các mô hình hai tháp để tạo ứng viên nhanh chóng và các mô hình sâu để chấm điểm chính xác. Những thách thức - khởi đầu nguội, thiên vị, thăm dò và cân bằng sự hài lòng của người dùng với mục tiêu kinh doanh - vẫn là lĩnh vực hoạt động nghiên cứu và kỹ thuật.