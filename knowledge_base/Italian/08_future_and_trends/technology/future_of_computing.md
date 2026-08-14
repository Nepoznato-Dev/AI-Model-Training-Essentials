<!--
---
# Metadata
title: "The Future of Computing"
description: "Moore's Law, quantum computing, neuromorphic chips, edge computing"
category: "Future and Trends"
subcategory: "Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to technology/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Future & Trends Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [future, computing, future-and-trends]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Il futuro dell'informatica
Il futuro dell’informatica è modellato da forze che mettono in discussione i presupposti fondamentali degli ultimi 60 anni. La legge di Moore – l’osservazione secondo cui la potenza di calcolo raddoppia all’incirca ogni due anni – sta rallentando. L'architettura von Neumann – CPU e memoria separate – sta colpendo un "muro di memoria". L’informatica quantistica promette di risolvere problemi che i computer classici non possono risolvere. I chip neuromorfi imitano l'architettura del cervello. L’edge computing allontana l’elaborazione dai data center centralizzati. E l’intelligenza artificiale sta cambiando la funzione dei computer: da strumenti che eseguono istruzioni a sistemi che apprendono, generano e ragionano. Comprendere questi cambiamenti è importante per chiunque costruisca, acquisti o faccia affidamento sulla tecnologia.
---

## La fine della legge di Moore
### Quello che è successo
| Epoca | Dimensioni del transistor | Tendenza |
|-----|----------------|-------|
| **Anni '70-2000** | 10.000 nm → 130 nm | Crescita esponenziale; le prestazioni raddoppiano ogni ~2 anni |
| **Anni 2000-2010** | 130 nm → 22 nm | La crescita è continuata ma la densità di potenza è diventata un problema |
| **Anni 2010-2020** | 22 nm → 3 nm | Rallentamento; ogni nodo costa di più; i benefici diminuiscono |
| **Anni 2020+** | 3 nm → inferiore a 1 nm | Avvicinamento ai limiti atomici; gli effetti quantistici interferiscono |
### Perché è importante
| Conseguenza | Descrizione |
|-------------|-------------|
| **Le prestazioni aumentano lentamente** | Non è possibile fare affidamento su transistor più piccoli per miglioramenti gratuiti delle prestazioni |
| **Specializzazione** | Le CPU generiche lasciano il posto ad acceleratori specifici del dominio (GPU, TPU, NPU) |
| **L'efficienza del software è importante** | Non è possibile usare la forza bruta con l'hardware; gli algoritmi e la qualità del codice diventano più importanti |
| **Necessarie nuove architetture** | Collo di bottiglia di Von Neumann; muro della memoria; muro di potere |
---

