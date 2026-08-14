---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [local, ai, architecture, ai-and-machine-learning]
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

# Kiến trúc AI cục bộ
Hướng dẫn thực tế để chạy hoàn toàn các mô hình ngôn ngữ lớn trên thiết bị — cân nhắc về phần cứng, công cụ suy luận, tối ưu hóa bộ nhớ và thiết kế hệ thống để triển khai ở biên.
---

## Tại sao nên chạy AI cục bộ?
- **Quyền riêng tư**: Không có dữ liệu nào rời khỏi thiết bị.
- **Chi phí**: Không có phí API cho mỗi mã thông báo.
- **Độ trễ**: Suy luận không cần mạng, có thể dự đoán được.
- **Tính khả dụng ngoại tuyến**: Hoạt động mà không cần internet.
- **Kiểm soát**: Kiểm soát hoàn toàn phiên bản mô hình, tùy chỉnh và tinh chỉnh.
---

## Yêu cầu phần cứng
### Bộ nhớ GPU (VRAM)
Nguồn lực quan trọng nhất. Kích thước mô hình trong bộ nhớ ≈ **tham số × byte cho mỗi tham số**.
| Chính xác | Byte cho mỗi tham số | Model 3.8B | Mô hình 7B | Mẫu 13B | mô hình 70B |
|----------||----------------------|-------------|----------|----------|----------||
| FP32 | 4 | ~15GB | ~28GB | ~52GB | ~280GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26 GB | ~140GB |
| INT8 (8-bit) | 1 | ~3,8 GB | ~7GB | ~13GB | ~70 GB |
| INT4 (4-bit) | 0,5 | ~1,9 GB | ~3,5 GB | ~6,5 GB | ~35 GB |
**Hướng dẫn thực hành:**
- 8GB VRAM → tối đa 7B model 4-bit.
- 12GB VRAM → lên tới 13B model 4-bit.
- 24GB VRAM → các model lên tới 70B ở 4 bit (hoặc 13B ở 8 bit).
- Apple Silicon (bộ nhớ hợp nhất) có thể chạy các mẫu 70B trên hệ thống 64GB+.
### RAM (Bộ nhớ hệ thống)
- Đối với CPU suy luận, bạn cần có đủ RAM hệ thống để tải mô hình (tương tự như số VRAM).
- Đối với suy luận GPU, RAM hệ thống đóng vai trò quan trọng trong việc tải mô hình vào bộ nhớ trước khi tải sang VRAM.
### Lưu trữ
- Trọng lượng mô hình lượng tử hóa chiếm vài GB (ví dụ: 4-bit 7B ≈ 4 GB trên đĩa). Đảm bảo có ít nhất 20–50 GB dung lượng trống cho nhiều kiểu máy.
###CPU
- Để xử lý nhanh chóng (điền trước) và giảm tải CPU, CPU đa lõi hiện đại sẽ trợ giúp.
- Chip Apple M-series có hiệu năng tuyệt vời dành cho LLM nhờ bộ nhớ hợp nhất và Neural Engine.
---

## Lượng tử hóa
Lượng tử hóa làm giảm độ chính xác về số của trọng lượng, cắt giảm đáng kể bộ nhớ và tăng tốc độ với chi phí chính xác nhỏ.
### Các định dạng phổ biến
| Định dạng | Bit | Mô tả | Sử dụng điển hình |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp, được tối ưu hóa cho kết hợp CPU/GPU | Tốt nhất cho suy luận cục bộ |
| **GPTQ** | 4–8 | Chỉ dành cho GPU, hiệu quả trên CUDA | Tốt nhất cho GPU NVIDIA |
| **AWQ** | 4 | Nhận biết kích hoạt, chỉ dành cho GPU | Tốt cho suy luận hàng loạt trên GPU |
| **ONNX** | biến | Chuẩn hóa, đa nền tảng | Phục vụ sản xuất |
### Chọn mức lượng tử hóa
- **Q8_0** (8-bit): giảm chất lượng tối thiểu, kích thước lớn nhất.
- **Q6_K** (6-bit): chất lượng tốt, độ nén khá.
- **Q5_K_M** (5-bit): điểm ngọt chung.
- **Q4_K_M** (4-bit): chất lượng nhỏ nhất, chấp nhận được đối với hầu hết các tác vụ.
- **IQ4_XS** / **IQ3_XS**: Lượng tử hóa được cải thiện với độ phức tạp tốt hơn ở 4/3 bit.
**Quy tắc chung:** Sử dụng Q4_K_M để có sự cân bằng tốt về chất lượng và kích thước. Nếu bạn có thêm VRAM, hãy sử dụng Q5 hoặc Q6.
---

