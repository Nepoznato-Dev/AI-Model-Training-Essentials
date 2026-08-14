---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, engineering, mlops, ai-and-machine-learning]
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
# Ingegneria ML e MLOps
Costruire un modello di machine learning è solo metà dell’opera. Metterlo in produzione, mantenerlo in esecuzione in modo affidabile, monitorarne la deriva ed eseguirne l'iterazione: è qui che entrano in gioco l'ingegneria ML e MLOps. Questo file copre l'intero ciclo di vita dall'esperimento al sistema di produzione.
---

## Il ciclo di vita del machine learning
| Fase | Descrizione | Attività chiave |
|-------|-------------|-------|
| **1. Definizione del problema** | Inquadra il problema aziendale come un'attività di machine learning | Definire metriche, vincoli, criteri di successo |
| **2. Raccolta dati** | Raccogliere ed etichettare i dati di addestramento | ETL, etichettatura, aumento |
| **3. Sperimentazione** | Formare e valutare i modelli | Ingegneria delle funzionalità, ottimizzazione degli iperparametri |
| **4. Selezione del modello** | Scegli il modello migliore | Confronta i parametri, valuta i compromessi |
| **5. Distribuzione** | Spedire il modello alla produzione | Al servizio dell'infrastruttura, API, batch |
| **6. Monitoraggio** | Attenzione alla deriva e al degrado | Deriva dei dati, deriva dei concetti, performance |
| **7. Riqualificazione** | Aggiorna il modello con nuovi dati | Riqualificazione programmata o attivata |
La maggior parte del valore (e della difficoltà) è nelle fasi 5–7. Una modella seduta su un taccuino Jupyter non crea valore aziendale.
---

## Modelli di servizio modello
| Modello | Descrizione | Latenza | Caso d'uso |
|---------|-----|---------|----------|
| **Inferenza batch** | Esegui il modello su un batch di dati secondo una pianificazione | Ore | Raccomandazioni giornaliere, punteggio di frode |
| **Inferenza online** | Previsione in tempo reale per richiesta | Millisecondi | Classifica della ricerca, classificazione in tempo reale |
| **Inferenza sullo streaming** | Elaborare previsioni su un flusso di dati | Secondi | Rilevamento anomalie, elaborazione eventi |
### Al servizio delle infrastrutture
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **Servizio TensorFlow** | Server modello | Modelli TensorFlow |
| **TorciaServe** | Server modello | Modelli PyTorch |
| **Server di inferenza Triton** | Multi-quadro | Inferenza GPU, framework multipli |
| **vLLM** | Servizio LLM | Inferenza LLM ad alto rendimento |
| **BentoML** | Servizio unificato | Distribuzione indipendente dal framework |
| **Seldon** | K8s-nativo | Distribuzione del modello Kubernetes |
| **Ray Serve** | Servizio scalabile | Modelli di grandi dimensioni, inferenza distribuita |
---

## Registri dei modelli
Un registro dei modelli è un archivio centralizzato per la gestione dei modelli ML: versioni, metadati, parametri e stato di distribuzione.
| Capacità | Descrizione |
|-----------|-------------|
| **Versione** | Tieni traccia di ogni versione del modello con ID univoco |
| **Metadati** | Dati di training, iperparametri, metriche, autore |
| **Transizioni di scena** | Spostare i modelli attraverso le fasi: Allestimento → Produzione → Archiviato |
| **Lignaggio** | Traccia quali dati e codici hanno prodotto ciascun modello |
| Strumento | Descrizione |
|------|-------------|
| **MLflow** | Open source; registro dei modelli + monitoraggio degli esperimenti |
| **Pesi e pregiudizi (W&B)** | Commerciale; monitoraggio degli esperimenti + registro dei modelli |
| **DVC** | Versionamento di dati e modelli con Git |
| **Azure ML/SageMaker** | Gestione dei modelli nativi del cloud |
---

## Monitoraggio degli esperimenti
Ogni esperimento di ML dovrebbe essere monitorato: quali dati sono stati utilizzati, quali iperparametri, quali metriche hanno prodotto.
| Strumento | Caratteristiche principali |
|------|-------------|
| **MLflow** | Open source, ospitato autonomamente, tiene traccia di parametri/metriche/artefatti |
| **W&B** | Ricca interfaccia utente, spazzate, controllo delle versioni degli artefatti, report |
| **Nettuno** | Archivio di metadati per MLOps |
| **TensorBoard** | Integrato in TensorFlow; visualizzare le curve di allenamento |
### Cosa monitorare
| Categoria | Esempi |
|----------|---------|
| **Parametri** | Tasso di apprendimento, dimensione del batch, architettura del modello, numero di epoche |
| **Metriche** | Precisione, perdita, F1, AUC-ROC (per epoca e finale) |
| **Manufatti** | Pesi dei modelli, matrici di confusione, campioni di previsione |
| **Dati** | Versione del set di dati, rapporti di suddivisione, passaggi di preelaborazione |
| **Ambiente** | Versione Python, versioni della libreria, hardware |
---

