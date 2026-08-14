---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Errori nella pipeline di dati e nell'ETL
Le pipeline di dati sono l'impianto idraulico delle organizzazioni moderne: spostano i dati dai sistemi di origine attraverso trasformazioni nei database, nei magazzini e nei laghi dove vengono utilizzati per l'analisi, l'apprendimento automatico e il processo decisionale. Quando funzionano, nessuno se ne accorge. Quando falliscono, le decisioni vengono prese su dati obsoleti, i modelli si addestrano sulla spazzatura, i report mostrano numeri impossibili e la fiducia nell’intera piattaforma dati si indebolisce. I guasti alle pipeline di dati sono tra i guasti più comuni e più costosi nelle organizzazioni tecnologiche.
---

## Modalità di errore comuni
### Problemi di qualità dei dati
| Fallimento | Descrizione | Impatto | Difficoltà di rilevamento |
|---------|-----|--------|---------------------|
| **Corruzione silenziosa dei dati** | I dati vengono modificati in modo errato senza che venga generato alcun errore | I sistemi a valle si fidano di dati errati; decisioni basate su informazioni false | Molto difficile: nessun segnale di errore |
| **Deriva dello schema** | Il sistema di origine modifica lo schema (aggiunge, rimuove, rinomina colonne) | La pipeline si rompe o rilascia silenziosamente i dati | Medio: la pipeline potrebbe non funzionare o produrre risultati parziali |
| **Tipo di dati non corrispondente** | L'origine invia la stringa dove è previsto l'intero; modifiche alla precisione del float | La pipeline fallisce; dati troncati; errori di arrotondamento | Medio: potrebbe causare errori nella pipeline o problemi relativi ai dati |
| **Record duplicati** | Stesso evento elaborato più volte | Conteggi gonfiati; aggregazioni errate | Difficile: ogni record sembra valido individualmente |
| **Valori nulli/mancanti** | I campi previsti sono vuoti | I calcoli falliscono; i modelli producono previsioni errate | Medio: dipende dalla gestione dei valori nulli |
| **Valori fuori range** | Valori fuori dai limiti previsti (età negative; date future) | Statistiche distorte; logica aziendale rotta | Medio: richiede regole di convalida |
| **Dati arrivati ​​in ritardo** | I dati arrivano dopo la chiusura della finestra di elaborazione | Risultati incompleti; record mancati | Difficile: i risultati sembrano completi ma non lo sono |
### Problemi relativi all'infrastruttura della pipeline
| Fallimento | Descrizione | Impatto |
|---------|-----|--------|
| **Errore dell'orchestrazione** | Lo scheduler (Airflow, Prefect) non attiva la pipeline | I dati sono obsoleti; non avviene alcuna elaborazione |
| **Esaurimento risorse** | La pipeline esaurisce la memoria, la CPU o il disco | Crash della pipeline; risultati parziali |
| **Errore della dipendenza** | Il sistema a monte è inattivo o lento | La pipeline attende per un tempo indefinito o fallisce |
| **Problemi di concorrenza** | Più pipeline modificano gli stessi dati contemporaneamente | Condizioni di gara; corruzione dei dati |
| **Deriva della configurazione** | Modifiche all'ambiente (rete, credenziali, endpoint) non riflesse nella pipeline | La pipeline si guasta inaspettatamente |
| **Contropressione** | I dati arrivano più velocemente di quanto la pipeline possa elaborare | Code crescenti; latenza crescente |
---

## Casi di studio
### Caso di studio 1: Duplicazione silenziosa dei dati
| Aspetto | Descrizione |
|--------|-------------|
| **Scenario** | La pipeline degli ordini di un'azienda di e-commerce elabora gli eventi da una coda di messaggi |
| **Cosa è andato storto** | Un riavvio del consumer ha causato il riutilizzo dei messaggi; non esisteva alcuna logica di deduplicazione |
| **Impatto** | I dati sui ricavi sono stati gonfiati del 15% per 3 settimane prima che qualcuno se ne accorgesse |
| **Causa principale** | Nessuna chiave di idempotenza; consegna almeno una volta senza deduplicazione |
| **Correzione** | Aggiunte chiavi di idempotenza basate sull'ID ordine; implementata la semantica esattamente una volta |
| **Lezione** | La consegna almeno una volta richiede la deduplicazione; convalidare sempre i totali rispetto ai sistemi di origine |
### Caso di studio 2: La modifica dello schema si interrompe a valle
| Aspetto | Descrizione |
|--------|-------------|
| **Scenario** | Un fornitore di servizi di pagamento modifica il nome di un campo nella risposta API |
| **Cosa è andato storto** | La pipeline ETL ha iniziato silenziosamente a scrivere valori null; nessuna convalida dello schema |
| **Impatto** | I rapporti finanziari hanno mostrato entrate pari a zero con quel metodo di pagamento per 2 mesi |
| **Causa principale** | Nessuna convalida dello schema al momento dell'acquisizione; valori nulli trattati come validi |
| **Correzione** | Aggiunta la convalida dello schema con avvisi; campi obbligatori applicati; controlli nulli |
| **Lezione** | Non fidarsi mai della stabilità degli schemi esterni; convalidare al confine |
### Caso di studio 3: Catastrofe del fuso orario
| Aspetto | Descrizione |
|--------|-------------|
| **Scenario** | Un'azienda globale aggrega parametri giornalieri tra gli uffici |
| **Cosa è andato storto** | Alcune fonti utilizzavano l'UTC, altre l'ora locale; la pipeline non si è normalizzata |
| **Impatto** | I totali giornalieri non corrispondevano; alcune transazioni conteggiate nel giorno sbagliato; la chiusura di fine mese era sbagliata |
| **Causa principale** | Nessuna politica di fuso orario standard; timestamp memorizzati in modo incoerente |
| **Correzione** | Tutti i timestamp memorizzati come UTC; conversione all'ora locale solo a livello di presentazione |
| **Lezione** | Standardizzare su UTC ovunque; essere espliciti sui fusi orari ad ogni confine |
---

