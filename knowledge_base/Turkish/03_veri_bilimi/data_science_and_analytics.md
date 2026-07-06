# Veri Bilimi ve Analitik

## Temel Kavramlar

### Veri Bilimi Nedir?
Veri bilimi, yapılandırılmış ve yapılandırılmamış verilerden bilgi ve içgörü çıkarmak için bilimsel yöntemler, süreçler, algoritmalar ve sistemler kullanan disiplinler arası bir alandır. Şunları bir araya getirir:
- **İstatistik**: Analiz için matematiksel temel
- **Bilgisayar Bilimi**: Programlama, algoritmalar, veri yapıları
- **Alan Uzmanlığı**: Konuya özgü bilgi
- **Veri Görselleştirme**: Bulguların etkili biçimde iletilmesi

### Veri Türleri
- **Yapılandırılmış Veri**: Satır/sütun düzeninde organize edilmiş veri (veritabanları, hesap tabloları)
- **Yapılandırılmamış Veri**: Önceden tanımlı bir biçimi olmayan veri (metin, görüntü, ses, video)
- **Yarı Yapılandırılmış Veri**: Bir miktar düzen içeren ama katı olmayan veri (JSON, XML, HTML)
- **Zaman Serisi Verisi**: Zaman sırasına göre dizinlenmiş ardışık veri noktaları
- **Mekânsal Veri**: Coğrafi/konum tabanlı bilgiler
- **Graf Verisi**: İlişkileri temsil eden düğümler ve kenarlar