## Công cụ suy luận (Cục bộ)
### llama.cpp
- Viết bằng C++.
- Hỗ trợ định dạng GGUF.
- Tối ưu hóa cho CPU và GPU (thông qua CUDA, Metal, OpenCL).
- Rất nhanh, đặc biệt là trên CPU.
- Dòng lệnh, chế độ máy chủ và các ràng buộc Python.
**Lệnh ví dụ:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

###Ollama
- Bao bọc llama.cpp bằng API CLI và REST đơn giản.
- Tự động tải xuống các mô hình, quản lý chúng.
- Tuyệt vời cho các ứng dụng tạo mẫu và máy tính để bàn.
- Hỗ trợ các Modelfiles tùy chỉnh cho lời nhắc hệ thống.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

###LM Studio
- Ứng dụng máy tính để bàn đồ họa cho Windows, macOS, Linux.
- Giao diện tải xuống và trò chuyện chỉ bằng một cú nhấp chuột.
- Máy chủ cục bộ tích hợp với API tương thích OpenAI.
- Tốt cho người dùng không rành về kỹ thuật và thử nghiệm nhanh.
### Ôm mặt Transformers + bitandbyte
- Thư viện Python chuẩn cho mô hình HF.
- Sử dụng`bitsandbytes`để lượng tử hóa 4 bit (`load_in_4bit=True`).
- Tinh chỉnh linh hoạt hơn nhưng chậm hơn llama.cpp cho suy luận.
### ExLlamaV2
- Suy luận GPU rất nhanh cho GPTQ và AWQ.
- Hiệu suất tốt nhất trên GPU NVIDIA.
- Hỗ trợ tạo hàng loạt.
### mlx (Táo)
- Khuôn khổ của Apple dành cho chip dòng M.
- Tối ưu hóa cao cho Apple Silicon.
- API Python.
---

## Quản lý bộ nhớ
### Cửa sổ ngữ cảnh và bộ đệm KV
Bộ đệm KV lưu trữ các cặp khóa-giá trị cho mọi lớp và mọi mã thông báo trong ngữ cảnh. Nó phát triển tuyến tính với độ dài ngữ cảnh.
Chi phí bộ nhớ ≈ 2 × lớp × (đầu KV × đầu mờ) × mã thông báo × byte cho mỗi giá trị
Đối với mô hình 32 lớp có 8 đầu KV và 128 đầu mờ, mỗi mã thông báo có giá ~32 × 8 × 128 × 2 byte = 65 KB mỗi mã thông báo. Đối với 128k mã thông báo, đó là ~8 GB chỉ dành cho bộ nhớ đệm.
### Chiến lược giảm tải
- **Giảm tải lớp**: Đặt một số lớp trên GPU, các lớp khác trên CPU. Nhanh hơn CPU thuần túy, yêu cầu VRAM thấp hơn.
- **Truyền phát mã thông báo**: Xử lý mã thông báo tăng dần thay vì tất cả cùng một lúc.
### Nhắc vào bộ nhớ đệm
Sử dụng lại bộ đệm KV trên các lời nhắc tương tự để tránh tính toán lại giai đoạn điền trước. Một số khung hỗ trợ điều này (ví dụ: vLLM, llama.cpp với`--prompt-cache`).
### Tệp được ánh xạ bộ nhớ
Tải trọng lượng mô hình trực tiếp từ đĩa mà không tải chúng hoàn toàn vào RAM (hữu ích cho các mô hình lớn trên hệ thống giới hạn bộ nhớ). llama.cpp sử dụng ánh xạ bộ nhớ theo mặc định.
---

