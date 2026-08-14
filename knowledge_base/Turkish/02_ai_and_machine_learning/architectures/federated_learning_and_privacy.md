<!--
---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
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
# Birleşik Öğrenim ve Gizlilik
Birleşik öğrenme, ham verileri paylaşmadan birden fazla cihaz veya kuruluşta makine öğrenimi modellerini eğitmeye yönelik bir tekniktir. Verileri merkezi bir sunucuya göndermek yerine, her cihaz yerel bir modeli eğitir ve yalnızca model güncellemelerini (gradyanlar veya ağırlıklar) paylaşır. Merkezi sunucu, global bir model oluşturmak için bu güncellemeleri bir araya getirir. Google tarafından Android telefonlarda klavye dili modellerini eğitmek için tasarlandı ve o zamandan beri gizliliği koruyan yapay zeka için önemli bir teknik haline geldi.
---

## Neden Birleşik Öğrenme?
| Motivasyon | Açıklama | Örnek |
|------------|------------|------------|
| **Veri gizliliği** | Ham veriler asla cihazdan ayrılmaz | Tıbbi kayıtlar hastanede kalır; fotoğraflar telefonda kal |
| **Yasal uyumluluk** | GDPR, HIPAA ve diğer düzenlemeler veri paylaşımını kısıtlıyor | Bankalar müşteri verilerini paylaşmadan işbirliği yapabilir |
| **Veri hacmi** | Verileri taşımak pahalı ve yavaştır | Verilerin yüklenmesi gerekiyorsa milyarlarca telefon üzerinde eğitim verilmesi pratik değildir |
| **Veri hassasiyeti** | Bazı veriler izin alınsa dahi paylaşılamayacak kadar hassastır | Hükümet istihbaratı; kişisel sağlık verileri |
---

## Birleşik Öğrenim Nasıl Çalışır?
### Temel Protokol (FedAvg)
| Adım | Ne Olur |
|------|-----------------|
| **1. Başlatma** | Merkezi sunucu, rastgele ağırlıklara sahip küresel bir model oluşturur |
| **2. Dağıt** | Sunucu geçerli global modeli seçilen cihazlara gönderir |
| **3. Yerel eğitim** | Her cihaz, modeli birkaç dönem için yerel verileriyle eğitir |
| **4. Yükle** | Cihazlar güncellenmiş model ağırlıklarını (verileri değil) sunucuya geri gönderir |
| **5. Toplam** | Sunucu, yeni bir küresel model oluşturmak için ağırlıkların ortalamasını (Birleştirilmiş Ortalama) alır |
| **6. Tekrarla** | Model yakınsayana kadar 2. adıma geri dönün |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Anahtar Özellikler
| Emlak | Açıklama |
|----------|----------------|
| **IID olmayan veriler** | Her cihazın farklı veri dağıtımları vardır (bağımsız değildir ve aynı şekilde dağıtılmıştır) |
| **Dengesiz veriler** | Bazı cihazlarda çok fazla veri bulunurken bazılarında çok az veri bulunur |
| **Kısmi katılım** | Her turda tüm cihazlar mevcut değildir |
| **İletişim verimliliği** | Darboğaz hesaplama değil iletişimdir |
---

## Birleşik Öğrenme Varyantları
| Varyant | Açıklama | Avantajı |
|-----------|---------------|-----------|
| **FedOrtalama** | Cihazlar arası ortalama model ağırlıkları | Basit; IID verileri için iyi çalışır |
| **FedProx** | Yerel eğitime yakın bir terim ekler | IID olmayan veriler için daha iyi |
| **İSKELE** | Veri heterojenliğini düzeltmek için kontrol değişkenlerini kullanır | IID olmayan veriler üzerinde daha hızlı yakınsama |
| **FedSGD** | FedAvg'ye benzer ancak tur başına bir degrade adımla | Tur başına daha düşük iletişim maliyeti |
| **Kişiselleştirilmiş FL** | Her cihaz, küresel modelin yanı sıra kişiselleştirilmiş bir modele sahiptir | Cihaz başına daha iyi performans |
| **Dikey FL** | Taraflar arasında farklı özellikler (farklı örnekler değil) | Taraflar aynı verinin farklı yönlerini elinde tuttuğunda |
---

