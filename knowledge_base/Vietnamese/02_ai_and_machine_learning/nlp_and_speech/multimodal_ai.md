---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [multimodal, ai, ai-and-machine-learning]
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
# AI đa phương thức
Hệ thống AI đa phương thức xử lý và kết hợp thông tin từ nhiều loại dữ liệu — văn bản, hình ảnh, âm thanh, video, v.v. — cùng một lúc. Trong khi các hệ thống AI trước đây thường chỉ có một phương thức (chỉ văn bản, chỉ hình ảnh), thì các hệ thống hiện đại có khả năng nhất là đa phương thức. GPT-4V đọc hình ảnh và văn bản cùng nhau; Gemini xử lý văn bản, hình ảnh, âm thanh và video một cách nguyên bản; và các hệ thống như Sora tạo video từ mô tả văn bản. Tệp này đề cập đến cách hoạt động của AI đa phương thức, các kiến ​​trúc đằng sau nó và lý do tại sao việc kết hợp các phương thức lại có tác dụng mạnh mẽ đến vậy.
---

## Tại sao là đa phương thức?
| Lợi ích | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Hiểu biết phong phú hơn** | Các phương thức khác nhau cung cấp thông tin bổ sung | Một video truyền tải chuyển động, âm thanh và bối cảnh mà chỉ văn bản không thể |
| **Tổng quát hóa tốt hơn** | Học qua các phương thức tạo ra các biểu diễn mạnh mẽ hơn | Người mẫu đã xem cả hình ảnh và văn bản mô tả về "con mèo" sẽ hiểu khái niệm này tốt hơn |
| **Tương tác tự nhiên hơn** | Con người giao tiếp qua nhiều kênh | Trợ lý giọng nói nhìn thấy những gì bạn đang chỉ vào |
| **Chuyển giao đa phương thức** | Kiến thức từ một phương thức này giúp ích cho một phương thức khác | Hiểu hình ảnh cải thiện việc tạo văn bản và ngược lại |
---

## Kiến trúc cốt lõi
### Mô hình ngôn ngữ tầm nhìn (VLM)
Các mô hình xử lý cả hình ảnh và văn bản cùng nhau.
| Kiến trúc | Nó hoạt động như thế nào | Ví dụ |
|-------------|-------------|---------|
| **Bộ mã hóa kép** | Bộ mã hóa riêng biệt cho hình ảnh và văn bản; kết hợp ở giai đoạn sau | CLIP, CĂN HỘ |
| **Bộ mã hóa tổng hợp** | Mã thông báo hình ảnh và văn bản được xen kẽ và xử lý cùng nhau | Chim hồng hạc, Song Tử |
| **Sự chú ý chéo** | Mã thông báo văn bản tham gia vào các tính năng của hình ảnh (hoặc ngược lại) | Flamingo, CoCa |
| **Mã thông báo hợp nhất** | Hình ảnh được chuyển đổi thành mã thông báo và được xử lý cùng với mã thông báo văn bản | Song Tử, Tắc Kè Hoa |
### Mô hình Ngôn ngữ-Tầm nhìn hoạt động như thế nào
| Bước | Mô tả |
|------|-------------|
| **1. Mã hóa hình ảnh** | Bộ mã hóa tầm nhìn (ViT, SigLIP) chuyển đổi hình ảnh thành một tập hợp các vectơ đặc trưng |
| **2. Mã hóa văn bản** | Bộ mã hóa ngôn ngữ xử lý mã thông báo văn bản |
| **3. Các phương thức cầu chì** | Các đặc điểm hình ảnh được chiếu vào không gian nhúng của mô hình ngôn ngữ |
| **4. Tạo** | Mô hình ngôn ngữ tạo ra văn bản dựa trên cả hình ảnh và văn bản đầu vào |
### Các mô hình ngôn ngữ-hình ảnh quan trọng
| Người mẫu | Nhà phát triển | Kiến trúc | Tính năng đáng chú ý |
|-------|----------||-------------|--------|
| **CLIP** | OpenAI | Bộ mã hóa kép (bộ mã hóa văn bản ViT +) | Phân loại hình ảnh không chụp qua văn bản |
| **LLaVA** | Mã nguồn mở | Bộ mã hóa hình ảnh LLaMA + CLIP | VLM nguồn mở; cộng đồng mạnh mẽ |
| **GPT-4V / 4o** | OpenAI | Thống nhất đa phương thức | Xử lý văn bản, hình ảnh, âm thanh cùng nhau |
| **Song Tử** | Google DeepMind | Tự nhiên đa phương thức từ đào tạo | Được xây dựng cho đa phương thức ngay từ đầu |
| **Claude** | Nhân chủng học | Tầm nhìn + văn bản | Mạnh về hiểu biết tài liệu và biểu đồ |
| **Qwen-VL** | Alibaba | VLM trọng lượng mở | Cạnh tranh bằng mô hình khép kín |
| **Thực tập sinhVL** | Mã nguồn mở | Bộ mã hóa tầm nhìn đa quy mô | Tùy chọn nguồn mở mạnh mẽ |
---

