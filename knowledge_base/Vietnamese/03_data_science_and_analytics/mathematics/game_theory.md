---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#Lý thuyết trò chơi
Lý thuyết trò chơi là toán học của sự tương tác chiến lược - những tình huống mà kết quả của bạn không chỉ phụ thuộc vào lựa chọn của chính bạn mà còn phụ thuộc vào lựa chọn của người khác. Từ cuộc chiến giá cả giữa các công ty đến cuộc chạy đua vũ khí hạt nhân, từ đấu giá trực tuyến đến sinh học tiến hóa, lý thuyết trò chơi cung cấp các công cụ để phân tích xung đột và hợp tác. Nó ngày càng trở nên phù hợp với học máy thông qua học tăng cường đa tác nhân, mạng đối thủ tổng quát (GAN) và thiết kế cơ chế cho các nền tảng trực tuyến.
---

## Trò chơi dạng chiến lược
### Sự định nghĩa
**Trò chơi dạng chiến lược (dạng bình thường)** bao gồm:
- Tập hợp người chơi N = {1, 2, ..., n}
- Bộ chiến lược S₁, S₂, ..., Sₙ cho mỗi người chơi
- Hàm hoàn trả u₁, u₂, ..., uₙ ánh xạ hồ sơ chiến lược sang số thực
### Ví dụ: Thế tiến thoái lưỡng nan của tù nhân
| | Hợp tác (C) | Khiếm khuyết (D) |
|---|--------------||-------------|
| **Hợp tác (C)** | (−1, −1) | (−3, 0) |
| **Khiếm khuyết (D)** | (0, −3) | (−2, −2) |
| Phân tích | Kết quả |
|----------|--------|
| Chiến lược chiếm ưu thế | Khiếm khuyết (D chiếm ưu thế C cho cả hai người chơi) |
| Cân bằng Nash | (D, D) với mức hoàn trả (−2, −2) |
| Tối ưu xã hội | (C, C) với mức hoàn trả (−1, −1) |
| Vấn đề nan giải | Sự hợp lý cá nhân dẫn đến sự phi lý tập thể |
### Thêm trò chơi cổ điển
**Trận chiến giới tính:**
| | Opera | Bóng đá |
|---|-------|----------|
| Opera | (2, 1) | (0, 0) |
| Bóng đá | (0, 0) | (1, 2) |
Hai điểm cân bằng Nash: (Opera, Opera) và (Bóng đá, Bóng đá).
**Gà (Hawk-Dove):**
| | Diều hâu | Bồ câu |
|---|------|------|
| Diều hâu | (−10, −10) | (5, 0) |
| Bồ câu | (0, 5) | (1, 1) |
Hai điểm cân bằng Nash: (Hawk, Dove) và (Dove, Hawk).
---

## Chiến lược chiếm ưu thế
| Khái niệm | Định nghĩa |
|----------|-------------|
| **Chi phối nghiêm ngặt** | Chiến lược sᵢ mang lại lợi nhuận cao hơn bất kỳ chiến lược nào khác, bất kể lựa chọn của đối thủ |
| **Ưu thế yếu** | Chiến lược sᵢ ít nhất mang lại lợi nhuận cao như bất kỳ chiến lược nào khác và cao hơn hoàn toàn đối với một số hồ sơ đối thủ |
| **Chiến lược thống trị** | Một chiến lược không bao giờ là phản ứng tốt nhất |
**Loại bỏ lặp đi lặp lại các chiến lược thống trị:**
1. Loại bỏ mọi chiến lược bị thống trị nghiêm ngặt
2. Lặp lại cho đến khi không thể gỡ bỏ được nữa
3. Nếu vẫn còn một hồ sơ chiến lược thì đó là trạng thái cân bằng Nash duy nhất
---

