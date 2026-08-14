---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
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
tags: [testing, methodologies, coding-and-technology]
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
# Phương pháp kiểm tra
Kiểm thử là cách bạn có được sự tự tin rằng mã của mình hoạt động — và quan trọng hơn, những thay đổi đó không phá vỡ những gì đã hoạt động. Thử nghiệm tốt sẽ phát hiện lỗi trước khi người dùng thực hiện, ghi lại hành vi dự kiến ​​và cho phép tái cấu trúc một cách dễ dàng. Tệp này bao gồm đầy đủ các chiến lược kiểm thử, từ kiểm thử đơn vị đến kiểm thử toàn diện và các nguyên tắc giúp kiểm thử hiệu quả.
---

## Kim tự tháp thử nghiệm
Kim tự tháp thử nghiệm mô tả cách phân bổ lý tưởng các thử nghiệm trong một dự án.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Cấp độ | Đếm | Tốc độ | Chi phí | Nó kiểm tra cái gì |
|-------|-------|-------|------|--------------|
| **Đơn vị** | Nhiều | Nhanh (ms) | Thấp | Các hàm, lớp, phương thức riêng lẻ |
| **Tích hợp** | Một số | Trung bình (100ms-s) | Trung bình | Các thành phần tương tác như thế nào; truy vấn cơ sở dữ liệu; Lệnh gọi API |
| **E2E** | Ít | Chậm (giây-phút) | Cao | Toàn bộ luồng người dùng thông qua hệ thống thực |
---

## Kiểm tra đơn vị
Kiểm tra các đơn vị mã riêng lẻ một cách riêng biệt.
### Nguyên tắc
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Nhanh** | Mỗi bài kiểm tra sẽ chạy trong mili giây |
| **Bị cô lập** | Các bài kiểm tra không phụ thuộc vào nhau; không có trạng thái chia sẻ |
| **Xác định** | Cùng một đầu vào → cùng một đầu ra mọi lúc (không ngẫu nhiên, không phụ thuộc vào thời gian) |
| **Tự kiểm tra** | Kiểm tra tự động đạt hoặc thất bại; không kiểm tra thủ công |
| **Kịp thời** | Được viết bên cạnh hoặc trước mã (TDD) |
### Cấu trúc của một bài kiểm tra
| Giai đoạn | Mô tả |
|-------|-------------|
| **Sắp xếp** | Thiết lập dữ liệu thử nghiệm và các phụ thuộc |
| **Đạo luật** | Gọi hàm hoặc phương thức đang được kiểm tra |
| **Khẳng định** | Xác minh kết quả phù hợp với mong đợi |
### Kiểm tra cái gì
| Danh mục | Ví dụ |
|----------|----------|
| **Con đường hạnh phúc** | Đầu vào bình thường tạo ra đầu ra dự kiến ​​|
| **Vỏ viền** | Đầu vào trống, null, 0, giá trị tối đa, phần tử đơn |
| **Các trường hợp lỗi** | Đầu vào không hợp lệ, thiếu dữ liệu, quyền bị từ chối |
| **Điều kiện biên** | Tắt từng cái một; chính xác ở giới hạn |
### Chế giễu và chọc ghẹo
| Kỳ hạn | Mô tả | Khi nào nên sử dụng |
|------|-------------|-------------|
| **Giả vờ** | Một đối tượng giả ghi lại cách nó được gọi | Xác minh tương tác (phương pháp này có được gọi không?) |
| **Sơ khai** | Một đối tượng giả mạo trả về các giá trị định trước | Cung cấp dữ liệu thử nghiệm (trả lại người dùng này từ cơ sở dữ liệu) |
| **Gián điệp** | Trình bao bọc ghi lại các cuộc gọi đến một đối tượng thực | Xác minh một phần |
| **Giả** | Cách triển khai đơn giản nhưng hiệu quả | Cơ sở dữ liệu trong bộ nhớ để kiểm tra |
| Thư viện mô phỏng | Ngôn ngữ |
|-------|--------|
| **unittest.mock** | Python |
| **Jest** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Moq** | C# |
| **làm chứng / gomock** | Đi |
---

## Kiểm tra tích hợp
Kiểm tra cách nhiều thành phần làm việc cùng nhau.
| Kiểm tra cái gì | Ví dụ |
|-------------|----------|
| **Truy vấn cơ sở dữ liệu** | ORM có tạo ra SQL chính xác không? Các chỉ mục có được sử dụng không? |
| **Điểm cuối API** | Chu trình yêu cầu-phản hồi đầy đủ có hoạt động không? |
| **Tương tác dịch vụ** | Dịch vụ A có gọi đúng dịch vụ B không? |
| **Phụ thuộc bên ngoài** | Tích hợp cổng thanh toán có hoạt động không? |
### Chiến lược
| Chiến lược | Mô tả | Đánh đổi |
|----------|-------------|----------|
| **Sự phụ thuộc thực sự** | Sử dụng cơ sở dữ liệu thực, hàng đợi tin nhắn thực | Thực tế nhất; chậm hơn; khó thiết lập hơn |
| **Bình chứa thử nghiệm** | Tăng tốc các vùng chứa Docker cho mỗi lần chạy thử nghiệm | Cân bằng tốt; tái sản xuất |
| **Các lựa chọn thay thế trong bộ nhớ** | H2 thay vì PostgreSQL; bus tin nhắn trong bộ nhớ | Nhanh; có thể bỏ lỡ các vấn đề trong thế giới thực |
| **Thử nghiệm hợp đồng** | Xác minh rằng các dịch vụ tôn trọng hợp đồng API của họ | Nắm bắt những thay đổi về giao diện |
---

