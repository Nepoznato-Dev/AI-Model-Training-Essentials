---
# Metadata
title: "Relativity"
description: "Special relativity, Lorentz transformations, time dilation, length contraction, mass-energy equivalence, four-vectors, and introduction to general relativity"
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
    changes: "Initial deep-dive into relativity"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [relativity, special-relativity, general-relativity, lorentz-transformations, time-dilation, length-contraction, mass-energy, spacetime]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Thuyết tương đối
Thuyết tương đối của Einstein đã cách mạng hóa sự hiểu biết của chúng ta về không gian, thời gian và lực hấp dẫn. **Thuyết tương đối đặc biệt** (1905) cho thấy rằng không gian và thời gian không tách rời mà được dệt thành một tấm vải duy nhất gọi là không thời gian, và tốc độ ánh sáng là như nhau đối với tất cả những người quan sát. **Thuyết tương đối rộng** (1915) đã mô phỏng lại lực hấp dẫn không phải là một lực mà là độ cong của không thời gian gây ra bởi khối lượng và năng lượng. Những lý thuyết này củng cố việc điều hướng GPS, máy gia tốc hạt và sự hiểu biết của chúng ta về lỗ đen và sự tiến hóa của vũ trụ.
---

## Định đề của thuyết tương đối đặc biệt
Einstein đã xây dựng thuyết tương đối đặc biệt dựa trên hai định đề có vẻ đơn giản:
| Định đề | Tuyên bố |
|----------||----------|
| **Nguyên lý tương đối** | Các định luật vật lý là như nhau trong mọi hệ quy chiếu quán tính (không gia tốc) |
| ** Hằng số c** | Tốc độ ánh sáng trong chân không (c ≈ 3 × 10⁸ m/s) là như nhau đối với tất cả người quan sát, bất kể chuyển động của họ hay chuyển động của nguồn |
Hai định đề này kết hợp với nhau đã lật đổ trực giác hàng thế kỷ của Newton về không gian và thời gian tuyệt đối.
---

## Phép biến đổi Lorentz
**Biến đổi Lorentz** liên hệ tọa độ giữa hai hệ quy chiếu quán tính chuyển động với vận tốc tương đối v.
### Phương trình chuyển đổi
Đối với khung S' chuyển động với vận tốc v dọc theo trục x so với khung S:
| Số lượng | Chuyển đổi |
|----------|--------------|
| x' | γ(x − vt) |
| t' | γ(t − vx/c2) |
| y' | y |
| z' | z |
trong đó γ (hệ số Lorentz) = 1/√(1 − v2/c2)
### Hệ số Lorentz γ
| v/c | γ | Hiệu ứng |
|------|---|--------|
| 0 | 1.0 | Không có hiệu ứng tương đối tính (giới hạn Newton) |
| 0,1 | 1,005 | Hiệu chỉnh 0,5% |
| 0,5 | 1.155 | Điều chỉnh 15,5% |
| 0,9 | 2.294 | Sự giãn nở thời gian đáng kể |
| 0,99 | 7.089 | Hiệu ứng cực chất |
| 0,999 | 22.37 | Chế độ máy gia tốc hạt |
| → 1 | → ∞ | Không thể đối với các vật thể có khối lượng lớn |
### Phép biến đổi nghịch đảo
Để đi từ S' quay lại S: thay v bằng −v.
---

