<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 資料 科學 和 Analytics

## Core Concepts

### What is 資料 科學?
資料 科學 is an interdisciplinary field that uses scientific methods, processes, algorithms, 和 系統 to extract knowledge 和 insights from structured 和 unstructured 資料. It combines:
- **統計**: Mathematical foundation 為 analysis
- **Computer 科學**: Programming, algorithms, 資料 structures
- **Domain Expertise**: Subject matter knowledge
- **資料 Visualization**: Communicating findings effectively

### 資料 Types
- **Structured 資料**: Organized 在 rows/columns (databases, spreadsheets)
- **Unstructured 資料**: No predefined format (text, images, audio, video)
- **Semi-structured 資料**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series 資料**: Sequential 資料 points indexed 在 time order
- **Spatial 資料**: Geographic/location-based information
- **Graph 資料**: Nodes 和 edges representing relationships

### 這 資料 科學 Process (CRISP-DM)
1. **商業 Understanding**: Define objectives 和 requirements
2. **資料 Understanding**: Collect 和 explore initial 資料
3. **資料 Preparation**: Clean, transform, 和 format 資料 (80% 的 work)
4. **Modeling**: Select 和 apply modeling techniques
5. **Evaluation**: Assess model 效能 against objectives
6. **部署**: Implement model 在 production environment

## 統計 基礎

### Descriptive 統計
- **Measures 的 Central Tendency**: Mean, median, mode
- **Measures 的 Dispersion**: Range, variance, standard deviation, interquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles 和 Quartiles**: Position within distribution

### Inferential 統計
- **Hypothesis 測試**: Null hypothesis, alternative hypothesis, p-values
- **Confidence Intervals**: Range 的 values likely containing population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejecting true null hypothesis)
- **Type II Error**: False negative (failing to reject false null hypothesis)
- **Power**: Probability 的 correctly rejecting false null hypothesis

### Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Binomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count 的 事件 在 fixed interval
- **Uniform Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between 事件
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical 資料 analysis

### Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test independence 的 categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Linear relationship between continuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

## 資料 Collection 和 Storage

### 資料 Sources
- **Databases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, 網路 scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming 資料**: Kafka, Kinesis, real-time feeds
- **Surveys 和 Experiments**: Primary 資料 collection
- **Public Datasets**: Government 資料, Kaggle, academic repositories

### 資料 Warehousing
- **ETL**: Extract, Transform, Load process
- **資料 Lake**: Raw 資料 storage 在 native format
- **資料 Warehouse**: Structured, processed 資料 為 analysis
- **資料 Mart**: Subset 的 warehouse 為 specific department
- **OLAP**: Online Analytical Processing, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

### 資料庫 Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassandra, HBase (optimized 為 columns)
- **Graph**: Neo4j, Amazon Neptune (nodes 和 relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped 資料)
- **Vector**: Pinecone, Milvus (embedding storage 為 ML)

## 資料 Preprocessing

### 資料 Cleaning
- **Missing Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capping, transformation)
- **Duplicates**: Identification 和 removal
- **Inconsistencies**: Standardizing formats, fixing typos
- **資料 Validation**: Checking constraints, ranges, types

### 資料 Transformation
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

## Exploratory 資料 Analysis (EDA)

### EDA Techniques
- **Summary 統計**: Describe central tendency, spread, shape
- **Univariate Analysis**: Single variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable interactions
- **Correlation Analysis**: Identify relationships 和 multicollinearity
- **Segmentation**: Group similar observations

### Visualization Tools
- **Histograms**: Distribution 的 single variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two continuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Charts**: Categorical comparisons
- **Line Charts**: Trends over time
- **Violin Plots**: Distribution density 與 box plot elements
- **Pair Plots**: Multiple scatter plots 為 variable pairs

### Python Libraries 為 EDA
- **pandas**: 資料 manipulation 和 analysis
- **numpy**: Numerical 計算
- **matplotlib**: Basic plotting
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific 計算 和 統計

## 機器學習 在 資料 科學

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
  - 支援 Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - 神經網絡

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

## Big 資料 Technologies

