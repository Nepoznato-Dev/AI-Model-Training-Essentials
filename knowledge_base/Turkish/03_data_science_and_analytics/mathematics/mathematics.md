<!--
---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Matematik
Matematik yalnızca okulda çalışılan bir ders değildir; neredeyse her teknik alanın temelini oluşturur. Fizik bunu evreni tanımlamak için kullanır. Bilgisayar bilimi bunu algoritma tasarlamak için kullanır. Makine öğrenimi bunu ağırlıkları optimize etmek için kullanır. Finans bunu fiyat riskine karşı kullanıyor. Her dalda ustalık gerekli değildir, ancak ortamı anlamak ve her dalın nerede geçerli olduğunu bilmek diğer konuların anlaşılmasını kolaylaştırır.
---

## Sayı Sistemleri
Her şeyden önce, üzerinde çalıştığınız sayı türlerini anlamanıza yardımcı olur. Her katman, eski katmanın çözemediği bir sorunu çözmek için bir öncekini genişletir.
| Numara Türü | Neleri İçerir | Neden İcat Edildi | Örnek |
|---|---|---|---|
| Doğal sayılar | 1, 2, 3, 4,... | Nesneleri sayma | 5 elma |
| Tam sayılar | 0, 1, 2, 3, ... | "Hiçbir şey"i temsil etme | 0 derece |
| Tamsayılar | ..., −2, −1, 0, 1, 2, ... | Borç, sıcaklık sıfırın altında | −15°C |
| Rasyonel sayılar | p/q burada q ≠ 0 | Eşyaları eşit olmayan bir şekilde bölmek | 1/3, 0,75 |
| İrrasyonel sayılar | Kesirler olarak ifade edilemez | Köşegenler, daireler, büyüme | √2, π, e |
| Gerçek sayılar | Hepsi rasyonel + irrasyonel | Tam sayı doğrusu | 3.14159... |
| Hayali sayılar | i'nin katları = √(−1) | x² + 1 = 0'ın çözümü | 3i |
| Karmaşık sayılar | a + bi (gerçek + sanal) | Elektrik mühendisliği, kuantum mekaniği | 2 + 3i |
---

## Aritmetik ve Sayılar Teorisi
Temel bilgiler: toplama, çıkarma, çarpma, bölme ve bunların sırasını belirleyen kurallar.
**İşlem sırası** (PEMDAS/BODMAS): Parantez → Üslü Sayılar → Çarpma/Bölme (soldan sağa) → Toplama/Çıkarma (soldan sağa).
**Asal sayılar** yani 1'den ve kendisinden başka böleni olmayan 1'den büyük tam sayılar, sayı teorisinin atomlarıdır. İlk birkaçı: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Asal sayılar neden matematik dersinin ötesinde önemlidir: Modern şifreleme (RSA), iki büyük asal sayıyı çarpmanın kolay olduğu gerçeğine dayanır, ancak sonucu geri çarpanlara ayırmanın hesaplama açısından acımasız olduğu gerçeğine dayanır.
**Yararlı işlemler:**
- Asal çarpanlara ayırma: 84 = 2² × 3 × 7
- 24 ve 36'nın En Büyük Ortak Bölünü (GCD): 12
- 4 ve 6'nın En Küçük Ortak Katı (LCM): 12
---

## Cebir
Cebir, belirli sayılarla çalışmayı bırakıp *ilişkilerle* çalışmaya başladığınız yerdir.`x`gibi bir değişkenin sabit bir değeri yoktur; denklemi doğru kılan şeyi temsil eder.
**İkinci dereceden formül** ax² + bx + c = 0'ı çözer:
x = (−b ± √(b² − 4ac)) / 2a
**Genel işlev türleri ve göründükleri yerler:**
| İşlev | Formül | Şekil | Gerçek Dünya Örneği |
|---|---|---|---|
| Doğrusal | y = mx + b | Düz çizgi | Sabit oranda birim başına maliyet |
| İkinci Dereceden | y = ax² + bx + c | Parabol | Mermi hareketi, fren mesafesi |
| Üstel | y = a × b² | Hızlı büyüme/çürüme | Bileşik faiz, nüfus artışı, viral yayılma |
| Logaritmik | y = log_b(x) | Yavaş büyüme, üstel büyümenin tersi | Desibel ölçeği, pH ölçeği, algoritma karmaşıklığı |
**Anahtar kelimeler:**
- **Domain**: all valid inputs (e.g., can't divide by zero, can't take √ of a negative in reals)
- **Aralık**: tüm olası çıkışlar
- **Slope** (m): rate of change — "for every 1 unit of x, y changes by m"
- **Intercept**: where the function crosses an axis
---

