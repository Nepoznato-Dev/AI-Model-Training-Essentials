# Local AI Architecture

पूरी तरह on-device बड़े भाषा models चलाने के लिए एक व्यावहारिक मार्गदर्शिका — hardware considerations, inference engines, memory optimisation, और edge deployment के लिए system design।

---

## AI को स्थानीय रूप से क्यों चलाएँ?

- **Privacy**: कोई डेटा device से बाहर नहीं जाता।
- **Cost**: प्रति token कोई API शुल्क नहीं।
- **Latency**: पूर्वानुमेय, network-free inference।
- **Offline availability**: internet के बिना भी काम करता है।
- **Control**: model version, customisation और fine-tuning पर पूर्ण नियंत्रण।

---

## Hardware Requirements

### GPU Memory (VRAM)
सबसे महत्वपूर्ण संसाधन। Memory में model size ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**व्यावहारिक दिशानिर्देश:**
- 8GB VRAM → 4-bit पर 7B models तक।
- 12GB VRAM → 4-bit पर 13B models तक।
- 24GB VRAM → 4-bit पर 70B models तक (या 8-bit पर 13B)।
- Apple Silicon (unified memory) 64GB+ systems पर 70B models चला सकता है।

### RAM (System Memory)
- CPU inference के लिए model load करने हेतु पर्याप्त system RAM चाहिए (लगभग VRAM जैसी ही संख्याएँ)।
- GPU inference के लिए system RAM model को memory में load करने और फिर VRAM में offload करने से पहले महत्वपूर्ण होती है।

### Storage
- Quantised model weights कुछ GB जगह लेते हैं (उदा., 4-bit 7B ≈ 4 GB disk पर)। कई models के लिए कम से कम 20–50 GB खाली रखें।

### CPU
- Prompt processing (prefill) और CPU-offloading के लिए आधुनिक multi-core CPU सहायक होता है।
- Apple M-series chips unified memory और Neural Engine के कारण LLMs के लिए उत्कृष्ट प्रदर्शन देती हैं।

---

## Quantisation

Quantisation weights की numerical precision कम करती है, जिससे memory बहुत घटती है और speed बढ़ती है, जबकि accuracy पर केवल थोड़ा प्रभाव पड़ता है।

### Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp format, CPU/GPU hybrid के लिए optimised | Local inference के लिए सर्वोत्तम |
| **GPTQ** | 4–8 | केवल GPU, CUDA पर कुशल | NVIDIA GPUs के लिए सर्वोत्तम |
| **AWQ** | 4 | Activation-aware, केवल GPU | GPUs पर batch inference के लिए अच्छा |
| **ONNX** | variable | Standardised, cross-platform | Production serving |

### Quantisation Level चुनना
- **Q8_0** (8-bit): quality loss न्यूनतम, size सबसे बड़ा।
- **Q6_K** (6-bit): अच्छी quality, उचित compression।
- **Q5_K_M** (5-bit): सामान्य sweet spot।
- **Q4_K_M** (4-bit): सबसे छोटा, अधिकांश tasks के लिए स्वीकार्य quality।
- **IQ4_XS** / **IQ3_XS**: 4/3 bits पर बेहतर perplexity वाली improved quantisation।

**Rule of thumb:** quality और size के अच्छे संतुलन के लिए Q4_K_M का उपयोग करें। यदि आपके पास अतिरिक्त VRAM है, तो Q5 या Q6 का उपयोग करें।

---

## Inference Engines (Local)

### llama.cpp
- C++ में लिखा गया।
- GGUF format को support करता है।
- CPU और GPU (CUDA, Metal, OpenCL के माध्यम से) के लिए optimised।
- विशेष रूप से CPU पर बहुत तेज़।
- Command-line, server mode, और Python bindings उपलब्ध।

**उदाहरण command:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)

Ollama
llama.cpp को एक सरल CLI और REST API के साथ wrap करता है।

Models को अपने-आप download करता है, और उन्हें manage करता है।

Prototyping और desktop apps के लिए बेहतरीन।

System prompts के लिए custom Modelfiles को support करता है।

