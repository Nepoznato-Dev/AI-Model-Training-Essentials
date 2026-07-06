# معماری هوش مصنوعی محلی

راهنمای عملی برای اجرای مدل‌های زبان بزرگ کاملاً روی دستگاه - ملاحظات سخت‌افزاری، موتورهای استنتاج، بهینه‌سازی حافظه و طراحی سیستم برای استقرار لبه.

---

## چرا هوش مصنوعی را به صورت محلی اجرا کنیم؟

- **حریم خصوصی**: هیچ داده ای از دستگاه خارج نمی شود.
- **هزینه**: بدون هزینه API برای هر توکن.
- **تأخیر**: استنتاج قابل پیش بینی و بدون شبکه.
- **در دسترس بودن آفلاین**: بدون اینترنت کار می کند.
- **کنترل**: کنترل کامل بر نسخه مدل، سفارشی سازی و تنظیم دقیق.

---

## الزامات سخت افزاری

### حافظه GPU (VRAM)
بحرانی ترین منبع اندازه مدل در حافظه ≈ **پارامترها × بایت در هر پارامتر**.

| دقت | بایت در هر پارامتر | مدل 3.8B | مدل 7B | مدل 13B | مدل 70B |
|-----------|--------------------|------------|---------|-----------|-----------|
| FP32 | 4 | ~ 15 گیگابایت | ~28 گیگابایت | ~52 گیگابایت | ~280 گیگابایت |
| FP16 | 2 | ~7.6 گیگابایت | ~14 گیگابایت | ~26 گیگابایت | ~140 گیگابایت |
| INT8 (8 بیتی) | 1 | ~3.8 گیگابایت | ~7 گیگابایت | ~13 گیگابایت | ~70 گیگابایت |
| INT4 (4 بیتی) | 0.5 | ~1.9 گیگابایت | ~3.5 گیگابایت | ~6.5 گیگابایت | ~35 گیگابایت |

**دستورالعمل های عملی:**
- 8 گیگابایت VRAM → تا مدل های 7B در 4 بیت.
- 12 گیگابایت VRAM → تا مدل های 13B در 4 بیت.
- 24 گیگابایت VRAM → تا مدل های 70B در 4 بیت (یا 13 بایت در 8 بیت).
- Apple Silicon (حافظه یکپارچه) می تواند مدل های 70B را روی سیستم های 64GB+ اجرا کند.

### رم (حافظه سیستم)
- برای استنتاج CPU، برای بارگذاری مدل به مقدار کافی RAM سیستم نیاز دارید (شبیه به اعداد VRAM).
- برای استنباط GPU، RAM سیستم برای بارگذاری مدل در حافظه قبل از بارگذاری به VRAM اهمیت دارد.

### ذخیره سازی
- وزن های مدل کوانتیزه شده چند گیگابایت را اشغال می کند (مثلاً 4 بیتی 7B ≈ 4 گیگابایتی روی دیسک). حداقل 20 تا 50 گیگابایت رایگان برای چندین مدل مطمئن شوید.

### سی پی یو
- برای پردازش سریع (پیش پر کردن) و تخلیه CPU، یک CPU چند هسته ای مدرن کمک می کند.
- تراشه های سری M اپل به دلیل حافظه یکپارچه و موتور عصبی عملکرد عالی برای LLM ها دارند.

---

## کمی سازی

کوانتیزه کردن دقت عددی وزنه ها را کاهش می دهد، حافظه را به طور چشمگیری کاهش می دهد و سرعت را با هزینه دقت کمی افزایش می دهد.

### فرمت های محبوب

