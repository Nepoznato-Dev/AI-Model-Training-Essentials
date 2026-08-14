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
# Data Engineering at Pipelines
Ang data engineering ay ang disiplina sa pagbuo ng mga system na gumagalaw, nagbabago, at nag-iimbak ng data sa sukat. Kung walang maaasahang pipeline ng data, hindi masasanay ang mga modelo ng machine learning, nagpapakita ang mga dashboard ng mga stale na numero, at ang mga desisyon sa negosyo ay batay sa hula. Sinasaklaw ng file na ito ang arkitektura, mga tool, at mga kasanayan para sa pagbuo ng imprastraktura ng data na gumagana.
---

## ETL vs ELT
| Diskarte | Paano Ito Gumagana | Pinakamahusay Para sa | Mga tool |
|----------|-------------|----------|-------|
| **ETL** (Extract → Transform → Load) | I-transform ang data *bago* mag-load sa warehouse | Mga tradisyunal na warehouse na may limitadong compute | Informatica, Talend, Apache NiFi |
| **ELT** (Extract → Load → Transform) | Mag-load muna ng raw data; transform *sa loob* ng bodega | Mga modernong cloud warehouse na may elastic compute | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
Ang paglipat mula sa ETL patungo sa ELT ay hinimok ng mga cloud data warehouse (BigQuery, Snowflake, Redshift) na maaaring mag-scale ng compute nang hiwalay mula sa storage. Hindi na kailangan pang iproseso ang lahat bago mag-load.
---

## Data Lakes vs Data Warehouses
| Tampok | Data Lake | Data Warehouse |
|---------|-----------|----------------|
| **Format ng Data** | Raw, katutubong format (schema-on-read) | Nakabalangkas, naproseso (schema-on-write) |
| **Skema** | Tinukoy sa oras ng query | Tinukoy bago i-load |
| **Mga Uri ng Data** | Structured, semi-structured, unstructured | Pangunahing nakabalangkas |
| **Mga Gumagamit** | Data scientist, mga inhinyero | Mga analyst ng negosyo, mga tool sa BI |
| **Gastos** | Mas murang storage (imbakan ng bagay) | Mas mahal (na-optimize para sa mga query) |
| **Mga Halimbawa** | AWS S3, Azure Data Lake, GCS | Snowflake, BigQuery, Redshift |
Ang modernong diskarte ay ang **lakehouse**: pagsamahin ang mura, nababaluktot na imbakan ng isang lawa kasama ang mga feature ng pamamahala at pagganap ng isang bodega. Ang Delta Lake, Apache Iceberg, at Apache Hudi ay ang mga pangunahing teknolohiya dito.
---

## Arkitektura ng Pipeline
### Batch vs Streaming
| Mode | Paglalarawan | Latency | Use Case |
|------|-------------|---------|----------|
| **Batch** | Iproseso ang data sa malalaking tipak sa mga naka-iskedyul na pagitan | Minuto hanggang oras | Mga pang-araw-araw na ulat, mga trabaho sa ETL, pagpapayaman ng data |
| **Pag-stream** | Patuloy na iproseso ang data pagdating nito | Milliseconds hanggang segundo | Mga real-time na dashboard, pagtuklas ng pandaraya, mga alerto |
| **Micro-batch** | Maliit na batch sa napakaikling pagitan | Segundo | Near-real-time na may batch na pagiging simple |
### Mga Bahagi ng Pipeline
Ang isang tipikal na pipeline ng data ay may mga yugtong ito:
| Yugto | Paglalarawan | Mga tool |
|-------|-------------|-------|
| **Paglunok** | Mangolekta ng data mula sa mga mapagkukunan | Kafka, Airbyte, Fivetran, Debezium |
| **Pagbabago** | Linisin, pagyamanin, pinagsama-sama | dbt, Spark, Panda |
| **Imbakan** | Ipagpatuloy ang naprosesong data | BigQuery, Snowflake, S3, Delta Lake |
| **Serving** | Gawing available ang data sa mga consumer | Mga API, dashboard, ML feature store |
| **Orkestrasyon** | Mag-iskedyul at pamahalaan ang mga dependency | Daloy ng hangin, Prefect, Dagster |
| **Pagsubaybay** | Subaybayan ang kalusugan ng pipeline at kalidad ng data | Mahusay na Inaasahan, Monte Carlo, mga pasadyang alerto |
---

