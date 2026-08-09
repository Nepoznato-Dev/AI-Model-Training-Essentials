---
# Metadata
title: "Low-Code and Platform Engineering"
description: "Low-code platforms, internal developer platforms, golden paths"
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
tags: [low, code, platform, engineering, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Kỹ thuật nền tảng và mã thấp
Nền tảng mã thấp cho phép mọi người xây dựng ứng dụng với lượng mã viết tay tối thiểu — thường thông qua giao diện kéo và thả, quy trình làm việc trực quan và trình kết nối dựng sẵn. Kỹ thuật nền tảng là nguyên tắc xây dựng nền tảng dành cho nhà phát triển nội bộ (IDP) giúp nhóm sản phẩm dễ dàng tự phục vụ cơ sở hạ tầng, CI/CD và công cụ vận hành. Cả hai xu hướng đều là phản ứng cho cùng một vấn đề: khoảng cách giữa nhu cầu về phần mềm và nguồn cung của các nhà phát triển có thể xây dựng nó.
---

## Nền tảng mã thấp
### Low-Code thực sự có nghĩa là gì
| Khía cạnh | Mô tả |
|--------|-------------|
| **Phát triển thị giác** | Trình tạo giao diện người dùng kéo và thả; trình chỉnh sửa quy trình làm việc trực quan; nhà thiết kế mẫu |
| **Các thành phần dựng sẵn** | Các vật dụng, trình kết nối, mẫu và tích hợp được tạo sẵn |
| **Logic khai báo** | Định cấu hình hành vi thông qua các quy tắc và điều kiện thay vì viết mã |
| **Khả năng mở rộng** | Khả năng thêm mã tùy chỉnh khi khả năng tích hợp của nền tảng không đủ |
| **Cơ sở hạ tầng được quản lý** | Nền tảng xử lý việc lưu trữ, mở rộng quy mô, vá lỗi bảo mật |
### Nền tảng mã thấp phổ biến
| Nền tảng | Sức mạnh | Trường hợp sử dụng điển hình |
|----------|----------|--------|
| **Nền tảng Microsoft Power** | Tích hợp sâu Microsoft 365/Azure; Power Apps, Power Automate, Power BI | Quy trình làm việc của doanh nghiệp; công cụ nội bộ |
| **Nền tảng Salesforce** | Nguồn gốc CRM; Apex cho tiện ích mở rộng; Trình tạo dòng chảy | Ứng dụng hướng tới khách hàng; quy trình bán hàng |
| **Dịch vụ ngay** | Quản lý dịch vụ CNTT; tự động hóa quy trình làm việc | Hoạt động CNTT; nhân sự; cơ sở vật chất |
| **Appian** | Khai thác quy trình; quản lý trường hợp | Quy trình kinh doanh phức tạp; tuân thủ |
| **Hệ thống ngoài** | Web và thiết bị di động đầy đủ; cấp doanh nghiệp | Cổng thông tin khách hàng; ứng dụng di động |
| **Trang bị lại** | Xây dựng công cụ nội bộ; kết nối với cơ sở dữ liệu và API | Bảng quản trị; bảng điều khiển; công cụ hoạt động |
| **Máy bay** | Kết hợp bảng tính-cơ sở dữ liệu; tự động hóa | Theo dõi dự án; CRM nhẹ |
### Khi Low-Code hoạt động tốt
| Kịch bản | Tại sao mã thấp phù hợp |
|----------|-------------------|
| **Công cụ nội bộ** | Xây dựng nhanh chóng; người dùng là người nội bộ nên tính linh hoạt của giao diện người dùng ít quan trọng hơn |
| **Các biểu mẫu và phê duyệt** | Những người xây dựng quy trình làm việc trực quan vượt trội ở điểm này |
| **Ứng dụng CRUD** | Hầu hết các nền tảng mã thấp đều được tối ưu hóa cho các mẫu tạo-đọc-cập nhật-xóa |
| **Tạo nguyên mẫu** | Xác thực một ý tưởng trong vài giờ thay vì hàng tuần |
| **Phát triển công dân** | Các nhà phân tích kinh doanh có thể xây dựng giải pháp của riêng họ với quản trị CNTT |
### Khi mã thấp bị thiếu
| Hạn chế | Tác động |
|----------||--------|
| **Khóa nhà cung cấp** | Các ứng dụng không thể dễ dàng di chuyển khỏi nền tảng |
| **Trần hiệu suất** | Không phù hợp với các ứng dụng có thông lượng cao hoặc nhạy cảm với độ trễ |
| **Ràng buộc về giao diện người dùng** | Thiết kế tùy chỉnh rất khó; bạn bị giới hạn ở những gì nền tảng hỗ trợ |
| **Độ phức tạp của việc tích hợp** | Việc kết nối với các API bất thường hoặc hệ thống cũ vẫn có thể yêu cầu mã tùy chỉnh |
| **Chi phí theo quy mô** | Giá cho mỗi người dùng hoặc mỗi ứng dụng có thể trở nên đắt đỏ khi mức sử dụng tăng lên |
| **Gỡ lỗi khó khăn** | Sự trừu tượng trực quan khiến việc chẩn đoán các vấn đề phức tạp trở nên khó khăn |
---

## Kỹ thuật nền tảng
### Kỹ thuật nền tảng giải quyết vấn đề
| Không có kỹ thuật nền tảng | Với Kỹ thuật nền tảng |
|------------------------------|---------------------------------------|
| Mỗi nhóm quản lý cơ sở hạ tầng của riêng mình | Nền tảng tự phục vụ tóm tắt cơ sở hạ tầng |
| Công cụ không nhất quán giữa các nhóm | Chuỗi công cụ được tiêu chuẩn hóa; những con đường vàng |
| Các nhà phát triển chờ ops cung cấp tài nguyên | Nhà phát triển cung cấp tài nguyên theo yêu cầu |
| Kho kiến ​​thức; kiến thức bộ lạc | Có tài liệu; tự động; có thể khám phá |
| Quá trình triển khai chậm cho các kỹ sư mới | Kỹ sư mới có thể triển khai ngay ngày đầu tiên |
### Các thành phần cốt lõi của Nền tảng nhà phát triển nội bộ
| Thành phần | Mục đích | Công cụ mẫu |
|----------||----------|---------------|
| **Danh mục dịch vụ** | Cơ quan đăng ký trung tâm của tất cả các dịch vụ và chủ sở hữu của chúng | Hậu trường; Cảng; Vỏ |
| **Giàn giáo mẫu** | Tạo dịch vụ mới từ các mẫu đã được phê duyệt | Mẫu phần mềm hậu trường; Máy cắt bánh quy |
| **Cơ sở hạ tầng tự phục vụ** | Các nhà phát triển cung cấp tài nguyên đám mây mà không cần nộp phiếu | Mô-đun địa hình; Pulumi; Máy bay đa năng |
| **Đường dẫn CI/CD** | Xây dựng, thử nghiệm, triển khai quy trình được chuẩn hóa | Hành động GitHub; GitLab CI; CD Argo |
| **Quản lý môi trường** | Môi trường phát triển/dàn dựng tạm thời theo yêu cầu | Vcluster; Không gian tên; Gitpod |
| **Khả năng quan sát** | Ghi nhật ký, số liệu, theo dõi được tích hợp trong mọi dịch vụ | Prometheus; Grafana; Đo từ xa mở; Cơ quan dữ liệu |
| **Quản lý bí mật** | Lưu trữ an toàn và luân chuyển thông tin đăng nhập | Kho tiền; Trình quản lý bí mật AWS; SOP |
| **Danh tính và quyền truy cập** | SSO; truy cập dựa trên vai trò; xác thực dịch vụ với dịch vụ | Được rồi; Áo choàng khóa; SPIFF |
### Những con đường vàng
Con đường vàng là cách được ủng hộ và có quan điểm để làm điều gì đó. Đó là con đường ít trở ngại nhất - nếu bạn đi theo nó, mọi thứ sẽ thành công. Bạn có thể đi chệch hướng, nhưng bạn phải tự mình đi.
| Con Đường Vàng | Nó cung cấp những gì |
|-------------|-----------------|
| **Dịch vụ mới** | Kho lưu trữ mẫu; CI/CD; giám sát; khai thác gỗ; cấu hình triển khai |
| **Cơ sở dữ liệu mới** | Phiên bản được cung cấp; chuỗi kết nối trong bí mật; cấu hình sao lưu |
| **Giao diện người dùng mới** | Xây dựng đường ống; CDN; môi trường xem trước; kiểm tra ngọn hải đăng |
| **Đường dẫn dữ liệu** | Dàn nhạc; xác nhận lược đồ; giám sát; cảnh báo |
### Quyết định xây dựng và mua
| Yếu tố | Xây dựng tùy chỉnh | Sử dụng công cụ hiện có |
|--------|-------------|-------------------|
| **Năng lực cốt lõi** | Duy nhất cho doanh nghiệp của bạn; lợi thế cạnh tranh | Hàng hóa; mọi công ty đều cần nó |
| **Gánh nặng bảo trì** | Bạn có khả năng duy trì nó | Công cụ được nhà cung cấp/cộng đồng duy trì tốt |
| **Nhu cầu hội nhập** | Yêu cầu tích hợp sâu với các hệ thống nội bộ | Đủ API và trình kết nối tiêu chuẩn |
| **Chi phí** | Xây dựng rẻ hơn giấy phép | Cấp phép rẻ hơn so với xây dựng |
---

## Mối quan hệ giữa mã thấp và kỹ thuật nền tảng
| Kích thước | Mã thấp | Kỹ thuật nền tảng |
|----------|----------|----------------------|
| **Người dùng mục tiêu** | Người dùng doanh nghiệp; nhà phát triển công dân | Kỹ sư phần mềm chuyên nghiệp |
| **Mục tiêu** | Giảm mã; tăng tốc độ | Giảm tải nhận thức; tăng quyền tự chủ |
| **Mức độ trừu tượng** | Rất cao; trực quan | Trung bình; dựa trên mã nhưng được đơn giản hóa |
| **Tính linh hoạt** | Bị giới hạn bởi khả năng của nền tảng | Hoàn toàn linh hoạt; bạn có thể viết bất kỳ mã nào |
| **Quản trị** | Nền tảng thực thi các quy tắc | Nền tảng cung cấp những con đường vàng |
Chúng bổ sung cho nhau: kỹ thuật nền tảng giúp các nhà phát triển chuyên nghiệp nhanh hơn, trong khi mã thấp cho phép những người không phải là nhà phát triển xây dựng các ứng dụng đơn giản. Cùng nhau, họ giải quyết khoảng cách phân phối phần mềm từ các góc độ khác nhau.
---

## Bản tóm tắt
Nền tảng mã thấp và nền tảng dành cho nhà phát triển nội bộ đều nhằm mục đích tăng số lượng người có thể cung cấp phần mềm. Low-code thực hiện điều này bằng cách trừu tượng hóa hoàn toàn mã - trình tạo trực quan, trình kết nối dựng sẵn, logic khai báo. Kỹ thuật nền tảng thực hiện điều này cho các nhà phát triển chuyên nghiệp bằng cách cung cấp cơ sở hạ tầng tự phục vụ, các đường dẫn vàng và công cụ được tiêu chuẩn hóa để họ dành ít thời gian hơn cho công việc vận hành và có nhiều thời gian hơn cho các tính năng của sản phẩm. Đây cũng không phải là viên đạn bạc: mã thấp có các hạn chế về hiệu suất và khả năng khóa của nhà cung cấp, đồng thời kỹ thuật nền tảng đòi hỏi phải đầu tư liên tục để duy trì. Nhưng khi áp dụng vào những vấn đề phù hợp — công cụ nội bộ, ứng dụng CRUD, cung cấp dịch vụ được tiêu chuẩn hóa — cả hai đều có thể giảm đáng kể thời gian từ ý tưởng đến sản xuất.