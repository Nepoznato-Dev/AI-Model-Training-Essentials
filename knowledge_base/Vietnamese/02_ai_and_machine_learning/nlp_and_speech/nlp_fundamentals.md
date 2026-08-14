---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [nlp, ai-and-machine-learning]
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

#NLP cơ bản
Xử lý ngôn ngữ tự nhiên (NLP) là lĩnh vực dạy máy hiểu, tạo và làm việc với ngôn ngữ của con người. Nó hỗ trợ các công cụ tìm kiếm, chatbot, hệ thống dịch thuật, phân tích cảm xúc và các mô hình ngôn ngữ lớn (LLM) đã biến đổi AI kể từ năm 2020. Tệp này đề cập đến quá trình phát triển từ các kỹ thuật cổ điển sang kiến ​​trúc dựa trên Transformer hiện đại.
---

## Tiền xử lý văn bản
Văn bản thô là lộn xộn. Trước khi một mô hình có thể sử dụng nó, nó cần phải được làm sạch và cấu trúc.
| Bước | Nó làm gì | Ví dụ |
|------|-------------|----------|
| **Mã thông báo** | Tách văn bản thành các mã thông báo (từ, từ phụ hoặc ký tự) | “Tôi yêu NLP” →`["I", "love", "NLP"]`|
| **Chữ thường** | Chuyển sang chữ thường | "Xin chào" → "xin chào" |
| **Dừng xóa từ** | Xóa các từ phổ biến (the, is, at) | "con mèo ngồi" → "mèo ngồi" |
| **Có cuống** | Chặt đuôi từ (thô) | "chạy" → "chạy" |
| **Từ ngữ** | Rút gọn về dạng từ điển (nhận biết ngữ cảnh) | "tốt hơn" → "tốt" |
| **Bình thường hóa** | Sửa mã hóa, loại bỏ các ký tự đặc biệt, mở rộng các từ viết tắt | “không” → “không” |
Các mô hình Transformer hiện đại thường bỏ qua việc loại bỏ từ dừng và xuất phát từ - chúng học các mẫu này từ dữ liệu.
---

## Trình bày văn bản
Máy móc cần những con số chứ không phải từ ngữ. Cách chúng ta biểu diễn văn bản dưới dạng vectơ là cơ bản.
### Phương pháp tiếp cận cổ điển
| Phương pháp | Mô tả | Hạn chế |
|--------|-------------|----------|
| **Mã hóa một lần** | Mỗi từ là một vị trí duy nhất trong một vector khổng lồ | thưa thớt; không có ý nghĩa ngữ nghĩa |
| **Túi Từ (BoW)** | Đếm tần số từ; bỏ qua đơn hàng | Mất trật tự từ hoàn toàn |
| **TF-IDF** | Trọng số các từ theo tần suất trong tài liệu × độ hiếm trên toàn bộ kho ngữ liệu | Vẫn bỏ qua trật tự và bối cảnh |
### Nhúng từ
Nhúng ánh xạ các từ thành các vectơ dày đặc trong đó các từ tương tự ở gần nhau.
| Người mẫu | Ý tưởng chính |
|-------|----------|
| **Word2Vec** (2013) | Dự đoán từ từ ngữ cảnh (CBOW) hoặc ngữ cảnh từ từ (Skip-gram) |
| **Găng tay** (2014) | Thống kê sự xuất hiện toàn cầu → vectơ dày đặc |
| **Văn bản nhanh** (2016) | Word2Vec + thông tin từ phụ (xử lý các từ hiếm tốt hơn) |
Ví dụ nổi tiếng:`king - man + woman ≈ queen`. Nhúng nắm bắt các mối quan hệ ngữ nghĩa.
**Hạn chế**: các cách nhúng cổ điển chỉ định một vectơ cho mỗi từ, vì vậy chúng không thể xử lý đa nghĩa (các từ có nhiều nghĩa). "Ngân hàng" trong "bờ sông" và "tài khoản ngân hàng" có cùng một vectơ.
---

