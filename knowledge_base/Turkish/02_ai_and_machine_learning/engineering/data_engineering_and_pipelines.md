<!--
---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Veri Mühendisliği ve Boru Hatları
Veri mühendisliği, verileri uygun ölçekte taşıyan, dönüştüren ve depolayan sistemleri oluşturma disiplinidir. Güvenilir veri hatları olmadan makine öğrenimi modelleri eğitilemez, gösterge tabloları eski rakamları gösterir ve iş kararları tahminlere dayalıdır. Bu dosya, çalışan veri altyapısı oluşturmaya yönelik mimariyi, araçları ve uygulamaları kapsar.
---

## ETL ve ELT
| Yaklaşım | Nasıl Çalışır | En İyisi | Araçlar |
|----------|----------------|----------|-------|
| **ETL** (Çıkart → Dönüştür → Yükle) | Verileri depoya yüklemeden *önce* dönüştürün | Sınırlı bilgi işlem kapasitesine sahip geleneksel depolar | Bilişim, Talend, Apache NiFi |
| **ELT** (Çıkart → Yükle → Dönüştür) | Önce ham verileri yükleyin; deponun *içini* dönüştürün | Esnek bilgi işlem özelliğine sahip modern bulut depoları | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
ETL'den ELT'ye geçiş, bilişimi depolamadan bağımsız olarak ölçeklendirebilen bulut veri ambarları (BigQuery, Snowflake, Redshift) tarafından sağlandı. Artık yüklemeden önce her şeyi önceden işlemeye gerek yok.
---

## Veri Gölleri ve Veri Ambarları
| Özellik | Veri Gölü | Veri Ambarı |
|-----------|---------------|---------------|
| **Veri Formatı** | Ham, yerel format (okunduğunda şema) | Yapılandırılmış, işlenmiş (yazma şeması) |
| **Şema** | Sorgu zamanında tanımlandı | Yüklemeden önce tanımlandı |
| **Veri Türleri** | Yapılandırılmış, yarı yapılandırılmış, yapılandırılmamış | Öncelikle yapılandırılmış |
| **Kullanıcılar** | Veri bilimcileri, mühendisler | İş analistleri, BI araçları |
| **Maliyet** | Daha ucuz depolama (nesne depolama) | Daha pahalı (sorgular için optimize edilmiş) |
| **Örnekler** | AWS S3, Azure Veri Gölü, GCS | Kar Tanesi, BigQuery, Kırmızıya Kayma |
Modern yaklaşım **göl evi**'dir: Gölün ucuz, esnek depolamasını bir deponun yönetim ve performans özellikleriyle birleştirir. Delta Lake, Apache Iceberg ve Apache Hudi buradaki anahtar teknolojilerdir.
---

## Boru Hattı Mimarisi
### Toplu ve Akış
| Modu | Açıklama | Gecikme | Kullanım Örneği |
|------|-------------|--------|----------|
| **Toplu** | Büyük parçalar halindeki verileri planlanmış aralıklarla işleyin | Dakikadan saate | Günlük raporlar, ETL işleri, veri zenginleştirme |
| **Akış** | Verileri geldikçe sürekli işleyin | Milisaniye için saniye | Gerçek zamanlı kontrol panelleri, dolandırıcılık tespiti, uyarılar |
| **Mikro-toplu** | Çok kısa aralıklarla küçük partiler | Saniye | Toplu işlem kolaylığıyla neredeyse gerçek zamanlı |
### Boru Hattı Bileşenleri
Tipik bir veri hattı şu aşamalara sahiptir:
| Sahne | Açıklama | Araçlar |
|----------|----------------|-------|
| **Yutma** | Kaynaklardan veri toplayın | Kafka, Airbyte, Fivetran, Debezium |
| **Dönüşüm** | Temizleyin, zenginleştirin, birleştirin | dbt, Spark, Pandalar |
| **Depolama** | İşlenmiş verilerin kalıcı olması | BigQuery, Kar Tanesi, S3, Delta Gölü |
| **Sunum yapılıyor** | Verileri tüketicilerin kullanımına sunun | API'ler, kontrol panelleri, makine öğrenimi özellik depoları |
| **Orkestrasyon** | Bağımlılıkları planlayın ve yönetin | Hava Akımı, Vali, Dagster |
| **İzleme** | Boru hattı sağlığını ve veri kalitesini izleyin | Büyük Umutlar, Monte Carlo, özel uyarılar |
---

