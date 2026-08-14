---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
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
tags: [graph, neural, networks, ai-and-machine-learning]
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

# Mạng lưới thần kinh đồ thị
Mạng thần kinh đồ thị (GNN) là mạng thần kinh được thiết kế để hoạt động trên dữ liệu có cấu trúc đồ thị - mạng gồm các nút được kết nối bởi các cạnh. Trong khi mạng thần kinh truyền thống hoạt động trên lưới (hình ảnh) hoặc chuỗi (văn bản), GNN xử lý các cấu trúc quan hệ tùy ý: mạng xã hội, biểu đồ phân tử, biểu đồ tri thức, mạng đường bộ, biểu đồ đề xuất, v.v. Chúng đã trở nên cần thiết cho việc khám phá ma túy, phát hiện gian lận, hệ thống khuyến nghị và bất kỳ lĩnh vực nào mà mối quan hệ giữa các thực thể là quan trọng.
---

## Đồ thị là gì?
| Thành phần | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Nút (đỉnh)** | Một thực thể | Một con người, một nguyên tử, một thành phố |
| **Cạnh** | Mối quan hệ giữa hai nút | Tình bạn, sự gắn kết hóa học, con đường |
| **Trọng lượng cạnh** | Sức mạnh hoặc loại mối quan hệ | Khoảng cách, sự tương đồng, năng lực |
| **Tính năng nút** | Thuộc tính của mỗi nút | Tuổi, số nguyên tử, dân số |
| **Tính năng cạnh** | Thuộc tính của từng cạnh | Kiểu quan hệ, khoảng cách |
| **Ma trận kề** | Ma trận A trong đó A[i][j] = 1 nếu nút i và j được kết nối | Mã hóa cấu trúc đồ thị |
### Các loại biểu đồ
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Không được định hướng** | Các cạnh không có hướng | Mạng lưới tình bạn |
| **Đạo diễn** | Các cạnh có hướng (A→B ≠ B→A) | Người theo dõi Twitter |
| **Có trọng số** | Các cạnh có giá trị bằng số | Mạng lưới đường bộ với khoảng cách |
| **Không đồng nhất** | Nhiều loại nút và cạnh | Biểu đồ học thuật (bài báo, tác giả, địa điểm) |
| **Năng động** | Cấu trúc đồ thị thay đổi theo thời gian | Mạng xã hội phát triển theo thời gian |
| **Lưỡng đảng** | Hai loại nút; chỉ các cạnh giữa các loại | Biểu đồ đề xuất mục người dùng |
---

## Tại sao không phải là Mạng thần kinh thông thường?
| Tiếp cận | Tại sao nó thất bại |
|----------|-------------|
| **Mạng chuyển tiếp nguồn cấp dữ liệu** | Yêu cầu đầu vào có kích thước cố định; đồ thị có kích thước và cấu trúc khác nhau |
| **CNN** | Giả sử cấu trúc lưới; đồ thị không có lưới thông thường |
| **RNN/Máy biến áp** | Giả sử thứ tự tuần tự; đồ thị không có thứ tự tự nhiên |
GNN giải quyết vấn đề này bằng cách hoạt động trực tiếp trên cấu trúc biểu đồ, xử lý từng nút trong bối cảnh các nút lân cận của nó.
---

