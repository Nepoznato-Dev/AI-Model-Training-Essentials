# Yerel AI Mimarisi

Büyük dil modellerini tamamen cihaz üzerinde çalıştırmaya yönelik; donanım gereksinimleri, inference motorları, bellek optimizasyonu ve edge deployment için sistem tasarımını kapsayan pratik bir rehber.

---

## AI'yi Neden Yerel Çalıştırmalı?

- **Privacy**: Veri cihazdan çıkmaz.
- **Cost**: Token başına API ücreti yoktur.
- **Latency**: Öngörülebilir, ağdan bağımsız inference.
- **Offline availability**: İnternet olmadan çalışır.
- **Control**: Model sürümü, özelleştirme ve fine-tuning üzerinde tam kontrol sağlar.

---

## Donanım Gereksinimleri

### GPU Belleği (VRAM)
En kritik kaynaktır. Bellekte model boyutu ≈ **parametre sayısı × parametre başına byte**.

| Precision | Parametre başına byte | 3.8B model | 7B model | 13B model | 70B model |
|-----------|-----------------------|------------|----------|-----------|-----------|
| FP32      | 4                     | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                     | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1                | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5              | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Pratik yönergeler:**
- 8GB VRAM → 4-bit'te 7B modellere kadar.
- 12GB VRAM → 4-bit'te 13B modellere kadar.
- 24GB VRAM → 4-bit'te 70B modellere kadar (veya 8-bit'te 13B).
- Apple Silicon (unified memory), 64GB+ sistemlerde 70B modelleri çalıştırabilir.

### RAM (Sistem Belleği)
- CPU inference için, modeli yükleyecek kadar sistem RAM'i gerekir (yaklaşık VRAM rakamlarına benzer).
- GPU inference için, model VRAM'e offload edilmeden önce belleğe alınacağı için sistem RAM'i önemlidir.

### Depolama
- Quantised model weights birkaç GB yer kaplar (ör. 4-bit 7B ≈ diskte 4 GB). Birden çok model için en az 20–50 GB boş alan bırakın.

### CPU
- Prompt processing (prefill) ve CPU offloading için modern, çok çekirdekli bir CPU faydalıdır.
- Apple M serisi çipler, unified memory ve Neural Engine sayesinde LLM'lerde çok iyi performans gösterir.

---

## Quantisation

Quantisation, ağırlıkların sayısal hassasiyetini düşürerek doğrulukta küçük bir bedel karşılığında belleği ciddi biçimde azaltır ve hızı artırır.

### Popüler Formatlar

| Format | Bits | Açıklama | Tipik kullanım |
|--------|------|----------|----------------|
| **GGUF** | 4–8 | llama.cpp formatı, CPU/GPU hibriti için optimize edilmiştir | Yerel inference için en iyisi |
| **GPTQ** | 4–8 | Yalnızca GPU, CUDA üzerinde verimli | NVIDIA GPU'lar için en iyisi |
| **AWQ** | 4 | Activation-aware, yalnızca GPU | GPU'larda batch inference için iyi |
| **ONNX** | variable | Standartlaştırılmış, platformlar arası | Production serving |

### Quantisation Seviyesi Seçimi
- **Q8_0** (8-bit): minimum kalite kaybı, en büyük boyut.
- **Q6_K** (6-bit): iyi kalite, makul sıkıştırma.
- **Q5_K_M** (5-bit): yaygın tatlı nokta.
- **Q4_K_M** (4-bit): en küçük boyut, çoğu görev için kabul edilebilir kalite.
- **IQ4_XS** / **IQ3_XS**: 4/3 bit'te daha iyi perplexity sunan geliştirilmiş quantisation.

**Genel kural:** Kalite ve boyut dengesi için Q4_K_M kullanın. Ek VRAM'iniz varsa Q5 veya Q6 kullanın.

---

## Inference Motorları (Yerel)

### llama.cpp
- C++ ile yazılmıştır.
- GGUF formatını destekler.
- CPU ve GPU için optimize edilmiştir (CUDA, Metal, OpenCL üzerinden).
- Özellikle CPU'da çok hızlıdır.
- Command-line, server mode ve Python bindings sunar.

**Örnek komut:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)

Ollama
llama.cpp'yi basit bir CLI ve REST API ile sarmalar.

Modelleri otomatik indirir ve yönetir.

