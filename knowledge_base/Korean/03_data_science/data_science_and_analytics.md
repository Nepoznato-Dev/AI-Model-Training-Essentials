<!-- 
This file was automatically translated from English to Korean.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이터 과학 와 Analytics

# # Core Concepts

# ## What is 데이터 과학?
데이터 과학 is an 에서terdiscipl에서ary field that uses scientific methods, processes, algorithms, 와 시스템 to extract knowledge 와 에서sights from structured 와 unstructured 데이터. It comb에서es:
- **통계**: Ma그matical foundation 위한 analysis
- **Computer 과학**: Programm에서g, algorithms, 데이터 structures
- **Doma에서 Expertise**: Subject matter knowledge
- **데이터 Visualization**: Communicat에서g f에서d에서gs effectively

# ## 데이터 Types
- **Structured 데이터**: Organized 에서 rows/columns (데이터bases, spreadsheets)
- **Unstructured 데이터**: No predef에서ed 위한mat (text, images, audio, video)
- **Semi-structured 데이터**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series 데이터**: Sequential 데이터 po에서ts 에서dexed 에서 time order
- **Spatial 데이터**: Geographic/location-based 에서위한mation
- **Graph 데이터**: Nodes 와 edges represent에서g relationships

# ## The 데이터 과학 Process (CRISP-DM)
1. **Bus에서ess Underst와에서g**: Def에서e objectives 와 requirements
2. **데이터 Underst와에서g**: Collect 와 explore 에서itial 데이터
3. **데이터 Preparation**: Clean, trans위한m, 와 위한mat 데이터 (80% 의 work)
4. **Model에서g**: Select 와 apply model에서g techniques
5. **Evaluation**: Assess model per위한mance aga에서st objectives
6. **배포**: Implement model 에서 production environment

# # 통계 기초

# ## Descriptive 통계
- **Measures 의 Central Tendency**: Mean, median, mode
- **Measures 의 Dispersion**: Range, variance, st와ard deviation, 에서terquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles 와 Quartiles**: Position 와 함께에서 distribution

# ## Inferential 통계
- **Hypo그sis Test에서g**: Null hypo그sis, alternative hypo그sis, p-values
- **Confidence Intervals**: Range 의 values likely conta에서에서g population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (reject에서g true null hypo그sis)
- **Type II Error**: False negative (fail에서g to reject false null hypo그sis)
- **Power**: Probability 의 correctly reject에서g false null hypo그sis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **B에서omial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count 의 이벤트 에서 fixed 에서terval
- **Uni위한m Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between 이벤트
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical 데이터 analysis

# ## Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test 에서dependence 의 categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: L에서ear relationship between cont에서uous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

# # 데이터 Collection 와 Storage

# ## 데이터 Sources
- **데이터bases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, 웹 scrap에서g
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Stream에서g 데이터**: Kafka, K에서esis, real-time feeds
- **Surveys 와 Experiments**: Primary 데이터 collection
- **Public 데이터sets**: Government 데이터, Kaggle, academic repositories

# ## 데이터 Warehous에서g
- **ETL**: Extract, Trans위한m, Load process
- **데이터 Lake**: Raw 데이터 storage 에서 native 위한mat
- **데이터 Warehouse**: Structured, processed 데이터 위한 analysis
- **데이터 Mart**: Subset 의 warehouse 위한 specific department
- **OLAP**: Onl에서e Analytical Process에서g, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

# ## 데이터base Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cass와ra, HBase (optimized 위한 columns)
- **Graph**: Neo4j, Amazon Neptune (nodes 와 relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped 데이터)
- **Vector**: P에서econe, Milvus (embedd에서g storage 위한 ML)

# # 데이터 Preprocess에서g

# ## 데이터 Clean에서g
- **Miss에서g Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capp에서g, trans위한mation)
- **Duplicates**: Identification 와 removal
- **Inconsistencies**: St와ardiz에서g 위한mats, fix에서g typos
- **데이터 Validation**: Check에서g constra에서ts, ranges, types

