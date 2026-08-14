---
# Metadata
title: "Discrete Mathematics"
description: "Sets in depth, relations, functions, combinatorics, pigeonhole principle, recurrence relations, and generating functions"
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
    changes: "Initial deep-dive into discrete mathematics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [discrete-mathematics, set-theory, relations, combinatorics, pigeonhole-principle, recurrence-relations, generating-functions]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "../logic_and_critical_thinking.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Toán rời rạc
Toán học rời rạc là nghiên cứu về các cấu trúc toán học về cơ bản có thể đếm được hoặc tách rời - trái ngược với toán học liên tục (phép tính, giải tích thực), liên quan đến các đại lượng trơn tru, không bị gián đoạn. Toán rời rạc làm nền tảng cho khoa học máy tính, mật mã, thiết kế thuật toán và cấu trúc dữ liệu. Nếu toán liên tục mô tả thế giới vật chất thì toán rời rạc mô tả thế giới tính toán.
---

## Đặt lý thuyết chuyên sâu
Tập hợp là nền tảng xây dựng gần như toàn bộ toán học hiện đại. **bộ** là một tập hợp không có thứ tự của các đối tượng riêng biệt, được gọi là **phần tử** hoặc **thành viên**.
### Cơ sở tiên đề (ZFC)
Lý thuyết tập hợp hiện đại dựa trên **các tiên đề Zermelo-Fraenkel với Tiên đề Lựa chọn (ZFC)**. Những tiên đề này giải quyết những nghịch lý như Nghịch lý của Russell (“tập hợp tất cả các tập hợp không chứa chính chúng”) bằng cách hạn chế cách hình thành các tập hợp.
| tiên đề | Tuyên bố không chính thức |
|-------|----------------------|
| Tính mở rộng | Hai bộ bằng nhau nếu chúng có cùng các phần tử |
| Bộ trống | Tồn tại một tập hợp không có phần tử nào: ∅ |
| Ghép nối | Với mọi a, b, tồn tại {a, b} |
| Liên minh | Đối với bất kỳ họ tập hợp nào, hợp của chúng tồn tại |
| Bộ nguồn | Với mọi tập S, tập hợp tất cả các tập con của S tồn tại: P(S) |
| Vô cực | Tồn tại một tập vô hạn |
| Đặc điểm kỹ thuật | Với mọi tập A và tính chất P, tồn tại {x ∈ A : P(x)} |
| Thay thế | Ảnh của một tập hợp dưới một hàm xác định được là một tập hợp |
| Đều đặn | Mọi tập hợp không trống đều chứa một phần tử tách rời khỏi nó (ngăn cản tư cách thành viên) |
| Lựa chọn | Đối với bất kỳ họ tập hợp rời rạc theo cặp không trống nào, tồn tại một hàm lựa chọn |
### Số lượng và kích thước của bộ
**Hạt số** của một tập hợp, ký hiệu là |S|, đo lường "kích thước" của nó.
| Khái niệm | Định nghĩa | Ví dụ |
|----------|-------------|----------|
| Tập hữu hạn | Có số tự nhiên là số lượng | |{a, b, c}| = 3 |
| Đếm được vô hạn | Lực lượng tương tự như ℕ | ℤ, ℚ là vô hạn đếm được |
| Không đếm được | Lớn hơn ℕ | ℝ, P(ℕ), tập hợp tất cả các hàm ℕ → {0,1} |
| Định lý Cantor | Với mọi tập S, |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**Đối số đường chéo của Cantor** chứng minh rằng ℝ là không đếm được: giả sử bạn có thể liệt kê tất cả các số thực trong [0,1], sau đó xây dựng một số thực mới khác với số thực được liệt kê thứ n ở vị trí thập phân thứ n — mâu thuẫn.
### Thao tác trên tập hợp
| Hoạt động | Ký hiệu | Định nghĩa | Bất động sản |
|----------|----------|-------------|----------|
| Liên minh | A ∪ B | {x : x ∈ A hoặc x ∈ B} | Giao hoán, kết hợp |
| Giao lộ | A ∩ B | {x : x ∈ A và x ∈ B} | Giao hoán, kết hợp |
| Sự khác biệt | A \ B | {x : x ∈ A và x ∉ B} | Không giao hoán |
| Sự khác biệt đối xứng | A △ B | (A \ B) ∪ (B \ A) | Giao hoán, kết hợp |
| Bổ sung | Aᶜ | U \ A (trong đó U là tập phổ quát) | (Aᶜ)ᶜ = A |
| Sản phẩm Descartes | A × B | {(a,b): a ∈ A, b ∈ B} | |A × B| = |A| · |B| |
**Định luật De Morgan:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Nguyên lý bao hàm-loại trừ** (đối với tập hợp hữu hạn):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## Quan hệ
**quan hệ** R trên các tập A và B là tập con của A × B. Khi (a, b) ∈ R, chúng ta viết aRb.
### Các loại quan hệ
Mối quan hệ R trên tập A có thể có các tính chất sau:
| Bất động sản | Định nghĩa | Ví dụ |
|----------|-------------|----------|
| Phản xạ | ∀a ∈ A: aRa | ℤ trên ℤ |
| Không phản xạ | ∀a ∈ A: и(aRa) | < trên ℤ |
| Đối xứng | ∀a,b: aRb → bRa | = trên bất kỳ bộ nào |
| Phản đối xứng | ∀a,b: aRb ∧ bRa → a = b | ℤ trên ℤ |
| Chuyển tiếp | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = trên ℤ |
### Quan hệ tương đương
**Quan hệ tương đương** có tính phản xạ, đối xứng và bắc cầu. Nó phân chia một tập hợp thành các **lớp tương đương** rời rạc.
**Ví dụ:** Số học mô-đun. Xác định a ~ b iff a ≡ b (mod n). Các lớp tương đương là [0], [1], ..., [n−1], phân chia ℤ thành n lớp.
**Ví dụ đã làm:** Trên ℤ × ℤ, xác định (a,b) ~ (c,d) nếu a + d = b + c. Đây là một quan hệ tương đương. Lớp [(0,0)] = {(n,n): n ∈ ℤ}. Lớp [(1,0)] = {(n+1,n) : n ∈ ℤ}. Cấu trúc này thực sự xác định các số nguyên từ các số tự nhiên.
### Đơn đặt hàng một phần
**Trật tự một phần** có tính chất phản xạ, phản đối xứng và bắc cầu. Một tập hợp có thứ tự một phần được gọi là **tập hợp có thứ tự một phần (poset)**.
| Khái niệm | Định nghĩa | Ví dụ |
|----------|-------------|----------|
| Đặt ra | (S, ₫) với ∎ bậc một phần | (P(A), ⊆) — các tập con được sắp xếp theo thứ tự bao gồm |
| Chuỗi | Một tập hợp con được sắp xếp hoàn toàn | {∅, {a}, {a,b}} trong P({a,b,c}) |
| Chống chuỗi | Một tập hợp con không có hai phần tử nào có thể so sánh được | {{a}, {b}} trong P({a,b}) |
| Sơ đồ Hasse | Biểu diễn trực quan của một poset | Chỉ vẽ các cạnh để che các quan hệ |
| Giới hạn trên | Một phần tử ≥ mọi phần tử trong tập con | sup({2,3}) = 6 in (ℤ, \|) (chia hết) |
| Giới hạn trên tối thiểu (sup) | Giới hạn trên nhỏ nhất | sup({2,3}) trong (ℕ, ≤) là 3 |
| Giới hạn dưới lớn nhất (inf) | Giới hạn dưới lớn nhất | inf({4,6}) trong (ℕ, \|) là 2 |
---

