---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [performance, optimization, coding-and-technology]
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
# Ottimizzazione delle prestazioni
L'ottimizzazione delle prestazioni è la pratica di rendere il software più veloce, riducendo i tempi di risposta, aumentando il throughput, riducendo l'utilizzo della memoria ed eliminando i colli di bottiglia. È una delle competenze di maggiore impatto che uno sviluppatore può avere, perché il software lento perde utenti, spreca risorse e frustra tutti. Ma è anche uno degli errori più comunemente commessi, con gli sviluppatori che ottimizzano le cose sbagliate basandosi sull'intuizione piuttosto che sull'evidenza.
---

## La regola d'oro
> **Prima misura, poi ottimizza.** Non ottimizzare mai in base a supposizioni. Profila il codice, trova il collo di bottiglia effettivo e risolvilo.
| Anti-modello | Perché è brutto |
|-------------|-------------|
| **Ottimizzazione prematura** | Dedicare tempo ad accelerare il codice che non è lento |
| **Ottimizzare senza misurare** | Risolvere il collo di bottiglia sbagliato; nessun modo per verificare il miglioramento |
| **Sacrificare la leggibilità per la velocità** | Il codice illeggibile costa più del guadagno in termini di prestazioni |
| **Memorizza tutto nella cache** | Dati obsoleti, memoria gonfia, complessità |
---

