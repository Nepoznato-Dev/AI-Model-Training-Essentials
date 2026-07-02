# डेटा साइंस और एनालिटिक्स

## मूल अवधारणाएँ

### Data Science क्या है?
Data science एक interdisciplinary field है जो structured और unstructured data से knowledge और insights निकालने के लिए scientific methods, processes, algorithms और systems का उपयोग करती है। यह निम्न को संयोजित करती है:
- **Statistics**: विश्लेषण के लिए गणितीय आधार
- **Computer Science**: programming, algorithms, data structures
- **Domain Expertise**: विषय-विशेष ज्ञान
- **Data Visualization**: निष्कर्षों का प्रभावी संप्रेषण

### Data Types
- **Structured Data**: rows/columns में व्यवस्थित (databases, spreadsheets)
- **Unstructured Data**: कोई पूर्वनिर्धारित format नहीं (text, images, audio, video)
- **Semi-structured Data**: कुछ संगठन होता है लेकिन कठोर नहीं (JSON, XML, HTML)
- **Time Series Data**: समय क्रम में indexed sequential data points
- **Spatial Data**: geographic/location-based information
- **Graph Data**: relationships को दर्शाने वाले nodes और edges

### Data Science Process (CRISP-DM)
1. **Business Understanding**: objectives और requirements परिभाषित करें
2. **Data Understanding**: प्रारंभिक data एकत्र करें और उसका अन्वेषण करें
3. **Data Preparation**: data को clean, transform, और format करें (काम का 80%)
4. **Modeling**: modeling techniques चुनें और लागू करें
5. **Evaluation**: objectives के विरुद्ध model performance का आकलन करें
6. **Deployment**: model को production environment में लागू करें

## सांख्यिकी की मूल बातें

### Descriptive Statistics
- **Measures of Central Tendency**: mean, median, mode
- **Measures of Dispersion**: range, variance, standard deviation, interquartile range
- **Distribution Shape**: skewness (असमरूपता), kurtosis (tails की प्रकृति)
- **Percentiles and Quartiles**: distribution के भीतर स्थिति

### Inferential Statistics
- **Hypothesis Testing**: null hypothesis, alternative hypothesis, p-values
- **Confidence Intervals**: values की वह range जिसमें population parameter होने की संभावना होती है
- **Statistical Significance**: परिणामों के संयोग से होने की संभावना
- **Type I Error**: false positive (सही null hypothesis को reject करना)
- **Type II Error**: false negative (गलत null hypothesis को reject न कर पाना)
- **Power**: गलत null hypothesis को सही रूप से reject करने की probability

### Probability Distributions
- **Normal Distribution**: bell curve, mean = median = mode
- **Binomial Distribution**: success/failure outcomes
- **Poisson Distribution**: निश्चित interval में घटनाओं की गिनती
- **Uniform Distribution**: सभी outcomes समान रूप से संभावित
- **Exponential Distribution**: घटनाओं के बीच का समय
- **t-Distribution**: छोटे sample sizes, unknown population variance
- **Chi-Square Distribution**: categorical data analysis

### Statistical Tests
- **t-test**: दो groups के बीच means की तुलना
- **ANOVA**: कई groups में means की तुलना
- **Chi-Square Test**: categorical variables की independence की जाँच
- **Mann-Whitney U**: t-test का non-parametric alternative
- **Pearson Correlation**: continuous variables के बीच linear relationship
- **Spearman Correlation**: monotonic relationship (rank-based)
- **Kolmogorov-Smirnov**: distributions की तुलना

## Data Collection and Storage

### Data Sources
- **Databases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, web scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming Data**: Kafka, Kinesis, real-time feeds
- **Surveys and Experiments**: primary data collection
- **Public Datasets**: government data, Kaggle, academic repositories

### Data Warehousing
- **ETL**: Extract, Transform, Load process
- **Data Lake**: native format में raw data storage
- **Data Warehouse**: analysis के लिए structured, processed data
- **Data Mart**: किसी specific department के लिए warehouse का subset
- **OLAP**: Online Analytical Processing, multidimensional queries
- **Star Schema**: dimension tables से घिरी fact tables
- **Snowflake Schema**: normalized dimension tables