## Informatica quantistica
### Fondamenti
| Concetto | Descrizione |
|---------|-----|
| **Qubit** | Bit quantistico; può essere 0, 1 o una sovrapposizione di entrambi |
| **Sovrapposizione** | Un qubit esiste in più stati simultaneamente finché non viene misurato |
| **Intreccio** | Due qubit diventano correlati; misurarne uno determina istantaneamente l'altro |
| **Interferenza** | Gli algoritmi quantistici amplificano le risposte corrette e cancellano quelle sbagliate |
| **Decoerenza** | I qubit perdono proprietà quantistiche attraverso l'interazione con l'ambiente; la principale sfida ingegneristica |
### Quantistici contro classici
| Aspetto | Classico | Quantistici |
|--------|-----------|---------|
| **Unità base** | Bit (0 o 1) | Qubit (sovrapposizione di 0 e 1) |
| **Operazioni** | Porte logiche (AND, OR, NOT) | Porte quantistiche (Hadamard, CNOT, ecc.) |
| **Parallelismo** | Un calcolo alla volta (o molti calcoli indipendenti) | La sovrapposizione consente di esplorare molte possibilità contemporaneamente |
| **Ridimensionamento** | n bit = n valori | n qubit = 2^n valori in sovrapposizione |
| **Tassi di errore** | Molto basso | Attualmente alto; richiede la correzione degli errori |
### Applicazioni in cui Quantum eccelle
| Applicazione | Perché Quantum aiuta | Cronologia |
|-------------|-------------|----------|
| **Crittografia** | L'algoritmo di Shor può violare la crittografia RSA | Minaccia la crittografia attuale; crittografia post-quantistica in fase di sviluppo |
| **Scoperta di farmaci** | Simulare le interazioni molecolari a livello quantistico | 5–15 anni per un impatto pratico |
| **Ottimizzazione** | Trovare soluzioni ottimali in ampi spazi di ricerca | Logistica; finanza; scienza dei materiali |
| **Apprendimento automatico** | Accelerazione quantistica per alcuni algoritmi ML | Prime ricerche; vantaggio pratico ancora poco chiaro |
| **Scienza dei materiali** | Simulare nuovi materiali a livello atomico | Materiali per batterie; catalizzatori; superconduttori |
### Stato attuale
| Azienda / Progetto | Avvicinamento | Qubit | Stato |
|--------------------|----------|--------|--------|
| **IBM** | Superconduttore | 1.000+ | Processore Condor; vantaggio quantistico non ancora dimostrato per problemi pratici |
| **Google** | Superconduttore | 70+ | Sicomoro; ha rivendicato la supremazia quantistica (2019) per un compito specifico |
| **IonQ** | Ioni intrappolati | 30+ (alta fedeltà) | Alta precisione; velocità del cancello più lente |
| **Quantinuum** | Ioni intrappolati | 50+ | Fusione Honeywell + Cambridge Quantum |
| **PsiQuantum** | Fotonico | Non divulgato | Targeting per 1 milione di qubit |
| **Microsoft** | Topologico | Fase di ricerca | Teoricamente più resistente agli errori; più difficile da costruire |
---

## Calcolo neuromorfico
| Aspetto | Descrizione |
|--------|-------------|
| **Ispirazione** | L'architettura neurale del cervello: neuroni e sinapsi |
| **Differenza fondamentale** | L'elaborazione e la memoria sono co-localizzate (come le sinapsi); nessun collo di bottiglia di von Neumann |
| **Reti neurali a picco** | I neuroni comunicano attraverso picchi discreti; ad alta efficienza energetica |
| **Basato sugli eventi** | Solo i neuroni attivi consumano energia; i neuroni inattivi sono liberi |
| **Esempi hardware** | Intel Loihi; Polo Nord IBM; SpiNNaker |
| **Applicazioni** | IA bordo; robotica; elaborazione sensoriale; dispositivi sempre attivi |
---

##Edge computing
### Perché Edge?
| Autista | Descrizione |
|--------|-------------|
| **Latenza** | L'elaborazione dei dati a livello locale evita il ritorno al cloud |
| **Larghezza di banda** | Non tutti i dati devono essere inviati al cloud (ad esempio, video dalle telecamere di sicurezza) |
| **Privacy** | I dati sensibili rimangono sul dispositivo |
| **Affidabilità** | Funziona quando la connettività è intermittente |
| **Costo** | Riduce i costi di elaborazione cloud e trasferimento dati |
### Spettro dell'edge computing
| Posizione | Latenza | Caso d'uso |
|----------|---------|----------|
| **Sul dispositivo** (telefono, IoT) | <1ms | Riconoscimento vocale; elaborazione della fotocamera |
| **Near edge** (gateway, stazione base) | 1–10ms | Controllo industriale; veicoli autonomi |
| **Far edge** (data center regionale) | 10–50 ms | Consegna dei contenuti; gioco |
| **Cloud** (centro dati centrale) | 50–200 ms | Formazione; elaborazione batch; analisi |
---

