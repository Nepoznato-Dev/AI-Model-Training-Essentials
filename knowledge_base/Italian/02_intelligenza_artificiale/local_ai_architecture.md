# Architettura IA locale

Una guida pratica per eseguire modelli linguistici di grandi dimensioni interamente sul dispositivo: considerazioni sull'hardware, motori di inferenza, ottimizzazione della memoria e progettazione del sistema per l'implementazione edge.

---

## Perché eseguire l'intelligenza artificiale a livello locale?

- **Privacy**: nessun dato lascia il dispositivo.
- **Costo**: nessuna commissione API per token.
- **Latenza**: inferenza prevedibile e senza rete.
- **Disponibilità offline**: funziona senza Internet.
- **Control**: controllo completo sulla versione del modello, sulla personalizzazione e sulla messa a punto.

---

## Requisiti hardware

### Memoria GPU (VRAM)
La risorsa più critica. Dimensioni del modello in memoria ≈ **parametri × byte per parametro**.

| Precisione | Byte per parametro | Modello 3.8B | Modello 7B | Modello 13B | Modello 70B |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32 | 4| ~15GB | ~28GB | ~52GB | ~280GB |
| FP16 | 2| ~7,6GB | ~14GB | ~26GB | ~140GB |
| INT8 (8 bit) | 1| ~3,8GB | ~7GB | ~13GB | ~70GB |
| INT4 (4 bit) | 0,5 | ~1,9GB | ~3,5GB | ~6,5GB | ~35GB |

**Linee guida pratiche:**
- VRAM da 8 GB → modelli fino a 7B a 4 bit.
- VRAM da 12 GB → modelli fino a 13B a ​​4 bit.
- VRAM da 24 GB → modelli fino a 70B a 4 bit (o 13B a ​​8 bit).
- Apple Silicon (memoria unificata) può eseguire modelli da 70B su sistemi da 64GB+.

### RAM (memoria di sistema)
- Per l'inferenza della CPU, è necessaria una RAM di sistema sufficiente per caricare il modello (simile ai numeri VRAM).
- Per l'inferenza della GPU, la RAM di sistema è importante per caricare il modello in memoria prima di scaricarlo su VRAM.

### Archiviazione
- I pesi dei modelli quantizzati occupano alcuni GB (ad esempio, 7B a 4 bit ≈ 4 GB su disco). Assicurati che ci siano almeno 20-50 GB liberi per più modelli.

###CPU
- Per l'elaborazione rapida (precompilazione) e lo scarico della CPU, una moderna CPU multi-core aiuta.
- I chip Apple serie M offrono prestazioni eccellenti per i LLM grazie alla memoria unificata e al Neural Engine.

---

## Quantizzazione

La quantizzazione riduce la precisione numerica dei pesi, riducendo drasticamente la memoria e aumentando la velocità con un piccolo costo in termini di precisione.

### Formati popolari

| Formato | Bit | Descrizione | Uso tipico |
|--------|------|-----|-------------|
| **GGUF** | 4–8 | Formato llama.cpp, ottimizzato per CPU/GPU ibrida | Ideale per l'inferenza locale |
| **GPTQ** | 4–8 | Solo GPU, efficiente su CUDA | Il meglio per le GPU NVIDIA |
| **AWQ** | 4| Con riconoscimento dell'attivazione, solo GPU | Buono per l'inferenza batch sulle GPU |
| **ONNX** | variabile | Standardizzato e multipiattaforma | Produzione che serve |

### Scelta di un livello di quantizzazione
- **Q8_0** (8 bit): perdita di qualità minima, dimensione massima.
- **Q6_K** (6 bit): buona qualità, compressione decente.
- **Q5_K_M** (5 bit): punto debole comune.
- **Q4_K_M** (4 bit): qualità più piccola e accettabile per la maggior parte delle attività.
- **IQ4_XS** / **IQ3_XS**: Quantizzazione migliorata con migliore perplessità a 4/3 bit.

