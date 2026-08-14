---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
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
tags: [performance, optimization, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#Tối ưu hóa hiệu suất
Tối ưu hóa hiệu suất là phương pháp làm cho phần mềm nhanh hơn — giảm thời gian phản hồi, tăng thông lượng, giảm mức sử dụng bộ nhớ và loại bỏ tắc nghẽn. Đó là một trong những kỹ năng có tác động mạnh nhất mà nhà phát triển có thể có, vì phần mềm chậm sẽ mất người dùng, lãng phí tài nguyên và khiến mọi người thất vọng. Nhưng đó cũng là một trong những lỗi thường được thực hiện sai nhất, khi các nhà phát triển tối ưu hóa những điều sai trái dựa trên trực giác hơn là bằng chứng.
---

## Nguyên tắc vàng
> **Đo lường trước, tối ưu hóa sau.** Không bao giờ tối ưu hóa dựa trên giả định. Lập hồ sơ mã, tìm nút cổ chai thực tế và khắc phục điều đó.
| Chống mẫu | Tại sao nó xấu |
|-------------|-------------|
| **Tối ưu hóa sớm** | Dành thời gian tăng tốc mã không chậm |
| **Tối ưu hóa không cần đo lường** | Sửa lỗi tắc nghẽn cổ chai; không có cách nào để xác minh sự cải thiện |
| **Hy sinh khả năng đọc để lấy tốc độ** | Mã không thể đọc được có giá cao hơn hiệu suất đạt được |
| **Lưu vào bộ nhớ đệm mọi thứ** | Dữ liệu cũ, bộ nhớ cồng kềnh, độ phức tạp |
---

## Lập hồ sơ
Trước khi bạn có thể làm việc gì đó nhanh hơn, bạn cần biết *thời gian* đang được sử dụng ở đâu.
| Loại công cụ | Nó đo lường những gì | Ví dụ |
|----------|-----------------|----------|
| **Trình hồ sơ CPU** | Chức năng nào tiêu tốn nhiều thời gian CPU nhất | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Trình lược tả bộ nhớ** | Phân bổ bộ nhớ và rò rỉ | tracemalloc (Python), Valgrind, heaptrack |
| **Trình lược tả I/O** | Tắc nghẽn I/O trên đĩa và mạng | iotop, strace, Wireshark |
| **APM (Giám sát hiệu suất ứng dụng)** | Thời gian yêu cầu từ đầu đến cuối | Di tích mới, Datadog, Jaeger |
| **Công cụ dành cho trình duyệt** | Kết xuất giao diện người dùng, thực thi JavaScript, mạng | Công cụ dành cho nhà phát triển Chrome, Trình phân tích Firefox |
### Quy trình lập hồ sơ
| Bước | Mô tả |
|------|-------------|
| 1. Xác định hoạt động chậm | Người dùng báo cáo tải trang chậm; giám sát cho thấy độ trễ cao |
| 2. Lập hồ sơ đường dẫn đầy đủ | Tìm thành phần nào mất nhiều thời gian nhất |
| 3. Đi sâu vào | Lập hồ sơ thành phần cụ thể đó để tìm hàm nóng |
| 4. Khắc phục nút cổ chai | Áp dụng tối ưu hóa phù hợp |
| 5. Đo lại | Xác minh sự cải tiến; kiểm tra hồi quy |
---

## Tối ưu hóa thuật toán
Hiệu suất đạt được lớn nhất đến từ việc chọn các thuật toán tốt hơn chứ không phải từ tối ưu hóa vi mô.
| Thay đổi | Cải tiến |
|--------|-------------|
| Tìm kiếm tuyến tính O(n) → Tra cứu bảng băm O(1) | 100x+ cho tập dữ liệu lớn |
| Vòng lặp lồng nhau O(n²) → Sắp xếp + tìm kiếm nhị phân O(n log n) | Bậc độ lớn cho n lớn |
| Tính toán lặp đi lặp lại → Ghi nhớ/lưu vào bộ nhớ đệm | Loại bỏ công việc dư thừa |
| Nối chuỗi trong một vòng lặp → Builder/join | Tránh sao chép chuỗi bậc hai |
| Dữ liệu chưa được sắp xếp → Dữ liệu được sắp xếp với tìm kiếm nhị phân | O(log n) thay vì O(n) mỗi lần tra cứu |
---

## Chiến lược bộ nhớ đệm
Bộ nhớ đệm lưu trữ các kết quả đã tính toán nên chúng không cần phải tính toán lại.
| Loại bộ đệm | Vị trí | Tốc độ | Trọn đời |
|----------|----------|-------|----------|
| **Bộ đệm CPU** | L1/L2/L3 | ~1 ns | Tự động |
| **Trong bộ nhớ** | RAM ứng dụng (dict, HashMap) | ~100 giây | Cho đến khi được xóa hoặc bị đuổi |
| **Bộ nhớ đệm được phân phối** | Redis, Memcached | ~1 mili giây | TTL có thể định cấu hình |
| **CDN** | Máy chủ biên trên toàn thế giới | ~10-50 mili giây | TTL có thể định cấu hình |
| **Bộ đệm của trình duyệt** | Trình duyệt của người dùng | ~1 mili giây | Tiêu đề bộ đệm HTTP |
| **Bộ đệm truy vấn cơ sở dữ liệu** | Cấp độ cơ sở dữ liệu hoặc ORM | ~1-10 mili giây | Cho đến khi dữ liệu thay đổi |
### Mẫu bộ nhớ đệm
| Mẫu | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Bỏ bộ nhớ đệm** | Ứng dụng kiểm tra bộ đệm; tải từ DB do lỡ; lưu trữ trong bộ đệm | Phổ biến nhất; đơn giản |
| **Viết qua** | Ghi đồng thời vào bộ đệm và DB | Khi đọc >> viết; tính nhất quán quan trọng |
| **Viết-đằng sau** | Ghi vào bộ đệm; ghi không đồng bộ vào DB | Thông lượng ghi cao; một số nguy cơ mất dữ liệu |
| **TTL (Thời gian để sống)** | Các mục trong bộ nhớ đệm hết hạn sau một thời gian đã đặt | Khi dữ liệu thay đổi định kỳ |
| **Vô hiệu** | Xóa rõ ràng các mục bộ đệm cũ | Khi bạn biết chính xác khi nào dữ liệu thay đổi |
### Vô hiệu hóa bộ đệm
Hai vấn đề khó khăn nhất trong khoa học máy tính: vô hiệu hóa bộ đệm, đặt tên các thứ và lỗi từng cái một.
| Chiến lược | Mô tả |
|----------|-------------|
| **Dựa trên TTL** | Các mục hết hạn sau N giây; đơn giản nhưng có thể cung cấp dữ liệu cũ |
| **Theo hướng sự kiện** | Vô hiệu khi dữ liệu thay đổi; phức tạp hơn nhưng chính xác hơn |
| **Dựa trên phiên bản** | Bao gồm số phiên bản; tăng theo những thay đổi |
| **Dựa trên thẻ** | Các mục bộ đệm liên quan đến thẻ; vô hiệu hóa tất cả các mục có thẻ |
---

## Tối ưu hóa cơ sở dữ liệu
Cơ sở dữ liệu thường là nút thắt cổ chai lớn nhất trong các ứng dụng web.
| Kỹ thuật | Mô tả | Tác động |
|----------|-------------|--------|
| **Lập chỉ mục** | Thêm chỉ mục trên các cột được sử dụng trong WHERE, JOIN, ORDER BY | Truy vấn nhanh hơn 10-1000 lần |
| **Tối ưu hóa truy vấn** | Tránh CHỌN *; sử dụng EXPLAIN để phân tích truy vấn | Giảm I/O |
| **Kết nối tổng hợp** | Tái sử dụng các kết nối cơ sở dữ liệu thay vì tạo kết nối mới | Loại bỏ chi phí kết nối |
| **Đọc bản sao** | Định tuyến các truy vấn đọc tới cơ sở dữ liệu bản sao | Phân phối tải đọc |
| **Phân vùng** | Chia các bảng lớn thành các phân vùng nhỏ hơn | Truy vấn nhanh hơn trên tập dữ liệu lớn |
| **Không chuẩn hóa** | Thêm dữ liệu dư thừa để tránh tham gia | Đọc nhanh hơn; viết chậm hơn |
| **Các quan điểm cụ thể hóa** | Kết quả truy vấn được tính toán trước | Truy vấn phức tạp tức thì |
| **Phòng ngừa N+1** | Sử dụng THAM GIA, tải háo hức hoặc truy vấn hàng loạt | Loại bỏ hàng ngàn truy vấn |
---

## Đồng thời và song song
| Khái niệm | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Xâu chuỗi** | Nhiều luồng trong một tiến trình | Nhiệm vụ giới hạn I/O (mạng, đĩa) |
| **Đa xử lý** | Nhiều quy trình (bỏ qua GIL trong Python) | Nhiệm vụ ràng buộc CPU |
| **Không đồng bộ/đang chờ** | Hợp tác đa nhiệm; chủ đề đơn | I/O đồng thời cao (máy chủ web) |
| **Tính toán GPU** | Hàng ngàn lõi song song | Hoạt động ma trận; xử lý hình ảnh; ML |
### Không đồng bộ so với phân luồng
| Khía cạnh | Không đồng bộ/Đang chờ | Luồng |
|--------|-------------|----------|
| **Người mẫu** | Hợp tác xã (kiểm soát năng suất nhiệm vụ) | Ưu tiên (OS chuyển chủ đề) |
| **Chi phí chung** | Rất thấp (không chuyển ngữ cảnh) | Cao hơn (tạo luồng, chuyển ngữ cảnh) |
| **Độ phức tạp** | Lý luận đơn giản hơn (luồng đơn) | Điều kiện cuộc đua, bế tắc, khóa |
| **Tốt nhất cho** | Nhiều thao tác I/O đồng thời | Chặn các hoạt động không thể thực hiện không đồng bộ |
| **Giới hạn** | Không thể sử dụng mã giới hạn CPU mà không chặn | GIL trong Python hạn chế tính song song thực sự |
---

## Hiệu suất giao diện người dùng
| Kỹ thuật | Mô tả | Tác động |
|----------|-------------|--------|
| **Giảm thiểu** | Xóa khoảng trắng và rút ngắn tên biến | Tệp nhỏ hơn 20-40% |
| **Gói** | Kết hợp nhiều tệp thành ít yêu cầu hơn | Ít yêu cầu HTTP hơn |
| **Chia mã** | Chỉ tải mã cần thiết cho trang hiện tại | Tải ban đầu nhanh hơn |
| **Tải lười biếng** | Tải hình ảnh và thành phần khi cần thiết | Kết xuất ban đầu nhanh hơn |
| **Cây rung chuyển** | Xóa mã không sử dụng khỏi gói | Gói nhỏ hơn |
| **Tối ưu hóa hình ảnh** | Sử dụng WebP/AVIF; hình ảnh đáp ứng; lười tải | Hình ảnh nhỏ hơn 50-80% |
| **CDN** | Phục vụ nội dung tĩnh từ máy chủ biên | Độ trễ thấp hơn trên toàn cầu |
| **HTTP/2 và HTTP/3** | Ghép kênh; nén tiêu đề; 0-RTT | Chi phí giao thức nhanh hơn |
| **Nhân viên phục vụ** | Nội dung bộ nhớ đệm để sử dụng ngoại tuyến; thông báo đẩy | Lượt truy cập lặp lại nhanh hơn |
---

## Tối ưu hóa bộ nhớ
| Kỹ thuật | Mô tả |
|----------||-------------|
| **Tổng hợp đối tượng** | Tái sử dụng các đối tượng thay vì tạo đối tượng mới |
| **Truyền phát** | Xử lý dữ liệu theo từng khối thay vì tải mọi thứ vào bộ nhớ |
| **Trình tạo / trình vòng lặp** | Mang lại từng giá trị một thay vì xây dựng danh sách |
| **Tệp ánh xạ bộ nhớ** | Truy cập các tệp lớn mà không cần tải chúng hoàn toàn |
| **Điều chỉnh việc thu gom rác** | Điều chỉnh các tham số GC cho khối lượng công việc của bạn |
| **Lựa chọn cấu trúc dữ liệu** | Sử dụng mảng thay vì danh sách liên kết cho vị trí bộ đệm; sử dụng bộ để kiểm tra tư cách thành viên |
---

## Tối ưu hóa mạng
| Kỹ thuật | Mô tả |
|----------||-------------|
| **Nén** | gzip, brotli cho phản hồi HTTP |
| **Tái sử dụng kết nối** | Kết nối duy trì; Ghép kênh HTTP/2 |
| **Yêu cầu phân nhóm** | Kết hợp nhiều lệnh gọi API thành một |
| **Phân trang** | Tải dữ liệu trong các trang thay vì tất cả cùng một lúc |
| **Nén ở trạng thái nghỉ** | Nén dữ liệu trong cơ sở dữ liệu và bộ nhớ đệm |
| **Lựa chọn giao thức** | gRPC (nhị phân, hiệu quả) so với REST (người có thể đọc được) |
---

## Giám sát và cảnh báo
| Số liệu | Nó nói gì với bạn |
|--------|-------------------|
| **Độ trễ P50 / P95 / P99** | Thời gian phản hồi ở các phần trăm khác nhau |
| **Thông lượng** | Yêu cầu mỗi giây |
| **Tỷ lệ lỗi** | Tỷ lệ yêu cầu không thành công |
| **Sử dụng CPU** | Dung lượng xử lý được sử dụng là bao nhiêu |
| **Sử dụng bộ nhớ** | tiêu thụ RAM; đang tiến tới giới hạn? |
| **Thời gian truy vấn cơ sở dữ liệu** | Truy vấn chậm cần tối ưu hóa |
---

## Bản tóm tắt
Tối ưu hóa hiệu suất là một quá trình có hệ thống: đo lường, xác định nút thắt cổ chai, khắc phục và đo lường lại. Chiến thắng lớn nhất đến từ những cải tiến về thuật toán và loại bỏ những công việc không cần thiết — không phải từ việc tối ưu hóa vi mô. Bộ nhớ đệm, lập chỉ mục cơ sở dữ liệu và tính đồng thời là những công cụ mạnh mẽ nhất. Hiệu suất giao diện người dùng phụ thuộc vào việc giảm thiểu kích thước tải trọng và các chuyến đi khứ hồi. Và quy tắc quan trọng nhất luôn giống nhau: đừng đoán - hồ sơ.