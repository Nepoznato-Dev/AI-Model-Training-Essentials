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
# Data Science and Analytics

Data science is the discipline of turning raw data into actionable insight. It sits at the intersection of statistics, computer science, and domain expertise — and it has become essential in every sector from finance to healthcare. This file walks through the core concepts, tools, and workflows that every practitioner should know.

---

## The Data Science Process

Most projects follow some variation of **CRISP-DM**, the industry-standard lifecycle:

| Phase | What Happens | Typical Time |
|-------|-------------|--------------|
| **Business Understanding** | Define objectives, success metrics, and constraints | 10–15% |
| **Data Understanding** | Collect, explore, and profile the data | 10–15% |
| **Data Preparation** | Clean, transform, engineer features | ~50–60% |
| **Modeling** | Select and train models | 10–15% |
| **Evaluation** | Assess performance against business goals | 5–10% |
| **Deployment** | Ship the model to production | 5–10% |

Data preparation, particularly data cleaning, is widely estimated to consume around 80% of a data scientist's time.

---

## Data Types at a Glance

| Type | Description | Example |
|------|-------------|---------|
| **Structured** | Organised in rows and columns | SQL tables, spreadsheets |
| **Unstructured** | No predefined format | Text, images, audio, video |
| **Semi-structured** | Some organisation but flexible | JSON, XML, HTML |
| **Time series** | Sequential data indexed by time | Stock prices, sensor readings |
| **Spatial** | Geographic or location-based | GPS coordinates, map data |
| **Graph** | Nodes and edges representing relationships | Social networks, knowledge graphs |

---

## Statistics Fundamentals

### Descriptive vs Inferential Statistics

Descriptive statistics summarise what you *have*; inferential statistics let you draw conclusions about what you *don't* have (the broader population).

| Concept | Key Ideas |
|---------|-----------|
| **Central tendency** | Mean (sensitive to outliers), median (robust), mode (most frequent) |
| **Dispersion** | Range, variance, standard deviation, interquartile range |
| **Distribution shape** | Skewness (asymmetry), kurtosis (tail heaviness) |
| **Hypothesis testing** | Null vs alternative hypothesis, p-values, significance level (α) |
| **Confidence intervals** | Range likely containing the true population parameter |
| **Type I / Type II errors** | False positive (rejecting a true null) / false negative (missing a real effect) |

### Common Statistical Tests

| Test | When to Use |
|------|-------------|
| **t-test** | Compare means between two groups |
| **ANOVA** | Compare means across three or more groups |
| **Chi-square** | Test independence of categorical variables |
| **Mann-Whitney U** | Non-parametric alternative to t-test (no normality assumption) |
| **Pearson correlation** | Linear relationship between two continuous variables |
| **Spearman correlation** | Monotonic relationship (rank-based, more robust) |

### Probability Distributions Worth Knowing

| Distribution | Use Case |
|-------------|----------|
| **Normal** | Natural phenomena, measurement errors — the classic bell curve |
| **Binomial** | Success/failure counts (coin flips, conversion rates) |
| **Poisson** | Event counts in a fixed interval (calls per hour, defects per batch) |
| **Exponential** | Time between events (wait times, failure intervals) |
| **t-Distribution** | Small samples or unknown population variance |
| **Chi-square** | Categorical data analysis, goodness-of-fit tests |

---

## Data Collection and Storage

### Where Data Comes From

Real-world data arrives from many sources: relational databases, APIs (REST, GraphQL), flat files (CSV, JSON, Parquet), streaming platforms (Kafka, Kinesis), surveys, and public repositories (Kaggle, government portals). The format you receive determines much of your preprocessing strategy.

### Data Warehousing Concepts

| Concept | Description |
|---------|-------------|
| **ETL** | Extract → Transform → Load — traditional pipeline approach |
| **ELT** | Extract → Load → Transform — modern cloud approach (load raw, transform in-warehouse) |
| **Data Lake** | Raw data stored in native format (schema-on-read) |
| **Data Warehouse** | Structured, processed data optimised for analysis (schema-on-write) |
| **Data Mart** | A subset of a warehouse, scoped to one department or domain |
| **Star Schema** | Central fact table surrounded by dimension tables |
| **Snowflake Schema** | Normalised dimension tables (less redundancy, more joins) |

### Database Types