## Strategie di prevenzione
### Convalida dei dati
| Strategia | Descrizione | Esempi di strumenti |
|----------|-------------|---------------|
| **Convalida dello schema** | Verificare che i dati corrispondano allo schema previsto in ogni fase | Grandi aspettative; Deequ; Soda |
| **Controlli della portata** | I valori rientrano nei limiti previsti | Affermazioni personalizzate; test dbt |
| **Controlli di freschezza** | I dati sono sufficientemente recenti per essere utili | Monitoraggio dei timestamp; Avvisi SLA |
| **Controlli del volume** | I conteggi delle righe rientrano nell'intervallo previsto | Rilevamento di anomalie sui conteggi delle righe |
| **Integrità referenziale** | Le chiavi esterne corrispondono; nessun record orfano | Vincoli SQL; strumenti per la qualità dei dati |
| **Riconciliazione tra sorgenti** | I totali corrispondono tra origine e destinazione | Lavori di riconciliazione automatizzata |
### Modelli di progettazione della pipeline
| Modello | Descrizione | Vantaggio |
|---------|-----|---------|
| **Idempotenza** | L'esecuzione della pipeline più volte produce lo stesso risultato | È sicuro riprovare; nessun duplicato |
| **Atomicità** | La pipeline ha esito positivo o negativo completo (nessuno stato parziale) | Nessun dato elaborato a metà |
| **Checkpoint** | Salva i progressi in ogni fase; riprendere dall'ultimo checkpoint | Tolleranza ai guasti; nessun ritrattamento |
| **Code di lettere non consegnate** | I record non riusciti vengono inseriti in una coda separata per l'analisi | Nessuna perdita di dati; può indagare e riprodurre |
| **Interruttori automatici** | Interrompere l'elaborazione quando il downstream non funziona | Prevenire guasti a cascata |
| **Contratti dati** | Accordo tra produttori e consumatori sul formato dei dati | Le modifiche allo schema sono coordinate |
### Monitoraggio e avvisi
| Cosa monitorare | Perché | Come |
|-----------------|-----|-----|
| **Durata del gasdotto** | L'aumento della durata segnala problemi | Analisi delle tendenze; Monitoraggio SLA |
| **Conta le righe** | Cambiamenti improvvisi indicano problemi | Confrontare con le medie storiche |
| **Tariffe nulle** | Problemi di schema o origine del segnale null in aumento | Tracciamento null a livello di colonna |
| **Freschezza dei dati** | I dati non aggiornati indicano che la pipeline non è in esecuzione | Timestamp dell'ultimo record |
| **Impatto a valle** | I report e i modelli utilizzano dati corretti? | Derivazione dei dati end-to-end |
| **Utilizzo delle risorse** | PROCESSORE; memoria; disco; rete | Monitoraggio delle infrastrutture |
---

## Strategie di recupero
| Situazione | Strategia |
|-----------|----------|
| **Dati errati già in magazzino** | Identificare l'intervallo di tempo interessato; rielaborare dalla fonte; informare i consumatori a valle |
| **Guasto alla pipeline a metà corsa** | Il design idempotente consente la riesecuzione sicura; il checkpoint consente di riprendere |
| **La modifica dello schema ha interrotto la pipeline** | Correzione della trasformazione; recuperare i dati interessati; aggiungere la gestione dell'evoluzione dello schema |
| **Corruzione silenziosa scoperta tardi** | Analisi delle cause profonde; determinare il raggio dell'esplosione; rielaborare; aggiungere il monitoraggio per individuare la ricorrenza |
| **Perdita di dati** | Ripristina dal backup; riproduzione dalla fonte; valutare se la perdita è recuperabile |
---

## Riepilogo
I guasti alle pipeline di dati sono onnipresenti e spesso più costosi delle interruzioni delle applicazioni perché producono risposte sbagliate anziché errori evidenti. I colpevoli più comuni sono il danneggiamento silenzioso dei dati, la deriva dello schema, i duplicati, i bug del fuso orario e i valori mancanti. Le principali strategie di prevenzione sono: convalidare i dati ad ogni confine (schema, intervallo, volume, freschezza); progettare condutture idempotenti e atomiche; monitorare tutto (durata, conteggi di righe, tassi nulli, freschezza); utilizzare code di messaggi non recapitabili per i record non riusciti; e stabilire contratti sui dati tra produttori e consumatori. Quando si verificano guasti, la risposta dovrebbe includere l’analisi della causa principale, la rielaborazione dei dati interessati, la notifica ai consumatori a valle e, soprattutto, l’aggiunta del monitoraggio per individuare la stessa classe di guasti in futuro. Le organizzazioni che riescono a farlo nel modo giusto trattano le pipeline di dati con lo stesso rigore del software di produzione: test, monitoraggio, avvisi, risposta agli incidenti e autopsie.