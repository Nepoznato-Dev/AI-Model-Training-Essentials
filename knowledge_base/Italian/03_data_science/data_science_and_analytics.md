# Scienza dei Dati e Analitica

## Concetti Fondamentali

### Cos'è la Data Science?
La data science è un campo interdisciplinare che utilizza metodi scientifici, processi, algoritmi e sistemi per estrarre conoscenza e approfondimenti da dati strutturati e non strutturati. Combina:
- **Statistica**: Fondamento matematico per l'analisi
- **Informatica**: Programmazione, algoritmi, strutture dati
- **Competenza di Dominio**: Conoscenza della materia
- **Visualizzazione dei Dati**: Comunicare efficacemente i risultati

### Tipi di Dati
- **Dati Strutturati**: Organizzati in righe/colonne (database, fogli di calcolo)
- **Dati Non Strutturati**: Nessun formato predefinito (testo, immagini, audio, video)
- **Dati Semi-strutturati**: Qualche organizzazione ma non rigida (JSON, XML, HTML)
- **Dati di Serie Temporali**: Punti dati sequenziali indicizzati in ordine temporale
- **Dati Spaziali**: Informazioni geografiche/basate sulla posizione
- **Dati a Grafo**: Nodi e archi che rappresentano relazioni

### Il Processo di Data Science (CRISP-DM)
1. **Comprensione del Business**: Definire obiettivi e requisiti
2. **Comprensione dei Dati**: Raccogliere ed esplorare i dati iniziali
3. **Preparazione dei Dati**: Pulire, trasformare e formattare i dati (80% del lavoro)
4. **Modellazione**: Selezionare e applicare tecniche di modellazione
5. **Valutazione**: Valutare le prestazioni del modello rispetto agli obiettivi
6. **Distribuzione**: Implementare il modello in ambiente di produzione

## Fondamenti di Statistica

### Statistica Descrittiva
- **Misure di Tendenza Centrale**: Media, mediana, moda
- **Misure di Dispersione**: Intervallo, varianza, deviazione standard, intervallo interquartile
- **Forma della Distribuzione**: Asimmetria, curtosi (code)
- **Percentili e Quartili**: Posizione all'interno della distribuzione