### Database Types
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON-like documents)
- **Key-Value**: Redis, DynamoDB (simple key-value pairs)
- **Column-Family**: Cassandra, HBase (columns के लिए optimised)
- **Graph**: Neo4j, Amazon Neptune (nodes और relationships)
- **Time-Series**: InfluxDB, TimescaleDB (timestamped data)
- **Vector**: Pinecone, Milvus (ML के लिए embedding storage)

## Data Preprocessing

### Data Cleaning
- **Missing Values**: imputation (mean, median, mode, prediction), deletion
- **Outliers**: detection (IQR, Z-score), treatment (capping, transformation)
- **Duplicates**: पहचान और removal
- **Inconsistencies**: formats को standardize करना, typos ठीक करना
- **Data Validation**: constraints, ranges, types की जाँच

### Data Transformation
- **Normalization**: 0-1 range तक scaling
- **Standardization**: Z-score normalization (mean=0, std=1)
- **Encoding**: one-hot, label, ordinal, target encoding
- **Binning**: continuous values को categories में समूहित करना
- **Log Transformation**: skewness कम करना
- **Feature Scaling**: features को तुलनीय बनाना

### Feature Engineering
- **Feature Creation**: मौजूदा features से नई features निकालना
- **Feature Selection**: सबसे relevant features चुनना
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimination)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: features को multiplicatively संयोजित करना
- **Polynomial Features**: higher-order terms बनाना

## Exploratory Data Analysis (EDA)

### EDA Techniques
- **Summary Statistics**: central tendency, spread, shape का वर्णन
- **Univariate Analysis**: single variable distributions
- **Bivariate Analysis**: दो variables के बीच relationships
- **Multivariate Analysis**: कई variables की interactions
- **Correlation Analysis**: relationships और multicollinearity की पहचान
- **Segmentation**: समान observations को समूहित करना

### Visualization Tools
- **Histograms**: single variable का distribution
- **Box Plots**: five-number summary, outlier detection
- **Scatter Plots**: दो continuous variables के बीच relationship
- **Heatmaps**: correlation matrices, density
- **Bar Charts**: categorical comparisons
- **Line Charts**: समय के साथ trends
- **Violin Plots**: box plot elements के साथ distribution density
- **Pair Plots**: variable pairs के लिए multiple scatter plots

### EDA के लिए Python Libraries
- **pandas**: data manipulation और analysis
- **numpy**: numerical computing
- **matplotlib**: basic plotting
- **seaborn**: statistical visualization
- **plotly**: interactive visualizations
- **scipy**: scientific computing और statistics

## Data Science में Machine Learning

### Supervised Learning
- **Regression**: continuous values का पूर्वानुमान
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Classification**: categorical labels का पूर्वानुमान
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Unsupervised Learning
- **Clustering**: समान observations को समूहित करना
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **Dimensionality Reduction**: feature count कम करना
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: साथ में होने वाले items खोजना
  - Apriori Algorithm
  - FP-Growth

### Model Evaluation
- **Classification Metrics**: accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuning**: grid search, random search, Bayesian optimization
- **Learning Curves**: bias-variance tradeoff का निदान

## Big Data Technologies

### Distributed Computing Frameworks
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: in-memory processing, Hadoop से तेज़
  - Spark SQL: structured data processing
  - Spark Streaming: real-time data
  - MLlib: machine learning library
  - GraphX: graph processing
- **Apache Flink**: low latency के साथ stream processing
- **Apache Beam**: unified batch और streaming

### Cloud Platforms
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: cloud data warehouse

### Data Pipeline Tools
- **Apache Airflow**: workflow orchestration
- **Luigi**: pipeline management (Spotify)
- **Prefect**: modern workflow orchestration
- **Dagster**: asset focus वाला data orchestrator
- **dbt**: warehouse में data transformation

## Business Intelligence and Analytics

### BI Tools
- **Tableau**: visual analytics platform
- **Power BI**: Microsoft business analytics
- **Looker**: data exploration और insights (Google)
- **Qlik Sense**: associative analytics
- **Metabase**: open-source BI
- **Superset**: Apache open-source BI

### Dashboard Design Principles
- **Know Your Audience**: user needs के अनुसार अनुकूलित करें
- **Choose Right Visualizations**: chart को data type से मिलाएँ
- **Use Color Strategically**: महत्वपूर्ण जानकारी को highlight करें
- **Maintain Consistency**: formats और scales को standardize करें
- **Enable Interactivity**: filters, drill-downs, tooltips
- **Optimize Performance**: fast loading, efficient queries
- **Mobile Considerations**: responsive design

