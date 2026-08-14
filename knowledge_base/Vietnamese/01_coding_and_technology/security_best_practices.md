<!--
---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Thực tiễn tốt nhất về bảo mật
Hướng dẫn thực tế để bảo mật ứng dụng, cơ sở hạ tầng và dữ liệu — từ quá trình phát triển đến sản xuất.
---

## OWASP Top 10 (2021) — Tổng quan
1. **Kiểm soát quyền truy cập bị hỏng**: Người dùng có thể truy cập các tài nguyên mà họ không nên truy cập.
2. **Lỗi về mật mã**: Mã hóa yếu hoặc bị thiếu.
3. **Tiêm**: SQL, NoSQL, lệnh OS hoặc chèn LDAP.
4. **Thiết kế không an toàn**: Lỗi kiến ​​trúc.
5. **Cấu hình sai bảo mật**: Mật khẩu mặc định, cổng mở, lỗi dài dòng.
6. **Các thành phần dễ bị tổn thương và lỗi thời**: Các CVE đã biết trong các phần phụ thuộc.
7. **Lỗi nhận dạng và xác thực**: Mật khẩu yếu, quản lý phiên kém.
8. **Lỗi về tính toàn vẹn của phần mềm và dữ liệu**: Tấn công chuỗi cung ứng, cập nhật không dấu.
9. **Lỗi giám sát và ghi nhật ký bảo mật**: Không phát hiện thấy vi phạm.
10. **Giả mạo yêu cầu phía máy chủ (SSRF)**: Lạm dụng máy chủ để thực hiện yêu cầu đến hệ thống nội bộ.
---

## Xác thực đầu vào và mã hóa đầu ra
### Quy tắc xác thực
- **Danh sách trắng > Danh sách đen**: Xác định các mẫu được phép (ví dụ: biểu thức chính quy cho email) thay vì chặn các mẫu xấu đã biết.
- **Giới hạn độ dài**: Thực thi độ dài tối đa để ngăn chặn tràn bộ đệm và DoS.
- **Kiểm tra kiểu**: Đảm bảo số nguyên là số nguyên, boolean là boolean.
- **Sử dụng các thư viện đã được kiểm tra kỹ**: Để xác thực email, URL và ngày, hãy sử dụng các thư viện tiêu chuẩn (ví dụ:`email-validator`trong Python,`validator.js`trong Node).
### Mã hóa đầu ra
- **Mã hóa HTML**: Mã hóa`<`,`>`,`&`,`"`,`'`để ngăn chặn XSS.
- **Tham số hóa SQL**: Không bao giờ ghép dữ liệu đầu vào của người dùng vào các truy vấn SQL. Sử dụng các truy vấn được tham số hóa (các câu lệnh đã chuẩn bị sẵn) hoặc ORM.
- **Thoát Shell**: Tránh xây dựng các lệnh shell từ đầu vào của người dùng; nếu không thể tránh khỏi, hãy sử dụng`shlex.quote()`hoặc tương tự.
---

## Xác thực và ủy quyền
### Quản lý mật khẩu
- **Băm**: Lưu trữ mật khẩu bằng thuật toán băm chậm, mạnh: **Argon2id** (ưu tiên), **bcrypt**, **scrypt** hoặc **PBKDF2**.
- **Muối**: Thêm loại muối duy nhất cho mỗi người dùng.
- **Độ dài tối thiểu**: Thực thi ít nhất 12–16 ký tự.
- **MFA (Xác thực đa yếu tố)**: Yêu cầu yếu tố thứ hai (TOTP, SMS, khóa phần cứng) cho các hoạt động nhạy cảm.
- **Giới hạn tỷ lệ**: Ngăn chặn các nỗ lực bạo lực trên các điểm cuối đăng nhập (ví dụ: 5 lần thử mỗi 5 phút cho mỗi IP/người dùng).
### Quản lý phiên
- Sử dụng cookie SameSite, an toàn, chỉ HTTP cho mã thông báo phiên.
- Set appropriate expiration times.
- Vô hiệu hóa các phiên đăng xuất và thay đổi mật khẩu.
- Avoid exposing session IDs in URLs.
### OAuth2 / OIDC
- Sử dụng các thư viện được thiết lập tốt (ví dụ: Authlib, PyJWT, Passport.js, Spring Security).
- Xác thực mã thông báo ID một cách kỹ lưỡng (chữ ký, nhà phát hành, đối tượng, ngày hết hạn).
- Sử dụng các tham số trạng thái để ngăn chặn CSRF.
- Giữ bí mật bí mật của khách hàng.
### JWT (Mã thông báo web JSON)
- **Ký**: Sử dụng RS256 hoặc ES256 (không đối xứng) để bảo mật tốt hơn; HS256 (đối xứng) có thể chấp nhận được nếu các bí mật chung được quản lý tốt.
- **Xác thực**: Luôn xác minh chữ ký, nhà phát hành (`iss`), đối tượng (`aud`) và ngày hết hạn (`exp`).
- **Giữ hết hạn ngắn**: 15–60 phút đối với mã thông báo truy cập; use refresh tokens for longer sessions.
- **Lưu trữ an toàn**: Không bao giờ lưu trữ JWT trong localStorage (dễ bị XSS); use HTTP-only cookies instead.
---