## Farklı Gizlilik
Diferansiyel gizlilik (DP), bir algoritmanın çıktısının herhangi bir bireyin verilerinin dahil edilip edilmediğini ortaya çıkarmadığına dair matematiksel bir garanti sağlar.
### Temel Tanım
Bir M mekanizması, bir kayıtta farklılık gösteren herhangi iki D ve D' veri kümesi için (ε, δ)-diferansiyel gizliliği karşılar:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parametre | Anlamı |
|-----------|------------|
| **ε (epsilon)** | Gizlilik bütçesi. Daha küçük = daha özel. Tipik değerler: 0,1–10. |
| **δ (delta)** | Gizlilik garantisinin başarısız olma olasılığı. Tipik olarak 1/N (veri kümesi boyutunun tersi) olarak ayarlanır. |
### Gizlilik Ekleme Mekanizmaları
| Mekanizma | Nasıl Çalışır | Kullanım Örneği |
|-----------|----------------|----------|
| **Gauss mekanizması** | Sorgunun hassasiyetine göre kalibre edilmiş Gauss gürültüsünü ekleyin | Sürekli değerler (model ağırlıkları) |
| **Laplace mekanizması** | Laplace gürültüsü ekle | Sorguları sayma |
| **Üstel mekanizma** | Faydalarıyla orantılı olasılıkla çıktıları seçin | Ayrık seçenekler |
### DP-SGD (Diferansiyel Olarak Özel Stokastik Gradyan İnişi)
| Adım | Açıklama |
|------|-----------------|
| 1. Numune başına gradyanları hesaplayın | Toplu degradeler yerine |
| 2. Degradeleri kırpın | Her degradenin maksimum normunu sınırladı (herhangi bir tek numunenin etkisini sınırlar) |
| 3. Gürültü ekleyin | Birleştirilmiş degradeye kalibre edilmiş Gauss gürültüsü ekleyin |
| 4. Parametreleri güncelleyin | Standart degrade iniş adımı |
| Takas | Açıklama |
|-----------|----------------|
| **Gizlilik ve doğruluk** | Daha güçlü gizlilik (düşük ε) daha fazla gürültü gerektirir, bu da model doğruluğunu azaltır |
| **Gizlilik ve eğitim süresi** | Daha fazla gürültü, daha yavaş yakınsama anlamına gelir |
| **Gizlilik bütçesi takibi** | Her eğitim adımı gizlilik bütçesinin bir kısmını tüketir; harcandıktan sonra geri alınamaz |
---

## Birleşik Öğrenimi Farklı Gizlilikle Birleştirmek
| Katman | Koruma |
|----------|---------------|
| **Birleşik öğrenim** | Ham veriler cihazlarda kalıyor |
| **Farklı gizlilik** | Model güncellemeleri bile gürültülü olduğundan bireysel katkılar korunuyor |
| **Güvenli toplama** | Sunucu, tek tek güncellemeleri değil, yalnızca tüm güncellemelerin toplamını görür |
Bu kombinasyon güçlü gizlilik garantileri sağlar: Sunucunun güvenliği ihlal edilmiş olsa bile, belirli bir kişinin verilerinin eğitimde kullanılıp kullanılmadığını belirleyemez.
---

## Diğer Gizliliği Koruma Teknikleri
### Güvenli Çok Taraflı Hesaplama (SMPC)
Birden fazla taraf, bireysel girdilerini açıklamadan, birleştirilmiş verileri üzerinden bir fonksiyon hesaplar.
| Özellik | Açıklama |
|-----------|------------|
| **Nasıl çalışır** | Veriler taraflar arasında dağıtılan paylaşımlara bölünür; hesaplama hisseler üzerinde gerçekleşir |
| **Garanti** | Hiçbir taraf diğerinin girdileri hakkında hiçbir şey öğrenemez |
| **Hafif** | Önemli iletişim ve hesaplama maliyeti |
| **Kullanım örneği** | Müşteri verilerini paylaşmadan ortak risk modelleri hesaplayan bankalar |
### Homomorfik Şifreleme (HE)
Hesaplamaları doğrudan şifrelenmiş veriler üzerinde gerçekleştirin.
| Tür | Neleri Destekliyor | Tepegöz |
|----------------|----------|----------|
| **Kısmen HE** | Bir işlem (toplama VEYA çarpma) | Düşük |
| **Biraz HE** | Her iki operasyondan da sınırlı sayıda | Orta |
| **Tamamen HE** | Keyfi hesaplamalar | Çok yüksek (100-1000x yavaşlama) |
| Başvuru | Açıklama |
|------------|------------|
| **Özel çıkarım** | ML modellerini şifrelenmiş veriler üzerinde çalıştırın; şifrelenmiş tahminleri döndür |
| **Şifrelenmiş eğitim** | Şifrelenmiş veriler üzerinde eğitim alın (derin öğrenme için çoğunlukla teoriktir) |
| **Özel sorgular** | Sorguyu veya verileri açıklamadan bir veritabanını sorgulayın |
### Güvenilir Yürütme Ortamları (TEE'ler)
Verileri işletim sisteminden bile koruyan donanım tabanlı izolasyon (Intel SGX, ARM Trustzone).
| Avantajı | Sınırlama |
|-----------|---------------|
| Yerele yakın performans | Özel donanım gerektirir |
| Güçlü güvenlik garantileri | Sınırlı bellek (bölge boyutu) |
| Şifreleme yükü yok | Yan kanal saldırıları mümkün |
---

