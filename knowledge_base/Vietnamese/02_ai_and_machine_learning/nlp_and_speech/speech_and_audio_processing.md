<!--
---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
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
tags: [speech, audio, processing, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Xử lý giọng nói và âm thanh
Xử lý giọng nói và âm thanh bao gồm các công nghệ cho phép máy nghe, hiểu, tạo và xử lý âm thanh. Điều này bao gồm nhận dạng giọng nói (chuyển lời nói thành văn bản), tổng hợp giọng nói (chuyển văn bản thành lời nói), nhận dạng người nói, tạo nhạc và hiểu âm thanh môi trường. Lĩnh vực này đã được chuyển đổi nhờ học sâu - các hệ thống hiện đại tiếp cận độ chính xác ở cấp độ con người để nhận dạng giọng nói và tạo ra giọng nói tổng hợp tự nhiên kỳ lạ.
---

## Nguyên tắc cơ bản về âm thanh kỹ thuật số
Âm thanh là một sóng áp suất. Để xử lý nó bằng kỹ thuật số, chúng tôi lấy mẫu sóng đều đặn.
| Khái niệm | Mô tả | Giá trị điển hình |
|----------|-------------|---------------|
| **Tỷ lệ mẫu** | Âm thanh được đo bao nhiêu lần mỗi giây | 8 kHz (điện thoại), 16 kHz (giọng nói), 44,1 kHz (CD), 48 kHz (chuyên nghiệp) |
| **Độ sâu bit** | Độ chính xác của từng mẫu | 16-bit (CD), 24-bit (chuyên nghiệp), float 32-bit (xử lý) |
| **Kênh** | Mono (1), âm thanh nổi (2), âm thanh vòm (5.1, 7.1) | Âm thanh nổi cho âm nhạc; mono cho bài phát biểu |
| **Thời lượng** | Độ dài của âm thanh | Khác nhau |
Bản ghi đơn âm dài 1 phút ở tần số 16 kHz, 16 bit = 1,92 MB. Một bài hát âm thanh nổi dài 3 phút ở tần số 44,1 kHz, 16 bit = 30,3 MB.
---

## Trích xuất tính năng âm thanh
Các dạng sóng âm thanh thô rất khó để các mô hình làm việc trực tiếp. Chúng tôi trích xuất các tính năng nắm bắt được các đặc điểm quan trọng của âm thanh.
| Tính năng | Nó ghi lại những gì | Trường hợp sử dụng |
|----------|-------------------|----------|
| **Biểu đồ Mel** | Nội dung tần số theo thời gian, được ánh xạ tới nhận thức thính giác của con người | Nhận dạng giọng nói, phân loại nhạc |
| **MFCC** (Hệ số Cepstral Mel-Tần số) | Biểu diễn nhỏ gọn của đường bao quang phổ | Nhận dạng giọng nói truyền thống |
| **Sắc ký** | Phân bổ lớp cao độ (nốt nào đang chơi) | Phân tích nhạc, phát hiện hợp âm |
| **Tỷ lệ vượt 0** | Tần suất tín hiệu vượt qua số 0 | Phát hiện có giọng nói và không có tiếng nói |
| **Năng lượng RMS** | Độ ồn tín hiệu theo thời gian | Phát hiện hoạt động giọng nói |
| **Cao độ (F0)** | Tần số cơ bản | Nhận dạng người nói, phiên âm nhạc |
### Biểu đồ Mel
Biểu diễn âm thanh phổ biến nhất cho deep learning. Nó chuyển đổi âm thanh thành định dạng giống hình ảnh 2D:
| Trục | Đại diện |
|------|-------------|
| **Trục X** | Thời gian |
| **Trục Y** | Tần số (theo thang Mel - cách đều nhau) |
| **Màu sắc/cường độ** | Năng lượng ở tần số và thời gian đó |
Thang đo Mel gần giống với thính giác của con người: chúng ta phân biệt tần số thấp tốt hơn tần số cao.
---

## Nhận dạng giọng nói tự động (ASR)
ASR chuyển đổi ngôn ngữ nói thành văn bản. Đây là một trong những ứng dụng quan trọng nhất về mặt thương mại của AI âm thanh.
### Sự phát triển của ASR
| Thời đại | Tiếp cận | Hạn chế |
|------|----------|-------------|
| **Trước năm 2010** | Mô hình Markov ẩn + Mô hình hỗn hợp Gaussian | Yêu cầu kỹ thuật thủ công rộng rãi; nghèo trong điều kiện ồn ào |
| **2010-2015** | lai DNN-HMM | Mạng lưới thần kinh thay thế GMM; cải thiện đáng kể |
| **2015-2020** | Mô hình đầu cuối (Deep Speech, LAS) | Mạng nơ-ron đơn từ âm thanh đến văn bản |
| **2020+** | Dựa trên máy biến áp (Whisper, Conformer) | Độ chính xác tiên tiến; đa ngôn ngữ; mạnh mẽ |
### Các mô hình ASR chính
| Người mẫu | Kiến trúc | Dữ liệu đào tạo | Tính năng đáng chú ý |
|-------|-------------|---------------|--------|
| **Thì thầm** (OpenAI) | Biến áp mã hóa-giải mã | 680.000 giờ, 99 ngôn ngữ | Đa ngôn ngữ; mạnh mẽ với các điểm nhấn và tiếng ồn; mã nguồn mở |
| **Tuân thủ** | Tích chập + tự chú ý | Khác nhau | Kết hợp các tính năng cục bộ (đối tượng) và toàn cầu (chú ý) |
| **wav2vec 2.0** | Máy biến áp tự giám sát | Bài phát biểu không nhãn | Học từ âm thanh thô mà không cần phiên âm |
| **USM** (Google) | Mô hình lời nói phổ quát | 2 triệu giờ, hơn 300 ngôn ngữ | Hầu hết các ngôn ngữ được bảo hiểm |
| **MMS** (Meta) | Bài phát biểu đa ngôn ngữ lớn | Hơn 1.400 ngôn ngữ | Mở rộng phạm vi phủ sóng sang các ngôn ngữ có nguồn tài nguyên thấp |
### Số liệu ASR
| Số liệu | Mô tả |
|--------|-------------|
| **WER** (Tỷ lệ lỗi từ) | Tỷ lệ từ được phiên âm sai. Thấp hơn là tốt hơn. Hiệu suất của con người là ~4-5% đối với tiếng Anh sạch. |
| **CER** (Tỷ lệ lỗi ký tự) | Tương tự như WER nhưng ở cấp độ nhân vật. Dùng cho các ngôn ngữ không có ranh giới từ (tiếng Trung, tiếng Nhật). |
### Những thách thức ASR thường gặp
| Thử thách | Mô tả |
|----------||-------------|
| **Giọng và phương ngữ** | Hiệu suất giảm đáng kể đối với các giọng không chuẩn |
| **Tiếng ồn xung quanh** | Âm nhạc, giao thông, các loa khác làm giảm độ chính xác |
| **Chuyển mã** | Người nói chuyển đổi giữa các ngôn ngữ ở giữa câu |
| **Từ đồng âm** | "Ở đó" vs "của họ" vs "họ" — yêu cầu ngữ cảnh |
| **Dấu câu và định dạng** | Đầu ra ASR thường không có dấu chấm câu; cần xử lý hậu kỳ |
| **Ngôn ngữ có nguồn tài nguyên thấp** | Hầu hết các mô hình hoạt động kém đối với các ngôn ngữ có ít dữ liệu huấn luyện |
---

## Chuyển văn bản thành giọng nói (TTS)
TTS chuyển đổi văn bản viết thành âm thanh nói. Các hệ thống hiện đại tạo ra lời nói thường không thể phân biệt được với bản ghi âm của con người.
### Sự phát triển của TTS
| Thời đại | Tiếp cận | Chất lượng |
|------|----------|----------|
| **Trước năm 2010** | Concatenative (khâu các đoạn đã ghi) | Robot; khả năng biểu đạt hạn chế |
| **2010-2017** | Tham số thống kê (HMM, thần kinh sớm) | Tốt hơn nhưng vẫn có thể nhận biết là tổng hợp |
| **2017-2020** | Thần kinh (Tacotron, WaveNet) | Chất lượng gần giống con người; biểu cảm |
| **2020+** | Bộ giải mã thần kinh (VALL-E, Bark) | Nhân bản giọng nói; vài phát bắn; rất tự nhiên |
### Các mô hình TTS chính
| Người mẫu | Kiến trúc | Tính năng đáng chú ý |
|-------|-------------|--------|
| **WaveNet** (DeepMind) | Mô hình thế hệ tự hồi quy | TTS thực sự tự nhiên đầu tiên |
| **Tacotron 2** (Google) | Seq2seq + bộ phát âm | Từ đầu đến cuối; chất lượng cao |
| **VITS** | Suy luận biến phân + huấn luyện đối nghịch | Nhanh; chất lượng tốt; được sử dụng rộng rãi |
| **VALL-E** (Microsoft) | Mô hình ngôn ngữ codec thần kinh | Nhân bản giọng nói từ mẫu 3 giây |
| **Vỏ cây** (Suno) | Dựa trên máy biến áp | Đa ngôn ngữ; âm thanh không phải lời nói (tiếng cười, âm nhạc) |
| **ElevenLabs** | Thương mại | Nhân bản giọng nói hàng đầu trong ngành |
| **Trò chuyệnTTS** | Mã nguồn mở | Được tối ưu hóa cho bài phát biểu đàm thoại |
| **Bài phát biểu của cá** | Mã nguồn mở | Nhanh; đa ngôn ngữ |
### Nhân bản giọng nói
Nhân bản giọng nói tạo ra giọng nói tổng hợp nghe giống một người cụ thể từ một mẫu âm thanh ngắn.
| Phương pháp | Dữ liệu cần thiết | Chất lượng |
|--------|-------------|---------|
| **Tinh chỉnh** | 10-60 phút thuyết trình | Chất lượng cao; loa cụ thể |
| **Ít ảnh** | Bài phát biểu 3-30 giây | Chất lượng tốt; thiết lập nhanh |
| **Không bắn** | Không có dữ liệu loa mục tiêu | Sử dụng âm thanh tham chiếu tại thời điểm suy luận |
**Vấn đề đạo đức**: tính năng nhân bản giọng nói có thể được sử dụng để mạo danh, lừa đảo và giả mạo sâu. Hầu hết các nhà cung cấp thương mại đều yêu cầu sự đồng ý bằng giọng nói.
---

## Nhận dạng người nói
| Nhiệm vụ | Mô tả | Ứng dụng |
|------|-------------|-------------|
| **Xác minh người nói** | "Đây có phải là người mà họ tuyên bố là?" | Ngân hàng qua điện thoại, mở khóa thiết bị |
| **Nhận dạng người nói** | "Ai đang nói?" | Phiên âm cuộc họp, pháp y |
| **Trình bày nhật ký của người nói** | "Ai đã nói chuyện khi nào?" (trong âm thanh nhiều loa) | Tóm tắt cuộc họp, tạo phụ đề |
| Người mẫu | Tiếp cận |
|-------|----------|
| **ECAPA-TDNN** | Dựa trên nhúng; công nghệ tiên tiến nhất để xác minh |
| **d-vector** | Nhúng loa đơn giản từ DNN |
| **x-vector** | Cải thiện khả năng nhúng loa; được sử dụng rộng rãi |
---

## Truy xuất thông tin âm nhạc
| Nhiệm vụ | Mô tả | Công cụ/Mô hình |
|------|-------------|-------------|
| **Phiên âm nhạc** | Chuyển đổi âm thanh sang bản nhạc / MIDI | Spotify Basic Pitch, Spleeter |
| **Tách nguồn** | Cô lập từng nhạc cụ hoặc giọng hát | Demucs, Spleeter, Tách nguồn nhạc |
| **Phân loại thể loại** | Phân loại nhạc theo thể loại | CNN trên quang phổ |
| **Theo dõi nhịp** | Phát hiện vị trí nhịp độ và nhịp | Librosa, thưa bà |
| **Nhận dạng hợp âm** | Nhận biết hợp âm trong âm nhạc | Các mô hình Chord-CNN, CRF |
| **Thế hệ âm nhạc** | Tạo nhạc mới | MusicGen, MuseNet, AIVA |
---

## Phát hiện âm thanh môi trường
| Nhiệm vụ | Mô tả | Ứng dụng |
|------|-------------|-------------|
| **Phát hiện sự kiện âm thanh** | Xác định âm thanh trong môi trường | Nhà thông minh (vỡ kính, bé khóc) |
| **Phân loại cảnh âm thanh** | Phân loại môi trường (văn phòng, công viên, giao thông) | Thiết bị nhận biết ngữ cảnh |
| **Phát hiện bất thường** | Phát hiện âm thanh bất thường | Giám sát công nghiệp (machineæ·…éšœ) |
| Bộ dữ liệu | Âm thanh | Kích thước |
|----------|--------|------|
| **Bộ âm thanh** | 632 lớp âm thanh | Hơn 2 triệu clip YouTube |
| **ESC-50** | 50 lớp âm thanh môi trường | 2.000 clip |
| **UrbanSound8K** | Âm thanh đô thị | 8.732 clip |
---

## Công cụ và Khung
| Công cụ | Mục đích |
|------|----------|
| **Librosa** | Thư viện Python để phân tích âm thanh (tính năng, hiệu ứng, hình ảnh hóa) |
| **Pydub** | Thao tác âm thanh đơn giản (cắt, nối, xuất) |
| **FFmpeg** | Xử lý âm thanh/video bằng dòng lệnh (con dao của quân đội Thụy Sĩ) |
| **Đèn pin** | Xử lý âm thanh PyTorch (biến đổi, bộ dữ liệu, mô hình) |
| **Ôm Mặt (Transformers)** | Các mô hình ASR và TTS được đào tạo trước |
| **Thì thầm (OpenAI)** | Nhận dạng giọng nói (mã nguồn mở) |
| **Coqui TTS** | Bộ công cụ TTS mã nguồn mở |
| **Demucs** | Tách nguồn nhạc |
| **SpeechBrain** | Bộ công cụ giọng nói tất cả trong một (ASR, TTS, nhận dạng người nói) |
---

## Lời khuyên thiết thực
- **Luôn lắng nghe dữ liệu của bạn.** Trước khi đào tạo bất cứ điều gì, hãy nghe âm thanh mẫu. Lưu ý tốc độ mẫu, độ ồn và đặc điểm của loa.
- **Khớp tốc độ lấy mẫu.** Whisper dự kiến ​​có tần số 16 kHz. Nếu âm thanh của bạn là 44,1 kHz, hãy lấy mẫu lại — nhưng lưu ý rằng việc lấy mẫu xuống sẽ làm mất thông tin.
- **Tăng cường dữ liệu âm thanh.** Thêm tiếng ồn xung quanh, thay đổi tốc độ và cường độ, mô phỏng các micrô khác nhau. Điều này cải thiện đáng kể độ bền.
- **Sử dụng các mô hình được đào tạo trước.** Whisper cho ASR và VITS/Bark cho TTS là những điểm khởi đầu tuyệt vời. Tinh chỉnh hầu như luôn tốt hơn so với đào tạo từ đầu.
- **Xử lý chế độ im lặng.** Tính năng Phát hiện hoạt động bằng giọng nói (VAD) sẽ loại bỏ chế độ im lặng trước khi xử lý, tiết kiệm điện toán và cải thiện độ chính xác. Silero VAD và WebRTC VAD là những lựa chọn phổ biến.
- **Bình thường hóa âm lượng.** Các bản ghi khác nhau có mức âm lượng rất khác nhau. Bình thường hóa đến mức nhất quán trước khi xử lý.
---

## Bản tóm tắt
Xử lý giọng nói và âm thanh đã được cách mạng hóa nhờ học sâu. Các hệ thống ASR hiện đại như Whisper tiếp cận độ chính xác ở cấp độ con người trên hàng chục ngôn ngữ. Hệ thống TTS tạo ra giọng nói ngày càng khó phân biệt được với bản ghi âm của con người. Nhân bản giọng nói hoạt động từ vài giây âm thanh. Việc tạo nhạc, tách nguồn và phát hiện âm thanh môi trường đều đang tiến bộ nhanh chóng. Lĩnh vực này phải đối mặt với những thách thức đang diễn ra - ngôn ngữ có nguồn tài nguyên thấp, môi trường ồn ào, mối lo ngại về đạo đức xung quanh việc nhân bản giọng nói - nhưng quỹ đạo rất rõ ràng: máy móc đang trở nên nghe, hiểu và tạo ra âm thanh tốt như con người.