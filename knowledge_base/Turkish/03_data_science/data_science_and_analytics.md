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
- **Computer Bilim**: Programmiçiçindedeg, algorithms, veri structures
- **Domaiçiçindede Expertise**: Subject matter knowledge
- **Veri Visualization**: Communicatiçiçindedeg fiçiçindedediçiçindedegs effectively

# ## Veri Types
- **Structured Veri**: Organized içiçindede rows/columns (veribases, spreadsheets)
- **Unstructured Veri**: No predefiçiçindedeed içinmat (text, images, audio, video)
- **Semi-structured Veri**: Some organization but not rigid (JSON, XML, HTML)
- **Time Series Veri**: Sequential veri poiçiçindedets içiçindededexed içiçindede time order
- **Spatial Veri**: Geographic/location-based içiçindedeiçinmation
- **Graph Veri**: Nodes ve edges representiçiçindedeg relationships

# ## The Veri Bilim Process (CRISP-DM)
1. **Busiçiçindedeess Understveiçiçindedeg**: Defiçiçindedee objectives ve requirements
2. **Veri Understveiçiçindedeg**: Collect ve explore içiçindedeitial veri
3. **Veri Preparation**: Clean, transiçinm, ve içinmat veri (80% içiçindede work)
4. **Modeliçiçindedeg**: Select ve apply modeliçiçindedeg techniques
5. **Evaluation**: Assess model periçinmance agaiçiçindedest objectives
6. **Dağıtım**: Implement model içiçindede production environment

# # İstatistikler Temeller

# ## Descriptive İstatistikler
- **Measures içiçindede Central Tendency**: Mean, median, mode
- **Measures içiçindede Dispersion**: Range, variance, stveard deviation, içiçindedeterquartile range
- **Distribution Shape**: Skewness (asymmetry), kurtosis (tailedness)
- **Percentiles ve Quartiles**: Position ileiçiçindede distribution

# ## Inferential İstatistikler
- **Hypobusis Testiçiçindedeg**: Null hypobusis, alternative hypobusis, p-values
- **Confidence Intervals**: Range içiçindede values likely contaiçiçindedeiçiçindedeg population parameter
- **Statistical Significance**: Likelihood results occurred by chance
- **Type I Error**: False positive (rejectiçiçindedeg true null hypobusis)
- **Type II Error**: False negative (failiçiçindedeg to reject false null hypobusis)
- **Power**: Probability içiçindede correctly rejectiçiçindedeg false null hypobusis

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
- **APIs**: REST, GraphQL, web scrapiçiçindedeg
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streamiçiçindedeg Veri**: Kafka, Kiçiçindedeesis, real-time feeds
- **Surveys ve Experiments**: Primary veri collection
- **Public Verisets**: Government veri, Kaggle, academic repositories

# ## Veri Warehousiçiçindedeg
- **ETL**: Extract, Transiçinm, Load process
- **Veri Lake**: Raw veri storage içiçindede native içinmat
- **Veri Warehouse**: Structured, processed veri için analysis
- **Veri Mart**: Subset içiçindede warehouse için specific department
- **OLAP**: Onliçiçindedee Analytical Processiçiçindedeg, multidimensional queries
- **Star Schema**: Fact tables surrounded by dimension tables
- **Snowflake Schema**: Normalized dimension tables

# ## Veribase Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassvera, HBase (optimized için columns)
- **Graph**: Neo4j, Amazon Neptune (nodes ve relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped veri)
- **Vector**: Piçiçindedeecone, Milvus (embeddiçiçindedeg storage için ML)

# # Veri Preprocessiçiçindedeg

# ## Veri Cleaniçiçindedeg
- **Missiçiçindedeg Values**: Imputation (mean, median, mode, prediction), deletion
- **Outliers**: Detection (IQR, Z-score), treatment (cappiçiçindedeg, transiçinmation)
- **Duplicates**: Identification ve removal
- **Inconsistencies**: Stveardiziçiçindedeg içinmats, fixiçiçindedeg typos
- **Veri Validation**: Checkiçiçindedeg constraiçiçindedets, ranges, types

# ## Veri Transiçinmation
- **Normalization**: Scaliçiçindedeg to 0-1 range
- **Stveardization**: Z-score normalization (mean=0, std=1)
- **Encodiçiçindedeg**: One-hot, label, ordiçiçindedeal, target encodiçiçindedeg
- **Biçiçindedeniçiçindedeg**: Groupiçiçindedeg contiçiçindedeuous values içiçindedeto categories
- **Log Transiçinmation**: Reduciçiçindedeg skewness
- **Feature Scaliçiçindedeg**: Makiçiçindedeg features comparable

