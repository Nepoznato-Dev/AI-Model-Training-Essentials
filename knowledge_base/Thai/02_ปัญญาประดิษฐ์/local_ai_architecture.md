# สถาปัตยกรรม AI ท้องถิ่น

คำแนะนำที่เป็นประโยชน์ในการใช้งานโมเดลภาษาขนาดใหญ่บนอุปกรณ์ทั้งหมด - ข้อควรพิจารณาด้านฮาร์ดแวร์ กลไกการอนุมาน การเพิ่มประสิทธิภาพหน่วยความจำ และการออกแบบระบบสำหรับการใช้งาน Edge

---

## ทำไมต้องใช้ AI ในพื้นที่?

- **ความเป็นส่วนตัว**: ไม่มีข้อมูลออกจากอุปกรณ์
- **ค่าใช้จ่าย**: ไม่มีค่าธรรมเนียม API ต่อโทเค็น
- **เวลาแฝง**: การอนุมานแบบไร้เครือข่ายที่คาดการณ์ได้
- **ความพร้อมใช้งานออฟไลน์**: ทำงานโดยไม่ใช้อินเทอร์เน็ต
- **การควบคุม**: ควบคุมเวอร์ชันของโมเดล การปรับแต่ง และการปรับแต่งได้อย่างสมบูรณ์

---

## ข้อกำหนดด้านฮาร์ดแวร์

### หน่วยความจำ GPU (VRAM)
ทรัพยากรที่สำคัญที่สุด ขนาดโมเดลในหน่วยความจำ γ **พารามิเตอร์ × ไบต์ต่อพารามิเตอร์**

| ความแม่นยำ | ไบต์ต่อพารามิเตอร์ | รุ่น 3.8B | รุ่น 7B | รุ่น 13B | รุ่น 70B |
|----------|---------------------|------------|----------|-----------|-----------|
| FP32 | 4 | ~15GB | ~28GB | ~52GB | ~280GB |
| FP16 | 2 | ~7.6GB | ~14GB | ~26GB | ~140GB |
| INT8 (8 บิต) | 1 | ~3.8GB | ~7GB | ~13GB | ~70GB |
| INT4 (4 บิต) | 0.5 | ~1.9GB | ~3.5GB | ~6.5GB | ~35GB |

**แนวทางปฏิบัติ:**
- 8GB VRAM → สูงสุด 7B รุ่น 4 บิต
- 12GB VRAM → สูงสุด 13B รุ่น 4 บิต
- 24GB VRAM → สูงสุดรุ่น 70B ที่ 4 บิต (หรือ 13B ที่ 8 บิต)
- Apple Silicon (หน่วยความจำแบบรวม) สามารถเรียกใช้รุ่น 70B บนระบบ 64GB+

### RAM (หน่วยความจำระบบ)
- สำหรับการอนุมาน CPU คุณต้องมี RAM ระบบเพียงพอที่จะโหลดโมเดล (คล้ายกับหมายเลข VRAM)
- สำหรับการอนุมาน GPU RAM ของระบบมีความสำคัญต่อการโหลดโมเดลลงในหน่วยความจำก่อนที่จะออฟโหลดไปยัง VRAM

### ที่เก็บข้อมูล
- น้ำหนักโมเดลเชิงปริมาณใช้พื้นที่ไม่กี่ GB (เช่น 7B 4 บิต 4 บิตบนดิสก์) ตรวจสอบให้แน่ใจว่ามีพื้นที่ว่างอย่างน้อย 20–50 GB สำหรับหลายรุ่น

### ซีพียู
- สำหรับการประมวลผลที่รวดเร็ว (เติมล่วงหน้า) และการถ่าย CPU CPU แบบมัลติคอร์ที่ทันสมัยจะช่วยได้
- ชิป Apple M-series มีประสิทธิภาพที่ยอดเยี่ยมสำหรับ LLM เนื่องจากมีหน่วยความจำแบบรวมและ Neural Engine

---

## ปริมาณ

