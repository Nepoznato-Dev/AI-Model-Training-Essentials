---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [prompt, engineering, ai-and-machine-learning]
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

# Kỹ thuật nhanh chóng
Kỹ thuật nhắc nhở là thực hành thiết kế, tinh chỉnh và tối ưu hóa các lời nhắc đầu vào để có được kết quả đầu ra tốt nhất có thể từ mô hình ngôn ngữ. Nó vừa là nghệ thuật vừa là khoa học, đồng thời là giao diện chính để kiểm soát hành vi LLM mà không cần tinh chỉnh.
---

## Nguyên tắc cốt lõi
### Rõ ràng và cụ thể
Một lời nhắc rõ ràng không có chỗ cho sự mơ hồ. Chỉ định chính xác những gì bạn muốn, bao gồm định dạng, độ dài và phối cảnh.
**Mơ hồ:**
> "Hãy kể cho tôi nghe về Python."
**Cụ thể:**
> "Giải thích Khóa thông dịch toàn cầu (GIL) của Python. Mô tả tác động của nó đối với đa luồng, đưa ra một cách giải quyết và giữ câu trả lời của bạn dưới 200 từ."
### Cung cấp ngữ cảnh
Người mẫu hoạt động tốt hơn khi họ biết vai trò, đối tượng và mục tiêu.
**Không có ngữ cảnh:**
> "Viết hàm sắp xếp danh sách."
**Với bối cảnh:**
> "Bạn là nhà phát triển Python cấp cao. Viết hàm để sắp xếp danh sách từ điển theo một khóa nhất định. Sử dụng gợi ý loại và xử lý các trường hợp khó khăn. Đối tượng là nhà phát triển cấp dưới."
### Sử dụng hướng dẫn tích cực
Nói với người mẫu những gì cần làm, không phải những gì cần tránh. "Không bao gồm biệt ngữ" yếu hơn "Sử dụng ngôn ngữ đơn giản mà trẻ 10 tuổi có thể tiếp cận được".
---

## Cấu trúc nhắc nhở
### Vai trò hệ thống / Người dùng / Trợ lý
Hầu hết các API LLM đều hỗ trợ cấu trúc nhiều lượt:
- **Thông báo hệ thống**: Đặt hành vi, tính cách và các ràng buộc của mô hình (kéo dài trong toàn bộ phiên).
- **Thông báo người dùng**: Truy vấn hoặc hướng dẫn hiện tại.
- **Thông báo hỗ trợ**: Các phản hồi trước đó của mô hình (dùng để đảm bảo tính liên tục).
**Ví dụ (kiểu API OpenAI):**
Hệ thống: Bạn là một trợ lý mã hóa hữu ích. Bạn trả lời bằng các ví dụ mã ngắn gọn và giải thích ngắn gọn. Không bao giờ cung cấp mã không an toàn.
Người dùng: Viết hàm Python để tải xuống tệp từ URL.
### Nhắc nhở ít lần bắn
Cung cấp 2–3 ví dụ về định dạng đầu vào-đầu ra mong muốn trước khi yêu cầu mô hình thực hiện nhiệm vụ. Điều này dạy các mô hình.
**Ví dụ:**
Người dùng: Chuyển các câu này sang thể bị động:
Đầu vào: Con mèo đuổi con chuột.
Kết quả: Con chuột bị con mèo đuổi.
Đầu vào: Đầu bếp nấu bữa ăn.
Đầu ra: Bữa ăn do đầu bếp nấu.
Đầu vào: Cơn bão đã phá hủy ngôi nhà.
Đầu ra: (mô hình hoàn thành)
### Chuỗi tư duy (CoT)
Khuyến khích mô hình trình bày lý luận của mình từng bước một. Điều này cải thiện độ chính xác của các tác vụ số học, logic và nhiều bước.
**Không có CoT:**
> "24 × 37 là gì?"
**Với CoT:**
> "Tính 24 × 37. Trình bày lý luận của bạn từng bước."
Mô hình sẽ đưa ra các bước trung gian, giảm thiểu sai sót số học.
### Kết quả đầu ra có cấu trúc
Yêu cầu một định dạng cụ thể như JSON, YAML hoặc bảng đánh dấu để làm cho việc phân tích cú pháp trở nên đáng tin cậy.
Người dùng: Liệt kê ba ưu và ba nhược điểm của microservice. Chỉ trả về một đối tượng JSON hợp lệ với các khóa "ưu" và "nhược điểm", mỗi chuỗi là một chuỗi.
---

