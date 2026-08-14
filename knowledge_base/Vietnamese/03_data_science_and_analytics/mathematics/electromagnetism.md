---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Điện từ
Điện từ là nghiên cứu về điện trường và từ trường và sự tương tác của chúng. Được thống nhất bởi Maxwell vào những năm 1860, điện từ giải thích ánh sáng, điện, từ tính, sóng vô tuyến và cấu trúc của nguyên tử. Đó là lực cơ bản đầu tiên được hiểu đầy đủ về mặt toán học, và các phương trình của nó đã truyền cảm hứng cho thuyết tương đối đặc biệt và lý thuyết trường hiện đại của Einstein.
---

## Điện trường
### Định luật Coulomb
Lực giữa hai điện tích điểm q₁ và q₂ cách nhau một khoảng r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Hằng số | Giá trị |
|----------|-------|
| ε₀ (độ thấm của không gian trống) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (Hằng số Coulomb k) | 8,988 × 10⁹ N·m2/C2 |
### Định nghĩa điện trường
**E** = **F**/q (lực trên mỗi đơn vị điện tích)
Đối với điện tích điểm Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Đường dây điện trường
| Bất động sản | Quy tắc |
|----------|------|
| Hướng | Hướng ra xa điện tích dương, hướng về phía âm |
| Mật độ | Các đường gần hơn = trường mạnh hơn |
| Vượt qua | Đường trường không bao giờ cắt nhau |
| Dây dẫn | Các đường thẳng vuông góc với nhau |
### Điện thế (Điện áp)
V = −∫ **E** · d**l** (hiệu điện thế là tích phân đường âm của E)
**E** = −∇V (trường là gradient âm của điện thế)
Đối với điện tích điểm: V = (1/4πε₀) · Q/r
| Khái niệm | Công thức | Đơn vị |
|----------|----------|------|
| Năng lượng tiềm năng | U = qV | Joule |
| Electron-volt | 1 eV = 1,602 × 10⁻¹⁹ J | Đơn vị năng lượng |
| Bề mặt đẳng thế | Bề mặt nơi V không đổi | E vuông góc với nó |
---

## Định luật Gauss
### Tuyên bố
Tổng dòng điện qua bất kỳ bề mặt kín nào bằng điện tích kèm theo chia cho ε₀:
∮ **E** · d**A** = Q_enc / ε₀
Ở dạng vi phân: ∇ · **E** = ρ/ε₀
### Sử dụng Định luật Gauss
Định luật Gauss hữu ích nhất khi tính đối xứng cho phép rút E ra khỏi tích phân.
| Đối xứng | Bề mặt Gauss | Kết quả |
|----------|---------|--------|
| Hình cầu | Quả cầu | E = Q/(4πε₀r²) bên ngoài |
| Hình trụ (dòng sạc) | Xi lanh | E = λ/(2πε₀r) |
| Planar (tấm vô hạn) | Hộp đựng thuốc | E = σ/(2ε₀) |
| Giữa các tấm song song | Hộp đựng thuốc | E = σ/ε₀ |
---

## Dây dẫn và tụ điện
### Dây dẫn ở trạng thái cân bằng tĩnh điện
| Bất động sản | Giải thích |
|----------|-------------|
| E = 0 bên trong | Phí sắp xếp lại để hủy trường nội bộ |
| Tất cả điện tích trên bề mặt | Không tính phí nội thất |
| E vuông góc trên bề mặt | Không có thành phần tiếp tuyến (nếu không điện tích sẽ di chuyển) |
| Đẳng thế xuyên suốt | Cùng một V ở mọi nơi bên trong và trên bề mặt |
### Tụ điện
**tụ điện** lưu trữ năng lượng trong điện trường giữa hai dây dẫn.
| Cấu hình | Điện dung |
|--------------|-------------|
| Tấm song song | C = ε₀A/d |
| Hình trụ | C = 2πε₀L / ln(b/a) |
| Hình cầu | C = 4πε₀ab / (b−a) |
| Công thức | Biểu hiện |
|----------|-------------|
| Điện áp sạc | Q = CV |
| Năng lượng được lưu trữ | U = ½CV² = ½Q²/C |
| Mật độ năng lượng | u = ½ε₀E² |
| Kết hợp loạt | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Kết hợp song song | C_total = C₁ + C₂ + ... |
### Điện môi
Chèn một chất điện môi (vật liệu cách điện) có hằng số κ làm tăng điện dung: C = κC₀.
---

