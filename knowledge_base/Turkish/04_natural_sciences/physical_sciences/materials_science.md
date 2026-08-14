---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to physical_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
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
# Malzeme Bilimi
Malzeme bilimi, bir malzemenin yapısının (atom, mikroskobik ve makroskobik ölçeklerde) özelliklerini nasıl belirlediğini ve istenen performansı elde etmek için bu yapıyı kontrol etmek için işleme yöntemlerinin nasıl kullanılabileceğini inceleyen çalışmadır. Şu tür soruların yanıtını veren alandır: Çelik neden güçlü ama ağırdır? Cam neden şeffaf ama kırılgandır? Daha hızlı şarj olan pilleri nasıl yapabiliriz? Mars koşullarında hangi malzemeler hayatta kalacak? Kullandığınız her teknoloji, malzemelerden yapılmıştır ve teknolojideki ilerlemeler neredeyse her zaman malzemelerde ilerlemeyi gerektirir.
---

## Malzeme Bilimi Dörtyüzlü
Alanı tanımlayan birbirine bağlı dört unsur:
| Eleman | Açıklama |
|-----------|------------|
| **Yapı** | Atomlar ve moleküller nasıl düzenlenir (kristal yapı; tane sınırları; kusurlar) |
| **Özellikler** | Malzemenin davranışı (mekanik; elektriksel; termal; optik; manyetik) |
| **İşleniyor** | Malzeme nasıl yapılır ve şekillendirilir (döküm; sinterleme; doping; tavlama) |
| **Performans** | Gerçek bir uygulamada malzeme nasıl çalışır |
Temel fikir: İşlemeyi değiştirmek yapıyı değiştirir, bu da özellikleri değiştirir, bu da performansı değiştirir.
---

## Malzeme Sınıfları
### Genel Bakış
| Sınıf | yapıştırma | Anahtar Özellikler | Örnekler |
|----------|------------|---------------|-----------|
| **Metaller** | Metalik (lokalize elektronlar) | Güçlü; sünek; iletken; opak | Çelik; alüminyum; bakır; titanyum |
| **Seramik** | İyonik / kovalent | Zor; kırılgan; ısıya dayanıklı; yalıtım | Alümina; silisyum karbür; bardak; porselen |
| **Polimerler** | Kovalent (zincirler) + van der Waals | Hafif; esnek; yalıtım; düşük erime noktası | Polietilen; naylon; lastik; epoksi |
| **Kompozitler** | İki veya daha fazla sınıfın birleşimi | Özelleştirilmiş özellikler; yüksek mukavemet/ağırlık | Karbon fiber; fiberglas; beton |
| **Yarı İletkenler** | Kovalent (kontrollü safsızlıklarla) | Ayarlanabilir iletkenlik; elektroniğin temeli | Silikon; germanyum; galyum arsenit |
| **Biyomateryaller** | Çeşitli; biyouyumluluk gereklidir | Biyolojik sistemlerle etkileşim | Titanyum implantlar; kolajen; hidroksiapatit |
---

## Kristal Yapılar
### Yaygın Metalik Kristal Yapılar
| Yapı | Birim Hücre Başına Atom | Paketleme Fraksiyonu | Örnekler |
|-----------|-----------|-----------------|-----------|
| **FCC** (Yüz Merkezli Kübik) | 4 | 0,74 (en yakın paket) | Alüminyum; bakır; altın; nikel; ostenit (γ-demir) |
| **BCC** (Gövde Merkezli Kübik) | 2 | 0,68 | Demir (α-demir); krom; tungsten; molibden |
| **HCP** (Altıgen Sıkı Paketlenmiş) | 6 | 0,74 (en yakın paket) | Titanyum; çinko; magnezyum; kobalt |
### Kristal Yapı Neden Önemlidir
| Emlak | Kristal Yapının Etkisi |
|----------|--------------------|
| **Güç** | Kayma sistemleri (atomların kaydığı düzlemler) yapıya göre farklılık gösterir; FCC metalleri HCP'den daha yumuşaktır |
| **Yoğunluk** | Paketleme fraksiyonu atomların ne kadar sıkı paketlendiğini belirler |
| **Faz dönüşümleri** | Demir, 912°C'de BCC'den FCC'ye dönüşür — bu çeliğin ısıl işleminin temelidir |
| **Anizotropi** | Kübik olmayan kristallerde özellikler yöne göre değişebilir |
---

