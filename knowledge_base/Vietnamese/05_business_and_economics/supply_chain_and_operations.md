<!--
---
# Metadata
title: "Supply Chain and Operations Management"
description: "Inventory management, lean manufacturing, logistics, bullwhip effect"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [supply, chain, operations, business-and-economics]
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

-->
# Quản lý chuỗi cung ứng và vận hành
Quản lý chuỗi cung ứng là sự phối hợp của tất cả các hoạt động liên quan đến tìm nguồn cung ứng, mua sắm, chuyển đổi và hậu cần - từ nguyên liệu thô đến thành phẩm trong tay khách hàng. Quản lý vận hành là hoạt động hàng ngày của các hệ thống sản xuất. Cùng nhau, họ xác định liệu một công ty có thể cung cấp đúng sản phẩm, vào đúng thời điểm, với chi phí phù hợp và chất lượng phù hợp hay không. Đại dịch, tình trạng thiếu chip và tắc nghẽn kênh đã cho thấy chuỗi cung ứng được kết nối toàn cầu và mong manh như thế nào.
---

## Nguyên tắc cơ bản về chuỗi cung ứng
### Luồng chuỗi cung ứng
| Sân khấu | Hoạt động | Mối quan tâm chính |
|-------|----------|-------------|
| **Kế hoạch** | Dự báo nhu cầu; lập kế hoạch cung ứng; S&OP | Sự chính xác; khả năng đáp ứng |
| **Nguồn** | Lựa chọn nhà cung cấp; mua sắm; ký hợp đồng | Trị giá; chất lượng; độ tin cậy; đạo đức |
| **Thực hiện** | Sản xuất; cuộc họp; kiểm soát chất lượng | Hiệu quả; tính linh hoạt; công suất |
| **Giao hàng** | Kho bãi; thực hiện đơn hàng; vận chuyển | Tốc độ; trị giá; độ chính xác |
| **Trở về** | Hậu cần ngược lại; trả lại; tái chế | Sự hài lòng của khách hàng; thu hồi chi phí |
### Các loại chuỗi cung ứng
| Loại | Đặc điểm | Tốt nhất cho |
|------|-------|----------|
| **Hiệu quả** | Công dụng cao; chi phí thấp; dự đoán được | Sản phẩm chức năng có nhu cầu ổn định (tạp hóa) |
| **Đáp ứng** | Dung lượng đệm; linh hoạt; nhanh | Sản phẩm sáng tạo với nhu cầu không chắc chắn (thời trang) |
| **Kiên cường** | Dự phòng; khả năng hiển thị; khả năng thích ứng | Môi trường có rủi ro cao; hàng hóa quan trọng |
| **Nhanh nhẹn** | Trì hoãn; tùy biến hàng loạt | Sản phẩm có tính đa dạng cao, vòng đời ngắn |
| **Gầy** | Loại bỏ chất thải; dựa trên lực kéo; đúng lúc | Âm lượng cao; ít đa dạng; nhu cầu ổn định |
---

## Quản lý hàng tồn kho
### Loại khoảng không quảng cáo
| Loại | Mô tả | Mục đích |
|------|-------------|----------|
| **Nguyên liệu** | Đầu vào chưa được xử lý | Bộ đệm chống lại sự thay đổi nguồn cung |
| **Đang tiến hành (WIP)** | Hàng thành phẩm một phần | Bộ đệm giữa các giai đoạn sản xuất |
| **Thành phẩm** | Sẵn sàng để bán | Bộ đệm chống lại sự thay đổi của nhu cầu |
| **MRO** (Bảo trì, Sửa chữa, Vận hành) | Vật tư cần thiết cho hoạt động | Tiếp tục hoạt động sản xuất |
| **Cổ phiếu an toàn** | Hàng tồn kho bổ sung vượt quá nhu cầu dự kiến ​​| Bảo vệ khỏi sự không chắc chắn |
| **Kiểm kê đường ống** | Đang chuyển tiếp giữa các địa điểm | Không thể tránh khỏi trong quá trình vận chuyển |
### Mô hình quản lý hàng tồn kho
| Người mẫu | Mô tả | Khi nào nên sử dụng |
|-------|-------------|-------------|
| **EOQ** (Số lượng đặt hàng kinh tế) | Kích thước đơn hàng tối ưu giúp giảm thiểu tổng chi phí lưu giữ + đặt hàng | Nhu cầu ổn định; thời gian dẫn liên tục |
| **Điểm đặt hàng lại (ROP)** | Đặt hàng khi hàng tồn kho giảm đến ngưỡng | Xem xét liên tục; dự đoán được nhu cầu |
| **Phân tích ABC** | Phân loại các mục theo giá trị: A (cao), B (trung bình), C (thấp) | Ưu tiên sự quan tâm quản lý |
| **Đúng lúc (JIT)** | Chỉ nhận hàng khi cần thiết trong sản xuất | Chuỗi cung ứng ổn định; độ biến thiên thấp |
| **Hàng tồn kho do nhà cung cấp quản lý (VMI)** | Nhà cung cấp quản lý mức tồn kho | Mối quan hệ nhà cung cấp mạnh mẽ |
| **Ký gửi** | Nhà cung cấp sở hữu hàng tồn kho cho đến khi sử dụng | Giảm chi phí vận chuyển của người mua |
---