### Key Performance Indicators (KPIs)
- **Financial**: revenue, profit margin, ROI, customer lifetime value
- **Customer**: acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: efficiency rates, cycle time, defect rates
- **Marketing**: conversion rates, click-through rates, attribution
- **Product**: active users, engagement, retention, feature adoption

## Advanced Analytics

### Predictive Analytics
- **Forecasting**: time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeling**: credit scoring, fraud detection, insurance
- **Customer Analytics**: churn prediction, propensity modeling
- **Demand Forecasting**: inventory optimization, supply chain
- **Maintenance Prediction**: equipment failure anticipation

### Prescriptive Analytics
- **Optimization**: linear programming, integer programming
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: decision trees, influence diagrams
- **A/B Testing**: experimental design, statistical significance
- **Multi-Armed Bandits**: adaptive experimentation

### Text Analytics (NLP)
- **Text Preprocessing**: tokenization, stemming, lemmatization
- **Sentiment Analysis**: positive/negative/neutral classification
- **Topic Modeling**: theme discovery के लिए LDA, NMF
- **Named Entity Recognition**: people, places, organizations की पहचान
- **Text Classification**: spam detection, categorization
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Data Ethics and Governance

### Data Privacy
- **GDPR**: EU General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (US healthcare)
- **Anonymization**: personally identifiable information को हटाना
- **Differential Privacy**: व्यक्तियों की सुरक्षा के लिए noise जोड़ना
- **Consent Management**: opt-in/opt-out mechanisms

### Data Quality
- **Accuracy**: data की शुद्धता
- **Completeness**: सभी आवश्यक data उपस्थित है
- **Consistency**: sources के बीच कोई विरोधाभास नहीं
- **Timeliness**: data ज़रूरत के समय उपलब्ध है
- **Validity**: परिभाषित rules के अनुरूप
- **Uniqueness**: कोई duplicates नहीं

### Bias and Fairness
- **Sampling Bias**: अप्रतिनिधिक data collection
- **Measurement Bias**: flawed data collection instruments
- **Algorithmic Bias**: भेदभावपूर्ण model predictions
- **Fairness Metrics**: demographic parity, equal opportunity
- **Bias Mitigation**: pre-processing, in-processing, post-processing

### Data Governance Framework
- **Data Stewardship**: data assets की ज़िम्मेदारी
- **Metadata Management**: data about data documentation
- **Data Lineage**: data flow और transformations को track करना
- **Access Control**: role-based permissions
- **Audit Trails**: data access और changes की logging
- **Compliance**: regulatory adherence

## Data Science में Career Paths

### Roles
- **Data Analyst**: descriptive analytics, dashboards, reporting पर केंद्रित
- **Data Scientist**: statistical modeling, machine learning, advanced analytics
- **ML Engineer**: production ML systems, model deployment, MLOps
- **Data Engineer**: data pipelines, infrastructure, ETL processes
- **Analytics Manager**: team leadership, strategy, stakeholder management
- **BI Developer**: dashboard creation, report development
- **Research Scientist**: novel algorithms, publications, advanced research

### Skills Matrix
- **Technical**: Python/R, SQL, statistics, ML frameworks, cloud platforms
- **Analytical**: problem-solving, critical thinking, experimental design
- **Communication**: storytelling, visualization, presentation skills
- **Business**: domain knowledge, stakeholder management, ROI analysis
- **Tools**: Git, Jupyter, Docker, CI/CD, models के लिए version control

## उभरते रुझान

### वर्तमान विकास
- **AutoML**: automated machine learning pipeline creation
- **MLOps**: machine learning के लिए DevOps practices
- **Feature Stores**: centralized feature management
- **Data Mesh**: decentralized data architecture
- **LLMs and Generative AI**: बड़े भाषा models, content generation
- **Edge Analytics**: source devices पर data processing
- **Real-Time Analytics**: streaming data analysis
- **Augmented Analytics**: AI-assisted data preparation और insights

### भविष्य की दिशाएँ
- **Quantum Machine Learning**: ML के लिए quantum computing
- **Federated Learning**: decentralized data पर models train करना
- **Causal Inference**: correlation से आगे बढ़कर causation तक पहुँचना
- **Responsible AI**: ethics, explainability, transparency
- **Data Fabric**: environments के बीच integrated data management
