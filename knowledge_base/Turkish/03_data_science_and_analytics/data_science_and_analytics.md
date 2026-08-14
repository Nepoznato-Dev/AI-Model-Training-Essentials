<!--
---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Veri Bilimi ve Analitik
Veri bilimi, ham verileri eyleme dönüştürülebilir içgörülere dönüştürme disiplinidir. İstatistik, bilgisayar bilimi ve alan uzmanlığının kesişim noktasında yer alır ve finanstan sağlık hizmetlerine kadar her sektörde vazgeçilmez hale gelmiştir. Bu dosyada her uygulayıcının bilmesi gereken temel kavramlar, araçlar ve iş akışları anlatılmaktadır.
---

## Veri Bilimi Süreci
Çoğu proje, endüstri standardı yaşam döngüsü olan **CRISP-DM**'nin bazı varyasyonlarını takip eder:
| Aşama | Ne Olur | Tipik Zaman |
|----------|----------------|-------------|
| **İş Anlayışı** | Hedefleri, başarı ölçütlerini ve kısıtlamaları tanımlayın | %10–15 |
| **Veri Anlama** | Verileri toplayın, keşfedin ve profilini çıkarın | %10–15 |
| **Veri Hazırlama** | Özellikleri temizleyin, dönüştürün, tasarlayın | ~%50–60 |
| **Modelleme** | Modelleri seçin ve eğitin | %10–15 |
| **Değerlendirme** | Performansı iş hedeflerine göre değerlendirin | %5–10 |
| **Dağıtım** | Modeli üretime gönderin | %5–10 |
Veri hazırlamanın, özellikle de veri temizlemenin, bir veri bilimcinin zamanının yaklaşık %80'ini harcadığı tahmin edilmektedir.
---

## Bir Bakışta Veri Türleri
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Yapılandırılmış** | Satır ve sütunlar halinde düzenlenmiştir | SQL tabloları, elektronik tablolar |
| **Yapılandırılmamış** | Önceden tanımlanmış format yok | Metin, resimler, ses, video |
| **Yarı yapılandırılmış** | Biraz organizasyon ama esnek | JSON, XML, HTML |
| **Zaman serisi** | Zamana göre indekslenen sıralı veriler | Hisse senedi fiyatları, sensör okumaları |
| **Uzaysal** | Coğrafi veya konuma dayalı | GPS koordinatları, harita verileri |
| **Grafik** | İlişkileri temsil eden düğümler ve kenarlar | Sosyal ağlar, bilgi grafikleri |
---

## İstatistiğin Temelleri
### Tanımlayıcı ve Çıkarımsal İstatistikler
Tanımlayıcı istatistikler *sahip olduklarınızı* özetler; Çıkarımsal istatistikler, *sahip olmadıklarınız* (daha geniş nüfus) hakkında sonuçlar çıkarmanıza olanak tanır.
| Konsept | Temel Fikirler |
|-----------|-----------|
| **Merkezi eğilim** | Ortalama (aykırı değerlere duyarlı), medyan (sağlam), mod (en sık) |
| **Dağılma** | Aralık, varyans, standart sapma, çeyrekler arası aralık |
| **Dağıtım şekli** | Çarpıklık (asimetri), basıklık (kuyruk ağırlığı) |
| **Hipotez testi** | Boş ve alternatif hipotez, p değerleri, anlamlılık düzeyi (α) |
| **Güven aralıkları** | Büyük olasılıkla gerçek popülasyon parametresini içeren aralık |
| **Tip I / Tip II hataları** | Yanlış pozitif (gerçek bir boş değerin reddedilmesi) / yanlış negatif (gerçek bir etkinin kaçırılması) |
### Ortak İstatistik Testleri
| Testi | Ne Zaman Kullanılmalı |
|------|-----------------|
| **t-testi** | İki grup arasındaki ortalamaları karşılaştırın |
| **ANOVA** | Üç veya daha fazla gruptaki ortalamaları karşılaştırın |
| **Ki-kare** | Kategorik değişkenlerin bağımsızlığını test edin |
| **Mann-Whitney U** | T-testinin parametrik olmayan alternatifi (normallik varsayımı yoktur) |
| **Pearson korelasyonu** | İki sürekli değişken arasındaki doğrusal ilişki |
| **Spearman korelasyonu** | Monotonik ilişki (sıralamaya dayalı, daha sağlam) |
### Bilmeye Değer Olasılık Dağılımları
| Dağıtım | Kullanım Örneği |
|---------------|----------|
| **Normal** | Doğa olayları, ölçüm hataları — klasik çan eğrisi |
| **Binom** | Başarı/başarısızlık sayıları (yazı-turalar, dönüşüm oranları) |
| **Poisson** | Sabit bir aralıktaki olay sayıları (saat başına çağrı, toplu iş başına kusur) |
| **Üstel** | Olaylar arasındaki süre (bekleme süreleri, arıza aralıkları) |
| **t-Dağıtım** | Küçük örnekler veya bilinmeyen popülasyon varyansı |
| **Ki-kare** | Kategorik veri analizi, uyum iyiliği testleri |
---