## Kiến trúc GNN cốt lõi
### Khung truyền tin nhắn
Hầu hết các GNN đều tuân theo cùng một mẫu: mỗi nút thu thập thông tin từ các nút lân cận, kết hợp thông tin đó và cập nhật cách trình bày của chính nó.
| Bước | Mô tả |
|------|-------------|
| **1. Tin nhắn** | Mỗi nút gửi một tin nhắn đến các nút lân cận (dựa trên các tính năng hiện tại của nó) |
| **2. Tổng hợp** | Mỗi nút thu thập và kết hợp các tin nhắn từ tất cả các nút lân cận |
| **3. Cập nhật** | Mỗi nút cập nhật cách trình bày riêng của mình bằng cách sử dụng thông báo tổng hợp |
| **4. Lặp lại** | Thực hiện việc này cho K lớp → mỗi nút nắm bắt thông tin từ K bước nhảy |
### Các mô hình GNN chính
| Người mẫu | Phương pháp tổng hợp | Đổi mới quan trọng |
|-------|-------------------|----------------|
| **GCN** (Mạng tích chập đồ thị) | Ý nghĩa của các tính năng lân cận | Đơn giản; hiệu quả; động lực quang phổ |
| **GraphSAGE** | Mẫu và tổng hợp; có thể sử dụng giá trị trung bình, LSTM hoặc gộp | Quy nạp (xử lý các nút không nhìn thấy); có thể mở rộng |
| **GAT** (Mạng lưới chú ý đồ thị) | Tổng hợp hàng xóm có trọng số chú ý | Tìm hiểu những người hàng xóm nào quan trọng nhất |
| **GIN** (Mạng đẳng cấu đồ thị) | Tổng hợp các tính năng lân cận | Biểu cảm tối đa; có thể phân biệt bất kỳ biểu đồ nào có thể phân biệt được bằng bài kiểm tra WL |
| **MPNN** (Mạng thần kinh truyền tin nhắn) | Khung truyền thông điệp chung | Hợp nhất nhiều biến thể GNN |
### Cách thức hoạt động của GCN (Từng bước)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Sau K lớp, cách biểu diễn của mỗi nút sẽ mã hóa thông tin từ K bước nhảy trong biểu đồ.
---

## Nhiệm vụ cấp đồ thị
| Nhiệm vụ | Mô tả | Ví dụ |
|------|-------------|----------|
| **Phân loại nút** | Dự đoán nhãn của từng nút | Phân loại người dùng là bot hay con người |
| **Dự đoán liên kết** | Dự đoán liệu một cạnh có tồn tại (hoặc sẽ tồn tại) | Dự đoán các mối quan hệ còn thiếu; giới thiệu kết nối |
| **Phân loại đồ thị** | Dự đoán nhãn cho toàn bộ biểu đồ | Phân loại các phân tử độc hại hoặc không độc hại |
| **Phát hiện cộng đồng** | Tìm cụm nút kết nối dày đặc | Xác định các nhóm xã hội |
| **Tạo đồ thị** | Tạo biểu đồ mới với các thuộc tính mong muốn | Thiết kế phân tử mới |
---

## Ứng dụng
### Khám phá thuốc và dự đoán đặc tính phân tử
| Nhiệm vụ | GNN trợ giúp như thế nào |
|------|--------------|
| **Dự đoán tính chất phân tử** | Biểu diễn các phân tử dưới dạng đồ thị (nguyên tử=nút, liên kết=cạnh); dự đoán độc tính, độ hòa tan, ái lực gắn kết |
| **Tương tác thuốc-thuốc** | Mô hình thuốc và mục tiêu dưới dạng biểu đồ; dự đoán tương tác bất lợi |
| **Thiết kế thuốc mới** | Tạo đồ thị phân tử mới với các đặc tính mong muốn |
### Hệ thống khuyến nghị
| Tiếp cận | Mô tả |
|----------|-------------|
| **Biểu đồ mục người dùng** | Người dùng và vật phẩm là các nút; lượt mua/lượt xem là lợi thế |
| **Lọc cộng tác dựa trên đồ thị** | GNN truyền bá các tùy chọn thông qua biểu đồ |
| **Khuyến nghị về biểu đồ tri thức** | Kết hợp sở thích của người dùng với kiến ​​thức về mục (thể loại, diễn viên, đạo diễn) |
### Phát hiện gian lận
| Ứng dụng | Cấu trúc đồ thị |
|-------------|----------------|
| **Gian lận tài chính** | Giao dịch tạo thành một biểu đồ; các mô hình lừa đảo xuất hiện dưới dạng cấu trúc đồ thị con |
| **Gian lận bảo hiểm** | Người yêu cầu bồi thường, nhà cung cấp và chính sách tạo thành một biểu đồ; vòng lừa đảo bị phát hiện |
| **Tiếp quản tài khoản** | Các mẫu đăng nhập tạo thành một biểu đồ; thỏa hiệp tín hiệu kết nối bất thường |
### Sơ đồ tri thức
| Nhiệm vụ | Mô tả |
|------|-------------|
| **Dự đoán liên kết** | Dự đoán những thông tin còn thiếu (ví dụ: "Paris là thủ đô của?") |
| **Giải quyết thực thể** | Xác định xem hai đề cập có đề cập đến cùng một thực thể hay không |
| **Trả lời câu hỏi** | Điều hướng biểu đồ để tìm câu trả lời |
---

