---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Lý thuyết đồ thị
**đồ thị** là một cấu trúc toán học bao gồm các đỉnh (nút) được kết nối bởi các cạnh (liên kết). Các mối quan hệ mô hình đồ thị: mạng xã hội, bản đồ đường đi, mạng lưới thần kinh, sự phụ thuộc, kênh truyền thông. Lý thuyết đồ thị - nghiên cứu về các cấu trúc này - cung cấp các thuật toán và định lý trọng tâm của khoa học máy tính, nghiên cứu hoạt động và khoa học dữ liệu.
---

## Khái niệm cơ bản
### Định nghĩa
| Kỳ hạn | Định nghĩa | Ký hiệu |
|------|-------------|----------|
| **Biểu đồ** | Cặp G = (V, E) gồm các đỉnh và cạnh | G |
| **Đỉnh (nút)** | Một phần tử của V | v, u, w |
| **Cạnh** | Một kết nối giữa hai đỉnh | e = (u, v) hoặc {u, v} |
| **Đặt hàng** | Số đỉnh | \|V\| = n |
| **Kích thước** | Số cạnh | \|E\| = m |
| **Bằng cấp** | Số cạnh liên quan đến một đỉnh | độ(v) |
| **Đường dẫn** | Chuỗi các đỉnh riêng biệt nối với nhau bằng các cạnh | v₁, v₂, ..., vₖ |
| **Chu kỳ** | Một đường đi bắt đầu và kết thúc ở cùng một đỉnh | v₁ → v₂ → ... → vₖ → v₁ |
| **Đã kết nối** | Một đường đi tồn tại giữa mọi cặp đỉnh | — |
| **Thành phần** | Một đồ thị con được kết nối tối đa | — |
| **Biểu đồ con** | Đồ thị được hình thành từ tập hợp con của V và E | H ⊆ G |
### Các loại biểu đồ
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Không được định hướng** | Các cạnh không có hướng | Mạng lưới tình bạn |
| **Chỉ đạo (chữ ghép)** | Các cạnh có hướng (cung) | Liên kết trang web |
| **Có trọng số** | Các cạnh mang giá trị số | Khoảng cách đường |
| **Không trọng lượng** | Tất cả các cạnh đều tương đương | Kết nối xã hội |
| **Đơn giản** | Không có vòng lặp, không có nhiều cạnh | Hầu hết các đồ thị trong sách giáo khoa |
| **Đa văn** | Cho phép nhiều cạnh giữa các đỉnh giống nhau | Đường bay (nhiều chuyến bay giữa các thành phố) |
| **Hoàn thành** | Mọi cặp đỉnh đều được kết nối | Kₙ có n(n−1)/2 cạnh |
| **Lưỡng đảng** | Các đỉnh chia thành hai nhóm; chỉ các nhóm chéo | Ma trận đề xuất mục người dùng |
| **Phẳng** | Có thể vẽ mà không cần cắt cạnh | Bố trí bảng mạch |
| **Cây** | Đồ thị kết nối, không theo chu kỳ | Cây quyết định, hệ thống tập tin |
| **DAG** | Có định hướng, không có chu kỳ có định hướng | Lập lịch tác vụ, biểu đồ phụ thuộc |
### Bổ đề bắt tay
Tổng số độ của đỉnh bằng hai lần số cạnh:
Σᵥ độ(v) = 2|E|
**Hệ quả tất yếu:** Mọi đồ thị đều có số đỉnh bậc lẻ là chẵn.
**Ví dụ:** Trong một bữa tiệc gồm 10 người, mọi người bắt tay với đúng 3 người khác: Σ deg = 30, vậy |E| = Tổng cộng 15 cái bắt tay.
---

