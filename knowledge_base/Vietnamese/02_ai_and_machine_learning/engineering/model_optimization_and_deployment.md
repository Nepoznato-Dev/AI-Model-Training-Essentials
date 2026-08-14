---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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
# Tối ưu hóa và triển khai mô hình
Việc đào tạo một mô hình AI lớn là một thành tựu đáng kể, nhưng việc triển khai nó một cách hiệu quả lại đòi hỏi hầu hết nỗ lực kỹ thuật. Một mô hình mất 10 giây để phản hồi hoặc yêu cầu 8 GPU A100 là không thực tế đối với hầu hết các ứng dụng trong thế giới thực. Tối ưu hóa mô hình là quá trình làm cho mô hình nhỏ hơn, nhanh hơn và tiết kiệm chi phí hơn — trong khi vẫn duy trì chất lượng ở mức chấp nhận được. Tệp này bao gồm lượng tử hóa, cắt tỉa, chưng cất và các công cụ thực tế để triển khai các mô hình trong sản xuất.
---

## Tại sao phải tối ưu hóa?
| Mối quan tâm | Tác động |
|----------|--------|
| **Độ trễ** | Người dùng mong đợi phản hồi trong vòng chưa đầy 1 giây; cứ thêm 100 mili giây sẽ mất tương tác |
| **Chi phí** | Suy luận GPU rất tốn kém; mô hình 70B có giá ~ 0,05-0,15 USD cho mỗi 1 triệu mã thông báo trên phần cứng đám mây |
| **Bộ nhớ** | Model 7B trong FP32 cần 28 GB VRAM; hầu hết GPU tiêu dùng đều có 8-24 GB |
| **Năng lượng** | Chạy mô hình lớn tiêu tốn điện năng đáng kể; vấn đề dành cho thiết bị di động và biên |
| **Tỷ lệ** | Phục vụ hàng triệu người dùng yêu cầu các mẫu máy phù hợp với phần cứng sẵn có |
---

## Lượng tử hóa
Lượng tử hóa làm giảm độ chính xác của trọng số mô hình từ dấu phẩy động 32 bit (FP32) sang các định dạng nhỏ hơn như INT8, INT4 hoặc thậm chí thấp hơn.
### Định dạng chính xác
| Định dạng | Bit trên mỗi trọng lượng | Bộ nhớ cho Model 7B | Chất lượng |
|--------|-------|--------------------|----------|
| **FP32** | 32 | 28 GB | Đường cơ sở (chính xác hoàn toàn) |
| **FP16 / BF16** | 16 | 14 GB | Gần giống với FP32 |
| **INT8** | 8 | 7 GB | Mất chất lượng rất nhỏ |
| **INT4** | 4 | 3,5 GB | Giảm chất lượng vừa phải; vẫn dùng được |
| **INT3 / INT2** | 3-2 | 2,6-1,75 GB | Giảm chất lượng đáng kể; giai đoạn nghiên cứu |
### Phương pháp lượng tử hóa
| Phương pháp | Khi Nó Xảy Ra | Nó hoạt động như thế nào | Chất lượng |
|--------|-------|--------------|---------|
| **Lượng tử hóa sau đào tạo (PTQ)** | Sau khi đào tạo xong | Hiệu chỉnh mô hình trên một tập dữ liệu nhỏ; tìm thang đo tối ưu | Tốt cho INT8; xuống cấp ở INT4 |
| **GPTQ** | Sau khi đào tạo | Lượng tử hóa INT4 thân thiện với GPU bằng cách sử dụng thông tin bậc hai gần đúng | Chất lượng tốt tại INT4 |
| **AWQ** (Lượng tử hóa trọng lượng nhận biết kích hoạt) | Sau khi đào tạo | Bảo vệ trọng lượng nổi bật dựa trên cường độ kích hoạt | Tốt hơn GPTQ tại INT4 |
| **GGUF** (định dạng llama.cpp) | Sau khi đào tạo | Lượng tử hóa thân thiện với CPU; độ chính xác hỗn hợp trên mỗi lớp | Tối ưu hóa cho suy luận CPU |
| **Đào tạo nhận biết lượng tử hóa (QAT)** | Trong quá trình đào tạo | Mô phỏng lượng tử hóa trong quá trình đào tạo để mô hình học cách đối phó | Chất lượng tốt nhất; yêu cầu đào tạo lại |
###Tác động thiết thực
| Người mẫu | Kích thước FP16 | Kích thước INT4 | Tăng tốc | Mất chất lượng |
|-------|----------|-------------|----------|-------------|
| **LLaMA 7B** | 14 GB | 3,5 GB | 2-4x | ~1-2% trên điểm chuẩn |
| **LLaMA 70B** | 140GB | 35GB | 2-3x | ~2-3% trên điểm chuẩn |
---