| Type | Examples | Best For |
|------|----------|----------|
| **Relational (SQL)** | PostgreSQL, MySQL, Oracle | Structured data, ACID transactions |
| **Document** | MongoDB, CouchDB | Flexible schemas, JSON-like data |
| **Key-Value** | Redis, DynamoDB | Caching, sessions, simple lookups |
| **Column-Family** | Cassandra, HBase | Write-heavy workloads, time series |
| **Graph** | Neo4j, Amazon Neptune | Relationships, social networks |
| **Time-Series** | InfluxDB, TimescaleDB | IoT metrics, monitoring |
| **Vector** | Pinecone, Milvus | Embedding storage for ML/AI search |

---

## Data Preprocessing and Feature Engineering

### Cleaning Checklist

Every real dataset has issues. Here's the standard cleanup:

| Issue | Approach |
|-------|----------|
| **Missing values** | Imputation (mean, median, prediction), or deletion if sparse |
| **Outliers** | Detect via IQR or Z-score; treat with capping or transformation |
| **Duplicates** | Identify and remove |
| **Inconsistencies** | Standardise formats, fix typos, normalise units |

### Transformation Techniques

| Technique | What It Does |
|-----------|-------------|
| **Normalization** | Scales values to 0–1 range |
| **Standardization** | Z-score: mean = 0, std = 1 |
| **One-hot encoding** | Converts categories to binary columns |
| **Label encoding** | Assigns integer labels to categories |
| **Log transformation** | Reduces right-skew in data |
| **Binning** | Groups continuous values into discrete buckets |

### Feature Engineering

Feature engineering is often the difference between a mediocre model and a great one. Key techniques include:

- **Feature creation**: Deriving new columns from existing ones (e.g., `age_group` from `age`).
- **Feature selection**: Filter methods (correlation), wrapper methods (recursive elimination), embedded methods (LASSO, tree importance).
- **Dimensionality reduction**: PCA for linear, t-SNE or UMAP for visualisation.
- **Interaction terms**: Combining features multiplicatively to capture joint effects.

---

## Exploratory Data Analysis (EDA)

EDA is where you develop intuition about your data before modelling. The goal is to spot patterns, anomalies, and relationships.

### Choosing the Right Chart

| Chart Type | Best For |
|-----------|----------|
| **Histogram** | Distribution of a single variable |
| **Box plot** | Five-number summary, outlier detection |
| **Scatter plot** | Relationship between two continuous variables |
| **Heatmap** | Correlation matrices, density visualisation |
| **Bar chart** | Comparing categories |
| **Line chart** | Trends over time |
| **Violin plot** | Distribution density + box plot summary |
| **Pair plot** | Quick overview of all variable pairs |

### The Python EDA Stack

| Library | Role |
|---------|------|
| **pandas** | Data manipulation and analysis |
| **numpy** | Numerical computing |
| **matplotlib** | Foundation plotting |
| **seaborn** | Statistical visualisation (built on matplotlib) |
| **plotly** | Interactive, web-based visualisations |
| **scipy** | Scientific computing and statistics |

---

## Machine Learning in Data Science

### Supervised Learning at a Glance

| Task | Algorithms |
|------|-----------|
| **Regression** (predict a number) | Linear, Ridge/LASSO, Decision Tree, Random Forest, Gradient Boosting (XGBoost, LightGBM) |
| **Classification** (predict a category) | Logistic Regression, k-NN, Naive Bayes, SVM, Decision Trees, Random Forest, Neural Networks |

### Unsupervised Learning at a Glance

| Task | Algorithms |
|------|-----------|
| **Clustering** | k-Means, Hierarchical, DBSCAN, Gaussian Mixture Models |
| **Dimensionality Reduction** | PCA, t-SNE, UMAP, Autoencoders |
| **Association Rules** | Apriori, FP-Growth |

### Model Evaluation

| Metric Type | Key Metrics |
|-------------|-------------|
| **Classification** | Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix |
| **Regression** | MAE, MSE, RMSE, R², Adjusted R² |
| **Validation** | k-fold cross-validation, stratified, time series split |
| **Tuning** | Grid search, random search, Bayesian optimisation |

---

## Big Data Technologies

When datasets exceed what a single machine can handle, distributed computing enters the picture.

| Framework | Strength |
|-----------|----------|
| **Apache Spark** | In-memory processing; Spark SQL, Streaming, MLlib, GraphX |
| **Apache Hadoop** | MapReduce + HDFS — the original big data stack |
| **Apache Flink** | Low-latency stream processing |
| **Apache Beam** | Unified batch and streaming model |

### Cloud Data Platforms