| قالب | بیت | توضیحات | استفاده معمولی |
|--------|------|-------------|-------------|
| **GGUF** | 4-8 | فرمت llama.cpp، بهینه سازی شده برای ترکیبی CPU/GPU | بهترین برای استنتاج محلی |
| **GPTQ** | 4-8 | فقط GPU، کارآمد در CUDA | بهترین برای پردازنده های گرافیکی NVIDIA |
| **AWQ** | 4 | فعال سازی، فقط GPU | خوب برای استنتاج دسته ای در GPU |
| **ONNX** | متغیر | استاندارد، کراس پلتفرم | خدمات تولیدی |

### انتخاب سطح کوانتیزاسیون
- **Q8_0** (8 بیت): حداقل افت کیفیت، بزرگترین اندازه.
- **Q6_K** (6 بیت): کیفیت خوب، فشرده سازی مناسب.
- **Q5_K_M** (5 بیتی): نقطه شیرین رایج.
- **Q4_K_M** (4 بیتی): کوچکترین کیفیت قابل قبول برای اکثر کارها.
- **IQ4_XS** / **IQ3_XS**: کمی سازی بهبود یافته با گیجی بهتر در 4/3 بیت.

**قاعده سرانگشتی:** برای تعادل خوب کیفیت و اندازه از Q4_K_M استفاده کنید. اگر VRAM اضافی دارید، از Q5 یا Q6 استفاده کنید.

---

## موتورهای استنتاج (محلی)

### llama.cpp
- نوشته شده در C++.
- پشتیبانی از فرمت GGUF
- بهینه شده برای CPU و GPU (از طریق CUDA، Metal، OpenCL).
- بسیار سریع، به خصوص در CPU.
- خط فرمان، حالت سرور و اتصالات پایتون.

**فرمان مثال:**
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

```نشانه گذاری
# بهترین شیوه های امنیتی

راهنمای عملی برای ایمن سازی برنامه ها، زیرساخت ها و داده ها - از توسعه تا تولید.

---

## OWASP Top 10 (2021) - نمای کلی

1. **دسترسی شکسته**: کاربران می توانند به منابعی که نباید دسترسی داشته باشند.
2. **شکست های رمزنگاری**: رمزگذاری ضعیف یا گم شده است.
3. **تزریق **: SQL، NoSQL، دستور OS یا تزریق LDAP.
4. **طراحی ناامن**: نقص های معماری.
5. **پیکربندی اشتباه امنیتی**: رمزهای عبور پیش فرض، پورت های باز، خطاهای پرمخاطب.
6. ** مولفه های آسیب پذیر و قدیمی **: CVE های شناخته شده در وابستگی ها.
7. **مشکلات شناسایی و احراز هویت**: رمزهای عبور ضعیف، مدیریت نادرست جلسه.
8. **نقص نرم افزار و یکپارچگی داده**: حملات زنجیره تامین، به روز رسانی بدون امضا.
9. **نقص ثبت و مانیتورینگ امنیتی**: عدم شناسایی نقض.
10. **جعل درخواست سمت سرور (SSRF)**: سوء استفاده از سرور برای درخواست به سیستم های داخلی.

---

## اعتبار سنجی ورودی و کدگذاری خروجی

### قوانین اعتبارسنجی
- **لیست سفید > لیست سیاه**: الگوهای مجاز را تعریف کنید (به عنوان مثال، regex برای ایمیل) به جای مسدود کردن الگوهای بد شناخته شده.
- **محدودیت طول**: حداکثر طول را برای جلوگیری از سرریز بافر و DoS اعمال کنید.
- **بررسی تایپ **: اطمینان حاصل کنید که اعداد صحیح اعداد صحیح هستند، بولی ها بولی هستند.
- **از کتابخانه های آزمایش شده استفاده کنید**: برای اعتبارسنجی ایمیل، URL و تاریخ، از کتابخانه های استاندارد استفاده کنید (به عنوان مثال، `email-validator` در Python، `validator.js` در Node).### کدگذاری خروجی
- **رمزگذاری HTML**: `<`، `>`، `&`، `"`، `'` را برای جلوگیری از XSS کدگذاری کنید.
- **پارامترسازی SQL**: هرگز ورودی کاربر را به کوئری های SQL الحاق نکنید. از پرس و جوهای پارامتری (عبارات آماده شده) یا یک ORM استفاده کنید.
- **شل فرار **: از ساخت دستورات پوسته از ورودی کاربر خودداری کنید. اگر اجتناب ناپذیر است، از `shlex.quote()` یا مشابه استفاده کنید.

