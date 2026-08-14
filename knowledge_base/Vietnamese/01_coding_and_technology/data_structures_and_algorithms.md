<!--
---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Cấu trúc dữ liệu và thuật toán
Cấu trúc dữ liệu là cách chúng ta tổ chức dữ liệu trong bộ nhớ để các thao tác trên nó có hiệu quả. Thuật toán là quy trình từng bước để giải quyết vấn đề. Cùng nhau, chúng tạo thành nền tảng của khoa học máy tính — mọi chương trình bạn từng sử dụng đều dựa vào chúng. Việc chọn cấu trúc dữ liệu phù hợp có thể biến một chương trình cực kỳ chậm thành một chương trình nhanh và việc biết thuật toán phù hợp có thể biến một vấn đề nan giải thành một vấn đề tầm thường.
---

## Cấu trúc dữ liệu cơ bản
### Cấu trúc tuyến tính
| Cấu trúc | Truy cập | Tìm kiếm | Chèn | Xóa | Trường hợp sử dụng |
|----------|--------|--------|--------|--------|----------|
| **Mảng** | O(1) theo chỉ số | O(n) | O(n) | O(n) | Bộ sưu tập có kích thước cố định; truy cập ngẫu nhiên |
| **Danh sách liên kết** | O(n) | O(n) | O(1) ở đầu | O(1) ở đầu | Kích thước động; chèn/xóa |
| **Chồng** | O(n) | O(n) | O(1) đẩy/bật | O(1) bật | Lời gọi hàm; hoàn tác; phân tích cú pháp |
| **Xếp hàng** | O(n) | O(n) | O(1) xếp hàng | O(1) dequeue | Lập kế hoạch nhiệm vụ; BFS; hàng đợi tin nhắn |
| **Deque** | O(1) ở cả hai đầu | O(n) | O(1) ở cả hai đầu | O(1) ở cả hai đầu | Cửa sổ trượt; ăn cắp công việc |
### Cấu trúc dựa trên hàm băm
| Cấu trúc | Tìm kiếm | Chèn | Xóa | Trường hợp sử dụng |
|----------|--------|--------|--------|----------|
| **Bảng băm** | O(1) trung bình | O(1) trung bình | O(1) trung bình | Tra cứu khóa-giá trị; bộ nhớ đệm; bộ |
| **Bộ băm** | O(1) | O(1) | O(1) | Kiểm tra tư cách thành viên; chống trùng lặp |
**Xung đột băm**: khi hai khóa băm vào cùng một vị trí, chúng sẽ được lưu trữ trong danh sách liên kết (chuỗi) hoặc vị trí có sẵn tiếp theo (địa chỉ mở). Hàm băm tốt giảm thiểu xung đột.
### Cấu trúc cây
| Cấu trúc | Tìm kiếm | Chèn | Xóa | Trường hợp sử dụng |
|----------|--------|--------|--------|----------|
| **Cây tìm kiếm nhị phân** | O(log n) trung bình | O(log n) | O(log n) | Dữ liệu được sắp xếp; truy vấn phạm vi |
| **AVL / Cây đỏ đen** | O(log n) được đảm bảo | O(log n) | O(log n) | Tự cân bằng; được sử dụng trong bản đồ/bộ |
| **Cây B / Cây B+** | O(log n) | O(log n) | O(log n) | Chỉ mục cơ sở dữ liệu; hệ thống tập tin |
| **Thử** | O(k) trong đó k = độ dài khóa | O(k) | O(k) | Tự động hoàn thành; khớp tiền tố |
| **Đống (nhị phân)** | O(n) | O(log n) | O(log n) | Hàng đợi ưu tiên; lập kế hoạch |
### Biểu diễn đồ thị
| Đại diện | Không gian | Tra cứu cạnh | Thêm cạnh | Lặp lại hàng xóm |
|--------------|-------|-------------|----------|-------------------|
| **Ma trận kề** | O(V²) | O(1) | O(1) | O(V) |
| **Danh sách lân cận** | O(V + E) | O(độ) | O(1) | O(độ) |
| **Danh sách cạnh** | O(E) | O(E) | O(1) | O(E) |
---

