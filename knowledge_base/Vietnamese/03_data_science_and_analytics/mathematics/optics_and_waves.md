---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
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
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Quang học và Sóng
Sóng có ở khắp mọi nơi: âm thanh, ánh sáng, nước, tín hiệu vô tuyến, biên độ xác suất lượng tử, biến động của thị trường chứng khoán và sự rung động khi kích hoạt mạng lưới thần kinh. Quang học - nghiên cứu về ánh sáng - là ngành khoa học sóng phát triển nhất và các công cụ toán học của nó (phân tích Fourier, giao thoa, nhiễu xạ) áp dụng cho mọi hiện tượng sóng. Hiểu biết về sóng là điều cần thiết để xử lý tín hiệu, phân tích hình ảnh, truyền thông và lớp vật lý của mọi công nghệ hiện đại.
---

## Phương trình sóng
### Phương trình sóng tổng quát
Phương trình sóng một chiều:
∂²u/∂t² = c² ∂²u/∂x²
trong đó u(x,t) là độ dịch chuyển của sóng và c là tốc độ sóng.
### Giải pháp chung (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
trong đó f là sóng truyền sang phải và g là sóng truyền sang trái.
### Thông số sóng chính
| Tham số | Biểu tượng | Đơn vị | Mô tả |
|----------|--------|------|-------------|
| Biên độ | A | khác nhau | Chuyển vị tối đa |
| Bước sóng | λ | mét | Khoảng cách giữa các đỉnh liên tiếp |
| Tần số | f hoặc ν | Hertz (Hz) | Chu kỳ mỗi giây |
| Thời kỳ | T = 1/f | giây | Thời gian cho một chu kỳ hoàn chỉnh |
| Số sóng | k = 2π/λ | rad/m | Tần số không gian |
| Tần số góc | ω = 2πf | rad/s | Tần số tạm thời |
| Tốc độ sóng | c = fλ = ω/k | m/s | Tốc độ lan truyền |
### Sóng hình sin
u(x,t) = A sin(kx − ωt + φ)
trong đó φ là hằng số pha.
### Tốc độ sóng trong các phương tiện khác nhau
| Loại sóng | Trung bình | Công thức tốc độ |
|----------|--------|---------------|
| Chuỗi | Lực căng T, mật độ tuyến tính μ | c = √(T/μ) |
| Âm thanh | Mô đun khối B, mật độ ρ | c = √(B/ρ) |
| Âm thanh (khí lý tưởng) | γ, R, T, M | c = √(γRT/M) |
| Sóng EM | Độ thấm ε, độ thấm μ | c = 1/√(με) |
| Sóng EM (chân không) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Chồng chất và giao thoa
### Nguyên lý chồng chất
Khi hai hoặc nhiều sóng chồng lên nhau, độ dịch chuyển tổng hợp là tổng của các độ dịch chuyển riêng lẻ:
u_total = u₁ + u₂ + ... + uₙ
Điều này đúng cho các phương trình sóng tuyến tính.
### Sự giao thoa của hai sóng
Hai sóng có cùng tần số, cùng biên độ, lệch pha Δφ:
u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Độ lệch pha | Kết quả | Cường độ |
|--------|--------|----------|
| Δφ = 0, 2π, 4π, ... | **Có tính xây dựng** (biên độ = 2A) | 4I₀ (tối đa) |
| Δφ = π, 3π, 5π, ... | **Có tính phá hủy** (biên độ = 0) | 0 (tối thiểu) |
| Δφ = π/2 | Một phần | 2I₀ |
### Điều kiện gây nhiễu
| Tình trạng | Loại | Sự khác biệt về con đường |
|----------|------|-----------------|
| Mang tính xây dựng | Rìa sáng | ΔL = mλ (m = 0, 1, 2, ...) |
| Phá hoại | Rìa tối | ΔL = (m + ½)λ |
---

