<!-- 
This file was automatically translated from English to Korean.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이터 과학 와 Analytics

## Core Concepts

### What is 데이터 과학?
데이터 과학 is an interdisciplinary field that uses scientific methods, processes, algorithms, 와 시스템 to extract knowledge 와 insights from structured 와 unstructured 데이터. It combines:
- **통계**: Mathematical foundation 위한 analysis
- **Computer 과학**: Programming, algorithms, 데이터 structures
- **Domain Expertise**: Subject matter knowledge
- **데이터 Visualization**: Communicating findings effectively

### 데이터 Types
- **Structured 데이터**: Organized 에서 rows/columns (databases, spreadsheets)
- **Unstructured 데이터**: No predefined format (text, images, audio, video)
- **Semi-structured 데이터**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series 데이터**: Sequential 데이터 points indexed 에서 time order
- **Spatial 데이터**: Geographic/location-based information
- **Graph 데이터**: Nodes 와 edges representing relationships

### 그 데이터 과학 Process (CRISP-DM)
1. **비즈니스 Understanding**: Define objectives 와 requirements
2. **데이터 Understanding**: Collect 와 explore initial 데이터
3. **데이터 Preparation**: Clean, transform, 와 format 데이터 (80% 의 work)
4. **Modeling**: Select 와 apply modeling techniques
5. **Evaluation**: Assess model 성능 against objectives
6. **배포**: Implement model 에서 production environment

## 통계 기초

### Descriptive 통계
- **Measures 의 Central Tendency**: Mean, median, mode
- **Measures 의 Dispersion**: Range, variance, standard deviation, interquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles 와 Quartiles**: Position within distribution

### Inferential 통계
- **Hypothesis 테스트**: Null hypothesis, alternative hypothesis, p-values
- **Confidence Intervals**: Range 의 values likely containing population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejecting true null hypothesis)
- **Type II Error**: False negative (failing to reject false null hypothesis)
- **Power**: Probability 의 correctly rejecting false null hypothesis

### Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Binomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count 의 이벤트 에서 fixed interval
- **Uniform Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between 이벤트
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical 데이터 analysis

### Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test independence 의 categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Linear relationship between continuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

## 데이터 Collection 와 Storage

### 데이터 Sources
- **Databases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, 웹 scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming 데이터**: Kafka, Kinesis, real-time feeds
- **Surveys 와 Experiments**: Primary 데이터 collection
- **Public Datasets**: Government 데이터, Kaggle, academic repositories

### 데이터 Warehousing
- **ETL**: Extract, Transform, Load process
- **데이터 Lake**: Raw 데이터 storage 에서 native format
- **데이터 Warehouse**: Structured, processed 데이터 위한 analysis
- **데이터 Mart**: Subset 의 warehouse 위한 specific department
- **OLAP**: Online Analytical Processing, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

### 데이터베이스 Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassandra, HBase (optimized 위한 columns)
- **Graph**: Neo4j, Amazon Neptune (nodes 와 relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped 데이터)
- **Vector**: Pinecone, Milvus (embedding storage 위한 ML)

## 데이터 Preprocessing

### 데이터 Cleaning
- **Missing Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capping, transformation)
- **Duplicates**: Identification 와 removal
- **Inconsistencies**: Standardizing formats, fixing typos
- **데이터 Validation**: Checking constraints, ranges, types

### 데이터 Transformation
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

## Exploratory 데이터 Analysis (EDA)

### EDA Techniques
- **Summary 통계**: Describe central tendency, spread, shape
- **Univariate Analysis**: Single variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable interactions
- **Correlation Analysis**: Identify relationships 와 multicollinearity
- **Segmentation**: Group similar observations

### Visualization Tools
- **Histograms**: Distribution 의 single variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two continuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Charts**: Categorical comparisons
- **Line Charts**: Trends over time
- **Violin Plots**: Distribution density 와 함께 box plot elements
- **Pair Plots**: Multiple scatter plots 위한 variable pairs

### Python Libraries 위한 EDA
- **pandas**: 데이터 manipulation 와 analysis
- **numpy**: Numerical 컴퓨팅
- **matplotlib**: Basic plotting
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific 컴퓨팅 와 통계

## 기계 학습 에서 데이터 과학

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
  - 지원 Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - 신경망

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

## Big 데이터 Technologies

