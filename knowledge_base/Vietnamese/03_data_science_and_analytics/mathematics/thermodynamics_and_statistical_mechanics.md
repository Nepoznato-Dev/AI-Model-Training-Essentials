<!--
---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Nhiệt động lực học và Cơ học thống kê
Nhiệt động lực học mô tả hành vi vĩ mô của các hệ thống về nhiệt độ, áp suất và entropy - mà không biết các nguyên tử trông như thế nào. Cơ học thống kê giải thích nhiệt động lực học từ dưới lên: nó rút ra các tính chất vĩ mô từ hành vi vi mô của một số lượng lớn các hạt. Cùng nhau, chúng cung cấp sự hiểu biết sâu sắc nhất về năng lượng, entropy và trạng thái cân bằng — các khái niệm đã được áp dụng vào lý thuyết thông tin, học máy và hơn thế nữa.
---

## Các biến nhiệt động và trạng thái
### Biến trạng thái
| Biến | Loại | Đơn vị | Mô tả |
|----------|------|------|-------------|
| Nhiệt độ (T) | Chuyên sâu | Kelvin (K) | Động năng trung bình trên mỗi hạt |
| Áp suất (P) | Chuyên sâu | Pascal (Pa) | Lực trên một đơn vị diện tích |
| Khối lượng (V) | Mở rộng | m³ | Không gian chiếm đóng |
| Nội năng (U) | Mở rộng | Joule (J) | Tổng năng lượng vi mô |
| Entropy (S) | Mở rộng | J/K | Đo lường mức độ rối loạn/vi mô |
| Số hạt (N) | Mở rộng | nốt ruồi hoặc đếm | Lượng chất |
Các biến **Chuyên sâu** không phụ thuộc vào kích thước hệ thống; **có nhiều biến ** rộng rãi.
### Phương trình trạng thái
Đối với khí lý tưởng: PV = nRT = Nk_BT
| Hằng số | Giá trị |
|----------|-------|
| R (hằng số khí) | 8,314 J/(mol·K) |
| k_B (hằng số Boltzmann) | 1,381 × 10⁻²³ J/K |
| N_A (số Avogadro) | 6,022 × 102³ /mol |
---

## Định luật nhiệt động lực học
### Luật số 0
Nếu A cân bằng nhiệt với B, B với C thì A cân bằng nhiệt với C.
**Ý nghĩa:** Nhiệt độ được xác định rõ ràng và có thể đo lường được.
### Định luật thứ nhất (Bảo toàn năng lượng)
ΔU = Q - W
| Biểu tượng | Ý nghĩa |
|--------|----------|
| ΔU | Thay đổi nội năng |
| Q | Nhiệt bổ sung vào hệ thống |
| W | Công việc do hệ thống thực hiện |
**Dạng vi phân:** dU = δQ − δW = δQ − PdV
| Quy trình | Ràng buộc | Hậu quả |
|----------|-------------|-------------|
| đẳng âm | dV = 0 | W = 0, ΔU = Q |
| đẳng áp | dP = 0 | W = PΔV |
| Đẳng nhiệt | dT = 0 | ΔU = 0 (khí lý tưởng), Q = W |
| đoạn nhiệt | δQ = 0 | ΔU = −W |
### Định luật thứ hai (Entropy)
**Phát biểu của Clausius:** Nhiệt không thể tự truyền từ nơi lạnh sang nơi nóng.
**Tuyên bố của Kelvin-Planck:** Không có động cơ nào có thể chuyển toàn bộ nhiệt thành công.
**Câu lệnh Entropy:** Đối với mọi quá trình: ΔS_universe ≥ 0
| Loại quy trình | ΔS_vũ trụ |
|-------------|-------------|
| Có thể đảo ngược | = 0 |
| Không thể đảo ngược (có thật) | > 0 |
**Thay đổi Entropy:** dS = δQ_rev / T
### Định luật thứ ba
Khi T → 0 K, entropy của một tinh thể hoàn hảo tiến tới 0: lim_{T→0} S = 0
**Ý nghĩa:** Không thể đạt được độ không tuyệt đối trong những bước hữu hạn.
---

## Entropy theo chiều sâu
### Entropy nhiệt động
S là một hàm trạng thái. Đối với quá trình thuận nghịch giữa trạng thái A và B:
ΔS = ∫_A^B δQ_vòng / T
**Ví dụ đã làm:** Sự thay đổi Entropy khi đun nóng nước từ T₁ đến T₂ ở áp suất không đổi.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropy thống kê (Boltzmann)
S = k_B ln Ω
trong đó Ω là số lượng trạng thái vi mô phù hợp với trạng thái vĩ mô.
| Vĩ mô | Trạng thái vi mô (Ω) | Entropy |
|----------|-----------------|----------|
| Tất cả gas trong một nửa hộp | Nhỏ | Thấp |
| Khí phân bổ đều | Rất lớn | Cao |
| Tinh thể hoàn hảo ở 0 K | 1 | 0 |
**Kết nối:** Định luật thứ hai trở thành định luật thống kê — các hệ thống tiến hóa theo hướng các trạng thái vĩ mô có nhiều trạng thái vi mô hơn đơn giản vì chúng có khả năng xảy ra cao hơn rất nhiều.
---

