<!-- 
This file was automatically translated from English to Korean.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이 터 과 학 분석

# # Core Concepts

# ## What is 데이 터 과 학?
데이 터 과 학 is an terdisciplary field that uses scientific methods, processes, algorithms, 시스템 to extract knowledge sights from 구조화된 un구조화된 데이 터. It comb:
- **통계**: Mamatical foundation analysis
- **Computer 과 학**: Programm, algorithms, 데이 터 structures
- **Doma Expertise**: Subject matter knowledge
- **데이 터 Visualization**: Communicat fds effectively

# ## 데이 터 Types
- **Structured 데이 터**: Organized rows/columns (데이 터bases, spreadsheets)
- **Un구조화된 데이 터**: No predefed mat (text, images, audio, video)
- **Semi-구조화된 데이 터**: Some organization but not rigid (JSON, X기계 학습, HT기계 학습)
- **Time Series 데이 터**: Sequential 데이 터 pots dexed time order
- **Spatial 데이 터**: Geographic/location-based mation
- **Graph 데이 터**: Nodes edges represent relationships

# ## The 데이 터 과 학 Process (CRISP-DM)
1. **Buss Underst**: Defe objectives requirements
2. **데이 터 Underst**: Collect explore itial 데이 터
3. **데이 터 Preparation**: Clean, transm, mat 데이 터 (80% work)
4. **Model**: Select apply model techniques
5. **Evaluation**: Assess model permance 대조 objectives
6. **배포**: Implement model production 환경

# # 통계 기초

# ## Descriptive 통계
- **Measures Central Tendency**: Mean, median, mode
- **Measures Dispersion**: Range, variance, stard deviation, terquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles Quartiles**: Position 함께 distribution

# ## Inferential 통계
- **Hyposis Test**: Null hyposis, alternative hyposis, p-values
- **Confidence Intervals**: Range values likely conta population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (reject true null hyposis)
- **Type II Error**: False negative (fail to reject false null hyposis)
- **Power**: Probability correctly reject false null hyposis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Bomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count 이 벤트 fixed terval
- **Unim Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between 이 벤트
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical 데이 터 analysis

# ## Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test dependence categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Lear relationship between contuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

# # 데이 터 Collection Storage

# ## 데이 터 Sources
- **데이 터bases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, 웹 scrap
- **파일**: CSV, JSON, X기계 학습, Parquet, Avro
- **Stream 데이 터**: Kafka, Kis, real-time feeds
- **Surveys Experiments**: Primary 데이 터 collection
- **Public 데이 터sets**: Government 데이 터, Kaggle, academic repositories

# ## 데이 터 Warehous
- **ETL**: Extract, Transm, Load process
- **데이 터 Lake**: Raw 데이 터 storage native mat
- **데이 터 Warehouse**: Structured, processed 데이 터 analysis
- **데이 터 Mart**: Subset warehouse specific department
- **OLAP**: Onle Analytical Process, multidimensional queries
- **Star Schema**: Fact 표 surrounded by dimension 표
- **Snowflake Schema**: Normalized dimension 표

# ## 데이 터base Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassra, HBase (optimized columns)
- **Graph**: Neo4j, Amazon Neptune (nodes relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped 데이 터)
- **Vector**: Pecone, Milvus (embedd storage 기계 학습)

# # 데이 터 Preprocess

# ## 데이 터 Clean
- **Miss Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capp, transmation)
- **Duplicates**: Identification removal
- **Inconsistencies**: Stardiz mats, fix typos
- **데이 터 Validation**: Check constrats, ranges, types

# ## 데이 터 Transmation
- **Normalization**: Scal to 0-1 range
- **Stardization**: Z-score normalization (mean=0, std=1)
- **Encod**: One-hot, label, ordal, target encod
- **Bn**: Group contuous values 로 categories
- **Log Transmation**: Reduc skewness
- **Feature Scal**: Mak features comparable

# ## Feature Engeer
- **Feature Creation**: Deriv new features from exist ones
- **Feature Selection**: Choos most relevant features
 - Filter methods (correlation, chi-square)
 - Wrapper methods (recursive feature elimation)
 - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Comb features multiplicatively
- **Polynomial Features**: Creat higher-order terms

# # Exploratory 데이 터 Analysis (EDA)

# ## EDA Techniques
- **Summary 통계**: Describe central tendency, spread, shape
- **Univariate Analysis**: Sle variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable teractions
- **Correlation Analysis**: Identify relationships multicollearity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution sle variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two contuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Ch예술**: Categorical comparisons
- **Le Ch예술**: Trends over time
- **Viol Plots**: Distribution density 함께 box plot elements
- **Pair Plots**: Multiple scatter plots variable pairs

# ## Python Libraries EDA
- **pas**: 데이 터 manipulation analysis
- **numpy**: Numerical comput
- **matplotlib**: Basic plott
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific comput 통계

# # Mache Learn 데이 터 과 학

# ## Supervised Learn
- **Regression**: Predict contuous values
 - Lear Regression
 - Polynomial Regression
 - Ridge/LASSO/Elastic Net
 - Decision Tree Regressor
 - Rom Forest Regressor
 - Gradient Boost (XGBoost, LightGBM, CatBoost)
 
- **Classification**: Predict categorical labels
 - Logistic Regression
 - k-Nearest Neighbors
 - Naive Bayes
 - Support Vector Mach
 - Decision Trees
 - Rom Forest
 - Gradient Boost
 - 신경망

# ## Unsupervised Learn
- **Cluster**: Group similar observations
 - k-Means
 - Hierarchical Cluster
 - DBSCAN (density-based)
 - Gaussian Mixture Models
 - Spectral Cluster
 