## Chức năng
A **hàm** f: A → B gán cho mỗi phần tử của A chính xác một phần tử của B.
### Phân loại hàm
| Loại | Định nghĩa | Ví dụ |
|------|-------------|----------|
| Tiêm (một-một) | f(a) = f(b) → a = b | f(x) = 2x từ ℤ → ℤ |
| Tính từ (lên) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2 từ ℤ → {0,1} |
| Tính từ | Cả tính từ và tính từ | f(x) = x + 1 từ ℤ → ℤ |
### Các khái niệm chức năng quan trọng
| Khái niệm | Định nghĩa | Trường hợp sử dụng |
|----------|-------------|----------|
| Hàm nghịch đảo | f⁻¹ tồn tại nếu f là tính từ | Giải mã dữ liệu được mã hóa |
| Thành phần | (g ∘ f)(x) = g(f(x)) | Chuỗi biến đổi |
| Chức năng nhận dạng | id(x) = x | Yếu tố trung tính cho bố cục |
| Điểm cố định | f(x) = x | Định nghĩa đệ quy, ngữ nghĩa |
| Hoán vị | Lời từ chối từ một tập hợp đến chính nó | Sắp xếp lại dữ liệu, xáo trộn |
### Chức năng đếm
Cho các tập hữu hạn |A| = m và |B| = n:
| Loại | Đếm |
|------|-------|
| Tất cả các chức năng A → B | nᵐ |
| Hàm tiêm | N! / (n−m)! (nếu n ≥ m thì khác 0) |
| Hàm tính từ | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (bằng cách bao gồm-loại trừ) |
| Hàm tính từ | N! (khi m = n) |
---

