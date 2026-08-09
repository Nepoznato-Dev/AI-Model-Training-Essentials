---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ai, ethics, governance, ai-and-machine-learning]
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
# Đạo đức và Quản trị AI
Hệ thống AI không trung lập. Chúng phản ánh dữ liệu mà họ đã được đào tạo, giá trị của người tạo ra chúng và động lực của các tổ chức triển khai chúng. Đạo đức không chỉ là việc hỏi "chúng ta có thể xây dựng cái này không?" nhưng "chúng ta có nên không?" Quản trị là tạo ra các cấu trúc - luật pháp, tiêu chuẩn, cơ quan giám sát - để đảm bảo AI được phát triển và sử dụng một cách có trách nhiệm. Tệp này bao gồm các khía cạnh đạo đức quan trọng của AI và các khuôn khổ quản trị đang nổi lên để giải quyết chúng.
---

## Nguyên tắc đạo đức cốt lõi cho AI
Hầu hết các khuôn khổ đạo đức AI đều hội tụ một bộ nguyên tắc chung.
| Nguyên tắc | Ý nghĩa của nó | Thử thách |
|----------||--------------|----------|
| **Công bằng** | AI không nên phân biệt đối xử với các nhóm được bảo vệ | Định nghĩa sự công bằng về mặt toán học khó đến mức đáng kinh ngạc; xung đột định nghĩa công bằng khác nhau |
| **Minh bạch** | Người dùng nên biết khi nào họ tương tác với AI và cách thức hoạt động của nó | Tính minh bạch hoàn toàn có thể cho phép chơi game; hệ thống độc quyền chống lại việc tiết lộ |
| **Trách nhiệm** | Phải có người chịu trách nhiệm khi AI gây hại | Phân tán trách nhiệm giữa các nhà phát triển, người triển khai và người dùng |
| **Quyền riêng tư** | AI nên tôn trọng dữ liệu cá nhân và quyền tự chủ | Dữ liệu đào tạo thường bao gồm thông tin cá nhân; xung đột về quyền riêng tư và tiện ích |
| **An toàn** | AI không được gây tổn hại về thể chất hoặc tâm lý | Việc xác định tác hại phụ thuộc vào ngữ cảnh; trường hợp khó lường là không thể đoán trước |
| **Sự giám sát của con người** | Con người nên giữ quyền kiểm soát có ý nghĩa | Xu hướng tự động hóa có nghĩa là con người trì hoãn AI; giám sát trở thành cao su dập |
---

