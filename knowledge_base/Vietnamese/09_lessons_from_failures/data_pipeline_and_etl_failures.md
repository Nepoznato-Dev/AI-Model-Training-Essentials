<!--
---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
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
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Lỗi đường ống dữ liệu và ETL
Đường ống dữ liệu là hệ thống ống nước của các tổ chức hiện đại — họ di chuyển dữ liệu từ hệ thống nguồn thông qua các quá trình chuyển đổi sang cơ sở dữ liệu, kho và hồ nơi dữ liệu được sử dụng để phân tích, học máy và ra quyết định. Khi họ làm việc, không ai để ý. Khi họ thất bại, các quyết định được đưa ra dựa trên dữ liệu cũ, các mô hình đào tạo dựa trên rác, các báo cáo hiển thị những con số không thể tin được và niềm tin vào toàn bộ nền tảng dữ liệu bị xói mòn. Lỗi đường truyền dữ liệu là một trong những lỗi phổ biến nhất và tốn kém nhất trong các tổ chức công nghệ.
---

## Các chế độ lỗi thường gặp
### Vấn đề về chất lượng dữ liệu
| Thất bại | Mô tả | Tác động | Độ khó phát hiện |
|----------|-------------|--------|----------------------|
| **Hỏng dữ liệu thầm lặng** | Dữ liệu được sửa đổi không chính xác mà không có bất kỳ lỗi nào phát sinh | Hệ thống hạ nguồn tin tưởng vào dữ liệu xấu; quyết định dựa trên thông tin sai lệch | Rất khó — không có tín hiệu lỗi |
| **Lược đồ trôi dạt** | Lược đồ thay đổi hệ thống nguồn (thêm, xóa, đổi tên cột) | Phá vỡ đường ống hoặc âm thầm làm rơi dữ liệu | Trung bình — đường ống có thể bị lỗi hoặc tạo ra một phần kết quả |
| **Loại dữ liệu không khớp** | Nguồn gửi chuỗi nơi số nguyên được mong đợi; thay đổi độ chính xác của phao | Đường ống bị lỗi; dữ liệu bị cắt bớt; lỗi làm tròn | Trung bình — có thể gây ra lỗi đường ống hoặc các vấn đề khó phát hiện về dữ liệu |
| **Bản ghi trùng lặp** | Cùng một sự kiện được xử lý nhiều lần | Số lượng tăng cao; tổng hợp không chính xác | Khó — mỗi bản ghi có vẻ hợp lệ riêng lẻ |
| **Giá trị rỗng/thiếu** | Các trường dự kiến ​​trống | Tính toán thất bại; mô hình đưa ra dự đoán sai | Trung bình - phụ thuộc vào việc xử lý null |
| **Giá trị ngoài phạm vi** | Giá trị nằm ngoài giới hạn dự kiến ​​(độ tuổi âm; ngày trong tương lai) | Thống kê sai lệch; logic kinh doanh bị hỏng | Trung bình — yêu cầu quy tắc xác thực |
| **Dữ liệu đến muộn** | Dữ liệu đến sau khi cửa sổ xử lý đóng | Kết quả không đầy đủ; hồ sơ bị bỏ lỡ | Khó — kết quả có vẻ hoàn chỉnh nhưng không phải |
### Vấn đề về cơ sở hạ tầng đường ống
| Thất bại | Mô tả | Tác động |
|----------|-------------|--------|
| **Phối hợp thất bại** | Bộ lập lịch (Airflow, Prefect) không kích hoạt đường ống | Dữ liệu đã cũ; không xảy ra quá trình xử lý |
| **Cạn kiệt tài nguyên** | Đường ống hết bộ nhớ, CPU hoặc đĩa | Sự cố đường ống; kết quả một phần |
| **Lỗi phụ thuộc** | Hệ thống ngược dòng không hoạt động hoặc chậm | Đường ống chờ vô thời hạn hoặc bị lỗi |
| **Vấn đề tương tranh** | Nhiều đường ống sửa đổi cùng một dữ liệu cùng một lúc | Điều kiện cuộc đua; tham nhũng dữ liệu |
| **Trôi cấu hình** | Các thay đổi về môi trường (mạng, thông tin xác thực, điểm cuối) không được phản ánh trong quy trình | Đường ống bị lỗi bất ngờ |
| **Áp lực ngược** | Dữ liệu đến nhanh hơn khả năng xử lý của đường ống | Hàng đợi ngày càng tăng; tăng độ trễ |
---