## Biểu diễn đồ thị
Cách bạn lưu trữ biểu đồ trong bộ nhớ sẽ xác định hiệu quả của mọi thuật toán bạn chạy trên đó.
| Đại diện | Không gian | Tra cứu cạnh | Lặp lại hàng xóm | Tốt nhất cho |
|-------|-------|-------------|--------------------|----------|
| **Ma trận kề** | O(n²) | O(1) | O(n) | Đồ thị dày đặc, kiểm tra cạnh nhanh |
| **Danh sách lân cận** | O(n + m) | O(độ(v)) | O(độ(v)) | Đồ thị thưa thớt, hầu hết các mạng trong thế giới thực |
| **Danh sách cạnh** | O(m) | O(m) | O(m) | Các thuật toán đơn giản, MST của Kruskal |
| **Ma trận tỷ lệ mắc** | O(n · m) | O(m) | O(m) | Thuật toán chuyên ngành |
### Ma trận kề
Một ma trận n × n A trong đó A[i][j] = 1 nếu cạnh (i,j) tồn tại, ngược lại là 0. Đối với đồ thị có trọng số, A[i][j] = trọng số.
**Thuộc tính:**
- Đối xứng cho đồ thị vô hướng
- Aᵏ[i][j] = số bước đi có độ dài k từ i đến j
- Giá trị riêng của A bộc lộ tính chất cấu trúc (xem Lý thuyết đồ thị phổ)
### Danh sách lân cận
Một mảng (hoặc bản đồ băm) trong đó mỗi đỉnh v lưu trữ một danh sách các đỉnh lân cận của nó.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Đây là cách biểu diễn phổ biến nhất cho các biểu đồ trong thế giới thực, thường rất thưa thớt (m ≪ n²).
---

## Cây
**cây** là một đồ thị vô hướng, liên thông. **Rừng** là sự kết hợp rời rạc của nhiều cây.
### Thuộc tính của cây
Đối với cây có n đỉnh:
- Nó có đúng n − 1 cạnh
- Có đúng một đường đi giữa hai đỉnh bất kỳ
- Loại bỏ bất kỳ cạnh nào sẽ ngắt kết nối nó
- Thêm bất kỳ cạnh nào sẽ tạo ra đúng một chu trình
### Các loại cây
| Loại | Mô tả | Ứng dụng |
|------|-------------|-------------|
| **Cây đã bén rễ** | Một đỉnh được chỉ định là gốc | Hệ thống tập tin, sơ đồ tổ chức |
| **Cây nhị phân** | Mỗi nút có tối đa 2 nút con | BST, phân tích biểu thức, cây quyết định |
| **Cây cân bằng** | Chiều cao là O(log n) | Cây AVL, cây đỏ đen (cơ sở dữ liệu) |
| **Cây bao trùm** | Đồ thị con bao gồm tất cả các đỉnh và là một cây | Thiết kế mạng, thuật toán xấp xỉ |
| **Cây bao trùm tối thiểu** | Cây bao trùm có tổng trọng lượng cạnh tối thiểu | Thiết kế mạng, phân cụm |
| **Biểu đồ ngôi sao** | Một nút trung tâm được kết nối với tất cả các nút khác | Mạng trung tâm và nan hoa |
### Thuộc tính cây nhị phân
| Bất động sản | Công thức |
|----------|----------|
| Các nút tối đa ở độ sâu d | 2ᵈ |
| Các nút tối đa trong cây có chiều cao h | 2ʰ⁺¹ − 1 |
| Chiều cao tối thiểu cho n nút | ⌊log₂(n)⌋ |
| Các nút lá trong cây nhị phân đầy đủ | Các nút nội bộ + 1 |
### Duyệt cây
| Truyền tải | Đặt hàng | Trường hợp sử dụng |
|----------|-------|----------|
| **Đặt hàng trước** | Gốc → Trái → Phải | Sao chép cây, biểu thức tiền tố |
| **Theo thứ tự** | Trái → Gốc → Phải | Đầu ra được sắp xếp từ BST |
| **Đặt hàng sau** | Trái → Phải → Gốc | Xóa cây, biểu thức hậu tố |
| **Thứ tự cấp độ (BFS)** | Cấp theo cấp độ, từ trái sang phải | Đường đi ngắn nhất trong cây không có trọng số |
---