**Regola pratica:** utilizza Q4_K_M per un buon equilibrio tra qualità e dimensioni. Se hai VRAM extra, usa Q5 o Q6.

---

## Motori di inferenza (locali)

### lama.cpp
- Scritto in C++.
- Supporta il formato GGUF.
- Ottimizzato per CPU e GPU (tramite CUDA, Metal, OpenCL).
- Molto veloce, soprattutto sulla CPU.
- Riga di comando, modalità server e collegamenti Python.

**Comando di esempio:**
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

```ribasso
# Migliori pratiche di sicurezza

Una guida pratica per proteggere applicazioni, infrastrutture e dati, dallo sviluppo alla produzione.

---

## OWASP Top 10 (2021) — Panoramica

1. **Controllo accesso interrotto**: gli utenti possono accedere a risorse a cui non dovrebbero.
2. **Errori crittografici**: crittografia debole o mancante.
3. **Injection**: SQL, NoSQL, comando del sistema operativo o injection LDAP.
4. **Design insicuro**: difetti architettonici.
5. **Errore di configurazione della sicurezza**: password predefinite, porte aperte, errori dettagliati.
6. **Componenti vulnerabili e obsoleti**: CVE noti nelle dipendenze.
7. **Errori di identificazione e autenticazione**: password deboli, cattiva gestione delle sessioni.
8. **Errori di integrità del software e dei dati**: attacchi alla catena di fornitura, aggiornamenti non firmati.
9. **Errori di registrazione e monitoraggio della sicurezza**: nessun rilevamento di violazioni.
10. **Server-Side Request Forgery (SSRF)**: abuso del server per effettuare richieste ai sistemi interni.

---

## Convalida dell'input e codifica dell'output

### Regole di convalida
- **Lista bianca > Lista nera**: definisce i modelli consentiti (ad esempio, regex per la posta elettronica) anziché bloccare i modelli dannosi noti.
- **Limiti di lunghezza**: applica lunghezze massime per prevenire overflow del buffer e DoS.
- **Controllo del tipo**: garantisce che i numeri interi siano numeri interi e che i booleani siano booleani.
- **Utilizza librerie ben testate**: per la convalida di email, URL e data, utilizza librerie standard (ad esempio, `email-validator` in Python, `validator.js` in Node).### Codifica dell'output
- **Codifica HTML**: codifica `<`, `>`, `&`, `"`, `'` per impedire XSS.
- **Parametrizzazione SQL**: non concatenare mai l'input dell'utente in query SQL. Utilizzare query parametrizzate (istruzioni preparate) o un ORM.
- **Escape della shell**: evita di creare comandi della shell dall'input dell'utente; se inevitabile, utilizzare `shlex.quote()` o simile.

---

## Autenticazione e autorizzazione

### gestione delle password
- **Hashing**: archivia le password con un algoritmo di hashing potente e lento: **Argon2id** (preferito), **bcrypt**, **scrypt** o **PBKDF2**.
- **Salting**: aggiungi un salt univoco per utente.
- **Lunghezza minima**: applica almeno 12-16 caratteri.
- **MFA (Multi-Factor Authentication)**: richiede un secondo fattore (TOTP, SMS, chiave hardware) per operazioni sensibili.
- **Limitazione della velocità**: impedisce i tentativi di forza bruta sugli endpoint di accesso (ad esempio, 5 tentativi ogni 5 minuti per IP/utente).

### gestione delle sessioni
- Utilizzare cookie sicuri, solo HTTP, SameSite per i token di sessione.
- Impostare tempi di scadenza appropriati.
- Invalidare le sessioni al logout e al cambio password.
- Evitare di esporre gli ID di sessione negli URL.

