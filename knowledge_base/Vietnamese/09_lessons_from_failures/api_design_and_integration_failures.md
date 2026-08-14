---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Lỗi thiết kế và tích hợp API
API (Giao diện lập trình ứng dụng) là mô liên kết của phần mềm hiện đại — chúng cho phép các dịch vụ giao tiếp, cho phép các bên thứ ba tích hợp và cho phép các nhóm làm việc độc lập. Khi thiết kế API gặp trục trặc, hậu quả sẽ lan ra khắp mọi hệ thống phụ thuộc vào nó: tích hợp bị hỏng, lỗ hổng bảo mật, sự thất vọng của nhà phát triển và việc viết lại tốn kém. Lỗi tích hợp — khi hệ thống không thể giao tiếp một cách đáng tin cậy — là một trong những nguyên nhân phổ biến nhất gây ra sự cố sản xuất.
---

## Lỗi thiết kế API phổ biến
### Lỗi thiết kế
| Sai lầm | Mô tả | Hậu quả |
|----------|-------------|-------------|
| **Đặt tên không nhất quán** | `/getUsers`so với`/list_users`so với`/fetch-users`| Lú lẫn; lỗi; phát triển chậm |
| **Điểm cuối quá tải** | Một điểm cuối thực hiện 10 việc khác nhau dựa trên các tham số | Khó hiểu; khó kiểm tra; khó thay đổi |
| **Không tìm nạp** | Khách hàng cần thực hiện 5 lệnh gọi API để lấy dữ liệu liên quan | Chậm; lãng phí; mã khách hàng phức tạp |
| **Tìm nạp quá mức** | API trả về tất cả các trường khi khách hàng chỉ cần 2 | Lãng phí băng thông; chậm trên thiết bị di động; rủi ro bảo mật (lộ dữ liệu không cần thiết) |
| **Không có phiên bản** | Những thay đổi đột phá được triển khai mà không có cảnh báo | Khách hàng phá vỡ; nhà phát triển tức giận |
| **Thông báo lỗi mơ hồ** | "Lỗi 500: Lỗi Máy chủ Nội bộ" không có thông tin chi tiết | Không thể gỡ lỗi; độ phân giải chậm |
| **Thiếu phân trang** | Điểm cuối trả về tất cả bản ghi (có thể là hàng triệu) | Hết giờ; cạn kiệt trí nhớ; khách hàng bị rơi |
| **Mã trạng thái không nhất quán** | 200 OK nếu có lỗi; 500 cho lỗi của khách hàng | Khách hàng không phân biệt được thành công và thất bại |
### Mẫu chống mẫu REST API
| Chống Mẫu | Mô tả | Cách tiếp cận tốt hơn |
|-------------|-------------|--------|
| **Sử dụng GET cho đột biến** |  __BẢO VỆ_0__ | Sử dụng phương pháp XÓA |
| **Sử dụng POST cho mọi thứ** |  __BẢO VỆ_1__ ;  __BẢO VỆ_2__ | Sử dụng các phương thức HTTP thích hợp (GET, POST, PUT, PATCH, DELETE) |
| **Trả về HTML từ API** | API trả về các đoạn HTML | Trả về JSON; để khách hàng kết xuất |
| **Logic nghiệp vụ trong URL** |  __BẢO VỆ_3__ | Sử dụng tham số truy vấn hoặc nội dung yêu cầu cho các bộ lọc phức tạp |
| **Hiển thị lược đồ cơ sở dữ liệu** |  __BẢO VỆ_4__ | Thiết kế API xoay quanh các tài nguyên và khái niệm miền, không phải bảng |
| **Không có HATEOAS / liên kết** | Khách hàng mã hóa cứng tất cả các URL | Bao gồm các liên kết đến các tài nguyên liên quan trong phản hồi |
---

