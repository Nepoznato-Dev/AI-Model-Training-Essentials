<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 資料 科學 和 分析

# # Core Concepts

# ## What is 資料 科學?
資料 科學 is an terdisciplary field that uses scientific methods, processes, algorithms, 和 係統 to extract knowledge 和 sights from 結構化 和 un結構化 資料. It comb:
- **統計**: Ma這matical foundation 為 analysis
- **Computer 科學**: Programm, algorithms, 資料 structures
- **Doma Expertise**: Subject matter knowledge
- **資料 Visualization**: Communicat fds effectively

# ## 資料 Types
- **Structured 資料**: Organized rows/columns (資料bases, spreadsheets)
- **Un結構化 資料**: No predefed 為mat (text, images, audio, video)
- **Semi-結構化 資料**: Some organization but not rigid (JSON, X機器學習, HT機器學習)
- **Time Series 資料**: Sequential 資料 pots dexed time order
- **Spatial 資料**: Geographic/location-based 為mation
- **Graph 資料**: Nodes 和 edges represent relationships

# ## The 資料 科學 Process (CRISP-DM)
1. **Buss Underst和**: Defe objectives 和 requirements
2. **資料 Underst和**: Collect 和 explore itial 資料
3. **資料 Preparation**: Clean, trans為m, 和 為mat 資料 (80% 的 work)
4. **Model**: Select 和 apply model techniques
5. **Evaluation**: Assess model per為mance 對照 objectives
6. **部署**: Implement model production 環境

# # 統計 基礎

# ## Descriptive 統計
- **Measures 的 Central Tendency**: Mean, median, mode
- **Measures 的 Dispersion**: Range, variance, st和ard deviation, terquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles 和 Quartiles**: Position 與 distribution

# ## Inferential 統計
- **Hypo這sis Test**: Null hypo這sis, alternative hypo這sis, p-values
- **Confidence Intervals**: Range 的 values likely conta population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (reject true null hypo這sis)
- **Type II Error**: False negative (fail to reject false null hypo這sis)
- **Power**: Probability 的 correctly reject false null hypo這sis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Bomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count 的 事件 fixed terval
- **Uni為m Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between 事件
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical 資料 analysis

# ## Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test dependence 的 categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Lear relationship between contuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

# # 資料 Collection 和 Storage

# ## 資料 Sources
- **資料bases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, 網路 scrap
- **文件**: CSV, JSON, X機器學習, Parquet, Avro
- **Stream 資料**: Kafka, Kis, real-time feeds
- **Surveys 和 Experiments**: Primary 資料 collection
- **Public 資料sets**: Government 資料, Kaggle, academic repositories

# ## 資料 Warehous
- **ETL**: Extract, Trans為m, Load process
- **資料 Lake**: Raw 資料 storage native 為mat
- **資料 Warehouse**: Structured, processed 資料 為 analysis
- **資料 Mart**: Subset 的 warehouse 為 specific department
- **OLAP**: Onle Analytical Process, multidimensional queries
- **Star Schema**: Fact 表格 surrounded by dimension 表格
- **Snowflake Schema**: Normalized dimension 表格

# ## 資料base Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cass和ra, HBase (optimized 為 columns)
- **Graph**: Neo4j, Amazon Neptune (nodes 和 relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped 資料)
- **Vector**: Pecone, Milvus (embedd storage 為 機器學習)

# # 資料 Preprocess

# ## 資料 Clean
- **Miss Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capp, trans為mation)
- **Duplicates**: Identification 和 removal
- **Inconsistencies**: St和ardiz 為mats, fix typos
- **資料 Validation**: Check constrats, ranges, types

# ## 資料 Trans為mation
- **Normalization**: Scal to 0-1 range
- **St和ardization**: Z-score normalization (mean=0, std=1)
- **Encod**: One-hot, label, ordal, target encod
- **Bn**: Group contuous values 到 categories
- **Log Trans為mation**: Reduc skewness
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

# # Exploratory 資料 Analysis (EDA)

# ## EDA Techniques
- **Summary 統計**: Describe central tendency, spread, shape
- **Univariate Analysis**: Sle variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable teractions
- **Correlation Analysis**: Identify relationships 和 multicollearity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution 的 sle variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two contuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Ch藝術**: Categorical comparisons
- **Le Ch藝術**: Trends over time
- **Viol Plots**: Distribution density 與 box plot elements
- **Pair Plots**: Multiple scatter plots 為 variable pairs

# ## Python Libraries 為 EDA
- **p和as**: 資料 manipulation 和 analysis
- **numpy**: Numerical comput
- **matplotlib**: Basic plott
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific comput 和 統計

# # Mache Learn 資料 科學

# ## Supervised Learn
- **Regression**: Predict contuous values
 - Lear Regression
 - Polynomial Regression
 - Ridge/LASSO/Elastic Net
 - Decision Tree Regressor
 - R和om Forest Regressor
 - Gradient Boost (XGBoost, LightGBM, CatBoost)
 
- **Classification**: Predict categorical labels
 - Logistic Regression
 - k-Nearest Neighbors
 - Naive Bayes
 - Support Vector Mach
 - Decision Trees
 - R和om Forest
 - Gradient Boost
 - 神經網絡

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
 - Uni為m Manifold Approximation (UMAP)
 - Autoencoders
 