### OAuth2/OIDC
- Utilizzare librerie consolidate (ad esempio Authlib, PyJWT, Passport.js, Spring Security).
- Convalida accuratamente i token ID (firma, emittente, pubblico, scadenza).
- Utilizzare i parametri di stato per prevenire CSRF.
- Mantenere riservati i segreti dei clienti.

### JWT (token Web JSON)
- **Segna**: utilizza RS256 o ES256 (asimmetrico) per una migliore sicurezza; HS256 (simmetrico) è accettabile se i segreti condivisi vengono gestiti correttamente.
- **Convalida**: verifica sempre la firma, l'emittente (`iss`), il pubblico (`aud`) e la scadenza (`exp`).
- **Mantieni scadenza breve**: 15–60 minuti per i token di accesso; utilizzare i token di aggiornamento per sessioni più lunghe.
- **Archivia in modo sicuro**: non archiviare mai i JWT in localStorage (vulnerabile a XSS); utilizzare invece cookie solo HTTP.

---

## Sicurezza dell'API

### Autenticazione
- Autenticare sempre le chiamate API (eccetto gli endpoint pubblici).
- Preferire chiavi API o token OAuth2 rispetto all'autenticazione di base (che invia credenziali a ogni richiesta).

### Limitazione e limitazione della velocità
- Applicare limiti di velocità per utente e per IP per prevenire abusi e DoS.
- Restituisce `429 Too Many Requests` con un'intestazione `Retry-After`.

### CORS (condivisione di risorse tra origini)
- Consentire solo origini specifiche (mai `*` in produzione).
- Convalida l'intestazione `Origin` sul lato server.

### Convalida dell'input
- Convalida tutti i parametri della richiesta, incluse intestazioni e corpo.
- Rifiuta campi imprevisti (`"strict": true` o `additionalProperties: false` nello schema JSON).

### HTTPS/TLS
- Applicare HTTPS in produzione.
- Utilizza HSTS (HTTP Strict Transport Security) per forzare i browser a utilizzare HTTPS.
- Utilizza TLS 1.2 o 1.3 (disabilita TLS 1.0/1.1).

---

## gestione dei segreti

### Non codificare mai i segreti
- Non impegnare segreti (chiavi API, password, URL di database) nel controllo del codice sorgente.
- Utilizzare variabili di ambiente o strumenti di gestione dei segreti.

### Strumenti
- **HashiCorp Vault**: segreti dinamici di livello aziendale.
- **AWS Secrets Manager/Azure Key Vault/GCP Secret Manager**: nativo del cloud.
- **SOPS**: crittografa i segreti nei file e li conferma (con KMS o GPG).
- **Segreti Docker**: per la modalità Swarm; Segreti Kubernetes (codifica base64, ma da usare con cautela; considerare il driver CSI Secrets Store esterno).

### Rotazione
- Ruota regolarmente i segreti e gli account di servizio.
- Automatizzare la rotazione ove possibile.

---

## gestione delle dipendenze

### Scansione delle vulnerabilità
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Nodo**: `npm audit`, `yarn audit`, `snyk`.
- **Ruggine**: `cargo audit`.
- **Vai**: `govulncheck`.
- **Generale**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Patch
- Mantieni le dipendenze aggiornate alle versioni con patch.
- Impostazione di richieste pull automatizzate per aggiornamenti minori/patch.
- Esamina i log delle modifiche per individuare eventuali modifiche sostanziali.

### Integrità della catena di fornitura
- Utilizzare i file di blocco dei pacchetti (`package-lock.json`, `Cargo.lock`, `go.sum`) per garantire build riproducibili.
- Verificare i checksum delle dipendenze scaricate.
- Preferisci i registri ufficiali e fidati solo degli editori verificati.

---

## Sicurezza delle infrastrutture

### Firewall
- Blocca tutte le porte in entrata tranne quelle esplicitamente necessarie (ad esempio, 80, 443).
- Limita l'accesso SSH a intervalli IP specifici (o utilizza un host VPN/bastione).
- Utilizza gruppi di sicurezza (AWS) o NSG (Azure) per un controllo granulare.

