---
# Metadata
title: "Management and Project Methodologies"
description: "Leadership, Agile/Scrum/Kanban, OKRs, risk management"
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
tags: [management, project, methodologies, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Phương pháp quản lý và dự án
Quản lý con người và dự án là một trong những trách nhiệm đòi hỏi khắt khe nhất trong bất kỳ tổ chức nào. Kỹ năng kỹ thuật cung cấp cơ hội đầu vào, nhưng khả năng lãnh đạo nhóm, đưa ra quyết định, giao tiếp hiệu quả và đưa ra kết quả sẽ quyết định liệu mục tiêu có đạt được hay không. Tệp này bao gồm các khuôn khổ, phương pháp và kỹ năng thực tế mà các nhà quản lý và lãnh đạo dự án hiệu quả áp dụng.
---

## Phong cách lãnh đạo
Không có cách lãnh đạo "đúng" duy nhất. Phong cách tốt nhất phụ thuộc vào nhóm, nhiệm vụ và bối cảnh.
| Phong cách | Mô tả | Tốt Nhất Khi | Rủi ro |
|-------|-------------|----------|------|
| **Chuyên quyền** | Người lãnh đạo đưa ra quyết định với đầu vào tối thiểu | Khủng hoảng; đội thiếu kinh nghiệm; áp lực thời gian | Tinh thần thấp; phụ thuộc vào người lãnh đạo |
| **Dân chủ** | Người lãnh đạo thu hút ý kiến ​​đóng góp; đội có ảnh hưởng thực sự | Đội ngũ lành nghề; những quyết định phức tạp cần được đồng tình | Quyết định chậm hơn; có thể cảm thấy mơ màng |
| **Laissez-faire** | Người lãnh đạo đưa ra phương hướng; nhóm tự quản lý | Chuyên gia có tay nghề cao, năng động | Thiếu sự phối hợp; trách nhiệm giải trình không rõ ràng |
| **Biến đổi** | Lãnh đạo truyền cảm hứng cho tầm nhìn và phát triển cá nhân | Thay đổi sáng kiến; xây dựng văn hóa hiệu suất cao | Có thể kiệt sức nếu không có căn cứ thực thi |
| **Lãnh đạo phục vụ** | Lãnh đạo ưu tiên nhu cầu và sự phát triển của nhóm | Công nhân tri thức; xây dựng niềm tin và lòng trung thành | Có thể bị coi là yếu kém trong các nền văn hóa có thứ bậc |
| **Tình huống** | Người lãnh đạo điều chỉnh phong cách phù hợp với sự trưởng thành và nhiệm vụ của nhóm | Hầu hết các tình huống thực tế | Yêu cầu trí tuệ cảm xúc cao |
### Những nhà quản lý vĩ đại thực sự làm gì
Nghiên cứu (đặc biệt là từ Dự án Oxygen của Google) đã xác định những hành vi hàng đầu của những người quản lý hiệu quả:
1. **Là một huấn luyện viên giỏi** — đặt câu hỏi, giúp mọi người suy nghĩ chứ không chỉ đưa ra câu trả lời
2. **Trao quyền cho nhóm** — đại biểu một cách có ý nghĩa; không quản lý vi mô
3. **Tạo một môi trường hòa nhập** — an toàn về mặt tâm lý; mọi người đều có thể đóng góp
4. **Có năng suất và hướng đến kết quả** — giúp nhóm tập trung vào những vấn đề quan trọng
5. **Là người giao tiếp tốt** — lắng nghe, chia sẻ bối cảnh, đưa ra định hướng rõ ràng
6. **Hỗ trợ phát triển nghề nghiệp** — nói về sự phát triển, không chỉ về nhiệm vụ
7. **Có tầm nhìn và chiến lược rõ ràng** - biết nhóm sẽ đi đâu và tại sao
8. **Có các kỹ năng kỹ thuật quan trọng** — có thể tư vấn và hiểu công việc (ngay cả khi không làm việc đó)
---

## Phương pháp quản lý dự án
### Truyền thống (Thác nước)
| Giai đoạn | Hoạt động |
|-------|----------|
| **Yêu cầu** | Tập hợp và ghi lại những gì cần xây dựng |
| **Thiết kế** | Kiến trúc, thông số kỹ thuật, kế hoạch |
| **Triển khai** | Xây dựng điều |
| **Thử nghiệm** | Xác minh nó hoạt động như được chỉ định |
| **Triển khai** | Phát hành cho sản xuất/người dùng |
| **Bảo trì** | Khắc phục sự cố; hỗ trợ liên tục |
**Tốt nhất cho**: Các ngành xây dựng, sản xuất, được quản lý có yêu cầu cố định và chi phí thay đổi tốn kém.
### Nhanh nhẹn
Agile là một tư duy, không phải là một phương pháp. Nó xuất phát từ[Agile Manifesto](https://agilemanifesto.org/)(2001):
> *Các cá nhân và sự tương tác* qua các quy trình và công cụ
> *Phần mềm hoạt động* trên tài liệu toàn diện
> *Cộng tác với khách hàng* trong quá trình đàm phán hợp đồng
> *Phản ứng với sự thay đổi* về việc tuân theo kế hoạch
| Nguyên tắc linh hoạt | Ý nghĩa của nó trong thực tế |
|-------|--------------------------|
| Cung cấp phần mềm hoạt động thường xuyên | Lặp lại ngắn (1–4 tuần) |
| Chào mừng các yêu cầu thay đổi | Thậm chí còn muộn trong quá trình phát triển |
| Doanh nghiệp và nhà phát triển làm việc cùng nhau | Cộng tác hàng ngày, không chỉ lúc bắt đầu và kết thúc |
| Xây dựng dự án xung quanh những cá nhân có động lực | Cung cấp cho họ môi trường và sự tin tưởng mà họ cần |
| Trò chuyện trực tiếp | Cách truyền tải thông tin hiệu quả nhất |
| Phần mềm hoạt động được là thước đo chính của sự tiến bộ | Không phải tài liệu, không phải kế hoạch |
| Tốc độ bền vững | Vô thời hạn; không có cuộc tuần hành tử thần |
| Liên tục chú ý đến sự xuất sắc về mặt kỹ thuật | Thiết kế tốt và mã sạch |
| Đơn giản | Tối đa hóa công việc chưa hoàn thành |
| Đội tự tổ chức | Những kiến ​​trúc và thiết kế tốt nhất xuất hiện từ chúng |
| Phản ánh và điều chỉnh thường xuyên | Hồi tưởng; cải tiến liên tục |
### Scrum
Scrum là khung Agile được sử dụng rộng rãi nhất.
| Yếu tố | Mô tả |
|----------|-------------|
| **Chạy nước rút** | Lặp lại có độ dài cố định (thường là 2 tuần) |
| **Chủ sở hữu sản phẩm** | Xác định và ưu tiên các hồ sơ tồn đọng; đại diện cho các bên liên quan |
| **ScrumMaster** | Tạo điều kiện thuận lợi cho quá trình; loại bỏ những trở ngại; bảo vệ đồng đội |
| **Nhóm phát triển** | Đa chức năng, tự tổ chức (lý tưởng là 5–9 người) |
| **Tồn đọng sản phẩm** | Danh sách ưu tiên mọi thứ có thể cần thiết |
| **Sprint tồn đọng** | Các mục được chọn cho lần chạy nước rút hiện tại + kế hoạch phân phối chúng |
| **Dự phòng hàng ngày** | Đồng bộ hóa 15 phút: Tôi đã làm gì? Tôi sẽ làm gì? Có bất kỳ trình chặn nào không? |
| **Đánh giá Sprint** | Demo phần mềm làm việc cho các bên liên quan; thu thập phản hồi |
| **Hồi tưởng nước rút** | Nhóm phản ánh về cách cải thiện quy trình |
### Kanban
Kanban là một phương pháp dựa trên dòng chảy tập trung vào việc trực quan hóa công việc và hạn chế công việc đang tiến hành.
| Thực hành | Mô tả |
|----------|-------------|
| **Trực quan hóa quy trình làm việc** | Bảng có các cột (Việc cần làm → Đang tiến hành → Đánh giá → Hoàn thành) |
| **Giới hạn WIP** | Đặt số lượng mục tối đa trong mỗi cột |
| **Quản lý luồng** | Đo thời gian chu kỳ; xác định và loại bỏ các nút thắt |
| **Đưa ra chính sách rõ ràng** | Mọi người đều đồng ý về ý nghĩa của "Xong" đối với mỗi cột |
| **Cải thiện hợp tác** | Sử dụng dữ liệu và phản hồi để phát triển quy trình |
**Scrum so với Kanban**:
| | Scrum | Kanban |
|---|-------|--------|
| **Nhịp** | Chạy nước rút cố định (2 tuần) | Dòng chảy liên tục |
| **Vai trò** | PO, Scrum Master, Nhóm | Không có vai trò quy định |
| **Thay đổi** | Không có thay đổi giữa nước rút | Thay đổi bất cứ lúc nào |
| **Số liệu** | Vận tốc (điểm câu chuyện trên mỗi lần chạy nước rút) | Thời gian chu kỳ, thông lượng |
| **Tốt nhất cho** | Phát triển sản phẩm với các bản phát hành thường xuyên | Các nhóm hỗ trợ; giao hàng liên tục |
---

## OKR và KPI
### OKRs (Mục tiêu và Kết quả then chốt)
OKR là khung thiết lập mục tiêu được Google, Intel, Spotify và nhiều công ty khác sử dụng.
| Thành phần | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Mục tiêu** | Chất lượng, đầy tham vọng, truyền cảm hứng | "Trở thành nền tảng phù hợp cho kế toán doanh nghiệp nhỏ" |
| **Kết quả chính 1** | Có thể đo lường được; chứng tỏ mục tiêu đang được đáp ứng | Tăng số người dùng hoạt động hàng tháng từ 10K lên 50K |
| **Kết quả chính 2** | Có thể đo lường được | Đạt điểm NPS từ 60+ |
| **Kết quả chính 3** | Có thể đo lường được | Giảm thời gian làm quen từ 30 phút xuống còn 5 phút |
**Các phương pháp hay nhất về OKR**:
- Đặt 3–5 mục tiêu mỗi quý
- Mỗi mục tiêu có 2–5 kết quả chính
- Đặt mục tiêu đạt được 70% (100% có nghĩa là mục tiêu quá dễ dàng)
- OKR tách biệt với đánh giá hiệu suất
- Minh bạch: mọi người đều có thể xem OKR của người khác
### KPI (Chỉ số hiệu suất chính)
| Danh mục | Ví dụ về KPI |
|----------|-------------|
| **Tài chính** | Doanh thu, tỷ suất lợi nhuận gộp, lợi nhuận ròng, EBITDA |
| **Khách hàng** | NPS, CSAT, tỷ lệ rời bỏ, CLV |
| **Sản phẩm** | DAU/MAU, áp dụng tính năng, thời gian định giá |
| **Kỹ thuật** | Tần suất triển khai, thời gian thực hiện, MTTR, tỷ lệ thất bại khi thay đổi |
| **Tiếp thị** | CAC, ROAS, tỷ lệ chuyển đổi, lưu lượng truy cập không phải trả tiền |
| **Mọi người** | NPS của nhân viên, tỷ lệ giữ chân, thời gian tuyển dụng |
---

## Quản lý các bên liên quan
| Loại bên liên quan | Họ quan tâm đến điều gì | Cách tham gia |
|-----------------|--------------------------|---------------|
| **Nhà tài trợ điều hành** | ROI, liên kết chiến lược, rủi ro | Cập nhật hàng tháng; tập trung vào kết quả |
| **Người dùng cuối** | Dễ sử dụng, độ tin cậy, giải quyết vấn đề của họ | Nghiên cứu người dùng; chương trình beta; kênh hỗ trợ |
| **Đội kỹ thuật** | Chất lượng mã, kiến ​​trúc, nợ kỹ thuật | Đánh giá kiến ​​trúc; các cuộc đàm phán về công nghệ; tham gia vào các quyết định |
| **Khách hàng bên ngoài** | Thời gian giao hàng, chất lượng, giá trị | Demo thường xuyên; giao tiếp rõ ràng; SLA |
| **Cơ quan quản lý / Tuân thủ** | Yêu cầu pháp lý, quy trình kiểm toán | Tài liệu; tham gia chủ động |
### Lưới quyền lực/lợi ích
| | Lãi suất thấp | Lãi Cao |
|---|-----------------|---------------|
| **Công suất cao** | Giữ hài lòng | Quản lý chặt chẽ (người chơi chủ chốt) |
| **Công suất thấp** | Màn hình (nỗ lực tối thiểu) | Cập nhật thông tin |
---

## Khung giao tiếp
| Khung | Cấu trúc | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **CHUẨN BỊ** | Điểm → Lý do → Ví dụ → Điểm | Giao tiếp thuyết phục; cuộc họp |
| **SAO** | Tình huống → Nhiệm vụ → Hành động → Kết quả | Phỏng vấn; đánh giá hiệu suất |
| **BLUF** | Dòng dưới lên Mặt trận | Email cho giám đốc điều hành; cập nhật trạng thái |
| **BAR** | Tình huống → Bối cảnh → Đánh giá → Khuyến nghị | Bàn giao; truyền thông sự cố |
| **7 chữ C** | Rõ ràng, ngắn gọn, cụ thể, chính xác, mạch lạc, đầy đủ, lịch sự | Giao tiếp bằng văn bản chung |
### Đưa ra phản hồi
| Tiếp cận | Mô tả |
|----------|-------------|
| **SBI** (Tình huống-Hành vi-Tác động) | "Trong cuộc họp (tình huống) ngày hôm qua, bạn đã làm gián đoạn (hành vi) của khách hàng, khiến họ ngừng hoạt động (tác động)." |
| **Tiếp tục** | Tập trung vào hành vi trong tương lai, không phải những sai lầm trong quá khứ. "Lần sau hãy thử..." |
| **Thành thực cấp tiến** (Kim Scott) | Quan tâm cá nhân + thách thức trực tiếp. Không quá tử tế (sự đồng cảm tàn hại) và không quá khắc nghiệt (sự hung hăng đáng ghét). |
---

## Mô hình ra quyết định
| Người mẫu | Mô tả | Tốt nhất cho |
|-------|-------------|----------|
| **NHANH CHÓNG** | Đề xuất, Đồng ý, Thực hiện, Đầu vào, Quyết định - làm rõ ai làm gì | Quyết định phức tạp với nhiều bên liên quan |
| **RACI** | Có trách nhiệm, Có trách nhiệm, Được tư vấn, Được cung cấp thông tin - vai trò rõ ràng | Nhiệm vụ và sản phẩm của dự án |
| **Ma trận Eisenhower** | Lưới khẩn cấp/quan trọng — ưu tiên các nhiệm vụ | Năng suất cá nhân; phân loại nhiệm vụ |
| **Ma trận quyết định** | Tùy chọn điểm theo tiêu chí có trọng số | Lựa chọn giữa các lựa chọn thay thế |
| **Vòng lặp OODA** | Quan sát → Định hướng → Quyết định → Hành động — chu kỳ quyết định nhanh chóng | Tình huống cạnh tranh; ứng phó sự cố |
| **Sáu chiếc mũ tư duy** | Nhìn nhận một quyết định từ 6 góc độ (sự thật, cảm xúc, rủi ro, lợi ích, tính sáng tạo, quy trình) | Quyết định của nhóm; tránh tư duy tập thể |
### Ma trận Eisenhower
| | Khẩn cấp | Không khẩn cấp |
|---|--------|-------------|
| **Quan trọng** | **Làm trước** — khủng hoảng, thời hạn, vấn đề quan trọng | **Lịch trình** — lập kế hoạch chiến lược, xây dựng mối quan hệ, học tập |
| **Không quan trọng** | **Đại biểu** — một số email, cuộc họp, sự gián đoạn | **Loại bỏ** — lãng phí thời gian, công việc bận rộn, duyệt web quá nhiều |
---

##Quản lý rủi ro
| Bước | Mô tả |
|------|-------------|
| **1. Xác định rủi ro** | Nghĩ xem điều gì có thể xảy ra sai sót (kỹ thuật, tiến độ, nguồn lực, bên ngoài) |
| **2. Đánh giá xác suất và tác động** | Đánh giá từng rủi ro: Cao/Trung bình/Thấp cho cả hai |
| **3. Ưu tiên** | Tập trung vào các rủi ro có xác suất cao, tác động lớn |
| **4. Lập kế hoạch phản hồi** | Tránh, giảm thiểu, chuyển giao hoặc chấp nhận từng rủi ro |
| **5. Giám sát** | Đánh giá thường xuyên; rủi ro thay đổi khi dự án phát triển |
### Chiến lược ứng phó rủi ro
| Chiến lược | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Tránh** | Thay đổi kế hoạch để loại bỏ rủi ro | Sử dụng công nghệ đã được chứng minh thay vì thử nghiệm |
| **Giảm thiểu** | Giảm xác suất hoặc tác động | Thêm thời gian đệm; thuê thêm nhân viên |
| **Chuyển** | Chuyển rủi ro sang bên thứ ba | Bảo hiểm; gia công phần mềm; hợp đồng giá cố định |
| **Chấp nhận** | Thừa nhận và lập kế hoạch nếu điều đó xảy ra | Quỹ dự phòng; kế hoạch dự phòng |
---

## Quản lý nhóm từ xa
| Thử thách | Giải pháp |
|----------||----------|
| **Khoảng cách trong giao tiếp** | Mặc định là viết; bối cảnh giao tiếp quá mức; sử dụng các công cụ không đồng bộ đầu tiên |
| **Cách ly** | Thông thường 1:1; sự kiện xã hội ảo; gặp mặt trực tiếp thường xuyên |
| **Múi giờ** | Luân phiên họp; ghi lại các quyết định; giảm thiểu sự phụ thuộc đồng bộ |
| **Tầm nhìn** | Các kênh công khai qua DM; cập nhật trạng thái bằng văn bản; bảng điều khiển được chia sẻ |
| **Tin tưởng** | Đo lường kết quả, không phải số giờ; tránh phần mềm giám sát |
| **Giới thiệu** | Hệ thống bạn bè có cấu trúc; các quy trình được ghi lại bằng văn bản; mục tiêu rõ ràng trong tuần đầu tiên |
###Cuộc họp hiệu quả
| Loại cuộc họp | Thời lượng | Tần số | Mục đích |
|-------------|----------|-------------|--------|
| **Dự phòng hàng ngày** | 15 phút | Hàng ngày | Đồng bộ hóa; chất chặn bề mặt |
| **Lập kế hoạch chạy nước rút** | 1–2 giờ | Mỗi lần chạy nước rút | Căn chỉnh những gì cần xây dựng tiếp theo |
| **Đánh giá nước rút** | 1 giờ | Mỗi lần chạy nước rút | Thử nghiệm; thu thập phản hồi |
| **Hồi tưởng** | 45–60 phút | Mỗi lần chạy nước rút | Cải tiến quy trình |
| **1:1** | 30 phút | Hàng tuần/hai tuần | Hỗ trợ và phát triển cá nhân |
| ** Chung tay** | 30–60 phút | Hàng tháng | Cập nhật về công ty/nhóm; Hỏi Đáp |
**Quy tắc cuộc họp**: Mọi cuộc họp đều cần có chương trình nghị sự. Bắt đầu đúng giờ. Kết thúc đúng giờ. Chỉ định các mục hành động với chủ sở hữu. Nếu nó có thể là một email, hãy biến nó thành một email.
---

## Cơ cấu tổ chức
| Cấu trúc | Mô tả | Ưu điểm | Nhược điểm |
|----------|-------------|------|------|
| **Chức năng** | Được tổ chức theo chuyên ngành (kỹ thuật, tiếp thị, bán hàng) | Chuyên môn sâu; con đường sự nghiệp rõ ràng | Silo; công việc đa chức năng chậm |
| **Chia rẽ** | Được tổ chức theo sản phẩm, thị trường hoặc địa lý | Tập trung; trách nhiệm giải trình | Tài nguyên trùng lặp; thực hành không nhất quán |
| **Ma trận** | Mọi người báo cáo cho cả người quản lý chức năng và dự án | Tính linh hoạt; chia sẻ tài nguyên | Các ưu tiên xung đột; nhầm lẫn về người chịu trách nhiệm |
| **Phẳng / Toàn diện** | Phân cấp tối thiểu; đội tự tổ chức | Tốc độ; quyền tự chủ; đổi mới | Quyết định không rõ ràng; không có quy mô tốt |
| **Cấu trúc liên kết nhóm** (Skelton/Pais) | Các nhóm được liên kết theo luồng + các nhóm nền tảng + các nhóm hỗ trợ + các nhóm hệ thống con phức tạp | Phù hợp với cách thức công việc thực sự diễn ra | Yêu cầu thiết kế chu đáo; không phải viên đạn bạc |
---

## Khái niệm cơ bản về quản lý sản phẩm
Quản lý sản phẩm là nguyên tắc quyết định xây dựng cái gì, cho ai và tại sao - đồng thời đảm bảo nó mang lại giá trị.
| Trách nhiệm | Mô tả |
|---------------|-------------|
| **Khám phá** | Nghiên cứu người dùng, phân tích thị trường, thông tin cạnh tranh |
| **Chiến lược** | Tầm nhìn sản phẩm, lộ trình, khung ưu tiên |
| **Thực thi** | Viết thông số kỹ thuật/câu chuyện của người dùng; làm việc với kỹ thuật và thiết kế |
| **Ra mắt** | Lập kế hoạch tiếp cận thị trường; định vị; hỗ trợ bán hàng |
| **Lặp lại** | Phân tích số liệu; thu thập phản hồi; ưu tiên những cải tiến tiếp theo |
### Khung ưu tiên
| Khung | Nó hoạt động như thế nào |
|----------||-------------|
| **MoSCoW** | Phải có/Nên có/Có thể có/Sẽ không có |
| **GẠO** | Phạm vi tiếp cận × Tác động × Sự tự tin → Nỗ lực |
| **Mô hình Kano** | Phân loại các tính năng là cơ bản, hiệu suất hoặc thú vị |
| **Ma trận giá trị và nỗ lực** | Vẽ đồ thị trên lưới 2×2; ưu tiên các hạng mục có giá trị cao, tốn ít công sức |
| **Chấm điểm cơ hội** | Tầm quan trọng trừ đi sự hài lòng; tìm những nhu cầu chưa được đáp ứng |
---

## Bản tóm tắt
Quản lý là thực hành đạt được mục tiêu thông qua người khác. Người quản lý hiệu quả kết hợp tư duy rõ ràng (khuôn khổ, phương pháp, số liệu) với kỹ năng giao tiếp cá nhân (lắng nghe, đồng cảm, tin tưởng). Không có phương pháp luận nào có thể thay thế được khả năng phán đoán tốt, nhưng khả năng phán đoán tốt được nâng cao nhờ các khuôn khổ hợp lý. Những điều này nên được áp dụng như những hướng dẫn thực tế hơn là những học thuyết cứng nhắc.