### Distributed 컴퓨팅 Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: 에서-memory processing, faster than Hadoop
  - Spark SQL: Structured 데이터 processing
  - Spark Streaming: Real-time 데이터
  - MLlib: 기계 학습 library
  - GraphX: Graph processing
- **Apache Flink**: Stream processing 와 함께 low latency
- **Apache Beam**: Unified batch 와 streaming

### Cloud Platforms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, 기계 학습, 데이터 Lake
- **Snowflake**: Cloud 데이터 warehouse

### 데이터 Pipeline Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeline 관리 (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: 데이터 orchestrator 와 함께 asset focus
- **dbt**: 데이터 transformation 에서 warehouse

## 비즈니스 Intelligence 와 Analytics

### BI Tools
- **Tableau**: Visual analytics platform
- **Power BI**: Microsoft 비즈니스 analytics
- **Looker**: 데이터 exploration 와 insights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

### Dashboard Design Principles
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to 데이터 type
- **Use Color Strategically**: Highlight important information
- **Maintain Consistency**: Standardize formats 와 scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize 성능**: Fast loading, efficient queries
- **Mobile Considerations**: Responsive design

### Key 성능 Indicators (KPIs)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

## 고급 Analytics

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
- **A/B 테스트**: Experimental design, statistical significance
- **Multi-Armed Bandits**: Adaptive experimentation

### Text Analytics (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeling**: LDA, NMF 위한 theme discovery
- **Named Entity Recognition**: Identifying people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

## 데이터 Ethics 와 Governance

### 데이터 Privacy
- **GDPR**: EU General 데이터 Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability 와 Accountability Act (US 의료)
- **Anonymization**: Removing personally identifiable information
- **Differential Privacy**: Adding noise to protect individuals
- **Consent 관리**: Opt-에서/opt-out mechanisms

### 데이터 Quality
- **Accuracy**: Correctness 의 데이터
- **Completeness**: All required 데이터 present
- **Consistency**: No contradictions across sources
- **Timeliness**: 데이터 사용 가능 when needed
- **Validity**: Conforms to defined rules
- **Uniqueness**: No duplicates

### Bias 와 Fairness
- **Sampling Bias**: Non-representative 데이터 collection
- **Measurement Bias**: Flawed 데이터 collection instruments
- **Algorithmic Bias**: Discriminatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, 에서-processing, post-processing

### 데이터 Governance Framework
- **데이터 Stewardship**: Responsibility 위한 데이터 assets
- **Metadata 관리**: 데이터 about 데이터 documentation
- **데이터 Lineage**: Tracking 데이터 flow 와 transformations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logging 데이터 access 와 changes
- **Compliance**: Regulatory adherence

## Career Paths 에서 데이터 과학

### Roles
- **데이터 Analyst**: Focus on descriptive analytics, dashboards, reporting
- **데이터 Scientist**: Statistical modeling, 기계 학습, 고급 analytics
- **ML Engineer**: Production ML 시스템, model 배포, MLOps
- **데이터 Engineer**: 데이터 pipelines, infrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder 관리
- **BI Developer**: Dashboard creation, report 개발
- **Research Scientist**: Novel algorithms, publications, 고급 research

### Skills Matrix
- **Technical**: Python/R, SQL, 통계, ML frameworks, cloud platforms
- **Analytical**: Problem-solving, critical thinking, experimental design
- **의사소통**: Storytelling, visualization, presentation skills
- **비즈니스**: Domain knowledge, stakeholder 관리, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control 위한 models

## Emerging Trends

### Current Developments
- **AutoML**: Automated 기계 학습 pipeline creation
- **MLOps**: DevOps practices 위한 기계 학습
- **Feature Stores**: Centralized feature 관리
- **데이터 Mesh**: Decentralized 데이터 아키텍처
- **LLMs 와 Generative AI**: Large 언어 models, content generation
- **Edge Analytics**: Processing 데이터 at source devices
- **Real-Time Analytics**: Streaming 데이터 analysis
- **Augmented Analytics**: AI-assisted 데이터 preparation 와 insights

### 미래 Directions
- **Quantum 기계 학습**: Quantum 컴퓨팅 위한 ML
- **Federated Learning**: Training models across decentralized 데이터
- **Causal Inference**: Moving beyond correlation to causation
- **Responsible AI**: Ethics, explainability, transparency
- **데이터 Fabric**: Integrated 데이터 관리 across environments