### Rafforzamento del sistema operativo
- Applicare regolarmente gli aggiornamenti di sicurezza (`sudo apt upgrade`, `yum update`).
- Disattiva i servizi non necessari e gli account predefiniti.
- Usa fail2ban per bloccare i tentativi di forza bruta su SSH.
- Rafforzare SSH: disabilita l'accesso root, usa l'autenticazione basata su chiave, cambia la porta predefinita (opzionale).### Segmentazione della rete
- Posiziona database e cache in sottoreti private senza accesso a Internet.
- Utilizzare una DMZ per i servizi rivolti al pubblico.
- Applicare il principio del privilegio minimo all'accesso alla rete.

### Segreti nelle infrastrutture
- Non archiviare mai i segreti nelle variabili di ambiente CI/CD a meno che non siano crittografati.
- Utilizza i ruoli IAM del fornitore di servizi cloud per le istanze EC2/VM invece delle chiavi di lunga durata.

---

## Registrazione e monitoraggio

### Cosa registrare
- Eventi di autenticazione (successo/fallimento).
- Decisioni di controllo degli accessi (mancate autorizzazioni).
- Azioni di amministrazione (creazione di utenti, eliminazione, modifiche delle autorizzazioni).
- Modifiche allo schema del database.
- Errori ed eccezioni di sistema.
- Richieste e risposte API (cancellare dati sensibili).

### Cosa non registrare
- Password, segreti, token, PII (informazioni di identificazione personale) a meno che non siano sottoposte ad hashing/censurate.
- Numeri completi delle carte di credito.

### Avviso
- Imposta avvisi per:
  - Numerosi accessi non riusciti (potenziale forza bruta).
  - Schemi di accesso insoliti (ad esempio, da nuove località, in orari strani).
  - Nuovi account amministratore creati.
  - Tassi di errore elevati o picchi di latenza.
- Utilizzare un SIEM (Security Information and Event Management) per la correlazione avanzata.

### Conservazione dei registri
- Conservare i registri per almeno 30-90 giorni a seconda dei requisiti normativi.
- Archiviare i log in un sistema centralizzato a prova di manomissione (ad esempio, ELK Stack, Splunk, Datadog).

---

## Ciclo di vita dello sviluppo sicuro (SDL)

1. **Formazione**: assicurati che gli sviluppatori comprendano le vulnerabilità comuni.
2. **Modellazione delle minacce**: identificare le potenziali minacce nelle prime fasi della progettazione.
3. **Standard di codifica sicuri**: applicazione tramite linter e liste di controllo per la revisione del codice.
4. **SAST** (Static Application Security Testing): scansione del codice sorgente per individuare eventuali vulnerabilità (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): scansione delle applicazioni in esecuzione (OWASP ZAP, Burp Suite).
6. **SCA** (Analisi della composizione software): scansione delle dipendenze.
7. **Test di penetrazione**: esercizi regolari di hacking etico.
8. **Bug bounty**: incoraggia i ricercatori esterni a individuare le vulnerabilità in modo responsabile.
9. **Piano di risposta agli incidenti**: disporre di un piano chiaro per quando viene rilevata una violazione.

---

## Lista di controllo di emergenza (quando si sospetta una violazione)

1. **Non farti prendere dal panico**, ma agisci rapidamente.
2. **Isolare** i sistemi interessati (disconnettersi dalla rete se necessario).
3. **Conserva prove**: acquisisci log, dump della memoria e immagini del disco.
4. **Identificare** l'ambito: quali sistemi, quali dati.
5. **Ruota** tutte le credenziali e i segreti compromessi.
6. **Correggere** la vulnerabilità.
7. **Informare** gli utenti interessati e gli organismi di regolamentazione, se necessario (entro i termini legali).
8. **Condurre un'autopsia** per comprendere la causa principale e migliorare i processi.