### Statistica Inferenziale
- **Test di Ipotesi**: Ipotesi nulla, ipotesi alternativa, valori p
- **Intervalli di Confidenza**: Intervallo di valori che probabilmente contiene il parametro della popolazione
- **Significatività Statistica**: Probabilità che i risultati si siano verificati per caso
- **Errore di Tipo I**: Falso positivo (rifiutare un'ipotesi nulla vera)
- **Errore di Tipo II**: Falso negativo (non rifiutare un'ipotesi nulla falsa)
- **Potenza**: Probabilità di rifiutare correttamente un'ipotesi nulla falsa

### Distribuzioni di Probabilità
- **Distribuzione Normale**: Curva a campana, media = mediana = moda
- **Distribuzione Binomiale**: Esiti successo/insuccesso
- **Distribuzione di Poisson**: Conteggio di eventi in intervallo fisso
- **Distribuzione Uniforme**: Tutti gli esiti ugualmente probabili
- **Distribuzione Esponenziale**: Tempo tra eventi
- **Distribuzione t**: Campioni piccoli, varianza della popolazione sconosciuta
- **Distribuzione Chi-Quadrato**: Analisi di dati categorici

### Test Statistici
- **Test t**: Confrontare le medie tra due gruppi
- **ANOVA**: Confrontare le medie tra più gruppi
- **Test Chi-Quadrato**: Testare l'indipendenza di variabili categoriche
- **Mann-Whitney U**: Alternativa non parametrica al test t
- **Correlazione di Pearson**: Relazione lineare tra variabili continue
- **Correlazione di Spearman**: Relazione monotona (basata sui ranghi)
- **Kolmogorov-Smirnov**: Confrontare distribuzioni

## Raccolta e Archiviazione dei Dati

### Fonti di Dati
- **Database**: SQL, NoSQL, relazionali, archivi documentali
- **API**: REST, GraphQL, web scraping
- **File**: CSV, JSON, XML, Parquet, Avro
- **Dati in Streaming**: Kafka, Kinesis, feed in tempo reale
- **Sondaggi ed Esperimenti**: Raccolta di dati primari
- **Dataset Pubblici**: Dati governativi, Kaggle, repository accademici

### Data Warehousing
- **ETL**: Processo Extract, Transform, Load
- **Data Lake**: Archiviazione di dati grezzi in formato nativo
- **Data Warehouse**: Dati strutturati e elaborati per l'analisi
- **Data Mart**: Sottoinsieme del warehouse per dipartimento specifico
- **OLAP**: Online Analytical Processing, query multidimensionali
- **Schema a Stella**: Tabelle fatti circondate da tabelle dimensioni
- **Schema a Fiocco di Neve**: Tabelle dimensioni normalizzate

### Tipi di Database
- **Relazionali (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Documentali**: MongoDB, CouchDB (documenti simili a JSON)
- **Chiave-Valore**: Redis, DynamoDB (coppie chiave-valore semplici)
- **Colonnari**: Cassandra, HBase (ottimizzati per colonne)
- **Grafo**: Neo4j, Amazon Neptune (nodi e relazioni)
- **Serie Temporali**: InfluxDB, TimescaleDB (dati con timestamp)
- **Vettoriali**: Pinecone, Milvus (archiviazione embedding per ML)

## Pre-elaborazione dei Dati

### Pulizia dei Dati
- **Valori Mancanti**: Imputazione (media, mediana, moda, previsione), eliminazione
- **Outlier**: Rilevamento (IQR, Z-score), trattamento (limitazione, trasformazione)
- **Duplicati**: Identificazione e rimozione
- **Incoerenze**: Standardizzazione dei formati, correzione errori di battitura
- **Validazione dei Dati**: Verifica di vincoli, intervalli, tipi

### Trasformazione dei Dati
- **Normalizzazione**: Scalatura a intervallo 0-1
- **Standardizzazione**: Normalizzazione Z-score (media=0, dev.std=1)
- **Codifica**: One-hot, label, ordinale, target encoding
- **Binning**: Raggruppamento di valori continui in categorie
- **Trasformazione Logaritmica**: Riduzione dell'asimmetria
- **Scalatura delle Feature**: Rendere le feature confrontabili

### Feature Engineering
- **Creazione di Feature**: Derivare nuove feature da quelle esistenti
- **Selezione delle Feature**: Scegliere le feature più rilevanti
  - Metodi filter (correlazione, chi-quadro)
  - Metodi wrapper (eliminazione ricorsiva delle feature)
  - Metodi embedded (LASSO, importanza basata su alberi)
- **Riduzione della Dimensionalità**: PCA, t-SNE, UMAP
- **Termini di Interazione**: Combinare feature moltiplicativamente
- **Feature Polinomiali**: Creare termini di ordine superiore

## Exploratory Data Analysis (EDA)

### Tecniche EDA
- **Statistiche Riassuntive**: Descrivere tendenza centrale, dispersione, forma
- **Analisi Univariata**: Distribuzioni di singola variabile
- **Analisi Bivariata**: Relazioni tra due variabili
- **Analisi Multivariata**: Interazioni tra più variabili
- **Analisi di Correlazione**: Identificare relazioni e multicollinearità
- **Segmentazione**: Raggruppare osservazioni simili

### Strumenti di Visualizzazione
- **Istogrammi**: Distribuzione di singola variabile
- **Box Plot**: Riepilogo a cinque numeri, rilevamento outlier
- **Scatter Plot**: Relazione tra due variabili continue
- **Heatmap**: Matrici di correlazione, densità
- **Grafici a Barre**: Confronti categorici
- **Grafici a Linee**: Trend nel tempo
- **Violin Plot**: Densità di distribuzione con elementi box plot
- **Pair Plot**: Multipli scatter plot per coppie di variabili

### Librerie Python per EDA
- **pandas**: Manipolazione e analisi dei dati
- **numpy**: Calcolo numerico
- **matplotlib**: Grafica di base
- **seaborn**: Visualizzazione statistica
- **plotly**: Visualizzazioni interattive
- **scipy**: Calcolo scientifico e statistica

## Machine Learning nella Data Science

### Apprendimento Supervisionato
- **Regressione**: Prevedere valori continui
  - Regressione Lineare
  - Regressione Polinomiale
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)

- **Classificazione**: Prevedere etichette categoriche
  - Regressione Logistica
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Apprendimento Non Supervisionato
- **Clustering**: Raggruppare osservazioni simili
  - k-Means
  - Clustering Gerarchico
  - DBSCAN (basato sulla densità)
  - Gaussian Mixture Models
  - Spectral Clustering

- **Riduzione della Dimensionalità**: Ridurre il numero di feature
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoder

- **Regole di Associazione**: Trovare elementi co-occorrenti
  - Algoritmo Apriori
  - FP-Growth

### Valutazione del Modello
- **Metriche di Classificazione**: Accuratezza, precisione, recall, F1-score, ROC-AUC, matrice di confusione
- **Metriche di Regressione**: MAE, MSE, RMSE, R², R² aggiustato
- **Cross-Validation**: k-fold, stratificata, leave-one-out, time series split
- **Ottimizzazione degli Iperparametri**: Grid search, random search, ottimizzazione bayesiana
- **Curve di Apprendimento**: Diagnosticare il tradeoff bias-varianza

## Tecnologie Big Data

### Framework di Calcolo Distribuito
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: Elaborazione in-memory, più veloce di Hadoop
  - Spark SQL: Elaborazione dati strutturati
  - Spark Streaming: Dati in tempo reale
  - MLlib: Libreria di machine learning
  - GraphX: Elaborazione di grafi
- **Apache Flink**: Elaborazione di stream con bassa latenza
- **Apache Beam**: Batch e streaming unificati

### Piattaforme Cloud
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Data warehouse cloud

### Strumenti per Pipeline Dati
- **Apache Airflow**: Orchestrazione del workflow
- **Luigi**: Gestione pipeline (Spotify)
- **Prefect**: Orchestrazione moderna del workflow
- **Dagster**: Orchestratore dati con focus sugli asset
- **dbt**: Trasformazione dati nel warehouse

## Business Intelligence e Analytics

### Strumenti BI
- **Tableau**: Piattaforma di analisi visiva
- **Power BI**: Business analytics Microsoft
- **Looker**: Esplorazione dati e approfondimenti (Google)
- **Qlik Sense**: Analytics associativo
- **Metabase**: BI open-source
- **Superset**: Apache BI open-source

### Principi di Progettazione Dashboard
- **Conosci il Tuo Pubblico**: Adattare alle esigenze dell'utente
- **Scegli le Visualizzazioni Giuste**: Abbinare il grafico al tipo di dato
- **Usa il Colore Strategicamente**: Evidenziare informazioni importanti
- **Mantieni la Coerenza**: Standardizzare formati e scale
- **Abilita l'Interattività**: Filtri, drill-down, tooltip
- **Ottimizza le Prestazioni**: Caricamento veloce, query efficienti
- **Considerazioni Mobile**: Design responsivo

### Key Performance Indicators (KPI)
- **Finanziari**: Ricavi, margine di profitto, ROI, customer lifetime value
- **Clienti**: Costo di acquisizione, tasso di churn, punteggio di soddisfazione, NPS
- **Operativi**: Tassi di efficienza, tempo di ciclo, tassi di difetto
- **Marketing**: Tassi di conversione, click-through rates, attribuzione
- **Prodotto**: Utenti attivi, engagement, retention, adozione funzionalità

## Analytics Avanzata

### Analytics Predittiva
- **Previsione**: Predizione di serie temporali (ARIMA, Prophet, LSTM)
- **Modellazione del Rischio**: Credit scoring, rilevamento frodi, assicurazioni
- **Analytics Clienti**: Previsione churn, modelli di propensione
- **Previsione della Domanda**: Ottimizzazione inventario, supply chain
- **Manutenzione Predittiva**: Anticipazione guasti attrezzature

### Analytics Prescrittiva
- **Ottimizzazione**: Programmazione lineare, programmazione intera
- **Simulazione**: Metodi Monte Carlo, simulazione a eventi discreti
- **Analisi Decisionale**: Alberi decisionali, diagrammi di influenza
- **Test A/B**: Progettazione sperimentale, significatività statistica
- **Multi-Armed Bandits**: Sperimentazione adattiva

### Text Analytics (NLP)
- **Pre-elaborazione del Testo**: Tokenizzazione, stemming, lemmatizzazione
- **Analisi del Sentimento**: Classificazione positivo/negativo/neutro
- **Topic Modeling**: LDA, NMF per scoperta di temi
- **Named Entity Recognition**: Identificare persone, luoghi, organizzazioni
- **Classificazione del Testo**: Rilevamento spam, categorizzazione
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Etica e Governance dei Dati

### Privacy dei Dati
- **GDPR**: Regolamento Generale sulla Protezione dei Dati UE
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (sanità USA)
- **Anonimizzazione**: Rimozione delle informazioni identificative personali
- **Privacy Differenziale**: Aggiunta di rumore per proteggere gli individui
- **Gestione del Consenso**: Meccanismi opt-in/opt-out

### Qualità dei Dati
- **Accuratezza**: Correttezza dei dati
- **Completezza**: Tutti i dati richiesti presenti
- **Consistenza**: Nessuna contraddizione tra fonti
- **Tempestività**: Dati disponibili quando necessario
- **Validità**: Conforme alle regole definite
- **Unicità**: Nessun duplicato

### Bias ed Equità
- **Bias di Campionamento**: Raccolta dati non rappresentativa
- **Bias di Misurazione**: Strumenti di raccolta dati difettosi
- **Bias Algoritmico**: Predizioni discriminatorie del modello
- **Metriche di Equità**: Parità demografica, pari opportunità
- **Mitigazione del Bias**: Pre-elaborazione, in-processing, post-processing

### Framework di Governance dei Dati
- **Data Stewardship**: Responsabilità per gli asset dati
- **Gestione dei Metadati**: Documentazione dei dati sui dati
- **Data Lineage**: Tracciamento del flusso e delle trasformazioni dei dati
- **Controllo degli Accessi**: Permessi basati sui ruoli
- **Audit Trail**: Registrazione accessi e modifiche ai dati
- **Conformità**: Adempimento normativo

## Percorsi di Carriera nella Data Science

### Ruoli
- **Data Analyst**: Focus su analytics descrittiva, dashboard, reporting
- **Data Scientist**: Modellazione statistica, machine learning, analytics avanzata
- **ML Engineer**: Sistemi ML di produzione, deployment modelli, MLOps
- **Data Engineer**: Pipeline dati, infrastruttura, processi ETL
- **Analytics Manager**: Leadership del team, strategia, gestione stakeholder
- **BI Developer**: Creazione dashboard, sviluppo report
- **Research Scientist**: Nuovi algoritmi, pubblicazioni, ricerca avanzata

### Matrice delle Competenze
- **Tecniche**: Python/R, SQL, statistica, framework ML, piattaforme cloud
- **Analitiche**: Risoluzione problemi, pensiero critico, progettazione sperimentale
- **Comunicazione**: Storytelling, visualizzazione, capacità di presentazione
- **Business**: Conoscenza del dominio, gestione stakeholder, analisi ROI
- **Strumenti**: Git, Jupyter, Docker, CI/CD, version control per modelli

## Trend Emergenti

### Sviluppi Attuali
- **AutoML**: Creazione automatica di pipeline di machine learning
- **MLOps**: Pratiche DevOps per il machine learning
- **Feature Store**: Gestione centralizzata delle feature
- **Data Mesh**: Architettura dati decentralizzata
- **LLM e AI Generativa**: Large language models, generazione di contenuti
- **Edge Analytics**: Elaborazione dati sui dispositivi sorgente
- **Analytics in Tempo Reale**: Analisi di dati in streaming
- **Augmented Analytics**: Preparazione dati e approfondimenti assistiti da AI

### Direzioni Future
- **Quantum Machine Learning**: Calcolo quantistico per ML
- **Federated Learning**: Addestramento modelli su dati decentralizzati
- **Inferenza Causale**: Andare oltre la correlazione alla causalità
- **AI Responsabile**: Etica, spiegabilità, trasparenza
- **Data Fabric**: Gestione dati integrata tra ambienti