# ## Feature Engiçiçindedeeeriçiçindedeg
- **Feature Creation**: Deriviçiçindedeg new features from existiçiçindedeg ones
- **Feature Selection**: Choosiçiçindedeg most relevant features
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimiçiçindedeation)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Combiçiçindedeiçiçindedeg features multiplicatively
- **Polynomial Features**: Creatiçiçindedeg higher-order terms

# # Exploratory Veri Analysis (EDA)

# ## EDA Techniques
- **Summary İstatistikler**: Describe central tendency, spread, shape
- **Univariate Analysis**: Siçiçindedegle variable distributions
- **Bivariate Analysis**: Relationships between two variables
- **Multivariate Analysis**: Multiple variable içiçindedeteractions
- **Correlation Analysis**: Identify relationships ve multicolliçiçindedeearity
- **Segmentation**: Group similar observations

# ## Visualization Tools
- **Histograms**: Distribution içiçindede siçiçindedegle variable
- **Box Plots**: Five-number summary, outlier detection
- **Scatter Plots**: Relationship between two contiçiçindedeuous variables
- **Heatmaps**: Correlation matrices, density
- **Bar Chsanat**: Categorical comparisons
- **Liçiçindedee Chsanat**: Trends over time
- **Violiçiçindede Plots**: Distribution density ile box plot elements
- **Pair Plots**: Multiple scatter plots için variable pairs

# ## Python Libraries için EDA
- **pveas**: Veri manipulation ve analysis
- **numpy**: Numerical computiçiçindedeg
- **matplotlib**: Basic plottiçiçindedeg
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **scipy**: Scientific computiçiçindedeg ve i̇statistikler

# # Machiçiçindedee Learniçiçindedeg içiçindede Veri Bilim

