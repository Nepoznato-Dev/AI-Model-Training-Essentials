---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Toán học
Toán học không chỉ là môn học ở trường mà nó còn là nền tảng của hầu hết mọi lĩnh vực kỹ thuật. Vật lý sử dụng nó để mô tả vũ trụ. Khoa học máy tính sử dụng nó để thiết kế các thuật toán. Học máy sử dụng nó để tối ưu hóa trọng lượng. Tài chính sử dụng nó để gây rủi ro về giá. Việc nắm vững mọi nhánh là không cần thiết, nhưng việc hiểu rõ bối cảnh - và biết từng nhánh áp dụng ở đâu - sẽ giúp bạn dễ dàng nắm bắt các chủ đề khác hơn.
---

## Hệ thống số
Trước hết, việc hiểu các loại số bạn đang làm việc sẽ giúp ích. Mỗi lớp mở rộng lớp trước để giải quyết vấn đề mà lớp cũ không thể giải quyết được.
| Loại Số | Nó bao gồm những gì | Tại sao nó được phát minh | Ví dụ |
|---|---|---|---|
| Số tự nhiên | 1, 2, 3, 4, ... | Đếm đồ vật | 5 quả táo |
| Số nguyên | 0, 1, 2, 3, ... | Đại diện cho "không có gì" | 0 độ |
| Số nguyên | ..., −2, −1, 0, 1, 2, ... | Nợ nần, nhiệt độ dưới 0 | −15°C |
| Số hữu tỷ | p/q trong đó q ≠ 0 | Phân chia mọi thứ không đồng đều | 1/3, 0,75 |
| Số vô tỷ | Không thể biểu diễn dưới dạng phân số | Đường chéo, hình tròn, tăng trưởng | √2, π, e |
| Số thực | Tất cả đều hợp lý + phi lý | Dòng số đầy đủ | 3.14159... |
| Số ảo | Bội số của i = √(−1) | Giải x2 + 1 = 0 | 3i |
| số phức | a + bi (thực + tưởng tượng) | Kỹ thuật điện, cơ học lượng tử | 2 + 3i |
---

## Lý thuyết số học và số
Khái niệm cơ bản: cộng, trừ, nhân, chia và các quy tắc chi phối thứ tự của chúng.
**Thứ tự thực hiện** (PEMDAS/BODMAS): Dấu ngoặc đơn → Số mũ → Nhân/Chia (trái sang phải) → Cộng/trừ (trái sang phải).
**Số nguyên tố** — các số nguyên lớn hơn 1 không có ước số nào khác ngoài 1 và chính nó — là nguyên tố của lý thuyết số. Số đầu tiên: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Tại sao các số nguyên tố lại quan trọng ngoài lớp toán: mã hóa hiện đại (RSA) dựa trên thực tế là việc nhân hai số nguyên tố lớn thì dễ dàng, nhưng việc phân tích kết quả lại thì rất khó về mặt tính toán.
**Thao tác hữu ích:**
- Phân tích thành thừa số nguyên tố: 84 = 2² × 3 × 7
- Ước chung lớn nhất (GCD) của 24 và 36: 12
- Bội chung nhỏ nhất (LCM) của 4 và 6: 12
---

## Đại số
Đại số là nơi bạn ngừng làm việc với những con số cụ thể và bắt đầu làm việc với *các mối quan hệ*. Một biến như`x`không có giá trị cố định — nó đại diện cho bất cứ điều gì làm cho phương trình đúng.
**Công thức bậc hai** giải ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Các loại hàm phổ biến và nơi chúng xuất hiện:**
| Chức năng | Công thức | Hình dạng | Ví dụ trong thế giới thực |
|---|---|---|---|
| Tuyến tính | y = mx + b | Đường thẳng | Chi phí cho mỗi đơn vị ở mức cố định |
| Bậc hai | y = ax² + bx + c | Parabol | Chuyển động của đạn, khoảng cách phanh |
| Hàm mũ | y = a × b2 | Tăng trưởng/suy tàn nhanh | Lãi kép, tăng dân số, lây lan virus |
| Logarit | y = log_b(x) | Tăng trưởng chậm, nghịch đảo theo cấp số nhân | Thang đo decibel, thang đo pH, độ phức tạp của thuật toán |
**Từ vựng chính:**
- **Miền**: tất cả dữ liệu đầu vào hợp lệ (ví dụ: không thể chia cho 0, không thể lấy √ của số âm trong số thực)
- **Phạm vi**: tất cả các kết quả đầu ra có thể
- **Slope** (m): tốc độ thay đổi — "với mỗi 1 đơn vị của x, y thay đổi một m"
- **Chặn**: nơi hàm đi qua một trục
---

