---
# Metadata
title: "Supply Chain and Operations Management"
description: "Inventory management, lean manufacturing, logistics, bullwhip effect"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [supply, chain, operations, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Tedarik Zinciri ve Operasyon Yönetimi
Tedarik zinciri yönetimi, hammaddeden müşterinin elindeki bitmiş ürüne kadar kaynak bulma, satın alma, dönüştürme ve lojistikle ilgili tüm faaliyetlerin koordinasyonudur. Operasyon yönetimi, üretim sistemlerinin günlük işleyişidir. Birlikte bir şirketin doğru ürünü, doğru zamanda, doğru maliyetle, doğru kalitede teslim edip edemeyeceğini belirlerler. Pandemi, çip kıtlığı ve kanal tıkanıklıkları, tedarik zincirlerinin ne kadar kırılgan ve küresel olarak birbirine bağlı olduğunu gösterdi.
---

## Tedarik Zincirinin Temelleri
### Tedarik Zinciri Akışı
| Sahne | Etkinlik | Önemli Konu |
|----------|----------|------------|
| **Plan** | Talep tahmini; tedarik planlaması; S&OP | Kesinlik; duyarlılık |
| **Kaynak** | Tedarikçi seçimi; satın alma; müteahhitlik | Maliyet; kalite; güvenilirlik; etik |
| **Yap** | Üretme; toplantı; kalite kontrol | Yeterlik; esneklik; kapasite |
| **Teslim Et** | Depolama; siparişin yerine getirilmesi; taşımacılık | Hız; maliyet; doğruluk |
| **Geri Dönüş** | Tersine lojistik; geri döner; geri dönüşüm | Müşteri memnuniyeti; maliyet kurtarma |
### Tedarik Zinciri Türleri
| Tür | Özellikler | En İyisi |
|----------|-----|----------|
| **Verimli** | Yüksek kullanım; düşük maliyetli; öngörülebilir | Talebi istikrarlı olan fonksiyonel ürünler (bakkaliye) |
| **Duyarlı** | Tampon kapasitesi; esnek; hızlı | Talebin belirsiz olduğu yenilikçi ürünler (moda) |
| **Dayanıklı** | Artıklık; görünürlük; uyarlanabilirlik | Yüksek riskli ortamlar; kritik ürünler |
| **Çevik** | Erteleme; kitlesel kişiselleştirme | Çok çeşitli ve kısa yaşam döngüsüne sahip ürünler |
| **Yalın** | Atıkları ortadan kaldırın; çekme tabanlı; tam zamanında | Yüksek hacimli; düşük çeşitlilik; istikrarlı talep |
---

## Envanter Yönetimi
### Envanter Türleri
| Tür | Açıklama | Amaç |
|------|-------------|--------|
| **Hammaddeler** | İşlenmemiş girdiler | Arz değişkenliğine karşı tampon |
| **Devam eden çalışmalar (WIP)** | Kısmen bitmiş ürünler | Üretim aşamaları arasında tampon |
| **Bitmiş ürünler** | Satışa hazır | Talep değişkenliğine karşı tampon |
| **MRO** (Bakım, Onarım, İşletme) | Operasyonlar için gerekli malzemeler | Üretimi devam ettirin |
| **Emniyet stoku** | Beklenenin üzerinde ekstra stok | Belirsizliğe karşı koruyun |
| **Boru hattı envanteri** | Konumlar arası geçişte | Taşıma sırasında kaçınılmaz |
### Envanter Yönetim Modelleri
| Modeli | Açıklama | Ne Zaman Kullanılmalı |
|----------|----------------|-------------|
| **EOQ** (Ekonomik Sipariş Miktarı) | Toplam stok + sipariş maliyetlerini en aza indiren optimum sipariş boyutu | İstikrarlı talep; sabit teslim süresi |
| **Yeniden sipariş noktası (ROP)** | Envanter belirli bir eşiğe düştüğünde sipariş verin | Sürekli inceleme; öngörülebilir talep |
| **ABC analizi** | Öğeleri değere göre sınıflandırın: A (yüksek), B (orta), C (düşük) | Yönetimin dikkatine öncelik verin |
| **Tam Zamanında (JIT)** | Malları yalnızca üretimde ihtiyaç duyulduğunda alın | İstikrarlı tedarik zinciri; düşük değişkenlik |
| **Satıcı tarafından yönetilen envanter (VMI)** | Tedarikçi envanter seviyelerini yönetiyor | Güçlü tedarikçi ilişkileri |
| **Sevkiyat** | Tedarikçi, kullanılana kadar envanterin sahibidir | Alıcının taşıma maliyetlerini azaltın |
---

## Üretim Sistemleri
### Üretim Yaklaşımları
| Yaklaşım | Açıklama | Cilt | çeşitlilik | Örnek |
|----------|----------------|-----------|------------|------------|
| **İş mağazası** | Özel ürünler; genel amaçlı ekipmanlar | Düşük | Yüksek | Makine atölyesi; özel mobilyalar |
| **Toplu** | Partiler halinde üretin; partiler arası geçiş | Orta | Orta | Fırınlar; eczacılık |
| **Seri üretim** | Yüksek hacimli; özel ekipman; montaj hatları | Yüksek | Düşük | Otomobiller; elektronik |
| **Sürekli akış** | Kesintisiz üretim; tam otomatik | Çok yüksek | Çok düşük | Petrol rafinerisi; kimyasallar; çelik |
| **Toplu kişiselleştirme** | Yüksek hacim + yüksek çeşitlilik; esnek otomasyon | Yüksek | Yüksek | Dell bilgisayarlar; Nike Senin Tarafından |
### Yalın Üretim
| Prensip | Açıklama |
|-----------|----------------|
| **Değer** | Müşterinin neyi değerli bulduğunu tanımlayın |
| **Değer akışı** | Tüm adımları haritalayın; değer katanları belirleyin |
| **Akış** | Değer yaratan adımların kesintisiz ve sorunsuz bir şekilde akmasını sağlayın |
| **Çek** | Yalnızca müşteri talep ettiğinde üretin |
| **Mükemmellik** | Atıkları (muda) sürekli olarak ortadan kaldırın |
### Yedi Çöl (Muda)
| Atık | Açıklama | Örnek |
|----------|----------------|-----------|
| **Fazla üretim** | İhtiyaç duyulandan fazlasını yapmak | Talebin belirsiz olduğu durumlarda tahmin yapmak |
| **Bekliyor** | Adımlar arasındaki boşta kalma süresi | Bir sonraki makineyi bekleyen parçalar |
| **Ulaşım** | Malzemelerin gereksiz hareketi | Ürünlerin uzak depolar arasında taşınması |
| **Aşırı işleme** | Gereğinden fazla iş yapmak | Ekstra denetimler; gereksiz özellikler |
| **Envanter** | İhtiyaç duyulanın ötesinde stok fazlası | Emniyet stoğu "her ihtimale karşı" |
| **Hareket** | İnsanların gereksiz hareketi | Aletleri almak için yürümek; parçalara ulaşma |
| **Kusurlar** | Spesifikasyonları karşılamayan ürünler | Yeniden işleme; hurda; garanti talepleri |
---

## Lojistik ve Taşımacılık
### Ulaşım Modları
| Modu | Maliyet | Hız | Kapasite | En İyisi |
|------|------|----------|----------|----------|
| **Yol** (kamyon) | Orta | Orta | Orta | Son mil; bölgesel; esnek yönlendirme |
| **Demiryolu** | Düşük | Orta | Yüksek | Toplu mallar; karada uzun mesafe |
| **Denizcilik** (gemi) | Çok düşük | Çok yavaş | Çok yüksek | Uluslararası; toplu; konteynerler |
| **Hava** | Çok yüksek | Çok hızlı | Düşük | Yüksek değerli; acil; bozulabilir |
| **Boru hattı** | Düşük (inşaat sonrası) | Sürekli | Yüksek | Yağ; gaz; su |
| **Çok modlu** | Değişir | Değişir | Yüksek | Modları birleştirmek; konteynerle nakliye |
### Depo Tasarımı
| Karar | Seçenekler | Takas |
|----------|------------|-----------|
| **Depo sayısı** | Az (merkezi) vs çok (bölgesel) | Maliyet verimliliği ve teslimat hızı |
| **Otomasyon düzeyi** | Manuel vs yarı otomatik vs tam otomatik | Sermaye maliyeti ile işçilik maliyeti ve doğruluğu |
| **Düzen** | U akışı ve geçiş akışı | Alan kullanımı ve seyahat mesafesi |
| **Depolama sistemi** | Raflar; raf; AS/RS; atlıkarınca | Yoğunluk, erişilebilirlik ve maliyet |
---

## Tedarik Zinciri Risk Yönetimi
### Yaygın Riskler
| Risk Kategorisi | Örnekler | Azaltma |
|-------------|----------|------------|
| **Talep riski** | Tahmin hataları; kırbaç etkisi | Daha iyi tahmin; talep algılama; emniyet stoğu |
| **Tedarik riski** | Tedarikçi iflası; kalite hataları | Çift kaynak kullanımı; tedarikçi denetimleri; emniyet stoğu |
| **Lojistik riski** | Liman tıkanıklığı; taşıyıcı arızaları | Çok modlu; alternatif rotalar |
| **jeopolitik risk** | Tarifeler; ticaret savaşları; yaptırımlar | Yakın kıyıya yanaşma; kaynak sağlayan ülkelerin çeşitlendirilmesi |
| **Doğal afet** | Deprem; sel basmak; salgın | Coğrafi çeşitlilik; iş sürekliliği planları |
| **Siber risk** | Fidye yazılımı; veri ihlali | BT güvenliği; yedekleme sistemleri |
### Kırbaç Etkisi
| Sebep | Açıklama | Çözüm |
|----------|----------------|----------|
| **Talep tahmininin güncellenmesi** | Her aşama kendi güvenlik stoğunu ekler | Satış noktası verilerini zincir genelinde paylaşın |
| **Sipariş toplulaştırma** | Periyodik siparişler talepte artışa neden oluyor | Sipariş döngüsü sürelerini azaltın; EDI |
| **Fiyat dalgalanmaları** | Promosyonlar sırasında ileri alım | Her gün düşük fiyatlandırma; istikrarlı fiyatlandırma |
| **Kıymetlendirme ve eksik oyun** | Kıtlık sırasında aşırı sipariş | Geçmiş satışlara göre tahsis edin; hisse kapasitesi bilgisi |
---

## Modern Tedarik Zinciri Trendleri
| Eğilim | Açıklama | Etki |
|----------|----------------|-----------|
| **Dijital ikizler** | Simülasyon için tedarik zincirinin sanal kopyası | Daha iyi planlama; senaryo analizi |
| **Tedarik zinciri kontrol kuleleri** | Tüm zincir boyunca merkezi görünürlük | Kesintilere daha hızlı yanıt |
| **Yakın kıyıya yakınlaşma / arkadaş kıyısına yakınlaşma** | Üretimi ana ülkeye veya müttefik ülkelere yaklaştırıyor | Azaltılmış risk; daha yüksek maliyet |
| **Döngüsel tedarik zincirleri** | Yeniden kullanım, yeniden üretim, geri dönüşüm için tasarım | Sürdürülebilirlik; kaynak verimliliği |
| **Yapay zeka destekli talep algılama** | Kısa vadeli tahminler için gerçek zamanlı verilerle makine öğrenimi | Daha doğru; daha hızlı yanıt |
| **Otonom araçlar ve insansız hava araçları** | Sürücüsüz kamyonlar; drone teslimatı | Daha düşük maliyet; daha hızlı son mil |
---

## Özet
Tedarik zinciri ve operasyon yönetimi, malların fiziksel akışını verimli, duyarlı ve dayanıklı hale getirmekle ilgilidir. Envanter yönetimi, stok tutma maliyetini stokta kalma riskine karşı dengeler. Üretim sistemleri, atölyelerden (özel, düşük hacimli) sürekli akışa (emtia, yüksek hacimli) kadar çeşitlilik gösterir. Yalın üretim, verimliliği artırmak için israfı ortadan kaldırır. Lojistik kararları (nakliye modu, depo konumu, otomasyon seviyesi) maliyeti ve hizmet kalitesini belirler. Risk yönetimi kırbaç etkisini, tedarikçi başarısızlıklarını, jeopolitik aksaklıkları ve doğal afetleri ele alır. Dijital ikizler, yapay zeka odaklı talep algılama ve yakın kıyıya erişim gibi modern trendler, sektörün giderek istikrarsızlaşan bir dünyaya verdiği tepkiyi yansıtıyor. En iyi tedarik zincirleri yalnızca verimli olmakla kalmaz, aynı zamanda görünürdür, esnektir ve kesintiye karşı hazırlıklıdır.