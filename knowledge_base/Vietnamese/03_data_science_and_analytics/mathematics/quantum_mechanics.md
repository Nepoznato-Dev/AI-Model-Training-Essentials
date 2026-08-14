---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Cơ học lượng tử
Cơ học lượng tử là lý thuyết vật lý ở quy mô nhỏ nhất - nguyên tử, electron, photon và các hạt cơ bản của tự nhiên. Nó thay thế thế giới tất định của cơ học cổ điển bằng xác suất, sự chồng chất và sự vướng víu. Bất chấp bản chất phản trực giác của nó, cơ học lượng tử là lý thuyết được thử nghiệm chính xác nhất trong toàn bộ khoa học. Ngày nay, các nguyên tắc của nó đang trở nên phù hợp trực tiếp với việc tính toán thông qua máy tính lượng tử, hứa hẹn giải quyết một số vấn đề nhất định nhanh hơn theo cấp số nhân so với các máy cổ điển.
---

## Động lực lịch sử
### Thất bại của Vật lý Cổ điển
| Vấn đề | Dự đoán cổ điển | Quan sát | Độ phân giải |
|----------|----------------------|-------------|----------||
| Bức xạ vật đen | Thảm họa tia cực tím (năng lượng vô hạn ở thời điểm ngắn λ) | Bước sóng cực đại hữu hạn | Planck: năng lượng bị lượng tử hóa (E = nhν) |
| Hiệu ứng quang điện | KE phụ thuộc vào cường độ chứ không phải tần số | KE phụ thuộc vào tần số | Einstein: ánh sáng bị lượng tử hóa (photon, E = hν) |
| Quang phổ nguyên tử | Phổ phát xạ liên tục | Các vạch quang phổ rời rạc | Bohr: các electron chiếm quỹ đạo lượng tử hóa |
| Nhiễu xạ điện tử | Các hạt không nhiễu xạ | Các electron tạo ra các mẫu giao thoa | de Broglie: hạt có bước sóng λ = h/p |
### Hằng số chính
| Hằng số | Biểu tượng | Giá trị |
|----------|--------|-------|
| hằng số Planck | h | 6,626 × 10⁻³⁴ J·s |
| Hằng số Planck giảm | ℏ = h/2π | 1,055 × 10⁻³⁴ J·s |
| Tốc độ ánh sáng | c | 3,0 × 10⁸ m/s |
| Khối lượng electron | tôi_e | 9,109 × 10⁻³¹ kg |
| Phí tiểu học | e | 1,602 × 10⁻¹⁹ C |
| Bán kính Bohr | a₀ | 5,292 × 10⁻¹¹ m |
---

## Lưỡng tính sóng-hạt
### de Broglie Bước sóng
Mọi hạt có động lượng p đều có bước sóng liên quan:
λ = h/p = h/(mv)
| Hạt | Điển hình λ | Hành vi sóng có thể quan sát được? |
|----------|--------------|------------------------------------------|
| Điện tử (100 eV) | 0,12nm | Có (nhiễu xạ tinh thể) |
| Proton | 0,003nm | Có (tán xạ neutron) |
| Bóng chày (40 m/s) | 10⁻³⁴ m | Không (quá nhỏ để phát hiện) |
### Thí nghiệm khe đôi
Thí nghiệm lượng tử tinh túy:
1. Các hạt cháy (electron, photon) lần lượt ở hai khe
2. Mỗi hạt chạm tới một điểm duy nhất trên máy dò
3. Theo thời gian, một hình ảnh giao thoa xuất hiện - như thể mỗi hạt đồng thời đi qua cả hai khe
4. Nếu bạn đo xem hạt đi qua khe nào thì vân giao thoa sẽ biến mất
**Kết luận:** Các vật thể lượng tử không thuần túy là hạt hay thuần túy sóng. Chúng thể hiện hành vi giống sóng khi không quan sát được và hành vi giống hạt khi đo.
---