## Lỗi bảo mật
### Các lỗ hổng API phổ biến
| Dễ bị tổn thương | Mô tả | Ví dụ |
|--------------|-------------|----------|
| **Xác thực bị hỏng** | API không xác minh danh tính đúng cách | Thiếu xác thực mã thông báo; chấp nhận mã thông báo hết hạn |
| **Tiếp xúc dữ liệu quá mức** | API trả về nhiều dữ liệu hơn nhu cầu của khách hàng | Điểm cuối của người dùng trả về giá trị băm mật khẩu và ID nội bộ |
| **Bài tập đại trà** | Khách hàng có thể đặt các trường mà họ không nên đặt | `PATCH /user`cho phép cài đặt`role: "admin"`|
| **Tiêm** | Đầu vào của người dùng được hiểu là mã | tiêm SQL; Tiêm NoSQL; tiêm lệnh |
| **IDOR** (Tham chiếu đối tượng trực tiếp không an toàn) | Truy cập tài nguyên bằng cách thay đổi ID trong URL | `/api/users/5`→ đổi thành`/api/users/6`để xem dữ liệu của người khác |
| **Thiếu giới hạn tỷ lệ** | Không giới hạn lệnh gọi API | Lực lượng vũ phu; từ chối dịch vụ; cạo |
| **Cấu hình sai CORS** | Truy cập nhiều nguồn gốc quá dễ dãi | `Access-Control-Allow-Origin: *`trên các điểm cuối được xác thực |
### Lỗi xác thực và ủy quyền
| Thất bại | Mô tả | Tác động |
|----------|-------------|--------|
| **Thông tin đăng nhập được mã hóa cứng** | Khóa API hoặc mật khẩu trong mã nguồn | Bị rò rỉ thông qua kiểm soát phiên bản; có thể truy cập được cho tất cả các nhà phát triển |
| **Không có mã thông báo hết hạn** | Token không bao giờ hết hạn | Mã thông báo bị đánh cắp cho phép truy cập vĩnh viễn |
| **Khóa bí mật yếu** | Khóa ký ngắn hoặc có thể dự đoán được | Token có thể bị giả mạo |
| **Không có phạm vi / quyền** | Tất cả các token đều có toàn quyền truy cập | Mã thông báo bị xâm phạm = quyền truy cập toàn bộ hệ thống |
| **Ghi nhật ký dữ liệu nhạy cảm** | Mã thông báo hoặc mật khẩu trong nhật ký | Có thể truy cập được đối với bất kỳ ai có quyền truy cập nhật ký |
| **Ủy quyền không nhất quán** | Một số điểm cuối kiểm tra quyền; những người khác thì không | Truy cập trái phép thông qua các điểm cuối không được bảo vệ |
---

## Lỗi tích hợp
### Sự cố tích hợp hệ thống phân tán
| Thất bại | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Khớp nối chặt** | Các dịch vụ phụ thuộc vào chi tiết triển khai nội bộ của nhau | Thay đổi cơ sở dữ liệu của một dịch vụ sẽ làm hỏng ba dịch vụ khác |
| **Chuỗi đồng bộ** | Dịch vụ A gọi B gọi C gọi D; độ trễ tích lũy | 200ms + 300ms + 500ms = Thời gian phản hồi 1 giây |
| **Không có cầu dao** | Dịch vụ không hoạt động gây ra lỗi xếp tầng | Dịch vụ D chậm; tất cả các dịch vụ ngược dòng đã cạn kiệt các luồng chờ đợi |
| **Không có logic thử lại** | Thất bại thoáng qua trở thành vĩnh viễn | Lỗi mạng = giao dịch thất bại; người dùng phải thử lại theo cách thủ công |
| **Thử lại quá nhiều** | Thử lại mà không có thời gian chờ làm dịch vụ khôi phục bị choáng ngợp | Vấn đề bầy đàn sấm sét |
| **Không có quyền bình thường** | Việc thử lại một thao tác không bình thường sẽ tạo ra các bản sao | Thanh toán tính phí hai lần; đơn hàng được tạo hai lần |
| **Sự bất ngờ về tính nhất quán cuối cùng** | Khách hàng đọc dữ liệu cũ sau khi ghi | Hồ sơ cập nhật của người dùng; làm mới trang; dữ liệu cũ vẫn hiển thị |
### Lỗi tích hợp của bên thứ ba
| Thất bại | Mô tả | Giảm nhẹ |
|----------|-------------|-------------|
| **Thay đổi API của nhà cung cấp** | Bên thứ ba thay đổi API của họ mà không cần thông báo | Ghim phiên bản; lớp trừu tượng; giám sát nhật ký thay đổi của nhà cung cấp |
| **Giới hạn tỷ lệ** | Bên thứ ba điều tiết yêu cầu của bạn | Bộ nhớ đệm; yêu cầu xếp hàng; đàm phán giới hạn cao hơn |
| **Nhà cung cấp ngừng hoạt động** | Dịch vụ của bên thứ ba không khả dụng | Bộ ngắt mạch; hành vi dự phòng; chiến lược đa nhà cung cấp |
| **Thay đổi định dạng dữ liệu** | Định dạng phản hồi thay đổi của bên thứ ba | Xác thực lược đồ; lớp chuyển đổi; cảnh báo về thay đổi định dạng |
| **Không dùng nữa mà không có đường dẫn di chuyển** | Nhà cung cấp không dùng điểm cuối không có điểm tương đương | Cập nhật thông tin; duy trì sự trừu tượng; lên kế hoạch di cư sớm |
---

