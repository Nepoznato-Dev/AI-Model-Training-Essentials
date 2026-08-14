---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, engineering, mlops, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# ML Mühendisliği ve MLOps
Bir makine öğrenimi modeli oluşturmak savaşın yalnızca yarısıdır. Üretime almak, güvenilir bir şekilde çalışmasını sağlamak, sapmaları izlemek ve yinelemek; makine öğrenimi mühendisliği ve MLOps'un devreye girdiği yer burasıdır. Bu dosya, denemeden üretim sistemine kadar tüm yaşam döngüsünü kapsar.
---

## ML Yaşam Döngüsü
| Aşama | Açıklama | Temel Faaliyetler |
|----------|----------------|---------------|
| **1. Sorun Tanımı** | İş sorununu bir makine öğrenimi görevi olarak çerçeveleyin | Metrikleri, kısıtlamaları ve başarı kriterlerini tanımlayın |
| **2. Veri Toplama** | Eğitim verilerini toplayın ve etiketleyin | ETL, etiketleme, büyütme |
| **3. Deney** | Modelleri eğitin ve değerlendirin | Özellik mühendisliği, hiperparametre ayarı |
| **4. Model Seçimi** | En iyi modeli seçin | Ölçütleri karşılaştırın, dengeleri değerlendirin |
| **5. Dağıtım** | Modeli üretime gönderin | Hizmet altyapısı, API, toplu |
| **6. İzleme** | Sürüklenme ve bozulmaya dikkat edin | Veri kayması, kavram kayması, performans |
| **7. Yeniden eğitim** | Modeli yeni verilerle güncelleyin | Planlanmış veya tetiklenen yeniden eğitim |
Değerin (ve zorluğun) çoğu 5-7. Aşamalardadır. Jupyter not defterinde duran bir model iş değeri yaratmaz.
---

## Model Servis Kalıpları
| Desen | Açıklama | Gecikme | Kullanım Örneği |
|-----------|------------|------------|----------|
| **Toplu Çıkarım** | Modeli bir zamanlamaya göre bir dizi veri üzerinde çalıştırın | Saat | Günlük öneriler, dolandırıcılık puanlaması |
| **Çevrimiçi Çıkarım** | İstek başına gerçek zamanlı tahmin | Milisaniye | Arama sıralaması, gerçek zamanlı sınıflandırma |
| **Akış Çıkarımı** | Veri akışında süreç tahminleri | Saniye | Anormallik tespiti, olay işleme |
### Hizmet Altyapısı
| Araç | Tür | En İyisi |
|------|----------|----------|
| **TensorFlow Sunumu** | Model sunucusu | TensorFlow modelleri |
| **Meşale Hizmeti** | Model sunucusu | PyTorch modelleri |
| **Triton Çıkarım Sunucusu** | Çoklu çerçeve | GPU çıkarımı, çoklu çerçeveler |
| **vLLM** | Yüksek Lisans hizmeti | Yüksek verimli LLM çıkarımı |
| **BentoML** | Birleşik sunum | Çerçeveden bağımsız dağıtım |
| **Seldon** | K8s-yerli | Kubernetes model dağıtımı |
| **Ray Hizmeti** | Ölçeklenebilir sunum | Büyük modeller, dağıtılmış çıkarım |
---

## Model Kayıtları
Model kaydı, makine öğrenimi modellerinin (sürümleri, meta verileri, ölçümleri ve dağıtım durumu) yönetilmesine yönelik merkezi bir depodur.
| Yetenek | Açıklama |
|-----------|----------------|
| **Sürüm oluşturma** | Her model sürümünü benzersiz kimlikle takip edin |
| **Meta veriler** | Eğitim verileri, hiperparametreler, ölçümler, yazar |
| **Sahne Geçişleri** | Modelleri aşamalar arasında taşıyın: Aşamalandırma → Üretim → Arşivlendi |
| **Soy** | Her modelin hangi veri ve kodu ürettiğini takip edin |
| Araç | Açıklama |
|------|-----------------|
| **ML akışı** | Açık kaynak; model kaydı + deneme takibi |
| **Ağırlıklar ve Sapmalar (W&B)** | Reklam; deneme izleme + model kaydı |
| **DVC** | Git ile veri ve model sürüm oluşturma |
| **Azure ML / SageMaker** | Bulutta yerel model yönetimi |
---