## Cân bằng Nash
**Cân bằng Nash** là một hồ sơ chiến lược trong đó không người chơi nào có thể cải thiện mức thu nhập của mình bằng cách đơn phương thay đổi chiến lược của họ.
### Sự định nghĩa
(s₁*, s₂*, ..., sₙ*) là điểm cân bằng Nash nếu với mọi người chơi i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) với mọi sᵢ ∈ Sᵢ
### Tìm điểm cân bằng Nash (Trò chơi 2×2)
**Phương pháp phản hồi tốt nhất:**
1. Ở mỗi cột, hãy gạch chân câu trả lời đúng nhất của người chơi 1
2. Với mỗi hàng, hãy gạch dưới câu trả lời hay nhất của người chơi 2
3. Các ô đều được gạch chân là cân bằng Nash
### Tồn tại (Định lý Nash)
Mọi trò chơi hữu hạn đều có ít nhất một điểm cân bằng Nash (có thể trong các chiến lược hỗn hợp).
### Chiến lược hỗn hợp
**Chiến lược hỗn hợp** là sự phân bổ xác suất trên các chiến lược thuần túy.
| Khái niệm | Định nghĩa |
|----------|-------------|
| Chiến lược hỗn hợp σᵢ | Phân bố xác suất trên Sᵢ |
| Chiến lược hỗn hợp NE | Không người chơi nào có thể cải thiện mức chi trả dự kiến ​​bằng cách thay đổi cách kết hợp của mình |
| Hỗ trợ | Tập hợp các chiến lược thuần túy được chơi với xác suất dương |
**Ví dụ đã thực hiện: Đồng xu phù hợp**
| | Thủ trưởng | Đuôi |
|---|-------|-------|
| Thủ trưởng | (1, −1) | (−1, 1) |
| Đuôi | (−1, 1) | (1, −1) |
Không có chiến lược thuần túy NE. NE hỗn hợp: cả hai đều chơi H và T với xác suất mỗi bên là ½.
---

## Định lý Minimax
### Trò chơi có tổng bằng 0
Trong **trò chơi có tổng bằng 0**, phần thắng của một người chơi chính xác là phần thua của người kia: u₁ + u₂ = 0.
### Định lý Minimax của Von Neumann
Đối với mọi trò chơi có tổng bằng 0 hữu hạn hai người chơi:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
**maximin** (trường hợp xấu nhất tốt nhất cho người chơi 1) bằng **minimax** (trường hợp xấu nhất tốt nhất cho người chơi 2). Giá trị chung này là **giá trị của trò chơi**.
### Giải trò chơi có tổng bằng 0
Đối với trò chơi có tổng bằng 0 2×2 có ma trận:
| | L | R |
|---|---|---|
| T | một | b |
| B | c | d |
Chiến lược hỗn hợp tối ưu của Người chơi 1: chơi T với xác suất p = (d−c)/((a−b)+(d−c))
Giá trị trò chơi: v = (ad−bc)/((a−b)+(d−c))
---

## Trò chơi dạng mở rộng
Các trò chơi có bước di chuyển tuần tự được thể hiện dưới dạng **cây trò chơi**.
### Các khái niệm chính
| Khái niệm | Định nghĩa |
|----------|-------------|
| **Cây trò chơi** | Cây hiển thị tất cả các chuỗi di chuyển có thể xảy ra |
| **Bộ thông tin** | Tập hợp các nút mà người chơi không thể phân biệt |
| **Thông tin hoàn hảo** | Mọi tập hợp thông tin đều là một tập hợp đơn lẻ (tất cả các bước di chuyển đều có thể quan sát được) |
| **Trò chơi phụ hoàn hảo NE** | Cân bằng Nash trong mọi trò chơi con |
| **Cảm ứng ngược** | Giải từ cuối cây ngược lại |
### Định lý Zermelo
Trong các trò chơi hữu hạn, thông tin hoàn hảo, hai người chơi không có cơ hội: một trong hai người chơi có chiến lược chiến thắng hoặc cả hai có thể buộc phải hòa (ví dụ: cờ vua).
---

