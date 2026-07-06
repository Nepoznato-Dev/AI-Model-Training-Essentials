# Lokalna architektura AI

Praktyczny przewodnik po uruchamianiu dużych modeli językowych całkowicie na urządzeniu — kwestie sprzętowe, silniki wnioskowania, optymalizacja pamięci i projektowanie systemów pod kątem wdrażania brzegowego.

---

## Po co uruchamiać sztuczną inteligencję lokalnie?

- **Prywatność**: Żadne dane nie opuszczają urządzenia.
- **Koszt**: Brak opłat API za token.
- **Opóźnienie**: Przewidywalne wnioskowanie bez konieczności korzystania z sieci.
- **Dostępność offline**: Działa bez Internetu.
- **Kontrola**: Pełna kontrola nad wersją modelu, dostosowywaniem i dostrajaniem.

---

## Wymagania sprzętowe

### Pamięć GPU (VRAM)
Najbardziej krytyczny zasób. Rozmiar modelu w pamięci ≈ **parametry × bajty na parametr**.

| Precyzja | Bajty na parametr | Model 3.8B | Model 7B | Model 13B | model 70B |
|-----------|-------|------------|----------|----------------|----------------|
| FP32 | 4 | ~15 GB | ~28 GB | ~52 GB | ~280 GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26 GB | ~140 GB |
| INT8 (8-bitowy) | 1 | ~3,8 GB | ~7 GB | ~13 GB | ~70 GB |
| INT4 (4-bitowy) | 0,5 | ~1,9 GB | ~3,5 GB | ~6,5 GB | ~35 GB |

**Praktyczne wskazówki:**
- 8 GB VRAM → modele do 7B przy 4-bitach.
- 12 GB VRAM → do 13B modeli w trybie 4-bitowym.
- 24 GB VRAM → modele do 70B przy 4-bitach (lub 13B przy 8-bitach).
- Apple Silicon (ujednolicona pamięć) może obsługiwać modele 70B w systemach 64 GB+.

### RAM (pamięć systemowa)
- Do wnioskowania o procesorze potrzebna jest wystarczająca ilość systemowej pamięci RAM, aby załadować model (podobnie jak numery VRAM).
— W przypadku procesora graficznego pamięć systemowa ma znaczenie przy ładowaniu modelu do pamięci przed przeniesieniem do VRAM.

### Przechowywanie
- Skwantowane wagi modeli zajmują kilka GB (np. 4-bitowy 7B ≈ 4 GB na dysku). Zapewnij co najmniej 20–50 GB wolnego miejsca dla wielu modeli.

### Procesor
- Do szybkiego przetwarzania (wstępnego napełniania) i odciążania procesora pomaga nowoczesny wielordzeniowy procesor.
- Chipy Apple z serii M charakteryzują się doskonałą wydajnością w przypadku LLM dzięki ujednoliconej pamięci i silnikowi neuronowemu.

---

## Kwantyzacja

Kwantyzacja zmniejsza precyzję numeryczną odważników, radykalnie zmniejszając pamięć i zwiększając prędkość przy niewielkim koszcie dokładności.

### Popularne formaty

| Formatuj | Bity | Opis | Typowe zastosowanie |
|------------|------|------------|------------|
| **GGUF** | 4–8 | Format llama.cpp, zoptymalizowany pod kątem hybrydy CPU/GPU | Najlepsze do wnioskowania lokalnego |
| **GPTQ** | 4–8 | Tylko GPU, wydajny na CUDA | Najlepsze dla procesorów graficznych NVIDIA |
| **AWQ** | 4 | Obsługuje aktywację, tylko GPU | Dobre do wnioskowania wsadowego na procesorach graficznych |
| **ONNX** | zmienna | Standaryzowany, wieloplatformowy | Produkcja serwująca |

### Wybór poziomu kwantyzacji
- **Q8_0** (8-bit): minimalna utrata jakości, największy rozmiar.
- **Q6_K** (6-bit): dobra jakość, przyzwoita kompresja.
- **Q5_K_M** (5-bitowy): wspólny słodki punkt.
- **Q4_K_M** (4-bitowy): najmniejsza, akceptowalna jakość dla większości zadań.
- **IQ4_XS** / **IQ3_XS**: Ulepszona kwantyzacja z większą złożonością przy 4/3 bitach.

**Ogólna zasada:** Użyj Q4_K_M, aby uzyskać dobrą równowagę jakości i rozmiaru. Jeśli masz dodatkową pamięć VRAM, użyj Q5 lub Q6.

---

## Silniki wnioskowania (lokalne)