การหาปริมาณจะลดความแม่นยำเชิงตัวเลขของตุ้มน้ำหนัก ลดหน่วยความจำลงอย่างมาก และเพิ่มความเร็วด้วยต้นทุนความแม่นยำเพียงเล็กน้อย

### รูปแบบยอดนิยม

| รูปแบบ | บิต | คำอธิบาย | การใช้งานทั่วไป |
|--------|-|-------------|-------------|
| **กุกฟ์** | 4–8 | รูปแบบ llama.cpp ปรับให้เหมาะสมสำหรับ CPU/GPU ไฮบริด | ดีที่สุดสำหรับการอนุมานเฉพาะที่ |
| **GPTQ** | 4–8 | GPU เท่านั้น มีประสิทธิภาพบน CUDA | ดีที่สุดสำหรับ NVIDIA GPU |
| **AWQ** | 4 | การรับรู้การเปิดใช้งาน GPU เท่านั้น | เหมาะสำหรับการอนุมานแบบแบตช์บน GPU |
| **ONNX** | ตัวแปร | ข้ามแพลตฟอร์มที่ได้มาตรฐาน | ให้บริการด้านการผลิต |

### การเลือกระดับปริมาณ
- **Q8_0** (8 บิต): การสูญเสียคุณภาพน้อยที่สุด, ขนาดที่ใหญ่ที่สุด
- **Q6_K** (6 บิต): คุณภาพดี การบีบอัดที่เหมาะสม
- **Q5_K_M** (5 บิต): จุดหวานทั่วไป
- **Q4_K_M** (4 บิต): เล็กที่สุด คุณภาพที่ยอมรับได้สำหรับงานส่วนใหญ่
- **IQ4_XS** / **IQ3_XS**: ปรับปรุงการหาปริมาณด้วยความฉงนสนเท่ห์ที่ดีขึ้นที่ 4/3 บิต

**หลักทั่วไป:** ใช้ Q4_K_M เพื่อความสมดุลระหว่างคุณภาพและขนาด หากคุณมี VRAM เพิ่มเติม ให้ใช้ Q5 หรือ Q6

---

## เครื่องมืออนุมาน (ท้องถิ่น)

### llama.cpp
- เขียนด้วยภาษา C++
- รองรับรูปแบบ GGUF
- ปรับให้เหมาะสมสำหรับ CPU และ GPU (ผ่าน CUDA, Metal, OpenCL)
- เร็วมาก โดยเฉพาะบน CPU
- บรรทัดคำสั่ง โหมดเซิร์ฟเวอร์ และการเชื่อมโยง Python

**คำสั่งตัวอย่าง:**
```bash
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

```มาร์กดาวน์
# แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย

คู่มือที่เป็นประโยชน์สำหรับการรักษาความปลอดภัยแอปพลิเคชัน โครงสร้างพื้นฐาน และข้อมูล ตั้งแต่การพัฒนาไปจนถึงการใช้งานจริง

---

## OWASP 10 อันดับแรก (2021) — ภาพรวม

1. **การควบคุมการเข้าถึงที่เสียหาย**: ผู้ใช้สามารถเข้าถึงทรัพยากรที่พวกเขาไม่ควร
2. **ความล้มเหลวในการเข้ารหัส**: การเข้ารหัสที่อ่อนแอหรือขาดหายไป
3. **การฉีด**: SQL, NoSQL, คำสั่ง OS หรือการแทรก LDAP
4. **การออกแบบที่ไม่ปลอดภัย**: ข้อบกพร่องทางสถาปัตยกรรม
5. **การกำหนดค่าความปลอดภัยผิดพลาด**: รหัสผ่านเริ่มต้น พอร์ตที่เปิดอยู่ ข้อผิดพลาดโดยละเอียด
6. **ส่วนประกอบที่มีช่องโหว่และล้าสมัย**: CVE ที่รู้จักในการอ้างอิง
7. **ความล้มเหลวในการระบุตัวตนและการตรวจสอบสิทธิ์**: รหัสผ่านที่อ่อนแอ การจัดการเซสชันไม่ถูกต้อง
8. **ความล้มเหลวด้านความสมบูรณ์ของซอฟต์แวร์และข้อมูล**: การโจมตีของห่วงโซ่อุปทาน การอัปเดตที่ไม่ได้ลงนาม
9. **การบันทึกความปลอดภัยและการตรวจสอบความล้มเหลว**: ไม่พบการละเมิด
10. **การปลอมแปลงคำขอฝั่งเซิร์ฟเวอร์ (SSRF)**: การใช้เซิร์ฟเวอร์ในทางที่ผิดเพื่อส่งคำขอไปยังระบบภายใน

