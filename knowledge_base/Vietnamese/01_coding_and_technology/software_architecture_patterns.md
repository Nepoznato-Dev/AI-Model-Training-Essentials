<!--
---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
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
# Các mẫu kiến ​​trúc phần mềm
Kiến trúc là tập hợp các quyết định mang tính cấu trúc về cách tổ chức một hệ thống - nó có những thành phần nào, chúng giao tiếp như thế nào và trách nhiệm nằm ở đâu. Kiến trúc tốt làm cho hệ thống dễ hiểu, dễ sửa đổi và có thể mở rộng quy mô. Kiến trúc tồi khiến mọi thay đổi trở thành một cuộc đấu tranh. Tệp này bao gồm các mẫu chính, thời điểm sử dụng từng mẫu và những cân nhắc liên quan.
---

## Monolith vs microservice
Đây là quyết định kiến ​​trúc cơ bản nhất và cần phải thực hiện đúng.
| Khía cạnh | Đá nguyên khối | Dịch vụ vi mô |
|--------|----------|---------------|
| **Cấu trúc** | Đơn vị có thể triển khai đơn lẻ | Nhiều dịch vụ nhỏ, có thể triển khai độc lập |
| **Dữ liệu** | Cơ sở dữ liệu dùng chung | Mỗi dịch vụ sở hữu dữ liệu của nó |
| **Giao tiếp** | Lệnh gọi hàm trong quá trình | Cuộc gọi mạng (HTTP, gRPC, nhắn tin) |
| **Tỷ lệ** | Mở rộng quy mô toàn bộ ứng dụng | Mở rộng quy mô dịch vụ riêng lẻ |
| **Triển khai** | Chu kỳ phát hành đơn | Triển khai độc lập |
| **Độ phức tạp** | Đơn giản hơn để phát triển ban đầu | Độ phức tạp trong vận hành (kết nối mạng, giám sát) |
| **Tốt nhất cho** | Nhóm nhỏ, sản phẩm giai đoạn đầu | Đội ngũ lớn, miền phức tạp, quy mô cao |
### Khi nào nên bắt đầu với Monolith
Hầu hết các ứng dụng sẽ bắt đầu dưới dạng nguyên khối. Việc xây dựng, thử nghiệm, triển khai và gỡ lỗi sẽ đơn giản hơn. Bạn luôn có thể trích xuất các dịch vụ sau này khi bạn có bức tranh rõ ràng hơn về ranh giới miền của mình. Điều này đôi khi được gọi là "đá nguyên khối mô-đun" — một khối nguyên khối có ranh giới bên trong rõ ràng giúp việc trích xuất sau này trở nên dễ dàng.
### Khi nào nên sử dụng microservice
Hãy xem xét microservice khi:
- Các đội đủ lớn nên việc phối hợp trở thành một nút thắt cổ chai.
- Các phần khác nhau của hệ thống có yêu cầu mở rộng rất khác nhau.
- Bạn cần triển khai độc lập các thành phần.
- Tên miền của bạn có bối cảnh giới hạn rõ ràng (xem DDD bên dưới).
---

## Kiến trúc lớp (N-Tier)
Mẫu kiến ​​trúc phổ biến nhất. Mã được tổ chức thành các lớp, mỗi lớp có một trách nhiệm cụ thể.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Lớp | Trách nhiệm | Quy tắc |
|-------|--------------||------|
| **Trình bày** | Xử lý các yêu cầu của người dùng/HTTP | Chỉ có thể gọi lớp Ứng dụng |
| **Ứng tuyển** | Sắp xếp các trường hợp sử dụng | Có thể gọi lớp Domain |
| **Miền** | Logic kinh doanh cốt lõi | Không nên phụ thuộc vào các lớp khác |
| **Cơ sở hạ tầng** | Những lo ngại về kỹ thuật | Triển khai các giao diện được xác định trong Domain |
**Quy tắc chính**: sự phụ thuộc hướng vào bên trong. Lớp Miền không biết về cơ sở dữ liệu hoặc khung web.
---

