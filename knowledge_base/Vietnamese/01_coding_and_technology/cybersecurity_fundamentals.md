---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cybersecurity, coding-and-technology]
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

#Các nguyên tắc cơ bản về an ninh mạng
Bảo mật là một nguyên tắc phải được tích hợp vào mọi lớp của hệ thống ngay từ đầu, thay vì bổ sung thêm sau đó. Cho dù xây dựng một ứng dụng web, quản lý cơ sở hạ tầng hay vận chuyển API, việc hiểu được bối cảnh mối đe dọa và các nguyên tắc cơ bản về phòng thủ là điều cần thiết.
---

## Mã hóa và mật mã
### Mã hóa đối xứng và bất đối xứng
| Loại | Nó hoạt động như thế nào | Tốc độ | Phân phối khóa | Ví dụ |
|------|-------------|-------|-------------------|----------|
| **Đối xứng** | Cùng một khóa để mã hóa và giải mã | Nhanh | Thách thức: làm thế nào để chia sẻ chìa khóa? | AES-256, ChaCha20 |
| **Bất đối xứng** | Mã hóa khóa công khai, giải mã khóa riêng | Chậm hơn | Khóa công khai có thể được chia sẻ công khai | RSA, ECC (Đường cong Elliptic) |
Trong thực tế, hầu hết các hệ thống đều sử dụng **cả hai**: mã hóa bất đối xứng để trao đổi khóa đối xứng một cách an toàn, sau đó mã hóa đối xứng cho phần lớn dữ liệu. Đây là cách TLS/HTTPS hoạt động.
### Băm
Băm là hàm một chiều: nó chuyển đổi đầu vào thành một chuỗi có kích thước cố định. Bạn không thể đảo ngược nó, nhưng cùng một đầu vào luôn tạo ra cùng một đầu ra.
| Trường hợp sử dụng | Thuật toán được đề xuất | Tránh |
|----------|--------------------------|-------|
| **Lưu trữ mật khẩu** | Argon2id, bcrypt, mã hóa | MD5, SHA-1, SHA-256 đơn giản (quá nhanh) |
| **Tính toàn vẹn dữ liệu** | SHA-256, SHA-3 | MD5 (bị hỏng), SHA-1 (bị hỏng) |
| **Chữ ký số** | Ed25519, RSA-2048+ | DSA |
###TLS/HTTPS
HTTPS là HTTP qua TLS (Bảo mật lớp vận chuyển). Nó cung cấp:
- **Mã hóa**: Kẻ nghe trộm không thể đọc được dữ liệu đang truyền.
- **Xác thực**: Máy chủ chứng minh danh tính của mình thông qua chứng chỉ.
- **Tính toàn vẹn**: Không thể sửa đổi dữ liệu trong quá trình truyền mà không bị phát hiện.
Sử dụng TLS 1.2 hoặc 1.3. Tắt TLS 1.0 và 1.1. Bật HSTS (HTTP Strict Transport Security) để buộc trình duyệt luôn sử dụng HTTPS.
---

## Xác thực và ủy quyền
### Xác thực: Bạn là ai?
| Phương pháp | Cấp độ bảo mật | Trường hợp sử dụng |
|--------|--------------||----------|
| **Mật khẩu** | Thấp-Trung bình | Tài khoản cơ bản (thực thi hơn 12 ký tự, kiểm tra vi phạm) |
| **MFA (TOTP)** | Cao | Tiêu chuẩn cho tài khoản nhạy cảm (Google Authenticator, Authy) |
| **Khóa phần cứng (FIDO2/WebAuthn)** | Rất Cao | Tài khoản bảo mật cao (YubiKey) |
| **Sinh trắc học** | Trung bình-Cao | Mở khóa thiết bị (vân tay, khuôn mặt) — yếu tố duy nhất không tốt |
| **OAuth2 / OIDC** | Cao | Đăng nhập của bên thứ ba ("Đăng nhập bằng Google") |
**Quy tắc mật khẩu**: thực thi độ dài tối thiểu (12–16 ký tự), kiểm tra danh sách mật khẩu bị vi phạm, sử dụng Argon2id hoặc bcrypt để băm bằng muối cho mỗi người dùng.
### Ủy quyền: Bạn có thể làm gì?
| Người mẫu | Mô tả | Ví dụ |
|-------|-----------------|---------|
| **RBAC** (Kiểm soát truy cập dựa trên vai trò) | Quyền được gán cho vai trò; người dùng nhận vai trò | Quản trị viên, Biên tập viên, Người xem |
| **ABAC** (Dựa trên thuộc tính) | Quy tắc dựa trên thuộc tính người dùng, tài nguyên, môi trường | "Người quản lý có thể phê duyệt yêu cầu của nhóm mình" |
| **ACL** (Danh sách kiểm soát truy cập) | Quyền rõ ràng cho mỗi người dùng/tài nguyên | Quyền truy cập tệp (đọc/ghi/thực thi) |
**Nguyên tắc đặc quyền tối thiểu**: chỉ cung cấp cho mọi người dùng, dịch vụ và quy trình quyền truy cập tối thiểu mà họ cần.
### JWT (Mã thông báo web JSON)
| Khía cạnh | Khuyến nghị |
|--------|--------------|
| **Ký** | Ưu tiên RS256 hoặc ES256 (không đối xứng); HS256 được chấp nhận với các bí mật được quản lý |
| **Hết hạn** | 15–60 phút đối với mã thông báo truy cập; sử dụng mã thông báo làm mới cho phiên dài hơn |
| **Lưu trữ** | Cookie chỉ HTTP (không phải localStorage - dễ bị XSS) |
| **Xác thực** | Luôn xác minh chữ ký, nhà phát hành, đối tượng và ngày hết hạn |
---

