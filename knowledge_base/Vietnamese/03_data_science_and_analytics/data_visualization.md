<!--
---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
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
tags: [data, visualization, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Trực quan hóa dữ liệu
Một biểu đồ được thiết kế tốt có thể tiết lộ các mẫu mà các bảng số ẩn giấu. Một thiết bị được thiết kế kém có thể gây nhầm lẫn, gây nhầm lẫn hoặc nhàm chán. Trực quan hóa dữ liệu là thủ công biến dữ liệu thành những câu chuyện trực quan để đưa ra quyết định. Tệp này bao gồm việc lựa chọn biểu đồ, nguyên tắc thiết kế, các lỗi phổ biến và các công cụ giúp thực hiện được tất cả.
---

## Chọn biểu đồ phù hợp
Quyết định quan trọng nhất trong bất kỳ hình ảnh trực quan nào là chọn loại biểu đồ phù hợp cho dữ liệu và thông điệp của bạn.
### Hướng dẫn lựa chọn biểu đồ
| Mục tiêu của bạn | Các loại biểu đồ tốt nhất |
|----------||-----------------|
| **So sánh danh mục** | Biểu đồ thanh, biểu đồ thanh nhóm |
| **Hiển thị sự thay đổi theo thời gian** | Biểu đồ đường, biểu đồ vùng |
| **Hiển thị phân phối** | Biểu đồ, ô hộp, ô violin |
| **Thể hiện mối quan hệ** | Biểu đồ phân tán, biểu đồ bong bóng |
| **Hiển thị bố cục** | Thanh xếp chồng, biểu đồ hình tròn (giới hạn lát), sơ đồ dạng cây |
| **Hiển thị mối tương quan** | Biểu đồ phân tán, bản đồ nhiệt, biểu đồ cặp |
| **Hiển thị thứ hạng** | Biểu đồ thanh ngang |
| **Hiển thị các mô hình địa lý** | Bản đồ Choropleth, bản đồ chấm |
| **Hiển thị từng phần theo thời gian** | Biểu đồ vùng xếp chồng |
### Khi nào nên sử dụng từng biểu đồ
| Biểu đồ | Điểm mạnh | Tránh Khi |
|-------|--------------|----------|
| **Thanh** | So sánh rõ ràng giữa các danh mục | Quá nhiều danh mục (>15) |
| **Dòng** | Xu hướng theo thời gian; dữ liệu liên tục | Dữ liệu không tuần tự |
| **Tán xạ** | Mối quan hệ giữa hai biến | Quá nhiều điểm trùng lặp |
| **Biểu đồ** | Hình dạng phân phối của một biến | Cỡ mẫu nhỏ (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Nguyên tắc thiết kế
### Ý tưởng cốt lõi của Tufte
Nguyên tắc của Edward Tufte vẫn là tiêu chuẩn vàng cho việc trực quan hóa dữ liệu:
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Tối đa hóa tỷ lệ mực dữ liệu** | Mỗi giọt mực sẽ truyền tải dữ liệu. Loại bỏ mọi thứ khác. |
| **Loại bỏ rác biểu đồ** | Không có hiệu ứng 3D, chuyển màu vô cớ hoặc các yếu tố trang trí. |
| **Hiển thị dữ liệu** | Đừng bóp méo, che giấu hoặc chọn lọc. Hãy để dữ liệu lên tiếng. |
| **Bội số nhỏ** | Sử dụng các biểu đồ nhỏ lặp đi lặp lại để so sánh giữa các danh mục. |
| **Đường lấp lánh** | Biểu đồ nhỏ, có kích thước bằng chữ cho dữ liệu xu hướng nội tuyến. |
### Quy tắc thiết kế thực tế
| Quy tắc | Tại sao |
|------|------|
| **Bắt đầu trục y ở mức 0** (đối với biểu đồ thanh) | Nếu không thì bạn phóng đại sự khác biệt |
| **Gắn nhãn trực tiếp** | Đặt nhãn trên dòng/thanh thay vì sử dụng chú giải khi có thể |
| **Sử dụng màu sắc có mục đích** | Làm nổi bật những gì quan trọng; sử dụng màu xám cho ngữ cảnh |
| **Giữ nó đơn giản** | Một tin nhắn trên mỗi biểu đồ; đừng quá tải |
| **Sử dụng thang đo nhất quán** | Khi so sánh các biểu đồ, hãy giữ nguyên các trục |
| **Đặt hàng ý nghĩa** | Sắp xếp các thanh theo giá trị (không theo thứ tự bảng chữ cái) trừ khi có thứ tự tự nhiên |
| **Cung cấp ngữ cảnh** | Thêm điểm chuẩn, mục tiêu hoặc mức trung bình lịch sử |
### Nguyên tắc về màu sắc
| Trường hợp sử dụng | Tiếp cận |
|----------|----------|
| **Phân loại** | Các màu sắc riêng biệt (xanh dương, cam, xanh lá cây, đỏ) - tối đa 7–8 loại |
| **Tuần tự** | Một màu từ nhạt đến đậm (xanh nhạt → xanh đậm) |
| **Phân kỳ** | Độ dốc hai màu cho dữ liệu có điểm giữa có ý nghĩa (đỏ ← trắng → xanh) |
| **Khả năng tiếp cận** | Thử nghiệm với mô phỏng mù màu; đừng chỉ dựa vào màu sắc (thêm nhãn hoặc mẫu) |
---

## Kể chuyện bằng dữ liệu
Một biểu đồ không có tường thuật thì chỉ là một bức tranh. Kể chuyện biến dữ liệu thành cái nhìn sâu sắc.
### Khung kể chuyện
1. **Bối cảnh**: Tình hình thế nào? Khán giả đã biết gì chưa?
2. **Xung đột**: Vấn đề, sự ngạc nhiên hoặc căng thẳng trong dữ liệu là gì?
3. **Giải pháp**: Khán giả nên làm gì với thông tin chi tiết này?
### Lời khuyên thiết thực
| Mẹo | Mô tả |
|------|-------------|
| **Dẫn đầu bằng sự hiểu biết sâu sắc** | Đặt tiêu đề cho biểu đồ bằng thông tin rút ra chứ không phải dữ liệu ("Doanh thu tăng 30%" chứ không phải "Doanh thu theo quý") |
| **Chú thích các điểm chính** | Thêm chú thích văn bản cho các sự kiện quan trọng hoặc bước ngoặt |
| **Sử dụng tiết lộ lũy tiến** | Hiển thị một biểu đồ tại một thời điểm; xây dựng câu chuyện từng bước |
| **Nổi bật những gì quan trọng** | Sử dụng màu sắc hoặc kích thước để thu hút sự chú ý vào điểm dữ liệu chính |
| **Cung cấp câu hỏi "thì sao?"** | Mỗi biểu đồ phải trả lời một câu hỏi hoặc nhắc nhở hành động |
---

## Những lỗi thường gặp
| Sai lầm | Tại sao nó xấu | Sửa chữa |
|----------|-------------|------|
| **Trục y bị cắt ngắn** | Phóng đại những khác biệt nhỏ | Bắt đầu từ số 0 cho biểu đồ thanh |
| **Khoảng thời gian hái anh đào** | Đánh lừa về xu hướng | Hiển thị đầy đủ phạm vi có sẵn |
| **Quá nhiều màu** | Khiến người xem choáng ngợp | Giới hạn ở mức 5–7; sử dụng màu xám cho ngữ cảnh |
| **Trục y kép** | Ngụ ý mối tương quan có thể không tồn tại | Sử dụng hai biểu đồ riêng biệt |
| **Biểu đồ 3D** | Làm biến dạng tỷ lệ | Luôn sử dụng 2D |
| **Biểu đồ hình tròn có hơn 10 lát** | Không thể so sánh | Thay vào đó hãy sử dụng biểu đồ thanh |
| **Thiếu nhãn** | Người xem không hiểu được biểu đồ | Luôn gắn nhãn trục, tiêu đề và đơn vị |
| **Biểu đồ khu vực gây hiểu lầm** | Các khu vực xếp chồng lên nhau làm sai lệch nhận thức về từng chuỗi riêng lẻ | Sử dụng biểu đồ dạng đường hoặc bội số nhỏ |
---

## Công cụ
### Python
| Thư viện | Sức mạnh |
|----------|----------|
| **matplotlib** | Nền tảng của âm mưu Python; hoàn toàn có thể tùy chỉnh |
| **sinh vật biển** | Trực quan hóa thống kê; những mặc định đẹp đẽ; được xây dựng trên matplotlib |
| **âm mưu** | Biểu đồ tương tác, dựa trên web; bảng điều khiển |
| **Bàn thờ** | Ngữ pháp khai báo đồ họa (Vega-Lite) |
| **bokeh** | Trực quan hóa tương tác cho trình duyệt |
###Javascript/Web
| Thư viện | Sức mạnh |
|----------|----------|
| **D3.js** | Tính linh hoạt tối đa; đường cong học tập dốc |
| **Chart.js** | Biểu đồ đơn giản, đáp ứng |
| **Biểu đồ lại** | Biểu đồ thân thiện với phản ứng |
| **Âm mưu có thể quan sát** | Ngữ pháp đồ họa nhẹ nhàng, biểu cảm |
### Công cụ không có mã / BI
| Công cụ | Loại |
|------|------|
| **Hoạt cảnh** | Phân tích trực quan theo tiêu chuẩn ngành |
| **Power BI** | Hệ sinh thái Microsoft; doanh nghiệp BI |
| **Người nhìn** | Đám mây của Google; thăm dò dữ liệu |
| **Siêu dữ liệu** | Nguồn mở; thiết lập đơn giản |
| **Siêu bộ Apache** | Nguồn mở; SQL gốc |
---

## Thiết kế bảng điều khiển
Bảng thông tin là tập hợp các hình ảnh trực quan cùng nhau kể một câu chuyện hoàn chỉnh về một quy trình, hệ thống hoặc hoạt động kinh doanh.
### Các loại bảng điều khiển
| Loại | Khán giả | Mục đích |
|------|----------|----------|
| **Chiến lược** | Giám đốc điều hành | KPI cấp cao; xu hướng dài hạn |
| **Hoạt động** | Người quản lý | Giám sát thời gian thực; hoạt động hàng ngày |
| **Phân tích** | Nhà phân tích | Thăm dò sâu; lọc, truy sâu |
### Danh sách kiểm tra thiết kế
- **Biết đối tượng của bạn**: Họ sẽ đưa ra quyết định gì từ trang tổng quan này?
- **Quy tắc 5 giây**: Có thể nắm được nội dung chính trong 5 giây không?
- **Bố cục**: Các số liệu quan trọng nhất ở trên cùng bên trái (nơi mà mắt nhìn đầu tiên).
- **Giới hạn loại biểu đồ**: tối đa 3–4 loại trên mỗi trang tổng quan để đảm bảo tính nhất quán.
- **Tương tác theo mặc định**: Bộ lọc, bộ chọn phạm vi ngày, thông tin chi tiết.
- **Hiệu suất**: Trang tổng quan mất >5 giây để tải sẽ không được sử dụng.
- **Di động**: Xem xét thiết kế đáp ứng nếu người dùng cần nó khi đang di chuyển.
---

## Bản tóm tắt
Trực quan hóa dữ liệu tốt là về sự rõ ràng, trung thực và tác động. Chọn biểu đồ phù hợp cho dữ liệu của bạn. Xóa mọi thứ không phục vụ tin nhắn. Sử dụng màu sắc và chú thích để hướng dẫn người xem. Và luôn luôn để dữ liệu kể câu chuyện - không phải ngược lại.