- **Dimensionality Reduction**: Reduce feature count
 - Prcipal Component Analysis (PCA)
 - t-Distributed Stochastic Neighbor Embedd (t-SNE)
 - Unim Manifold Approximation (UMAP)
 - Autoencoders
 
- **Association Rules**: Fd co-occurr items
 - Apriori Algorithm
 - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tun**: Grid search, rom search, Bayesian optimization
- **Learn Curves**: Diagnose bias-variance tradef

# # Big 데이 터 Technologies

# ## Distributed Comput Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory process, faster than Hadoop
 - Spark SQL: Structured 데이 터 process
 - Spark Stream: Real-time 데이 터
 - 기계 학습lib: Mache learn library
 - GraphX: Graph process
- **Apache Flk**: Stream process 함께 low latency
- **Apache Beam**: Unified batch stream

# ## Cloud Platms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, 데이 터proc, 인공 지능 Platm, Cloud Storage
- **Azure**: Synapse 분석, 데이 터bricks, Mache Learn, 데이 터 Lake
- **Snowflake**: Cloud 데이 터 warehouse

# ## 데이 터 Pipele Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipele 관리 (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: 데이 터 orchestrator 함께 asset focus
- **dbt**: 데이 터 transmation warehouse

# # Buss Intelligence 분석

# ## BI Tools
- **Tableau**: Visual analytics platm
- **Power BI**: Microst buss analytics
- **Looker**: 데이 터 exploration sights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Prciples
- **Know Your Audience**: Tailor to 사용자 요구
- **Choose Right Visualizations**: Match chart to 데이 터 type
- **Use Color Strategically**: Highlight important mation
- **Mata Consistency**: Stardize mats scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Permance**: Fast load, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Permance Indicators (KPIs)
- **Fancial**: Revenue, prit marg, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Market**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # 고급 분석

# ## Predictive 분석
- **Forecast**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Model**: Credit scor, fraud detection, surance
- **Customer 분석**: Churn prediction, propensity model
- **Dem Forecast**: Inventory optimization, supply cha
- **Matenance Prediction**: Equipment failure anticipation

# ## Prescriptive 분석
- **Optimization**: Lear programm, teger programm
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, fluence 다이 어램
- **A/B Test**: Experimental design, statistical significance
- **Multi-Armed Bits**: Adaptive experimentation

# ## Text 분석 (NLP)
- **Text Preprocess**: Tokenization, stemm, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Model**: LDA, NMF me discovery
- **Named Entity Recognition**: Identify people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embedds**: Word2Vec, GloVe, BERT

# # 데이 터 Ethics Governance

# ## 데이 터 Privacy
- **GDPR**: EU General 데이 터 Protection Regulation
- **CCPA**: Calinia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability Accountability Act (US 료)
- **Anonymization**: Remov personally identifiable mation
- **Differential Privacy**: Add noise to protect dividuals
- **Consent 관리**: Opt-/opt-out mechanisms

# ## 데이 터 Quality
- **Accuracy**: Correctness 데이 터
- **Completeness**: All required 데이 터 present
- **Consistency**: No contradictions across sources
- **Timels**: 데이 터 available when needed
- **Validity**: Conms to defed rules
- **Uniqueness**: No duplicates

# ## Bias Fairness
- **Sampl Bias**: Non-representative 데이 터 collection
- **Measurement Bias**: F법률ed 데이 터 collection struments
- **Algorithmic Bias**: Discrimatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-process, -process, post-process

# ## 데이 터 Governance Framework
- **데이 터 Stewardship**: Responsibility 데이 터 assets
- **Meta데이 터 관리**: 데이 터 about 데이 터 documentation
- **데이 터 Leage**: Track 데이 터 flow transmations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logg 데이 터 access changes
- **Compliance**: Regulatory adherence

# # Career Paths 데이 터 과 학

# ## Roles
- **데이 터 Analyst**: Focus on descriptive analytics, dashboards, report
- **데이 터 Scientist**: Statistical model, mache learn, 고급 analytics
- **기계 학습 Engeer**: Production 기계 학습 시스템, model 배포, 기계 학습Ops
- **데이 터 Engeer**: 데이 터 pipel, frastructure, ETL processes
- **분석 Manager**: Team leadership, strategy, stakeholder 관리
- **BI Developer**: Dashboard creation, report 개발
- **Research Scientist**: Novel algorithms, publications, 고급 research

# ## Skills Matrix
- **Technical**: Python/R, SQL, 통계, 기계 학습 frameworks, 클라우드 platms
- **Analytical**: Problem-solv, critical thk, experimental design
- **사소통**: Storytell, visualization, presentation skills
- **Buss**: Doma knowledge, stakeholder 관리, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control models

# # Emerg Trends

# ## Current 개발s
- **Auto기계 학습**: Automated mache learn pipele creation
- **기계 학습Ops**: DevOps practices mache learn
- **Feature Stores**: Centralized feature 관리
- **데이 터 Mesh**: Decentralized 데이 터 아키텍처
- **대규모 언어 모델 Generative 인공 지능**: Large 언어 models, 콘텐츠 generation
- **Edge 분석**: Process 데이 터 at source devices
- **Real-Time 분석**: Stream 데이 터 analysis
- **Augmented 분석**: 인공 지능-assisted 데이 터 preparation sights

# ## 미래 Directions
- **Quantum Mache Learn**: Quantum comput 기계 학습
- **Federated Learn**: Tra models across decentralized 데이 터
- **Causal Inference**: Mov beyond correlation to causation
- **Responsible 인공 지능**: Ethics, explaability, transparency
- **데이 터 Fabric**: Integrated 데이 터 관리 across 환경s