## Khái niệm GNN nâng cao
### Làm mịn quá mức
| Vấn đề | Mô tả | Giải pháp |
|----------|-------------|----------|
| **Làm mịn quá mức** | Sau nhiều lớp, tất cả các biểu diễn nút trở nên giống nhau | Độ sâu giới hạn (2-4 lớp); sử dụng các kết nối còn lại; sử dụng Kiến thức Nhảy |
### Đè quá mức
| Vấn đề | Mô tả | Giải pháp |
|----------|-------------|----------|
| **Đè bẹp quá mức** | Thông tin từ các nút ở xa được nén thành các vectơ có kích thước cố định | Sử dụng máy biến đổi đồ thị; tổng hợp theo thứ bậc |
### Máy biến đổi đồ thị
| Người mẫu | Tính năng chính |
|-------|-------------|
| **Biến đổi đồ thị** | Áp dụng sự chú ý của Transformer tiêu chuẩn cho tất cả các cặp nút |
| **GPS** (Hệ thống nhắc đồ thị) | Kết hợp các lớp GNN cục bộ với các lớp Transformer toàn cầu |
| **Nhà vẽ đồ họa** | Thêm mã hóa vị trí dựa trên cấu trúc biểu đồ |
### Mạng đồ thị không đồng nhất
| Người mẫu | Mô tả |
|-------|-------------|
| **R-GCN** | GCN quan hệ; ma trận trọng số khác nhau cho các loại cạnh khác nhau |
| **HAN** | Mạng chú ý không đồng nhất; chú ý đến các loại nút và cạnh khác nhau |
| **HetGNN** | Mạng lưới thần kinh đồ thị không đồng nhất; xử lý nhiều loại nút |
---

## Khả năng mở rộng
| Thử thách | Giải pháp |
|----------||----------|
| **Biểu đồ lớn** (hàng triệu nút) | Đào tạo theo đợt nhỏ; lấy mẫu hàng xóm |
| **Bộ nhớ** | Phân vùng đồ thị trên GPU |
| **Tốc độ** | Hoạt động ma trận thưa thớt; thư viện chuyên ngành |
### Chiến lược lấy mẫu
| Chiến lược | Mô tả |
|----------|-------------|
| **Lấy mẫu nút** | Lấy mẫu một tập hợp con các nút và vùng lân cận K-hop của chúng |
| **Lấy mẫu cạnh** | Các cạnh mẫu và các nút mà chúng kết nối |
| **Lấy mẫu cụm** | Phân chia đồ thị thành các cụm; tàu theo cụm |
| **Lấy mẫu bước đi ngẫu nhiên** | Các nút mẫu thông qua các bước đi ngẫu nhiên từ các nút mục tiêu |
---

## Công cụ và Khung
| Công cụ | Mục đích |
|------|----------|
| **Hình học PyTorch (PyG)** | Thư viện GNN phổ biến nhất; bộ mô hình và bộ dữ liệu phong phú |
| **DGL** (Thư viện đồ thị sâu) | Khung bất khả tri; hỗ trợ PyTorch, TensorFlow, MXNet |
| **MạngX** | Các thuật toán đồ thị cổ điển; thao tác dữ liệu |
| **OGB** (Điểm chuẩn đồ thị mở) | Điểm chuẩn và bộ dữ liệu tiêu chuẩn cho nghiên cứu GNN |
| **CogDL** | Học sâu cho đồ thị; định hướng nghiên cứu |
| **Nói chuyện** | Thư viện GNN cho TensorFlow/Keras |
---

## Bản tóm tắt
Mạng nơ-ron đồ thị mở rộng khả năng học sâu sang dữ liệu quan hệ — mạng, phân tử, đồ thị tri thức và bất kỳ hệ thống nào nơi các thực thể được kết nối. Chúng hoạt động bằng cách truyền tin nhắn giữa các nút lân cận, cho phép mỗi nút học hỏi từ bối cảnh cục bộ của nó. GNN đã tìm thấy những ứng dụng mạnh mẽ nhất của họ trong việc khám phá ma túy, hệ thống khuyến nghị, phát hiện gian lận và biểu đồ tri thức. Lĩnh vực này đang phát triển theo hướng biến đổi đồ thị, đồ thị không đồng nhất và đào tạo có thể mở rộng cho các mạng trong thế giới thực khổng lồ. Nếu dữ liệu của bạn có mối quan hệ, GNN có thể đáng được xem xét.