## Hệ thống sản xuất
### Phương pháp sản xuất
| Tiếp cận | Mô tả | Khối lượng | Đa dạng | Ví dụ |
|----------|-------------|--------|----------|----------|
| **Cửa hàng việc làm** | Sản phẩm tùy chỉnh; thiết bị đa năng | Thấp | Cao | Cửa hàng máy móc; nội thất tùy chỉnh |
| **Đợt** | Sản xuất theo lô; chuyển đổi giữa các đợt | Trung bình | Trung bình | tiệm bánh; dược phẩm |
| **Sản xuất hàng loạt** | Âm lượng cao; thiết bị chuyên dụng; dây chuyền lắp ráp | Cao | Thấp | Ô tô; điện tử |
| **Dòng chảy liên tục** | Sản xuất không ngừng; hoàn toàn tự động | Rất cao | Rất thấp | Lọc dầu; hóa chất; thép |
| **Tùy chỉnh hàng loạt** | Khối lượng lớn + đa dạng; tự động hóa linh hoạt | Cao | Cao | máy tính Dell; Nike Bởi Bạn |
### Sản xuất tinh gọn
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Giá trị** | Xác định những gì khách hàng coi là có giá trị |
| **Luồng giá trị** | Lập bản đồ tất cả các bước; xác định những thứ làm tăng thêm giá trị |
| **Dòng chảy** | Làm cho các bước tạo ra giá trị diễn ra suôn sẻ mà không bị gián đoạn |
| **Kéo** | Chỉ sản xuất khi khách hàng yêu cầu |
| **Sự hoàn hảo** | Liên tục loại bỏ chất thải (muda) |
### Bảy phế thải (Muda)
| Chất thải | Mô tả | Ví dụ |
|-------|-----------------|---------|
| **Sản xuất thừa** | Làm nhiều hơn mức cần thiết | Sản xuất để dự báo khi nhu cầu không chắc chắn |
| **Đang chờ** | Thời gian nhàn rỗi giữa các bước | Các bộ phận chờ máy tiếp theo |
| **Giao thông** | Di chuyển vật liệu không cần thiết | Di chuyển sản phẩm giữa các kho ở xa |
| **Xử lý quá mức** | Làm nhiều việc hơn mức cần thiết | Kiểm tra bổ sung; tính năng không cần thiết |
| **Hàng tồn kho** | Hàng tồn kho vượt quá mức cần thiết | Dự trữ an toàn "đề phòng" |
| **Chuyển động** | Sự di chuyển không cần thiết của người dân | Đi bộ để lấy dụng cụ; tiếp cận các bộ phận |
| **Khiếm khuyết** | Sản phẩm không đạt quy cách | Làm lại; phế liệu; yêu cầu bảo hành |
---

## Hậu cần và Vận tải
### Phương thức vận chuyển
| Chế độ | Chi phí | Tốc độ | Công suất | Tốt nhất cho |
|------|------|-------|----------|----------|
| **Đường** (xe tải) | Trung bình | Trung bình | Trung bình | Dặm cuối cùng; khu vực; định tuyến linh hoạt |
| **Đường sắt** | Thấp | Trung bình | Cao | Hàng hóa số lượng lớn; đường dài trên đất liền |
| **Hàng hải** (tàu) | Rất thấp | Rất chậm | Rất cao | Quốc tế; số lượng lớn; container |
| **Không khí** | Rất cao | Rất nhanh | Thấp | Giá trị cao; cấp bách; dễ hư hỏng |
| **Đường ống** | Thấp (sau khi xây dựng) | Liên tục | Cao | Dầu; khí đốt; nước |
| **Đa phương thức** | Khác nhau | Khác nhau | Cao | Kết hợp các chế độ; vận chuyển hàng container |
###Thiết kế nhà kho
| Quyết định | Tùy chọn | Đánh đổi |
|----------|----------|----------|
| **Số lượng kho** | Ít (tập trung) và nhiều (khu vực) | Hiệu quả chi phí so với tốc độ giao hàng |
| **Mức độ tự động hóa** | Thủ công, bán tự động và hoàn toàn tự động | Chi phí vốn so với chi phí lao động và độ chính xác |
| **Bố cục** | Dòng chảy chữ U và dòng chảy qua | Sử dụng không gian so với khoảng cách di chuyển |
| **Hệ thống lưu trữ** | Kệ; giá đỡ; NHƯ/RS; băng chuyền | Mật độ so với khả năng tiếp cận và chi phí |
---