## Kiến trúc hướng sự kiện
Các thành phần giao tiếp bằng cách phát ra và phản ứng với **sự kiện** — những điều đã xảy ra.
| Mẫu | Mô tả |
|----------|-------------|
| **Thông báo sự kiện** | Dịch vụ A phát ra "OrderPlaced"; dịch vụ B, C, D phản ứng |
| **Tìm nguồn cung ứng sự kiện** | Lưu trữ tất cả các thay đổi trạng thái dưới dạng một chuỗi sự kiện (không chỉ trạng thái hiện tại) |
| **CQRS** | Tách mô hình đọc (truy vấn) khỏi mô hình ghi (lệnh) |
### Tìm nguồn cung ứng sự kiện
Thay vì lưu trữ "trạng thái hiện tại" trong cơ sở dữ liệu, hãy lưu trữ mọi thay đổi trạng thái dưới dạng sự kiện:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Lợi ích: quá trình kiểm tra hoàn chỉnh, khả năng tái tạo lại bất kỳ trạng thái nào trong quá khứ, người tiêu dùng tách rời. Thách thức: phát triển lược đồ sự kiện, tính nhất quán cuối cùng, độ phức tạp của việc gỡ lỗi.
### CQRS (Phân chia trách nhiệm truy vấn lệnh)
| Bên | Mục đích | Cơ sở dữ liệu |
|------|----------|----------|
| **Lệnh (Ghi)** | Xử lý đột biến; thực thi các quy tắc kinh doanh | Tối ưu hóa cho việc ghi (chuẩn hóa) |
| **Truy vấn (Đọc)** | Phục vụ yêu cầu đọc | Tối ưu hóa cho việc đọc (không chuẩn hóa) |
CQRS kết hợp một cách tự nhiên với Tìm nguồn cung ứng sự kiện: các sự kiện từ phía ghi được chiếu vào các chế độ xem được tối ưu hóa cho việc đọc.
---

## Hàng đợi tin nhắn và nhà môi giới sự kiện
Khi các dịch vụ cần giao tiếp không đồng bộ, hàng đợi tin nhắn là xương sống.
| Công cụ | Loại | Tốt nhất cho |
|------|------|----------|
| **Apache Kafka** | Nhật ký sự kiện được phân phối | Truyền phát sự kiện thông lượng cao, tìm nguồn cung ứng sự kiện |
| **ThỏMQ** | Môi giới tin nhắn với định tuyến | Hàng đợi nhiệm vụ, mẫu định tuyến phức tạp |
| **SQS của AWS** | Hàng đợi được quản lý | Dựa trên AWS, xếp hàng đơn giản |
| **AWS SNS** | Thông báo xuất bản/phụ | Fan-out cho nhiều người đăng ký |
| **Nhà xuất bản/Sub của Google** | Quản lý quán rượu/phụ | Phát trực tuyến sự kiện gốc GCP |
| **Luồng Redis** | Luồng nhẹ | Các trường hợp sử dụng bộ nhớ đệm, ghi nhật ký sự kiện đơn giản |
### Mẫu tin nhắn
| Mẫu | Mô tả |
|----------|-------------|
| **Điểm-điểm** | Một nhà sản xuất, một người tiêu dùng cho mỗi tin nhắn |
| **Xuất bản/Đăng ký** | Một nhà sản xuất, nhiều người đăng ký |
| **Yêu cầu/Trả lời** | Kiểu đồng bộ qua vận chuyển không đồng bộ |
| **Hàng đợi thư chết** | Các thư không được xử lý sẽ được chuyển đến một hàng đợi riêng để kiểm tra |
---

## Thiết kế hướng tên miền (DDD)
DDD là một cách tiếp cận chiến lược để thiết kế phần mềm tập trung vào mã xung quanh các khái niệm kinh doanh hơn là các vấn đề kỹ thuật.
### Các khái niệm chính
| Khái niệm | Mô tả |
|----------|-------------|
| **Ngữ cảnh bị giới hạn** | Ranh giới trong đó mô hình miền nhất quán (ví dụ: "Đặt hàng", "Giao hàng", "Thanh toán") |
| **Ngôn ngữ phổ biến** | Từ vựng được chia sẻ giữa các nhà phát triển và chuyên gia tên miền |
| **Tập hợp** | Các cụm thực thể liên quan được coi là một đơn vị duy nhất để thay đổi dữ liệu |
| **Thực thể** | Các đối tượng có danh tính (ví dụ: Người dùng có user_id) |
| **Đối tượng giá trị** | Đối tượng không có danh tính; được xác định bởi các thuộc tính của chúng (ví dụ: Tiền, Địa chỉ) |
| **Sự kiện trên miền** | Đã xảy ra sự cố trong miền (ví dụ: OrderPlaced) |
| **Lớp chống tham nhũng** | Lớp dịch giữa miền của bạn và các hệ thống bên ngoài |
### Khi DDD trợ giúp
DDD có giá trị nhất khi lĩnh vực kinh doanh phức tạp - hãy nghĩ đến thương mại điện tử, hậu cần, dịch vụ tài chính, chăm sóc sức khỏe. Nếu miền của bạn đơn giản (blog, ứng dụng việc cần làm) thì DDD là quá mức cần thiết.
---

