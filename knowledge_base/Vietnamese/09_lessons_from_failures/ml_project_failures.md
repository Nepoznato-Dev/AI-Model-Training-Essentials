---
# Metadata
title: "Machine Learning Project Failures"
description: "Data leakage, expectation mismatches, deployment failures, model decay"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, project, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Thất bại của dự án Machine Learning
Các dự án học máy thất bại ở mức đáng báo động - ước tính của ngành cho thấy 60-85% dự án ML không bao giờ đi vào sản xuất. Những thất bại thường không nằm ở thuật toán; chúng đang ở trong quá trình, dữ liệu, kỳ vọng và bối cảnh tổ chức. Hiểu lý do tại sao các dự án ML thất bại là điều cần thiết đối với bất kỳ ai xây dựng hệ thống ML, bởi vì các chế độ lỗi có thể dự đoán được và phần lớn có thể tránh được.
---

## Tại sao dự án ML thất bại
### Loại lỗi
| Danh mục | Chia sẻ thất bại | Mô tả |
|----------|-------------------|-------------|
| **Vấn đề về dữ liệu** | ~30% | Dữ liệu không đủ, sai lệch, cũ hoặc không thể truy cập |
| **Định nghĩa vấn đề** | ~20% | Vấn đề ML không phù hợp với nhu cầu kinh doanh |
| **Kỳ vọng không phù hợp** | ~15% | Các bên liên quan mong đợi điều kỳ diệu; thực tế là sự cải tiến gia tăng |
| **Triển khai thất bại** | ~15% | Mô hình hoạt động trong máy tính xách tay nhưng không thể sản xuất được |
| ** các vấn đề về tổ chức** | ~10% | Không có quyền sở hữu rõ ràng; đội thiếu kỹ năng; không có hỗ trợ điều hành |
| **Hiệu suất mô hình** | ~10% | Mô hình không đạt được độ chính xác cần thiết hoặc có tính khái quát kém |
---

## Lỗi liên quan đến dữ liệu
### Các vấn đề thường gặp về dữ liệu
| Vấn đề | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Không đủ dữ liệu** | Không đủ ví dụ để học các mẫu có ý nghĩa | Đào tạo mô hình phát hiện gian lận trên 500 giao dịch |
| **Chất lượng nhãn** | Nhãn đào tạo sai, không nhất quán hoặc chủ quan | Hình ảnh y tế được dán nhãn bởi những người không phải chuyên gia; nhãn tình cảm có thỏa thuận giữa những người đánh giá thấp |
| **Rò rỉ dữ liệu** | Thông tin từ tương lai hoặc mục tiêu rò rỉ vào các tính năng | Sử dụng kết quả rời bỏ khách hàng làm tính năng; bao gồm dữ liệu kiểm tra trong đào tạo |
| **Thành kiến ​​lựa chọn** | Dữ liệu đào tạo không đại diện cho số lượng triển khai | Đào tạo mô hình y tế trên dữ liệu từ một bệnh viện; triển khai toàn quốc |
| **Trôi khái niệm** | Mối quan hệ giữa đặc điểm và mục tiêu thay đổi theo thời gian | Hành vi của người tiêu dùng thay đổi sau đại dịch; mô hình được đào tạo về dữ liệu trước đại dịch |
| **Tính năng không khớp** | Các tính năng có sẵn trong quá trình đào tạo khác với các tính năng có sẵn trong sản xuất | Đào tạo với nhãn thủ công; sản xuất sử dụng nhãn tự động với cách phân phối khác nhau |
| **Mất cân bằng giai cấp** | Các lớp mục tiêu có độ lệch cao | 99% âm tính, 1% dương tính; người mẫu học cách luôn dự đoán tiêu cực |
### Vấn đề rò rỉ dữ liệu
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Rò rỉ mục tiêu** | Một tính năng chỉ khả dụng sau khi mục tiêu xảy ra | "Kết quả điều trị" được sử dụng như một tính năng để dự đoán "thành công điều trị" |
| **Ô nhiễm trong thử nghiệm tàu** | Dữ liệu kiểm tra ảnh hưởng đến việc đào tạo | Mở rộng quy mô với số liệu thống kê toàn cầu (bao gồm dữ liệu thử nghiệm); tăng dữ liệu bị rò rỉ |
| **Độ lệch lấy mẫu** | Đào tạo và sản xuất sử dụng mẫu khác nhau | Đào tạo về lưu lượng truy cập web; triển khai trên lưu lượng ứng dụng di động |
| **Rò rỉ trước khi xử lý** | Bước tiền xử lý sử dụng thông tin từ bộ dữ liệu đầy đủ | Nhập các giá trị còn thiếu bằng giá trị trung bình toàn cầu (bao gồm dữ liệu thử nghiệm) |
---