## Từ trường
### Lực từ
**F** = q(**v** × **B**) (Lực Lorentz, thành phần từ tính)
| Bất động sản | Tuyên bố |
|----------|----------|
| Hướng | Vuông góc với cả v và B (quy tắc bàn tay phải) |
| Công việc đã hoàn thành | Bằng không (lực vuông góc với vận tốc) |
| Chuyển động tròn | Bán kính r = mv/(qB) trong trường B đều |
### Luật Biot-Savart
Từ trường do một phần tử dòng điện nhỏ gây ra:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Hằng số | Giá trị |
|----------|-------|
| μ₀ (độ thấm của không gian trống) | 4π × 10⁻⁷ T·m/A |
### Định luật Ampe
∮ **B** · d**l** = μ₀I_enc
Ở dạng vi phân: ∇ × **B** = μ₀**J**
**Ứng dụng:**
| Cấu hình | Trường B |
|--------------|----------|
| Dây thẳng dài | B = μ₀I/(2πr) |
| Điện từ (bên trong) | B = μ₀nI |
| Hình xuyến (bên trong) | B = μ₀NI/(2πr) |
---

## Cảm ứng điện từ
### Định luật Faraday
Từ thông thay đổi tạo ra một suất điện động (EMF):
EMF = −dΦ_B/dt
trong đó Φ_B = ∫ **B** · d**A** là từ thông.
Ở dạng vi phân: ∇ × **E** = −∂**B**/∂t
**Định luật Lenz:** EMF cảm ứng chống lại sự thay đổi của từ thông (dấu trừ).
### Ứng dụng của quy nạp
| Ứng dụng | Nguyên tắc |
|-------------|-------------|
| Máy phát điện | Cuộn dây quay trong trường B → EMF xen kẽ |
| Máy biến áp | Thay đổi dòng điện ở sơ cấp → EMF ở thứ cấp |
| Cuộn cảm | Chống lại sự thay đổi của dòng điện: EMF = −L(dI/dt) |
| Dòng điện xoáy | Dòng điện cảm ứng trong dây dẫn số lượng lớn (phanh, sưởi ấm) |
### Cuộn cảm
| Công thức | Biểu hiện |
|----------|-------------|
| Liên kết thông lượng | Φ = LI |
| Năng lượng được lưu trữ | U = ½LI² |
| Kết hợp loạt | L_total = L₁ + L₂ + ... |
| Kết hợp song song | 1/L_total = 1/L₁ + 1/L₂ + ... |
---

## Phương trình Maxwell
Các phương trình Maxwell thống nhất điện và từ thành một lý thuyết duy nhất.
### Ở dạng tích phân
| Phương trình | Tên | Tuyên bố |
|----------|------|----------|
| ∮ **E** · d**A** = Q/ε₀ | Định luật Gauss (điện) | Thông lượng điện = điện tích kèm theo |
| ∮ **B** · d**A** = 0 | Định luật Gauss (từ tính) | Không có đơn cực từ |
| ∮ **E** · d**l** = −dΦ_B/dt | Định luật Faraday | Thay đổi B gây ra E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Định luật Ampe-Maxwell | Hiện tại và thay đổi E tạo ra B |
### Ở dạng vi phân
| Phương trình | Tên | Biểu hiện |
|----------|------|-------------|
| Gauss (điện) | ∇ · **E** = ρ/ε₀ |
| Gauss (từ tính) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampe-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Dòng điện dịch chuyển
Bổ sung quan trọng của Maxwell: thuật ngữ μ₀ε₀ ∂**E**/∂t (dòng dịch chuyển). Điều này đảm bảo bảo toàn điện tích và dự đoán sóng điện từ.
---

