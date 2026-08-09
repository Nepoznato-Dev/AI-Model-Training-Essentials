---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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
# Lokale KI-Architektur
Ein praktischer Leitfaden zum vollständigen Ausführen großer Sprachmodelle auf dem Gerät – Überlegungen zur Hardware, Inferenz-Engines, Speicheroptimierung und Systemdesign für die Edge-Bereitstellung.
---

## Warum KI lokal ausführen?
- **Datenschutz**: Keine Daten verlassen das Gerät.
- **Kosten**: Keine API-Gebühren pro Token.
- **Latenz**: Vorhersehbare, netzwerkfreie Schlussfolgerung.
- **Offline-Verfügbarkeit**: Funktioniert ohne Internet.
- **Kontrolle**: Volle Kontrolle über Modellversion, Anpassung und Feinabstimmung.
---

## Hardwareanforderungen
### GPU-Speicher (VRAM)
Die wichtigste Ressource. Modellgröße im Speicher ≈ **Parameter × Bytes pro Parameter**.
| Präzision | Bytes pro Parameter | 3.8B-Modell | 7B-Modell | 13B-Modell | 70B-Modell |
|-----------|------|------------|----------|-----------|-----------|
| FP32 | 4 | ~15 GB | ~28 GB | ~52 GB | ~280 GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26 GB | ~140 GB |
| INT8 (8-Bit) | 1 | ~3,8 GB | ~7 GB | ~13 GB | ~70 GB |
| INT4 (4-Bit) | 0,5 | ~1,9 GB | ~3,5 GB | ~6,5 GB | ~35 GB |
**Praktische Richtlinien:**
- 8 GB VRAM → bis zu 7B-Modelle bei 4-Bit.
- 12 GB VRAM → bis zu 13 B-Modelle bei 4 Bit.
- 24 GB VRAM → bis zu 70 B Modelle bei 4 Bit (oder 13 B bei 8 Bit).
- Apple Silicon (Unified Memory) kann 70B-Modelle auf Systemen mit mehr als 64 GB ausführen.
### RAM (Systemspeicher)
- Für die CPU-Inferenz benötigen Sie genügend System-RAM, um das Modell zu laden (ähnlich wie bei VRAM-Nummern).
– Für die GPU-Inferenz ist der System-RAM wichtig, um das Modell in den Speicher zu laden, bevor es in den VRAM verlagert wird.
### Lagerung
- Quantisierte Modellgewichte belegen einige GB (z. B. 4-Bit 7B ≈ 4 GB auf der Festplatte). Stellen Sie sicher, dass für mehrere Modelle mindestens 20–50 GB frei sind.
### CPU
- Zur zeitnahen Verarbeitung (Prefill) und CPU-Entlastung hilft eine moderne Multicore-CPU.
- Chips der Apple M-Serie bieten aufgrund des einheitlichen Speichers und der Neural Engine eine hervorragende Leistung für LLMs.
---

## Quantisierung
Die Quantisierung verringert die numerische Präzision von Gewichten, reduziert den Speicher drastisch und erhöht die Geschwindigkeit bei geringen Genauigkeitskosten.
### Beliebte Formate
| Formatieren | Bits | Beschreibung | Typische Verwendung |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp-Format, optimiert für CPU/GPU-Hybrid | Am besten für lokale Schlussfolgerungen |
| **GPTQ** | 4–8 | Nur GPU, effizient auf CUDA | Am besten für NVIDIA-GPUs |
| **AWQ** | 4 | Aktivierungsbewusst, nur GPU | Gut für Batch-Inferenz auf GPUs |
| **ONNX** | Variable | Standardisiert, plattformübergreifend | Produktionsdienst |
### Auswahl einer Quantisierungsstufe
- **Q8_0** (8-Bit): minimaler Qualitätsverlust, größte Größe.
- **Q6_K** (6-Bit): gute Qualität, ordentliche Komprimierung.
- **Q5_K_M** (5-Bit): gemeinsamer Sweet Spot.
- **Q4_K_M** (4-Bit): kleinste, akzeptable Qualität für die meisten Aufgaben.
- **IQ4_XS** / **IQ3_XS**: Verbesserte Quantisierung mit besserer Ratlosigkeit bei 4/3 Bit.
**Faustregel:** Verwenden Sie Q4_K_M für ein gutes Gleichgewicht zwischen Qualität und Größe. Wenn Sie über zusätzlichen VRAM verfügen, verwenden Sie Q5 oder Q6.
---