## Bảo mật API
### Xác thực
- Luôn xác thực các lệnh gọi API (ngoại trừ các điểm cuối công khai).
- Ưu tiên khóa API hoặc mã thông báo OAuth2 hơn xác thực cơ bản (gửi thông tin xác thực theo mọi yêu cầu).
### Giới hạn và điều chỉnh tỷ lệ
- Áp dụng giới hạn tốc độ cho mỗi người dùng và mỗi IP để ngăn chặn lạm dụng và DoS.
- Trả về`429 Too Many Requests`với tiêu đề `Retry-After`.
### CORS (Chia sẻ tài nguyên nhiều nguồn gốc)
- Chỉ cho phép nguồn gốc cụ thể (không bao giờ`*`trong sản xuất).
- Xác thực tiêu đề`Origin`ở phía máy chủ.
### Xác thực đầu vào
- Xác thực tất cả các tham số yêu cầu, bao gồm tiêu đề và nội dung.
- Từ chối các trường không mong muốn (`"strict": true`hoặc`additionalProperties: false`trong Lược đồ JSON).
### HTTPS / TLS
- Thực thi HTTPS trong sản xuất.
- Sử dụng HSTS (HTTP Strict Transport Security) để buộc trình duyệt sử dụng HTTPS.
- Sử dụng TLS 1.2 hoặc 1.3 (tắt TLS 1.0/1.1).
---

## Quản lý bí mật
### Không bao giờ có bí mật về mã cứng
- Không cam kết bí mật (khóa API, mật khẩu, URL cơ sở dữ liệu) để kiểm soát nguồn.
- Sử dụng các biến môi trường hoặc các công cụ quản lý bí mật.
### Công cụ
| Công cụ | Mô tả |
|------|-------------|
| **HashiCorp Vault** | Bí mật động, cấp doanh nghiệp |
| **Trình quản lý bí mật AWS / Kho khóa Azure / Trình quản lý bí mật GCP** | Bản địa trên nền tảng đám mây |
| **SOP** | Mã hóa bí mật trong tệp và cam kết chúng (với KMS hoặc GPG) |
| **Bí mật của Docker** | Đối với chế độ Swarm; Bí mật Kubernetes (xem xét trình điều khiển CSI của Secrets Store bên ngoài) |
### Xoay
- Thường xuyên luân chuyển bí mật và tài khoản dịch vụ.
- Tự động xoay nếu có thể.
---

## Quản lý phụ thuộc
### Quét lỗ hổng
| Ngôn ngữ/Nền tảng | Công cụ |
|-------------------|-------|
| **Trăn** | `safety`,`pip-audit`,`bandit`|
| **Nút** | `npm audit`,`yarn audit`,`snyk`|
| **Rỉ sét** |  __BẢO VỆ_6__ |
| **Đi** |  __BẢO VỆ_7__ |
| **Chung** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Đang vá lỗi
- Luôn cập nhật các phần phụ thuộc lên các phiên bản được vá.
- Thiết lập các yêu cầu kéo tự động cho các cập nhật nhỏ/bản vá.
- Xem lại nhật ký thay đổi để tìm những thay đổi vi phạm.
### Tính toàn vẹn của chuỗi cung ứng
- Sử dụng các tệp khóa gói (`package-lock.json`,`Cargo.lock`,`go.sum`) để đảm bảo các bản dựng có thể tái tạo.
- Xác minh tổng kiểm tra các phụ thuộc đã tải xuống.
- Ưu tiên các cơ quan đăng ký chính thức và chỉ tin tưởng các nhà xuất bản đã được xác minh.
---