## Gizlilik Düzenlemeleri ve ML
| Yönetmelik | Bölge | ML'ye Etkisi |
|------------|-----------|------------|
| **GDPR** | AB | Açıklama hakkı; veri minimizasyonu; işleme izni; silme hakkı |
| **CCPA** | Kaliforniya | Veri satışını bilme, silme ve devre dışı bırakma hakkı |
| **HIPAA** | ABD (sağlık) | Sağlık verileri üzerinde sıkı kontroller; kimlik gizleme gereklilikleri |
| **PIPL** | Çin | Veri yerelleştirmesi; onay gereksinimleri; sınır ötesi transfer kuralları |
| **Yapay Zeka Yasası** | AB | Şeffaflık gereklilikleri; risk sınıflandırması; yasaklanmış uygulamalar |
### Makine Öğrenimi İş Akışları Üzerindeki Etki
| GDPR İlkesi | ML Uygulaması |
|----------------|---------------|
| **Veri minimizasyonu** | Yalnızca ihtiyaç duyulanları toplayın; birleşik öğrenme yardımcı olur |
| **Amaç sınırlaması** | Yeni izin olmadan veriler yeniden kullanılamaz |
| **Silme hakkı** | Bir kişinin verilerini eğitimli bir modelden kaldırabilmelidir (makine öğrenimini iptal etme) |
| **Açıklama hakkı** | Modeller bireysel tahminleri açıklayabilecek kadar yorumlanabilir olmalıdır |
| **Tasarım gereği gizlilik** | Gizlilik baştan itibaren sistemlere entegre edilmelidir |
---

## Zorluklar
| Mücadelesi | Açıklama |
|-----------|----------------|
| **İletişim maliyeti** | Milyonlarca cihaza model güncellemesi göndermek pahalıdır |
| **IID olmayan veriler** | Cihazların çok farklı veri dağılımları olması yakınsamaya zarar veriyor |
| **Başıboşlar** | Yavaş cihazlar tüm turu geciktirir |
| **Gizlilik-yardımcı program takası** | Daha güçlü gizlilik, daha kötü model performansı anlamına gelir |
| **Zehirlenme saldırıları** | Kötü niyetli katılımcılar küresel modeli bozabilir |
| **Model çıkarma** | Paylaşılan model güncellemeleri bile eğitim verileriyle ilgili bilgileri sızdırabilir |
| **Donanım heterojenliği** | Farklı cihazların farklı bilgi işlem yetenekleri vardır |
---

## Araçlar ve Çerçeveler
| Araç | Amaç |
|------|------------|
| **Çiçek** | Açık kaynaklı birleşik öğrenme çerçevesi; çerçeveden bağımsız |
| **TensorFlow Federe** | Google'ın TensorFlow modelleri için FL çerçevesi |
| **PySyft** (OpenMined) | PyTorch'ta gizliliği koruyan makine öğrenimi |
| **KADER** (Web Bankası) | Endüstriyel düzeyde birleşik öğrenme platformu |
| **YAPRAK** | Birleşik öğrenme araştırması için karşılaştırma paketi |
| **Opacus** (Meta) | PyTorch için farklı gizlilik |
| **Google'ın TF Gizliliği** | TensorFlow için farklı gizlilik |
---

## Özet
Birleşik öğrenme ve gizliliği koruma teknikleri temel bir gerilimi ele alıyor: Veriler dağıtıldığında, hassas olduğunda veya düzenlendiğinde güçlü yapay zeka modellerini nasıl oluşturursunuz? Birleşik öğrenme, verileri cihazlarda tutar ve yalnızca model güncellemelerini paylaşır. Diferansiyel gizlilik, bireysel katkıların tespit edilemeyeceğine dair matematiksel garantiler ekler. Güvenli hesaplama ve homomorfik şifreleme daha da ileri giderek şifrelenmiş veriler üzerinde hesaplama yapılmasına olanak tanır. Her tekniğin maliyetleri vardır (iletişim yükü, azaltılmış doğruluk, hesaplama masrafı) ancak bunlar bir arada, dünyanın verilerinden öğrenmeye devam ederken mahremiyete saygı duyan bir yapay zeka oluşturmak için bir araç seti oluşturur.