---

## การตรวจสอบอินพุตและการเข้ารหัสเอาต์พุต

### กฎการตรวจสอบ
- **บัญชีขาว > บัญชีดำ**: กำหนดรูปแบบที่อนุญาต (เช่น regex สำหรับอีเมล) แทนที่จะบล็อกรูปแบบที่รู้จักที่ไม่ดี
- **ขีดจำกัดความยาว**: บังคับใช้ความยาวสูงสุดเพื่อป้องกันบัฟเฟอร์ล้นและ DoS
- **การตรวจสอบประเภท**: ตรวจสอบให้แน่ใจว่าจำนวนเต็มเป็นจำนวนเต็ม บูลีนคือบูลีน
- **ใช้ไลบรารีที่ผ่านการทดสอบอย่างดี**: สำหรับการตรวจสอบอีเมล, URL และวันที่ ให้ใช้ไลบรารีมาตรฐาน (เช่น `email-validator` ใน Python, `validator.js` ใน Node)### การเข้ารหัสเอาต์พุต
- **การเข้ารหัส HTML**: เข้ารหัส `<`, `>`, `&`, `"`, `'` เพื่อป้องกัน XSS
- **การกำหนดพารามิเตอร์ SQL**: ไม่ต้องเชื่อมอินพุตของผู้ใช้เข้ากับคำสั่ง SQL ใช้แบบสอบถามแบบมีพารามิเตอร์ (คำสั่งที่เตรียมไว้) หรือ ORM
- **การหลบหนีของเชลล์**: หลีกเลี่ยงการสร้างคำสั่งเชลล์จากอินพุตของผู้ใช้ หากหลีกเลี่ยงไม่ได้ ให้ใช้ `shlex.quote()` หรือที่คล้ายกัน

---

## การรับรองความถูกต้องและการอนุญาต

### การจัดการรหัสผ่าน
- **การแฮช**: จัดเก็บรหัสผ่านด้วยอัลกอริธึมการแฮชที่รัดกุมและช้า: **Argon2id** (แนะนำ), **bcrypt**, **scrypt** หรือ **PBKDF2**
- **การเติมเกลือ**: เพิ่มเกลือเฉพาะต่อผู้ใช้
- **ความยาวขั้นต่ำ**: บังคับใช้อักขระอย่างน้อย 12–16 ตัว
- **MFA (การตรวจสอบสิทธิ์แบบหลายปัจจัย)**: ต้องมีปัจจัยที่สอง (TOTP, SMS, คีย์ฮาร์ดแวร์) สำหรับการดำเนินการที่มีความละเอียดอ่อน
- **การจำกัดอัตรา**: ป้องกันความพยายามแบบเดรัจฉานบนปลายทางการเข้าสู่ระบบ (เช่น 5 ครั้งต่อ 5 นาทีต่อ IP/ผู้ใช้)

### การจัดการเซสชัน
- ใช้คุกกี้ SameSite แบบ HTTP เท่านั้นที่ปลอดภัยสำหรับโทเค็นเซสชัน
- ตั้งเวลาหมดอายุให้เหมาะสม
- ทำให้เซสชันใช้งานไม่ได้เมื่อออกจากระบบและเปลี่ยนรหัสผ่าน
- หลีกเลี่ยงการเปิดเผยรหัสเซสชันใน URL

### OAuth2 / OIDC
- ใช้ไลบรารี่ที่มีชื่อเสียง (เช่น Authlib, PyJWT, Passport.js, Spring Security)
- ตรวจสอบโทเค็น ID อย่างละเอียด (ลายเซ็น ผู้ออก ผู้ชม การหมดอายุ)
- ใช้พารามิเตอร์สถานะเพื่อป้องกัน CSRF
- รักษาความลับของลูกค้าเป็นความลับ