##Top 10 OWASP (2021)
OWASP Top 10 là tài liệu nhận thức tiêu chuẩn về bảo mật ứng dụng web. Nó đại diện cho những rủi ro nghiêm trọng nhất:
| # | Rủi ro | Ý nghĩa của nó |
|---|------|--------------|
| 1 | **Kiểm soát truy cập bị hỏng** | Người dùng có thể truy cập các tài nguyên mà họ không nên truy cập |
| 2 | **Lỗi mật mã** | Mã hóa yếu hoặc thiếu đối với dữ liệu nhạy cảm |
| 3 | **Tiêm** | SQL, NoSQL, lệnh OS hoặc chèn LDAP |
| 4 | **Thiết kế không an toàn** | Những lỗi kiến ​​trúc không thể sửa được khi triển khai |
| 5 | **Cấu hình bảo mật sai** | Mật khẩu mặc định, cổng mở, thông báo lỗi dài dòng |
| 6 | **Thành phần dễ bị tổn thương** | CVE đã biết trong phần phụ thuộc |
| 7 | **Lỗi xác thực** | Mật khẩu yếu, quản lý phiên kém |
| 8 | **Thất bại về tính toàn vẹn** | Tấn công chuỗi cung ứng, cập nhật không dấu |
| 9 | **Lỗi ghi nhật ký/giám sát** | Không phát hiện vi phạm |
| 10 | **SSRF** | Server bị lừa gửi yêu cầu tới hệ thống nội bộ |
---

## Thực hành mã hóa an toàn
### Xác thực đầu vào
| Quy tắc | Tại sao |
|------|------|
| **Danh sách trắng > Danh sách đen** | Xác định những gì được phép, không phải những gì bị chặn |
| **Truy vấn được tham số hóa** | Không bao giờ ghép nối đầu vào của người dùng vào SQL - sử dụng các câu lệnh đã chuẩn bị sẵn hoặc ORM |
| **Mã hóa HTML** | Mã hóa`<`,`>`,`&`,`"`,`'`để ngăn chặn XSS |
| **Thoát Shell** | Tránh xây dựng các lệnh shell từ đầu vào của người dùng; sử dụng`shlex.quote()`|
| **Giới hạn độ dài** | Thực thi độ dài tối đa để ngăn chặn lỗi tràn bộ đệm và DoS |
| **Kiểm tra kiểu** | Đảm bảo số nguyên là số nguyên, booleans là booleans |
### Các lỗ hổng phổ biến
| Dễ bị tổn thương | Tấn công | Phòng thủ |
|--------------|--------|---------|
| **Tiêm SQL** | `' OR 1=1 --`ở dạng đăng nhập | Truy vấn được tham số hóa |
| **XSS** | `<script>alert('hacked')</script>`trong trường nhận xét | Mã hóa đầu ra, Chính sách bảo mật nội dung |
| **CSRF** | Lừa trình duyệt của người dùng thực hiện yêu cầu trái phép | Mã thông báo CSRF, cookie SameSite |
| **Truyền tải đường dẫn** | `../../etc/passwd`trong tham số tệp | Xác thực và vệ sinh đường dẫn tệp |
| **IDOR** | Đổi`/user/123`thành`/user/124`để xem dữ liệu của người khác | Kiểm tra ủy quyền theo mọi yêu cầu |
---

## An ninh mạng
### Tường lửa
| Loại | Mô tả |
|------|-------------|
| **Lọc gói** | Quy tắc dựa trên IP, cổng, giao thức |
| **Trạng thái** | Theo dõi trạng thái kết nối; lọc thông minh hơn |
| **Cấp ứng dụng (WAF)** | Kiểm tra lưu lượng HTTP; chặn SQL SQL, XSS, v.v. |
| **Nhóm bảo mật đám mây** | Tường lửa ảo cho phiên bản đám mây (AWS SG, Azure NSG) |
**Quy tắc chung**: chặn tất cả lưu lượng truy cập vào theo mặc định; chỉ mở những gì thực sự cần thiết (80, 443 cho web).
### Phân đoạn mạng
Đặt cơ sở dữ liệu và bộ nhớ đệm trong các mạng con riêng tư không có quyền truy cập internet trực tiếp. Sử dụng DMZ cho các dịch vụ công khai (máy chủ web, bộ cân bằng tải). Áp dụng nguyên tắc đặc quyền tối thiểu để truy cập mạng.
---

