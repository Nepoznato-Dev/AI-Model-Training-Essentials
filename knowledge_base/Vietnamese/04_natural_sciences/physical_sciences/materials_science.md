---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to physical_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Khoa học vật liệu
Khoa học vật liệu là nghiên cứu về cách cấu trúc của vật liệu (ở quy mô nguyên tử, vi mô và vĩ mô) xác định các tính chất của nó và cách sử dụng các phương pháp xử lý để kiểm soát cấu trúc đó nhằm đạt được hiệu suất mong muốn. Đó là lĩnh vực giải đáp những câu hỏi như: tại sao thép cứng mà lại nặng? Tại sao thủy tinh trong suốt nhưng dễ vỡ? Làm thế nào chúng ta có thể làm cho pin sạc nhanh hơn? Những vật liệu nào sẽ tồn tại trong điều kiện trên sao Hỏa? Mọi thiết bị công nghệ bạn từng sử dụng đều được làm từ vật liệu và những tiến bộ về công nghệ hầu như luôn đòi hỏi những tiến bộ về vật liệu.
---

## Tứ diện khoa học vật liệu
Bốn yếu tố liên kết với nhau xác định trường:
| Yếu tố | Mô tả |
|----------|-------------|
| **Cấu trúc** | Cách sắp xếp các nguyên tử và phân tử (cấu trúc tinh thể; ranh giới hạt; khuyết tật) |
| **Thuộc tính** | Vật liệu hoạt động như thế nào (cơ, điện, nhiệt, quang, từ) |
| **Đang xử lý** | Cách chế tạo và tạo hình vật liệu (đúc; thiêu kết; pha tạp; ủ) |
| **Hiệu suất** | Vật liệu hoạt động như thế nào trong ứng dụng thực tế |
Thông tin chi tiết quan trọng: việc thay đổi quá trình xử lý sẽ thay đổi cấu trúc, thay đổi thuộc tính, thay đổi hiệu suất.
---

## Các loại vật liệu
### Tổng quan
| Lớp | Liên kết | Thuộc tính chính | Ví dụ |
|-------|----------|---------------|----------|
| **Kim loại** | Kim loại (electron được định vị) | Mạnh; dẻo; dẫn điện; mờ đục | Thép; nhôm; đồng; titan |
| **Gốm sứ** | Ion / cộng hóa trị | Cứng; giòn; chịu nhiệt; cách nhiệt | nhôm; cacbua silic; thủy tinh; sứ |
| **Polyme** | Cộng hóa trị (chuỗi) + van der Waals | Nhẹ; linh hoạt; cách nhiệt; điểm nóng chảy thấp | Polyetylen; nylon; cao su; epoxy |
| **Vật liệu tổng hợp** | Sự kết hợp của hai lớp trở lên | Thuộc tính phù hợp; cường độ cao theo trọng lượng | Sợi cacbon; sợi thủy tinh; bê tông |
| **Chất bán dẫn** | Cộng hóa trị (có tạp chất được kiểm soát) | Độ dẫn có thể điều chỉnh; cơ sở điện tử | Silicon; gecmani; gali arsenua |
| **Vật liệu sinh học** | Nhiều; yêu cầu tương thích sinh học | Tương tác với các hệ thống sinh học | cấy ghép titan; collagen; hydroxyapatite |
---

## Cấu trúc tinh thể
### Cấu trúc tinh thể kim loại phổ biến
| Cấu trúc | Nguyên tử trên mỗi ô đơn vị | Phần đóng gói | Ví dụ |
|----------|-------------------|-----------------|----------|
| **FCC** (Khối lấy mặt làm trung tâm) | 4 | 0,74 (đóng gói gần nhất) | Nhôm; đồng; vàng; niken; austenite (γ-sắt) |
| **BCC** (Khối lấy cơ thể làm trung tâm) | 2 | 0,68 | Sắt (α-sắt); crom; vonfram; molypden |
| **HCP** (Đóng gói hình lục giác) | 6 | 0,74 (đóng gói gần nhất) | Titan; kẽm; magiê; coban |
### Tại sao cấu trúc tinh thể lại quan trọng
| Bất động sản | Ảnh hưởng của cấu trúc tinh thể |
|----------|------------------------------|
| **Sức mạnh** | Hệ trượt (mặt phẳng mà nguyên tử trượt dọc theo) khác nhau về cấu trúc; Kim loại FCC dẻo hơn HCP |
| **Mật độ** | Phần đóng gói xác định mức độ chặt chẽ của các nguyên tử |
| **Biến đổi pha** | Sắt biến đổi từ BCC sang FCC ở 912°C - đây là cơ sở của quá trình xử lý nhiệt thép |
| **Bất đẳng hướng** | Các tính chất có thể thay đổi theo hướng trong tinh thể không lập phương |
---