## Truyền tải đồ thị
Các thuật toán truyền tải truy cập mọi đỉnh có thể tiếp cận một cách có hệ thống.
### Tìm kiếm theo chiều rộng (BFS)
Khám phá các đỉnh theo từng lớp bằng cách sử dụng **hàng đợi**.
| Bất động sản | Giá trị |
|----------|-------|
| Cấu trúc dữ liệu | Hàng đợi (FIFO) |
| Độ phức tạp thời gian | O(V + E) |
| Độ phức tạp của không gian | O(V) |
| Tìm đường đi ngắn nhất? | Có (đồ thị không có trọng số) |
| Hoàn thành? | Có (khám phá tất cả các đỉnh có thể tiếp cận) |
**Thuật toán:**
1. Bắt đầu tại đỉnh nguồn s. Mark đã đến thăm. Enqueue s.
2. Khi hàng đợi không trống: dequeue đỉnh u. Đối với mỗi người hàng xóm chưa được thăm v của bạn: đánh dấu v đã ghé thăm, enqueue v.
**Ứng dụng:** đường đi ngắn nhất trong biểu đồ không có trọng số, các thành phần được kết nối, kiểm tra tính lưỡng cực, thu thập thông tin trên web.
### Tìm kiếm theo chiều sâu (DFS)
Khám phá càng sâu càng tốt trước khi quay lui, sử dụng **ngăn xếp** (hoặc đệ quy).
| Bất động sản | Giá trị |
|----------|-------|
| Cấu trúc dữ liệu | Ngăn xếp (LIFO) / đệ quy |
| Độ phức tạp thời gian | O(V + E) |
| Độ phức tạp của không gian | O(V) |
| Tìm đường đi ngắn nhất? | Không |
| Hoàn thành? | Có (đối với đồ thị hữu hạn) |
**Thuật toán:**
1. Bắt đầu từ đỉnh s. Mark đã đến thăm.
2. Đối với mỗi lân cận chưa được thăm v của s: DFS đệ quy từ v.
**DFS phân loại các cạnh thành:**
- **Cạnh cây:** một phần của cây DFS
- **Cạnh sau:** kết nối một đỉnh với tổ tiên của nó (biểu thị chu trình)
- **Cạnh tiến:** nối một đỉnh với đỉnh con của nó
- **Cạnh chéo:** kết nối các đỉnh ở các nhánh khác nhau
**Ứng dụng:** sắp xếp tôpô, phát hiện chu trình, các thành phần được kết nối mạnh, giải mê cung.
### So sánh BFS và DFS
| Tiêu chí | BFS | DFS |
|----------||------|------|
| Chiến lược | Rộng rồi sâu | Sâu rồi rộng |
| Ký ức | Cao hơn (biên giới cửa hàng) | Hạ (đường dẫn cửa hàng) |
| Đường đi ngắn nhất (không có trọng số) | Đảm bảo | Không được đảm bảo |
| Sử dụng khi giải pháp gần bắt đầu | Tốt hơn | Tệ hơn |
| Sử dụng khi đồ thị rất sâu | Tệ hơn | Tốt hơn |
| Sắp xếp cấu trúc liên kết | Biến thể thuật toán của Kahn | Cách tiếp cận tiêu chuẩn |
---