## Quản lý rủi ro chuỗi cung ứng
### Rủi ro thường gặp
| Danh mục Rủi ro | Ví dụ | Giảm nhẹ |
|--------------|----------|-------------|
| **Rủi ro nhu cầu** | Lỗi dự báo; hiệu ứng roi da | Dự báo tốt hơn; cảm biến nhu cầu; cổ phiếu an toàn |
| **Rủi ro nguồn cung** | Nhà cung cấp phá sản; thất bại về chất lượng | Tìm nguồn cung ứng kép; kiểm toán nhà cung cấp; cổ phiếu an toàn |
| **Rủi ro hậu cần** | ùn tắc cảng; sự cố của nhà cung cấp dịch vụ | Đa phương thức; tuyến đường thay thế |
| **Rủi ro địa chính trị** | Thuế quan; chiến tranh thương mại; lệnh trừng phạt | Gần bờ; đa dạng hóa các nước tìm nguồn cung ứng |
| **Thiên tai** | Động đất; lụt; đại dịch | Đa dạng hóa về mặt địa lý; kế hoạch kinh doanh liên tục |
| **Rủi ro mạng** | Phần mềm tống tiền; vi phạm dữ liệu | Bảo mật CNTT; hệ thống dự phòng |
### Hiệu ứng Bullwhip
| Nguyên nhân | Mô tả | Giải pháp |
|-------|-------------|----------|
| **Cập nhật dự báo nhu cầu** | Mỗi giai đoạn bổ sung thêm kho an toàn riêng | Chia sẻ dữ liệu điểm bán hàng trên toàn chuỗi |
| **Đơn hàng theo lô** | Đặt hàng định kỳ tạo ra nhu cầu tăng đột biến | Giảm thời gian chu kỳ đặt hàng; EDI |
| **Biến động giá** | Mua kỳ hạn trong thời gian khuyến mãi | Giá thấp hàng ngày; giá cả ổn định |
| **Chơi game theo khẩu phần và thiếu hụt** | Đặt hàng quá nhiều trong thời gian thiếu hụt | Phân bổ dựa trên doanh số bán hàng trong quá khứ; chia sẻ thông tin năng lực |
---

## Xu hướng chuỗi cung ứng hiện đại
| Xu hướng | Mô tả | Tác động |
|-------|-------------|--------|
| **Cặp song sinh kỹ thuật số** | Bản sao ảo của chuỗi cung ứng để mô phỏng | Lập kế hoạch tốt hơn; phân tích kịch bản |
| **Tháp kiểm soát chuỗi cung ứng** | Khả năng hiển thị tập trung trên toàn bộ chuỗi | Phản ứng nhanh hơn với sự gián đoạn |
| **Gần bờ / bạn bè** | Di chuyển sản xuất về gần quê hương hoặc các nước đồng minh | Giảm rủi ro; chi phí cao hơn |
| **Chuỗi cung ứng tuần hoàn** | Thiết kế tái sử dụng, tái sản xuất, tái chế | Tính bền vững; hiệu quả tài nguyên |
| **Cảm biến nhu cầu dựa trên AI** | Học máy trên dữ liệu thời gian thực để dự báo ngắn hạn | Chính xác hơn; phản ứng nhanh hơn |
| **Phương tiện tự hành và máy bay không người lái** | Xe tải tự lái; giao hàng bằng máy bay không người lái | Chi phí thấp hơn; dặm cuối nhanh hơn |
---

## Bản tóm tắt
Quản lý chuỗi cung ứng và vận hành là làm cho dòng hàng hóa vật chất trở nên hiệu quả, đáp ứng nhanh và linh hoạt. Quản lý hàng tồn kho cân bằng giữa chi phí giữ hàng với nguy cơ hết hàng. Hệ thống sản xuất trải dài từ các cửa hàng việc làm (tùy chỉnh, khối lượng thấp) đến dòng chảy liên tục (hàng hóa, khối lượng lớn). Sản xuất tinh gọn giúp loại bỏ lãng phí để nâng cao hiệu quả. Các quyết định về hậu cần - phương thức vận chuyển, vị trí kho, mức độ tự động hóa - xác định chi phí và chất lượng dịch vụ. Quản lý rủi ro giải quyết hiệu ứng bullwhip, thất bại của nhà cung cấp, gián đoạn địa chính trị và thiên tai. Các xu hướng hiện đại như bản sao kỹ thuật số, cảm biến nhu cầu do AI điều khiển và hoạt động gần bờ phản ánh phản ứng của ngành đối với một thế giới ngày càng biến động. Chuỗi cung ứng tốt nhất không chỉ hiệu quả - chúng còn rõ ràng, linh hoạt và sẵn sàng cho sự gián đoạn.