## Tính chất cơ học
### Các số liệu chính
| Bất động sản | Định nghĩa | Đơn vị | Giá trị tiêu biểu |
|----------|----------||-------|-------|
| **Mô đun Young (E)** | Độ cứng; ứng suất/biến dạng trong vùng đàn hồi | GPa | Thép: 200; nhôm: 70; Cao su: 0,01–0,1 |
| **Sức mạnh năng suất** | Ứng suất tại đó bắt đầu biến dạng vĩnh viễn (dẻo) | MPa | Thép: 250–1000; Nhôm: 40–500 |
| **Độ bền kéo (UTS)** | Căng thẳng tối đa trước khi thất bại | MPa | Thép: 400–2000; Nhôm: 90–600 |
| **Độ dẻo (% độ giãn dài)** | Vật liệu co giãn bao nhiêu trước khi đứt | % | Thép: 10–50; Kính: <1 |
| **Độ dẻo dai** | Năng lượng hấp thụ trước khi gãy (diện tích dưới đường cong ứng suất-biến dạng) | MJ/m³ | Thép: cao; gốm sứ: thấp |
| **Độ cứng** | Khả năng chống lõm bề mặt | Cân khác nhau | Kim cương: cứng nhất; bột talc: mềm nhất |
### Tăng cường cơ chế
| Cơ chế | Nó hoạt động như thế nào | Ví dụ |
|----------|-------------|----------|
| **Sàng lọc hạt** | Hạt nhỏ hơn = ranh giới hạt nhiều hơn = trật khớp di chuyển khó hơn | Mối quan hệ Hall-Petch |
| **Tăng cường dung dịch rắn** | Các nguyên tử lạ làm biến dạng mạng; cản trở chuyển động trật khớp | Thêm kẽm vào đồng → đồng thau |
| **Mưa đông cứng** | Các hạt nhỏ chặn chuyển động trật khớp | Hợp kim nhôm cứng lâu năm |
| **Làm cứng công việc (làm cứng biến dạng)** | Biến dạng dẻo làm tăng mật độ trật khớp; chúng quấn vào nhau và cản trở nhau | Thép cán nguội |
| **Tăng cường tổng hợp** | Các sợi chắc chắn trong nền mềm hơn chịu tải | Polyme gia cố bằng sợi carbon |
---

## Thuộc tính điện và nhiệt
### Độ dẫn điện
| Loại vật liệu | Độ dẫn điện (S/m) | Cơ chế |
|--------------|--------------------|----------|
| **Dây dẫn** (đồng, bạc) | 10^7 – 10^8 | Electron tự do trong liên kết kim loại |
| **Chất bán dẫn** (silicon, GaAs) | 10^-6 – 10^4 | Điều chỉnh bằng doping; kỹ thuật khoảng cách dải |
| **Chất cách điện** (thủy tinh, cao su) | 10^-12 – 10^-20 | Khoảng cách dải lớn; liên kết electron |
| **Chất siêu dẫn** | Vô hạn (dưới nhiệt độ tới hạn) | Điện trở bằng không; Hiệu ứng Meissner |
### Tính chất nhiệt
| Bất động sản | Mô tả | Quan trọng đối với |
|----------|-------------|---------------|
| **Độ dẫn nhiệt** | Nhiệt truyền qua vật liệu tốt như thế nào | Tản nhiệt; cách nhiệt |
| **Giãn nở nhiệt** | Vật liệu nở ra bao nhiêu khi bị nung nóng | Vật liệu phù hợp trong vật liệu tổng hợp; cầu; đường ray |
| **Nhiệt dung riêng** | Năng lượng cần thiết để tăng nhiệt độ thêm 1°C | Lưu trữ năng lượng nhiệt |
| **Điểm nóng chảy** | Nhiệt độ tại đó chất rắn trở thành chất lỏng | Ứng dụng nhiệt độ cao |
---

