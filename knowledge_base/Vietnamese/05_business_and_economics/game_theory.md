<!--
---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Lý thuyết trò chơi và tư duy chiến lược
Lý thuyết trò chơi là nghiên cứu toán học về các tương tác chiến lược - những tình huống mà kết quả của bạn không chỉ phụ thuộc vào những gì bạn làm mà còn phụ thuộc vào những gì người khác làm. Nó áp dụng ở mọi nơi: cạnh tranh kinh doanh, quan hệ quốc tế, đấu giá, đàm phán, sinh học tiến hóa và các quyết định hàng ngày như chọn tuyến đường khi tham gia giao thông. Cái nhìn sâu sắc cốt lõi là các tác nhân hợp lý trong các tình huống chiến lược không chỉ tối ưu hóa chiến lược của riêng họ - họ dự đoán những gì người khác sẽ làm và những người khác cũng đang làm như vậy.
---

## Khái niệm cơ bản
### Thuật ngữ chính
| Kỳ hạn | Định nghĩa |
|------|-------------|
| **Trò chơi** | Bất kỳ tình huống nào có hai hoặc nhiều người ra quyết định (người chơi) mà các lựa chọn của họ ảnh hưởng đến kết quả của nhau |
| **Người chơi** | Người ra quyết định trong trò chơi |
| **Chiến lược** | Một kế hoạch hành động hoàn chỉnh cho mọi tình huống có thể phát sinh |
| **Tiền hoàn trả** | Kết quả mà người chơi nhận được từ sự kết hợp chiến lược cụ thể |
| **Cân bằng Nash** | Một tập hợp các chiến lược mà không người chơi nào có thể cải thiện lợi ích của mình bằng cách đơn phương thay đổi chiến lược của họ |
| **Chiến lược chiếm ưu thế** | Một chiến lược tốt nhất bất kể người chơi khác làm gì |
| **Trò chơi có tổng bằng 0** | Lợi ích của người chơi này chính xác là sự mất mát của người chơi khác |
| **Trò chơi có tổng khác 0** | Người chơi có thể được tất cả hoặc thua tất cả |
| **Trò chơi hợp tác** | Người chơi có thể hình thành các thỏa thuận ràng buộc |
| **Trò chơi không hợp tác** | Không có thỏa thuận ràng buộc; mỗi người chơi hành động vì lợi ích cá nhân |
---

## Trò chơi cổ điển
### Thế lưỡng nan của tù nhân
Hai nghi phạm bị bắt giữ. Mỗi người có thể hợp tác (im lặng) hoặc phản bội (thú nhận).
| | B hợp tác | B Khiếm Khuyết |
|---|-------------|----------|
| **A hợp tác** | A: 1 năm, B: 1 năm | A: 10 năm, B: miễn phí |
| **Một khiếm khuyết** | A: miễn phí, B: 10 năm | A: 5 năm, B: 5 năm |
| Cái nhìn sâu sắc | Mô tả |
|----------|-------------|
| **Chiến lược chiếm ưu thế** | Khiếm khuyết chiếm ưu thế đối với cả hai người chơi |
| **Cân bằng Nash** | Cả hai khiếm khuyết (mỗi lỗi 5 năm) |
| **Tối ưu Pareto** | Cả hai hợp tác (mỗi người 1 năm) |
| **Bài học** | Những quyết định hợp lý của cá nhân có thể dẫn đến những kết quả chung tồi tệ hơn |
### Các trò chơi cổ điển khác
| Trò chơi | Mô tả | Cân bằng Nash | Bài học |
|------|-------------|--------|--------|
| **Gà (Hawk-Dove)** | Hai người lái xe hướng về nhau; đổi hướng hoặc đi thẳng | Một người rẽ, một người đi thẳng | Kỹ năng bên bờ vực; độ tin cậy của cam kết |
| **Săn hươu** | Cùng nhau săn hươu (chi trả cao) hoặc săn thỏ một mình (chi trả thấp) | Cả hai con hươu hoặc cả hai con thỏ | Phối hợp; tin tưởng |
| **Trận chiến giới tính** | Hai người chơi thích kết quả khác nhau nhưng muốn phối hợp | Cả hai cùng đi dự sự kiện | Nhiều điểm cân bằng; ai đi trước có lợi thế |
| **Trò chơi tối hậu** | Người đề nghị chia tiền; người trả lời chấp nhận hoặc từ chối (cả hai đều không nhận được gì) | Người đề xuất đưa ra mức tối thiểu; người trả lời chấp nhận | Mọi người từ chối những lời đề nghị không công bằng (phi lý nhưng phổ biến) |
| **Trò chơi hàng hóa công cộng** | Đóng góp vào một nhóm chung hoặc đi xe miễn phí | Mọi người đi xe miễn phí | Bi kịch của cộng đồng; cần thực thi |
---