## Thuật toán đường đi ngắn nhất
Tìm đường đi ngắn nhất giữa các đỉnh là một trong những bài toán đồ thị quan trọng nhất trong thực tế.
### Thuật toán Dijkstra
Tìm đường đi ngắn nhất từ ​​một nguồn đến tất cả các đỉnh khác trong biểu đồ có trọng số cạnh **không âm**.
| Bất động sản | Giá trị |
|----------|-------|
| Trọng lượng cạnh | Phải ≥ 0 |
| Thời gian (đống nhị phân) | O((V + E) log V) |
| Thời gian (đống Fibonacci) | O(E + V log V) |
| Tham? | Có |
| Xử lý trọng số âm? | Không |
**Thuật toán:**
1. Khởi tạo dist[s] = 0, dist[v] = ∞ với mọi v ≠ s. Hàng đợi ưu tiên Q với tất cả các đỉnh.
2. Khi Q không trống: trích xuất đỉnh u với khoảng cách nhỏ nhất. Với mỗi lân cận v của u có trọng số cạnh w: nếu dist[u] + w < dist[v], cập nhật dist[v] = dist[u] + w.
**Ví dụ đã hoạt động:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Thuật toán Bellman-Ford
Xử lý các trọng số cạnh **âm** và phát hiện các chu kỳ âm.
| Bất động sản | Giá trị |
|----------|-------|
| Trọng lượng cạnh | Bất kỳ (phát hiện chu kỳ tiêu cực) |
| Độ phức tạp thời gian | O(V · E) |
| Độ phức tạp của không gian | O(V) |
| Xử lý chu kỳ tiêu cực? | Có (phát hiện và báo cáo) |
**Thuật toán:**
1. Khởi tạo dist[s] = 0, dist[v] = ∞ với mọi v ≠ s.
2. Lặp lại V − 1 lần: với mỗi cạnh (u, v) có trọng số w: nếu dist[u] + w < dist[v], cập nhật dist[v].
3. Kiểm tra các chu kỳ âm: nếu bất kỳ cạnh nào vẫn có thể được nới lỏng thì tồn tại một chu kỳ âm.
### Thuật toán Floyd-Warshall
Tìm đường đi ngắn nhất giữa **tất cả các cặp** đỉnh.
| Bất động sản | Giá trị |
|----------|-------|
| Độ phức tạp thời gian | O(V³) |
| Độ phức tạp của không gian | O(V²) |
| Xử lý trọng số âm? | Có (nhưng không phải chu kỳ âm) |
| Tiếp cận | Lập trình động |
**Tái phát:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) cho mỗi đỉnh trung gian k.
### Hướng dẫn lựa chọn thuật toán
| Kịch bản | Thuật toán |
|----------|----------|
| Nguồn đơn, trọng số không âm | Dijkstra |
| Nguồn đơn, có thể có trọng số âm | Bellman-Ford |
| Tất cả các cặp, đồ thị dày đặc | Floyd-Warshall |
| Tất cả các cặp, đồ thị thưa thớt | Chạy Dijkstra từ mỗi đỉnh |
| Đồ thị không có trọng số | BFS |
| DAG (không có chu kỳ) | Sắp xếp cấu trúc liên kết + thư giãn |
| A* (theo hướng dẫn heuristic) | Tìm kiếm A* (để tìm đường với phương pháp phỏng đoán tốt) |
---