## Hàm sóng
### Sự định nghĩa
**hàm sóng** ψ(x, t) mô tả hoàn toàn một hệ lượng tử. Đây là một hàm có giá trị phức có mô đun bình phương cho mật độ xác suất:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Chuẩn hóa
Tổng xác suất phải bằng 1:
∫ |ψ(x)|² dx = 1 (trên toàn bộ không gian)
### Quy tắc sinh ra
Xác suất tìm thấy hạt giữa x và x + dx:
P(x đến x+dx) = |ψ(x)|² dx
Đối với một cái chung có thể quan sát được với các trạng thái riêng φₙ:
P(đo giá trị riêng aₙ) = |⟨φₙ|ψ⟩|²
---

## Phương trình Schrodinger
### Phương trình Schrodinger phụ thuộc thời gian
iℏ ∂ψ/∂t = Ĥψ
trong đó Ĥ là **toán tử Hamilton** (toán tử năng lượng tổng).
### Phương trình Schrodinger độc lập với thời gian
Đối với trạng thái dừng (trạng thái năng lượng riêng):
Ĥψ = Eψ
Đây là một phương trình giá trị riêng: năng lượng cho phép E là giá trị riêng của Ĥ.
### Hạt trong hộp (Giếng vuông vô hạn)
Hệ lượng tử đơn giản nhất: hạt giới hạn ở 0 < x < L.
| Số lượng | Kết quả |
|----------|--------|
| Hàm sóng | ψₙ(x) = √(2/L) sin(nπx/L) |
| Mức năng lượng | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Trạng thái cơ bản | n = 1, E₁ = h²/(8mL²) |
| Năng lượng điểm không | E₁ > 0 (hạt không thể đứng yên hoàn toàn) |
| Số lượng tử | n = 1, 2, 3, ... (chỉ số nguyên dương) |
### Dao động điều hòa lượng tử
V(x) = ½mω²x²
| Số lượng | Kết quả |
|----------|--------|
| Mức năng lượng | Eₙ = (n + ½)ℏω |
| Năng lượng điểm không | E₀ = ½ℏω |
| Khoảng cách | ΔE = ℏω (đồng đều) |
| Hàm sóng | Đa thức Hermite × Gaussian |
---

## Toán tử và vật quan sát
Trong cơ học lượng tử, mọi vật thể có thể quan sát được đều tương ứng với **toán tử Hermitian**.
### Toán tử chính
| Có thể quan sát | Toán tử (không gian vị trí) | Giá trị riêng |
|----------|--------------------------|-------------|
| Vị trí | x̂ = x | Tất cả đều có thật x |
| Động lực | p̂ = −iℏ ∂/∂x | Tất cả thực p |
| Năng lượng (Hamiltonian) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (rời rạc cho các trạng thái ràng buộc) |
| Xung lượng góc | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Quay | Ŝ = (ℏ/2)σ (ma trận Pauli) | ±ℏ/2 (đối với spin-½) |
### Giá trị kỳ vọng
Kết quả trung bình của phép đo A có thể quan sát được ở trạng thái ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Quan hệ giao hoán
[Â, B̂] = ÂB̂ − B̂Â
| Cổ góp | Kết quả | Ý nghĩa |
|----------|----------|-------------|
| [x̂, p̂] | tôiℏ | Vị trí và động lượng không tương thích |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Các thành phần động lượng góc không tương thích |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Ma trận Pauli (thành phần spin) |
Nếu [Â, B̂] = 0, các giá trị có thể quan sát được có thể được đo đồng thời (chia sẻ trạng thái riêng).
---

## Nguyên tắc bất định
### Nguyên lý bất định Heisenberg
Δx · Δp ≥ ℏ/2
Tổng quát hơn, đối với hai vật thể quan sát A và B bất kỳ:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Mối quan hệ không chắc chắn
| Cặp | Quan hệ | Giải thích |
|------|----------|-------|
| Vị trí-đà | ΔxΔp ≥ ℏ/2 | Không thể biết chính xác cả hai |
| Năng lượng-thời gian | ΔEΔt ≥ ℏ/2 | Các trạng thái tồn tại trong thời gian ngắn có năng lượng không chắc chắn |
| Xung lượng góc | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Không thể biết đồng thời tất cả các thành phần |
**Quan trọng:** Độ không đảm bảo đo không phải là nhiễu loạn đo lường — nó là một tính chất cơ bản của trạng thái lượng tử. Một hạt không có vị trí và động lượng xác định cùng một lúc.
---

