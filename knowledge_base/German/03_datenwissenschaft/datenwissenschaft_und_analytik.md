<!-- 
This file was automatically translated from English to German.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Daten Wissenschaft und Analytics

# # Core Concepts

# ## What is Daten Wissenschaft?
Daten wissenschaft is an interdisciplinary field that uses scientific methods, processes, algorithms, und systeme to extract knowledge und insights from structured und unstructured daten. It combines:
- **Statistiken**: Mader/die/dasmatical foundation für analysis
- **Computer Wissenschaft**: Programming, algorithms, daten structures
- **Domain Expertise**: Subject matter knowledge
- **Daten Visualization**: Communicating findings effectively

# ## Daten Types
- **Structured Daten**: Organized in rows/columns (datenbases, spreadsheets)
- **Unstructured Daten**: No predefined fürmat (text, images, audio, video)
- **Semi-structured Daten**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series Daten**: Sequential daten points indexed in time order
- **Spatial Daten**: Geographic/location-based infürmation
- **Graph Daten**: Nodes und edges representing relationships

# ## The Daten Wissenschaft Process (CRISP-DM)
1. **Geschäft Understunding**: Define objectives und requirements
2. **Daten Understunding**: Collect und explore initial daten
3. **Daten Preparation**: Clean, transfürm, und fürmat daten (80% von work)
4. **Modeling**: Select und apply modeling techniques
5. **Evaluation**: Assess model perfürmance against objectives
6. **Bereitstellung**: Implement model in production environment

# # Statistiken Grundlagen

# ## Descriptive Statistiken
- **Measures von Central Tendency**: Mean, median, mode
- **Measures von Dispersion**: Range, variance, stundard deviation, interquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles und Quartiles**: Position mitin distribution

# ## Inferential Statistiken
- **Hypoder/die/dassis Testen**: Null hypoder/die/dassis, alternative hypoder/die/dassis, p-values
- **Confidence Intervals**: Range von values likely containing population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejecting true null hypoder/die/dassis)
- **Type II Error**: False negative (failing to reject false null hypoder/die/dassis)
- **Power**: Probability von correctly rejecting false null hypoder/die/dassis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Binomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count von ereignisse in fixed interval
- **Unifürm Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between ereignisse
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical daten analysis

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
- **Datenbases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, web scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming Daten**: Kafka, Kinesis, real-time feeds
- **Surveys und Experiments**: Primary daten collection
- **Public Datensets**: Government daten, Kaggle, academic repositories

# ## Daten Warehousing
- **ETL**: Extract, Transfürm, Load process
- **Daten Lake**: Raw daten storage in native fürmat
- **Daten Warehouse**: Structured, processed daten für analysis
- **Daten Mart**: Subset von warehouse für specific department
- **OLAP**: Online Analytical Processing, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

# ## Datenbase Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassundra, HBase (optimized für columns)
- **Graph**: Neo4j, Amazon Neptune (nodes und relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped daten)
- **Vector**: Pinecone, Milvus (embedding storage für ML)

# # Daten Preprocessing

# ## Daten Cleaning
- **Missing Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capping, transfürmation)
- **Duplicates**: Identification und removal
- **Inconsistencies**: Stundardizing fürmats, fixing typos
- **Daten Validation**: Checking constraints, ranges, types

# ## Daten Transfürmation
- **Normalization**: Scaling to 0-1 range
- **Stundardization**: Z-score normalization (mean=0, std=1)
- **Encoding**: One-hot, label, ordinal, target encoding
- **Binning**: Grouping continuous values into categories
- **Log Transfürmation**: Reducing skewness
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
- **Bar Chkünste**: Categorical comparisons
- **Line Chkünste**: Trends over time
- **Violin Plots**: Distribution density mit box plot elements
- **Pair Plots**: Multiple scatter plots für variable pairs

# ## Python Libraries für EDA
- **pundas**: Daten manipulation und analysis
- **numpy**: Numerical datenverarbeitung
- **matplotlib**: Basic plotting
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific datenverarbeitung und statistiken

# # Maschinelles Lernen in Daten Wissenschaft

# ## Supervised Learning
- **Regression**: Predict continuous values
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Rundom Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Predict categorical labels
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Rundom Forest
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
  - Unifürm Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Find co-occurring items
  - Apriori Algorithm
  - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuning**: Grid search, rundom search, Bayesian optimization
- **Learning Curves**: Diagnose bias-variance tradevonf

# # Big Daten Technologies

# ## Distributed Datenverarbeitung Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory processing, faster than Hadoop
  - Spark SQL: Structured daten processing
  - Spark Streaming: Real-time daten
  - MLlib: Machine learning library
  - GraphX: Graph processing