## Düzenleme Araçları
| Araç | Yaklaşım | Güç |
|------|----------|----------|
| **Apache Hava Akışı** | Python tabanlı DAG'ler; endüstri standardı | Devasa ekosistem, olgun, esnek |
| **Prefect** | Python'a özgü; Airflow'tan daha temiz API | Modern tasarım, mükemmel hata yönetimi |
| **Hançer** | Varlık merkezli; yazılım mühendisliği yaklaşımı | Tip sistemi, test etme, gözlemlenebilirlik |
| **Luigi** | Spotify'ın orijinal ardışık düzen aracı | Basit ama daha az aktif olarak geliştirildi |
### Hava Akışı Örneği
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## Apaçi Kafka
Kafka birçok gerçek zamanlı veri sisteminin omurgasıdır. Yüksek verimli, hataya dayanıklı mesajlaşma sağlayan dağıtılmış bir olay günlüğüdür.
### Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Konu** | Bir mesaj kategorisi (ör.`orders`,`user-events`) |
| **Bölme** | Konular paralellik sağlamak amacıyla bölümlere ayrılmıştır |
| **Yapımcı** | Konulara mesaj yazan uygulama |
| **Tüketici** | Konulardaki mesajları okuyan uygulama |
| **Tüketici Grubu** | Bir konuyu okuma yükünü paylaşan tüketici grubu |
| **Ofset** | Bir bölüm içindeki tüketicinin konumu |
| **Komisyoncu** | Bir Kafka sunucu düğümü |
### Kafka Ne Zaman Kullanılmalı
- **Olay akışı**: Geniş ölçekte gerçek zamanlı olay işleme.
- **Ayırma hizmetleri**: Üreticilerin ve tüketicilerin birbirleri hakkında bilgi sahibi olmasına gerek yoktur.
- **Tekrar**: Mesajlar korunur; tüketiciler herhangi bir ofsetten yeniden okuyabilir.
- **Geri baskı**: Kafka, üreticiler ve tüketiciler arasındaki hız farklılıklarını doğal olarak ele alıyor.
---

## Veri Modelleme
### Yıldız Şeması ve Kar Tanesi Şeması
| Şema | Yapı | Artıları | Eksileri |
|----------|-----------|------|------|
| **Yıldız** | Normalleştirilmemiş boyut tablolarıyla çevrili merkezi olgu tablosu | Basit sorgular, hızlı okumalar | Veri artıklığı |
| **Kar tanesi** | Boyut tabloları normalleştirildi (alt tablolara bölündü) | Daha az artıklık | Daha fazla katılım, daha yavaş sorgular |
### Gerçek ve Boyut Tabloları
| Masa Tipi | İçerir | Örnek |
|-----------|----------|-----------|
| **Gerçek** | Ölçülebilir olaylar (metrikler) | `orders`(sipariş_kimliği, ürün_kimliği, müşteri_kimliği, tutar, tarih) |
| **Boyut** | Tanımlayıcı özellikler | `products`(ürün_kimliği, ad, kategori, fiyat),`customers`(müşteri_kimliği, ad, şehir) |
---

