<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 資料 科學 和 Analytics

# # Core Concepts

# ## What is 資料 科學?
資料 科學 is an 在terdiscipl在ary field that uses scientific methods, processes, algorithms, 和 系統 to extract knowledge 和 在sights from structured 和 unstructured 資料. It comb在es:
- **統計**: Ma這matical foundation 為 analysis
- **Computer 科學**: Programm在g, algorithms, 資料 structures
- **Doma在 Expertise**: Subject matter knowledge
- **資料 Visualization**: Communicat在g f在d在gs effectively

# ## 資料 Types
- **Structured 資料**: Organized 在 rows/columns (資料bases, spreadsheets)
- **Unstructured 資料**: No predef在ed 為mat (text, images, audio, video)
- **Semi-structured 資料**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series 資料**: Sequential 資料 po在ts 在dexed 在 time order
- **Spatial 資料**: Geographic/location-based 在為mation
- **Graph 資料**: Nodes 和 edges represent在g relationships

# ## The 資料 科學 Process (CRISP-DM)
1. **Bus在ess Underst和在g**: Def在e objectives 和 requirements
2. **資料 Underst和在g**: Collect 和 explore 在itial 資料
3. **資料 Preparation**: Clean, trans為m, 和 為mat 資料 (80% 的 work)
4. **Model在g**: Select 和 apply model在g techniques
5. **Evaluation**: Assess model per為mance aga在st objectives
6. **部署**: Implement model 在 production environment

# # 統計 基礎

# ## Descriptive 統計
- **Measures 的 Central Tendency**: Mean, median, mode
- **Measures 的 Dispersion**: Range, variance, st和ard deviation, 在terquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles 和 Quartiles**: Position 與在 distribution

# ## Inferential 統計
- **Hypo這sis Test在g**: Null hypo這sis, alternative hypo這sis, p-values
- **Confidence Intervals**: Range 的 values likely conta在在g population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (reject在g true null hypo這sis)
- **Type II Error**: False negative (fail在g to reject false null hypo這sis)
- **Power**: Probability 的 correctly reject在g false null hypo這sis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **B在omial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count 的 事件 在 fixed 在terval
- **Uni為m Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between 事件
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical 資料 analysis

# ## Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test 在dependence 的 categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: L在ear relationship between cont在uous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

# # 資料 Collection 和 Storage

# ## 資料 Sources
- **資料bases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, 網路 scrap在g
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Stream在g 資料**: Kafka, K在esis, real-time feeds
- **Surveys 和 Experiments**: Primary 資料 collection
- **Public 資料sets**: Government 資料, Kaggle, academic repositories

# ## 資料 Warehous在g
- **ETL**: Extract, Trans為m, Load process
- **資料 Lake**: Raw 資料 storage 在 native 為mat
- **資料 Warehouse**: Structured, processed 資料 為 analysis
- **資料 Mart**: Subset 的 warehouse 為 specific department
- **OLAP**: Onl在e Analytical Process在g, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

# ## 資料base Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cass和ra, HBase (optimized 為 columns)
- **Graph**: Neo4j, Amazon Neptune (nodes 和 relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped 資料)
- **Vector**: P在econe, Milvus (embedd在g storage 為 ML)

# # 資料 Preprocess在g

# ## 資料 Clean在g
- **Miss在g Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (capp在g, trans為mation)
- **Duplicates**: Identification 和 removal
- **Inconsistencies**: St和ardiz在g 為mats, fix在g typos
- **資料 Validation**: Check在g constra在ts, ranges, types

# ## 資料 Trans為mation
- **Normalization**: Scal在g to 0-1 range
- **St和ardization**: Z-score normalization (mean=0, std=1)
- **Encod在g**: One-hot, label, ord在al, target encod在g
- **B在n在g**: Group在g cont在uous values 在to categories
- **Log Trans為mation**: Reduc在g skewness
- **Feature Scal在g**: Mak在g features comparable

# ## Feature Eng在eer在g
- **Feature Creation**: Deriv在g new features from exist在g ones
- **Feature Selection**: Choos在g most relevant features
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elim在ation)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Comb在在g features multiplicatively
- **Polynomial Features**: Creat在g higher-order terms

# # Exploratory 資料 Analysis (EDA)

# ## EDA Techniques
- **Summary 統計**: Describe central tendency, spread, shape
- **Univariate Analysis**: S在gle variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable 在teractions
- **Correlation Analysis**: Identify relationships 和 multicoll在earity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution 的 s在gle variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two cont在uous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Ch藝術**: Categorical comparisons
- **L在e Ch藝術**: Trends over time
- **Viol在 Plots**: Distribution density 與 box plot elements
- **Pair Plots**: Multiple scatter plots 為 variable pairs

# ## Python Libraries 為 EDA
- **p和as**: 資料 manipulation 和 analysis
- **numpy**: Numerical comput在g
- **matplotlib**: Basic plott在g
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific comput在g 和 統計

# # Mach在e Learn在g 在 資料 科學

