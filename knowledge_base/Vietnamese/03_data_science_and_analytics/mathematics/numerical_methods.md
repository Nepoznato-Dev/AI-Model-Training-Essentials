---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Phương pháp số
Phương pháp số là cầu nối giữa lý thuyết toán học và tính toán thực tế. Trong khi toán học thuần túy chứng minh rằng các nghiệm tồn tại thì các phương pháp số thực sự tính toán các câu trả lời gần đúng với độ chính xác hữu hạn. Mọi mô hình học máy, mô phỏng vật lý và quy trình phân tích dữ liệu cuối cùng đều dựa vào tính toán số. Hiểu các phương pháp này — độ chính xác, tính ổn định và hạn chế của chúng — là điều cần thiết để xây dựng phần mềm đáng tin cậy.
---

## Số học dấu phẩy động
Máy tính biểu diễn số thực với độ chính xác hữu hạn. **Tiêu chuẩn IEEE 754** xác định cách lưu trữ và xử lý các số có dấu phẩy động.
### Định dạng IEEE 754
| Định dạng | Bit | Số mũ | thần chú | Chữ số thập phân gần đúng | Phạm vi |
|--------|------|----------|----------|--------------------------|-------|
| Một nửa (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Độc thân (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Đôi (fp64) | 64 | 11 | 52 | 15,9 | ±1,8 × 10³⁰⁸ |
### Máy Epsilon
**Epsilon máy** (ε_mach) là số nhỏ nhất sao cho 1 + ε_mach > 1 ở dạng dấu phẩy động.
| Định dạng | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Những cạm bẫy thường gặp
| Cạm bẫy | Ví dụ | Hậu quả |
|----------|----------|-------------|
| **Hủy bỏ thảm khốc** | Tính (1 + x) − 1 cho x nhỏ | Mất chữ số có nghĩa |
| **Hấp thụ** | 10⁸ + 1 = 10⁸ trong fp32 | Giá trị nhỏ bị mất với số tiền lớn |
| **Không liên kết** | (a + b) + c ≠ a + (b + c) | Tổng thứ tự quan trọng |
| **Chia cho gần bằng 0** | 1/10⁻³⁰⁰ → tràn | Vô cực hoặc NaN |
### Chiến lược giảm thiểu
| Chiến lược | Mô tả |
|----------|-------------|
| **Tóm tắt Kahan** | Tổng bù để giảm lỗi hấp thụ |
| **Kahan-Babuska-Neumaier** | Phiên bản cải tiến của phép tính tổng Kahan |
| **Tổng hợp được sắp xếp** | Tính tổng số nhỏ trước để tránh bị hấp thụ |
| **Số học nhân đôi** | Sử dụng các cặp đôi để có độ chính xác cao hơn |
| **Phân tích điều hòa** | Hiểu liệu bản thân vấn đề có khuếch đại lỗi hay không |
---

## Tìm gốc
Tìm x sao cho f(x) = 0.
### Phương pháp chia đôi
| Bất động sản | Giá trị |
|----------|-------|
| Yêu cầu | f liên tục, f(a) và f(b) trái dấu |
| Hội tụ | Tuyến tính (sai số giảm một nửa mỗi bước) |
| Được đảm bảo? | Có - luôn hội tụ |
| Lặp lại cho chữ số d | ≈ d / log₁₀(2) ≈ 3,32d |
**Thuật toán:**
1. Bắt đầu với khoảng [a, b] trong đó f(a) · f(b) < 0
2. Tính trung điểm c = (a + b)/2
3. Nếu f(c) = 0 hoặc |b − a| < khoan dung, dừng lại
4. Nếu f(a) · f(c) < 0 thì đặt b = c; nếu không đặt a = c
5. Lặp lại
### Phương pháp Newton-Raphson
| Bất động sản | Giá trị |
|----------|-------|
| Yêu cầu | f khả vi, f'(x) ≠ 0 tại nghiệm |
| Hội tụ | Bậc hai (gần căn) |
| Được đảm bảo? | Không - có thể phân kỳ hoặc quay vòng |
| Cập nhật quy tắc | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Ví dụ đã giải:** Tìm √2 bằng cách giải f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1.41421356... (đúng đến 8 chữ số thập phân)
### Phương pháp cát tuyến
Giống như phương pháp Newton nhưng gần đúng với đạo hàm:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Bất động sản | Giá trị |
|----------|-------|
| Hội tụ | Siêu tuyến tính (bậc ≈ 1.618, tỷ lệ vàng) |
| Yêu cầu | Hai lần đoán ban đầu (không cần đạo hàm) |
### So sánh các phương pháp tìm gốc
| Phương pháp | Hội tụ | Cần phái sinh? | Được đảm bảo? | Chi phí mỗi bước |
|--------|-------------|-------------------|-------------|--------------|
| Chia đôi | Tuyến tính (1) | Không | Có | Đánh giá 1 hàm |
| Newton-Raphson | Bậc hai (2) | Có | Không | Đánh giá 2 chức năng |
| cát tuyến | Siêu tuyến tính (1.618) | Không | Không | Đánh giá 1 hàm |
| Phương pháp Brent | Siêu tuyến tính | Không | Có | Khác nhau |
**Phương pháp của Brent** kết hợp phép chia đôi (sự hội tụ được đảm bảo) với phép nội suy bậc hai cát tuyến/nghịch đảo (hội tụ nhanh). Nó là công cụ tìm gốc mặc định trong hầu hết các thư viện số.
---

## Tích phân số (Quadrature)
Đang tính xấp xỉ ∫ₐᵇ f(x) dx.
### Phương pháp
| Phương pháp | Công thức | Lỗi | Đặt hàng |
|--------|----------|-------|-------|
| **Hình chữ nhật (điểm giữa)** | (b−a) · f((a+b)/2) | O(h2) | 1 |
| **Hình thang** | (b−a)/2 · [f(a) + f(b)] | O(h2) | 2 |
| **1/3 của Simpson** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Ngày 8/3 của Simpson** | Sử dụng 4 điểm cách đều nhau | O(h⁴) | 4 |
| **Bình phương Gaussian** | Vị trí nút tối ưu | O(h²ⁿ) | n điểm |
### Quy tắc tổng hợp
Với n khoảng con có chiều rộng h = (b−a)/n:
| Quy tắc | Công thức tổng hợp | Lỗi |
|------|-------------------|-------|
| Hình thang tổng hợp | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h2) |
| Simpson tổng hợp | h/3[f(a) + 4Σf(lẻ) + 2Σf(chẵn) + f(b)] | O(h⁴) |
**Ví dụ đã thực hiện:** Ước tính ∫₀¹ e^(−x²) dx bằng cách sử dụng hình thang tổng hợp có n = 4.
- h = 0,25, điểm: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Giá trị thực: ≈ 0,7468 (sai số ≈ 0,5%)
### Cầu phương thích ứng
Tự động chia nhỏ các khoảng trong đó hàm số thay đổi nhanh chóng, sử dụng ít điểm hơn khi hàm số trơn tru. Đây là những gì`scipy.integrate.quad`sử dụng (dựa trên QUADPACK).
---

## Nội suy
Ước tính giá trị giữa các điểm dữ liệu đã biết.
### Phương pháp
| Phương pháp | Mô tả | Độ mượt | Dao động |
|--------|-------------|-------------|-------------|
| **Hàng xóm gần nhất** | Sử dụng điểm dữ liệu gần nhất | Không liên tục | Không có |
| **Tuyến tính** | Nối các điểm bằng đường thẳng | C⁰ (liên tục) | Không có |
| **Đa thức (Lagrange)** | Đa thức đơn qua mọi điểm | C^∞ | Nặng ở nhiều điểm (hiện tượng Runge) |
| **Spline khối** | Khối từng khối, nhẵn ở các khớp | C2 | Tối thiểu |
| **Hàm cơ sở xuyên tâm** | Tổng trọng số của hạt xuyên tâm | Phụ thuộc vào hạt nhân | Thấp |
### Nội suy Lagrange
Cho n+1 điểm (x₀, y₀), ..., (xₙ, yₙ), đa thức duy nhất bậc ≤ n đi qua tất cả các điểm:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Hiện tượng Runge:** Phép nội suy đa thức bậc cao tại các điểm cách đều nhau có thể dao động dữ dội gần các cạnh. Giảm nhẹ bằng cách sử dụng các nút hoặc đường trục Chebyshev.
### Splines khối
Đa thức bậc ba từng phần là C2 liên tục (đạo hàm bậc hai liên tục).
| Loại | Điều kiện biên |
|------|-------------------|
| Spline tự nhiên | S''(x₀) = S''(xₙ) = 0 |
| Spline kẹp | S'(x₀) và S'(xₙ) được chỉ định |
| Không phải là một nút thắt | Đạo hàm cấp ba liên tục tại x₁ và xₙ₋₁ |
---

## Bộ giải ODE
Giải phương trình vi phân thông thường dy/dt = f(t, y) bằng số.
### Phương pháp Euler
Bộ giải ODE đơn giản nhất.
**Cập nhật:** y_{n+1} = y_n + h · f(t_n, y_n)
| Bất động sản | Giá trị |
|----------|-------|
| Đặt hàng | 1 (lỗi mỗi bước: O(h²), toàn cầu: O(h)) |
| Tính ổn định | Ổn định có điều kiện (yêu cầu h nhỏ) |
| Chi phí | Đánh giá 1 chức năng mỗi bước |
### Phương pháp Runge-Kutta
| Phương pháp | Đặt hàng | Giai đoạn | Ghi chú |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Đơn giản nhất |
| **Trung điểm** | 2 | 2 | Độ chính xác tốt hơn |
| **Heun's (RK2)** | 2 | 2 | Dự đoán-sửa lỗi |
| **RK4 cổ điển** | 4 | 4 | Tiêu chuẩn lao động |
| **Hoàng tử ký túc xá (RK45)** | 4(5) | 6 | Kích thước bước thích ứng (được sử dụng trong ode45) |
### RK4 cổ điển (Runge-Kutta bậc 4)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Bất động sản | Giá trị |
|----------|-------|
| Đặt hàng | 4 (lỗi chung: O(h⁴)) |
| Chi phí | 4 đánh giá chức năng mỗi bước |
| Tính ổn định | Tốt hơn nhiều so với Euler |
| Cách sử dụng | Mặc định cho ODE không cố định |
### ODE cứng nhắc
Một ODE **cứng** có các thành phần khác nhau ở những khoảng thời gian rất khác nhau. Các phương pháp rõ ràng (Euler, RK4) yêu cầu kích thước bước nhỏ không thực tế.
| Phương pháp | Loại | Tính ổn định |
|--------|------|----------|
| Euler ngầm định | ngầm định | A-ổn định (ổn định vô điều kiện) |
| Công thức vi phân ngược (BDF) | ngầm định | A-ổn định (tối đa đơn hàng 5) |
| Runge-Kutta ngầm | ngầm định | Có các biến thể ổn định L |
| LSODA | Tự động | Chuyển đổi giữa cứng/không cứng |
---

## Ổn định số và điều hòa
### Số điều kiện
**Số điều kiện** đo lường mức độ thay đổi đầu ra của một vấn đề so với những thay đổi nhỏ ở đầu vào.
Đối với hệ tuyến tính Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Giải thích |
|-------|--------------|
| ≈ 1 | Điều hòa tốt |
| 10³ | Nhạy cảm nhẹ |
| 10⁸ | Điều kiện kém (mất ~8 chữ số chính xác) |
| → ∞ | Số ít (không có giải pháp duy nhất) |
### Tính ổn định của thuật toán
Một thuật toán **ổn định về mặt số** nếu những nhiễu loạn nhỏ ở đầu vào dẫn đến những nhiễu loạn nhỏ ở đầu ra (so với số điều kiện của bài toán).
| Thuật toán | Ổn định? | Ghi chú |
|----------|--------------|-------|
| Loại bỏ Gaussian bằng cách xoay một phần | Có | Cách tiếp cận tiêu chuẩn |
| Tính giá trị riêng qua QR | Có | Ổn định ngược |
| Tổng hợp ngây thơ (lớn + nhỏ trước) | Không | Sử dụng phép tính tổng Kahan |
| Tính phương sai dưới dạng E[X²] − (E[X])² | Có khả năng không | Sử dụng thuật toán trực tuyến của Welford |
### Thuật toán trực tuyến của Welford
Tính toán ổn định về số lượng của giá trị trung bình và phương sai:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Điều này tránh được sự hủy bỏ thảm khốc xảy ra trong công thức hai lượt đơn giản.
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Phương pháp số | Ứng dụng |
|--------|-------------|
| Dấu phẩy động (fp16/fp32/bf16) | Đào tạo có độ chính xác hỗn hợp, lượng tử hóa mô hình, hiệu quả bộ nhớ |
| Tìm gốc | Ước tính khả năng tối đa (tìm nơi gradient = 0) |
| Tích phân số | Suy luận Bayes (tính toán khả năng cận biên), giá trị kỳ vọng |
| Nội suy | Làm mịn, cắt bỏ, mô hình thay thế, chức năng kích hoạt |
| Bộ giải ODE | ODE thần kinh, RNN thời gian liên tục, động lực học dân số, ML thông tin vật lý |
| Số điều kiện | Hiểu các vấn đề về số trong hồi quy tuyến tính, phương trình chuẩn |
| Tổng hợp ổn định | Tính toán hàm mất mát, thống kê chuẩn hóa hàng loạt |
| RK4 / bộ giải thích ứng | Mô phỏng hệ động lực, huấn luyện mạng chuyên sâu liên tục |
---

## Bản tóm tắt
| Chủ đề | Ý tưởng cốt lõi | Phương pháp chính |
|-------|-------------|-------------|
| Dấu phẩy động | Biểu diễn độ chính xác hữu hạn | IEEE 754, tổng kết Kahan |
| Tìm gốc | Giải f(x) = 0 | Phân chia, Newton-Raphson, Brent |
| Tích phân số | Xấp xỉ ∫f(x)dx | Hình thang, Simpson, cầu phương Gaussian |
| Nội suy | Ước tính giữa các điểm dữ liệu | Đường trục khối, Lagrange, RBF |
| Bộ giải ODE | Giải dy/dt = f(t,y) | Euler, RK4, phương pháp thích ứng |
| Tính ổn định | Nhạy cảm với lỗi làm tròn | Số điều kiện, thuật toán ổn định |
Phương pháp số là nơi toán học gặp thực tế. Không có máy tính nào có thể biểu diễn chính xác hầu hết các số thực, không có đạo hàm nào được tính toán một cách tượng trưng trong thực tế và không có tích phân nào được tính ở dạng đóng cho các bài toán trong thế giới thực. Hiểu các phương pháp số cho phép bạn chọn thuật toán phù hợp, dự đoán độ chính xác của nó và tránh các lỗi tinh vi phát sinh từ số học có độ chính xác hữu hạn.