## Inferenz-Engines (lokal)
### lama.cpp
- Geschrieben in C++.
- Unterstützt das GGUF-Format.
- Optimiert für CPU und GPU (über CUDA, Metal, OpenCL).
- Sehr schnell, besonders auf der CPU.
- Befehlszeile, Servermodus und Python-Bindungen.
**Beispielbefehl:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
– Umschließt llama.cpp mit einer einfachen CLI- und REST-API.
- Lädt Modelle automatisch herunter und verwaltet sie.
- Ideal für Prototyping und Desktop-Apps.
- Unterstützt benutzerdefinierte Modelldateien für Systemeingabeaufforderungen.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Grafische Desktop-App für Windows, macOS, Linux.
- Download- und Chat-Oberfläche mit einem Klick.
- Integrierter lokaler Server mit OpenAI-kompatibler API.
- Gut für technisch nicht versierte Benutzer und zum schnellen Testen.
### Hugging Face Transformers + Bitsandbytes
– Die Standard-Python-Bibliothek für HF-Modelle.
- Verwenden Sie`bitsandbytes`für die 4-Bit-Quantisierung (`load_in_4bit=True`).
– Flexibler für die Feinabstimmung, aber langsamer als llama.cpp für Rückschlüsse.
### ExLlamaV2
- Sehr schnelle GPU-Inferenz für GPTQ und AWQ.
- Beste Leistung auf NVIDIA-GPUs.
- Unterstützt die Batch-Generierung.
### mlx (Apple)
- Apples Framework für Chips der M-Serie.
- Hochoptimiert für Apple Silicon.
- Python-API.
---

## Speicherverwaltung
### Kontextfenster und KV-Cache
Der KV-Cache speichert Schlüssel-Wert-Paare für jede Ebene und jedes Token im Kontext. Es wächst linear mit der Kontextlänge.
Speicherkosten ≈ 2 × Schichten × (KV-Köpfe × Kopfdimmung) × Token × Bytes pro Wert
Für ein 32-Layer-Modell mit 8 KV-Köpfen und 128 Head-Dim kostet jeder Token ~32 × 8 × 128 × 2 Byte = 65 KB pro Token. Bei 128.000 Token sind das etwa 8 GB allein für den Cache.
### Offloading-Strategien
- **Layer-Offloading**: Legen Sie einige Layer auf die GPU, andere auf die CPU. Schneller als reine CPU, geringerer VRAM-Bedarf.
- **Token-Streaming**: Verarbeiten Sie Token schrittweise und nicht alle auf einmal.
### Prompt-Caching
Verwenden Sie KV-Caches für ähnliche Eingabeaufforderungen erneut, um eine Neuberechnung der Vorfüllphase zu vermeiden. Einige Frameworks unterstützen dies (z. B. vLLM, llama.cpp mit`--prompt-cache`).
### Speicherzugeordnete Dateien
Laden Sie Modellgewichte direkt von der Festplatte, ohne sie vollständig in den RAM zu laden (nützlich für große Modelle auf Systemen mit begrenztem Speicher). llama.cpp verwendet standardmäßig die Speicherzuordnung.
---

