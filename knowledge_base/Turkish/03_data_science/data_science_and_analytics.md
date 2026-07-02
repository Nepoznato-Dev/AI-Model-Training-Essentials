<!-- 
This file was automatically translated from English to Turkish.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Veri Bilim ve Analytics

## Core Concepts

### What is Veri Bilim?
Veri Bilim is an interdisciplinary field that uses scientific methods, processes, algorithms, ve Sistemler to extract knowledge ve insights from structured ve unstructured Veri. It combines:
- **İstatistikler**: Mathematical foundation için analysis
- **Computer Bilim**: Programming, algorithms, Veri structures
- **Domain Expertise**: Subject matter knowledge
- **Veri Visualization**: Communicating findings effectively

### Veri Types
- **Structured Veri**: Organized içinde rows/columns (databases, spreadsheets)
- **Unstructured Veri**: No predefined format (text, images, audio, video)
- **Semi-structured Veri**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series Veri**: Sequential Veri points indexed içinde time order
- **Spatial Veri**: Geographic/location-based information
- **Graph Veri**: Nodes ve edges representing relationships

### bu Veri Bilim Process (CRISP-DM)
1. **İş Understanding**: Define objectives ve requirements
2. **Veri Understanding**: Collect ve explore initial Veri
3. **Veri Preparation**: Clean, transform, ve format Veri (80% içinde work)
4. **Modeling**: Select ve apply modeling techniques
5. **Evaluation**: Assess model Performans against objectives
6. **Dağıtım**: Implement model içinde production environment

## İstatistikler Temeller

### Descriptive İstatistikler
- **Measures içinde Central Tendency**: Mean, median, mode
- **Measures içinde Dispersion**: Range, variance, standard deviation, interquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles ve Quartiles**: Position within distribution

### Inferential İstatistikler
- **Hypothesis Test Etme**: Null hypothesis, alternative hypothesis, p-values
- **Confidence Intervals**: Range içinde values likely containing population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejecting true null hypothesis)
- **Type II Error**: False negative (failing to reject false null hypothesis)
- **Power**: Probability içinde correctly rejecting false null hypothesis

### Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Binomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count içinde Olaylar içinde fixed interval
- **Uniform Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between Olaylar
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical Veri analysis

### Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test independence içinde categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Linear relationship between continuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

## Veri Collection ve Storage

### Veri Sources
- **Databases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, Web scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming Veri**: Kafka, Kinesis, real-time feeds
- **Surveys ve Experiments**: Primary Veri collection
- **Public Datasets**: Government Veri, Kaggle, academic repositories

### Veri Warehousing
- **ETL**: Extract, Transform, Load process
- **Veri Lake**: Raw Veri storage içinde native format
- **Veri Warehouse**: Structured, processed Veri için analysis
- **Veri Mart**: Subset içinde warehouse için specific department
- **OLAP**: Online Analytical Processing, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

### Veritabanı Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassandra, HBase (optimized için columns)
- **Graph**: Neo4j, Amazon Neptune (nodes ve relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped Veri)
- **Vector**: Pinecone, Milvus (embedding storage için ML)

## Veri Preprocessing

### Veri Cleaning
- **Missing Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capping, transformation)
- **Duplicates**: Identification ve removal
- **Inconsistencies**: Standardizing formats, fixing typos
- **Veri Validation**: Checking constraints, ranges, types

### Veri Transformation
- **Normalization**: Scaling to 0-1 range
- **Standardization**: Z-score normalization (mean=0, std=1)
- **Encoding**: One-hot, label, ordinal, target encoding
- **Binning**: Grouping continuous values into categories
- **Log Transformation**: Reducing skewness
- **Feature Scaling**: Making features comparable

### Feature Engineering
- **Feature Creation**: Deriving new features from existing ones
- **Feature Selection**: Choosing most relevant features
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimination)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Combining features multiplicatively
- **Polynomial Features**: Creating higher-order terms

## Exploratory Veri Analysis (EDA)

### EDA Techniques
- **Summary İstatistikler**: Describe central tendency, spread, shape
- **Univariate Analysis**: Single variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable interactions
- **Correlation Analysis**: Identify relationships ve multicollinearity
- **Segmentation**: Group similar observations

### Visualization Tools
- **Histograms**: Distribution içinde single variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two continuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Charts**: Categorical comparisons
- **Line Charts**: Trends over time
- **Violin Plots**: Distribution density ile box plot elements
- **Pair Plots**: Multiple scatter plots için variable pairs

### Python Libraries için EDA
- **pandas**: Veri manipulation ve analysis
- **numpy**: Numerical Bilişim
- **matplotlib**: Basic plotting
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific Bilişim ve İstatistikler

## Makine Öğrenimi içinde Veri Bilim

### Supervised Learning
- **Regression**: Predict continuous values
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Predict categorical labels
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Sinir Ağları

