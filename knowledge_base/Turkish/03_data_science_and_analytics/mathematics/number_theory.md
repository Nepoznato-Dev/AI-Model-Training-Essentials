---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
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
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Sayı Teorisi
Sayı teorisi tamsayıların (tam sayılar ve bunların özelliklerinin) incelenmesidir. Gauss buna "matematiğin kraliçesi" adını verdi. En basit nesneleri (1, 2, 3, ...) incelemesine rağmen sayılar teorisi, matematikteki en derin ve en zor problemlerden bazılarını üretir. Günümüzde modern kriptografiyi, karma algoritmaları, hata düzeltme kodlarını ve rastgele sayı üretimini desteklemektedir.
---

## Bölünebilme ve Bölme Algoritması
### Temel Tanımlar
| Dönem | Tanımı | Örnek |
|------|------------|-----------|
| **Böler** | bir \| b, ∃k ∈ ℤ anlamına gelir: b = ak | 3 \| 12 (12 = 3 × 4 olduğundan) |
| **Bölen** | Bir sayıyı bölen sayı | 12'nin bölenleri: 1, 2, 3, 4, 6, 12 |
| **Birden fazla** | b, a'nın katı ise a \| b | 15, 5'in katıdır |
| **Bölüm** | Bölme sonucu | 17 ÷ 5 = bölüm 3 |
| **Kalan** | Bölme işleminden sonra geriye kalan | 17 ÷ 5 = kalan 2 |
### Bölme Algoritması
b > 0 olan herhangi bir a ve b tamsayıları için, benzersiz q (bölüm) ve r (kalan) tam sayıları vardır, öyle ki:
a = bq + r, burada 0 ≤ r < b
**Örnek:** 23 = 5 × 4 + 3. Bölüm q = 4, kalan r = 3.
### Bölünebilme Özellikleri
| Emlak | Açıklama |
|----------|-----------|
| Geçişlilik | Eğer bir \| b ve b \| c, ardından a \| c |
| Doğrusallık | Eğer bir \| b ve a \| c, ardından a \| (bx + cy) tüm x, y tam sayıları için |
| Karşılaştırma | Eğer bir \| b ve b > 0 ise a ≤ b |
| Önemsiz | bir \| tümü için 0; 1 \| her şey için a; bir \| hepsi için a a ≠ 0 |
---

## En Büyük Ortak Bölen (GCD)
a ve b'nin **en büyük ortak böleni**, gcd(a, b) ile gösterilir, hem a hem de b'yi bölen en büyük pozitif tamsayıdır.
### Öklid Algoritması
GCD'yi hesaplamak için en etkili klasik algoritma.
**Önemli bilgi:** gcd(a, b) = gcd(b, a mod b)
**Algoritma:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Çalışılan Örnek:** gcd(252, 105)
- 252 = 105 × 2 + 42 → eb(105, 42)
- 105 = 42 × 2 + 21 → ebc(42, 21)
- 42 = 21 × 2 + 0 → ebd(21, 0)
- Sonuç: gcd(252, 105) = 21
| Emlak | Değer |
|----------|----------|
| Zaman karmaşıklığı | O(log(min(a, b))) |
| Uzay karmaşıklığı | O(1) yinelemeli |
### Bézout'un Kimliği
Herhangi bir a, b tam sayısı için x, y tam sayıları vardır, öyle ki:
ax + by = gcd(a, b)
**Genişletilmiş Öklid Algoritması** gcd(a, b)'yi ve x, y katsayılarını aynı anda hesaplar.
**Çalışılan Örnek:** 252x + 105y = 21 olacak şekilde x, y'yi bulun.
- Öklid algoritmasından geri ikame:
  - 21 = 105 - 42 × 2
  - 42 = 252 - 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 – 252 × 2
- Yani x = −2, y = 5. Kontrol edin: 252(−2) + 105(5) = −504 + 525 = 21.
### GCD'nin Temel Özellikleri
| Emlak | Açıklama |
|----------|-----------|
| gcd(a, 0) | = bir |
| gcd(a, 1) | = 1 (a ve 1 her zaman aralarında asaldır) |
| gcd(a, b) = gcd(b, a) | Değişmeli |
| gcd(a, b) = gcd(a, b + ka) | Katları eklemek GCD'yi değiştirmez |
| gcd(ca, cb) | = c · gcd(a, b) |
| Prime | gcd(a, b) = 1, a ve b'nin hiçbir ortak çarpanı paylaşmadığı anlamına gelir |
---

