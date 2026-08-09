---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [recommendation, systems, ai-and-machine-learning]
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

# Öneri Sistemleri
Öneri sistemleri, bir kullanıcının bundan sonra ne görmek, satın almak veya etkileşimde bulunmak isteyeceğini tahmin eder. Sosyal medyadaki içerik akışlarını, e-ticaret sitelerindeki ürün önerilerini, yayın platformlarındaki film seçimlerini ve arama sonuçlarını desteklerler. Çoğu kullanıcı için görünmez olmalarına rağmen ticari açıdan dünyadaki en etkili yapay zeka sistemleri arasında yer alıyorlar. Netflix, öneri motorunun abone kaybını azaltarak yılda 1 milyar dolardan fazla tasarruf sağladığını tahmin ediyor.
---

## Öneriler Neden Zordur?
| Mücadelesi | Açıklama |
|-----------|----------------|
| **Ölçek** | Milyonlarca kullanıcı × milyonlarca öğe = milyarlarca olası çift |
| **seyreklik** | Her kullanıcı mevcut öğelerin çok küçük bir kısmıyla etkileşime girmiştir |
| **Soğuk başlatma** | Yeni kullanıcıların ve yeni öğelerin etkileşim geçmişi yoktur |
| **Dinamik tercihler** | Kullanıcının zevkleri zamanla değişir |
| **Doğruluğun ötesinde** | Öneriler aynı zamanda çeşitli, yeni ve tesadüfi olmalıdır |
| **İş hedefleri** | Etkileşimi en üst düzeye çıkarmak ≠ kullanıcı refahını en üst düzeye çıkarmak |
---

## Temel Yaklaşımlar
### İşbirlikçi Filtreleme
Fikir şu: A ve B kullanıcıları geçmişte aynı fikirdeyse, muhtemelen gelecekte de aynı fikirde olacaklardır.
| Tür | Nasıl Çalışır | Örnek |
|------|-------------|--------|
| **Kullanıcı tabanlı** | Benzer kullanıcıları bulun; beğendikleri şeyleri tavsiye edin | "Bunu beğenen kullanıcılar şunu da beğendi..." |
| **Öğe bazlı** | Kullanıcının zaten beğendiği şeylere benzer öğeler bulun | "Çünkü izlediniz..." |
| **Matris çarpanlarına ayırma** | Kullanıcı öğesi etkileşim matrisini gizli faktörlere ayrıştırın | SVD, ALS (Alternatif En Küçük Kareler) |
| Güç | Zayıflık |
|----------|----------|
| Öğelerin kendisini anlamanıza gerek yok | Soğuk başlatma sorunu: yeni öğeler öneremiyorum |
| Karmaşık, örtülü tercihleri ​​yakalar | Çok sayıda etkileşim verisi gerektirir |
| Her türlü içerik türünde çalışır | Popülerlik eğilimi: halihazırda popüler olan öğeleri önerir |
### İçerik Tabanlı Filtreleme
Öğe özelliklerine göre kullanıcının zaten beğendiği öğelere benzer öğeler önerin.
| Özellik Türü | Örnek |
|---------------|-----------|
| **Metin** | Tür, açıklama, anahtar kelimeler, oyuncular |
| **Ses** | Tempo, tür, ruh hali (müzik için) |
| **Görsel** | Renk paleti, stil (resimler/moda için) |
| **Meta veriler** | Fiyat, marka, kategori |
| Güç | Zayıflık |
|----------|----------|
| Öğeler için soğuk başlatma yok (özellikler biliniyor) | Kullanıcının mevcut zevki dışında öğeler önerilemez |
| Daha az etkileşim verisiyle çalışır | İyi özellik mühendisliği gerektirir |
| Açıklanabilir ("X'e benzer olduğu için önerilir") | Daha az şans |
### Hibrit Yaklaşımlar
Çoğu üretim sistemi işbirlikçi ve içerik tabanlı yöntemleri birleştirir.
| Hibrit Strateji | Açıklama |
|----------------|---------------|
| **Ağırlıklı** | Birden fazla modelden alınan puanları birleştirin |
| **Geçiş yapma** | Yeni kullanıcılar için içerik tabanlı, yerleşik kullanıcılar için ise işbirlikçi kullanın |
| **Kademeli** | Önce basit bir model kullanın, ardından karmaşık bir modelle iyileştirin |
| **Özellik kombinasyonu** | İşbirliği ve içerik özelliklerini tek bir modelde birleştirin |
| **Meta-öğrenme** | Farklı tavsiye verenleri nasıl birleştireceğinizi öğrenin |
---

