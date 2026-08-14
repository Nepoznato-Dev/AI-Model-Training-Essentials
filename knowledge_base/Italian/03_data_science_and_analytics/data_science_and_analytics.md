<!--
---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Scienza dei dati e analisi
La scienza dei dati è la disciplina che trasforma i dati grezzi in informazioni fruibili. Si trova all’intersezione tra statistica, informatica e competenze di settore ed è diventato essenziale in ogni settore, dalla finanza alla sanità. Questo file illustra i concetti fondamentali, gli strumenti e i flussi di lavoro che ogni professionista dovrebbe conoscere.
---

## Il processo di scienza dei dati
La maggior parte dei progetti segue alcune varianti di **CRISP-DM**, il ciclo di vita standard del settore:
| Fase | Cosa succede | Orario tipico |
|-------|-------------|------|
| **Comprensione aziendale** | Definire obiettivi, parametri di successo e vincoli | 10–15% |
| **Comprensione dei dati** | Raccogli, esplora e profila i dati | 10–15% |
| **Preparazione dei dati** | Pulisci, trasforma, ingegnerizza le funzionalità | ~50–60% |
| **Modellazione** | Selezionare e addestrare i modelli | 10–15% |
| **Valutazione** | Valutare le prestazioni rispetto agli obiettivi aziendali | 5–10% |
| **Distribuzione** | Spedire il modello alla produzione | 5–10% |
Si stima che la preparazione dei dati, in particolare la pulizia dei dati, richieda circa l'80% del tempo di un data scientist.
---

## Tipi di dati in breve
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Strutturato** | Organizzato in righe e colonne | Tabelle SQL, fogli di calcolo |
| **Non strutturato** | Nessun formato predefinito | Testi, immagini, audio, video |
| **Semistrutturato** | Una certa organizzazione ma flessibile | JSON, XML, HTML |
| **Serie storica** | Dati sequenziali indicizzati per ora | Quotazioni azionarie, letture dei sensori |
| **Spaziale** | Geografico o basato sulla posizione | Coordinate GPS, dati mappa |
| **Grafico** | Nodi e spigoli che rappresentano le relazioni | Social network, grafici della conoscenza |
---

## Fondamenti di statistica
### Statistica descrittiva e inferenziale
Le statistiche descrittive riassumono ciò che *hai*; le statistiche inferenziali ti consentono di trarre conclusioni su ciò che *non* hai (la popolazione più ampia).
| Concetto | Idee chiave |
|---------|-----------|
| **Tendenza centrale** | Media (sensibile ai valori anomali), mediana (robusta), moda (più frequente) |
| **Dispersione** | Intervallo, varianza, deviazione standard, intervallo interquartile |
| **Forma di distribuzione** | Asimmetria (asimmetria), curtosi (pesantezza della coda) |
| **Verifica di ipotesi** | Ipotesi nulla vs alternativa, valori p, livello di significatività (α) |
| **Intervalli di confidenza** | Intervallo che probabilmente contiene il vero parametro della popolazione |
| **Errori di tipo I/tipo II** | Falso positivo (rifiuto di un vero nullo) / falso negativo (manca un effetto reale) |
### Test statistici comuni
| Prova | Quando usarlo |
|------|-------------|
| **t-test** | Confronta le medie tra due gruppi |
| **ANOVA** | Confronta le medie di tre o più gruppi |
| **Chi-quadrato** | Testare l'indipendenza delle variabili categoriali |
| **U Mann-Whitney** | Alternativa non parametrica al t-test (nessuna ipotesi di normalità) |
| **Correlazione di Pearson** | Relazione lineare tra due variabili continue |
| **Correlazione di Spearman** | Relazione monotona (basata sul rango, più robusta) |
### Distribuzioni di probabilità che vale la pena conoscere
| Distribuzione | Caso d'uso |
|-------------|----------|
| **Normale** | Fenomeni naturali, errori di misurazione: la classica curva a campana |
| **Binomiale** | Conta il successo/fallimento (lanci di monete, tassi di conversione) |
| **Poisson** | Conteggio degli eventi in un intervallo fisso (chiamate per ora, difetti per lotto) |
| **Esponenziale** | Tempo tra gli eventi (tempi di attesa, intervalli di guasto) |
| **t-Distribuzione** | Campioni piccoli o varianza sconosciuta della popolazione |
| **Chi-quadrato** | Analisi dei dati categorici, test di bontà di adattamento |
---

