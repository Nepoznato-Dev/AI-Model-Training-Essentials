---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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

# Ottimizzazione e distribuzione del modello
L’addestramento di un modello di intelligenza artificiale di grandi dimensioni è un risultato significativo, ma la sua implementazione efficiente è l’ambito in cui è richiesta la maggior parte dello sforzo ingegneristico. Un modello che impiega 10 secondi per rispondere o richiede otto GPU A100 non è pratico per la maggior parte delle applicazioni del mondo reale. L'ottimizzazione del modello è il processo che consente di realizzare modelli più piccoli, più rapidi e più convenienti, pur mantenendo una qualità accettabile. Questo file copre la quantizzazione, l'eliminazione, la distillazione e gli strumenti pratici per l'implementazione dei modelli nella produzione.
---

## Perché ottimizzare?
| Preoccupazione | Impatto |
|---------|--------|
| **Latenza** | Gli utenti si aspettano risposte in meno di 1 secondo; ogni 100 ms in più si perde il coinvolgimento |
| **Costo** | L'inferenza della GPU è costosa; un modello da 70 miliardi costa ~$0,05-0,15 per 1 milione di token su hardware cloud |
| **Memoria** | Un modello 7B in FP32 necessita di 28 GB di VRAM; la maggior parte delle GPU consumer ha 8-24 GB |
| **Energia** | L'esecuzione di modelli di grandi dimensioni consuma una quantità significativa di elettricità; è importante per dispositivi mobili ed edge |
| **Scala** | Servire milioni di utenti richiede modelli che si adattino all'hardware disponibile |
---

