---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
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
tags: [time, series, forecasting, ai-and-machine-learning]
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

# Zaman Serisi ve Tahmin
Zaman serisi verileri, zaman içinde toplanan herhangi bir veridir: hisse senedi fiyatları, sıcaklık okumaları, web sitesi trafiği, satış rakamları, kalp atış hızı monitörleri, enerji tüketimi. Tahmin, geçmiş kalıplara dayanarak gelecekteki değerleri tahmin etmek anlamına gelir. Bu, veri biliminin pratik olarak en değerli uygulamalarından biridir ve en zorlarından biridir çünkü gelecek gerçekten belirsizdir ve gerçek dünyadaki zaman serileri gürültü, mevsimsellik ve yapısal kırılmalarla doludur.
---

## Zaman Serisinin Özellikleri
| Bileşen | Açıklama | Örnek |
|-----------|----------------|-----------|
| **Eğilim** | Uzun vadeli artış veya azalış | Küresel sıcaklıklar onlarca yıldır artıyor |
| **Mevsimsellik** | Sabit aralıklarla düzenli, öngörülebilir modeller | Perakende satışlar her Aralık ayında yükselişe geçiyor |
| **Döngüsellik** | Sabit olmayan aralıklarla dalgalanmalar (genellikle ekonomik) | Her 5-10 yılda bir durgunluk |
| **Gürültü (artık)** | Açıklanamayan rastgele varyasyon | Günlük hisse senedi fiyat hareketleri |
| **Otokorelasyon** | Mevcut değerler geçmiş değerlere bağlıdır | Bugünün sıcaklığı dünün sıcaklığına benzer |
### Durağanlık
Bir zaman serisi, istatistiksel özellikleri (ortalama, varyans) zaman içinde değişmiyorsa **durağandır**. Çoğu tahmin yöntemi durağanlığı varsayar.
| Testi | Amaç |
|------|------------|
| **Artırılmış Dickey-Fuller (ADF)** | Birim kökün mevcut olup olmadığını (durağan olmayan) test eder |
| **KPSS sınavı** | Serinin trend durağan olup olmadığını test eder |
| Dönüşüm | Ne Zaman Kullanılmalı |
|---------------|---------------|
| **Farklılık yaratan** | Trendi kaldır: y'(t) = y(t) - y(t-1) |
| **Günlük dönüşümü** | Varyansı stabilize edin (üstel büyüme için) |
| **Mevsimsel farklılık** | Sezonsallığı kaldırın: y'(t) = y(t) - y(t-s) burada s sezon uzunluğu |
---

## Klasik Tahmin Yöntemleri
### Hareketli Ortalamalar
| Yöntem | Açıklama | En İyisi |
|----------|----------------|----------|
| **Basit Hareketli Ortalama (SMA)** | Son N gözlemin ortalaması | Gürültülü verileri yumuşatma |
| **Ağırlıklı Hareketli Ortalama** | Daha yeni gözlemlerin ağırlığı artıyor | Güncel veriler daha önemli olduğunda |
| **Üstel Hareketli Ortalama (EMA)** | Katlanarak azalan ağırlıklar | Trendleri daha az gecikmeyle takip etme |
### Üstel Düzeltme
| Yöntem | Bileşenler | Kullanım Örneği |
|----------|---------------|----------|
| **Basit (SES)** | Yalnızca seviye | Trend yok, mevsimsellik yok |
| **Holt'un (Çift)** | Seviye + trend | Trend içeren ancak mevsimsellik içermeyen veriler |
| **Holt-Kışlar (Üçlü)** | Seviye + trend + sezonluk | Hem trend hem de sezonsallık içeren veriler |
### ARIMA ve Çeşitleri
ARIMA (OtoRegresif Entegre Hareketli Ortalama), klasik zaman serisi tahmininin en güçlü ürünüdür.
| Bileşen | Anlamı | Parametre |
|-----------|------------|-----------|
| **AR (p)** | Önceki p değerlerine göre gerileme | Kaç tane geçmiş değer kullanılacak |
| **ben (d)** | Sabit hale getirmek için farklılaştırma adımlarının sayısı | Kaç kez fark |
| **MA (q)** | Hatayı geçmiş hataların birleşimi olarak modelleyin | Kaç tane geçmiş hata kullanılacak |
| Varyant | Uzantı | Kullanım Örneği |
|-----------|---------------|----------|
| **SARIMA** | Mevsimsel bileşenler ekler (P, D, Q, s) | Güçlü mevsimsellik içeren veriler |
| **ARIMAX** | Harici değişkenler ekler | Yaklaşan etkinlikler hakkında bilgi sahibi olduğunuzda |
| **VAR** | Çok değişkenli ARIMA; çoklu birbirine bağlı seriler | Değişkenler birbirini etkilediğinde |
---