##Sóng điện từ
Trong chân không (không có điện tích, không có dòng điện), các phương trình Maxwell mang lại phương trình sóng:
∇2**E** = μ₀ε₀ ∂2**E**/∂t²
∇2**B** = μ₀ε₀ ∂2**B**/∂t²
**Tốc độ ánh sáng:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Thuộc tính của sóng EM
| Bất động sản | Mô tả |
|----------|-------------|
| Ngang | E và B vuông góc với nhau và cùng hướng truyền |
| Đang trong giai đoạn | E và B đồng thời đạt cực đại |
| Tỷ lệ độ lớn | E = cB |
| Dòng năng lượng | S = (1/μ₀)**E** × **B** (Vectơ Poynting) |
| Cường độ | I = ⟨S⟩ = E₀²/(2μ₀c) |
### Quang phổ điện từ
| Loại | Bước sóng | Tần số | Nguồn |
|------|-------------|----------|--------|
| Đài phát thanh | > 1m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Quá trình hạt nhân |
---

## Mạch điện xoay chiều
### Linh kiện mạch RLC
| Thành phần | Quan hệ điện áp-dòng điện | Trở kháng |
|----------|------------------------------|----------|
| Điện trở (R) | V = IR | Z_R = R |
| Cuộn cảm (L) | V = L(dI/dt) | Z_L = jωL |
| Tụ điện (C) | I = C(dV/dt) | Z_C = 1/(jωC) |
### Trở kháng và cộng hưởng
Trở kháng tổng (loạt RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Cộng hưởng:** Khi ωL = 1/ωC → ω₀ = 1/√(LC)
- Khi cộng hưởng: trở kháng nhỏ nhất (= R), dòng điện lớn nhất
- **Hệ số chất lượng:** Q = ω₀L/R (độ sắc nét của cộng hưởng)
### Nguồn trong mạch điện xoay chiều
| Số lượng | Công thức |
|----------|----------|
| Công suất trung bình | P_avg = V_rms · I_rms · cos φ |
| Hệ số công suất | cos φ = R/\|Z\| |
| Điện áp RMS | V_rms = V₀/√2 |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm EM | Ứng dụng |
|----------||-------------|
| Phương trình Maxwell | Mạng lưới thần kinh thông tin vật lý, điện từ tính toán |
| Phương trình sóng | Nền tảng xử lý tín hiệu, động lực phân tích Fourier |
| Phổ điện từ | Dữ liệu cảm biến (Camera hồng ngoại, radar, ảnh vệ tinh) |
| Mạch điện xoay chiều / trở kháng | Hiểu phần cứng chạy ML (nguồn điện, tính toàn vẹn tín hiệu) |
| Vector Poynting | Dòng năng lượng trong giao tiếp không dây (có liên quan đến IoT/edge ML) |
| Định luật Gauss | Tương tự như sự phân kỳ trong phép tính vectơ, được sử dụng trong mô phỏng động lực học chất lỏng |
| Tụ điện/cuộn cảm | Điện toán tương tự cho mạng lưới thần kinh, phần cứng mô phỏng thần kinh |
| Cộng hưởng | Thiết kế bộ lọc, phân tích miền tần số, phương pháp quang phổ |
| Bài toán giá trị biên | Phương pháp phần tử hữu hạn, mô phỏng dựa trên lưới |
| Phép tính vectơ (∇·, ∇×) | Các công cụ toán học thiết yếu được sử dụng trong suốt lý thuyết ML |
---

## Bản tóm tắt
| Luật | Nó nói gì | Dạng vi phân |
|------|-------------|-------------------|
| Gauss (điện) | Điện tích tạo ra sự phân kỳ điện trường | ∇ · E = ρ/ε₀ |
| Gauss (từ tính) | Không có đơn cực từ | ∇ · B = 0 |
| Faraday | Thay đổi B tạo ra lọn tóc E | ∇ × E = −∂B/∂t |
| Ampe-Maxwell | Dòng điện và sự thay đổi E tạo ra độ quăn B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
Điện từ là lý thuyết vật lý hoàn chỉnh và được thử nghiệm tốt nhất từng được xây dựng. Các phương trình của nó - chỉ có bốn - mô tả mọi thứ, từ tĩnh điện đến ánh sáng cho đến hoạt động của mọi thiết bị điện tử từng được chế tạo. Đối với các nhà khoa học dữ liệu, sự hiểu biết về điện từ mang lại trực giác sâu sắc về các hiện tượng sóng, phép tính vectơ và vật lý làm nền tảng cho tất cả phần cứng máy tính hiện đại.