## Chiến lược bộ nhớ đệm
Bộ nhớ đệm là một trong những cách hiệu quả nhất để cải thiện hiệu suất, nhưng nó gây ra sự phức tạp xung quanh tính nhất quán.
| Chiến lược | Mô tả | Đánh đổi |
|----------|-------------|----------|
| **Bỏ bộ nhớ đệm** | Ứng dụng kiểm tra bộ đệm trước; tải từ DB khi bỏ lỡ | Đơn giản; tính nhất quán cuối cùng |
| **Viết qua** | Ghi đồng thời vào bộ đệm và DB | Nhất quán; viết chậm hơn |
| **Viết-Đằng Sau** | Ghi vào bộ đệm; ghi không đồng bộ vào DB | Viết nhanh; nguy cơ mất dữ liệu |
| **Đọc qua** | Tải bộ nhớ đệm từ DB khi bị trượt một cách minh bạch | Đơn giản hơn việc bỏ bộ nhớ đệm |
### Cần lưu vào bộ nhớ cache nội dung gì
| Lớp | Cái gì | Công cụ |
|-------|------|-------|
| **CDN** | Nội dung tĩnh, phản hồi API | CloudFront, Cloudflare |
| **Ứng tuyển** | Kết quả tính toán, dữ liệu phiên | Redis, Memcached |
| **Cơ sở dữ liệu** | Kết quả truy vấn, dòng truy cập thường xuyên | Bộ đệm truy vấn, chế độ xem cụ thể |
**Việc vô hiệu hóa bộ nhớ đệm** nổi tiếng là khó. Các chiến lược phổ biến: TTL (thời gian tồn tại), vô hiệu hóa theo sự kiện (xóa bộ nhớ đệm khi thay đổi dữ liệu) và trục xuất LRU (ít được sử dụng gần đây nhất).
---

## Mẫu thiết kế
### Nguyên tắc RẮN
| Nguyên tắc | Ý nghĩa của nó |
|----------||--------------|
| **S** — Trách nhiệm duy nhất | Một lớp nên có một lý do để thay đổi |
| **O** — Mở/Đóng | Mở để mở rộng, đóng để sửa đổi |
| **L** — Thay thế Liskov | Các kiểu con phải được thay thế cho các kiểu cơ sở của chúng |
| **I** — Phân chia giao diện | Nhiều giao diện cụ thể > một giao diện đa năng |
| **D** — Đảo ngược phụ thuộc | Phụ thuộc vào sự trừu tượng, không phải sự cụ thể hóa |
### Các mẫu phổ biến
| Mẫu | Ý định | Ví dụ |
|--------------|--------|---------|
| **Độc thân** | Đảm bảo một lớp chỉ có một phiên bản | Nhóm kết nối cơ sở dữ liệu |
| **Nhà máy** | Tạo đối tượng mà không chỉ định lớp chính xác |  __BẢO VỆ_0__ |
| **Người quan sát** | Thông báo cho người phụ thuộc khi trạng thái thay đổi | Trình nghe sự kiện, pub/sub |
| **Chiến lược** | Hoán đổi thuật toán khi chạy | Chiến lược thanh toán: Thẻ tín dụng, PayPal, tiền điện tử |
| **Kho lưu trữ** | Truy cập dữ liệu trừu tượng đằng sau một giao diện rõ ràng |  __BẢO VỆ_1__ |
| **Người trang trí** | Thêm hành vi động | Trình trang trí ghi nhật ký xung quanh một dịch vụ |
| **Bộ chuyển đổi** | Làm cho các giao diện không tương thích hoạt động cùng nhau | Bộ điều hợp API kế thừa |
---

## Lựa chọn kiến ​​trúc phù hợp
Không có kiến ​​trúc "tốt nhất" trên toàn cầu. Sự lựa chọn đúng đắn phụ thuộc vào:
| Yếu tố | Ủng hộ đá nguyên khối khi... | Ưu tiên các dịch vụ vi mô khi... |
|--------|------------------------------|------------------------------|
| **Quy mô nhóm** | < 10 developers | >20 nhà phát triển, nhiều nhóm |
| **Độ phức tạp của tên miền** | Đơn giản hoặc dễ hiểu | Bối cảnh phức tạp, nhiều giới hạn |
| **Yêu cầu về quy mô** | Nhu cầu mở rộng quy mô thống nhất | Các thành phần khác nhau cần quy mô khác nhau |
| **Nhịp triển khai** | Chu kỳ phát hành đơn | Cần triển khai độc lập |
| **Đa dạng công nghệ** | Một ngăn xếp là được | Các dịch vụ khác nhau cần công nghệ khác nhau |
**Lời khuyên thiết thực**: hãy bắt đầu với một mô-đun nguyên khối. Chỉ trích xuất dịch vụ khi bạn có nhu cầu rõ ràng và ranh giới miền rõ ràng. Dịch vụ vi mô chưa hoàn thiện là một trong những lỗi kiến ​​trúc phổ biến nhất trong ngành.