## Özellik Mağazaları
Özellik deposu, modellere girdi olarak kullanılan türetilmiş değerler (ör. "kullanıcının son 30 gündeki ortalama sipariş değeri") olan ML özelliklerinin merkezi bir deposudur.
| Yetenek | Açıklama |
|-----------|----------------|
| **Özellik Kaydı** | Meta verilerle birlikte kullanılabilir özelliklerin kataloğu |
| **Çevrimdışı Mağaza** | Model eğitiminin tarihsel özellikleri (toplu) |
| **Çevrimiçi Mağaza** | Gerçek zamanlı çıkarım için hizmet veren düşük gecikmeli özellik |
| **Özellik İzleme** | Sapmayı, eksik değerleri, dağıtım değişikliklerini tespit edin |
| Araç | Açıklama |
|------|-----------------|
| **bayram** | Açık kaynak; herhangi bir makine öğrenimi çerçevesiyle çalışır |
| **Tekton** | Reklam; gerçek zamanlı özellik platformu |
| **Şerbetçiotu** | Açık kaynak; özellik deposuyla tam makine öğrenimi platformu |
| **Databricks Özellik Mağazası** | Databricks/Spark ile entegre |
---

## Veri Kalitesi
Veri kalitesi, makine öğrenimi projelerinin sessiz katilidir. Çöp içeri, çöp dışarı.
### Kalite Boyutları
| Boyut | Soru |
|---------------|----------|
| **Doğruluk** | Veriler gerçeği yansıtıyor mu? |
| **Bütünlük** | Gerekli alanlar doldurulmuş mu? |
| **Tutarlılık** | Değerler kaynaklar arasında aynı fikirde mi? |
| **Zamanındalık** | Veriler güncel mi? |
| **Geçerlilik** | Değerler tanımlanmış kurallara uyuyor mu? |
| **Benzersizlik** | Yinelenen kayıtlar var mı? |
### Veri Kalitesi Araçları
| Araç | Yaklaşım |
|----------|----------|
| **Büyük Beklentiler** | Python tabanlı; verilerle ilgili "beklentileri" tanımlayın |
| **Monte Carlo** | ML destekli veri gözlemlenebilirlik platformu |
| **dbt testleri** | Ambar verilerine yönelik yerleşik testler (benzersiz, boş değil, ilişkiler) |
| **Soda** | Açık kaynaklı veri kalitesi taraması |
---

## Veri Yönetişimi
Veri yönetişimi, verilerin kuruluş genelinde sorumlu bir şekilde yönetilmesini sağlar.
| Alan | Açıklama |
|------|-----------------|
| **Veri Kataloğu** | Meta veriler içeren veri kümelerinin aranabilir envanteri (Amundsen, DataHub, Atlan) |
| **Veri Kökeni** | Verilerin nereden geldiğini ve nasıl dönüştüğünü takip edin |
| **Erişim Kontrolü** | Rol tabanlı izinler; kim neyi okuyabilir/yazabilir |
| **Uyumluluk** | GDPR, CCPA, HIPAA uyumu |
| **Veri Sahipliği** | Her veri kümesinin sahipliğini temizleyin (yönetim) |
| **Saklama Politikaları** | Verilerin ne kadar süre saklanacağını ve ne zaman silineceğini tanımlayın |
---

## Modern Veri Yığını
"Modern veri yığını", günümüzde veri ekipleri tarafından kullanılan araçların tipik kombinasyonunu ifade eder:
| Katman | Tipik Araçlar |
|----------|----------------|
| **Yutma** | Fivetran, Airbyte |
| **Depo** | Kar Tanesi, BigQuery, Kırmızıya Kayma |
| **Dönüşüm** | dbt |
| **Orkestrasyon** | Hava Akımı, Vali, Dagster |
| **BI / Görselleştirme** | Looker, Metatabanı, Tablo |
| **Ters ETL** | Census, Hightouch (depo verilerini araçlarla senkronize edin) |
| **Veri Kalitesi** | Büyük Umutlar, Monte Carlo |
Trend, yekpare platformlar yerine açık standartlarla (SQL, dbt modelleri, Airflow DAG'ler) bağlanan modüler, türünün en iyisi araçlara yöneliyor.