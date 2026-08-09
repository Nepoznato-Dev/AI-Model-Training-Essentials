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
|--------|------|-----|-----|
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
**Comando di esempio:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

###Ollama
- Avvolge llama.cpp con una semplice CLI e API REST.
- Scarica automaticamente i modelli e li gestisce.
- Ottimo per la prototipazione e le app desktop.
- Supporta file modello personalizzati per i prompt del sistema.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### Studio LM
- App desktop grafica per Windows, macOS, Linux.
- Interfaccia di download e chat con un clic.
- Server locale integrato con API compatibile con OpenAI.
- Buono per utenti non tecnici e test rapidi.
### Trasformatori di volti abbracciati + bitsandbytes
- La libreria Python standard per i modelli HF.
- Utilizzare`bitsandbytes`per la quantizzazione a 4 bit (`load_in_4bit=True`).
- Più flessibile per la messa a punto ma più lento di llama.cpp per l'inferenza.
### ExLlamaV2
- Inferenza GPU molto veloce per GPTQ e AWQ.
- Migliori prestazioni sulle GPU NVIDIA.
- Supporta la generazione batch.
### mlx (Apple)
- Framework Apple per i chip della serie M.
- Altamente ottimizzato per Apple Silicon.
- API Python.
---

## Gestione della memoria
### Finestra di contesto e cache KV
La cache KV memorizza coppie chiave-valore per ogni livello e ogni token nel contesto. Cresce linearmente con la lunghezza del contesto.
Costo della memoria ≈ 2 × strati × (teste KV × attenuazione testina) × token × byte per valore
Per un modello a 32 strati con testine da 8 KV e dim testina da 128, ciascun token costa ~32 × 8 × 128 × 2 byte = 65 KB per token. Per i token da 128.000, sono circa 8 GB solo per la cache.
### Strategie di scarico
- **Offload dei livelli**: metti alcuni livelli sulla GPU, altri sulla CPU. Più veloce della CPU pura, requisiti VRAM inferiori.
- **Streaming di token**: elabora i token in modo incrementale anziché tutti in una volta.
### Memorizzazione nella cache dei prompt
Riutilizzare le cache KV tra prompt simili per evitare di ricalcolare la fase di precompilazione. Alcuni framework lo supportano (ad esempio, vLLM, llama.cpp con`--prompt-cache`).
### File mappati in memoria
Carica i pesi del modello direttamente dal disco senza caricarli interamente nella RAM (utile per modelli di grandi dimensioni su sistemi con memoria limitata). llama.cpp utilizza la mappatura della memoria per impostazione predefinita.
---

## Architetture di distribuzione
### Modalità a dispositivo singolo
Un modello funziona su una macchina (laptop, smartphone, dispositivo edge). Utilizzato per assistenti personali, app per prendere appunti, completamento del codice.
### Edge cloud ibrido
Il modello locale gestisce le query comuni; ricorrere a un modello cloud per domande complesse. Ciò offre il meglio di entrambi i mondi: velocità/privatezza per la maggior parte, funzionalità per i casi limite.
### Inferenza distribuita (multi-GPU)
Per i modelli più grandi, dividi i livelli su più GPU (parallelismo del tensore) o dividi il contesto tra i dispositivi (parallelismo della pipeline). Utilizza llama.cpp con`-ngl`o ExLlamaV2 con`--num-gpu-layers`.
### Distribuzione mobile
- **Android**: utilizza llama.cpp tramite collegamenti JNI o ML Kit.
- **iOS**: utilizza llama.cpp tramite collegamenti Swift o mlx.
- **Web**: utilizza WebLLM (funziona su WebGPU tramite runtime ONNX) o Transformers.js.
---

## Ottimizzazione delle prestazioni
### Flash Attenzione
Accelera il calcolo dell'attenzione e riduce l'utilizzo della memoria. Disponibile in llama.cpp, ExLlamaV2 e nelle moderne librerie di trasformatori.
### Inferenza batch
Elabora più richieste in un unico passaggio di inoltro. Aumenta notevolmente la produttività. Utilizza`llama-batch`o vLLM.
### Arresto anticipato/ Budgeting dei token
Imposta un budget massimo per i token per impedire una generazione illimitata.
### Decodifica speculativa
Utilizza un piccolo modello veloce (bozza) per prevedere i token, quindi verifica con il modello grande in parallelo. Può produrre un'accelerazione di 2–3 volte.
---

## Guida pratica all'installazione
### 1. Installa Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Tira un modello
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Esegui con l'API
```bash
ollama serve
```

Quindi invia le richieste a`http://localhost:11434/api/generate`.
### 4. Integrazione con Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternativa) Utilizzare direttamente llama.cpp
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Monitoraggio e osservabilità
- Tieni traccia dell'utilizzo della GPU (`nvidia-smi` su Linux, Activity Monitor su macOS).
- Tieni traccia dell'utilizzo della memoria (RAM e VRAM).
- Traccia i token al secondo (throughput).
- Tieni traccia del tempo fino al primo token (latenza).
- Utilizza la registrazione integrata da llama.cpp o Ollama.
---

## Limitazioni e compromessi
- **Gap di qualità**: i modelli locali piccoli (3,8B-7B) generalmente sottoperformano i modelli cloud di grandi dimensioni (GPT-4, Claude 3,5) su ragionamenti complessi.
- **Taglio della conoscenza**: la conoscenza del modello è congelata al momento dell'addestramento; utilizzare RAG per inserire le informazioni correnti.
- **Multilingue**: i modelli più piccoli potrebbero avere meno funzionalità multilingue.
- **Utilizzo dello strumento**: i flussi di lavoro agentici (chiamata di funzione) potrebbero essere meno affidabili su modelli di piccole dimensioni.
Per molte attività quotidiane (riepilogo, domande e risposte, completamento del codice, classificazione), i modelli locali sono già sufficienti e stanno migliorando rapidamente.