Usage:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Windows, macOS, Linux के लिए graphical desktop app।

One-click download और chat interface।

Built-in local server, OpenAI-compatible API के साथ।

Non-technical users और quick testing के लिए अच्छा।

Hugging Face Transformers + bitsandbytes
HF models के लिए standard Python library।

4-bit quantisation के लिए bitsandbytes का उपयोग करें (`load_in_4bit=True`)।

Fine-tuning के लिए अधिक flexible, लेकिन inference के लिए llama.cpp से धीमा।

ExLlamaV2
GPTQ और AWQ के लिए बहुत तेज़ GPU inference।

NVIDIA GPUs पर सर्वोत्तम प्रदर्शन।

Batched generation को support करता है।

mlx (Apple)
M-series chips के लिए Apple का framework।

Apple Silicon के लिए अत्यधिक optimised।

Python API।

Memory Management
Context Window and KV Cache
KV cache context में हर layer और हर token के लिए key-value pairs store करता है। यह context length के साथ linear रूप से बढ़ता है।

Memory cost ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

32-layer model जिसमें 8 KV heads और 128 head dim हो, उसमें प्रत्येक token की लागत ~32 × 8 × 128 × 2 bytes = 65 KB प्रति token होती है। 128k tokens के लिए केवल cache ही ~8 GB ले सकता है।

Offloading Strategies
Layer offloading: कुछ layers को GPU पर और बाकी को CPU पर रखें। यह pure CPU से तेज़ है और VRAM की आवश्यकता कम होती है।

Token streaming: सभी tokens को एक साथ प्रोसेस करने के बजाय incremental रूप से प्रोसेस करें।

Prompt Caching
समान prompts के बीच KV caches का पुनः उपयोग करें ताकि prefill phase को दोबारा compute न करना पड़े। कुछ frameworks इसे support करते हैं (उदा., vLLM, llama.cpp with --prompt-cache)।

Memory-Mapped Files
Model weights को पूरी तरह RAM में load किए बिना सीधे disk से load करें (memory-limited systems पर विशाल models के लिए उपयोगी)। llama.cpp default रूप से memory-mapping का उपयोग करता है।

Deployment Architectures
Single-Device Mode
एक model एक मशीन पर चलता है (laptop, smartphone, edge device)। इसका उपयोग personal assistants, note-taking apps, code completion के लिए होता है।

Hybrid Edge-Cloud
Local model सामान्य queries संभालता है; जटिल प्रश्नों के लिए cloud model fallback होता है। इससे दोनों का लाभ मिलता है — अधिकांश के लिए speed/private, edge cases के लिए capability।

Distributed Inference (Multi-GPU)
बड़े models के लिए layers को कई GPUs में बाँटें (tensor parallelism) या context को devices के बीच विभाजित करें (pipeline parallelism)। llama.cpp को `-ngl` के साथ या ExLlamaV2 को `--num-gpu-layers` के साथ उपयोग करें।

Mobile Deployment
Android: JNI bindings या ML Kit के माध्यम से llama.cpp का उपयोग करें।

iOS: Swift bindings या mlx के माध्यम से llama.cpp का उपयोग करें।

Web: WebLLM (जो WebGPU पर ONNX runtime के माध्यम से चलता है) या transformers.js का उपयोग करें।

Performance Optimisation
Flash Attention
Attention computation को तेज़ करता है और memory usage घटाता है। यह llama.cpp, ExLlamaV2, और आधुनिक transformers libraries में उपलब्ध है।

Batch Inference
कई prompts को एक single forward pass में प्रोसेस करें। इससे throughput बहुत बढ़ता है। llama-batch या vLLM का उपयोग करें।

Early Stopping / Token Budgeting
अनियंत्रित generation को रोकने के लिए maximum token budget निर्धारित करें।

Speculative Decoding
एक छोटा तेज़ model (draft) tokens का अनुमान लगाता है, फिर बड़ा model समानांतर में उन्हें verify करता है। इससे 2–3× speedup मिल सकता है।

