# Lokale AI-Architektur

Ein praktischer Leitfaden zum vollständigen Ausführen großer Sprachmodelle auf dem Gerät — Hardware-Aspekte, Inferenz-Engines, Speicheroptimierung und Systemdesign für Edge-Deployment.

---

## Warum AI lokal ausführen?

- **Datenschutz**: Keine Daten verlassen das Gerät.
- **Kosten**: Keine API-Gebühren pro Token.
- **Latenz**: Vorhersagbare Inferenz ohne Netzwerk.
- **Offline-Verfügbarkeit**: Funktioniert ohne Internet.
- **Kontrolle**: Vollständige Kontrolle über Modellversion, Anpassung und Fine-Tuning.

---

## Hardware-Anforderungen

### GPU-Speicher (VRAM)
Die kritischste Ressource. Modellgröße im Speicher ≈ **Parameter × Bytes pro Parameter**.

| Präzision | Bytes pro Parameter | 3.8B-Modell | 7B-Modell | 13B-Modell | 70B-Modell |
|-----------|---------------------|-------------|-----------|------------|------------|
| FP32      | 4                   | ~15 GB      | ~28 GB    | ~52 GB     | ~280 GB    |
| FP16      | 2                   | ~7.6 GB     | ~14 GB    | ~26 GB     | ~140 GB    |
| INT8 (8-bit) | 1              | ~3.8 GB     | ~7 GB     | ~13 GB     | ~70 GB     |
| INT4 (4-bit) | 0.5            | ~1.9 GB     | ~3.5 GB   | ~6.5 GB    | ~35 GB     |

**Praktische Richtlinien:**
- 8GB VRAM → bis zu 7B-Modelle in 4-bit.
- 12GB VRAM → bis zu 13B-Modelle in 4-bit.
- 24GB VRAM → bis zu 70B-Modelle in 4-bit (oder 13B in 8-bit).
- Apple Silicon (Unified Memory) kann 70B-Modelle auf Systemen mit 64GB+ ausführen.

### RAM (Systemspeicher)
- Für CPU-Inferenz benötigst du genügend System-RAM, um das Modell zu laden (ähnlich den VRAM-Zahlen).
- Für GPU-Inferenz ist System-RAM wichtig, um das Modell in den Speicher zu laden, bevor es in den VRAM ausgelagert wird.

### Speicherplatz
- Quantisierte Modellgewichte belegen einige GB (z. B. 4-bit 7B ≈ 4 GB auf der Festplatte). Stelle sicher, dass mindestens 20–50 GB für mehrere Modelle frei sind.

### CPU
- Für Prompt-Verarbeitung (prefill) und CPU-Offloading hilft eine moderne Multi-Core-CPU.
- Apple-M-series-Chips bieten wegen Unified Memory und Neural Engine eine ausgezeichnete Leistung für LLMs.

---

## Quantisierung

Quantisierung reduziert die numerische Präzision von Gewichten, senkt den Speicherbedarf drastisch und erhöht die Geschwindigkeit bei geringem Genauigkeitsverlust.

### Beliebte Formate

| Format | Bits | Beschreibung | Typischer Einsatz |
|--------|------|--------------|-------------------|
| **GGUF** | 4–8 | llama.cpp-Format, optimiert für CPU/GPU-Hybrid | Am besten für lokale Inferenz |
| **GPTQ** | 4–8 | Nur GPU, effizient auf CUDA | Am besten für NVIDIA-GPUs |
| **AWQ** | 4 | Activation-aware, nur GPU | Gut für Batch-Inferenz auf GPUs |
| **ONNX** | variable | Standardisiert, plattformübergreifend | Produktionsbereitstellung |

### Auswahl eines Quantisierungsniveaus
- **Q8_0** (8-bit): minimaler Qualitätsverlust, größte Größe.
- **Q6_K** (6-bit): gute Qualität, ordentliche Komprimierung.
- **Q5_K_M** (5-bit): verbreiteter Sweet Spot.
- **Q4_K_M** (4-bit): am kleinsten, akzeptable Qualität für die meisten Aufgaben.
- **IQ4_XS** / **IQ3_XS**: Verbesserte Quantisierung mit besserer Perplexity bei 4/3 Bits.

**Faustregel:** Verwende Q4_K_M für eine gute Balance aus Qualität und Größe. Wenn du zusätzlichen VRAM hast, verwende Q5 oder Q6.

---

## Inferenz-Engines (lokal)