## Hardware IA
### Tipi di acceleratori IA
| Ferramenta | Forza | Debolezza | Esempio |
|----------|----------|----------|---------|
| **GPU** | Massicciamente parallelo; ottimo per la formazione e l'inferenza | assetato di potere; uso generale | NVIDIA H100; AMD MI300 |
| **TPU** (Unità di elaborazione tensore) | Progettato per operazioni di tensore; efficiente | Meno flessibile delle GPU | Google TPU v5 |
| **NPU** (Unità di elaborazione neurale) | Inferenza AI sul dispositivo; ad alta efficienza energetica | Limitato all'inferenza; modelli più piccoli | Motore neurale Apple; Qualcomm Esagono |
| **FPGA** | Riconfigurabile; bassa latenza | Più difficile da programmare; ecosistema più piccolo | IntelAgilex; Xilinx Versal |
| **ASIC** | Progettato su misura per carichi di lavoro IA specifici | Costoso da progettare; inflessibile | Google TPU (anche un ASIC); Cerebri |
| **Scala wafer** | L'intero wafer è un chip; parallelismo massiccio | Romanzo; costoso | Cerebras WSE-3 |
### Il Muro della Memoria
| Problema | Descrizione | Soluzioni |
|---------|-------------|-----------|
| **Collo di bottiglia di Von Neumann** | I dati devono spostarsi tra CPU e memoria; questo trasferimento è più lento del calcolo | Calcolo quasi della memoria; elaborazione in memoria |
| **Larghezza di banda della memoria** | I modelli di intelligenza artificiale devono leggere miliardi di parametri; la memoria non può alimentare i dati abbastanza velocemente | Memoria ad elevata larghezza di banda (HBM); compressione |
| **Capacità di memoria** | I modelli di grandi dimensioni non entrano nella memoria veloce | Parallelismo del modello; scarico in uno spazio di archiviazione più lento |
---

## Tecnologie post-silicio
| Tecnologia | Descrizione | Potenziale |
|-----------|-------------|-----------|
| **Calcolo fotonico** | Usa la luce invece dell'elettricità per i calcoli | Più veloce; potenza inferiore; sfide nella miniaturizzazione |
| **Spintronica** | Utilizzare lo spin dell'elettrone (non la carica) per informazioni | Non volatile; bassa potenza; prime ricerche |
| **Transistor ai nanotubi di carbonio** | Transistor a base di carbonio invece che di silicio | Più veloce; più efficiente; sfide produttive |
| **Calcolo del DNA** | Utilizzare le molecole di DNA per il calcolo | Parallelismo massiccio; molto lento; fase di ricerca |
| **Informatica biologica** | Utilizzare le cellule viventi per il calcolo | Biologia programmabile; applicazioni mediche |
---

## Tendenze del software
| Tendenza | Descrizione | Impatto |
|-------|-------------|--------|
| **Programmazione assistita dall'intelligenza artificiale** | Gli LLM generano, esaminano ed eseguono il debug del codice | Aumenti di produttività; modifica del ruolo di sviluppatore |
| **Programmazione probabilistica** | Programmi che ragionano nell'incertezza | Migliori modelli di intelligenza artificiale; processo decisionale in condizioni di incertezza |
| **WebAssembly (Wasm)** | Prestazioni quasi native nei browser; portatile | Informatica perimetrale; plugin; senza server |
| **Sicurezza contro ruggine e memoria** | Garanzie a livello linguistico contro i bug di memoria | Software di sistema più sicuro |
| **Dichiarativo/funzionale** | Descrivi cosa, non come | Più facile da parallelizzare; meno soggetto a errori |
---

## Riepilogo
Il futuro dell’informatica non è una semplice continuazione del passato. La Legge di Moore sta rallentando, costringendo il passaggio da processori generici ad acceleratori specializzati. L’informatica quantistica promette accelerazioni esponenziali per problemi specifici – crittografia, scoperta di farmaci, scienza dei materiali – ma i computer quantistici pratici e con correzione degli errori sono ancora lontani anni. I chip neuromorfici imitano l’architettura del cervello per un’intelligenza artificiale edge ad alta efficienza energetica. L'edge computing sposta l'elaborazione più vicino alle origini dati per una minore latenza e una migliore privacy. L'hardware AI si sta diversificando: GPU, TPU, NPU, FPGA e ASIC personalizzati soddisfano ciascuno esigenze diverse. Il muro della memoria, ovvero il divario tra la velocità del processore e la larghezza di banda della memoria, è un collo di bottiglia fondamentale che guida l’innovazione nell’elaborazione quasi-memoria. Le tecnologie post-silicio (fotonica, spintronica, nanotubi di carbonio) sono in fase di ricerca, ma potrebbero rimodellare l’informatica tra decenni. Il tema generale è la specializzazione: l’era dell’informatica universale sta finendo, sostituita da sistemi eterogenei ottimizzati per carichi di lavoro specifici.