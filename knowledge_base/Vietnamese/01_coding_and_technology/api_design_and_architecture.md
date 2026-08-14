<!--
---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, architecture, coding-and-technology]
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
# Thiết kế và kiến ​​trúc API
API (Giao diện lập trình ứng dụng) là cách các thành phần phần mềm giao tiếp với nhau. API được thiết kế tốt sẽ trực quan, nhất quán và mang lại niềm vui khi làm việc. Một thiết kế kém sẽ gây ra sự nhầm lẫn, lỗi và sự thất vọng. Tệp này bao gồm các nguyên tắc, mẫu và phương pháp xây dựng API mà nhà phát triển thực sự muốn sử dụng.
---

## Nguyên tắc API REST
REST (Chuyển giao trạng thái đại diện) là phong cách kiến ​​trúc chủ đạo cho các API web. Nó xử lý dữ liệu dưới dạng **tài nguyên** được xác định bởi URL và sử dụng các phương thức HTTP để thao tác trên chúng.
### Nguyên tắc cốt lõi
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Tài nguyên** | Mọi thứ đều là tài nguyên có URI (`/users/123`,`/orders/456`) |
| **Phương thức HTTP** | GET (đọc), POST (tạo), PUT (thay thế), PATCH (cập nhật một phần), DELETE (xóa) |
| **Không quốc tịch** | Mỗi yêu cầu chứa tất cả thông tin cần thiết; không có trạng thái phiên phía máy chủ |
| **Giao diện thống nhất** | Đặt tên tài nguyên nhất quán, phương pháp tiêu chuẩn, mã trạng thái tiêu chuẩn |
| **Đại diện** | Tài nguyên có thể được biểu diễn dưới nhiều định dạng (JSON, XML) |
### Quy ước đặt tên tài nguyên
| Làm | Đừng |
|----|-------|
| `/users`(danh từ số nhiều) | `/user`(số ít) |
| `/users/123/orders`(lồng nhau) |  __BẢO VỆ_3__ |
| `/products?category=electronics`(thông số truy vấn để lọc) |  __BẢO VỆ_5__ |
| Sử dụng dấu gạch nối:`/user-profiles`| Sử dụng dấu gạch dưới:`/user_profiles`|
### Phương thức HTTP và tính tạm thời
| Phương pháp | Mục đích | Bình thường? | An toàn? |
|--------|----------|-------------|-------|
| ** NHẬN ** | Đọc một nguồn tài liệu | ✅ Có | ✅ Có |
| **BÀI ĐĂNG** | Tạo tài nguyên | ❌ Không | ❌ Không |
| **ĐƯA** | Thay thế hoàn toàn một tài nguyên | ✅ Có | ❌ Không |
| ** VÁ ** | Cập nhật một phần tài nguyên | ❌ Không* | ❌ Không |
| **XÓA** | Xóa tài nguyên | ✅ Có | ❌ Không |
*PATCH có thể được thực hiện bình thường với thiết kế cẩn thận.
### Mã trạng thái HTTP
| Mã | Ý nghĩa | Khi nào nên sử dụng |
|------|----------|-------------|
| **200** | được | NHẬN, PUT, PATCH, XÓA thành công |
| **201** | Đã tạo | POST thành công (đã tạo tài nguyên) |
| **204** | Không có nội dung | XÓA thành công (không có gì để trả lại) |
| **400** | Yêu cầu Xấu | Đầu vào không hợp lệ hoặc yêu cầu không đúng định dạng |
| **401** | trái phép | Xác thực bị thiếu hoặc không hợp lệ |
| **403** | Bị cấm | Đã xác thực nhưng không được ủy quyền |
| **404** | Không tìm thấy | Tài nguyên không tồn tại |
| **409** | Xung đột | Tài nguyên trùng lặp hoặc xung đột trạng thái |
| **422** | Thực thể không thể xử lý | JSON hợp lệ nhưng có lỗi ngữ nghĩa |
| **429** | Quá Nhiều Yêu Cầu | Đã vượt quá giới hạn tỷ lệ |
| **500** | Lỗi Máy chủ Nội bộ | Lỗi máy chủ không mong muốn |
| **502** | Cổng xấu | Lỗi dịch vụ ngược dòng |
| **503** | Dịch vụ không có sẵn | Quá tải hoặc bảo trì tạm thời |
---