## Geometri
Geometri şekilleri, boyutları ve mekansal ilişkileri inceler. Her yerde karşımıza çıkıyor: Oyun motorları onu render için kullanıyor, robot bilimi onu yol planlaması için kullanıyor, mimari onu yapısal tasarım için kullanıyor.
**Temel formüller:**
| Şekil | Emlak | Formül |
|---|---|---|
| Üçgen | Açı toplamı | 180° |
| Dörtgen | Açı toplamı | 360° |
| daire | Çevre | 2πr |
| daire | Alan | πr² |
| Küre | Cilt | (4/3)πr³ |
| Sağ üçgen | Pisagor teoremi | a² + b² = c² |
**π (pi)** ≈ 3,14159 — herhangi bir dairenin çevresinin çapına oranı. Beklemeyeceğiniz yerlerde ortaya çıkıyor: olasılık (normal dağılım), mühendislik (sinyal işleme), hatta Heisenberg'in belirsizlik ilkesi denklemi.
---

## Matematik
Matematik *değişimi* ve *birikimi* inceler. Eğer cebir anlık görüntüleri ele alıyorsa, matematik de hareketli görüntüleri ele alır.
### Diferansiyel Hesabı
Değişim oranları. F'(x) türevi size f'nin herhangi bir noktada ne kadar hızlı değiştiğini söyler.
| Fonksiyon f(x) | Türev f'(x) | Sezgi |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Güç kuralı |
| eˣ | eˣ | Kendi türevine eşit olan tek fonksiyon |
| ln(x) | 1/x | x arttıkça büyüme hızı yavaşlar |
| günah(x) | çünkü(x) | Salınım değişim hızı |
**ML'de türevler neden önemlidir:** gradyan iniş - çoğu sinir ağını eğiten algoritma - kayıp fonksiyonunun türevlerini hesaplayarak ve hatayı azaltan yönde adım atarak çalışır.
### Temel Farklılaştırma Kuralları
| Kural | Formül | Kullanım Örneği |
|------|------------|----------|
| **Zincir Kuralı** | (f∘g)' = f'(g(x)) · g'(x) | İç içe geçmiş işlevler — sinir ağlarında geri yayılım |
| **Ürün Kuralı** | (fg)' = f'g + fg' | x'in iki fonksiyonunun çarpılması |
| **Bölüm Kuralı** | (f/g)' = (f'g − fg') / g² | x'in iki fonksiyonunu bölme |
### İntegral Hesabı
Birikim. İntegral bir eğrinin altındaki alanı temsil eder. Türevler "Ne kadar hızlı değişiyor?" sorusunu yanıtlıyorsa, integraller "Ne kadar birikti?" sorusunu yanıtlıyor.
**Kalkülüsün temel teoremi** her ikisini de birbirine bağlar: türev alma ve entegrasyon ters işlemlerdir.
| İntegral | Sonuç | Kullanım Örneği |
|----------|-----------|----------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Polinom eğrilerinin altındaki alan |
| ∫ eˣ dx | eˣ + C | Toplam birikmiş büyüme |
| ∫ 1/xdx | ln|x| + C | Logaritmik birikim |
---

