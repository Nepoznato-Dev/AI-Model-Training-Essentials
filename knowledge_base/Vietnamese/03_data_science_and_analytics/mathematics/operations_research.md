---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Nghiên cứu hoạt động
Nghiên cứu hoạt động (OR) là việc áp dụng các phương pháp toán học vào việc ra quyết định. Ra đời trong Thế chiến thứ hai dành cho lĩnh vực hậu cần quân sự, giờ đây nó tối ưu hóa chuỗi cung ứng, lên lịch cho các hãng hàng không, định tuyến đội tàu giao hàng, quản lý hàng tồn kho và phân bổ nguồn lực cho mọi ngành. HOẶC cung cấp bộ công cụ toán học để đưa ra quyết định tốt nhất có thể trong điều kiện ràng buộc.
---

## Công thức lập trình tuyến tính
###Mẫu chuẩn
Giảm thiểu cᵀx
Tuân theo: Ax = b, x ≥ 0
### Công thức LP phổ biến
**Kết hợp sản phẩm:**
- Biến quyết định: xⱼ = số lượng sản phẩm j cần sản xuất
- Mục tiêu: tối đa hóa lợi nhuận Σ pⱼxⱼ
- Ràng buộc: giới hạn tài nguyên Σ aᵢⱼxⱼ ≤ bᵢ
**Vấn đề ăn kiêng:**
- Biến quyết định: xⱼ = lượng thực phẩm j cần mua
- Mục tiêu: giảm thiểu chi phí Σ cⱼxⱼ
- Hạn chế: yêu cầu dinh dưỡng Σ nᵢⱼxⱼ ≥ rᵢ
**Vấn đề pha trộn:**
- Biến quyết định: xⱼ = tỷ lệ thành phần j trong hỗn hợp
- Mục tiêu: giảm thiểu chi phí
- Ràng buộc: yêu cầu về chất lượng (chỉ số octan, cường độ, v.v.)
### Ví dụ hoạt động: Lập kế hoạch sản xuất
Một nhà máy sản xuất sản phẩm A và B.
- A cần 2 giờ lao động, 1 kg nguyên liệu; lợi nhuận $30
- B cần 1 giờ lao động, 3 kg vật liệu; lợi nhuận $40
- Có sẵn: 40 giờ lao động, 30 kg nguyên liệu
**Công thức:**
- Tăng tối đa: 30x_A + 40x_B
- Chịu: 2x_A + x_B ≤ 40 (lao động)
- x_A + 3x_B 30 (vật liệu)
- x_A, x_B ≥ 0
**Giải:** Các đỉnh của miền khả thi: (0,0), (20,0), (18,4), (0,10)
- (0,0): lợi nhuận = 0
- (20,0): lãi = 600
- (18,4): lợi nhuận = 700 ← tối ưu
- (0,10): lãi = 400
---

## Vấn đề giao thông
Vận chuyển hàng hóa từ m nguồn tới n điểm đến với chi phí tối thiểu.
### Công thức
- Biến quyết định: xᵢⱼ = số lượng vận chuyển từ nguồn i đến đích j
- Mục tiêu: giảm thiểu Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Tuân theo: Σⱼ xᵢⱼ = sᵢ (hạn chế về nguồn cung)
- Σᵢ xᵢⱼ = dⱼ (hạn chế nhu cầu)
- xᵢⱼ ≥ 0
### Phương pháp giải
| Phương pháp | Mô tả | Chất lượng của giải pháp ban đầu |
|--------|-------------|------------------------------------------|
| **Góc Tây Bắc** | Bắt đầu từ trên cùng bên trái, phân bổ tham lam | Khả thi nhưng thường kém |
| **Xấp xỉ Vogel** | Xem xét chi phí phạt | Giải pháp ban đầu tốt hơn |
| **MODI / Bước đệm** | Lặp đi lặp lại cải tiến giải pháp ban đầu | Tìm tối ưu |
### Ví dụ đã hoạt động
| | D1 | D2 | D3 | Cung cấp |
|---|----|----|------|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Nhu cầu | 40 | 30 | 30 | 100 |
---