### llama.cpp
- In C++ geschrieben.
- Unterstützt das GGUF-Format.
- Für CPU und GPU optimiert (via CUDA, Metal, OpenCL).
- Sehr schnell, besonders auf der CPU.
- Kommandozeile, Server-Modus und Python-Bindings.

**Beispielbefehl:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 lagert 32 Layers auf die GPU aus)

Ollama
Umschließt llama.cpp mit einer einfachen CLI und REST-API.

Lädt Modelle automatisch herunter und verwaltet sie.

Großartig für Prototyping und Desktop-Apps.

Unterstützt benutzerdefinierte Modelfiles für System-Prompts.

Verwendung:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Grafische Desktop-App für Windows, macOS und Linux.

Ein-Klick-Download und Chat-Oberfläche.

Eingebauter lokaler Server mit OpenAI-kompatibler API.

Gut für nichttechnische Nutzer und schnelle Tests.

Hugging Face Transformers + bitsandbytes
Die Standard-Python-Bibliothek für HF-Modelle.

Verwende bitsandbytes für 4-bit-Quantisierung (load_in_4bit=True).

Flexibler für Fine-Tuning, aber bei Inferenz langsamer als llama.cpp.

ExLlamaV2
Sehr schnelle GPU-Inferenz für GPTQ und AWQ.

Beste Leistung auf NVIDIA-GPUs.

Unterstützt Batch-Generierung.

mlx (Apple)
Apples Framework für M-series-Chips.

Stark optimiert für Apple Silicon.

Python-API.

Speicherverwaltung
Kontextfenster und KV-Cache
Der KV-Cache speichert key-value-Paare für jede Layer und jedes Token im Kontext. Er wächst linear mit der Kontextlänge.

Speicherkosten ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

Für ein 32-Layer-Modell mit 8 KV-Heads und 128 head dim kostet jedes Token ~32 × 8 × 128 × 2 Bytes = 65 KB pro Token. Bei 128k Tokens sind das ~8 GB nur für den Cache.

Offloading-Strategien
Layer-Offloading: Lege einige Layers auf die GPU, andere auf die CPU. Schneller als reine CPU, geringerer VRAM-Bedarf.

Token-Streaming: Verarbeite Tokens inkrementell statt alle auf einmal.

Prompt-Caching
Verwende KV-Caches für ähnliche Prompts wieder, um die prefill-Phase nicht erneut berechnen zu müssen. Einige Frameworks unterstützen das (z. B. vLLM, llama.cpp mit --prompt-cache).

Memory-Mapped Files
Lade Modellgewichte direkt von der Festplatte, ohne sie vollständig in den RAM zu laden (nützlich für riesige Modelle auf Systemen mit begrenztem Speicher). llama.cpp verwendet standardmäßig Memory-Mapping.

Deployment-Architekturen
Single-Device-Modus
Ein Modell läuft auf einer Maschine (Laptop, Smartphone, Edge-Gerät). Verwendet für persönliche Assistenten, Notiz-Apps, Code Completion.

Hybrid Edge-Cloud
Das lokale Modell bearbeitet häufige Anfragen; für komplexe Fragen gibt es einen Fallback auf ein Cloud-Modell. Das bietet das Beste aus beiden Welten — Geschwindigkeit/Privatsphäre für die meisten Fälle, Fähigkeit für Sonderfälle.

Verteilte Inferenz (Multi-GPU)
Für größere Modelle teile Layers über mehrere GPUs auf (Tensor Parallelism) oder teile den Kontext über Geräte auf (Pipeline Parallelism). Verwende llama.cpp mit -ngl oder ExLlamaV2 mit --num-gpu-layers.

Mobile Bereitstellung
Android: Verwende llama.cpp via JNI-Bindings oder ML Kit.

iOS: Verwende llama.cpp via Swift-Bindings oder mlx.

Web: Verwende WebLLM (läuft auf WebGPU via ONNX runtime) oder transformers.js.

Leistungsoptimierung
Flash Attention
Beschleunigt die Attention-Berechnung und reduziert den Speicherverbrauch. Verfügbar in llama.cpp, ExLlamaV2 und modernen transformers-Bibliotheken.

Batch-Inferenz
Verarbeite mehrere Prompts in einem einzigen Forward Pass. Erhöht den Durchsatz drastisch. Verwende llama-batch oder vLLM.

Early Stopping / Token Budgeting
Setze ein maximales Token-Budget, um unbegrenzte Generierung zu verhindern.