## Quản lý bí mật
### Nguyên tắc vàng
**Không bao giờ mã hóa bí mật.** Không có khóa API, mật khẩu hoặc URL cơ sở dữ liệu trong mã nguồn. Không có bí mật nào trong các biến môi trường được cam kết với Git. Không có bí mật trong hình ảnh Docker.
### Công cụ
| Công cụ | Loại | Tốt nhất cho |
|------|------|----------|
| **HashiCorp Vault** | Người quản lý bí mật doanh nghiệp | Bí mật động, mã hóa như một dịch vụ |
| **Trình quản lý bí mật AWS** | Bản địa trên nền tảng đám mây | Môi trường AWS |
| **Kho khóa Azure** | Bản địa trên nền tảng đám mây | Môi trường Azure |
| **SOP** | Tập tin được mã hóa | Mã hóa bí mật trong Git (bằng KMS hoặc GPG) |
| **Bí mật của Docker** | Vùng chứa gốc | Docker Swarm (đối với K8, hãy xem xét Secrets Store CSI) |
| **dotenv (.env)** | Phát triển địa phương | Chỉ phát triển - chưa bao giờ được sản xuất hoặc cam kết |
### Xoay
Xoay bí mật thường xuyên và tự động. Nếu một bí mật bị rò rỉ (ví dụ: được đưa vào một kho lưu trữ công khai), hãy xoay nó ngay lập tức - ngay cả khi bạn nghĩ rằng không ai nhìn thấy nó.
---

## Bảo mật phụ thuộc
Ứng dụng của bạn chỉ an toàn như phần phụ thuộc yếu nhất của nó.
### Công cụ quét
| Ngôn ngữ | Công cụ |
|----------|-------|
| **Trăn** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Rỉ sét** | `cargo audit`|
| **Đi** | `govulncheck`|
| **Chung** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Tính toàn vẹn của chuỗi cung ứng
- Sử dụng các tệp khóa (`package-lock.json`,`Cargo.lock`,`go.sum`) cho các bản dựng có thể tái tạo.
- Xác minh tổng kiểm tra các phụ thuộc đã tải xuống.
- Ưu tiên đăng ký chính thức và nhà xuất bản đã được xác minh.
- Tự động cập nhật bản vá/nhỏ thông qua Dependabot hoặc Renovate.
---

## Vòng đời phát triển bảo mật (SDL)
| Giai đoạn | Hoạt động |
|-------|----------|
| **Đào tạo** | Đảm bảo các nhà phát triển hiểu các lỗ hổng phổ biến |
| **Mô hình hóa mối đe dọa** | Xác định các mối đe dọa tiềm ẩn trong quá trình thiết kế |
| **Tiêu chuẩn mã hóa an toàn** | Thực thi thông qua danh sách kiểm tra đánh giá mã và linters |
| **SAST** | Phân tích tĩnh mã nguồn (SonarQube, CodeQL) |
| **CHÚT** | Phân tích động của ứng dụng đang chạy (OWASP ZAP, Burp Suite) |
| **SCA** | Phân tích thành phần phần mềm - quét phụ thuộc |
| **Thử nghiệm thâm nhập** | Các bài tập hack đạo đức thường xuyên |
| **Tiền thưởng lỗi** | Khuyến khích các nhà nghiên cứu bên ngoài tìm ra lỗ hổng |
| **Kế hoạch ứng phó sự cố** | Có kế hoạch rõ ràng khi phát hiện vi phạm |
---

## Danh sách kiểm tra khẩn cấp
Khi bạn nghi ngờ có vi phạm:
1. **Đừng hoảng sợ** — nhưng hãy hành động nhanh chóng.
2. **Cô lập** các hệ thống bị ảnh hưởng (ngắt kết nối khỏi mạng nếu cần).
3. **Bảo quản bằng chứng**: ghi lại nhật ký, kết xuất bộ nhớ, ảnh đĩa.
4. **Xác định phạm vi**: hệ thống nào, dữ liệu nào?
5. **Xoay vòng** tất cả thông tin xác thực và bí mật bị xâm phạm.
6. **Vá** lỗ hổng.
7. **Thông báo** cho người dùng và cơ quan quản lý bị ảnh hưởng nếu được yêu cầu (trong khung thời gian pháp lý).
8. **Sau khi khám nghiệm**: ghi lại nguyên nhân gốc rễ và các mục hành động trong vòng 24–48 giờ.