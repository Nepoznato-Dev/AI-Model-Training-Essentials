<!--
---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Hệ thống động lực
**Hệ thống động** mô tả cách một trạng thái phát triển theo thời gian theo một quy tắc cố định. Từ quỹ đạo hành tinh đến động thái dân số, từ mô hình thời tiết đến mạng lưới thần kinh huấn luyện, lý thuyết hệ thống động lực cung cấp ngôn ngữ và công cụ để hiểu mọi thứ thay đổi như thế nào. Tệp này bao gồm các phương trình vi phân thông thường (ODE), phương trình vi phân từng phần (PDE), phân tích độ ổn định, hỗn loạn và phân nhánh.
---

## Phương trình vi phân thông thường (ODE)
ODE liên hệ một hàm với các đạo hàm của nó theo một biến độc lập duy nhất (thường là thời gian).
### Phân loại
| Bất động sản | Các loại |
|----------|-------|
| **Đặt hàng** | Hiện tại phái sinh cao nhất (bậc 1, bậc 2, v.v.) |
| **Tuyến tính và phi tuyến** | Tuyến tính: y'' + p(t)y' + q(t)y = g(t); Phi tuyến: bất cứ điều gì khác |
| **Đồng nhất** | g(t) = 0 (không có số hạng bắt buộc) |
| **Tự trị** | Không phụ thuộc rõ ràng vào thời gian: dy/dt = f(y) |
| **Hệ số không đổi** | p, q là các hằng số |
### ODE bậc nhất
**Dạng tổng quát:** dy/dt = f(t, y)
| Loại | Mẫu | Phương pháp giải |
|------|------|-----------------|
| Có thể tách rời | dy/dt = g(t)h(y) | Tách và tích phân: ∫dy/h(y) = ∫g(t)dt |
| Bậc nhất tuyến tính | dy/dt + p(t)y = q(t) | Hệ số tích phân: μ(t) = e^(∫p dt) |
| Chính xác | M(t,y)dt + N(t,y)dy = 0 với ∂M/∂y = ∂N/∂t | Tìm hàm thế F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Thay thế v = y^(1−n) để tuyến tính hóa |
**Ví dụ đã làm (Tích phân hệ số):** Giải dy/dt + 2y = e^(−t), y(0) = 1.
- Hệ số tích phân: μ(t) = e^(∫2 dt) = e^(2t)
- Nhân: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Tích phân: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Điều kiện ban đầu: y(0) = 1 → 1 = 1 + C → C = 0
- Giải: y(t) = e^(−t)
### ODE tuyến tính bậc hai
**Dạng tổng quát:** ay'' + by' + cy = g(t)
**Trường hợp thuần nhất** (g ​​= 0): Giải phương trình đặc tính ar² + br + c = 0.
| Phân biệt đối xử | Rễ | Giải pháp chung |
|-------------|-------|-------------------|
| b² > 4ac (quá tải) | Hai r₁ thực khác biệt, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (giảm chấn nghiêm trọng) | Lặp đi lặp lại gốc thực r | y = (C₁ + C₂t)e^(rt) |
| b2 < 4ac (giảm âm) | Các nghiệm phức α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Giải thích vật lý:** Một hệ giảm chấn lò xo khối lượng mx'' + bx' + kx = 0.
- Overdamped: giảm chấn nặng, không dao động (đóng cửa)
- Giảm chấn tới hạn: quay trở lại nhanh nhất mà không bị dao động (mục tiêu thiết kế hệ thống treo ô tô)
- Underdamped: dao động với biên độ giảm dần (dây đàn guitar)
### Hệ thống ODE
Nhiều hệ thống thực tế bao gồm nhiều biến tương tác:
dx/dt = f(x, y)
dy/dt = g(x, y)
Điều này có thể được viết dưới dạng vector: d**x**/dt = **F**(**x**)
**Hệ thống tuyến tính:** d**x**/dt = A**x**, trong đó A là ma trận.
Lời giải phụ thuộc vào giá trị riêng của A:
| Giá trị riêng | Hành vi |
|-------------|-------------|
| Cả thực, tiêu cực | Nút ổn định (tất cả các quỹ đạo đều hội tụ về điểm gốc) |
| Cả thực tế, tích cực | Nút không ổn định |
| Dấu hiệu thực, trái ngược | Điểm yên ngựa (không ổn định) |
| Phần thực phức, phần thực âm | Xoắn ốc ổn định (dao động tắt dần) |
| Phần thực phức, dương | Xoắn ốc không ổn định |
| Tưởng tượng thuần túy | Trung tâm (quỹ đạo kín) |
---