### JWT (โทเค็นเว็บ JSON)
- **ลงชื่อ**: ใช้ RS256 หรือ ES256 (ไม่สมมาตร) เพื่อความปลอดภัยที่ดีขึ้น HS256 (สมมาตร) เป็นที่ยอมรับได้หากมีการจัดการความลับร่วมกันอย่างดี
- **ตรวจสอบ**: ตรวจสอบลายเซ็น ผู้ออก (`iss`) ผู้ชม (`aud`) และการหมดอายุ (`exp`) เสมอ
- **ให้หมดอายุสั้น**: 15–60 นาทีสำหรับโทเค็นการเข้าถึง ใช้โทเค็นการรีเฟรชสำหรับเซสชันที่นานขึ้น
- **จัดเก็บอย่างปลอดภัย**: ห้ามจัดเก็บ JWT ใน localStorage (เสี่ยงต่อ XSS) ใช้คุกกี้ HTTP เท่านั้นแทน

---

## ความปลอดภัยของ API

### การรับรองความถูกต้อง
- ตรวจสอบสิทธิ์การเรียก API เสมอ (ยกเว้นจุดสิ้นสุดสาธารณะ)
- ต้องการคีย์ API หรือโทเค็น OAuth2 มากกว่าการตรวจสอบสิทธิ์พื้นฐาน (ซึ่งส่งข้อมูลรับรองในทุกคำขอ)

### การจำกัดอัตราและการควบคุมปริมาณ
- ใช้ขีดจำกัดอัตราต่อผู้ใช้และต่อ IP เพื่อป้องกันการละเมิดและ DoS
- ส่งกลับ `429 Too Many Requests` โดยมีส่วนหัว `Retry-After`

### CORS (การแบ่งปันทรัพยากรข้ามแหล่งกำเนิด)
- อนุญาตเฉพาะต้นทางที่เฉพาะเจาะจงเท่านั้น (ไม่เคย `*` ในการผลิต)
- ตรวจสอบส่วนหัว `Origin` บนฝั่งเซิร์ฟเวอร์

### การตรวจสอบอินพุต
- ตรวจสอบพารามิเตอร์คำขอทั้งหมด รวมถึงส่วนหัวและเนื้อหา
- ปฏิเสธฟิลด์ที่ไม่คาดคิด (`"strict": true` หรือ `additionalProperties: false` ใน JSON Schema)

### HTTPS / TLS
- บังคับใช้ HTTPS ในการผลิต
- ใช้ HSTS (HTTP Strict Transport Security) เพื่อบังคับให้เบราว์เซอร์ใช้ HTTPS
- ใช้ TLS 1.2 หรือ 1.3 (ปิดใช้งาน TLS 1.0/1.1)

---

## การจัดการความลับ

### ไม่เคยมีความลับแบบ Hardcode
- ห้ามส่งข้อมูลลับ (คีย์ API, รหัสผ่าน, URL ของฐานข้อมูล) ให้กับการควบคุมแหล่งที่มา
- ใช้ตัวแปรสภาพแวดล้อมหรือเครื่องมือการจัดการความลับ

### เครื่องมือ
- **HashiCorp Vault**: ข้อมูลลับแบบไดนามิกระดับองค์กร
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: บนคลาวด์
- **SOPS**: เข้ารหัสความลับในไฟล์และส่งข้อมูลเหล่านั้น (ด้วย KMS หรือ GPG)
- **ความลับนักเทียบท่า**: สำหรับโหมด Swarm; ข้อมูลลับของ Kubernetes (เข้ารหัส base64 แต่ใช้ด้วยความระมัดระวัง โปรดพิจารณาไดรเวอร์ Secrets Store CSI ภายนอก)

### การหมุน
- หมุนเวียนข้อมูลลับและบัญชีบริการเป็นประจำ
- หมุนอัตโนมัติเมื่อเป็นไปได้

---

## การจัดการการพึ่งพา