## Strategie di distribuzione del modello
| Strategia | Come funziona | Rischio |
|----------|-------------|------|
| **Distribuzione ombra** | Il nuovo modello si affianca al vecchio; pronostici confrontati ma non serviti | Rischio zero; convalida prima di andare in diretta |
| **Versione alle Canarie** | Indirizzare una piccola percentuale di traffico al nuovo modello; aumentare gradualmente | Basso rischio; rollback veloce |
| **Test A/B** | Dividere gli utenti tra vecchi e nuovi; confrontare i parametri aziendali | Misura l'impatto reale |
| **Blu-Verde** | Due ambienti identici; scambia tutto il traffico contemporaneamente | Rollback istantaneo; doppio costo durante la transizione |
| **Flag funzionalità** | Attiva/disattiva il modello per segmento utente | Controllo a grana fine |
---

## Monitoraggio dei sistemi ML
I sistemi ML necessitano di un monitoraggio maggiore rispetto ai software tradizionali perché i dati stessi possono cambiare.
### Tipi di deriva
| Tipo di deriva | Cosa cambia | Esempio |
|-----------|-------------|---------|
| **Driva dei dati** | Cambiamenti nella distribuzione degli input | Cambiamento demografico dei clienti dopo una campagna di marketing |
| **Deriva del concetto** | Il rapporto tra input e output cambia | Cambiamenti nel comportamento dei consumatori durante una recessione |
| **Deriva dell'etichetta** | Cambiamenti nella distribuzione target | Il tasso di frode aumenta dall'1% al 5% |
### Cosa monitorare
| Categoria | Metriche |
|----------|---------|
| **Prestazioni del modello** | Accuratezza, precisione, richiamo, F1, AUC (rispetto al basale) |
| **Qualità dei dati** | Valori mancanti, distribuzioni di caratteristiche, valori anomali |
| **Rilevamento della deriva** | Test statistici (test KS, PSI, divergenza KL) |
| **Infrastrutture** | Latenza, throughput, utilizzo della GPU, memoria |
| **Metriche aziendali** | Tasso di conversione, impatto sulle entrate, soddisfazione degli utenti |
### Strumenti di monitoraggio
| Strumento | Digitare |
|------|------|
| **Evidentemente AI** | Deriva dei dati open source e monitoraggio delle prestazioni dei modelli |
| **Grafana** | Visualizzazione dashboard (funziona con Prometheus) |
| **PerchéLabs** | Piattaforma di osservabilità dei dati |
| **Arize** | Osservabilità del ML e analisi delle cause principali |
| **Prometeo + Grafana** | Metriche dell'infrastruttura e dell'applicazione |
---

## Formazione riproducibile
Riproducibilità significa che puoi ripetere un esperimento e ottenere lo stesso risultato. È essenziale per il debug, il controllo e la conformità.
### Requisiti
| Requisito | Come raggiungerlo |
|-------------|-------------|
| **Versione dei dati** | DVC, Delta Lake o snapshot di set di dati con hash |
| **Versione del codice** | Git per tutto il codice di formazione |
| **Bloccaggio dell'ambiente** | `requirements.txt`,`conda env`, Immagini Docker con versioni esatte |
| **Impostazione del seme** | Correggi i semi casuali per Numpy, Torch, Tensorflow |
| **Gestione configurazione** | Configurazioni Hydra, OmegaConf o YAML per tutti gli iperparametri |
| **Tracciamento degli artefatti** | MLflow o W&B per registrare ogni esperimento |
---

## Inferenza di ridimensionamento
Quando un modello deve soddisfare milioni di richieste al giorno, le prestazioni contano.
| Tecnica | Descrizione |
|-----------|-------------|
| **Batch** | Raggruppare più richieste in un unico passaggio di inoltro |
| **Quantizzazione** | Ridurre la precisione del modello (FP32 → INT8 o INT4) per un'inferenza più rapida |
| **Distillazione modello** | Addestra un modello più piccolo per imitarne uno più grande |
| **Potatura** | Rimuovere pesi o neuroni non importanti |
| **Memorizzazione nella cache** | Memorizza nella cache le previsioni frequenti per evitare il ricalcolo |
| **Ottimizzazione GPU** | TensorRT, runtime ONNX, attenzione Flash |
| **Ridimensionamento orizzontale** | Esegui più repliche di modelli dietro un sistema di bilanciamento del carico |
---

## Flag di funzionalità per ML
I flag di funzionalità ti consentono di controllare quale versione del modello serve quali utenti, senza ridistribuirli.
| Caso d'uso | Descrizione |
|----------|-------------|
| **Implementazione graduale** | Offri il nuovo modello al 5% degli utenti, quindi aumenta |
| **Interruttore di interruzione** | Torna immediatamente al modello precedente se vengono rilevati problemi |
| **Basato sul segmento** | Diversi modelli per diversi segmenti di utenti |
| **Sperimentazione** | Varianti del modello di test A/B con metriche aziendali |
Strumenti: LaunchDarkly, Unleash, Flagsmith o semplici flag di funzionalità supportati da database.
---

## La curva di maturità di MLOps
| Livello | Caratteristiche |
|-------|----------------|
| **Livello 0 — Manuale** | Formazione manuale, distribuzione manuale, nessun monitoraggio |
| **Livello 1 — Sperimentazione** | Tracciamento degli esperimenti, registro dei modelli, CI di base |
| **Livello 2 — Automazione** | Riqualificazione automatizzata, CI/CD per modelli, test automatizzati |
| **Livello 3: pipeline completa** | Pipeline automatizzata end-to-end con monitoraggio, rilevamento della deriva e riqualificazione automatica |
La maggior parte delle organizzazioni si colloca tra il livello 0 e il livello 1. L'obiettivo è il livello 2-3, in cui il ciclo di vita del machine learning è automatizzato e autoriparante.