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
| FP32 | 4 | ~15 GB | ~28GB | ~52 GB | ~280 GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26 GB | ~140 GB |
| INT8 (8-bit) | 1 | ~3,8 GB | ~7GB | ~13 GB | ~70 GB |
| INT4 (4-bit) | 0,5 | ~1,9 GB | ~3,5 GB | ~6,5 GB | ~35GB |

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

### CPU
- Để xử lý nhanh chóng (điền trước) và giảm tải CPU, CPU đa lõi hiện đại sẽ trợ giúp.
- Chip Apple M-series có hiệu năng tuyệt vời dành cho LLM nhờ bộ nhớ hợp nhất và Neural Engine.

---

## Lượng tử hóa

Lượng tử hóa làm giảm độ chính xác về số của trọng lượng, cắt giảm đáng kể bộ nhớ và tăng tốc độ với chi phí chính xác nhỏ.

### Các định dạng phổ biến

| Định dạng | Bit | Mô tả | Sử dụng điển hình |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp, được tối ưu hóa cho kết hợp CPU/GPU | Tốt nhất cho suy luận địa phương |
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

**Lệnh ví dụ:**
giảm giá ```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)

Ollama
Wraps llama.cpp with a simple CLI and REST API.

Auto-downloads models, manages them.

Great for prototyping and desktop apps.

Supports custom Modelfiles for system prompts.

Usage:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Graphical desktop app for Windows, macOS, Linux.

One-click download and chat interface.

Built-in local server with OpenAI-compatible API.

Good for non-technical users and quick testing.

Hugging Face Transformers + bitsandbytes
The standard Python library for HF models.

Use bitsandbytes for 4-bit quantisation (load_in_4bit=True).

More flexible for fine-tuning but slower than llama.cpp for inference.

ExLlamaV2
Very fast GPU inference for GPTQ and AWQ.

Best performance on NVIDIA GPUs.

Supports batched generation.

mlx (Apple)
Apple's framework for M-series chips.

Highly optimised for Apple Silicon.

Python API.

Memory Management
Context Window and KV Cache
The KV cache stores key-value pairs for every layer and every token in the context. It grows linearly with context length.

Memory cost ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

For a 32-layer model with 8 KV heads and 128 head dim, each token costs ~32 × 8 × 128 × 2 bytes = 65 KB per token. For 128k tokens, that's ~8 GB just for the cache.

Offloading Strategies
Layer offloading: Put some layers on GPU, others on CPU. Faster than pure CPU, lower VRAM requirement.

Token streaming: Process tokens incrementally rather than all at once.

Prompt Caching
Reuse KV caches across similar prompts to avoid recomputing the prefill phase. Some frameworks support this (e.g., vLLM, llama.cpp with --prompt-cache).

Memory-Mapped Files
Load model weights directly from disk without loading them entirely into RAM (useful for huge models on memory-limited systems). llama.cpp uses memory-mapping by default.

Deployment Architectures
Single-Device Mode
One model runs on one machine (laptop, smartphone, edge device). Used for personal assistants, note-taking apps, code completion.

Hybrid Edge-Cloud
Local model handles common queries; fallback to a cloud model for complex questions. This gives the best of both worlds — speed/private for most, capability for edge cases.

Distributed Inference (Multi-GPU)
For larger models, split layers across multiple GPUs (tensor parallelism) or split context across devices (pipeline parallelism). Use llama.cpp with -ngl or ExLlamaV2 with --num-gpu-layers.

Mobile Deployment
Android: Use llama.cpp via JNI bindings or ML Kit.

iOS: Use llama.cpp via Swift bindings or mlx.

Web: Use WebLLM (runs on WebGPU via ONNX runtime) or transformers.js.

Performance Optimisation
Flash Attention
Speeds up attention computation and reduces memory usage. Available in llama.cpp, ExLlamaV2, and modern transformers libraries.

Batch Inference
Process multiple prompts in a single forward pass. Increases throughput dramatically. Use llama-batch or vLLM.

Early Stopping / Token Budgeting
Set a maximum token budget to prevent unbounded generation.

Speculative Decoding
Use a small fast model (draft) to predict tokens, then verify with the large model in parallel. Can yield 2–3× speedup.

Practical Setup Guide
1. Install Ollama
bash
curl -fsSL https://ollama.com/install.sh | sh
2. Pull a Model
bash
ollama pull phi3:3.8b-q4_K_M
3. Run with API
bash
ollama serve
Then send requests to http://localhost:11434/api/generate.

4. Python Integration
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Alternative) Use llama.cpp directly
bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
Monitoring and Observability
Track GPU utilisation (nvidia-smi on Linux, Activity Monitor on macOS).

Track memory usage (RAM and VRAM).

Track tokens per second (throughput).

Track time to first token (latency).

Use built-in logging from llama.cpp or Ollama.

Limitations and Tradeoffs
Quality gap: Small local models (3.8B–7B) generally underperform large cloud models (GPT-4, Claude 3.5) on complex reasoning.

Knowledge cutoff: Model knowledge is frozen at training time; use RAG to inject current information.

Multilingual: Smaller models may have less multilingual capability.

Tool use: Agentic workflows (function calling) may be less reliable on small models.

For many everyday tasks (summarisation, Q&A, code completion, classification), local models are already sufficient and improving rapidly.

text

---

## File 4: `security_best_practices.md`

```
# Thực tiễn tốt nhất về bảo mật