## Modern ML Yaklaşımları
### LSTM ve RNN Tabanlı Modeller
| Modeli | Mimarlık | Avantajı |
|----------|----------------|-----------|
| **LSTM** | Uzun Kısa Süreli Bellek ağı | Uzun vadeli zamansal bağımlılıkları yakalar |
| **GRU** | Geçitli Tekrarlayan Ünite (daha basit LSTM) | Daha hızlı eğitim; benzer performans |
| **Sıra2Sıra** | Zaman serileri için kodlayıcı-kod çözücü | Esnek giriş/çıkış uzunlukları |
| **Geçici Evrişimli Ağ (TCN)** | Genişlemiş nedensel kıvrımlar | Paralel eğitim; uzun alıcı alan |
### Peygamber (Meta)
İş zaman serileri için tasarlanmış pratik bir tahmin aracı.
| Özellik | Açıklama |
|-----------|------------|
| **Ayrışma** | Trend + sezonluk + tatiller |
| **Esnek** | Eksik verileri, aykırı değerleri ve yapısal kırılmaları ele alır |
| **Yorumlanabilir** | Bileşenler insan tarafından okunabilir |
| **Otomatik** | Makul varsayılanlar; minimum ayar gerekli |
| Güç | Sınırlama |
|----------|---------------|
| İş ölçümleri (satışlar, kullanıcılar) için harika | Çok yüksek frekanslı veriler için ideal değil |
| Tatiller ve özel etkinliklerle ilgilenir | Toplama veya çarpımsal mevsimselliği varsayar |
| Aykırı değerlere karşı dayanıklı | Karmaşık modeller için derin öğrenmeden daha az doğruluk |
### Trafo Tabanlı Modeller
| Modeli | Temel Özellik |
|----------|----------------|
| **Muhabir** | ProbUzun diziler için dikkatin az olması |
| **Otomatik Biçimlendirici** | Seri ayrıştırma için otomatik korelasyon mekanizması |
| **TST Yaması** | Zaman serisini yamalar; kanaldan bağımsız |
| **TimesFM** (Google) | Zaman serileri için temel model; çeşitli veriler üzerine önceden eğitilmiş |
| **Kronos** (Amazon) | Zaman serilerini tokenleştirir; Yüksek Lisans tarzı mimariyi kullanıyor |
---

## Zaman Serisinde Anormallik Tespiti
Beklenen davranıştan sapan olağandışı kalıpların tespit edilmesi.
| Yöntem | Yaklaşım | Kullanım Örneği |
|----------|----------|----------|
| **İstatistiksel** | Z-skoru, IQR, kontrol grafikleri | Basit, iyi anlaşılmış |
| **İzolasyon Ormanı** | Ağaç bazlı; anormallikleri rastgele bölümlemeyle izole eder | Çok değişkenli anormallik tespiti |
| **LOF** (Yerel Aykırı Faktör) | Yoğunluğa dayalı; yerel yoğunluğu komşularla karşılaştırır | Anormallikler düşük yoğunluklu bölgelerde olduğunda |
| **Otomatik kodlayıcılar** | Yeniden yapılanma hatası; yüksek hata = anormallik | Karmaşık, doğrusal olmayan modeller |
| **LSTM tabanlı** | Bir sonraki adımı tahmin edin; büyük tahmin hatası = anormallik | Sıralı anormallikler |
### Uygulamalar
| Etki Alanı | Anomalilerin Anlamı |
|----------|-----------|
| **Finans** | Dolandırıcılık, piyasa çöküşleri, ani çöküşler |
| **Sağlık Hizmetleri** | Anormal kalp hızı, nöbet başlangıcı |
| **İmalat** | Ekipman arızası, kalite kusurları |
| **Siber güvenlik** | İzinsiz giriş girişimleri, DDoS saldırıları |
| **Altyapı** | Sunucunun aşırı yüklenmesi, ağ arızaları |
---

