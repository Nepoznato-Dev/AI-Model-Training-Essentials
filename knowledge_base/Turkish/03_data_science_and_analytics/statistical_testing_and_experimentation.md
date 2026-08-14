<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
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

-->
# İstatistiksel Test ve Deney
İstatistik bilimin grameridir. Gerçek kalıpları rastgele gürültüden ayırt etmek, bir değişikliğin gerçekten işleri iyileştirip iyileştirmediğini ölçmek ve belirsizlik altında kararlar almak için size araçlar sağlar. Bu dosya hipotez testi, deneysel tasarım ve insanları tuzağa düşüren yaygın tuzaklara ilişkin temel kavramları kapsar.
---

## Hipotez Test Çerçevesi
Her istatistiksel test aynı mantığı izler:
1. **Sıfır hipotezini belirtin (H₀)**: Etki yok / fark yok.
2. **Alternatif hipotezi belirtiniz (H₁)**: Bir etki/fark vardır.
3. **Bir anlamlılık düzeyi seçin (α)**: Genellikle 0,05 (%5 yanlış pozitif şansı).
4. **Verileri toplayın ve bir test istatistiği hesaplayın**.
5. **p değerini hesaplayın**: H₀ doğruysa bu sonucun (veya daha uç noktanın) gözlemlenme olasılığı.
6. **Bir karar verin**: Eğer p < α ise H₀'yi reddedin (istatistiksel olarak anlamlı). Aksi halde H₀'yi reddetmeyin.
### Temel Kavramlar
| Konsept | Anlamı | Yaygın Yanılgı |
|-----------|-----------|----------|
| **p-değeri** | P(veri \| H₀ doğrudur) | "H₀'nin doğru olma olasılığı" DEĞİL |
| **α (anlam düzeyi)** | H₀'yi reddetme eşiği | Etki önemi ölçüsü değil |
| **İstatistiksel anlamlılık** | Yalnızca şansa bağlı olarak sonuç pek olası değil | Pratik olarak anlamlı olduğu anlamına DEĞİLDİR |
| **Etki boyutu** | Gözlemlenen etkinin büyüklüğü | p değerinden ayrı; küçük bir etki büyük N | ile önemli olabilir
| **Güç** | Yanlış bir H₀'yi doğru şekilde reddetme olasılığı | Genellikle %80+ hedefleyin |
| **Güven aralığı** | Parametre için makul değer aralığı | %95 GA "gerçek değerin %95 olasılıkla bu aralıkta olduğu" anlamına gelmez |
---

## Hata Türleri
| | H₀ Doğrudur | H₀ Yanlıştır |
|---|-----------|------------|
| **H₀'yi Reddet** | Tip I Hata (yanlış pozitif) | ✅ Doğru (gerçek pozitif) |
| **H₀ reddedilemedi** | ✅ Doğru (gerçek negatif) | Tip II Hata (yanlış negatif) |
| Hata | Sembol | Anlamı |
|----------|-----------|-----------|
| **Tip I** | α | Olmadığında bir etki olduğu sonucuna varıyoruz |
| **Tip II** | β | Gerçek bir efekt eksik |
---

## Doğru Testi Seçmek
| Senaryo | Testi | Varsayımlar |
|----------|------|------------|
| 2 grubun ortalamalarını karşılaştırın | **t-testi** (bağımsız) | Normal dağılım, eşit varyans |
| Eşleştirilmiş gözlemlerin araçlarını karşılaştırın | **Eşleştirilmiş t testi** | Farklılıklar normal olarak dağıtılır |
| 3+ grubun ortalamalarını karşılaştırın | **ANOVA** | Normal dağılım, eşit varyans |
| Kategorik dağılımları karşılaştırın | **Ki-kare testi** | Hücre başına yeterli örnek boyutu |
| Dağılımları karşılaştırın (parametrik olmayan) | **Mann-Whitney U** | Normallik varsayımı yok |
| 3'ten fazla grubu karşılaştırın (parametrik olmayan) | **Kruskal-Wallis** | Normallik varsayımı yok |
| Test korelasyonu | **Pearson** (doğrusal) veya **Spearman** (monoton) | Pearson: normallik; Spearman: sıralamaya dayalı |
| Verilerin bir dağılımı takip edip etmediğini test edin | **Kolmogorov-Smirnov** | Sürekli veri |
### Parametrik ve Parametrik Olmayan
| | Parametrik | Parametrik Olmayan |
|---|-----------|---------------|
| **Varsayımlar** | Veriler belirli bir dağılıma sahiptir (genellikle normaldir) | Dağıtım varsayımı yok |
| **Güç** | Varsayımlar karşılandığında daha yüksek | Daha alçak ama daha sağlam |
| **Ne zaman kullanılmalı** | Büyük örnekler, yaklaşık olarak normal veriler | Küçük örnekler, çarpık veriler, sıralı veriler |
---

