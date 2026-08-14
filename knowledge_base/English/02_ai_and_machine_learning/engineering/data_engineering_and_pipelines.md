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

# Data Engineering and Pipelines

Data engineering is the discipline of building the systems that move, transform, and store data at scale. Without reliable data pipelines, machine learning models can't be trained, dashboards show stale numbers, and business decisions are based on guesswork. This file covers the architecture, tools, and practices for building data infrastructure that works.

---

## ETL vs ELT

| Approach | How It Works | Best For | Tools |
|----------|-------------|----------|-------|
| **ETL** (Extract → Transform → Load) | Transform data *before* loading into the warehouse | Traditional warehouses with limited compute | Informatica, Talend, Apache NiFi |
| **ELT** (Extract → Load → Transform) | Load raw data first; transform *inside* the warehouse | Modern cloud warehouses with elastic compute | dbt, Fivetran, Airbyte + BigQuery/Snowflake |

The shift from ETL to ELT has been driven by cloud data warehouses (BigQuery, Snowflake, Redshift) that can scale compute independently from storage. There's no longer a need to pre-process everything before loading.

---

## Data Lakes vs Data Warehouses

| Feature | Data Lake | Data Warehouse |
|---------|-----------|---------------|
| **Data Format** | Raw, native format (schema-on-read) | Structured, processed (schema-on-write) |
| **Schema** | Defined at query time | Defined before loading |
| **Data Types** | Structured, semi-structured, unstructured | Primarily structured |
| **Users** | Data scientists, engineers | Business analysts, BI tools |
| **Cost** | Cheaper storage (object storage) | More expensive (optimised for queries) |
| **Examples** | AWS S3, Azure Data Lake, GCS | Snowflake, BigQuery, Redshift |

The modern approach is the **lakehouse**: combine the cheap, flexible storage of a lake with the management and performance features of a warehouse. Delta Lake, Apache Iceberg, and Apache Hudi are the key technologies here.

---

## Pipeline Architecture

### Batch vs Streaming

| Mode | Description | Latency | Use Case |
|------|-------------|---------|----------|
| **Batch** | Process data in large chunks at scheduled intervals | Minutes to hours | Daily reports, ETL jobs, data enrichment |
| **Streaming** | Process data continuously as it arrives | Milliseconds to seconds | Real-time dashboards, fraud detection, alerts |
| **Micro-batch** | Small batches at very short intervals | Seconds | Near-real-time with batch simplicity |

### Pipeline Components

A typical data pipeline has these stages:

| Stage | Description | Tools |
|-------|-------------|-------|
| **Ingestion** | Collect data from sources | Kafka, Airbyte, Fivetran, Debezium |
| **Transformation** | Clean, enrich, aggregate | dbt, Spark, Pandas |
| **Storage** | Persist processed data | BigQuery, Snowflake, S3, Delta Lake |
| **Serving** | Make data available to consumers | APIs, dashboards, ML feature stores |
| **Orchestration** | Schedule and manage dependencies | Airflow, Prefect, Dagster |
| **Monitoring** | Track pipeline health and data quality | Great Expectations, Monte Carlo, custom alerts |

---

## Orchestration Tools

| Tool | Approach | Strength |
|------|----------|----------|
| **Apache Airflow** | Python-based DAGs; industry standard | Huge ecosystem, mature, flexible |
| **Prefect** | Python-native; cleaner API than Airflow | Modern design, great error handling |
| **Dagster** | Asset-centric; software engineering approach | Type system, testing, observability |
| **Luigi** | Spotify's original pipeline tool | Simple, but less actively developed |

### Airflow Example

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

Kafka is the backbone of many real-time data systems. It's a distributed event log that provides high-throughput, fault-tolerant messaging.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Topic** | A category of messages (e.g., `orders`, `user-events`) |
| **Partition** | Topics are split into partitions for parallelism |
| **Producer** | Application that writes messages to topics |
| **Consumer** | Application that reads messages from topics |
| **Consumer Group** | Group of consumers that share the load of reading a topic |
| **Offset** | Position of a consumer within a partition |
| **Broker** | A Kafka server node |