## Hình học
Hình học nghiên cứu hình dạng, kích thước và mối quan hệ không gian. Nó xuất hiện ở khắp mọi nơi: công cụ trò chơi sử dụng nó để kết xuất, robot sử dụng nó để lập kế hoạch đường đi, kiến ​​trúc sử dụng nó để thiết kế kết cấu.
**Công thức thiết yếu:**
| Hình dạng | Bất động sản | Công thức |
|---|---|---|
| Tam giác | Tổng góc | 180° |
| Tứ giác | Tổng góc | 360° |
| Vòng tròn | Chu vi | 2πr |
| Vòng tròn | Khu vực | πr² |
| Quả cầu | Khối lượng | (4/3)πr³ |
| Tam giác vuông | Định lý Pythagore | a2 + b2 = c2 |
**π (pi)** ≈ 3.14159 — tỷ lệ giữa chu vi của bất kỳ hình tròn nào với đường kính của nó. Nó xuất hiện ở những nơi bạn không mong đợi: xác suất (phân phối chuẩn), kỹ thuật (xử lý tín hiệu), thậm chí cả phương trình cho nguyên lý bất định Heisenberg.
---

## Phép tính
Nghiên cứu tính toán *thay đổi* và *tích lũy*. Nếu đại số xử lý ảnh chụp nhanh thì phép tính xử lý hình ảnh chuyển động.
### Phép tính vi phân
Tỷ lệ thay đổi. Đạo hàm f'(x) cho bạn biết f thay đổi nhanh như thế nào tại bất kỳ điểm nào.
| Hàm f(x) | Đạo hàm f'(x) | Trực giác |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Quy tắc quyền lực |
| eˣ | eˣ | Hàm duy nhất bằng đạo hàm riêng của nó |
| ln(x) | 1/x | Tốc độ tăng trưởng chậm lại khi x tăng |
| tội lỗi(x) | cos(x) | Tỷ lệ thay đổi dao động |
**Tại sao đạo hàm lại quan trọng trong ML:** giảm độ dốc — thuật toán đào tạo hầu hết các mạng thần kinh — hoạt động bằng cách tính toán đạo hàm của hàm mất mát và bước theo hướng giảm lỗi.
### Quy tắc phân biệt chính
| Quy tắc | Công thức | Trường hợp sử dụng |
|------|----------|----------|
| **Quy tắc chuỗi** | (f∘g)' = f'(g(x)) · g'(x) | Các hàm lồng nhau - lan truyền ngược trong mạng thần kinh |
| **Quy tắc sản phẩm** | (fg)' = f'g + fg' | Nhân hai hàm của x |
| **Quy tắc thương** | (f/g)' = (f'g − fg') / g² | Chia hai hàm của x |
### Phép tính tích phân
Tích lũy. Tích phân biểu thị diện tích dưới một đường cong. Nếu đạo hàm trả lời "nó thay đổi nhanh như thế nào?", thì tích phân trả lời "đã tích lũy được bao nhiêu?"
**Định lý cơ bản của phép tính** kết nối cả hai: vi phân và tích phân là các phép toán nghịch đảo.
| Tích phân | Kết quả | Trường hợp sử dụng |
|----------|--------|----------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Diện tích dưới đường cong đa thức |
| ∫ eˣ dx | eˣ + C | Tổng tăng trưởng tích lũy |
| ∫ 1/x dx | ln|x| + C | Tích lũy logarit |
---

