<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [statistical, testing, experimentation, data-science-and-analytics]
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

-->
# Kiểm tra và thử nghiệm thống kê
Thống kê là ngữ pháp của khoa học. Nó cung cấp cho bạn các công cụ để phân biệt các mẫu thực với nhiễu ngẫu nhiên, để đo lường xem một thay đổi có thực sự cải thiện mọi thứ hay không và đưa ra quyết định trong điều kiện không chắc chắn. Tệp này bao gồm các khái niệm cốt lõi về kiểm tra giả thuyết, thiết kế thử nghiệm và những cạm bẫy phổ biến khiến mọi người vấp ngã.
---

## Khung kiểm tra giả thuyết
Mọi kiểm tra thống kê đều tuân theo cùng một logic:
1. **Nêu giả thuyết khống (H₀)**: Không có ảnh hưởng/không có sự khác biệt.
2. **Nêu giả thuyết thay thế (H₁)**: Có ảnh hưởng/sự khác biệt.
3. **Chọn mức ý nghĩa (α)**: Thường là 0,05 (5% khả năng dương tính giả).
4. **Thu thập dữ liệu và tính toán thống kê kiểm tra**.
5. **Tính giá trị p**: Xác suất quan sát được kết quả này (hoặc cực đoan hơn) nếu H₀ đúng.
6. **Đưa ra quyết định**: Nếu p < α, hãy bác bỏ H₀ (có ý nghĩa thống kê). Ngược lại, không thể bác bỏ H₀.
### Các khái niệm chính
| Khái niệm | Ý nghĩa | Quan niệm sai lầm phổ biến |
|----------|----------|----------------------|
| **giá trị p** | P(dữ liệu \| H₀ là đúng) | KHÔNG phải "xác suất H₀ đúng" |
| **α (mức ý nghĩa)** | Ngưỡng từ chối H₀ | Không phải là thước đo tầm quan trọng của hiệu ứng |
| **Ý nghĩa thống kê** | Kết quả khó xảy ra chỉ do ngẫu nhiên | KHÔNG có nghĩa là có ý nghĩa thực tế |
| **Kích thước hiệu ứng** | Độ lớn của hiệu ứng quan sát được | Tách khỏi giá trị p; một hiệu ứng nhỏ có thể có ý nghĩa với N |
| **Sức mạnh** | Xác suất từ ​​chối chính xác H₀ sai | Thường nhắm tới 80%+ |
| **Khoảng tin cậy** | Phạm vi giá trị hợp lý cho tham số | CI 95% không có nghĩa là "xác suất 95% giá trị thực nằm trong phạm vi này" |
---

## Các loại lỗi
| | H₀ là đúng | H₀ là sai |
|---|----------||-------------|
| **Từ chối H₀** | Lỗi Loại I (dương tính giả) | ✅ Đúng (đúng dương tính) |
| **Không thể từ chối H₀** | ✅ Đúng (âm tính thật) | Lỗi Loại II (âm tính giả) |
| Lỗi | Biểu tượng | Ý nghĩa |
|-------|--------|---------|
| **Loại I** | α | Kết luận có tác dụng khi không có |
| **Loại II** | β | Thiếu tác dụng thực sự |
---

## Chọn bài kiểm tra phù hợp
| Kịch bản | Kiểm tra | Giả định |
|----------|------|-------------|
| So sánh phương tiện của 2 nhóm | **t-test** (độc lập) | Phân phối chuẩn, phương sai bằng nhau |
| So sánh các phương tiện quan sát theo cặp | **Kiểm tra t theo cặp** | Sự khác biệt được phân phối bình thường |
| So sánh phương tiện của hơn 3 nhóm | **ANOVA** | Phân phối chuẩn, phương sai bằng nhau |
| So sánh phân phối phân loại | **Kiểm tra chi bình phương** | Đủ cỡ mẫu cho mỗi ô |
| So sánh các bản phân phối (phi tham số) | **Mann-Whitney U** | Không có giả định quy tắc |
| So sánh hơn 3 nhóm (không tham số) | **Kruskal-Wallis** | Không có giả định quy tắc |
| Kiểm tra tương quan | **Pearson** (tuyến tính) hoặc **Spearman** (đơn điệu) | Pearson: tính bình thường; Spearman: dựa trên cấp bậc |
| Kiểm tra xem dữ liệu có tuân theo phân phối hay không | **Kolmogorov-Smirnov** | Dữ liệu liên tục |
### Có tham số và không có tham số
| | Tham số | Không tham số |
|---|--------------|---------------|
| **Giả định** | Dữ liệu tuân theo một phân phối cụ thể (thường là bình thường) | Không có giả định phân phối |
| **Sức mạnh** | Cao hơn khi đáp ứng các giả định | Thấp hơn nhưng mạnh mẽ hơn |
| **Khi nào nên sử dụng** | Mẫu lớn, dữ liệu gần đúng | Mẫu nhỏ, dữ liệu sai lệch, dữ liệu thứ tự |
---