## Asal Sayılar
**asal**, tek pozitif bölenleri 1 ve kendisi olan, 1'den büyük bir tamsayıdır.
### Temel Özellikler
| Emlak | Açıklama |
|----------|-----------|
| **Aritmetiğin Temel Teoremi** | Her n > 1 tamsayının benzersiz bir asal çarpanlara ayırması vardır |
| **Asal sayıların sonsuzluğu** | Sonsuz sayıda asal sayı vardır (Öklid, ~MÖ 300) |
| **Asal Sayı Teoremi** | ≤ n asal sayısı yaklaşık olarak n / ln(n) |
| **Bertrand'ın Postülası** | Her n > 1 için, n < p < 2n | olan bir asal p vardır.
### İlk Asal Sayılar
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Asal çarpanlara ayırma
Her n > 1 tamsayı benzersiz olarak şu şekilde yazılabilir:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
p₁ < p₂ < ... < pₖ asal sayılardır ve aᵢ ≥ 1'dir.
**Örnekler:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**GCD ve LCM'yi hesaplamak için çarpanlara ayırmanın kullanılması:**
- gcd(a, b) = paylaşılan asal sayıların minimum kuvvetlerinin çarpımı
- lcm(a, b) = tüm asal sayıların maksimum kuvvetlerinin çarpımı
**Örnek:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- ebd(12, 18) = 2¹ × 3¹ = 6
- 1cm(12, 18) = 2² × 3² = 36
### Eratostenes Eleği
N sınırına kadar tüm asal sayıları bulmaya yönelik klasik algoritma.
| Emlak | Değer |
|----------|----------|
| Zaman karmaşıklığı | O(N günlük günlük N) |
| Uzay karmaşıklığı | O(N) |
**Algoritma:**
1. 2'den N'ye kadar tüm tam sayıları listeleyin.
2. p = 2 ile başlayın. p'nin tüm katlarının üzerini çizin (p²'den başlayarak).
3. Sonraki çaprazlanmamış sayıyı bulun > s. P'yi bu sayıya ayarlayın.
4. p² > N olana kadar tekrarlayın. Tüm çaprazlanmamış sayılar asaldır.
### Asallık Testi
| Yöntem | Tür | Zaman | Kullanım Örneği |
|----------|------|------|----------|
| Deneme bölümü | Deterministik | Ö(√n) | Küçük sayılar |
| Fermat testi | Olasılıksal | O(k log² n) | Hızlı tarama |
| Miller-Rabin | Olasılıksal | O(k log² n) | Genel amaçlı |
| AKS | Deterministik | O(log⁶ n) | Teorik önemi |
**Fermat asallık testi:** Eğer p asalsa ve gcd(a, p) = 1 ise aᵖ⁻¹ ≡ 1 (mod p). Eğer bu bazı a'lar için başarısız olursa, o zaman p kesinlikle bileşiktir. Birçok rastgele a değeri için geçerliyse, p muhtemelen asaldır.
**Uyarı:** Carmichael sayıları (ör. 561) tüm eş asal bazlar için Fermat testini geçer ancak bileşiktir. Miller-Rabin bu sorundan kaçınıyor.
---

## Modüler Aritmetik
Modüler aritmetik, tamsayıları "sarmalama" altında inceler - saat yüzündeki aritmetik.
### Uyumluluk İlişkileri
a ≡ b (mod n) n anlamına gelir | (a − b), yani a ve b, n'ye bölündüğünde aynı kalanı bırakır.
### Aritmetik Özellikler
| Operasyon | Kural |
|-----------|------|
| İlave | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Çarpma | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Üs | aᵇ mod n tekrarlanan kare alma işlemiyle verimli bir şekilde hesaplanabilir |
| Olumsuzluk | (−a) mod n = n − (a mod n) |
### Modüler Üs Alma
**tekrarlanan kare alma** yöntemini kullanarak verimli bir şekilde hesaplama yapmak:
**Çalışılan Örnek:** 3¹³ mod 7
- İkili sistemde 13: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Emlak | Değer |
|----------|----------|
| Zaman karmaşıklığı | O(log b · log² n) |
| Uzay karmaşıklığı | Ç(1) |
### Euler'in Totient Fonksiyonu
φ(n), 1'den n'ye kadar n'ye eş asal olan tam sayıları sayar.
| n | φ(n) | Eş asal tamsayılar |
|---|------|-------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 asaldır) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Formüller:**
- Eğer p asal ise: φ(p) = p − 1
- Eğer p asal ise: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Eğer gcd(m, n) = 1 ise: φ(mn) = φ(m) · φ(n) (çarpımsallık)
- Genel: φ(n) = n · Π_{p|n} (1 − 1/p) burada çarpım n'nin farklı asal faktörleri üzerindedir
---