## Quantizzazione
La quantizzazione riduce la precisione dei pesi del modello da virgola mobile a 32 bit (FP32) a formati più piccoli come INT8, INT4 o anche inferiori.
### Formati di precisione
| Formato | Bit per peso | Memoria per il modello 7B | Qualità |
|--------|----------------|--------------------|---------|
| **PQ32** | 32| 28GB | Linea di base (precisione totale) |
| **FP16 / BF16** | 16| 14GB | Quasi identico a FP32 |
| **INT8** | 8| 7GB | Perdita di qualità molto piccola |
| **INT4** | 4| 3,5GB | Perdita moderata di qualità; ancora utilizzabile |
| **INT3/INT2** | 3-2| 2,6-1,75GB | Perdita significativa di qualità; fase di ricerca |
### Metodi di quantizzazione
| Metodo | Quando succede | Come funziona | Qualità |
|--------|----------------|------|---------|
| **Quantizzazione post-allenamento (PTQ)** | Una volta completata la formazione | Calibrare il modello su un piccolo set di dati; trovare scale ottimali | Buono per INT8; degrada a INT4 |
| **GPTQ** | Dopo l'allenamento | Quantizzazione INT4 compatibile con GPU utilizzando informazioni approssimative del secondo ordine | Buona qualità a INT4 |
| **AWQ** (quantizzazione del peso consapevole dell'attivazione) | Dopo l'allenamento | Proteggi i pesi salienti in base alle grandezze di attivazione | Meglio di GPTQ su INT4 |
| **GGUF** (formato llama.cpp) | Dopo l'allenamento | Quantizzazione compatibile con la CPU; precisione mista per strato | Ottimizzato per l'inferenza della CPU |
| **Formazione consapevole della quantizzazione (QAT)** | Durante l'allenamento | Simulare la quantizzazione durante l'addestramento in modo che il modello impari a farcela | Migliore qualità; richiede riqualificazione |
### Impatto pratico
| Modello | FP16 Dimensioni | INT4 Dimensioni | Accelera | Perdita di qualità |
|-------|-----------|-----------|---------|-------------|
| **LLaMA7B** | 14GB | 3,5GB | 2-4x | ~1-2% sui benchmark |
| **LLaMA70B** | 140GB | 35GB | 2-3x | ~2-3% sui benchmark |
---

## Potatura
La potatura rimuove pesi o neuroni non necessari da un modello addestrato.
| Digitare | Descrizione | Vantaggio | Sfida |
|------|-------------|-----------|-----------|
| **Non strutturato** | Rimuovere i singoli pesi (impostarli su zero) | Rapporti di compressione più alti | Richiede un supporto hardware limitato |
| **Strutturato** | Rimuovere interi neuroni, teste di attenzione o strati | Riduce direttamente le dimensioni del modello | Potrebbe perdere più qualità |
| **Basato sulla magnitudine** | Rimuovere i pesi con i valori assoluti più piccoli | Semplice; funziona bene | Potrebbero mancare piccoli pesi importanti |
| **Basato sull'importanza** | Rimuovere i pesi in base al loro contributo alla produzione | Migliore conservazione della qualità | Più costoso da calcolare |
### Pipeline di potatura
| Passo | Descrizione |
|------|-------------|
| 1. Treno | Addestra normalmente il modello completo |
| 2. Punteggio | Calcola i punteggi di importanza per ciascun peso/neurone |
| 3. Potare | Rimuovere gli elementi meno importanti |
| 4. Ottimizzazione | Riqualificarsi per recuperare la precisione perduta |
| 5. Ripeti | Ripetere la potatura e la messa a punto per una compressione più elevata |
---

## Distillazione della conoscenza
Addestrare un piccolo modello "studente" per imitare un grande modello "insegnante".
| Componente | Ruolo |
|-----------|------|
| **Insegnante** | Modello grande e di alta qualità |
| **Studente** | Piccolo modello che impara dall'insegnante |
| **Perdita per distillazione** | Lo studente cerca di corrispondere alla distribuzione dei risultati dell'insegnante (etichette soft) |
### Tipi di distillazione
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Basato su Log** | Lo studente corrisponde alle probabilità di output dell'insegnante | Distillazione originale di Hinton |
| **Basato su funzionalità** | Lo studente corrisponde alle rappresentazioni intermedie dell'insegnante | FitNet |
| **Basato sulle relazioni** | Lo studente abbina le relazioni tra i campioni | RKD (Distillazione della conoscenza relazionale) |
| **Senza dati** | Non sono necessari dati di allenamento originali; usa la generazione dell'insegnante | DAFL, Inversione profonda |
### Esempi notevoli di distillazione
| Insegnante | Studente | Risultato |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (si dice) | Modello più piccolo con gran parte della qualità del GPT-4 |
| **BERT-Grande** | DistillBERT | 40% più piccolo, 60% più veloce, 97% delle prestazioni di BERT |
| **LLaMA70B** | LLaMA 7B (tramite distillazione) | Il piccolo modello open source si avvicina alla qualità del modello grande |
---

## Ottimizzazioni specifiche per LLM
### Ottimizzazione della cache KV
I modelli linguistici di grandi dimensioni memorizzano nella cache le coppie chiave-valore dei token precedenti per evitare il ricalcolo.
| Tecnica | Descrizione | Impatto |
|-----------|-------------|--------|
| **Attenzione multi-query (MQA)** | Tutte le teste dell'attenzione condividono una coppia KV | Riduce la memoria; leggera perdita di qualità |
| **Attenzione alle query raggruppate (GQA)** | I gruppi di teste condividono coppie KV | Equilibrio tra MQA e attenzione standard |
| **Attenzione alla finestra scorrevole** | Attendi solo gli ultimi gettoni W | Riduce la dimensione della cache KV per contesti lunghi |
### Decodifica speculativa
| Passo | Descrizione |
|------|-------------|
| 1| Un piccolo modello "bozza" genera rapidamente K token |
| 2| Il modello grande verifica tutti i token K in un passaggio in avanti |
| 3| I token accettati vengono mantenuti; quelli rifiutati vengono rigenerati |
Risultato: 2-3 volte più veloce nella generazione senza perdita di qualità (il modello grande ha sempre l'ultima parola).
### Flash Attenzione
| Caratteristica | Descrizione |
|---------|-----|
| **Problema** | L'attenzione standard richiede memoria O(n²) per la matrice di attenzione |
| **Soluzione** | Calcola l'attenzione in blocchi; non materializzare mai l'intera matrice in memoria |
| **Risultato** | 2-4 volte più veloce; abilita finestre di contesto molto più lunghe |
| **Varianti** | Flash Attention 2 (più veloce), FlashDecoding (ottimizzato per l'inferenza) |
---

## Framework di servizio
| Quadro | Ideale per | Caratteristica fondamentale |
|-----------|----------|-------------|
| **vLLM** | Servizio LLM | PaginatoAttenzione; dosaggio continuo; rendimento elevato |
| **TensorRT-LLM** | Inferenza GPU NVIDIA | Massime prestazioni sull'hardware NVIDIA |
| **llama.cpp** | Inferenza CPU e GPU consumer | Esegue modelli quantizzati su laptop e telefoni |
| **Ollama** | Modello locale in esecuzione | Wrapper intuitivo attorno a llama.cpp |
| **Server di inferenza Triton** | Servizio multi-framework | Supporta TensorFlow, PyTorch, ONNX, TensorRT |
| **TorciaServe** | Servizio modello PyTorch | Integrazione nativa di PyTorch |
| **Runtime ONNX** | Inferenza multipiattaforma | Esecuzione ottimizzata su tutto l'hardware |
| **BentoML** | Distribuzione della produzione | Indipendente dal contesto; si occupa di confezionamento e servizio |
---

## Modelli di distribuzione
| Modello | Descrizione | Quando usarlo |
|---------|-----|-----|
| **Distribuzione Edge** | Esegui modelli su telefoni, dispositivi IoT o hardware incorporato | Bassa latenza; non in linea; riservatezza |
| **API cloud** | Ospitare modelli su GPU cloud; servire tramite API | Calcolo massimo; pagare per utilizzo |
| **Ibrido** | Modello piccolo sul dispositivo; modello di grandi dimensioni nella nuvola | Il meglio di entrambi i mondi |
| **Senza server** | Scala a zero; paghi solo se usato | Traffico sporadico; sensibile ai costi |
| **Inferenza batch** | Elaborare i dati in blocco secondo una pianificazione | Quando il tempo reale non serve |
---

## Analisi comparativa
| Metrico | Cosa misura |
|--------|-----------------|
| **Gettoni al secondo** | Throughput di generazione (più alto è, meglio è) |
| **Tempo al primo token (TTFT)** | Latenza prima che venga visualizzato il primo token di output |
| **Latenza per richiesta** | Tempo totale dall'input all'output completo |
| **Utilizzo della memoria** | VRAM o RAM consumata durante l'inferenza |
| **Produttività** | Richieste servite al secondo |
| **Costo per 1 milione di token** | Costo in dollari per l'elaborazione di 1 milione di token |
---

## Consigli pratici
- **Inizia con la quantizzazione.** La quantizzazione INT4 (AWQ o GPTQ) offre il miglior compromesso tra qualità e dimensione. La maggior parte dei modelli 7B funziona comodamente su una singola GPU consumer a INT4.
- **Utilizza vLLM per la fornitura LLM.** È l'opzione open source più veloce per l'inferenza LLM a throughput elevato.
- **Profilo prima dell'ottimizzazione.** Misura dove viene effettivamente trascorso il tempo. Spesso è la larghezza di banda della memoria, non il calcolo, a rappresentare il collo di bottiglia.
- **Abbina il modello all'attività.** Un modello 7B va bene per la maggior parte delle attività. Non utilizzare 70B quando andrà bene 7B.
- **Considera la distillazione.** Se hai bisogno di un modello piccolo e veloce per la produzione, distilla da un modello più grande anziché addestrarlo da zero.
- **Monitora continuamente.** Le prestazioni del modello possono peggiorare nel tempo man mano che la distribuzione dei dati cambia. Tieni traccia dei parametri di latenza, throughput e qualità.
---

## Riepilogo
L’ottimizzazione del modello è il ponte tra ricerca e produzione. La quantizzazione riduce i modelli di 4-8 volte con una perdita di qualità minima. La potatura rimuove il peso morto. La distillazione trasferisce la conoscenza da modelli grandi a modelli piccoli. I trucchi Flash Attention e KV-cache rendono l'inferenza più veloce. Insieme, queste tecniche trasformano un modello che richiede un data center in uno che funziona su un laptop o un telefono. Il settore si sta muovendo rapidamente: ciò che l'anno scorso richiedeva otto A100 viene eseguito oggi su una GPU consumer.