## Thể loại trò chơi
### Theo thời gian
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Đồng thời** | Người chơi di chuyển cùng lúc (hoặc không biết nước đi của người khác) | Kéo-búa-bao; đấu giá kín |
| **Tuần tự** | Người chơi lần lượt di chuyển; người chơi sau quan sát nước đi trước | Cờ vua; quyết định gia nhập thị trường |
| **Lặp lại** | Cùng một trò chơi được chơi nhiều lần | Tình thế tiến thoái lưỡng nan của tù nhân lặp đi lặp lại; cạnh tranh kinh doanh đang diễn ra |
###Theo thông tin
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Thông tin hoàn hảo** | Tất cả người chơi đều biết tất cả các nước đi trước đó | Cờ vua; cờ đam |
| **Thông tin không hoàn hảo** | Một số chiêu thức bị ẩn | Bài xì phé; cạnh tranh kinh doanh |
| **Thông tin đầy đủ** | Tất cả người chơi đều biết tất cả phần thưởng và chiến lược | Hầu hết các trò chơi sách giáo khoa |
| **Thông tin không đầy đủ** | Một số khoản hoàn trả hoặc loại không xác định | Đấu giá; đàm phán |
---

## Khái niệm giải pháp
### Cân bằng Nash
| Khía cạnh | Mô tả |
|--------|-------------|
| **Định nghĩa** | Không người chơi nào có thể cải thiện thành quả của mình chỉ bằng cách thay đổi chiến lược của mình |
| **Cách tìm** | Đối với mỗi người chơi, hãy tìm câu trả lời tốt nhất cho chiến lược của người khác; nơi chúng giao nhau là điểm cân bằng Nash |
| **Sự tồn tại** | Mọi trò chơi hữu hạn đều có ít nhất một điểm cân bằng Nash (có thể trong các chiến lược hỗn hợp) |
| **Tính độc đáo** | Trò chơi có thể có nhiều điểm cân bằng Nash; vấn đề phối hợp phát sinh |
| **Giới hạn** | Cân bằng Nash không cho bạn biết cân bằng nào sẽ được chọn; không tính đến sự công bằng |
### Cân bằng chiến lược chiếm ưu thế
| Bước | Mô tả |
|------|-------------|
| **1. Xác định chiến lược** | Liệt kê tất cả các chiến lược có sẵn cho mỗi người chơi |
| **2. Tìm chiến lược chiếm ưu thế** | Một chiến lược tốt nhất bất kể người khác làm gì |
| **3. Nếu tất cả người chơi đều có** | Sự kết hợp là sự cân bằng chiến lược chiếm ưu thế |
| **4. Nếu không** | Sử dụng phương pháp loại bỏ lặp đi lặp lại các chiến lược bị chi phối hoặc trạng thái cân bằng Nash |
### Cảm ứng ngược (Trò chơi tuần tự)
| Bước | Mô tả |
|------|-------------|
| **1. Vẽ cây trò chơi** | Nút = điểm quyết định; nhánh = hành động |
| **2. Bắt đầu ở cuối** | Xác định lựa chọn tối ưu của người chơi cuối cùng tại mỗi nút cuối |
| **3. Làm việc ngược** | Tại mỗi nút trước đó, hãy chọn hành động dẫn đến kết quả tốt nhất |
| **4. Kết quả** | Trò chơi con cân bằng hoàn hảo — chiến lược tối ưu ở mọi thời điểm quyết định |
---

## Khái niệm nâng cao
### Chiến lược hỗn hợp
| Khái niệm | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Chiến lược hỗn hợp** | Ngẫu nhiên hóa giữa các hành động theo xác suất | Trò chơi oẳn tù tì: chơi mỗi trò có xác suất 1/3 |
| **Tại sao chọn ngẫu nhiên?** | Ngăn chặn đối thủ dự đoán nước đi của bạn | Đá phạt đền trong bóng đá; kiểm toán thuế |
| **Chiến lược hỗn hợp Cân bằng Nash** | Mỗi người chơi đều thờ ơ với các chiến lược thuần túy của mình | Không người chơi nào có thể khai thác người kia |
### Trò chơi lặp đi lặp lại và Định lý dân gian
| Khái niệm | Mô tả |
|----------|-------------|
| **Lặp lại vô hạn** | Cảm ứng lùi làm sáng tỏ sự hợp tác; giống như trò chơi một lần | Cuộc đào tẩu ở vòng cuối lan truyền ngược |
| **Lặp lại vô hạn** | Hợp tác có thể được duy trì thông qua các mối đe dọa trừng phạt trong tương lai | Ăn miếng trả miếng; chiến lược kích hoạt nghiệt ngã |
| **Định lý dân gian** | Bất kỳ khoản hoàn trả hợp lý riêng lẻ nào cũng có thể là trạng thái cân bằng Nash trong một trò chơi lặp lại vô hạn | Có thể hợp tác nếu tương lai đủ quan trọng |
| **Hệ số chiết khấu** | Người chơi đánh giá cao mức độ hoàn trả trong tương lai; cao hơn = hợp tác nhiều hơn | Người chơi kiên nhẫn hợp tác nhiều hơn |
### Thiết kế cơ chế (Lý thuyết trò chơi đảo ngược)
| Khái niệm | Mô tả |
|----------|-------------|
| **Mục tiêu** | Thiết kế luật chơi để đạt được kết quả mong muốn |
| **Ứng dụng** | Đấu giá; hệ thống bỏ phiếu; thiết kế hợp đồng; thiết kế chợ |
| **Nguyên tắc mặc khải** | Bất kỳ kết quả nào có thể đạt được bằng bất kỳ cơ chế nào đều có thể đạt được bằng cơ chế trực tiếp trung thực |
| **Ví dụ** | Đấu giá Vickrey (giá thầu kín ở mức giá thứ hai) - đặt giá thầu giá trị thực của bạn là một chiến lược vượt trội |
---