---

## احراز هویت و مجوز

### مدیریت رمز عبور
- **Hashing**: رمزهای عبور را با یک الگوریتم هش قوی و آهسته ذخیره کنید: **Argon2id** (ترجیحا)، **bcrypt**، **scrypt**، یا **PBKDF2**.
- **نمکی**: یک نمک منحصر به فرد برای هر کاربر اضافه کنید.
- **حداقل طول**: حداقل 12 تا 16 کاراکتر را اعمال کنید.
- **MFA (Multi-Factor Authentication)**: نیاز به فاکتور دوم (TOTP، SMS، کلید سخت افزاری) برای عملیات حساس.
- **محدود کردن نرخ**: از تلاش های بی رحمانه برای نقاط پایانی ورود به سیستم جلوگیری کنید (مثلاً 5 بار در هر 5 دقیقه برای هر IP/کاربر).

### مدیریت جلسه
- از کوکی های امن، فقط HTTP، SameSite برای نشانه های جلسه استفاده کنید.
- زمان انقضا مناسب را تنظیم کنید.
- جلسات هنگام خروج از سیستم و تغییر رمز عبور را باطل کنید.
- از افشای شناسه های جلسه در URL ها خودداری کنید.

### OAuth2 / OIDC
- از کتابخانه های تثبیت شده (مانند Authlib، PyJWT، Passport.js، Spring Security) استفاده کنید.
- اعتبار شناسه توکن ها (امضا، صادرکننده، مخاطبان، انقضا) را به طور کامل تأیید کنید.
- از پارامترهای حالت برای جلوگیری از CSRF استفاده کنید.
- اسرار مشتری را محرمانه نگه دارید.

### JWT (JSON Web Tokens)
- **نشانه**: برای امنیت بهتر از RS256 یا ES256 (نامتقارن) استفاده کنید. اگر اسرار مشترک به خوبی مدیریت شوند، HS256 (متقارن) قابل قبول است.
- ** اعتبارسنجی **: همیشه امضا، صادرکننده (`iss`)، مخاطبان (`aud`)، و انقضا (`exp`) را تأیید کنید.
- ** انقضا کوتاه نگه دارید **: 15 تا 60 دقیقه برای نشانه های دسترسی. برای جلسات طولانی تر از نشانه های تازه سازی استفاده کنید.
- **ذخیره ایمن**: هرگز JWT ها را در localStorage ذخیره نکنید (در برابر XSS آسیب پذیر است). به جای آن از کوکی های فقط HTTP استفاده کنید.

---

## امنیت API

### احراز هویت
- همیشه تماس های API (به جز نقاط پایانی عمومی) را احراز هویت کنید.
- کلیدهای API یا توکن‌های OAuth2 را به اعتبار پایه ترجیح دهید (که اعتبارنامه‌ها را در هر درخواست ارسال می‌کند).

### محدود کردن و کاهش سرعت
- برای جلوگیری از سوء استفاده و DoS، محدودیت‌های نرخ هر کاربر و هر IP را اعمال کنید.
- `429 Too Many Requests` را با سرصفحه `Retry-After` برگردانید.

### CORS (اشتراک گذاری منابع متقابل)
- فقط مبداهای خاص را مجاز کنید (هرگز `*` در تولید نباشد).
- هدر `Origin` را در سمت سرور تأیید کنید.

### اعتبار سنجی ورودی
- اعتبار تمام پارامترهای درخواست، از جمله هدر و بدنه.
- فیلدهای غیرمنتظره (`"strict": true` یا `additionalProperties: false` در طرحواره JSON) را رد کنید.