Prototipleme ve masaüstü uygulamaları için çok uygundur.

System prompt'lar için özel Modelfile'ları destekler.

Kullanım:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Windows, macOS ve Linux için grafik masaüstü uygulaması.

Tek tıklamayla indirme ve chat arayüzü sunar.

OpenAI uyumlu API'ye sahip yerleşik bir yerel server içerir.

Teknik olmayan kullanıcılar ve hızlı testler için uygundur.

Hugging Face Transformers + bitsandbytes
HF modelleri için standart Python kütüphanesidir.

4-bit quantisation için bitsandbytes kullanın (load_in_4bit=True).

Fine-tuning açısından daha esnektir, ancak inference için llama.cpp'den daha yavaştır.

ExLlamaV2
GPTQ ve AWQ için çok hızlı GPU inference sağlar.

NVIDIA GPU'larda en iyi performansı verir.

Batch generation destekler.

mlx (Apple)
Apple'ın M serisi çipler için framework'üdür.

Apple Silicon için yoğun biçimde optimize edilmiştir.

Python API.

Bellek Yönetimi
Context Window ve KV Cache
KV cache, context içindeki her layer ve her token için key-value çiftlerini saklar. Context uzunluğuyla doğrusal olarak büyür.

Bellek maliyeti ≈ 2 × layers × (KV heads × head dim) × tokens × value başına byte

8 KV head ve 128 head dim'e sahip 32 katmanlı bir model için her token yaklaşık ~32 × 8 × 128 × 2 byte = token başına 65 KB maliyet oluşturur. 128k token'da bu, yalnızca cache için ~8 GB demektir.

Offloading Stratejileri
Layer offloading: Bazı katmanları GPU'ya, diğerlerini CPU'ya koyun. Tam CPU'ya göre daha hızlıdır, VRAM gereksinimi daha düşüktür.

Token streaming: Tüm token'ları tek seferde değil, artımlı olarak işleyin.

Prompt Caching
Prefill aşamasını yeniden hesaplamamak için benzer prompt'lar arasında KV cache'leri yeniden kullanın. Bazı framework'ler bunu destekler (ör. vLLM, --prompt-cache ile llama.cpp).

Memory-Mapped Files
Model weights'i tamamen RAM'e almadan doğrudan diskten yükleyin (belleği sınırlı sistemlerde büyük modeller için faydalıdır). llama.cpp varsayılan olarak memory-mapping kullanır.

Dağıtım Mimarileri
Single-Device Mode
Tek bir model tek bir makinede çalışır (laptop, smartphone, edge device). Kişisel asistanlar, not alma uygulamaları, code completion için kullanılır.

Hybrid Edge-Cloud
Yerel model yaygın sorguları işler; karmaşık sorular için cloud model'e geri düşer. Böylece her iki dünyanın da en iyisini verir — çoğu durumda hız/mahremiyet, uç durumlarda yetenek.

Distributed Inference (Multi-GPU)
Daha büyük modeller için katmanları birden fazla GPU'ya bölün (tensor parallelism) veya context'i cihazlar arasında bölün (pipeline parallelism). llama.cpp'de -ngl ya da ExLlamaV2'de --num-gpu-layers kullanın.

Mobile Deployment
Android: JNI bindings veya ML Kit üzerinden llama.cpp kullanın.

iOS: Swift bindings veya mlx üzerinden llama.cpp kullanın.

Web: WebLLM (ONNX runtime üzerinden WebGPU'da çalışır) veya transformers.js kullanın.

Performans Optimizasyonu
Flash Attention
Attention hesaplamasını hızlandırır ve bellek kullanımını azaltır. llama.cpp, ExLlamaV2 ve modern transformers kütüphanelerinde bulunur.

Batch Inference
Birden fazla prompt'u tek bir forward pass içinde işleyin. Throughput'u ciddi biçimde artırır. llama-batch veya vLLM kullanın.

Early Stopping / Token Budgeting
Sınırsız üretimi önlemek için maksimum token bütçesi belirleyin.

Speculative Decoding
Küçük ve hızlı bir model (draft), token'ları tahmin eder; büyük model bunları paralel olarak doğrular. 2–3× hızlanma sağlayabilir.

Pratik Kurulum Rehberi
1. Ollama'yı kurun
bash
curl -fsSL https://ollama.com/install.sh | sh
2. Bir model çekin
bash
ollama pull phi3:3.8b-q4_K_M
3. API ile çalıştırın
bash
ollama serve
Ardından istekleri http://localhost:11434/api/generate adresine gönderin.

4. Python Entegrasyonu
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Alternatif) Doğrudan llama.cpp kullanın
bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
İzleme ve Gözlemlenebilirlik
GPU kullanımını izleyin (Linux'ta nvidia-smi, macOS'te Activity Monitor).