## Kiến trúc triển khai
### Chế độ một thiết bị
Một mô hình chạy trên một máy (máy tính xách tay, điện thoại thông minh, thiết bị biên). Được sử dụng cho trợ lý cá nhân, ứng dụng ghi chú, hoàn thiện mã.
### Đám mây biên lai
Mô hình cục bộ xử lý các truy vấn phổ biến; dự phòng sang mô hình đám mây cho các câu hỏi phức tạp. Điều này mang lại lợi ích tốt nhất cho cả hai thế giới — tốc độ/riêng tư cho hầu hết mọi người, khả năng cho các trường hợp biên.
### Suy luận phân tán (Đa GPU)
Đối với các mô hình lớn hơn, hãy phân chia các lớp trên nhiều GPU (song song tensor) hoặc phân chia bối cảnh trên các thiết bị (song song đường ống). Sử dụng llama.cpp với`-ngl`hoặc ExLlamaV2 với`--num-gpu-layers`.
### Triển khai di động
- **Android**: Sử dụng llama.cpp thông qua liên kết JNI hoặc ML Kit.
- **iOS**: Sử dụng llama.cpp thông qua liên kết Swift hoặc mlx.
- **Web**: Sử dụng WebLLM (chạy trên WebGPU thông qua thời gian chạy ONNX) hoặc Transforms.js.
---

## Tối ưu hóa hiệu suất
### Chú ý chớp nhoáng
Tăng tốc độ tính toán chú ý và giảm mức sử dụng bộ nhớ. Có sẵn trong thư viện llama.cpp, ExLlamaV2 và máy biến áp hiện đại.
### Suy luận hàng loạt
Xử lý nhiều lời nhắc trong một lần chuyển tiếp. Tăng thông lượng đáng kể. Sử dụng`llama-batch`hoặc vLLM.
### Dừng sớm / Lập ngân sách mã thông báo
Đặt ngân sách mã thông báo tối đa để ngăn chặn việc tạo không giới hạn.
### Giải mã suy đoán
Sử dụng mô hình nhanh nhỏ (bản nháp) để dự đoán mã thông báo, sau đó xác minh song song với mô hình lớn. Có thể tăng tốc 2–3×.
---

## Hướng dẫn thiết lập thực tế
### 1. Cài đặt Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Kéo mô hình
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Chạy bằng API
```bash
ollama serve
```

Sau đó gửi yêu cầu đến `http://localhost:11434/api/generate`.
### 4. Tích hợp Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Thay thế) Sử dụng trực tiếp llama.cpp
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Giám sát và quan sát
- Theo dõi việc sử dụng GPU (`nvidia-smi`trên Linux, Giám sát hoạt động trên macOS).
- Theo dõi việc sử dụng bộ nhớ (RAM và VRAM).
- Theo dõi mã thông báo mỗi giây (thông lượng).
- Theo dõi thời gian tới token đầu tiên (độ trễ).
- Sử dụng tính năng ghi nhật ký tích hợp từ llama.cpp hoặc Ollama.
---

## Hạn chế và đánh đổi
- **Khoảng cách chất lượng**: Các mô hình cục bộ nhỏ (3,8B–7B) thường hoạt động kém hơn các mô hình đám mây lớn (GPT-4, Claude 3.5) về lý luận phức tạp.
- **Mức cắt kiến ​​thức**: Kiến thức mô hình bị đóng băng trong thời gian đào tạo; sử dụng RAG để đưa thông tin hiện tại vào.
- **Đa ngôn ngữ**: Các mẫu máy nhỏ hơn có thể có ít khả năng đa ngôn ngữ hơn.
- **Sử dụng công cụ**: Quy trình công việc tác nhân (gọi hàm) có thể kém tin cậy hơn trên các mô hình nhỏ.
Đối với nhiều công việc hàng ngày (tóm tắt, hỏi đáp, hoàn thành mã, phân loại), các mô hình cục bộ đã đủ và đang được cải thiện nhanh chóng.