### HTTPS / TLS
- اجرای HTTPS در تولید.
- از HSTS (HTTP Strict Transport Security) برای وادار کردن مرورگرها به استفاده از HTTPS استفاده کنید.
- از TLS 1.2 یا 1.3 استفاده کنید (TLS 1.0/1.1 را غیرفعال کنید).

---

## مدیریت اسرار

### هرگز اسرار کد سخت
- اسرار (کلیدهای API، گذرواژه‌ها، آدرس‌های اینترنتی پایگاه داده) را به کنترل منبع متعهد نکنید.
- از متغیرهای محیطی یا ابزارهای مدیریت مخفی استفاده کنید.

### ابزار
- ** HashiCorp Vault **: اسرار پویا، درجه سازمانی.
- ** AWS Secrets Manager / Azure Key Vault / GCP Secret Manager **: Cloud-native.
- **SOPS**: اسرار موجود در فایل ها را رمزگذاری کرده و آنها را متعهد کنید (با KMS یا GPG).
- ** اسرار داکر **: برای حالت Swarm. اسرار Kubernetes (با پایه 64 رمزگذاری شده است، اما با احتیاط استفاده کنید؛ درایور خارجی Secrets Store CSI را در نظر بگیرید).

### چرخش
- به طور منظم اسرار و حساب های خدمات را بچرخانید.
- چرخش را در صورت امکان به صورت خودکار انجام دهید.

---

## مدیریت وابستگی

### اسکن آسیب پذیری
- ** Python**: `safety`، `pip-audit`، `bandit`.
- **گره**: `npm audit`، `yarn audit`، `snyk`.
- **زنگ زدگی**: `cargo audit`.
- **برو**: `govulncheck`.
- **عمومی**: `Dependabot` (GitHub)، `Renovate`، `Trivy`.

### پچ کردن
- وابستگی ها را به نسخه های وصله شده به روز نگه دارید.
- درخواست‌های کشش خودکار را برای به‌روزرسانی‌های جزئی/پچ تنظیم کنید.
- بررسی تغییرات لاگ برای شکستن تغییرات.

### یکپارچگی زنجیره تامین
- از فایل‌های قفل بسته (`package-lock.json`، `Cargo.lock`، `go.sum`) برای اطمینان از ساخت‌های قابل تکرار استفاده کنید.
- بررسی وابستگی های دانلود شده را بررسی کنید.
- ثبت رسمی را ترجیح دهید و فقط به ناشران تأیید شده اعتماد کنید.

---

## امنیت زیرساخت

### فایروال ها
- تمام پورت های ورودی به جز آنهایی که به صراحت مورد نیاز هستند را مسدود کنید (به عنوان مثال، 80، 443).
- دسترسی SSH را به محدوده IP خاص محدود کنید (یا از یک میزبان VPN/bastion استفاده کنید).
- از گروه های امنیتی (AWS) یا NSG (آژور) برای کنترل دقیق استفاده کنید.

### سخت شدن سیستم عامل
- به‌روزرسانی‌های امنیتی را مرتباً اعمال کنید (`sudo apt upgrade`، `yum update`).
- خدمات غیر ضروری و حساب های پیش فرض را غیرفعال کنید.
- از fail2ban برای جلوگیری از تلاش های brute-force در SSH استفاده کنید.
- Harden SSH: غیرفعال کردن ورود به ریشه، استفاده از احراز هویت مبتنی بر کلید، تغییر پورت پیش فرض (اختیاری).### تقسیم بندی شبکه
- پایگاه داده ها و کش ها را در زیرشبکه های خصوصی بدون دسترسی به اینترنت قرار دهید.
- از DMZ برای خدمات عمومی استفاده کنید.
- استفاده از اصل حداقل امتیاز برای دسترسی به شبکه.