## Trạng thái lượng tử và sự chồng chất
### Ký hiệu Dirac (Bra-Ket)
| Biểu tượng | Tên | Ý nghĩa |
|--------|------|---------|
| \|ψ⟩ | Kết | Vectơ trạng thái (vectơ cột) |
| ⟨ψ\| | Áo ngực | Chuyển vị liên hợp (vectơ hàng) |
| ⟨φ\|ψ⟩ | Sản phẩm bên trong | Biên độ của ψ được tìm thấy ở trạng thái φ |
| \|ψ\|² | Bình phương chuẩn | Xác suất |
### Nguyên lý chồng chất
Nếu \|ψ₁⟩ và \|ψ₂⟩ là các trạng thái lượng tử hợp lệ, thì bất kỳ tổ hợp tuyến tính nào cũng hợp lệ:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

trong đó |α|² + |β|² = 1 (chuẩn hóa).
**Đo lường:** Khi được đo, hệ thống "sụp đổ" thành \|ψ₁⟩ với xác suất |α|² hoặc \|ψ₂⟩ với xác suất |β|².
### Qubit
**qubit** là bit lượng tử: một hệ lượng tử hai cấp.
\|ψ⟩ = α\|0⟩ + β\|1⟩, trong đó |α|² + |β|² = 1
| Đại diện | \|0⟩ | \|1⟩ |
|--------------|------|------|
| Quay | Quay lên ↑ | Quay xuống ↓ |
| Phân cực photon | Ngang | Dọc |
| Mức năng lượng | Trạng thái cơ bản | Trạng thái kích thích |
| Mạch | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Qubit cầu:** Bất kỳ trạng thái qubit nào cũng có thể được viết là:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
trong đó θ ∈ [0, π] và φ ∈ [0, 2π). Không gian trạng thái là một hình cầu.
---

## Rắc rối
Hai qubit **bị vướng víu** khi trạng thái chung của chúng không thể được viết dưới dạng tích của các trạng thái riêng lẻ.
### Chuông Kỳ (Vướng víu tối đa)
| Tiểu bang | Biểu hiện | Tên |
|-------|-------------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Trạng thái chuông |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Trạng thái chuông |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Trạng thái chuông |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Trạng thái đơn lẻ |
### Thuộc tính của sự vướng víu
| Bất động sản | Mô tả |
|----------|-------------|
| Tương quan | Đo một qubit ngay lập tức xác định qubit kia, bất kể khoảng cách |
| Không liên lạc | Không thể chỉ sử dụng sự vướng víu để gửi thông tin nhanh hơn ánh sáng |
| Chế độ một vợ một chồng | Nếu A vướng víu với B tối đa thì nó không thể vướng vào C |
| Mong manh | Tương tác với môi trường phá hủy sự vướng víu (mất kết hợp) |
### Nghịch lý EPR và Định lý Bell
Einstein, Podolsky và Rosen lập luận rằng cơ học lượng tử phải không đầy đủ (các biến ẩn). Bell đã chỉ ra rằng mọi lý thuyết biến ẩn cục bộ đều thỏa mãn những bất đẳng thức nhất định. Các thí nghiệm vi phạm bất đẳng thức Bell - xác nhận cơ học lượng tử và loại trừ các biến ẩn cục bộ.
---