## Temel Teoremler
### Fermat'ın Küçük Teoremi
Eğer p asalsa ve gcd(a, p) = 1 ise, o zaman:
aᵖ⁻¹ ≡ 1 (mod p)
**Sonuç (tüm a için):** aᵖ ≡ a (mod p)
**Kullanım:** Modül asal olduğunda hızlı modüler ters: a⁻¹ ≡ aᵖ⁻² (mod p)
**Çalışılan Örnek:** 3⁻¹ mod 7'yi bulun.
- Fermat'a göre: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Kontrol edin: 3 × 5 = 15 ≡ 1 (mod 7).
### Euler Teoremi (Fermat'ın Genelleştirilmesi)
Eğer gcd(a, n) = 1 ise:
a^φ(n) ≡ 1 (mod n)
Bu, Fermat'ın Küçük Teoremini asal sayılardan herhangi bir modüle kadar genelleştirir.
### Çin Kalan Teoremi (CRT)
Eğer m₁, m₂, ..., mₖ ikili asal ise sistem:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
benzersiz bir çözüm moduloya sahiptir: M = m₁ · m₂ · ... · mₖ.
**Çalışılan Örnek:** x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)'yi çözün.
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Terslerini bulun: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Kontrol edin: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Wilson Teoremi
(p - 1)! ≡ −1 (mod p) ancak ve ancak p asal ise.
Çoğunlukla teorik ilgi çekicidir - faktöriyellerin hesaplanması pahalı olduğundan asallık testi için pratik değildir.
### İkinci Dereceden Kalıntılar
Eğer x² ≡ a (mod n)'nin bir çözümü varsa, a tamsayısı **ikinci dereceden kalıntı mod n**'dir.
**Euler kriteri:** a ikinci dereceden bir kalıntıdır mod üssü p iff a^((p−1)/2) ≡ 1 (mod p).
**Efsane sembolü:** (a/p) = a^((p−1)/2) mod p, +1, −1 veya 0'ı verir.
**İkinci Dereceden Karşılıklılık** (Gauss): Farklı tek asal sayılar p, q için:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Bu derin teorem, farklı asal sayılardaki ikinci dereceden kalıntıları birbirine bağlar ve p = 2 durumlarını ele alan sekiz ek yasaya sahiptir.
---

