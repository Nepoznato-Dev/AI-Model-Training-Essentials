<!-- 
This file was automatically translated from English to Turkish.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Veri Bilim ve Analytics

# # Core Concepts

# ## What is Veri Bilim?
Veri bilim is an içiçindedeterdiscipliçiçindedeary field that uses scientific methods, processes, algorithms, ve sistemler to extract knowledge ve içiçindedesights from structured ve unstructured veri. It combiçiçindedees:
- **İstatistikler**: Mabumatical foundation için analysis
- **Computer Bilim**: Programmİçinde, algorithms, veri structures
- **Domaiçiçindede Expertise**: Subject matter knowledge
- **Veri Visualization**: Communicatİçinde fiçiçindededİçindes effectively

# ## Veri Types
- **Structured Veri**: Organized içiçindede rows/columns (veribases, spreadsheets)
- **Unstructured Veri**: No predefiçiçindedeed içinmat (text, images, audio, video)
- **Semi-structured Veri**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series Veri**: Sequential veri poiçiçindedets içiçindededexed içiçindede time order
- **Spatial Veri**: Geographic/location-based içiçindedeiçinmation
- **Graph Veri**: Nodes ve edges representİçinde relationships

# ## The Veri Bilim Process (CRISP-DM)
1. **Busiçiçindedeess Understveİçinde**: Defiçiçindedee objectives ve requirements
2. **Veri Understveİçinde**: Collect ve explore içiçindedeitial veri
3. **Veri Preparation**: Clean, transiçinm, ve içinmat veri (80% içiçindede work)
4. **Modelİçinde**: Select ve apply modelİçinde techniques
5. **Evaluation**: Assess model periçinmance agaiçiçindedest objectives
6. **Dağıtım**: Implement model içiçindede production environment

# # İstatistikler Temeller

# ## Descriptive İstatistikler
- **Measures içiçindede Central Tendency**: Mean, median, mode
- **Measures içiçindede Dispersion**: Range, variance, stveard deviation, içiçindedeterquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles ve Quartiles**: Position ileiçiçindede distribution

# ## Inferential İstatistikler
- **Hypobusis Testİçinde**: Null hypobusis, alternative hypobusis, p-values
- **Confidence Intervals**: Range içiçindede values likely contaiçiçindedeİçinde population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejectİçinde true null hypobusis)
- **Type II Error**: False negative (failİçinde to reject false null hypobusis)
- **Power**: Probability içiçindede correctly rejectİçinde false null hypobusis

# ## Probability Distributions
- **Normal Distribution**: Bell curve, mean = median = mode
- **Biçiçindedeomial Distribution**: Success/failure outcomes
- **Poisson Distribution**: Count içiçindede olaylar içiçindede fixed içiçindedeterval
- **Uniiçinm Distribution**: All outcomes equally likely
- **Exponential Distribution**: Time between olaylar
- **t-Distribution**: Small sample sizes, unknown population variance
- **Chi-Square Distribution**: Categorical veri analysis

# ## Statistical Tests
- **t-test**: Compare means between two groups
- **ANOVA**: Compare means across multiple groups
- **Chi-Square Test**: Test içiçindededependence içiçindede categorical variables
- **Mann-Whitney U**: Non-parametric alternative to t-test
- **Pearson Correlation**: Liçiçindedeear relationship between contiçiçindedeuous variables
- **Spearman Correlation**: Monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: Compare distributions

# # Veri Collection ve Storage

# ## Veri Sources
- **Veribases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, web scrapİçinde
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streamİçinde Veri**: Kafka, Kiçiçindedeesis, real-time feeds
- **Surveys ve Experiments**: Primary veri collection
- **Public Verisets**: Government veri, Kaggle, academic repositories

# ## Veri Warehousİçinde
- **ETL**: Extract, Transiçinm, Load process
- **Veri Lake**: Raw veri storage içiçindede native içinmat
- **Veri Warehouse**: Structured, processed veri için analysis
- **Veri Mart**: Subset içiçindede warehouse için specific department
- **OLAP**: Onliçiçindedee Analytical Processİçinde, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

# ## Veribase Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassvera, HBase (optimized için columns)
- **Graph**: Neo4j, Amazon Neptune (nodes ve relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped veri)
- **Vector**: Piçiçindedeecone, Milvus (embeddİçinde storage için ML)

# # Veri Preprocessİçinde

# ## Veri Cleanİçinde
- **Missİçinde Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (cappİçinde, transiçinmation)
- **Duplicates**: Identification ve removal
- **Inconsistencies**: Stveardizİçinde içinmats, fixİçinde typos
- **Veri Validation**: Checkİçinde constraiçiçindedets, ranges, types