## Nghiên cứu trường hợp
### Nghiên cứu điển hình 1: Sao chép dữ liệu thầm lặng
| Khía cạnh | Mô tả |
|--------|-------------|
| **Kịch bản** | Quy trình đặt hàng của một công ty thương mại điện tử xử lý các sự kiện từ hàng đợi tin nhắn |
| **Đã xảy ra lỗi gì** | Việc khởi động lại của người tiêu dùng khiến tin nhắn được sử dụng lại; không tồn tại logic chống trùng lặp |
| **Tác động** | Số liệu doanh thu đã tăng 15% trong 3 tuần trước khi có người nhận ra |
| **Nguyên nhân gốc rễ** | Không có phím bình thường; giao hàng ít nhất một lần mà không bị trùng lặp |
| **Sửa** | Đã thêm khóa bình thường dựa trên ID đơn hàng; thực hiện ngữ nghĩa chính xác một lần |
| **Bài học** | Việc phân phối ít nhất một lần yêu cầu loại bỏ sự trùng lặp; luôn xác thực tổng số so với hệ thống nguồn |
### Nghiên cứu trường hợp 2: Sự thay đổi của lược đồ ở hạ lưu
| Khía cạnh | Mô tả |
|--------|-------------|
| **Kịch bản** | Nhà cung cấp thanh toán thay đổi tên trường trong phản hồi API của họ |
| **Đã xảy ra lỗi gì** | Đường dẫn ETL âm thầm bắt đầu ghi các giá trị null; không có xác nhận lược đồ |
| **Tác động** | Báo cáo tài chính cho thấy doanh thu bằng 0 từ phương thức thanh toán đó trong 2 tháng |
| **Nguyên nhân gốc rễ** | Không xác thực lược đồ khi nhập; giá trị null được coi là hợp lệ |
| **Sửa** | Đã thêm xác thực lược đồ bằng các cảnh báo; các trường bắt buộc được thực thi; kiểm tra null |
| **Bài học** | Không bao giờ tin tưởng các lược đồ bên ngoài sẽ ổn định; xác nhận tại ranh giới |
### Nghiên cứu trường hợp 3: Thảm họa múi giờ
| Khía cạnh | Mô tả |
|--------|-------------|
| **Kịch bản** | Một công ty toàn cầu tổng hợp số liệu hàng ngày ở các văn phòng |
| **Đã xảy ra lỗi gì** | Một số nguồn sử dụng UTC, một số khác sử dụng giờ địa phương; đường ống không bình thường hóa |
| **Tác động** | Tổng số hàng ngày không khớp; một số giao dịch được tính sai ngày; đóng sai cuối tháng |
| **Nguyên nhân gốc rễ** | Không có chính sách múi giờ tiêu chuẩn; dấu thời gian được lưu trữ không nhất quán |
| **Sửa** | Tất cả các dấu thời gian được lưu trữ dưới dạng UTC; chỉ chuyển đổi sang giờ địa phương ở lớp trình bày |
| **Bài học** | Chuẩn hóa UTC ở mọi nơi; rõ ràng về múi giờ ở mọi ranh giới |
---

