---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [artificial, intelligence, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#trí tuệ nhân tạo
Trí tuệ nhân tạo là nỗ lực chế tạo những cỗ máy có thể làm những việc đòi hỏi trí thông minh nếu con người làm: nhận diện khuôn mặt, hiểu lời nói, đưa ra quyết định, viết văn bản, chơi trò chơi, lái ô tô, chẩn đoán bệnh. Lĩnh vực này cũng lâu đời như chính máy tính vậy - Alan Turing đã hỏi "Máy móc có thể suy nghĩ được không?" vào năm 1950 - nhưng sự bùng nổ về năng lực gần đây (những năm 2020) đã khiến AI trở thành một trong những công nghệ quan trọng và gây tranh cãi nhất trong lịch sử loài người.
---

## Tóm tắt lịch sử
AI đã trải qua những chu kỳ cường điệu và thất vọng trong nhiều thập kỷ. Hiểu lịch sử này giúp bạn hiểu tại sao mọi người vừa hào hứng vừa hoài nghi.
| Thời đại | Chuyện gì đã xảy ra | Kết quả |
|------|---------------|----------|
| **Thập niên 1950-1960** | Sự lạc quan sớm. Thử nghiệm Turing được đề xuất (1950). Hội nghị Dartmouth đồng xu "Trí tuệ nhân tạo" (1956). Các chương trình ban đầu như ELIZA (chatbot) và SHRDLU (hiểu ngôn ngữ). | Sự phấn khích: "Chúng ta sẽ có AGI trong một thế hệ!" |
| **Thập niên 1970** | Mùa đông AI đầu tiên. Những hạn chế của phương pháp tiếp cận sớm trở nên rõ ràng. Nguồn tài trợ cạn kiệt. | Thất vọng: lời hứa không được đáp ứng |
| **Thập niên 1980** | Sự bùng nổ của hệ thống chuyên gia - các chương trình dựa trên quy tắc mã hóa kiến ​​thức chuyên môn của con người. Dự án Thế hệ thứ năm của Nhật Bản. | Sự phấn khích trở lại: đầu tư AI của công ty |
| **1987-1993** | Mùa đông AI thứ hai. Hệ thống chuyên gia tỏ ra dễ vỡ và tốn kém để duy trì. | Lại thất vọng |
| **Những năm 2000** | Học máy đạt được lực kéo. Nhiều dữ liệu có sẵn (internet). Phương pháp thống kê thay thế các quy tắc được mã hóa bằng tay. | Tiến bộ ổn định |
| **2012+** | Cuộc cách mạng học tập sâu. AlexNet giành chiến thắng trong cuộc thi ImageNet sử dụng GPU. Mạng lưới thần kinh bắt đầu hoạt động tốt hơn các phương pháp truyền thống về thị giác, lời nói và ngôn ngữ. | Chuyển đổi nhanh chóng |
| **2017** | Bài viết "Chú ý là tất cả những gì bạn cần" giới thiệu kiến ​​trúc Transformer. | Nền tảng cho mọi thứ tiếp theo |
| **2020-2026** | Các mô hình ngôn ngữ lớn (GPT-3, GPT-4, Claude, Gemini, LLaMA). AI tạo ra văn bản, mã, hình ảnh, video. Việc áp dụng doanh nghiệp tăng tốc. | AI trở thành một phần của cuộc sống hàng ngày |
---

## AI hiện đại hoạt động như thế nào
### Học máy - Học từ dữ liệu
Thay vì lập trình các quy tắc rõ ràng, máy học sẽ cung cấp dữ liệu cho các thuật toán tự tìm ra mẫu.
| Loại | Nó hoạt động như thế nào | Ví dụ |
|------|-------------|----------|
| **Học tập có giám sát** | Đào tạo về các ví dụ được gắn nhãn (đầu vào → đầu ra đúng) | Phát hiện thư rác: cung cấp cho nó hàng nghìn email được gắn nhãn "thư rác" hoặc "không phải thư rác" |
| **Học không giám sát** | Tìm các mẫu trong dữ liệu chưa được gắn nhãn | Phân khúc khách hàng: nhóm những khách hàng giống nhau mà không xác định trước các nhóm |
| **Học tăng cường** | Đại lý học bằng cách thử và sai, nhận phần thưởng hoặc hình phạt | AI chơi trò chơi: thử di chuyển, nhận điểm khi chiến thắng, tìm hiểu chiến lược nào hiệu quả |
### Học sâu - Mạng thần kinh
Học sâu sử dụng mạng lưới thần kinh nhân tạo - các lớp phép toán đơn giản, xếp chồng lên nhau, có thể học các mẫu cực kỳ phức tạp. "Sâu" đề cập đến số lượng lớp.
Các kiến ​​trúc chính:
| Kiến trúc | Tốt nhất tại | Sử dụng trong thế giới thực |
|-------------|----------|-------|
| **CNN** (Mạng thần kinh chuyển đổi) | Dữ liệu hình ảnh và không gian | Nhận dạng khuôn mặt, hình ảnh y tế, xe tự lái |
| **RNN/LSTM** | Dữ liệu tuần tự (chuỗi thời gian) | Nhận dạng giọng nói, tạo nhạc (phần lớn được thay thế bởi Transformers) |
| **Máy biến áp** | Mọi thứ — văn bản, hình ảnh, âm thanh, mã | GPT, Claude, Gemini, BERT, DALL-E — kiến ​​trúc thống trị |
| **GAN** (Mạng đối thủ sáng tạo) | Tạo dữ liệu thực tế | Tổng hợp hình ảnh, chuyển kiểu (thay thế một phần bằng mô hình khuếch tán) |
| **Mô hình khuếch tán** | Tạo hình ảnh/video chất lượng cao | Khuếch tán ổn định, DALL-E 3, Midjourney, Sora |
### Mô hình ngôn ngữ lớn (LLM)
LLM là các mô hình dựa trên Transformer được đào tạo trên số lượng lớn văn bản. Họ học cách dự đoán mã thông báo tiếp theo (đoạn từ) trong một chuỗi, điều này đòi hỏi phải hiểu ngữ pháp, sự kiện, lý luận và thậm chí cả thứ gì đó giống như "kiến thức".
| Người mẫu | Nhà phát triển | Tính năng đáng chú ý |
|-------|-------------|--------|
| **GPT-4 / GPT-4o** | OpenAI | Đa phương thức (văn bản + hình ảnh); lý luận mạnh mẽ |
| **Claude** | Nhân chủng học | Tập trung vào sự an toàn và hữu ích; cửa sổ ngữ cảnh dài |
| **Song Tử** | Google DeepMind | Vốn đa phương thức; tích hợp với các dịch vụ của Google |
| **LLaMA / Llama 3** | Meta | Trọng lượng mở; có thể được chạy cục bộ; cộng đồng lớn |
| **Mistral** | AI của Mistral | Các mô hình mở hiệu quả cạnh tranh với các mô hình lớn hơn nhiều |
**Quy trình đào tạo**:
1. **Đào tạo trước**: Tìm hiểu từ dữ liệu văn bản lớn (dự đoán mã thông báo tiếp theo). Đây là nơi mô hình tiếp thu "kiến thức".
2. **Tinh chỉnh**: Đào tạo các nhiệm vụ cụ thể hoặc theo sở thích của con người.
3. **RLHF** (Học tập tăng cường từ phản hồi của con người): Con người đánh giá kết quả đầu ra của mô hình; mô hình học cách tạo ra kết quả đầu ra mà con người ưa thích.
**Cửa sổ ngữ cảnh** (lượng văn bản mà mô hình có thể xử lý cùng một lúc) đã tăng từ 4K mã thông báo (GPT-3 đầu tiên) lên hơn 1 triệu mã thông báo trong các mô hình năm 2026.
---

## AI có thể và không thể làm gì
### Năng lực hiện tại
| Nhiệm vụ | Hiệu suất | Hạn chế |
|------|-------------|-------------|
| **Tạo văn bản** | Xuất sắc - mạch lạc, theo ngữ cảnh, đa dạng về mặt phong cách | Có thể gây ảo giác (tự tin tạo ra thông tin sai lệch) |
| **Tạo mã** | Rất tốt cho các mẫu thông thường; có thể viết toàn bộ chương trình | Đấu tranh với kiến ​​trúc mới lạ; có thể giới thiệu các lỗi tinh vi |
| **Tạo hình ảnh** | Ảnh thực tế; phong cách nghệ thuật; chỉnh sửa | Bàn tay và văn bản vẫn chưa hoàn hảo; đấu tranh với lý luận không gian chính xác |
| **Dịch** | Gần con người cho các cặp ngôn ngữ chính | Ngôn ngữ có nguồn tài nguyên thấp kém chính xác hơn; sắc thái văn hóa có thể bị mất đi |
| **Nhận dạng giọng nói** | Gần gũi với con người trong âm thanh rõ ràng | Đấu tranh với giọng nặng, tiếng ồn xung quanh |
| **Lý luận** | Cải thiện nhanh chóng; có thể giải được nhiều bài toán logic | Thất bại trong các vấn đề mới đòi hỏi sự hiểu biết thực sự |
| **Toán học** | Giỏi các vấn đề tiêu chuẩn | Mắc lỗi về các bằng chứng mới; không phải là sự thay thế cho việc xác minh chính thức |
| **Lập kế hoạch và sử dụng công cụ** | Mới nổi (đại lý) | Vẫn không đáng tin cậy đối với các nhiệm vụ nhiều bước phức tạp mà không có sự giám sát của con người |
### Những gì AI không thể làm được (tính đến năm 2026)
- **Thực sự hiểu** bất cứ điều gì theo cách con người làm - nó xử lý các khuôn mẫu chứ không phải ý nghĩa
- **Đảm bảo độ chính xác thực tế** — ảo giác vẫn là một vấn đề chưa được giải quyết
- **Thay thế sự phán xét của con người** trong các quyết định mang tính rủi ro cao mà không có sự giám sát
- **Tổng quát hóa hoàn hảo** cho các miền rất khác với dữ liệu huấn luyện
- **Hoạt động tự chủ** trong môi trường vật lý không thể đoán trước (robot vẫn còn khó)
---

## Đạo đức và An toàn AI
AI không trung lập. Nó phản ánh dữ liệu đã được đào tạo, sự lựa chọn của các nhà phát triển và động lực của các tổ chức triển khai nó.
### Mối quan tâm chính
| Vấn đề | Điều gì xảy ra | Ví dụ |
|-------|-----------------|---------|
| **Thành kiến** | Hệ thống AI tái tạo và khuếch đại những thành kiến ​​trong dữ liệu đào tạo | Thuật toán tuyển dụng ưu tiên ứng viên nam; nhận dạng khuôn mặt với tỷ lệ lỗi cao hơn cho làn da sẫm màu |
| **Quyền riêng tư** | AI được đào tạo về dữ liệu cá nhân; khả năng giám sát | Đào tạo về tác phẩm có bản quyền; nhận dạng khuôn mặt trong không gian công cộng |
| **Lạm dụng** | Deepfakes, thông tin sai lệch, lừa đảo tự động | Video giả mạo do AI tạo ra về các chính trị gia; cuộc gọi lừa đảo tự động |
| **Chuyển việc** | Tự động hóa các nhiệm vụ trước đây do con người thực hiện | Sáng tạo nội dung, dịch vụ khách hàng, nhập dữ liệu, một số chương trình |
| **Căn chỉnh** | Đảm bảo mục tiêu AI phù hợp với giá trị con người | Một AI được yêu cầu "tối đa hóa việc sản xuất kẹp giấy" có thể chuyển đổi tất cả vật chất thành kẹp giấy |
| **Rủi ro hiện hữu** | Mối quan tâm lý thuyết về AGI trong tương lai | Tranh luận giữa các nhà nghiên cứu - một số cho rằng vấn đề này là khẩn cấp, một số khác cho rằng còn quá sớm |
### Ai đang làm việc về an toàn
- **Anthropic** — được thành lập bởi các nhà nghiên cứu trước đây của OpenAI, đặc biệt tập trung vào an toàn AI
- **DeepMind Safety** — nhóm nghiên cứu trong Google DeepMind
- **MIRI** (Viện nghiên cứu trí tuệ máy) — nghiên cứu an toàn về mặt lý thuyết
- **ARC** (Trung tâm nghiên cứu AI) — nghiên cứu an toàn thực nghiệm
- **Các cơ quan chính phủ** — Đạo luật AI của EU (2026), các sắc lệnh hành pháp của Hoa Kỳ, các khuôn khổ quốc tế
---

## AI trong thực tế — Theo ngành
| Công nghiệp | Ứng dụng | Trưởng thành |
|----------|-------------|----------|
| **Chăm sóc sức khỏe** | Chẩn đoán ung thư từ hình ảnh; khám phá thuốc (AlphaFold); dự đoán kết quả của bệnh nhân | Triển khai và mở rộng |
| **Tài chính** | Phát hiện gian lận, giao dịch thuật toán, chấm điểm tín dụng, cố vấn robo | Triển khai rộng rãi |
| **Giao thông** | Xe tự lái (Waymo, Tesla Autopilot); tối ưu hóa tuyến đường | Triển khai một phần; quyền tự chủ hoàn toàn vẫn còn hạn chế |
| **Giáo dục** | Học tập cá nhân hóa; Dạy kèm AI; chấm điểm tự động | Phát triển nhanh chóng |
| **Trường quảng cáo** | Tạo hình ảnh (Giữa hành trình, DALL-E); âm nhạc; hỗ trợ viết; hoàn thành mã | Chuyển đổi quy trình công việc ngay bây giờ |
| **An ninh mạng** | Phát hiện mối đe dọa; nhận dạng bất thường; cả tấn công và phòng thủ | Cuộc chạy đua vũ trang đang diễn ra |
| **Pháp lý** | Phân tích hợp đồng; xem xét tài liệu; nghiên cứu pháp luật | Được nhận làm con nuôi; mối quan tâm về độ chính xác |
| **Nông nghiệp** | Giám sát cây trồng qua vệ tinh/máy bay không người lái; phun chính xác; dự đoán năng suất | Đang phát triển |
| **Sản xuất** | Kiểm tra chất lượng; bảo trì dự đoán; tối ưu hóa chuỗi cung ứng | Triển khai rộng rãi |
---

## Robot và AI thể hiện
Robotics kết hợp AI với máy móc vật lý. Bất chấp nhiều thập kỷ tiến bộ, tương tác vật lý với thế giới vẫn khó hơn nhiều so với trí tuệ kỹ thuật số.
- **Boston Dynamics' Atlas** — chuyển động hai chân tiên tiến; parkour; nhiệm vụ kho
- **Robot công nghiệp** (ABB, FANUC, KUKA) — tự động hóa sản xuất; hàn; lắp ráp
- **Robot phẫu thuật** (Hệ thống da Vinci) — phẫu thuật xâm lấn tối thiểu với độ chính xác vượt xa bàn tay con người
- **Robot gia đình** (Roomba) — đơn giản nhưng thành công về mặt thương mại
- **Robot hình người** (Tesla Optimus, Hình AI) — mới nổi; nhiệm vụ thể chất có mục đích chung vẫn còn rất khó khăn
Khoảng cách giữa AI kỹ thuật số (đã đạt được tiến bộ vượt bậc) và AI vật lý (vật lộn với sự khéo léo, cân bằng và môi trường không thể đoán trước) là một trong những thách thức lớn của lĩnh vực này.
---

## Xu hướng hiện tại (thập niên 2020)
| Xu hướng | Chuyện gì đang xảy ra |
|-------|-------------------|
| **AI đa phương thức** | Hệ thống xử lý văn bản, hình ảnh, âm thanh và video cùng nhau (GPT-4V, Gemini) |
| **Đại lý** | LLM có thể sử dụng các công cụ, duyệt web, viết mã và thực hiện các hành động gồm nhiều bước |
| **Mẫu xe có trọng lượng mở** | LLaMA của Meta và những người khác dân chủ hóa quyền truy cập vào các mô hình lớn |
| **AI trên thiết bị** | Chạy các mô hình cục bộ trên điện thoại và máy tính xách tay (Apple Intelligence, NPU Qualcomm) |
| **Quy định về AI** | Đạo luật AI của EU (2026) — luật AI toàn diện đầu tiên; phân loại hệ thống theo mức độ rủi ro |
| **AI trong khoa học** | Gấp protein (AlphaFold), khám phá vật liệu, lập mô hình khí hậu, chứng minh toán học |
| **Mô hình ngôn ngữ nhỏ** | Các mô hình hiệu quả chạy trên phần cứng tiêu dùng; chất lượng tiếp cận các mô hình lớn hơn |
---

## Bản tóm tắt
AI là sự phát triển công nghệ quan trọng nhất của thế kỷ 21 cho đến nay. Đó không phải là phép thuật - đó là việc khớp mẫu trên quy mô lớn, được hỗ trợ bởi dữ liệu lớn, phần cứng mạnh mẽ và kiến ​​trúc thông minh. Điều làm cho nó có tính biến đổi là việc khớp mẫu, nếu được thực hiện đủ tốt, có thể tái tạo nhiều nhiệm vụ mà trước đây đòi hỏi trí thông minh của con người. Những thách thức đều quan trọng không kém: ảo giác, thành kiến, dịch chuyển công việc, lạm dụng và câu hỏi mở về việc liệu con đường từ AI hẹp đến trí thông minh tổng quát là ngắn hay dài không tưởng. Điều rõ ràng là AI sẽ định hình lại mọi ngành, mọi ngành nghề và mọi khía cạnh của cuộc sống hàng ngày. Hiểu cách nó hoạt động - và những gì nó không thể làm - là điều cần thiết để định hướng thế giới mà chúng ta đang xây dựng.