## Raccolta e archiviazione dei dati
### Da dove provengono i dati
I dati del mondo reale provengono da molte fonti: database relazionali, API (REST, GraphQL), file flat (CSV, JSON, Parquet), piattaforme di streaming (Kafka, Kinesis), sondaggi e archivi pubblici (Kaggle, portali governativi). Il formato che ricevi determina gran parte della tua strategia di preelaborazione.
### Concetti di data warehousing
| Concetto | Descrizione |
|---------|-----|
| **ETL** | Estrai → Trasforma → Carica: approccio tradizionale alla pipeline |
| **ELT** | Estrai → Carica → Trasforma: approccio cloud moderno (caricamento grezzo, trasformazione in magazzino) |
| **Data Lake** | Dati grezzi archiviati in formato nativo (schema-on-read) |
| **Data Warehouse** | Dati strutturati ed elaborati ottimizzati per l'analisi (schema-on-write) |
| **DataMart** | Un sottoinsieme di un magazzino, limitato a un reparto o dominio |
| **Schema stella** | Tabella dei fatti centrale circondata da tabelle delle dimensioni |
| **Schema del fiocco di neve** | Tabelle delle dimensioni normalizzate (meno ridondanza, più join) |
### Tipi di database
| Digitare | Esempi | Ideale per |
|------|----------|----------|
| **Relazionale (SQL)** | PostgreSQL, MySQL, Oracle | Dati strutturati, transazioni ACID |
| **Documento** | MongoDB, CouchDB | Schemi flessibili, dati simili a JSON |
| **Valore-chiave** | Redis, DynamoDB | Caching, sessioni, ricerche semplici |
| **Famiglia di colonne** | Cassandra, HBase | Carichi di lavoro pesanti in scrittura, serie temporali |
| **Grafico** | Neo4j, Amazon Nettuno | Relazioni, social network |
| **Serie temporali** | DB afflusso, DB scala temporale | Metriche IoT, monitoraggio |
| **Vettore** | Pigna, Milvo | Incorporamento dello spazio di archiviazione per la ricerca ML/AI |
---