### การสแกนช่องโหว่
- **หลาม**: `safety`, `pip-audit`, `bandit`.
- **โหนด**: `npm audit`, `yarn audit`, `snyk`.
- **สนิม**: `cargo audit`.
- **ไป**: `govulncheck`.
- **ทั่วไป**: `Dependabot` (GitHub), `Renovate`, `Trivy`

### กำลังแพตช์
- อัปเดตการพึ่งพาให้เป็นเวอร์ชันที่มีแพตช์
- ตั้งค่าคำขอดึงข้อมูลอัตโนมัติสำหรับการอัพเดตรอง/แพตช์
- ตรวจสอบบันทึกการเปลี่ยนแปลงเพื่อทำลายการเปลี่ยนแปลง

### ความซื่อสัตย์ในห่วงโซ่อุปทาน
- ใช้ไฟล์ล็อคแพ็คเกจ (`package-lock.json`, `Cargo.lock`, `go.sum`) เพื่อให้แน่ใจว่าสร้างซ้ำได้
- ตรวจสอบการตรวจสอบการพึ่งพาที่ดาวน์โหลด
- ต้องการการลงทะเบียนอย่างเป็นทางการและไว้วางใจเฉพาะผู้เผยแพร่ที่ได้รับการยืนยันเท่านั้น

---

## การรักษาความปลอดภัยโครงสร้างพื้นฐาน

### ไฟร์วอลล์
- บล็อกพอร์ตขาเข้าทั้งหมด ยกเว้นพอร์ตที่จำเป็นอย่างชัดเจน (เช่น 80, 443)
- จำกัดการเข้าถึง SSH ในช่วง IP เฉพาะ (หรือใช้โฮสต์ VPN/ป้อมปราการ)
- ใช้กลุ่มความปลอดภัย (AWS) หรือ NSG (Azure) เพื่อการควบคุมแบบละเอียด

### OS แข็งตัว
- ใช้การอัปเดตความปลอดภัยเป็นประจำ (`sudo apt upgrade`, `yum update`)
- ปิดการใช้งานบริการที่ไม่จำเป็นและบัญชีเริ่มต้น
- ใช้ Fail2ban เพื่อป้องกันความพยายามแบบเดรัจฉานใน SSH
- Harden SSH: ปิดการใช้งานการเข้าสู่ระบบรูท, ใช้การตรวจสอบสิทธิ์แบบใช้คีย์, เปลี่ยนพอร์ตเริ่มต้น (ตัวเลือก)### การแบ่งส่วนเครือข่าย
- วางฐานข้อมูลและแคชในซับเน็ตส่วนตัวโดยไม่ต้องเชื่อมต่ออินเทอร์เน็ต
- ใช้ DMZ สำหรับบริการสาธารณะ
- ใช้หลักการสิทธิพิเศษน้อยที่สุดในการเข้าถึงเครือข่าย

### ความลับในโครงสร้างพื้นฐาน
- ห้ามเก็บความลับไว้ในตัวแปรสภาพแวดล้อม CI/CD เว้นแต่จะมีการเข้ารหัส
- ใช้บทบาท IAM ของผู้ให้บริการคลาวด์สำหรับอินสแตนซ์ EC2/VM แทนคีย์ที่มีอายุการใช้งานยาวนาน

---

## การบันทึกและการตรวจสอบ

### สิ่งที่ต้องบันทึก
- เหตุการณ์การรับรองความถูกต้อง (สำเร็จ/ล้มเหลว)
- การตัดสินใจควบคุมการเข้าถึง (ความล้มเหลวในการอนุญาต)
- การดำเนินการของผู้ดูแลระบบ (การสร้างผู้ใช้ การลบ การเปลี่ยนแปลงสิทธิ์)
- การเปลี่ยนแปลงสคีมาฐานข้อมูล
- ข้อผิดพลาดและข้อยกเว้นของระบบ
- คำขอและการตอบกลับ API (แก้ไขข้อมูลที่ละเอียดอ่อน)