## Kriptografiye Uygulamalar
### RSA Şifreleme Sistemi
Büyük tam sayıları çarpanlara ayırmanın zorluğuna dayanan, en yaygın şekilde kullanılan açık anahtarlı şifreleme sistemi.
**Kurulum:**
1. İki büyük asal sayı p, q seçin (genellikle her biri 1024+ bit)
2. n = pq ve φ(n) = (p−1)(q−1)'i hesaplayın
3. e'yi 1 < e < φ(n) ve gcd(e, φ(n)) = 1 olacak şekilde seçin (ortak: e = 65537)
4. Genişletilmiş Öklid Algoritmasını kullanarak d ≡ e⁻¹ (mod φ(n))'yi hesaplayın
5. **Genel anahtar:** (n, e). **Özel anahtar:** (n, d)
**Şifreleme:** c = mᵉ mod n (burada m, düz metin mesajıdır)
**Şifre çözme:** m = cᵈ mod n
**Neden işe yarıyor:** Euler teoremine göre cᵈ = m^(ed) ≡ m (mod n), çünkü ed ≡ 1 (mod φ(n)).
**Güvenlik:** Büyük n (2048+ bit) için n'yi p ve q'ya ayırmak hesaplama açısından mümkün değildir. P ve q olmadan saldırgan φ(n)'yi hesaplayamaz ve dolayısıyla d'yi bulamaz.
### Diffie-Hellman Anahtar Değişimi
İki tarafın güvenli olmayan bir kanal üzerinden paylaşılan bir sır oluşturmasına olanak tanır.
**Kurulum:** Büyük bir asal p ve bir jeneratör g (mod p) üzerinde anlaşın.
**Protokol:**
1. Alice gizli a'yı seçer ve Bob'a A = gᵃ mod p'yi gönderir
2. Bob gizli b'yi seçer ve Alice'e B = mod p'yi gönderir
3. Alice s = B mod p = g mod p'yi hesaplar
4. Bob s = Aᵇ mod p = gᵃᵇ mod p'yi hesaplar
5. Her ikisi de sırrı paylaşıyor s = gᵃᵇ mod p
**Güvenlik:** **ayrık logaritma probleminin** zorluğuna dayanmaktadır — gᵃ mod p'den a'yı bulma.
### Hash Fonksiyonları ve Sayı Teorisi
İyi karma işlevleri, anahtarları eşit şekilde dağıtmak için modüler aritmetik kullanır:
- **Çarpımsal karma:** h(k) = (k · A) mod m, burada A ≈ m · (√5 − 1) / 2 (altın oran)
- **Evrensel karma:** h(k) = ((ak + b) mod p) mod m, burada p asaldır, a, b rastgeledir
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Sayı Teorisi Kavramı | Başvuru |
|---------------------|----------------|
| Modüler aritmetik | Karma (karma tabloları, karma haritaları), rastgele sayı üretimi |
| Asal sayılar | Karma tablo boyutlandırması (çarpışmaları azaltmak için asal tablo boyutlarını kullanın) |
| GCD / Öklid algoritması | Rasyonel aritmetik, olasılıkta kesirleri basitleştirme |
| Modüler üs alma | HTTPS üzerinden hizmet veren makine öğrenimi modeli için şifreleme güvenliği |
| Euler'in sabırlısı | RSA anahtar üretimi, kriptografik garantileri anlama |
| Çin Kalan Teoremi | Dağıtılmış hesaplama, paralel modüler aritmetik |
| Asallık testi | Kriptografik işlemler için asal sayılar oluşturma |
| İkinci dereceden kalıntılar | Gelişmiş kriptografide ikinci dereceden artıklık sorunu |
| Sonlu alanlar (GF(p), GF(2ᵏ)) | Hata düzeltme kodları, Reed-Solomon kodları, AES şifreleme |
---

## Özet
| Konu | Temel Fikir | Temel Sonuç |
|----------|---------------|-----------|
| Bölünebilirlik | Kalanlı Bölme | Bölme algoritması: a = bq + r |
| GCD | En büyük paylaşılan faktör | Öklid algoritması: O(log n) |
| Asal Sayılar | Tam sayıların atomları | Aritmetiğin Temel Teoremi (benzersiz çarpanlara ayırma) |
| Modüler Aritmetik | Çevreleyen aritmetik | Eşlik sınıfları, modüler üs alma |
| Euler'in Totient'i | Eş asal tam sayıları sayma | φ(n) = n · Π(1 − 1/p) |
| Fermat'ın Küçük Teoremi | Asal modül kısayolu | aᵖ⁻¹ ≡ 1 (mod p) |
| Euler Teoremi | Genelleştirilmiş Fermat | a^φ(n) ≡ 1 (mod n) |
| Çin Kalan Teoremi | Modüler sistemlerin birleştirilmesi | Coprime modüllerinin benzersiz çözüm mod ürünü |
| Kriptografi | Zor sayı-teorik problemler | RSA (faktoring), Diffie-Hellman (ayrık günlük) |
Sayı teorisi, tam sayılarla ilgili basit soruları derin pratik uygulamalarla derin matematiğe dönüştürür. Her güvenli web bağlantısı, şifrelenmiş mesaj ve dijital imza, bilgisayarların var olmasından yüzyıllar önce keşfedilen sayı-teorik sonuçlara dayanır. Veri bilimcileri ve makine öğrenimi mühendisleri için sayı teorisini anlamak, karma oluşturma, rastgele sayı oluşturma ve aktarım halindeki ve hareketsiz verileri koruyan şifreleme altyapısı hakkında bilgi sağlar.