## Bộ
**tập hợp** là một tập hợp các đối tượng riêng biệt — nền tảng của toán học hiện đại.
| Hoạt động | Biểu tượng | Ý nghĩa | Ví dụ (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Liên minh | A ∪ B | Các phần tử trong một trong hai bộ | {1, 2, 3, 4} |
| Giao lộ | A ∩ B | Các phần tử trong cả hai bộ | {2} |
| Sự khác biệt | A \ B | Các phần tử thuộc A nhưng không thuộc B | {1, 3} |
| Bộ trống | ∅ | Không chứa gì | {} |
| Tập hợp con | A ⊂ B | Tất cả các phần tử của A đều có trong B | {1,2} ⊂ {1,2,3} |
Lý thuyết tập hợp xuất hiện trong cơ sở dữ liệu (SQL THAM GIA về cơ bản là các hoạt động được thiết lập), xác suất (sự kiện là tập hợp kết quả) và lập trình (bộ, bản đồ băm).
---

## Cơ sở nhị phân và số
Máy tính suy nghĩ ở dạng nhị phân (cơ sở 2): chỉ 0 và 1. Con người suy nghĩ theo số thập phân (cơ số 10). Các lập trình viên thường sử dụng hệ thập lục phân (cơ số 16) như một cách rút gọn để biểu diễn nhị phân.
| Căn cứ | Chữ số được sử dụng | Ví dụ | Tương đương thập phân |
|---|---|---|---|
| Nhị phân (cơ sở 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Thập phân (cơ số 10) | 0–9 | 11 | 11 |
| Hệ thập lục phân (cơ sở 16) | 0–9, A–F | B | 11 |
| Thập lục phân | 0–9, A–F | A3 | 160 + 3 = 163 |
**Tại sao lại quan trọng:** mọi phần dữ liệu trong máy tính — văn bản, hình ảnh, âm thanh, video — cuối cùng chỉ là nhị phân. Một byte (8 bit) có thể biểu thị 256 giá trị riêng biệt. Màu sắc trong CSS (#FF5733), địa chỉ bộ nhớ (0x7FFF) và địa chỉ IP đều sử dụng hệ thập lục phân vì nó nén các chuỗi nhị phân dài thành thứ có thể đọc được.
---

## Đại số tuyến tính cho ML và Đồ họa
Đại số tuyến tính — vectơ, ma trận và phép biến đổi — là công cụ toán học đằng sau máy học, đồ họa máy tính, mô phỏng vật lý và công cụ tìm kiếm.
### Vectơ
**Vectơ** là danh sách các số có thứ tự. Trong ML, mỗi điểm dữ liệu là một vectơ đặc trưng:
- [23, 1.8, 75] có thể biểu thị tuổi của một người, chiều cao tính bằng mét và cân nặng tính bằng kg.
| Hoạt động Vector | Công thức | Trường hợp sử dụng |
|--------|----------|----------|
| **Bổ sung** | a + b = [a₁+b₁, a₂+b₂, ...] | Kết hợp các vectơ đặc trưng |
| **Phép nhân vô hướng** | c·a = [c·a₁, c·a₂, ...] | Tính năng mở rộng quy mô |
| **Chấm sản phẩm** | a·b = Σ aᵢbᵢ | Sự tương đồng, dự đoán |
| **Định mức (cường độ)** | ||a|| = √(Σ aᵢ²) | Chiều dài vectơ |
| **Sản phẩm chéo** | a × b (chỉ 3D) | Vectơ vuông góc, diện tích |
### Ma trận
**Ma trận** là mảng số 2D. Trọng số của mạng lưới thần kinh được lưu trữ dưới dạng ma trận. Một lô 100 hình ảnh có thể là một ma trận có hình dạng (100, 784) - 100 hàng, mỗi hàng có giá trị 784 pixel.
**Các thao tác chính:**
| Hoạt động | Nó làm gì | Nó xuất hiện ở đâu |
|---|---|---|
| Sản phẩm chấm | Đo độ tương tự giữa hai vectơ | Hệ thống khuyến nghị, độ tương tự cosin |
| Phép nhân ma trận | Kết hợp các phép biến đổi tuyến tính | Mỗi lớp của mạng lưới thần kinh |
| Giá trị riêng/vector riêng | Hướng một ma trận chia tỷ lệ (không quay) | Giảm kích thước PCA, PageRank |
| Xếp hạng ma trận | Lượng thông tin độc lập | Nén, xấp xỉ thứ hạng thấp |
| Chuyển cung | Lật hàng và cột | Tính toán độ dốc |
| Nghịch đảo | A⁻¹ sao cho A·A⁻¹ = I | Giải hệ tuyến tính |
**Độ tương tự cosine** = (a·b) / (||a|| × ||b||) — nằm trong khoảng từ −1 (ngược lại) đến 1 (cùng hướng). Đây là cách các công cụ tìm kiếm đo lường xem hai tài liệu có "giống nhau" hay không và cách các mô hình nhúng so sánh sự giống nhau về ngữ nghĩa.
---

## Bản tóm tắt
| Chi nhánh | Câu hỏi cốt lõi | Ứng dụng chính |
|---|---|---|
| Số học & Lý thuyết số | Các con số hành xử như thế nào? | Mật mã, băm |
| Đại số | Những điều chưa biết có liên quan như thế nào? | Mô hình hóa, phương trình |
| Hình học | Hình dạng và không gian hoạt động như thế nào? | Đồ họa, robot, kiến ​​trúc |
| Giải tích | Mọi thứ thay đổi như thế nào? | Đào tạo mạng lưới thần kinh, vật lý |
| Lý thuyết tập hợp | Các bộ sưu tập có liên quan như thế nào? | Cơ sở dữ liệu, xác suất |
| Đại số tuyến tính | Các phép biến đổi hoạt động như thế nào? | ML, đồ họa, công cụ tìm kiếm |
Không phải tất cả các chủ đề này đều cần thiết ngay lập tức. Tuy nhiên, khi một người đi sâu hơn vào bất kỳ lĩnh vực kỹ thuật nào, những nền tảng này ngày càng trở nên phù hợp. Mỗi nhánh trở nên rõ ràng hơn khi vấn đề được thiết kế để giải quyết được hiểu rõ.