## Độ phức tạp của thuật toán (Big-O)
Ký hiệu Big-O mô tả yêu cầu về thời gian hoặc không gian của thuật toán tăng lên như thế nào khi kích thước đầu vào tăng lên.
| Độ phức tạp | Tên | Ví dụ |
|----------|------|----------|
| **O(1)** | Hằng số | Tra cứu bảng băm; truy cập mảng theo chỉ mục |
| **O(log n)** | Logarit | Tìm kiếm nhị phân; hoạt động cây cân bằng |
| **O(n)** | Tuyến tính | Tìm kiếm tuyến tính; lặp lại một mảng |
| **O(n log n)** | Tuyến tính | Hợp nhất sắp xếp; sắp xếp đống; các loại mục đích chung hiệu quả nhất |
| **O(n²)** | Bậc hai | Sắp xếp bong bóng; các vòng lặp lồng nhau trên cùng một dữ liệu |
| **O(2^n)** | Hàm mũ | Tạo tập hợp con vũ phu; Fibonacci đệ quy ngây thơ |
| **O(n!)** | Giai thừa | Nhân viên bán hàng du lịch (vũ phu); hoán vị |
### Những quan niệm sai lầm thường gặp
| Quan Niệm Sai Lầm | Thực tế |
|--------------|----------|
| "O(n) luôn nhanh hơn O(n²)" | Với n nhỏ, hệ số hằng số quan trọng hơn |
| "Big-O thấp hơn luôn tốt hơn" | Sự đánh đổi không-thời gian tồn tại; Tra cứu O(1) sử dụng bộ nhớ O(n) |
| "Big-O cho bạn biết tốc độ chính xác" | Nó mô tả tốc độ tăng trưởng, không phải thời gian tuyệt đối |
---

## Thuật toán sắp xếp
| Thuật toán | Tốt nhất | Trung bình | Tệ nhất | Không gian | Ổn định | Tại chỗ |
|----------|------|---------|-------|-------|----------|----------|
| **Sắp xếp theo bong bóng** | O(n) | O(n²) | O(n²) | O(1) | Có | Có |
| **Sắp xếp chèn** | O(n) | O(n²) | O(n²) | O(1) | Có | Có |
| **Sắp xếp lựa chọn** | O(n²) | O(n²) | O(n²) | O(1) | Không | Có |
| **Sắp xếp hợp nhất** | O(n log n) | O(n log n) | O(n log n) | O(n) | Có | Không |
| **Sắp xếp nhanh** | O(n log n) | O(n log n) | O(n²) | O(log n) | Không | Có |
| **Sắp xếp đống** | O(n log n) | O(n log n) | O(n log n) | O(1) | Không | Có |
| **Sắp xếp thời gian** | O(n) | O(n log n) | O(n log n) | O(n) | Có | Không |
**Lời khuyên thiết thực**: sử dụng tính năng sắp xếp có sẵn trong ngôn ngữ của bạn (`sorted()` của Python,`Array.sort()`của JavaScript). Họ sử dụng các thuật toán được tối ưu hóa cao (Tim Sort, Introsort) để xử lý tất cả các trường hợp khó khăn.
---

## Thuật toán tìm kiếm
| Thuật toán | Cấu trúc dữ liệu | Độ phức tạp | Yêu cầu |
|----------|---------------|----------|-------------|
| **Tìm kiếm tuyến tính** | Bất kỳ | O(n) | Không có |
| **Tìm kiếm nhị phân** | Mảng được sắp xếp | O(log n) | Dữ liệu phải được sắp xếp |
| **Tra cứu bảng băm** | Bảng băm | O(1) trung bình | Hàm băm tốt |
| **BFS** (Tìm kiếm theo chiều rộng) | Đồ thị/cây | O(V + E) | Con đường ngắn nhất không có trọng số |
| **DFS** (Tìm kiếm theo chiều sâu) | Đồ thị/cây | O(V + E) | Tìm đường đi; phát hiện chu kỳ |
| **Dijkstra's** | Đồ thị có trọng số | O((V + E) log V) | Trọng số không âm; con đường ngắn nhất |
| **A* Tìm kiếm** | Đồ thị có trọng số | O((V + E) log V) | Hướng dẫn heuristic; tối ưu với phương pháp phỏng đoán có thể chấp nhận được |
---