## Chân dung pha
**Chân dung pha** trực quan hóa quỹ đạo của một hệ động lực trong không gian trạng thái (mà không giải quyết một cách rõ ràng).
### Các tính năng chính
| Tính năng | Mô tả |
|----------|-------------|
| **Điểm cố định (cân bằng)** | Trong đó dx/dt = 0 (không chuyển động) |
| **Quỹ đạo** | Đường đi được hệ thống vạch ra trong không gian trạng thái |
| **Nulcline** | Đường cong trong đó đạo hàm của một thành phần bằng 0 |
| **Chu kỳ giới hạn** | Quỹ đạo khép kín cô lập (dao động tự duy trì) |
| **Lưu vực hấp dẫn** | Tập các điều kiện ban đầu dẫn tới một nhân hút cho trước |
| **Tách** | Ranh giới giữa các lưu vực hấp dẫn khác nhau |
### Mô hình Predator-Prey (Lotka-Volterra)
dx/dt = αx − βxy (con mồi)
dy/dt = δxy − γy (động vật ăn thịt)
**Điểm cố định:**
1. (0, 0) — tuyệt chủng (điểm yên ngựa)
2. (γ/δ, α/β) — cùng tồn tại (trung tâm — quỹ đạo đóng)
Hệ thống thể hiện các dao động định kỳ: con mồi tăng → động vật ăn thịt tăng → con mồi giảm → động vật ăn thịt giảm → chu kỳ lặp lại.
---

## Phân tích độ ổn định
### Ổn định tuyến tính
Đối với một điểm cố định x*, tuyến tính hóa quanh điểm đó: đặt u = x − x*, khi đó du/dt ≈ J(x*)u trong đó J là ma trận Jacobian.
**Tiêu chí ổn định:** Điểm cố định là:
- **Ổn định** nếu mọi giá trị riêng của J đều có phần thực âm
- **Không ổn định** nếu bất kỳ giá trị riêng nào cũng có phần thực dương
- **Ổn định biên** nếu giá trị riêng không có phần thực (cần phân tích phi tuyến)
### Tính ổn định của Lyapunov
**Phương pháp trực tiếp của Lyapunov** xác định độ ổn định mà không cần tuyến tính hóa.
**Hàm Lyapunov** V(x) thỏa mãn:
1. V(x*) = 0 và V(x) > 0 với x ≠ x* (xác định dương)
2. dV/dt 0 dọc theo quỹ đạo (không tăng)
| Tình trạng | Kết luận |
|----------||-------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Không ổn định |
**Ví dụ đã làm:** Hệ dx/dt = −x + y², dy/dt = −y.
- Thử V(x,y) = x² + y² (hàm dạng năng lượng)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Gần gốc tọa độ: dV/dt ≈ −2x² − 2y² < 0 (đối với y nhỏ thì −2y² chiếm ưu thế)
- Kết luận: gốc ổn định tiệm cận cục bộ
---

