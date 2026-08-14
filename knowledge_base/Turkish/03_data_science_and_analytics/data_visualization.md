<!--
---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
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
tags: [data, visualization, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Veri Görselleştirme
İyi tasarlanmış bir grafik, sayı tablolarının gizlediği kalıpları ortaya çıkarabilir. Kötü tasarlanmış bir şey yanıltıcı olabilir, kafa karıştırabilir veya sıkıcı olabilir. Veri görselleştirme, verileri kararlara bilgi veren görsel hikayelere dönüştürme sanatıdır. Bu dosya grafik seçimini, tasarım ilkelerini, yaygın hataları ve bunları mümkün kılan araçları kapsar.
---

## Doğru Grafiği Seçmek
Herhangi bir görselleştirmede en önemli karar, verileriniz ve mesajınız için doğru grafik türünü seçmektir.
### Grafik Seçim Kılavuzu
| Hedefiniz | En İyi Grafik Türleri |
|-----------|----------|
| **Kategorileri karşılaştırın** | Çubuk grafik, gruplandırılmış çubuk grafik |
| **Zaman içindeki değişimi göster** | Çizgi grafiği, alan grafiği |
| **Dağılımı göster** | Histogram, kutu grafiği, keman grafiği |
| **İlişkiyi göster** | Dağılım grafiği, kabarcık grafiği |
| **Kompozisyonu göster** | Yığılmış çubuk, pasta grafiği (sınırlı dilimler), ağaç haritası |
| **Korelasyonu göster** | Dağılım grafiği, ısı haritası, çift grafiği |
| **Sıralamayı göster** | Yatay çubuk grafiği |
| **Coğrafi kalıpları göster** | Choropleth haritası, nokta haritası |
| **Zaman içinde parçadan bütüne göster** | Yığılmış alan grafiği |
### Her Grafik Ne Zaman Kullanılmalı
| Grafik | Güçlü Yönler | Ne Zaman Kaçının |
|----------|---------------|-----------|
| **Bar** | Kategoriler arasında net karşılaştırmalar | Çok fazla kategori (>15) |
| **Hat** | Zaman içindeki eğilimler; sürekli veri | Veriler sıralı değil |
| **Dağılım** | İki değişken arasındaki ilişkiler | Çok fazla örtüşen nokta |
| **Histogram** | Tek değişkenin dağılım şekli | Küçük numune boyutları (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Tasarım İlkeleri
### Tufte'nin Temel Fikirleri
Edward Tufte'nin ilkeleri veri görselleştirmede altın standart olmaya devam ediyor:
| Prensip | Açıklama |
|-----------|----------------|
| **Veri-mürekkep oranını en üst düzeye çıkarın** | Her damla mürekkep veriyi iletmelidir. Diğer her şeyi kaldırın. |
| **Çizim önemsizliğini ortadan kaldırın** | 3D efektler, gereksiz degradeler veya dekoratif öğeler yok. |
| **Verileri göster** | Bozmayın, saklamayın veya gelişigüzel seçmeyin. Bırakın veriler konuşsun. |
| **Küçük katlar** | Kategoriler arasında karşılaştırma yapmak için tekrarlanan küçük çizelgeleri kullanın. |
| **Küçük çizgiler** | Satır içi trend verileri için küçük, kelime boyutunda grafikler. |
### Pratik Tasarım Kuralları
| Kural | Neden |
|----------|-----|
| **Y eksenini sıfırdan başlatın** (çubuk grafikler için) | Aksi takdirde farklılıkları abartırsınız |
| **Doğrudan etiketleyin** | Mümkün olduğunda açıklama kullanmak yerine çizgilere/çubuklara etiket koyun |
| **Renkleri bilinçli kullanın** | Önemli olanı vurgulayın; bağlam için griyi kullanın |
| **Basit tutun** | Grafik başına bir mesaj; aşırı yüklemeyin |
| **Tutarlı ölçekler kullanın** | Grafikleri karşılaştırırken eksenleri aynı tutun |
| **Anlamlı bir şekilde sipariş verin** | Doğal bir sıralama olmadığı sürece çubukları değere göre (alfabetik olarak değil) sıralayın |
| **Bağlam sağlayın** | Kıyaslamalar, hedefler veya geçmiş ortalamalar ekleyin |
### Renk Yönergeleri
| Kullanım Örneği | Yaklaşım |
|----------|----------|
| **Kategorik** | Farklı tonlar (mavi, turuncu, yeşil, kırmızı) — maksimum 7–8 kategori |
| **Sıralı** | Tek renk tonunun açıktan koyuya (açık mavi → koyu mavi) |
| **Ayrılan** | Anlamlı bir orta noktaya sahip veriler için iki renkli gradyan (kırmızı ← beyaz → mavi) |
| **Erişilebilirlik** | Renk körü simülatörleriyle test edin; yalnızca renge güvenmeyin (etiket veya desen ekleyin) |
---

## Verilerle Hikaye Anlatımı
Anlatımı olmayan bir grafik sadece bir resimdir. Hikaye anlatımı, verileri içgörüye dönüştürür.
### Hikaye Anlatma Çerçevesi
1. **Bağlam**: Durum nedir? İzleyici zaten ne biliyor?
2. **Çatışma**: Verilerdeki sorun, sürpriz veya gerilim nedir?
3. **Çözüm**: İzleyici bu analizle ne yapmalıdır?
### Pratik İpuçları
| İpucu | Açıklama |
|-----|-------------|
| **İçgörüyle liderlik edin** | Grafiğe verilerle değil, sonuçla başlık verin ("Gelir %30 arttı" değil, "Çeyrek Bazında Gelir") |
| **Önemli noktalara açıklama ekleyin** | Önemli olaylar veya dönüm noktaları için metin açıklamaları ekleyin |
| **Aşamalı açıklamayı kullanın** | Her seferinde bir grafik gösterin; hikayeyi adım adım oluşturun |
| **Önemli olanı vurgulayın** | Önemli veri noktasına dikkat çekmek için renk veya boyut kullanın |
| **"Ne olmuş yani?" deyin** | Her grafik bir soruyu yanıtlamalı veya bir eylemi teşvik etmelidir |
---

## Yaygın Hatalar
| Hata | Neden Kötü | Düzelt |
|-----------|---------------|-----|
| **Kesilmiş y ekseni** | Küçük farkları abartır | Çubuk grafikler için sıfırdan başlayın |
| **Kiraz toplama zaman aralığı** | Trendler hakkında yanıltıcı bilgiler | Mevcut aralığın tamamını göster |
| **Çok fazla renk** | İzleyiciyi şaşkına çeviriyor | 5-7 ile sınırlayın; bağlam için griyi kullanın |
| **Çift y ekseni** | Var olmayabilecek korelasyonu ima eder | İki ayrı grafik kullanın |
| **3 boyutlu grafikler** | Oranları bozuyor | Her zaman 2D'yi kullanın |
| **10'dan fazla dilimli pasta grafikler** | Karşılaştırmak imkansız | Bunun yerine çubuk grafik kullanın |
| **Eksik etiketler** | İzleyici grafiği anlayamıyor | Her zaman eksenleri, başlıkları ve birimleri etiketleyin |
| **Yanıltıcı alan grafikleri** | Yığılmış alanlar bireysel serilerin algısını bozuyor | Çizgi grafikleri veya küçük katları kullanın |
---

## Aletler
### Python
| Kütüphane | Güç |
|-----------|----------|
| **matplotlib** | Python çiziminin temeli; tamamen özelleştirilebilir |
| **deniz doğumlu** | İstatistiksel görselleştirme; güzel varsayılanlar; matplotlib üzerine inşa edildi |
| **komplo** | Etkileşimli, web tabanlı grafikler; gösterge tabloları |
| **altair** | Grafiklerin bildirimsel dilbilgisi (Vega-Lite) |
| **bokeh** | Tarayıcılar için etkileşimli görselleştirme |
### JavaScript / Web
| Kütüphane | Güç |
|-----------|----------|
| **D3.js** | Maksimum esneklik; dik öğrenme eğrisi |
| **Chart.js** | Basit, duyarlı grafikler |
| **Yeniden çizelgeler** | Tepki dostu grafikler |
| **Gözlemlenebilir Arsa** | Hafif, etkileyici grafik grameri |
### Kodsuz / BI Araçları
| Araç | Tür |
|------|------|
| **Tablo** | Endüstri standardında görsel analiz |
| **Power BI** | Microsoft ekosistemi; kurumsal iş zekası |
| **Bakıcı** | Google Bulut; veri araştırması |
| **Metatabanı** | Açık kaynak; basit kurulum |
| **Apache Süper Seti** | Açık kaynak; SQL'de yerel |
---

## Kontrol Paneli Tasarımı
Kontrol paneli, bir süreç, sistem veya iş hakkında eksiksiz bir hikayeyi birlikte anlatan bir görselleştirmeler koleksiyonudur.
### Kontrol Paneli Türleri
| Tür | İzleyici | Amaç |
|------|----------|-----------|
| **Stratejik** | Yöneticiler | Üst düzey KPI'lar; uzun vadeli trendler |
| **Operasyonel** | Yöneticiler | Gerçek zamanlı izleme; günlük operasyonlar |
| **Analitik** | Analistler | Derin keşif; filtreleme, detaya inme |
### Tasarım Kontrol Listesi
- **Kitlenizi tanıyın**: Bu kontrol panelinden hangi kararları alacaklar?
- **5 saniye kuralı**: Ana paket 5 saniyede kavranabilir mi?
- **Düzen**: En önemli metrikler sol üstte (gözlerin ilk gittiği yer).
- **Grafik türlerini sınırlayın**: Tutarlılık için kontrol paneli başına maksimum 3-4 tür.
- **Varsayılan olarak etkileşimli**: Filtreler, tarih aralığı seçiciler, ayrıntılı incelemeler.
- **Performans**: Yüklenmesi 5 saniyeden uzun süren kontrol panelleri kullanılmaz.
- **Mobil**: Kullanıcıların hareket halindeyken ihtiyaç duyması durumunda duyarlı tasarımı değerlendirin.
---

## Özet
İyi veri görselleştirme açıklık, dürüstlük ve etkiyle ilgilidir. Verileriniz için doğru grafiği seçin. Mesaja hizmet etmeyen her şeyi kaldırın. İzleyiciye rehberlik etmek için renk ve açıklamaları kullanın. Ve her zaman hikayeyi verilerin anlatmasına izin verin; tam tersi değil.