## Xu hướng trong hệ thống AI
### Xu hướng đến từ đâu
| Nguồn | Mô tả | Ví dụ |
|--------|-------------|----------|
| **Dữ liệu đào tạo** | Những thành kiến ​​lịch sử được mã hóa trong dữ liệu | Dữ liệu tuyển dụng phản ánh sự phân biệt đối xử trong quá khứ → mô hình phân biệt đối xử |
| **Thành kiến ​​về nhãn** | Người chú thích con người áp đặt thành kiến ​​​​của họ | Sơ yếu lý lịch có tên "nữ" được người chú thích đánh giá thấp hơn |
| **Thành kiến ​​lựa chọn** | Dữ liệu không đại diện cho nhóm đối tượng mục tiêu | Nhận dạng khuôn mặt được đào tạo chủ yếu trên khuôn mặt có làn da sáng |
| **Độ lệch đo lường** | Tính năng proxy cho các thuộc tính được bảo vệ | Mã zip tương quan với chủng tộc |
| **Độ lệch thuật toán** | Tối ưu hóa khuếch đại những thành kiến ​​nhỏ | Một lỗ hổng nhỏ trong dữ liệu huấn luyện sẽ trở thành một lỗ hổng lớn trong dự đoán |
### Số liệu công bằng
| Số liệu | Định nghĩa | Khi nào nên sử dụng |
|--------|-------------|-------------|
| **Bình đẳng về nhân khẩu học** | Tỷ lệ dương tính bằng nhau giữa các nhóm | Khi bạn muốn có kết quả bình đẳng |
| **Tỷ lệ cược ngang nhau** | Tỷ lệ dương tính thật và tỷ lệ dương tính giả bằng nhau giữa các nhóm | Khi bạn muốn tỷ lệ lỗi bằng nhau |
| **Tính chẵn lẻ dự đoán** | Độ chính xác là như nhau giữa các nhóm | Khi bạn muốn dự đoán có ý nghĩa giống nhau đối với tất cả các nhóm |
| **Sự công bằng cá nhân** | Những cá nhân tương tự được đối xử tương tự | Khi bạn muốn sự nhất quán |
**Định lý bất khả thi**: bạn thường không thể thỏa mãn nhiều định nghĩa về tính công bằng cùng một lúc. Việc lựa chọn thước đo công bằng nào để sử dụng bản thân nó đã là một đánh giá về giá trị.
### Giảm thiểu thành kiến
| Sân khấu | Kỹ thuật |
|-------|----------|
| **Tiền xử lý** | Cân bằng lại dữ liệu đào tạo; loại bỏ các tính năng sai lệch; lấy mẫu tổng hợp |
| **Đang xử lý** | Thêm các ràng buộc công bằng cho hàm mất mát; suy thoái đối nghịch |
| **Xử lý hậu kỳ** | Điều chỉnh ngưỡng cho mỗi nhóm; hiệu chỉnh dự đoán |
| **Đánh giá** | Kiểm toán công bằng thường xuyên; số liệu hiệu suất được phân tách |
---

## Khả năng giải thích
### Tại sao khả năng giải thích lại quan trọng
| Lý do | Mô tả |
|--------|-------------|
| **Tin tưởng** | Người dùng cần hiểu lý do đưa ra quyết định |
| **Gỡ lỗi** | Nhà phát triển cần tìm và sửa lỗi mô hình |
| **Quy định** | "Quyền giải thích" của GDPR; Yêu cầu về Đạo luật AI của EU |
| **Công bằng** | Bạn không thể phát hiện ra sự thiên vị nếu không hiểu hành vi của mô hình |
| **Trách nhiệm** | Các tổ chức cần biện minh cho các quyết định tự động |
### Phương pháp giải thích
| Phương pháp | Loại | Nó hoạt động như thế nào | Hạn chế |
|--------|------|-------------|----------||
| **CHẮC CHẮN** | Tầm quan trọng của tính năng | Ước tính sự đóng góp của từng tính năng bằng lý thuyết trò chơi | Tính toán đắt tiền; xấp xỉ |
| **VÔI** | Người thay thế địa phương | Phù hợp với một mô hình đơn giản xung quanh dự đoán | Không ổn định; không phản ánh logic mô hình thực tế |
| **Hình dung chú ý** | Cơ chế nội bộ | Hiển thị đầu vào nào mà mô hình tham gia | Chú ý ≠ tầm quan trọng; có thể gây hiểu nhầm |
| **Phản thực tế** | Phân tích điều gì xảy ra nếu | "Nếu đặc điểm này khác đi, liệu dự đoán có thay đổi không?" | Phụ thuộc vào phản thực tế thực tế |
| **Ghi công tính năng** | Điểm quan trọng | Bản đồ độ nổi, độ dốc tích hợp | Không giải thích *tại sao*; chỉ *ở đâu* |
---