## Kỹ thuật nâng cao
### Tính tự nhất quán
Tạo nhiều câu trả lời cho cùng một lời nhắc (có nhiệt độ > 0) và lấy đa số phiếu cho câu trả lời cuối cùng. Điều này đặc biệt hiệu quả đối với các nhiệm vụ lý luận.
### Cây suy nghĩ
Khám phá song song nhiều con đường lý luận, đánh giá từng con đường và chọn con đường tốt nhất. Đây là một kỹ thuật ở cấp độ nghiên cứu nhưng có thể được ước tính gần đúng bằng cách yêu cầu mô hình "khám phá các giải pháp thay thế".
### ReAct (Lý luận + Diễn xuất)
Hãy để mô hình xen kẽ lý luận với các lệnh gọi công cụ. Nó có thể suy nghĩ, sau đó hành động (ví dụ: tìm kiếm trên web, chạy mã), sau đó suy nghĩ lại dựa trên kết quả.
**Cấu trúc gợi ý:**
Bạn có quyền truy cập vào một máy tính và một công cụ tìm kiếm. Với mỗi bước, xuất ra:
Suy nghĩ: (lý luận của bạn)
Hành động: (tên công cụ, đầu vào)
Quan sát: (công cụ đầu ra)
... tiếp tục cho đến khi bạn có câu trả lời cuối cùng.
### Bài tập Persona
Chỉ định một nhân vật cụ thể để đóng khung phản hồi.
**Ví dụ:**
- "Bạn là nhà phát triển nhân Linux đang giải thích việc quản lý bộ nhớ cho sinh viên mới tốt nghiệp."
- "Bạn là một chuyên gia dinh dưỡng thân thiện đưa ra lời khuyên chung cho khách hàng."
- "Bạn là một nhà phê bình công nghệ hoài nghi đang đánh giá một tiện ích mới."
---

## Điều chỉnh tham số
- **Nhiệt độ** (0,0 – 1,0+): Kiểm soát tính ngẫu nhiên. Thấp hơn = quyết đoán hơn, cao hơn = sáng tạo hơn. Sử dụng 0,0–0,3 cho câu trả lời thực tế; 0,7–1,0 cho bài viết sáng tạo.
- **Top-p** (lấy mẫu hạt nhân): Cắt khối lượng xác suất ở một ngưỡng tích lũy nhất định. 0,9 có nghĩa là các mẫu mô hình từ 90% mã thông báo có khả năng cao nhất. Thường điều chỉnh nhiệt độ hoặc top-p, không phải cả hai.
- **Mã thông báo tối đa**: Đặt độ dài đầu ra tối đa. Hãy nhớ dành chỗ cho phản hồi trong cửa sổ ngữ cảnh.
- **Hình phạt tần suất**: Giảm sự lặp lại của các mã thông báo giống nhau.
- **Hình phạt hiện diện**: Khuyến khích người mẫu giới thiệu chủ đề mới.
---

## Những cạm bẫy và cách khắc phục thường gặp
| Vấn đề | Nguyên nhân có thể | Sửa chữa |
|----------|--------------|------|
| Mô hình bỏ qua các phần của dấu nhắc | Lời nhắc quá dài hoặc quá tải | Rút ngắn; đặt hướng dẫn quan trọng nhất ở cuối |
| Đầu ra quá dài dòng | Không hạn chế về độ dài | Thêm "Giới hạn ở 3 câu" hoặc đặt max_tokens |
| Đầu ra quá ngắn gọn | Quá hạn chế | Thêm "Giải thích chi tiết" hoặc hạ nhiệt độ |
| Ảo giác thực tế | Không đủ ngữ cảnh hoặc câu hỏi mơ hồ | Thêm "Nếu bạn không chắc chắn, hãy nói 'Tôi không biết'" và cung cấp ngữ cảnh RAG |
| Định dạng không nhất quán | Không có hướng dẫn định dạng rõ ràng | Yêu cầu JSON, bảng đánh dấu hoặc danh sách dấu đầu dòng |
| Câu trả lời mẫu sai ngôn ngữ | Không có hướng dẫn ngôn ngữ | Nêu rõ "Trả lời bằng tiếng Anh" (hoặc ngôn ngữ mục tiêu của bạn) |
---

## Mẫu nhắc nhở cho các tác vụ thông thường
### Tóm tắt
Tóm tắt văn bản sau bằng 3 gạch đầu dòng. Tập trung vào các lập luận chính và tránh các chi tiết.
Văn bản: [chèn văn bản]

### Tạo mã
Viết hàm [ngôn ngữ] [thực hiện X].
Yêu cầu:
Sử dụng gợi ý loại.
Bao gồm một chuỗi tài liệu.
Xử lý các trường hợp cạnh: [danh sách].
Không sử dụng thư viện bên ngoài trừ khi được chỉ định.

### Giải thích
Giải thích [khái niệm] cho [người không phải chuyên gia/sinh viên đại học/trẻ em]. Sử dụng một sự tương tự khi thích hợp.
### Động não
Tạo 10 ý tưởng cho [chủ đề]. Đối với mỗi ý tưởng, hãy đưa ra một câu mô tả và một thử thách tiềm ẩn.
chữ
### Phân loại
Phân loại phản hồi của khách hàng sau đây là [tích cực, trung lập, tiêu cực].
Cung cấp điểm tin cậy (0-100) và lý do ngắn gọn.
Phản hồi: [chèn văn bản]
### Dịch có phong cách
Dịch đoạn văn bản tiếng Anh sau đây sang tiếng Tây Ban Nha. Sử dụng giọng điệu thân mật phù hợp cho bài đăng trên mạng xã hội.
Văn bản: [chèn văn bản]
---

## Đánh giá lời nhắc
Hãy coi lời nhắc như mã: phiên bản chúng, kiểm tra chúng và lặp lại.
- **Thử nghiệm A/B** các biến thể lời nhắc khác nhau trên một nhóm truy vấn được đưa ra.
- **Đo lường thành công** thông qua đánh giá của con người hoặc số liệu tự động (ví dụ: đối sánh chính xác, BLEU, tính điểm tùy chỉnh).
- **Giữ sổ đăng ký lời nhắc** (một tệp văn bản hoặc bảng tính đơn giản) với lời nhắc, phiên bản và hiệu suất được quan sát.
---