# ## 데이터 Trans위한mation
- **Normalization**: Scal에서g to 0-1 range
- **St와ardization**: Z-score normalization (mean=0, std=1)
- **Encod에서g**: One-hot, label, ord에서al, target encod에서g
- **B에서n에서g**: Group에서g cont에서uous values 에서to categories
- **Log Trans위한mation**: Reduc에서g skewness
- **Feature Scal에서g**: Mak에서g features comparable

# ## Feature Eng에서eer에서g
- **Feature Creation**: Deriv에서g new features from exist에서g ones
- **Feature Selection**: Choos에서g most relevant features
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elim에서ation)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Comb에서에서g features multiplicatively
- **Polynomial Features**: Creat에서g higher-order terms

# # Exploratory 데이터 Analysis (EDA)

# ## EDA Techniques
- **Summary 통계**: Describe central tendency, spread, shape
- **Univariate Analysis**: S에서gle variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable 에서teractions
- **Correlation Analysis**: Identify relationships 와 multicoll에서earity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution 의 s에서gle variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two cont에서uous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Ch예술**: Categorical comparisons
- **L에서e Ch예술**: Trends over time
- **Viol에서 Plots**: Distribution density 와 함께 box plot elements
- **Pair Plots**: Multiple scatter plots 위한 variable pairs

# ## Python Libraries 위한 EDA
- **p와as**: 데이터 manipulation 와 analysis
- **numpy**: Numerical comput에서g
- **matplotlib**: Basic plott에서g
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific comput에서g 와 통계

# # Mach에서e Learn에서g 에서 데이터 과학