Hướng dẫn thực tế để bảo mật ứng dụng, cơ sở hạ tầng và dữ liệu — từ quá trình phát triển đến sản xuất.

---

## OWASP Top 10 (2021) — Tổng quan

1. **Kiểm soát truy cập bị hỏng**: Người dùng có thể truy cập các tài nguyên mà họ không nên truy cập.
2. **Lỗi về mật mã**: Mã hóa yếu hoặc bị thiếu.
3. **Tiêm**: SQL, NoSQL, lệnh OS hoặc chèn LDAP.
4. **Thiết kế không an toàn**: Lỗi kiến ​​trúc.
5. **Cấu hình sai bảo mật**: Mật khẩu mặc định, cổng mở, lỗi dài dòng.
6. **Các thành phần dễ bị tổn thương và lỗi thời**: Các CVE đã biết trong các phần phụ thuộc.
7. **Lỗi nhận dạng và xác thực**: Mật khẩu yếu, quản lý phiên kém.
8. **Lỗi về tính toàn vẹn của phần mềm và dữ liệu**: Tấn công chuỗi cung ứng, cập nhật không dấu.
9. **Lỗi giám sát và ghi nhật ký bảo mật**: Không phát hiện thấy vi phạm.
10. **Giả mạo yêu cầu phía máy chủ (SSRF)**: Lạm dụng máy chủ để thực hiện yêu cầu đến hệ thống nội bộ.

---

## Xác thực đầu vào và mã hóa đầu ra

### Quy tắc xác thực
- **Danh sách trắng > Danh sách đen**: Xác định các mẫu được phép (ví dụ: biểu thức chính quy cho email) thay vì chặn các mẫu xấu đã biết.
- **Giới hạn độ dài**: Thực thi độ dài tối đa để tránh tràn bộ đệm và DoS.
- **Kiểm tra kiểu**: Đảm bảo số nguyên là số nguyên, boolean là boolean.
- **Sử dụng các thư viện đã được kiểm tra kỹ**: Để xác thực email, URL và ngày, hãy sử dụng các thư viện tiêu chuẩn (ví dụ: `email-validator` trong Python, `validator.js` trong Node).

### Mã hóa đầu ra
- **Mã hóa HTML**: Mã hóa `<`, `>`, `&`, `"`, `'` để ngăn chặn XSS.
- **Tham số hóa SQL**: Không bao giờ ghép dữ liệu đầu vào của người dùng vào các truy vấn SQL. Sử dụng các truy vấn được tham số hóa (các câu lệnh đã chuẩn bị sẵn) hoặc ORM.
- **Thoát Shell**: Tránh xây dựng các lệnh shell từ đầu vào của người dùng; nếu không thể tránh khỏi, hãy sử dụng `shlex.quote()` hoặc tương tự.

---

## Xác thực và ủy quyền

### Quản lý mật khẩu
- **Băm**: Lưu trữ mật khẩu bằng thuật toán băm mạnh, chậm: **Argon2id** (ưu tiên), **bcrypt**, **scrypt** hoặc **PBKDF2**.
- **Muối**: Thêm loại muối duy nhất cho mỗi người dùng.
- **Độ dài tối thiểu**: Thực thi ít nhất 12–16 ký tự.
- **MFA (Xác thực đa yếu tố)**: Yêu cầu yếu tố thứ hai (TOTP, SMS, khóa phần cứng) cho các hoạt động nhạy cảm.
- **Giới hạn tỷ lệ**: Ngăn chặn các nỗ lực bạo lực trên các điểm cuối đăng nhập (ví dụ: 5 lần thử mỗi 5 phút cho mỗi IP/người dùng).

### Quản lý phiên
- Sử dụng cookie SameSite, an toàn, chỉ HTTP cho mã thông báo phiên.
- Đặt thời gian hết hạn thích hợp.
- Vô hiệu hóa các phiên đăng xuất và thay đổi mật khẩu.
- Tránh để lộ ID phiên trong URL.

### OAuth2 / OIDC
- Sử dụng các thư viện được thiết lập tốt (ví dụ: Authlib, PyJWT, Passport.js, Spring Security).
- Xác thực mã thông báo ID một cách kỹ lưỡng (chữ ký, nhà phát hành, đối tượng, ngày hết hạn).
- Sử dụng các tham số trạng thái để ngăn chặn CSRF.
- Giữ bí mật bí mật của khách hàng.