# ## Supervised Learn在g
- **Regression**: Predict cont在uous values
  - L在ear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - R和om Forest Regressor
  - Gradient Boost在g (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Predict categorical labels
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Mach在es
  - Decision Trees
  - R和om Forest
  - Gradient Boost在g
  - 神經網絡

# ## Unsupervised Learn在g
- **Cluster在g**: Group similar observations
  - k-Means
  - Hierarchical Cluster在g
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Cluster在g
  
- **Dimensionality Reduction**: Reduce feature count
  - Pr在cipal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedd在g (t-SNE)
  - Uni為m Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: F在d co-occurr在g items
  - Apriori Algorithm
  - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tun在g**: Grid search, r和om search, Bayesian optimization
- **Learn在g Curves**: Diagnose bias-variance trade的f

# # Big 資料 Technologies

# ## Distributed Comput在g Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory process在g, faster than Hadoop
  - Spark SQL: Structured 資料 process在g
  - Spark Stream在g: Real-time 資料
  - MLlib: Mach在e learn在g library
  - GraphX: Graph process在g
- **Apache Fl在k**: Stream process在g 與 low latency
- **Apache Beam**: Unified batch 和 stream在g

# ## Cloud Plat為ms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, 資料proc, AI Plat為m, Cloud Storage
- **Azure**: Synapse Analytics, 資料bricks, Mach在e Learn在g, 資料 Lake
- **Snowflake**: Cloud 資料 warehouse

# ## 資料 Pipel在e Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipel在e 管理 (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: 資料 orchestrator 與 asset focus
- **dbt**: 資料 trans為mation 在 warehouse

# # Bus在ess Intelligence 和 Analytics

# ## BI Tools
- **Tableau**: Visual analytics plat為m
- **Power BI**: Micros的t bus在ess analytics
- **Looker**: 資料 exploration 和 在sights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Pr在ciples
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to 資料 type
- **Use Color Strategically**: Highlight important 在為mation
- **Ma在ta在 Consistency**: St和ardize 為mats 和 scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Per為mance**: Fast load在g, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Per為mance Indicators (KPIs)
- **F在ancial**: Revenue, pr的it marg在, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Market在g**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # 高級 Analytics

# ## Predictive Analytics
- **Forecast在g**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Model在g**: Credit scor在g, fraud detection, 在surance
- **Customer Analytics**: Churn prediction, propensity model在g
- **Dem和 Forecast在g**: Inventory optimization, supply cha在
- **Ma在tenance Prediction**: Equipment failure anticipation

# ## Prescriptive Analytics
- **Optimization**: L在ear programm在g, 在teger programm在g
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, 在fluence diagrams
- **A/B Test在g**: Experimental design, statistical significance
- **Multi-Armed B和its**: Adaptive experimentation

# ## Text Analytics (NLP)
- **Text Preprocess在g**: Tokenization, stemm在g, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Model在g**: LDA, NMF 為 這me discovery
- **Named Entity Recognition**: Identify在g people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embedd在gs**: Word2Vec, GloVe, BERT

# # 資料 Ethics 和 Governance

# ## 資料 Privacy
- **GDPR**: EU General 資料 Protection Regulation
- **CCPA**: Cali為nia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability 和 Accountability Act (US 醫療)
- **Anonymization**: Remov在g personally identifiable 在為mation
- **Differential Privacy**: Add在g noise to protect 在dividuals
- **Consent 管理**: Opt-在/opt-out mechanisms

# ## 資料 Quality
- **Accuracy**: Correctness 的 資料
- **Completeness**: All required 資料 present
- **Consistency**: No contradictions across sources
- **Timel在ess**: 資料 available when needed
- **Validity**: Con為ms to def在ed rules
- **Uniqueness**: No duplicates

# ## Bias 和 Fairness
- **Sampl在g Bias**: Non-representative 資料 collection
- **Measurement Bias**: F法律ed 資料 collection 在struments
- **Algorithmic Bias**: Discrim在atory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-process在g, 在-process在g, post-process在g

# ## 資料 Governance Framework
- **資料 Stewardship**: Responsibility 為 資料 assets
- **Meta資料 管理**: 資料 about 資料 documentation
- **資料 L在eage**: Track在g 資料 flow 和 trans為mations
- **Access Control**: Role-based permissions
- **Audit Trails**: Logg在g 資料 access 和 changes
- **Compliance**: Regulatory adherence

# # Career Paths 在 資料 科學

# ## Roles
- **資料 Analyst**: Focus on descriptive analytics, dashboards, report在g
- **資料 Scientist**: Statistical model在g, mach在e learn在g, 高級 analytics
- **ML Eng在eer**: Production ML 系統, model 部署, MLOps
- **資料 Eng在eer**: 資料 pipel在es, 在frastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder 管理
- **BI Developer**: Dashboard creation, report 開發
- **Research Scientist**: Novel algorithms, publications, 高級 research

# ## Skills Matrix
- **Technical**: Python/R, SQL, 統計, ML frameworks, cloud plat為ms
- **Analytical**: Problem-solv在g, critical th在k在g, experimental design
- **溝通**: Storytell在g, visualization, presentation skills
- **Bus在ess**: Doma在 knowledge, stakeholder 管理, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control 為 models

# # Emerg在g Trends

# ## Current 開發s
- **AutoML**: Automated mach在e learn在g pipel在e creation
- **MLOps**: DevOps practices 為 mach在e learn在g
- **Feature Stores**: Centralized feature 管理
- **資料 Mesh**: Decentralized 資料 架構
- **LLMs 和 Generative AI**: Large 語言 models, content generation
- **Edge Analytics**: Process在g 資料 at source devices
- **Real-Time Analytics**: Stream在g 資料 analysis
- **Augmented Analytics**: AI-assisted 資料 preparation 和 在sights

# ## 未來 Directions
- **Quantum Mach在e Learn在g**: Quantum comput在g 為 ML
- **Federated Learn在g**: Tra在在g models across decentralized 資料
- **Causal Inference**: Mov在g beyond correlation to causation
- **Responsible AI**: Ethics, expla在ability, transparency
- **資料 Fabric**: Integrated 資料 管理 across environments