## Mô hình trình tự
Trước Transformers, cách tiếp cận tiêu chuẩn cho NLP là xử lý văn bản một cách tuần tự.
| Kiến trúc | Nó hoạt động như thế nào | Sức mạnh | Điểm yếu |
|-------------|-------------|----------|----------|
| **RNN** | Xử lý từng mã thông báo một; duy trì trạng thái ẩn | Xử lý đầu vào có độ dài thay đổi | Độ dốc biến mất; không thể nắm bắt được sự phụ thuộc lâu dài |
| **LSTM** | RNN có cổng (quên, nhập, xuất) để điều khiển luồng thông tin | Tốt hơn ở các phụ thuộc tầm xa | Vẫn tuần tự; đào tạo chậm |
| **GRU** | LSTM đơn giản hóa (ít cổng hơn) | Nhanh hơn LSTM; hiệu suất tương tự | Những hạn chế cơ bản giống nhau |
Các mô hình này xử lý văn bản từ trái sang phải, nghĩa là chúng được huấn luyện chậm (không thể song song) và gặp khó khăn với các phần phụ thuộc dài hạn.
---

## Cơ chế chú ý
Sự chú ý cho phép mô hình xem xét đồng thời tất cả các vị trí trong một chuỗi và quyết định vị trí nào phù hợp nhất với dự đoán hiện tại.
### Thông tin chi tiết quan trọng
Thay vì nén toàn bộ câu vào một trạng thái ẩn duy nhất (như RNN làm), sự chú ý sẽ tính tổng có trọng số của tất cả các trạng thái ẩn, trong đó các trọng số được học.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Thành phần | Vai trò |
|----------||------|
| **Truy vấn (Q)** | Tôi đang tìm kiếm cái gì? |
| **Phím (K)** | Tôi chứa đựng những gì? |
| **Giá trị (V)** | Tôi cung cấp thông tin gì? |
| **√d_k** | Hệ số tỷ lệ để ngăn chặn các sản phẩm có chấm lớn |
---

## Kiến trúc máy biến áp
Người biến hình (Vaswani và cộng sự, 2017 - "Tất cả những gì bạn cần là sự chú ý") đã thay thế hoàn toàn sự tái diễn bằng sự chú ý. Đó là nền tảng của hầu hết tất cả NLP hiện đại.
### Ngành kiến ​​​​trúc
| Thành phần | Mô tả |
|----------||-------------|
| **Bộ mã hóa** | Đọc văn bản đầu vào; tạo ra các biểu diễn theo ngữ cảnh |
| **Bộ giải mã** | Tạo văn bản đầu ra; tham gia vào đầu ra bộ mã hóa |
| **Tự chú ý** | Mỗi mã thông báo liên quan đến tất cả các mã thông báo khác trong cùng một chuỗi |
| **Chú ý nhiều đầu** | Chạy song song nhiều đầu chú ý; nắm bắt các mối quan hệ khác nhau |
| **Mã hóa vị trí** | Tiêm thông tin vị trí (vì không tái phát) |
| **Mạng chuyển tiếp nguồn cấp dữ liệu** | Áp dụng độc lập cho từng vị trí |
| **Chuẩn hóa lớp** | Ổn định đào tạo |
| **Kết nối còn lại** | Bỏ qua các kết nối cho luồng gradient |
### Chỉ bộ mã hóa, Chỉ bộ giải mã, Bộ mã hóa-Bộ giải mã
| Biến thể | Kiến trúc | Tốt nhất cho | Ví dụ |
|----------|-------------|----------|--------|
| **Chỉ dành cho bộ mã hóa** | Hiểu văn bản | Phân loại, NER, phân tích tình cảm | BERT, RoBERTa, DeBERTa |
| **Chỉ dành cho bộ giải mã** | Tạo văn bản | Mô hình ngôn ngữ, chatbot, tạo mã | GPT-3/4, LLaMA, Claude |
| **Bộ mã hóa-giải mã** | Chuyển đổi văn bản | Dịch thuật, tóm tắt | T5, BART, mBART |
---

## Những gia đình kiểu mẫu lớn
### Dòng BERT (Chỉ dành cho bộ mã hóa)
| Người mẫu | Tính năng chính |
|-------|-------------|
| **BERT** (2018) | Mô hình ngôn ngữ đeo mặt nạ + Dự đoán câu tiếp theo |
| **RoBERTa** | Đã xóa NSP; được đào tạo lâu hơn với nhiều dữ liệu hơn |
| **ALBERT** | Chia sẻ tham số; dấu chân nhỏ hơn |
| **DeBERTa** | Phân tán sự chú ý; NLU cải tiến |
| **Chưng cất** | Nhỏ hơn 40%, nhanh hơn 60%, giữ lại 97% hiệu suất của BERT |
### Dòng GPT (Chỉ dành cho bộ giải mã)
| Người mẫu | Thông số | Ghi chú |
|-------|----------|-------|
| **GPT-2** | 1,5B | Các mô hình chỉ có bộ giải mã được hiển thị có thể tạo ra văn bản mạch lạc |
| **GPT-3** | 175B | Học ít lần; được nhắc thay vì tinh chỉnh |
| **GPT-3.5 / GPT-4** | Không tiết lộ | Điều chỉnh theo hướng dẫn + RLHF; đàm thoại |
| **LLaMA** (Meta) | 7B–70B | Trọng lượng mở; sinh ra hệ sinh thái LLM nguồn mở |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Các mô hình mở hiệu quả với hiệu suất mạnh mẽ |
---

