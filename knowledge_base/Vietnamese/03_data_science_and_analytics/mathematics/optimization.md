<!--
---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Tối ưu hóa
Tối ưu hóa là toán học tìm ra giải pháp tốt nhất từ ​​một tập hợp các giải pháp khả thi. Nó hỏi: với một hàm và các ràng buộc, đầu vào nào sẽ giảm thiểu (hoặc tối đa hóa) đầu ra? Tối ưu hóa là động cơ của máy học - đào tạo một mô hình có nghĩa là giảm thiểu hàm mất mát. Nó xuất hiện trong nghiên cứu hoạt động, kinh tế, thiết kế kỹ thuật và hầu như mọi lĩnh vực định lượng.
---

## Xây dựng vấn đề
**Bài toán tối ưu hóa** tổng quát có dạng:
Giảm thiểu f(x)
Tuân theo: gᵢ(x) 0 (ràng buộc bất đẳng thức), hⱼ(x) = 0 (ràng buộc đẳng thức)
| Kỳ hạn | Ý nghĩa |
|------|----------|
| **Hàm mục tiêu** f(x) | Số lượng cần giảm thiểu (hoặc tối đa hóa) |
| **Biến quyết định** x | Các giá trị chúng ta có thể kiểm soát |
| **Khu vực khả thi** | Tập hợp tất cả x thỏa mãn mọi ràng buộc |
| **Tối thiểu toàn cầu** | Khả thi x* với f(x*) ≤ f(x) với mọi x khả thi |
| **Tối thiểu cục bộ** | Khả thi x* với f(x*) ≤ f(x) với mọi x khả thi ở một lân cận nào đó |
| **Bài toán lồi** | f là lồi, vùng khả thi là tập lồi (local min = toàn cục min) |
---

## Lập trình tuyến tính (LP)
Khi cả mục tiêu và tất cả các ràng buộc đều **tuyến tính** thì bài toán là một chương trình tuyến tính.
###Mẫu chuẩn
Giảm thiểu cᵀx
Tuân theo: Ax ≤ b, x ≥ 0
trong đó c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Của cải
| Bất động sản | Tuyên bố |
|----------|----------|
| Độ lồi | LP luôn là bài toán lồi |
| Giải pháp tối ưu | Luôn ở một đỉnh (điểm góc) của đa giác khả thi |
| Sự tồn tại | Nếu vùng khả thi bị chặn và không trống thì tồn tại lời giải tối ưu |
| Nhiều tối ưu | Nếu hai đỉnh là tối ưu thì mọi điểm trên cạnh giữa chúng cũng tối ưu |
### Phương pháp đơn giản
**Phương pháp đơn giản** (Dantzig, 1947) di chuyển dọc theo các cạnh của polytope khả thi từ đỉnh này sang đỉnh khác, luôn cải thiện mục tiêu cho đến khi đạt được mức tối ưu.
| Bất động sản | Giá trị |
|----------|-------|
| Thời điểm xấu nhất | O(2ⁿ) (số mũ - hiếm trong thực tế) |
| Thời gian trường hợp trung bình | Đa thức cho hầu hết các bài toán thực tế |
| Ý tưởng chính | Di chuyển đến đỉnh liền kề có giá trị mục tiêu tốt hơn |
**Thuật toán (tổng quan):**
1. Bắt đầu từ một giải pháp khả thi cơ bản (đỉnh của đa giác)
2. Chọn một biến đầu vào (một biến cải thiện mục tiêu)
3. Chọn biến rời (duy trì tính khả thi)
4. Pivot: di chuyển tới đỉnh mới
5. Lặp lại cho đến khi không còn hướng cải thiện nào nữa
### Phương pháp điểm bên trong
Thay thế cho đơn giản: tiếp cận tối ưu từ bên trong vùng khả thi.
| Bất động sản | Giá trị |
|----------|-------|
| Thời điểm xấu nhất | Đa thức (O(n³·⁵) cho một số biến thể) |
| Hiệu suất thực tế | Cạnh tranh với đơn hình trong các bài toán lớn |
| Ý tưởng chính | Đi theo "con đường trung tâm" xuyên qua nội thất |
### Ví dụ về LP đã hoạt động
**Vấn đề:** Một nhà máy sản xuất ghế (x₁) và bàn (x₂).
- Lợi nhuận: 30$/ghế, 50$/bàn
- Gỗ: 2x₁ + 4x₂ 100 (có sẵn chân ván)
- Lao động: x₁ + 3x₂ ≤ 60 (có số giờ làm việc)
- Tối đa hóa: 30x₁ + 50x₂
**Giải (phương pháp đồ họa cho 2 biến):**
- Các đỉnh của vùng khả thi: (0,0), (30,0), (40,10), (0,20)
- Đánh giá mục tiêu tại mỗi đỉnh:
  - (0,0): lợi nhuận = 0
  - (30,0): lãi = 900
  - (40,10): lợi nhuận = 1700 ← tối ưu
  - (0,20): lãi = 1000