## Deneme Takibi
Her makine öğrenimi denemesi izlenmelidir: hangi veriler kullanıldı, hangi hiper parametreler, hangi ölçümler sonuçlandı.
| Araç | Temel Özellikler |
|------|-----------------|
| **ML akışı** | Açık kaynaklı, kendi kendine barındırılan, parametreleri/ölçümleri/yapıları izler |
| **W&B** | Zengin kullanıcı arayüzü, taramalar, yapay sürüm oluşturma, raporlar |
| **Neptün** | MLOps için meta veri deposu |
| **TensorBoard** | TensorFlow'a yerleşik; antrenman eğrilerini görselleştirin |
### Ne Takip Edilmeli
| Kategori | Örnekler |
|----------|-----------|
| **Parametreler** | Öğrenme oranı, parti büyüklüğü, model mimarisi, çağ sayısı |
| **Metrikler** | Doğruluk, kayıp, F1, AUC-ROC (dönem başına ve son) |
| **Yapılar** | Model ağırlıkları, karışıklık matrisleri, tahmin örnekleri |
| **Veri** | Veri kümesi sürümü, bölünmüş oranlar, ön işleme adımları |
| **Çevre** | Python sürümü, kütüphane sürümleri, donanım |
---

## Model Dağıtım Stratejileri
| Strateji | Nasıl Çalışır | Risk |
|----------|----------------|------|
| **Gölge Dağıtımı** | Yeni model eskisinin yanında çalışır; tahminler karşılaştırıldı ancak yayınlanmadı | Sıfır risk; yayına geçmeden önce doğrulanır |
| **Kanarya Sürümü** | Trafiğin küçük bir yüzdesini yeni modele yönlendirin; kademeli olarak artırın | Düşük risk; hızlı geri alma |
| **A/B Testi** | Kullanıcıları eski ve yeni arasında ayırın; iş ölçümlerini karşılaştırın | Gerçek etkiyi ölçer |
| **Mavi-Yeşil** | İki özdeş ortam; tüm trafiği aynı anda değiştirin | Anında geri alma; geçiş sırasında iki kat maliyet |
| **Özellik Bayrakları** | Kullanıcı segmentine göre modeli açma/kapama | İnce taneli kontrol |
---

## ML Sistemlerini İzleme
ML sistemleri, verilerin kendisi değişebileceği için geleneksel yazılımlara göre daha fazla izlemeye ihtiyaç duyar.
### Drift Türleri
| Drift Türü | Neler Değişiyor | Örnek |
|-----------|----------------|-----------|
| **Veri Kayması** | Giriş dağıtımı değişiklikleri | Müşteri demografik özellikleri bir pazarlama kampanyası sonrasında değişiyor |
| **Konsept Drift** | Giriş ve çıkış değişiklikleri arasındaki ilişki | Ekonomik durgunluk sırasında tüketici davranışı değişiyor |
| **Etiket Kayması** | Hedef dağılım değişiklikleri | Dolandırıcılık oranı %1'den %5'e çıktı |
### Neler İzlenmeli
| Kategori | Metrikler |
|----------|-----------|
| **Model Performansı** | Doğruluk, kesinlik, geri çağırma, F1, AUC (taban çizgisiyle karşılaştırıldığında) |
| **Veri Kalitesi** | Eksik değerler, özellik dağılımları, aykırı değerler |
| **Sürüklenme Algılama** | İstatistiksel testler (KS testi, PSI, KL sapması) |
| **Altyapı** | Gecikme, verim, GPU kullanımı, bellek |
| **İş Metrikleri** | Dönüşüm oranı, gelir etkisi, kullanıcı memnuniyeti |
### İzleme Araçları
| Araç | Tür |
|------|------|
| **Açıkçası AI** | Açık kaynaklı veri kayması ve model performansı izleme |
| **Grafana** | Kontrol paneli görselleştirmesi (Prometheus ile çalışır) |
| **NedenLabs** | Veri gözlemlenebilirlik platformu |
| **Arize** | ML gözlemlenebilirliği ve temel neden analizi |
| **Prometheus + Grafana** | Altyapı ve uygulama ölçümleri |
---

