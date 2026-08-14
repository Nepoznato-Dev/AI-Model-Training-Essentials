<!--
---
# Metadata
title: "Data Ethics and Privacy"
description: "GDPR, data consent, algorithmic bias, dark patterns, anonymisation"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, ethics, privacy, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Đạo đức dữ liệu và quyền riêng tư
Đạo đức dữ liệu là nghiên cứu về cách thu thập, phân tích và triển khai dữ liệu ảnh hưởng đến quyền, quyền tự chủ và phúc lợi của mọi người. Quyền riêng tư là mối quan tâm cụ thể về người kiểm soát thông tin cá nhân và cách thông tin đó được chia sẻ. Các chủ đề này đã chuyển từ các cuộc tranh luận học thuật sang tin tức trên trang nhất - thực thi GDPR, vi phạm dữ liệu ảnh hưởng đến hàng tỷ người dùng và ngày càng nâng cao nhận thức của công chúng rằng hoạt động sử dụng dữ liệu của các công ty công nghệ có hậu quả thực sự đối với dân chủ, bình đẳng và tự do cá nhân.
---

## Tại sao đạo đức dữ liệu lại quan trọng
| Mối quan tâm | Mô tả | Tác động trong thế giới thực |
|----------|-------------|-------------------|
| **Chủ nghĩa tư bản giám sát** | Các công ty kiếm tiền từ dữ liệu cá nhân trên quy mô lớn | Mất quyền riêng tư; thao túng hành vi |
| **Độ lệch thuật toán** | Các mô hình được đào tạo về dữ liệu sai lệch tái tạo sai lệch | Phân biệt đối xử trong tuyển dụng, cho vay, kiểm soát |
| **Sự đồng ý có hiểu biết** | Người dùng không hiểu họ đồng ý với điều gì | Dữ liệu được thu thập cho một mục đích được sử dụng cho mục đích khác |
| **Vi phạm dữ liệu** | Dữ liệu nhạy cảm bị lộ do bảo mật kém | Trộm cắp danh tính; gian lận tài chính; thiệt hại về danh tiếng |
| **Lọc bong bóng** | Nguồn cấp dữ liệu được cá nhân hóa củng cố niềm tin hiện có | Phân cực chính trị; thông tin sai lệch |
| **Mẫu tối** | Giao diện người dùng được thiết kế để lừa người dùng chia sẻ dữ liệu | Đăng ký không mong muốn; chia sẻ dữ liệu ngoài ý muốn |
---

## Khung và quy định về quyền riêng tư
### Luật bảo mật chính
| Quy định | Vùng | Yêu cầu chính |
|----------|--------|-----------------|
| **GDPR** (Quy định chung về bảo vệ dữ liệu) | EU / EEA | Căn cứ hợp pháp để xử lý; quyền truy cập; quyền được lãng quên; khả năng di chuyển dữ liệu; Thông báo vi phạm 72 giờ; phạt tới 4% doanh thu toàn cầu |
| **CCPA / CPRA** (Đạo luật về quyền riêng tư của California) | California, Hoa Kỳ | Quyền được biết; quyền xóa; quyền từ chối bán hàng; lựa chọn tham gia hạn chế cho trẻ em |
| **LGPD** (Lei Geral de Proteção de Dados) | Brazil | Tương tự như GDPR; cơ sở hợp pháp; quyền của chủ thể dữ liệu; Yêu cầu DPO |
| **PIPL** (Luật bảo vệ thông tin cá nhân) | Trung Quốc | Cần có sự đồng ý; nội địa hóa dữ liệu; hạn chế chuyển tiền xuyên biên giới |
| **POPIA** (Đạo luật bảo vệ thông tin cá nhân) | Nam Phi | Điều kiện xử lý hợp pháp; quyền của chủ thể dữ liệu; điều chỉnh |
| **Đạo luật DPDP** (Đạo luật bảo vệ dữ liệu cá nhân kỹ thuật số) | Ấn Độ | Bằng lòng; giới hạn mục đích; quyền chính về dữ liệu; nghĩa vụ ủy thác dữ liệu |
### Nguyên tắc cốt lõi của GDPR
| Nguyên tắc | Yêu cầu |
|----------||-------------|
| **Tính hợp pháp, công bằng, minh bạch** | Xử lý dữ liệu một cách hợp pháp; không đánh lừa người dùng; cởi mở về những gì bạn thu thập |
| **Giới hạn mục đích** | Chỉ thu thập dữ liệu cho các mục đích rõ ràng, cụ thể |
| **Giảm thiểu dữ liệu** | Chỉ thu thập những gì bạn thực sự cần |
| **Độ chính xác** | Giữ dữ liệu chính xác; sửa hoặc xóa dữ liệu không chính xác |
| **Giới hạn bộ nhớ** | Đừng giữ dữ liệu lâu hơn mức cần thiết |
| **Tính toàn vẹn và bảo mật** | Bảo mật dữ liệu khỏi bị truy cập và mất mát trái phép |
| **Trách nhiệm** | Thể hiện sự tuân thủ tất cả những điều trên |
---