## Trò chơi hợp tác
Trong **trò chơi hợp tác**, người chơi có thể hình thành các thỏa thuận và liên minh ràng buộc.
### Chức năng đặc trưng
Trò chơi hợp tác được xác định bởi **hàm đặc trưng** v: 2^N → ℝ, trong đó v(S) là giá trị mà liên minh S có thể đạt được.
| Bất động sản | Định nghĩa |
|----------|-------------|
| **Siêu phụ gia** | v(S ∪ T) ≥ v(S) + v(T) đối với S, T rời nhau |
| **Lồi** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) với S ⊂ T |
### Cốt lõi
**Cốt lõi** là tập hợp các phân bổ mà không liên minh nào có thể cải thiện bằng cách tách rời:
Core = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) với mọi S ⊂ N}
Lõi có thể trống - trong trường hợp đó không tồn tại sự phân bổ ổn định.
### Giá trị Shapley
**Giá trị Shapley** cung cấp sự phân bổ công bằng duy nhất dựa trên đóng góp cận biên:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Bất động sản | Tuyên bố |
|----------|----------|
| Hiệu quả | Σ φᵢ = v(N) (tất cả giá trị được phân phối) |
| Đối xứng | Những người đóng góp ngang nhau nhận được phần thưởng như nhau |
| Người chơi giả | Những người không đóng góp không nhận được |
| Phụ gia | φ(v + w) = φ(v) + φ(w) |
**Giải thích:** Giá trị Shapley của mỗi người chơi là mức đóng góp cận biên trung bình của họ trên tất cả các thứ tự có thể có của việc hình thành liên minh.
### Ví dụ đã hoạt động
Ba người chơi: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Người chơi | Đóng góp cận biên (trung bình trên số đơn đặt hàng) | Giá trị Shapley |
|--------|----------------------------------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27,5 |
| 3 | (100+70+60+70+60+0)/6 | 35,0 |
(Được tính toán chính xác bằng công thức Shapley cho mỗi hoán vị.)
---

## Thiết kế cơ chế
**Thiết kế cơ chế** là "lý thuyết trò chơi nghịch đảo" — thay vì phân tích các trò chơi nhất định, hãy thiết kế các trò chơi tạo ra kết quả mong muốn.
### Nguyên tắc Mặc khải
Bất kỳ cơ chế nào đạt được kết quả mong muốn đều có thể được thay thế bằng **cơ chế tiết lộ trực tiếp** trong đó việc nói sự thật là trạng thái cân bằng Nash.
### Lý thuyết đấu giá
| Loại đấu giá | Nội quy | Doanh thu tương đương |
|-------------|-------|----------------------|
| **Bán kín giá đầu tiên** | Người trả giá cao nhất sẽ thắng, trả giá | Tất cả các phiên đấu giá tiêu chuẩn đều mang lại doanh thu dự kiến ​​như nhau |
| **Bán kín giá thứ hai (Vickrey)** | Người trả giá cao nhất thắng, trả giá thầu cao thứ hai | (theo giá trị riêng tư độc lập) |
| **Tiếng Anh (tăng dần)** | Giá tăng; đầu tiên chấp nhận chiến thắng | — |
| **Tiếng Hà Lan (giảm dần)** | Giá giảm; đầu tiên chấp nhận chiến thắng | — |
### Đấu giá Vickrey (Giá thứ hai)
**Chiến lược chiếm ưu thế:** Đặt giá thầu theo giá trị thực của bạn.
| Bất động sản | Tuyên bố |
|----------|----------|
| Đấu thầu trung thực | Chiến lược chiếm ưu thế yếu |
| Hiệu quả | Vật phẩm thuộc về người trả giá cao nhất |
| Doanh thu | Doanh thu dự kiến ​​tương tự như giá đầu tiên (Định lý tương đương doanh thu) |
### Thiết kế đấu giá tối ưu (Myerson)
Phiên đấu giá tối đa hóa doanh thu:
- Phân bổ cho người đặt giá thầu có **giá trị ảo** cao nhất
- Đặt giá khởi điểm
- Định giá ảo: ψ(v) = v − (1−F(v))/f(v)
---

