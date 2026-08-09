---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
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
tags: [recommendation, systems, ai-and-machine-learning]
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
# Sistemi di raccomandazione
I sistemi di raccomandazione prevedono ciò che un utente vorrà vedere, acquistare o interagire in seguito. Alimentano i feed di contenuti sui social media, i suggerimenti di prodotti sui siti di e-commerce, le scelte di film sulle piattaforme di streaming e i risultati di ricerca. Nonostante siano invisibili alla maggior parte degli utenti, sono tra i sistemi di intelligenza artificiale di maggior impatto commerciale al mondo: Netflix stima che il suo motore di raccomandazione faccia risparmiare oltre 1 miliardo di dollari all’anno riducendo il tasso di abbandono degli abbonati.
---

## Perché i consigli sono difficili
| Sfida | Descrizione |
|-----------|-------------|
| **Scala** | Milioni di utenti × milioni di articoli = miliardi di possibili paia |
| **Sparsità** | Ogni utente ha interagito con una piccola frazione di elementi disponibili |
| **Avvio a freddo** | I nuovi utenti e i nuovi elementi non hanno una cronologia delle interazioni |
| **Preferenze dinamiche** | I gusti degli utenti cambiano nel tempo |
| **Oltre la precisione** | Le raccomandazioni devono anche essere diverse, nuove e fortuite |
| **Obiettivi aziendali** | Massimizzare il coinvolgimento ≠ massimizzare il benessere dell'utente |
---

## Approcci fondamentali
### Filtraggio collaborativo
L'idea: se gli utenti A e B erano d'accordo in passato, probabilmente lo saranno anche in futuro.
| Digitare | Come funziona | Esempio |
|------|-------------|---------|
| **Basato sull'utente** | Trova utenti simili; consigliare cosa gli è piaciuto | "Gli utenti a cui è piaciuto questo hanno apprezzato anche..." |
| **Basato sugli articoli** | Trova articoli simili a ciò che già piace all'utente | "Perché hai guardato..." |
| **Fattorizzazione matriciale** | Scomporre la matrice di interazione utente-oggetto in fattori latenti | SVD, ALS (minimi quadrati alternati) |
| Forza | Debolezza |
|----------|----------|
| Non è necessario comprendere gli elementi stessi | Problema di avvio a freddo: non posso consigliare nuovi articoli |
| Cattura preferenze complesse e implicite | Richiede molti dati di interazione |
| Funziona con qualsiasi tipo di contenuto | Bias di popolarità: consiglia articoli già popolari |
### Filtraggio basato sui contenuti
Consiglia articoli simili a quelli che già piacciono all'utente, in base alle caratteristiche dell'articolo.
| Tipo di funzione | Esempio |
|-------------|---------|
| **Testo** | Genere, descrizione, parole chiave, cast |
| **Audio** | Tempo, genere, umore (per la musica) |
| **Visivo** | Tavolozza dei colori, stile (per immagini/moda) |
| **Metadati** | Prezzo, marca, categoria |
| Forza | Debolezza |
|----------|----------|
| Nessun avvio a freddo per gli articoli (le funzionalità sono note) | Impossibile consigliare articoli che non rientrano nei gusti attuali dell'utente |
| Funziona con meno dati di interazione | Richiede una buona progettazione delle funzionalità |
| Spiegabile ("consigliato perché simile a X") | Meno serendipità |
### Approcci ibridi
La maggior parte dei sistemi di produzione combina metodi collaborativi e basati sui contenuti.
| Strategia ibrida | Descrizione |
|----------------|-------------|
| **Ponderato** | Combina punteggi di più modelli |
| **Commutazione** | Utilizzo basato sui contenuti per i nuovi utenti, collaborativo per quelli consolidati |
| **Cascata** | Utilizzare prima un modello semplice, quindi perfezionarlo con uno complesso |
| **Combinazione di funzionalità** | Unisci funzionalità di collaborazione e di contenuto in un unico modello |
| **Metaapprendimento** | Scopri come combinare diversi consiglieri |
---