# ## Veri Transiçinmation
- **Normalization**: Scalİçinde to 0-1 range
- **Stveardization**: Z-score normalization (mean=0, std=1)
- **Encodİçinde**: One-hot, label, ordiçiçindedeal, target encodİçinde
- **Biçiçindedenİçinde**: Groupİçinde contiçiçindedeuous values içiçindedeto categories
- **Log Transiçinmation**: Reducİçinde skewness
- **Feature Scalİçinde**: Makİçinde features comparable

# ## Feature Engiçiçindedeeerİçinde
- **Feature Creation**: Derivİçinde new features from existİçinde ones
- **Feature Selection**: Choosİçinde most relevant features
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimiçiçindedeation)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Combiçiçindedeİçinde features multiplicatively
- **Polynomial Features**: Creatİçinde higher-order terms

# # Exploratory Veri Analysis (EDA)

# ## EDA Techniques
- **Summary İstatistikler**: Describe central tendency, spread, shape
- **Univariate Analysis**: Sİçindele variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable içiçindedeteractions
- **Correlation Analysis**: Identify relationships ve multicolliçiçindedeearity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution içiçindede sİçindele variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two contiçiçindedeuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Chsanat**: Categorical comparisons
- **Liçiçindedee Chsanat**: Trends over time
- **Violiçiçindede Plots**: Distribution density ile box plot elements
- **Pair Plots**: Multiple scatter plots için variable pairs

# ## Python Libraries için EDA
- **pveas**: Veri manipulation ve analysis
- **numpy**: Numerical computİçinde
- **matplotlib**: Basic plottİçinde
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific computİçinde ve i̇statistikler

# # Machiçiçindedee Learnİçinde içiçindede Veri Bilim