##Polyme
### Các loại polyme
| Loại | Cấu trúc | Thuộc tính | Ví dụ |
|------|--------------|-------------|--------|
| **Nhựa nhiệt dẻo** | Chuỗi tuyến tính hoặc phân nhánh; lực liên phân tử yếu | Tan chảy khi đun nóng; có thể tái chế | Polyetylen; polystyren; nylon |
| **Bình giữ nhiệt** | Mạng liên kết chéo; liên kết cộng hóa trị giữa các chuỗi | Đừng tan chảy; phân hủy ở nhiệt độ cao | Epoxy; cao su lưu hóa; Bakelite |
| **Chất đàn hồi** | Liên kết chéo nhẹ; dây chuyền cuộn | Kéo dài và trở lại hình dạng | Cao su tự nhiên; silicon; cao su tổng hợp |
### Thuộc tính polyme
| Bất động sản | Mô tả |
|----------|-------------|
| **Nhiệt độ chuyển thủy tinh (Tg)** | Dưới Tg: cứng và giòn. Trên Tg: mềm mại và linh hoạt |
| **Kết tinh** | Các polyme bán tinh thể bền hơn và đục hơn; vô định hình trong suốt |
| **Trọng lượng phân tử** | MW cao hơn = mạnh hơn; khó xử lý hơn |
| **Mức độ trùng hợp** | Số lượng đơn vị monome; ảnh hưởng đến tài sản |
---

## Sơ đồ pha
### Sơ đồ pha sắt-cacbon (Đơn giản hóa)
| Giai đoạn | Hàm lượng cacbon | Cấu trúc | Thuộc tính |
|-------|--------------|-------------|----------|
| **Ferrit (α)** | Lên tới 0,022% | sắt BCC | Mềm mại; dẻo; từ tính |
| **Austenit (γ)** | Lên tới 2,14% | Sắt FCC | Không có từ tính; có thể định hình |
| **Xi măng (Fe₃C)** | 6,67% | Trực thoi | Cứng; giòn |
| **Ngọc trai** | 0,76% (eutectoid) | Các lớp ferit và xi măng xen kẽ | Mạnh; khó khăn |
| **Martensite** | Bất kỳ (được hình thành bằng cách làm nguội nhanh) | BCT (tứ giác lấy cơ thể làm trung tâm) | Rất khó; giòn |
---

## Vật liệu hiện đại và mới nổi
| Chất liệu | Mô tả | Ứng dụng |
|----------|-------------|-------------|
| **Graphene** | Một lớp nguyên tử carbon; vật liệu bền nhất được biết đến; nhạc trưởng xuất sắc | Điện tử; vật liệu tổng hợp; cảm biến |
| **Ống nano cacbon** | Các ống trụ graphene cuộn lại; tỷ lệ sức mạnh trên trọng lượng cực cao | Vật liệu tổng hợp; điện tử; lưu trữ năng lượng |
| **Perovskite** | Cấu trúc tinh thể ABX₃; khoảng cách băng tần có thể điều chỉnh | Pin mặt trời; đèn LED; máy dò |
| **Khung kim loại-hữu cơ (MOF)** | Vật liệu tinh thể xốp; diện tích bề mặt khổng lồ | Kho chứa khí; xúc tác; giao thuốc |
| **Hợp kim nhớ hình** | Trở lại hình dạng ban đầu khi đun nóng | Stent; bộ truyền động; kết cấu tự sửa chữa |
| **Siêu vật liệu** | Cấu trúc vi mô được thiết kế mang lại những đặc tính không có trong tự nhiên | chỉ số khúc xạ âm; che giấu |
| **Hợp kim có entropy cao** | Nhiều yếu tố chính; sự kết hợp bất thường của các thuộc tính | Môi trường khắc nghiệt; hàng không vũ trụ |
---

## Bản tóm tắt
Khoa học vật liệu kết nối cấu trúc nguyên tử của vật liệu với các đặc tính vĩ mô và hiệu suất trong thế giới thực của nó. Kim loại mạnh và dẫn điện nhưng nặng. Gốm sứ cứng và chịu nhiệt nhưng giòn. Polyme nhẹ và linh hoạt nhưng bị giới hạn bởi nhiệt độ. Vật liệu tổng hợp kết hợp tốt nhất của các lớp khác nhau. Cấu trúc tinh thể xác định hành vi cơ học. Gia công - xử lý nhiệt, tạo hợp kim, làm cứng sản phẩm - kiểm soát cấu trúc vi mô và do đó các tính chất. Các vật liệu hiện đại như graphene, perovskites và MOF đã vượt qua ranh giới của những gì có thể. Lĩnh vực này về cơ bản có tính liên ngành: vật lý giải thích liên kết, hóa học giải thích các phản ứng, kỹ thuật giải thích hiệu suất và tất cả những điều đó đều quan trọng đối với mọi công nghệ từ điện thoại thông minh đến tàu vũ trụ.