## Bereitstellungsarchitekturen
### Einzelgerätemodus
Ein Modell läuft auf einer Maschine (Laptop, Smartphone, Edge-Gerät). Wird für persönliche Assistenten, Notizen-Apps und Code-Vervollständigung verwendet.
### Hybride Edge-Cloud
Das lokale Modell verarbeitet häufige Abfragen. Rückgriff auf ein Cloud-Modell für komplexe Fragestellungen. Dies bietet das Beste aus beiden Welten – Geschwindigkeit/Privatheit für die meisten, Funktionalität für Randfälle.
### Verteilte Inferenz (Multi-GPU)
Teilen Sie bei größeren Modellen Schichten auf mehrere GPUs auf (Tensor-Parallelität) oder teilen Sie den Kontext auf mehrere Geräte auf (Pipeline-Parallelität). Verwenden Sie llama.cpp mit`-ngl`oder ExLlamaV2 mit`--num-gpu-layers`.
### Mobile Bereitstellung
- **Android**: Verwenden Sie llama.cpp über JNI-Bindungen oder ML-Kit.
- **iOS**: Verwenden Sie llama.cpp über Swift-Bindungen oder mlx.
- **Web**: Verwenden Sie WebLLM (läuft auf WebGPU über ONNX-Laufzeit) oder Transformers.js.
---

## Leistungsoptimierung
### Flash-Aufmerksamkeit
Beschleunigt die Aufmerksamkeitsberechnung und reduziert den Speicherverbrauch. Verfügbar in llama.cpp, ExLlamaV2 und modernen Transformer-Bibliotheken.
### Batch-Inferenz
Verarbeiten Sie mehrere Eingabeaufforderungen in einem einzigen Vorwärtsdurchlauf. Erhöht den Durchsatz erheblich. Verwenden Sie`llama-batch`oder vLLM.
### Frühes Stoppen / Token-Budgetierung
Legen Sie ein maximales Token-Budget fest, um eine unbegrenzte Generierung zu verhindern.
### Spekulative Dekodierung
Verwenden Sie ein kleines schnelles Modell (Entwurf), um Token vorherzusagen, und überprüfen Sie es dann parallel mit dem großen Modell. Kann eine 2–3-fache Beschleunigung bewirken.
---

## Praktische Einrichtungsanleitung
### 1. Ollama installieren
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Ziehen Sie ein Modell
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Mit API ausführen
```bash
ollama serve
```

Senden Sie dann Anfragen an`http://localhost:11434/api/generate`.
### 4. Python-Integration
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternative) Verwenden Sie llama.cpp direkt
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Überwachung und Beobachtbarkeit
- Verfolgen Sie die GPU-Auslastung (`nvidia-smi`unter Linux, Aktivitätsmonitor unter macOS).
- Verfolgen Sie die Speichernutzung (RAM und VRAM).
- Verfolgen Sie Token pro Sekunde (Durchsatz).
- Verfolgen Sie die Zeit bis zum ersten Token (Latenz).
- Verwenden Sie die integrierte Protokollierung von llama.cpp oder Ollama.
---

## Einschränkungen und Kompromisse
- **Qualitätslücke**: Kleine lokale Modelle (3.8B–7B) schneiden bei komplexen Überlegungen im Allgemeinen schlechter ab als große Cloud-Modelle (GPT-4, Claude 3.5).
- **Wissensgrenze**: Modellwissen wird zum Trainingszeitpunkt eingefroren; Verwenden Sie RAG, um aktuelle Informationen einzuspeisen.
- **Mehrsprachig**: Kleinere Modelle verfügen möglicherweise über weniger Mehrsprachigkeit.
- **Werkzeugverwendung**: Agentische Arbeitsabläufe (Funktionsaufrufe) sind bei kleinen Modellen möglicherweise weniger zuverlässig.
Für viele alltägliche Aufgaben (Zusammenfassung, Fragen und Antworten, Code-Vervollständigung, Klassifizierung) sind lokale Modelle bereits ausreichend und verbessern sich rasch.