## Nhiệm vụ NLP cốt lõi
| Nhiệm vụ | Mô tả | Mẫu điển hình |
|------|-------------|--------------|
| **Phân loại văn bản** | Gán nhãn cho văn bản (thư rác/không phải thư rác, tích cực/tiêu cực) | BERT, bộ phân loại được tinh chỉnh |
| **Nhận dạng thực thể được đặt tên (NER)** | Xác định người, tổ chức, địa điểm trong văn bản | Lớp BERT + CRF |
| **Phân tích tình cảm** | Xác định giai điệu cảm xúc | BERT tinh chỉnh hoặc LLM không bắn |
| **Dịch máy** | Dịch giữa các ngôn ngữ | T5, mBART, MarianMT |
| **Trả lời câu hỏi** | Trả lời câu hỏi theo ngữ cảnh | BERT (khai thác), GPT (sáng tạo) |
| **Tóm tắt** | Thu gọn văn bản dài | T5, BART, GPT |
| **Tạo văn bản** | Tạo văn bản mạch lạc | GPT-4, LLaMA, Claude |
---

## Tinh chỉnh và nhắc nhở
| Tiếp cận | Nó hoạt động như thế nào | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Tinh chỉnh** | Cập nhật trọng số mô hình trên dữ liệu nhiệm vụ cụ thể của bạn | Bạn đã dán nhãn dữ liệu; cần hiệu suất tối đa |
| **Nhắc nhở** | Đưa ra hướng dẫn mô hình bằng ngôn ngữ tự nhiên | Tạo mẫu nhanh; dữ liệu hạn chế; sử dụng LLM |
| **Ít ảnh** | Bao gồm các ví dụ trong lời nhắc | Khi bạn có một vài ví dụ nhưng chưa đủ để tinh chỉnh |
| **LoRA / QLoRA** | Tinh chỉnh hiệu quả; cập nhật ma trận cấp thấp nhỏ | Tinh chỉnh các mô hình lớn với bộ nhớ GPU hạn chế |
---

## Công cụ và Khung
| Công cụ | Mục đích |
|------|----------|
| **Biến hình ôm mặt** | Các mô hình được đào tạo trước, mã thông báo, quy trình tinh chỉnh |
| **spaCy** | Quy trình NLP cấp sản xuất (mã thông báo, NER, POS, phụ thuộc) |
| **NLTK** | Giáo dục; thuật toán NLP cổ điển |
| **Gensim** | Mô hình hóa chủ đề (LDA), nhúng từ (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Các khung để xây dựng các ứng dụng hỗ trợ LLM |
| **vLLM** | Phục vụ LLM thông lượng cao |
| **Mã thông báo (HF)** | Mã thông báo nhanh (BPE, WordPiece, SentencePiece) |
---

## Cảnh quan LLM
Bối cảnh NLP hiện đại bị chi phối bởi các Mô hình Ngôn ngữ Lớn:
| Danh mục | Ví dụ | Ghi chú |
|----------|----------|-------|
| **Độc quyền** | GPT-4, Claude, Song Tử | Hiệu suất tốt nhất; Chỉ truy cập API |
| **Trọng lượng mở** | LLaMA 3, Mistral, Qwen | Trọng lượng có sẵn; chạy cục bộ |
| **Nguồn mở** | Pythia, LỰA CHỌN | Mở hoàn toàn (dữ liệu, trọng lượng, mã) |
| **Đa phương thức** | GPT-4V, Song Tử, LLaVA | Xử lý văn bản + hình ảnh |
| **Chuyên về mã** | CodeLlama, StarCoder, DeepSeek Coder | Được đào tạo về mã |
| **Nhỏ / Hiệu quả** | Phi-3, Gemma, TinyLlama | Hiệu suất mạnh mẽ ở quy mô nhỏ |
Lĩnh vực này đang di chuyển nhanh chóng. Những gì tiên tiến ngày nay có thể bị thay thế trong nhiều tháng. Các nguyên tắc cơ bản — sự chú ý, mã thông báo, tinh chỉnh, đánh giá — vẫn ổn định.