## Sự giãn nở thời gian
Đồng hồ chuyển động chạy chậm.
Δt = γΔt₀
trong đó Δt₀ là **thời gian thích hợp** (thời gian được đo trong khung nghỉ của đồng hồ).
**Ví dụ đã hoạt động:** Một muon được tạo ra ở độ cao 10 km di chuyển với tốc độ 0,998c. Thời gian tồn tại của khung nghỉ là 2,2 μs.
- γ = 1/√(1 − 0,9982) ≈ 15,8
- Tuổi thọ giãn nở: Δt = 15,8 × 2,2 μs = 34,8 μs
- Quãng đường đi được: d = 0,998c × 34,8 μs ≈ 10,4 km
- Không giãn nở thời gian: d = 0,998c × 2,2 μs ≈ 0,66 km (sẽ không bao giờ chạm tới mặt đất)
- **Thực tế:** Muon chạm tới bề mặt Trái đất — xác nhận sự giãn nở thời gian bằng thực nghiệm.
### Nghịch lý song sinh
Một cặp song sinh di chuyển với tốc độ cao và quay trở lại. Họ trẻ hơn cặp song sinh ở nhà. Đây không phải là một nghịch lý thực sự - cặp song sinh đang di chuyển tăng tốc (thay đổi hệ quy chiếu quán tính), phá vỡ tính đối xứng.
---

## Co chiều dài
Vật chuyển động bị rút ngắn dọc theo hướng chuyển động.
L = L₀/γ
trong đó L₀ là **độ dài thích hợp** (độ dài được đo trong khung nghỉ của đối tượng).
| v/c | γ | Hệ số co L/L₀ |
|------|---|---------------|
| 0,5 | 1.15 | 87% |
| 0,9 | 2,29 | 44% |
| 0,99 | 7.09 | 14% |
| 0,999 | 22.4 | 4,5% |
**Điểm mấu chốt:** Sự co lại chiều dài không phải là ảo ảnh quang học — nó là hiệu ứng vật lý thực sự được đo bởi những người quan sát trong chuyển động tương đối.
---

## Tính tương đối của tính đồng thời
Các sự kiện diễn ra đồng thời trong một khung hình KHÔNG đồng thời trong một khung hình khác chuyển động so với khung hình đầu tiên.
**Thí nghiệm tưởng tượng về đoàn tàu của Einstein:** Sét đánh vào cả hai đầu của một đoàn tàu đang chuyển động. Một người quan sát trên sân ga coi chúng là đồng thời. Một người quan sát trên tàu (di chuyển về phía một đòn tấn công) nhìn thấy đòn tấn công phía trước trước.
**Kết luận:** "Đồng thời" không phải là tuyệt đối — nó phụ thuộc vào hệ quy chiếu của người quan sát.
---

## Cộng vận tốc
Vận tốc không chỉ đơn giản thêm vào thuyết tương đối đặc biệt.
### Cộng vận tốc tương đối tính
Nếu một vật chuyển động với vận tốc u' trong hệ quy chiếu S', và S' chuyển động với vận tốc v so với S:
u = (u' + v) / (1 + u'v/c²)
| Kịch bản | Kết quả |
|----------|--------|
| u' = c (ánh sáng) | u = c (tốc độ ánh sáng là bất biến) |
| u', v ≪ c | u ≈ u' + v (rút gọn về phép cộng Galilê) |
| u' = 0,9c, v = 0,9c | u = 0,9945c (không bao giờ vượt quá c) |
---

## Tương đương khối lượng-năng lượng
E = mc2
| Khái niệm | Công thức | Ý nghĩa |
|----------|----------|---------|
| Nghỉ ngơi năng lượng | E₀ = mc2 | Năng lượng của khối lượng đứng yên |
| Tổng năng lượng | E = γmc2 | Bao gồm động năng |
| Động năng | KE = (γ − 1)mc2 | Giảm xuống ½mv² cho v ≪ c |
| Động lượng-năng lượng | E2 = (pc)2 + (mc2)2 | Mối quan hệ năng lượng-động lượng tương đối tính |
| Hạt không khối lượng | E = máy tính | Photon có năng lượng và động lượng nhưng không có khối lượng nghỉ |
### Ví dụ về năng lượng hạt nhân
| Phản ứng | Khiếm khuyết hàng loạt | Năng lượng được giải phóng |
|----------|-------------|--------|
| Phân hạch U-235 | 0,1% khối lượng | ~200 MeV mỗi lần phân hạch |
| Hợp nhất D-T | 0,7% khối lượng | 17,6 MeV mỗi phản ứng |
| Vật chất-phản vật chất | 100% khối lượng | 2mc² (chuyển đổi hoàn chỉnh) |
---