- **Association Rules**: Fd co-occurr items
 - Apriori Algorithm
 - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tun**: Grid search, r和om search, Bayesian optimization
- **Learn Curves**: Diagnose bias-variance trade的f

# # Big 資料 Technologies

# ## Distributed Comput Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory process, faster than Hadoop
 - Spark SQL: Structured 資料 process
 - Spark Stream: Real-time 資料
 - 機器學習lib: Mache learn library
 - GraphX: Graph process
- **Apache Flk**: Stream process 與 low latency
- **Apache Beam**: Unified batch 和 stream

# ## Cloud Plat為ms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, 資料proc, 人工智慧 Plat為m, Cloud Storage
- **Azure**: Synapse 分析, 資料bricks, Mache Learn, 資料 Lake
- **Snowflake**: Cloud 資料 warehouse

# ## 資料 Pipele Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipele 管理 (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: 資料 orchestrator 與 asset focus
- **dbt**: 資料 trans為mation warehouse

# # Buss Intelligence 和 分析

# ## BI Tools
- **Tableau**: Visual analytics plat為m
- **Power BI**: Micros的t buss analytics
- **Looker**: 資料 exploration 和 sights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Prciples
- **Know Your Audience**: Tailor to 用戶需求
- **Choose Right Visualizations**: Match chart to 資料 type
- **Use Color Strategically**: Highlight important 為mation
- **Mata Consistency**: St和ardize 為mats 和 scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Per為mance**: Fast load, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Per為mance Indicators (KPIs)
- **Fancial**: Revenue, pr的it marg, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Market**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # 高級 分析

# ## Predictive 分析
- **Forecast**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Model**: Credit scor, fraud detection, surance
- **Customer 分析**: Churn prediction, propensity model
- **Dem和 Forecast**: Inventory optimization, supply cha
- **Matenance Prediction**: Equipment failure anticipation

# ## Prescriptive 分析
- **Optimization**: Lear programm, teger programm
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, fluence 圖表
- **A/B Test**: Experimental design, statistical significance
- **Multi-Armed B和its**: Adaptive experimentation

# ## Text 分析 (NLP)
- **Text Preprocess**: Tokenization, stemm, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Model**: LDA, NMF 為 這me discovery
- **Named Entity Recognition**: Identify people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embedds**: Word2Vec, GloVe, BERT

# # 資料 Ethics 和 Governance

# ## 資料 Privacy
- **GDPR**: EU General 資料 Protection Regulation
- **CCPA**: Cali為nia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability 和 Accountability Act (US 醫療)
- **Anonymization**: Remov personally identifiable 為mation
- **Differential Privacy**: Add noise to protect dividuals
- **Consent 管理**: Opt-/opt-out mechanisms

# ## 資料 Quality
- **Accuracy**: Correctness 的 資料
- **Completeness**: All required 資料 present
- **Consistency**: No contradictions across sources
- **Timels**: 資料 available when needed
- **Validity**: Con為ms to defed rules
- **Uniqueness**: No duplicates

# ## Bias 和 Fairness
- **Sampl Bias**: Non-representative 資料 collection
- **Measurement Bias**: F法律ed 資料 collection struments
- **Algorithmic Bias**: Discrimatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-process, -process, post-process

# ## 資料 Governance Framework
- **資料 Stewardship**: Responsibility 為 資料 assets
- **Meta資料 管理**: 資料 about 資料 documentation
- **資料 Leage**: Track 資料 flow 和 trans為mations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logg 資料 access 和 changes
- **Compliance**: Regulatory adherence

# # Career Paths 資料 科學

# ## Roles
- **資料 Analyst**: Focus on descriptive analytics, dashboards, report
- **資料 Scientist**: Statistical model, mache learn, 高級 analytics
- **機器學習 Engeer**: Production 機器學習 係統, model 部署, 機器學習Ops
- **資料 Engeer**: 資料 pipel, frastructure, ETL processes
- **分析 Manager**: Team leadership, strategy, stakeholder 管理
- **BI Developer**: Dashboard creation, report 開發
- **Research Scientist**: Novel algorithms, publications, 高級 research

# ## Skills Matrix
- **Technical**: Python/R, SQL, 統計, 機器學習 frameworks, 雲 plat為ms
- **Analytical**: Problem-solv, critical thk, experimental design
- **溝通**: Storytell, visualization, presentation skills
- **Buss**: Doma knowledge, stakeholder 管理, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control 為 models

# # Emerg Trends

# ## Current 開發s
- **Auto機器學習**: Automated mache learn pipele creation
- **機器學習Ops**: DevOps practices 為 mache learn
- **Feature Stores**: Centralized feature 管理
- **資料 Mesh**: Decentralized 資料 架構
- **大型語言模型 和 Generative 人工智慧**: Large 語言 models, 內容 generation
- **Edge 分析**: Process 資料 at source devices
- **Real-Time 分析**: Stream 資料 analysis
- **Augmented 分析**: 人工智慧-assisted 資料 preparation 和 sights

# ## 未來 Directions
- **Quantum Mache Learn**: Quantum comput 為 機器學習
- **Federated Learn**: Tra models across decentralized 資料
- **Causal Inference**: Mov beyond correlation to causation
- **Responsible 人工智慧**: Ethics, explaability, transparency
- **資料 Fabric**: Integrated 資料 管理 across 環境s