## Lỗi định nghĩa vấn đề
### Mẫu sai lệch
| Mẫu | Mô tả | Hậu quả |
|----------|-------------|-------------|
| **Giải quyết vấn đề sai** | Nhu cầu kinh doanh X; xây dựng nhóm Y | Mô hình tốt về mặt kỹ thuật nhưng vô dụng |
| **ML khi quy tắc là đủ** | Vấn đề có quy luật tất định; ML thêm độ phức tạp | Kỹ thuật quá mức; khó bảo trì hơn; ít diễn giải hơn |
| **ML khi dữ liệu không tồn tại** | Sự cố yêu cầu dữ liệu chưa được thu thập | Dự án không thể bắt đầu; nhiều tháng lãng phí vì tính khả thi |
| **Mục tiêu chính xác không có bối cảnh kinh doanh** | "Chúng tôi cần độ chính xác 95%" — nhưng điều đó có ý nghĩa gì đối với doanh nghiệp? | Mô hình đáp ứng độ chính xác nhưng không giải quyết được bài toán kinh doanh |
| **Bỏ qua chi phí do sai sót** | Dương tính giả và âm tính giả có chi phí khác nhau | Mô hình tối ưu hóa số liệu sai |
| **Không có đường cơ sở** | Không so sánh với cách tiếp cận hiện tại | Không thể biết liệu ML có thực sự tốt hơn một phương pháp phỏng đoán đơn giản hay không |
---

## Thất bại như mong đợi
### Chu kỳ cường điệu trong các dự án ML
| Giai đoạn | Mô tả | Rủi ro |
|-------|-------------|------|
| **Hưng phấn** | "AI sẽ giải quyết mọi thứ!" | Quá hứa hẹn; thiếu nguồn lực |
| **Bằng chứng về khái niệm** | Mô hình hoạt động trên dữ liệu sạch trong sổ ghi chép | Sự tự tin sai lầm; "nó hoạt động!" |
| **Kiểm tra thực tế** | Dữ liệu sản xuất lộn xộn; hiệu suất giảm | Thất vọng; "ML không hoạt động" |
| **Cuộc hành quân tử thần** | Nhóm cố gắng ép nó vào sản xuất | Nợ kỹ thuật; kiệt sức |
| **Bỏ rơi hoặc triển khai trong im lặng** | Dự án bị hủy bỏ hoặc triển khai mà không có giám sát | Đầu tư lãng phí |
### Quản lý kỳ vọng
| Chiến lược | Mô tả |
|----------|-------------|
| **Bắt đầu với đường cơ sở** | So sánh với cách tiếp cận đơn giản nhất có thể (quy tắc; hiệu suất của con người) |
| **Xác định trước các chỉ số thành công** | Các số liệu kinh doanh (doanh thu; tiết kiệm chi phí) không chỉ các số liệu ML (độ chính xác; F1) |
| **Khám phá hộp thời gian** | Cho nhóm 2-4 tuần để đánh giá tính khả thi trước khi cam kết |
| **Cho thấy những gì ML không thể làm** | Hãy trung thực về những hạn chế; đặt kỳ vọng thực tế |
| **Lặp lại tăng dần** | Trước tiên hãy triển khai một mô hình đơn giản; cải tiến lặp đi lặp lại |
| **Định lượng chi phí sai sót** | Biến hiệu suất của mô hình thành tác động kinh doanh |
---

## Lỗi triển khai
### Tại sao người mẫu không được đưa vào sản xuất
| Vấn đề | Mô tả | Giải pháp |
|----------|-------------|----------|
| **Sổ tay cho khoảng cách sản xuất** | Mã hoạt động trong Jupyter nhưng chưa sẵn sàng để sản xuất | thực hành MLOps; CI/CD cho ML; đánh giá mã |
| **Yêu cầu về độ trễ** | Suy luận mô hình quá chậm để sử dụng trong thời gian thực | Tối ưu hóa mô hình; lượng tử hóa; bộ nhớ đệm |
| **Khả năng mở rộng** | Mô hình không thể xử lý lưu lượng sản xuất | Xử lý hàng loạt; chia tỷ lệ theo chiều ngang; mô hình phục vụ hạ tầng |
| **Khoảng trống giám sát** | Không có cách nào để phát hiện khi mô hình xuống cấp | Giám sát trôi dạt dữ liệu; giám sát hiệu suất; cảnh báo |
| **Quản lý phụ thuộc** | Môi trường đào tạo và phục vụ khác nhau | Container hóa; môi trường tái tạo |
| **Không có kế hoạch khôi phục** | Không thể quay lại mô hình trước khi mô hình mới bị lỗi | Đăng ký mẫu; phiên bản; khôi phục tự động |
### Suy thoái mô hình
| Loại | Mô tả | Phát hiện |
|------|-------------|----------|
| **Trôi dạt dữ liệu** | Thay đổi phân phối tính năng đầu vào | Theo dõi số liệu thống kê tính năng; KL phân kỳ; PSI |
| **Trôi khái niệm** | Mối quan hệ giữa tính năng và thay đổi mục tiêu | Theo dõi độ chính xác của dự đoán theo thời gian |
| **Trôi nhãn** | Định nghĩa hoặc phân bổ các thay đổi mục tiêu | Theo dõi phân phối nhãn; tương quan số liệu kinh doanh |
| **Những thay đổi ngược dòng** | Nguồn dữ liệu thay đổi định dạng, thời gian hoặc chất lượng | Xác thực lược đồ; giám sát độ tươi |
---