## Thử nghiệm từ đầu đến cuối (E2E)
Kiểm tra hệ thống hoàn chỉnh từ quan điểm của người dùng.
| Công cụ | Loại | Tốt nhất cho |
|------|------|----------|
| **Nhà viết kịch** | Tự động hóa trình duyệt | Ứng dụng web; đa trình duyệt |
| **Cây bách** | Tự động hóa trình duyệt | Ứng dụng web; kinh nghiệm của nhà phát triển |
| **Selen** | Tự động hóa trình duyệt | Di sản; hỗ trợ ngôn ngữ rộng rãi |
| **Giải độc** | E2E di động | Phản ứng ứng dụng gốc |
| **Appium** | E2E di động | Ứng dụng di động gốc và lai |
| **Maestro** | E2E di động | Ứng dụng di động; cú pháp YAML đơn giản |
| **k6 / Châu chấu** | Kiểm tra tải | Hiệu suất khi tải |
### Các phương pháp hay nhất về E2E
| Thực hành | Tại sao |
|----------|------|
| **Chỉ kiểm tra các đường dẫn quan trọng** | Kiểm tra E2E chậm; tập trung vào những gì quan trọng nhất |
| **Sử dụng nhà máy dữ liệu thử nghiệm** | Tạo dữ liệu thử nghiệm theo chương trình; không dựa vào dữ liệu hạt giống |
| **Dọn dẹp sau khi kiểm tra** | Mỗi bài kiểm tra phải để hệ thống ở trạng thái đã biết |
| **Tránh kiểm tra chi tiết giao diện người dùng** | Kiểm tra hành vi, không phải lớp CSS hoặc vị trí thành phần |
| **Chạy trong CI** | Các bài kiểm tra E2E phải chạy tự động sau mỗi thay đổi |
---

## Phát triển dựa trên thử nghiệm (TDD)
Viết bài kiểm tra trước, sau đó viết mã để vượt qua.
| Bước | Mô tả |
|------|-------------|
| **1. Đỏ** | Viết một bài kiểm tra thất bại mô tả hành vi mong muốn |
| **2. Xanh** | Viết mã tối thiểu để vượt qua bài kiểm tra |
| **3. Tái cấu trúc** | Dọn dẹp mã trong khi vẫn giữ cho các bài kiểm tra luôn xanh |
| Lợi ích | Mô tả |
|----------|-------------|
| **Phản hồi về thiết kế** | Các thử nghiệm buộc bạn phải suy nghĩ về giao diện trước khi thực hiện |
| **An toàn hồi quy** | Mọi lỗi đều được kiểm tra; lỗi không bao giờ có thể quay trở lại |
| **Tài liệu** | Các thử nghiệm đóng vai trò là tài liệu sống về hành vi được mong đợi |
| **Tự tin** | Phạm vi kiểm tra cao cho phép tái cấu trúc dễ dàng |
---

## Phát triển theo hướng hành vi (BDD)
BDD mở rộng TDD bằng cách viết các bài kiểm tra bằng ngôn ngữ tự nhiên mô tả hành vi từ quan điểm của người dùng.
### Định dạng cho trước khi nào
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Công cụ | Ngôn ngữ |
|------|----------|
| **Dưa chuột** | Java, JavaScript, Ruby và các ngôn ngữ khác |
| **Cư xử** | Python |
| **SpecFlow** | C# |
| **Jest** (với mô tả/nó) | JavaScript |
---

## Các loại thử nghiệm khác
| Loại | Nó kiểm tra cái gì | Công cụ |
|------|--------------|-------|
| **Hiệu suất/Tải** | Hành vi của hệ thống đang tải | k6, JMeter, Locust, Gatling |
| **An ninh** | Lỗ hổng và vectơ tấn công | OWASP ZAP, Burp Suite, Snyk |
| **Khả năng tiếp cận** | Tuân thủ WCAG | rìu, Ngọn hải đăng, pa11y |
| **Hợp đồng** | Khả năng tương thích API giữa các dịch vụ | Hiệp ước, Hợp đồng đám mây mùa xuân |
| **Đột biến** | Chất lượng của chính bộ thử nghiệm | Stryker, đột biến, PIT |
| **Hồi quy trực quan** | Thay đổi giao diện người dùng giữa các phiên bản | Percy, Màu sắc, BackstopJS |
| **Hỗn loạn** | Khả năng phục hồi của hệ thống trước các lỗi | Khỉ hỗn loạn, Litmus, Gremlin |
| **Khói** | Chức năng cơ bản sau khi triển khai | Tập lệnh tùy chỉnh; kiểm tra sức khỏe |
| **Ngâm** | Hành vi của hệ thống trong thời gian dài | Kiểm tra tải chạy dài |
---

