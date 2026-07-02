<!-- 
This file was automatically translated from English to German.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Daten Wissenschaft und Analytics

# # Core Concepts

# ## What is Daten Wissenschaft?
Daten Wissenschaft is an interdisciplinary field that uses scientific methods, processes, algorithms, und Systeme to extract knowledge und insights from structured und unstructured Daten. It combines:
- **Statistiken**: Mathematical foundation für analysis
- **Computer Wissenschaft**: Programming, algorithms, Daten structures
- **Domain Expertise**: Subject matter knowledge
- **Daten Visualization**: Communicating findings effectively

# ## Daten Types
- **Structured Daten**: Organized in rows/columns (databases, spreadsheets)
- **Unstructured Daten**: No predefined format (text, images, audio, video)
- **Semi-structured Daten**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series Daten**: Sequential Daten points indexed in time order
- **Spatial Daten**: Geographic/location-based information
- **Graph Daten**: Nodes und edges representing relationships

# ## der/die/das Daten Wissenschaft Process (CRISP-DM)
1. **Geschäft Understanding**: Define objectives und requirements
2. **Daten Understanding**: Collect und explore initial Daten
3. **Daten Preparation**: Clean, transform, und format Daten (80% von work)
4. **Modeling**: Select und apply modeling techniques
5. **Evaluation**: Assess model Leistung against objectives
6. **Bereitstellung**: Implement model in production environment

# # Statistiken Grundlagen

# ## Descriptive Statistiken
- **Measures von Central Tendency**: Mean, median, mode
- **Measures von Dispersion**: Range, variance, standard deviation, interquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles und Quartiles**: Position within distribution

# ## Inferential Statistiken
- **Hypothesis Testen**: Null hypothesis, alternative hypothesis, p-values
- **Confidence Intervals**: Range von values likely containing population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejecting true null hypothesis)
- **Type II Error**: False negative (failing to reject false null hypothesis)
- **Power**: Probability von correctly rejecting false null hypothesis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Binomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count von Ereignisse in fixed interval
- **Uniform Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between Ereignisse
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical Daten analysis

# ## Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test independence von categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Linear relationship between continuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

# # Daten Collection und Storage

# ## Daten Sources
- **Databases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, Web scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming Daten**: Kafka, Kinesis, real-time feeds
- **Surveys und Experiments**: Primary Daten collection
- **Public Datasets**: Government Daten, Kaggle, academic repositories

# ## Daten Warehousing
- **ETL**: Extract, Transform, Load process
- **Daten Lake**: Raw Daten storage in native format
- **Daten Warehouse**: Structured, processed Daten für analysis
- **Daten Mart**: Subset von warehouse für specific department
- **OLAP**: Online Analytical Processing, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

# ## Datenbank Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassandra, HBase (optimized für columns)
- **Graph**: Neo4j, Amazon Neptune (nodes und relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped Daten)
- **Vector**: Pinecone, Milvus (embedding storage für ML)

# # Daten Preprocessing

# ## Daten Cleaning
- **Missing Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capping, transformation)
- **Duplicates**: Identification und removal
- **Inconsistencies**: Standardizing formats, fixing typos
- **Daten Validation**: Checking constraints, ranges, types

# ## Daten Transformation
- **Normalization**: Scaling to 0-1 range
- **Standardization**: Z-score normalization (mean=0, std=1)
- **Encoding**: One-hot, label, ordinal, target encoding
- **Binning**: Grouping continuous values into categories
- **Log Transformation**: Reducing skewness
- **Feature Scaling**: Making features comparable

# ## Feature Engineering
- **Feature Creation**: Deriving new features from existing ones
- **Feature Selection**: Choosing most relevant features
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimination)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Combining features multiplicatively
- **Polynomial Features**: Creating higher-order terms

# # Exploratory Daten Analysis (EDA)

# ## EDA Techniques
- **Summary Statistiken**: Describe central tendency, spread, shape
- **Univariate Analysis**: Single variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable interactions
- **Correlation Analysis**: Identify relationships und multicollinearity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution von single variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two continuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Charts**: Categorical comparisons
- **Line Charts**: Trends over time
- **Violin Plots**: Distribution density mit box plot elements
- **Pair Plots**: Multiple scatter plots für variable pairs

# ## Python Libraries für EDA
- **pandas**: Daten manipulation und analysis
- **numpy**: Numerical Datenverarbeitung
- **matplotlib**: Basic plotting
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific Datenverarbeitung und Statistiken

# # Maschinelles Lernen in Daten Wissenschaft

# ## Supervised Learning
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
  - Neuronale Netze

# ## Unsupervised Learning
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

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Learning Curves**: Diagnose bias-variance tradeoff