## Thất bại về mặt tổ chức
| Thất bại | Mô tả | Phòng ngừa |
|----------|-------------|-------------|
| **Không có quyền sở hữu rõ ràng** | Không ai chịu trách nhiệm về mô hình trong sản xuất | Chỉ định chủ sở hữu mô hình; định nghĩa RACI |
| **Các đội riêng lẻ** | Các nhà khoa học dữ liệu xây dựng mô hình; kỹ sư triển khai; không ai giao tiếp | Các nhóm đa chức năng; mục tiêu chung |
| **Không có thời gian đáo hạn MLOps** | Không có đăng ký mô hình; không có CI/CD; không giám sát | Đầu tư tăng dần vào cơ sở hạ tầng MLOps |
| **Các mốc thời gian không thực tế** | "Xây dựng hệ thống ML sản xuất trong 2 tuần" | Khám phá hộp thời gian; lặp đi lặp lại; giao tiếp phức tạp |
| **Thiếu kiến ​​thức chuyên môn về miền** | Nhóm ML không hiểu vấn đề kinh doanh | Nhúng các chuyên gia tên miền vào nhóm ML |
| **Không có khung đánh giá** | Không thể biết mô hình có đang hoạt động trong sản xuất hay không | Xác định số liệu kinh doanh; thiết lập bảng điều khiển; đánh giá thường xuyên |
---

## Bài học rút ra
### Danh sách kiểm tra dự án ML
| Giai đoạn | Câu hỏi chính |
|-------|-------------|
| **Định nghĩa vấn đề** | Đây thực sự có phải là một vấn đề ML? Đường cơ sở là gì? Thành công trông như thế nào? |
| **Đánh giá dữ liệu** | Chúng ta có đủ dữ liệu không? Nó có tính đại diện không? Nhãn có đáng tin cậy không? |
| **Tính khả thi** | Chúng ta có thể xây dựng một nguyên mẫu hoạt động được trong 2-4 tuần không? Những rủi ro là gì? |
| **Phát triển** | Có rò rỉ dữ liệu không? Chúng ta có đang sử dụng thước đo đánh giá phù hợp không? |
| **Tiền sản xuất** | Nó có hoạt động với dữ liệu sản xuất không? Liệu nó có đủ nhanh không? Nó có được theo dõi không? |
| **Triển khai** | Chúng ta có thể quay lại được không? Ai đang trực? Điều gì xảy ra khi nó xuống cấp? |
| **Sau triển khai** | Có phải chúng ta đang theo dõi sự trôi dạt? Các số liệu kinh doanh có được theo dõi không? Có kế hoạch đào tạo lại không? |
---

## Bản tóm tắt
Các dự án ML thất bại không phải vì thuật toán quá khó mà vì quy trình xung quanh chúng bị hỏng. Các vấn đề về dữ liệu - dữ liệu không đầy đủ, nhãn kém, rò rỉ, trôi dạt - là nguyên nhân gây ra lỗi lớn nhất. Thất bại trong việc xác định vấn đề - giải quyết sai vấn đề, sử dụng ML khi các quy tắc là đủ, bỏ qua chi phí do sai sót - lãng phí hàng tháng trời nỗ lực. Thất bại trong kỳ vọng - hứa hẹn quá mức, phân phối dưới mức, không quản lý các bên liên quan - phá hủy niềm tin của tổ chức vào ML. Lỗi triển khai — khoảng cách từ máy tính xách tay đến sản xuất, vấn đề về độ trễ, không có giám sát — có nghĩa là các mô hình đang hoạt động trong quá trình phát triển không bao giờ tạo ra giá trị trong sản xuất. Những thất bại về mặt tổ chức - không có quyền sở hữu, các nhóm riêng lẻ, không có MLOps - khiến cho cấu trúc không thể thành công. Thuốc giải độc là thực hành có kỷ luật: bắt đầu từ đường cơ sở; khám phá hộp thời gian; xác thực dữ liệu một cách nghiêm ngặt; kiểm tra rò rỉ; xác định số liệu kinh doanh; triển khai tăng dần; giám sát liên tục; và lặp đi lặp lại. Các nhóm ML giỏi nhất dành nhiều thời gian cho dữ liệu và quy trình hơn là cho các mô hình.