## Cây bao trùm tối thiểu
**Cây bao trùm tối thiểu (MST)** kết nối tất cả các đỉnh có tổng trọng số cạnh tối thiểu.
### Của cải
- Một MST có đúng n − 1 cạnh (đối với n đỉnh)
- MST tồn tại nếu đồ thị được kết nối
- Một biểu đồ có trọng số cạnh khác nhau có MST duy nhất
- MST thỏa mãn **thuộc tính cắt**: cạnh có trọng lượng tối thiểu cắt bất kỳ vết cắt nào thuộc về MST
- MST thỏa mãn **thuộc tính chu trình**: cạnh có trọng số lớn nhất trong chu trình bất kỳ không thuộc MST
### Thuật toán Kruskal
| Bất động sản | Giá trị |
|----------|-------|
| Chiến lược | Tham lam - thêm các cạnh theo thứ tự trọng số |
| Cấu trúc dữ liệu | Disjoint-set (union-find) |
| Độ phức tạp thời gian | O(E log E) |
| Tốt nhất cho | Đồ thị thưa thớt |
**Thuật toán:**
1. Sắp xếp tất cả các cạnh theo trọng số.
2. Đối với mỗi cạnh (theo thứ tự): nếu việc thêm nó không tạo ra một chu trình (kiểm tra bằng Union-find), hãy thêm nó vào MST.
3. Dừng khi n − 1 cạnh được chọn.
### Thuật toán Prim
| Bất động sản | Giá trị |
|----------|-------|
| Chiến lược | Tham lam — mọc cây từ đỉnh bắt đầu |
| Cấu trúc dữ liệu | Hàng đợi ưu tiên (min-heap) |
| Độ phức tạp thời gian | O(E log V) với đống nhị phân |
| Tốt nhất cho | Đồ thị dày đặc |
**Thuật toán:**
1. Bắt đầu từ bất kỳ đỉnh nào. Đánh dấu nó là một phần của MST.
2. Thêm liên tục cạnh có trọng số tối thiểu nối một đỉnh trong MST với một đỉnh bên ngoài nó.
3. Dừng lại khi đã bao gồm tất cả các đỉnh.
### Ứng dụng MST
| Ứng dụng | MST giúp ích như thế nào |
|-------------|--------------|
| Thiết kế mạng | Đặt cáp/ống tối thiểu để kết nối tất cả các vị trí |
| Phân cụm | Loại bỏ k − 1 cạnh MST dài nhất để có được k cụm |
| Thuật toán xấp xỉ | 2-xấp xỉ cho số liệu TSP |
| Phân đoạn hình ảnh | Nhóm các pixel theo MST có độ tương tự màu |
| Loại bỏ tính năng | Loại bỏ các tính năng dư thừa bằng MST của đồ thị tương quan |
---

## Luồng mạng
Các vấn đề về luồng mạng mô hình hóa sự di chuyển của các tài nguyên thông qua một hệ thống.
### Định nghĩa mạng luồng
**Mạng luồng** là một đồ thị có hướng với:
- Một đỉnh **nguồn** s (tạo ra luồng)
- Một đỉnh **sink** t (tiêu thụ luồng)
- **Công suất** c(u,v) ≥ 0 trên mỗi cạnh
- **Dòng chảy** f(u,v) thỏa mãn:
  - **Ràng buộc về công suất:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Bảo toàn luồng:** luồng vào = luồng ra ở mọi đỉnh ngoại trừ s và t
### Vấn đề về lưu lượng tối đa
Tìm tổng luồng tối đa từ s đến t.
**Phương pháp Ford-Fulkerson:**
1. Trong đồ thị dư tồn tại một đường tăng dần từ s lên t:
2. Tìm dung lượng nút cổ chai dọc theo đường dẫn
3. Tăng lưu lượng dọc theo đường dẫn bằng mức nút cổ chai
4. Cập nhật công suất còn lại
| Thuật toán | Độ phức tạp thời gian | Ghi chú |
|----------|--------------------------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) trong đó f* là lưu lượng tối đa | Không thể chấm dứt với năng lực phi lý |
| Edmonds-Karp (BFS) | O(V · E²) | Luôn kết thúc, chọn đường tăng ngắn nhất |
| Thuật toán Dinic | O(V² · E) | Sử dụng các luồng chặn; O(V^(1/2) · E) cho công suất đơn vị |
### Định lý cắt cực tiểu lưu lượng tối đa
**luồng tối đa** từ s đến t bằng công suất **cắt tối thiểu** tách s khỏi t.
A **cut** (S, T) chia các đỉnh thành S (chứa s) và T (chứa t). Khả năng cắt là tổng khả năng của các cạnh từ S đến T.
**Ứng dụng lưu lượng tối đa:**
- Kết hợp hai bên (phân công công việc cho người lao động)
- Phân đoạn hình ảnh (tách nền trước và nền)
- Loại bóng chày (đội X vẫn có thể thắng chứ?)
- Độ tin cậy của mạng (thông lượng dữ liệu tối đa)
### Kết hợp hai bên thông qua Luồng tối đa
Cho đồ thị lưỡng cực G = (L ∪ R, E):
1. Thêm các nguồn có cạnh vào tất cả các đỉnh trong L (dung lượng 1)
2. Thêm sink t với các cạnh từ tất cả các đỉnh trong R (dung lượng 1)
3. Đặt tất cả dung lượng cạnh ban đầu thành 1
4. Lưu lượng tối đa = khớp tối đa
---

