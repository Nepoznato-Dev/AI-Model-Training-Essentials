---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
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

# Cơ học cổ điển
Cơ học cổ điển mô tả chuyển động của vật dưới tác dụng của lực. Từ những quả táo rơi đến các hành tinh quay quanh, từ các dây dao động đến các hạt va chạm, các nguyên lý của nó chi phối thế giới vĩ mô. Ngoài các ứng dụng vật lý, cơ học cổ điển đã khai sinh ra phép tính biến phân, hình học đối xứng và khuôn khổ Hamilton làm nền tảng cho cơ học lượng tử và tối ưu hóa hiện đại.
---

## Cơ học Newton
### Ba định luật Newton
| Luật | Tuyên bố | Dạng toán học |
|------|-------------|-------------------|
| **Đầu tiên (Quán tính)** | Một vật vẫn đứng yên hoặc chuyển động thẳng đều trừ khi bị tác dụng bởi một lực | Nếu F_net = 0 thì v = hằng số |
| **Giây (F = ma)** | Lực bằng khối lượng nhân với gia tốc | **F** = m**a** = m(d²**x**/dt²) |
| **Thứ ba (Hành động-Phản ứng)** | Mọi hành động đều có phản ứng bình đẳng và ngược chiều | **F**₁₂ = −**F**₂₁ |
### Sơ đồ cơ thể tự do
**Sơ đồ vật tự do** cô lập một vật thể và hiển thị tất cả các lực tác dụng lên nó.
**Lực lượng chung:**
| Lực lượng | Công thức | Hướng |
|-------|----------|----------|
| Trọng lực (gần Trái đất) | F = mg | Đi xuống |
| Lực bình thường | N | Vuông góc với bề mặt |
| Ma sát (tĩnh) | f_s ≤ μ_s N | Phản đối chuyển động sắp xảy ra |
| Ma sát (động học) | f_k = μ_k N | Phản đối chuyển động |
| Mùa xuân (định luật Hooke) | F = −kx | Khôi phục (hướng tới trạng thái cân bằng) |
| Căng thẳng | T | Dọc theo dây/dây |
| Kéo | F_d = ½C_d ρAv² | Vận tốc đối lập |
### Ví dụ hoạt động: Chặn trên đường nghiêng
Một vật có khối lượng m nằm trên mặt phẳng nghiêng không ma sát góc θ.
- Lực: trọng lực (mg hướng xuống), lực pháp tuyến (N vuông góc với bề mặt)
- Phân hủy trọng lực: mg sin θ (theo mặt nghiêng), mg cos θ (vào bề mặt)
- N = mg cos θ (không chuyển động vuông góc với bề mặt)
- Gia tốc dọc theo mặt nghiêng: a = g sin θ
---

## Phương pháp năng lượng
### Công và Động năng
**Công** được thực hiện bởi một lực: W = ∫ **F** · d**r**
**Định lý công-năng lượng:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Năng lượng tiềm năng
| Lực lượng | Năng lượng tiềm năng | Ghi chú |
|-------|--------------------------------|-------|
| Trọng lực (gần bề mặt) | U = mgh | h = chiều cao trên tham chiếu |
| Trọng lực (chung) | U = −GMm/r | Số không ở vô cực |
| Mùa xuân | U = ½kx² | x = độ dịch chuyển khỏi vị trí cân bằng |
| Tĩnh điện | U = kq₁q₂/r | Các điện tích giống nhau: dương U |
### Bảo tồn năng lượng
Nếu chỉ có lực bảo toàn tác dụng: E ​​= KE + PE = hằng số
½mv₁² + U₁ = ½mv₂² + U₂
**Ví dụ đã làm:** Một quả bóng rơi từ độ cao h.
- Ban đầu: KE = 0, PE = mgh
- Ngay trước khi chạm đất: KE = ½mv², PE = 0
- Bảo toàn: mgh = ½mv² → v = √(2gh)
### Quyền lực
P = dW/dt = **F** · **v** (tỷ lệ thực hiện công)
---

