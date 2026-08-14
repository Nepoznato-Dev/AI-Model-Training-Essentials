<!--
---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sinyal İşleme
Sinyal işleme, sinyallerin (zamana, mekana veya frekansa göre değişen fiziksel niceliklerin temsilleri) analiz edilmesi, değiştirilmesi ve sentezlenmesi bilimidir. Ses, görseller, video, sensör verileri, beyin dalgaları, hisse senedi fiyatları; hepsi sinyaldir. Sinyal işlemenin matematiksel araçları (Fourier dönüşümleri, filtreler, örnekleme teorisi), makine öğrenimi, iletişim, tıbbi görüntüleme ve verilerle çalışan hemen hemen her alanın temelini oluşturur.
---

## Sinyaller ve Sistemler
### Sinyal Sınıflandırması
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| **Sürekli zaman** | Tüm t ∈ ℝ | Ses voltajı, sıcaklık |
| **Ayrık zamanlı** | Tamsayı indekslerinde tanımlanır n | Örneklenmiş ses, piksel değerleri |
| **Analog** | Zaman ve genlik açısından sürekli | Vinil plak oluğu |
| **Dijital** | Zaman ve niceliksel genlik açısından ayrık | MP3 dosyası, JPEG resmi |
| **Periyodik** | x(t + T) = x(t) her t için | Sinüs dalgası, kare dalga |
| **periyodik olmayan** | Tekrarlanan desen yok | Konuşma, müzik |
| **Deterministik** | Tamamen öngörülebilir | Sinüs dalgası |
| **Stokastik** | Rastgelelik içerir | Gürültü, hisse senedi fiyatları |
### Sistem Özellikleri
| Emlak | Tanımı | Örnek |
|----------|-----------|-----------|
| **Doğrusal** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Alçak geçiren filtre |
| **Zamanla değişmez** | Girişte kaydırma → çıkışta aynı kaydırma | Herhangi bir sabit filtre |
| **Nedensel** | Çıktı yalnızca mevcut ve geçmiş girdilere bağlıdır | Gerçek zamanlı sistem |
| **Durağan (BIBO)** | Sınırlı giriş → sınırlı çıkış | İyi tasarlanmış filtre |
| **Hafızasız** | Çıkış yalnızca mevcut girişe bağlıdır | Amplifikatör |
---