## Setler
**küme** farklı nesnelerin bir koleksiyonudur; modern matematiğin temelidir.
| Operasyon | Sembol | Anlamı | Örnek (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Birliği | A ∪ B | Her iki kümedeki öğeler | {1, 2, 3, 4} |
| Kavşak | bir ∩ B | Her iki kümedeki öğeler | {2} |
| Fark | A \ B | A'daki ancak B'deki olmayan öğeler | {1, 3} |
| Boş set | ∅ | Hiçbir şey içermiyor | {} |
| Altküme | A ⊂ B | A'nın tüm elemanları B'dedir | {1,2} ⊂ {1,2,3} |
Küme teorisi veritabanlarında (SQL JOIN'ler esasen ayarlanmış işlemlerdir), olasılıkta (olaylar sonuç kümeleridir) ve programlamada (kümeler, karma haritalar) ortaya çıkar.
---

## İkili ve Sayı Tabanları
Bilgisayarlar ikili (taban 2) olarak düşünür: yalnızca 0'lar ve 1'ler. İnsanlar ondalık sayıyla (10 tabanında) düşünürler. Programcılar ikiliyi temsil etmenin kompakt bir yolu olarak genellikle onaltılık sistemi (16 tabanı) kullanırlar.
| Baz | Kullanılan Rakamlar | Örnek | Ondalık Eşdeğeri |
|---|---|---|---|
| İkili (taban 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Ondalık (10 tabanı) | 0–9 | 11 | 11 |
| Onaltılık (taban 16) | 0–9, A–F | B | 11 |
| Onaltılı | 0–9, A–F | A3 | 160 + 3 = 163 |
**Neden önemlidir:** Bir bilgisayardaki her veri parçası (metin, resim, ses, video) sonuçta yalnızca ikilidir. Bir bayt (8 bit) 256 farklı değeri temsil edebilir. CSS'deki renkler (#FF5733), bellek adresleri (0x7FFF) ve IP adreslerinin tümü hex kullanır çünkü uzun ikili dizeleri okunabilir bir şeye sıkıştırır.
---

## Makine Öğrenmesi ve Grafikler için Doğrusal Cebir
Doğrusal cebir (vektörler, matrisler ve dönüşümler) makine öğreniminin, bilgisayar grafiklerinin, fizik simülasyonlarının ve arama motorlarının arkasındaki matematiksel motordur.
### Vektörler
**Vektörler** sıralı sayı listeleridir. ML'de her veri noktası, özelliklerin bir vektörüdür:
- [23, 1.8, 75] kişinin yaşını, metre cinsinden boyunu ve kg cinsinden ağırlığını temsil edebilir.
| Vektör İşlemi | Formül | Kullanım Örneği |
|----------------|------------|----------|
| **Ekleme** | a + b = [a₁+b₁, a₂+b₂, ...] | Özellik vektörlerini birleştirme |
| **Skaler çarpma** | c·a = [c·a₁, c·a₂, ...] | Ölçeklendirme özellikleri |
| **Nokta çarpım** | a·b = Σ aᵢbᵢ | Benzerlik, öngörüler |
| **Norm (büyüklük)** | ||bir|| = √(Σ aᵢ²) | Vektör uzunluğu |
| **Çapraz çarpım** | a × b (yalnızca 3D) | Dik vektör, alan |
### Matrisler
**Matrisler** 2 boyutlu sayı dizileridir. Bir sinir ağının ağırlıkları matrisler halinde depolanır. 100 görüntüden oluşan bir grup, her biri 784 piksel değerine sahip 100 satırdan oluşan bir şekil matrisi (100, 784) olabilir.
**Anahtar işlemler:**
| Operasyon | Ne İşe Yarar | Nerede Görünüyor |
|---|---|---|
| Nokta ürün | İki vektör arasındaki benzerliği ölçer | Öneri sistemleri, kosinüs benzerliği |
| Matris çarpımı | Doğrusal dönüşümleri birleştirir | Bir sinir ağının her katmanı |
| Özdeğerler/özvektörler | Bir matrisin ölçeklendiği yönler (döndürülmez) | PCA boyutluluk azaltma, PageRank |
| Matris sıralaması | Bağımsız bilgi miktarı | Sıkıştırma, düşük dereceli yaklaşım |
| Transpoze | Satırları ve sütunları döndürür | Gradyan hesaplaması |
| Ters | A⁻¹ öyle ki A·A⁻¹ = I | Doğrusal sistemleri çözme |
**Kosinüs benzerliği** = (a·b) / (||a|| × ||b||) — −1 (ters) ile 1 (aynı yön) arasında değişir. Arama motorları, iki belgenin "aynı şeyle ilgili" olup olmadığını ve yerleştirme modellerinin anlamsal benzerliği nasıl karşılaştırdığını bu şekilde ölçer.
---

## Özet
| Şube | Temel Soru | Anahtar Uygulama |
|---|---|---|
| Aritmetik ve Sayılar Teorisi | Sayılar nasıl davranır? | Kriptografi, karma |
| Cebir | Bilinmeyenler nasıl ilişki kurar? | Modelleme, denklemler |
| Geometri | Şekiller ve uzaylar nasıl çalışır? | Grafik, robotik, mimari |
| Matematik | İşler nasıl değişir? | Sinir ağlarının eğitimi, fizik |
| Küme Teorisi | Koleksiyonlar arasında nasıl bir ilişki var? | Veritabanları, olasılık |
| Lineer Cebir | Dönüşümler nasıl çalışır? | Makine öğrenimi, grafikler, arama motorları |
Bu konuların hepsine hemen ihtiyaç duyulmaz. Ancak herhangi bir teknik alanda derinlere inildikçe bu temeller giderek daha alakalı hale gelir. Her dal, çözmek için tasarlandığı sorun anlaşılınca daha da netleşir.