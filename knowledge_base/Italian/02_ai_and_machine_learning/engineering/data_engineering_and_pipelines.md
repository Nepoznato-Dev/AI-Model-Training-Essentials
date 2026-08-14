<!--
---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
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
tags: [data, engineering, pipelines, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Ingegneria dei dati e pipeline
L'ingegneria dei dati è la disciplina che mira a costruire sistemi che spostano, trasformano e archiviano dati su larga scala. Senza pipeline di dati affidabili, i modelli di machine learning non possono essere addestrati, i dashboard mostrano numeri obsoleti e le decisioni aziendali si basano su congetture. Questo file copre l'architettura, gli strumenti e le pratiche per creare un'infrastruttura dati che funzioni.
---

## ETL contro ELT
| Avvicinamento | Come funziona | Ideale per | Strumenti |
|----------|-------------|----------|-------|
| **ETL** (Estrai → Trasforma → Carica) | Trasformare i dati *prima* del caricamento nel magazzino | Magazzini tradizionali con calcolo limitato | Informatica, Talend, Apache NiFi |
| **ELT** (Estrai → Carica → Trasforma) | Caricare prima i dati grezzi; trasformare *dentro* il magazzino | Moderni magazzini cloud con calcolo elastico | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
Il passaggio da ETL a ELT è stato guidato da data warehouse su cloud (BigQuery, Snowflake, Redshift) in grado di scalare l'elaborazione indipendentemente dallo storage. Non è più necessario preelaborare tutto prima del caricamento.
---

## Data Lake e data warehouse
| Caratteristica | Lago dati | Magazzino dati |
|---------|-----------|-------|
| **Formato dati** | Formato nativo non elaborato (schema in lettura) | Strutturato, elaborato (schema-on-write) |
| **Schema** | Definito al momento della query | Definito prima del caricamento |
| **Tipi di dati** | Strutturato, semistrutturato, non strutturato | Strutturato principalmente |
| **Utenti** | Data scientist, ingegneri | Analisti aziendali, strumenti BI |
| **Costo** | Archiviazione più economica (archiviazione di oggetti) | Più costoso (ottimizzato per le query) |
| **Esempi** | AWS S3, Azure Data Lake, GCS | Fiocco di neve, BigQuery, Redshift |
L'approccio moderno è il **lakehouse**: combinare lo stoccaggio economico e flessibile di un lago con le caratteristiche gestionali e prestazionali di un magazzino. Delta Lake, Apache Iceberg e Apache Hudi sono le tecnologie chiave qui.
---

## Architettura della pipeline
### Batch o streaming
| Modalità | Descrizione | Latenza | Caso d'uso |
|------|-------------|---------|----------|
| **Lotto** | Elaborare i dati in blocchi di grandi dimensioni a intervalli pianificati | Da minuti a ore | Rapporti giornalieri, lavori ETL, arricchimento dei dati |
| **Streaming** | Elaborare i dati continuamente man mano che arrivano | Millisecondi in secondi | Dashboard in tempo reale, rilevamento delle frodi, avvisi |
| **Microlotto** | Piccoli lotti a intervalli molto brevi | Secondi | Quasi in tempo reale con semplicità batch |
### Componenti della pipeline
Una tipica pipeline di dati prevede queste fasi:
| Palcoscenico | Descrizione | Strumenti |
|-------|-------------|-------|
| **Ingestione** | Raccogliere dati da fonti | Kafka, Airbyte, Fivetran, Debezium |
| **Trasformazione** | Pulisci, arricchisci, aggrega | dbt, Spark, Panda |
| **Archiviazione** | Persistenza dei dati elaborati | BigQuery, Fiocco di neve, S3, Delta Lake |
| **Servo** | Rendere i dati disponibili ai consumatori | API, dashboard, negozi di funzionalità ML |
| **Orchestrazioni** | Pianificare e gestire le dipendenze | Flusso d'aria, Prefetto, Dagster |
| **Monitoraggio** | Tieni traccia dello stato della pipeline e della qualità dei dati | Grandi aspettative, Monte Carlo, avvisi personalizzati |
---

## Strumenti di orchestrazione
| Strumento | Avvicinamento | Forza |
|------|----------|----------|
| **Flusso d'aria di Apache** | DAG basati su Python; standard industriale | Ecosistema enorme, maturo, flessibile |
| **Prefetto** | Nativo Python; API più pulita rispetto a Airflow | Design moderno, ottima gestione degli errori |
| **Dagster** | Incentrato sulle risorse; approccio di ingegneria del software | Sistema di tipi, test, osservabilità |
| **Luigi** | Lo strumento pipeline originale di Spotify | Semplice, ma sviluppato meno attivamente |
### Esempio di flusso d'aria
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

##Apache Kafka
Kafka è la spina dorsale di molti sistemi di dati in tempo reale. Si tratta di un registro eventi distribuito che fornisce messaggistica a elevata velocità effettiva e con tolleranza agli errori.
### Concetti fondamentali
| Concetto | Descrizione |
|---------|-----|
| **Argomento** | Una categoria di messaggi (ad esempio,`orders`,`user-events`) |
| **Partizione** | Gli argomenti sono suddivisi in partizioni per parallelismo |
| **Produttore** | Applicazione che scrive messaggi agli argomenti |
| **Consumatore** | Applicazione che legge i messaggi dagli argomenti |
| **Gruppo di consumatori** | Gruppo di consumatori che condividono il carico di leggere un argomento |
| **Offset** | Posizione di un consumatore all'interno di una partizione |
| **Intermediario** | Un nodo server Kafka |
### Quando utilizzare Kafka
- **Streaming di eventi**: elaborazione di eventi in tempo reale su larga scala.
- **Servizi di disaccoppiamento**: produttori e consumatori non hanno bisogno di conoscersi a vicenda.
- **Replay**: i messaggi vengono conservati; i consumatori possono rileggere da qualsiasi compensazione.
- **Contropressione**: Kafka gestisce naturalmente le differenze di velocità tra produttori e consumatori.
---

## Modellazione dei dati
### Schema a stella contro schema a fiocco di neve
| Schema | Struttura | Pro | Contro |
|--------|-----------|------|------|
| **Stella** | Tabella dei fatti centrale circondata da tabelle delle dimensioni denormalizzate | Query semplici, letture veloci | Ridondanza dei dati |
| **Fiocco di neve** | Le tabelle dimensionali sono normalizzate (divise in sottotabelle) | Meno ridondanza | Più join, query più lente |
### Tabelle di fatti e dimensioni
| Tipo di tabella | Contiene | Esempio |
|-----------|----------|---------|
| **Fatto** | Eventi misurabili (metriche) | `orders`(id_ordine, id_prodotto, id_cliente, importo, data) |
| **Dimensione** | Attributi descrittivi | `products`(id_prodotto, nome, categoria, prezzo),`customers`(id_cliente, nome, città) |
---

## Negozi di articoli particolari
Un archivio di funzionalità è un repository centralizzato di funzionalità ML: i valori derivati ​​utilizzati come input per i modelli (ad esempio, "valore medio degli ordini dell'utente negli ultimi 30 giorni").
| Capacità | Descrizione |
|-----------|-------------|
| **Registro delle funzionalità** | Catalogo delle funzionalità disponibili con metadati |
| **Negozio offline** | Caratteristiche storiche per l'addestramento del modello (batch) |
| **Negozio online** | Funzionalità a bassa latenza per l'inferenza in tempo reale |
| **Monitoraggio delle funzionalità** | Rileva deriva, valori mancanti, cambiamenti di distribuzione |
| Strumento | Descrizione |
|------|-------------|
| **Festa** | Open source; funziona con qualsiasi framework ML |
| **Tecton** | Commerciale; piattaforma di funzionalità in tempo reale |
| **Opere di luppolo** | Open source; piattaforma ML completa con negozio di funzionalità |
| **Archivio di funzionalità Databricks** | Integrato con Databricks/Spark |
---

## Qualità dei dati
La qualità dei dati è il killer silenzioso dei progetti ML. Immondizia dentro, spazzatura fuori.
### Dimensioni di qualità
| Dimensione | Domanda |
|-----------|----------|
| **Precisione** | I dati rispecchiano la realtà? |
| **Completezza** | I campi obbligatori sono compilati? |
| **Coerenza** | I valori concordano tra le fonti? |
| **Tempestività** | I dati sono aggiornati? |
| **Validità** | I valori sono conformi a regole definite? |
| **Unicità** | Sono presenti record duplicati? |
### Strumenti per la qualità dei dati
| Strumento | Avvicinamento |
|------|----------|
| **Grandi aspettative** | Basato su Python; definire le "aspettative" sui dati |
| **Montecarlo** | Piattaforma di osservabilità dei dati basata su ML |
| **test dbt** | Test integrati per i dati di warehouse (unique, not_null, relazioni) |
| **Soda** | Scansione della qualità dei dati open source |
---

##Governance dei dati
La governance dei dati garantisce che i dati siano gestiti in modo responsabile in tutta l’organizzazione.
| Zona | Descrizione |
|------|-------------|
| **Catalogo dati** | Inventario ricercabile di set di dati con metadati (Amundsen, DataHub, Atlan) |
| **Linea dati** | Tieni traccia della provenienza dei dati e di come si trasformano |
| **Controllo degli accessi** | Autorizzazioni basate sul ruolo; chi sa leggere/scrivere cosa |
| **Conformità** | Adesione a GDPR, CCPA, HIPAA |
| **Proprietà dei dati** | Proprietà chiara per ciascun set di dati (gestione) |
| **Politiche di conservazione** | Definisci per quanto tempo vengono conservati i dati e quando vengono eliminati |
---

## Lo stack di dati moderno
Il "modern data stack" si riferisce alla tipica combinazione di strumenti utilizzati oggi dai data team:
| Strato | Strumenti tipici |
|-------|--------------|
| **Ingestione** | Fivetran, Airbyte |
| **Magazzino** | Fiocco di neve, BigQuery, Redshift |
| **Trasformazione** | db |
| **Orchestrazioni** | Flusso d'aria, Prefetto, Dagster |
| **BI/Visualizzazione** | Looker, Metabase, Tableau |
| **ETL inverso** | Censimento, Hightouch (sincronizza i dati del magazzino con gli strumenti) |
| **Qualità dei dati** | Grandi aspettative, Montecarlo |
La tendenza è verso strumenti modulari e all’avanguardia collegati da standard aperti (SQL, modelli dbt, DAG Airflow) piuttosto che piattaforme monolitiche.