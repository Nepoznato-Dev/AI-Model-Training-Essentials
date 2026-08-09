---
# Metadata
title: "Mathematics and Logic"
description: "Mathematics, logic, proofs"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [math, logic, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Toán học và Logic
Toán học không chỉ là môn học bạn học ở trường - nó là hệ điều hành nằm trong hầu hết mọi lĩnh vực kỹ thuật. Vật lý sử dụng nó để mô tả vũ trụ. Khoa học máy tính sử dụng nó để thiết kế các thuật toán. Học máy sử dụng nó để tối ưu hóa trọng lượng. Tài chính sử dụng nó để gây rủi ro về giá. Bạn không cần phải nắm vững mọi nhánh nhưng hiểu được bối cảnh — và biết vị trí mỗi nhánh xuất hiện — sẽ khiến mọi thứ khác nhấp chuột nhanh hơn.
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
**Số nguyên tố** — các số nguyên lớn hơn 1 không có ước số nào khác ngoài 1 và chính nó — là các nguyên tử của lý thuyết số. Số đầu tiên: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Tại sao các số nguyên tố lại quan trọng ngoài lớp toán: mã hóa hiện đại (RSA) dựa trên thực tế là việc nhân hai số nguyên tố lớn thì dễ dàng, nhưng việc phân tích kết quả lại thì rất khó khăn về mặt tính toán.
**Thao tác hữu ích:**
- Phân tích thành thừa số nguyên tố: 84 = 2² × 3 × 7
- Ước chung lớn nhất (GCD) của 24 và 36: 12
- Bội chung nhỏ nhất (LCM) của 4 và 6: 12
---

## Đại số
Đại số là nơi bạn ngừng làm việc với những con số cụ thể và bắt đầu làm việc với *các mối quan hệ*. Một biến như`x`không có giá trị cố định — nó đại diện cho bất cứ điều gì làm cho phương trình đúng.
**Công thức bậc hai** giải ax² + bx + c = 0:
x = (−b ± √(b2 − 4ac)) / 2a
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
Hình học nghiên cứu hình dạng, kích thước và mối quan hệ không gian. Nó xuất hiện ở mọi nơi: công cụ trò chơi sử dụng nó để kết xuất, robot sử dụng nó để lập kế hoạch đường đi, kiến ​​trúc sử dụng nó để thiết kế kết cấu.
**Công thức thiết yếu:**
| Hình dạng | Tài sản | Công thức |
|---|---|---|
| Tam giác | Tổng góc | 180° |
| Tứ giác | Tổng góc | 360° |
| Vòng tròn | Chu vi | 2πr |
| Vòng tròn | Khu vực | πr² |
| Quả cầu | Khối lượng | (4/3)πr³ |
| Tam giác vuông | Định lý Pythagore | a2 + b2 = c2 |
**π (pi)** ≈ 3.14159 — tỷ lệ giữa chu vi của bất kỳ hình tròn nào với đường kính của nó. Nó xuất hiện ở những nơi bạn không mong đợi: xác suất (phân phối chuẩn), kỹ thuật (xử lý tín hiệu), thậm chí cả phương trình cho nguyên lý bất định Heisenberg.
---

## Thống kê và xác suất
Thống kê là cách bạn hiểu dữ liệu. Đó là sự khác biệt giữa "Tôi nghĩ cách này hiệu quả" và "Tôi có bằng chứng cho thấy cách này hiệu quả".
**Đo lường xu hướng trung tâm — thế nào là "điển hình":**
| Đo | Cách tính toán | Khi nào nên sử dụng nó |
|---|---|---|
| Trung bình (trung bình) | Tổng → đếm | Lựa chọn mặc định; nhạy cảm với các ngoại lệ |
| Trung vị | Giá trị trung bình khi được sắp xếp | Dữ liệu sai lệch (ví dụ: giá nhà, tiền lương) |
| Chế độ | Giá trị thường xuyên nhất | Dữ liệu phân loại (ví dụ: màu phổ biến nhất) |
**Các thước đo về mức độ lây lan — mức độ "đa dạng" của dữ liệu:**
| Đo | Ý tưởng Công thức | Nó nói gì với bạn |
|---|---|---|
| Phạm vi | tối đa - tối thiểu | Tổng mức chênh lệch nhưng nhạy cảm với ngoại lệ |
| Phương sai | Độ lệch bình phương trung bình so với giá trị trung bình | Theo đơn vị bình phương (khó diễn giải trực tiếp) |
| Độ lệch chuẩn | √phương sai | Đơn vị tương tự như dữ liệu - thước đo lan truyền tiếp theo |
**Cơ bản về xác suất:**
- Phạm vi từ 0 (không thể) đến 1 (chắc chắn)
- Biến cố độc lập: P(A và B) = P(A) × P(B)
- Ví dụ: tung liên tiếp hai số 6 = (1/6) × (1/6) = 1/36
**Phân phối xác suất bạn sẽ gặp trong ML:**
| Phân phối | Nó mô hình gì | Ví dụ |
|---|---|---|
| Bernoulli | Thử nghiệm đơn, hai kết quả | Lật một đồng xu |
| Nhị thức | Thành công trong n thử nghiệm | Câu trả lời đúng trong MCQ 10 câu hỏi |
| Bình thường (Gaussian) | Đường cong chuông, hiện tượng tự nhiên | Độ cao, điểm kiểm tra, độ ồn đo |
| Poisson | Sự kiện trong một khoảng thời gian cố định | Email mỗi giờ, lỗi mỗi đợt |
**Định lý Bayes** — cập nhật niềm tin bằng bằng chứng:
P(A|B) = P(B|A) × P(A) / P(B)
Đây là xương sống của bộ lọc thư rác, chẩn đoán y tế và mô hình Bayesian ML. Nó nói: niềm tin cập nhật của bạn = (bằng chứng phù hợp với giả thuyết của bạn như thế nào × niềm tin trước đây của bạn) / khả năng của bằng chứng tổng thể như thế nào.
---

## Phép tính
Nghiên cứu tính toán *thay đổi* và *tích lũy*. Nếu đại số xử lý ảnh chụp nhanh thì phép tính xử lý hình ảnh chuyển động.
**Phép tính vi phân** — tỷ lệ thay đổi. Đạo hàm f'(x) cho bạn biết f thay đổi nhanh như thế nào tại bất kỳ điểm nào.
| Hàm f(x) | Đạo hàm f'(x) | Trực giác |
|---|---|---|
| xⁿ | n·xⁿâ»¹ | Quy tắc quyền lực |
| e² | e² | Hàm duy nhất bằng đạo hàm riêng của nó |
| ln(x) | 1/x | Tốc độ tăng trưởng chậm lại khi x tăng |
| tội lỗi(x) | cos(x) | Tỷ lệ thay đổi dao động |
Tại sao đạo hàm lại quan trọng trong ML: giảm độ dốc - thuật toán đào tạo hầu hết các mạng thần kinh - hoạt động bằng cách tính toán đạo hàm của hàm mất mát và bước theo hướng giảm lỗi.
**Phép tính tích phân** — tích lũy. Tích phân biểu thị diện tích dưới một đường cong. Nếu đạo hàm trả lời "nó thay đổi nhanh như thế nào?", thì tích phân trả lời "đã tích lũy được bao nhiêu?"
**Định lý cơ bản của phép tính** kết nối cả hai: vi phân và tích phân là các phép toán nghịch đảo.
---

## Logic và lý luận
Logic là nghiên cứu về lý luận *hợp lệ* - không phải liệu một kết luận có *cảm thấy* đúng hay không, mà là liệu nó có *tuân theo* từ các tiền đề hay không.
**Lý luận suy diễn** (kết luận được đảm bảo nếu tiền đề đúng):
- Tất cả con người đều phải chết. Socrates là con người. → Socrates phải chết.
**Lý luận quy nạp** (kết luận có thể xảy ra, không đảm bảo):
- Mọi con thiên nga tôi từng thấy đều có màu trắng. → Tất cả thiên nga có lẽ đều có màu trắng. (Nhưng thiên nga đen có tồn tại.)
**Những sai lầm logic phổ biến — những lỗi trông giống như lý luận nhưng thực ra không phải:**
| Sai lầm | Nó là gì | Ví dụ |
|---|---|---|
| Quảng cáo hominem | Tấn công người chứ không phải luận điểm | "Bạn không thể tin tưởng vào ý tưởng chính sách của cô ấy - cô ấy còn trẻ." |
| Người rơm | Trình bày sai một lập luận để đánh đổ nó | "Ông ta muốn cắt giảm chi tiêu quân sự? Ông ta muốn để chúng ta không có khả năng tự vệ!" |
| Sự phân đôi sai lầm | Trình bày hai lựa chọn khi tồn tại nhiều hơn | "Bạn hoặc ở bên chúng tôi hoặc chống lại chúng tôi." |
| Lý luận vòng tròn | Lấy kết luận làm tiền đề | "Luật này bất công vì nó không công bằng." |
| Khiếu nại chính quyền | "Đó là sự thật bởi vì một chuyên gia đã nói như vậy" | “Cổ phiếu này sẽ tăng giá – một nhà đầu tư nổi tiếng đã nói như vậy.” |
| Đăng bài | Giả sử A gây ra B vì A có trước | "Tôi đã uống thuốc bổ sung này, sau đó cơn cảm lạnh của tôi biến mất. Thuốc bổ sung này đã chữa khỏi bệnh cho tôi." |
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
**Vectơ** là danh sách các số có thứ tự. Trong ML, mỗi điểm dữ liệu là một vectơ đặc trưng:
- [23, 1.8, 75] có thể biểu thị tuổi của một người, chiều cao tính bằng mét và cân nặng tính bằng kg.
**Ma trận** là mảng số 2D. Trọng số của mạng lưới thần kinh được lưu trữ dưới dạng ma trận. Một lô 100 hình ảnh có thể là một ma trận có hình dạng (100, 784) - 100 hàng, mỗi hàng có giá trị 784 pixel.
**Các thao tác chính:**
| Hoạt động | Nó làm gì | Nó xuất hiện ở đâu |
|---|---|---|
| Sản phẩm chấm | Đo độ tương tự giữa hai vectơ | Hệ thống khuyến nghị, độ tương tự cosin |
| Phép nhân ma trận | Kết hợp các phép biến đổi tuyến tính | Mỗi lớp của mạng lưới thần kinh |
| Giá trị riêng/vector riêng | Hướng một ma trận chia tỷ lệ (không quay) | Giảm kích thước PCA, PageRank |
| Xếp hạng ma trận | Lượng thông tin độc lập | Nén, xấp xỉ thứ hạng thấp |
**Độ tương tự cosine** = (a·b) / (||a|| × ||b||) — nằm trong khoảng từ −1 (ngược lại) đến 1 (cùng hướng). Đây là cách các công cụ tìm kiếm đo lường xem hai tài liệu có "giống nhau" hay không và cách các mô hình nhúng so sánh sự giống nhau về ngữ nghĩa.
---

## Bản tóm tắt
| Chi nhánh | Câu hỏi cốt lõi | Ứng dụng chính |
|---|---|---|
| Số học & Lý thuyết số | Các con số hoạt động như thế nào? | Mật mã, băm |
| Đại số | Những điều chưa biết có liên quan như thế nào? | Mô hình hóa, phương trình |
| Hình học | Hình dạng và không gian hoạt động như thế nào? | Đồ họa, robot, kiến ​​trúc |
| Thống kê & Xác suất | Dữ liệu nói lên điều gì? | ML, thử nghiệm A/B, phân tích rủi ro |
| Giải tích | Mọi thứ thay đổi như thế nào? | Đào tạo mạng lưới thần kinh, vật lý |
| Logic | Lý do này có hợp lý không? | Lập trình, chứng minh, phân tích luận cứ |
| Lý thuyết tập hợp | Các bộ sưu tập có liên quan như thế nào? | Cơ sở dữ liệu, xác suất |
| Đại số tuyến tính | Các phép biến đổi hoạt động như thế nào? | ML, đồ họa, công cụ tìm kiếm |
Bạn không cần tất cả những thứ này vào ngày đầu tiên. Nhưng khi bạn đi sâu hơn vào bất kỳ lĩnh vực kỹ thuật nào, bạn sẽ tiếp tục quay lại những nền tảng này. Tin tốt: mỗi nhánh sẽ có ý nghĩa hơn rất nhiều khi bạn biết *tại sao* nó được phát minh — nó đang cố gắng giải quyết vấn đề gì.