Speculative Decoding
Verwende ein kleines, schnelles Modell (draft), um Tokens vorherzusagen, und verifiziere sie dann parallel mit dem großen Modell. Kann 2–3× Beschleunigung liefern.

Praktischer Setup-Leitfaden
1. Installiere Ollama
bash
curl -fsSL https://ollama.com/install.sh | sh
2. Ziehe ein Modell
bash
ollama pull phi3:3.8b-q4_K_M
3. Mit API ausführen
bash
ollama serve
Sende dann Anfragen an http://localhost:11434/api/generate.

4. Python-Integration
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Alternative) llama.cpp direkt verwenden
bash
# GGUF von Hugging Face herunterladen
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Server starten
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
Monitoring und Observability
Verfolge die GPU-Auslastung (nvidia-smi unter Linux, Activity Monitor unter macOS).

Verfolge die Speichernutzung (RAM und VRAM).

Verfolge Tokens pro Sekunde (Durchsatz).

Verfolge die Zeit bis zum ersten Token (Latenz).

Verwende integriertes Logging von llama.cpp oder Ollama.

Einschränkungen und Trade-offs
Qualitätslücke: Kleine lokale Modelle (3.8B–7B) liegen bei komplexem Reasoning im Allgemeinen hinter großen Cloud-Modellen (GPT-4, Claude 3.5) zurück.

Knowledge cutoff: Modellwissen ist zum Trainingszeitpunkt eingefroren; verwende RAG, um aktuelle Informationen einzuspeisen.

Mehrsprachigkeit: Kleinere Modelle haben möglicherweise geringere mehrsprachige Fähigkeiten.

Tool use: Agentische Workflows (function calling) können bei kleinen Modellen weniger zuverlässig sein.

Für viele Alltagsaufgaben (Zusammenfassung, Q&A, Code Completion, Klassifikation) sind lokale Modelle bereits ausreichend und verbessern sich schnell.

Text

---

## Datei 4: `security_best_practices.md`

```markdown
# Security Best Practices

Ein praktischer Leitfaden zur Absicherung von Anwendungen, Infrastruktur und Daten — von der Entwicklung bis zur Produktion.

---

## OWASP Top 10 (2021) — Überblick

1. **Broken Access Control**: Nutzer können auf Ressourcen zugreifen, auf die sie keinen Zugriff haben sollten.
2. **Cryptographic Failures**: Schwache oder fehlende Verschlüsselung.
3. **Injection**: SQL-, NoSQL-, OS-command- oder LDAP-Injection.
4. **Insecure Design**: Architektonische Schwächen.
5. **Security Misconfiguration**: Standardpasswörter, offene Ports, ausführliche Fehlermeldungen.
6. **Vulnerable and Outdated Components**: Bekannte CVEs in Abhängigkeiten.
7. **Identification and Authentication Failures**: Schwache Passwörter, fehlerhaftes Session-Management.
8. **Software and Data Integrity Failures**: Supply-Chain-Angriffe, unsignierte Updates.
9. **Security Logging and Monitoring Failures**: Keine Erkennung von Sicherheitsverletzungen.
10. **Server-Side Request Forgery (SSRF)**: Missbrauch des Servers, um Anfragen an interne Systeme zu stellen.

---

## Eingabevalidierung und Ausgabekodierung

### Validierungsregeln
- **Whitelist > Blacklist**: Definiere erlaubte Muster (z. B. regex für E-Mail), statt bekannte schlechte Muster zu blockieren.
- **Längenlimits**: Erzwinge maximale Längen, um Buffer Overflows und DoS zu verhindern.
- **Typprüfung**: Stelle sicher, dass Integers Integers sind und Booleans Booleans.
- **Verwende gut getestete Bibliotheken**: Für E-Mail-, URL- und Datumsvalidierung verwende Standardbibliotheken (z. B. `email-validator` in Python, `validator.js` in Node).

### Ausgabekodierung
- **HTML encoding**: Kodiere `<`, `>`, `&`, `"`, `'`, um XSS zu verhindern.
- **SQL parameterisation**: Hänge Benutzereingaben niemals an SQL-Abfragen an. Verwende parametrisierte Abfragen (prepared statements) oder ein ORM.
- **Shell escaping**: Vermeide es, Shell-Befehle aus Benutzereingaben zusammenzubauen; falls unvermeidbar, verwende `shlex.quote()` oder Ähnliches.

---

## Authentifizierung und Autorisierung