## An ninh cơ sở hạ tầng
### Tường lửa
- Chặn tất cả các cổng gửi đến ngoại trừ những cổng thực sự cần thiết (ví dụ: 80, 443).
- Giới hạn quyền truy cập SSH vào các dải IP cụ thể (hoặc sử dụng máy chủ VPN/pháo đài).
- Sử dụng nhóm bảo mật (AWS) hoặc NSG (Azure) để kiểm soát chi tiết.
### Tăng cường hệ điều hành
- Áp dụng các bản cập nhật bảo mật thường xuyên (`sudo apt upgrade`,`yum update`).
- Vô hiệu hóa các dịch vụ không cần thiết và tài khoản mặc định.
- Sử dụng Fail2ban để chặn các nỗ lực bạo lực trên SSH.
- Harden SSH: vô hiệu hóa đăng nhập root, sử dụng xác thực dựa trên khóa, thay đổi cổng mặc định (tùy chọn).
### Phân đoạn mạng
- Đặt cơ sở dữ liệu và bộ nhớ đệm trong các mạng con riêng tư không có quyền truy cập internet.
- Sử dụng DMZ cho các dịch vụ công cộng.
- Áp dụng nguyên tắc đặc quyền tối thiểu trong truy cập mạng.
### Bí mật về cơ sở hạ tầng
- Không bao giờ lưu trữ bí mật trong các biến môi trường CI/CD trừ khi được mã hóa.
- Sử dụng vai trò IAM của nhà cung cấp đám mây cho phiên bản EC2/VM thay vì khóa tồn tại lâu dài.
---

## Ghi nhật ký và giám sát
### Đăng nhập những gì
- Sự kiện xác thực (thành công/thất bại).
- Quyết định kiểm soát truy cập (lỗi ủy quyền).
- Hành động của quản trị viên (tạo, xóa người dùng, thay đổi quyền).
- Thay đổi lược đồ cơ sở dữ liệu.
- Lỗi hệ thống và ngoại lệ.
- Yêu cầu và phản hồi API (xử lý lại dữ liệu nhạy cảm).
### Những gì không được đăng nhập
- Mật khẩu, bí mật, mã thông báo, PII (Thông tin nhận dạng cá nhân) trừ khi được băm/tái cấu trúc.
- Số thẻ tín dụng đầy đủ.
### Cảnh báo
- Thiết lập cảnh báo cho:
  - Nhiều lần đăng nhập không thành công (tiềm năng bạo lực).
  - Kiểu truy cập bất thường (ví dụ: từ vị trí mới, vào giờ lẻ).
  - Tài khoản quản trị viên mới được tạo.
  - Tỷ lệ lỗi cao hoặc độ trễ tăng đột biến.
- Sử dụng SIEM (Quản lý sự kiện và thông tin bảo mật) để có mối tương quan nâng cao.
### Lưu giữ nhật ký
- Lưu giữ nhật ký ít nhất 30–90 ngày tùy theo yêu cầu quy định.
- Lưu trữ nhật ký trong một hệ thống tập trung, chống giả mạo (ví dụ: ELK Stack, Splunk, Datadog).
---

## Vòng đời phát triển an toàn (SDL)
1. **Đào tạo**: Đảm bảo các nhà phát triển hiểu được các lỗ hổng phổ biến.
2. **Mô hình hóa mối đe dọa**: Xác định sớm các mối đe dọa tiềm ẩn trong thiết kế.
3. **Tiêu chuẩn mã hóa an toàn**: Thực thi thông qua các danh sách kiểm tra đánh giá mã và linters.
4. **SAST** (Kiểm tra bảo mật ứng dụng tĩnh): Quét mã nguồn để tìm lỗ hổng (SonarQube, CodeQL).
5. **DAST** (Kiểm tra bảo mật ứng dụng động): Quét các ứng dụng đang chạy (OWASP ZAP, Burp Suite).
6. **SCA** (Phân tích thành phần phần mềm): Quét các phần phụ thuộc.
7. **Thử nghiệm thâm nhập**: Các bài tập hack có đạo đức thường xuyên.
8. **Tiền thưởng phát hiện lỗi**: Khuyến khích các nhà nghiên cứu bên ngoài tìm ra các lỗ hổng một cách có trách nhiệm.
9. **Kế hoạch ứng phó sự cố**: Có kế hoạch rõ ràng khi phát hiện vi phạm.
---

## Danh sách kiểm tra khẩn cấp (Khi nghi ngờ có vi phạm)
1. **Đừng hoảng sợ** — mà hãy hành động nhanh chóng.
2. **Cô lập** các hệ thống bị ảnh hưởng (ngắt kết nối mạng nếu cần).
3. **Lưu giữ bằng chứng**: Ghi lại nhật ký, kết xuất bộ nhớ và ảnh đĩa.
4. **Xác định** phạm vi: hệ thống nào, dữ liệu nào.
5. **Xoay vòng** tất cả thông tin xác thực và bí mật bị xâm phạm.
6. **Vá** lỗ hổng.
7. **Thông báo** cho người dùng và cơ quan quản lý bị ảnh hưởng nếu được yêu cầu (trong khung thời gian pháp lý).
8. **Tiến hành khám nghiệm tử thi** để hiểu nguyên nhân cốt lõi và cải thiện quy trình.