### JWT (Mã thông báo web JSON)
- **Ký**: Sử dụng RS256 hoặc ES256 (không đối xứng) để bảo mật tốt hơn; HS256 (đối xứng) có thể chấp nhận được nếu các bí mật chung được quản lý tốt.
- **Xác thực**: Luôn xác minh chữ ký, nhà phát hành (`iss`), đối tượng (`aud`) và ngày hết hạn (`exp`).
- **Giữ hết hạn ngắn**: 15–60 phút đối với mã thông báo truy cập; sử dụng mã thông báo làm mới cho các phiên dài hơn.
- **Lưu trữ an toàn**: Không bao giờ lưu trữ JWT trong localStorage (dễ bị XSS); thay vào đó hãy sử dụng cookie chỉ HTTP.

---

## Bảo mật API

### Xác thực
- Luôn xác thực các lệnh gọi API (ngoại trừ các điểm cuối công khai).
- Ưu tiên khóa API hoặc mã thông báo OAuth2 hơn xác thực cơ bản (gửi thông tin xác thực theo mọi yêu cầu).

### Giới hạn và điều chỉnh tỷ lệ
- Áp dụng giới hạn tốc độ cho mỗi người dùng và mỗi IP để ngăn chặn lạm dụng và DoS.
- Trả về `429 Too Many Requests` với tiêu đề `Retry-After`.

### CORS (Chia sẻ tài nguyên nhiều nguồn gốc)
- Chỉ cho phép xuất xứ cụ thể (không bao giờ `*` trong sản xuất).
- Xác thực tiêu đề `Origin` ở phía máy chủ.

### Xác thực đầu vào
- Xác thực tất cả các tham số yêu cầu, bao gồm tiêu đề và nội dung.
- Từ chối các trường không mong muốn (`"strict": true` hoặc `additionalProperties: false` trong Lược đồ JSON).

### HTTPS / TLS
- Thực thi HTTPS trong sản xuất.
- Sử dụng HSTS (HTTP Strict Transport Security) để buộc trình duyệt sử dụng HTTPS.
- Sử dụng TLS 1.2 hoặc 1.3 (tắt TLS 1.0/1.1).

---

## Quản lý bí mật

### Không bao giờ có bí mật về mã cứng
- Không cam kết bí mật (khóa API, mật khẩu, URL cơ sở dữ liệu) để kiểm soát nguồn.
- Sử dụng các biến môi trường hoặc các công cụ quản lý bí mật.

### Công cụ
- **HashiCorp Vault**: Bí mật động, cấp doanh nghiệp.
- **Trình quản lý bí mật AWS / Azure Key Vault / Trình quản lý bí mật GCP**: Bản địa trên nền tảng đám mây.
- **SOPS**: Mã hóa bí mật trong tệp và xác nhận chúng (với KMS hoặc GPG).
- **Bí mật của Docker**: Dành cho chế độ Swarm; Bí mật Kubernetes (được mã hóa base64, nhưng hãy cẩn thận khi sử dụng; hãy xem xét trình điều khiển CSI của Secrets Store bên ngoài).

### Xoay
- Thường xuyên luân chuyển bí mật và tài khoản dịch vụ.
- Tự động xoay nếu có thể.

---

## Quản lý phụ thuộc

### Quét lỗ hổng
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Nút**: `npm audit`, `yarn audit`, `snyk`.
- **Rỉ sét**: `cargo audit`.
- **Đi**: `govulncheck`.
- **Chung**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Đang vá lỗi
- Luôn cập nhật các phần phụ thuộc lên các phiên bản được vá.
- Thiết lập các yêu cầu kéo tự động cho các cập nhật nhỏ/bản vá.
- Xem lại nhật ký thay đổi để tìm những thay đổi vi phạm.

### Tính toàn vẹn của chuỗi cung ứng
- Sử dụng các tệp khóa gói (`package-lock.json`, `Cargo.lock`, `go.sum`) để đảm bảo các bản dựng có thể tái tạo.
- Xác minh tổng kiểm tra các phụ thuộc đã tải xuống.
- Ưu tiên các cơ quan đăng ký chính thức và chỉ tin tưởng các nhà xuất bản đã được xác minh.

---

## An ninh cơ sở hạ tầng

### Tường lửa
- Chặn tất cả các cổng vào ngoại trừ những cổng thực sự cần thiết (ví dụ: 80, 443).
- Giới hạn quyền truy cập SSH vào các dải IP cụ thể (hoặc sử dụng máy chủ VPN/pháo đài).
- Sử dụng nhóm bảo mật (AWS) hoặc NSG (Azure) để kiểm soát chi tiết.