## Entanpi và năng lượng tự do
### Entanpy
H = U + PV
Hữu ích cho các quá trình ở áp suất không đổi (hầu hết hóa học và sinh học).
ΔH = Q_p (nhiệt ở áp suất không đổi)
### Năng lượng miễn phí Helmholtz
F = U − TS
| Bất động sản | Tuyên bố |
|----------|----------|
| Ý nghĩa | Công lớn nhất có thể trích xuất được ở hằng số T, V |
| Cân bằng | Hệ thống cực tiểu hóa F tại hằng số T, V |
| Liên quan đến chức năng phân vùng | F = −k_BT ln Z |
### Năng lượng miễn phí Gibbs
G = H − TS = U + PV − TS
| Bất động sản | Tuyên bố |
|----------|----------|
| Ý nghĩa | Công không giãn nở tối đa ở hằng số T, P |
| Cân bằng | Hệ thống cực tiểu hóa G tại hằng số T, P |
| Tính tự phát | ΔG < 0 → tự phát; ΔG = 0 → cân bằng |
| Phản ứng hóa học | ΔG = ΔH − TΔS xác định hướng |
### Tóm tắt thế năng nhiệt động
| Tiềm năng | Biến tự nhiên | Vi sai | Giảm thiểu khi |
|----------|-------------------|-------------|-------|
| U (năng lượng bên trong) | S, V | dU = TdS − PdV | Hệ thống biệt lập |
| H (entanpy) | S, P | dH = TdS + VdP | Hằng số P, đoạn nhiệt |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Hằng số T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Hằng số T, P |
---

## Chu trình Carnot
**Chu trình Carnot** là động cơ nhiệt hiệu quả nhất có thể, hoạt động giữa nhiệt độ T_H (nóng) và T_C (lạnh).
### Bốn giai đoạn
| Sân khấu | Quy trình | Điều gì xảy ra |
|-------|----------|-------------|
| 1 → 2 | Giãn nở đẳng nhiệt | Hấp thụ nhiệt Q_H từ nguồn nóng tại T_H |
| 2 → 3 | Sự giãn nở đoạn nhiệt | Khí nguội đi từ T_H đến T_C |
| 3 → 4 | Nén đẳng nhiệt | Thải nhiệt Q_C sang bình lạnh tại T_C |
| 4 → 1 | Nén đoạn nhiệt | Khí nóng lên từ T_C đến T_H |
### Hiệu quả của Carnot
η_Carnot = 1 − T_C/T_H
| TH | T_C | η_Carnot |
|------|------|----------|
| 500K | 300K | 40% |
| 1000K | 300K | 70% |
| 300K | 299K | 0,33% |
**Không có động cơ thực nào có thể vượt quá hiệu suất của Carnot.** Động cơ thực luôn không thể đảo ngược (ma sát, nhiễu loạn, chênh lệch nhiệt độ hữu hạn).
---