### Passwortverwaltung
- **Hashing**: Speichere Passwörter mit einem starken, langsamen Hashing-Algorithmus: **Argon2id** (bevorzugt), **bcrypt**, **scrypt** oder **PBKDF2**.
- **Salting**: Füge pro Benutzer ein eindeutiges Salt hinzu.
- **Mindestlänge**: Erzwinge mindestens 12–16 Zeichen.
- **MFA (Multi-Factor Authentication)**: Fordere für sensible Operationen einen zweiten Faktor an (TOTP, SMS, Hardware-Key).
- **Rate limiting**: Verhindere Brute-Force-Versuche auf Login-Endpunkten (z. B. 5 Versuche pro 5 Minuten pro IP/User).

### Session-Management
- Verwende sichere, HTTP-only, SameSite-Cookies für Session-Tokens.
- Setze angemessene Ablaufzeiten.
- Invalidiere Sessions bei Logout und bei Passwortänderung.
- Vermeide es, Session-IDs in URLs offenzulegen.

### OAuth2 / OIDC
- Verwende etablierte Bibliotheken (z. B. Authlib, PyJWT, Passport.js, Spring Security).
- Validiere ID-Tokens gründlich (Signatur, issuer, audience, expiration).
- Verwende state-Parameter, um CSRF zu verhindern.
- Halte Client-Secrets vertraulich.

### JWT (JSON Web Tokens)
- **Sign**: Verwende RS256 oder ES256 (asymmetrisch) für bessere Sicherheit; HS256 (symmetrisch) ist akzeptabel, wenn Shared Secrets gut verwaltet werden.
- **Validate**: Verifiziere immer Signatur, issuer (`iss`), audience (`aud`) und expiration (`exp`).
- **Kurze Ablaufzeit beibehalten**: 15–60 Minuten für Access Tokens; verwende Refresh Tokens für längere Sitzungen.
- **Sicher speichern**: Speichere JWTs niemals in localStorage (anfällig für XSS); verwende stattdessen HTTP-only-Cookies.

---

## API-Sicherheit

### Authentifizierung
- Authentifiziere API-Aufrufe immer (außer bei öffentlichen Endpunkten).
- Bevorzuge API-Keys oder OAuth2-Tokens gegenüber Basic Auth (das bei jeder Anfrage Credentials sendet).

### Rate Limiting und Throttling
- Wende Rate Limits pro User und pro IP an, um Missbrauch und DoS zu verhindern.
- Gib `429 Too Many Requests` mit einem `Retry-After`-Header zurück.

### CORS (Cross-Origin Resource Sharing)
- Erlaube nur bestimmte Origins (niemals `*` in Produktion).
- Validiere den `Origin`-Header serverseitig.

### Eingabevalidierung
- Validiere alle Request-Parameter, einschließlich Header und Body.
- Weise unerwartete Felder zurück (`"strict": true` oder `additionalProperties: false` in JSON Schema).

### HTTPS / TLS
- Erzwinge HTTPS in Produktion.
- Verwende HSTS (HTTP Strict Transport Security), um Browser zur Nutzung von HTTPS zu zwingen.
- Verwende TLS 1.2 oder 1.3 (deaktiviere TLS 1.0/1.1).

---

## Secrets-Management

### Secrets niemals hartkodieren
- Committe keine Secrets (API-Keys, Passwörter, Datenbank-URLs) in die Versionsverwaltung.
- Verwende Environment Variables oder Tools für Secrets-Management.

### Tools
- **HashiCorp Vault**: Enterprise-tauglich, dynamische Secrets.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-nativ.
- **SOPS**: Verschlüssele Secrets in Dateien und committe sie (mit KMS oder GPG).
- **Docker secrets**: Für den Swarm-Modus; Kubernetes secrets (base64-kodiert, aber mit Vorsicht verwenden; erwäge einen externen Secrets Store CSI driver).

### Rotation
- Rotiere Secrets und Service Accounts regelmäßig.
- Automatisiere die Rotation, wo möglich.

---

## Dependency-Management

### Schwachstellen-Scanning
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Rust**: `cargo audit`.
- **Go**: `govulncheck`.
- **Allgemein**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Patching
- Halte Abhängigkeiten auf gepatchten Versionen aktuell.
- Richte automatisierte Pull Requests für Minor-/Patch-Updates ein.
- Prüfe Changelogs auf Breaking Changes.