## Veri Toplama ve Depolama
### Veriler Nereden Geliyor?
Gerçek dünya verileri birçok kaynaktan gelir: ilişkisel veritabanları, API'ler (REST, GraphQL), düz dosyalar (CSV, JSON, Parquet), akış platformları (Kafka, Kinesis), anketler ve halka açık depolar (Kaggle, devlet portalları). Aldığınız format, ön işleme stratejinizin çoğunu belirler.
### Veri Depolama Kavramları
| Konsept | Açıklama |
|-----------|------------|
| **ETL** | Çıkart → Dönüştür → Yükle — geleneksel boru hattı yaklaşımı |
| **ELT** | Çıkart → Yükle → Dönüştür — modern bulut yaklaşımı (ham yükleme, depoda dönüştürme) |
| **Veri Gölü** | Yerel formatta saklanan ham veriler (okunduğunda şema) |
| **Veri Ambarı** | Analiz için optimize edilmiş yapılandırılmış, işlenmiş veriler (yazma şeması) |
| **Veri Pazarı** | Kapsamı tek bir departman veya etki alanı olan bir deponun alt kümesi |
| **Yıldız Şeması** | Boyut tablolarıyla çevrili merkezi olgu tablosu |
| **Kar Tanesi Şeması** | Normalleştirilmiş boyut tabloları (daha az artıklık, daha fazla birleştirme) |
### Veritabanı Türleri
| Tür | Örnekler | En İyisi |
|------|----------|----------|
| **İlişkisel (SQL)** | PostgreSQL, MySQL, Oracle | Yapılandırılmış veriler, ACID işlemleri |
| **Belge** | MongoDB, CouchDB | Esnek şemalar, JSON benzeri veriler |
| **Anahtar/Değer** | Redis, DynamoDB | Önbelleğe alma, oturumlar, basit aramalar |
| **Sütun Ailesi** | Cassandra, HBase | Yazma ağırlıklı iş yükleri, zaman serileri |
| **Grafik** | Neo4j, Amazon Neptün | İlişkiler, sosyal ağlar |
| **Zaman Serisi** | InfluxDB, TimescaleDB | IoT ölçümleri, izleme |
| **Vektör** | Çam kozalağı, Milvus | ML/AI araması için depolamayı yerleştirme |
---

