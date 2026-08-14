---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Quá trình ngẫu nhiên
**Quá trình ngẫu nhiên** là tập hợp các biến ngẫu nhiên được lập chỉ mục theo thời gian (hoặc không gian). Trong khi lý thuyết xác suất nghiên cứu các sự kiện ngẫu nhiên riêng lẻ thì các quá trình ngẫu nhiên nghiên cứu tính ngẫu nhiên phát triển như thế nào theo thời gian. Họ lập mô hình giá cổ phiếu, độ dài hàng đợi, sự lây lan của bệnh tật, tạo ra ngôn ngữ và động lực đào tạo của các mô hình học máy.
---

## Nền tảng
### Sự định nghĩa
Quá trình ngẫu nhiên {X_t : t ∈ T} là một họ các biến ngẫu nhiên được xác định trên một không gian xác suất chung. T là **bộ chỉ mục** (thời gian):
- **Thời gian rời rạc:** T = {0, 1, 2, ...}
- **Thời gian liên tục:** T = [0, ∞)
**Không gian trạng thái** S là tập hợp các giá trị có thể X_t có thể nhận.
### Thuộc tính chính
| Bất động sản | Định nghĩa |
|----------|-------------|
| **Tính cố định** | Phân bố chung của (X_{t₁}, ..., X_{tₖ}) giống như (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Độc lập** | X_t độc lập với X_s với t ≠ s |
| **Tính linh hoạt** | Trung bình thời gian hội tụ về trung bình tổng thể |
| **Tài sản Markov** | Tương lai chỉ phụ thuộc vào hiện tại, không phụ thuộc vào quá khứ |
| **Martingale** | Giá trị kỳ vọng trong tương lai bằng giá trị hiện tại |
---

## Xích Markov
**Chuỗi Markov** là một quá trình ngẫu nhiên trong đó trạng thái tương lai chỉ phụ thuộc vào trạng thái hiện tại (thuộc tính không có bộ nhớ).
### Chuỗi Markov thời gian rời rạc (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
**Ma trận chuyển tiếp** P có các mục p_{ij} = P(đi tới j | hiện tại tại i).
| Bất động sản | Tuyên bố |
|----------|----------|
| Tổng hàng | Mỗi hàng có tổng bằng 1: Σⱼ p_{ij} = 1 |
| chuyển tiếp n bước | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Phân phối cố định | πP = π (vector riêng bên trái có giá trị riêng 1) |
### Phân loại các bang
| Kỳ hạn | Định nghĩa |
|------|-------------|
| **Tái phát** | Chuỗi trở về trạng thái i với xác suất 1 |
| **Tạm thời** | Xác suất không bao giờ quay trở lại khác 0 |
| **Hấp thụ** | p_{ii} = 1 (đã nhập, không bao giờ rời) |
| **Thời gian** | GCD của thời gian trở về; kỳ 1 = không định kỳ |
| **Giao tiếp** | Trạng thái i và j có thể đến được với nhau |
### Phân phối cố định
Đối với chuỗi Markov hồi quy dương, bất khả quy, phân phối dừng π tồn tại, là duy nhất và thỏa mãn:
πP = π, Σᵢ πᵢ = 1
**Giải thích:** πᵢ = tỷ lệ thời gian dài hạn dành cho trạng thái i.
**Ví dụ đã hoạt động:** Mô hình thời tiết với các trạng thái {Nắng, Mưa}.
P = [[0,9, 0,1], [0,5, 0,5]] (hàng: từ Nắng, từ Mưa)
Phân bố cố định: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Giải: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Hội tụ tới tính dừng
Đối với một chuỗi hồi quy dương, không tuần hoàn, bất khả quy:
- Pⁿ → Π (ma trận có tất cả các hàng bằng π) là n → ∞
- **Thời gian trộn:** Số bước cho đến khi phân phối gần bằng số π
- **Khoảng cách quang phổ:** 1 − |λ₂| (trong đó λ₂ là giá trị riêng lớn thứ hai) xác định tốc độ trộn
### Chuỗi Markov thời gian liên tục (CTMC)
Quá trình chuyển đổi xảy ra vào những thời điểm ngẫu nhiên được điều chỉnh bởi phân phối theo cấp số nhân.
| Khái niệm | Mô tả |
|----------|-------------|
| **Ma trận tỷ lệ Q** | q_{ij} ≥ 0 với i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Xác suất chuyển tiếp** | P(t) = e^{Qt} (ma trận hàm mũ) |
| **Phân phối cố định** | πQ = 0 |
| **Thời gian nắm giữ** | Thời gian ở trạng thái i là Exp(−q_{ii}) |
---

## Đi bộ ngẫu nhiên
**Bước đi ngẫu nhiên** là đường dẫn được hình thành bởi các bước ngẫu nhiên liên tiếp.
### Đi bộ ngẫu nhiên đơn giản
X_n = X_{n-1} + Z_n, trong đó Z_n ∈ {+1, −1} với xác suất p, q = 1−p.
| Bất động sản | p = 1/2 (đối xứng) | p ≠ 1/2 (thiên vị) |
|----------|----------------------|-------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Trở về nguồn gốc? | Có (với xác suất 1) | Không (trôi đi) |
| Tái phát? | Có (ở dạng 1D và 2D) | Không |
### Bước đi ngẫu nhiên ở các chiều không gian cao hơn
| Kích thước | Tái phát? | Trực giác |
|----------||-------------|----------|
| 1D | Có | “Người say luôn tìm đường về nhà” |
| 2D | Có | “Con chim say luôn tìm đường về nhà” |
| 3D+ | Không | “Chim sẻ say rượu không tìm được đường về nhà” |
### Kết nối với Chuyển động Brownian
Chia tỷ lệ bước đi ngẫu nhiên: đặt S_n = ΣZ_i. Sau đó, với kích thước bước → 0 và các bước → ∞:
S_{⌊nt⌋} / √n → B(t) (Chuyển động Brown, theo định lý Donsker)
---

## Chuyển động Brown
**Chuyển động Brown** (Quá trình Wiener) B(t) là giới hạn thời gian liên tục của một bước đi ngẫu nhiên.
### Sự định nghĩa
B(t) thỏa mãn:
1. B(0) = 0
2. B(t) có đường đi liên tục
3. Gia số độc lập: B(t) − B(s) độc lập với B(s) − B(r) với r < s < t
4. B(t) − B(s) ~ N(0, t − s) (Gia số Gaussian)
### Thuộc tính chính
| Bất động sản | Tuyên bố |
|----------|----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = phút(s, t) |
| Không nơi nào khác biệt được | Đường đi liên tục nhưng không có đạo hàm |
| Kích thước Fractal | Đồ thị có chiều Hausdorff 3/2 |
| Tài sản Markov | Tương lai chỉ phụ thuộc vào vị trí hiện tại |
| Martingale | E[B(t) | F_s] = B(s) cho s < t |
### Chuyển động Brown hình học
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Đây là mô hình chuẩn về giá cổ phiếu trong khuôn khổ Black-Scholes.
- μ: drift (lợi nhuận kỳ vọng)
- σ: độ biến động
---

## Quy trình Poisson
A **Quy trình Poisson** N(t) đếm số sự kiện xảy ra trong [0, t].
### Sự định nghĩa
N(t) ~ Poisson(λt), trong đó λ là tốc độ (sự kiện trên một đơn vị thời gian).
| Bất động sản | Tuyên bố |
|----------|----------|
| N(0) = 0 | — |
| Gia tăng độc lập | Các sự kiện trong các khoảng thời gian rời nhau là độc lập |
| Gia tăng cố định | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Thời gian giữa các chuyến đi | Phân phối theo cấp số nhân: T_i ~ Exp(λ) |
### Khái quát hóa
| Biến thể | Mô tả |
|----------|-------------|
| **Không đồng nhất** | Tốc độ λ(t) thay đổi theo thời gian |
| **Hợp chất Poisson** | Mỗi sự kiện có kích thước ngẫu nhiên: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Đo ngẫu nhiên Poisson** | Điểm trong không-thời gian, không chỉ thời gian |
| **Đa biến** | Nhiều loại sự kiện có thể tương tác |
---

## Martingales
**martingale** là một trò chơi công bằng: giá trị kỳ vọng trong tương lai, với tất cả thông tin hiện tại, bằng giá trị hiện tại.
### Sự định nghĩa
{X_n} là một martingale đối với việc lọc {F_n} nếu:
1. X_n là F_n có thể đo lường được (đã điều chỉnh)
2. E[|X_n|] < ∞ (có thể tích hợp)
3. E[X_{n+1} | F_n] = X_n (trò chơi công bằng)
| Biến thể | Tình trạng | Giải thích |
|----------|--------------------------|-------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Trò chơi công bằng |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Trò chơi thuận lợi (có xu hướng tăng) |
| **Siêu thị** | E[X_{n+1} | F_n] ≤ X_n | Trò chơi không thuận lợi (có xu hướng giảm) |
### Định lý chính
| Định lý | Tuyên bố |
|----------|----------|
| **Dừng tùy chọn** | Trong điều kiện, E[X_T] = E[X_0] trong thời gian dừng T |
| **Hội tụ** | Một martingale bị chặn gần như chắc chắn hội tụ |
| **Bất bình đẳng tối đa** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |
---

## Phương pháp Monte Carlo
**Phương pháp Monte Carlo** sử dụng mẫu ngẫu nhiên để ước tính số lượng xác định.
### Ý tưởng cơ bản
Để ước tính E[f(X)] trong đó X ~ P:
1. Vẽ N mẫu: x₁, x₂, ..., x_N từ P
2. Tính: Î = (1/N) Σᵢ f(xᵢ)
3. Theo định luật số lớn: Î → E[f(X)] là N → ∞
**Lỗi:** Sai số chuẩn = σ_f / √N, trong đó σ_f² = Var[f(X)]
### Kỹ thuật giảm phương sai
| Kỹ thuật | Ý tưởng | Tăng tốc |
|----------|------|----------|
| **Lấy mẫu quan trọng** | Mẫu từ Q thay vì P, trọng số theo P/Q | Có thể kịch tính |
| **Các biến thể phản đề** | Sử dụng cặp (x, −x) để hủy phương sai | ~2x |
| **Kiểm soát các biến thể** | Trừ hàm kỳ vọng đã biết tương quan với f | Khác nhau |
| **Lấy mẫu phân tầng** | Chia miền, lấy mẫu từng tầng | Giảm phương sai |
| **Rao-Blackwell** | Điều kiện về số liệu thống kê đầy đủ | Luôn giúp đỡ |
---

## Chuỗi Markov Monte Carlo (MCMC)
MCMC xây dựng chuỗi Markov có phân phối cố định là phân phối mục tiêu. Sau khoảng thời gian "đốt cháy", các mẫu sẽ lấy gần đúng từ mục tiêu.
### Thuật toán Metropolis-Hastings
| Bước | Hành động |
|------|--------|
| 1 | Trạng thái hiện tại: x_t |
| 2 | Đề xuất: x* ~ q(x* \| x_t) (phân phối đề xuất) |
| 3 | Tỷ lệ chấp nhận: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Chấp nhận với xác suất α: x_{t+1} = x* (chấp nhận) hoặc x_t (từ chối) |
**Trường hợp đặc biệt — Thuật toán Metropolis:** Đề xuất đối xứng q(x*|x) = q(x|x*), do đó α = min(1, π(x*)/π(x_t)).
### Lấy mẫu Gibbs
Một trường hợp đặc biệt của Metropolis-Hastings trong đó mỗi biến được cập nhật từ phân phối có điều kiện đầy đủ của nó.
Đối với mục tiêu π(x₁, x₂, ..., xₖ):
1. Mẫu x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Mẫu x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Tiếp tục cho tất cả các biến
4. Lặp lại
| Bất động sản | Tuyên bố |
|----------|----------|
| Luôn chấp nhận | α = 1 (không có bước bác bỏ) |
| Yêu cầu | Khả năng lấy mẫu từ mỗi điều kiện đầy đủ |
| Hội tụ | Được đảm bảo cho chuỗi không tuần hoàn, bất khả quy |
### Chẩn đoán MCMC
| Chẩn đoán | Mục đích |
|----------||----------|
| **Âm mưu theo dõi** | Kiểm tra trực quan để trộn và ổn định |
| **Tự tương quan** | Đo sự phụ thuộc mẫu (muốn tự tương quan thấp) |
| **Gelman-Rubin (R̂)** | So sánh nhiều chuỗi; R̂ < 1,05 gợi ý sự hội tụ |
| **Cỡ mẫu hiệu quả** | N_eff = N / (1 + 2Σρₖ); tài khoản cho tự tương quan |
| **Đốt cháy** | Loại bỏ các mẫu ban đầu trước khi dây chuyền đạt đến trạng thái dừng |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Quá trình ngẫu nhiên | Ứng dụng |
|-------------------|-------------|
| Chuỗi Markov | PageRank (đi bộ ngẫu nhiên trên biểu đồ web), tạo văn bản (mô hình n-gram), MCMC |
| Đi bộ ngẫu nhiên | Node2Vec và DeepWalk (nhúng biểu đồ), khám phá trong RL |
| Chuyển động Brown | Mô hình giá cổ phiếu, mô hình phổ biến trong AI sáng tạo |
| Quá trình Poisson | Lập mô hình các sự kiện đến (lần nhấp, lỗi), lý thuyết xếp hàng |
| Martingales | Toán tài chính, chứng minh sự hội tụ của SGD (xấp xỉ ngẫu nhiên) |
| Monte Carlo | Ước tính giá trị kỳ vọng, suy luận Bayes, học tăng cường (đánh giá chính sách) |
| MCMC (Thủ đô-Hastings) | Lấy mẫu sau Bayesian, lập trình xác suất (Stan, PyMC) |
| Lấy mẫu Gibbs | Mô hình chủ đề (LDA), mạng Bayes, khử nhiễu hình ảnh |
| Chẩn đoán MCMC | Đảm bảo suy luận đáng tin cậy từ các mô hình xác suất |
---

## Bản tóm tắt
| Quy trình | Không gian Nhà nước | Thời gian | Thuộc tính chính |
|----------|-------------|------|--------------|
| Chuỗi Markov | Rời rạc/liên tục | Rời rạc/liên tục | Không có bộ nhớ (thuộc tính Markov) |
| Đi bộ ngẫu nhiên | ℤᵈ | Rời Rạc | Tổng của i.i.d. bước |
| Chuyển động Brown | ℝ | Liên tục | Gia số Gaussian, đường dẫn liên tục |
| Quá trình Poisson | ℕ | Liên tục | Quá trình đếm với khoảng cách hàm mũ |
| Martingale | ℝ | Rời rạc/liên tục | Trò chơi công bằng (E[X_{t+1}|F_t] = X_t) |
Các quá trình ngẫu nhiên là toán học về tính ngẫu nhiên theo thời gian. Chúng củng cố suy luận Bayesian hiện đại (MCMC), học tăng cường (quy trình ra quyết định Markov), mô hình tổng quát (mô hình khuếch tán), toán tài chính và lý thuyết xếp hàng. Việc hiểu các quy trình này sẽ cung cấp cho bạn các công cụ để mô hình hóa sự không chắc chắn một cách linh hoạt — không chỉ như một ảnh chụp nhanh mà còn khi nó phát triển.