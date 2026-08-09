---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
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
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Nedensel Çıkarım
Nedensel çıkarım, yalnızca ilişkili olup olmadıklarını değil, bir şeyin aslında bir başka şeye neden olup olmadığını belirleme bilimidir. Korelasyon size iki değişkenin birlikte hareket ettiğini söyler. Nedensellik, birini değiştirmenin diğerini de değiştireceğini söyler. Bu ayrım tıpta (bu ilaç işe yarıyor mu?), politikada (bu müdahale yoksulluğu azaltıyor mu?), iş dünyasında (bu reklam kampanyası satışları artırıyor mu?) ve bilimde (bu mekanizma fenomeni açıklıyor mu?) son derece önemlidir.
---

## Korelasyon ve Nedensellik
| Konsept | Açıklama | Örnek |
|-----------|------------|------------|
| **Korelasyon** | İki değişken birlikte hareket ediyor | Yaz aylarında dondurma satışları ve boğulma ölümleri artıyor |
| **Nedensellik** | Bir değişken diğerini doğrudan etkiler | Sigara içmek akciğer kanserine neden olur |
| **Kafa karıştırıcı** | Üçüncü bir değişken her ikisine de neden olur | Sıcak hava hem dondurma satışlarına hem de yüzmeye (ve boğulmaya) neden oluyor |
| **Ters nedensellik** | Etki aslında varsayılan nedene neden oluyor | İnsanlar sağlık takviyelerini hasta oldukları için alıyorlar, tam tersi değil |
| **Sahte korelasyon** | Tesadüfi ilişki | Kişi başına düşen peynir tüketimi, çarşaf dolanmasından kaynaklanan ölümlerle bağlantılıdır |
---

## Potansiyel Sonuçlar Çerçevesi
### Rubin Nedensel Model
| Konsept | Açıklama |
|-----------|------------|
| **Potansiyel sonuçlar** | Her birim için, eğer işlem yapılırsa Y(1) ve işlem yapılmaz ise Y(0) bir sonuç vardır |
| **Tedavi etkisi** | Fark: Belirli bir birim için Y(1) - Y(0) |
| **Temel sorun** | Aynı birim için hem Y(1) hem de Y(0)'ı hiçbir zaman gözlemleyemeyiz; yalnızca birini görebiliriz |
| **Ortalama Tedavi Etkisi (ATE)** | Nüfus genelinde bireysel tedavi etkilerinin ortalaması |
| **Karşıolgusal** | Gözlemlenmeyen sonuç – diğer koşullar altında ne olurdu |
### Temel Varsayımlar
| Varsayım | Anlamı | Nasıl Tatmin Edilir |
|-----------|-----------|----------------|
| **İhmal edilebilirlik (şaşkınlık)** | Tedavi ataması, gözlemlenen ortak değişkenler dikkate alındığında potansiyel sonuçlardan bağımsızdır | Rastgeleleştirme; tüm karıştırıcıları ölçün |
| **Olumluluk (örtüşme)** | Her birimin her iki tedaviyi de alma olasılığı sıfırdan farklıdır | Gruplar arasındaki ortak değişken örtüşmesini kontrol edin |
| **SUTVA** (Kararlı Birim Arıtma Değeri Varsayımı) | Bir birimin tedavisi diğerinin sonucunu etkilemez; tedavi tutarlıdır | Parazit yok; tedavinin gizli versiyonları yok |
| **Tutarlılık** | Gözlemlenen sonuç, alınan tedavi kapsamındaki potansiyel sonuca eşittir | İyi tanımlanmış tedavi |
---