## Kỹ thuật bảo vệ quyền riêng tư
| Kỹ thuật | Nó hoạt động như thế nào | Đánh đổi |
|----------|-------------|----------|
| **Ẩn danh** | Xóa thông tin nhận dạng cá nhân (PII) | Khó ẩn danh hoàn toàn; rủi ro tái nhận dạng |
| **Bí danh** | Thay thế số nhận dạng bằng bút danh | Có thể đảo ngược; vẫn là dữ liệu cá nhân theo GDPR |
| **Quyền riêng tư khác biệt** | Thêm tiếng ồn đã hiệu chỉnh vào kết quả truy vấn | Giảm độ chính xác; cung cấp bảo đảm quyền riêng tư về toán học |
| **Học tập liên kết** | Đào tạo mô hình trên thiết bị; chỉ chia sẻ thông tin cập nhật về mô hình | Đào tạo chậm hơn; chi phí truyền thông |
| **Tính toán an toàn cho nhiều bên** | Nhiều bên tính toán một hàm mà không tiết lộ đầu vào | Tính toán đắt tiền; phức tạp để thực hiện |
| **Mã hóa đồng cấu** | Thực hiện tính toán trên dữ liệu được mã hóa | Rất chậm; hỗ trợ hoạt động hạn chế |
| **Mặt nạ dữ liệu** | Ẩn các phần dữ liệu (ví dụ:`***-**-1234`) | Bảo vệ đơn giản nhưng hạn chế |
---

## Thu thập dữ liệu đạo đức
### Nguyên tắc thu thập có đạo đức
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Sự đồng ý có hiểu biết** | Người dùng hiểu những gì họ đồng ý; không được chôn cất trong pháp luật |
| **Mục đích minh bạch** | Nêu rõ lý do dữ liệu được thu thập và dữ liệu sẽ được sử dụng như thế nào |
| **Bộ sưu tập tối thiểu** | Chỉ thu thập những gì cần thiết cho mục đích đã nêu |
| **Kiểm soát người dùng** | Cho phép người dùng truy cập, sửa, tải xuống và xóa dữ liệu của họ |
| **Lưu giữ có giới hạn** | Xóa dữ liệu khi không còn cần thiết |
| **Đánh giá tác động** | Đánh giá tác hại tiềm ẩn trước khi thu thập dữ liệu nhạy cảm |
### Các mẫu tối phổ biến
| Mẫu | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Khai thác quyền riêng tư** | Lừa người dùng chia sẻ nhiều hơn dự định | "Chia sẻ với bạn bè" được kiểm tra trước khi đăng ký |
| **Nhà nghỉ Roach** | Dễ dàng đăng ký; khó hủy | Xóa tài khoản cần gọi điện thoại hoặc fax |
| **Bắt buộc phải liên tục** | Dùng thử miễn phí chuyển đổi sang trả phí mà không cần thông báo rõ ràng | Phí đăng ký xuất hiện trên thẻ tín dụng |
| **Xác nhận đáng xấu hổ** | Cảm giác tội lỗi khi người dùng chọn tham gia | "Không, cảm ơn, tôi không muốn tiết kiệm tiền" |
| **Cài đặt ẩn** | Kiểm soát quyền riêng tư được chôn sâu trong menu | Chọn không tham gia ẩn dưới 5 cấp độ cài đặt |
---

