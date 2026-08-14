---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [multimodal, ai, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# IA multimodale
I sistemi di intelligenza artificiale multimodale elaborano e combinano informazioni provenienti da più tipi di dati (testo, immagini, audio, video e altro) contemporaneamente. Mentre i precedenti sistemi di intelligenza artificiale erano tipicamente monomodali (solo testo, solo immagini), i sistemi moderni più capaci sono multimodali. GPT-4V legge insieme immagini e testo; Gemini elabora testo, immagini, audio e video in modo nativo; e sistemi come Sora generano video da descrizioni testuali. Questo file spiega come funziona l'intelligenza artificiale multimodale, le architetture dietro di essa e perché la combinazione delle modalità è così potente.
---

## Perché multimodale?
| Vantaggio | Descrizione | Esempio |
|---------|-----|---------|
| **Comprensione più ricca** | Diverse modalità forniscono informazioni complementari | Un video trasmette movimento, suono e contesto che il testo da solo non può |
| **Migliore generalizzazione** | L'apprendimento attraverso le modalità crea rappresentazioni più robuste | Un modello che ha visto sia le immagini che le descrizioni testuali di "gatto" capisce meglio il concetto |
| **Interazione più naturale** | Gli esseri umani comunicano attraverso più canali | Assistenti vocali che vedono ciò che stai indicando |
| **Trasferimento intermodale** | La conoscenza di una modalità aiuta con un'altra | La comprensione delle immagini migliora la generazione del testo e viceversa |
---

## Architetture principali
### Modelli Visione-Linguaggio (VLM)
Modelli che elaborano insieme immagini e testo.
| Architettura | Come funziona | Esempi |
|-------------|-------------|---------|
| **Doppio codificatore** | Codificatori separati per immagine e testo; combinare in una fase successiva | CLIP, ALLINEA |
| **Codificatore di fusione** | I token di immagine e testo vengono intercalati ed elaborati insieme | Fenicottero, Gemelli |
| **Attenzione incrociata** | I token di testo si occupano delle funzionalità dell'immagine (o viceversa) | Fenicottero, CoCa |
| **Tokenizzatore unificato** | Le immagini vengono convertite in token ed elaborate insieme ai token di testo | Gemelli, Camaleonte |
### Come funzionano i modelli linguaggio-visivo
| Passo | Descrizione |
|------|-------------|
| **1. Codifica immagine** | Un codificatore di visione (ViT, SigLIP) converte l'immagine in un insieme di vettori di caratteristiche |
| **2. Codifica testo** | Un codificatore linguistico elabora i token di testo |
| **3. Modalità fusibile** | Le caratteristiche dell'immagine vengono proiettate nello spazio di incorporamento del modello linguistico |
| **4. Genera** | Il modello linguistico produce testo condizionato sia dagli input di immagini che di testo |
### Modelli chiave del linguaggio visivo
| Modello | Sviluppatore | Architettura | Caratteristica notevole |
|-------|-----------|-------------|-----------------|
| **CLIP** | OpenAI | Doppio codificatore (ViT + codificatore testo) | Classificazione delle immagini zero-shot tramite testo |
| **LLaVA** | Open source | Codificatore visivo LLaMA + CLIP | VLM open source; comunità forte |
| **GPT-4V/4o** | OpenAI | Multimodale unificato | Elabora insieme testo, immagini e audio |
| **Gemelli** | Google DeepMind | Nativamente multimodale dalla formazione | Costruito per il multimodale da zero |
| **Claude** | Antropico | Visione + testo | Forte nella comprensione di documenti e grafici |
| **Qwen-VL** | Alibaba | VLM a peso aperto | Competitivo con i modelli chiusi |
| **StagistaVL** | Open source | Encoder di visione multiscala | Forte opzione open source |
---

## Modelli audio e vocali
### Riconoscimento vocale (ASR)
| Modello | Architettura | Caratteristica notevole |
|-------|-------------|-----------------|
| **Sussurro** (OpenAI) | Trasformatore encoder-decodificatore | Formazione su 680.000 ore di audio multilingue; robusto |
| **Conforme** | Convoluzione + autoattenzione | Combina funzionalità locali e globali |
| **wav2vec 2.0** | Autocontrollo | Impara dal discorso senza etichetta |
| **USM** (Google) | Modello vocale universale | 2 milioni di ore di dati etichettati; Oltre 300 lingue |
### Sintesi vocale (TTS)
| Modello | Avvicinamento | Caratteristica notevole |
|-------|----------|-----------|
| **VALL-E** (Microsoft) | Codec neurale | Clonazione vocale da un campione di 3 secondi |
| **Corteccia** (Suno) | Basato su trasformatore | Multilingue; include suoni non vocali |
| **UndiciLabs** | Commerciale | Clonazione vocale di alta qualità |
| **ChatTTS** | Open source | Discorso colloquiale con prosodia naturale |
| **Discorso dei pesci** | Open source | Multilingue; inferenza veloce |
### Comprensione dell'audio
| Modello | Capacità |
|-------|-----------|
| **AudioLDM** | Generazione di effetti sonori dal testo |
| **MusicGen** (Meta) | Generazione di testo in musica |
| **Audio Qwen** | Comprensione audio (parlato, musica, suoni ambientali) |
| **SALMONE** | Comprensione del parlato, dell'audio, del linguaggio, della musica e del rumore |
---

## Modelli video
Il video combina immagini, audio, testo e tempo, rendendolo la modalità più complessa.
| Modello | Digitare | Capacità |
|-------|------|-----|
| **Sora** (OpenAI) | Dal testo al video | Fino a 1080p; capisce la fisica |
| **Gemelli** | Comprensione del video | Può analizzare video lunghi con audio |
| **Video-LLaVA** | Video + testo | Comprensione video open source |
| **Pista Gen-3** | Testo/immagine in video | Generazione di video commerciali |
| **Kling** | Dal testo al video | Generazione di video di lunga durata |
### Video Sfide di comprensione
| Sfida | Descrizione |
|-----------|-------------|
| **Ragionamento temporale** | Comprendere gli eventi che si svolgono nel tempo |
| **Contesto lungo** | I video possono durare ore; l'elaborazione di tutti i frame è costosa |
| **Sincronizzazione audiovisiva** | Collegare ciò che viene detto con ciò che viene mostrato |
| **Causalità** | Comprendere causa ed effetto nelle sequenze video |
---

## Recupero cross-modale
Trovare contenuti pertinenti attraverso diverse modalità.
| Compito | Descrizione | Esempio |
|------|-------------|---------|
| **Testo → Immagine** | Trova immagini corrispondenti a una query di testo | Cerca "tramonto sulle montagne" in una libreria fotografica |
| **Immagine → Testo** | Trova testo rilevante per un'immagine | Generazione di didascalie per immagini |
| **Testo → Audio** | Trova suoni corrispondenti a una descrizione | Sound design: "passi sulla ghiaia" |
| **Immagine → Immagine** | Trova immagini visivamente simili | Ricerca prodotti per immagine |
### CLIP per il recupero intermodale
Lo spazio di incorporamento condiviso di CLIP consente il recupero intermodale zero-shot:
| Passo | Descrizione |
|------|-------------|
| 1| Codifica tutte le immagini con il codificatore di visione |
| 2| Codificare la query di testo con il codificatore di testo |
| 3| Calcola la somiglianza del coseno tra l'incorporamento del testo e tutti gli incorporamenti delle immagini |
| 4| Restituisci le immagini con la massima somiglianza |
Funziona senza alcuna formazione specifica per l'attività, una proprietà chiamata capacità **zero-shot**.
---

## IA incarnata
L’intelligenza artificiale incorporata combina la percezione multimodale con l’azione fisica.
| Sistema | Modalità | Applicazione |
|--------|----------|-------------|
| **RT-2** (Google) | Visione + linguaggio → azioni del robot | Controllo robot per scopi generali da istruzioni di testo |
| **Otto** | Politica sui robot open source | Addestrato su diversi dati robot |
| **Tesla Optimus** | Visione + linguaggio → compiti fisici | Robot umanoide per compiti generali |
| **Figura 01** | Visione + linguaggio + parola | Robot umanoide con capacità di conversazione |
### Sfide nell'intelligenza artificiale incarnata
| Sfida | Perché è difficile |
|-----------|--------------|
| **Divario tra simulazione e realtà** | La simulazione non cattura perfettamente la fisica del mondo reale |
| **Destrezza** | Il controllo motorio fine (mani, dita) è estremamente difficile |
| **Sicurezza** | I robot fisici possono causare danni reali |
| **Elaborazione in tempo reale** | Deve percepire, decidere e agire in millisecondi |
| **Generalizzazione** | Un robot addestrato a raccogliere le tazze rosse potrebbe non riuscire a raccogliere quelle blu |
---

## Dati e Formazione
### Dati di allenamento multimodale
| Insieme di dati | Modalità | Taglia |
|---------|-----------|------|
| **LAION-5B** | Coppie immagine-testo | 5,85 miliardi di paia |
| **CompData** | Immagine-testo curato | Punto di riferimento per la progettazione di set di dati |
| **WIT** (Wikipedia) | Testo immagine da Wikipedia | 11,5 milioni di paia |
| **Come fare per 100M** | Videotesto (video dimostrativi) | 100 milioni di clip |
| **LibriSpeech** | Testo vocale | 1.000 ore di inglese |
| **Voce Comune** | Testo vocale | Multilingue; contributo della comunità |
### Strategie di formazione
| Strategia | Descrizione | Quando usarlo |
|----------|-------------|-------------|
| **Formazione congiunta** | Allenarsi su tutte le modalità contemporaneamente | Dopo aver allineato i dati multimodali |
| **Apprendimento curriculare** | Inizia con esempi semplici; aumenta la difficoltà | Migliora la convergenza |
| **Apprendimento contrastivo** | Impara ad abbinare coppie correlate tra le modalità (stile CLIP) | Costruire rappresentazioni condivise |
| **Sintonia delle istruzioni** | Formazione su coppie istruzione-risposta multimodali | La realizzazione dei modelli segue le istruzioni multimodali |
---

## Valutazione
| Punto di riferimento | Modalità | Cosa prova |
|-----------|-----------|---------------|
| **MMLU** | Testo | Conoscenza di 57 argomenti |
| **MMMU** | Testo + immagini | Ragionamento a livello universitario con diagrammi |
| **MathVista** | Testo + immagini | Ragionamento matematico con dati visivi |
| **Video-MME** | Testo + video | Comprensione video e ragionamento temporale |
| **CASCO** | Testo + audio | Valutazione multimodale a lungo contesto |
| **Panca SWE** | Testo + codice | Attività di ingegneria del software nel mondo reale |
---

## Riepilogo
L’intelligenza artificiale multimodale rappresenta il passaggio da modelli monouso a sistemi che percepiscono e ragionano su tutte le forme di dati. I modelli con linguaggio visivo come GPT-4V e Gemini possono comprendere immagini e testo insieme; modelli vocali come Whisper e VALL-E gestiscono l'audio; i modelli video stanno iniziando a elaborare l'intera complessità delle immagini in movimento con il suono. La tendenza è chiara: i sistemi di intelligenza artificiale più capaci del futuro saranno nativamente multimodali, elaborando tutti i tipi di informazioni contemporaneamente. Le sfide – allineamento dei dati, costi computazionali, valutazione e implementazione incorporata – sono significative, ma i progressi nel periodo 2024-2026 sono stati rapidi.