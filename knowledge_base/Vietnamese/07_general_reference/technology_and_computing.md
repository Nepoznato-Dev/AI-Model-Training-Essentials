<!--
---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Công nghệ và Máy tính
Máy tính có ở khắp mọi nơi — trong điện thoại, ô tô, tủ lạnh, thiết bị y tế và cơ sở hạ tầng vận hành xã hội hiện đại. Bạn không cần phải là một lập trình viên mới có thể hiểu được cách hoạt động của mọi thứ. Tệp này bao gồm các nguyên tắc cơ bản: máy tính là gì, Internet hoạt động như thế nào, cách xây dựng phần mềm và các khái niệm hình thành nên thế giới kỹ thuật số.
> **Bạn muốn tìm hiểu sâu hơn?** Tệp này là một cái nhìn tổng quan. Để biết thông tin chi tiết về bất kỳ chủ đề nào, hãy xem các tệp chuyên dụng trong[`01_coding_and_technology/`](../01_coding_and_technology/)— bao gồm[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)và.
---

## Máy tính là gì?
Về cốt lõi, mọi máy tính - từ điện thoại thông minh đến siêu máy tính - đều thực hiện cùng một công việc: nhận đầu vào, xử lý theo hướng dẫn (một chương trình) và tạo ra đầu ra. Sự kỳ diệu nằm ở tốc độ và quy mô.
### Kiến trúc Von Neumann
Hầu hết tất cả các máy tính hiện đại đều tuân theo thiết kế cơ bản này:
| Thành phần | Nó làm gì | Tương tự |
|----------|-------------|----------|
| **CPU** (Bộ xử lý trung tâm) | Thực hiện các hướng dẫn; "bộ não" | Đầu bếp làm theo công thức |
| **RAM** (Bộ nhớ) | Lưu trữ dữ liệu mà CPU đang sử dụng; bị mất khi mất điện | Mặt bàn — truy cập nhanh, không gian hạn chế |
| **Bộ nhớ** (SSD/HDD) | Lưu trữ dữ liệu vĩnh viễn | Phòng đựng thức ăn - truy cập chậm hơn, nhiều không gian hơn |
| **Đầu vào/Đầu ra** | Bàn phím, chuột, màn hình, mạng | Cách đầu bếp nhận đơn đặt hàng và giao đồ ăn |
| **GPU** (Bộ xử lý đồ họa) | Bộ xử lý chuyên dụng cho các tác vụ song song (đồ họa, AI) | Một nhóm trợ lý đều làm cùng một nhiệm vụ |
**Thông tin chi tiết quan trọng**: RAM nhanh nhưng tạm thời. Lưu trữ chậm nhưng vĩnh viễn. Khi máy tính của bạn "cảm thấy chậm", thường là do máy hết RAM và phải sử dụng bộ nhớ lưu trữ làm bộ nhớ tạm thời (hoán đổi), tốc độ chậm hơn nhiều.
---