## Mekanik Özellikler
### Temel Metrikler
| Emlak | Tanımı | Birimler | Tipik Değerler |
|----------|-----------|----------|-----|
| **Young modülü (E)** | Sertlik; elastik bölgedeki gerilim / gerinim | not ortalaması | Çelik: 200; Alüminyum: 70; Kauçuk: 0,01–0,1 |
| **Verim gücü** | Kalıcı (plastik) deformasyonun başladığı gerilim | MPa | Çelik: 250–1000; Alüminyum: 40–500 |
| **Çekilme mukavemeti (UTS)** | Arızadan önce maksimum gerilim | MPa | Çelik: 400–2000; Alüminyum: 90–600 |
| **Düzenlik (%uzama)** | Bir malzeme kırılmadan önce ne kadar uzar | % | Çelik: 10–50; Cam: <1 |
| **Dayanıklılık** | Kırılmadan önce emilen enerji (gerilme-gerinim eğrisi altındaki alan) | MJ/m³ | Çelik: yüksek; seramikler: düşük |
| **Sertlik** | Yüzey girintisine karşı direnç | Çeşitli ölçekler | Elmas: en sert; talk: en yumuşak |
### Güçlendirme Mekanizmaları
| Mekanizma | Nasıl Çalışır | Örnek |
|-----------|----------------|-----------|
| **Tahıl inceltme** | Daha küçük taneler = daha fazla tane sınırı = dislokasyonların hareket etmesi daha zor | Hall-Petch ilişkisi |
| **Katı çözüm güçlendirme** | Yabancı atomlar kafesi bozar; dislokasyon hareketini engeller | Bakıra çinko eklenmesi → pirinç |
| **Yağmur sertleşmesi** | Küçük parçacıklar dislokasyon hareketini engeller | Zamanla sertleştirilmiş alüminyum alaşımları |
| **Çalışma sertleşmesi (gerinim sertleşmesi)** | Plastik deformasyon dislokasyon yoğunluğunu arttırır; birbirine karışıyor ve birbirlerine engel oluyorlar | Soğuk haddelenmiş çelik |
| **Kompozit güçlendirme** | Daha yumuşak bir matristeki güçlü lifler yükü taşır | Karbon fiber takviyeli polimer |
---

## Elektriksel ve Termal Özellikler
### Elektriksel İletkenlik
| Malzeme Türü | İletkenlik (S/m) | Mekanizma |
|-------------|------------|-----------|
| **İletkenler** (bakır, gümüş) | 10^7 – 10^8 | Metalik bağlarda serbest elektronlar |
| **Yarı İletkenler** (silikon, GaAs) | 10^-6 – 10^4 | Dopingle ayarlanabilir; bant aralığı mühendisliği |
| **İzolatörler** (cam, kauçuk) | 10^-12 – 10^-20 | Büyük bant aralığı; elektronlar bağlı |
| **Süper İletkenler** | Sonsuz (kritik sıcaklığın altında) | Sıfır elektrik direnci; Meissner etkisi |
### Termal Özellikler
| Emlak | Açıklama | Önemli |
|----------|----------------|---------------|
| **Isı iletkenliği** | Malzemeden ısı ne kadar iyi akıyor | Isı emiciler; yalıtım |
| **Termal genleşme** | Bir malzeme ısıtıldığında ne kadar genişler | Kompozitlerde eşleşen malzemeler; köprüler; raylar |
| **Özgül ısı kapasitesi** | Sıcaklığı 1°C artırmak için gereken enerji | Termal enerji depolama |
| **Erime noktası** | Katının sıvı hale geldiği sıcaklık | Yüksek sıcaklık uygulamaları |
---