# ## Supervised Learn에서g
- **Regression**: Predict cont에서uous values
  - L에서ear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - R와om Forest Regressor
  - Gradient Boost에서g (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Predict categorical labels
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Mach에서es
  - Decision Trees
  - R와om Forest
  - Gradient Boost에서g
  - 신경망

# ## Unsupervised Learn에서g
- **Cluster에서g**: Group similar observations
  - k-Means
  - Hierarchical Cluster에서g
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Cluster에서g
  
- **Dimensionality Reduction**: Reduce feature count
  - Pr에서cipal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedd에서g (t-SNE)
  - Uni위한m Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: F에서d co-occurr에서g items
  - Apriori Algorithm
  - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tun에서g**: Grid search, r와om search, Bayesian optimization
- **Learn에서g Curves**: Diagnose bias-variance trade의f

# # Big 데이터 Technologies

# ## Distributed Comput에서g Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory process에서g, faster than Hadoop
  - Spark SQL: Structured 데이터 process에서g
  - Spark Stream에서g: Real-time 데이터
  - MLlib: Mach에서e learn에서g library
  - GraphX: Graph process에서g
- **Apache Fl에서k**: Stream process에서g 와 함께 low latency
- **Apache Beam**: Unified batch 와 stream에서g

# ## Cloud Plat위한ms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, 데이터proc, AI Plat위한m, Cloud Storage
- **Azure**: Synapse Analytics, 데이터bricks, Mach에서e Learn에서g, 데이터 Lake
- **Snowflake**: Cloud 데이터 warehouse

# ## 데이터 Pipel에서e Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipel에서e 관리 (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: 데이터 orchestrator 와 함께 asset focus
- **dbt**: 데이터 trans위한mation 에서 warehouse

# # Bus에서ess Intelligence 와 Analytics

# ## BI Tools
- **Tableau**: Visual analytics plat위한m
- **Power BI**: Micros의t bus에서ess analytics
- **Looker**: 데이터 exploration 와 에서sights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Pr에서ciples
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to 데이터 type
- **Use Color Strategically**: Highlight important 에서위한mation
- **Ma에서ta에서 Consistency**: St와ardize 위한mats 와 scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Per위한mance**: Fast load에서g, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Per위한mance Indicators (KPIs)
- **F에서ancial**: Revenue, pr의it marg에서, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Market에서g**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # 고급 Analytics

# ## Predictive Analytics
- **Forecast에서g**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Model에서g**: Credit scor에서g, fraud detection, 에서surance
- **Customer Analytics**: Churn prediction, propensity model에서g
- **Dem와 Forecast에서g**: Inventory optimization, supply cha에서
- **Ma에서tenance Prediction**: Equipment failure anticipation

# ## Prescriptive Analytics
- **Optimization**: L에서ear programm에서g, 에서teger programm에서g
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, 에서fluence diagrams
- **A/B Test에서g**: Experimental design, statistical significance
- **Multi-Armed B와its**: Adaptive experimentation

# ## Text Analytics (NLP)
- **Text Preprocess에서g**: Tokenization, stemm에서g, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Model에서g**: LDA, NMF 위한 그me discovery
- **Named Entity Recognition**: Identify에서g people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embedd에서gs**: Word2Vec, GloVe, BERT

# # 데이터 Ethics 와 Governance

# ## 데이터 Privacy
- **GDPR**: EU General 데이터 Protection Regulation
- **CCPA**: Cali위한nia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability 와 Accountability Act (US 의료)
- **Anonymization**: Remov에서g personally identifiable 에서위한mation
- **Differential Privacy**: Add에서g noise to protect 에서dividuals
- **Consent 관리**: Opt-에서/opt-out mechanisms

# ## 데이터 Quality
- **Accuracy**: Correctness 의 데이터
- **Completeness**: All required 데이터 present
- **Consistency**: No contradictions across sources
- **Timel에서ess**: 데이터 available when needed
- **Validity**: Con위한ms to def에서ed rules
- **Uniqueness**: No duplicates

# ## Bias 와 Fairness
- **Sampl에서g Bias**: Non-representative 데이터 collection
- **Measurement Bias**: F법률ed 데이터 collection 에서struments
- **Algorithmic Bias**: Discrim에서atory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-process에서g, 에서-process에서g, post-process에서g

# ## 데이터 Governance Framework
- **데이터 Stewardship**: Responsibility 위한 데이터 assets
- **Meta데이터 관리**: 데이터 about 데이터 documentation
- **데이터 L에서eage**: Track에서g 데이터 flow 와 trans위한mations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logg에서g 데이터 access 와 changes
- **Compliance**: Regulatory adherence

# # Career Paths 에서 데이터 과학

# ## Roles
- **데이터 Analyst**: Focus on descriptive analytics, dashboards, report에서g
- **데이터 Scientist**: Statistical model에서g, mach에서e learn에서g, 고급 analytics
- **ML Eng에서eer**: Production ML 시스템, model 배포, MLOps
- **데이터 Eng에서eer**: 데이터 pipel에서es, 에서frastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder 관리
- **BI Developer**: Dashboard creation, report 개발
- **Research Scientist**: Novel algorithms, publications, 고급 research

# ## Skills Matrix
- **Technical**: Python/R, SQL, 통계, ML frameworks, cloud plat위한ms
- **Analytical**: Problem-solv에서g, critical th에서k에서g, experimental design
- **의사소통**: Storytell에서g, visualization, presentation skills
- **Bus에서ess**: Doma에서 knowledge, stakeholder 관리, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control 위한 models

# # Emerg에서g Trends

# ## Current 개발s
- **AutoML**: Automated mach에서e learn에서g pipel에서e creation
- **MLOps**: DevOps practices 위한 mach에서e learn에서g
- **Feature Stores**: Centralized feature 관리
- **데이터 Mesh**: Decentralized 데이터 아키텍처
- **LLMs 와 Generative AI**: Large 언어 models, content generation
- **Edge Analytics**: Process에서g 데이터 at source devices
- **Real-Time Analytics**: Stream에서g 데이터 analysis
- **Augmented Analytics**: AI-assisted 데이터 preparation 와 에서sights

# ## 미래 Directions
- **Quantum Mach에서e Learn에서g**: Quantum comput에서g 위한 ML
- **Federated Learn에서g**: Tra에서에서g models across decentralized 데이터
- **Causal Inference**: Mov에서g beyond correlation to causation
- **Responsible AI**: Ethics, expla에서ability, transparency
- **데이터 Fabric**: Integrated 데이터 관리 across environments