# ## Supervised Learnİçinde
- **Regression**: Predict contiçiçindedeuous values
  - Liçiçindedeear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Rveom Forest Regressor
  - Gradient Boostİçinde (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Predict categorical labels
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machiçiçindedees
  - Decision Trees
  - Rveom Forest
  - Gradient Boostİçinde
  - Sinir Ağları

# ## Unsupervised Learnİçinde
- **Clusterİçinde**: Group similar observations
  - k-Means
  - Hierarchical Clusterİçinde
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Clusterİçinde
  
- **Dimensionality Reduction**: Reduce feature count
  - Priçiçindedecipal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embeddİçinde (t-SNE)
  - Uniiçinm Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Fiçiçindeded co-occurrİçinde items
  - Apriori Algorithm
  - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tunİçinde**: Grid search, rveom search, Bayesian optimization
- **Learnİçinde Curves**: Diagnose bias-variance tradeiçiçindedef

# # Big Veri Technologies

# ## Distributed Computİçinde Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory processİçinde, faster than Hadoop
  - Spark SQL: Structured veri processİçinde
  - Spark Streamİçinde: Real-time veri
  - MLlib: Machiçiçindedee learnİçinde library
  - GraphX: Graph processİçinde
- **Apache Fliçiçindedek**: Stream processİçinde ile low latency
- **Apache Beam**: Unified batch ve streamİçinde

# ## Cloud Platiçinms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Veriproc, AI Platiçinm, Cloud Storage
- **Azure**: Synapse Analytics, Veribricks, Machiçiçindedee Learnİçinde, Veri Lake
- **Snowflake**: Cloud veri warehouse

# ## Veri Pipeliçiçindedee Tools
- **Apache Airflow**: Workflow orchestration
- **Luigi**: Pipeliçiçindedee yönetim (Spotify)
- **Prefect**: Modern workflow orchestration
- **Dagster**: Veri orchestrator ile asset focus
- **dbt**: Veri transiçinmation içiçindede warehouse

# # Busiçiçindedeess Intelligence ve Analytics

# ## BI Tools
- **Tableau**: Visual analytics platiçinm
- **Power BI**: Microsiçiçindedet busiçiçindedeess analytics
- **Looker**: Veri exploration ve içiçindedesights (Google)
- **Qlik Sense**: Associative analytics
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

# ## Dashboard Design Priçiçindedeciples
- **Know Your Audience**: Tailor to user needs
- **Choose Right Visualizations**: Match chart to veri type
- **Use Color Strategically**: Highlight important içiçindedeiçinmation
- **Maiçiçindedetaiçiçindede Consistency**: Stveardize içinmats ve scales
- **Enable Interactivity**: Filters, drill-downs, tooltips
- **Optimize Periçinmance**: Fast loadİçinde, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Periçinmance Indicators (KPIs)
- **Fiçiçindedeancial**: Revenue, priçiçindedeit margiçiçindede, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketİçinde**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # İleri Düzey Analytics

# ## Predictive Analytics
- **Forecastİçinde**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modelİçinde**: Credit scorİçinde, fraud detection, içiçindedesurance
- **Customer Analytics**: Churn prediction, propensity modelİçinde
- **Demve Forecastİçinde**: Inventory optimization, supply chaiçiçindede
- **Maiçiçindedetenance Prediction**: Equipment failure anticipation

# ## Prescriptive Analytics
- **Optimization**: Liçiçindedeear programmİçinde, içiçindedeteger programmİçinde
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, içiçindedefluence diagrams
- **A/B Testİçinde**: Experimental design, statistical significance
- **Multi-Armed Bveits**: Adaptive experimentation

# ## Text Analytics (NLP)
- **Text Preprocessİçinde**: Tokenization, stemmİçinde, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modelİçinde**: LDA, NMF için bume discovery
- **Named Entity Recognition**: Identifyİçinde people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddİçindes**: Word2Vec, GloVe, BERT

# # Veri Ethics ve Governance

# ## Veri Privacy
- **GDPR**: EU General Veri Protection Regulation
- **CCPA**: Caliiçinnia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability ve Accountability Act (US sağlık hizmetleri)
- **Anonymization**: Removİçinde personally identifiable içiçindedeiçinmation
- **Differential Privacy**: Addİçinde noise to protect içiçindededividuals
- **Consent Yönetim**: Opt-içiçindede/opt-out mechanisms

# ## Veri Quality
- **Accuracy**: Correctness içiçindede veri
- **Completeness**: All required veri present
- **Consistency**: No contradictions across sources
- **Timeliçiçindedeess**: Veri available when needed
- **Validity**: Coniçinms to defiçiçindedeed rules
- **Uniqueness**: No duplicates

# ## Bias ve Fairness
- **Samplİçinde Bias**: Non-representative veri collection
- **Measurement Bias**: Fhukuked veri collection içiçindedestruments
- **Algorithmic Bias**: Discrimiçiçindedeatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processİçinde, içiçindede-processİçinde, post-processİçinde

# ## Veri Governance Framework
- **Veri Stewardship**: Responsibility için veri assets
- **Metaveri Yönetim**: Veri about veri documentation
- **Veri Liçiçindedeeage**: Trackİçinde veri flow ve transiçinmations
- **Access Control**: Role-based permissions
- **Audit Trails**: Loggİçinde veri access ve changes
- **Compliance**: Regulatory adherence

# # Career Paths içiçindede Veri Bilim

# ## Roles
- **Veri Analyst**: Focus on descriptive analytics, dashboards, reportİçinde
- **Veri Scientist**: Statistical modelİçinde, machiçiçindedee learnİçinde, i̇leri düzey analytics
- **ML Engiçiçindedeeer**: Production ML sistemler, model dağıtım, MLOps
- **Veri Engiçiçindedeeer**: Veri pipeliçiçindedees, içiçindedefrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder yönetim
- **BI Developer**: Dashboard creation, report geliştirme
- **Research Scientist**: Novel algorithms, publications, i̇leri düzey research

# ## Skills Matrix
- **Technical**: Python/R, SQL, i̇statistikler, ML frameworks, cloud platiçinms
- **Analytical**: Problem-solvİçinde, critical thiçiçindedekİçinde, experimental design
- **İletişim**: Storytellİçinde, visualization, presentation skills
- **Busiçiçindedeess**: Domaiçiçindede knowledge, stakeholder yönetim, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control için models

# # Emergİçinde Trends

# ## Current Geliştirmes
- **AutoML**: Automated machiçiçindedee learnİçinde pipeliçiçindedee creation
- **MLOps**: DevOps practices için machiçiçindedee learnİçinde
- **Feature Stores**: Centralized feature yönetim
- **Veri Mesh**: Decentralized veri mimari
- **LLMs ve Generative AI**: Large dil models, content generation
- **Edge Analytics**: Processİçinde veri at source devices
- **Real-Time Analytics**: Streamİçinde veri analysis
- **Augmented Analytics**: AI-assisted veri preparation ve içiçindedesights

# ## Gelecek Directions
- **Quantum Machiçiçindedee Learnİçinde**: Quantum computİçinde için ML
- **Federated Learnİçinde**: Traiçiçindedeİçinde models across decentralized veri
- **Causal Inference**: Movİçinde beyond correlation to causation
- **Responsible AI**: Ethics, explaiçiçindedeability, transparency
- **Veri Fabric**: Integrated veri yönetim across environments