## Cổng lượng tử
Cổng lượng tử là các hoạt động đơn nhất trên qubit.
### Cổng Qubit đơn
| Cổng | Ma trận | Hiệu ứng |
|------|--------|--------|
| **Pauli-X** (KHÔNG) | [[0,1],[1,0]] | Lật bit: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Đảo bit + pha |
| **Pauli-Z** | [[1,0],[0,−1]] | Lật pha: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Tạo sự chồng chất: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Giai đoạn** (S) | [[1,0],[0,i]] | π/2 quay quanh Z |
| **Cổng T** | [[1,0],[0,e^{iπ/4}]] | π/4 quay quanh Z |
| **Xoay** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Xoay θ quanh trục X |
### Cổng hai Qubit
| Cổng | Mô tả | Hiệu ứng |
|------|-------------|--------|
| **KHÔNG** | Kiểm soát-KHÔNG | Lật mục tiêu nếu quyền kiểm soát là \|1⟩ |
| **CZ** | Kiểm soát-Z | Áp dụng Z cho mục tiêu nếu điều khiển là \|1⟩ |
| **Hoán đổi** | Trao đổi qubit | \|ab⟩ → \|ba⟩ |
### Tạo vướng víu
Áp dụng H cho qubit 1, sau đó CNOT với qubit 1 làm đối chứng:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Thuật toán lượng tử
| Thuật toán | Tăng tốc | Ứng dụng |
|----------||----------|-------------|
| **Shor's** | Hàm mũ (bao thanh toán) | Phá vỡ mã hóa RSA |
| **Grover's** | Bậc hai (tìm kiếm) | Tìm kiếm phi cấu trúc trong O(√N) |
| **VQE** | Kinh nghiệm | Tìm năng lượng trạng thái cơ bản (hóa học, vật liệu) |
| **QAOA** | Kinh nghiệm | Tối ưu hóa tổ hợp |
| **HHL** | Hàm mũ (theo điều kiện) | Giải hệ tuyến tính |
| **Mô phỏng lượng tử** | Hàm mũ | Mô phỏng hệ thống lượng tử (động lực ban đầu của Feynman) |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm lượng tử | Ứng dụng |
|-------|-------------|
| Qubit và sự chồng chất | Học máy lượng tử, lấy mẫu tăng cường lượng tử |
| Sự vướng víu | Truyền thông lượng tử, phân phối khóa lượng tử (QKD) |
| Cổng lượng tử | Thiết kế mạch lượng tử cho chương trình con ML |
| Thuật toán Grover | Tăng tốc bậc hai để tối ưu hóa dựa trên tìm kiếm |
| Thuật toán Shor | Mối đe dọa đối với mật mã hiện tại; thúc đẩy tiền điện tử hậu lượng tử |
| Mô phỏng lượng tử | Khám phá thuốc, khoa học vật liệu, mô phỏng hóa học |
| Thuật toán biến đổi (VQE, QAOA) | ML lượng tử ngắn hạn trên thiết bị NISQ |
| Quy tắc sinh ra | Kết quả xác suất tương tự như lấy mẫu từ phân phối |
| Sản phẩm Tenor | Hệ thống nhiều qubit (không gian trạng thái hàm mũ - phép toán tương tự như đại số đa tuyến tính trong ML) |
| Ma trận đơn nhất | Tương tự lượng tử của các phép biến đổi trực giao |
---

## Bản tóm tắt
| Khái niệm | Ý tưởng cốt lõi | Phương trình khóa |
|----------|-------------|-------------|
| Lưỡng tính sóng-hạt | Vật chất có tính chất sóng | λ = h/p |
| Hàm sóng | Mô tả đầy đủ về trạng thái lượng tử | P(x) = \|ψ(x)\|² |
| Phương trình Schrodinger | Các trạng thái lượng tử phát triển như thế nào | iℏ ∂ψ/∂t = Ĥψ |
| Người vận hành | Đài quan sát là toán tử Hermitian | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Sự không chắc chắn | Giới hạn cơ bản về kiến ​​thức đồng thời | ΔxΔp ≥ ℏ/2 |
| Sự chồng chất | Các tiểu bang có thể được thêm vào | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Sự vướng víu | Trạng thái chung không thể tách rời | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Cổng lượng tử | Hoạt động đơn nhất trên qubit | bộ cổng H, CNOT và cổng vạn năng |
Cơ học lượng tử thách thức trực giác sâu sắc nhất của chúng ta về thực tế - các hạt là sóng, vật thể ở hai nơi cùng một lúc, các mối tương quan thách thức lời giải thích cổ điển. Tuy nhiên, toán học của nó rất chính xác và những dự đoán của nó có độ chính xác không gì sánh được. Đối với các nhà khoa học dữ liệu, cơ học lượng tử đang trở nên có liên quan trực tiếp thông qua điện toán lượng tử, điều này hứa hẹn sẽ biến đổi tính tối ưu hóa, mật mã, mô phỏng và khả năng tự học máy.