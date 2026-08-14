---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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
# Model Optimizasyonu ve Dağıtımı
Büyük bir yapay zeka modelini eğitmek önemli bir başarıdır, ancak onu verimli bir şekilde dağıtmak, mühendislik çabalarının çoğunun gerekli olduğu yerdir. Yanıt vermesi 10 saniye süren veya sekiz A100 GPU gerektiren bir model, çoğu gerçek dünya uygulaması için pratik değildir. Model optimizasyonu, kabul edilebilir kaliteyi korurken modelleri daha küçük, daha hızlı ve daha uygun maliyetli hale getirme sürecidir. Bu dosya niceleme, budama, damıtma ve modellerin üretimde dağıtımına yönelik pratik araçları kapsar.
---

## Neden Optimize Etmeliyim?
| endişe | Etki |
|-----------|-----------|
| **Gecikme** | Kullanıcılar 1 saniyeden kısa sürede yanıt bekliyor; her ekstra 100 ms etkileşimi kaybeder |
| **Maliyet** | GPU çıkarımı pahalıdır; 70B modelinin maliyeti, bulut donanımındaki 1 milyon token başına ~0,05-0,15 ABD dolarıdır |
| **Bellek** | FP32'deki bir 7B modelinin 28 GB VRAM'e ihtiyacı vardır; çoğu tüketici GPU'sunda 8-24 GB |
| **Enerji** | Büyük modelleri çalıştırmak önemli miktarda elektrik tüketir; mobil ve uç noktalara yönelik konular |
| **Ölçek** | Milyonlarca kullanıcıya hizmet vermek, mevcut donanıma uygun modeller gerektirir |
---

## Kuantizasyon
Niceleme, model ağırlıklarının hassasiyetini 32 bit kayan noktadan (FP32) INT8, INT4 gibi daha küçük formatlara ve hatta daha düşük formatlara azaltır.
### Hassas Formatlar
| Biçim | Ağırlık Başına Bit | 7B Modeli için Bellek | Kalite |
|----------|----------------|-----------|---------|
| **FP32** | 32 | 28GB | Temel çizgi (tam hassasiyet) |
| **FP16 / BF16** | 16 | 14GB | FP32 ile neredeyse aynı |
| **INT8** | 8 | 7 GB | Çok küçük kalite kaybı |
| **INT4** | 4 | 3,5 GB | Orta kalite kaybı; hala kullanılabilir |
| **INT3 / INT2** | 3-2 | 2,6-1,75GB | Önemli kalite kaybı; araştırma aşaması |
### Niceleme Yöntemleri
| Yöntem | Ne Zaman Olur | Nasıl Çalışır | Kalite |
|----------|-----|-------------|-----------|
| **Eğitim Sonrası Niceleme (PTQ)** | Eğitim tamamlandıktan sonra | Modeli küçük bir veri kümesinde kalibre edin; en uygun ölçekleri bulun | INT8 için iyi; INT4'te bozulur |
| **GPTQ** | Eğitimden sonra | Yaklaşık ikinci derece bilgileri kullanan GPU dostu INT4 nicelemesi | INT4'te kaliteli |
| **AWQ** (Etkinleştirme Farkında Ağırlık Ölçümü) | Eğitimden sonra | Aktivasyon büyüklüklerine göre göze çarpan ağırlıkları koruyun | INT4'te GPTQ'dan daha iyi |
| **GGUF** (llama.cpp biçimi) | Eğitimden sonra | CPU dostu niceleme; katman başına karma hassasiyet | CPU çıkarımı için optimize edildi |
| **Kuantizasyon Farkındalık Eğitimi (QAT)** | Eğitim sırasında | Modelin başa çıkmayı öğrenmesi için eğitim sırasında nicelemeyi simüle edin | En iyi kalite; yeniden eğitim gerektirir |
### Pratik Etki
| Modeli | FP16 Boyutu | INT4 Boyutu | Hızlandırma | Kalite Kaybı |
|----------|-----------|-----------|------------|------------|
| **LLaMA 7B** | 14GB | 3,5 GB | 2-4x | Karşılaştırmalı değerlendirmelerde ~%1-2 |
| **LLaMA 70B** | 140GB | 35GB | 2-3x | Karşılaştırmalı değerlendirmelerde ~%2-3 |
---

