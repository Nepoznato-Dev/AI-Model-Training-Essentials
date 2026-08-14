---
# Metadata
title: "Relativity"
description: "Special relativity, Lorentz transformations, time dilation, length contraction, mass-energy equivalence, four-vectors, and introduction to general relativity"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into relativity"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [relativity, special-relativity, general-relativity, lorentz-transformations, time-dilation, length-contraction, mass-energy, spacetime]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Görelilik
Einstein'ın görelilik teorileri uzay, zaman ve yerçekimi anlayışımızda devrim yarattı. **Özel görelilik** (1905), uzay ve zamanın ayrı olmadığını, uzay-zaman adı verilen tek bir doku halinde örülmüş olduğunu ve ışık hızının tüm gözlemciler için aynı olduğunu gösterdi. **Genel görelilik** (1915), yerçekimini bir kuvvet olarak değil, kütle ve enerjinin neden olduğu uzay-zamanın eğriliği olarak yeniden tasavvur etti. Bu teoriler GPS navigasyonunu, parçacık hızlandırıcılarını ve kara delikler ile evrenin evrimi hakkındaki anlayışımızı desteklemektedir.
---

## Özel Görelilik Postülatları
Einstein özel göreliliği aldatıcı derecede basit iki önerme üzerine kurdu:
| Varsayım | Açıklama |
|-----------|---------------|
| **Görelilik İlkesi** | Fizik yasaları tüm eylemsiz (ivmelenmeyen) referans çerçevelerinde aynıdır |
| **c'nin sabitliği** | Işığın boşluktaki hızı (c ≈ 3 × 10⁸ m/s), hareketlerinden veya kaynağın hareketinden bağımsız olarak tüm gözlemciler için aynıdır |
Bu iki varsayım bir araya geldiğinde, Newton'un mutlak uzay ve zamana dair yüzyıllardır süregelen sezgilerini alt üst ediyor.
---

## Lorentz Dönüşümleri
**Lorentz dönüşümleri** v bağıl hızıyla hareket eden iki eylemsiz çerçeve arasındaki koordinatları ilişkilendirir.
### Dönüşüm Denklemleri
S çerçevesine göre x ekseni boyunca v hızıyla hareket eden S' çerçevesi için:
| Miktar | Dönüşüm |
|----------|---------------|
| x' | γ(x − vt) |
| t' | γ(t − vx/c²) |
| sen | y |
| z' | z |
burada γ (Lorentz faktörü) = 1/√(1 − v²/c²)
### Lorentz Faktörü γ
| v/c | γ | Efekt |
|-----|---|--------|
| 0 | 1.0 | Göreli etki yok (Newton sınırı) |
| 0.1 | 1.005 | %0,5 düzeltme |
| 0,5 | 1.155 | %15,5 düzeltme |
| 0.9 | 2.294 | Önemli zaman genişlemesi |
| 0,99 | 7.089 | Aşırı etkiler |
| 0,999 | 22.37 | Parçacık hızlandırıcı rejimi |
| → 1 | → ∞ | Devasa nesneler için imkansız |
### Ters Dönüşümler
S''den S'ye geri dönmek için: v'yi -v ile değiştirin.
---

## Zaman Uzaması
Hareket eden saatler yavaş çalışır.
Δt = γΔt₀
burada Δt₀ **uygun zamandır** (saatin dinlenme çerçevesinde ölçülen zaman).
**Çalışılan Örnek:** 10 km yükseklikte oluşturulan bir müon 0,998c sıcaklıkta hareket ediyor. Dinlenme çerçevesinin ömrü 2,2 μs'dir.
- γ = 1/√(1 − 0,998²) ≈ 15,8
- Genişletilmiş kullanım ömrü: Δt = 15,8 × 2,2 μs = 34,8 μs
- Kat edilen mesafe: d = 0,998c × 34,8 μs ≈ 10,4 km
- Zaman genişlemesi olmadan: d = 0,998c × 2,2 μs ≈ 0,66 km (yere asla ulaşamaz)
- **Gerçek:** Müonlar Dünya yüzeyine ulaşıyor; bu da zaman genişlemesini deneysel olarak doğruluyor.
### İkiz Paradoksu
İkizlerden biri yüksek hızda seyahat eder ve geri döner. Onlar evde oturan ikizden daha genç. Gerçek bir paradoks değil; seyahat eden ikiz hızlanır (eylemsiz çerçeveleri değiştirir), simetriyi bozar.
---

## Uzunluk Kısalması
Hareketli nesneler hareket yönü boyunca kısaltılır.
L = L₀/γ
burada L₀ **uygun uzunluk**tur (nesnenin hareketsiz çerçevesinde ölçülen uzunluk).
| v/c | γ | Daralma faktörü L/L₀ |
|-----|---|-------------|
| 0,5 | 1.15 | %87 |
| 0.9 | 2.29 | %44 |
| 0,99 | 7.09 | %14 |
| 0,999 | 22.4 | %4,5 |
**Anahtar nokta:** Uzunluk kısalması optik bir yanılsama değildir; göreceli hareket halindeki gözlemciler tarafından ölçülen gerçek bir fiziksel etkidir.
---