## Bốn vectơ và Không thời gian
### Không thời gian Minkowski
Thuyết tương đối hẹp hợp nhất không gian và thời gian thành 4D **Không thời gian Minkowski** với tọa độ (ct, x, y, z).
### Khoảng thời gian không gian
ds2 = −c2dt2 + dx2 + dy2 + dz2
| Loại khoảng | Tình trạng | Ý nghĩa |
|--------------|-------------|---------|
| **Vượt thời gian** | ds²< 0 | Events can be causally connected |
| **Lightlike (null)** | ds² = 0 | Connected by a light signal |
| **Spacelike** | ds² >0 | Các sự kiện không thể ảnh hưởng lẫn nhau |
Khoảng không thời gian là **bất biến** — tất cả những người quan sát đều đồng ý về giá trị của nó.
### Bốn vectơ
| Bốn Vector | Linh kiện | Số lượng bất biến |
|-------------|-------------|-------------------|
| Vị trí | (ct, x, y, z) | Khoảng thời gian |
| Vận tốc | γ(c, vₓ, vᵧ, v_z) | Thời điểm thích hợp |
| Động lực | (E/c, pₓ, pᵧ, p_z) | Khối lượng nghỉ: m2c2 = E2/c2 − p2 |
| Lực lượng | dP/dτ | Tăng tốc hợp lý |
---

## Giới thiệu về Thuyết tương đối rộng
### Nguyên tắc tương đương
| Phiên bản | Tuyên bố |
|----------|----------|
| **Yếu** | Khối lượng hấp dẫn = khối lượng quán tính (mọi vật rơi với tốc độ như nhau) |
| **Einstein** | Một hệ quy chiếu gia tốc đều không thể phân biệt được cục bộ với trường hấp dẫn |
| **Mạnh** | Tất cả các định luật vật lý (không chỉ cơ học) đều giống nhau cục bộ trong một hệ quy chiếu rơi tự do |
### Trọng lực như Không thời gian cong
Ý tưởng trung tâm của thuyết tương đối rộng: không thời gian cong khối lượng và năng lượng, và các vật thể đi theo những đường thẳng nhất có thể (trắc địa) thông qua không thời gian cong.
**Phương trình trường Einstein:**
G_μν + Λg_μν = (8πG/c⁴) T_μν
| Biểu tượng | Ý nghĩa |
|--------|----------|
| G_μν | Tensor Einstein (mã hóa độ cong không thời gian) |
| Λ | Hằng số vũ trụ (năng lượng tối) |
| g_μν | Tenxơ hệ mét (mô tả hình học của không thời gian) |
| G | Hằng số hấp dẫn Newton |
| T_μν | Tensor ứng suất-năng lượng (hàm lượng vật chất và năng lượng) |
**Tóm tắt của John Wheeler:** "Không thời gian cho biết vật chất chuyển động như thế nào; vật chất cho không thời gian biết đường cong."
### Dự đoán về thuyết tương đối rộng
| Dự đoán | Mô tả | Đã xác nhận? |
|----------|-------------|-------------|
| Sự giãn nở thời gian hấp dẫn | Đồng hồ chạy chậm hơn trong trường hấp dẫn mạnh hơn | Có (GPS yêu cầu hiệu chỉnh) |
| Thấu kính hấp dẫn | Ánh sáng uốn cong xung quanh các vật thể có khối lượng lớn | Có (Eddington 1919, hình ảnh Hubble) |
| Dịch chuyển đỏ hấp dẫn | Ánh sáng mất năng lượng khi leo ra khỏi giếng trọng lực | Có (Pound-Rebka 1959) |
| Lỗ đen | Các khu vực có độ cong không thời gian ngăn ánh sáng thoát ra | Có (LIGO, EHT 2019) |
| Sóng hấp dẫn | Những gợn sóng trong không thời gian do khối lượng gia tốc | Có (LIGO 2015) |
| Tuế sai điểm cận nhật của sao Thủy | Thêm 43 cung giây mỗi thế kỷ | Có (giải thích sự bất thường từ năm 1859) |
| Kéo khung | Khối lượng quay kéo không thời gian xung quanh chúng | Có (Đầu dò trọng lực B 2011) |
### Số liệu Schwarzschild
Giải pháp lỗ đen đơn giản nhất (không quay, không tích điện):
ds 2 = −(1 − 2GM/rc 2)c 2GM/rc 2
**Bán kính Schwarzschild:** r_s = 2GM/c²
| Đối tượng | Thánh lễ | r_s |
|--------|------|------|
| Trái đất | 6 × 102⁴ kg | 9 mm |
| Mặt trời | 2 × 10³⁰ kg | 3 km |
| Sgr A* (Trung tâm Dải Ngân Hà) | 4 × 10⁶ M☉ | 12 triệu km |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm tương đối | Ứng dụng |
|-------------------|-------------|
| Phép biến đổi Lorentz | Mạng nơ-ron tương đương Lorentz, mô hình nhận biết đối xứng |
| Hình học không thời gian | Học sâu hình học, học đa dạng |
| Bốn vectơ | Ký hiệu tensor được sử dụng trong mô phỏng vật lý tương đối tính |
| Sự giãn nở thời gian hấp dẫn | Chỉnh sửa GPS (dịch vụ dựa trên vị trí, ML không gian địa lý) |
| Thấu kính hấp dẫn | Phân tích dữ liệu thiên văn, lập bản đồ vật chất tối |
| Thuyết tương đối rộng | Mạng lưới thần kinh thông tin vật lý để phát hiện sóng hấp dẫn |
| Hình học Riemannian | Giảm độ dốc tự nhiên (hình học thông tin), tối ưu hóa đa dạng |
| Tenxơ hệ mét | Xác định khoảng cách trong không gian cong — cơ bản cho việc học đa dạng |
| Trắc địa | Đường đi ngắn nhất trên đa tạp - được sử dụng trong chế tạo robot, nhúng đồ thị |
| Phép tính tenxơ | Nền tảng để hiểu đa tạp dữ liệu chiều cao |
---