## Các bài kiểm tra cụ thể chi tiết
###t-Kiểm tra
So sánh phương tiện của hai nhóm.
| Biến thể | Trường hợp sử dụng |
|----------|----------|
| **T-kiểm tra độc lập** | Hai nhóm riêng biệt (điều trị và kiểm soát) |
| **Kiểm tra t theo cặp** | Cùng một nhóm đo hai lần (trước và sau) |
| **Kiểm tra t một mẫu** | So sánh giá trị trung bình mẫu với giá trị đã biết |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Phân tích phương sai)
So sánh ý nghĩa của 3 nhóm trở lên. Kiểm tra xem ít nhất một nhóm có nghĩa là khác với phần còn lại.
| Loại | Thiết kế |
|------|--------|
| **ANOVA một chiều** | Một biến độc lập có hơn 3 cấp độ |
| **ANOVA hai chiều** | Hai biến độc lập; kiểm tra hiệu ứng tương tác |
| **Các biện pháp lặp lại ANOVA** | Các đối tượng giống nhau được đo trong các điều kiện khác nhau |
Nếu ANOVA có ý nghĩa quan trọng, hãy theo dõi **các bài kiểm tra hậu kiểm** (Tukey's HSD) để tìm ra các nhóm cụ thể khác nhau.
### Kiểm tra Chi-Square
Kiểm tra xem hai biến phân loại có độc lập hay không.
| Trường hợp sử dụng | Ví dụ |
|----------|----------|
| **Kiểm tra tính độc lập** | Giới tính có liên quan đến sở thích sản phẩm không? |
| **Sự phù hợp tốt** | Liệu một cuộn súc sắc có tuân theo sự phân bố đồng đều không? |
**Quy tắc chung**: mỗi ô phải có số lượng dự kiến ​​ít nhất là 5.
---

##Thử nghiệm A/B
Thử nghiệm A/B là ứng dụng thử nghiệm giả thuyết vào các quyết định kinh doanh - thường so sánh điều khiển (A) với biến thể (B).
###Quy trình thiết kế
| Bước | Mô tả |
|------|-------------|
| **1. Xác định giả thuyết** | "Đổi màu nút từ xanh lam sang xanh lục sẽ tăng tỷ lệ nhấp chuột" |
| **2. Chọn số liệu** | Chính: tỷ lệ nhấp chuột. Thứ cấp: tỷ lệ chuyển đổi, doanh thu. |
| **3. Tính cỡ mẫu** | Dựa trên hiệu ứng, công suất tối thiểu có thể phát hiện được (80%) và mức ý nghĩa (5%) |
| **4. Ngẫu nhiên** | Phân công ngẫu nhiên người dùng để kiểm soát và điều trị |
| **5. Chạy thử nghiệm** | Thu thập dữ liệu cho đến khi đạt được cỡ mẫu mục tiêu |
| **6. Phân tích** | So sánh các số liệu bằng cách sử dụng thử nghiệm thống kê thích hợp |
| **7. Quyết định** | Thực hiện nếu có ý nghĩa thống kê và thực tế |
### Tính toán cỡ mẫu
Cỡ mẫu bạn cần phụ thuộc vào:
| Yếu tố | Ảnh hưởng đến cỡ mẫu |
|--------|----------------------|
| **Hiệu ứng phát hiện nhỏ hơn** | Cần thêm mẫu |
| **Sức mạnh cao hơn** | Cần thêm mẫu |
| **Mức ý nghĩa thấp hơn** | Cần thêm mẫu |
| **Phương sai cao hơn** | Cần thêm mẫu |
### Những lỗi thử nghiệm A/B thường gặp
| Sai lầm | Tại sao nó sai |
|----------|---------------|
| **Nhìn trộm sớm** | Kiểm tra kết quả hàng ngày tăng tỷ lệ dương tính giả |
| **Nhiều số liệu không cần chỉnh sửa** | Kiểm tra 20 số liệu ở mức α=0,05 → tình cờ có 1 kết quả dương tính giả |
| **Dừng lại trước mục tiêu N** | Test yếu không phát hiện được tác dụng thật |
| **Bỏ qua tính thời vụ** | Chạy thử nghiệm trong thời gian nghỉ lễ so với tuần bình thường |
| **Bài tập không ngẫu nhiên** | Sai lệch lựa chọn (ví dụ: chỉ định người dùng mới vào điều trị) |
| **Ý nghĩa khó hiểu với tầm quan trọng** | Mức tăng 0,1% có thể có ý nghĩa thống kê nhưng không đáng để vận chuyển |
---

## Nhiều so sánh
Khi bạn chạy nhiều xét nghiệm cùng lúc, khả năng xảy ra ít nhất một kết quả dương tính giả sẽ tăng lên đáng kể.
| Số lượng bài kiểm tra | Xác suất ≥1 Dương tính giả (ở mức α=0,05) |
|-------|-------------------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Sửa lỗi
| Phương pháp | Nó hoạt động như thế nào | Khi nào nên sử dụng |
|--------|-------------|-------------|
| **Bonferroni** | Chia α cho số lần kiểm tra (α/n) | Thận trọng; vài so sánh |
| **Holm-Bonferroni** | Thủ tục xuống bậc; ít bảo thủ hơn | Sử dụng chung |
| **Benjamini-Hochberg (FDR)** | Kiểm soát tỷ lệ phát hiện sai | Nhiều bài kiểm tra; phân tích thăm dò |
---

## Kích thước hiệu ứng
Giá trị P cho bạn biết *liệu* hiệu ứng có tồn tại hay không. Kích thước hiệu ứng cho bạn biết *lớn* nó như thế nào.
| Đo | Dành cho | Giải thích |
|----------|------|---------------|
| **Cohen's ** | Sự khác biệt giữa hai phương tiện | 0,2 = nhỏ, 0,5 = trung bình, 0,8 = lớn |
| **Pearson's** | Tương quan | 0,1 = nhỏ, 0,3 = trung bình, 0,5 = lớn |
| **η² (eta bình phương)** | ANOVA | 0,01 = nhỏ, 0,06 = trung bình, 0,14 = lớn |
| **Tỷ lệ cược** | Kết quả phân loại | 1,0 = không có hiệu lực; >1 hoặc <1 = hiệu ứng |
**Luôn báo cáo kích thước hiệu ứng cùng với giá trị p.** Một kết quả có thể có ý nghĩa thống kê nhưng thực tế là vô nghĩa.
---

## Bayesian vs Người thường xuyên
| Khía cạnh | Người thường xuyên | Bayes |
|--------|-------------|----------|
| **Xác suất** | Tần suất các sự kiện trong thời gian dài | Mức độ niềm tin |
| **Thông số** | Đã sửa nhưng chưa biết | Biến ngẫu nhiên có phân phối |
| **Công dụng** | giá trị p, khoảng tin cậy, kiểm tra giả thuyết | Phân phối sau, khoảng tin cậy |
| **Trước** | Không có niềm tin trước đó được kết hợp | Phân phối trước rõ ràng |
| **Giải thích** | "Nếu chúng ta lặp lại thí nghiệm này nhiều lần..." | "Dựa trên dữ liệu, xác suất là..." |
| **Điểm mạnh** | Khách quan, có căn cứ, đơn giản | Giải thích trực quan, kết hợp kiến ​​thức sẵn có |
| **Điểm yếu** | giá trị p bị hiểu lầm rộng rãi | Lựa chọn trước có thể chủ quan |
---

## Cơ bản về suy luận nhân quả
Sự tương quan không phải là nhân quả. Nhưng đôi khi bạn cần biết *liệu X có gây ra Y* hay không, chứ không chỉ liệu chúng có liên quan với nhau hay không.
| Phương pháp | Mô tả | Khi nào nên sử dụng |
|--------|-------------|-------------|
| **Thí nghiệm ngẫu nhiên** | Tiêu chuẩn vàng; phân công ngẫu nhiên giúp loại bỏ các yếu tố gây nhiễu | Khi bạn có thể chọn ngẫu nhiên |
| **Sự khác biệt trong sự khác biệt (DiD)** | So sánh sự thay đổi theo thời gian giữa điều trị và đối chứng | Thay đổi chính sách, thử nghiệm tự nhiên |
| **Gián đoạn hồi quy (RDD)** | Khai thác ngưỡng cắt | Học bổng, ngưỡng đủ điều kiện |
| **Biến công cụ (IV)** | Sử dụng một công cụ ảnh hưởng đến việc điều trị nhưng không ảnh hưởng trực tiếp đến kết quả | Khi không thể ngẫu nhiên hóa |
| **So khớp điểm xu hướng** | So sánh các đơn vị được xử lý và đối chứng về các đặc điểm được quan sát | Nghiên cứu quan sát |
---

## Những lỗi thống kê thường gặp
| Sai lầm | Mô tả |
|----------|-------------|
| **p-hack** | Thử nhiều phân tích cho đến khi tìm thấy p < 0,05 |
| **HARKing** | Đưa ra giả thuyết sau khi biết kết quả |
| **Thành kiến ​​sống sót** | Chỉ nhìn vào thành công (ví dụ: các công ty thành công) |
| **Nghịch lý Simpson** | Xu hướng đảo ngược khi dữ liệu được tổng hợp và chia theo nhóm |
| **Bỏ qua lãi suất cơ bản** | Bỏ qua xác suất trước khi diễn giải kết quả |
| **Ngụy biện sinh thái** | Suy ra hành vi cá nhân từ dữ liệu cấp nhóm |
| **Thật khó hiểu** | Biến thứ ba giải thích mối quan hệ được quan sát |
| **Trang bị quá mức** | Mô hình thu được tiếng ồn chứ không phải tín hiệu |
---

## Bản tóm tắt
Kiểm tra thống kê là việc đưa ra quyết định trong điều kiện không chắc chắn với sự trung thực về mặt trí tuệ. Luôn nêu giả thuyết của bạn trước khi thu thập dữ liệu. Chọn thử nghiệm phù hợp cho loại dữ liệu của bạn. Báo cáo kích thước hiệu ứng, không chỉ giá trị p. Đúng cho nhiều so sánh. Và hãy nhớ: ý nghĩa thống kê không giống với ý nghĩa thực tế.