## Lý thuyết đồ thị phổ
Lý thuyết đồ thị phổ nghiên cứu đồ thị thông qua các giá trị riêng và vectơ riêng của ma trận liên kết với đồ thị.
### Ma trận chính
| Ma trận | Định nghĩa | Nó ghi lại những gì |
|--------|-------------|-------------------|
| **Ma trận kề** A | A[i][j] = 1 nếu cạnh (i,j) tồn tại | Mô hình kết nối |
| **Ma trận độ** D | Đường chéo; D[i][i] = độ(i) | Tầm quan trọng của đỉnh theo độ |
| **Laplacian** L = D − A | L[i][j] = −1 nếu cạnh, deg(i) trên đường chéo | Độ mượt của các hàm trên đồ thị |
| **Laplacian chuẩn hóa** L_norm = D^(−1/2) L D^(−1/2) | Phiên bản bất biến tỷ lệ | Cấu trúc cộng đồng |
### Giá trị riêng của Laplacian
Laplacian L là nửa xác định dương nên tất cả các giá trị riêng đều ≥ 0.
| Giá trị riêng | Ý nghĩa |
|----------||---------|
| λ₁ = 0 | Luôn bằng không; vectơ riêng là vectơ không đổi |
| λ₂ (kết nối đại số) | > 0 nếu đồ thị được kết nối; lớn hơn = kết nối tốt hơn |
| Số giá trị riêng bằng 0 | Bằng số lượng thành phần được kết nối |
| λₙ | Liên quan đến mức độ tối đa và khai triển đồ thị |
### Ứng dụng của phương pháp quang phổ
| Ứng dụng | Phương pháp |
|-------------|--------|
| **Phân vùng đồ thị** | Sử dụng vectơ riêng của L để chia đồ thị thành các phần cân bằng |
| **Phát hiện cộng đồng** | Phân cụm quang phổ: nhúng các đỉnh bằng cách sử dụng vectơ riêng phía dưới, sau đó phân cụm |
| **Xếp hạng trang** | Vectơ riêng của ma trận kề (hoặc ma trận chuyển tiếp) của đồ thị web |
| **Vẽ đồ thị** | Định vị các đỉnh bằng vectơ riêng của Laplacian |
| **Học bán giám sát** | Tuyên truyền nhãn bằng đồ thị Laplacian (lan truyền nhãn) |
| **Mạng lưới thần kinh đồ thị** | Tích chập phổ: lọc tín hiệu trên đồ thị bằng vectơ riêng của L |
### Bất bình đẳng của Cheeger
Liên hệ giá trị riêng thứ hai λ₂ với **mở rộng** của biểu đồ (mức độ liên kết của nó):
λ₂ / 2 ≤ h(G) √(2λ₂)
trong đó h(G) là hằng số Cheeger (số đẳng giác). Điều này có nghĩa là λ₂ đo lường gần đúng mức độ khó để cắt biểu đồ thành hai phần — một thông tin chuyên sâu quan trọng để phân cụm.
---