## Bản tóm tắt
| Khái niệm | Ý tưởng cốt lõi | Phương trình khóa |
|----------|-------------|-------------|
| Thuyết tương đối đặc biệt | Không gian và thời gian được thống nhất; c là tuyệt đối | Phép biến đổi Lorentz |
| Sự giãn nở thời gian | Đồng hồ chuyển động chạy chậm | Δt = γΔt₀ |
| Co chiều dài | Đối tượng chuyển động rút ngắn | L = L₀/γ |
| Năng lượng khối lượng | Khối lượng và năng lượng tương đương | E = mc2 |
| Bốn vectơ | Mô tả không thời gian thống nhất | Khoảng bất biến ds² |
| Nguyên lý tương đương | Trọng lực = gia tốc cục bộ | Nền tảng của GR |
| Thuyết tương đối rộng | Lực hấp dẫn là không thời gian bị cong | G_μν = (8πG/c⁴)T_μν |
| Trắc địa | Các vật thể đi theo đường thẳng nhất trong không thời gian cong | Đường đi ngắn nhất trên đa tạp |
Thuyết tương đối đã định hình lại sự hiểu biết của chúng ta về những khía cạnh cơ bản nhất của thực tế - không gian, thời gian, khối lượng, năng lượng và trọng lực. Các công cụ toán học của nó — tensor, đa tạp, trắc địa, không gian số liệu — đã vượt xa vật lý sang học máy, nơi chúng cung cấp năng lượng cho việc học sâu hình học, phương pháp gradient tự nhiên và thuật toán học đa dạng.