### lama.cpp
- Napisane w C++.
- Obsługuje format GGUF.
- Zoptymalizowany pod kątem procesora i karty graficznej (poprzez CUDA, Metal, OpenCL).
- Bardzo szybki, zwłaszcza na procesorze.
- Wiersz poleceń, tryb serwera i powiązania Python.

**Przykładowe polecenie:**
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

```przecena
# Najlepsze praktyki dotyczące bezpieczeństwa

Praktyczny przewodnik po zabezpieczaniu aplikacji, infrastruktury i danych — od programowania po produkcję.

---

## OWASP Top 10 (2021) — przegląd

1. **Zepsuta kontrola dostępu**: Użytkownicy mogą uzyskać dostęp do zasobów, do których nie powinni.
2. **Awarie kryptograficzne**: Słabe lub brakujące szyfrowanie.
3. **Wstrzykiwanie**: SQL, NoSQL, polecenie systemu operacyjnego lub wstrzyknięcie LDAP.
4. **Niepewny projekt**: Wady architektoniczne.
5. **Błędna konfiguracja zabezpieczeń**: Domyślne hasła, otwarte porty, szczegółowe błędy.
6. **Wrażliwe i nieaktualne komponenty**: Znane CVE w zależnościach.
7. **Błędy identyfikacji i uwierzytelnienia**: Słabe hasła, złe zarządzanie sesją.
8. **Awarie integralności oprogramowania i danych**: Ataki na łańcuch dostaw, niepodpisane aktualizacje.
9. **Błędy rejestrowania i monitorowania bezpieczeństwa**: Brak wykrycia naruszeń.
10. **Fałszowanie żądań po stronie serwera (SSRF)**: Nadużycie serwera w celu wysyłania żądań do systemów wewnętrznych.

---

## Walidacja danych wejściowych i kodowanie wyjściowe

### Zasady walidacji
- **Biała lista > Czarna lista**: Zdefiniuj dozwolone wzorce (np. wyrażenie regularne dla wiadomości e-mail) zamiast blokować znane złe wzorce.
- **Ograniczenia długości**: wymuszają maksymalne długości, aby zapobiec przepełnieniu bufora i DoS.
- **Sprawdzanie typu**: Upewnij się, że liczby całkowite są liczbami całkowitymi, a wartości logiczne są wartościami logicznymi.
- **Użyj dobrze przetestowanych bibliotek**: Do sprawdzania poprawności adresu e-mail, adresu URL i daty użyj bibliotek standardowych (np. `email-validator` w Pythonie, `validator.js` w Node).### Kodowanie wyjściowe
- **Kodowanie HTML**: Zakoduj `<`, `>`, `&`, `"`, `'`, aby zapobiec XSS.
- **Parametryzacja SQL**: Nigdy nie łącz danych wejściowych użytkownika z zapytaniami SQL. Użyj sparametryzowanych zapytań (przygotowanych instrukcji) lub ORM.
- **Ucieczka powłoki**: Unikaj tworzenia poleceń powłoki na podstawie danych wprowadzonych przez użytkownika; jeśli jest to nieuniknione, użyj `shlex.quote()` lub podobnego.

---

## Uwierzytelnianie i autoryzacja

### Zarządzanie hasłami
- **Haszowanie**: Przechowuj hasła przy użyciu silnego, powolnego algorytmu mieszania: **Argon2id** (preferowany), **bcrypt**, **scrypt** lub **PBKDF2**.
- **Solenie**: Dodaj unikalną sól dla każdego użytkownika.
- **Minimalna długość**: Wymuś co najmniej 12–16 znaków.
- **MFA (Uwierzytelnianie wieloskładnikowe)**: Wymaga drugiego czynnika (TOTP, SMS, klucz sprzętowy) w przypadku wrażliwych operacji.
- **Ograniczenie szybkości**: Zapobiegaj próbom użycia siły na punktach końcowych logowania (np. 5 prób na 5 minut na adres IP/użytkownika).

### Zarządzanie sesją
- Używaj bezpiecznych plików cookie SameSite obsługujących wyłącznie protokół HTTP dla tokenów sesji.
- Ustaw odpowiednie czasy ważności.
- Unieważnij sesje po wylogowaniu i zmianie hasła.
- Unikaj ujawniania identyfikatorów sesji w adresach URL.

### OAuth2 / OIDC
- Korzystaj ze sprawdzonych bibliotek (np. Authlib, PyJWT, Passport.js, Spring Security).
- Dokładnie zweryfikuj tokeny identyfikacyjne (podpis, wydawca, odbiorcy, data ważności).
- Użyj parametrów stanu, aby zapobiec CSRF.
- Zachowaj tajemnicę klienta w tajemnicy.