Practical Setup Guide
1. Ollama install करें
bash
curl -fsSL https://ollama.com/install.sh | sh
2. एक Model pull करें
bash
ollama pull phi3:3.8b-q4_K_M
3. API के साथ चलाएँ
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
5. (Alternative) llama.cpp को सीधे उपयोग करें
bash
# Hugging Face से GGUF download करें
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Server चलाएँ
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
Monitoring and Observability
GPU utilisation track करें (Linux पर `nvidia-smi`, macOS पर Activity Monitor)।

Memory usage (RAM और VRAM) track करें।

Tokens per second (throughput) track करें।

पहले token तक का समय (latency) track करें।

llama.cpp या Ollama की built-in logging का उपयोग करें।

Limitations and Tradeoffs
Quality gap: छोटे local models (3.8B–7B) जटिल reasoning में सामान्यतः बड़े cloud models (GPT-4, Claude 3.5) से कम प्रदर्शन करते हैं।

Knowledge cutoff: model knowledge training समय पर freeze होती है; current information inject करने के लिए RAG का उपयोग करें।

Multilingual: छोटे models में multilingual capability कम हो सकती है।

Tool use: agentic workflows (function calling) छोटे models पर कम विश्वसनीय हो सकते हैं।

कई रोज़मर्रा के कार्यों (summarisation, Q&A, code completion, classification) के लिए local models पहले से पर्याप्त हैं और तेज़ी से बेहतर हो रहे हैं।

text

---

## File 4: `security_best_practices.md`

```markdown
# Security Best Practices

Applications, infrastructure, और data को सुरक्षित करने के लिए एक व्यावहारिक मार्गदर्शिका — development से production तक।

---

## OWASP Top 10 (2021) — अवलोकन

1. **Broken Access Control**: users उन resources तक पहुँच सकते हैं जहाँ उन्हें नहीं पहुँचनी चाहिए।
2. **Cryptographic Failures**: कमजोर या अनुपस्थित encryption।
3. **Injection**: SQL, NoSQL, OS command, या LDAP injection।
4. **Insecure Design**: architectural flaws।
5. **Security Misconfiguration**: default passwords, open ports, verbose errors।
6. **Vulnerable and Outdated Components**: dependencies में ज्ञात CVEs।
7. **Identification and Authentication Failures**: कमजोर passwords, खराब session management।
8. **Software and Data Integrity Failures**: supply chain attacks, unsigned updates।
9. **Security Logging and Monitoring Failures**: breaches का पता न चलना।
10. **Server-Side Request Forgery (SSRF)**: internal systems को requests भेजने के लिए server का दुरुपयोग।

---

## Input Validation and Output Encoding

### Validation Rules
- **Whitelist > Blacklist**: ज्ञात खराब patterns को block करने के बजाय अनुमत patterns परिभाषित करें (उदा., email के लिए regex)।
- **Length limits**: buffer overflows और DoS को रोकने के लिए अधिकतम lengths लागू करें।
- **Type checking**: सुनिश्चित करें कि integers वास्तव में integers हों, booleans वास्तव में booleans हों।
- **Use well-tested libraries**: email, URL, और date validation के लिए standard libraries का उपयोग करें (उदा., Python में `email-validator`, Node में `validator.js`)।

### Output Encoding
- **HTML encoding**: XSS को रोकने के लिए `<`, `>`, `&`, `"`, `'` encode करें।
- **SQL parameterisation**: user input को कभी भी सीधे SQL queries में concatenate न करें। Parameterised queries (prepared statements) या ORM का उपयोग करें।
- **Shell escaping**: user input से shell commands बनाना टालें; यदि अपरिहार्य हो, तो `shlex.quote()` या समान साधन का उपयोग करें।

---

## Authentication and Authorisation

### Password Management
- **Hashing**: passwords को मजबूत, धीमे hashing algorithm के साथ store करें: **Argon2id** (preferred), **bcrypt**, **scrypt**, या **PBKDF2**।
- **Salting**: प्रत्येक user के लिए unique salt जोड़ें।
- **Minimum length**: कम से कम 12–16 characters अनिवार्य करें।
- **MFA (Multi-Factor Authentication)**: संवेदनशील operations के लिए second factor (TOTP, SMS, hardware key) आवश्यक करें।
- **Rate limiting**: login endpoints पर brute-force attempts रोकें (उदा., प्रति IP/user प्रति 5 मिनट में 5 attempts)।