## Modern Derin Öğrenme Yaklaşımları
### İki Kuleli Modeller
Büyük ölçekli öneri için baskın mimari (YouTube, Pinterest, Spotify tarafından kullanılır).
| Bileşen | Rol |
|-----------|------|
| **Kullanıcı kulesi** | Kullanıcı özelliklerini ve geçmişini bir yerleştirmeye kodlayan sinir ağı |
| **Eşya kulesi** | Öğe özelliklerini bir yerleştirmeye kodlayan sinir ağı |
| **Benzerlik** | Kullanıcı ve öğe yerleştirmeleri arasındaki nokta çarpım veya kosinüs benzerliği |
| Adım | Açıklama |
|------|-----------------|
| 1 | Etkileşimde bulunan kullanıcı öğesi çiftleri için benzer yerleştirmeler üretmek üzere her iki kuleyi de eğitin |
| 2 | Sunum sırasında öğe yerleştirmelerini önceden hesaplayın |
| 3 | Bir kullanıcı isteği için kullanıcı yerleştirmeyi hesaplayın |
| 4 | En benzer öğeleri bulmak için yaklaşık en yakın komşu (ANN) aramasını kullanın |
### Öneriler için Sıra Modelleri
Kullanıcı davranışı sıralıdır; dün izledikleriniz bugün izleyeceklerinizi etkiler.
| Modeli | Yaklaşım |
|----------|----------|
| **GRU4Rec** | Oturum bazlı öneriler için GRU tabanlı model |
| **SASRec** | Öz-dikkat temelli sıralı önerici |
| **BERT4Rec** | Sıralı öneriler için Çift Yönlü Transformatör |
| **YouTube DNN** | Derin sinir ağı, izleme geçmişini bir dizi olarak ele alıyor |
### Alma ve Sıralama
Modern sistemler önerileri iki aşamaya ayırır:
| Sahne | Amaç | Yöntem |
|----------|------------|--------|
| **Geri alma (aday oluşturma)** | Milyonlarca öğeyi ~1.000 adaya daraltın | İki kuleli model; YSA araması; hızlı ama yaklaşık |
| **Sıralama (puanlama)** | Adayları tam olarak puanlayın ve sıralayın | Birçok özelliğe sahip derin model; daha yavaş ama doğru |
| **Yeniden sıralama** | Çeşitliliğe, iş kurallarına ve tazeliğe göre ayarlayın | Bağlamsal haydutlar; kısıtlama optimizasyonu |
---

## Değerlendirme Metrikleri
| Metrik | Neyi Ölçer | Ne Zaman Kullanılmalı |
|----------|----------|------------|
| **Hassas@K** | İlgili en iyi K önerilerinin oranı | En çok tercih edilenlerin doğruluğuna önem verdiğinizde |
| **Geri Çağırma@K** | Top-K'de bulunan ilgili öğelerin oranı | İyi eşyaları kaçırmamaya önem verdiğinizde |
| **NDCG** (Normalleştirilmiş İndirgenmiş Kümülatif Kazanç) | Sıralama kalitesi; ilgili öğeleri daha yükseğe çıkaran ödüller | Sıralama sırası önemli olduğunda |
| **HARİTA** (Ortalama Ortalama Hassasiyet) | Tüm kullanıcılar arasında ortalama hassasiyet | Genel sıralama kalitesi |
| **İsabet Oranı@K** | En az bir ilgili öğenin üst K'da görünüp görünmediği | İkili alaka senaryoları |
| **Kapsam** | Tavsiye edilen öğelerin oranı | Çeşitlilik ve adalet |
| **Mutluluk** | Beklenmedik ama alakalı öneriler | Kullanıcı memnuniyeti |
---

## Soğuk Başlatma Sorunu
| Senaryo | Mücadelesi | Çözümler |
|----------|---------------|-----------|
| **Yeni kullanıcı** | Etkileşim geçmişi yok | Demografiyi kullanın; popüler öğeleri göster; bağlamsal sinyalleri kullanın (konum, cihaz, zaman) |
| **Yeni öğe** | Henüz kimse onunla etkileşime girmedi | İçerik özelliklerini kullanın; keşfetme-kullanma stratejileri; haydut algoritmaları |
| **Yeni sistem** | Hiç veri yok | Benzer alanlardan öğrenmeyi aktarın; başlangıç ​​içeriğini seç |
---