## Vấn đề về bài tập
Phân công n công nhân vào n công việc (một-một) để giảm thiểu tổng chi phí.
### Công thức
- Biến quyết định: xᵢⱼ ∈ {0, 1} (1 nếu nhân viên i được giao công việc j)
- Giảm thiểu: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Tuân theo: Σⱼ xᵢⱼ = 1 (mỗi công nhân làm một công việc)
- Σᵢ xᵢⱼ = 1 (mỗi công việc có 1 công nhân)
### Thuật toán Hungary
| Bất động sản | Giá trị |
|----------|-------|
| Độ phức tạp thời gian | O(n³) |
| Tối ưu? | Có |
| Tiếp cận | Giảm ma trận + che phủ tối thiểu |
**Các bước:**
1. Trừ số tiền tối thiểu của hàng từ mỗi hàng
2. Trừ số tiền tối thiểu của cột từ mỗi cột
3. Che tất cả các số 0 bằng số dòng tối thiểu
4. Nếu dòng = n, phép gán tối ưu được tìm thấy giữa các số 0
5. Nếu không, hãy điều chỉnh ma trận và lặp lại
---

## Tối ưu hóa luồng mạng
### Dòng chi phí tối thiểu
Cho một mạng có dung lượng và chi phí ở biên, hãy tìm luồng thỏa mãn nhu cầu với chi phí tối thiểu.
**Công thức:**
- Giảm thiểu: Σ cᵢⱼxᵢⱼ
- Tuân thủ: bảo toàn dòng chảy tại mỗi nút
- Giới hạn công suất: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Đường dẫn ngắn nhất dưới dạng luồng mạng
Bài toán đường đi ngắn nhất là trường hợp đặc biệt của luồng chi phí tối thiểu (gửi 1 đơn vị từ s đến t).
### Ứng dụng
| Ứng dụng | Mô hình mạng |
|-------------|--------------|
| Chuỗi cung ứng | Nút = kho, cạnh = tuyến vận chuyển |
| Truyền thông | Nút = bộ định tuyến, cạnh = liên kết có băng thông |
| Giao thông | Nút = nút giao, cạnh = đường có sức chứa |
| Quản lý dự án | Mạng CPM/PERT |
---

## Lập trình động
**Lập trình động (DP)** giải quyết các vấn đề phức tạp bằng cách chia chúng thành các bài toán con chồng chéo.
### Nguyên lý tối ưu của Bellman
Một chính sách tối ưu có đặc tính là bất kể trạng thái và quyết định ban đầu là gì, các quyết định còn lại phải tạo thành chính sách tối ưu cho trạng thái kết quả.
### Các yếu tố chính
| Yếu tố | Mô tả |
|----------|-------------|
| **Sân khấu** | Điểm quyết định (bước thời gian, chỉ số mục) |
| **Tiểu bang** | Thông tin cần thiết để đưa ra quyết định |
| **Quyết định** | Lựa chọn được thực hiện ở từng giai đoạn |
| **Tái phát** | Giá trị tối ưu ở giai đoạn n theo giai đoạn n−1 |
### Sự cố DP cổ điển
| Vấn đề | Tái Phát | Độ phức tạp |
|----------|-------------|-------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) với bản ghi nhớ |
| **Ba lô** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Con đường ngắn nhất** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) hoặc O(E log V) |
| **Chỉnh sửa khoảng cách** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+chi phí) | O(mn) |
| **Chuỗi con chung dài nhất** | L(i,j) = L(i−1,j−1)+1 nếu khớp, nếu không thì max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Nhân chuỗi ma trận** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Ví dụ hoạt động: 0/1 Ba lô
Mục: {weight: value} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Công suất W = 7.
V(i, w) = giá trị tối đa sử dụng i mục đầu tiên có dung lượng w
| tôi\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|------|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Tối ưu: V(4, 7) = 23 (mục 1 và 4: trọng số 2+5=7, giá trị 12+11=23).
---

