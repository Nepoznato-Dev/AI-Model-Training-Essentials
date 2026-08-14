---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
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
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Lý Thuyết Số
Lý thuyết số là nghiên cứu về số nguyên - số nguyên và tính chất của chúng. Gauss gọi nó là “nữ hoàng toán học”. Mặc dù nghiên cứu những đối tượng đơn giản nhất (1, 2, 3, ...), lý thuyết số vẫn tạo ra một số vấn đề sâu sắc nhất và khó nhất trong toán học. Ngày nay, nó là nền tảng của mật mã hiện đại, thuật toán băm, mã sửa lỗi và tạo số ngẫu nhiên.
---

## Tính chia hết và thuật toán chia
### Định nghĩa cốt lõi
| Kỳ hạn | Định nghĩa | Ví dụ |
|------|-------------|----------|
| **Chia** | một \| b nghĩa là ∃k ∈ ℤ: b = ak | 3 \| 12 (vì 12 = 3 × 4) |
| **Số chia** | Một số chia cho số khác | Ước của 12: 1, 2, 3, 4, 6, 12 |
| **Nhiều** | b là bội số của a nếu a \| b | 15 là bội số của 5 |
| **Thương số** | Kết quả của phép chia | 17 `5 = thương 3 |
| **Phần còn lại** | Những gì còn lại sau khi chia | 17 `5 = dư 2 |
### Thuật toán chia
Với mọi số nguyên a và b có b > 0, tồn tại duy nhất các số nguyên q (thương) và r (số dư) sao cho:
a = bq + r, trong đó 0 ≤ r < b
**Ví dụ:** 23 = 5 × 4 + 3. Thương q = 4, số dư r = 3.
### Thuộc tính của khả năng chia hết
| Bất động sản | Tuyên bố |
|----------|----------|
| Tính chuyển tiếp | Nếu một \| b và b \| c thì a \| c |
| Tuyến tính | Nếu một \| b và a \| c thì a \| (bx + cy) với mọi số nguyên x, y |
| So sánh | Nếu một \| b và b > 0 thì a ≤ b |
| tầm thường | một \| 0 với mọi a; 1 \| a cho mọi a; một \| a với mọi a ≠ 0 |
---

## Ước chung lớn nhất (GCD)
**ước chung lớn nhất** của a và b, ký hiệu là gcd(a, b), là số nguyên dương lớn nhất chia cả a và b.
### Thuật toán Euclide
Thuật toán cổ điển hiệu quả nhất để tính toán GCD.
**Thông tin chi tiết chính:** gcd(a, b) = gcd(b, a mod b)
**Thuật toán:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Ví dụ đã hoạt động:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Kết quả: gcd(252, 105) = 21
| Bất động sản | Giá trị |
|----------|-------|
| Độ phức tạp thời gian | O(log(min(a, b))) |
| Độ phức tạp của không gian | O(1) lặp lại |
### Danh tính Bézout
Với mọi số nguyên a, b, tồn tại các số nguyên x, y sao cho:
ax + by = gcd(a, b)
**Thuật toán Euclide mở rộng** tính toán gcd(a, b) và các hệ số x, y cùng một lúc.
**Ví dụ đã làm:** Tìm x, y sao cho 252x + 105y = 21.
- Thay ngược từ thuật toán Euclide:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Vậy x = −2, y = 5. Kiểm tra: 252(−2) + 105(5) = −504 + 525 = 21.
### Thuộc tính chính của GCD
| Bất động sản | Tuyên bố |
|----------|----------|
| gcd(a, 0) | = một |
| gcd(a, 1) | = 1 (a và 1 luôn nguyên tố cùng nhau) |
| gcd(a, b) = gcd(b, a) | Giao hoán |
| gcd(a, b) = gcd(a, b + ka) | Thêm bội số không thay đổi GCD |
| gcd(ca, cb) | = c · gcd(a, b) |
| Đồng nguyên | gcd(a, b) = 1 nghĩa là a và b không có ước chung |
---