### Tăng cường hệ điều hành
- Áp dụng các bản cập nhật bảo mật thường xuyên (`sudo apt upgrade`, `yum update`).
- Vô hiệu hóa các dịch vụ không cần thiết và tài khoản mặc định.
- Sử dụng Fail2ban để chặn các nỗ lực bạo lực trên SSH.
- Harden SSH: vô hiệu hóa đăng nhập root, sử dụng xác thực dựa trên khóa, thay đổi cổng mặc định (tùy chọn).

### Phân đoạn mạng
- Đặt cơ sở dữ liệu và bộ nhớ đệm trong các mạng con riêng tư không có quyền truy cập internet.
- Sử dụng DMZ cho các dịch vụ công cộng.
- Áp dụng nguyên tắc đặc quyền tối thiểu trong truy cập mạng.

### Bí mật về cơ sở hạ tầng
- Không bao giờ lưu trữ bí mật trong các biến môi trường CI/CD trừ khi được mã hóa.
- Sử dụng vai trò IAM của nhà cung cấp đám mây cho các phiên bản EC2/VM thay vì các khóa tồn tại lâu dài.

---

## Ghi nhật ký và giám sát

### Đăng nhập những gì
- Sự kiện xác thực (thành công/thất bại).
- Quyết định kiểm soát truy cập (lỗi ủy quyền).
- Hành động của quản trị viên (tạo, xóa người dùng, thay đổi quyền).
- Thay đổi lược đồ cơ sở dữ liệu.
- Lỗi hệ thống và ngoại lệ.
- Yêu cầu và phản hồi API (xử lý lại dữ liệu nhạy cảm).

### Những gì không được đăng nhập
- Mật khẩu, bí mật, mã thông báo, PII (Thông tin nhận dạng cá nhân) trừ khi được băm/tái cấu trúc.
- Số thẻ tín dụng đầy đủ.

### Cảnh báo
- Thiết lập cảnh báo cho:
  - Nhiều lần đăng nhập không thành công (tiềm năng bạo lực).
  - Kiểu truy cập bất thường (ví dụ: từ vị trí mới, vào giờ lẻ).
  - Tài khoản quản trị viên mới được tạo.
  - Tỷ lệ lỗi cao hoặc độ trễ tăng đột biến.
- Sử dụng SIEM (Quản lý sự kiện và thông tin bảo mật) để có mối tương quan nâng cao.

### Lưu giữ nhật ký
- Lưu giữ nhật ký trong ít nhất 30–90 ngày tùy theo yêu cầu quy định.
- Lưu trữ nhật ký trong một hệ thống tập trung, chống giả mạo (ví dụ: ELK Stack, Splunk, Datadog).

---

## Vòng đời phát triển an toàn (SDL)

1. **Đào tạo**: Đảm bảo các nhà phát triển hiểu được các lỗ hổng phổ biến.
2. **Mô hình hóa mối đe dọa**: Xác định sớm các mối đe dọa tiềm ẩn trong thiết kế.
3. **Tiêu chuẩn mã hóa an toàn**: Thực thi thông qua các danh sách kiểm tra đánh giá mã và linters.
4. **SAST** (Kiểm tra bảo mật ứng dụng tĩnh): Quét mã nguồn để tìm lỗ hổng (SonarQube, CodeQL).
5. **DAST** (Kiểm tra bảo mật ứng dụng động): Quét các ứng dụng đang chạy (OWASP ZAP, Burp Suite).
6. **SCA** (Phân tích thành phần phần mềm): Quét các phần phụ thuộc.
7. **Thử nghiệm thâm nhập**: Các bài tập hack có đạo đức thường xuyên.
8. **Tiền thưởng phát hiện lỗi**: Khuyến khích các nhà nghiên cứu bên ngoài tìm ra các lỗ hổng một cách có trách nhiệm.
9. **Kế hoạch ứng phó sự cố**: Có kế hoạch rõ ràng khi phát hiện vi phạm.

---

## Danh sách kiểm tra khẩn cấp (Khi nghi ngờ có vi phạm)

1. **Đừng hoảng sợ** — mà hãy hành động nhanh chóng.
2. **Cô lập** các hệ thống bị ảnh hưởng (ngắt kết nối mạng nếu cần).
3. **Lưu giữ bằng chứng**: Ghi lại nhật ký, kết xuất bộ nhớ và ảnh đĩa.
4. **Xác định** phạm vi: hệ thống nào, dữ liệu nào.
5. **Xoay vòng** tất cả thông tin xác thực và bí mật bị xâm phạm.
6. **Vá** lỗ hổng.
7. **Thông báo** cho người dùng và cơ quan quản lý bị ảnh hưởng nếu được yêu cầu (trong khung thời gian pháp lý).
8. **Tiến hành khám nghiệm tử thi** để hiểu nguyên nhân cốt lõi và cải thiện quy trình.