## Thí nghiệm khe đôi của Young
Ánh sáng truyền qua hai khe hẹp cách nhau khoảng d, tạo ra vân giao thoa trên màn hứng ở khoảng cách L.
### Vị trí rìa
| Rìa | Vị trí trên màn hình |
|--------|-------------------|
| Sáng (cực đại) | y_m = mλL/d |
| Tối (tối thiểu) | y_m = (m + ½)λL/d |
| Khoảng cách rìa | Δy = λL/d |
Thí nghiệm này đã chứng minh bản chất sóng của ánh sáng (Thomas Young, 1801) và sau đó trở thành trung tâm của cơ học lượng tử (lưỡng tính sóng-hạt).
---

## Nhiễu xạ
**Nhiễu xạ** là sự uốn cong và lan truyền của sóng xung quanh chướng ngại vật và xuyên qua các khe hở.
### Nhiễu xạ một khe
Ánh sáng qua khe có chiều rộng a tạo ra vân sáng và vân tối.
| Tính năng | Tình trạng |
|----------|----------|
| Trung tâm tối đa | Rộng nhất và sáng nhất; chiều rộng = 2λL/a |
| Cực tiểu (rìa tối) | một tội lỗi θ = mλ (m = ±1, ±2, ...) |
| Cực đại thứ cấp | Khoảng giữa tối thiểu; mờ hơn nhiều |
### Cách tử nhiễu xạ
N khe cách đều nhau (khoảng cách d) tạo ra cực đại rất sắc nét:
d sinθ = mλ (m = 0, 1, 2, ...)
| Bất động sản | Hiệu ứng |
|----------|--------|
| Nhiều khe hơn (N lớn hơn) | Cực đại sắc nét hơn, sáng hơn |
| Quyền lực giải quyết | R = mN (có thể phân biệt được các bước sóng gần) |
| Ứng dụng | Quang phổ, đo bước sóng |
### Tiêu chí Rayleigh (Giới hạn độ phân giải)
Hai nguồn điểm chỉ có thể phân giải được khi cực đại trung tâm của một nguồn nằm trên mức tối thiểu đầu tiên của nguồn kia:
θ_min = 1,22 λ/D
trong đó D là đường kính khẩu độ.
| Hệ thống | λ | D | θ_min |
|--------|---|---|-------|
| Mắt người | 550nm | 5 mm | 1,3 × 10⁻⁴ rad (~0,01°) |
| Kính viễn vọng Không gian Hubble | 550nm | 2,4m | 2,8 × 10⁻⁷ rad |
| Kính thiên văn vô tuyến (Arecibo) | 21 cm | 305 m | 8,4 × 10⁻⁴ rad |
---