## Số nguyên tố
**số nguyên tố** là số nguyên lớn hơn 1 có ước số dương duy nhất là 1 và chính nó.
### Thuộc tính cơ bản
| Bất động sản | Tuyên bố |
|----------|----------|
| **Định lý cơ bản của số học** | Mọi số nguyên n > 1 đều có một hệ số nguyên tố duy nhất |
| **Vô số số nguyên tố** | Có vô số số nguyên tố (Euclid, ~300 BC) |
| **Định lý số nguyên tố** | Số số nguyên tố ≤ n xấp xỉ n / ln(n) |
| **Định đề Bertrand** | Với mọi n > 1, tồn tại một số nguyên tố p với n < p < 2n |
### Những số nguyên tố đầu tiên
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Hệ số nguyên tố
Mọi số nguyên n > 1 đều có thể viết duy nhất dưới dạng:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
trong đó p₁ < p₂ < ... < pₖ là số nguyên tố và aᵢ ≥ 1.
**Ví dụ:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7×11×13
**Dùng hệ số hóa để tính GCD và LCM:**
- gcd(a, b) = tích lũy thừa min của các số nguyên tố chung
- lcm(a, b) = tích lũy thừa cực đại của mọi số nguyên tố
**Ví dụ:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Sàng Eratosthenes
Thuật toán cổ điển để tìm tất cả các số nguyên tố đến giới hạn N.
| Bất động sản | Giá trị |
|----------|-------|
| Độ phức tạp thời gian | O(N log log N) |
| Độ phức tạp của không gian | O(N) |
**Thuật toán:**
1. Liệt kê tất cả các số nguyên từ 2 đến N.
2. Bắt đầu với p = 2. Gạch bỏ tất cả các bội số của p (bắt đầu từ p²).
3. Tìm số chưa gạch chéo tiếp theo > p. Đặt p thành số đó.
4. Lặp lại cho đến khi p² > N. Tất cả các số không bị gạch chéo đều là số nguyên tố.
### Kiểm tra tính nguyên thủy
| Phương pháp | Loại | Thời gian | Trường hợp sử dụng |
|--------|------|------|----------|
| Phòng thử nghiệm | Xác định | O(√n) | Số nhỏ |
| Thử nghiệm Fermat | Xác suất | O(k log2 n) | Sàng lọc nhanh |
| Miller-Rabin | Xác suất | O(k log2 n) | Mục đích chung |
| AKS | Xác định | O(log⁶ n) | Tầm quan trọng về mặt lý thuyết |
**Kiểm tra tính nguyên tố Fermat:** Nếu p là số nguyên tố và gcd(a, p) = 1, thì aᵖ⁻¹ ≡ 1 (mod p). Nếu điều này không thành công với một số a thì p chắc chắn là hợp số. Nếu nó vượt qua nhiều giá trị a ngẫu nhiên, p có thể là số nguyên tố.
**Lưu ý:** Số Carmichael (ví dụ: 561) vượt qua bài kiểm tra Fermat cho tất cả các cơ sở nguyên tố cùng nhau nhưng là hợp số. Miller-Rabin tránh vấn đề này.
---

## Số học mô-đun
Số học mô-đun nghiên cứu các số nguyên dưới dạng "bao quanh" — số học trên mặt đồng hồ.
### Quan hệ đồng đẳng
a ≡ b (mod n) nghĩa là n | (a − b), tức là a và b có cùng số dư khi chia cho n.
### Thuộc tính số học
| Hoạt động | Quy tắc |
|----------||------|
| Ngoài ra | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Phép nhân | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| lũy thừa | aᵇ mod n có thể được tính toán một cách hiệu quả bằng cách bình phương lặp lại |
| Phủ định | (−a) mod n = n − (a mod n) |
### lũy thừa mô-đun
Tính toán aᵇ mod n một cách hiệu quả bằng cách sử dụng **bình phương lặp lại**:
**Ví dụ đã hoạt động:** 3¹³ mod 7
- 13 ở dạng nhị phân: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Bất động sản | Giá trị |
|----------|-------|
| Độ phức tạp thời gian | O(log b · log² n) |
| Độ phức tạp của không gian | O(1) |
### Hàm tổng Euler
φ(n) đếm các số nguyên nguyên tố cùng nhau từ 1 đến n.
| n | φ(n) | Số nguyên tố cùng nhau |
|---|------|-------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 là số nguyên tố) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Công thức:**
- Nếu p là số nguyên tố: φ(p) = p − 1
- Nếu p là số nguyên tố: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Nếu gcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (nhân)
- Tổng quát: φ(n) = n · Π_{p|n} (1 − 1/p) trong đó tích trên thừa số nguyên tố riêng biệt của n
---