### Session Management
- Session tokens के लिए secure, HTTP-only, SameSite cookies का उपयोग करें।
- उपयुक्त expiration times सेट करें।
- logout और password change पर sessions को invalidate करें।
- URLs में session IDs को expose करने से बचें।

### OAuth2 / OIDC
- अच्छी तरह स्थापित libraries का उपयोग करें (उदा., Authlib, PyJWT, Passport.js, Spring Security)।
- ID tokens को पूरी तरह validate करें (signature, issuer, audience, expiration)।
- CSRF को रोकने के लिए state parameters का उपयोग करें।
- Client secrets को गोपनीय रखें।

### JWT (JSON Web Tokens)
- **Sign**: बेहतर सुरक्षा के लिए RS256 या ES256 (asymmetric) का उपयोग करें; HS256 (symmetric) भी स्वीकार्य है यदि shared secrets अच्छी तरह managed हों।
- **Validate**: हमेशा signature, issuer (`iss`), audience (`aud`), और expiration (`exp`) verify करें।
- **Keep short expiration**: access tokens के लिए 15–60 minutes; लंबी sessions के लिए refresh tokens का उपयोग करें।
- **Store securely**: JWTs को localStorage में कभी store न करें (XSS के प्रति संवेदनशील); इसके बजाय HTTP-only cookies का उपयोग करें।

---

## API Security

### Authentication
- API calls को हमेशा authenticate करें (public endpoints को छोड़कर)।
- Basic auth की तुलना में API keys या OAuth2 tokens को प्राथमिकता दें (क्योंकि basic auth हर request में credentials भेजता है)।

### Rate Limiting and Throttling
- Abuse और DoS रोकने के लिए प्रति-user और प्रति-IP rate limits लागू करें।
- `429 Too Many Requests` को `Retry-After` header के साथ लौटाएँ।

### CORS (Cross-Origin Resource Sharing)
- केवल specific origins को allow करें (production में कभी `*` नहीं)।
- Server side पर `Origin` header validate करें।

### Input Validation
- Headers और body सहित सभी request parameters validate करें।
- अप्रत्याशित fields को reject करें (`"strict": true` या JSON Schema में `additionalProperties: false`)।

### HTTPS / TLS
- Production में HTTPS अनिवार्य करें।
- Browsers को HTTPS उपयोग करने के लिए force करने हेतु HSTS (HTTP Strict Transport Security) का उपयोग करें।
- TLS 1.2 या 1.3 का उपयोग करें (TLS 1.0/1.1 disable करें)।

---

## Secrets Management

### Secrets को कभी Hardcode न करें
- Secrets (API keys, passwords, database URLs) को source control में commit न करें।
- Environment variables या secret management tools का उपयोग करें।

### Tools
- **HashiCorp Vault**: enterprise-grade, dynamic secrets।
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: cloud-native।
- **SOPS**: files में secrets encrypt करें और उन्हें commit करें (KMS या GPG के साथ)।
- **Docker secrets**: Swarm mode के लिए; Kubernetes secrets (base64-encoded, लेकिन सावधानी से उपयोग करें; external Secrets Store CSI driver पर विचार करें)।

### Rotation
- Secrets और service accounts को नियमित रूप से rotate करें।
- जहाँ संभव हो, rotation को automate करें।

---

## Dependency Management

### Vulnerability Scanning
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **General**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Patching
- Dependencies को patched versions तक updated रखें।
- Minor/patch updates के लिए automated pull requests सेट करें।
- Breaking changes के लिए changelogs की समीक्षा करें।

### Supply Chain Integrity
- Reproducible builds सुनिश्चित करने के लिए package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) का उपयोग करें।
- Download की गई dependencies के checksums verify करें।
- Official registries को प्राथमिकता दें और केवल verified publishers पर भरोसा करें।