## Cắt tỉa
Việc cắt tỉa sẽ loại bỏ các trọng lượng hoặc nơ-ron không cần thiết khỏi mô hình đã được huấn luyện.
| Loại | Mô tả | Lợi thế | Thử thách |
|------|-------------|-------------|----------|
| **Không có cấu trúc** | Xóa từng trọng số (đặt thành 0) | Tỷ lệ nén cao nhất | Yêu cầu hỗ trợ phần cứng thưa thớt |
| **Có cấu trúc** | Loại bỏ toàn bộ tế bào thần kinh, đầu chú ý hoặc lớp | Trực tiếp giảm kích thước mô hình | Có thể mất chất lượng hơn |
| **Dựa trên cường độ** | Xóa trọng số có giá trị tuyệt đối nhỏ nhất | Đơn giản; hoạt động tốt | Có thể bỏ lỡ trọng lượng nhỏ quan trọng |
| **Dựa trên tầm quan trọng** | Loại bỏ trọng số dựa trên sự đóng góp của chúng vào sản lượng | Bảo quản chất lượng tốt hơn | Đắt hơn để tính toán |
### Đường ống cắt tỉa
| Bước | Mô tả |
|------|-------------|
| 1. Tàu hỏa | Đào tạo mô hình đầy đủ thông thường |
| 2. Điểm | Tính điểm quan trọng cho từng trọng lượng/tế bào thần kinh |
| 3. Tỉa | Loại bỏ các yếu tố ít quan trọng nhất |
| 4. Tinh chỉnh | Đào tạo lại để khôi phục độ chính xác đã mất |
| 5. Lặp lại | Lặp lại việc cắt tỉa và tinh chỉnh để có độ nén cao hơn |
---

## Chắt lọc kiến ​​thức
Đào tạo mô hình “học sinh” nhỏ để bắt chước mô hình “giáo viên” lớn.
| Thành phần | Vai trò |
|----------||------|
| **Giáo viên** | Model lớn, chất lượng cao |
| **Sinh viên** | Mô hình nhỏ học từ thầy |
| **Tổn thất do chưng cất** | Học sinh cố gắng khớp phân phối đầu ra của giáo viên (nhãn mềm) |
### Các loại chưng cất
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Dựa trên nhật ký** | Học sinh phù hợp với xác suất đầu ra của giáo viên | Sự chưng cất ban đầu của Hinton |
| **Dựa trên tính năng** | Học sinh so sánh cách trình bày trung gian của giáo viên | FitNets |
| **Dựa trên quan hệ** | Sinh viên khớp mối quan hệ giữa các mẫu | RKD (Chưng cất kiến ​​thức quan hệ) |
| **Không có dữ liệu** | Không cần dữ liệu đào tạo ban đầu; sử dụng thế hệ của giáo viên | DAFL, Đảo ngược sâu |
### Ví dụ chưng cất đáng chú ý
| Giáo viên | Sinh viên | Kết quả |
|----------|----------|--------|
| **GPT-4** | GPT-3.5-turbo (tin đồn) | Model nhỏ hơn nhưng có nhiều chất lượng của GPT-4 |
| **BERT-Lớn** | Chưng cấtBERT | Nhỏ hơn 40%, nhanh hơn 60%, hiệu suất bằng 97% BERT |
| **LLaMA 70B** | LLaMA 7B (thông qua chưng cất) | Mô hình nhỏ nguồn mở tiếp cận chất lượng mô hình lớn |
---

## Tối ưu hóa dành riêng cho LLM
### Tối ưu hóa bộ đệm KV
Các mô hình ngôn ngữ lớn lưu trữ các cặp khóa-giá trị từ mã thông báo trước đó để tránh tính toán lại.
| Kỹ thuật | Mô tả | Tác động |
|----------|-------------|--------|
| **Chú ý nhiều truy vấn (MQA)** | Tất cả người đứng đầu chú ý chia sẻ một cặp KV | Giảm trí nhớ; giảm chất lượng nhẹ |
| **Chú ý truy vấn theo nhóm (GQA)** | Nhóm trưởng chia sẻ cặp KV | Cân bằng giữa MQA và sự chú ý tiêu chuẩn |
| **Chú ý đến cửa sổ trượt** | Chỉ tham dự vào token W cuối cùng | Giảm kích thước bộ nhớ đệm KV cho ngữ cảnh dài |
### Giải mã suy đoán
| Bước | Mô tả |
|------|-------------|
| 1 | Một mô hình "dự thảo" nhỏ tạo ra K token nhanh chóng |
| 2 | Mô hình lớn xác minh tất cả K token trong một lần chuyển tiếp |
| 3 | Mã thông báo được chấp nhận sẽ được giữ lại; những người bị từ chối được tái sinh |
Kết quả: Tăng tốc thế hệ lên 2-3 lần mà không làm giảm chất lượng (mô hình lớn luôn có tiếng nói cuối cùng).
### Chú ý chớp nhoáng
| Tính năng | Mô tả |
|----------|-------------|
| **Vấn đề** | Sự chú ý tiêu chuẩn yêu cầu bộ nhớ O(n²) cho ma trận chú ý |
| **Giải pháp** | Tính toán sự chú ý theo khối; không bao giờ cụ thể hóa toàn bộ ma trận trong bộ nhớ |
| **Kết quả** | nhanh hơn 2-4 lần; cho phép các cửa sổ ngữ cảnh dài hơn nhiều |
| **Biến thể** | Flash Chú ý 2 (nhanh hơn), FlashDecoding (được tối ưu hóa cho suy luận) |
---