# # Big Daten Technologies

# ## Distributed Datenverarbeitung Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: in-memory processing, faster than Hadoop
  - Spark SQL: Structured Daten processing
  - Spark Streaming: Real-time Daten
  - MLlib: Maschinelles Lernen library
  - GraphX: Graph processing
- **Apache Flink**: Stream processing mit low latency
- **Apache Beam**: Unified batch und streaming

# ## Cloud Platforms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Maschinelles Lernen, Daten Lake
- **Snowflake**: Cloud Daten warehouse

# ## Daten Pipeline Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeline Verwaltung (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: Daten orchestrator mit asset focus
- **dbt**: Daten transformation in warehouse

# # Geschäft Intelligence und Analytics

# ## BI Tools
- **Tableau**: Visual analytics platform
- **Power BI**: Microsoft Geschäft analytics
- **Looker**: Daten exploration und insights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Principles
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to Daten type
- **Use Color Strategically**: Highlight important information
- **Maintain Consistency**: Standardize formats und scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Leistung**: Fast loading, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Leistung Indicators (KPIs)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # Fortgeschritten Analytics

# ## Predictive Analytics
- **Forecasting**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeling**: Credit scoring, fraud detection, insurance
- **Customer Analytics**: Churn prediction, propensity modeling
- **Demand Forecasting**: Inventory optimization, supply chain
- **Maintenance Prediction**: Equipment failure anticipation

# ## Prescriptive Analytics
- **Optimization**: Linear programming, integer programming
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, influence diagrams
- **A/B Testen**: Experimental design, statistical significance
- **Multi-Armed Bandits**: Adaptive experimentation

# ## Text Analytics (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeling**: LDA, NMF für theme discovery
- **Named Entity Recognition**: Identifying people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

# # Daten Ethics und Governance

# ## Daten Privacy
- **GDPR**: EU General Daten Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability und Accountability Act (US Gesundheitswesen)
- **Anonymization**: Removing personally identifiable information
- **Differential Privacy**: Adding noise to protect individuals
- **Consent Verwaltung**: Opt-in/opt-out mechanisms

# ## Daten Quality
- **Accuracy**: Correctness von Daten
- **Completeness**: All required Daten present
- **Consistency**: No contradictions across sources
- **Timeliness**: Daten available when needed
- **Validity**: Conforms to defined rules
- **Uniqueness**: No duplicates

# ## Bias und Fairness
- **Sampling Bias**: Non-representative Daten collection
- **Measurement Bias**: Flawed Daten collection instruments
- **Algorithmic Bias**: Discriminatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, in-processing, post-processing

# ## Daten Governance Framework
- **Daten Stewardship**: Responsibility für Daten assets
- **Metadata Verwaltung**: Daten about Daten documentation
- **Daten Lineage**: Tracking Daten flow und transformations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logging Daten access und changes
- **Compliance**: Regulatory adherence

# # Career Paths in Daten Wissenschaft

# ## Roles
- **Daten Analyst**: Focus on descriptive analytics, dashboards, reporting
- **Daten Scientist**: Statistical modeling, Maschinelles Lernen, Fortgeschritten analytics
- **ML Engineer**: Production ML Systeme, model Bereitstellung, MLOps
- **Daten Engineer**: Daten pipelines, infrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder Verwaltung
- **BI Developer**: Dashboard creation, report Entwicklung
- **Research Scientist**: Novel algorithms, publications, Fortgeschritten research

# ## Skills Matrix
- **Technical**: Python/R, SQL, Statistiken, ML frameworks, cloud platforms
- **Analytical**: Problem-solving, critical thinking, experimental design
- **Kommunikation**: Storytelling, visualization, presentation skills
- **Geschäft**: Domain knowledge, stakeholder Verwaltung, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control für models

# # Emerging Trends

# ## Current Developments
- **AutoML**: Automated Maschinelles Lernen pipeline creation
- **MLOps**: DevOps practices für Maschinelles Lernen
- **Feature Stores**: Centralized feature Verwaltung
- **Daten Mesh**: Decentralized Daten Architektur
- **LLMs und Generative AI**: Large Sprache models, content generation
- **Edge Analytics**: Processing Daten at source devices
- **Real-Time Analytics**: Streaming Daten analysis
- **Augmented Analytics**: AI-assisted Daten preparation und insights

# ## Zukunft Directions
- **Quantum Maschinelles Lernen**: Quantum Datenverarbeitung für ML
- **Federated Learning**: Training models across decentralized Daten
- **Causal Inference**: Moving beyond correlation to causation
- **Responsible AI**: Ethics, explainability, transparency
- **Daten Fabric**: Integrated Daten Verwaltung across environments