### Supply-Chain-Integrität
- Verwende Package-Lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`), um reproduzierbare Builds sicherzustellen.
- Verifiziere Checksums heruntergeladener Abhängigkeiten.
- Bevorzuge offizielle Registries und vertraue nur verifizierten Publishern.

---

## Infrastruktursicherheit

### Firewalls
- Blockiere alle eingehenden Ports außer denen, die ausdrücklich benötigt werden (z. B. 80, 443).
- Begrenze SSH-Zugriff auf bestimmte IP-Bereiche (oder verwende einen VPN-/Bastion-Host).
- Verwende Security Groups (AWS) oder NSGs (Azure) für feingranulare Kontrolle.

### OS Hardening
- Spiele Sicherheitsupdates regelmäßig ein (`sudo apt upgrade`, `yum update`).
- Deaktiviere unnötige Dienste und Standardkonten.
- Verwende fail2ban, um Brute-Force-Versuche auf SSH zu blockieren.
- Härte SSH ab: Root-Login deaktivieren, Key-based Auth verwenden, Standardport ändern (optional).

### Netzwerksegmentierung
- Platziere Datenbanken und Caches in privaten Subnetzen ohne Internetzugang.
- Verwende eine DMZ für öffentlich erreichbare Dienste.
- Wende das Prinzip der geringsten Privilegien auf Netzwerkzugriffe an.

### Secrets in der Infrastruktur
- Speichere Secrets niemals in CI/CD-Environment-Variables, es sei denn, sie sind verschlüsselt.
- Verwende die IAM-Rollen des Cloud-Anbieters für EC2-/VM-Instanzen statt langlebiger Keys.

---

## Logging und Monitoring

### Was protokolliert werden sollte
- Authentifizierungsereignisse (Erfolg/Fehlschlag).
- Entscheidungen der Zugriffskontrolle (Autorisierungsfehler).
- Admin-Aktionen (Benutzererstellung, Löschung, Berechtigungsänderungen).
- Änderungen am Datenbankschema.
- Systemfehler und Exceptions.
- API-Anfragen und -Antworten (sensible Daten schwärzen).

### Was nicht protokolliert werden sollte
- Passwörter, Secrets, Tokens, PII (Personal Identifiable Information), sofern sie nicht gehasht/geschwärzt sind.
- Vollständige Kreditkartennummern.

### Alarmierung
- Richte Alerts ein für:
  - Mehrere fehlgeschlagene Logins (mögliche Brute Force).
  - Ungewöhnliche Zugriffsmuster (z. B. aus neuen Orten, zu ungewöhnlichen Zeiten).
  - Neu erstellte Admin-Konten.
  - Hohe Fehlerraten oder Latenzspitzen.
- Verwende ein SIEM (Security Information and Event Management) für fortgeschrittene Korrelation.

### Log-Aufbewahrung
- Bewahre Logs je nach regulatorischen Anforderungen mindestens 30–90 Tage auf.
- Speichere Logs in einem zentralisierten, manipulationssicheren System (z. B. ELK Stack, Splunk, Datadog).

---

## Secure Development Lifecycle (SDL)

1. **Training**: Stelle sicher, dass Entwickler gängige Schwachstellen verstehen.
2. **Threat modelling**: Identifiziere potenzielle Bedrohungen früh im Design.
3. **Secure coding standards**: Erzwinge sie über Linter und Code-Review-Checklisten.
4. **SAST** (Static Application Security Testing): Scanne Quellcode auf Schwachstellen (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): Scanne laufende Anwendungen (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): Scanne Abhängigkeiten.
7. **Penetration testing**: Regelmäßige ethische Hacking-Übungen.
8. **Bug bounty**: Ermutige externe Forschende, Schwachstellen verantwortungsvoll zu finden.
9. **Incident response plan**: Habe einen klaren Plan für den Fall, dass eine Sicherheitsverletzung erkannt wird.

---

## Notfall-Checkliste (wenn ein Sicherheitsvorfall vermutet wird)

1. **Nicht in Panik geraten** — aber schnell handeln.
2. **Isoliere** die betroffenen Systeme (bei Bedarf vom Netzwerk trennen).
3. **Beweise sichern**: Erfasse Logs, Memory Dumps und Festplatten-Images.
4. **Identifiziere** den Umfang: welche Systeme, welche Daten.
5. **Rotiere** alle kompromittierten Credentials und Secrets.
6. **Patche** die Schwachstelle.
7. **Benachrichtige** betroffene Nutzer und Aufsichtsbehörden, falls erforderlich (innerhalb gesetzlicher Fristen).