## Cơ học thống kê
### Phân phối Boltzmann
Đối với một hệ cân bằng nhiệt ở nhiệt độ T, xác suất ở trạng thái vi mô có năng lượng E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
trong đó Z là **hàm phân vùng**:
Z = Σᵢ e^{−E_i / k_BT}
### Chức năng phân vùng
Z mã hóa tất cả thông tin nhiệt động về hệ thống.
| Số lượng | Công thức |
|----------|----------|
| Năng lượng tự do Helmholtz | F = −k_BT ln Z |
| Năng lượng trung bình | ⟨E⟩ = −∂(ln Z)/∂β trong đó β = 1/(k_BT) |
| Entropy | S = k_B(ln Z + β⟨E⟩) |
| Công suất nhiệt | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Áp lực | P = (1/β) ∂(ln Z)/∂V |
### Ví dụ hoạt động: Hệ thống hai trạng thái
Một hạt có thể ở trạng thái 0 (năng lượng 0) hoặc trạng thái 1 (năng lượng ε).
Z = 1 + e^{−βε}
| Số lượng | Kết quả |
|----------|--------|
| P (trạng thái 0) | 1/(1 + e^{−βε}) |
| P (trạng thái 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Giới hạn T cao (β→0) | ⟨E⟩ → ε/2 (xác suất bằng nhau) |
| Giới hạn T thấp (β→∞) | ⟨E⟩ → 0 (trạng thái cơ bản) |
### Định lý đẳng thức
Mỗi bậc tự do bậc hai đóng góp ½k_BT vào năng lượng trung bình.
| Hệ thống | Mức độ Tự do | ⟨E⟩ |
|--------|-------------------|------|
| Khí đơn nguyên tử (He) | 3 bản dịch | (3/2)k_BT |
| Khí diatomic (N₂) tại phòng T | 3 xuyên + 2 thối | (5/2)k_BT |
| Khí diatomic ở mức T cao | 3 trans + 2 thối + 1 vib | (7/2)k_BT |
| Chất rắn (mô hình Einstein) | 3 rung động (mỗi nguyên tử) | 3k_BT |
---

## Kết nối với lý thuyết thông tin
### Entropy của Shannon và Entropy nhiệt động
| Khía cạnh | Shannon Entropy H(X) | Entropy nhiệt động S |
|--------|----------------------|---------------|
| Định nghĩa | −Σ pᵢ log pᵢ | k_B ln Ω (hoặc −k_B Σ pᵢ ln pᵢ) |
| Tối đa khi | Phân phối thống nhất | Cân bằng nhiệt |
| Biện pháp | Nội dung thông tin/sự không chắc chắn | Số lượng microstate có thể truy cập |
| Đơn vị | Bit hoặc nats | J/K |
**Công thức entropy Gibbs:** S = −k_B Σᵢ pᵢ ln pᵢ (có dạng giống hệt entropy Shannon)
### Nguyên tắc Entropy tối đa
Cả hai lĩnh vực đều sử dụng cùng một nguyên tắc: phân bố thể hiện tốt nhất trạng thái kiến ​​thức của chúng ta là phân bố tối đa hóa entropy theo các ràng buộc đã biết.
| Ràng buộc | Phân phối Kết quả |
|----------||----------------------|
| Được biết đến có nghĩa là | Phân phối theo cấp số nhân |
| Giá trị trung bình và phương sai đã biết | Phân phối Gauss |
| Năng lượng đã biết ⟨E⟩ | Phân phối Boltzmann |
| Không có ràng buộc | Phân phối thống nhất |
### Nguyên lý Landauer
Việc xóa một bit thông tin sẽ làm tiêu hao ít nhất k_BT ln 2 năng lượng dưới dạng nhiệt. Điều này kết nối trực tiếp việc xử lý thông tin với nhiệt động lực học - tính toán có tiêu tốn năng lượng cơ bản.
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm Nhiệt/StatMech | Ứng dụng |
|------------------------|-------------|
| Phân phối Boltzmann | Chức năng Softmax, mô hình dựa trên năng lượng, ủ mô phỏng |
| Chức năng phân vùng | Chuẩn hóa hằng số trong các mô hình xác suất, nói chung khó hiểu |
| Năng lượng miễn phí | Suy luận biến phân (tối thiểu năng lượng tự do biến thiên = giảm thiểu phân kỳ KL) |
| Entropy | Chính quy hóa, thăm dò trong RL (RL entropy tối đa), cây quyết định |
| Nguyên lý entropy tối đa | Bộ phân loại MaxEnt, lựa chọn trước, ước tính phân phối |
| Ủ mô phỏng | Tối ưu hóa toàn cầu bằng cách giảm dần "nhiệt độ" |
| Cơ học thống kê | Hiểu các giai đoạn chuyển tiếp trong học tập (lò mò, đi xuống kép) |
| Thiết bị | Hiểu sự phân bố năng lượng trong mô phỏng vật lý |
| Nguyên lý Landauer | Giới hạn cơ bản của tính toán, tính toán thuận nghịch |
| Lấy mẫu Gibbs | Phương pháp MCMC lấy cảm hứng trực tiếp từ cơ học thống kê |
| Nhiệt độ (tính bằng softmax) | Kiểm soát tính ngẫu nhiên của các dự đoán: P(i) ∝ exp(z_i/T) |
---

## Bản tóm tắt
| Luật/Khái niệm | Ý tưởng cốt lõi | Công thức |
|----------||-------------|----------|
| Luật thứ không | Nhiệt độ được xác định rõ ràng | Độ truyền nhiệt của cân bằng nhiệt |
| Luật đầu tiên | Năng lượng được bảo toàn | ΔU = Q - W |
| Luật thứ hai | Entropy của vũ trụ tăng | ΔS ≥ 0 |
| Định luật thứ ba | Độ không tuyệt đối là không thể đạt được | S → 0 dưới dạng T → 0 |
| Entropy Boltzmann | Entropy đếm microstate | S = k_B ln Ω |
| Phân phối Boltzmann | Xác suất trạng thái năng lượng | P ∝ e^{−E/k_BT} |
| Chức năng phân vùng | Mã hóa tất cả thông tin nhiệt động lực học | Z = Σ e^{−E_i/k_BT} |
| Năng lượng miễn phí | Công việc hữu ích có sẵn | F = U − TS, G = H − TS |
| Hiệu quả Carnot | Hiệu suất động cơ nhiệt tối đa | η = 1 − T_C/T_H |
Nhiệt động lực học và cơ học thống kê là nơi vật lý gặp lý thuyết thông tin. Entropy tương tự chi phối động cơ nhiệt chi phối việc nén dữ liệu. Phân phối Boltzmann tương tự mô tả các phân tử khí cung cấp năng lượng cho lớp softmax trong mọi bộ phân loại. Hiểu được những kết nối này sẽ mang lại cho bạn cái nhìn thống nhất về vật lý, xác suất và học máy.