Bellek kullanımını izleyin (RAM ve VRAM).

Saniye başına token sayısını izleyin (throughput).

İlk token'a kadar geçen süreyi izleyin (latency).

llama.cpp veya Ollama'nın yerleşik log'larını kullanın.

Sınırlamalar ve Ödünleşimler
Kalite farkı: Küçük yerel modeller (3.8B–7B), karmaşık akıl yürütmede genellikle büyük cloud modellerinin (GPT-4, Claude 3.5) gerisinde kalır.

Knowledge cutoff: Model bilgisi eğitim anında donar; güncel bilgiyi eklemek için RAG kullanın.

Multilingual: Daha küçük modellerin çok dilli yetenekleri daha sınırlı olabilir.

Tool use: Agentic workflow'lar (function calling), küçük modellerde daha az güvenilir olabilir.

Birçok gündelik görev için (summarisation, Q&A, code completion, classification) yerel modeller şimdiden yeterlidir ve hızla gelişmektedir.

text

---

## Dosya 4: `security_best_practices.md`

```markdown
# Güvenlik için En İyi Uygulamalar

Uygulamaları, altyapıyı ve veriyi geliştirmeden production'a kadar güvence altına almaya yönelik pratik bir rehber.

---

## OWASP Top 10 (2021) — Genel Bakış

1. **Broken Access Control**: Kullanıcılar erişmemeleri gereken kaynaklara erişebilir.
2. **Cryptographic Failures**: Zayıf ya da eksik şifreleme.
3. **Injection**: SQL, NoSQL, OS command veya LDAP injection.
4. **Insecure Design**: Mimari kusurlar.
5. **Security Misconfiguration**: Varsayılan parolalar, açık portlar, aşırı ayrıntılı hata mesajları.
6. **Vulnerable and Outdated Components**: Bağımlılıklardaki bilinen CVE'ler.
7. **Identification and Authentication Failures**: Zayıf parolalar, hatalı session yönetimi.
8. **Software and Data Integrity Failures**: Supply chain saldırıları, imzasız güncellemeler.
9. **Security Logging and Monitoring Failures**: İhlallerin tespit edilememesi.
10. **Server-Side Request Forgery (SSRF)**: Sunucunun iç sistemlere istek yapması için kötüye kullanılması.

---

## Girdi Doğrulama ve Çıktı Kodlama

### Doğrulama Kuralları
- **Whitelist > Blacklist**: Bilinen kötü desenleri engellemek yerine izin verilen desenleri tanımlayın (ör. e-posta için regex).
- **Length limits**: Buffer overflow ve DoS'u önlemek için maksimum uzunlukları zorunlu kılın.
- **Type checking**: Integer'ların integer, boolean'ların boolean olduğundan emin olun.
- **Use well-tested libraries**: E-posta, URL ve tarih doğrulaması için standart kütüphaneleri kullanın (ör. Python'da `email-validator`, Node'da `validator.js`).

### Çıktı Kodlama
- **HTML encoding**: XSS'i önlemek için `<`, `>`, `&`, `"`, `'` karakterlerini kodlayın.
- **SQL parameterisation**: Kullanıcı girdisini asla SQL sorgularına doğrudan eklemeyin. Parameterised query'ler (prepared statements) veya bir ORM kullanın.
- **Shell escaping**: Kullanıcı girdisinden shell komutu oluşturmayın; kaçınılmazsa `shlex.quote()` veya benzerini kullanın.

---

## Kimlik Doğrulama ve Yetkilendirme

### Parola Yönetimi
- **Hashing**: Parolaları güçlü ve yavaş bir hashing algoritmasıyla saklayın: **Argon2id** (tercih edilir), **bcrypt**, **scrypt** veya **PBKDF2**.
- **Salting**: Kullanıcı başına benzersiz bir salt ekleyin.
- **Minimum length**: En az 12–16 karakter zorunlu kılın.
- **MFA (Multi-Factor Authentication)**: Hassas işlemler için ikinci bir faktör (TOTP, SMS, hardware key) isteyin.
- **Rate limiting**: Login endpoint'lerinde brute-force denemelerini önleyin (ör. IP/kullanıcı başına 5 dakikada 5 deneme).

