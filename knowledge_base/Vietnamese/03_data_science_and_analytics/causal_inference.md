<!--
---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
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
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#Suy luận nhân quả
Suy luận nhân quả là khoa học xác định liệu một điều có thực sự gây ra một điều khác hay không - chứ không chỉ liệu chúng có tương quan với nhau hay không. Tương quan cho bạn biết rằng hai biến di chuyển cùng nhau. Nhân quả cho bạn biết rằng thay đổi cái này sẽ thay đổi cái kia. Sự khác biệt này có ý nghĩa rất lớn trong y học (loại thuốc này có tác dụng không?), chính sách (sự can thiệp này có làm giảm nghèo không?), kinh doanh (chiến dịch quảng cáo này có làm tăng doanh số bán hàng không?) và khoa học (cơ chế này có giải thích được hiện tượng này không?).
---

## Mối tương quan và quan hệ nhân quả
| Khái niệm | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Tương quan** | Hai biến di chuyển cùng nhau | Doanh số bán kem và tử vong do đuối nước đều tăng trong mùa hè |
| **Nhân quả** | Một biến ảnh hưởng trực tiếp đến một biến khác | Hút thuốc gây ung thư phổi |
| **Thật khó hiểu** | Biến thứ ba gây ra cả | Nắng nóng khiến cả doanh số bán kem lẫn việc bơi lội (và chết đuối) |
| **Nhân quả ngược** | Kết quả thực sự gây ra nguyên nhân được cho là | Người ta mua thực phẩm bổ sung sức khỏe vì họ bị bệnh chứ không phải ngược lại |
| **Tương quan giả** | Mối tình trùng hợp | Mức tiêu thụ phô mai bình quân đầu người tương quan với số ca tử vong do vướng ga trải giường |
---

## Khung kết quả tiềm năng
### Mô hình nhân quả Rubin
| Khái niệm | Mô tả |
|----------|-------------|
| **Kết quả tiềm năng** | Đối với mỗi đơn vị, sẽ có một kết quả nếu được xử lý Y(1) và một kết quả nếu không được xử lý Y(0) |
| **Hiệu quả điều trị** | Sự khác biệt: Y(1) - Y(0) cho một đơn vị nhất định |
| **Vấn đề cơ bản** | Chúng ta không bao giờ có thể quan sát cả Y(1) và Y(0) cho cùng một đơn vị - chúng ta chỉ có thể thấy một |
| **Hiệu quả điều trị trung bình (ATE)** | Hiệu quả điều trị trung bình trên toàn bộ dân số |
| **Phản thực** | Kết quả không được quan sát - điều gì sẽ xảy ra trong điều kiện kia |
### Các giả định chính
| Giả định | Ý nghĩa | Làm thế nào để thỏa mãn |
|----------|---------|-------|
| **Sự thiếu hiểu biết (sự vô căn cứ)** | Việc chỉ định điều trị không phụ thuộc vào kết quả tiềm năng, dựa trên các đồng biến được quan sát | Ngẫu nhiên hóa; đo lường tất cả các yếu tố gây nhiễu |
| **Tích cực (chồng chéo)** | Mọi đơn vị đều có xác suất nhận được một trong hai cách xử lý khác 0 | Kiểm tra sự chồng chéo đồng biến giữa các nhóm |
| **SUTVA** (Giả định giá trị xử lý đơn vị ổn định) | Việc điều trị của một đơn vị không ảnh hưởng đến kết quả của đơn vị khác; điều trị nhất quán | Không can thiệp; không có phiên bản điều trị ẩn |
| **Tính nhất quán** | Kết quả quan sát được bằng kết quả tiềm năng của phương pháp điều trị nhận được | Điều trị được xác định rõ ràng |
---