## Lý thuyết xếp hàng
Lý thuyết xếp hàng nghiên cứu về hàng chờ - chúng dài bao nhiêu, bạn đợi bao lâu và làm thế nào để giảm cả hai.
### Ký hiệu của Kendall
A/B/c/K/N/D trong đó:
- A = quá trình đến (M = Markovian/Poisson, D = xác định, G = tổng quát)
- B = quy trình dịch vụ (tùy chọn tương tự)
- c = số lượng máy chủ
- K = dung lượng (mặc định ∞)
- N = dân số (mặc định ∞)
- D = kỷ luật (FIFO, LIFO, Ưu tiên)
### Hàng đợi M/M/1 (Máy chủ đơn)
| Số liệu | Công thức |
|--------|----------|
| Sử dụng | ρ = λ/μ |
| Số trung bình trong hệ thống | L = ρ/(1−ρ) |
| Thời gian trung bình trong hệ thống | W = 1/(μ−λ) |
| Số lượng trung bình trong hàng đợi | L_q = ρ²/(1−ρ) |
| Thời gian chờ trung bình | W_q = ρ/(μ−λ) |
trong đó λ = tốc độ đến, μ = tốc độ dịch vụ, ρ = mức sử dụng.
### Hàng đợi M/M/c (Nhiều máy chủ)
| Số liệu | Công thức |
|--------|----------|
| Sử dụng | ρ = λ/(cμ) |
| Xác suất chờ đợi (Erlang C) | P_w = công thức phức tạp gồm ρ và c |
| Độ dài hàng đợi trung bình | L_q = P_w · ρ/(1−ρ) |
### Định luật nhỏ
L = λW (số trung bình trong hệ thống = tốc độ đến × thời gian trung bình)
Điều này áp dụng cho BẤT KỲ hệ thống xếp hàng nào, bất kể phân phối dịch vụ đến/dịch vụ.
### Ví dụ ứng dụng
| Kịch bản | Mô hình xếp hàng |
|----------|-------------|
| Trung tâm cuộc gọi | M/M/c (c đại lý) |
| Yêu cầu máy chủ web | M/M/1 hoặc M/G/1 |
| Bệnh viện cấp cứu | M/G/c có mức độ ưu tiên |
| Dây chuyền sản xuất | Mạng lưới hàng đợi |
| Lập lịch CPU máy tính | Chia sẻ bộ xử lý M/M/1 |
---

## Mô hình khoảng không quảng cáo
### Số lượng đặt hàng kinh tế (EOQ)
Số lượng đặt hàng tối ưu giúp giảm thiểu tổng chi phí tồn kho.
Q* = √(2DS/H)
| Biến | Ý nghĩa |
|----------|----------|
| D | Nhu cầu hàng năm |
| S | Chi phí đặt hàng mỗi đơn hàng |
| H | Chi phí nắm giữ mỗi đơn vị mỗi năm |
| Hỏi* | Số lượng đặt hàng tối ưu |
**Tổng chi phí tại Q*:** TC = √(2DSH)
### Tiện ích mở rộng
| Người mẫu | Gia hạn |
|-------|----------|
| **EOQ có giảm giá** | Giảm giá theo số lượng thay đổi hàm chi phí |
| **Số lượng đặt hàng sản xuất** | Mặt hàng được sản xuất dần dần, không giao hết một lúc |
| **(s, Q) mô hình** | Sắp xếp lại đơn vị Q khi tồn kho giảm xuống mức s |
| **(s, S) model** | Đặt hàng tới S khi tồn kho giảm xuống s |
| **Mô hình nhà cung cấp tin tức** | Nhu cầu một kỳ, không chắc chắn |
###Mô hình nhà cung cấp báo
Số lượng đặt hàng tối ưu cho hàng tồn kho dễ hư hỏng trong một kỳ:
P(D ≤ Q*) = c_u / (c_u + c_o)
trong đó c_u = chi phí thiếu hụt (lợi nhuận bị mất) và c_o = chi phí thiếu hụt (lãng phí).
---

