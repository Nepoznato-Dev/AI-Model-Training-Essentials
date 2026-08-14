---
# Metadata
title: "Generative AI Deep Dive"
description: "GANs, VAEs, diffusion models, LLMs, generative AI applications"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [generative, ai, deep, dive, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Nghiên cứu chuyên sâu về AI sáng tạo
AI sáng tạo đề cập đến các mô hình tạo ra nội dung mới - hình ảnh, văn bản, âm thanh, video, mã - thay vì chỉ phân loại hoặc dự đoán dữ liệu hiện có. Trong khi các mô hình ngôn ngữ lớn nhận được phần lớn sự chú ý, thì bối cảnh AI tổng quát lại rộng hơn nhiều. Tệp này bao gồm các kiến ​​trúc, kỹ thuật và sự cân bằng đằng sau các hệ thống tạo sinh hiện đại, từ mô hình khuếch tán đến bộ mã hóa biến thiên đến mô hình dòng chảy.
---

## Điều gì tạo nên một mô hình “có tính sáng tạo”?
| Loại | Nó làm gì | Ví dụ |
|------|-------------|----------|
| **Phân biệt đối xử** | Tìm hiểu ranh giới giữa các lớp | "Hình ảnh này là một con mèo hay một con chó?" |
| **Sáng tạo** | Tìm hiểu việc phân phối dữ liệu | "Tạo hình ảnh mới của một con mèo" |
Các mô hình tổng quát nắm bắt *cách dữ liệu được tạo ra*, không chỉ cách phân loại dữ liệu. Về cơ bản, điều này khiến chúng mạnh hơn - và khó huấn luyện hơn.
---

## Kiến trúc sáng tạo chính
### Bộ mã hóa tự động biến đổi (VAE)
VAE tìm hiểu cách biểu diễn có cấu trúc, nén (không gian tiềm ẩn) của dữ liệu, sau đó tạo các mẫu mới bằng cách lấy mẫu từ không gian đó.
| Thành phần | Vai trò |
|----------||------|
| **Bộ mã hóa** | Ánh xạ dữ liệu đầu vào tới một phân bố trong không gian tiềm ẩn (trung bình và phương sai) |
| **Không gian tiềm ẩn** | Một không gian liên tục, ít chiều, nơi các điểm dữ liệu tương tự ở gần nhau |
| **Bộ giải mã** | Bản đồ các điểm trong không gian tiềm ẩn trở lại không gian dữ liệu |
| **Phân kỳ KL** | Thuật ngữ chính quy hóa giúp giữ cho phân phối tiềm ẩn gần với phân phối chuẩn chuẩn |
**Cách tạo hoạt động**: lấy mẫu một vectơ ngẫu nhiên từ không gian tiềm ẩn → chuyển nó qua bộ giải mã → lấy điểm dữ liệu mới.
| Sức mạnh | Điểm yếu |
|----------|----------|
| Không gian tiềm ẩn mượt mà, liên tục | Đầu ra có xu hướng bị mờ |
| Khung toán học nguyên tắc | Bị giới hạn bởi năng lực của kiến ​​trúc |
| Có thể nội suy giữa các ví dụ | Ít sắc nét hơn so với đầu ra khuếch tán hoặc GAN |
VAE thường được sử dụng làm thành phần trong các mô hình khác (ví dụ: Khuếch tán ổn định sử dụng VAE như một phần của đường dẫn của nó).
### Mạng đối thủ sáng tạo (GAN)
GAN tạo ra hai mạng đối lập nhau: một **trình tạo** tạo ra dữ liệu giả và **bộ phân biệt đối xử** cố gắng phân biệt dữ liệu thật và giả.
| Thành phần | Mục tiêu |
|----------||------|
| **Máy phát điện** | Tạo ra dữ liệu đánh lừa người phân biệt đối xử |
| **Người phân biệt đối xử** | Phân loại chính xác dữ liệu thực và dữ liệu được tạo |
Họ tập luyện đồng thời, mỗi người thúc đẩy nhau tiến bộ. Về lý thuyết, trình tạo cuối cùng sẽ tạo ra dữ liệu không thể phân biệt được với dữ liệu thực.
| Biến thể GAN | Đổi mới quan trọng |
|-------------|--------------|
| **DCGAN** | Kiến trúc tích chập; đào tạo ổn định |
| **StyleGAN / StyleGAN2 / StyleGAN3** | Thế hệ dựa trên phong cách; khuôn mặt chân thực; thuộc tính có thể kiểm soát |
| **CycleGAN** | Dịch từ hình ảnh sang hình ảnh không ghép đôi (ngựa → ngựa vằn) |
| **Pix2Pix** | Dịch ghép nối hình ảnh với hình ảnh (phác thảo → ảnh) |
| **ProGAN** | Phát triển lũy tiến cho hình ảnh có độ phân giải cao |
| **BigGAN** | Tạo lớp có điều kiện ở quy mô |
**Tại sao GAN bị từ chối**: Quá trình đào tạo nổi tiếng là không ổn định (thu gọn chế độ, biến mất độ dốc). Các mô hình khuếch tán hiện tạo ra chất lượng tốt hơn cho hầu hết các tác vụ tạo hình ảnh. GAN vẫn được sử dụng cho các ứng dụng thời gian thực (chúng suy luận nhanh) và các tác vụ cụ thể như siêu phân giải.
### Mô hình khuếch tán
Các mô hình khuếch tán là công nghệ tiên tiến nhất hiện nay để tạo ra hình ảnh và video. Chúng hoạt động bằng cách thêm dần tiếng ồn vào dữ liệu cho đến khi đó là tiếng ồn ngẫu nhiên thuần túy, sau đó học cách đảo ngược quá trình.
| Giai đoạn | Điều gì xảy ra |
|-------|-------------|
| **Quy trình chuyển tiếp (đào tạo)** | Từ từ thêm nhiễu Gaussian qua hàng trăm/nghìn bước cho đến khi dữ liệu bị hủy |
| **Quy trình ngược lại (thế hệ)** | Tìm hiểu cách khử nhiễu từng bước, bắt đầu từ nhiễu thuần túy, cho đến khi xuất hiện hình ảnh sạch |
| Người mẫu | Nhà phát triển | Tính năng đáng chú ý |
|-------|-------------|--------|
| **DDPM** (Mô hình xác suất khuếch tán khử nhiễu) | Hồ và cộng sự, 2020 | Các mô hình khuếch tán được hiển thị có thể tạo ra hình ảnh chất lượng cao |
| ** Khuếch tán ổn định ** | Tính ổn định AI | Khuếch tán tiềm ẩn (chạy trong không gian nén); mã nguồn mở |
| **DALL-E 3** | OpenAI | Tích hợp với ChatGPT để hiểu văn bản |
| **Giữa hành trình** | Giữa hành trình | Chất lượng nghệ thuật; nguồn đóng |
| **Hình ảnh** | Google DeepMind | Chuyển văn bản thành hình ảnh có độ trung thực cao |
| **Sora** | OpenAI | Tạo video thông qua máy biến áp khuếch tán |
| **FLUX** | Phòng thí nghiệm Rừng Đen | Kế thừa trọng lượng mở cho Khuếch tán ổn định |
### Tại sao Mô hình Khuếch tán Chiến thắng
| Lợi thế | Giải thích |
|----------||-------------|
| **Đào tạo ổn định** | Ổn định hơn nhiều so với GAN; không đào tạo đối thủ |
| **Chất lượng đầu ra** | Chất lượng hình ảnh hiện đại và đa dạng |
| **Khả năng kiểm soát** | Có thể được hướng dẫn bằng văn bản (thông qua CLIP), mặt nạ vẽ hoặc các điều kiện khác |
| **Đa dạng** | Ít bị sập chế độ hơn GAN; tạo ra kết quả đầu ra đa dạng |
| Nhược điểm | Giải thích |
|-------------|-------------|
| **Suy luận chậm** | Yêu cầu nhiều bước khử nhiễu (điển hình là 20–50) |
| **Tính toán chuyên sâu** | Mỗi bước là một bước chuyển tiếp đầy đủ thông qua một mô hình lớn |
### Khuếch tán tiềm ẩn
Chạy khuếch tán trong không gian pixel rất tốn kém. **Khuếch tán tiềm ẩn** (được sử dụng bởi Khuếch tán ổn định) thay vào đó thực hiện quá trình khuếch tán trong không gian tiềm ẩn bị nén.
| Bước | Điều gì xảy ra |
|------|-------------|
| 1. Nén | VAE được đào tạo trước sẽ mã hóa hình ảnh thành một biểu diễn tiềm ẩn nhỏ hơn |
| 2. Khuếch tán | Mô hình khuếch tán thêm/loại bỏ tiếng ồn trong không gian tiềm ẩn |
| 3. Giải mã | Bộ giải mã VAE chuyển đổi hình ảnh tiềm ẩn thành hình ảnh đầy đủ |
Điều này làm cho việc tạo ra nhanh hơn và rẻ hơn đáng kể trong khi vẫn đảm bảo chất lượng.
---

## Thế hệ có điều kiện văn bản
Hầu hết các hệ thống tạo sinh hiện đại đều dựa trên các lời nhắc bằng văn bản - bạn mô tả những gì bạn muốn và mô hình sẽ tạo ra nó.
### CLIP (Huấn luyện trước ngôn ngữ-hình ảnh tương phản)
CLIP tìm hiểu không gian nhúng chung cho văn bản và hình ảnh. Nó được đào tạo trên hàng tỷ cặp văn bản-hình ảnh từ internet.
| Năng lực | Mô tả |
|----------||-------------|
| **Phân loại bắn không** | Phân loại hình ảnh bằng mô tả văn bản mà không cần đào tạo |
| **Truy xuất văn bản-hình ảnh** | Tìm hình ảnh phù hợp nhất cho truy vấn văn bản |
| **Khuếch tán hướng dẫn** | Hướng việc tạo hình ảnh về phía lời nhắc văn bản |
### Hướng dẫn không cần phân loại (CFG)
CFG kiểm soát mức độ chặt chẽ của hình ảnh được tạo theo lời nhắc văn bản.
| Cân CFG | Hiệu ứng |
|----------||--------|
| **1,0** | Không có hướng dẫn; đa dạng nhưng có thể không khớp với lời nhắc |
| **5,0–7,5** | Cân bằng; chất lượng tốt và tuân thủ nhanh chóng |
| **10.0++** | Tuân thủ mạnh mẽ; có thể tạo ra những hình ảnh quá bão hòa hoặc có nhiều yếu tố giả tạo |
---

## Các phương pháp tiếp cận sáng tạo khác
### Chuẩn hóa luồng
| Tính năng | Mô tả |
|----------|-------------|
| **Cách thức hoạt động** | Tìm hiểu ánh xạ không thể đảo ngược giữa dữ liệu và phân phối đơn giản |
| **Sức mạnh** | Tính toán khả năng chính xác; lấy mẫu nhanh |
| **Điểm yếu** | Yêu cầu kiến ​​trúc được thiết kế cẩn thận; kém linh hoạt |
| **Trường hợp sử dụng** | Phát hiện bất thường, ước tính mật độ |
### Mô hình tự hồi quy
| Tính năng | Mô tả |
|----------|-------------|
| **Cách thức hoạt động** | Tạo dữ liệu từng phần tử một, dựa trên tất cả các phần tử trước đó |
| **Sức mạnh** | Tự nhiên cho dữ liệu tuần tự (văn bản, mã, âm nhạc) |
| **Điểm yếu** | Tạo chậm (phải tuần tự); bị giới hạn bởi việc phân phối dữ liệu đào tạo |
| **Ví dụ** | GPT (văn bản), WaveNet (âm thanh), ImageGPT (hình ảnh) |
### Mô hình dựa trên năng lượng
| Tính năng | Mô tả |
|----------|-------------|
| **Cách thức hoạt động** | Tìm hiểu một hàm năng lượng; năng lượng thấp = dữ liệu thực tế |
| **Sức mạnh** | Linh hoạt; không cần chuẩn hóa |
| **Điểm yếu** | Đào tạo là khó khăn; lấy mẫu yêu cầu MCMC |
| **Trường hợp sử dụng** | Nghiên cứu lý thuyết; một số ứng dụng robot |
---

## Số liệu đánh giá
Làm thế nào để bạn đo lường chất lượng của dữ liệu được tạo ra? Nó khó hơn bạn nghĩ.
| Số liệu | Dành cho | Nó đo lường những gì | Hạn chế |
|--------|------|-----------------|-------------|
| **FID** (Khoảng cách khởi động Fréchet) | Hình ảnh | Khoảng cách giữa phân phối hình ảnh thực và được tạo | Thấp hơn là tốt hơn; không nắm bắt tốt sự đa dạng |
| **IS** (Điểm khởi đầu) | Hình ảnh | Chất lượng và sự đa dạng của hình ảnh được tạo ra | Gây tranh cãi; có thể chơi được |
| **Điểm CLIP** | Chuyển văn bản thành hình ảnh | Mức độ phù hợp của hình ảnh với lời nhắc văn bản | Phụ thuộc vào thành kiến ​​của CLIP |
| **Bối rối** | văn bản | Mô hình dự đoán mã thông báo tiếp theo tốt như thế nào | Thấp hơn là tốt hơn; không đo lường sự gắn kết |
| **BLEU / ROUGE** | Tạo văn bản | Trùng lặp với văn bản tham chiếu | Proxy kém cho sự phán xét của con người |
| **FAD** (Khoảng cách âm thanh Fréchet) | Âm thanh | Khoảng cách giữa phân phối âm thanh thực và được tạo | Tương tự FID cho âm thanh |
---

## Thế hệ có thể điều khiển được
Các hệ thống hiện đại cho phép bạn kiểm soát những gì được tạo ra ngoài những lời nhắc bằng văn bản.
| Phương pháp | Loại điều khiển | Ví dụ |
|--------|-------------|----------|
| **Sơn trong** | Điền vào các vùng bị che | Xóa đối tượng khỏi ảnh |
| **Sơn ngoại thất** | Mở rộng ra ngoài ranh giới hình ảnh | Làm cho cảnh quan rộng hơn |
| **Mạng điều khiển** | Hướng dẫn cấu trúc (cạnh, độ sâu, tư thế) | Tạo hình ảnh phù hợp với một tư thế cụ thể |
| **Bộ chuyển đổi IP** | Phong cách hoặc nội dung từ một hình ảnh tham khảo | "Làm cho nó giống như bức tranh này" |
| **LoRA** | Phong cách hoặc khái niệm được tinh chỉnh | Thêm một nhân vật hoặc phong cách nghệ thuật cụ thể |
| **Img2Img** | Chuyển đổi hình ảnh hiện có | Biến bản phác thảo thành hình ảnh chân thực |
---

## Tạo video
Thế hệ video là biên giới tiếp theo sau hình ảnh. Nó bổ sung thêm chiều hướng của thời gian và chuyển động.
| Người mẫu | Tiếp cận | Tính năng đáng chú ý |
|-------|----------|-----------------|
| **Sora** (OpenAI) | Máy biến áp khuếch tán | Lên tới 1080p; hiểu vật lý khá tốt |
| **Đường băng Gen-3** | Dựa trên sự khuếch tán | Công cụ tạo video thương mại |
| **Pika** | Dựa trên sự khuếch tán | Đoạn video ngắn từ văn bản |
| **Kling** | Tự hồi quy + khuếch tán | Tạo video dạng dài |
| **Veo 2** (Google) | Máy biến áp khuếch tán | Video chất lượng cao, nhất quán về mặt thể chất |
### Những thách thức trong việc tạo video
| Thử thách | Tại sao nó khó |
|----------||--------------|
| **Tính nhất quán về thời gian** | Các đối tượng phải trông giống nhau trên các khung |
| **Vật lý** | Trọng lực, va chạm, động lực học chất lỏng phải gần đúng |
| **Chiều dài** | Tạo ra từng phút video mạch lạc khó hơn nhiều so với một hình ảnh duy nhất |
| **Tính** | Video về cơ bản là nhiều hình ảnh; quy mô chi phí với số lượng khung hình |
| **Đánh giá** | Không có số liệu tiêu chuẩn nào nắm bắt được chất lượng video tốt |
---

## Tạo âm thanh
| Người mẫu | Loại | Ứng dụng |
|-------|------|-------------|
| **WaveNet** (DeepMind) | Tự thoái lui | Tổng hợp giọng nói chất lượng cao |
| **VALL-E** (Microsoft) | Bộ giải mã thần kinh | Chuyển văn bản thành giọng nói từ mẫu giọng nói 3 giây |
| **MusicGen** (Meta) | Dựa trên máy biến áp | Tạo văn bản thành nhạc |
| **Âm thanhLDM** | Khuếch tán tiềm ẩn | Tạo hiệu ứng âm thanh |
| **ElevenLabs** | Thương mại | Nhân bản và tổng hợp giọng nói |
---

## Kinh tế thế hệ
| Yếu tố | Tác động |
|--------|--------|
| **Chi phí đào tạo** | Mô hình phổ biến: $100K–$10M+ tùy theo quy mô |
| **Chi phí suy luận** | Tạo hình ảnh: ~$0,01–0,05 mỗi hình ảnh ở tỷ lệ |
| **Phần cứng** | Đào tạo: nhiều GPU A100/H100; Suy luận: có thể dùng một GPU |
| **Mở và đóng** | Các mô hình mở (Khuếch tán ổn định, FLUX) có thể chạy cục bộ; các mô hình đóng (DALL-E, Midjourney) chỉ dành cho API |
---

## Bản tóm tắt
AI sáng tạo đã phát triển từ GAN thông qua VAE đến các mô hình phổ biến và hơn thế nữa. Thông tin chuyên sâu quan trọng trên tất cả các kiến ​​trúc này đều giống nhau: tìm hiểu cách phân phối dữ liệu, sau đó lấy mẫu từ dữ liệu đó để tạo nội dung mới. Các mô hình khuếch tán hiện đang thống trị việc tạo hình ảnh và video do tính ổn định khi huấn luyện và chất lượng đầu ra của chúng. VAE đóng vai trò là khối xây dựng quan trọng. Các mô hình tự hồi quy thống trị văn bản và mã. Lĩnh vực này đang hướng tới việc tạo ra đa phương thức - các hệ thống có thể tạo ra văn bản, hình ảnh, âm thanh và video từ bất kỳ sự kết hợp đầu vào nào - và hướng tới việc tạo ra thế hệ nhanh hơn, rẻ hơn và dễ kiểm soát hơn.