## Động lượng và va chạm
### Động lượng tuyến tính
**p** = m**v**
Định luật thứ hai của Newton (dạng thay thế): **F** = d**p**/dt
### Bảo toàn động lượng
Nếu không có ngoại lực: tổng động lượng được bảo toàn.
| Kiểu va chạm | KE được bảo tồn? | Động lượng được bảo toàn? |
|--------------|---------------|--------------------------|
| **Đàn hồi** | Có | Có |
| **Không co giãn** | Không | Có |
| **Không co giãn hoàn hảo** | Không (mất tối đa) | Có (các vật dính vào nhau) |
**Va chạm đàn hồi 1D:** Hai khối lượng m₁, m₂ với vận tốc ban đầu u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Động lượng góc
**L** = **r** × **p** = m(**r** × **v**)
Mô-men xoắn: **τ** = d**L**/dt = **r** × **F**
**Sự bảo toàn:** Nếu không có mô men xoắn ngoài thì động lượng góc được bảo toàn.
---

## Cơ học Lagrange
Công thức **Lagrangian** thay thế lực bằng năng lượng, mang đến một khuôn khổ tổng quát và thanh lịch hơn.
### Lagrangian
L = T − V (động năng trừ đi thế năng)
### Nguyên tắc hành động tối thiểu (Nguyên tắc Hamilton)
Đường đi thực tế mà một hệ thống đi giữa các thời điểm t₁ và t₂ giảm thiểu (chính xác hơn là làm cho nó đứng yên) **hành động**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Phương trình Euler-Lagrange
Điều kiện δS = 0 mang lại:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
với mỗi tọa độ tổng quát q.
**Ví dụ đã làm:** Con lắc đơn (chiều dài l, khối lượng m, góc θ so với phương thẳng đứng).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Ưu điểm của cơ học Lagrange
| Lợi thế | Giải thích |
|----------||-------------|
| Phối hợp độc lập | Hoạt động trong mọi hệ tọa độ |
| Xử lý các ràng buộc một cách tự nhiên | Không cần tính toán lực ràng buộc |
| Đối xứng → bảo toàn | Định lý Noether kết nối sự đối xứng với đại lượng bảo toàn |
| Khái quát hóa dễ dàng | Đến các lĩnh vực, thuyết tương đối, cơ học lượng tử |
---

## Cơ học Hamilton
Công thức **Hamiltonian** là sự phát triển lại của cơ học Lagrange sử dụng vị trí và mô men (thay vì vị trí và vận tốc).
### Người Hamilton
H = Σᵢ pᵢq̇ᵢ − L = T + V (đối với hầu hết các hệ thống cơ khí)
trong đó pᵢ = ∂L/∂q̇ᵢ là **động lượng tổng quát**.
### Phương trình Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Đây là 2n ODE bậc nhất (so với n phương trình Euler-Lagrange bậc hai).
**Ví dụ đã làm:** Bộ dao động điều hòa (khối lượng m, hằng số lò xo k).
- H = p2/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (như mong đợi)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (định luật Hooke)
### Dấu ngoặc Poisson
Đối với các hàm f(q, p) và g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Bất động sản | Tuyên bố |
|----------|----------|
| Sự tiến hóa theo thời gian | df/dt = {f, H} + ∂f/∂t |
| Bảo tồn | f được bảo toàn nếu {f, H} = 0 (và ∂f/∂t = 0) |
| Dấu ngoặc cơ bản | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Kết nối với cơ học lượng tử:** Dấu ngoặc Poisson trở thành cổ góp: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Định luật bảo toàn và Định lý Noether
### Định lý Noether
Mọi đối xứng liên tục của Lagrangian đều tương ứng với một đại lượng được bảo toàn.
| Đối xứng | Số lượng bảo tồn |
|----------|-------------------|
| Bất biến dịch thời gian | Năng lượng |
| Bất biến dịch không gian | Động lượng tuyến tính |
| Bất biến quay | Xung lượng góc |
| Máy đo bất biến | Điện tích |
Đây là một trong những kết quả sâu sắc nhất trong vật lý học - nó kết nối hình học của không thời gian với các định luật bảo toàn cơ bản.
---