## Approcci moderni al deep learning
### Modelli a due torri
L'architettura dominante per raccomandazioni su larga scala (utilizzata da YouTube, Pinterest, Spotify).
| Componente | Ruolo |
|-----------|------|
| **Torre utente** | Rete neurale che codifica le funzionalità e la cronologia dell'utente in un incorporamento |
| **Torre degli oggetti** | Rete neurale che codifica le caratteristiche dell'elemento in un incorporamento |
| **Somiglianza** | Somiglianza del prodotto scalare o del coseno tra gli incorporamenti dell'utente e dell'elemento |
| Passo | Descrizione |
|------|-------------|
| 1| Addestra entrambe le torri a produrre incorporamenti simili per coppie utente-elemento che interagiscono |
| 2| Al momento della pubblicazione, precalcola gli incorporamenti degli elementi |
| 3| Per una richiesta utente, calcola l'incorporamento dell'utente |
| 4| Utilizza la ricerca approssimata del vicino più vicino (ANN) per trovare gli articoli più simili |
### Modelli di sequenza per raccomandazioni
Il comportamento degli utenti è sequenziale: ciò che hai guardato ieri influenza ciò che guarderai oggi.
| Modello | Avvicinamento |
|-------|----------|
| **GRU4Rec** | Modello basato su GRU per raccomandazioni basate sulla sessione |
| **SASRec** | Raccomandatore sequenziale basato sull'autoattenzione |
| **BERT4Rec** | Trasformatore bidirezionale per raccomandazioni sequenziali |
| **YouTube DNN** | Rete neurale profonda che tratta la cronologia delle visualizzazioni come una sequenza |
### Recupero vs Classifica
I sistemi moderni dividono le raccomandazioni in due fasi:
| Palcoscenico | Scopo | Metodo |
|-------|---------|--------|
| **Recupero (generazione del candidato)** | Restringi milioni di elementi a circa 1.000 candidati | Modello a due torri; Ricerca RNA; veloce ma approssimativo |
| **Classifica (punteggio)** | Punteggio preciso e ordine dei candidati | Modello profondo con molte funzionalità; più lento ma preciso |
| **Riclassificazione** | Adattarsi alla diversità, alle regole aziendali, alla freschezza | Banditi contestuali; ottimizzazione dei vincoli |
---

## Metriche di valutazione
| Metrico | Cosa misura | Quando usarlo |
|--------|-----------|-------------|
| **Precisione@K** | Frazione delle raccomandazioni top-K rilevanti | Quando ti interessa l'accuratezza delle scelte migliori |
| **Richiamo@K** | Frazione di elementi rilevanti trovati in top-K | Quando ci tieni a non perderti i buoni articoli |
| **NDCG** (guadagno cumulativo scontato normalizzato) | Qualità della classifica; premi mettendo gli elementi rilevanti più in alto | Quando l'ordine in classifica conta |
| **MAP** (precisione media media) | Precisione media tra tutti gli utenti | Qualità della classifica generale |
| **Percentuale di successo@K** | Se almeno un elemento rilevante appare in top-K | Scenari di rilevanza binaria |
| **Copertura** | Frazione di articoli che vengono consigliati | Diversità ed equità |
| **Serendipità** | Raccomandazioni inaspettate ma rilevanti | Soddisfazione dell'utente |
---

## Il problema dell'avvio a freddo
| Scenario | Sfida | Soluzioni |
|----------|-----------|-----------|
| **Nuovo utente** | Nessuna cronologia delle interazioni | Utilizzare i dati demografici; mostrare articoli popolari; utilizzare segnali contestuali (località, dispositivo, ora) |
| **Nuovo oggetto** | Nessuno ha ancora interagito con esso | Utilizzare le funzionalità dei contenuti; strategie di esplorazione-sfruttamento; algoritmi banditi |
| **Nuovo sistema** | Nessun dato | Trasferire l'apprendimento da domini simili; curare il contenuto iniziale |
---

## Esplorazione vs sfruttamento
| Strategia | Descrizione | Scambio |
|----------|-------------|-----------|
| **ε-avido** | Mostra elementi casuali con probabilità ε | Semplice ma inefficiente |
| **Campionamento Thompson** | Campione dalla distribuzione a posteriori della qualità dell'articolo | Di principio; buone proprietà teoriche |
| **Limite di fiducia superiore (UCB)** | Preferire elementi con elevata incertezza | Buon equilibrio tra esplorazione e sfruttamento |
| **Banditi contestuali** | Esplorazione condizionata al contesto utente | Più efficiente dell'esplorazione cieca |
| **Iniezione di diversità** | Includere deliberatamente elementi diversi o nuovi | Semplice; può ridurre l'impegno a breve termine |
---