## Budama
Budama, eğitimli bir modeldeki gereksiz ağırlıkları veya nöronları ortadan kaldırır.
| Tür | Açıklama | Avantajı | Mücadelesi |
|------|-------------|-----------|-----------|
| **Yapılandırılmamış** | Bireysel ağırlıkları kaldırın (sıfıra ayarlayın) | En yüksek sıkıştırma oranları | Seyrek donanım desteği gerektirir |
| **Yapılandırılmış** | Tüm nöronları, dikkat başlıklarını veya katmanları kaldırın | Model boyutunu doğrudan azaltır | Daha fazla kalite kaybedilebilir |
| **Büyüklüğe dayalı** | Mutlak değerleri en küçük olan ağırlıkları kaldırın | Basit; iyi çalışıyor | Önemli küçük ağırlıkları kaçırabilir |
| **Öneme dayalı** | Çıktıya katkılarına göre ağırlıkları kaldırın | Daha kaliteli koruma | Hesaplanması daha pahalı |
### Budama Boru Hattı
| Adım | Açıklama |
|------|-----------------|
| 1. Tren | Tam modeli normal şekilde eğitin |
| 2. Puan | Her ağırlık/nöron için önem puanlarını hesaplayın |
| 3. Kuru erik | En az önemli unsurları kaldırın |
| 4. İnce ayar | Kaybolan doğruluğu geri kazanmak için yeniden eğitim alın |
| 5. Tekrarla | Daha yüksek sıkıştırma için yinelemeli budama ve ince ayar |
---

## Bilgi Damıtma
Büyük bir "öğretmen" modelini taklit etmek için küçük bir "öğrenci" modelini eğitmek.
| Bileşen | Rol |
|-----------|------|
| **Öğretmen** | Büyük, yüksek kaliteli model |
| **Öğrenci** | Öğretmeninden öğrenen küçük model |
| **Distilasyon kaybı** | Öğrenci, öğretmenin çıktı dağıtımını (yumuşak etiketler) eşleştirmeye çalışır |
### Damıtma Türleri
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Logit tabanlı** | Öğrenci, öğretmenin çıktı olasılıklarını eşleştirir | Hinton'un orijinal damıtması |
| **Özellik tabanlı** | Öğrenci, öğretmenin ara temsillerini eşleştirir | FitNet'ler |
| **İlişki bazlı** | Öğrenci örnekler arasındaki ilişkileri eşleştirir | RKD (İlişkisel Bilgi Damıtma) |
| **Verisiz** | Orijinal eğitim verisine gerek yok; öğretmen neslini kullanın | DAFL, Derin Ters Çevirme |
### Önemli Damıtma Örnekleri
| Öğretmen | Öğrenci | Sonuç |
|------------|-----------|--------|
| **GPT-4** | GPT-3.5-turbo (söylentiler) | GPT-4 kalitesinin çoğunu taşıyan daha küçük model |
| **BERT-Büyük** | DistilBERT | %40 daha küçük, %60 daha hızlı, BERT'in performansının %97'si |
| **LLaMA 70B** | LLaMA 7B (damıtma yoluyla) | Açık kaynaklı küçük model, büyük model kalitesine yaklaşıyor |
---

## LLM'ye Özel Optimizasyonlar
### KV-Önbellek Optimizasyonu
Büyük dil modelleri, yeniden hesaplamayı önlemek için önceki belirteçlerdeki anahtar/değer çiftlerini önbelleğe alır.
| Tekniği | Açıklama | Etki |
|-----------|----------------|-----------|
| **Çoklu Sorgu Dikkati (MQA)** | Tüm dikkat kafaları bir KV çiftini paylaşır | Belleği azaltır; hafif kalite kaybı |
| **Gruplandırılmış Sorgu Dikkati (GQA)** | Kafa grupları KV çiftlerini paylaşıyor | MQA ile standart dikkat arasındaki denge |
| **Sürgülü pencere dikkati** | Yalnızca son W jetonlarına katılın | Uzun bağlamlar için KV önbellek boyutunu azaltır |
### Spekülatif Kod Çözme
| Adım | Açıklama |
|------|-----------------|
| 1 | Küçük bir "taslak" model, hızlı bir şekilde K tokeni üretir |
| 2 | Büyük model, tüm K jetonlarını tek ileri geçişte doğrular |
| 3 | Kabul edilen tokenlar saklanır; reddedilenler yeniden oluşturuluyor |
Sonuç: Kalite kaybı olmadan üretimde 2-3 kat hızlanma (son söz her zaman büyük modeldedir).
### Flaş Dikkati
| Özellik | Açıklama |
|-----------|------------|
| **Sorun** | Standart dikkat, dikkat matrisi için O(n²) hafıza gerektirir |
| **Çözüm** | Dikkati bloklar halinde hesaplayın; matrisin tamamını hiçbir zaman bellekte gerçekleştirmeyin |
| **Sonuç** | 2-4 kat daha hızlı; çok daha uzun bağlam pencerelerine olanak tanır |
| **Çeşitler** | Flash Attention 2 (daha hızlı), FlashDecoding (çıkarım için optimize edilmiştir) |
---