## Phân cực
**Phân cực** mô tả hướng dao động của điện trường trong sóng ngang.
### Các loại phân cực
| Loại | Mô tả |
|------|-------------|
| **Tuyến tính** | E dao động trong mặt phẳng cố định |
| **Thông tư** | E quay một vòng tròn (thuận tay phải hoặc tay trái) |
| **Hình elip** | E vẽ một hình elip (tổng quát nhất) |
| **Không phân cực** | Hỗn hợp ngẫu nhiên của tất cả các phân cực (ánh sáng tự nhiên nhất) |
### Định luật Malus
Khi ánh sáng phân cực đi qua kính phân cực ở góc θ so với hướng phân cực:
Tôi = I₀ cos²θ
| Góc θ | Cường độ truyền qua |
|----------|----------------------|
| 0° | 100% (I₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (bị chặn hoàn toàn) |
### Phân cực bằng phản xạ (Góc Brewster)
Ánh sáng phản xạ ở góc Brewster bị phân cực hoàn toàn:
tan θ_B = n₂/n₁
| Giao diện | n₁ | n₂ | θ_B |
|----------|------|------|------|
| Không khí → thủy tinh | 1.0 | 1,5 | 56,3° |
| Không khí → nước | 1.0 | 1.33 | 53,1° |
| Thủy tinh → kim cương | 1,5 | 2,42 | 58,1° |
---

## Quang học hình học
Quang học hình học (tia) coi ánh sáng là các tia truyền theo đường thẳng, uốn cong ở các mặt phân cách.
### Định luật Snell (Khúc xạ)
n₁ sinθ₁ = n₂ sinθ₂
| Chất liệu | Chỉ số khúc xạ n |
|----------|-------------------|
| Hút chân không | 1.000 |
| Không khí | 1.0003 |
| Nước | 1.33 |
| Kính (vương miện) | 1,52 |
| Thủy tinh (đá lửa) | 1,62 |
| Kim cương | 2,42 |
### Phản xạ toàn phần bên trong
Khi ánh sáng truyền từ môi trường chiết quang hơn sang môi trường chiết quang kém hơn **góc tới hạn**:
θ_c = arcsin(n₂/n₁)
Tất cả ánh sáng đều bị phản xạ - đây là cách hoạt động của sợi quang.
### Phương trình thấu kính mỏng
1/f = 1/d_o + 1/d_i
| Số lượng | Ý nghĩa |
|----------|----------|
| f | Tiêu cự |
| d_o | Khoảng cách đối tượng |
| d_i | Khoảng cách hình ảnh |
| M = −d_i/d_o | Phóng đại |
| Loại ống kính | f | Hình ảnh |
|----------|---|-------|
| Hội tụ (lồi) | Tích cực | Thực (nếu d_o > f) hoặc ảo |
| Phân kỳ (lõm) | Tiêu cực | Luôn ảo, ngay thẳng, thu gọn |
### Phương trình gương
Có dạng tương tự như phương trình thấu kính: 1/f = 1/d_o + 1/d_i, trong đó f = R/2 đối với gương cầu.
---

## Quang học Fourier
Quang học Fourier xử lý hình ảnh và nhiễu xạ như các phép biến đổi Fourier.
### Nguyên tắc chính
Mẫu nhiễu xạ trường xa của khẩu độ là **Biến đổi Fourier** của hàm khẩu độ.
| Khẩu độ | Mẫu nhiễu xạ (Biến đổi Fourier) |
|----------|-------------------------------------------------------|
| Khe đơn | hàm chân thành |
| Khẩu độ tròn | Đĩa thoáng (J₁(r)/r) |
| Khẩu độ hình chữ nhật | 2D chân thành |
| Lưới | Hàm delta rời rạc |
### Biến đổi Fourier quang
Một ống kính thực hiện biến đổi Fourier 2D: đặt một vật thể ở mặt phẳng tiêu cự phía trước sẽ tạo ra biến đổi Fourier của nó ở mặt phẳng tiêu cự phía sau.
### Ứng dụng
| Ứng dụng | Quang học Fourier giúp ích như thế nào |
|-------------|--------------------------|
| Lọc hình ảnh | Đặt mặt nạ ở mặt phẳng Fourier để chặn/vượt qua tần số không gian |
| Phát hiện cạnh | Lọc thông cao trong mặt phẳng Fourier |
| Nhận dạng mẫu | Tương quan thông qua biến đổi Fourier |
| Hình ba chiều | Ghi lại và tái tạo mặt sóng |
| Điện toán quang học | Thực hiện các phép biến đổi Fourier với tốc độ ánh sáng |
---

## Âm thanh và Âm học
### Thuộc tính sóng âm
| Bất động sản | Phạm vi điển hình | Đơn vị |
|----------|--------------|------|
| Tần số | 20 − 20.000 (thính giác của con người) | Hz |
| Tốc độ (không khí, 20°C) | 343 | m/s |
| Tốc độ (nước) | 1.480 | m/s |
| Tốc độ (thép) | 5.960 | m/s |
| Ngưỡng cường độ | 10⁻¹² | W/m2 |
### Thang đo Decibel
β = 10 log₁₀(I/I₀) dB, trong đó I₀ = 10⁻¹² W/m²
| Âm thanh | Cường độ (W/m2) | Mức (dB) |
|-------|-------------------|-------------|
| Ngưỡng nghe | 10⁻¹² | 0 |
| Lá xào xạc | 10⁻¹¹ | 10 |
| Trò chuyện bình thường | 10⁻⁶ | 60 |
| Buổi hòa nhạc rock | 1 | 120 |
| Ngưỡng đau | 10 | 130 |
| Động cơ phản lực | 100 | 140 |
### Hiệu ứng Doppler
Tần số quan sát được khi nguồn và người quan sát chuyển động tương đối với nhau:
f' = f(v ± v_o)/(v ∓ v_s)
| Kịch bản | Hiệu ứng |
|----------|--------|
| Nguồn tiếp cận | Tần số cao hơn (chuyển đổi màu xanh cho ánh sáng) |
| Nguồn rút lui | Tần số thấp hơn (sự dịch chuyển màu đỏ đối với ánh sáng) |
| Ứng dụng | Radar, siêu âm y tế, thiên văn học (dịch chuyển đỏ của các thiên hà) |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm Sóng/Quang học | Ứng dụng |
|----------------------|-------------|
| Phương trình sóng | Mạng lưới thần kinh thông tin vật lý, phân tích dữ liệu địa chấn, xử lý âm thanh |
| Phân tích Fourier | Cơ sở xử lý tín hiệu, phân tích quang phổ, trích chọn đặc trưng |
| Biến đổi Fourier | CNN ngầm thực hiện phân tích Fourier cục bộ; FFT được sử dụng trong tiền xử lý dữ liệu |
| Can thiệp | Điện toán tương tự, mạng lưới thần kinh quang học |
| Nhiễu xạ | Mô hình hình thành ảnh, thuật toán làm mờ, chụp ảnh tính toán |
| Phân cực | Viễn thám, phân loại vật liệu, phân tích ảnh vệ tinh |
| Quang học hình học | Các mẫu máy ảnh trong thị giác máy tính, dò tia để tạo dữ liệu tổng hợp |
| Phương trình thấu kính | Hiệu chỉnh camera, ước tính độ sâu, tái tạo 3D |
| Quang học Fourier | Điện toán quang học, mạng lưới thần kinh sâu nhiễu xạ (D²NN) |
| Hiệu ứng Doppler | Xử lý tín hiệu radar, hình ảnh y tế (siêu âm Doppler), ước tính vận tốc |
| Thang đo decibel | Kỹ thuật tính năng âm thanh, tiền xử lý nhận dạng giọng nói |
| Lý thuyết lấy mẫu | Định lý Nyquist-Shannon kết nối lý thuyết sóng với xử lý tín hiệu số |
---

## Bản tóm tắt
| Chủ đề | Ý tưởng cốt lõi | Phương trình khóa |
|-------|----------||-------------|
| Phương trình sóng | Sóng truyền với tốc độ c | ∂`u/∂t` = c`∂`u/∂x` |
| Sự chồng chất | Sóng thêm tuyến tính | u = u₁ + u₂ |
| Can thiệp | Giai đoạn xác định việc củng cố | Δφ = 2πΔL/λ |
| Nhiễu xạ | Sóng uốn quanh chướng ngại vật | a sin θ = mλ (khe đơn) |
| Phân cực | Định hướng dao động | Định luật Malus: I = I₀cos²θ |
| Quang học hình học | Ánh sáng như tia sáng | Định luật Snell: n₁sinθ₁ = n₂sinθ₂ |
| Quang học Fourier | Hình ảnh dưới dạng biến đổi Fourier | Trường xa = FT của khẩu độ |
| Hiệu ứng Doppler | Sự thay đổi tần số từ chuyển động | f' = f(v ± v_o)/(v ∓ v_s) |
Sóng là ngôn ngữ phổ quát của các hệ dao động. Cho dù bạn đang xử lý tín hiệu âm thanh, phân tích chuỗi thời gian, thiết kế hệ thống nhận dạng hình ảnh hay xây dựng mô phỏng vật lý, toán học về sóng — chồng chất, phân tích Fourier, giao thoa, nhiễu xạ — đều cung cấp bộ công cụ cần thiết. Quang học, với tư cách là ngành khoa học sóng trưởng thành nhất, cung cấp cả nền tảng lý thuyết và kỹ thuật thực hành thấm nhuần khoa học dữ liệu hiện đại.