### When to Use Kafka

- **Event streaming**: Real-time event processing at scale.
- **Decoupling services**: Producers and consumers don't need to know about each other.
- **Replay**: Messages are retained; consumers can re-read from any offset.
- **Backpressure**: Kafka naturally handles speed differences between producers and consumers.

---

## Data Modelling

### Star Schema vs Snowflake Schema

| Schema | Structure | Pros | Cons |
|--------|-----------|------|------|
| **Star** | Central fact table surrounded by denormalised dimension tables | Simple queries, fast reads | Data redundancy |
| **Snowflake** | Dimension tables are normalised (split into sub-tables) | Less redundancy | More joins, slower queries |

### Fact and Dimension Tables

| Table Type | Contains | Example |
|-----------|----------|---------|
| **Fact** | Measurable events (metrics) | `orders` (order_id, product_id, customer_id, amount, date) |
| **Dimension** | Descriptive attributes | `products` (product_id, name, category, price), `customers` (customer_id, name, city) |

---

## Feature Stores

A feature store is a centralised repository of ML features — the derived values used as input to models (e.g., "user's average order value in last 30 days").

| Capability | Description |
|-----------|-------------|
| **Feature Registry** | Catalogue of available features with metadata |
| **Offline Store** | Historical features for model training (batch) |
| **Online Store** | Low-latency feature serving for real-time inference |
| **Feature Monitoring** | Detect drift, missing values, distribution changes |

| Tool | Description |
|------|-------------|
| **Feast** | Open-source; works with any ML framework |
| **Tecton** | Commercial; real-time feature platform |
| **Hopsworks** | Open-source; full ML platform with feature store |
| **Databricks Feature Store** | Integrated with Databricks/Spark |

---

## Data Quality

Data quality is the silent killer of ML projects. Garbage in, garbage out.

### Quality Dimensions

| Dimension | Question |
|-----------|----------|
| **Accuracy** | Does the data reflect reality? |
| **Completeness** | Are required fields populated? |
| **Consistency** | Do values agree across sources? |
| **Timeliness** | Is the data current? |
| **Validity** | Do values conform to defined rules? |
| **Uniqueness** | Are there duplicate records? |

### Data Quality Tools

| Tool | Approach |
|------|----------|
| **Great Expectations** | Python-based; define "expectations" about data |
| **Monte Carlo** | ML-powered data observability platform |
| **dbt tests** | Built-in tests for warehouse data (unique, not_null, relationships) |
| **Soda** | Open-source data quality scanning |

---

## Data Governance

Data governance ensures that data is managed responsibly across the organisation.

| Area | Description |
|------|-------------|
| **Data Catalogue** | Searchable inventory of datasets with metadata (Amundsen, DataHub, Atlan) |
| **Data Lineage** | Track where data comes from and how it transforms |
| **Access Control** | Role-based permissions; who can read/write what |
| **Compliance** | GDPR, CCPA, HIPAA adherence |
| **Data Ownership** | Clear ownership for each dataset (stewardship) |
| **Retention Policies** | Define how long data is kept and when it's deleted |

---

## The Modern Data Stack

The "modern data stack" refers to the typical combination of tools used by data teams today:

| Layer | Typical Tools |
|-------|--------------|
| **Ingestion** | Fivetran, Airbyte |
| **Warehouse** | Snowflake, BigQuery, Redshift |
| **Transformation** | dbt |
| **Orchestration** | Airflow, Prefect, Dagster |
| **BI / Visualisation** | Looker, Metabase, Tableau |
| **Reverse ETL** | Census, Hightouch (sync warehouse data back to tools) |
| **Data Quality** | Great Expectations, Monte Carlo |

The trend is toward modular, best-of-breed tools connected by open standards (SQL, dbt models, Airflow DAGs) rather than monolithic platforms.