## Chiến lược phòng ngừa
### Xác thực dữ liệu
| Chiến lược | Mô tả | Ví dụ về công cụ |
|----------|-------------|---------------|
| **Xác thực lược đồ** | Xác minh dữ liệu khớp với lược đồ dự kiến ​​ở từng giai đoạn | Kỳ vọng lớn lao; Deequ; Nước ngọt |
| **Kiểm tra phạm vi** | Giá trị nằm trong giới hạn dự kiến ​​| Xác nhận tùy chỉnh; kiểm tra dbt |
| **Kiểm tra độ tươi** | Dữ liệu đủ gần đây để hữu ích | Giám sát dấu thời gian; Cảnh báo SLA |
| **Kiểm tra khối lượng** | Số lượng hàng nằm trong phạm vi dự kiến ​​| Phát hiện bất thường về số lượng hàng |
| **Tính toàn vẹn tham chiếu** | Khóa ngoại khớp; không có hồ sơ mồ côi | các ràng buộc SQL; công cụ chất lượng dữ liệu |
| **Đối chiếu nguồn chéo** | Tổng số khớp giữa nguồn và đích | Công việc đối chiếu tự động |
### Mẫu thiết kế đường ống
| Mẫu | Mô tả | Lợi ích |
|----------|-------------|----------|
| **Idempotence** | Chạy quy trình nhiều lần sẽ tạo ra kết quả tương tự | An toàn để thử lại; không trùng lặp |
| **Tính nguyên tử** | Đường ống thành công hoàn toàn hoặc thất bại hoàn toàn (không có trạng thái một phần) | Không có dữ liệu được xử lý một nửa |
| **Điểm kiểm tra** | Lưu tiến độ ở từng giai đoạn; tiếp tục từ điểm kiểm tra cuối cùng | Khả năng chịu lỗi; không tái chế |
| **Hàng đợi thư chết** | Hồ sơ không đạt sẽ được chuyển sang hàng đợi riêng để điều tra | Không mất dữ liệu; có thể điều tra và phát lại |
| **Bộ ngắt mạch** | Dừng xử lý khi quá trình xuôi dòng bị lỗi | Ngăn chặn sự cố xếp tầng |
| **Hợp đồng dữ liệu** | Thỏa thuận giữa nhà sản xuất và người tiêu dùng về định dạng dữ liệu | Các thay đổi lược đồ được phối hợp |
### Giám sát và cảnh báo
| Những gì cần theo dõi | Tại sao | Như thế nào |
|-----------------|------|------|
| **Thời lượng đường ống** | Vấn đề về tín hiệu thời lượng tăng | Phân tích xu hướng; Theo dõi SLA |
| **Số hàng** | Những thay đổi đột ngột cho thấy có vấn đề | So sánh với mức trung bình lịch sử |
| **Tỷ lệ không** | Tăng lược đồ tín hiệu null hoặc các vấn đề về nguồn | Theo dõi null cấp cột |
| **Làm mới dữ liệu** | Dữ liệu cũ có nghĩa là đường ống không chạy | Dấu thời gian của kỷ lục mới nhất |
| **Tác động xuôi dòng** | Các báo cáo và mô hình có sử dụng dữ liệu chính xác không? | Dòng dữ liệu đầu cuối |
| **Sử dụng tài nguyên** | CPU; ký ức; đĩa; mạng | Giám sát cơ sở hạ tầng |
---

## Chiến lược phục hồi
| Tình huống | Chiến lược |
|----------||----------|
| **Dữ liệu xấu đã có trong kho** | Xác định phạm vi thời gian bị ảnh hưởng; xử lý lại từ nguồn; thông báo cho người tiêu dùng hạ lưu |
| **Sự cố đường ống giữa chừng** | Thiết kế bình thường cho phép chạy lại an toàn; điểm kiểm tra cho phép sơ yếu lý lịch |
| **Thay đổi lược đồ đã làm hỏng đường dẫn** | Sửa chữa chuyển đổi; chèn lấp dữ liệu bị ảnh hưởng; thêm xử lý tiến hóa lược đồ |
| **Tham nhũng thầm lặng được phát hiện muộn** | Phân tích nguyên nhân gốc rễ; xác định bán kính vụ nổ; tái xử lý; thêm giám sát để phát hiện tái phát |
| **Mất dữ liệu** | Khôi phục từ bản sao lưu; phát lại từ nguồn; đánh giá xem tổn thất có thể thu hồi được hay không |
---

## Bản tóm tắt
Lỗi đường truyền dữ liệu xảy ra phổ biến và thường tốn kém hơn so với việc ngừng ứng dụng vì chúng tạo ra các câu trả lời sai thay vì lỗi rõ ràng. Lỗi dữ liệu thầm lặng, trôi dạt lược đồ, trùng lặp, lỗi múi giờ và thiếu giá trị là những thủ phạm phổ biến nhất. Các chiến lược phòng ngừa chính là: xác thực dữ liệu ở mọi ranh giới (lược đồ, phạm vi, khối lượng, độ mới); thiết kế các đường ống trở nên bình thường và nguyên tử; giám sát mọi thứ (thời lượng, số hàng, tỷ lệ null, độ mới); sử dụng hàng đợi thư chết cho các bản ghi không thành công; và thiết lập hợp đồng dữ liệu giữa nhà sản xuất và người tiêu dùng. Khi xảy ra lỗi, phản hồi phải bao gồm phân tích nguyên nhân gốc rễ, xử lý lại dữ liệu bị ảnh hưởng, thông báo cho người tiêu dùng ở hạ nguồn và - quan trọng - bổ sung giám sát để phát hiện loại lỗi tương tự trong tương lai. Các tổ chức có được quyền này xử lý các đường dẫn dữ liệu một cách nghiêm ngặt như phần mềm sản xuất: kiểm tra, giám sát, cảnh báo, ứng phó sự cố và khám nghiệm tử thi.