## Ayrıntılı Olarak Spesifik Testler
### t-Testi
İki grubun ortalamalarını karşılaştırır.
| Varyant | Kullanım Örneği |
|-----------|----------|
| **Bağımsız t testi** | İki ayrı grup (tedavi ve kontrol) |
| **Eşleştirilmiş t testi** | Aynı grup iki kez ölçüldü (öncesi ve sonrası) |
| **Tek örnekli t testi** | Örnek ortalamayı bilinen bir değerle karşılaştırın |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Varyans Analizi)
Ortalamaları 3 veya daha fazla grup arasında karşılaştırır. En az bir grup ortalamasının diğerlerinden farklı olup olmadığını test eder.
| Tür | Tasarım |
|------|--------|
| **Tek yönlü ANOVA** | 3+ seviyeli bir bağımsız değişken |
| **İki yönlü ANOVA** | İki bağımsız değişken; etkileşim etkilerini test ediyor |
| **Tekrarlanan Ölçümler ANOVA** | Aynı denekler farklı koşullar altında ölçüldü |
ANOVA anlamlıysa hangi grupların farklılık gösterdiğini bulmak için **post-hoc testler** (Tukey's HSD) ile takip edin.
### Ki-Kare Testi
İki kategorik değişkenin bağımsız olup olmadığını test eder.
| Kullanım Örneği | Örnek |
|----------|-----------|
| **Bağımsızlık testi** | Cinsiyet ürün tercihiyle ilişkili midir? |
| **Uyumun iyiliği** | Bir kalıp rulosu düzgün bir dağılım izliyor mu? |
**Temel kural**: Her hücrenin beklenen sayısı en az 5 olmalıdır.
---

## A/B Testi
A/B testi, hipotez testinin iş kararlarına uygulanmasıdır; genellikle bir kontrolü (A) bir değişken (B) ile karşılaştırır.
### Tasarım Süreci
| Adım | Açıklama |
|------|-----------------|
| **1. Hipotezi tanımlayın** | "Düğme rengini maviden yeşile değiştirmek tıklama oranını artıracaktır" |
| **2. Metrik seçin** | Birincil: tıklama oranı. İkincil: dönüşüm oranı, gelir. |
| **3. Örnek boyutunu hesaplayın** | Minimum tespit edilebilir etki, güç (%80) ve anlamlılığa (%5) dayanmaktadır |
| **4. Rastgeleleştir** | Kullanıcıları kontrol ve tedaviye rastgele atayın |
| **5. Denemeyi çalıştırın** | Hedef örneklem büyüklüğüne ulaşılana kadar veri toplayın |
| **6. Analiz** | Uygun istatistiksel testi kullanarak ölçümleri karşılaştırın |
| **7. Karar verin** | İstatistiksel ve pratik olarak anlamlı ise uygulayın |
### Örnek Boyutu Hesaplaması
İhtiyacınız olan numune boyutu şunlara bağlıdır:
| Faktör | Örneklem Büyüklüğüne Etkisi |
|----------|-----------|
| **Algılanması daha küçük etki** | Daha fazla örneğe ihtiyacınız var |
| **Daha yüksek güç** | Daha fazla örneğe ihtiyacınız var |
| **Düşük anlamlılık düzeyi** | Daha fazla örneğe ihtiyacınız var |
| **Daha yüksek fark** | Daha fazla örneğe ihtiyacınız var |
### Yaygın A/B Testi Hataları
| Hata | Neden Yanlış |
|-----------|---------------|
| **Erkenden göz atıyoruz** | Sonuçların günlük olarak kontrol edilmesi yanlış pozitiflik oranını artırıyor |
| **Düzeltilmeden birden fazla metrik** | 20 metrik α=0,05'te test ediliyor → şans eseri 1 yanlış pozitif bekleniyor |
| **Hedef N'den önce durmak** | Yetersiz güç testi gerçek efektleri tespit edemiyor |
| **Mevsimsellik göz ardı ediliyor** | Tatil döneminde normal haftaya göre test çalıştırma |
| **Rastgele olmayan atama** | Seçim yanlılığı (örn. tedaviye yeni kullanıcılar atama) |
| **Önemliliği önemlilikle karıştırmak** | %0,1'lik bir artış istatistiksel olarak anlamlı olabilir ancak dikkate alınmaya değmez |
---

## Çoklu Karşılaştırmalar
Aynı anda birçok testi çalıştırdığınızda en az bir hatalı pozitiflik olasılığı önemli ölçüde artar.
| Test Sayısı | ≥1 Yanlış Pozitif Olasılığı (α=0,05'te) |
|----------------|------------------------------------------------|
| 1 | %5 |
| 5 | %23 |
| 10 | %40 |
| 20 | %64 |
### Düzeltmeler
| Yöntem | Nasıl Çalışır | Ne Zaman Kullanılmalı |
|----------|----------------|-------------|
| **Bonferroni** | α'yı test sayısına bölün (α/n) | Tutucu; birkaç karşılaştırma |
| **Holm-Bonferroni** | Adım aşağı prosedür; daha az muhafazakar | Genel kullanım |
| **Benjamini-Hochberg (FDR)** | Yanlış keşif oranını kontrol eder | Birçok test; keşif analizi |
---

## Efekt Boyutu
P değerleri size bir etkinin * olup olmadığını* söyler. Etki boyutu size *ne kadar büyük* olduğunu söyler.
| Ölçü | | Yorumlama |
|-----------|-----|---------------|
| **Cohen'in d** | İki araç arasındaki fark | 0,2 = küçük, 0,5 = orta, 0,8 = büyük |
| **Pearson'un r** | Korelasyon | 0,1 = küçük, 0,3 = orta, 0,5 = büyük |
| **η² (eta-kare)** | ANOVA | 0,01 = küçük, 0,06 = orta, 0,14 = büyük |
| **Oran Oranı** | Kategorik sonuçlar | 1,0 = etki yok; >1 veya <1 = etki |
**Etki büyüklüğünü her zaman p değerlerinin yanında rapor edin.** Bir sonuç istatistiksel olarak anlamlı ancak pratikte anlamsız olabilir.
---

## Bayesian vs Frequentist
| Görünüş | Frequentist | Bayesian |
|----------|---------------|----------|
| **Olasılık** | Uzun vadeli olayların sıklığı | İnanç derecesi |
| **Parametreler** | Düzeltildi ancak bilinmiyor | Dağılımlı rastgele değişkenler |
| **Kullanımlar** | p değerleri, güven aralıkları, hipotez testleri | Arka dağılımlar, güvenilir aralıklar |
| **Önceki** | Hiçbir önceden inanç dahil edilmemiştir | Açık ön dağıtım |
| **Yorumlama** | "Bu deneyi birçok kez tekrarlasaydık..." | "Veriler göz önüne alındığında, olasılık..." |
| **Güçlü yönler** | Nesnel, köklü, basit | Sezgisel yorumlama, ön bilgileri birleştirir |
| **Zayıf yönler** | p değerleri yaygın olarak yanlış anlaşılıyor | Öncekinin seçimi öznel olabilir |
---

## Nedensel Çıkarımın Temelleri
Korelasyon nedensellik değildir. Ancak bazen yalnızca ilişkili olup olmadıklarını değil, *X'in Y'ye neden olup olmadığını* bilmeniz gerekir.
| Yöntem | Açıklama | Ne Zaman Kullanılmalı |
|----------|----------------|-------------|
| **Rastgele deneyler** | Altın standardı; rastgele atama, kafa karıştırıcı durumları ortadan kaldırır | Ne zaman rastgele seçim yapabilirsiniz |
| **Farklılıklar Arasındaki Fark (DiD)** | Tedavi ve kontrol arasında zaman içindeki değişiklikleri karşılaştırın | Politika değişiklikleri, doğal deneyler |
| **Regresyon Süreksizliği (RDD)** | Bir kesme eşiğinden yararlanın | Burslar, uygunluk eşikleri |
| **Araçsal Değişkenler (IV)** | Tedaviyi etkileyen ancak sonucu doğrudan etkilemeyen bir araç kullanın | Rastgeleleştirme mümkün olmadığında |
| **Eğilim Puanı Eşleştirme** | İşlenen ve kontrol ünitelerini gözlemlenen özelliklere göre eşleştirin | Gözlemsel çalışmalar |
---

## Yaygın İstatistiksel Hatalar
| Hata | Açıklama |
|-----------|------------|
| **p-hackleme** | P < 0.05'i bulana kadar birçok analiz yapmaya çalışıyoruz |
| **HARKing** | Sonuçlar Bilindikten Sonra Varsayımda Bulunmak |
| **Hayatta kalma önyargısı** | Yalnızca başarılara bakmak (örneğin başarılı şirketler) |
| **Simpson paradoksu** | Veriler toplandığında ve gruba göre ayrıldığında trend tersine dönüyor |
| **Taban oran ihmali** | Sonuçları yorumlarken önceki olasılığı göz ardı etmek |
| **Ekolojik yanılgı** | Grup düzeyindeki verilerden bireysel davranışların çıkarılması |
| **Kafa karıştırıcı** | Üçüncü bir değişken gözlemlenen ilişkiyi açıklıyor |
| **Fazla uyum** | Model sinyali değil gürültüyü yakalıyor |
---

## Özet
İstatistiksel test, belirsizlik altında entelektüel dürüstlükle karar vermekle ilgilidir. Veri toplamadan önce daima hipotezlerinizi belirtin. Veri türünüz için doğru testi seçin. Yalnızca p değerlerini değil, etki boyutlarını da raporlayın. Çoklu karşılaştırmalar için doğru. Ve unutmayın: istatistiksel önem, pratik önem ile aynı şey değildir.