## Lý thuyết hỗn loạn
**Sự hỗn loạn** mang tính quyết định nhưng không thể đoán trước: hệ thống tuân theo các quy tắc chính xác, nhưng những khác biệt nhỏ trong điều kiện ban đầu dẫn đến những kết quả rất khác nhau.
### Yêu cầu đối với Hỗn loạn
| Bất động sản | Mô tả |
|----------|-------------|
| Xác định | Không có sự ngẫu nhiên - bị chi phối bởi các phương trình chính xác |
| Nhạy cảm với điều kiện ban đầu | Quỹ đạo gần đó phân kỳ theo cấp số nhân |
| Bị ràng buộc | Quỹ đạo không thoát tới vô cùng |
| Không định kỳ | Không bao giờ lặp lại chính xác |
### Hệ thống Lorenz
Ví dụ kinh điển về sự hỗn loạn tất định:
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz
Với các thông số chuẩn σ = 10, ρ = 28, β = 8/3:
- Hệ có 3 điểm cố định, tất cả đều không ổn định
- Quỹ đạo quay quanh một điểm cố định rồi đột ngột chuyển sang điểm cố định khác
- Kết quả là **s hút Lorenz** — một đường hút kỳ lạ có cấu trúc fractal
**Số mũ Lyapunov:** Đo tốc độ phân kỳ của các quỹ đạo gần đó.
- Số mũ Lyapunov dương → hỗn loạn
- Đối với hệ Lorenz có tham số chuẩn: số mũ lớn nhất ≈ 0,9 > 0
### Bản đồ hậu cần
Một hệ thống rời rạc đơn giản thể hiện sự hỗn loạn:
x_{n+1} = rx_n(1 − x_n)
| Tham số r | Hành vi |
|-------------|-------------|
| 0 < r < 1 | Dân số chết đi (x → 0) |
| 1 < r < 3 | Điểm cố định ổn định tại x = 1 − 1/r |
| 3 < r < 3.449 | Dao động chu kì 2 |
| 3,449 < r < 3,544 | Dao động chu kì 4 |
| 3,544 < r < 3,570 | Chu kỳ-8, 16, 32, ... (thác nhân đôi chu kỳ) |
| r ≈ 3,570 | Bắt đầu hỗn loạn |
| 3.570 < r < 4 | Chủ yếu là hỗn loạn, với các cửa sổ định kỳ |
| r = 4 | Hoàn toàn hỗn loạn trên [0, 1] |
### Hiệu ứng cánh bướm
Tên phổ biến cho sự phụ thuộc nhạy cảm vào điều kiện ban đầu. Trong các hệ thống thời tiết (được mô hình hóa bằng phương trình Lorenz), một con bướm vỗ cánh ở Brazil có thể gây ra một cơn lốc xoáy ở Texas - không phải do con bướm gây ra mà vì những nhiễu loạn nhỏ tăng theo cấp số nhân.
---

## Lý thuyết phân nhánh
**phân nhánh** là sự thay đổi về chất trong hành vi của hệ thống khi tham số thay đổi.
### Các loại phân nhánh
| Phân nhánh | Mẫu bình thường | Điều gì xảy ra |
|-------------|-------------|--------------|
| **Nút yên ngựa** | dx/dt = r − x² | Hai điểm cố định xuất hiện/biến mất |
| ** Xuyên suốt** | dx/dt = rx − x² | Hai điểm cố định trao đổi ổn định |
| **Pitchfork (siêu tới hạn)** | dx/dt = rx − x³ | Một điểm ổn định chia thành hai điểm ổn định + một điểm không ổn định |
| **Pitchfork (cận trọng)** | dx/dt = rx + x³ | Những cành cây không ổn định sẽ sụp đổ (thường là thảm họa) |
| **Hopf** | Hệ thống 2D | Điểm cố định trở nên không ổn định, xuất hiện chu kỳ giới hạn |
### Sơ đồ phân nhánh
Biểu đồ các điểm cố định so với giá trị tham số, thể hiện độ ổn định (rắn = ổn định, nét đứt = không ổn định). Sơ đồ phân nhánh của bản đồ logistic cho thấy lộ trình nhân đôi chu kỳ dẫn đến hỗn loạn và **hằng số Feigenbaum** δ ≈ 4,669 nổi tiếng (tỷ lệ chung giữa các khoảng phân nhánh liên tiếp).
---