## Phương pháp suy luận nhân quả
### Phương pháp thực nghiệm
| Phương pháp | Mô tả | Sức mạnh | Hạn chế |
|--------|-------------|----------|----------||
| **Thử nghiệm ngẫu nhiên có kiểm soát (RCT)** | Phân công ngẫu nhiên các đơn vị để xử lý hoặc kiểm soát | Tiêu chuẩn vàng; loại bỏ nhiễu | Đắt; đôi khi phi đạo đức; có thể không khái quát hóa |
| **Thử nghiệm A/B** | RCT trong bối cảnh kinh doanh/công nghệ | Đơn giản; khắt khe | Số liệu ngắn hạn; hiệu ứng mới lạ; nhiễu |
| **Thử nghiệm chuyển đổi ngược** | Điều trị thay thế theo thời gian | Xử lý sự can thiệp trên thị trường | Yêu cầu môi trường ổn định |
### Phương pháp gần như thực nghiệm
| Phương pháp | Mô tả | Giả định chính |
|--------|--------------------------|-------|
| **Sự khác biệt trong sự khác biệt (DiD)** | So sánh sự thay đổi về kết quả giữa nhóm can thiệp và nhóm đối chứng theo thời gian | Xu hướng song song: các nhóm sẽ đi theo cùng một quỹ đạo nếu không được điều trị |
| **Gián đoạn hồi quy (RD)** | So sánh các đơn vị ngay trên và ngay dưới ngưỡng điều trị | Các đơn vị gần điểm cắt có thể so sánh được (như thể ngẫu nhiên) |
| **Biến công cụ (IV)** | Sử dụng một biến có ảnh hưởng đến việc điều trị nhưng không ảnh hưởng đến kết quả ngoại trừ thông qua điều trị | Dụng cụ có tương quan với việc điều trị; chỉ ảnh hưởng đến kết quả thông qua điều trị |
| **Kiểm soát tổng hợp** | Xây dựng tổ hợp có trọng số của các đơn vị điều khiển để phù hợp với đơn vị được xử lý | Kiểm soát tổng hợp thể hiện chính xác phản thực của đơn vị được xử lý |
| **So khớp điểm xu hướng** | So sánh các đơn vị được xử lý và đối chứng có xác suất xử lý tương tự | Tất cả các yếu tố gây nhiễu đều được đo lường và đưa vào mô hình xu hướng |
### Sự khác biệt trong sự khác biệt (Trực quan hóa)
| Thời kỳ | Nhóm được điều trị | Nhóm kiểm soát | Sự khác biệt |
|--------|--------------|---------------|----------||
| **Tiền xử lý** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Sau điều trị** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **Ước tính của DiD** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Đồ thị chu kỳ có hướng (DAG)
DAG là công cụ trực quan để mã hóa các giả định nguyên nhân và xác định các yếu tố gây nhiễu.
### Cấu trúc cơ bản
| Cấu trúc | Mẫu | Hàm ý |
|----------||----------|-------------|
| **Chuỗi** | A → B → C | A và C được liên kết thông qua B; điều khiển B chặn đường |
| **Nĩa** | A ← B → C | A và C bị nhầm lẫn bởi B; điều khiển B chặn đường |
| **Máy va chạm** | A → B ← C | A và C độc lập; kiểm soát B mở đường dẫn (tạo liên kết giả) |
### Quy tắc dành cho DAG
| Quy tắc | Mô tả |
|------|-------------|
| **Tiêu chí cửa sau** | Để ước tính tác động nhân quả của X đối với Y, hãy chặn tất cả các đường dẫn cửa sau (các đường dẫn có mũi tên vào X) bằng cách điều chỉnh các biến thích hợp |
| **Tiêu chí cửa trước** | Nếu không thể chặn đường dẫn cửa sau, hãy sử dụng bộ trung gian: ước tính X → M → Y theo hai giai đoạn |
| **Không điều kiện cho máy va chạm** | Kiểm soát một hiệu ứng chung sẽ mở ra một con đường giả mạo |
| **Đừng đặt điều kiện vào con cháu của máy va chạm** | Vấn đề tương tự như việc điều hòa trên chính máy va chạm |
---

## Những cạm bẫy thường gặp
| Cạm bẫy | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Độ lệch biến bị bỏ qua** | Không kiểm soát được yếu tố gây nhiễu | Ước tính trình độ học vấn → thu nhập mà không kiểm soát khả năng |
| **Kiểm soát quá mức** | Điều hòa trên máy trung gian hoặc máy va chạm | Kiểm soát chức danh công việc khi ước tính trình độ học vấn → thu nhập |
| **Thành kiến ​​lựa chọn** | Điều hòa trên một biến bị ảnh hưởng bởi điều trị | Chỉ phân tích người có việc làm khi học đào tạo → tiền lương |
| **Thành kiến ​​thời gian bất tử** | Phân loại sai thời gian của con người trong các nghiên cứu đoàn hệ | Bệnh nhân phải sống sót đủ lâu để được điều trị |
| **Hồi quy về giá trị trung bình** | Các giá trị cực trị có xu hướng tiến về mức trung bình | Bệnh nhân bệnh cải thiện sau khi điều trị bất kể |
| **Thành kiến ​​sau điều trị** | Điều hòa các biến số xảy ra sau điều trị | Kiểm soát các tác dụng phụ khi ước tính hiệu quả của thuốc |
---

## Công cụ và Thư viện
| Công cụ | Ngôn ngữ | Mô tả |
|------|----------|-------------|
| **Làm Tại sao** | Python | thư viện Microsoft; Suy luận nhân quả dựa trên DAG |
| **Nhân quả** | Python | Thư viện của Uber dành cho mô hình nâng cao và ML nhân quả |
| **EconML** | Python | ML kép, rừng nguyên nhân, biến công cụ |
| **mô hình tuyến tính** | Python | IV, mô hình dữ liệu bảng, DiD |
| **MatchIt** | R | So sánh điểm xu hướng |
| **ngầu** | R/web | phân tích DAG; xác định bộ điều chỉnh |
| **Tác động nhân quả** | R/Python | Chuỗi thời gian cấu trúc Bayes cho suy luận nhân quả |
---

## Bản tóm tắt
Suy luận nhân quả là việc vượt ra ngoài "những gì đã xảy ra" thành "điều gì sẽ xảy ra nếu mọi việc khác đi". Thách thức cơ bản là chúng ta không bao giờ có thể quan sát cả kết quả được xử lý và không được xử lý cho cùng một đơn vị - luôn thiếu kết quả phản thực. Các thí nghiệm ngẫu nhiên giải quyết vấn đề này bằng cách làm cho các nhóm can thiệp và đối chứng có thể so sánh được. Khi không thể ngẫu nhiên hóa, các phương pháp gần như thực nghiệm - DiD, gián đoạn hồi quy, các biến công cụ, kiểm soát tổng hợp - cố gắng tái tạo lại phản thực từ dữ liệu quan sát. DAG giúp đưa ra các giả định rõ ràng và xác định các biến phù hợp để kiểm soát. Kỹ năng quan trọng là suy nghĩ cẩn thận về quá trình tạo dữ liệu: điều gì gây ra điều gì, điều gì gây nhiễu, điều gì là máy va chạm và điều gì sẽ xảy ra trong trường hợp thay thế.