## Keşif ve Sömürü
| Strateji | Açıklama | Takas |
|----------|----------------|-----------|
| **ε-açgözlü** | Olasılıkla rastgele öğeleri göster ε | Basit ama verimsiz |
| **Thompson örneklemesi** | Madde kalitesinin sonsal dağılımından örnek | İlkeli; iyi teorik özellikler |
| **Üst Güven Sınırı (UCB)** | Belirsizliğin yüksek olduğu ürünleri tercih edin | Keşif ve kullanım arasında iyi bir denge |
| **Bağlamsal haydutlar** | Kullanıcı bağlamına bağlı keşif | Kör keşiften daha verimli |
| **Çeşitlilik enjeksiyonu** | Kasıtlı olarak çeşitli veya yeni öğeleri dahil edin | Basit; kısa vadeli etkileşimi azaltabilir |
---

## Önyargı ve Adalet
| Önyargı Türü | Açıklama | Etki |
|-----------|----------------|-----------|
| **Popülerlik önyargısı** | Popüler ürünler daha fazla tavsiye ediliyor ve daha popüler hale geliyor | Uzun kuyruklu ürünler yetersiz servis ediliyor |
| **Seçim yanlılığı** | Modeller olası tüm etkileşimlerden değil, gözlemlenen etkileşimlerden öğrenir | Aktif kullanıcılara doğru eğimli |
| **Konum sapması** | Daha yüksek konumlarda gösterilen öğeler, kaliteden bağımsız olarak daha fazla tıklama alır | Üst konumları güçlendiriyor |
| **Maruz kalma yanlılığı** | Gösterilen öğeler daha fazla eğitim sinyali alıyor | Geri bildirim döngüsü |
| **Demografik önyargı** | Öneriler demografik özelliklere göre adil olmayan şekillerde farklılık gösteriyor | Ayrımcılık; bazı gruplar için kötü deneyim |
### Etki Azaltma Stratejileri
| Strateji | Açıklama |
|----------|----------------|
| **Ters eğilim ağırlıklandırması** | Antrenmanlarda düşük ağırlıklı popüler ürünler |
| **Katmanların önyargısını giderme** | Modele önyargı giderme bileşeni ekleyin |
| **Adillik kısıtlamaları** | Adil muameleyi sağlamak için kısıtlamalar ekleyin |
| **Çeşitli öneriler** | Uygunluğun yanı sıra çeşitliliği de açıkça optimize edin |
| **Denetim ve izleme** | Gruplar arasındaki önyargı önerilerini düzenli olarak kontrol edin |
---

## Endüstri Örnekleri
| Şirket | Sistem | Yaklaşım |
|-----------|-----------|----------|
| **Netflix** | Film/TV önerileri | İki kuleli erişim + derin sıralama + sanat eserleri için bağlamsal haydutlar |
| **YouTube** | Video önerileri | Aday üretimi için derin sinir ağı; ayrı sıralama modeli |
| **Spotify** | Müzik önerileri | İşbirliğine dayalı filtreleme + çalma listelerinde NLP + ses analizi |
| **Amazon** | Ürün önerileri | Öğeden öğeye işbirliğine dayalı filtreleme; uygun ölçekte kişiselleştirilmiş |
| **TikTok** | Kısa video yayını | Takviyeli öğrenme; keşfe güçlü vurgu |
| **Pinterest** | Görsel öneriler | İki kuleli model; görsel benzerlik |
---

## Araçlar ve Çerçeveler
| Araç | Amaç |
|------|------------|
| **TensorFlow Önericileri (TFRS)** | İki kuleli modeller, erişim, sıralama |
| **PyTorch RecSys** | Araştırma odaklı öneri modelleri |
| **Sürpriz** | Klasik işbirlikçi filtreleme (SVD, NMF, KNN) |
| **Örtülü** | Örtülü geri bildirim için hızlı işbirliğine dayalı filtreleme (ALS, BPR) |
| **Faiss** (Meta) | Büyük ölçekte yaklaşık en yakın komşu araması |
| **Milvus / Çam Kozalağı / Weaviate** | Benzerlik araması için vektör veritabanları |
| **Recbole** | Kapsamlı öneri araştırma kütüphanesi |
| **Merlin** (NVIDIA) | GPU ile hızlandırılmış öneri hattı |
---

## Özet
Öneri sistemleri endüstrideki en etkili yapay zeka uygulamaları arasındadır. Bu alan, basit işbirliğine dayalı filtrelemeden, kullanıcı geçmişini, öğe içeriğini, bağlamsal sinyalleri ve iş hedeflerini birleştiren derin öğrenme mimarilerine doğru gelişmiştir. Modern sistemler, hızlı aday oluşturma için iki kuleli modeller ve hassas puanlama için derin modeller içeren bir alma-sıralama-yeniden sıralama hattını kullanır. Soğuk başlangıç, önyargı, keşif ve kullanıcı memnuniyetini iş hedefleriyle dengeleme gibi zorluklar, araştırma ve mühendisliğin aktif alanları olmaya devam ediyor.