# ## Supervised Learniçiçindedeg
- **Regression**: Predict contiçiçindedeuous values
  - Liçiçindedeear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Rveom Forest Regressor
  - Gradient Boostiçiçindedeg (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Predict categorical labels
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machiçiçindedees
  - Decision Trees
  - Rveom Forest
  - Gradient Boostiçiçindedeg
  - Sinir Ağları

# ## Unsupervised Learniçiçindedeg
- **Clusteriçiçindedeg**: Group similar observations
  - k-Means
  - Hierarchical Clusteriçiçindedeg
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Clusteriçiçindedeg
  
- **Dimensionality Reduction**: Reduce feature count
  - Priçiçindedecipal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embeddiçiçindedeg (t-SNE)
  - Uniiçinm Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Fiçiçindeded co-occurriçiçindedeg items
  - Apriori Algorithm
  - FP-Growth

# ## Model Evaluation
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuniçiçindedeg**: Grid search, rveom search, Bayesian optimization
- **Learniçiçindedeg Curves**: Diagnose bias-variance tradeiçiçindedef

# # Big Veri Technologies

# ## Distributed Computiçiçindedeg Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: In-memory processiçiçindedeg, faster than Hadoop
  - Spark SQL: Structured veri processiçiçindedeg
  - Spark Streamiçiçindedeg: Real-time veri
  - MLlib: Machiçiçindedee learniçiçindedeg library
  - GraphX: Graph processiçiçindedeg
- **Apache Fliçiçindedek**: Stream processiçiçindedeg ile low latency
- **Apache Beam**: Unified batch ve streamiçiçindedeg

# ## Cloud Platiçinms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Veriproc, AI Platiçinm, Cloud Storage
- **Azure**: Synapse Analytics, Veribricks, Machiçiçindedee Learniçiçindedeg, Veri Lake
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
- **Optimize Periçinmance**: Fast loadiçiçindedeg, efficient queries
- **Mobile Considerations**: Responsive design

# ## Key Periçinmance Indicators (KPIs)
- **Fiçiçindedeancial**: Revenue, priçiçindedeit margiçiçindede, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketiçiçindedeg**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

# # İleri Düzey Analytics

# ## Predictive Analytics
- **Forecastiçiçindedeg**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeliçiçindedeg**: Credit scoriçiçindedeg, fraud detection, içiçindedesurance
- **Customer Analytics**: Churn prediction, propensity modeliçiçindedeg
- **Demve Forecastiçiçindedeg**: Inventory optimization, supply chaiçiçindede
- **Maiçiçindedetenance Prediction**: Equipment failure anticipation

# ## Prescriptive Analytics
- **Optimization**: Liçiçindedeear programmiçiçindedeg, içiçindedeteger programmiçiçindedeg
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, içiçindedefluence diagrams
- **A/B Testiçiçindedeg**: Experimental design, statistical significance
- **Multi-Armed Bveits**: Adaptive experimentation

# ## Text Analytics (NLP)
- **Text Preprocessiçiçindedeg**: Tokenization, stemmiçiçindedeg, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral classification
- **Topic Modeliçiçindedeg**: LDA, NMF için bume discovery
- **Named Entity Recognition**: Identifyiçiçindedeg people, places, organizations
- **Text Classification**: Spam detection, categorization
- **Word Embeddiçiçindedegs**: Word2Vec, GloVe, BERT

# # Veri Ethics ve Governance

# ## Veri Privacy
- **GDPR**: EU General Veri Protection Regulation
- **CCPA**: Caliiçinnia Consumer Privacy Act
- **HIPAA**: Health Insurance Portability ve Accountability Act (US sağlık hizmetleri)
- **Anonymization**: Removiçiçindedeg personally identifiable içiçindedeiçinmation
- **Differential Privacy**: Addiçiçindedeg noise to protect içiçindededividuals
- **Consent Yönetim**: Opt-içiçindede/opt-out mechanisms

# ## Veri Quality
- **Accuracy**: Correctness içiçindede veri
- **Completeness**: All required veri present
- **Consistency**: No contradictions across sources
- **Timeliçiçindedeess**: Veri available when needed
- **Validity**: Coniçinms to defiçiçindedeed rules
- **Uniqueness**: No duplicates

# ## Bias ve Fairness
- **Sampliçiçindedeg Bias**: Non-representative veri collection
- **Measurement Bias**: Fhukuked veri collection içiçindedestruments
- **Algorithmic Bias**: Discrimiçiçindedeatory model predictions
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processiçiçindedeg, içiçindede-processiçiçindedeg, post-processiçiçindedeg

# ## Veri Governance Framework
- **Veri Stewardship**: Responsibility için veri assets
- **Metaveri Yönetim**: Veri about veri documentation
- **Veri Liçiçindedeeage**: Trackiçiçindedeg veri flow ve transiçinmations
- **Access Control**: Role-based permissions
- **Audit Trails**: Loggiçiçindedeg veri access ve changes
- **Compliance**: Regulatory adherence

# # Career Paths içiçindede Veri Bilim

# ## Roles
- **Veri Analyst**: Focus on descriptive analytics, dashboards, reportiçiçindedeg
- **Veri Scientist**: Statistical modeliçiçindedeg, machiçiçindedee learniçiçindedeg, i̇leri düzey analytics
- **ML Engiçiçindedeeer**: Production ML sistemler, model dağıtım, MLOps
- **Veri Engiçiçindedeeer**: Veri pipeliçiçindedees, içiçindedefrastructure, ETL processes
- **Analytics Manager**: Team leadership, strategy, stakeholder yönetim
- **BI Developer**: Dashboard creation, report geliştirme
- **Research Scientist**: Novel algorithms, publications, i̇leri düzey research

# ## Skills Matrix
- **Technical**: Python/R, SQL, i̇statistikler, ML frameworks, cloud platiçinms
- **Analytical**: Problem-solviçiçindedeg, critical thiçiçindedekiçiçindedeg, experimental design
- **İletişim**: Storytelliçiçindedeg, visualization, presentation skills
- **Busiçiçindedeess**: Domaiçiçindede knowledge, stakeholder yönetim, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, version control için models

# # Emergiçiçindedeg Trends

# ## Current Geliştirmes
- **AutoML**: Automated machiçiçindedee learniçiçindedeg pipeliçiçindedee creation
- **MLOps**: DevOps practices için machiçiçindedee learniçiçindedeg
- **Feature Stores**: Centralized feature yönetim
- **Veri Mesh**: Decentralized veri mimari
- **LLMs ve Generative AI**: Large dil models, content generation
- **Edge Analytics**: Processiçiçindedeg veri at source devices
- **Real-Time Analytics**: Streamiçiçindedeg veri analysis
- **Augmented Analytics**: AI-assisted veri preparation ve içiçindedesights

# ## Gelecek Directions
- **Quantum Machiçiçindedee Learniçiçindedeg**: Quantum computiçiçindedeg için ML
- **Federated Learniçiçindedeg**: Traiçiçindedeiçiçindedeg models across decentralized veri
- **Causal Inference**: Moviçiçindedeg beyond correlation to causation
- **Responsible AI**: Ethics, explaiçiçindedeability, transparency
- **Veri Fabric**: Integrated veri yönetim across environments