### JWT (tokeny internetowe JSON)
- **Znak**: Użyj RS256 lub ES256 (asymetryczny) dla większego bezpieczeństwa; HS256 (symetryczny) jest akceptowalny, jeśli dobrze zarządza się wspólnymi sekretami.
- **Weryfikuj**: Zawsze sprawdzaj podpis, wydawcę (`iss`), odbiorców (`aud`) i datę ważności (`exp`).
- **Zachowaj krótki okres ważności**: 15–60 minut dla tokenów dostępu; używaj tokenów odświeżania w przypadku dłuższych sesji.
- **Przechowuj bezpiecznie**: Nigdy nie przechowuj JWT w localStorage (podatny na XSS); zamiast tego używaj plików cookie obsługujących wyłącznie protokół HTTP.

---

## Bezpieczeństwo API

### Uwierzytelnianie
- Zawsze uwierzytelniaj wywołania API (z wyjątkiem publicznych punktów końcowych).
- Preferuj klucze API lub tokeny OAuth2 zamiast uwierzytelniania podstawowego (które wysyła dane uwierzytelniające na każde żądanie).

### Ograniczanie szybkości i ograniczanie przepustowości
- Zastosuj limity szybkości dla użytkownika i adresu IP, aby zapobiec nadużyciom i DoS.
- Zwróć `429 Too Many Requests` z nagłówkiem `Retry-After`.

### CORS (współdzielenie zasobów między źródłami)
- Zezwalaj tylko na określone źródła (nigdy `*` w produkcji).
- Sprawdź nagłówek `Origin` po stronie serwera.

### Walidacja danych wejściowych
- Sprawdź wszystkie parametry żądania, w tym nagłówki i treść.
- Odrzuć nieoczekiwane pola (`"strict": true` lub `additionalProperties: false` w schemacie JSON).

### HTTPS/TLS
— Wymuś protokół HTTPS w środowisku produkcyjnym.
- Użyj HSTS (HTTP Strict Transport Security), aby zmusić przeglądarki do korzystania z protokołu HTTPS.
- Użyj TLS 1.2 lub 1.3 (wyłącz TLS 1.0/1.1).

---

## Zarządzanie tajemnicami

### Nigdy nie ma sekretów kodowanych na stałe
- Nie przekazuj sekretów (kluczy API, haseł, adresów URL baz danych) kontroli źródła.
- Używaj zmiennych środowiskowych lub narzędzi do zarządzania sekretami.

### Narzędzia
- **HashiCorp Vault**: dynamiczne sekrety klasy korporacyjnej.
- **Menedżer sekretów AWS / Azure Key Vault / Menedżer sekretów GCP**: Natywny w chmurze.
- **SOPS**: Szyfruj sekrety w plikach i zatwierdzaj je (za pomocą KMS lub GPG).
- **Sekrety Dokera**: Dla trybu Roju; Sekrety Kubernetes (zakodowane w formacie Base64, ale używaj ich ostrożnie; rozważ zewnętrzny sterownik CSI magazynu sekretów).

### Obrót
- Regularnie zmieniaj sekrety i konta usług.
- Automatyzuj rotację tam, gdzie to możliwe.

---

## Zarządzanie zależnościami

### Skanowanie pod kątem luk w zabezpieczeniach
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Węzeł**: `npm audit`, `yarn audit`, `snyk`.
- **Rdza**: `cargo audit`.
- **Idź**: `govulncheck`.
- **Ogólne**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Łatanie
- Aktualizuj zależności do poprawionych wersji.
- Skonfiguruj automatyczne żądania ściągnięcia dla mniejszych aktualizacji/łatek.
- Przejrzyj dzienniki zmian pod kątem istotnych zmian.

### Integralność łańcucha dostaw
- Użyj plików blokujących pakiety (`package-lock.json`, `Cargo.lock`, `go.sum`), aby zapewnić powtarzalność kompilacji.
- Sprawdź sumy kontrolne pobranych zależności.
- Preferuj oficjalne rejestry i ufaj tylko zweryfikowanym wydawcom.

---

## Bezpieczeństwo infrastruktury

### Zapory sieciowe
- Blokuj wszystkie porty przychodzące z wyjątkiem tych wyraźnie potrzebnych (np. 80, 443).
- Ogranicz dostęp SSH do określonych zakresów IP (lub użyj hosta VPN/bastionu).
— Użyj grup zabezpieczeń (AWS) lub sieciowych grup zabezpieczeń (Azure), aby uzyskać precyzyjną kontrolę.