## Tổ hợp
Tổ hợp là toán học đếm, sắp xếp và lựa chọn.
### Nguyên tắc tính cơ bản
| Nguyên tắc | Tuyên bố | Ví dụ |
|----------|-------------|----------|
| Quy Tắc Tổng | Nếu A và B rời nhau, |A ∪ B| = |A| + |B| | Chọn một loại trái cây: 3 quả táo + 4 quả cam = 7 lựa chọn |
| Quy tắc sản phẩm | |A × B| = |A| · |B| | Trang phục: 3 áo × 4 quần = 12 bộ trang phục |
| Quy tắc song ánh | Nếu f: A → B là song ánh, |A| = |B| | Đếm các tập hợp con bằng cách đếm chuỗi nhị phân |
| Bổ sung | |A| = |U| − |Aᶜ| | Đếm tổng cộng "ít nhất một" trừ "không" |
### Hoán vị và kết hợp
| Ký hiệu | Tên | Công thức | Ý nghĩa |
|----------|------|----------|--------|
| C(n,k) hoặc (nk) | Hệ số nhị thức | N! / (k!(n−k)!) | Cách chọn k mục từ n (thứ tự không quan trọng) |
| P(n, k) | hoán vị k của n | N! / (n−k)! | Cách sắp xếp k mục từ n (thứ tự quan trọng) |
| N! | Giai thừa | n × (n−1) × ... × 1 | Cách sắp xếp tất cả n mục |
| (n k) với sự lặp lại | Chọn nhiều | C(n+k−1, k) | Chọn k từ n với phép lặp lại |
**Định lý nhị thức:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Đương thức Pascal:** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Nguyên lý chuồng bồ câu
**Dạng cơ bản:** Nếu đặt n+1 đồ vật vào n hộp thì ít nhất một hộp chứa ≥ 2 đồ vật.
**Dạng tổng quát:** Nếu N đồ vật được đặt vào k hộp thì ít nhất một hộp chứa ≥ ⌈N/k⌉ đồ vật.
**Ví dụ đã hoạt động:**
1. Trong 13 người bất kỳ, có ít nhất 2 người có cùng tháng sinh. (13 người, 12 tháng → chuồng bồ câu.)
2. Chứng minh rằng trong 5 số nguyên bất kỳ luôn tồn tại 3 số có tổng chia hết cho 3.
   - Xét thặng dư mod 3: {0, 1, 2}. Với 5 số nguyên và 3 lớp dư lượng, theo chuồng bồ câu tổng quát, ít nhất ⌈5/3⌉ = 2 chia sẻ một phần dư.
   - Nếu 3 có chung dư r: tổng của chúng ≡ 3r ≡ 0 (mod 3).
   - Nếu 2 phần dư 0 và 2 phần dư 1: chọn một trong mỗi cặp cộng với phần tử dư 0 → tổng ≡ 0 (mod 3).