- **Tối ưu:** x₁ = 40 ghế, x₂ = 10 bàn, lợi nhuận = $1700
---

## Tối ưu hóa lồi
Một bài toán **lồi** nếu hàm mục tiêu là lồi và vùng khả thi là một tập lồi.
### Tập lồi và hàm lồi
| Khái niệm | Định nghĩa |
|----------|-------------|
| **Tập lồi** | Với mọi x, y trong tập hợp và t ∈ [0,1]: tx + (1−t)y cũng thuộc tập hợp |
| **Hàm lồi** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) với mọi t ∈ [0,1] |
| **Lồi chặt** | Bất đẳng thức nghiêm ngặt đối với t ∈ (0,1) và x ≠ y |
**Thuộc tính chính:** Để tối ưu hóa lồi, mọi cực tiểu cục bộ đều là cực tiểu toàn cục.
### Hàm lồi phổ biến
| Chức năng | Lồi? | Ở đâu |
|----------|----------|-------|
| ax + b (tuyến tính) | Có (và lõm) | Mọi nơi |
| x² | Có | ℝ |
| eˣ | Có | ℝ |
| −log(x) | Có | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Có | ℝⁿ |
| max(f₁, f₂) nếu f₁, f₂ lồi | Có | Giao điểm của các miền |
### Giảm độ dốc
Thuật toán tối ưu hóa cơ bản nhất trong học máy.
**Quy tắc cập nhật:** x_{k+1} = x_k − α∇f(x_k)
trong đó α > 0 là **tốc độ học** (kích thước bước).
| Biến thể | Cập nhật quy tắc | Lợi thế |
|----------|-------------|----------|
| **GD hàng loạt** | x ← x − α∇f(x) | Hội tụ ổn định |
| **GD ngẫu nhiên (SGD)** | x ← x − α∇fᵢ(x) (một mẫu) | Nhanh mỗi lần lặp, thoát khỏi mức tối thiểu cục bộ |
| **SGD lô nhỏ** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Cân bằng giữa lô và ngẫu nhiên |
| **Động lực** | v ← βv − α∇f(x); x ← x + v | Tăng tốc qua vùng bằng phẳng |
| **Adam** | Tỷ lệ học tập thích ứng trên mỗi tham số | Hoạt động tốt cho việc học sâu |
| **RMSprop** | Chia tỷ lệ tốc độ học tập bằng cách chạy trung bình độ lớn | Tốt cho RNN |
### Tỷ lệ hội tụ
| Phương pháp | Lồi f | Lồi mạnh f |
|--------|----------|-------------------|
| Độ dốc gốc | O(1/k) | O((1−μ/L)ᵏ) (tuyến tính) |
| SGD | O(1/√k) | O(1/k) |
| GD tăng tốc (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
trong đó k = số lần lặp, μ = tham số độ lồi mạnh, L = hằng số Lipschitz.
### Chọn tốc độ học tập
| Chiến lược | Mô tả |
|----------|-------------|
| Đã sửa lỗi | Đơn giản nhưng có thể phân kỳ (quá lớn) hoặc hội tụ chậm (quá nhỏ) |
| Tìm kiếm dòng | Tìm α làm cực tiểu hóa f(x − α∇f(x)) dọc theo hướng gradient |
| lịch trình phân rã | α_t = α₀ / (1 + βt) hoặc α_t = α₀ · βᵗ |
| Khởi động | Bắt đầu nhỏ, tăng dần rồi giảm dần (thường gặp trong đào tạo máy biến áp) |
| Thích ứng (Adam) | Tỷ lệ học tập trên mỗi tham số dựa trên thống kê độ dốc |
---

## Tối ưu hóa ràng buộc
### Hệ số Lagrange
Đối với bài toán: cực tiểu hóa f(x) để h(x) = 0.
**Lagrange:** L(x, λ) = f(x) + λh(x)
Ở mức tối ưu: ∇ₓL = 0 và ∇_λL = 0 (cho h(x) = 0).
**Ví dụ đã thực hiện:** Giảm thiểu f(x,y) = x² + y² theo x + y = 1.
- L = x2 + y2 + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Ràng buộc: x + y = 1 → −λ = 1 → λ = −1
- Giải: x = 1/2, y = 1/2, f = 1/2
### Điều kiện KKT
**Các điều kiện Karush-Kuhn-Tucker (KKT)** tổng quát hóa các số nhân Lagrange cho các ràng buộc bất đẳng thức.
Với: cực tiểu f(x) tuân theo gᵢ(x) 0, hⱼ(x) = 0.
**Lagrangian:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Điều kiện KKT** (cần thiết để tối ưu):
| Tình trạng | Phương trình |
|----------||----------|
| Tính cố định | ∇ₓL = 0 |
| Tính khả thi ban đầu | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Tính khả thi kép | λᵢ ≥ 0 |
| Sự lỏng lẻo bổ sung | λᵢgᵢ(x) = 0 với mọi i |
**Độ chùng bổ sung** có nghĩa là: nếu ràng buộc gᵢ không hoạt động (gᵢ(x) < 0), thì λᵢ = 0 (ràng buộc không ảnh hưởng đến lời giải).
Đối với các bài toán lồi thỏa mãn điều kiện Slater thì điều kiện KKT vừa cần vừa đủ.
---

## Tính hai mặt
Mọi vấn đề tối ưu hóa (**nguyên thủy**) đều có vấn đề **kép** liên quan.
### Lưỡng tính yếu và mạnh
| Khái niệm | Tuyên bố |
|----------|----------|
| **Chức năng kép** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Vấn đề kép** | Tối đa hóa g(λ, ν) tùy theo λ ≥ 0 |
| **Lưỡng tính yếu** | Tối ưu kép ≤ Tối ưu nguyên thủy (luôn giữ) |
| **Tính hai mặt mạnh mẽ** | Tối ưu kép = Tối ưu cơ bản (giữ cho các bài toán lồi với điều kiện Slater) |
| **Khoảng cách nhị nguyên** | Tối ưu nguyên thủy − Tối ưu kép (không dưới tính đối ngẫu mạnh) |
### Tại sao tính hai mặt lại quan trọng
| Ứng dụng | Tính hai mặt giúp ích như thế nào |
|-------------|-------------------|
| Giới hạn dưới | Dual cấp chứng chỉ về mức độ tốt của giải pháp cơ bản |
| SVM | Vấn đề kép của SVM dẫn đến thủ thuật kernel |
| Phân tích độ nhạy | Các biến kép đo lường mức độ thay đổi tối ưu nếu các ràng buộc được nới lỏng |
| Phân hủy | Các bài toán lớn có thể được chia thành các bài toán con nhỏ hơn thông qua phép toán kép |
---

## Lập trình số nguyên
Khi một số hoặc tất cả các biến phải là **số nguyên**, vấn đề sẽ trở nên khó khăn hơn nhiều (nói chung là NP-hard).
### Các loại
| Loại | Mô tả |
|------|-------------|
| IP thuần túy | Tất cả các biến phải là số nguyên |
| IP hỗn hợp (MIP) | Một số biến nguyên, một số liên tục |
| IP nhị phân | Các biến bị giới hạn ở {0, 1} |
### Phương pháp giải
| Phương pháp | Ý tưởng |
|--------|------|
| **Chi nhánh và ràng buộc** | Chia thành các bài toán con, giải bài thư giãn LP, cắt tỉa |
| **Máy bay cắt** | Thêm các ràng buộc tuyến tính để thắt chặt việc nới lỏng LP |
| **Chi nhánh và cắt** | Kết hợp rẽ nhánh và ràng buộc với mặt phẳng cắt |
| **Heuristics** | Tham lam, tìm kiếm cục bộ, mô phỏng quá trình ủ cho các giải pháp gần đúng |
---

## Phương pháp Heuristic và Metaheuristic
Khi việc tối ưu hóa chính xác là khó khăn, các phương pháp phỏng đoán sẽ tìm ra các giải pháp tốt (không nhất thiết phải tối ưu).
| Phương pháp | Ý tưởng chính | Tốt nhất cho |
|--------|----------|----------|
| **Giảm độ dốc** | Đi theo con đường dốc nhất | Chức năng mượt mà, khác biệt |
| **Phương pháp Newton** | Sử dụng thông tin bậc hai (độ cong) | Các vấn đề được giải quyết ổn thỏa, ổn định |
| **Ủ mô phỏng** | Chấp nhận các giải pháp tồi tệ hơn với xác suất giảm dần | Tối ưu hóa toàn cầu, tổ hợp |
| **Thuật toán di truyền** | Tiến hóa quần thể bằng cách chọn lọc, lai ghép, đột biến | Đa mục tiêu, không khác biệt |
| **Bầy hạt** | Đặc vụ khám phá không gian, chịu ảnh hưởng của các vị trí nổi tiếng nhất | Liên tục, không lồi |
| **Tối ưu hóa Bayes** | Xây dựng mô hình thay thế, sử dụng chức năng thu nhận | Các chức năng hộp đen đắt tiền (điều chỉnh siêu tham số) |
### Phương pháp tối ưu hóa của Newton
**Quy tắc cập nhật:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
trong đó H là ma trận Hessian (ma trận đạo hàm bậc hai).
| Bất động sản | Giá trị |
|----------|-------|
| Tỷ lệ hội tụ | Bậc hai (gần tối ưu) |
| Chi phí mỗi lần lặp | O(n³) cho phép đảo ngược Hessian |
| Yêu cầu | Hessian xác định dương, khả vi hai lần |
| Quasi-Newton (BFGS) | Hessian gần đúng từ độ dốc | O(n²) mỗi lần lặp |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm tối ưu hóa | Ứng dụng |
|----------------------|-------------|
| Độ dốc gốc | Đào tạo mạng lưới thần kinh, hồi quy logistic, bất kỳ mô hình khác biệt nào |
| SGD và các biến thể | ML quy mô lớn (đào tạo theo đợt nhỏ), học trực tuyến |
| Adam, RMSprop | Trình tối ưu hóa mặc định cho deep learning |
| Tối ưu hóa lồi | SVM, hồi quy logistic, LASSO, Ridge (đảm bảo tối ưu toàn cầu) |
| Số nhân Lagrange | Học tập hạn chế, ML công bằng, phân bổ nguồn lực |
| điều kiện KKT | Suy ra SVM kép, hiểu hoạt động ràng buộc |
| Tính hai mặt | Thủ thuật hạt nhân SVM, phân tích độ nhạy, phương pháp phân rã |
| Lập trình tuyến tính | Phân bổ nguồn lực, tối ưu hóa danh mục đầu tư, luồng mạng |
| Lập trình số nguyên | Lựa chọn tính năng (nhị phân), lập kế hoạch, các vấn đề tổ hợp |
| Tối ưu hóa Bayes | Điều chỉnh siêu tham số (Optuna, Hyperopt) |
| Newton/gần như Newton | Phương pháp bậc hai cho các bài toán vừa và nhỏ (L-BFGS) |
---

## Bản tóm tắt
| Phương pháp | Loại vấn đề | Đảm bảo | Quy mô |
|--------|-------------|-------------|-------|
| Đơn giản | Lập trình tuyến tính | Chính xác tối ưu | Hàng triệu biến |
| Điểm nội thất | Lồi (LP, QP, SOCP) | Chính xác tối ưu | Quy mô lớn |
| Độ dốc gốc | Mượt mà không bị giới hạn | Hội tụ về cực tiểu địa phương | Rất lớn (học sâu) |
| SGD | Rủi ro thực nghiệm quy mô lớn | Hội tụ (có phân rã) | Bộ dữ liệu khổng lồ |
| Newton / BFGS | Mượt mà, có thể phân biệt hai lần | Hội tụ bậc hai | Nhỏ đến vừa |
| KKT / Lagrange | Bị ràng buộc (lồi) | Chính xác theo điều kiện | Trung bình |
| Chi nhánh và ràng buộc | Lập trình số nguyên | Chính xác tối ưu | Nhỏ đến vừa |
| Chẩn đoán | Bất kỳ (không lồi, tổ hợp) | Không đảm bảo | Khác nhau |
Tối ưu hóa được cho là công cụ toán học quan trọng nhất trong học máy. Mọi mô hình bạn đào tạo - từ hồi quy tuyến tính đến mô hình ngôn ngữ lớn - đều liên quan đến việc giải quyết vấn đề tối ưu hóa. Việc hiểu khi nào một bài toán lồi (được đảm bảo tối ưu toàn cục), khi nào độ dốc giảm sẽ hội tụ và cách xử lý các ràng buộc sẽ cung cấp cho bạn nền tảng lý thuyết để thiết kế, gỡ lỗi và cải thiện các thuật toán học tập.