## Mga Tool sa Orkestrasyon
| Tool | Diskarte | Lakas |
|------|----------|----------|
| **Apache Airflow** | Mga DAG na nakabatay sa Python; pamantayan ng industriya | Malaking ecosystem, mature, flexible |
| **Prefect** | Katutubong sawa; mas malinis na API kaysa sa Airflow | Modernong disenyo, mahusay na paghawak ng error |
| **Dagster** | Asset-centric; diskarte sa software engineering | Uri ng system, pagsubok, observability |
| **Luigi** | Orihinal na pipeline tool ng Spotify | Simple, ngunit hindi gaanong aktibong binuo |
### Halimbawa ng Airflow
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

## Apache Kafka
Ang Kafka ay ang backbone ng maraming real-time na data system. Isa itong distributed event log na nagbibigay ng high-throughput, fault-tolerant na pagmemensahe.
### Mga Pangunahing Konsepto
| Konsepto | Paglalarawan |
|---------|-------------|
| **Paksa** | Isang kategorya ng mga mensahe (hal.,`orders`,`user-events`) |
| **Paghati** | Ang mga paksa ay nahahati sa mga partisyon para sa paralelismo |
| **Producer** | Application na nagsusulat ng mga mensahe sa mga paksa |
| **Consumer** | Application na nagbabasa ng mga mensahe mula sa mga paksa |
| **Pangkat ng Consumer** | Grupo ng mga mamimili na nagbabahagi ng pag-load ng pagbabasa ng isang paksa |
| **Offset** | Posisyon ng isang mamimili sa loob ng isang partisyon |
| **Broker** | Isang Kafka server node |
### Kailan Gamitin ang Kafka
- **Pag-stream ng kaganapan**: Real-time na pagpoproseso ng kaganapan sa sukat.
- **Decoupling services**: Hindi kailangang malaman ng mga producer at consumer ang tungkol sa isa't isa.
- **Replay**: Pinapanatili ang mga mensahe; maaaring muling basahin ng mga mamimili mula sa anumang offset.
- **Backpressure**: Natural na pinangangasiwaan ng Kafka ang mga pagkakaiba sa bilis sa pagitan ng mga producer at mga consumer.
---

## Pagmomodelo ng Data
### Star Schema vs Snowflake Schema
| Schema | Istraktura | Mga Pros | Cons |
|--------|-----------|------|------|
| **Bituin** | Central fact table na napapalibutan ng mga denormalized na talahanayan ng dimensyon | Mga simpleng query, mabilis na pagbabasa | Kalabisan ng data |
| **Snowflake** | Ang mga talahanayan ng dimensyon ay na-normalize (nahati sa mga sub-table) | Mas kaunting redundancy | Mas maraming sumali, mas mabagal na mga query |
### Talahanayan ng Katotohanan at Dimensyon
| Uri ng Talahanayan | Naglalaman ng | Halimbawa |
|-----------|----------|---------|
| **Katotohanan** | Mga nasusukat na kaganapan (sukatan) | `orders`(order_id, product_id, customer_id, halaga, petsa) |
| **Dimensyon** | Mga katangiang naglalarawan | `products`(product_id, pangalan, kategorya, presyo),`customers`(customer_id, pangalan, lungsod) |
---