## Nghiên cứu trường hợp
### Case Study 1: API trả về mọi thứ
| Khía cạnh | Mô tả |
|--------|-------------|
| **Kịch bản** | API người dùng của công ty SaaS trả về tất cả các trường người dùng bao gồm siêu dữ liệu nội bộ |
| **Đã xảy ra lỗi gì** | Không lọc trường; phản hồi bao gồm băm mật khẩu, ghi chú nội bộ và cờ quản trị viên |
| **Tác động** | Các nhà nghiên cứu bảo mật đã phát hiện ra sự phơi nhiễm; tiết lộ công khai; Điều tra GDPR |
| **Nguyên nhân gốc rễ** | API tuần tự hóa toàn bộ mô hình cơ sở dữ liệu mà không lọc |
| **Sửa** | Mô hình phản hồi rõ ràng; kiểm soát truy cập cấp trường; đánh giá bảo mật của tất cả các điểm cuối |
| **Bài học** | Không bao giờ hiển thị trực tiếp mô hình cơ sở dữ liệu của bạn thông qua API; sử dụng DTO (Đối tượng truyền dữ liệu) |
### Nghiên cứu trường hợp 2: Thất bại xếp tầng
| Khía cạnh | Mô tả |
|--------|-------------|
| **Kịch bản** | Kiến trúc microservice với khả năng giao tiếp đồng bộ giữa các dịch vụ |
| **Đã xảy ra lỗi gì** | Một dịch vụ gặp phải tình trạng cơ sở dữ liệu bị chậm lại; dịch vụ thượng nguồn chờ phản hồi; nhóm chủ đề cạn kiệt |
| **Tác động** | Toàn bộ hệ thống ngừng hoạt động trong 45 phút; tất cả các dịch vụ bị ảnh hưởng |
| **Nguyên nhân gốc rễ** | Không có bộ ngắt mạch; không có thời gian chờ; chuỗi phụ thuộc đồng bộ |
| **Sửa** | Bộ ngắt mạch; thời gian chờ; giao tiếp không đồng bộ nếu có thể; vách ngăn |
| **Bài học** | Các cuộc gọi đồng bộ giữa các dịch vụ tạo ra các chuỗi dễ vỡ; thiết kế cho sự thất bại |
---

## Các phương pháp hay nhất
### Danh sách kiểm tra thiết kế API
| Khu vực | Thực hành |
|------|----------|
| **Đặt tên** | Sử dụng danh từ cho tài nguyên; Phương thức HTTP cho hành động; quy ước đặt tên nhất quán |
| **Phiên bản** | Phiên bản từ ngày đầu tiên; sử dụng phiên bản URL (`/v1/`) hoặc phiên bản tiêu đề |
| **Phân trang** | Luôn phân trang các điểm cuối của danh sách; sử dụng phân trang dựa trên con trỏ cho các tập dữ liệu lớn |
| **Xử lý lỗi** | Định dạng lỗi nhất quán; bao gồm mã lỗi; cung cấp thông điệp có thể hành động |
| **Giới hạn tỷ lệ** | Thực hiện giới hạn tỷ lệ; trả về 429 với tiêu đề thử lại sau |
| **Idempotence** | Hỗ trợ các khóa bình thường cho điểm cuối đột biến |
| **Tài liệu** | Thông số OpenAPI/Swagger; giữ cho nó được cập nhật; cung cấp ví dụ |
| **Thử nghiệm** | Kiểm tra hợp đồng; kiểm tra tích hợp; thử nghiệm hợp đồng do người tiêu dùng định hướng |
| **Giám sát** | Theo dõi độ trễ; tỷ lệ lỗi; thông lượng; sức khỏe phụ thuộc |
| **Không dùng nữa** | Thông báo trước về việc ngừng sử dụng; cung cấp hướng dẫn di chuyển |
---

## Bản tóm tắt
Lỗi thiết kế API bao gồm từ mỹ phẩm (đặt tên không nhất quán) đến thảm họa (lỗ hổng bảo mật, lỗi xếp tầng). Các lỗi thiết kế phổ biến nhất — điểm cuối quá tải, tìm nạp quá mức, thiếu phân trang, lỗi mơ hồ — khiến API khó sử dụng và bảo trì. Lỗi bảo mật — xác thực bị hỏng, IDOR, gán hàng loạt, lộ dữ liệu quá mức — khiến hệ thống dễ bị tấn công. Lỗi tích hợp - khớp nối chặt chẽ, chuỗi đồng bộ, thiếu bộ ngắt mạch, không có sự ổn định - tạo ra các hệ thống dễ vỡ trong đó một lỗi xảy ra trên các dịch vụ. Tích hợp của bên thứ ba gây thêm rủi ro bên ngoài: thay đổi API, giới hạn tốc độ và thời gian ngừng hoạt động của nhà cung cấp. Các chiến lược phòng ngừa được thiết lập tốt: sử dụng các mô hình phản ứng rõ ràng; phiên bản từ ngày đầu tiên; thực hiện ngắt mạch và thời gian chờ; thiết kế cho sự bình thường; xác nhận và vệ sinh tất cả đầu vào; giám sát mọi thứ; và coi hợp đồng API là thỏa thuận ràng buộc cần có sự phối hợp để thay đổi. Các API tốt nhất đều nhàm chán - có thể dự đoán được, nhất quán, được ghi chép đầy đủ và có khả năng chống chịu thất bại.