## Nedensel Çıkarım Yöntemleri
### Deneysel Yöntemler
| Yöntem | Açıklama | Güç | Sınırlama |
|----------|----------------|----------|------------|
| **Randomize kontrollü çalışma (RKÇ)** | Tedavi veya kontrole birimleri rastgele atayın | Altın standardı; karışıklığı ortadan kaldırır | Masraflı; bazen etik değildir; genelleme yapılamaz |
| **A/B testi** | İşletme/teknoloji bağlamında RCT | Basit; titiz | Kısa vadeli ölçümler; yenilik efektleri; girişim |
| **Geri dönüş deneyleri** | Zaman aralıklarında alternatif tedavi | Pazar yerlerindeki müdahaleleri yönetir | Kararlı bir ortam gerektirir |
### Yarı Deneysel Yöntemler
| Yöntem | Açıklama | Temel Varsayım |
|----------|----------------|----------------|
| **Farklılıklar arasındaki fark (DiD)** | Tedavi edilen ve kontrol grupları arasındaki sonuçların zaman içindeki değişimini karşılaştırın | Paralel eğilimler: gruplar tedavi olmaksızın aynı yolu izleyeceklerdi |
| **Regresyon süreksizliği (RD)** | Tedavi sınırının hemen üstündeki ve hemen altındaki birimleri karşılaştırın | Sınır noktasına yakın birimler karşılaştırılabilir (sanki rastgele) |
| **araçsal değişkenler (IV)** | Tedaviyi etkileyen ancak tedavi yoluyla sonuçlanmayan bir değişken kullanın | Enstrüman tedaviyle ilişkilidir; sonucu yalnızca tedavi yoluyla etkiler |
| **Sentetik kontrol** | İşlenen üniteye uyacak şekilde ağırlıklı bir kontrol ünitesi kombinasyonu oluşturun | Sentetik kontrol, işlenen birimin karşı olgusallığını doğru bir şekilde temsil eder |
| **Eğilim puanı eşleştirme** | İşleme tabi tutulan birimleri ve benzer işlem olasılıklarına sahip kontrol birimlerini eşleştirin | Tüm karıştırıcılar ölçülür ve eğilim modeline dahil edilir |
### Farklılıklardaki Fark (Görselleştirilmiş)
| Dönem | İşlem Görmüş Grup | Kontrol Grubu | Fark |
|----------|-----------------|---------------|------------|
| **Ön işlem** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Tedavi sonrası** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **DiD tahmini** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Yönlendirilmiş Döngüsel Olmayan Grafikler (DAG'ler)
DAG'ler nedensel varsayımları kodlamak ve kafa karıştırıcı unsurları belirlemek için kullanılan görsel araçlardır.
### Temel Yapılar
| Yapı | Desen | Çıkarım |
|-----------|------------|-------------|
| **Zincir** | A → B → C | A ve C, B aracılığıyla ilişkilendirilir; B'nin kontrol edilmesi yolu engeller |
| **Çatal** | A ← B → C | A ve C, B ile karıştırılıyor; B'nin kontrol edilmesi yolu engeller |
| **Çarpıştırıcı** | A → B ← C | A ve C bağımsızdır; B'nin kontrol edilmesi yolu açar (sahte ilişkilendirme yaratır) |
### DAG Kuralları
| Kural | Açıklama |
|------|-----------------|
| **Arka kapı kriteri** | X'in Y üzerindeki nedensel etkisini tahmin etmek için, uygun değişkenleri koşullandırarak tüm arka kapı yollarını (X'e giden oklu yollar) engelleyin |
| **Ön kapı kriteri** | Arka kapı yolları engellenemiyorsa aracıları kullanın: X → M → Y'yi iki aşamada tahmin edin |
| **Çarpıştırıcılara koşul vermeyin** | Ortak bir etkiyi kontrol etmek sahte bir yol açar |
| **Çarpıştırıcıların soyundan gelenlere şart koşmayın** | Çarpıştırıcının kendisinde koşullandırmayla aynı sorun |
---

## Yaygın Tuzaklar
| Tuzak | Açıklama | Örnek |
|-----------|------------|------------|
| **Değişken önyargısı atlandı** | Kafa karıştırıcı bir durum için kontrol başarısızlığı | Eğitimi tahmin etme → yeteneği kontrol etmeden kazanç |
| **Aşırı kontrol** | Bir aracı veya çarpıştırıcı üzerinde koşullandırma | Eğitimi tahmin ederken iş unvanını kontrol etmek → kazançlar |
| **Seçim yanlılığı** | Tedaviden etkilenen bir değişkene koşullanma | Eğitim çalışırken yalnızca çalışan kişileri analiz etmek → ücretler |
| **Ölümsüz zaman önyargısı** | Grup çalışmalarında kişi zamanının yanlış sınıflandırılması | Hastalar tedavi görecek kadar uzun süre hayatta kalmalıdır |
| **Ortalama regresyon** | Aşırı değerler ortalamaya doğru ilerleme eğilimindedir | Hasta hastalar tedaviden sonra ne olursa olsun iyileşir |
| **Tedavi sonrası önyargı** | Tedavi Sonrası Oluşan Değişkenlere İlişkin Koşullanma | İlaç etkinliğini tahmin ederken olumsuz olayların kontrol edilmesi |
---

## Araçlar ve Kütüphaneler
| Araç | Dil | Açıklama |
|------|----------|------------|
| **Neden Yap** | Python | Microsoft kütüphanesi; DAG tabanlı nedensel çıkarım |
| **NedenselML** | Python | Uber'in iyileştirme modellemesi ve nedensel makine öğrenimi kütüphanesi |
| **EconML** | Python | Çift ML, nedensel ormanlar, araçsal değişkenler |
| **doğrusal modeller** | Python | IV, panel veri modelleri, DiD |
| **Eşleştir** | R | Eğilim puanı eşleştirme |
| **dagitty** | R/web | DAG analizi; ayar setlerini tanımlayın |
| **NedenselEtki** | R / Python | Nedensel çıkarım için Bayes yapısal zaman serileri |
---

## Özet
Nedensel çıkarım, "olanların" ötesine geçerek "her şey farklı olsaydı ne olurdu" sorusuna geçmekle ilgilidir. Temel zorluk, aynı ünite için hem işlenmiş hem de işlenmemiş sonuçları asla gözlemleyemeyeceğimizdir; karşı olgusallık her zaman eksiktir. Rastgele deneyler, tedavi ve kontrol gruplarını karşılaştırılabilir hale getirerek bu sorunu çözer. Rastgeleleştirme mümkün olmadığında, yarı deneysel yöntemler (DiD, regresyon süreksizliği, araçsal değişkenler, sentetik kontrol) gözlemsel verilerden karşı olgusal olanı yeniden oluşturmaya çalışır. DAG'ler varsayımların açık bir şekilde ortaya konulmasına ve kontrol edilecek doğru değişkenlerin belirlenmesine yardımcı olur. Temel beceri, veri oluşturma süreci hakkında dikkatlice düşünmektir: neyin sebep olduğu, karıştırıcının ne olduğu, çarpıştırıcının ne olduğu ve alternatifin etkisi altında ne olabileceği.