## Quy định về AI
### Đạo luật AI của EU (2026)
Luật AI toàn diện đầu tiên trên thế giới.
| Mức độ rủi ro | Ví dụ | Yêu cầu |
|----------||----------|-------------|
| **Rủi ro không thể chấp nhận** | Tính điểm xã hội; thao tác thăng hoa; giám sát sinh trắc học thời gian thực (có ngoại lệ) | Bị cấm |
| **Rủi ro cao** | AI y tế; xe tự hành; thực thi pháp luật; cơ sở hạ tầng quan trọng | Đánh giá sự phù hợp; sự giám sát của con người; minh bạch |
| **Rủi ro hạn chế** | Chatbot; deepfake; hệ thống khuyến nghị | Phải tiết lộ sự tham gia của AI |
| **Rủi ro tối thiểu** | Bộ lọc thư rác; trò chơi điện tử; hầu hết các ứng dụng AI | Không có yêu cầu cụ thể |
### Các phương pháp quản lý khác
| Vùng | Tiếp cận | Trạng thái |
|--------|----------|--------|
| **Hoa Kỳ** | Theo ngành cụ thể; mệnh lệnh điều hành; cam kết tự nguyện | Bị phân mảnh; không có luật liên bang toàn diện |
| **Vương quốc Anh** | Dựa trên nguyên tắc; cơ quan quản lý ngành | Viện An toàn AI; cách tiếp cận ủng hộ đổi mới |
| **Trung Quốc** | Các quy định cụ thể về AI tổng hợp, deepfake, đề xuất | Thực thi tích cực; yêu cầu nội dung |
| **Canada** | AIDA (Đạo luật dữ liệu và trí tuệ nhân tạo) | Đề xuất; tương tự như cách tiếp cận của EU |
| **Brazil** | Khung quy định AI | Đang tiến hành |
---

##Tác động môi trường
Việc đào tạo và chạy các mô hình AI tiêu thụ năng lượng và tạo ra lượng khí thải carbon.
| Hoạt động | Lượng phát thải ước tính | So sánh |
|----------|-------------------|-------------|
| **Đào tạo GPT-4** | Ước tính hơn 50 tấn CO₂ | Tương đương với lượng khí thải hàng năm của một số ô tô |
| **Huấn luyện Transformer cỡ lớn** | 280-620 tấn CO₂ | gấp 5 lần lượng khí thải trong đời của một chiếc ô tô |
| **Suy luận hàng ngày (1 triệu người dùng)** | Đang diễn ra; phụ thuộc vào kích thước model và phần cứng | Có thể vượt quá lượng khí thải đào tạo theo thời gian |
| **Tinh chỉnh mô hình 7B** | 1-5 tấn CO₂ | Đáng kể nhưng ít hơn nhiều so với trước khi đào tạo |
### Giảm nhẹ
| Chiến lược | Tác động |
|----------|--------|
| **Phần cứng hiệu quả** | GPU mới tiết kiệm năng lượng hơn trên mỗi lần tính toán |
| **Tối ưu hóa mô hình** | Các mô hình lượng tử hóa nhỏ hơn sử dụng ít năng lượng hơn |
| **Năng lượng xanh** | Cung cấp năng lượng cho trung tâm dữ liệu bằng năng lượng tái tạo |
| **Kiến trúc hiệu quả** | Hỗn hợp các chuyên gia; mô hình thưa thớt; chưng cất |
| **Lập kế hoạch nhận biết carbon** | Chạy huấn luyện khi lưới sạch nhất |
---

## Sở hữu trí tuệ và bản quyền
| Vấn đề | Mô tả | Trạng thái |
|-------|-------------|--------|
| **Đào tạo về tác phẩm có bản quyền** | Người mẫu được đào tạo trên sách, bài viết, hình ảnh trái phép | Các vụ kiện tích cực; tranh luận về sử dụng hợp lý |
| **Đầu ra do AI tạo** | Ai sở hữu nội dung do AI tạo ra? | Văn phòng Bản quyền Hoa Kỳ: Nội dung do AI tạo ra không có bản quyền nếu không có đủ quyền tác giả của con người |
| **Giả phong cách** | AI có thể bắt chước phong cách của một nghệ sĩ | Màu xám hợp pháp; mối quan tâm về đạo đức |
| **Cơ chế từ chối** | Một số nhà cung cấp cho phép người sáng tạo chọn không tham gia đào tạo | robot.txt; lọc nội dung |
---