## Khung phục vụ
| Khung | Tốt nhất cho | Tính năng chính |
|----------|----------|-------------|
| **vLLM** | LLM phục vụ | PagedChú ý; trộn liên tục; thông lượng cao |
| **TensorRT-LLM** | Suy luận GPU NVIDIA | Hiệu suất tối đa trên phần cứng NVIDIA |
| **llama.cpp** | Suy luận CPU và GPU tiêu dùng | Chạy các mô hình lượng tử hóa trên máy tính xách tay và điện thoại |
| **Ollama** | Mô hình địa phương đang chạy | Trình bao bọc thân thiện với người dùng xung quanh llama.cpp |
| **Máy chủ suy luận Triton** | Phục vụ đa khung | Hỗ trợ TensorFlow, PyTorch, ONNX, TensorRT |
| **Phục vụ ngọn đuốc** | Phục vụ mô hình PyTorch | Tích hợp PyTorch gốc |
| **Thời gian chạy ONNX** | Suy luận đa nền tảng | Thực thi được tối ưu hóa trên phần cứng |
| **BentoML** | Triển khai sản xuất | Khung bất khả tri; xử lý việc đóng gói và phục vụ |
---

## Các mẫu triển khai
| Mẫu | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **Triển khai biên** | Chạy mô hình trên điện thoại, thiết bị IoT hoặc phần cứng nhúng | Độ trễ thấp; ngoại tuyến; sự riêng tư |
| **API đám mây** | Mô hình lưu trữ trên GPU đám mây; phục vụ qua API | Tính toán tối đa; trả tiền cho mỗi lần sử dụng |
| **Kết hợp** | Mô hình nhỏ trên thiết bị; mô hình lớn trên đám mây | Tốt nhất của cả hai thế giới |
| **Không có máy chủ** | Chia tỷ lệ về 0; chỉ trả tiền khi sử dụng | Giao thông lẻ tẻ; nhạy cảm với chi phí |
| **Suy luận hàng loạt** | Xử lý dữ liệu hàng loạt theo lịch trình | Khi không cần thời gian thực |
---

## Đo điểm chuẩn
| Số liệu | Nó đo lường những gì |
|--------|-------------------|
| **Mã thông báo mỗi giây** | Thông lượng thế hệ (càng cao càng tốt) |
| **Thời gian đến mã thông báo đầu tiên (TTFT)** | Độ trễ trước khi mã thông báo đầu ra đầu tiên xuất hiện |
| **Độ trễ theo yêu cầu** | Tổng thời gian từ đầu vào đến hoàn thiện đầu ra |
| **Sử dụng bộ nhớ** | VRAM hoặc RAM tiêu thụ trong quá trình suy luận |
| **Thông lượng** | Yêu cầu được phục vụ mỗi giây |
| **Chi phí cho mỗi 1 triệu token** | Chi phí xử lý 1 triệu token |
---

## Lời khuyên thiết thực
- **Bắt đầu với lượng tử hóa.** Lượng tử hóa INT4 (AWQ hoặc GPTQ) mang lại sự cân bằng tốt nhất giữa chất lượng và kích thước. Hầu hết các mẫu 7B đều chạy thoải mái trên một GPU tiêu dùng duy nhất ở INT4.
- **Sử dụng vLLM để phân phối LLM.** Đây là tùy chọn nguồn mở nhanh nhất để suy luận LLM thông lượng cao.
- **Hồ sơ trước khi tối ưu hóa.** Đo lường thời gian thực sự được sử dụng. Đó thường là băng thông bộ nhớ chứ không phải tính toán, đó là điểm nghẽn.
- **Nối mô hình với nhiệm vụ.** Mô hình 7B phù hợp với hầu hết các nhiệm vụ. Đừng sử dụng 70B khi 7B sẽ làm được.
- **Cân nhắc việc chưng cất.** Nếu bạn cần một mô hình nhỏ, nhanh để sản xuất, hãy chắt lọc từ một mô hình lớn hơn thay vì đào tạo lại từ đầu.
- **Giám sát liên tục.** Hiệu suất của mô hình có thể giảm theo thời gian do sự phân bổ dữ liệu thay đổi. Theo dõi độ trễ, thông lượng và số liệu chất lượng.
---

## Bản tóm tắt
Tối ưu hóa mô hình là cầu nối giữa nghiên cứu và sản xuất. Lượng tử hóa thu nhỏ mô hình từ 4-8 lần với mức giảm chất lượng tối thiểu. Cắt tỉa loại bỏ trọng lượng chết. Chưng cất chuyển kiến ​​thức từ mô hình lớn sang mô hình nhỏ. Thủ thuật Flash Chú ý và KV-cache giúp suy luận nhanh hơn. Cùng với nhau, những kỹ thuật này biến mô hình yêu cầu trung tâm dữ liệu thành mô hình chạy trên máy tính xách tay hoặc điện thoại. Lĩnh vực này đang phát triển nhanh chóng – hiện nay yêu cầu 8 chiếc A100 chạy trên GPU dành cho người tiêu dùng.