## Các mẫu thuật toán chính
| Mẫu | Mô tả | Vấn đề ví dụ |
|----------|-------------|--------|
| **Chia rẽ và chinh phục** | Chia vấn đề thành các vấn đề phụ; giải quyết đệ quy; kết hợp | Hợp nhất sắp xếp; sắp xếp nhanh; tìm kiếm nhị phân |
| **Lập trình động** | Chia thành các vấn đề phụ chồng chéo; kết quả bộ đệm | Fibonacci; ba lô; dãy con chung dài nhất |
| **Tham lam** | Đưa ra lựa chọn tối ưu cục bộ ở mỗi bước | của Dijkstra; Mã hóa Huffman; lựa chọn hoạt động |
| **Quay lại** | Hãy thử các khả năng; hoàn tác những lựa chọn xấu; thử các lựa chọn thay thế | Người giải Sudoku; N-nữ hoàng; hoán vị |
| **Cửa sổ trượt** | Duy trì một cửa sổ các phần tử; trượt nó qua dữ liệu | Phân mảng tổng tối đa có kích thước K; chuỗi con dài nhất không lặp lại |
| **Hai con trỏ** | Sử dụng hai con trỏ di chuyển về phía nhau hoặc cùng hướng | Cặp tổng trong mảng được sắp xếp; loại bỏ trùng lặp |
| **Tìm kiếm nhị phân trên câu trả lời** | Tìm kiếm nhị phân không gian câu trả lời | Phân bổ các trang tối thiểu; bò hung hãn |
---

## Khi nào nên sử dụng cái gì
| Vấn đề | Cấu trúc dữ liệu | Thuật toán |
|----------|--------------|----------|
| Tra cứu khóa-giá trị nhanh | Bảng băm / từ điển | Băm |
| Duy trì thứ tự sắp xếp | BST cân bằng (TreeMap, std::set) | Vận hành cây |
| Xử lý dựa trên mức độ ưu tiên | Hàng đợi đống / ưu tiên | Hoạt động heap |
| Đường đi ngắn nhất (không có trọng số) | Đồ thị (danh sách kề) | BFS |
| Đường đi ngắn nhất (có trọng số) | Đồ thị (danh sách kề) | Dijkstra's / A* |
| Kiểm tra tư cách thành viên | Bộ băm / Bộ lọc Bloom | Băm |
| Khớp tiền tố | Trí | Trie traversal |
| Truy vấn phạm vi | Cây phân đoạn / Cây Fenwick | Vận hành cây |
| Bộ đệm LRU | Bản đồ băm + danh sách liên kết đôi | Hoạt động kết hợp |
| Các thành phần được kết nối | Liên minh thiết lập rời rạc (Union-Find) | Liên minh và Tìm kiếm |
---

## Bản tóm tắt
Cấu trúc dữ liệu và thuật toán không chỉ là chủ đề phỏng vấn — chúng còn là nền tảng của phần mềm hiệu quả. Mảng và bảng băm xử lý hầu hết các nhu cầu hàng ngày. Cây và đồ thị xử lý dữ liệu phân cấp và quan hệ. Sắp xếp và tìm kiếm là những vấn đề được giải quyết trong các thư viện tiêu chuẩn. Các mô hình thuật toán - phân chia để chinh phục, lập trình động, tham lam, quay lui - là những chiến lược có thể tái sử dụng để giải quyết các vấn đề mới. Kỹ năng quan trọng không phải là ghi nhớ các thuật toán; nó nhận ra mẫu nào phù hợp với một vấn đề nhất định và chọn cấu trúc dữ liệu phù hợp cho công việc.