## Tiết lộ có trách nhiệm
| Nguyên tắc | Mô tả |
|----------||-------------|
| **Thử nghiệm trước khi triển khai** | Nhóm đỏ, kiểm tra thiên vị, đánh giá an toàn trước khi phát hành |
| **Triển khai dần dần** | Bắt đầu với quyền truy cập hạn chế; mở rộng khi sự an toàn được chứng minh |
| **Báo cáo sự cố** | Ghi lại và chia sẻ thông tin về những thất bại và tác hại |
| **Tiền thưởng lỗi** | Khen thưởng các nhà nghiên cứu bên ngoài vì đã tìm ra lỗ hổng |
| **Thẻ mẫu** | Khả năng, hạn chế của mô hình tài liệu và mục đích sử dụng |
---

## Xuất xứ dữ liệu
| Mối quan tâm | Mô tả |
|----------|-------------|
| **Minh bạch dữ liệu đào tạo** | Hầu hết các mô hình biên giới không tiết lộ dữ liệu đào tạo của họ |
| **Đồng ý** | Dữ liệu của các cá nhân có được sử dụng với sự hiểu biết và sự cho phép của họ không? |
| **Ngộ độc dữ liệu** | Kẻ tấn công có thể tiêm dữ liệu độc hại vào tập huấn luyện không? |
| **Thẻ tập dữ liệu** | Tài liệu về thành phần tập dữ liệu, phương pháp thu thập và các hạn chế |
| **Hình mờ** | Nhúng các điểm đánh dấu vô hình vào nội dung do AI tạo để xác định nội dung đó |
---

## Khung đạo đức thực tế
### Dành cho nhà phát triển AI
| Câu hỏi | Tại sao nó lại quan trọng |
|----------|--------------|
| **Ai có thể bị tổn hại bởi hệ thống này?** | Xác định các bên liên quan bị ảnh hưởng |
| **Điều gì xảy ra nếu mô hình sai?** | Đánh giá chi phí của sai sót |
| **Các quyết định của mô hình có thể được giải thích không?** | Xác định các yêu cầu về khả năng giải thích |
| ** Dữ liệu đào tạo có phải là đại diện không?** | Kiểm tra độ lệch lựa chọn và đo lường |
| **Các chế độ lỗi là gì?** | Dự đoán các trường hợp nguy hiểm và sử dụng sai |
| **Hệ thống sẽ được giám sát như thế nào?** | Kế hoạch giám sát liên tục |
###Dành cho các tổ chức triển khai AI
| Thực hành | Mô tả |
|----------|-------------|
| **Ban quản trị AI** | Nhóm đa chức năng xem xét việc triển khai AI |
| **Đánh giá tác động** | Đánh giá tác hại tiềm ẩn trước khi triển khai |
| **Quy trình giám sát con người** | Xóa đường dẫn báo cáo khi AI mắc lỗi |
| **Kiểm toán thường xuyên** | Kiểm tra các hậu quả thiên vị, trôi dạt và ngoài ý muốn |
| **Kênh phản hồi của người dùng** | Cho phép người bị ảnh hưởng báo cáo vấn đề |
| **Tài liệu** | Duy trì hồ sơ về các quyết định mẫu và lý do căn bản |
---

## Bản tóm tắt
Đạo đức và quản trị AI không phải là những điều cần cân nhắc - chúng là những yêu cầu kỹ thuật. Thành kiến, thiếu minh bạch, chi phí môi trường và vi phạm quyền riêng tư không chỉ là những lo ngại về đạo đức; chúng là những con bọ gây hại thực sự cho người thật. Bối cảnh quản trị đang phát triển nhanh chóng, với Đạo luật AI của EU thiết lập tiêu chuẩn toàn cầu. Nhưng chỉ quy định thôi thì chưa đủ. Mọi nhà phát triển AI cần suy nghĩ về sự công bằng, khả năng giải thích và trách nhiệm giải trình như một phần công việc hàng ngày của họ. Câu hỏi không phải là liệu AI có nên được quản lý hay không - mà là làm thế nào để xây dựng các hệ thống đáng tin cậy.