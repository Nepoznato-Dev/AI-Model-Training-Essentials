<!--
---
# Metadata
title: "Geospatial Analysis"
description: "Coordinate systems, spatial operations, GeoPandas, raster analysis"
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
tags: [geospatial, analysis, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Jeo-uzaysal Analiz
Jeo-uzaysal analiz, coğrafi bir bileşeni olan verileri (koordinatlar, adresler, sınırlar veya Dünya üzerindeki bir konuma bağlı herhangi bir veri) inceleme sürecidir. "Müşterilerimiz nerede?", "en uygun rota nedir?" ve "arazi kullanımı zaman içinde nasıl değişiyor?" gibi sorulara yanıt verir. Her veri kümesinin uzamsal bir boyutu vardır ve bunu anlamak, saf istatistiksel analizin gözden kaçırdığı içgörülerin kilidini açar.
---

## Temel Kavramlar
### Koordinat Sistemleri
| Sistem | Açıklama | Kullanım Örneği |
|----------|----------------|----------|
| **WGS 84 (EPSG:4326)** | Küresel standart; derece cinsinden enlem/boylam | KÜRESEL KONUMLAMA SİSTEMİ; çoğu web haritalaması; GeoJSON |
| **Web Mercator (EPSG:3857)** | Küreyi bir silindire yansıtır; kutuplardaki alanı bozuyor | Google Haritalar; Harita kutusu; çoğu web döşeme hizmetleri |
| **UTM** (Evrensel Enine Mercator) | Dünyayı 60 bölgeye ayırır; metre bazlı | Askeri; araştırma; yüksek hassasiyetli yerel çalışma |
| **İngiliz Ulusal Şebekesi (EPSG:27700)** | OSGB36 verisi; metre bazlı | İngiltere haritalaması |
| **Yerel öngörüler** | Belirli bölgeler için özel projeksiyonlar | Belirli bir alan için distorsiyonu en aza indirin |
### Geometri Türleri
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Nokta** | Tek koordinat | Bir restoran; bir sensör; bir müşteri |
| **LineString** | Sıralı nokta dizisi | Bir yol; bir nehir; bir rota |
| **Çokgen** | İçi kapalı şekil | Bir ülke; bir göl; teslimat bölgesi |
| **Çok Noktalı** | Puanların toplanması | Bir şehirdeki tüm otobüs durakları |
| **MultiLineString** | Hat koleksiyonu | Bir ağdaki tüm yollar |
| **Çoklu Çokgen** | Çokgen koleksiyonu | Bir takımada; adaları olan bir ülke |
| **GeometriKoleksiyonu** | Karışık türler | Şehirleri, yolları ve nehirleriyle bir ülke |
---

## Veri Formatları
| Biçim | Tür | Temel Özellik |
|----------|----------|------------|
| **GeoJSON** | Metin (JSON) | İnsan tarafından okunabilir; web dostu; tüm geometri türlerini destekler |
| **Şekil dosyası** | İkili (birden fazla dosya) | ESRI'den eski format; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Earth; 3D'yi ve zamanı destekler |
| **Coğrafi paket** | SQLite tabanlı | Tek dosya; raster ve vektörü destekler; modern standart |
| **GeoParke** | Sütunlu (Parke) | Büyük veri kümeleri için verimlidir; veri mühendisliği araçlarıyla entegre olur |
| **WKT / WKB** | Metin / İkili | Tanınmış Metin; Tanınmış İkili; veritabanı depolaması için kullanılır |
| **MVT** | İkili | Mapbox Vektör Döşemeleri; harita verilerini web istemcilerine sunmak için |
---

## Uzaysal Operasyonlar
### Temel İşlemler
| Operasyon | Açıklama | Örnek |
|-----------|----------------|-----------|
| **Mesafe** | Geometriler arasındaki mesafeyi hesaplayın | "10 km yakınındaki tüm hastaneleri bul" |
| **Tampon** | Belirli bir mesafede bir geometri etrafında çokgen oluşturun | "Bir okulun etrafındaki 500 metrelik alanı gösterin" |
| **Kavşak** | Geometriler arasındaki örtüşen alanı bulun | "Sel bölgesinde hangi parseller var?" |
| **Birlik** | Geometrileri tek bir geometride birleştirin | "Tüm arazi parsellerini tek bir bölgede birleştirin" |
| **Fark** | Bir geometriyi diğerinden çıkarın | "Korunan bölgeler hariç inşa edilebilir alan" |
| **İçerir / İçerisinde** | Bir geometrinin diğerinin içinde olup olmadığını test edin | "Bu teslimat bölgesinde hangi müşteriler var?" |
| **En yakın komşu** | En yakın geometriyi bulun | "En yakın itfaiye istasyonu hangisi?" |
| **Uzaysal birleştirme** | Uzamsal ilişkiye dayalı nitelikleri birleştirin | "Her noktayı kendi nüfus sayımı sistemine atayın" |
### Uzamsal İndeksleme
| Dizin Türü | Açıklama | Kullanım Örneği |
|-----------|----------------|----------|
| **R-ağacı** | Sınırlayıcı kutu hiyerarşisi; en yaygın | PostGIS; SQLite; genel amaçlı |
| **Dörtlü ağaç** | Çeyreklere özyinelemeli alt bölüm | Nokta verileri; oyun motorları |
| **Geohash** | Hiyerarşik ızgara; dizeyi kodlar | Yakınlık araması; veritabanı parçalama |
| **H3** (Uber) | Altıgen hiyerarşik ızgara | Analitik; yolculuk paylaşımı; üniforma kutuları |
| **S2** (Google) | Küre üzerinde hücre tabanlı hiyerarşi | Büyük ölçekli mekansal indeksleme |
---

## Araçlar ve Kütüphaneler
| Araç / Kitaplık | Dil | Açıklama |
|---------------|----------|------------|
| **PostGIS** | SQL (PostgreSQL) | Uzamsal veritabanları için altın standart; tam uzaysal SQL |
| **QGIS** | Masaüstü (Python/C++) | Ücretsiz, açık kaynaklı CBS; eklenti ekosistemi |
| **GeoPandalar** | Python | Pandalar + Düzgün + Fiona; mekansal Veri Çerçeveleri |
| **Düzgün** | Python | Geometri işlemleri; GEOS'a dayalı |
| **Folyum** | Python | Python'dan İnteraktif Broşür haritaları |
| **Turf.js** | JavaScript | İstemci tarafı coğrafi analiz |
| **Deck.gl** | JavaScript | Haritalarda büyük ölçekli veri görselleştirmesi |
| **GDAL** | C++ (Python bağlamalarıyla) | Raster ve vektör veri çevirisi; İsviçre çakısı |
| **Rasterio** | Python | Tarama verilerini okuma/yazma; GDAL'a dayalı |
| **Kepler.gl** | JavaScript | WebGL destekli coğrafi görselleştirme |
---

## Jeo-uzaysal Analiz Modelleri
### Ortak Analiz Türleri
| Desen | Açıklama | Kullanım Örneği |
|-----------|---------------|----------|
| **Nokta deseni analizi** | Puan dağılımını inceleyin | Suç haritalaması; hastalık salgını tespiti |
| **Sıcak nokta analizi** | İstatistiksel olarak anlamlı kümeleri bulun | Perakende satış yeri; suç; epidemiyoloji |
| **Ağ analizi** | Rota optimizasyonu; servis alanları | Lojistik; acil müdahale; kamu hizmetleri |
| **Uzaysal enterpolasyon** | Örneklenmemiş konumlardaki değerleri tahmin edin | Hava kalitesi; toprak özellikleri; hava durumu |
| **Arazi kullanımı değişikliği tespiti** | Zaman içindeki uydu görüntülerini karşılaştırın | Kentsel yayılma; ormansızlaşma; tarım |
| **Uygunluk analizi** | Birden çok kriteri karşılayan konumları bulun | Yer seçimi; koruma planlaması |
| **Uzaysal otokorelasyon** | Yakındaki değerlerin nasıl ilişkili olduğunu ölçün | Emlak fiyatları; hastalığın yayılması |
### Değiştirilebilir Alan Birimi Sorunu (MAUP)
| Görünüş | Sorun |
|----------|------------|
| **Ölçek efekti** | Sonuçlar, analiz birimlerinin boyutuna bağlı olarak değişir (nüfus sayımı bölgeleri, ilçeler ve eyaletler) |
| **İmar etkisi** | Sonuçlar, aynı ölçekte bile sınırların nasıl çizildiğine bağlı olarak değişir |
| **Sonuç** | Hiçbir zaman bir toplama düzeyindeki sonuçların diğerinde geçerli olduğunu varsaymayın; daima sınırlara karşı hassasiyeti test edin |
---

## Pratik Hususlar
| endişe | Rehberlik |
|-----------|----------|
| **Koordinat referans sistemleri** | Her zaman CRS'yi kontrol edin; tahminleri asla hesaplamalara karıştırmayın; mesafeleri hesaplamadan önce dönüşüm |
| **Hassaslık** | Kayan nokta hassasiyeti küçük ölçeklerde önemlidir; uygun veri türlerini kullanın |
| **Performans** | Uzaysal operasyonlar pahalıdır; mekansal indeksleri kullanın; gösterim için geometrileri basitleştirin |
| **Topoloji** | Analizden önce geometrilerin geçerli olduğundan emin olun (kendi kendine kesişme yok, kapalı çokgenler).
| **Ölçek** | Web Mercator alanı bozuyor; alan hesaplamaları için kullanmayın |
| **Veri kalitesi** | Sıfır geometrileri, yinelenen köşe noktalarını, şerit çokgenlerini kontrol edin |
---

## Özet
Jeo-uzaysal analiz, konum verilerini eyleme dönüştürülebilir içgörülere dönüştürür. Noktalar, çizgiler ve çokgenler gerçek dünyadaki varlıkları temsil eder. Uzamsal işlemler (mesafe, tampon, kesişme, birleştirme) yakınlık, örtüşme ve sınırlama hakkındaki soruları yanıtlar. Araçlar, veritabanı ölçeğinde analiz için PostGIS'ten Python iş akışları için GeoPandas'a ve web görselleştirmesi için Deck.gl'ye kadar çeşitlilik gösterir. Temel zorluklar, doğru koordinat sistemini seçmek, büyük veri kümeleriyle performansı yönetmek ve toplama sınırları seçiminizin sonuçlarınızı etkilediği gerçeği olan MAUP'ın farkında olmaktır. İster teslimat rotalarını optimize ediyor, ister hastalığın yayılmasını analiz ediyor, ister kentsel büyümeyi haritalandırıyor olun, jeouzaysal analiz, saf sayıların yakalayamayacağı mekansal bağlamı sağlar.