### สิ่งที่ไม่ควรบันทึก
- รหัสผ่าน ความลับ โทเค็น PII (ข้อมูลที่สามารถระบุตัวบุคคลได้) เว้นแต่จะมีการแฮช/แก้ไข
- หมายเลขบัตรเครดิตครบถ้วน

### การแจ้งเตือน
- ตั้งค่าการแจ้งเตือนสำหรับ:
  - การเข้าสู่ระบบล้มเหลวหลายครั้ง (อาจใช้กำลังดุร้าย)
  - รูปแบบการเข้าถึงที่ผิดปกติ (เช่น จากสถานที่ใหม่ ในเวลาคี่)
  - สร้างบัญชีผู้ดูแลระบบใหม่แล้ว
  - อัตราข้อผิดพลาดสูงหรือความล่าช้าที่เพิ่มขึ้นอย่างรวดเร็ว
- ใช้ SIEM (ข้อมูลความปลอดภัยและการจัดการเหตุการณ์) เพื่อความสัมพันธ์ขั้นสูง

### การเก็บรักษาบันทึก
- เก็บรักษาบันทึกเป็นเวลาอย่างน้อย 30–90 วัน ขึ้นอยู่กับข้อกำหนดด้านกฎระเบียบ
- จัดเก็บบันทึกในระบบที่รวมศูนย์และชัดเจน (เช่น ELK Stack, Splunk, Datadog)

---

## วงจรการพัฒนาที่ปลอดภัย (SDL)

1. **การฝึกอบรม**: ตรวจสอบให้แน่ใจว่านักพัฒนาเข้าใจช่องโหว่ทั่วไป
2. **การสร้างแบบจำลองภัยคุกคาม**: ระบุภัยคุกคามที่อาจเกิดขึ้นตั้งแต่เนิ่นๆ ในการออกแบบ
3. **มาตรฐานการเข้ารหัสที่ปลอดภัย**: บังคับใช้ผ่าน linters และรายการตรวจสอบการตรวจสอบโค้ด
4. **SAST** (การทดสอบความปลอดภัยของแอปพลิเคชันแบบคงที่): สแกนซอร์สโค้ดเพื่อหาช่องโหว่ (SonarQube, CodeQL)
5. **DAST** (การทดสอบความปลอดภัยของแอปพลิเคชันแบบไดนามิก): สแกนแอปพลิเคชันที่ทำงานอยู่ (OWASP ZAP, Burp Suite)
6. **SCA** (การวิเคราะห์องค์ประกอบของซอฟต์แวร์): สแกนการอ้างอิง
7. **การทดสอบการเจาะระบบ**: แบบฝึกหัดการแฮ็กอย่างมีจริยธรรมเป็นประจำ
8. **รางวัลบั๊ก**: ส่งเสริมให้นักวิจัยภายนอกค้นหาช่องโหว่อย่างมีความรับผิดชอบ
9. **แผนการตอบสนองต่อเหตุการณ์**: มีแผนที่ชัดเจนเมื่อตรวจพบการละเมิด

---

## รายการตรวจสอบฉุกเฉิน (เมื่อสงสัยว่ามีการละเมิด)

1. **อย่าตกใจ** — แต่ให้ดำเนินการอย่างรวดเร็ว
2. **แยก** ระบบที่ได้รับผลกระทบ (ตัดการเชื่อมต่อจากเครือข่ายหากจำเป็น)
3. **เก็บหลักฐาน**: บันทึกบันทึก ดัมพ์หน่วยความจำ และอิมเมจของดิสก์
4. **ระบุ** ขอบเขต: ระบบไหน ข้อมูลไหน
5. **หมุนเวียน** ข้อมูลประจำตัวและความลับที่ถูกบุกรุกทั้งหมด
6. **แก้ไข** ช่องโหว่
7. **แจ้ง** ผู้ใช้ที่ได้รับผลกระทบและหน่วยงานกำกับดูแลหากจำเป็น (ภายในกรอบเวลาทางกฎหมาย)
8. **ดำเนินการชันสูตรศพ** เพื่อทำความเข้าใจสาเหตุที่แท้จริงและปรับปรุงกระบวนการ