## Pregiudizi ed equità
| Tipo di polarizzazione | Descrizione | Impatto |
|-----------|-------------|--------|
| **Pregiudizio di popolarità** | Gli articoli più popolari vengono consigliati di più, diventando più popolari | Gli articoli a coda lunga sono sottoserviti |
| **Distorsione di selezione** | I modelli apprendono dalle interazioni osservate, non da tutte quelle possibili | Distorto verso gli utenti attivi |
| **Distorsione di posizione** | Gli elementi mostrati nelle posizioni più alte ottengono più clic indipendentemente dalla qualità | Rafforza le prime posizioni |
| **Distorsione da esposizione** | Gli elementi che sono stati mostrati ricevono più segnali di allenamento | Ciclo di feedback |
| **Pregiudizio demografico** | Le raccomandazioni differiscono in modo ingiusto a seconda dei dati demografici | Discriminazione; esperienza negativa per alcuni gruppi |
### Strategie di mitigazione
| Strategia | Descrizione |
|----------|-------------|
| **Ponderazione della propensione inversa** | Articoli popolari di peso ridotto nell'allenamento |
| **Strati di debiasing** | Aggiungere una componente di debiasing al modello |
| **Vincoli di equità** | Aggiungere vincoli per garantire un trattamento equo |
| **Diverse raccomandazioni** | Ottimizzare esplicitamente per la diversità insieme alla pertinenza |
| **Audit e monitoraggio** | Controllare regolarmente le raccomandazioni per individuare eventuali distorsioni tra i gruppi |
---

## Esempi di settore
| Azienda | Sistema | Avvicinamento |
|---------|--------|----------|
| **Netflix** | Consigli su film/TV | Recupero di due torri + classificazione profonda + banditi contestuali per opere d'arte |
| **YouTube** | Consigli video | Rete neurale profonda per la generazione di candidati; modello di classificazione separato |
| **Spotify** | Consigli musicali | Filtraggio collaborativo + PNL su playlist + analisi audio |
| **Amazzonia** | Consigli sul prodotto | Filtraggio collaborativo articolo per articolo; personalizzato su larga scala |
| **TikTok** | Breve feed video | Apprendimento per rinforzo; forte enfasi sull'esplorazione |
| **Pinterest** | Consigli visivi | Modello a due torri; somiglianza visiva |
---

## Strumenti e framework
| Strumento | Scopo |
|------|---------|
| **Consigli TensorFlow (TFRS)** | Modelli a due torri, recupero, classifica |
| **PyTorch RecSys** | Modelli di raccomandazione orientati alla ricerca |
| **Sorpresa** | Filtraggio collaborativo classico (SVD, NMF, KNN) |
| **Implicito** | Filtraggio collaborativo rapido per feedback implicito (ALS, BPR) |
| **Faiss** (Meta) | Ricerca approssimativa del vicino più vicino su scala |
| **Milvus / Pigna / Weaviate** | Database vettoriali per la ricerca di somiglianze |
| **Raccolta** | Libreria completa di ricerche sulle raccomandazioni |
| **Merlino** (NVIDIA) | Pipeline di raccomandazioni accelerate dalla GPU |
---

## Riepilogo
I sistemi di raccomandazione sono tra le applicazioni di intelligenza artificiale di maggior impatto nel settore. Il campo si è evoluto da un semplice filtraggio collaborativo ad architetture di deep learning che combinano cronologia utente, contenuto degli elementi, segnali contestuali e obiettivi aziendali. I sistemi moderni utilizzano una pipeline di recupero-classificazione-riclassificazione, con modelli a due torri per la generazione rapida dei candidati e modelli profondi per un punteggio preciso. Le sfide – avvio a freddo, pregiudizi, esplorazione e bilanciamento della soddisfazione degli utenti con gli obiettivi aziendali – rimangono aree attive di ricerca e ingegneria.