## Định lý chính
### Định lý nhỏ Fermat
Nếu p là số nguyên tố và gcd(a, p) = 1 thì:
aᵖ⁻¹ ≡ 1 (mod p)
**Hệ quả tất yếu (với mọi a):** aᵖ ≡ a (mod p)
**Sử dụng:** Nghịch đảo mô đun nhanh khi mô đun là số nguyên tố: a⁻¹ ≡ aᵖ⁻² (mod p)
**Ví dụ đã làm:** Tìm 3⁻¹ mod 7.
- Bởi Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Kiểm tra: 3 × 5 = 15 ≡ 1 (mod 7).
### Định lý Euler (Tổng quát hóa Fermat)
Nếu gcd(a, n) = 1 thì:
a^φ(n) ≡ 1 (mod n)
Điều này khái quát hóa Định lý nhỏ Fermat từ số nguyên tố đến mô đun bất kỳ.
### Định lý số dư Trung Hoa (CRT)
Nếu m₁, m₂, ..., mₖ là nguyên tố cùng nhau theo cặp thì hệ:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
có nghiệm duy nhất modulo M = m₁ · m₂ · ... · mₖ.
**Ví dụ đã làm:** Giải x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3×5×7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Tìm nghịch đảo: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Kiểm tra: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Định lý Wilson
(p-1)! ≡ −1 (mod p) khi và chỉ nếu p là số nguyên tố.
Chủ yếu được quan tâm về mặt lý thuyết - không thực tế cho việc kiểm tra tính nguyên tố vì việc tính toán giai thừa rất tốn kém.
### Dư lượng bậc hai
Số nguyên a là **dư lượng bậc hai mod n** nếu x² ≡ a (mod n) có nghiệm.
**Tiêu chí Euler:** a là thặng dư bậc hai mod nguyên tố p iff a^((p−1)/2) ≡ 1 (mod p).
**Biểu tượng huyền thoại:** (a/p) = a^((p−1)/2) mod p, cho kết quả +1, −1 hoặc 0.
**Khả năng tương hỗ bậc hai** (Gauss): Đối với các số nguyên tố lẻ khác nhau p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Định lý sâu sắc này kết nối các thặng dư bậc hai của các số nguyên tố khác nhau và có tám định luật bổ sung xử lý các trường hợp p = 2.
---