## Mga Tampok na Tindahan
Ang isang feature store ay isang sentralisadong repositoryo ng mga feature ng ML — ang mga nakuhang halaga na ginamit bilang input sa mga modelo (hal., "ang average na halaga ng order ng user sa nakalipas na 30 araw").
| Kakayahan | Paglalarawan |
|-----------|-------------|
| **Registry ng Tampok** | Catalog ng mga available na feature na may metadata |
| **Offline na Tindahan** | Mga makasaysayang tampok para sa pagsasanay ng modelo (batch) |
| **Online na Tindahan** | Low-latency feature na naghahatid para sa real-time na inference |
| **Pagsubaybay sa Tampok** | I-detect ang drift, mga nawawalang value, mga pagbabago sa pamamahagi |
| Tool | Paglalarawan |
|------|-------------|
| **Pista** | Open-source; gumagana sa anumang ML framework |
| **Tecton** | Komersyal; real-time na feature platform |
| **Hopsworks** | Open-source; buong ML platform na may feature store |
| **Databricks Feature Store** | Pinagsama sa Databricks/Spark |
---

## Kalidad ng Data
Ang kalidad ng data ay ang silent killer ng mga proyekto ng ML. Basura pasok, basura palabas.
### Mga Dimensyon ng Kalidad
| Dimensyon | Tanong |
|-----------|----------|
| **Katumpakan** | Sinasalamin ba ng data ang katotohanan? |
| **Pagiging kumpleto** | Napo-populate ba ang mga kinakailangang field? |
| **Consistency** | Sumasang-ayon ba ang mga halaga sa mga mapagkukunan? |
| **Pagiging napapanahon** | Kasalukuyan ba ang data? |
| **Katotohanan** | Ang mga halaga ba ay umaayon sa tinukoy na mga panuntunan? |
| **Kakaiba** | Mayroon bang mga duplicate na tala? |
### Mga Tool sa Kalidad ng Data
| Tool | Diskarte |
|------|----------|
| **Mahusay na Inaasahan** | Batay sa Python; tukuyin ang "mga inaasahan" tungkol sa data |
| **Monte Carlo** | ML-powered data observability platform |
| **mga pagsubok sa dbt** | Mga built-in na pagsubok para sa data ng warehouse (natatangi, hindi_null, mga relasyon) |
| **Soda** | Open-source na pag-scan sa kalidad ng data |
---

## Pamamahala ng Data
Tinitiyak ng pamamahala ng data na ang data ay pinamamahalaan nang responsable sa buong organisasyon.
| Lugar | Paglalarawan |
|------|-------------|
| **Catalogue ng Data** | Mahahanap na imbentaryo ng mga dataset na may metadata (Amundsen, DataHub, Atlan) |
| **Data Lineage** | Subaybayan kung saan nagmumula ang data at kung paano ito nagbabago |
| **Kontrol sa Pag-access** | Mga pahintulot na nakabatay sa tungkulin; sino ang maaaring magbasa/magsulat ng ano |
| **Pagsunod** | GDPR, CCPA, HIPAA na pagsunod |
| **Pagmamay-ari ng Data** | I-clear ang pagmamay-ari para sa bawat dataset (stewardship) |
| **Mga Patakaran sa Pagpapanatili** | Tukuyin kung gaano katagal pinapanatili ang data at kung kailan ito tinanggal |
---

## Ang Modernong Data Stack
Ang "modernong data stack" ay tumutukoy sa karaniwang kumbinasyon ng mga tool na ginagamit ng mga data team ngayon:
| Layer | Mga Karaniwang Tool |
|-------|--------------|
| **Paglunok** | Fivetran, Airbyte |
| **Warehouse** | Snowflake, BigQuery, Redshift |
| **Pagbabago** | dbt |
| **Orkestrasyon** | Daloy ng hangin, Prefect, Dagster |
| **BI / Visualization** | Looker, Metabase, Tableau |
| **Reverse ETL** | Census, Hightouch (i-sync ang data ng warehouse pabalik sa mga tool) |
| **Kalidad ng Data** | Mahusay na Inaasahan, Monte Carlo |
Ang trend ay patungo sa modular, pinakamahusay na lahi na mga tool na konektado ng mga bukas na pamantayan (SQL, dbt models, Airflow DAGs) kaysa sa mga monolitikong platform.