### Hartowanie systemu operacyjnego
- Regularnie stosuj aktualizacje zabezpieczeń (`sudo apt upgrade`, `yum update`).
- Wyłącz niepotrzebne usługi i konta domyślne.
- Użyj funkcji Fail2ban, aby zablokować próby brutalnej siły na SSH.
- Wzmocnij SSH: wyłącz logowanie roota, użyj uwierzytelniania na podstawie klucza, zmień domyślny port (opcjonalnie).### Segmentacja sieci
- Umieść bazy danych i pamięci podręczne w prywatnych podsieciach bez dostępu do Internetu.
- Korzystaj ze strefy DMZ dla usług publicznych.
- Zastosuj zasadę najmniejszych uprawnień w dostępie do sieci.

### Sekrety infrastruktury
- Nigdy nie przechowuj sekretów w zmiennych środowiskowych CI/CD, chyba że są one zaszyfrowane.
- Używaj ról IAM dostawcy chmury dla instancji EC2/VM zamiast kluczy długotrwałych.

---

## Rejestrowanie i monitorowanie

### Co rejestrować
- Zdarzenia uwierzytelniające (sukces/niepowodzenie).
- Decyzje dotyczące kontroli dostępu (błędy autoryzacyjne).
- Działania administracyjne (tworzenie użytkowników, usuwanie, zmiany uprawnień).
- Zmiany schematu bazy danych.
- Błędy systemowe i wyjątki.
- Żądania i odpowiedzi API (redagowanie wrażliwych danych).

### Czego nie rejestrować
- Hasła, tajemnice, tokeny, PII (dane osobowe), chyba że zostały zaszyfrowane/zredagowane.
- Pełne numery kart kredytowych.

### Alarmowanie
- Skonfiguruj alerty dla:
  - Wiele nieudanych logowań (potencjalna brutalna siła).
  - Nietypowe wzorce dostępu (np. z nowych lokalizacji, w nieparzystych godzinach).
  - Utworzono nowe konta administratorów.
  - Wysoki poziom błędów lub skoki opóźnień.
- Użyj SIEM (zarządzanie informacjami o bezpieczeństwie i zdarzeniami) w celu uzyskania zaawansowanej korelacji.

### Przechowywanie dziennika
- Przechowuj dzienniki przez co najmniej 30–90 dni, w zależności od wymogów prawnych.
- Przechowuj logi w scentralizowanym systemie zabezpieczającym przed manipulacją (np. ELK Stack, Splunk, Datadog).

---

## Bezpieczny cykl życia oprogramowania (SDL)

1. **Szkolenie**: Upewnij się, że programiści rozumieją typowe luki w zabezpieczeniach.
2. **Modelowanie zagrożeń**: Zidentyfikuj potencjalne zagrożenia na wczesnym etapie projektowania.
3. **Bezpieczne standardy kodowania**: Egzekwuj za pomocą lintersów i list kontrolnych przeglądu kodu.
4. **SAST** (statyczne testowanie bezpieczeństwa aplikacji): Skanuj kod źródłowy pod kątem luk w zabezpieczeniach (SonarQube, CodeQL).
5. **DAST** (Dynamiczne testowanie bezpieczeństwa aplikacji): Skanuj uruchomione aplikacje (OWASP ZAP, Burp Suite).
6. **SCA** (Analiza składu oprogramowania): Zależności skanowania.
7. **Testy penetracyjne**: Regularne ćwiczenia etycznego hakowania.
8. **Nagroda za błąd**: Zachęcaj zewnętrznych badaczy do odpowiedzialnego wyszukiwania luk w zabezpieczeniach.
9. **Plan reagowania na incydenty**: Miej jasny plan na wypadek wykrycia naruszenia.

---

## Awaryjna lista kontrolna (w przypadku podejrzenia naruszenia)

1. **Nie panikuj** – ale działaj szybko.
2. **Odizoluj** systemy, których dotyczy problem (w razie potrzeby odłącz od sieci).
3. **Zachowaj dowody**: Przechwytuj dzienniki, zrzuty pamięci i obrazy dysków.
4. **Określ** zakres: jakie systemy, jakie dane.
5. **Obróć** wszystkie skompromitowane dane uwierzytelniające i sekrety.
6. **Załataj** lukę.
7. **Powiadom** zainteresowanych użytkowników i organy regulacyjne, jeśli jest to wymagane (w terminach prawnych).
8. **Przeprowadź sekcję zwłok**, aby poznać pierwotną przyczynę i ulepszyć procesy.