## Preelaborazione dei dati e ingegneria delle funzionalità
### Lista di controllo per la pulizia
Ogni set di dati reale presenta problemi. Ecco la pulizia standard:
| Problema | Avvicinamento |
|-------|----------|
| **Valori mancanti** | Imputazione (media, mediana, previsione) o cancellazione se sparsa |
| **Valori anomali** | Rilevamento tramite IQR o punteggio Z; trattare con capping o trasformazione |
| **Duplicati** | Identificare e rimuovere |
| **Incoerenze** | Standardizza formati, correggi errori di battitura, normalizza unità |
### Tecniche di trasformazione
| Tecnica | Cosa fa |
|-----------|-------------|
| **Normalizzazione** | Ridimensiona i valori nell'intervallo 0–1 |
| **Standardizzazione** | Punteggio Z: media = 0, std = 1 |
| **Codifica one-hot** | Converte le categorie in colonne binarie |
| **Codifica etichetta** | Assegna etichette intere alle categorie |
| **Trasformazione registro** | Riduce l'inclinazione a destra dei dati |
| **Cestinamento** | Raggruppa valori continui in intervalli discreti |
### Ingegneria delle funzionalità
L'ingegneria delle funzionalità spesso fa la differenza tra un modello mediocre e uno eccezionale. Le tecniche chiave includono:
- **Creazione di funzionalità**: derivazione di nuove colonne da quelle esistenti (ad esempio,`age_group`da`age`).
- **Selezione funzionalità**: metodi filtro (correlazione), metodi wrapper (eliminazione ricorsiva), metodi incorporati (LASSO, importanza dell'albero).
- **Riduzione della dimensionalità**: PCA per lineare, t-SNE o UMAP per la visualizzazione.
- **Termini di interazione**: combinazione moltiplicativa di funzionalità per catturare effetti congiunti.
---

## Analisi esplorativa dei dati (EDA)
EDA è il luogo in cui sviluppi l'intuizione sui tuoi dati prima della modellazione. L’obiettivo è individuare modelli, anomalie e relazioni.
### Scegliere il grafico giusto
| Tipo di grafico | Ideale per |
|-----------|----------|
| **Istogramma** | Distribuzione di una singola variabile |
| **Box plot** | Riepilogo di cinque numeri, rilevamento di valori anomali |
| **Grafico a dispersione** | Relazione tra due variabili continue |
| **Mappa termica** | Matrici di correlazione, visualizzazione della densità |
| **Grafico a barre** | Categorie a confronto |
| **Grafico a linee** | Tendenze nel tempo |
| **Trama del violino** | Densità di distribuzione + riepilogo del box plot |
| **Trama di coppia** | Panoramica rapida di tutte le coppie di variabili |
### Lo stack EDA Python
| Biblioteca | Ruolo |
|---------|------|
| **panda** | Manipolazione e analisi dei dati |
| **stupido** | Calcolo numerico |
| **matplotlib** | Trama della fondazione |
| **nato dal mare** | Visualizzazione statistica (basata su matplotlib) |
| **trama** | Visualizzazioni interattive basate sul web |
| **scipy** | Calcolo scientifico e statistica |
---

## Apprendimento automatico nella scienza dei dati
### Apprendimento supervisionato in breve
| Compito | Algoritmi |
|------|-----------|
| **Regressione** (prevedere un numero) | Lineare, Ridge/LASSO, Albero decisionale, Foresta casuale, Potenziamento gradiente (XGBoost, LightGBM) |
| **Classificazione** (prevedere una categoria) | Regressione logistica, k-NN, Naive Bayes, SVM, alberi decisionali, foresta casuale, reti neurali |
### Apprendimento non supervisionato in breve
| Compito | Algoritmi |
|------|-----------|
| **Clustering** | Modelli k-medie, gerarchici, DBSCAN, miscela gaussiana |
| **Riduzione della dimensionalità** | PCA, t-SNE, UMAP, codificatori automatici |
| **Regolamento associativo** | Apriori, FP-Crescita |
### Valutazione del modello
| Tipo metrico | Metriche chiave |
|-------------|-------------|
| **Classificazione** | Accuratezza, precisione, richiamo, punteggio F1, ROC-AUC, matrice di confusione |
| **Regressione** | MAE, MSE, RMSE, R², R² rettificato |
| **Convalida** | Convalida incrociata k-fold, stratificata, serie temporale suddivisa |
| **Sintonizzazione** | Ricerca su griglia, ricerca casuale, ottimizzazione bayesiana |
---

## Tecnologie per i Big Data
Quando i set di dati superano ciò che una singola macchina può gestire, entra in gioco il calcolo distribuito.
| Quadro | Forza |
|-----------|----------|
| **Apache Spark** | Elaborazione in memoria; Spark SQL, streaming, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS: lo stack big data originale |
| **Apache Flink** | Elaborazione del flusso a bassa latenza |
| **Apache Beam** | Modello batch e streaming unificato |
### Piattaforme dati cloud
| Fornitore | Servizi chiave |
|----------|-------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Colla |
| **Google Cloud** | BigQuery, Dataproc, piattaforma AI, archiviazione cloud |
| **Azzurro** | Analisi sinapsi, databricks, machine learning, data Lake |
| **Fiocco di neve** | Data warehouse nativo del cloud (indipendente dal provider) |
### Orchestrazione della pipeline
| Strumento | Note |
|------|-------|
| **Flusso d'aria di Apache** | Standard del settore; DAG basati su Python |
| **Prefetto** | Alternativa moderna con API più pulite |
| **Dagster** | Orchestrazione incentrata sulle risorse |
| **dbt** | Prima trasformazione dei dati SQL in magazzino |
---

## Business intelligence e analisi
### Strumenti BI a confronto
| Strumento | Digitare | Forza |
|------|------|----------|
| **Tabella** | Commerciale | Analisi visiva ricca, trascina e rilascia |
| **Power BI** | Commerciale (Microsoft) | Integrazione profonda di Office/Azure |
| **Guardatore** | Commerciale (Google) | Esplorazione dei dati, modellazione LookML |
| **Metabase** | Open source | Configurazione semplice, SQL nativo |
| **Superinsieme** | Open source (Apache) | Scalabile, SQL-first |
### Principi di progettazione del dashboard
Dashboard efficaci seguono principi consolidati: identificare il pubblico, scegliere la visualizzazione appropriata per ciascuna metrica, utilizzare il colore in modo strategico (non decorativo), mantenere scale coerenti e consentire l'interattività (filtri, approfondimenti). Anche le prestazioni sono importanti: i dashboard con tempi di caricamento lenti riducono l'adozione da parte degli utenti.
### Categorie KPI comuni
| Categoria | Esempi |
|----------|---------|
| **Finanziario** | Entrate, margine di profitto, ROI, valore della vita del cliente |
| **Cliente** | Costo di acquisizione (CAC), tasso di abbandono, NPS, punteggio di soddisfazione |
| **Operativo** | Tassi di efficienza, tempo di ciclo, tassi di difetto |
| **Marketing** | Tasso di conversione, percentuale di clic, ROAS, attribuzione |
| **Prodotto** | Utenti attivi giornalieri, coinvolgimento, fidelizzazione, adozione di funzionalità |
---

## Analisi avanzate
| Avvicinamento | Tecniche | Quando usarlo |
|----------|-----------|-------------|
| **Predittivo** | Serie temporali (ARIMA, Prophet, LSTM), modellizzazione del rischio, previsione dell'abbandono | Previsione dei valori futuri |
| **Prescrittiva** | Programmazione lineare, simulazione Monte Carlo, test A/B, banditi multi-armati | Ottimizzare le decisioni |
| **Analisi del testo** | Tokenizzazione, analisi del sentiment, modellazione degli argomenti (LDA), NER, incorporamenti di parole (Word2Vec, BERT) | Estrarre informazioni dal testo |
---

## Etica e governance dei dati
### Normativa sulla privacy
| Regolamento | Ambito |
|-----------|-------|
| **GDPR** | Interessati UE; diritto alla cancellazione, consenso, portabilità dei dati |
| **CCPA** | Consumatori della California; rinuncia alla vendita dei dati |
| **HIPAAA** | Dati sanitari statunitensi; rigide regole di riservatezza |
### Dimensioni della qualità dei dati
| Dimensione | Domanda |
|-----------|----------|
| **Precisione** | I dati sono corretti? |
| **Completezza** | Manca qualcosa? |
| **Coerenza** | Le fonti sono d'accordo? |
| **Tempestività** | È attuale? |
| **Validità** | È conforme ai formati previsti? |
| **Unicità** | Ci sono duplicati? |
### Pregiudizi ed equità
I bias possono verificarsi in qualsiasi fase: bias di campionamento (dati non rappresentativi), bias di misurazione (strumenti difettosi) o bias algoritmici (previsioni discriminatorie). Le strategie di mitigazione includono la pre-elaborazione (correzione dei dati), l'elaborazione in corso (vincolando il modello) e la post-elaborazione (aggiustando gli output). Parametri di equità come la parità demografica e le pari opportunità aiutano a quantificare il problema.
---

##Percorsi di carriera
| Ruolo | Messa a fuoco |
|------|-------|
| **Analista dati** | Analisi descrittiva, dashboard, reporting |
| **Scienziato dei dati** | Modellazione statistica, ML, analisi avanzate |
| **Ingegnere ML** | Sistemi ML di produzione, distribuzione del modello, MLOps |
| **Ingegnere dei dati** | Condutture di dati, infrastrutture, ETL |
| **Responsabile analisi** | Leadership del team, strategia, gestione degli stakeholder |
| **Ricercatore** | Nuovi algoritmi, pubblicazioni |
---

## Tendenze emergenti
- **AutoML**: creazione automatizzata di pipeline e selezione del modello.
- **MLOps**: pratiche DevOps applicate alla gestione del ciclo di vita del machine learning.
- **Archivi di funzionalità**: gestione centralizzata delle funzionalità per il riutilizzo tra i team.
- **Data Mesh**: architettura dei dati decentralizzata e di proprietà del dominio.
- **LLM e intelligenza artificiale generativa**: modelli linguistici di grandi dimensioni che trasformano flussi di lavoro di testo, codice e immagini.
- **Edge Analytics**: elaborazione dei dati sul dispositivo anziché nel cloud.
- **Inferenza causale**: andare oltre la correlazione per comprendere la causa e l'effetto reali.
- **Apprendimento federato**: formazione di modelli su dati decentralizzati senza spostarli.
- **AI responsabile**: etica, spiegabilità e trasparenza diventano requisiti standard.