### Distributed 計算 Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: 在-memory processing, faster than Hadoop
  - Spark SQL: Structured 資料 processing
  - Spark Streaming: Real-time 資料
  - MLlib: 機器學習 library
  - GraphX: Graph processing
- **Apache Flink**: Stream processing 與 low latency
- **Apache Beam**: Unified batch 和 streaming

### Cloud Platforms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, 機器學習, 資料 Lake
- **Snowflake**: Cloud 資料 warehouse

### 資料 Pipeline Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeline 管理 (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: 資料 orchestrator 與 asset focus
- **dbt**: 資料 transformation 在 warehouse

## 商業 Intelligence 和 Analytics

### BI Tools
- **Tableau**: Visual analytics platform
- **Power BI**: Microsoft 商業 analytics
- **Looker**: 資料 exploration 和 insights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

### Dashboard Design Principles
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to 資料 type
- **Use Color Strategically**: Highlight important information
- **Maintain Consistency**: Standardize formats 和 scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize 效能**: Fast loading, efficient queries
- **Mobile Considerations**: Responsive design

### Key 效能 Indicators (KPIs)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

## 高級 Analytics

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
- **A/B 測試**: Experimental design, statistical significance
- **Multi-Armed Bandits**: Adaptive experimentation

### Text Analytics (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeling**: LDA, NMF 為 theme discovery
- **Named Entity Recognition**: Identifying people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

## 資料 Ethics 和 Governance

### 資料 Privacy
- **GDPR**: EU General 資料 Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability 和 Accountability Act (US 醫療)
- **Anonymization**: Removing personally identifiable information
- **Differential Privacy**: Adding noise to protect individuals
- **Consent 管理**: Opt-在/opt-out mechanisms

### 資料 Quality
- **Accuracy**: Correctness 的 資料
- **Completeness**: All required 資料 present
- **Consistency**: No contradictions across sources
- **Timeliness**: 資料 可用 when needed
- **Validity**: Conforms to defined rules
- **Uniqueness**: No duplicates

### Bias 和 Fairness
- **Sampling Bias**: Non-representative 資料 collection
- **Measurement Bias**: Flawed 資料 collection instruments
- **Algorithmic Bias**: Discriminatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, 在-processing, post-processing

### 資料 Governance Framework
- **資料 Stewardship**: Responsibility 為 資料 assets
- **Metadata 管理**: 資料 about 資料 documentation
- **資料 Lineage**: Tracking 資料 flow 和 transformations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logging 資料 access 和 changes
- **Compliance**: Regulatory adherence

## Career Paths 在 資料 科學

### Roles
- **資料 Analyst**: Focus on descriptive analytics, dashboards, reporting
- **資料 Scientist**: Statistical modeling, 機器學習, 高級 analytics
- **ML Engineer**: Production ML 系統, model 部署, MLOps
- **資料 Engineer**: 資料 pipelines, infrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder 管理
- **BI Developer**: Dashboard creation, report 開發
- **Research Scientist**: Novel algorithms, publications, 高級 research

### Skills Matrix
- **Technical**: Python/R, SQL, 統計, ML frameworks, cloud platforms
- **Analytical**: Problem-solving, critical thinking, experimental design
- **溝通**: Storytelling, visualization, presentation skills
- **商業**: Domain knowledge, stakeholder 管理, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control 為 models

## Emerging Trends

### Current Developments
- **AutoML**: Automated 機器學習 pipeline creation
- **MLOps**: DevOps practices 為 機器學習
- **Feature Stores**: Centralized feature 管理
- **資料 Mesh**: Decentralized 資料 架構
- **LLMs 和 Generative AI**: Large 語言 models, content generation
- **Edge Analytics**: Processing 資料 at source devices
- **Real-Time Analytics**: Streaming 資料 analysis
- **Augmented Analytics**: AI-assisted 資料 preparation 和 insights

### 未來 Directions
- **Quantum 機器學習**: Quantum 計算 為 ML
- **Federated Learning**: Training models across decentralized 資料
- **Causal Inference**: Moving beyond correlation to causation
- **Responsible AI**: Ethics, explainability, transparency
- **資料 Fabric**: Integrated 資料 管理 across environments
