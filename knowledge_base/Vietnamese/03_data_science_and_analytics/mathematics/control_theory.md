---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Lý thuyết điều khiển
Lý thuyết điều khiển là toán học làm cho hệ thống hoạt động theo cách bạn muốn. Từ máy điều nhiệt đến máy lái tự động, từ cánh tay robot đến lò phản ứng hóa học, hệ thống điều khiển cảm nhận, quyết định và hành động để duy trì hành vi mong muốn. Lĩnh vực này cung cấp các công cụ nghiêm ngặt để phân tích độ ổn định, hiệu suất và độ bền — các khái niệm đã được chuyển sang học tăng cường, điều chỉnh siêu tham số và hệ thống thích ứng.
---

## Khái niệm cơ bản
### Vòng lặp mở và Vòng lặp kín
| Loại | Mô tả | Ví dụ | Lợi thế |
|------|-------------|----------|----------|
| **Vòng lặp mở** | Hành động điều khiển độc lập với đầu ra | Hẹn giờ máy giặt | Đơn giản, không cần cảm biến |
| **Vòng kín (phản hồi)** | Hành động điều khiển phụ thuộc vào đầu ra | Bộ điều nhiệt, kiểm soát hành trình | Loại bỏ nhiễu loạn, mạnh mẽ |
### Các phần tử sơ đồ khối
| Yếu tố | Biểu tượng | Chức năng |
|----------|--------|----------|
| **Thực vật** | G (các) | Hệ thống đang được điều khiển |
| **Bộ điều khiển** | C (các) | Tính toán hành động điều khiển |
| **Cảm biến** | H (các) | Đo đầu ra |
| **Ngã ba tổng hợp** | ⊕ | Lỗi tính toán: r − y |
| **Tham khảo** | r(t) | Đầu ra mong muốn |
| **Lỗi** | e(t) = r(t) − y(t) | Sự khác biệt giữa mong muốn và thực tế |
| **Rối loạn** | d(t) | Đầu vào không mong muốn ảnh hưởng đến nhà máy |
### Chức năng truyền vòng kín
Đối với hệ thống phản hồi tiêu cực tiêu chuẩn:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Số lượng | Công thức |
|----------|----------|
| Hàm truyền vòng hở | L(s) = C(s)G(s)H(s) |
| Hàm truyền vòng kín | T(s) = L(s)/H(s) / (1 + L(s)) |
| Chức năng chuyển lỗi | E(s)/R(s) = 1 / (1 + L(s)) |
| Độ nhạy | S(s) = 1 / (1 + L(s)) |
---

##Chức năng chuyển giao
**Hàm truyền** H(s) = Y(s)/X(s) mô tả mối quan hệ đầu vào-đầu ra của hệ thống tuyến tính bất biến theo thời gian (LTI) trong miền Laplace.
### Mẫu chuẩn
| Hệ thống | Chức năng chuyển giao | Thông số |
|--------|-------------------|-------------|
| **Đơn hàng đầu tiên** | K/(τs + 1) | K = độ lợi, τ = hằng số thời gian |
| **Bậc hai** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = tần số riêng, ζ = hệ số giảm chấn |
| **Nhà tích hợp** | K/s | — |
| **Sự khác biệt** | Ks | — |
| **Trì hoãn** | e^{−sT_d} | T_d = độ trễ thời gian |
### Hành vi của hệ thống bậc hai
| Hệ số giảm chấn ζ | Hành vi | Địa điểm cực |
|--------|----------|---------------|
| ζ = 0 | Dao động không suy giảm | Tưởng tượng thuần túy |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Quá tải (chậm, không dao động) | Thực tế, khác biệt |
### Số liệu hiệu suất (Phản hồi theo bước)
| Số liệu | Công thức (bậc 2, giảm chấn) | Mô tả |
|--------|-----------------------------------|-------------|
| Thời gian tăng (t_r) | ≈ 1,8/ωₙ | Thời gian tăng từ 10% lên 90% |
| Giờ cao điểm (t_p) | π/(ωₙ√(1−ζ²)) | Thời gian đạt mức tối đa đầu tiên |
| Vượt mức (M_p) | e^{−πζ/√(1−ζ²)} × 100% | Đỉnh tối đa trên giá trị cuối cùng |
| Thời gian lắng (t_s) | ≈ 4/(ζωₙ) | Thời gian ở lại trong vòng 2% cuối cùng |
| Lỗi trạng thái ổn định | Phụ thuộc vào loại hệ thống | Sự khác biệt giữa mong muốn và thực tế khi t → ∞ |
---