## Eşzamanlılığın Göreliliği
Bir karede eşzamanlı olan olaylar, birincisine göre hareket eden başka bir karede eşzamanlı DEĞİLDİR.
**Einstein'ın tren düşünce deneyi:** Hareket halindeki bir trenin her iki ucuna da yıldırım düşer. Platformdaki bir gözlemci bunları eşzamanlı olarak görüyor. Trendeki bir gözlemci (bir vuruşa doğru ilerlerken) önce öndeki vuruşu görür.
**Sonuç:** "Eşzamanlı" mutlak değildir; gözlemcinin referans çerçevesine bağlıdır.
---

## Hız Toplama
Hızlar yalnızca özel göreliliğe katkıda bulunmaz.
### Göreli Hız Toplama
Eğer bir nesne S' çerçevesinde u' hızıyla hareket ediyorsa ve S', S'ye göre v hızıyla hareket ediyorsa:
u = (u' + v) / (1 + u'v/c²)
| Senaryo | Sonuç |
|----------|-----------|
| u' = c (ışık) | u = c (ışık hızı değişmez) |
| u', v ≪ c | u ≈ u' + v (Galile toplamasına indirgenir) |
| u' = 0,9c, v = 0,9c | u = 0,9945c (asla c'yi aşmaz) |
---

## Kütle-Enerji Eşdeğerliği
E = mc²
| Konsept | Formül | Anlamı |
|-----------|-----------|------------|
| Dinlenme enerjisi | E₀ = mc² | Durgun bir kütlenin enerjisi |
| Toplam enerji | E = γmc² | Kinetik enerji içerir |
| Kinetik enerji | KE = (γ − 1)mc² | v ≪ c | için ½mv²'ye düşer
| Momentum-enerji | E² = (pc)² + (mc²)² | Göreli enerji-momentum ilişkisi |
| Kütlesiz parçacıklar | E = adet | Fotonların enerjisi ve momentumu vardır ancak durgun kütlesi yoktur |
### Nükleer Enerji Örnekleri
| Tepki | Kütle Kusuru | Enerji Serbest Bırakıldı |
|----------|----------------|------|
| U-235 fisyon | kütlenin %0,1'i | ~200 MeV fisyon başına |
| D-T füzyonu | kütlenin %0,7'si | reaksiyon başına 17,6 MeV |
| Madde-antimadde | kütlenin %100'ü | 2mc² (tam dönüşüm) |
---

## Dört-Vektörler ve Uzayzaman
### Minkowski Uzay Zamanı
Özel görelilik, uzay ve zamanı koordinatlarla (ct, x, y, z) 4 boyutlu **Minkowski uzay-zamanında** birleştirir.
### Uzayzaman Aralığı
ds² = −c²dt² + dx² + dy² + dz²
| Aralık Türü | Durum | Anlamı |
|----------------|-----------|-----------|
| **Zamana benzer** | ds²< 0 | Events can be causally connected |
| **Lightlike (null)** | ds² = 0 | Connected by a light signal |
| **Spacelike** | ds² >0 | Olaylar birbirini etkileyemez |
Uzay-zaman aralığı **değişmezdir**; tüm gözlemciler bu aralığın değeri konusunda hemfikirdir.
### Dört-Vektörler
| Dört-Vektör | Bileşenler | Değişmez Miktar |
|------------|-----------|-------------------|
| Pozisyon | (ct, x, y, z) | Uzay-zaman aralığı |
| Hız | γ(c, vₓ, vᵧ, v_z) | Uygun zaman |
| ivme | (E/c, pₓ, pᵧ, p_z) | Kalan kütle: m²c² = E²/c² − p² |
| Kuvvet | dP/dτ | Uygun hızlanma |
---