## Phiên bản API
API phát triển. Khi bạn cần thực hiện những thay đổi đột phá, việc lập phiên bản sẽ cho phép các máy khách hiện tại tiếp tục hoạt động.
| Chiến lược | Ví dụ | Ưu điểm | Nhược điểm |
|----------|----------|------|------|
| **Đường dẫn URL** |  __BẢO VỆ_0__ , __BẢO VỆ_1__ | Đơn giản, rõ ràng | Thay đổi URL theo phiên bản |
| **Tham số truy vấn** |  __BẢO VỆ_2__ | Linh hoạt | Dễ quên |
| **Tiêu đề** |  __BẢO VỆ_3__ | URL sạch | Ít được khám phá hơn |
| **Không có phiên bản** | Chỉ tiến hóa lược đồ | Đơn giản nhất | Những thay đổi đột phá ảnh hưởng đến mọi người |
**Phương pháp tốt nhất**: sử dụng phiên bản đường dẫn URL (`/v1/`) để làm rõ. Hỗ trợ ít nhất một phiên bản trước đó. Loại bỏ các phiên bản cũ với mốc thời gian rõ ràng.
---

## Phương thức xác thực
| Phương pháp | Nó hoạt động như thế nào | Tốt nhất cho |
|--------|-------------|----------|
| **Khóa API** | Khóa bí mật trong tiêu đề (`X-API-Key: abc123`) | Máy chủ đến máy chủ, tích hợp đơn giản |
| **OAuth2** | Ủy quyền dựa trên mã thông báo với phạm vi | Quyền truy cập của bên thứ ba, ứng dụng do người dùng ủy quyền |
| **JWT** | Mã thông báo độc lập có xác nhận quyền sở hữu | Xác thực không trạng thái trên các dịch vụ |
| **Xác thực cơ bản** | Tên người dùng được mã hóa Base64: mật khẩu | Chỉ phát triển - không bao giờ sản xuất nếu không có TLS |
| **Cookie phiên** | ID phiên phía máy chủ trong cookie chỉ HTTP | Ứng dụng web truyền thống |
### Luồng OAuth2 (Đơn giản hóa)
1. Máy khách chuyển hướng người dùng đến máy chủ ủy quyền.
2. Người dùng đăng nhập và cấp quyền.
3. Máy chủ ủy quyền trả về mã ủy quyền.
4. Khách hàng trao đổi mã lấy mã thông báo truy cập (và mã thông báo làm mới tùy chọn).
5. Khách hàng sử dụng mã thông báo truy cập để gọi API.
6. Khi mã truy cập hết hạn, hãy sử dụng mã thông báo làm mới để nhận mã mới.
---

## Kiểu API: REST, GraphQL và gRPC
| Tính năng | NGHỈ LẠI | Đồ thịQL | gRPC |
|----------|------|---------|------|
| **Định dạng dữ liệu** | JSON (thông thường) | JSON | Protobuf (nhị phân) |
| **Điểm cuối** | Nhiều (một cho mỗi tài nguyên) | Điểm cuối duy nhất | Được xác định bởi tệp .proto |
| **Tìm nạp quá mức** | Chung (nhận được nhiều hơn mức cần thiết) | Không có (khách hàng chỉ định các trường) | Không (được xác định theo lược đồ) |
| **Không tìm nạp** | Yêu cầu nhiều cuộc gọi | Không có (nhận chính xác những gì cần thiết) | Không có |
| **Thời gian thực** | WebSockets cần thiết | Đăng ký tích hợp | Truyền phát tích hợp |
| **Bộ nhớ đệm** | Bộ nhớ đệm HTTP hoạt động tự nhiên | Khó lưu vào bộ nhớ đệm hơn | Hạn chế |
| **Đường cong học tập** | Thấp | Trung bình | Trung bình-Cao |
| **Tốt nhất cho** | API công khai, ứng dụng CRUD | Giao diện người dùng phức tạp, ứng dụng di động | Dịch vụ vi mô nội bộ, hiệu suất cao |
---

## Phân trang, lọc và sắp xếp
Đối với các điểm cuối trả về danh sách:
| Kỹ thuật | Ví dụ | Khi nào nên sử dụng |
|----------||----------|-------------|
| **Bù đắp/Giới hạn** |  __BẢO VỆ_0__ | Đơn giản; hoạt động với các tập dữ liệu nhỏ |
| **Dựa trên con trỏ** |  __BẢO VỆ_1__ | Bộ dữ liệu lớn; kết quả nhất quán |
| **Bộ phím** |  __BẢO VỆ_2__ | Rất hiệu quả; yêu cầu khóa duy nhất |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Giới hạn tỷ lệ
Bảo vệ API của bạn khỏi bị lạm dụng và đảm bảo sử dụng hợp lý.
| Chiến lược | Nó hoạt động như thế nào |
|----------|-------------|
| **Cửa sổ cố định** | N yêu cầu trong mỗi khoảng thời gian (ví dụ: 100/giờ) |
| **Cửa sổ trượt** | Nhiều chi tiết hơn; đếm yêu cầu trong cửa sổ cuộn |
| **Nhóm mã thông báo** | Token được thêm vào với tỷ lệ cố định; mỗi yêu cầu tiêu thụ một mã thông báo |
Trả về`429 Too Many Requests`với tiêu đề:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Xử lý lỗi
Phản hồi lỗi nhất quán giúp API hoạt động dễ dàng hơn nhiều:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Nguyên tắc**: sử dụng cấu trúc lỗi nhất quán, bao gồm các thông báo có thể xử lý, sử dụng mã trạng thái HTTP tiêu chuẩn, ghi lỗi phía máy chủ với ID tương quan và không bao giờ để lộ dấu vết ngăn xếp hoặc thông tin chi tiết nội bộ.
---