## Lên lịch
### Lập kế hoạch cửa hàng việc làm
| Ký hiệu | Ý nghĩa |
|----------|----------|
| n/m/J/C_max | n việc làm, m máy móc, cửa hàng việc làm, giảm thiểu makespan |
| Cửa hàng dòng chảy | Tất cả công việc truy cập vào máy theo thứ tự giống nhau |
| Cửa hàng việc làm | Mỗi công việc có trình tự máy riêng |
| Mở cửa hàng | Không có ràng buộc đặt hàng |
### Quy tắc ưu tiên
| Quy tắc | Mô tả | Hiệu ứng |
|------|-------------|--------|
| FCFS | Đến trước được phục vụ trước | Công bằng nhưng chưa tối ưu |
| SPT | Thời gian xử lý ngắn nhất trước tiên | Giảm thiểu mức độ hoàn thành trung bình |
| EDD | Ngày đáo hạn sớm nhất trước | Giảm thiểu độ trễ tối đa |
| CR | Tỷ lệ quan trọng (ngày hết hạn còn lại/thời gian xử lý) | Cân bằng |
| LPT | Thời gian xử lý đầu tiên lâu nhất | Tốt cho việc sửa chữa trên các máy song song |
### Thuật toán Johnson (Cửa hàng 2 máy)
Với n công việc trên 2 máy, giảm thiểu thời gian tạm ứng:
1. Tìm công việc có thời gian xử lý ngắn nhất
2. Nếu ở máy 1, hãy lên lịch trước; nếu ở máy 2 thì hẹn cuối cùng
3. Xóa công việc đó và lặp lại
Tối ưu cho 2 máy; NP-hard cho hơn 3 máy.
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| HOẶC Khái niệm | Ứng dụng |
|----------||-------------|
| Lập trình tuyến tính | Phân bổ nguồn lực, tối ưu hóa danh mục đầu tư, phân bổ ngân sách quảng cáo |
| Vận chuyển/phân công | Hậu cần, kết nối đi chung xe, phân công nhiệm vụ |
| Luồng mạng | Tối ưu hóa chuỗi cung ứng, định tuyến lưu lượng trung tâm dữ liệu |
| Lập trình động | Căn chỉnh trình tự (tin sinh học), thuật toán Viterbi (HMM), RL (phương trình Bellman) |
| Lý thuyết xếp hàng | Lập kế hoạch dung lượng máy chủ, lập mô hình độ trễ, phân bổ tài nguyên đám mây |
| Mô hình hàng tồn kho | Tích hợp dự báo nhu cầu, chuỗi cung ứng ML |
| Lập kế hoạch | Điều phối đường ống ML, lập lịch công việc GPU, lập lịch tìm kiếm siêu tham số |
| Lập trình số nguyên | Lựa chọn tính năng (nhị phân), lựa chọn mô hình, thiết kế mạng |
---

## Bản tóm tắt
| Chủ đề | Vấn đề cốt lõi | Phương pháp chính |
|-------|-------------|-------------|
| Công thức LP | Tối ưu hóa mục tiêu tuyến tính với các ràng buộc | Simplex, điểm nội thất |
| Giao thông vận tải | Vận chuyển hàng hóa với chi phí tối thiểu | MODI, bước đệm |
| Bài tập | Kết nối người lao động với công việc | Thuật toán Hungary |
| Luồng mạng | Định tuyến luồng qua mạng | Thuật toán luồng chi phí tối thiểu |
| Lập trình động | Các bài toán con chồng chéo | Nguyên tắc Bellman, ghi nhớ |
| Lý thuyết xếp hàng | Phân tích hàng chờ | M/M/1, Định luật Little |
| Hàng tồn kho | Đặt hàng khi nào và bao nhiêu | EOQ, nhà cung cấp tin tức |
| Lập kế hoạch | Trình tự công việc trên máy | Quy tắc ưu tiên, thuật toán Johnson |
Nghiên cứu hoạt động chuyển đổi việc ra quyết định từ nghệ thuật sang khoa học. Bằng cách hình thành các vấn đề trong thế giới thực bằng toán học, OR cung cấp các giải pháp tối ưu (hoặc gần tối ưu) có thể chứng minh được cho các vấn đề về hậu cần, lập kế hoạch, phân bổ nguồn lực và lập kế hoạch có ảnh hưởng đến mọi ngành. Đối với các nhà khoa học dữ liệu, phương pháp OR bổ sung cho học máy: trong khi ML dự đoán, OR quy định — và cùng nhau, chúng tạo thành nền tảng của hệ thống quyết định thông minh.