### Veri Bilimi Süreci (CRISP-DM)
1. **İş Anlayışı**: Hedefleri ve gereksinimleri tanımlama
2. **Veri Anlayışı**: İlk veriyi toplama ve keşfetme
3. **Veri Hazırlama**: Veriyi temizleme, dönüştürme ve biçimlendirme (işin %80'i)
4. **Modelleme**: Modelleme tekniklerini seçme ve uygulama
5. **Değerlendirme**: Model performansını hedeflere göre değerlendirme
6. **Dağıtım**: Modeli üretim ortamında uygulama

## İstatistik Temelleri

### Betimsel İstatistik
- **Merkezi Eğilim Ölçüleri**: Ortalama, medyan, mod
- **Dağılım Ölçüleri**: Aralık, varyans, standart sapma, çeyrekler arası açıklık
- **Dağılım Şekli**: Çarpıklık (asimetri), basıklık (kuyruk yapısı)
- **Yüzdelikler ve Çeyrekler**: Dağılım içindeki konum

### Çıkarımsal İstatistik
- **Hipotez Testi**: Sıfır hipotezi, alternatif hipotez, p-değerleri
- **Güven Aralıkları**: Anakütle parametresini içermesi muhtemel değer aralığı
- **İstatistiksel Anlamlılık**: Sonuçların tesadüfen ortaya çıkmış olma olasılığı
- **Tip I Hata**: Yanlış pozitif (doğru sıfır hipotezini reddetmek)
- **Tip II Hata**: Yanlış negatif (yanlış sıfır hipotezini reddedememek)
- **Güç**: Yanlış sıfır hipotezini doğru biçimde reddetme olasılığı

### Olasılık Dağılımları
- **Normal Dağılım**: Çan eğrisi, ortalama = medyan = mod
- **Binom Dağılımı**: Başarı/başarısızlık sonuçları
- **Poisson Dağılımı**: Sabit bir aralıktaki olay sayısı
- **Uniform Dağılım**: Tüm sonuçların eşit olasılıklı olması
- **Üstel Dağılım**: Olaylar arasındaki süre
- **t-Dağılımı**: Küçük örneklem boyutları, bilinmeyen anakütle varyansı
- **Ki-Kare Dağılımı**: Kategorik veri analizi

### İstatistiksel Testler
- **t-testi**: İki grup arasındaki ortalamaları karşılaştırma
- **ANOVA**: Birden fazla grup arasındaki ortalamaları karşılaştırma
- **Ki-Kare Testi**: Kategorik değişkenlerin bağımsızlığını test etme
- **Mann-Whitney U**: t-testine parametrik olmayan alternatif
- **Pearson Korelasyonu**: Sürekli değişkenler arasındaki doğrusal ilişki
- **Spearman Korelasyonu**: Monoton ilişki (sıralama tabanlı)
- **Kolmogorov-Smirnov**: Dağılımları karşılaştırma

## Veri Toplama ve Depolama

### Veri Kaynakları
- **Veritabanları**: SQL, NoSQL, ilişkisel, belge depoları
- **API'ler**: REST, GraphQL, web kazıma
- **Dosyalar**: CSV, JSON, XML, Parquet, Avro
- **Akış Verisi**: Kafka, Kinesis, gerçek zamanlı akışlar
- **Anketler ve Deneyler**: Birincil veri toplama
- **Açık Veri Kümeleri**: Devlet verileri, Kaggle, akademik depolar

### Veri Ambarı
- **ETL**: Ayıkla, Dönüştür, Yükle süreci
- **Veri Gölü**: Ham verinin doğal biçiminde saklanması
- **Veri Ambarı**: Analiz için yapılandırılmış, işlenmiş veri
- **Veri Pazarı**: Belirli bir departman için ambarın alt kümesi
- **OLAP**: Çevrimiçi Analitik İşleme, çok boyutlu sorgular
- **Yıldız Şema**: Boyut tablolarıyla çevrili olgu tabloları
- **Kar Tanesi Şema**: Normalize edilmiş boyut tabloları

### Veritabanı Türleri
- **İlişkisel (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **Belge**: MongoDB, CouchDB (JSON benzeri belgeler)
- **Anahtar-Değer**: Redis, DynamoDB (basit anahtar-değer çiftleri)
- **Sütun Ailesi**: Cassandra, HBase (sütunlar için optimize edilmiş)
- **Graf**: Neo4j, Amazon Neptune (düğümler ve ilişkiler)
- **Zaman Serisi**: InfluxDB, TimescaleDB (zaman damgalı veri)
- **Vektör**: Pinecone, Milvus (ML için gömme depolama)

## Veri Ön İşleme

### Veri Temizleme
- **Eksik Değerler**: Atama (ortalama, medyan, mod, tahmin), silme
- **Aykırı Değerler**: Tespit (IQR, Z-skoru), işleme (sınırlandırma, dönüşüm)
- **Yinelenenler**: Belirleme ve kaldırma
- **Tutarsızlıklar**: Biçimleri standartlaştırma, yazım hatalarını düzeltme
- **Veri Doğrulama**: Kısıtları, aralıkları, türleri kontrol etme

### Veri Dönüştürme
- **Normalizasyon**: 0-1 aralığına ölçekleme
- **Standartlaştırma**: Z-skoru normalizasyonu (ortalama=0, std=1)
- **Kodlama**: One-hot, etiket, sıralı, hedef kodlama
- **Binning**: Sürekli değerleri kategorilere gruplama
- **Log Dönüşümü**: Çarpıklığı azaltma
- **Özellik Ölçekleme**: Özellikleri karşılaştırılabilir hale getirme

### Özellik Mühendisliği
- **Özellik Oluşturma**: Mevcut özelliklerden yeni özellikler türetme
- **Özellik Seçimi**: En ilgili özellikleri seçme
  - Filtre yöntemleri (korelasyon, ki-kare)
  - Sarmalayıcı yöntemler (özyinelemeli özellik eleme)
  - Gömülü yöntemler (LASSO, ağaç tabanlı önem)
- **Boyut İndirgeme**: PCA, t-SNE, UMAP
- **Etkileşim Terimleri**: Özellikleri çarpımsal biçimde birleştirme
- **Polinom Özellikler**: Daha yüksek dereceden terimler oluşturma

## Keşifsel Veri Analizi (EDA)

### EDA Teknikleri
- **Özet İstatistikler**: Merkezi eğilim, yayılım ve şekli tanımlama
- **Tek Değişkenli Analiz**: Tek değişkenli dağılımlar
- **İki Değişkenli Analiz**: İki değişken arasındaki ilişkiler
- **Çok Değişkenli Analiz**: Birden fazla değişken arasındaki etkileşimler
- **Korelasyon Analizi**: İlişkileri ve çoklu doğrusal bağlantıyı belirleme
- **Segmentasyon**: Benzer gözlemleri gruplama

### Görselleştirme Araçları
- **Histogramlar**: Tek bir değişkenin dağılımı
- **Kutu Grafikleri**: Beş sayı özeti, aykırı değer tespiti
- **Dağılım Grafikleri**: İki sürekli değişken arasındaki ilişki
- **Isı Haritaları**: Korelasyon matrisleri, yoğunluk
- **Çubuk Grafikler**: Kategorik karşılaştırmalar
- **Çizgi Grafikler**: Zaman içindeki eğilimler
- **Keman Grafikleri**: Kutu grafiği öğeleriyle dağılım yoğunluğu
- **Çiftli Grafikler**: Değişken çiftleri için çoklu dağılım grafikleri

### EDA için Python Kütüphaneleri
- **pandas**: Veri işleme ve analiz
- **numpy**: Sayısal hesaplama
- **matplotlib**: Temel çizim
- **seaborn**: İstatistiksel görselleştirme
- **plotly**: Etkileşimli görselleştirmeler
- **scipy**: Bilimsel hesaplama ve istatistik

## Veri Biliminde Makine Öğrenimi

### Denetimli Öğrenme
- **Regresyon**: Sürekli değerleri tahmin etme
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Sınıflandırma**: Kategorik etiketleri tahmin etme
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Destek Vektör Makineleri
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - Sinir Ağları

### Denetimsiz Öğrenme
- **Kümeleme**: Benzer gözlemleri gruplama
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (yoğunluk tabanlı)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **Boyut İndirgeme**: Özellik sayısını azaltma
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **Birliktelik Kuralları**: Birlikte görülen öğeleri bulma
  - Apriori Algorithm
  - FP-Growth

### Model Değerlendirme
- **Sınıflandırma Metrikleri**: Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- **Regresyon Metrikleri**: MAE, MSE, RMSE, R², Adjusted R²
- **Çapraz Doğrulama**: k-fold, stratified, leave-one-out, time series split
- **Hiperparametre Ayarlama**: Grid search, random search, Bayesian optimization
- **Öğrenme Eğrileri**: Bias-variance dengesini teşhis etme

## Büyük Veri Teknolojileri

### Dağıtık Hesaplama Çerçeveleri
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: Bellek içi işleme, Hadoop'dan daha hızlı
  - Spark SQL: Yapılandırılmış veri işleme
  - Spark Streaming: Gerçek zamanlı veri
  - MLlib: Makine öğrenimi kütüphanesi
  - GraphX: Graf işleme
- **Apache Flink**: Düşük gecikmeyle akış işleme
- **Apache Beam**: Birleşik toplu iş ve akış

### Bulut Platformları
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: Bulut veri ambarı

### Veri Hattı Araçları
- **Apache Airflow**: İş akışı orkestrasyonu
- **Luigi**: İş hattı yönetimi (Spotify)
- **Prefect**: Modern iş akışı orkestrasyonu
- **Dagster**: Varlık odaklı veri orkestratörü
- **dbt**: Ambar içinde veri dönüştürme

## İş Zekâsı ve Analitik

### BI Araçları
- **Tableau**: Görsel analitik platformu
- **Power BI**: Microsoft iş analitiği
- **Looker**: Veri keşfi ve içgörüler (Google)
- **Qlik Sense**: İlişkisel analitik
- **Metabase**: Açık kaynaklı BI
- **Superset**: Apache açık kaynaklı BI

### Gösterge Paneli Tasarım İlkeleri
- **Hedef Kitleni Tanı**: Kullanıcı ihtiyaçlarına göre uyarlama
- **Doğru Görselleştirmeleri Seç**: Grafiği veri türüyle eşleştirme
- **Rengi Stratejik Kullan**: Önemli bilgileri vurgulama
- **Tutarlılığı Koru**: Biçimleri ve ölçekleri standartlaştırma
- **Etkileşimi Etkinleştir**: Filtreler, detaylara inme, ipuçları
- **Performansı Optimize Et**: Hızlı yükleme, verimli sorgular
- **Mobil Hususlar**: Duyarlı tasarım

### Temel Performans Göstergeleri (KPI'lar)
- **Finansal**: Gelir, kâr marjı, ROI, müşteri yaşam boyu değeri
- **Müşteri**: Edinme maliyeti, müşteri kaybı oranı, memnuniyet skoru, NPS
- **Operasyonel**: Verimlilik oranları, çevrim süresi, hata oranları
- **Pazarlama**: Dönüşüm oranları, tıklama oranları, atıf
- **Ürün**: Aktif kullanıcılar, etkileşim, elde tutma, özellik benimseme

## İleri Analitik

### Tahmine Dayalı Analitik
- **Tahminleme**: Zaman serisi tahmini (ARIMA, Prophet, LSTM)
- **Risk Modelleme**: Kredi puanlama, dolandırıcılık tespiti, sigorta
- **Müşteri Analitiği**: Müşteri kaybı tahmini, eğilim modelleme
- **Talep Tahmini**: Envanter optimizasyonu, tedarik zinciri
- **Bakım Tahmini**: Ekipman arızasını öngörme

### Reçeteci Analitik
- **Optimizasyon**: Doğrusal programlama, tamsayılı programlama
- **Simülasyon**: Monte Carlo yöntemleri, kesikli olay simülasyonu
- **Karar Analizi**: Karar ağaçları, etki diyagramları
- **A/B Testi**: Deney tasarımı, istatistiksel anlamlılık
- **Çok Kollu Kumarbazlar**: Uyarlanabilir deneyler

### Metin Analitiği (NLP)
- **Metin Ön İşleme**: Tokenization, stemming, lemmatization
- **Duygu Analizi**: Pozitif/negatif/nötr sınıflandırma
- **Konu Modelleme**: Tema keşfi için LDA, NMF
- **Adlandırılmış Varlık Tanıma**: İnsanları, yerleri, kuruluşları belirleme
- **Metin Sınıflandırma**: Spam tespiti, kategorilendirme
- **Kelime Gömme**: Word2Vec, GloVe, BERT

## Veri Etiği ve Yönetişim

### Veri Gizliliği
- **GDPR**: AB Genel Veri Koruma Tüzüğü
- **CCPA**: California Tüketici Gizliliği Yasası
- **HIPAA**: Health Insurance Portability and Accountability Act (ABD sağlık hizmetleri)
- **Anonimleştirme**: Kişisel olarak tanımlanabilir bilgileri kaldırma
- **Diferansiyel Gizlilik**: Bireyleri korumak için gürültü ekleme
- **Rıza Yönetimi**: Opt-in/opt-out mekanizmaları

### Veri Kalitesi
- **Doğruluk**: Verinin doğruluğu
- **Eksiksizlik**: Gereken tüm verinin mevcut olması
- **Tutarlılık**: Kaynaklar arasında çelişki olmaması
- **Zamanlılık**: Verinin gerektiğinde kullanılabilir olması
- **Geçerlilik**: Tanımlı kurallara uygunluk
- **Benzersizlik**: Yinelenen kayıt olmaması

### Önyargı ve Adillik
- **Örnekleme Önyargısı**: Temsil gücü olmayan veri toplama
- **Ölçüm Önyargısı**: Kusurlu veri toplama araçları
- **Algoritmik Önyargı**: Ayrımcı model tahminleri
- **Adillik Metrikleri**: Demografik eşitlik, fırsat eşitliği
- **Önyargı Azaltma**: Ön işleme, süreç içi, süreç sonrası

### Veri Yönetişim Çerçevesi
- **Veri Sorumluluğu**: Veri varlıkları için sorumluluk
- **Üst Veri Yönetimi**: Veri hakkındaki verinin belgelenmesi
- **Veri Soy Ağacı**: Veri akışını ve dönüşümleri izleme
- **Erişim Kontrolü**: Rol tabanlı izinler
- **Denetim İzleri**: Veri erişimini ve değişiklikleri kaydetme
- **Uyumluluk**: Düzenlemelere uygunluk

## Veri Biliminde Kariyer Yolları

### Roller
- **Veri Analisti**: Betimsel analitik, gösterge panoları, raporlama odaklı
- **Veri Bilimci**: İstatistiksel modelleme, makine öğrenimi, ileri analitik
- **ML Mühendisi**: Üretim ML sistemleri, model dağıtımı, MLOps
- **Veri Mühendisi**: Veri hatları, altyapı, ETL süreçleri
- **Analitik Müdürü**: Ekip liderliği, strateji, paydaş yönetimi
- **BI Geliştiricisi**: Gösterge paneli oluşturma, rapor geliştirme
- **Araştırma Bilimcisi**: Yeni algoritmalar, yayınlar, ileri araştırma

### Beceri Matrisi
- **Teknik**: Python/R, SQL, istatistik, ML çerçeveleri, bulut platformları
- **Analitik**: Problem çözme, eleştirel düşünme, deney tasarımı
- **İletişim**: Hikâyeleştirme, görselleştirme, sunum becerileri
- **İş**: Alan bilgisi, paydaş yönetimi, ROI analizi
- **Araçlar**: Git, Jupyter, Docker, CI/CD, modeller için sürüm kontrolü

## Yükselen Eğilimler

### Güncel Gelişmeler
- **AutoML**: Otomatik makine öğrenimi hattı oluşturma
- **MLOps**: Makine öğrenimi için DevOps uygulamaları
- **Feature Store'lar**: Merkezî özellik yönetimi
- **Veri Ağı**: Merkeziyetsiz veri mimarisi
- **LLM'ler ve Üretken Yapay Zekâ**: Büyük dil modelleri, içerik üretimi
- **Uç Analitiği**: Veriyi kaynak cihazlarda işleme
- **Gerçek Zamanlı Analitik**: Akış verisi analizi
- **Artırılmış Analitik**: Yapay zekâ destekli veri hazırlama ve içgörüler

### Gelecek Yönelimleri
- **Kuantum Makine Öğrenimi**: ML için kuantum hesaplama
- **Federated Learning**: Modelleri merkeziyetsiz veriler üzerinde eğitme
- **Nedensel Çıkarım**: Korelasyondan nedenselliğe geçiş
- **Sorumlu Yapay Zekâ**: Etik, açıklanabilirlik, şeffaflık
- **Veri Kumaşı**: Ortamlar arasında entegre veri yönetimi