## Tài liệu API
| Công cụ | Mô tả |
|------|-------------|
| **OpenAPI (Vênh vang)** | Tiêu chuẩn ngành cho tài liệu API REST |
| **Giao diện người dùng vênh vang** | Tài liệu API tương tác từ thông số OpenAPI |
| **Người đưa thư** | Kiểm tra API, tài liệu và chia sẻ bộ sưu tập |
| **Làm lại** | Tài liệu tham khảo API đẹp mắt từ thông số OpenAPI |
| **Sân chơi GraphQL / GraphiQL** | Khám phá GraphQL tương tác |
**Phương pháp hay nhất**: viết thông số OpenAPI trước (phát triển theo thông số kỹ thuật), sau đó tạo tài liệu và SDK ứng dụng khách từ thông số đó.
---

## Mẫu cổng API
Cổng API nằm giữa máy khách và dịch vụ phụ trợ, cung cấp một điểm truy cập duy nhất.
| Trách nhiệm | Mô tả |
|---------------|-------------|
| **Định tuyến** | Yêu cầu trực tiếp tới các dịch vụ phụ trợ thích hợp |
| **Xác thực** | Xác thực mã thông báo ở cấp cổng |
| **Giới hạn tỷ lệ** | Áp dụng giới hạn toàn cầu hoặc cho mỗi khách hàng |
| **Biến đổi** | Chuyển đổi giữa các giao thức (REST ↔ gRPC) |
| **Bộ nhớ đệm** | Lưu trữ các phản hồi chung |
| **Giám sát** | Ghi nhật ký và số liệu tập trung |
| **Cân bằng tải** | Phân phối lưu lượng truy cập trên các phiên bản dịch vụ |
| Công cụ | Loại |
|------|------|
| **Kong** | Cổng API nguồn mở (dựa trên Nginx) |
| **Cổng API AWS** | Được quản lý hoàn toàn, tích hợp với AWS |
| **Quản lý API Azure** | Cổng được quản lý với cổng thông tin dành cho nhà phát triển |
| **Đặc phái viên / Istio** | Lưới dịch vụ có khả năng cổng API |
| **Traefik** | Tự động khám phá, Tích hợp mã hóa |
---

## Webhook
Webhooks cho phép API của bạn đẩy các sự kiện tới khách hàng theo thời gian thực, thay vì bắt khách hàng thăm dò ý kiến ​​về các thay đổi.
| Khía cạnh | Thực hành tốt nhất |
|--------|--------------|
| **Giao hàng** | Yêu cầu POST có tải trọng JSON tới URL của khách hàng |
| **An ninh** | Ký tải trọng với HMAC; khách hàng xác minh chữ ký |
| **Độ tin cậy** | Thử lại việc giao hàng không thành công với thời gian chờ theo cấp số nhân |
| **Idempotence** | Bao gồm ID sự kiện duy nhất; khách hàng xử lý các bản sao |
| **Phiên bản** | Bao gồm phiên bản API trong tải trọng webhook |
---

## Danh sách kiểm tra thiết kế
- [ ] Tài nguyên là danh từ số nhiều (`/users`, không phải`/getUser`)
- [ ] Các phương thức HTTP được sử dụng chính xác (GET để đọc, POST để tạo, v.v.)
- [] Định dạng phản hồi lỗi nhất quán
- [] Phân trang cho tất cả các điểm cuối danh sách
- [] Giới hạn tốc độ với tiêu đề rõ ràng
- [] Chiến lược phiên bản API được xác định
- [ ] Xác thực và ủy quyền tại chỗ
- [ ] Xác thực đầu vào trên tất cả các điểm cuối
- [] Tài liệu OpenAPI/Swagger được duy trì
- [] CORS được cấu hình đúng
- [] HTTPS được thực thi trong sản xuất
- [] Khóa tạm thời cho các hoạt động POST khi cần thiết