---

## Infrastructure Security

### Firewalls
- उन inbound ports को छोड़कर बाकी सब block करें जिनकी स्पष्ट रूप से आवश्यकता हो (उदा., 80, 443)।
- SSH access को specific IP ranges तक सीमित करें (या VPN/bastion host उपयोग करें)।
- Fine-grained control के लिए security groups (AWS) या NSGs (Azure) का उपयोग करें।

### OS Hardening
- Security updates नियमित रूप से लागू करें (`sudo apt upgrade`, `yum update`)।
- अनावश्यक services और default accounts disable करें।
- SSH पर brute-force attempts रोकने के लिए fail2ban का उपयोग करें।
- SSH को harden करें: root login disable करें, key-based auth उपयोग करें, default port बदलें (optional)।

### Network Segmentation
- Databases और caches को private subnets में रखें जहाँ internet access न हो।
- Public-facing services के लिए DMZ का उपयोग करें।
- Network access पर least privilege के सिद्धांत को लागू करें।

### Infrastructure में Secrets
- CI/CD environment variables में secrets कभी store न करें जब तक वे encrypted न हों।
- Long-lived keys के बजाय EC2/VM instances के लिए cloud provider की IAM roles का उपयोग करें।

---

## Logging and Monitoring

### क्या Log करें
- Authentication events (success/failure)।
- Access control decisions (authorisation failures)।
- Admin actions (user creation, deletion, permission changes)।
- Database schema changes।
- System errors और exceptions।
- API requests और responses (sensitive data redact करके)।

### क्या Log न करें
- Passwords, secrets, tokens, PII (Personal Identifiable Information), जब तक वे hashed/redacted न हों।
- Full credit card numbers।

### Alerting
- इन स्थितियों के लिए alerts सेट करें:
  - कई failed logins (संभावित brute force)।
  - असामान्य access patterns (उदा., नई locations से, या अजीब समय पर)।
  - नए admin accounts का बनना।
  - उच्च error rates या latency spikes।
- उन्नत correlation के लिए SIEM (Security Information and Event Management) का उपयोग करें।

### Log Retention
- Regulatory requirements के अनुसार logs को कम से कम 30–90 days तक रखें।
- Logs को centralised, tamper-evident system में store करें (उदा., ELK Stack, Splunk, Datadog)।

---

## Secure Development Lifecycle (SDL)

1. **Training**: सुनिश्चित करें कि developers सामान्य vulnerabilities को समझते हों।
2. **Threat modelling**: design की शुरुआत में संभावित threats की पहचान करें।
3. **Secure coding standards**: linters और code review checklists के माध्यम से enforce करें।
4. **SAST** (Static Application Security Testing): vulnerabilities के लिए source code scan करें (SonarQube, CodeQL)।
5. **DAST** (Dynamic Application Security Testing): चल रही applications scan करें (OWASP ZAP, Burp Suite)।
6. **SCA** (Software Composition Analysis): dependencies scan करें।
7. **Penetration testing**: नियमित ethical hacking exercises।
8. **Bug bounty**: external researchers को ज़िम्मेदारीपूर्वक vulnerabilities खोजने के लिए प्रोत्साहित करें।
9. **Incident response plan**: breach detect होने पर स्पष्ट योजना तैयार रखें।

---

## Emergency Checklist (जब Breach की आशंका हो)

1. **घबराएँ नहीं** — लेकिन जल्दी कार्रवाई करें।
2. **Isolate** करें प्रभावित systems को (ज़रूरत हो तो network से disconnect करें)।
3. **Evidence सुरक्षित रखें**: logs, memory dumps, और disk images capture करें।
4. **Identify** करें दायरा: कौन-से systems, कौन-सा data।
5. **Rotate** करें सभी compromised credentials और secrets।
6. **Patch** करें vulnerability को।
7. आवश्यकता होने पर प्रभावित users और regulatory bodies को सूचित करें (कानूनी समयसीमाओं के भीतर)।
8. **Post-mortem** करें ताकि root cause समझा जा सके और processes बेहतर हों।