## Tổ chức kiểm tra
| Mẫu | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Cùng địa điểm** | Các bài kiểm tra bên cạnh mã họ kiểm tra (`src/utils.test.ts`) | Hầu hết các dự án; dễ tìm |
| **Thư mục riêng** | Kiểm tra trong thư mục`tests/`hoặc`__tests__/`| Dự án lớn; tách biệt rõ ràng |
| **Thiết bị thử nghiệm** | Dữ liệu thử nghiệm được chia sẻ trong thư mục`fixtures/`| Khi nhiều bài kiểm tra cần cùng một dữ liệu |
| **Thử nghiệm tiện ích** | Người trợ giúp được chia sẻ trong thư mục`test-utils/`| Khi logic thiết lập phức tạp |
---

## Phạm vi mã
| Số liệu | Nó đo lường những gì | Hạn chế |
|--------|-------------------|-------------|
| **Phạm vi phủ sóng của đường dây** | Tỷ lệ dòng mã được thực thi bởi các bài kiểm tra | Không đo lường chất lượng của các khẳng định |
| **Phạm vi chi nhánh** | Tỷ lệ chi nhánh (nếu/khác) được thực hiện | Tốt hơn so với phạm vi phủ sóng đường dây; vẫn không bắt hết lỗi |
| **Phạm vi bao phủ đường dẫn** | Tỷ lệ đường dẫn thực hiện được thực hiện | Kỹ lưỡng nhất; hàm mũ trong mã phức tạp |
| **Điểm đột biến** | Tỷ lệ đột biến được phát hiện qua các xét nghiệm | Thước đo tốt nhất về chất lượng bài kiểm tra |
**Mục tiêu**: Phạm vi phủ sóng 80% là mặc định hợp lý. Nhưng mức độ bao phủ là một hướng dẫn, không phải là mục tiêu - mức độ bao phủ 100% với các xác nhận yếu kém hơn mức độ bao phủ 70% với các bài kiểm tra kỹ lưỡng.
---

## Tích hợp và thử nghiệm liên tục
| Thực hành | Mô tả |
|----------|-------------|
| **Chạy tất cả các bài kiểm tra đơn vị trên mỗi lần xác nhận** | Phản hồi nhanh; bắt hồi quy ngay lập tức |
| **Chạy thử nghiệm tích hợp trên PR** | Nắm bắt các vấn đề mà bài kiểm tra đơn vị bỏ lỡ |
| **Chạy thử nghiệm E2E hàng đêm hoặc khi hợp nhất vào chính** | Chậm nhưng kỹ lưỡng |
| **Thất bại nhanh** | Dừng đường ống khi có sự cố đầu tiên để tiết kiệm thời gian |
| **Chính sách kiểm tra không ổn định** | Cách ly hoặc xóa các bài kiểm tra không ổn định ngay lập tức; không bao giờ bỏ qua |
| **Kiểm tra song song** | Chạy thử nghiệm song song để giảm thời gian CI |
---

## Lời khuyên thiết thực
- **Đặt tên các bài kiểm tra một cách rõ ràng.**`test_calculates_tax_for_high_earner`cho bạn biết điều gì đã xảy ra. `test_1`không cho bạn biết điều gì.
- **Một khẳng định cho mỗi bài kiểm tra (khi thực tế).** Giúp dễ dàng chẩn đoán lỗi.
- **Không kiểm tra chi tiết triển khai.** Kiểm tra hành vi. Nếu bạn cấu trúc lại phần bên trong, các bài kiểm tra sẽ không bị hỏng.
- **Tránh kiểm tra mã của bên thứ ba.** Giả lập các thư viện bên ngoài; kiểm tra sự tương tác giữa mã của bạn với chúng.
- **Thực hiện các thử nghiệm nhanh chóng.** Nếu bộ thử nghiệm của bạn mất 10 phút, nhà phát triển sẽ ngừng chạy nó. Tối ưu hóa không ngừng.
- **Xóa các bài kiểm tra chết.** Các bài kiểm tra luôn đạt hoặc kiểm tra mã bị xóa là nhiễu.
- **Coi mã kiểm thử như mã sản xuất.** Mã này phải dễ đọc, dễ bảo trì và có cấu trúc tốt.
---

## Bản tóm tắt
Việc kiểm thử không phải là tùy chọn — đó là cách bạn xây dựng phần mềm không bị hỏng. Kim tự tháp thử nghiệm hướng dẫn bạn thực hiện nhiều thử nghiệm đơn vị nhanh, một số thử nghiệm tích hợp và một số thử nghiệm E2E. TDD và BDD cung cấp các phương pháp tiếp cận có cấu trúc. Mocking cô lập các đơn vị để thử nghiệm. Phạm vi bảo hiểm của mã đo lường chiều rộng nhưng không đo chiều sâu. Nguyên tắc quan trọng nhất là: nếu nó không được kiểm tra thì nó sẽ hỏng - chỉ là bạn chưa biết điều đó thôi.