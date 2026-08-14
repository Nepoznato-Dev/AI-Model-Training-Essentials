---
# Metadata
title: "Abstract Algebra"
description: "Groups, subgroups, homomorphisms, rings, fields, vector spaces, linear maps, eigen theory, and applications in coding theory and quantum computing"
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
    changes: "Initial deep-dive into abstract algebra"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [abstract-algebra, groups, rings, fields, vector-spaces, linear-maps, eigen-theory, coding-theory, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Đại số trừu tượng
Đại số trừu tượng nghiên cứu các cấu trúc đại số - các bộ được trang bị các phép toán tuân theo các quy tắc cụ thể. Thay vì làm việc với các con số, đại số trừu tượng làm việc với bất kỳ đối tượng nào thỏa mãn các tiên đề. Tính tổng quát này rất mạnh mẽ: một định lý đã được chứng minh cho "nhóm" áp dụng đồng thời cho các số nguyên, đối xứng, ma trận, hoán vị và trạng thái lượng tử. Đại số trừu tượng làm nền tảng cho mật mã, mã sửa lỗi, điện toán lượng tử và phân tích đối xứng được sử dụng trong vật lý.
---

## Nhóm
**nhóm** là cấu trúc đại số cơ bản nhất. Nó nắm bắt được bản chất của sự đối xứng.
### Sự định nghĩa
**nhóm** (G, ∗) là tập G có phép toán nhị phân ∗ thỏa mãn:
| tiên đề | Tuyên bố | Ví dụ (ℤ, +) |
|-------|-------------|--------|
| **Đóng cửa** | ∀a,b ∈ G: a ∗ b ∈ G | a + b là số nguyên |
| **Tính liên kết** | (a ∗ b) ∗ c = a ∗ (b ∗ c) | (a + b) + c = a + (b + c) |
| **Danh tính** | ∃e ∈ G: e ∗ a = a ∗ e = a | 0 + a = a + 0 = a |
| **Nghịch đảo** | ∀a ∈ G, ∃a⁻¹: a ∗ a⁻¹ = a⁻¹ ∗ a = e | a + (−a) = 0 |
Nếu phép toán cũng **giao hoán** (a ∗ b = b ∗ a), nhóm được gọi là **abelian**.
### Ví dụ về nhóm
| Nhóm | Đặt | Hoạt động | Bản sắc | Nghịch đảo | Abelian? |
|-------|------|-------------|----------|----------|----------|
| (ℤ, +) | Số nguyên | Ngoài ra | 0 | −a | Có |
| (ℚ*, ×) | Các số hữu tỉ khác 0 | Phép nhân | 1 | 1/a | Có |
| (ℤ/nℤ, +) | Dư lượng mod n | Mod bổ sung n | [0] | [n−a] | Có |
| Sₙ | Hoán vị của {1,...,n} | Thành phần | id | Hoán vị nghịch đảo | Không (n ≥ 3) |
| GL(n, ℝ) | Ma trận n×n khả nghịch | Phép nhân ma trận | Tôiₙ | A⁻¹ | Không (n ≥ 2) |
| (ℝⁿ, +) | vectơ n chiều | Phép cộng vector | 0 | −v | Có |
### Thứ tự của một nhóm và các phần tử
| Kỳ hạn | Định nghĩa | Ví dụ |
|------|-------------|----------|
| **Bậc G** (\|G\|) | Số phần tử trong G | \|ℤ/5ℤ\| = 5 |
| **Thứ tự của phần tử a** (ord(a)) | k dương nhỏ nhất với aᵏ = e | ord(2) trong (ℤ/7ℤ)* = 3 (vì 2³ = 8 ≡ 1) |
| **Nhóm hữu hạn** | \|G\| là hữu hạn | S₃ có đơn hàng 6 |
| **Nhóm vô hạn** | \|G\| là vô hạn | (ℤ, +) |
### Nhóm con
**Nhóm con** H của G là tập con H ⊆ G mà bản thân nó là một nhóm trong cùng một phép toán.
**Kiểm tra nhóm con:** H là nhóm con của G iff:
1. H không trống
2. Với mọi a, b ∈ H: a ∗ b⁻¹ ∈ H
**Ví dụ:**
- (ℤ, +) có các nhóm con nℤ = {..., −2n, −n, 0, n, 2n, ...} với mỗi n ≥ 0
- **Nhóm con tầm thường** {e} và nhóm G luôn là nhóm con
- Trong S₃ tập {id, (12)} là nhóm con cấp 2
### Cosets và Định lý Lagrange
Đối với nhóm con H của G và phần tử a ∈ G:
- **Vỏ bọc bên trái:** aH = {ah : h ∈ H}
- **Vỏ phải:** Ha = {ha : h ∈ H}
**Định lý Lagrange:** Đối với nhóm hữu hạn G và nhóm con H:
|H| chia |G|
**Hệ quả:**
- Thứ tự các phần tử chia |G|
- Nếu |G| = p (nguyên tố) thì G là tuần hoàn (không có nhóm con không tầm thường)
- a^|G| = e với mọi a ∈ G (tổng quát hóa Định lý nhỏ Fermat)
### Nhóm tuần hoàn
Một nhóm G là **tuần hoàn** nếu tồn tại g ∈ G sao cho mọi phần tử của G đều là lũy thừa của g. Chúng ta viết G = ⟨g⟩.
| Bất động sản | Tuyên bố |
|----------|----------|
| Mọi nhóm tuần hoàn đều là nhóm abelian | — |
| ℤ/nℤ dưới phép cộng có tính tuần hoàn | Được tạo bởi [1] |
| (ℤ/pℤ)* là tuần hoàn cho số nguyên tố p | Trình tạo được gọi là gốc nguyên thủy |
| Phân loại | Mọi nhóm tuần hoàn hữu hạn đều đẳng cấu với ℤ/nℤ với một số n |
---

## Đồng cấu và đẳng cấu
**đồng hình** là bản đồ bảo toàn cấu trúc giữa các nhóm.
### Định nghĩa
| Kỳ hạn | Định nghĩa | Ví dụ |
|------|-------------|----------|
| **Đồng cấu** | φ: G → H trong đó φ(ab) = φ(a)φ(b) | det: GL(n,ℝ) → ℝ* |
| **Đẳng cấu** | Một sự đồng hình tính từ (các nhóm "giống nhau") | (ℤ/6ℤ) ≅ (ℤ/2ℤ) × (ℤ/3ℤ) |
| **Hạt nhân** | ker(φ) = {g ∈ G : φ(g) = e_H} | ker(det) = SL(n, ℝ) |
| **Hình ảnh** | im(φ) = {φ(g) : g ∈ G} | im(det) = ℝ* |
### Định lý đẳng cấu thứ nhất
Nếu φ: G → H là đồng cấu thì:
G / ker(φ) ≅ im(φ)
Đây là một trong những định lý quan trọng nhất trong đại số - nó nói rằng mọi phép đồng cấu đều phân tách thành một thương số theo sau là một phép đẳng cấu.
---

## Nhẫn
**ring** thêm phép toán thứ hai vào một nhóm, mô hình hóa số học với cả phép cộng và phép nhân.
### Sự định nghĩa
Một **ring** (R, +, ×) là một tập R có hai phép toán thỏa mãn:
| tiên đề | Tuyên bố |
|-------|----------|
| (R, +) là nhóm Abel | Phép cộng có tính giao hoán, kết hợp, có đơn vị 0, mọi phần tử đều có phép cộng nghịch đảo |
| Phép nhân có tính kết hợp | (a × b) × c = a × (b × c) |
| Luật phân phối | a(b + c) = ab + ac và (a + b)c = ac + bc |
Nếu phép nhân cũng có tính giao hoán và có đẳng thức (1) thì R là **vành giao hoán có đơn vị**.
### Ví dụ về Nhẫn
| Nhẫn | Mô tả | Giao hoán? | Có 1? |
|------|-------------|-------------|--------|
| (ℤ, +, ×) | Số nguyên | Có | Có |
| (ℚ, +, ×) | Lý lẽ | Có | Có |
| (ℝ, +, ×) | Số thực | Có | Có |
| (ℤ/nℤ, +, ×) | Số nguyên mod n | Có | Có |
| Mₙ(ℝ) | ma trận thực n×n | Không (n ≥ 2) | Có |
| ℝ[x] | Đa thức có hệ số thực | Có | Có |
### Nhẫn lý tưởng và nhẫn thương
Một **lý tưởng** I của vành R là tập con:
1. Là nhóm con được phép cộng
2. Hấp thụ phép nhân: với mọi r ∈ R và a ∈ I, cả ra ∈ I và ar ∈ I
**Vòng thương** R/I: các phần tử là các tập hợp của I, với các phép toán kế thừa từ R.
**Ví dụ:** ℤ/nℤ = ℤ/nℤ là thương của ℤ với lý tưởng nℤ.
### Tên miền và trường tích hợp
| Cấu trúc | Định nghĩa | Ví dụ |
|----------||-------------|----------|
| **Miền tích hợp** | Vành giao hoán có 1, không có ước số 0 (ab = 0 → a = 0 hoặc b = 0) | ℤ, ℚ[x], ℝ[x] |
| **Trường** | Vành giao hoán trong đó mọi phần tử khác 0 đều có số nghịch đảo | ℚ, ℝ, ℂ, ℤ/pℤ (p nguyên tố) |
---

## Trường
Trường là đối tượng đại số có cấu trúc nhất được sử dụng phổ biến. Mọi phần tử khác 0 đều có thể được cộng, trừ, nhân và chia.
### Thuộc tính chính
| Bất động sản | Tuyên bố |
|----------|----------|
| Mọi trường đều là một miền nguyên | — |
| Mọi miền tích phân hữu hạn đều là một trường | — |
| Đặc trưng | N nhỏ nhất với n·1 = 0, hoặc 0 nếu không tồn tại n |
| char(ℚ) = char(ℝ) = char(ℂ) | = 0 |
| char(ℤ/pℤ) | = p (đối với p nguyên tố) |
### Trường hữu hạn (Trường Galois)
Với mọi lũy thừa nguyên tố pᵏ, tồn tại một trường hữu hạn duy nhất (lên đến đẳng cấu) cấp pᵏ, ký hiệu là GF(pᵏ) hoặc 𝔽_{pᵏ}.
| Lĩnh vực | Kích thước | Xây dựng | Ứng dụng |
|-------|------|-------------|-------------|
| GF(2) | 2 | {0, 1} mod 2 | Số học nhị phân, XOR |
| GF(2ᵏ) | 2ᵏ | Đa thức mod đa thức tối giản trên GF(2) | Mã hóa AES, mã CRC |
| GF(p) | p | ℤ/pℤ cho số nguyên tố p | Số học mô-đun, lý thuyết mã hóa |
| GF(pᵏ) | pᵏ | Trường mở rộng | Mã Reed-Solomon, đường cong elip |
**Cấu trúc của GF(2⁸)** (được sử dụng trong AES):
- Bắt đầu với GF(2) = {0, 1}
- Chọn đa thức tối giản p(x) = x⁸ + x⁴ + x³ + x + 1 trên GF(2)
- Các phần tử là đa thức bậc < 8 có hệ số trong GF(2)
- Số học: phép cộng đa thức (XOR) và phép nhân mod p(x)
---

## Không gian vectơ
**Không gian vectơ** là một tập hợp các vectơ có thể được cộng và chia tỷ lệ, tạo thành nền tảng của đại số tuyến tính.
### Sự định nghĩa
**Không gian vectơ** V trên trường F là một tập hợp có:
- Phép cộng vectơ: V × V → V (làm cho V thành nhóm abelian)
- Phép nhân vô hướng: F × V → V
Thỏa mãn: tính kết hợp, tính giao hoán của phép cộng, tính phân phối của phép nhân vô hướng và 1·v = v.
### Các khái niệm chính
| Khái niệm | Định nghĩa | Ví dụ |
|----------|-------------|----------|
| **Cơ sở** | Tập bao trùm độc lập tuyến tính | {e₁, e₂, ..., eₙ} cho Fⁿ |
| **Kích thước** | Số vectơ trong cơ sở bất kỳ | mờ(ℝ³) = 3 |
| **Không gian con** | Tập hợp con khép kín dưới phép cộng và nhân vô hướng | Một mặt phẳng đi qua gốc tọa độ ở ℝ³ |
| **Kết hợp tuyến tính** | Σ cᵢvᵢ trong đó cᵢ ∈ F | 3v₁ + 2v₂ − v₃ |
| **Khoảng cách** | Tập hợp tất cả các kết hợp tuyến tính | Span({v₁, v₂}) = mặt phẳng nếu v₁, v₂ độc lập |
| **Độc lập tuyến tính** | Không có vectơ nào là sự kết hợp tuyến tính của các vectơ khác | e₁, e₂, e₃ ở ℝ³ |
### Các không gian vectơ quan trọng
| Không gian | Mô tả | Kích thước |
|-------|-------------|----------|
| Fⁿ | n-tuple trên trường F | n |
| Pₙ(F) | Đa thức bậc ≤ n | n + 1 |
| Mₘₓₙ(F) | ma trận m × n trên F | mn |
| C[a,b] | Hàm liên tục trên [a,b] | Vô hạn |
| L²(ℝ) | Hàm tích phân vuông | Vô hạn (Không gian Hilbert) |
---

## Bản đồ tuyến tính và lý thuyết riêng
### Bản đồ tuyến tính
Một **bản đồ tuyến tính** (biến đổi tuyến tính) T: V → W thỏa mãn:
- T(u + v) = T(u) + T(v)
- T(cv) = cT(v) với mọi đại lượng vô hướng c
| Khái niệm | Định nghĩa | Ví dụ |
|----------|-------------|----------|
| **Hạt nhân** | {v ∈ V : T(v) = 0} | Không gian rỗng của ma trận |
| **Hình ảnh** | {T(v) : v ∈ V} | Không gian cột của ma trận |
| **Định lý vô hiệu cấp bậc** | dim(ker T) + dim(im T) = dim(V) | Ràng buộc cơ bản |
| **Biểu diễn ma trận** | T(v) = Av đối với ma trận A nào đó | Mọi ánh xạ tuyến tính giữa các không gian hữu hạn chiều |
### Giá trị riêng và vectơ riêng
Đối với bản đồ tuyến tính T: V → V (hoặc ma trận A):
**Phương trình giá trị riêng:** Av = λv, trong đó v ≠ 0
| Kỳ hạn | Định nghĩa |
|------|-------------|
| **Giá trị riêng** λ | Vô hướng sao cho Av = λv với một số v ≠ 0 |
| **Véc tơ riêng** v | Vectơ khác 0 thỏa mãn Av = λv |
| **Đa thức đặc trưng** | det(A − λI) = 0 |
| **Không gian riêng** | {v : Av = λv} — tập hợp tất cả các vectơ riêng của λ (cộng 0) |
| **Phổ** | Tập hợp tất cả các giá trị riêng |
### Tính giá trị riêng
Đối với ma trận 2×2 A = [[a, b], [c, d]]:
- Đa thức đặc trưng: λ² − (a+d)λ + (ad−bc) = 0
- λ = ((a+d) ± √((a+d)² − 4(ad−bc))) / 2
**Thuộc tính chính:**
- Tổng các giá trị riêng = trace(A) = tổng các phần tử đường chéo
- Tích các giá trị riêng = det(A)
### Đường chéo
Ma trận A **có thể chéo** nếu nó có n vectơ riêng độc lập tuyến tính (trong đó A là n×n).
Nếu A = PDP⁻¹ trong đó D là đường chéo:
- Aᵏ = PDᵏP⁻¹ (lũy thừa ma trận nhanh)
- D chứa các giá trị riêng trên đường chéo
- P chứa các vectơ riêng dạng cột
**Định lý phổ:** Mọi ma trận đối xứng thực đều có thể chéo hóa được bằng một ma trận trực giao. Các giá trị riêng của nó là thực.
---

## Ứng dụng
### Lý thuyết mã hóa (Mã sửa lỗi)
Các trường hữu hạn là nền tảng của mã sửa lỗi hiện đại.
| Mã | Lĩnh vực | Sửa chữa | Ứng dụng |
|------|-------|----------|-------------|
| Mã Hamming | GF(2) | 1 lỗi mỗi khối | RAM ECC, kết nối mạng sớm |
| Sậy-Solomon | GF(2ᵏ) | Nhiều lỗi | CD, DVD, mã QR, thông tin vệ tinh |
| Mã BCH | GF(2ᵏ) | Nhiều lỗi | Bộ nhớ flash, vệ tinh |
| Mã LDPC | GF(2) | Nhiều lỗi | Wi-Fi (802.11n), DVB-S2, 5G |
**Mã hóa Reed-Solomon:** Xử lý dữ liệu dưới dạng đa thức trên GF(2ᵏ), đánh giá ở một số điểm. Ngay cả khi một số đánh giá bị sai, đa thức ban đầu vẫn có thể được phục hồi.
### Điện toán lượng tử
Các trạng thái lượng tử tồn tại trong các không gian vectơ phức tạp (không gian Hilbert). Cổng lượng tử là ma trận đơn nhất.
| Khái niệm lượng tử | Cấu trúc đại số |
|----------------|-------------------|
| Qubit | Vectơ đơn vị tính bằng ℂ² (không gian vectơ 2D phức tạp) |
| Cổng lượng tử | Ma trận đơn nhất U ∈ U(2ⁿ) |
| Đo lường | Toán tử chiếu |
| Sự vướng víu | Trạng thái tích tensor không thể tách rời |
| Định lý không nhân bản | Không có bản đồ tuyến tính nào có thể sao chép một trạng thái lượng tử chưa biết |
**Cổng qubit đơn:**
| Cổng | Ma trận | Hiệu ứng |
|------|--------|--------|
| Pauli-X (KHÔNG) | [[0,1],[1,0]] | lật bit |
| Pauli-Z | [[1,0],[0,−1]] | Lật pha |
| Hadamard | (1/√2)[[1,1],[1,−1]] | Tạo sự chồng chất |
| CNOT | Cổng điều khiển 4×4 | Làm vướng víu hai qubit |
### Mật mã
| Ứng dụng | Đại số được sử dụng |
|-------------|-------------|
| RSA | Nhóm nhân (ℤ/nℤ)* |
| Mật mã đường cong Elliptic | Nhóm điểm trên đường cong elip trên trường hữu hạn |
| AES | Số học trong GF(2⁸) |
| Diffie-Hellman | Nhóm con tuần hoàn của (ℤ/pℤ)* hoặc nhóm đường cong elip |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái Niệm Đại Số | Ứng dụng |
|-------|-------------|
| Không gian vectơ | Không gian đặc trưng, ​​​​không gian nhúng, học cách biểu diễn |
| Bản đồ tuyến tính | Các lớp mạng thần kinh (y = Wx + b), giảm kích thước |
| Giá trị riêng/vectơ | PCA, phân cụm quang phổ, PageRank, phân tích độ ổn định |
| Phân rã ma trận | SVD, phân tách riêng để nén mô hình |
| Trường hữu hạn | Mã sửa lỗi để lưu trữ/truyền dữ liệu đáng tin cậy |
| Lý thuyết nhóm | Tính đối xứng trong vật lý (định luật bảo toàn), tăng dữ liệu (quay, phản xạ) |
| Sản phẩm Tenor | Học tập đa phương thức, điện toán lượng tử, cơ chế chú ý |
| Vành và đa thức | Phương pháp hạt nhân, bản đồ đặc trưng đa thức |
---

## Bản tóm tắt
| Cấu trúc | Hoạt động | Thuộc tính chính | Ví dụ |
|----------||----------||--------------|--------|
| Nhóm | Một (∗) | Đóng cửa, kết hợp, nhận dạng, nghịch đảo | (ℤ, +), Sₙ |
| Nhẫn | Hai (+, ×) | Nhóm Abel dưới +, monoid dưới ×, phân phối | ℤ, ℤ/nℤ, Mₙ(ℝ) |
| Lĩnh vực | Hai (+, ×) | Đổ chuông nơi các phần tử khác 0 tạo thành một nhóm dưới × | ℚ, ℝ, ℂ, GF(p) |
| Không gian vectơ | Phép cộng + vô hướng | Mô-đun trên một trường | ℝⁿ, Pₙ(F), không gian hàm |
Đại số trừu tượng cung cấp ngôn ngữ cho chính cấu trúc. Các nhóm nắm bắt tính đối xứng, các vòng nắm bắt số học, các trường nắm bắt phép chia và không gian vectơ nắm bắt tuyến tính. Những cấu trúc này không phải là trừu tượng — chúng xuất hiện trong mọi mã sửa lỗi để bảo vệ dữ liệu của bạn, mọi giao thức mật mã bảo vệ thông tin liên lạc của bạn, mọi thuật toán lượng tử mà một ngày nào đó có thể biến đổi điện toán và mọi phép biến đổi tuyến tính chạy qua mạng lưới thần kinh.