## Mô hình âm thanh và giọng nói
### Nhận dạng giọng nói (ASR)
| Người mẫu | Kiến trúc | Tính năng đáng chú ý |
|-------|-------------|--------|
| **Thì thầm** (OpenAI) | Biến áp mã hóa-giải mã | Được đào tạo về 680 nghìn giờ âm thanh đa ngôn ngữ; mạnh mẽ |
| **Tuân thủ** | Tích chập + tự chú ý | Kết hợp các tính năng cục bộ và toàn cầu |
| **wav2vec 2.0** | Tự giám sát | Học từ lời nói không nhãn |
| **USM** (Google) | Mô hình lời nói phổ quát | 2 triệu giờ dữ liệu được dán nhãn; Hơn 300 ngôn ngữ |
### Chuyển văn bản thành giọng nói (TTS)
| Người mẫu | Tiếp cận | Tính năng đáng chú ý |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Bộ giải mã thần kinh | Nhân bản giọng nói từ mẫu 3 giây |
| **Vỏ cây** (Suno) | Dựa trên máy biến áp | Đa ngôn ngữ; bao gồm các âm thanh không phải lời nói |
| **ElevenLabs** | Thương mại | Nhân bản giọng nói chất lượng cao |
| **Trò chuyệnTTS** | Mã nguồn mở | Lời nói hội thoại với ngữ điệu tự nhiên |
| **Bài phát biểu của cá** | Mã nguồn mở | Đa ngôn ngữ; suy luận nhanh |
### Hiểu âm thanh
| Người mẫu | Năng lực |
|-------|----------|
| **Âm thanhLDM** | Tạo hiệu ứng âm thanh từ văn bản |
| **MusicGen** (Meta) | Tạo văn bản thành nhạc |
| **Qwen-Audio** | Hiểu âm thanh (lời nói, âm nhạc, âm thanh môi trường) |
| **CÁ HỒI** | Hiểu lời nói, âm thanh, ngôn ngữ, âm nhạc và tiếng ồn |
---

## Mô hình video
Video kết hợp hình ảnh, âm thanh, văn bản và thời gian — khiến nó trở thành phương thức phức tạp nhất.
| Người mẫu | Loại | Năng lực |
|-------|------|-------------|
| **Sora** (OpenAI) | Chuyển văn bản thành video | Lên tới 1080p; hiểu vật lý |
| **Song Tử** | Hiểu video | Có thể phân tích video dài bằng âm thanh |
| **Video-LLaVA** | Video + văn bản | Hiểu biết về video nguồn mở |
| **Đường băng Gen-3** | Chuyển văn bản/hình ảnh thành video | Tạo video thương mại |
| **Kling** | Chuyển văn bản thành video | Tạo video dạng dài |
### Thử thách hiểu video
| Thử thách | Mô tả |
|----------||-------------|
| **Lý luận về thời gian** | Hiểu các sự kiện diễn ra theo thời gian |
| **Ngữ cảnh dài** | Video có thể dài hàng giờ; xử lý tất cả các khung hình rất tốn kém |
| **Đồng bộ hóa nghe nhìn** | Kết nối những gì đã nói với những gì được hiển thị |
| **Nhân quả** | Hiểu nguyên nhân và kết quả trong chuỗi video |
---

## Truy xuất đa phương thức
Tìm nội dung có liên quan trên các phương thức khác nhau.
| Nhiệm vụ | Mô tả | Ví dụ |
|------|-------------|----------|
| **Văn bản → Hình ảnh** | Tìm hình ảnh phù hợp với truy vấn văn bản | Tìm kiếm "hoàng hôn trên núi" trong thư viện ảnh |
| **Hình ảnh → Văn bản** | Tìm văn bản có liên quan đến hình ảnh | Tạo chú thích cho hình ảnh |
| **Văn bản → Âm thanh** | Tìm âm thanh phù hợp với mô tả | Thiết kế âm thanh: “tiếng bước chân trên sỏi” |
| **Hình ảnh → Hình ảnh** | Tìm hình ảnh trực quan tương tự | Tìm kiếm sản phẩm bằng hình ảnh |
### CLIP để truy xuất đa phương thức
Không gian nhúng được chia sẻ của CLIP cho phép truy xuất đa phương thức không cần bắn:
| Bước | Mô tả |
|------|-------------|
| 1 | Mã hóa tất cả hình ảnh bằng bộ mã hóa tầm nhìn |
| 2 | Mã hóa truy vấn văn bản bằng bộ mã hóa văn bản |
| 3 | Tính toán độ tương tự cosine giữa nhúng văn bản và tất cả các nhúng hình ảnh |
| 4 | Trả lại hình ảnh có độ tương đồng cao nhất |
Tính năng này hoạt động mà không cần đào tạo về nhiệm vụ cụ thể — một thuộc tính được gọi là khả năng **không bắn**.
---