## Ứng dụng vào mật mã
### Hệ thống mật mã RSA
Hệ thống mật mã khóa công khai được triển khai rộng rãi nhất, dựa trên độ khó của việc phân tích các số nguyên lớn.
**Cài đặt:**
1. Chọn hai số nguyên tố lớn p, q (mỗi số thường có hơn 1024 bit)
2. Tính n = pq và φ(n) = (p−1)(q−1)
3. Chọn e sao cho 1 < e < φ(n) và gcd(e, φ(n)) = 1 (phổ biến: e = 65537)
4. Tính d ≡ e⁻¹ (mod φ(n)) bằng Thuật toán Euclide mở rộng
5. **Khóa công khai:** (n, e). **Khóa riêng:** (n, d)
**Mã hóa:** c = mᵉ mod n (trong đó m là tin nhắn văn bản gốc)
**Giải mã:** m = cᵈ mod n
**Tại sao nó hoạt động:** cᵈ = m^(ed) ≡ m (mod n) theo định lý Euler, vì ed ≡ 1 (mod φ(n)).
**Bảo mật:** Phân tích n thành p và q là không khả thi về mặt tính toán đối với n lớn (2048+ bit). Không có p và q, kẻ tấn công không thể tính φ(n) và do đó không thể tìm thấy d.
### Trao đổi khóa Diffie-Hellman
Cho phép hai bên thiết lập bí mật chung trên kênh không an toàn.
**Thiết lập:** Đồng ý về số nguyên tố lớn p và số sinh g (mod p).
**Giao thức:**
1. Alice chọn bí mật a, gửi A = gᵃ mod p cho Bob
2. Bob chọn bí mật b, gửi B = gᵇ mod p cho Alice
3. Alice tính s = Bᵃ mod p = gᵃᵇ mod p
4. Bob tính s = Aᵇ mod p = gᵃᵇ mod p
5. Cả hai cùng chia sẻ bí mật s = gᵃᵇ mod p
**Bảo mật:** Dựa trên độ khó của **bài toán logarit rời rạc** — tìm a từ gᵃ mod p.
### Hàm băm và Lý thuyết số
Các hàm băm tốt sử dụng số học mô-đun để phân phối các khóa một cách đồng đều:
- **Băm nhân:** h(k) = (k · A) mod m, trong đó A ≈ m · (√5 − 1) / 2 (tỷ lệ vàng)
- **Băm toàn cục:** h(k) = ((ak + b) mod p) mod m, trong đó p là số nguyên tố, a, b là ngẫu nhiên
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái Niệm Lý Thuyết Số | Ứng dụng |
|----------------------|-------------|
| Số học mô-đun | Băm (bảng băm, bản đồ băm), tạo số ngẫu nhiên |
| Số nguyên tố | Định cỡ bảng băm (sử dụng kích thước bảng nguyên tố để giảm xung đột) |
| Thuật toán GCD / Euclide | Số học hợp lý, đơn giản hóa phân số trong xác suất |
| lũy thừa mô-đun | Bảo mật mật mã cho mô hình ML phân phát qua HTTPS |
| tổng số Euler | Tạo khóa RSA, hiểu các đảm bảo về mật mã |
| Định lý số dư Trung Hoa | Tính toán phân tán, số học mô-đun song song |
| Kiểm tra tính nguyên thủy | Tạo số nguyên tố cho các hoạt động mã hóa |
| Dư lượng bậc hai | Bài toán dư bậc hai trong mật mã nâng cao |
| Trường hữu hạn (GF(p), GF(2ᵏ)) | Mã sửa lỗi, mã Reed-Solomon, mã hóa AES |
---

## Bản tóm tắt
| Chủ đề | Ý tưởng cốt lõi | Kết quả then chốt |
|-------|-------------|-------------|
| Tính chia hết | Phép chia có số dư | Thuật toán chia: a = bq + r |
| GCD | Yếu tố chia sẻ lớn nhất | Thuật toán Euclide: O(log n) |
| Số nguyên tố | Nguyên tử của số nguyên | Định lý cơ bản của số học (phân tích nhân tử duy nhất) |
| Số học mô-đun | Số học bao quanh | Các lớp đồng đẳng, lũy thừa mô-đun |
| Euler's Totient | Đếm số nguyên tố cùng nhau | φ(n) = n · Π(1 − 1/p) |
| Định lý nhỏ Fermat | Phím tắt mô đun chính | aᵖ⁻¹ ≡ 1 (mod p) |
| Định lý Euler | Fermat tổng quát | a^φ(n) ≡ 1 (mod n) |
| Định lý số dư Trung Hoa | Kết hợp các hệ thống mô-đun | Sản phẩm mod giải pháp độc đáo của coprime moduli |
| Mật mã | Những bài toán lý thuyết số khó | RSA (bao thanh toán), Diffie-Hellman (nhật ký rời rạc) |
Lý thuyết số biến những câu hỏi đơn giản về số nguyên thành toán học sâu sắc với những ứng dụng thực tiễn sâu sắc. Mọi kết nối web an toàn, tin nhắn được mã hóa và chữ ký số đều dựa vào kết quả lý thuyết số được phát hiện từ nhiều thế kỷ trước khi máy tính tồn tại. Đối với các nhà khoa học dữ liệu và kỹ sư ML, việc hiểu lý thuyết số cung cấp cái nhìn sâu sắc về hàm băm, tạo số ngẫu nhiên và cơ sở hạ tầng mật mã bảo vệ dữ liệu khi truyền và ở trạng thái nghỉ.