## Tekrarlanabilir Eğitim
Tekrarlanabilirlik, bir deneyi yeniden çalıştırıp aynı sonucu elde edebileceğiniz anlamına gelir. Hata ayıklama, denetim ve uyumluluk için gereklidir.
### Gereksinimler
| Gereksinim | Bunu Nasıl Başarırsınız |
|---------------|-----------|
| **Veri sürümü oluşturma** | DVC, Delta Lake veya hash'li veri kümesi anlık görüntüleri |
| **Kod sürümü oluşturma** | Tüm eğitim kodları için Git |
| **Ortam sabitleme** | `requirements.txt`,`conda env`, Tam sürümlerle Docker görüntüleri |
| **Tohum ayarı** | Numpy, meşale, tensorflow için rastgele tohumları düzeltin |
| **Yapılandırma yönetimi** | Tüm hiperparametreler için Hydra, OmegaConf veya YAML yapılandırmaları |
| **Yapı takibi** | Her deneyi günlüğe kaydetmek için MLflow veya W&B |
---

## Ölçekleme Çıkarımı
Bir modelin günde milyonlarca isteğe hizmet vermesi gerektiğinde performans önemlidir.
| Tekniği | Açıklama |
|-----------|----------------|
| **Toplama** | Birden fazla isteği tek bir ileri geçişte gruplayın |
| **Kuantizasyon** | Daha hızlı çıkarım için model hassasiyetini azaltın (FP32 → INT8 veya INT4) |
| **Model Damıtma** | Daha büyük bir modeli taklit etmek için daha küçük bir modeli eğitin |
| **Budama** | Önemsiz ağırlıkları veya nöronları kaldırın |
| **Önbelleğe alma** | Yeniden hesaplamayı önlemek için sık tahminleri önbelleğe alın |
| **GPU Optimizasyonu** | TensorRT, ONNX Çalışma Zamanı, Flash Dikkati |
| **Yatay Ölçeklendirme** | Bir yük dengeleyicinin arkasında birden çok model replikası çalıştırın |
---

## ML için Özellik Bayrakları
Özellik bayrakları, yeniden dağıtım yapmadan hangi model sürümünün hangi kullanıcılara hizmet vereceğini kontrol etmenize olanak tanır.
| Kullanım Örneği | Açıklama |
|----------|----------------|
| **Kademeli kullanıma sunma** | Yeni modeli kullanıcıların %5'ine sunun, ardından artırın |
| **Kilitleme anahtarı** | Sorun tespit edilirse anında önceki modele dönün |
| **Segment bazlı** | Farklı kullanıcı segmentlerine yönelik farklı modeller |
| **Deney** | İş ölçümlerine sahip A/B testi modeli çeşitleri |
Araçlar: LaunchDarkly, Unleash, Flagsmith veya basit veritabanı destekli özellik bayrakları.
---

## MLOps Olgunluk Eğrisi
| Seviye | Özellikler |
|----------|----------------|
| **Seviye 0 — Manuel** | Manuel eğitim, manuel dağıtım, izleme yok |
| **Seviye 1 — Deney** | Deney izleme, model kaydı, temel CI |
| **Seviye 2 — Otomasyon** | Otomatik yeniden eğitim, modeller için CI/CD, otomatik test |
| **Seviye 3 — Tam Boru Hattı** | İzleme, sapma tespiti ve otomatik yeniden eğitim ile uçtan uca otomatik işlem hattı |
Çoğu kuruluş Düzey 0 ile Düzey 1 arasında bir yerdedir. Hedef, ML yaşam döngüsünün otomatikleştirildiği ve kendi kendini iyileştirdiği Düzey 2-3'tür.