## Sunum Çerçeveleri
| Çerçeve | En İyisi | Temel Özellik |
|-----------|----------|------------|
| **vLLM** | Yüksek Lisans hizmeti | PagedDikkat; sürekli harmanlama; yüksek verim |
| **TensorRT-LLM** | NVIDIA GPU çıkarımı | NVIDIA donanımında maksimum performans |
| **llama.cpp** | CPU ve tüketici GPU çıkarımı | Dizüstü bilgisayarlarda ve telefonlarda nicelenmiş modelleri çalıştırır |
| **Ollama** | Yerel model çalışıyor | llama.cpp çevresindeki kullanıcı dostu sarmalayıcı |
| **Triton Çıkarım Sunucusu** | Çoklu çerçeve sunumu | TensorFlow, PyTorch, ONNX, TensorRT'yi destekler |
| **Meşale Hizmeti** | PyTorch model sunumu | Yerel PyTorch entegrasyonu |
| **ONNX Çalışma Zamanı** | Platformlar arası çıkarım | Donanım genelinde optimize edilmiş yürütme |
| **BentoML** | Üretim dağıtımı | Çerçeveden bağımsız; paketleme ve servis kolları |
---

## Dağıtım Modelleri
| Desen | Açıklama | Ne Zaman Kullanılmalı |
|-----------|---------------|------------|
| **Uç dağıtımı** | Modelleri telefonlarda, IoT cihazlarında veya yerleşik donanımda çalıştırın | Düşük gecikme; çevrimdışı; gizlilik |
| **Bulut API'si** | Modelleri bulut GPU'larda barındırın; API aracılığıyla hizmet verin | Maksimum hesaplama; kullanım başına ödeme |
| **Hibrit** | Cihazdaki küçük model; bulutta büyük model | Her iki dünyanın da en iyisi |
| **Sunucusuz** | Sıfıra ölçeklendirin; yalnızca kullanıldığında ödeme yapın | Sporadik trafik; maliyete duyarlı |
| **Toplu çıkarım** | Verileri toplu olarak planlı bir şekilde işleyin | Gerçek zamana ihtiyaç duyulmadığında |
---

## Karşılaştırma
| Metrik | Neyi Ölçer |
|----------|------|
| **Saniye başına jeton** | Üretim verimi (daha yüksek, daha iyidir) |
| **İlk jetona ulaşma süresi (TTFT)** | İlk çıktı jetonu görünmeden önceki gecikme |
| **İstek başına gecikme** | Girişten çıkışın tamamlanmasına kadar geçen toplam süre |
| **Bellek kullanımı** | Çıkarım sırasında tüketilen VRAM veya RAM |
| **Verim** | Saniyede sunulan istekler |
| **1 milyon token başına maliyet** | 1 milyon jetonun işlenmesinin dolar maliyeti |
---

## Pratik İpuçları
- **Kuantizasyonla başlayın.** INT4 nicemleme (AWQ veya GPTQ), kaliteden boyuta en iyi dengeyi sağlar. Çoğu 7B modeli, INT4'teki tek bir tüketici GPU'sunda rahatça çalışır.
- **LLM sunumu için vLLM'yi kullanın.** Yüksek verimli LLM çıkarımı için en hızlı açık kaynak seçeneğidir.
- **Optimize etmeden önce profil oluşturun.** Zamanın gerçekte nerede harcandığını ölçün. Darboğaz genellikle bilgi işlem değil, bellek bant genişliğidir.
- **Modeli görevle eşleştirin.** 7B modeli çoğu görev için uygundur. 7B işe yarayacakken 70B'yi kullanmayın.
- **Damıtmayı düşünün.** Üretim için küçük, hızlı bir modele ihtiyacınız varsa, sıfırdan eğitim vermek yerine daha büyük bir modelden damıtın.
- **Sürekli izleyin.** Veri dağılımları değiştikçe model performansı zaman içinde düşebilir. Gecikme, aktarım hızı ve kalite ölçümlerini izleyin.
---

## Özet
Model optimizasyonu araştırma ve üretim arasındaki köprüdür. Niceleme, minimum kalite kaybıyla modelleri 4-8 kat küçültür. Budama ölü ağırlığı ortadan kaldırır. Damıtma, bilgiyi büyük modellerden küçük modellere aktarır. Flash Attention ve KV-önbellek hileleri, çıkarımı daha hızlı hale getirir. Bu teknikler birlikte, veri merkezi gerektiren bir modeli dizüstü bilgisayar veya telefonda çalışan bir modele dönüştürür. Alan hızla ilerliyor; geçen yıl sekiz A100'ün gerektirdiği şey, bugün tüketici GPU'sunda çalışıyor.