### Session Management
- Session token'ları için secure, HTTP-only, SameSite cookie'ler kullanın.
- Uygun expiration süreleri belirleyin.
- Logout sırasında ve parola değişiminde session'ları geçersiz kılın.
- Session ID'lerini URL'lerde göstermeyin.

### OAuth2 / OIDC
- İyi bilinen kütüphaneleri kullanın (ör. Authlib, PyJWT, Passport.js, Spring Security).
- ID token'ları ayrıntılı biçimde doğrulayın (signature, issuer, audience, expiration).
- CSRF'yi önlemek için state parametreleri kullanın.
- Client secret'ları gizli tutun.

### JWT (JSON Web Tokens)
- **Sign**: Daha iyi güvenlik için RS256 veya ES256 (asimetrik) kullanın; paylaşılan secret'lar iyi yönetiliyorsa HS256 (simetrik) de kabul edilebilir.
- **Validate**: Her zaman signature, issuer (`iss`), audience (`aud`) ve expiration (`exp`) doğrulaması yapın.
- **Keep short expiration**: Access token'lar için 15–60 dakika kullanın; daha uzun session'lar için refresh token kullanın.
- **Store securely**: JWT'leri asla localStorage'da tutmayın (XSS'e açıktır); bunun yerine HTTP-only cookie kullanın.

---

## API Güvenliği

### Authentication
- API çağrılarını her zaman doğrulayın (public endpoint'ler hariç).
- Basic auth yerine API key veya OAuth2 token'larını tercih edin (basic auth her istekte credential gönderir).

### Rate Limiting ve Throttling
- Kötüye kullanımı ve DoS'u önlemek için kullanıcı ve IP başına oran sınırları uygulayın.
- `Retry-After` header'ı ile birlikte `429 Too Many Requests` döndürün.

### CORS (Cross-Origin Resource Sharing)
- Yalnızca belirli origin'lere izin verin (production'da asla `*` kullanmayın).
- Sunucu tarafında `Origin` header'ını doğrulayın.

### Input Validation
- Header ve body dâhil tüm request parametrelerini doğrulayın.
- Beklenmeyen alanları reddedin (`"strict": true` veya JSON Schema'da `additionalProperties: false`).

### HTTPS / TLS
- Production'da HTTPS'i zorunlu kılın.
- Tarayıcıları HTTPS kullanmaya zorlamak için HSTS (HTTP Strict Transport Security) kullanın.
- TLS 1.2 veya 1.3 kullanın (TLS 1.0/1.1'i devre dışı bırakın).

---

## Secrets Management

### Secret'ları Asla Hardcode Etmeyin
- Secret'ları (API key'ler, parolalar, veritabanı URL'leri) source control'e commit etmeyin.
- Environment variable'lar veya secret management araçları kullanın.

### Araçlar
- **HashiCorp Vault**: Kurumsal düzeyde, dinamik secret yönetimi.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-native çözümler.
- **SOPS**: Secret'ları dosyalarda şifreler ve commit etmenizi sağlar (KMS veya GPG ile).
- **Docker secrets**: Swarm mode için; Kubernetes secrets (base64-encoded olsa da dikkatli kullanın; harici Secrets Store CSI driver'ı değerlendirin).

### Rotasyon
- Secret'ları ve service account'ları düzenli olarak döndürün.
- Mümkünse rotasyonu otomatikleştirin.

---

## Bağımlılık Yönetimi

### Güvenlik Açığı Taraması
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Yama Yönetimi
- Bağımlılıkları yamalı sürümlerde güncel tutun.
- Minor/patch güncellemeleri için otomatik pull request'ler kurun.
- Breaking change'ler için changelog'ları inceleyin.

### Supply Chain Integrity
- Tekrarlanabilir build'ler için package lockfile'larını (`package-lock.json`, `Cargo.lock`, `go.sum`) kullanın.
- İndirilen bağımlılıkların checksum'larını doğrulayın.
- Resmî registry'leri tercih edin ve yalnızca doğrulanmış yayıncılara güvenin.

---

## Altyapı Güvenliği

### Firewalls
- Açıkça gerekli olanlar dışında tüm gelen portları engelleyin (ör. 80, 443).
- SSH erişimini belirli IP aralıklarıyla sınırlayın (veya VPN/bastion host kullanın).
- İnce taneli kontrol için security group'ları (AWS) veya NSG'leri (Azure) kullanın.

### OS Hardening
- Güvenlik güncellemelerini düzenli uygulayın (`sudo apt upgrade`, `yum update`).
- Gereksiz servisleri ve varsayılan hesapları devre dışı bırakın.
- SSH üzerindeki brute-force denemelerini engellemek için fail2ban kullanın.
- SSH'yi sıkılaştırın: root login'i devre dışı bırakın, key-based auth kullanın, varsayılan portu değiştirin (isteğe bağlı).

### Network Segmentation
- Veritabanlarını ve cache'leri internet erişimi olmayan özel subnet'lere yerleştirin.
- Public-facing servisler için DMZ kullanın.
- Network erişiminde least privilege ilkesini uygulayın.

### Altyapıda Secret'lar
- Şifrelenmemişse secret'ları asla CI/CD environment variable'larında saklamayın.
- Uzun ömürlü anahtarlar yerine EC2/VM instance'ları için cloud sağlayıcısının IAM rollerini kullanın.

---

## Logging ve Monitoring

### Ne Loglanmalı?
- Authentication olayları (başarı/başarısızlık).
- Access control kararları (yetkilendirme hataları).
- Admin işlemleri (kullanıcı oluşturma, silme, izin değişiklikleri).
- Veritabanı şema değişiklikleri.
- Sistem hataları ve exception'lar.
- API request ve response'ları (hassas verileri maskeleyerek).

### Ne Loglanmamalı?
- Hash'lenmemiş / maskelenmemiş parolalar, secret'lar, token'lar, PII (Personal Identifiable Information).
- Tam kredi kartı numaraları.

### Alerting
- Şunlar için uyarılar ayarlayın:
  - Birden fazla başarısız login (olası brute force).
  - Olağandışı erişim örüntüleri (ör. yeni konumlardan, sıra dışı saatlerde).
  - Oluşturulan yeni admin hesapları.
  - Yüksek hata oranları veya gecikme sıçramaları.
- İleri düzey korelasyon için bir SIEM (Security Information and Event Management) kullanın.

### Log Retention
- Düzenleyici gereksinimlere bağlı olarak log'ları en az 30–90 gün saklayın.
- Log'ları merkezî, kurcalamaya dayanıklı bir sistemde tutun (ör. ELK Stack, Splunk, Datadog).

---

## Secure Development Lifecycle (SDL)

1. **Training**: Geliştiricilerin yaygın güvenlik açıklarını anladığından emin olun.
2. **Threat modelling**: Olası tehditleri tasarımın erken aşamalarında belirleyin.
3. **Secure coding standards**: Linters ve code review checklist'leriyle zorunlu kılın.
4. **SAST** (Static Application Security Testing): Source code'u güvenlik açıkları için tarayın (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): Çalışan uygulamaları tarayın (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): Bağımlılıkları tarayın.
7. **Penetration testing**: Düzenli etik hacking çalışmaları yapın.
8. **Bug bounty**: Harici araştırmacıları güvenlik açıklarını sorumlu biçimde bulmaya teşvik edin.
9. **Incident response plan**: Bir ihlal tespit edildiğinde uygulanacak net bir planınız olsun.

---

## Acil Durum Kontrol Listesi (Bir İhlalden Şüphelenildiğinde)

1. **Panik yapmayın** — ama hızlı hareket edin.
2. Etkilenen sistemleri **izole edin** (gerekirse ağ bağlantısını kesin).
3. **Kanıtı koruyun**: Log'ları, memory dump'ları ve disk imajlarını alın.
4. **Kapsamı belirleyin**: Hangi sistemler, hangi veriler etkilendi.
5. Tehlikeye girmiş tüm credential ve secret'ları **döndürün**.
6. Güvenlik açığını **yamayın**.
7. Gerekliyse etkilenen kullanıcıları ve düzenleyici kurumları **bilgilendirin** (yasal süreler içinde).
8. Kök nedeni anlamak ve süreçleri iyileştirmek için **post-mortem** gerçekleştirin.