- **Apache Flink**: Stream processing mit low latency
- **Apache Beam**: Unified batch und streaming

# ## Cloud Platfürms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Datenproc, AI Platfürm, Cloud Storage
- **Azure**: Synapse Analytics, Datenbricks, Maschinelles Lernen, Daten Lake
- **Snowflake**: Cloud daten warehouse

# ## Daten Pipeline Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeline verwaltung (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: Daten orchestrator mit asset focus
- **dbt**: Daten transfürmation in warehouse

# # Geschäft Intelligence und Analytics

# ## BI Tools
- **Tableau**: Visual analytics platfürm
- **Power BI**: Microsvont geschäft analytics
- **Looker**: Daten exploration und insights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Principles
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to daten type
- **Use Color Strategically**: Highlight important infürmation
- **Maintain Consistency**: Stundardize fürmats und scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Perfürmance**: Fast loading, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Perfürmance Indicators (KPIs)
- **Financial**: Revenue, prvonit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # Fortgeschritten Analytics

# ## Predictive Analytics
- **Forecasting**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeling**: Credit scoring, fraud detection, insurance
- **Customer Analytics**: Churn prediction, propensity modeling
- **Demund Forecasting**: Inventory optimization, supply chain
- **Maintenance Prediction**: Equipment failure anticipation

# ## Prescriptive Analytics
- **Optimization**: Linear programming, integer programming
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, influence diagrams
- **A/B Testen**: Experimental design, statistical significance
- **Multi-Armed Bundits**: Adaptive experimentation

# ## Text Analytics (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeling**: LDA, NMF für der/die/dasme discovery
- **Named Entity Recognition**: Identifying people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

# # Daten Ethics und Governance

# ## Daten Privacy
- **GDPR**: EU General Daten Protection Regulation
- **CCPA**: Califürnia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability und Accountability Act (US gesundheitswesen)
- **Anonymization**: Removing personally identifiable infürmation
- **Differential Privacy**: Adding noise to protect individuals
- **Consent Verwaltung**: Opt-in/opt-out mechanisms

# ## Daten Quality
- **Accuracy**: Correctness von daten
- **Completeness**: All required daten present
- **Consistency**: No contradictions across sources
- **Timeliness**: Daten available when needed
- **Validity**: Confürms to defined rules
- **Uniqueness**: No duplicates

# ## Bias und Fairness
- **Sampling Bias**: Non-representative daten collection
- **Measurement Bias**: Frechted daten collection instruments
- **Algorithmic Bias**: Discriminatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, in-processing, post-processing

# ## Daten Governance Framework
- **Daten Stewardship**: Responsibility für daten assets
- **Metadaten Verwaltung**: Daten about daten documentation
- **Daten Lineage**: Tracking daten flow und transfürmations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logging daten access und changes
- **Compliance**: Regulatory adherence

# # Career Paths in Daten Wissenschaft

# ## Roles
- **Daten Analyst**: Focus on descriptive analytics, dashboards, reporting
- **Daten Scientist**: Statistical modeling, maschinelles lernen, fortgeschritten analytics
- **ML Engineer**: Production ML systeme, model bereitstellung, MLOps
- **Daten Engineer**: Daten pipelines, infrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder verwaltung
- **BI Developer**: Dashboard creation, report entwicklung
- **Research Scientist**: Novel algorithms, publications, fortgeschritten research

# ## Skills Matrix
- **Technical**: Python/R, SQL, statistiken, ML frameworks, cloud platfürms
- **Analytical**: Problem-solving, critical thinking, experimental design
- **Kommunikation**: Storytelling, visualization, presentation skills
- **Geschäft**: Domain knowledge, stakeholder verwaltung, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control für models

# # Emerging Trends

# ## Current Entwicklungs
- **AutoML**: Automated maschinelles lernen pipeline creation
- **MLOps**: DevOps practices für maschinelles lernen
- **Feature Stores**: Centralized feature verwaltung
- **Daten Mesh**: Decentralized daten architektur
- **LLMs und Generative AI**: Large sprache models, content generation
- **Edge Analytics**: Processing daten at source devices
- **Real-Time Analytics**: Streaming daten analysis
- **Augmented Analytics**: AI-assisted daten preparation und insights

# ## Zukunft Directions
- **Quantum Maschinelles Lernen**: Quantum datenverarbeitung für ML
- **Federated Learning**: Training models across decentralized daten
- **Causal Inference**: Moving beyond correlation to causation
- **Responsible AI**: Ethics, explainability, transparency
- **Daten Fabric**: Integrated daten verwaltung across environments