3. **Ứng dụng trong CS:** Bất kỳ thuật toán nén không mất dữ liệu nào cũng phải mở rộng một số đầu vào. (Nếu mỗi chuỗi n-bit được nén thành < n bit, bạn sẽ ánh xạ 2ⁿ chuỗi thành ít hơn 2ⁿ chuỗi nén — vi phạm tính tiêm.)
### Số Catalan
Số thứ n **Số Catalan** Cₙ = C(2n, n) / (n+1) được tính:
| Cấu trúc | Ví dụ |
|----------||----------|
| Chuỗi dấu ngoặc hợp lệ | ()(), (()) với n = 2 |
| Cây nhị phân có n nút bên trong | 2 cây cho n = 2 |
| Đường dẫn không cắt nhau | Đường dẫn lưới từ (0,0) đến (n,n) nằm dưới y = x |
| Tam giác của đa giác | Cách chia (n+2)-giác thành tam giác |
Một số đầu tiên: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Tái diễn: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Quan hệ tái diễn
**Mối quan hệ lặp lại** xác định mỗi thuật ngữ của một chuỗi là một hàm của các thuật ngữ trước đó.
### Loại và giải pháp
| Loại | Mẫu | Phương pháp giải |
|------|------|-----------------|
| Tuyến tính đồng nhất (hệ số không đổi) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Phương trình đặc trưng |
| Tuyến tính không đồng nhất | aₙ = c₁aₙ₋₁ + ... + f(n) | Giải pháp đặc biệt + giải pháp đồng nhất |
| Chia rẽ và chinh phục | T(n) = aT(n/b) + f(n) | Định lý tổng thể |
### Phương pháp phương trình đặc trưng
Với aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, hãy lập phương trình đặc trưng:
r² − c₁r − c₂ = 0
| Trường hợp | Rễ | Giải pháp chung |
|------|-------|-------------------|
| Hai nghiệm thực riêng biệt r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Gốc lặp đi lặp lại r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Các nghiệm phức α ± βi | Chuyển đổi sang cực: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |
**Ví dụ đã thực hiện:** Chuỗi Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Phương trình đặc trưng: r² − r − 1 = 0
- Nghiệm: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1.618, ψ = (1−√5)/2 ≈ −0.618
- Giải tổng quát: Fₙ = A·φⁿ + B·ψⁿ
- Từ điều kiện ban đầu: A = 1/√5, B = −1/√5
- **Dạng đóng:** Fₙ = (φⁿ − ψⁿ) / √5 (công thức Binet)
### Định lý tổng thể
Đối với các phép truy toán có dạng T(n) = aT(n/b) + f(n) trong đó a ≥ 1, b > 1:
Đặt c = log_b(a).
| Trường hợp | Tình trạng | Giải pháp |
|------|-------------|----------|
| 1 | f(n) = O(nᵈ) trong đó d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c và af(n/b) ≤ kf(n) với một số k < 1 | T(n) = Θ(nᵈ) |
**Ví dụ:**
- Sắp xếp hợp nhất: T(n) = 2T(n/2) + O(n). Ở đây a=2, b=2, c=1, f(n)=n=Θ(n¹). Trường hợp 2: T(n) = Θ(n log n).
- Tìm kiếm nhị phân: T(n) = T(n/2) + O(1). Ở đây a=1, b=2, c=0, f(n)=1=Θ(n⁰). Trường hợp 2: T(n) = Θ(log n).
---