## Polimerler
### Polimer Türleri
| Tür | Yapı | Özellikler | Örnekler |
|------|-----------|-----------|-----------|
| **Termoplastikler** | Doğrusal veya dallanmış zincirler; zayıf moleküller arası kuvvetler | Isıtıldığında eritin; geri dönüştürülebilir | Polietilen; polistiren; naylon |
| **Termosetler** | Çapraz bağlı ağ; zincirler arasındaki kovalent bağlar | Erimeyin; yüksek sıcaklıkta ayrışır | Epoksi; vulkanize kauçuk; Bakalit |
| **Elastomerler** | Hafifçe çapraz bağlı; sarmal zincirler | Esnetin ve şekle dönün | Doğal kauçuk; silikon; neopren |
### Polimer Özellikleri
| Emlak | Açıklama |
|----------|----------------|
| **Cam geçiş sıcaklığı (Tg)** | Tg'nin altında: sert ve kırılgan. Tg'nin üstünde: yumuşak ve esnek |
| **Kristallik** | Yarı kristalli polimerler daha güçlü ve daha opaktır; amorflar şeffaftır |
| **Molekül ağırlığı** | Daha yüksek MW = daha güçlü; işlenmesi daha zor |
| **Polimerizasyon derecesi** | Monomer birimlerinin sayısı; özellikleri etkiler |
---

## Faz Diyagramları
### Demir-Karbon Faz Diyagramı (Basitleştirilmiş)
| Aşama | Karbon İçeriği | Yapı | Özellikler |
|----------|---------------|-----------|-----------|
| **Ferrit (α)** | %0,022'ye kadar | BCC demir | Yumuşak; sünek; manyetik |
| **Östenit (γ)** | %2,14'e kadar | FCC demir | Manyetik olmayan; şekillendirilebilir |
| **Sementit (Fe₃C)** | %6,67 | ortorombik | Zor; kırılgan |
| **Perlit** | %0,76 (ötektoid) | Alternatif ferrit ve sementit katmanları | Güçlü; sert |
| **martenzit** | Herhangi biri (hızlı söndürmeyle oluşur) | BCT (vücut merkezli dörtgen) | Çok zor; kırılgan |
---

## Modern ve Gelişen Malzemeler
| Malzeme | Açıklama | Başvuru |
|----------|----------------|------------|
| **Grafen** | Tek katmanlı karbon atomları; bilinen en güçlü malzeme; mükemmel şef | Elektronik; kompozitler; sensörler |
| **Karbon nanotüpleri** | Kıvrılmış grafen silindirleri; olağanüstü güç-ağırlık oranı | Kompozitler; elektronik; enerji depolama |
| **Perovskitler** | Kristal yapı ABX₃; ayarlanabilir bant aralığı | Güneş pilleri; LED'ler; dedektörler |
| **Metal-organik çerçeveler (MOF'ler)** | Gözenekli kristal malzemeler; muazzam yüzey alanı | Gaz depolama; kataliz; ilaç teslimatı |
| **Şekil hafızalı alaşımlar** | Isıtıldığında orijinal şekline dönün | Stentler; aktüatörler; kendi kendini onaran yapılar |
| **Metamateryaller** | Tasarlanmış mikro yapı, doğada bulunmayan özellikler kazandırır | Negatif kırılma indisi; gizleme |
| **Yüksek entropili alaşımlar** | Çoklu temel unsurlar; alışılmadık özellik kombinasyonları | Aşırı ortamlar; havacılık |
---

## Özet
Malzeme bilimi, bir malzemenin atomik yapısını onun makroskobik özelliklerine ve gerçek dünyadaki performansına bağlar. Metaller güçlü ve iletkendir ancak ağırdır. Seramikler sert ve ısıya dayanıklıdır ancak kırılgandır. Polimerler hafif ve esnektir ancak sıcaklıkla sınırlıdır. Kompozitler farklı sınıfların en iyilerini birleştirir. Kristal yapı mekanik davranışı belirler. İşleme (ısıl işlem, alaşımlama, iş sertleştirmesi) mikro yapıyı ve dolayısıyla özellikleri kontrol eder. Grafen, perovskitler ve MOF'lar gibi modern malzemeler mümkün olanın sınırlarını zorluyor. Bu alan temelde disiplinler arasıdır: fizik bağlanmayı, kimya reaksiyonları, mühendislik performansı açıklar ve bunların hepsi akıllı telefonlardan uzay araçlarına kadar her teknoloji için önemlidir.