| Provider | Key Services |
|----------|-------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Glue |
| **Google Cloud** | BigQuery, Dataproc, AI Platform, Cloud Storage |
| **Azure** | Synapse Analytics, Databricks, Machine Learning, Data Lake |
| **Snowflake** | Cloud-native data warehouse (provider-agnostic) |

### Pipeline Orchestration

| Tool | Notes |
|------|-------|
| **Apache Airflow** | Industry standard; Python-based DAGs |
| **Prefect** | Modern alternative with cleaner API |
| **Dagster** | Asset-centric orchestration |
| **dbt** | SQL-first data transformation in-warehouse |

---

## Business Intelligence and Analytics

### BI Tools Compared

| Tool | Type | Strength |
|------|------|----------|
| **Tableau** | Commercial | Rich visual analytics, drag-and-drop |
| **Power BI** | Commercial (Microsoft) | Deep Office/Azure integration |
| **Looker** | Commercial (Google) | Data exploration, LookML modelling |
| **Metabase** | Open-source | Easy setup, SQL-native |
| **Superset** | Open-source (Apache) | Scalable, SQL-first |

### Dashboard Design Principles

Effective dashboards follow established principles: identify the audience, choose the appropriate visualisation for each metric, use colour strategically (not decoratively), maintain consistent scales, and enable interactivity (filters, drill-downs). Performance is also important — dashboards with slow load times reduce user adoption.

### Common KPI Categories

| Category | Examples |
|----------|---------|
| **Financial** | Revenue, profit margin, ROI, customer lifetime value |
| **Customer** | Acquisition cost (CAC), churn rate, NPS, satisfaction score |
| **Operational** | Efficiency rates, cycle time, defect rates |
| **Marketing** | Conversion rate, click-through rate, ROAS, attribution |
| **Product** | Daily active users, engagement, retention, feature adoption |

---

## Advanced Analytics

| Approach | Techniques | When to Use |
|----------|-----------|-------------|
| **Predictive** | Time series (ARIMA, Prophet, LSTM), risk modelling, churn prediction | Forecasting future values |
| **Prescriptive** | Linear programming, Monte Carlo simulation, A/B testing, multi-armed bandits | Optimising decisions |
| **Text Analytics** | Tokenization, sentiment analysis, topic modelling (LDA), NER, word embeddings (Word2Vec, BERT) | Extracting insight from text |

---

## Data Ethics and Governance

### Privacy Regulations

| Regulation | Scope |
|-----------|-------|
| **GDPR** | EU data subjects; right to erasure, consent, data portability |
| **CCPA** | California consumers; opt-out of data sales |
| **HIPAA** | US healthcare data; strict confidentiality rules |

### Data Quality Dimensions

| Dimension | Question |
|-----------|----------|
| **Accuracy** | Is the data correct? |
| **Completeness** | Is anything missing? |
| **Consistency** | Do sources agree? |
| **Timeliness** | Is it current? |
| **Validity** | Does it conform to expected formats? |
| **Uniqueness** | Are there duplicates? |

### Bias and Fairness

Bias can enter at any stage: sampling bias (non-representative data), measurement bias (flawed instruments), or algorithmic bias (discriminatory predictions). Mitigation strategies include pre-processing (fixing the data), in-processing (constraining the model), and post-processing (adjusting outputs). Fairness metrics like demographic parity and equal opportunity help quantify the problem.

---

## Career Paths

| Role | Focus |
|------|-------|
| **Data Analyst** | Descriptive analytics, dashboards, reporting |
| **Data Scientist** | Statistical modelling, ML, advanced analytics |
| **ML Engineer** | Production ML systems, model deployment, MLOps |
| **Data Engineer** | Data pipelines, infrastructure, ETL |
| **Analytics Manager** | Team leadership, strategy, stakeholder management |
| **Research Scientist** | Novel algorithms, publications |

---

## Emerging Trends

- **AutoML**: Automated pipeline creation and model selection.
- **MLOps**: DevOps practices applied to ML lifecycle management.
- **Feature Stores**: Centralised feature management for reuse across teams.
- **Data Mesh**: Decentralised, domain-owned data architecture.
- **LLMs and Generative AI**: Large language models transforming text, code, and image workflows.
- **Edge Analytics**: Processing data on-device rather than in the cloud.
- **Causal Inference**: Moving beyond correlation to understand actual cause and effect.
- **Federated Learning**: Training models across decentralised data without moving it.
- **Responsible AI**: Ethics, explainability, and transparency becoming standard requirements.