### اسرار در زیرساخت
- هرگز اسرار را در متغیرهای محیط CI/CD ذخیره نکنید مگر اینکه رمزگذاری شده باشد.
- از نقش های IAM ارائه دهنده ابر برای نمونه های EC2/VM به جای کلیدهای طولانی مدت استفاده کنید.

---

## ثبت و نظارت

### چه چیزی را وارد کنید
- رویدادهای احراز هویت (موفقیت / شکست).
- تصمیمات کنترل دسترسی (شکست های مجوز).
- اقدامات مدیریت (ایجاد کاربر، حذف، تغییرات مجوز).
- تغییرات طرحواره پایگاه داده
- خطاها و استثنائات سیستم
- درخواست ها و پاسخ های API (داده های حساس را ویرایش کنید).

### چه چیزی را نباید ثبت کرد
- رمزهای عبور، اسرار، نشانه‌ها، PII (اطلاعات شناسایی شخصی) مگر اینکه هش یا ویرایش شده باشند.
- شماره کارت اعتباری کامل

### هشدار
- تنظیم هشدار برای:
  - چندین بار ورود ناموفق (بالقوه brute force).
  - الگوهای دسترسی غیرمعمول (به عنوان مثال، از مکان های جدید، در ساعت های فرد).
  - ایجاد حساب های مدیریت جدید
  - نرخ خطا یا افزایش تاخیر.
- از SIEM (اطلاعات امنیتی و مدیریت رویداد) برای همبستگی پیشرفته استفاده کنید.

### حفظ گزارش
- لاگ ها را حداقل 30 تا 90 روز بسته به الزامات نظارتی نگهداری کنید.
- لاگ‌ها را در یک سیستم متمرکز و غیرقابل دستکاری (مانند ELK Stack، Splunk، Datadog) ذخیره کنید.

---

## چرخه عمر توسعه امن (SDL)

1. **آموزش**: اطمینان حاصل کنید که توسعه دهندگان آسیب پذیری های رایج را درک می کنند.
2. **مدل سازی تهدید**: تهدیدهای بالقوه را در ابتدای طراحی شناسایی کنید.
3. **استانداردهای کدگذاری ایمن**: از طریق لینترها و چک لیست های بازبینی کد اعمال می شود.
4. **SAST** (تست امنیتی برنامه استاتیک): کد منبع را برای آسیب‌پذیری‌ها اسکن کنید (SonarQube، CodeQL).
5. **DAST** (تست امنیت برنامه پویا): برنامه های در حال اجرا را اسکن کنید (OWASP ZAP، Burp Suite).
6. **SCA** (تحلیل ترکیب نرم افزار): وابستگی ها را اسکن کنید.
7. **تست نفوذ**: تمرینات هک اخلاقی منظم.
8. **باگ بوونتی**: محققان خارجی را تشویق کنید تا آسیب پذیری ها را مسئولانه پیدا کنند.
9. **طرح واکنش به حادثه**: برای زمانی که یک تخلف شناسایی می شود، یک برنامه روشن داشته باشید.

---

## چک لیست اضطراری (وقتی مشکوک به نقض است)

1. ** وحشت نکنید ** - اما سریع عمل کنید.
2. **ایزوله** سیستم های آسیب دیده (در صورت نیاز از شبکه جدا شوید).
3. **حفظ شواهد**: ضبط سیاهههای مربوط، روگرفت حافظه، و تصاویر دیسک.
4. **شناسایی** محدوده: کدام سیستم ها، کدام داده ها.
5. ** چرخش ** همه اعتبارنامه ها و اسرار به خطر افتاده.
6. **وصله** آسیب پذیری.
7. **به کاربران متاثر و نهادهای نظارتی در صورت نیاز (در چارچوب زمانی قانونی) اطلاع دهید.
8. ** برای درک علت اصلی و بهبود فرآیندها، یک پس از مرگ انجام دهید.