## Tạo hàm
**Hàm tạo** mã hóa một chuỗi (aₙ) dưới dạng hệ số của chuỗi lũy thừa hình thức.
### Các loại
| Loại | Mẫu | Trường hợp sử dụng |
|------|------|----------|
| Thông thường (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Cấu trúc, tác phẩm không ghi nhãn |
| Hàm mũ (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Cấu trúc được gắn nhãn, hoán vị |
### Các hàm tạo thông dụng
| Trình tự aₙ | OGF G(x) |
|-------------|-------------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r2, r³, ... | 1/(1−rx) |
| C(n,k) cho k cố định | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Tiếng Catalan Cₙ | (1 − √(1−4x)) / (2x) |
### Sử dụng hàm sinh để giải quyết các lần lặp lại
**Ví dụ đã thực hiện:** Giải aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Đặt G(x) = Σ aₙxⁿ.
2. Từ phép truy hồi: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Thay thế: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Phân số riêng: G(x) = 2/(1−2x) − 1/(1−x)
7. Hệ số trích xuất: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Xác minh:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Kiểm tra: 3(3) − 2(1) = 7.
---

## Đại số Boolean và Logic mệnh đề
Đại số Boolean là đại số của hai giá trị chân lý: **Đúng (1)** và **Sai (0)**. Nó là nền tảng toán học của các mạch kỹ thuật số, truy vấn cơ sở dữ liệu và các điều kiện lập trình.
### Hoạt động và Luật
| Hoạt động | Biểu tượng | Ý nghĩa | Bảng Sự Thật |
|----------|----------|---------|-------------|
| VÀ | p ∧ q | Chỉ đúng khi cả hai đều đúng | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| HOẶC | p ∨ q | Đúng khi có ít nhất một giá trị đúng | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| KHÔNG | Âp | Phủ định | ¨T=F, ÂF=T |
| XOR | p ⊕ q | Đúng khi có chính xác một điều đúng | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| NGỤ Ý | p → q | Chỉ sai khi p=T và q=F | T→T=T, T→F=F, F→T=T, F→F=T |
| BI ĐIỀU KIỆN | p ↔ q | Đúng khi cả hai đều có cùng giá trị | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Nhận dạng Boolean chính
| Luật | Công thức |
|------|--------|
| Tính giao hoán | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Tính kết hợp | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Phân phối | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| Định luật De Morgan | ¨(p ∧ q) = �p ∨ �q; â€(p ∨ q) = â€p ∧ â€q |
| Phủ định kép | â(€p) = p |
| Bất lực | p ∧ p = p; p ∨ p = p |
| Hấp thụ | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Ngược chiều | (p → q) ≡ (€q → âp) |
### Biểu mẫu thông thường
| Mẫu | Cấu trúc | Trường hợp sử dụng |
|------|-------------|----------|
| Dạng thông thường liên hợp (CNF) | AND của OR: (A∨B) ∧ (C∨D) | Người giải SAT, giải quyết chứng minh định lý |
| Dạng chuẩn phân biệt (DNF) | HOẶC của AND: (A∧B) ∨ (C∧D) | Thiết kế mạch, hệ thống dựa trên quy tắc |
**Chuyển đổi sang CNF:** Áp dụng định luật De Morgan, phân phối OR trên AND, loại bỏ các phủ định kép.
---

## Số học mô-đun và đồng đẳng
Số học mô-đun nghiên cứu các số nguyên dưới phép toán "số dư sau khi chia". Nó rất cần thiết cho mật mã, băm và lý thuyết số.
### Định nghĩa cốt lõi
| Khái niệm | Ký hiệu | Định nghĩa |
|----------|----------|-------------|
| Sự phù hợp | a ≡ b (mod n) | n chia (a − b) |
| Lớp dư lượng | [a]ₙ | Tập {a + kn : k ∈ ℤ} |
| Mô-đun nghịch đảo | a⁻¹ mod n | Giá trị x sao cho ax ≡ 1 (mod n) |
| tổng số Euler | φ(n) | Đếm các số nguyên trong {1,...,n} nguyên tố cùng nhau đến n |
### Thuộc tính chính
| Bất động sản | Tuyên bố |
|----------|----------|
| Ngoài ra | Nếu a ≡ b và c ≡ d (mod n), thì a+c ≡ b+d (mod n) |
| Phép nhân | Nếu a ≡ b và c ≡ d (mod n), thì ac ≡ bd (mod n) |
| Định lý nhỏ Fermat | Nếu p là số nguyên tố và gcd(a,p) = 1 thì aᵖ⁻¹ ≡ 1 (mod p) |
| Định lý Euler | Nếu gcd(a,n) = 1, thì a^φ(n) ≡ 1 (mod n) |
| Định lý số dư Trung Hoa | Nếu gcd(m,n) = 1 thì hệ x ≡ a (mod m), x ≡ b (mod n) có nghiệm duy nhất mod mn |
### Tính tổng số Euler
Với n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (hệ số nguyên tố):
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Ví dụ:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Thật vậy, {1, 5, 7, 11} là nguyên tố cùng nhau với 12.
### Ứng dụng: Mật mã RSA (Tổng quan)
1. Chọn số nguyên tố lớn p, q. Tính n = pq, φ(n) = (p−1)(q−1).
2. Chọn e sao cho gcd(e, φ(n)) = 1 (số mũ công khai).
3. Tính d ≡ e⁻¹ (mod φ(n)) (số mũ riêng).
4. Mã hóa: c = mᵉ mod n. Giải mã: m = cᵈ mod n.
5. Tính bảo mật dựa vào độ khó của việc phân tích n để tìm p và q.
---

## Quy nạp toán học
**Quy nạp toán học** là kỹ thuật chứng minh cơ bản cho các phát biểu về mọi số tự nhiên.
### Cấu trúc của chứng minh bằng quy nạp
1. **Trường hợp cơ sở:** Chứng minh mệnh đề với n = 0 (hoặc n = 1).
2. **Bước quy nạp:** Giả sử mệnh đề đúng với n = k (giả thuyết quy nạp), sau đó chứng minh mệnh đề đó với n = k + 1.
### Biến thể
| Biến thể | Khi nào nên sử dụng |
|----------|-------------|
| Cảm ứng đơn giản | Chứng minh P(k) → P(k+1) |
| Cảm ứng mạnh | Giả sử P(0), P(1), ..., P(k) chứng minh P(k+1) |
| Cảm ứng cấu trúc | Chứng minh tính chất của cấu trúc được xác định đệ quy (cây, công thức) |
| Cảm ứng vô hạn | Mở rộng quy nạp cho các tập hợp có thứ tự tốt vượt quá ℕ |
**Ví dụ đã làm (Quy nạp mạnh):** Chứng minh mọi số nguyên n ≥ 2 đều có thể viết dưới dạng tích các số nguyên tố.
- Cơ sở: n = 2 là số nguyên tố nên là tích của các số nguyên tố (chính nó).
- Bước quy nạp: Giả sử đúng với mọi số nguyên từ 2 đến k. Hãy xem xét k+1.
  - Nếu k+1 là số nguyên tố thì xong.
  - Nếu k+1 là hợp số thì k+1 = ab trong đó 2 ≤ a, b ≤ k. Theo giả thuyết quy nạp, cả a và b đều là tích của các số nguyên tố nên k+1 là tích của các số nguyên tố.
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái Niệm Toán Rời Rạc | Ứng dụng trong ML / Khoa học dữ liệu |
|--------------|------------------------------------------------|
| Lý thuyết tập hợp | Hoạt động cơ sở dữ liệu (SQL THAM GIA), thao tác bộ tính năng, sự kiện xác suất |
| Quan hệ | Lược đồ cơ sở dữ liệu, mô hình hóa mối quan hệ thực thể, biểu đồ tri thức |
| Chức năng | Chức năng kích hoạt, chuyển đổi tính năng, ánh xạ giữa các không gian |
| Tổ hợp | Lựa chọn tính năng (chọn k từ n), định cỡ tìm kiếm lưới siêu tham số |
| Nguyên lý chuồng bồ câu | Xung đột băm, giới hạn dưới về nén, chứng minh lý thuyết thông tin |
| Quan hệ tái diễn | Lập trình động, phân tích độ phức tạp của thuật toán, mô hình chuỗi thời gian |
| Tạo hàm | Hàm sinh xác suất, giải các bài toán tổ hợp trong kỹ thuật đặc trưng |
| Số Catalan | Đếm cấu trúc cây (cây quyết định), biểu thức phân tích cú pháp, thao tác ngăn xếp |
| Lý thuyết đồ thị (xem file tiếp theo) | Phân tích mạng xã hội, hệ thống khuyến nghị, trình bày kiến ​​thức |
---

## Bản tóm tắt
| Chủ đề | Ý tưởng cốt lõi | Công cụ chính |
|-------|-------------|----------|
| Lý thuyết tập hợp | Bộ sưu tập các đồ vật riêng biệt | Tiên đề ZFC, lượng số, phép tính |
| Quan hệ | Kết nối giữa các phần tử | Quan hệ tương đương, bậc một phần |
| Chức năng | Ánh xạ giữa các bộ | Tính từ, tính từ, tính từ |
| Tổ hợp | Sắp xếp đếm | Hệ số nhị thức, nguyên lý chuồng bồ câu |
| Quan hệ tái diễn | Trình tự được xác định đệ quy | Phương trình đặc trưng, ​​Định lý tổng thể |
| Tạo hàm | Trình tự như chuỗi lũy thừa | OGF/EGF, giải các phép truy toán bằng đại số |
Toán học rời rạc cung cấp ngôn ngữ và công cụ để suy luận về các cấu trúc hữu hạn hoặc đếm được - đó chính xác là những gì máy tính thao tác. Mọi thuật toán, cấu trúc dữ liệu, truy vấn cơ sở dữ liệu và giao thức mật mã đều dựa trên nền tảng riêng biệt. Việc nắm vững các chủ đề này giúp nâng cao khả năng giải quyết vấn đề và cung cấp vốn từ vựng cho nghiên cứu nâng cao về thuật toán, lý thuyết phức tạp và học máy.