## Sự thiên vị và công bằng trong dữ liệu
| Nguồn thiên vị | Mô tả | Ví dụ |
|-------|--------------------------|----------|
| **Thành kiến ​​lựa chọn** | Dữ liệu không đại diện cho nhóm đối tượng mục tiêu | Đào tạo mô hình tuyển dụng dựa trên dữ liệu chỉ từ một nhóm nhân khẩu học |
| **Thành kiến ​​lịch sử** | Sự phân biệt đối xử trong quá khứ được mã hóa trong dữ liệu | Hồ sơ bắt giữ phản ánh các hoạt động trị an thiên vị |
| **Độ lệch đo lường** | Các biến được sử dụng làm proxy đều có sai sót | Sử dụng mã zip làm đại diện cho uy tín tín dụng |
| **Thành kiến ​​tổng hợp** | Đối xử với các nhóm đa dạng như đồng nhất | Một mô hình cho mọi dân tộc; bỏ qua các mẫu dành riêng cho nhóm |
| **Thành kiến ​​sống sót** | Chỉ nhìn vào những trường hợp thành công | Nghiên cứu các công ty khởi nghiệp thành công và bỏ qua những công ty thất bại |
### Chiến lược giảm thiểu
| Chiến lược | Mô tả |
|----------|-------------|
| **Thu thập dữ liệu đa dạng** | Đảm bảo dữ liệu đào tạo đại diện cho tất cả các nhóm bị ảnh hưởng |
| **Kiểm toán thiên vị** | Thường xuyên kiểm tra các mô hình về tác động khác nhau giữa các nhóm |
| **Chỉ số công bằng** | Đo lường sự bình đẳng về nhân khẩu học, cơ hội bình đẳng, tỷ lệ chênh lệch ngang bằng |
| **Đánh giá của con người** | Yêu cầu con người xem xét các quyết định mang tính rủi ro cao |
| **Báo cáo minh bạch** | Xuất bản dữ liệu về hiệu suất mô hình theo nhân khẩu học |
| **Sự tham gia của cộng đồng** | Thu hút sự tham gia của cộng đồng bị ảnh hưởng vào việc thiết kế và đánh giá |
---

## Quản trị dữ liệu
### Vai trò trong Quản trị Dữ liệu
| Vai trò | Trách nhiệm |
|------|--------------|
| **Chủ sở hữu dữ liệu** | Lãnh đạo cấp cao chịu trách nhiệm về miền dữ liệu |
| **Người quản lý dữ liệu** | Quản lý hàng ngày; chất lượng; phân loại |
| **Nhân viên bảo vệ dữ liệu (DPO)** | tuân thủ GDPR; đánh giá tác động đến quyền riêng tư; liên lạc với cơ quan quản lý |
| **Kỹ sư dữ liệu** | Đường ống; kho; chuyển đổi |
| **Nhà khoa học dữ liệu** | Phân tích; mô hình hóa; báo cáo |
| **Nhà phân tích quyền riêng tư dữ liệu** | Giám sát việc tuân thủ; xử lý các yêu cầu chủ đề dữ liệu |
### Phân loại dữ liệu
| Phân loại | Mô tả | Xử lý |
|--------------|-------------|----------|
| **Công cộng** | Có thể được chia sẻ miễn phí | Không hạn chế |
| **Nội bộ** | Chỉ dành cho nhân viên | Kiểm soát truy cập; không chia sẻ ra bên ngoài |
| **Bí mật** | Dữ liệu kinh doanh nhạy cảm | Mã hóa; kiểm soát truy cập nghiêm ngặt; ghi nhật ký kiểm tra |
| **Bị hạn chế** | Độ nhạy cao; quy định (PII, sức khỏe, tài chính) | Mã hóa khi lưu trữ và đang chuyển tiếp; DLP; truy cập tối thiểu |
---

## Bản tóm tắt
Đạo đức dữ liệu và quyền riêng tư không còn là những cân nhắc tùy chọn nữa — chúng là các yêu cầu pháp lý, mệnh lệnh kinh doanh và nghĩa vụ đạo đức. GDPR và các quy định tương tự thiết lập các quy tắc rõ ràng: thu thập ở mức tối thiểu, sử dụng minh bạch, bảo vệ nghiêm ngặt và trao cho người dùng quyền kiểm soát. Các kỹ thuật bảo vệ quyền riêng tư như quyền riêng tư khác biệt, học tập liên kết và mã hóa giúp có thể lấy được giá trị từ dữ liệu mà không làm lộ thông tin cá nhân. Nhưng chỉ công nghệ thôi là chưa đủ. Các tổ chức cần cấu trúc quản trị dữ liệu, thực hành kiểm toán thiên vị và văn hóa coi dữ liệu cá nhân là thứ cần được quản lý chứ không chỉ khai thác. Những công ty có được quyền này sẽ có được sự tin tưởng; những người không làm như vậy sẽ phải đối mặt với các khoản phạt theo quy định, phản ứng dữ dội của công chúng và sự sẵn sàng chia sẻ dữ liệu của người dùng sẽ dần bị xói mòn.