## Phương trình vi phân từng phần (PDE)
PDE liên quan đến hàm nhiều biến và đạo hàm riêng của chúng.
### Phân loại PDE tuyến tính bậc hai
Với Au_xx + 2Bu_xy + Cu_yy + ... = 0:
| Loại | Tình trạng | Hành vi | Ví dụ |
|------|--------------|-------------|--------|
| **Hình elip** | B² − AC< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Truyền sóng, bảo toàn nét sắc nét | Phương trình sóng: u_tt = c²u_xx |
### Phương trình nhiệt
∂u/∂t = α ∂²u/∂x²
Mô hình khuếch tán nhiệt, phân bố dân số, định giá quyền chọn (Black-Scholes).
| Bất động sản | Tuyên bố |
|----------|----------|
| Làm mịn | Các giải pháp trở nên trơn tru ngay lập tức, thậm chí từ dữ liệu ban đầu không liên tục |
| Nguyên tắc tối đa | Nhiệt độ tối đa xảy ra tại thời điểm biên hoặc thời điểm ban đầu |
| Đảo ngược thời gian | Không thể đảo ngược - không thể chạy lùi |
### Phương trình sóng
∂²u/∂t² = c² ∂²u/∂x²
Mô hình dây dao động, âm thanh, sóng điện từ.
| Bất động sản | Tuyên bố |
|----------|----------|
| Tuyên truyền | Nhiễu loạn di chuyển với tốc độ c |
| Khả năng đảo ngược | Đảo ngược thời gian |
| giải pháp d'Alembert | u(x,t) = f(x−ct) + g(x+ct) (sự chồng chất của sóng trái/phải) |
### Phương trình Laplace
∇`u = ∂`u/∂x` + ∂`u/∂y` = 0
Giải pháp (hàm điều hòa) biểu thị nhiệt độ ở trạng thái ổn định, thế tĩnh điện, dòng chất lỏng không nén được.
| Bất động sản | Tuyên bố |
|----------|----------|
| Thuộc tính giá trị trung bình | u(x₀) = trung bình của u trên bất kỳ đường tròn nào có tâm tại x₀ |
| Nguyên tắc tối đa | Không có cực đại hoặc cực tiểu bên trong |
| Tính độc đáo | Xác định hoàn toàn bởi điều kiện biên |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm DS | Ứng dụng |
|----------||-------------|
| ODE | ODE thần kinh (mạng có độ sâu liên tục), động lực mạng tái phát |
| Phân tích độ ổn định | Động lực đào tạo của việc giảm độ dốc (mất mát có giảm ổn định không?) |
| Hàm Lyapunov | Chứng minh sự hội tụ của các thuật toán học tập, tăng cường tính ổn định học tập |
| Hỗn loạn | Hiểu độ nhạy trong RNN (độ dốc biến mất/nổ), dự báo thời tiết |
| Phân nhánh | Chuyển tiếp các giai đoạn trong học tập (grokking), thay đổi chế độ trong động lực đào tạo |
| PDE | Mô hình khuếch tán (mô hình tổng quát dựa trên điểm số), mạng lưới thần kinh thông tin vật lý |
| Phương trình nhiệt | Các quá trình khuếch tán trong mô hình tổng quát, làm mịn đồ thị Laplacian |
| Phương trình sóng | Xử lý dữ liệu địa chấn, mô hình tín hiệu âm thanh |
| Lotka-Volterra | Động lực dân số, dịch tễ học, các tác nhân ML cạnh tranh |
| Chân dung pha | Trực quan hóa động lực cảnh quan mất mát, tìm hiểu đào tạo GAN |
---

## Bản tóm tắt
| Chủ đề | Ý tưởng cốt lõi | Công cụ chính |
|-------|-------------|----------|
| ODE | Hàm số và đạo hàm theo thời gian | Phương trình đặc trưng, ​​tích phân |
| Hệ thống ODE | Nhiều biến tương tác | Phân tích giá trị riêng của Jacobian |
| Chân dung pha | Trực quan hóa động lực học trong không gian trạng thái | Điểm cố định, đường null, chu kỳ giới hạn |
| Tính ổn định | Hệ thống sẽ trở lại trạng thái cân bằng? | Tuyến tính hóa, hàm Lyapunov |
| Hỗn loạn | Tính không thể đoán trước | Số mũ Lyapunov, các nhân hút lạ |
| Phân nhánh | Thay đổi định tính với các tham số | Dạng chuẩn, sơ đồ phân nhánh |
| PDE | Hàm nhiều biến | Phương trình nhiệt, sóng và Laplace |
Lý thuyết hệ thống động lực là toán học về sự thay đổi. Nó giải thích tại sao một số hệ ổn định, tại sao một số dao động và tại sao một số lại hành xử hỗn loạn. Đối với các nhà khoa học dữ liệu, nó cung cấp các công cụ để hiểu động lực đào tạo, thiết kế các thuật toán ổn định, lập mô hình chuỗi thời gian và xây dựng thế hệ mô hình học máy tiếp theo dựa trên vật lý.