## Kết nối với Machine Learning
### Mạng đối thủ sáng tạo (GAN)
GAN là trò chơi hai người chơi giữa người tạo G và người phân biệt đối xử D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Khái niệm lý thuyết trò chơi | Tương đương GAN |
|-------------------||-----------------|
| Trò chơi có tổng bằng 0 dành cho hai người chơi | Trình tạo và phân biệt đối xử |
| Cân bằng Nash | G tạo dữ liệu thực, D xuất ra ½ mọi nơi |
| Tối thiểu | Hàm mục tiêu GAN |
| Chế độ sụp đổ | Không đạt được trạng thái cân bằng |
### Học tăng cường đa tác nhân (MARL)
| Khái niệm | Ứng dụng MARL |
|----------|-------------------|
| Cân bằng Nash | Chính sách ổn định trong cài đặt đa tác nhân |
| Tối thiểu | Chính sách mạnh mẽ chống lại đối thủ |
| Trò chơi hợp tác | Thành lập liên minh, phân công nhiệm vụ |
| Giá trị Shapley | Chuyển nhượng tín dụng (đại lý nào đã đóng góp gì?) |
| Thiết kế cơ chế | Thiết kế ưu đãi trong hệ thống đa tác nhân |
| Vở kịch hư cấu | Thuật toán học hội tụ về trạng thái cân bằng Nash |
### Các kết nối ML khác
| Ứng dụng | Công cụ lý thuyết trò chơi |
|-------------|-----------------|
| Thiết kế đấu giá quảng cáo (Google, Facebook) | Thiết kế cơ chế, lý thuyết đấu giá |
| Thiết kế thị trường (Uber, Airbnb) | Lý thuyết so khớp, thiết kế cơ chế |
| Sự mạnh mẽ của đối thủ | Trò chơi có tổng bằng 0 giữa kẻ tấn công và người phòng thủ |
| Phân chia công bằng | Giá trị Shapley, phân bổ không gây ghen tị |
| Học tập liên kết | Lý thuyết trò chơi hợp tác để đo lường sự đóng góp |
| Hệ thống khuyến nghị | Thiết kế cơ chế khơi gợi sở thích trung thực |
---

## Bản tóm tắt
| Khái niệm | Ý tưởng cốt lõi | Kết quả then chốt |
|----------|-------------|-------------|
| Trò chơi chiến lược | Người chơi, chiến lược, phần thưởng | Biểu diễn ma trận trò chơi |
| Chiến lược chiếm ưu thế | Tốt nhất bất kể người khác | Loại bỏ lặp đi lặp lại |
| Cân bằng Nash | Không có sự sai lệch đơn phương có lợi nhuận | Tồn tại trong mọi trò chơi hữu hạn |
| Chiến lược hỗn hợp | Chọn ngẫu nhiên các hành động | Định lý tồn tại Nash |
| Tối thiểu | Trường hợp xấu nhất tốt nhất (tổng bằng 0) | Định lý cực tiểu của Von Neumann |
| Dạng mở rộng | Di chuyển tuần tự | Cảm ứng ngược, trò chơi phụ hoàn hảo |
| Trò chơi hợp tác | Liên minh ràng buộc | Giá trị cốt lõi, Shapley |
| Thiết kế cơ chế | Thiết kế trò chơi để đạt được kết quả | Nguyên tắc khai sáng, đấu giá tối ưu |
| Lý thuyết đấu giá | Bán hàng thông qua cạnh tranh | Doanh thu tương đương, đấu giá Vickrey |
Lý thuyết trò chơi là toán học của tư duy chiến lược. Trong một thế giới ngày càng đông dân bởi các tác nhân AI tương tác, thị trường tự động và hệ thống đối thủ, lý thuyết trò chơi cung cấp bộ công cụ thiết yếu để dự đoán hành vi, thiết kế cơ chế và xây dựng hệ thống đa tác nhân mạnh mẽ. Đối với các nhà khoa học dữ liệu, nó giải thích cách GAN hoạt động, cách đấu giá trực tuyến tạo ra hàng tỷ doanh thu và cách xây dựng hệ thống AI hoạt động tốt trong môi trường cạnh tranh.