## Ngôn ngữ lập trình - Nói chuyện với máy tính
Ngôn ngữ lập trình là một tập hợp các hướng dẫn mà máy tính có thể thực thi. Các ngôn ngữ khác nhau được thiết kế cho các mục đích khác nhau. Để biết thông tin chi tiết về 34 ngôn ngữ riêng lẻ, hãy xem thư mục [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Ngôn ngữ | Tốt nhất cho | Tại sao chọn nó |
|----------|----------|---------------|
| **Trăn** | Khoa học dữ liệu, AI, tự động hóa, phụ trợ web | Cú pháp đơn giản; hệ sinh thái khổng lồ; tuyệt vời cho người mới bắt đầu |
| **JavaScript** | Giao diện web, toàn bộ ngăn xếp (Node.js) | Chạy trong mọi trình duyệt; cần thiết cho việc phát triển web |
| **Java** | Phần mềm doanh nghiệp, ứng dụng Android | Nền tảng độc lập (JVM); hệ sinh thái lớn |
| **C/C++** | Lập trình hệ thống, trò chơi, nhúng | Hiệu suất tối đa; điều khiển phần cứng trực tiếp |
| **Rỉ sét** | Lập trình hệ thống với sự đảm bảo an toàn | An toàn bộ nhớ mà không cần thu gom rác |
| **Đi** | Dịch vụ đám mây, microservice, công cụ CLI | Đơn giản; đồng thời tuyệt vời; biên soạn nhanh |
| **SQL** | Truy vấn cơ sở dữ liệu | Ngôn ngữ phổ quát để làm việc với dữ liệu |
| **TypeScript** | Ứng dụng web quy mô lớn | JavaScript với việc kiểm tra loại; bắt lỗi sớm |
---

## Internet hoạt động như thế nào
Internet không giống như web. Internet là mạng vật lý — cáp, bộ định tuyến, máy chủ và giao thức kết nối hàng tỷ thiết bị. World Wide Web là một dịch vụ chạy trên internet (cùng với email, truyền tệp, phát trực tuyến, chơi trò chơi, v.v.).
### Hành trình của một yêu cầu web
Khi bạn nhập`https://www.example.com`vào trình duyệt của mình:
1. **Tra cứu DNS**: Trình duyệt của bạn yêu cầu máy chủ DNS dịch "www.example.com" sang địa chỉ IP (như 93.184.216.34).
2. **Kết nối TCP**: Thiết bị của bạn thiết lập kết nối đến địa chỉ IP đó bằng TCP (giao thức đảm bảo phân phối đáng tin cậy).
3. **Bắt tay TLS**: Nếu sử dụng HTTPS, trình duyệt của bạn và máy chủ sẽ đàm phán kết nối được mã hóa.
4. **Yêu cầu HTTP**: Trình duyệt của bạn gửi yêu cầu: "Hãy cung cấp cho tôi trang tại /index.html."
5. **Xử lý máy chủ**: Máy chủ web tìm thấy trang, có thể truy vấn cơ sở dữ liệu và chuẩn bị phản hồi.
6. **Phản hồi HTTP**: Máy chủ gửi lại HTML, CSS và JavaScript.
7. **Hiển thị**: Trình duyệt của bạn phân tích cú pháp HTML, áp dụng các kiểu CSS và thực thi JavaScript để hiển thị trang.
Toàn bộ quá trình này thường mất ít hơn một giây.
### Giao thức chính
| Giao thức | Nó làm gì | Lớp |
|----------|-------------|-------|
| **IP** (Giao thức Internet) | Định tuyến các gói giữa các mạng | Mạng |
| **TCP** | Giao hàng theo yêu cầu, đáng tin cậy (truyền lại các gói bị mất) | Vận tải |
| **UDP** | Giao hàng nhanh, không đáng tin cậy (không truyền lại) | Vận tải |
| **HTTP/HTTPS** | Chuyển trang web (HTTPS thêm mã hóa) | Ứng dụng |
| **DNS** | Dịch tên miền sang địa chỉ IP | Ứng dụng |
| **SSH** | Bảo mật quyền truy cập từ xa vào máy tính | Ứng dụng |
| **SMTP/IMAP** | Gửi và nhận email | Ứng dụng |
---

## Phát triển phần mềm - Cách xây dựng chương trình
### Quá trình phát triển
1. **Viết mã**: Nhà phát triển viết hướng dẫn bằng ngôn ngữ lập trình.
2. **Mã kiểm tra**: Chạy mã để xác minh nó hoạt động chính xác.
3. **Kiểm soát phiên bản**: Theo dõi các thay đổi bằng Git — tiêu chuẩn chung.
4. **Đánh giá**: Các nhà phát triển khác kiểm tra lỗi và chất lượng mã.
5. **Build**: Chuyển đổi mã nguồn thành chương trình có thể chạy được (biên dịch).
6. **Triển khai**: Phát hành chương trình cho người dùng (máy chủ, cửa hàng ứng dụng, v.v.).
7. **Giám sát**: Theo dõi các lỗi và vấn đề về hiệu suất trong quá trình sản xuất.
### Các khái niệm chính
| Khái niệm | Ý nghĩa của nó | Tại sao nó lại quan trọng |
|----------|---------------|-------|
| **Kiểm soát phiên bản (Git)** | Theo dõi mọi thay đổi về mã theo thời gian | Sự hợp tác; khả năng sửa chữa sai lầm |
| **API** (Giao diện lập trình ứng dụng) | Một cách xác định để các thành phần phần mềm giao tiếp | Cho phép các hệ thống khác nhau làm việc cùng nhau |
| **Cơ sở dữ liệu** | Lưu trữ có tổ chức cho dữ liệu | Mọi ứng dụng đều cần lưu trữ và truy xuất dữ liệu |
| **Thử nghiệm** | Tự động kiểm tra xem mã có hoạt động chính xác không | Ngăn chặn lỗi tiếp cận người dùng |
| **CI/CD** (Tích hợp/Cung cấp liên tục) | Quy trình tự động từ cam kết mã đến sản xuất | Phát hành nhanh hơn, an toàn hơn |
| **Container hóa (Docker)** | Đóng gói một ứng dụng với tất cả các phần phụ thuộc của nó | "Hoạt động trên máy của tôi" trở thành "hoạt động ở mọi nơi" |
---

## Cơ sở dữ liệu - Nơi dữ liệu tồn tại
Mọi ứng dụng đều cần lưu trữ dữ liệu. Cơ sở dữ liệu là hệ thống thực hiện việc này một cách hiệu quả và đáng tin cậy.
| Loại | Cách lưu trữ dữ liệu | Tốt nhất cho | Ví dụ |
|------|-------------------|----------|--------|
| **Quan hệ (SQL)** | Bảng có hàng và cột; lược đồ nghiêm ngặt | Dữ liệu có cấu trúc; truy vấn phức tạp; giao dịch | PostgreSQL, MySQL, SQLite |
| **Tài liệu (NoSQL)** | Các tài liệu giống JSON; lược đồ linh hoạt | Dữ liệu bán cấu trúc; lặp lại nhanh chóng | MongoDB, CouchDB |
| **Khóa-giá trị** | Khóa đơn giản → cặp giá trị | Bộ nhớ đệm; lưu trữ phiên; tra cứu nhanh | Redis, DynamoDB |
| **Biểu đồ** | Nút và cạnh (mối quan hệ) | Mạng xã hội; công cụ đề xuất | Neo4j, JanusGraph |
| **Dòng thời gian** | Được tối ưu hóa cho dữ liệu có dấu thời gian | Giám sát; phân tích; IoT | InfluxDB, TimescaleDB |
**SQL** (Ngôn ngữ truy vấn có cấu trúc) là ngôn ngữ tiêu chuẩn cho cơ sở dữ liệu quan hệ. Đây là một trong những kỹ năng kỹ thuật có giá trị nhất mà bạn có thể học - hầu hết mọi tổ chức đều sử dụng cơ sở dữ liệu và SQL là cách bạn giao tiếp với họ.
---

## Hệ điều hành
Hệ điều hành (OS) là lớp phần mềm giữa bạn (và các chương trình của bạn) và phần cứng. Nó quản lý bộ nhớ, quy trình, tập tin và thiết bị.
| Hệ điều hành | Nó thống trị ở đâu | Tính năng chính |
|------|-------------------|-------------|
| **Cửa sổ** | Máy tính để bàn/máy tính xách tay (~72% thị phần) | Khả năng tương thích phần mềm/phần cứng rộng nhất |
| **macOS** | Chuyên gia sáng tạo, nhà phát triển | Dựa trên Unix; giao diện người dùng được đánh bóng; Hệ sinh thái Apple |
| **Linux** | Máy chủ (~96%), siêu máy tính (100%), thiết bị nhúng, nhà phát triển | Nguồn mở; miễn phí; cực kỳ tùy biến |
| **Android** | Di động (~72% thị phần toàn cầu) | Dựa trên nhân Linux; mã nguồn mở |
| **iOS** | Di động (~27% toàn cầu, nhưng doanh thu cao hơn) | Hệ sinh thái khép kín; đánh bóng; tập trung vào quyền riêng tư |
Linux xứng đáng được đề cập đặc biệt: nó hỗ trợ hầu hết Internet, mọi siêu máy tính trong top 500, hầu hết cơ sở hạ tầng đám mây và tất cả điện thoại Android. Nó miễn phí, mã nguồn mở và được duy trì bởi cộng đồng toàn cầu.
---

## Điện toán đám mây
Điện toán đám mây có nghĩa là thuê tài nguyên máy tính (máy chủ, bộ lưu trữ, cơ sở dữ liệu, v.v.) qua internet thay vì mua và bảo trì phần cứng của riêng bạn. Để có hướng dẫn toàn diện về kiến ​​trúc đám mây, mô hình dịch vụ và so sánh nhà cung cấp, hãy xem[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Mô hình dịch vụ | Những gì bạn nhận được | Tương tự | Ví dụ |
|--------------|-------------|----------|----------|
| **IaaS** (Cơ sở hạ tầng) | Máy chủ ảo, lưu trữ, kết nối mạng | Thuê một lô đất và xây dựng những gì bạn muốn | AWS EC2, Công cụ điện toán của Google |
| **PaaS** (Nền tảng) | Môi trường thời gian chạy; bạn mang theo mã | Thuê căn hộ có nội thất | Heroku, Máy ứng dụng của Google |
| **SaaS** (Phần mềm) | Ứng dụng hoàn chỉnh; bạn chỉ cần sử dụng nó | Ở tại khách sạn | Gmail, Slack, Lực lượng bán hàng |
Ba nhà cung cấp đám mây lớn là **AWS** (Amazon, ~32% thị phần), **Azure** (Microsoft, ~23%) và **GCP** (Google, ~10%). Họ cung cấp hàng trăm dịch vụ bao gồm điện toán, lưu trữ, cơ sở dữ liệu, AI, kết nối mạng, v.v.
---

## An ninh mạng — Bảo vệ hệ thống kỹ thuật số
An ninh mạng là hoạt động bảo vệ máy tính, mạng và dữ liệu khỏi bị tấn công. Điều này quan trọng vì mọi thứ đều được kết nối và chi phí cho những vi phạm là rất lớn. Để có hướng dẫn đầy đủ về Top 10 OWASP, vòng đời phát triển an toàn và quản lý bí mật, hãy xem.
### Các mối đe dọa phổ biến
| Đe dọa | Nó là gì | Phòng ngừa |
|--------|-------------|-------------|
| **Phần mềm độc hại** | Phần mềm độc hại (vi rút, sâu, trojan) | Chống virus; luôn cập nhật phần mềm |
| **Lừa đảo** | Email/tin nhắn giả mạo lừa bạn tiết lộ thông tin | Đào tạo; lọc email; chủ nghĩa hoài nghi |
| **Phần mềm tống tiền** | Mã hóa dữ liệu của bạn; yêu cầu thanh toán chìa khóa | Sao lưu; hệ thống vá lỗi; không trả tiền |
| **DDoS** | Áp đảo một dịch vụ với lưu lượng truy cập | Lọc lưu lượng truy cập; Bảo vệ CDN |
| **Chèn SQL** | Chèn SQL độc hại vào trường nhập liệu | Truy vấn được tham số hóa; xác thực đầu vào |
| **Người đứng giữa** | Chặn liên lạc giữa hai bên | Mã hóa HTTPS/TLS |
### Nguyên tắc bảo mật cơ bản
- **Mã hóa**: Xáo trộn dữ liệu để chỉ những bên được ủy quyền mới có thể đọc được. HTTPS sử dụng TLS để mã hóa lưu lượng truy cập web.
- **Xác thực**: Xác minh danh tính. Sử dụng xác thực đa yếu tố (MFA) - mật khẩu + thứ khác (mã, sinh trắc học).
- **Ủy quyền**: Xác minh quyền. Chỉ vì bạn đã đăng nhập không có nghĩa là bạn nên truy cập mọi thứ.
- **Nguyên tắc đặc quyền tối thiểu**: Chỉ cấp cho người dùng và hệ thống quyền truy cập mà họ cần, không có gì hơn.
- **Quản lý bản vá**: Luôn cập nhật phần mềm. Hầu hết các vi phạm đều khai thác các lỗ hổng đã biết đã có bản vá.
---

## Định dạng dữ liệu
Các chương trình trao đổi dữ liệu ở các định dạng cụ thể. Phổ biến nhất:
| Định dạng | Cấu trúc | Được sử dụng cho |
|--------|-------------|----------|
| **JSON** | Cặp khóa-giá trị; con người có thể đọc được | API; cấu hình; trao đổi dữ liệu |
| **XML** | Dựa trên thẻ; dài dòng nhưng linh hoạt | Hệ thống kế thừa; tài liệu; API SOAP |
| **YAML** | Dựa trên thụt lề; rất dễ đọc | Cấu hình (Docker, Kubernetes, CI/CD) |
| **CSV** | Hàng và cột văn bản thuần túy | Nhập/xuất dữ liệu; bảng tính |
---

## Bản tóm tắt
Máy tính không phải là phép thuật - nó là kỹ thuật. Máy tính làm theo hướng dẫn với tốc độ đáng kinh ngạc. Internet kết nối hàng tỷ người trong số họ bằng các giao thức được tiêu chuẩn hóa. Phần mềm được xây dựng bởi các nhóm người viết, thử nghiệm và triển khai mã theo chu kỳ lặp đi lặp lại. Cơ sở dữ liệu lưu trữ và truy xuất dữ liệu. Điện toán đám mây cho phép mọi người truy cập tài nguyên điện toán khổng lồ theo yêu cầu. Và an ninh mạng là cuộc chiến đang diễn ra nhằm giữ an toàn cho tất cả những thứ này khỏi những người muốn khai thác nó. Việc hiểu những nguyên tắc cơ bản này sẽ giúp bạn điều hướng thế giới kỹ thuật số — cho dù bạn là người dùng, nhà phát triển hay chỉ là người đang cố gắng tìm hiểu công nghệ định hình cuộc sống hiện đại.