# Veri Bilimi ve Analitik

## Temel Kavramlar

### Veri Bilimi Nedir?
Veri bilimi, yapılandırılmış ve yapılandırılmamış verilerden bilgi ve içgörü çıkarmak için bilimsel yöntemler, süreçler, algoritmalar ve sistemler kullanan disiplinler arası bir alandır. Şunları bir araya getirir:
- **İstatistik**: Analizin matematiksel temeli
- **Computer Science**: Programlama, algoritmalar, veri yapıları
- **Alan Uzmanlığı**: Konu alanı bilgisi
- **Veri Görselleştirme**: Bulguları etkili biçimde iletme

### Veri Türleri
- **Structured Data**: Satır/sütun hâlinde düzenlenmiş veriler (veritabanları, spreadsheets)
- **Unstructured Data**: Önceden tanımlı bir formatı olmayan veriler (metin, görseller, ses, video)
- **Semi-structured Data**: Bir miktar düzeni olan ama katı yapıda olmayan veriler (JSON, XML, HTML)
- **Time Series Data**: Zaman sırasına göre indekslenmiş ardışık veri noktaları
- **Spatial Data**: Coğrafi / konum tabanlı bilgiler
- **Graph Data**: İlişkileri temsil eden düğümler ve kenarlar

### Veri Bilimi Süreci (CRISP-DM)
1. **İş Anlayışı**: Hedefleri ve gereksinimleri tanımlayın
2. **Veri Anlayışı**: İlk veriyi toplayın ve keşfedin
3. **Veri Hazırlama**: Veriyi temizleyin, dönüştürün ve biçimlendirin (işin %80'i)
4. **Modelleme**: Modelleme tekniklerini seçin ve uygulayın
5. **Değerlendirme**: Model performansını hedeflere göre ölçün
6. **Dağıtım**: Modeli production ortamına alın

## İstatistik Temelleri

### Betimsel İstatistik
- **Merkezi Eğilim Ölçüleri**: Mean, median, mode
- **Dağılım Ölçüleri**: Range, variance, standard deviation, interquartile range
- **Dağılım Şekli**: Skewness (asimetri), kurtosis (kuyrukluluk)
- **Percentile ve Quartile'lar**: Dağılım içindeki konum

### Çıkarımsal İstatistik
- **Hipotez Testi**: Null hypothesis, alternative hypothesis, p-value'lar
- **Güven Aralıkları**: Anakütle parametresini büyük olasılıkla içeren değer aralığı
- **İstatistiksel Anlamlılık**: Sonuçların tesadüfen ortaya çıkmış olma olasılığı
- **Type I Error**: False positive (doğru null hypothesis'i reddetmek)
- **Type II Error**: False negative (yanlış null hypothesis'i reddedememek)
- **Power**: Yanlış null hypothesis'i doğru biçimde reddetme olasılığı

### Olasılık Dağılımları
- **Normal Distribution**: Çan eğrisi, mean = median = mode
- **Binomial Distribution**: Başarı/başarısızlık sonuçları
- **Poisson Distribution**: Sabit bir aralıktaki olay sayısı
- **Uniform Distribution**: Tüm sonuçlar eşit olasılıklıdır
- **Exponential Distribution**: Olaylar arasındaki süre
- **t-Distribution**: Küçük örneklem boyutları, bilinmeyen anakütle varyansı
- **Chi-Square Distribution**: Kategorik veri analizi

### İstatistiksel Testler
- **t-test**: İki grup arasındaki ortalamaları karşılaştırır
- **ANOVA**: Birden fazla grup arasındaki ortalamaları karşılaştırır
- **Chi-Square Test**: Kategorik değişkenlerin bağımsızlığını test eder
- **Mann-Whitney U**: t-test için parametrik olmayan alternatif
- **Pearson Correlation**: Sürekli değişkenler arasındaki doğrusal ilişki
- **Spearman Correlation**: Monoton ilişki (sıra tabanlı)
- **Kolmogorov-Smirnov**: Dağılımları karşılaştırır

## Veri Toplama ve Depolama

### Veri Kaynakları
- **Databases**: SQL, NoSQL, relational, document stores
- **APIs**: REST, GraphQL, web scraping
- **Files**: CSV, JSON, XML, Parquet, Avro
- **Streaming Data**: Kafka, Kinesis, gerçek zamanlı akışlar
- **Surveys and Experiments**: Birincil veri toplama
- **Public Datasets**: Devlet verileri, Kaggle, akademik depolar

### Veri Ambarı
- **ETL**: Extract, Transform, Load süreci
- **Data Lake**: Ham verinin yerel formatında depolanması
- **Data Warehouse**: Analiz için yapılandırılmış, işlenmiş veri
- **Data Mart**: Belirli bir departman için ambarın alt kümesi
- **OLAP**: Online Analytical Processing, çok boyutlu sorgular
- **Star Schema**: Dimension table'larla çevrili fact table'lar
- **Snowflake Schema**: Normalize edilmiş dimension table'lar

### Veritabanı Türleri
- **Relational (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Document**: MongoDB, CouchDB (JSON benzeri belgeler)
- **Key-Value**: Redis, DynamoDB (basit anahtar-değer çiftleri)
- **Column-Family**: Cassandra, HBase (sütunlar için optimize edilmiştir)
- **Graph**: Neo4j, Amazon Neptune (düğümler ve ilişkiler)
- **Time-Series**: InfluxDB, TimescaleDB (zaman damgalı veri)
- **Vector**: Pinecone, Milvus (ML için embedding depolama)

## Veri Ön İşleme

### Veri Temizleme
- **Missing Values**: Imputation (mean, median, mode, prediction), silme
- **Outliers**: Tespit (IQR, Z-score), işleme (capping, transformation)
- **Duplicates**: Belirleme ve kaldırma
- **Inconsistencies**: Formatları standardize etme, yazım hatalarını düzeltme
- **Data Validation**: Kısıtları, aralıkları ve tipleri kontrol etme

### Veri Dönüştürme
- **Normalization**: 0-1 aralığına ölçekleme
- **Standardization**: Z-score normalization (mean=0, std=1)
- **Encoding**: One-hot, label, ordinal, target encoding
- **Binning**: Sürekli değerleri kategorilere ayırma
- **Log Transformation**: Skewness'i azaltma
- **Feature Scaling**: Feature'ları karşılaştırılabilir hâle getirme

### Feature Engineering
- **Feature Creation**: Mevcut feature'lardan yeni feature'lar türetme
- **Feature Selection**: En ilgili feature'ları seçme
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimination)
  - Embedded methods (LASSO, tree-based importance)
- **Dimensionality Reduction**: PCA, t-SNE, UMAP
- **Interaction Terms**: Feature'ları çarpımsal olarak birleştirme
- **Polynomial Features**: Daha yüksek dereceli terimler oluşturma

## Keşifsel Veri Analizi (EDA)

### EDA Teknikleri
- **Summary Statistics**: Merkezi eğilim, yayılım ve şekli açıklama
- **Univariate Analysis**: Tek değişkenli dağılımlar
- **Bivariate Analysis**: İki değişken arasındaki ilişkiler
- **Multivariate Analysis**: Birden fazla değişkenin etkileşimi
- **Correlation Analysis**: İlişkileri ve multicollinearity'yi belirleme
- **Segmentation**: Benzer gözlemleri gruplama

### Görselleştirme Araçları
- **Histograms**: Tek bir değişkenin dağılımı
- **Box Plots**: Beş sayı özeti, aykırı değer tespiti
- **Scatter Plots**: İki sürekli değişken arasındaki ilişki
- **Heatmaps**: Korelasyon matrisleri, yoğunluk
- **Bar Charts**: Kategorik karşılaştırmalar
- **Line Charts**: Zaman içindeki eğilimler
- **Violin Plots**: Box plot öğeleriyle dağılım yoğunluğu
- **Pair Plots**: Değişken çiftleri için çoklu scatter plot'lar

### EDA için Python Kütüphaneleri
- **pandas**: Veri manipülasyonu ve analizi
- **numpy**: Sayısal hesaplama
- **matplotlib**: Temel grafik çizimi
- **seaborn**: İstatistiksel görselleştirme
- **plotly**: Etkileşimli görselleştirmeler
- **scipy**: Bilimsel hesaplama ve istatistik

## Veri Biliminde Makine Öğrenimi

### Denetimli Öğrenme
- **Regression**: Sürekli değerleri tahmin etme
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Classification**: Kategorik etiketleri tahmin etme
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Neural Networks

### Denetimsiz Öğrenme
- **Clustering**: Benzer gözlemleri gruplama
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **Dimensionality Reduction**: Feature sayısını azaltma
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Association Rules**: Birlikte görülen öğeleri bulma
  - Apriori Algorithm
  - FP-Growth

### Model Değerlendirme
- **Classification Metrics**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regression Metrics**: MAE, MSE, RMSE, R², Adjusted R²
- **Cross-Validation**: k-fold, stratified, leave-one-out, time series split
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Learning Curves**: Bias-variance ödünleşimini teşhis etme

## Big Data Teknolojileri

### Dağıtık Hesaplama Framework'leri
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: Bellek içi işleme, Hadoop'tan daha hızlı
  - Spark SQL: Yapılandırılmış veri işleme
  - Spark Streaming: Gerçek zamanlı veri
  - MLlib: Makine öğrenimi kütüphanesi
  - GraphX: Grafik işleme
- **Apache Flink**: Düşük gecikmeli stream processing
- **Apache Beam**: Birleşik batch ve streaming

### Cloud Platformları
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Cloud data warehouse

### Veri Pipeline Araçları
- **Apache Airflow**: Workflow orkestrasyonu
- **Luigi**: Pipeline yönetimi (Spotify)
- **Prefect**: Modern workflow orkestrasyonu
- **Dagster**: Asset odaklı veri orkestratörü
- **dbt**: Warehouse içinde veri dönüşümü

## İş Zekâsı ve Analitik

### BI Araçları
- **Tableau**: Görsel analitik platformu
- **Power BI**: Microsoft business analytics
- **Looker**: Veri keşfi ve içgörü üretimi (Google)
- **Qlik Sense**: İlişkisel analitik
- **Metabase**: Open-source BI
- **Superset**: Apache open-source BI

### Dashboard Tasarım İlkeleri
- **Know Your Audience**: Kullanıcı ihtiyaçlarına göre uyarlayın
- **Choose Right Visualizations**: Grafiği veri türüne göre eşleştirin
- **Use Color Strategically**: Önemli bilgileri vurgulayın
- **Maintain Consistency**: Formatları ve ölçekleri standartlaştırın
- **Enable Interactivity**: Filter'lar, drill-down'lar, tooltips
- **Optimize Performance**: Hızlı yükleme, verimli sorgular
- **Mobile Considerations**: Responsive design

### Key Performance Indicators (KPI'lar)
- **Financial**: Revenue, profit margin, ROI, customer lifetime value
- **Customer**: Acquisition cost, churn rate, satisfaction score, NPS
- **Operational**: Efficiency rates, cycle time, defect rates
- **Marketing**: Conversion rates, click-through rates, attribution
- **Product**: Active users, engagement, retention, feature adoption

## İleri Analitik

### Predictive Analytics
- **Forecasting**: Time series prediction (ARIMA, Prophet, LSTM)
- **Risk Modeling**: Credit scoring, fraud detection, insurance
- **Customer Analytics**: Churn prediction, propensity modeling
- **Demand Forecasting**: Inventory optimization, supply chain
- **Maintenance Prediction**: Ekipman arızasını önceden tahmin etme

### Prescriptive Analytics
- **Optimization**: Linear programming, integer programming
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: Decision trees, influence diagrams
- **A/B Testing**: Deney tasarımı, istatistiksel anlamlılık
- **Multi-Armed Bandits**: Uyarlanabilir deneyleme

### Metin Analitiği (NLP)
- **Text Preprocessing**: Tokenization, stemming, lemmatization
- **Sentiment Analysis**: Positive/negative/neutral sınıflandırma
- **Topic Modeling**: Tema keşfi için LDA, NMF
- **Named Entity Recognition**: Kişileri, yerleri, kuruluşları belirleme
- **Text Classification**: Spam detection, kategorizasyon
- **Word Embeddings**: Word2Vec, GloVe, BERT

## Veri Etiği ve Yönetişim

### Veri Gizliliği
- **GDPR**: EU General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (US healthcare)
- **Anonymization**: Kişisel olarak tanımlanabilir bilgilerin kaldırılması
- **Differential Privacy**: Bireyleri korumak için gürültü ekleme
- **Consent Management**: Opt-in/opt-out mekanizmaları

### Veri Kalitesi
- **Accuracy**: Verinin doğruluğu
- **Completeness**: Gerekli tüm verilerin mevcut olması
- **Consistency**: Kaynaklar arasında çelişki olmaması
- **Timeliness**: Verinin gerektiğinde hazır olması
- **Validity**: Tanımlanmış kurallara uygunluk
- **Uniqueness**: Tekrarlı kayıtların olmaması

### Önyargı ve Adillik
- **Sampling Bias**: Temsil gücü düşük veri toplama
- **Measurement Bias**: Kusurlu veri toplama araçları
- **Algorithmic Bias**: Ayrımcı model tahminleri
- **Fairness Metrics**: Demographic parity, equal opportunity
- **Bias Mitigation**: Pre-processing, in-processing, post-processing

### Veri Yönetişimi Çerçevesi
- **Data Stewardship**: Veri varlıkları için sorumluluk
- **Metadata Management**: Veri hakkındaki verinin dokümantasyonu
- **Data Lineage**: Veri akışını ve dönüşümleri izleme
- **Access Control**: Rol tabanlı izinler
- **Audit Trails**: Veri erişimi ve değişikliklerinin kaydı
- **Compliance**: Düzenlemelere uyum

## Veri Biliminde Kariyer Yolları

### Roller
- **Data Analyst**: Betimsel analitik, dashboard'lar, raporlama odaklı
- **Data Scientist**: İstatistiksel modelleme, makine öğrenimi, ileri analitik
- **ML Engineer**: Production ML sistemleri, model dağıtımı, MLOps
- **Data Engineer**: Veri pipeline'ları, altyapı, ETL süreçleri
- **Analytics Manager**: Ekip liderliği, strateji, paydaş yönetimi
- **BI Developer**: Dashboard oluşturma, rapor geliştirme
- **Research Scientist**: Yeni algoritmalar, yayınlar, ileri araştırma

### Beceri Matrisi
- **Technical**: Python/R, SQL, istatistik, ML framework'leri, cloud platformları
- **Analytical**: Problem çözme, eleştirel düşünme, deney tasarımı
- **Communication**: Hikâye anlatımı, görselleştirme, sunum becerileri
- **Business**: Alan bilgisi, paydaş yönetimi, ROI analizi
- **Tools**: Git, Jupyter, Docker, CI/CD, modeller için version control

## Yükselen Eğilimler

### Güncel Gelişmeler
- **AutoML**: Otomatik makine öğrenimi pipeline oluşturma
- **MLOps**: Makine öğrenimi için DevOps uygulamaları
- **Feature Stores**: Merkezî feature yönetimi
- **Data Mesh**: Dağıtık veri mimarisi
- **LLMs and Generative AI**: Large language models, içerik üretimi
- **Edge Analytics**: Veriyi kaynak cihazlarda işleme
- **Real-Time Analytics**: Streaming veri analizi
- **Augmented Analytics**: AI destekli veri hazırlama ve içgörü üretimi

### Gelecek Yönelimleri
- **Quantum Machine Learning**: ML için quantum computing
- **Federated Learning**: Modelleri dağıtık veri üzerinde eğitme
- **Causal Inference**: Korelasyondan nedenselliğe geçiş
- **Responsible AI**: Etik, açıklanabilirlik, şeffaflık
- **Data Fabric**: Ortamlar arası entegre veri yönetimi