## Değerlendirme Metrikleri
| Metrik | Formül (kavramsal) | Ne Zaman Kullanılmalı |
|----------|----------|------------|
| **MAE** (Ortalama Mutlak Hata) | Mutlak hataların ortalaması | Yorumlanabilir; verilerle aynı birimler |
| **RMSE** (Kök Ortalama Kare Hatası) | Ortalama karesel hataların karekökü | Büyük hataları cezalandırır daha fazla |
| **MAPE** (Ortalama Mutlak Yüzde Hatası) | Mutlak yüzde hatalarının ortalaması | Göreceli hata önemli olduğunda |
| **SMAPE** (Simetrik MAPE) | MAPE'nin simetrik versiyonu | Sıfıra yakın değerleri daha iyi işler |
| **MASE** (Ortalama Mutlak Ölçeklendirilmiş Hata) | Saf bir tahmine göre MAE | Farklı seriler arasında karşılaştırma |
---

## Pratik İş Akışı
| Adım | Açıklama |
|------|-----------------|
| **1. Keşfedin** | Serinin grafiğini çizin; trendi, mevsimselliği ve aykırı değerleri belirleyin |
| **2. Ayrıştırma** | Trend, mevsimsel ve kalan bileşenlere ayırın |
| **3. Durağanlaştırma** | Gerekiyorsa farkları veya dönüşümleri uygulayın |
| **4. Bölünmüş** | Zamana dayalı bölünme (zaman serileri için asla rastgele bölünmez) |
| **5. Temel** | Saf bir tahminle başlayın (son değer, mevsimsel saf) |
| **6. Modeli** | Klasik yöntemleri (ARIMA, Prophet) deneyin, ardından makine öğrenimi yöntemlerini deneyin |
| **7. Değerlendir** | Uygun ölçümleri kullanın; temel değerle karşılaştır |
| **8. Tekrarla** | Özellikler ekleyin, farklı modelleri deneyin, hiperparametreleri ayarlayın |
---

## Araçlar ve Kütüphaneler
| Araç | Amaç |
|------|------------|
| **istatistik modelleri** | Klasik zaman serileri (ARIMA, ETS, ayrıştırma) |
| **Peygamber** (Meta) | Ticari zaman serisi tahmini |
| **sktime** | Zaman serileri için birleşik ML arayüzü |
| **Dart** | Kapsamlı tahmin kitaplığı (klasik + derin öğrenme) |
| **GluonTS** (Amazon) | Olasılıksal zaman serisi modelleme |
| **Sinir Peygamberi** | Sinir ağı bileşenleriyle Peygamber |
| **tsfresh** | Otomatik zaman serisi özellik çıkarma |
| **pandalar** | Zaman serisi manipülasyonu ve yeniden örnekleme |
---

## Özet
Zaman serisi tahmini, klasik istatistikleri modern makine öğrenimiyle harmanlar. Klasik yöntemler (ARIMA, üstel düzeltme, Prophet) yorumlanabilir, hızlı ve çoğu zaman şaşırtıcı derecede doğrudur. Derin öğrenme yöntemleri (LSTM, Transformers) karmaşık modelleri yakalar ancak daha fazla veri ve ayarlama gerektirir. Temel ilkeler, yöntem ne olursa olsun aynı kalır: Verilerinizin yapısını anlayın (trend, mevsimsellik, gürültü), her zaman basit bir temel çizgiyle karşılaştırma yapın, uygun ölçümlerle değerlendirin ve geleceğin asla geçmişin mükemmel bir tekrarı olmadığını unutmayın.