## Động lực học cơ thể cứng nhắc
**Vật rắn** là một vật mà tất cả các khoảng cách bên trong vẫn cố định.
### Các khái niệm chính
| Khái niệm | Công thức | Mô tả |
|----------|----------|-------------|
| **Momen quán tính** | I = Σmᵢrᵢ² hoặc I = ∫r² dm | Khả năng chống gia tốc quay |
| **KE quay** | KE = ½Iω² | Năng lượng quay |
| **Động lượng góc** | L = Iω | Phép quay tương tự của p = mv |
| **Mô-men xoắn** | τ = Iα | Phép quay tương tự của F = ma |
### Momen quán tính (Hình dạng thông thường)
| Hình dạng | Trục | Tôi |
|-------|------|---|
| Quả cầu rắn | Qua trung tâm | (2/5)MR² |
| Quả cầu rỗng | Qua trung tâm | (2/3)MR² |
| Xi lanh rắn | Dọc theo trục | (1/2)MR² |
| Thanh mỏng | Qua tâm, vuông góc | (1/12)ML² |
| Thanh mỏng | Qua cuối, vuông góc | (1/3)ML² |
| Đĩa | Qua tâm, vuông góc | (1/2)MR² |
---

## Cơ học quỹ đạo
### Định luật Kepler
| Luật | Tuyên bố |
|------|-------------|
| **Đầu tiên (Dấu chấm lửng)** | Các hành tinh chuyển động theo hình elip với Mặt trời ở một tiêu điểm |
| **Thứ hai (Diện tích bằng nhau)** | Một đường thẳng từ Mặt trời đến hành tinh quét những diện tích bằng nhau trong những khoảng thời gian bằng nhau |
| **Thứ ba (Hòa âm)** | T² ∝ a³ (chu kỳ bình phương tỉ lệ với bán trục lớn lập phương) |
### Năng lượng quỹ đạo
E = ½mv² − GMm/r
| E | Loại quỹ đạo |
|---|----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hyperbolic (không bị ràng buộc) |
### Vận tốc thoát hiểm
v_escape = √(2GM/R)
Đối với Trái đất: v_escape ≈ 11,2 km/s
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm cơ học | Ứng dụng |
|-------------------|-------------|
| Định luật Newton | Động cơ vật lý trong mô phỏng, trò chơi AI, robot |
| Phương pháp năng lượng | Mô hình dựa trên năng lượng, mạng Hopfield, máy Boltzmann |
| Cơ học Lagrange | Mạng lưới thần kinh thông tin vật lý, điều khiển tối ưu, tối ưu hóa quỹ đạo |
| Cơ học Hamilton | Mạng thần kinh Hamilton (HNN), bộ tích hợp đối xứng để mô phỏng |
| Định luật bảo toàn | Độ lệch quy nạp trong mô hình ML, mạng nơ ron tương đương |
| Định lý Noether | Học máy nhận biết đối xứng, học sâu hình học |
| Động lực học cơ thể cứng nhắc | Mô phỏng robot, động lực phân tử, hoạt hình 3D |
| Cơ học quỹ đạo | Định vị vệ tinh (GPS cho ML dựa trên vị trí), thiết kế sứ mệnh không gian |
| Không gian pha (Hamiltonian) | Tìm hiểu hệ động lực, mạng thu hút |
| Phép tính biến phân | Vận chuyển tối ưu, mô hình tổng quát (khớp luồng) |
---

## Bản tóm tắt
| Khung | Phương trình cốt lõi | Sức mạnh |
|----------|--------------|----------|
| Newton | **F** = m**a** | Phân tích lực trực tiếp, trực quan |
| Lagrange | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Không có tọa độ, xử lý các ràng buộc |
| Hamilton | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Cấu trúc đơn giản, kết nối với QM |
| Định luật bảo toàn | Định lý Noether | Kết nối bảo toàn đối xứng sâu |
Cơ học cổ điển không chỉ nói về những quả bóng rơi và con lắc lắc lư. Các khuôn khổ toán học của nó - cơ học Lagrange và Hamilton - là một trong những ý tưởng có ảnh hưởng nhất trong toàn bộ khoa học. Họ khái quát hóa cơ học lượng tử, lý thuyết trường và thậm chí cả học máy hiện đại, trong đó các mô hình dựa trên năng lượng và mạng lưới thần kinh được thông tin về vật lý dựa trực tiếp vào các công thức có từ hàng thế kỷ này.