## AI hiện thân
AI thể hiện kết hợp nhận thức đa phương thức với hành động vật lý.
| Hệ thống | Phương thức | Ứng dụng |
|--------|----------|-------------|
| **RT-2** (Google) | Tầm nhìn + ngôn ngữ → hành động của robot | Điều khiển robot đa năng từ hướng dẫn bằng văn bản |
| **Tháng 10** | Chính sách về robot nguồn mở | Được đào tạo về dữ liệu robot đa dạng |
| **Tesla Optimus** | Tầm nhìn + ngôn ngữ → nhiệm vụ thể chất | Robot hình người làm nhiệm vụ chung |
| **Hình 01** | Tầm nhìn + ngôn ngữ + lời nói | Robot hình người có khả năng đàm thoại |
### Những thách thức trong AI thể hiện
| Thử thách | Tại sao nó khó |
|----------||--------------|
| **Khoảng cách giữa sim và thật** | Mô phỏng không nắm bắt hoàn hảo vật lý trong thế giới thực |
| **Khéo léo** | Điều khiển vận động tinh (tay, ngón tay) cực kỳ khó |
| **An toàn** | Robot vật lý có thể gây hại thực sự |
| **Xử lý theo thời gian thực** | Phải nhận thức, quyết định và hành động trong mili giây |
| **Tổng quát hóa** | Robot được huấn luyện để nhặt cốc màu đỏ có thể thất bại với cốc màu xanh |
---

## Dữ liệu và đào tạo
### Dữ liệu đào tạo đa phương thức
| Bộ dữ liệu | Phương thức | Kích thước |
|----------|-------------|------|
| **LAION-5B** | Cặp văn bản-hình ảnh | 5,85 tỷ đôi |
| **DataComp** | Văn bản hình ảnh được tuyển chọn | Điểm chuẩn cho thiết kế tập dữ liệu |
| **WIT** (Wikipedia) | Văn bản hình ảnh từ Wikipedia | 11,5 triệu đôi |
| **HowTo100M** | Văn bản video (video hướng dẫn) | 100 triệu clip |
| **LibriSpeech** | Văn bản lời nói | 1.000 giờ tiếng Anh |
| **Tiếng nói chung** | Văn bản lời nói | Đa ngôn ngữ; do cộng đồng đóng góp |
### Chiến lược đào tạo
| Chiến lược | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Đào tạo chung** | Đào tạo đồng thời trên tất cả các phương thức | Khi bạn đã căn chỉnh dữ liệu đa phương thức |
| **Chương trình giảng dạy** | Bắt đầu với những ví dụ dễ hiểu; tăng độ khó | Cải thiện sự hội tụ |
| **Học tập tương phản** | Tìm hiểu cách khớp các cặp liên quan giữa các phương thức (kiểu CLIP) | Xây dựng cơ quan đại diện chia sẻ |
| **Điều chỉnh hướng dẫn** | Đào tạo về các cặp lệnh-phản hồi đa phương thức | Làm mô hình theo hướng dẫn đa phương thức |
---

## Sự đánh giá
| Điểm chuẩn | Phương thức | Nó kiểm tra cái gì |
|----------|-------------|---------------|
| **MMLU** | văn bản | Kiến thức xuyên suốt 57 môn học |
| **MMMU** | Văn bản + hình ảnh | Lý luận cấp đại học bằng sơ đồ |
| **MathVista** | Văn bản + hình ảnh | Lý luận toán học với dữ liệu trực quan |
| **Video-MME** | Văn bản + video | Hiểu video và lý luận về thời gian |
| **MŨ BẢO HIỂM** | Văn bản + âm thanh | Đánh giá đa phương thức theo ngữ cảnh dài |
| **Băng ghế SWE** | Văn bản + mã | Nhiệm vụ kỹ thuật phần mềm trong thế giới thực |
---

## Bản tóm tắt
AI đa phương thức thể hiện sự chuyển đổi từ các mô hình đơn mục đích sang các hệ thống nhận thức và suy luận trên tất cả các dạng dữ liệu. Các mô hình ngôn ngữ thị giác như GPT-4V và Gemini có thể hiểu hình ảnh và văn bản cùng nhau; các mô hình giọng nói như Whisper và VALL-E xử lý âm thanh; các mô hình video đang bắt đầu xử lý toàn bộ sự phức tạp của hình ảnh chuyển động có âm thanh. Xu hướng rất rõ ràng: các hệ thống AI có khả năng nhất trong tương lai sẽ có tính đa phương thức, xử lý đồng thời tất cả các loại thông tin. Những thách thức — căn chỉnh dữ liệu, chi phí tính toán, đánh giá và triển khai cụ thể — là rất đáng kể, nhưng tiến độ trong giai đoạn 2024–2026 rất nhanh chóng.