## Ứng dụng
### Việc kinh doanh
| Ứng dụng | Khái niệm lý thuyết trò chơi | Cái nhìn sâu sắc |
|-------------|-------------------|----------|
| **Cạnh tranh về giá** | Thế tiến thoái lưỡng nan của tù nhân | Cuộc chiến về giá làm tổn thương cả hai công ty; thông đồng ngầm trong trò chơi lặp đi lặp lại |
| **Gia nhập thị trường** | Trò chơi tuần tự; cam kết | Lời đe dọa chống gia nhập của những người đương nhiệm chỉ đáng tin cậy nếu họ đã đầu tư vào năng lực |
| **Đấu giá** | Thiết kế cơ chế | Đấu giá theo giá thứ hai gợi ra những giá trị đích thực; đấu giá phổ tăng hàng tỷ đô la |
| **Đàm phán** | Trò chơi thương lượng; Cân bằng Nash | Chia phần thặng dư; lợi thế dẫn đầu trong trò chơi tối hậu thư |
| **Báo hiệu** | Mô hình giáo dục của Spence | Tín hiệu đắt tiền là đáng tin cậy vì loại chất lượng thấp không thể mua được |
###Quan hệ quốc tế
| Ứng dụng | Khái niệm lý thuyết trò chơi | Cái nhìn sâu sắc |
|-------------|-------------------|----------|
| **Chạy đua vũ trang** | Thế tiến thoái lưỡng nan của tù nhân | Sẽ tốt hơn nếu cả hai bên giải trừ vũ khí nhưng không thể tin tưởng lẫn nhau |
| **Chiến tranh thương mại** | Trò chơi lặp đi lặp lại | Ăn miếng trả miếng: hợp tác đến khi nào có khuyết điểm thì trả đũa |
| **Thỏa thuận về khí hậu** | Trò chơi hàng công | Đi xe miễn phí là hợp lý; cơ chế thực thi cần thiết |
| **Răn đe** | Thịt gà; cam kết đáng tin cậy | Sự hủy diệt được đảm bảo lẫn nhau là trạng thái cân bằng Nash |
---

## Bản tóm tắt
Lý thuyết trò chơi nghiên cứu các tương tác chiến lược trong đó kết quả của bạn phụ thuộc vào hành động của người khác. Cân bằng Nash - nơi không người chơi nào được hưởng lợi từ việc thay đổi chiến lược một mình - là khái niệm giải pháp trung tâm. Những trò chơi cổ điển như thế tiến thoái lưỡng nan của tù nhân cho thấy những quyết định hợp lý của cá nhân có thể tạo ra những kết quả tồi tệ về mặt tập thể. Trò chơi tuần tự được giải bằng quy nạp ngược. Trò chơi lặp đi lặp lại có thể duy trì sự hợp tác thông qua mối đe dọa trừng phạt trong tương lai. Các chiến lược hỗn hợp liên quan đến sự ngẫu nhiên để không thể đoán trước được. Thiết kế cơ chế đảo ngược câu hỏi: thay vì dự đoán kết quả, nó thiết kế các quy tắc để đạt được kết quả mong muốn (như trong đấu giá). Các ứng dụng bao gồm kinh doanh (định giá, gia nhập, đấu giá), chính trị (bỏ phiếu, hiệp ước), sinh học (chiến lược ổn định tiến hóa) và cuộc sống hàng ngày. Bài học cơ bản là chiến lược không chỉ liên quan đến những gì bạn làm - mà còn là việc dự đoán những gì người khác sẽ làm, biết rằng họ cũng đang làm như vậy.