## Genel Göreliliğe Giriş
### Eşdeğerlik İlkesi
| Sürüm | Açıklama |
|-----------|-----------|
| **Zayıf** | Yerçekimi kütlesi = eylemsizlik kütlesi (tüm nesneler aynı oranda düşer) |
| **Einstein** | Eşit şekilde hızlanan bir çerçeve, yerel olarak yerçekimi alanından ayırt edilemez |
| **Güçlü** | Serbest düşen bir çerçevede tüm fiziksel yasalar (sadece mekanik değil) yerel olarak aynıdır |
### Kavisli Uzay Zaman Olarak Yerçekimi
Genel göreliliğin ana fikri: kütle ve enerji uzay-zamanı eğriler ve nesneler kavisli uzay-zaman boyunca mümkün olan en düz yolları (jeodezikler) takip eder.
**Einstein alan denklemleri:**
G_μν + Λg_μν = (8πG/c⁴) T_μν
| Sembol | Anlamı |
|----------|------------|
| G_μν | Einstein tensörü (uzay-zaman eğriliğini kodlar) |
| Λ | Kozmolojik sabit (karanlık enerji) |
| g_μν | Metrik tensör (uzay-zaman geometrisini tanımlar) |
| G | Newton'un yerçekimi sabiti |
| T_μν | Stres-enerji tensörü (madde ve enerji içeriği) |
**John Wheeler'ın özeti:** "Uzay-zaman maddeye nasıl hareket edeceğini söyler; madde ise uzay-zamanın nasıl kıvrılacağını söyler."
### Genel Göreliliğin Tahminleri
| Tahmin | Açıklama | Onaylandı mı? |
|-----------|----------------|------------|
| Yerçekimi zaman genişlemesi | Daha güçlü yerçekimi alanlarında saatler daha yavaş çalışır | Evet (GPS düzeltme gerektirir) |
| Yerçekimi merceklenmesi | Işık büyük nesnelerin etrafından bükülüyor | Evet (Eddington 1919, Hubble görüntüleri) |
| Yerçekimi kırmızıya kayma | Işık, yerçekimi kuyularından çıkarken enerjisini kaybediyor | Evet (Pound-Rebka 1959) |
| Kara delikler | Uzay-zaman eğriliğinin ışığın kaçmasını engellediği bölgeler | Evet (LIGO, EHT 2019) |
| Yerçekimi dalgaları | Uzay-zamanda hızlanan kütlelerden kaynaklanan dalgalanmalar | Evet (LIGO 2015) |
| Merkür'ün günberi devinimi | Yüzyıl başına ekstra 43 yay saniyesi | Evet (1859'dan bu yana açıklanan anomali) |
| Çerçeve sürükleme | Dönen kütleler uzay-zamanı etraflarında sürükler | Evet (Yerçekimi Sondası B 2011) |
### Schwarzschild Metrik
En basit kara delik çözümü (dönmeyen, yüksüz):
ds² = −(1 − 2GM/rc²)c²dt² + (1 − 2GM/rc²)⁻¹dr² + r²dΩ²
**Schwarzschild yarıçapı:** r_s = 2GM/c²
| Nesne | Kütle | r_s |
|----------|----------|-----|
| Dünya | 6 × 10²⁴ kg | 9mm |
| Güneş | 2 × 10³⁰ kg | 3km |
| Sgr A* (Samanyolu merkezi) | 4 × 10⁶ M☉ | 12 milyon km |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Görelilik Kavramı | Başvuru |
|---------------------|----------------|
| Lorentz dönüşümleri | Lorentz-eşdeğer sinir ağları, simetriye duyarlı modeller |
| Uzay-zaman geometrisi | Geometrik derin öğrenme, çoklu öğrenme |
| Dört vektör | Göreli fizik simülasyonlarında kullanılan tensör gösterimi |
| Yerçekimi zaman genişlemesi | GPS düzeltmeleri (konum tabanlı hizmetler, jeouzaysal ML) |
| Yerçekimi merceklenmesi | Astronomik veri analizi, karanlık madde haritalaması |
| Genel görelilik | Yerçekimi dalgası tespiti için fizik bilgili sinir ağları |
| Riemann geometrisi | Doğal gradyan inişi (bilgi geometrisi), manifold optimizasyonu |
| Metrik tensör | Kavisli uzaylardaki mesafeleri tanımlar — çok yönlü öğrenmenin temeli |
| Jeodezikler | Manifoldlardaki en kısa yollar — robot biliminde, grafik yerleştirmede kullanılır |
| Tensör hesabı | Yüksek boyutlu veri manifoldlarını anlamanın temeli |
---

## Özet
| Konsept | Temel Fikir | Anahtar Denklem |
|-----------|-----------|------------|
| Özel görelilik | Uzay ve zaman birleşmiştir; c mutlaktır | Lorentz dönüşümleri |
| Zaman genişlemesi | Hareketli saatler yavaş çalışır | Δt = γΔt₀ |
| Uzunluk daralması | Hareketli nesneler kısalır | L = L₀/γ |
| Kütle enerjisi | Kütle ve enerji eşdeğerdir | E = mc² |
| Dört vektör | Birleşik uzay-zaman açıklamaları | Değişmez aralık ds² |
| Denklik ilkesi | Yerçekimi = yerel ivme | GR'nin Kuruluşu |
| Genel görelilik | Yerçekimi kavisli uzay-zamandır | G_μν = (8πG/c⁴)T_μν |
| Jeodezikler | Nesneler kavisli uzay-zamanda en düz yolları takip eder | Manifolddaki en kısa yol |
Görelilik, gerçekliğin en temel yönlerine (uzay, zaman, kütle, enerji ve yerçekimi) ilişkin anlayışımızı yeniden şekillendirdi. Matematiksel araçları (tensörler, manifoldlar, jeodezikler, metrik uzaylar) fiziğin çok ötesine geçmiş, geometrik derin öğrenmeyi, doğal gradyan yöntemlerini ve manifold öğrenme algoritmalarını güçlendirdikleri makine öğrenimine geçmiştir.