### Unsupervised Learning
- **Clustering**: Group similar observations
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **Dimensionality Reduction**: Reduce feature count
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Find co-occurring items
  - Apriori Algorithm
  - FP-Growth

### Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Learning Curves**: Diagnose bias-variance tradeoff

## Big Veri Technologies

### Distributed Bilişim Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: içinde-memory processing, faster than Hadoop
  - Spark SQL: Structured Veri processing
  - Spark Streaming: Real-time Veri
  - MLlib: Makine Öğrenimi library
  - GraphX: Graph processing
- **Apache Flink**: Stream processing ile low latency
- **Apache Beam**: Unified batch ve streaming

### Cloud Platforms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Makine Öğrenimi, Veri Lake
- **Snowflake**: Cloud Veri warehouse

### Veri Pipeline Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeline Yönetim (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: Veri orchestrator ile asset focus
- **dbt**: Veri transformation içinde warehouse

## İş Intelligence ve Analytics

### BI Tools
- **Tableau**: Visual analytics platform
- **Power BI**: Microsoft İş analytics
- **Looker**: Veri exploration ve insights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

### Dashboard Design Principles
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to Veri type
- **Use Color Strategically**: Highlight important information
- **Maintain Consistency**: Standardize formats ve scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Performans**: Fast loading, efficient queries
- **Mobile Considerations**: Responsive design

### Key Performans Indicators (KPIs)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

## İleri Düzey Analytics

### Predictive Analytics
- **Forecasting**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeling**: Credit scoring, fraud detection, insurance
- **Customer Analytics**: Churn prediction, propensity modeling
- **Demand Forecasting**: Inventory optimization, supply chain
- **Maintenance Prediction**: Equipment failure anticipation

### Prescriptive Analytics
- **Optimization**: Linear programming, integer programming
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, influence diagrams
- **A/B Test Etme**: Experimental design, statistical significance
- **Multi-Armed Bandits**: Adaptive experimentation

### Text Analytics (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeling**: LDA, NMF için theme discovery
- **Named Entity Recognition**: Identifying people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Veri Ethics ve Governance

### Veri Privacy
- **GDPR**: EU General Veri Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability ve Accountability Act (US Sağlık Hizmetleri)
- **Anonymization**: Removing personally identifiable information
- **Differential Privacy**: Adding noise to protect individuals
- **Consent Yönetim**: Opt-içinde/opt-out mechanisms

### Veri Quality
- **Accuracy**: Correctness içinde Veri
- **Completeness**: All required Veri present
- **Consistency**: No contradictions across sources
- **Timeliness**: Veri available when needed
- **Validity**: Conforms to defined rules
- **Uniqueness**: No duplicates

### Bias ve Fairness
- **Sampling Bias**: Non-representative Veri collection
- **Measurement Bias**: Flawed Veri collection instruments
- **Algorithmic Bias**: Discriminatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, içinde-processing, post-processing

### Veri Governance Framework
- **Veri Stewardship**: Responsibility için Veri assets
- **Metadata Yönetim**: Veri about Veri documentation
- **Veri Lineage**: Tracking Veri flow ve transformations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logging Veri access ve changes
- **Compliance**: Regulatory adherence

## Career Paths içinde Veri Bilim

### Roles
- **Veri Analyst**: Focus on descriptive analytics, dashboards, reporting
- **Veri Scientist**: Statistical modeling, Makine Öğrenimi, İleri Düzey analytics
- **ML Engineer**: Production ML Sistemler, model Dağıtım, MLOps
- **Veri Engineer**: Veri pipelines, infrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder Yönetim
- **BI Developer**: Dashboard creation, report Geliştirme
- **Research Scientist**: Novel algorithms, publications, İleri Düzey research

### Skills Matrix
- **Technical**: Python/R, SQL, İstatistikler, ML frameworks, cloud platforms
- **Analytical**: Problem-solving, critical thinking, experimental design
- **İletişim**: Storytelling, visualization, presentation skills
- **İş**: Domain knowledge, stakeholder Yönetim, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control için models

## Emerging Trends

### Current Developments
- **AutoML**: Automated Makine Öğrenimi pipeline creation
- **MLOps**: DevOps practices için Makine Öğrenimi
- **Feature Stores**: Centralized feature Yönetim
- **Veri Mesh**: Decentralized Veri Mimari
- **LLMs ve Generative AI**: Large Dil models, content generation
- **Edge Analytics**: Processing Veri at source devices
- **Real-Time Analytics**: Streaming Veri analysis
- **Augmented Analytics**: AI-assisted Veri preparation ve insights

### Gelecek Directions
- **Quantum Makine Öğrenimi**: Quantum Bilişim için ML
- **Federated Learning**: Training models across decentralized Veri
- **Causal Inference**: Moving beyond correlation to causation
- **Responsible AI**: Ethics, explainability, transparency
- **Veri Fabric**: Integrated Veri Yönetim across environments