## Veri Ön İşleme ve Özellik Mühendisliği
### Temizleme Kontrol Listesi
Her gerçek veri kümesinin sorunları vardır. İşte standart temizleme:
| Sayı | Yaklaşım |
|----------|----------|
| **Eksik değerler** | Atama (ortalama, medyan, tahmin) veya seyrekse silme |
| **Aykırı Değerler** | IQR veya Z-skoruyla tespit edin; kapatma veya dönüşümle işleme |
| **Kopyalar** | Tanımla ve kaldır |
| **Tutarsızlıklar** | Formatları standartlaştırın, yazım hatalarını düzeltin, birimleri normalleştirin |
### Dönüşüm Teknikleri
| Tekniği | Ne İşe Yarar |
|-----------|----------------|
| **Normalleşme** | Değerleri 0–1 aralığına ölçeklendirir |
| **Standartlaştırma** | Z-puanı: ortalama = 0, std = 1 |
| **Tek seferde kodlama** | Kategorileri ikili sütunlara dönüştürür |
| **Etiket kodlaması** | Tamsayı etiketlerini kategorilere atar |
| **Günlük dönüşümü** | Verilerdeki sağa çarpıklığı azaltır |
| **Bölme** | Sürekli değerleri ayrı gruplar halinde gruplandırır |
### Özellik Mühendisliği
Özellik mühendisliği genellikle vasat bir model ile harika bir model arasındaki farktır. Anahtar teknikler şunları içerir:
- **Özellik oluşturma**: Mevcut sütunlardan yeni sütunlar türetme (örneğin, `age`'den `age_group`).
- **Özellik seçimi**: Filtre yöntemleri (korelasyon), sarma yöntemleri (özyinelemeli eleme), gömülü yöntemler (LASSO, ağaç önemi).
- **Boyutsallık azaltma**: Doğrusal için PCA, görselleştirme için t-SNE veya UMAP.
- **Etkileşim terimleri**: Ortak etkileri yakalamak için özelliklerin çarpımsal olarak birleştirilmesi.
---

## Keşif Amaçlı Veri Analizi (EDA)
EDA, modellemeden önce verileriniz hakkında sezgi geliştirdiğiniz yerdir. Amaç kalıpları, anormallikleri ve ilişkileri tespit etmektir.
### Doğru Grafiği Seçmek
| Grafik Türü | En İyisi |
|---------------|----------|
| **Histogram** | Tek bir değişkenin dağılımı |
| **Kutu grafiği** | Beş rakamlı özet, aykırı değer tespiti |
| **Dağılım grafiği** | İki sürekli değişken arasındaki ilişki |
| **Isı haritası** | Korelasyon matrisleri, yoğunluk görselleştirmesi |
| **Çubuk grafik** | Kategorileri karşılaştırma |
| **Çizgi grafiği** | Zaman içindeki eğilimler |
| **Keman konusu** | Dağıtım yoğunluğu + kutu grafiği özeti |
| **Çift grafiği** | Tüm değişken çiftlerine hızlı genel bakış |
### Python EDA Yığını
| Kütüphane | Rol |
|-----------|------|
| **pandalar** | Veri manipülasyonu ve analizi |
| **numpy** | Sayısal hesaplama |
| **matplotlib** | Temel çizimi |
| **deniz doğumlu** | İstatistiksel görselleştirme (matplotlib üzerine kurulmuştur) |
| **komplo** | Etkileşimli, web tabanlı görselleştirmeler |
| **scipy** | Bilimsel hesaplama ve istatistik |
---

## Veri Biliminde Makine Öğrenimi
### Bir Bakışta Denetimli Öğrenme
| Görev | Algoritmalar |
|------|---------------|
| **Regresyon** (bir sayı tahmin edin) | Doğrusal, Sırt/LASSO, Karar Ağacı, Rastgele Orman, Gradyan Arttırma (XGBoost, LightGBM) |
| **Sınıflandırma** (bir kategori tahmin edin) | Lojistik Regresyon, k-NN, Naive Bayes, SVM, Karar Ağaçları, Rastgele Orman, Sinir Ağları |
### Bir Bakışta Denetimsiz Öğrenme
| Görev | Algoritmalar |
|------|---------------|
| **Kümelenme** | k-Ortalamalar, Hiyerarşik, DBSCAN, Gauss Karışım Modelleri |
| **Boyutsallığın Azaltılması** | PCA, t-SNE, UMAP, Otomatik Kodlayıcılar |
| **İlişkilendirme Kuralları** | Apriori, FP-Büyüme |
### Model Değerlendirmesi
| Metrik Türü | Temel Metrikler |
|------------|------------|
| **Sınıflandırma** | Doğruluk, hassasiyet, geri çağırma, F1 puanı, ROC-AUC, karışıklık matrisi |
| **Regresyon** | MAE, MSE, RMSE, R², Düzeltilmiş R² |
| **Doğrulama** | k-katlı çapraz doğrulama, katmanlı, zaman serisi bölünmüş |
| **Ayarlama** | Izgara araması, rastgele arama, Bayes optimizasyonu |
---

## Büyük Veri Teknolojileri
Veri kümeleri tek bir makinenin işleyebileceğini aştığında, dağıtılmış bilgi işlem devreye girer.
| Çerçeve | Güç |
|---------------|----------|
| **Apache Spark** | Bellek içi işleme; Spark SQL, Akış, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — orijinal büyük veri yığını |
| **Apache Flink** | Düşük gecikmeli akış işleme |
| **Apache Işını** | Birleşik toplu iş ve akış modeli |
### Bulut Veri Platformları
| Sağlayıcı | Anahtar Hizmetler |
|----------|----------------|
| **AWS** | S3, EMR, Kırmızıya Kayma, SageMaker, Tutkal |
| **Google Bulut** | BigQuery, Dataproc, Yapay Zeka Platformu, Bulut Depolama |
| **Azure** | Synapse Analytics, Databricks, Makine Öğrenimi, Veri Gölü |
| **Kar tanesi** | Bulutta yerel veri ambarı (sağlayıcıdan bağımsız) |
### Boru Hattı Düzenlemesi
| Araç | Notlar |
|------|----------|
| **Apache Hava Akışı** | Endüstri standardı; Python tabanlı DAG'ler |
| **Prefect** | Temizleyici API ile modern alternatif |
| **Hançer** | Varlık merkezli orkestrasyon |
| **dbt** | Depoda SQL'de ilk veri dönüşümü |
---

## İş Zekası ve Analitik
### BI Araçları Karşılaştırıldı
| Araç | Tür | Güç |
|------|----------|----------|
| **Tablo** | Ticari | Zengin görsel analiz, sürükle ve bırak |
| **Power BI** | Ticari (Microsoft) | Derin Ofis/Azure entegrasyonu |
| **Bakıcı** | Ticari (Google) | Veri araştırması, LookML modelleme |
| **Metatabanı** | Açık kaynak | Kolay kurulum, SQL'de yerel |
| **Süper set** | Açık kaynak (Apache) | Ölçeklenebilir, SQL öncelikli |
### Kontrol Paneli Tasarım İlkeleri
Etkili gösterge tabloları yerleşik ilkeleri takip eder: hedef kitleyi belirleyin, her metrik için uygun görselleştirmeyi seçin, rengi stratejik olarak kullanın (dekoratif olarak değil), tutarlı ölçekleri koruyun ve etkileşimi etkinleştirin (filtreler, ayrıntılı incelemeler). Performans da önemlidir; yavaş yükleme süreli gösterge tabloları kullanıcıların benimsemesini azaltır.
### Ortak KPI Kategorileri
| Kategori | Örnekler |
|----------|-----------|
| **Finansal** | Gelir, kar marjı, yatırım getirisi, müşteri yaşam boyu değeri |
| **Müşteri** | Edinme maliyeti (CAC), kayıp oranı, NPS, memnuniyet puanı |
| **Operasyonel** | Verimlilik oranları, çevrim süresi, kusur oranları |
| **Pazarlama** | Dönüşüm oranı, tıklama oranı, ROAS, ilişkilendirme |
| **Ürün** | Günlük aktif kullanıcılar, katılım, elde tutma, özelliklerin benimsenmesi |
---

## Gelişmiş Analiz
| Yaklaşım | Teknikleri | Ne Zaman Kullanılmalı |
|----------|-----------|------------|
| **Tahmin edici** | Zaman serileri (ARIMA, Prophet, LSTM), risk modelleme, kayıp tahmini | Gelecekteki değerlerin tahmini |
| **kuralcı** | Doğrusal programlama, Monte Carlo simülasyonu, A/B testi, çok kollu haydutlar | Kararları optimize etme |
| **Metin Analizi** | Tokenleştirme, duyarlılık analizi, konu modelleme (LDA), NER, kelime yerleştirmeler (Word2Vec, BERT) | Metinden içgörü çıkarma |
---

## Veri Etiği ve Yönetişim
### Gizlilik Düzenlemeleri
| Yönetmelik | Kapsam |
|-----------|----------|
| **GDPR** | AB veri sahipleri; silme hakkı, rıza, veri taşınabilirliği |
| **CCPA** | Kaliforniya tüketicileri; veri satışlarından vazgeçme |
| **HIPAA** | ABD sağlık verileri; katı gizlilik kuralları |
### Veri Kalitesi Boyutları
| Boyut | Soru |
|---------------|----------|
| **Doğruluk** | Veriler doğru mu? |
| **Bütünlük** | Eksik bir şey var mı? |
| **Tutarlılık** | Kaynaklar aynı fikirde mi? |
| **Zamanındalık** | Güncel mi? |
| **Geçerlilik** | Beklenen formatlara uyuyor mu? |
| **Benzersizlik** | Kopyalar var mı? |
### Önyargı ve Adillik
Önyargı herhangi bir aşamada ortaya çıkabilir: örnekleme yanlılığı (temsili olmayan veriler), ölçüm yanlılığı (kusurlu araçlar) veya algoritmik yanlılık (ayrımcı tahminler). Azaltma stratejileri arasında ön işleme (verilerin düzeltilmesi), işlem sırasında (modelin kısıtlanması) ve işlem sonrası (çıktıların ayarlanması) yer alır. Demografik eşitlik ve fırsat eşitliği gibi adalet ölçümleri sorunun ölçülmesine yardımcı olur.
---

## Kariyer Yolları
| Rol | Odaklanma |
|------|----------|
| **Veri Analisti** | Tanımlayıcı analizler, kontrol panelleri, raporlama |
| **Veri Bilimcisi** | İstatistiksel modelleme, makine öğrenimi, ileri analitik |
| **ML Mühendisi** | Üretim makine öğrenimi sistemleri, model dağıtımı, MLOps |
| **Veri Mühendisi** | Veri hatları, altyapı, ETL |
| **Analiz Yöneticisi** | Takım liderliği, strateji, paydaş yönetimi |
| **Araştırmacı Bilim Adamı** | Yeni algoritmalar, yayınlar |
---

## Yükselen Trendler
- **AutoML**: Otomatik ardışık düzen oluşturma ve model seçimi.
- **MLOps**: ML yaşam döngüsü yönetimine uygulanan DevOps uygulamaları.
- **Özellik Mağazaları**: Ekipler arasında yeniden kullanım için merkezi özellik yönetimi.
- **Veri Ağı**: Merkezi olmayan, etki alanına ait veri mimarisi.
- **LLM'ler ve Üretken Yapay Zeka**: Metin, kod ve görüntü iş akışlarını dönüştüren büyük dil modelleri.
- **Edge Analytics**: Verilerin bulut yerine cihazda işlenmesi.
- **Nedensel Çıkarım**: Gerçek neden ve sonucu anlamak için korelasyonun ötesine geçmek.
- **Birleşik Öğrenme**: Modelleri merkezi olmayan veriler üzerinde, taşımadan eğitme.
- **Sorumlu yapay zeka**: Etik, açıklanabilirlik ve şeffaflık standart gereksinimler haline geliyor.