## Bộ điều khiển PID
**Bộ điều khiển PID** là bộ điều khiển được sử dụng rộng rãi nhất trong công nghiệp (trên 90% bộ điều khiển công nghiệp).
### Công thức PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Trong miền Laplace: C(s) = K_p + K_i/s + K_d s
| Kỳ hạn | Hiệu ứng | Quá nhiều | Quá Ít |
|------|--------|----------|----------|
| **Tỷ lệ (K_p)** | Phản ứng với lỗi hiện tại | Dao động, mất ổn định | Phản hồi chậm, lỗi lớn |
| **Tích phân (K_i)** | Loại bỏ lỗi trạng thái ổn định | Vượt quá, dao động | Bù đắp liên tục |
| **Đạo hàm (K_d)** | Dự đoán lỗi trong tương lai (giảm xóc) | Khuếch đại tiếng ồn | Từ chối nhiễu kém |
### Phương pháp điều chỉnh PID
| Phương pháp | Tiếp cận |
|--------|----------|
| **Ziegler-Nichols** | Tăng K_u cho đến khi dao động; sử dụng K_u và kỳ P_u để đặt mức tăng |
| **Cohen-Coon** | Dựa trên các thông số phản hồi từng bước (độ lợi, hằng số thời gian, thời gian chết) |
| **IMC (Kiểm soát mô hình nội bộ)** | Dựa trên mô hình quy trình; cung cấp độ bền tốt |
| **Tự động điều chỉnh** | Nhận dạng + điều chỉnh trực tuyến (nhiều bộ điều khiển hiện đại) |
| **Hướng dẫn sử dụng** | Chỉ bắt đầu với K_p, thêm K_i để loại bỏ offset, thêm K_d để giảm chấn |
### Quy tắc Ziegler-Nichols
1. Đặt K_i = K_d = 0
2. Tăng K_p cho đến khi dao động duy trì: mức tăng cuối cùng K_u, chu kỳ P_u
3. Đặt mức tăng:
| Bộ điều khiển | K_p | K_i | K_d |
|----------||------|------|------|
| P | 0,5K_u | — | — |
| PI | 0,45K_u | 1,2K_u/P_u | — |
| PID | 0,6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Phân tích độ ổn định
Một hệ thống **ổn định** nếu đầu ra của nó vẫn bị giới hạn đối với các đầu vào bị chặn (độ ổn định BIBO).
### Ổn định dựa trên cực
| Tình trạng | Tính ổn định |
|----------||----------|
| Tất cả các cực trong nửa mặt phẳng bên trái (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Không ổn định |
| Các cực trên trục ảo (Re(s) = 0) | Ổn định một chút (hoặc không ổn định khi lặp lại) |
### Tiêu chí Routh-Hurwitz
Xác định độ ổn định mà không cần tính toán cực một cách rõ ràng. Xây dựng mảng Routh từ các hệ số đa thức đặc trưng.
**Quy tắc:** Số lần đổi dấu ở cột đầu tiên bằng số cực của nửa mặt phẳng phải.
### Tiêu chí ổn định Nyquist
Vẽ biểu đồ đáp ứng tần số vòng hở L(jω) trong mặt phẳng phức.
**Quy tắc:** Hệ thống vòng kín ổn định nếu đồ thị Nyquist bao quanh điểm (−1, 0) ngược chiều kim đồng hồ một số lần bằng số cực không ổn định của vòng lặp mở.
**Biên độ tăng:** Mức tăng có thể tăng bao nhiêu trước khi không ổn định (khoảng cách từ đồ thị đến −1 trên trục thực).
**Biên pha:** Độ trễ pha có thể tăng bao nhiêu trước khi mất ổn định (góc từ biểu đồ đến vòng tròn đơn vị khi giao nhau khuếch đại).
### Phân tích đồ thị Bode
Biểu đồ mức tăng (dB) và pha (độ) so với tần số (thang log).
| Số liệu | Định nghĩa | Giá trị mong muốn |
|--------|----------|---------------|
| **Lợi nhuận tăng (GM)** | Tăng mức tăng để đạt 0 dB tại pha = −180° | > 6dB |
| **Lề pha (PM)** | Pha ở mức tăng chéo (0 dB) + 180° | > 45° |
| **Tăng chéo** | Tần số có mức tăng = 0 dB | — |
| **Chuyển pha** | Tần số trong đó pha = −180° | — |
---

## Đại diện không gian trạng thái
Đối với các hệ thống nhiều đầu vào, nhiều đầu ra (MIMO), dạng không gian trạng thái tự nhiên hơn các hàm truyền.
###Mẫu chuẩn
ẋ(t) = Ax(t) + Bu(t) (phương trình trạng thái)
y(t) = Cx(t) + Du(t) (phương trình đầu ra)
| Ma trận | Tên | Kích thước |
|--------|------|----------|
| A | Ma trận hệ thống/trạng thái | n × n |
| B | Ma trận đầu vào | n × m |
| C | Ma trận đầu ra | p × n |
| D | Ma trận tiếp liệu | p×m |
### Hàm truyền từ không gian trạng thái
G(s) = C(sI − A)⁻¹B + D
### Khả năng kiểm soát và khả năng quan sát
| Bất động sản | Kiểm tra | Ý nghĩa |
|----------|------|----------|
| **Có thể kiểm soát** | Hạng[C_B] = n (trong đó C_B = [B, AB, A²B, ...]) | Có thể lái đến bất kỳ trạng thái nào |
| **Có thể quan sát** | Xếp hạng[O_B] = n (trong đó O_B = [C; CA; CA²; ...]) | Có thể xác định trạng thái từ đầu ra |
Một hệ thống phải có khả năng điều khiển được để có thể ổn định bằng phản hồi và có thể quan sát được để ước tính trạng thái.
### Phản hồi của Tiểu bang
u = −Kx + r (phản hồi trạng thái đầy đủ)
Vòng kín: ẋ = (A − BK)x + Br
**Vị trí cực:** Chọn K sao cho A − BK có giá trị riêng (cực) mong muốn.
---

## Kiểm soát tối ưu
### Bộ điều chỉnh bậc hai tuyến tính (LQR)
Giảm thiểu: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
trong đó Q ≥ 0 (chi phí trạng thái) và R > 0 (chi phí kiểm soát).
**Giải pháp:** u = −Kx trong đó K = R⁻¹BᵀP và P giải được **phương trình Riccati đại số:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Điều chỉnh | Hiệu ứng |
|--------|--------|
| Tăng Q | Phản ứng nhanh hơn, nỗ lực kiểm soát nhiều hơn |
| Tăng R | Phản ứng chậm hơn, nỗ lực kiểm soát ít hơn |
| Q ≫ R | Kiểm soát tích cực (như K_p cao) |
### Bộ lọc Kalman
Công cụ ước tính trạng thái tối ưu cho các hệ thống tuyến tính có nhiễu Gaussian.
**Mô hình hệ thống:**
ẋ = Ax + Bu + w (nhiễu xử lý w ~ N(0, Q))
y = Cx + v (nhiễu đo v ~ N(0, R))
**Phương trình lọc Kalman:**
- Dự đoán: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Cập nhật: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Bộ lọc Kalman là bộ lọc LQR kép - nó giảm thiểu phương sai lỗi ước tính.
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm lý thuyết điều khiển | Ứng dụng |
|----------------------|-------------|
| Kiểm soát phản hồi | Tỷ lệ học tập thích ứng, ổn định đào tạo |
| bộ điều khiển PID | Điều chỉnh siêu tham số, kiểm soát nhiệt độ trong trung tâm dữ liệu |
| Mô hình không gian trạng thái | Mô hình hóa chuỗi thời gian, mạng lưới thần kinh tái phát |
| Bộ lọc Kalman | Theo dõi, tổng hợp cảm biến, ước tính trạng thái, dự báo chuỗi thời gian |
| LQR / điều khiển tối ưu | Học tăng cường (điều khiển LQG), robot |
| Phân tích độ ổn định | Động lực huấn luyện của GAN, sự hội tụ của thuật toán RL |
| Khả năng kiểm soát/quan sát | Hiểu biểu thức RNN, nhận dạng hệ thống |
| Hàm chuyển giao | Hiểu CNN như bộ lọc tuyến tính, phân tích miền tần số |
| Nyquist/Bode | Phân tích độ bền cho hệ thống thích ứng |
| Vị trí cực | Thiết kế động lực học của các hệ thống đã học (ODE thần kinh) |
---

## Bản tóm tắt
| Khái niệm | Ý tưởng cốt lõi | Công cụ chính |
|----------|-------------|----------|
| Phản hồi | Sử dụng đầu ra để sửa đầu vào | Hàm truyền vòng kín |
| Hàm chuyển | Mối quan hệ đầu vào-đầu ra trong miền s | G(s) = Y(s)/X(s) |
| điều khiển PID | Tỷ lệ + Tích phân + Đạo hàm | Bộ điều khiển công nghiệp được sử dụng rộng rãi nhất |
| Tính ổn định | Đầu ra bị chặn cho đầu vào bị chặn | Routh-Hurwitz, Nyquist, Bode |
| Không gian trạng thái | Đại diện nội bộ nhà nước | ẋ = Ax + Bu, y = Cx + Du |
| Khả năng kiểm soát | Chúng ta có thể đạt đến bất kỳ trạng thái nào không? | Kiểm tra xếp hạng về ma trận khả năng kiểm soát |
| Khả năng quan sát | Chúng ta có thể suy ra trạng thái không? | Kiểm tra xếp hạng trên ma trận khả năng quan sát |
| LQR | Phản hồi trạng thái tối ưu | Phương trình Riccati |
| Bộ lọc Kalman | Ước tính trạng thái tối ưu | Chu kỳ cập nhật dự đoán |
Lý thuyết điều khiển là toán học giúp hệ thống thực hiện những gì bạn muốn — một cách đáng tin cậy, mạnh mẽ và hiệu quả. Các nguyên tắc phản hồi, ổn định và tối ưu của nó đã được chứng minh là phổ biến, xuất hiện trong các lĩnh vực từ robot đến học tập tăng cường, từ kinh tế đến sinh học. Đối với các nhà khoa học dữ liệu, lý thuyết điều khiển cung cấp ngôn ngữ để hiểu các hệ thống thích ứng, thiết kế các quy trình đào tạo ổn định và xây dựng các tác nhân thông minh tương tác với môi trường năng động.