## Fourier Dönüşümü
**Fourier dönüşümü** bir sinyali kendisini oluşturan frekanslara ayrıştırır.
### Sürekli Fourier Dönüşümü
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Tersi: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Fourier Dönüşüm Çiftleri
| Zaman Alanı x(t) | Frekans Alanı X(f) |
|---------------------|--------------------------|
| Dikdörtgen darbe | beri işlevi |
| beri işlevi | Dikdörtgen darbe |
| Gauss e^{−at²} | Gaussian (√(π/a))e^{−π²f²/a} |
| Dirac deltası δ(t) | 1 (tüm frekanslar) |
| Karmaşık üstel e^{j2πf₀t} | δ(f - f₀) |
| Kosinüs cos(2πft₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Anahtar Özellikler
| Emlak | Zaman Alanı | Frekans Alanı |
|----------|----------------|------|
| Doğrusallık | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Zaman kayması | x(t − t₀) | X(f)e^{−j2πft₀} |
| Frekans kayması | x(t)e^{j2πf₀t} | X(f − f₀) |
| Evrişim | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Çarpma | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Farklılaşma | dx/dt | j2πf X(f) |
| Parseval teoremi | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Evrişim teoremi:** Zamanda evrişim = frekansta çarpma. Bu en önemli özelliktir; pahalı evrişim işlemlerini ucuz çarpmalara dönüştürür.
### Ayrık Fourier Dönüşümü (DFT)
x[0], x[1], ..., x[N−1] dizisi için:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Emlak | Değer |
|----------|----------|
| Giriş | N gerçek veya karmaşık örnekler |
| Çıkış | N karmaşık frekans kutuları |
| Frekans çözünürlüğü | f_s/N (burada f_s örnekleme hızıdır) |
| Nyquist frekansı | f_s/2 (maksimum temsil edilebilir frekans) |
| Karmaşıklık | O(N²) doğrudan hesaplama |
### Hızlı Fourier Dönüşümü (FFT)
**FFT**, DFT'yi O(N²) yerine O(N log N) cinsinden hesaplar.
| N | O(N²) İşlemleri | O(N log N) İşlemler | Hızlandırma |
|---|------------------|------------|------|
| 1.024 | 1.048.576 | 10.240 | 102× |
| 1.048.576 | 1,1 × 10¹² | 20.971.520 | 52,428× |
FFT şimdiye kadar icat edilen en önemli algoritmalardan biridir. Gerçek zamanlı ses işleme, görüntü sıkıştırma (JPEG), kablosuz iletişim (OFDM) ve spektral analize olanak tanır.
---

## Laplace Dönüşümü
**Laplace dönüşümü** Fourier dönüşümünü kararsız sistemleri ve geçici analizleri yönetecek şekilde genişletir.
F(s) = ∫₀^∞ f(t) e^{−st} dt, burada s = σ + jω
### Ortak Laplace Dönüşümleri
| f(t) | F(ler) | Yakınsama Bölgesi |
|------|------|-----------|
| δ(t) (impuls) | 1 | Hepsi |
| u(t) (adım) | 1/sn | Yanıt(lar) > 0 |
| e^{−at}u(t) | 1/(s+a) | Yanıt(lar) > −a |
| tⁿu(t) | n!/s^{n+1} | Yanıt(lar) > 0 |
| günah(ωt)u(t) | ω/(s²+ω²) | Yanıt(lar) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Yanıt(lar) > 0 |
### Fourier Dönüşümüne Bağlantı
σ = 0 (s = jω) olduğunda Laplace dönüşümü Fourier dönüşümüne indirgenir. Laplace dönüşümü, büyüme/bozunma (σ) hakkındaki bilgileri dahil ederek daha eksiksiz bir resim sağlar.
---

## Z-Dönüşümü
**Z dönüşümü** Laplace dönüşümünün ayrık zamanlı eşdeğeridir.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Yaygın Z-Dönüşümleri
| x[n] | X(z) | ROC |
|------|----------|-----|
| δ[n] | 1 | Hepsi |
| u[n] (adım) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| sin(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Diğer Dönüşümlerle İlişki
| Dönüştürme | Etki Alanı | Değişken |
|-----------|-----------|----------|
| Fourier | Sürekli frekans | f veya ω |
| Laplace | Karmaşık frekans | s = σ + jω |
| Z dönüşümü | Karmaşık frekans (ayrık) | z = e^{sT} |
Z düzlemindeki birim çember (|z| = 1) Fourier dönüşümüne karşılık gelir.
---

## Filtreler
Filtreler belirli frekans bileşenlerini seçici olarak geçirir veya engeller.
### Filtre Türleri
| Tür | Geçişler | Bloklar | Başvuru |
|------|--------|--------|-------------|
| **Alçak geçiş** | Düşük frekanslar | Yüksek frekanslar | Pürüzsüzleştirme, kenar yumuşatma |
| **Yüksek geçiş** | Yüksek frekanslar | Düşük frekanslar | Kenar algılama, gürültü giderme |
| **Bant geçişi** | Çeşitli frekanslar | Menzilin dışında | Kanal seçimi (radyo) |
| **Bant durdurma (çentik)** | Bir aralık dışında her şey | Belirli bir aralık | Güç hattı vızıltısının giderilmesi |
### FIR ve IIR Filtreleri
| Emlak | FIR (Sonlu Dürtü Tepkisi) | IIR (Sonsuz Dürtü Tepkisi) |
|----------|-------------------------------|--------------------------------|
| Dürtü yanıtı | Sonlu süre | Sonsuz süre |
| Kararlılık | Her zaman istikrarlı | Kararsız olabilir |
| Aşama | Tam olarak doğrusal olabilir | Genellikle doğrusal olmayan faz |
| Geribildirim | Hayır | Evet |
| Hesaplama | Daha fazla katsayıya ihtiyaç var | Aynı yuvarlanma için daha az katsayı |
| Tasarım | Pencereleme, Parklar-McClellan | Butterworth, Chebyshev, eliptik |
| Aktarım fonksiyonu | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Filtre Tasarımı Özellikleri
| Parametre | Açıklama |
|-----------|----------------|
| **Geçiş bandı** | Minimum kayıpla geçmesi gereken frekans aralığı |
| **Durdurma bandı** | Zayıflatılması gereken frekans aralığı |
| **Kesim frekansı** | Geçiş bandı ve durdurma bandı arasındaki sınır |
| **Dalgalanma** | Geçiş bandı (veya durdurma bandı) kazancındaki değişiklik |
| **Geri alma** | Zayıflama oranı (oktav veya on yıl başına dB) |
| **Geçiş bandı** | Geçiş bandı ve durdurma bandı arasındaki bölge |
### Ortak Filtre Tasarımları
| Tasarım | Özellikler | Kullanım Örneği |
|----------|-----|----------|
| **Butterworth** | Maksimum düz geçiş bandı, orta düzeyde yuvarlanma | Genel amaçlı |
| **Çebişev Tip I** | Geçiş bandında dalgalanma, daha dik dönüş | Geri çekilme önemli olduğunda |
| **Çebişev Tip II** | Durdurma bandında dalgalanma, düz geçiş bandı | Geçiş bandının düzlüğü önemli olduğunda |
| **Eliptik (Cauer)** | Her ikisinde de dalgalanma, en dik düşüş | Minimum sipariş gerekli |
| **Bessel** | Doğrusal faz (maksimum düz grup gecikmesi) | Dalga formu şeklini koruma |
---

## Örnekleme Teorisi
### Nyquist-Shannon Örnekleme Teoremi
Örnekleme hızı maksimum frekansın iki katını aşarsa, sürekli bir sinyal örneklerinden mükemmel şekilde yeniden oluşturulabilir:
f_s > 2f_max
| Dönem | Tanımı |
|------|------------|
| **Örnekleme oranı** (f_s) | Saniyedeki örnek sayısı |
| **Nyquist oranı** | 2f_max (minimum örnekleme oranı) |
| **Nyquist frekansı** | f_s/2 (maksimum temsil edilebilir frekans) |
| **Tam Adlandırma** | f_s < 2f_max | olduğunda düşük frekanslar gibi görünen yüksek frekanslar |
### Ortak Örnekleme Oranları
| Başvuru | Oranı | Nyquist Frekansı |
|------------|----------|-------|
| Telefon konuşması | 8 kHz | 4 kHz |
| Ses CD'si | 44,1 kHz | 22,05 kHz |
| Profesyonel ses | 48 kHz | 24 kHz |
| Yüksek çözünürlüklü ses | 96 kHz | 48 kHz |
| Video (30 fps) | 30 Hz (zamansal) | 15Hz |
### Kenar Yumuşatma
Örneklemeden önce, bir **kenar yumuşatma filtresi** (düşük geçiş), örtüşmeyi önlemek için f_s/2'nin üzerindeki frekansları kaldırır.
---

## Pencereleme
Bir sinyalin sonlu bir bölümünü analiz ederken, dolaylı olarak dikdörtgen bir pencereyle çarparız ve bu da spektral sızıntıya neden olur. **Pencere işlevleri** bu sızıntıyı azaltır.
### Ortak Windows
| Pencere | Ana Lob Genişliği | Yan Lob Seviyesi | Kullanım Örneği |
|----------|----------------|----------|----------|
| Dikdörtgen | En Dar | −13 dB | Çözünürlük en önemli olduğunda |
| Han | 2× dikdörtgen | −31 dB | Genel amaçlı |
| Hamming | 2× dikdörtgen | −41 dB | En yakın yan lob azaltıldı |
| Kara Adam | 3× dikdörtgen | −58 dB | Yüksek dinamik aralık |
| Kaiser | Ayarlanabilir | Ayarlanabilir (β aracılığıyla) | Takas ayarlanabilir olduğunda |
### Spektral Sızıntı
Bir sinyalin bir pencere ile çarpılması, onun spektrumunu pencerenin spektrumuyla evriştirir. Daha geniş ana loblar frekans çözünürlüğünü azaltır; alt yan loblar sızıntıyı azaltır.
---

## Dalgacıklar
**Dalgacıklar**, çoklu çözünürlüklü sinyal analizi için kullanılan küçük, yerelleştirilmiş dalga benzeri işlevlerdir.
### Dalgacık Dönüşümü
Fourier dönüşümünün (küresel frekans bilgisi veren) aksine, dalgacık dönüşümü **zaman-frekans** lokalizasyonu sağlar.
| Dönüştürme | Zaman Çözünürlüğü | Frekans Çözünürlüğü |
|---------------------|-----|----------|
| Fourier | Yok (küresel) | Mükemmel |
| Kısa Süreli FT | Sabit (pencere boyutu) | Sabit |
| Dalgacık | Değişken (yüksek frekansta iyi) | Değişken (düşük frekansta iyi) |
### Ortak Dalgacık Aileleri
| Aile | Özellikler | Başvuru |
|----------|---------------|------------|
| **Haar** | En basit, süreksiz | Kenar algılama, hızlı analiz |
| **Daubechies** (dbN) | Kompakt destek, N sayıda kaybolan an | Sıkıştırma, gürültü giderme |
| **Symlets** | Neredeyse simetrik Daubechies | Azaltılmış faz bozulması |
| **Coiflet'ler** | Anlık koşullar için tasarlandı | Sinyal işleme |
| **Morlet** | Gauss pencereli sinüzoid | Zaman-frekans analizi |
| **Meksika Şapkası** | Gaussian'ın ikinci türevi | Özellik algılama |
### Dalgacıkların Uygulamaları
| Başvuru | Dalgacıklar Nasıl Yardımcı Olur |
|---------------|-----------|
| Görüntü sıkıştırma (JPEG 2000) | Çoklu çözünürlüklü gösterim, kenarlar için DCT'den daha iyi |
| Gürültü Giderme | Eşik küçük dalgacık katsayıları (sinyal büyük katsayılardadır) |
| Özellik algılama | Kenar algılama, zaman serilerinde geçici algılama |
| EKG analizi | QRS komplekslerinin tespiti, aritmi sınıflandırması |
| Sismik analiz | Jeolojik katmanların belirlenmesi, deprem sinyali işleme |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Sinyal İşleme Konsepti | Başvuru |
|--------------------------|---------------|
| Fourier dönüşümü | Ses ML'si için spektral özellikler, zaman serilerinin frekans alanı analizi |
| FFT | CNN'lerde hızlı evrişim (spektral evrişim), verimli korelasyon |
| Evrişim teoremi | CNN'lerin nasıl çalıştığını anlamak (bunlar öğrenilmiş filtrelerdir) |
| Filtreler | Ön işleme (düzleştirme, gürültü giderme), özellik çıkarma |
| Örnekleme teoremi | Ayrıklaştırmayı anlama, sensör hızlarını seçme, takma adlardan kaçınma |
| Pencereleme | Ses ML'si (spektrogramlar) için STFT, zaman-frekans analizi |
| Dalgacıklar | Zaman serileri için özellik çıkarma, sıkıştırma, gürültü giderme |
| Laplace/Z dönüşümü | Robotik için kontrol teorisi, sistem kararlılığını anlama |
| Spektral analiz | EEG/fMRI analizi, titreşim izleme, kestirimci bakım |
| Nyquist kuru | Makine öğrenimi ardışık düzenleri için uygun veri toplama hızlarını seçme |
---

## Özet
| Araç | Etki Alanı | Temel Bilgiler |
|------|--------|------------|
| Fourier Dönüşümü | Zaman → Frekans | Sinyaller sinüzoidlerin toplamıdır |
| Laplace Dönüşümü | Zaman → Karmaşık frekans | Geçici durumları ve kararlılığı yönetir |
| Z-Dönüşümü | Ayrık zaman → Karmaşık | Dijital filtre analizi ve tasarımı |
| FFT | Verimli DFT hesaplaması | O(N log N) yerine O(N²) |
| Filtreler | Frekans seçimi | İhtiyacınız olanı iletin, ihtiyacınız olanı engelleyin |
| Örnekleme Teoremi | Sürekli ↔ ayrık | Yeterince hızlı örnek alın, hiçbir şey kaybetmeyin |
| Pencereleme | Zaman-frekans dengesi | Terazi çözünürlüğü ve sızıntı |
| Dalgacıklar | Çoklu çözünürlüklü analiz | Hem zaman hem de sıklık açısından yerel |
Sinyal işleme, verileri anlamak, analiz etmek ve işlemek için matematiksel temel sağlar. Zaman serileri, ses, görüntüler veya sensör verileriyle çalışan her makine öğrenimi ardışık düzeni, dolaylı olarak sinyal işleme kavramlarını kullanır. Özellikle Fourier dönüşümü, herhangi bir veri bilimci için tartışmasız hesaplamadan sonra en önemli matematiksel araçtır.