## Profilazione
Prima di poter realizzare qualcosa più velocemente, devi sapere *dove* viene impiegato il tempo.
| Tipo di strumento | Cosa misura | Esempi |
|-----------|-----------|----------|
| **Profilatore CPU** | Quali funzioni consumano più tempo della CPU | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Profilatore di memoria** | Allocazione e perdite di memoria | tracemalloc (Python), Valgrind, heaptrack |
| **Profilatore I/O** | Colli di bottiglia I/O su disco e rete | iotop, strace, Wireshark |
| **APM (Monitoraggio delle prestazioni dell'applicazione)** | Tempistiche delle richieste end-to-end | Nuova Reliquia, Datadog, Jaeger |
| **Strumenti di sviluppo del browser** | Rendering frontend, esecuzione JavaScript, rete | Chrome DevTools, Firefox Profiler |
### Flusso di lavoro della profilazione
| Passo | Descrizione |
|------|-------------|
| 1. Identificare l'operazione lenta | Gli utenti segnalano un caricamento lento della pagina; il monitoraggio mostra un'elevata latenza |
| 2. Profilare il percorso completo | Trova quale componente richiede più tempo |
| 3. Eseguire il drill-down | Profila il componente specifico per trovare la funzione interessante |
| 4. Risolvere il collo di bottiglia | Applicare l'ottimizzazione appropriata |
| 5. Misurare nuovamente | Verificare il miglioramento; controlla le regressioni |
---

## Ottimizzazione algoritmica
I maggiori miglioramenti in termini di prestazioni derivano dalla scelta di algoritmi migliori, non da micro-ottimizzazioni.
| Cambia | Miglioramento |
|--------|------------|
| Ricerca lineare O(n) → Ricerca nella tabella hash O(1) | 100x+ per set di dati di grandi dimensioni |
| Ciclo annidato O(n²) → Ordina + ricerca binaria O(n log n) | Ordini di grandezza per grandi n |
| Calcolo ripetuto → Memoizzazione/caching | Elimina il lavoro ridondante |
| Concatenazione di stringhe in un ciclo → Builder / join | Evita la copiatura di stringhe quadratiche |
| Dati non ordinati → Dati ordinati con ricerca binaria | O(log n) invece di O(n) per ricerca |
---

## Strategie di memorizzazione nella cache
La memorizzazione nella cache memorizza i risultati calcolati in modo che non sia necessario ricalcolarli.
| Tipo di cache | Posizione | Velocità | A vita |
|-----------|----------|-------|----------|
| **Cache della CPU** | L1/L2/L3 | ~1 ns | Automatico |
| **In memoria** | RAM dell'applicazione (dict, HashMap) | ~100 ns | Fino alla liquidazione o allo sfratto |
| **Cache distribuita** | Redis, Memcached | ~1ms | TTL configurabile |
| **CDN** | Server periferici in tutto il mondo | ~10-50ms | TTL configurabile |
| **Cache del browser** | Browser dell'utente | ~1ms | Intestazioni della cache HTTP |
| **Cache delle query del database** | Livello database o ORM | ~1-10 ms | Fino a quando i dati non cambiano |
### Modelli di memorizzazione nella cache
| Modello | Descrizione | Quando usarlo |
|---------|-----|-----|
| **Cache a parte** | L'applicazione controlla la cache; caricamenti da DB in caso di errore; memorizza nella cache | Più comune; semplice |
| **Scrittura** | Scrivi contemporaneamente nella cache e nel DB | Quando legge >> scrive; coerenza importante |
| **Scrivi dietro** | Scrivi nella cache; scrivere in modo asincrono su DB | Velocità di scrittura elevata; qualche rischio di perdita di dati |
| **TTL (Time to Live)** | Le voci della cache scadono dopo un periodo di tempo prestabilito | Quando i dati cambiano periodicamente |
| **Invalidazione** | Rimuovere esplicitamente le voci della cache obsolete | Quando sai esattamente quando cambiano i dati |
### Invalidazione della cache
I due problemi più difficili in informatica: invalidazione della cache, denominazione delle cose ed errori off-by-one.
| Strategia | Descrizione |
|----------|-------------|
| **Basato su TTL** | Le voci scadono dopo N secondi; semplice ma potrebbe contenere dati obsoleti |
| **Basato sugli eventi** | Invalidare quando i dati cambiano; più complesso ma accurato |
| **Basato sulla versione** | Includere un numero di versione; incremento sulle modifiche |
| **Basato su tag** | Voci della cache correlate ai tag; invalidare tutte le voci con un tag |
---

## Ottimizzazione del database
I database rappresentano spesso il più grande collo di bottiglia nelle applicazioni web.
| Tecnica | Descrizione | Impatto |
|-----------|-------------|--------|
| **Indicizzazione** | Aggiungi indici sulle colonne utilizzate in WHERE, JOIN, ORDER BY | Query 10-1000 volte più veloci |
| **Ottimizzazione delle query** | Evita SELEZIONA *; utilizzare EXPLAIN per analizzare le query | Ridurre I/O |
| **Pool di connessione** | Riutilizzare le connessioni al database invece di crearne di nuove | Eliminare il sovraccarico della connessione |
| **Leggi le repliche** | Instradare le query di lettura ai database di replica | Distribuisci il carico di lettura |
| **Partizionamento** | Dividere tabelle di grandi dimensioni in partizioni più piccole | Query più veloci su set di dati di grandi dimensioni |
| **Denormalizzazione** | Aggiungi dati ridondanti per evitare unioni | Letture più veloci; più lento scrive |
| **Viste materializzate** | Risultati della query precalcolati | Query complesse istantanee |
| **Prevenzione N+1** | Utilizza JOIN, caricamento rapido o query batch | Elimina migliaia di query |
---

## Concorrenza e parallelismo
| Concetto | Descrizione | Quando usarlo |
|---------|-----|-----|
| **Filettatura** | Più thread all'interno di un singolo processo | Attività legate a I/O (rete, disco) |
| **Multielaborazione** | Processi multipli (ignora GIL in Python) | Attività legate alla CPU |
| **Asincrono/attendi** | Multitasking cooperativo; filo unico | I/O ad alta concorrenza (server Web) |
| **Calcolo GPU** | Migliaia di nuclei paralleli | Operazioni su matrici; elaborazione delle immagini; Ml |
### Asincrono e threading
| Aspetto | Asincrono/Aspetta | Filettatura |
|--------|------------|-----------|
| **Modello** | Cooperativa (controllo rendimento compiti) | Preemptive (il sistema operativo cambia thread) |
| **In alto** | Molto basso (nessun cambio di contesto) | Superiore (creazione di thread, cambio di contesto) |
| **Complessità** | Ragionamento più semplice (thread singolo) | Condizioni di gara, situazioni di stallo, blocchi |
| **Ideale per** | Molte operazioni I/O simultanee | Blocco delle operazioni che non possono essere rese asincrone |
| **Limitazione** | Impossibile utilizzare il codice associato alla CPU senza bloccare | GIL in Python limita il vero parallelismo |
---

## Prestazioni del frontend
| Tecnica | Descrizione | Impatto |
|-----------|-------------|--------|
| **Minificazione** | Rimuovi gli spazi bianchi e accorcia i nomi delle variabili | File più piccoli del 20-40% |
| **Bundling** | Combina più file in meno richieste | Meno richieste HTTP |
| **Suddivisione del codice** | Carica solo il codice necessario per la pagina corrente | Caricamento iniziale più veloce |
| **Caricamento lento** | Carica immagini e componenti quando sono necessari | Rendering iniziale più veloce |
| **Tremore dell'albero** | Rimuovi il codice inutilizzato dai bundle | Pacchetti più piccoli |
| **Ottimizzazione dell'immagine** | Utilizza WebP/AVIF; immagini reattive; caricamento lento | Immagini più piccole del 50-80% |
| **CDN** | Servire risorse statiche da server periferici | Latenza inferiore a livello globale |
| **HTTP/2 e HTTP/3** | Multiplexing; compressione dell'intestazione; 0-RTT | Overhead del protocollo più veloce |
| **Addetti ai servizi** | Memorizzare nella cache le risorse per l'utilizzo offline; notifiche push | Visite ripetute più veloci |
---

## Ottimizzazione della memoria
| Tecnica | Descrizione |
|-----------|-------------|
| **Pool di oggetti** | Riutilizzare gli oggetti invece di crearne di nuovi |
| **Streaming** | Elaborare i dati in blocchi invece di caricare tutto in memoria |
| **Generatori/iteratori** | Ottieni valori uno alla volta invece di creare elenchi |
| **File mappati in memoria** | Accedi a file di grandi dimensioni senza caricarli interamente |
| **Ottimizzazione della raccolta dei rifiuti** | Regola i parametri GC per il tuo carico di lavoro |
| **Scelta della struttura dei dati** | Utilizza array invece di elenchi collegati per la località della cache; utilizzare i set per testare l'appartenenza |
---

## Ottimizzazione della rete
| Tecnica | Descrizione |
|-----------|-------------|
| **Compressione** | gzip, brotli per le risposte HTTP |
| **Riutilizzo della connessione** | Connessioni keep-alive; Multiplexing HTTP/2 |
| **Richiedi batch** | Combina più chiamate API in una |
| **Impaginazione** | Caricare i dati in pagine invece che tutti in una volta |
| **Compressione a riposo** | Comprimere i dati nei database e nella cache |
| **Scelta del protocollo** | gRPC (binario, efficiente) vs REST (leggibile dall'uomo) |
---

## Monitoraggio e avvisi
| Metrico | Cosa ti dice |
|--------|------------|
| **Latenza P50 / P95 / P99** | Tempo di risposta ai vari percentili |
| **Produttività** | Richieste al secondo |
| **Tasso di errore** | Percentuale di richieste non riuscite |
| **Utilizzo CPU** | Quanta capacità di elaborazione viene utilizzata |
| **Utilizzo della memoria** | Consumo di RAM; avvicinarsi ai limiti? |
| **Tempo di interrogazione del database** | Query lente che necessitano di ottimizzazione |
---

## Riepilogo
L'ottimizzazione delle prestazioni è un processo sistematico: misurare, identificare il collo di bottiglia, risolverlo, misurare nuovamente. I maggiori successi derivano dai miglioramenti algoritmici e dall’eliminazione del lavoro non necessario, non dalle micro-ottimizzazioni. La memorizzazione nella cache, l'indicizzazione del database e la concorrenza sono gli strumenti più potenti. Le prestazioni del frontend dipendono dalla riduzione al minimo delle dimensioni del carico utile e dei viaggi di andata e ritorno. E la regola più importante è sempre la stessa: non indovinare: profilo.