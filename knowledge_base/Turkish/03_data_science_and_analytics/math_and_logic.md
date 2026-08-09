---
# Metadata
title: "Mathematics and Logic"
description: "Mathematics, logic, proofs"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [math, logic, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Matematik ve Mantık
Matematik sadece okulda okuduğunuz bir ders değildir; neredeyse her teknik alanın altında yatan işletim sistemidir. Fizik bunu evreni tanımlamak için kullanır. Bilgisayar bilimi bunu algoritma tasarlamak için kullanır. Makine öğrenimi bunu ağırlıkları optimize etmek için kullanır. Finans bunu fiyat riskine karşı kullanıyor. Her dalda uzmanlaşmanıza gerek yok, ancak manzarayı anlamak ve her dalın nerede göründüğünü bilmek, diğer her şeyin daha hızlı tıklamasını sağlar.
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
- **Alan**: tüm geçerli girişler (ör. sıfıra bölünemez, reel olarak negatifin √'sini alamaz)
- **Aralık**: tüm olası çıkışlar
- **Eğim** (m): değişim oranı — "her 1 birim x için y, m kadar değişir"
- **Kesme noktası**: fonksiyonun bir ekseni geçtiği yer
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

## İstatistik ve Olasılık
İstatistik, verileri nasıl anlamlandırdığınızdır. "Bunun işe yaradığını düşünüyorum" ile "Bunun işe yaradığına dair kanıtım var" arasındaki fark budur.
**Merkezi eğilim ölçüleri — "tipik" olan nedir:**
| Ölçü | Nasıl Hesaplanıyor | Ne Zaman Kullanılmalı |
|---|---|---|
| Ortalama (ortalama) | Toplam ÷ sayım | Varsayılan seçim; aykırı değerlere duyarlı |
| Medyan | Sıralandığında orta değer | Çarpık veriler (örn. ev fiyatları, maaşlar) |
| Modu | En sık görülen değer | Kategorik veriler (ör. en popüler renk) |
**Yayılma ölçüleri — verilerin ne kadar "çeşitli" olduğu:**
| Ölçü | Formül Fikri | Size Ne Anlatıyor |
|---|---|---|
| Menzil | maksimum – minimum | Toplam yayılma, ancak aykırı değerlere duyarlı |
| Varyans | Ortalamadan sapmanın karesi | Kare birimler halinde (doğrudan yorumlanması zor) |
| Standart sapma | √varyans | Verilerle aynı birimler — başvurulacak yayılma ölçüsü |
**Olasılıkla ilgili temel bilgiler:**
- 0'dan (imkansız) 1'e (kesin) kadar aralıklar
- Bağımsız olaylar: P(A ve B) = P(A) × P(B)
- Örnek: art arda iki 6'yı yuvarlamak = (1/6) × (1/6) = 1/36
**ML'de karşılaşacağınız olasılık dağılımları:**
| Dağıtım | Ne Modelleri | Örnek |
|---|---|---|
| Bernoulli | Tek deneme, iki sonuç | Bir yazı tura atma |
| Binom | n denemede başarı | 10 soruluk ÇSS'nin doğru yanıtları |
| Normal (Gauss) | Çan eğrisi, doğal olaylar | Yükseklikler, test puanları, ölçüm gürültüsü |
| Poisson | Sabit bir aralıktaki olaylar | Saat başına e-posta sayısı, toplu iş başına kusurlar |
**Bayes teoremi** — inançların kanıtlarla güncellenmesi:
P(A|B) = P(B|A) × P(A) / P(B)
Bu, spam filtrelerinin, tıbbi teşhislerin ve Bayesian ML modellerinin omurgasını oluşturur. Şöyle diyor: güncellenmiş inancınız = (kanıtların hipotezinize ne kadar iyi uyduğu × önceki inancınız) / kanıtın genel olarak ne kadar muhtemel olduğu.
---

## Matematik
Matematik *değişimi* ve *birikimi* inceler. Eğer cebir anlık görüntüleri ele alıyorsa, matematik de hareketli görüntüleri ele alır.
**Diferansiyel hesap** — değişim oranları. F'(x) türevi size f'nin herhangi bir noktada ne kadar hızlı değiştiğini söyler.
| Fonksiyon f(x) | Türev f'(x) | Sezgi |
|---|---|---|
| xⁿ | n·xⁿâ»¹ | Güç kuralı |
| e² | e² | Kendi türevine eşit olan tek fonksiyon |
| ln(x) | 1/x | x arttıkça büyüme hızı yavaşlar |
| günah(x) | çünkü(x) | Salınım değişim hızı |
ML'de türevler neden önemlidir: gradyan iniş - çoğu sinir ağını eğiten algoritma - kayıp fonksiyonunun türevlerini hesaplayarak ve hatayı azaltan yönde adım atarak çalışır.
**İntegral hesap** — birikim. İntegral bir eğrinin altındaki alanı temsil eder. Türevler "Ne kadar hızlı değişiyor?" sorusunu yanıtlıyorsa, integraller "Ne kadar birikti?" sorusunu yanıtlıyor.
**Hesaplamanın temel teoremi** her ikisini de birbirine bağlar: türev alma ve entegrasyon ters işlemlerdir.
---

## Mantık ve Muhakeme
Mantık, *geçerli* akıl yürütmenin incelenmesidir; bir sonucun *doğru gelip gelmediği* değil, öncüllerden *sonuçlanıp sonuçlanmadığı*.
**Tümdengelimli akıl yürütme** (öncüller doğruysa garantili sonuç):
- Bütün insanlar ölümlüdür. Sokrates insandır. → Sokrates ölümlüdür.
**Tümevarımsal akıl yürütme** (olası sonuç, garanti edilmez):
- Gördüğüm her kuğu beyazdır. → Bütün kuğular muhtemelen beyazdır. (Ama siyah kuğular var.)
**Yaygın mantıksal yanılgılar — muhakeme gibi görünen ama aslında öyle olmayan hatalar:**
| Yanılgı | Nedir | Örnek |
|---|---|---|
| Ad hominem | Tartışmaya değil kişiye saldırmak | "Onun politika fikrine güvenemezsin; o genç." |
| Saman adam | Bir argümanı yıkmak için yanlış sunmak | "Askeri harcamaları kısmak mı istiyor? Bizi savunmasız bırakmak mı istiyor!" |
| Yanlış ikilem | Daha fazlası mevcut olduğunda iki seçeneğin sunulması | "Ya bizimlesin ya da bize karşısın." |
| Dairesel akıl yürütme | Sonucun kendi öncülü olarak kullanılması | "Bu yasa adil değil çünkü adil değil." |
| Otoriteye itiraz | "Doğru çünkü bir uzman öyle söyledi" | "Bu hisse senedi yükselecek; ünlü bir yatırımcı öyle söyledi." |
| Sonradan | A'nın B'ye neden olduğunu, çünkü A'nın önce geldiğini varsayıyoruz | "Bu takviyeyi aldım, sonra soğuk algınlığım geçti. Takviye beni iyileştirdi." |
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
Bilgisayarlar ikili (taban 2) olarak düşünür: yalnızca 0'lar ve 1'ler. İnsanlar ondalık sayıyla (10 tabanında) düşünürler. Programcılar genellikle ikili sayıyı temsil etmenin kompakt bir yolu olarak onaltılık sayıyı (16 tabanı) kullanırlar.
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
**Vektörler** sıralı sayı listeleridir. ML'de her veri noktası, özelliklerin bir vektörüdür:
- [23, 1.8, 75] kişinin yaşını, metre cinsinden boyunu ve kg cinsinden ağırlığını temsil edebilir.
**Matrisler** 2 boyutlu sayı dizileridir. Bir sinir ağının ağırlıkları matrisler olarak depolanır. 100 görüntüden oluşan bir grup, her biri 784 piksel değerine sahip 100 satırdan oluşan bir şekil matrisi (100, 784) olabilir.
**Anahtar işlemler:**
| Operasyon | Ne İşe Yarar | Nerede Görünüyor |
|---|---|---|
| Nokta ürün | İki vektör arasındaki benzerliği ölçer | Öneri sistemleri, kosinüs benzerliği |
| Matris çarpımı | Doğrusal dönüşümleri birleştirir | Bir sinir ağının her katmanı |
| Özdeğerler/özvektörler | Bir matrisin ölçeklendiği yönler (döndürülmez) | PCA boyutluluk azaltma, PageRank |
| Matris sıralaması | Bağımsız bilgi miktarı | Sıkıştırma, düşük dereceli yaklaşım |
**Kosinüs benzerliği** = (a·b) / (||a|| × ||b||) — −1 (ters) ile 1 (aynı yön) arasında değişir. Arama motorları, iki belgenin "aynı şeyle ilgili" olup olmadığını ve yerleştirme modellerinin anlamsal benzerliği nasıl karşılaştırdığını bu şekilde ölçer.
---

## Özet
| Şube | Temel Soru | Anahtar Uygulama |
|---|---|---|
| Aritmetik ve Sayılar Teorisi | Sayılar nasıl davranır? | Kriptografi, karma |
| Cebir | Bilinmeyenler nasıl ilişki kurar? | Modelleme, denklemler |
| Geometri | Şekiller ve uzaylar nasıl çalışır? | Grafik, robotik, mimari |
| İstatistik ve Olasılık | Veriler ne diyor? | ML, A/B testi, risk analizi |
| Matematik | İşler nasıl değişir? | Sinir ağlarının eğitimi, fizik |
| Mantık | Bu mantık geçerli mi? | Programlama, ispatlar, argüman analizi |
| Küme Teorisi | Koleksiyonlar arasında nasıl bir ilişki var? | Veritabanları, olasılık |
| Lineer Cebir | Dönüşümler nasıl çalışır? | Makine öğrenimi, grafikler, arama motorları |
İlk gün bunların hepsine ihtiyacınız yok. Ancak herhangi bir teknik alanda derinlere indikçe bu temellere geri dönmeye devam edeceksiniz. İyi haber: Her dalın *neden* icat edildiğini, hangi sorunu çözmeye çalıştığını gördüğünüzde çok daha anlamlı hale gelir.