## Cấu trúc đồ thị đặc biệt
| Đồ thị | Đỉnh | Cạnh | Thuộc tính |
|-------|----------|-------|-------------|
| Hoàn thành Kₙ | n | n(n−1)/2 | Mỗi cặp được kết nối; đường kính 1 |
| Chu kỳ Cₙ ​​| n | n | 2-thường xuyên; đã kết nối |
| Đường dẫn Pₙ | n | n−1 | Cây; đường kính n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-thường xuyên; đường kính k; lưỡng đảng |
| Hoàn thành lưỡng cực K_{m,n} | m+n | m·n | Mọi đỉnh trong một phần đều kết nối với tất cả các đỉnh khác |
| Đồ thị Petersen | 10 | 15 | 3-thường xuyên; đường kính 2; không phẳng; không có chu trình Hamilton |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm đồ thị | Ứng dụng |
|---------------|-------------|
| BFS / DFS | Thu thập dữ liệu web, phân tích mạng xã hội, ghi nhãn thành phần được kết nối |
| Dijkstra / A* | Lập kế hoạch lộ trình, trò chơi tìm đường AI, điều hướng bằng robot |
| Cây bao trùm tối thiểu | Phân cụm (liên kết đơn), lựa chọn tính năng, thiết kế mạng |
| Lưu lượng tối đa / cắt phút | Phân đoạn hình ảnh, đối sánh hai bên, phân công đề xuất |
| Phương pháp quang phổ | Phân cụm quang phổ, mạng lưới thần kinh đồ thị, giảm kích thước (bản đồ riêng Laplacian) |
| Xếp hạng trang | Xếp hạng công cụ tìm kiếm, phân tích ảnh hưởng trên mạng xã hội |
| DAG | Mạng Bayes, suy luận nhân quả, lập lịch tác vụ, đồ thị tính toán trong deep learning |
| Đồ thị lưỡng cực | Ma trận vật phẩm người dùng trong hệ thống gợi ý, thị trường hai mặt |
| Cấu trúc cây | Cây quyết định, rừng ngẫu nhiên, phân cụm theo cấp bậc, điều hướng hệ thống tệp |
| Biểu diễn đồ thị | Biểu đồ tri thức (Wikidata, DBpedia), biểu đồ phân tử (khám phá thuốc), mạng trích dẫn |
---

## Bản tóm tắt
| Chủ đề | Ý tưởng cốt lõi | Thuật toán chính / Kết quả |
|-------|----------||----------------------|
| Nguyên tắc cơ bản | Đỉnh, cạnh, độ, đường đi | Bổ đề bắt tay |
| Đại diện | Cách lưu trữ đồ thị | Ma trận kề và danh sách kề |
| Cây | Đồ thị không theo chu kỳ được kết nối | n đỉnh → n−1 cạnh |
| Truyền tải | Thăm dò đỉnh có hệ thống | BFS (đường đi ngắn nhất), DFS (thăm dò sâu) |
| Đường dẫn ngắn nhất | Các tuyến có trọng lượng tối thiểu | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Cây bao trùm tối thiểu | Cách rẻ nhất để kết nối tất cả các đỉnh | Kruskal's, Prim's |
| Luồng mạng | Thông lượng tối đa | Ford-Fulkerson, định lý cắt cực đại dòng chảy cực đại |
| Lý thuyết quang phổ | Giá trị riêng tiết lộ cấu trúc | Giá trị riêng Laplacian, phân cụm quang phổ |
Lý thuyết đồ thị được cho là nhánh toán học có thể áp dụng trực tiếp nhất vào khoa học dữ liệu hiện đại. Mạng xã hội, biểu đồ tri thức, cấu trúc phân tử, biểu đồ tính toán trong khung học sâu, độ phân giải phụ thuộc, hệ thống đề xuất - về cơ bản đều là các vấn đề về biểu đồ. Các thuật toán được đề cập ở đây không chỉ mang tính lý thuyết; chúng chạy ở quy mô lớn trong các hệ thống sản xuất hàng ngày.