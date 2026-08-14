<!--
---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [testing, methodologies, coding-and-technology]
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
# Test Metodolojileri
Test etmek, kodunuzun çalıştığına ve daha da önemlisi, kodda yapılan değişikliklerin zaten işe yarayanları bozmadığına dair güveni nasıl kazanacağınızdır. İyi testler, hataları kullanıcılardan önce yakalar, beklenen davranışı belgelendirir ve korkusuzca yeniden düzenlemeye olanak tanır. Bu dosya, birim testlerden uçtan uca testlere kadar tüm test stratejileri yelpazesini ve testi etkili kılan ilkeleri kapsar.
---

## Test Piramidi
Test piramidi bir projedeki testlerin ideal dağılımını tanımlar.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Seviye | Sayısı | Hız | Maliyet | Neyi Test Ediyor |
|----------|----------|----------|------|---------------|
| **Birim** | Birçok | Hızlı (ms) | Düşük | Bireysel işlevler, sınıflar, yöntemler |
| **Entegrasyon** | Bazıları | Orta (100ms-s) | Orta | Bileşenler nasıl etkileşime girer; veritabanı sorguları; API çağrıları |
| **E2E** | Az | Yavaş (saniye-dakika) | Yüksek | Tam kullanıcı gerçek sistem üzerinden akar |
---

## Birim Testi
Ayrı ayrı kod birimlerinin ayrı ayrı test edilmesi.
### İlkeler
| Prensip | Açıklama |
|-----------|----------------|
| **Hızlı** | Her test milisaniye cinsinden yürütülmelidir |
| **İzole** | Testler birbirine bağlı değildir; paylaşılan durum yok |
| **Deterministik** | Aynı girdi → her seferinde aynı çıktı (rastgelelik yok, zamana bağımlılık yok) |
| **Kendi kendini kontrol etme** | Test otomatik olarak geçer veya başarısız olur; manuel incelemeye gerek yok |
| **Zamanında** | (TDD) kodunun yanında veya öncesinde yazılmıştır |
### Bir Testin Anatomisi
| Aşama | Açıklama |
|----------|----------------|
| **Düzenle** | Test verilerini ve bağımlılıkları ayarlayın |
| **Yasa** | Test edilen işlevi veya yöntemi çağırın |
| **İddia** | Sonucun beklentilerle eşleştiğini doğrulayın |
### Neyi Test Etmeli
| Kategori | Örnekler |
|----------|-----------|
| **Mutlu yol** | Normal girdiler beklenen çıktıları üretir |
| **Kenar kasaları** | Boş giriş, boş, sıfır, maksimum değerler, tek öğe |
| **Hata durumları** | Geçersiz giriş, eksik veri, izin reddedildi |
| **Sınır koşulları** | Tek tek; tam olarak sınırlarda |
### Alaycı ve İnatçı
| Dönem | Açıklama | Ne Zaman Kullanılmalı |
|------|-------------|------------|
| **Sahte** | Nasıl adlandırıldığını kaydeden sahte bir nesne | Etkileşimler doğrulanıyor (bu yöntem çağrıldı mı?) |
| **Taslak** | Önceden belirlenmiş değerleri döndüren sahte bir nesne | Test verilerinin sağlanması (bu kullanıcıyı veritabanından döndürün) |
| **Casus** | Gerçek bir nesneye yapılan çağrıları kaydeden bir sarmalayıcı | Kısmi doğrulama |
| **Sahte** | Basitleştirilmiş ancak çalışan bir uygulama | Testler için bellek içi veritabanı |
| Alaycı Kütüphane | Dil |
|----------------|-----------|
| **unittest.mock** | Python |
| **şaka** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Adedi** | C# |
| **tanıklık et / hareket et** | Git |
---

## Entegrasyon Testi
Birden fazla bileşenin birlikte nasıl çalıştığını test etmek.
| Ne Test Edilmeli | Örnek |
|---------------|-----------|
| **Veritabanı sorguları** | ORM doğru SQL üretiyor mu? İndeksler kullanılıyor mu? |
| **API uç noktaları** | İstek-yanıt döngüsünün tamamı çalışıyor mu? |
| **Hizmet etkileşimleri** | A servisi B servisini doğru şekilde çağırıyor mu? |
| **Dış bağımlılıklar** | Ödeme ağ geçidi entegrasyonu çalışıyor mu? |
### Stratejiler
| Strateji | Açıklama | Takas |
|----------|----------------|-----------|
| **Gerçek bağımlılıklar** | Gerçek bir veritabanı, gerçek mesaj kuyruğu kullanın | En gerçekçi; Yavaş; kurulumu daha zor |
| **Test kapsayıcıları** | Her test çalıştırması için Docker kapsayıcılarını etkinleştirin | İyi denge; tekrarlanabilir |
| **Bellek içi alternatifler** | PostgreSQL yerine H2; bellek içi mesaj veri yolu | Hızlı; gerçek dünyadaki sorunları kaçırabilir |
| **Sözleşme testi** | Hizmetlerin API sözleşmelerine uyduğunu doğrulayın | Arayüz değişikliklerini yakalar |
---

## Uçtan Uca (E2E) Testi
Tüm sistemin kullanıcı bakış açısıyla test edilmesi.
| Araç | Tür | En İyisi |
|------|----------|----------|
| **Oyun yazarı** | Tarayıcı otomasyonu | Web uygulamaları; çapraz tarayıcı |
| **selvi** | Tarayıcı otomasyonu | Web uygulamaları; geliştirici deneyimi |
| **Selenyum** | Tarayıcı otomasyonu | Miras; geniş dil desteği |
| **Detoks** | Mobil E2E | Yerel uygulamalara tepki verin |
| **Appium** | Mobil E2E | Yerel ve hibrit mobil uygulamalar |
| **Maestro** | Mobil E2E | Mobil uygulamalar; basit YAML sözdizimi |
| **k6 / Keçiboynuzu** | Yük testi | Yük altında performans |
### E2E En İyi Uygulamaları
| Alıştırma | Neden |
|----------|-----|
| **Yalnızca kritik yolları test edin** | E2E testleri yavaştır; en önemli olana odaklanın |
| **Test veri fabrikalarını kullanın** | Test verilerini programlı olarak oluşturun; tohum verilerine güvenmeyin |
| **Testlerden sonra temizleyin** | Her test sistemi bilinen bir durumda bırakmalıdır |
| **Kullanıcı arayüzü ayrıntılarını test etmekten kaçının** | Davranışı test edin, CSS sınıflarını veya öğe konumlarını değil |
| **CI'da çalıştır** | E2E testleri her değişiklikte otomatik olarak çalıştırılmalıdır |
---

## Test Odaklı Geliştirme (TDD)
Önce testi yazın, ardından geçmesini sağlayacak kodu yazın.
| Adım | Açıklama |
|------|-----------------|
| **1. Kırmızı** | İstenilen davranışı açıklayan başarısız bir test yazın |
| **2. Yeşil** | Testi geçmek için minimum kodu yazın |
| **3. Yeniden düzenleme** | Testleri yeşil tutarken kodu temizleyin |
| Fayda | Açıklama |
|-----------|------------|
| **Tasarım geri bildirimi** | Testler sizi uygulamadan önce arayüzler hakkında düşünmeye zorlar |
| **Regresyon güvenliği** | Her hata bir testten geçer; hata asla geri dönemez |
| **Belgeler** | Testler, beklenen davranışın canlı belgelenmesi görevi görür |
| **Güven** | Yüksek test kapsamı, korkusuz yeniden düzenlemeye olanak tanır |
---

## Davranış Odaklı Geliştirme (BDD)
BDD, davranışı kullanıcının bakış açısından tanımlayan doğal dilde testler yazarak TDD'yi genişletir.
### Verilen-O Zaman-O Zaman Formatı
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Araç | Dil |
|----------|----------|
| **Salatalık** | Java, JavaScript, Ruby ve diğerleri |
| **Davranış** | Python |
| **SpecFlow** | C# |
| **Jest** (açıklama/it ile) | JavaScript |
---

## Diğer Test Türleri
| Tür | Neyi Test Ediyor | Araçlar |
|------|--------------|-------|
| **Performans/Yük** | Yük altında sistem davranışı | k6, JMeter, Locust, Gatling |
| **Güvenlik** | Güvenlik açıkları ve saldırı vektörleri | OWASP ZAP, Burp Paketi, Snyk |
| **Erişilebilirlik** | WCAG uyumluluğu | balta, Deniz Feneri, pa11y |
| **Sözleşme** | Hizmetler arasında API uyumluluğu | Paktı, Bahar Bulutu Sözleşmesi |
| **Mutasyon** | Test paketinin kalitesi | Stryker, Mutmut, PIT |
| **Görsel regresyon** | Sürümler arasında kullanıcı arayüzü değişiklikleri | Percy, Kromatik, BackstopJS |
| **Kaos** | Arızalara karşı sistem dayanıklılığı | Kaos Maymunu, Turnusol, Gremlin |
| **Duman** | Dağıtımdan sonraki temel işlevsellik | Özel komut dosyaları; sağlık kontrolleri |
| **Islatma** | Uzun süre boyunca sistem davranışı | Uzun süreli yük testleri |
---

## Test Organizasyonu
| Desen | Açıklama | Ne Zaman Kullanılmalı |
|-----------|---------------|------------|
| **Ortak konum** | Test ettikleri kodun yanındaki testler (`src/utils.test.ts`) | Çoğu proje; bulması kolay |
| **Ayrı dizin** |`tests/`veya`__tests__/`klasöründeki testler | Büyük projeler; net ayrım |
| **Test fikstürleri** |`fixtures/`dizininde paylaşılan test verileri | Birden fazla test aynı verilere ihtiyaç duyduğunda |
| **Test yardımcı programları** |`test-utils/`dizinindeki paylaşılan yardımcılar | Kurulum mantığı karmaşık olduğunda |
---

## Kod Kapsamı
| Metrik | Neyi Ölçer | Sınırlama |
|----------|----------|-----------|
| **Hat kapsamı** | Testler tarafından yürütülen kod satırlarının yüzdesi | İddiaların kalitesini ölçmüyor |
| **Şube kapsamı** | Alınan şubelerin yüzdesi (eğer/başka) | Hat kapsama alanından daha iyi; hala tüm hataları yakalayamıyor |
| **Yol kapsamı** | Alınan yürütme yollarının yüzdesi | En kapsamlısı; karmaşık kodda üstel |
| **Mutasyon puanı** | Testlerle yakalanan mutasyonların yüzdesi | Test kalitesinin en iyi ölçüsü |
**Hedef**: %80 hat kapsamı makul bir varsayılan değerdir. Ancak kapsam bir hedef değil, bir kılavuzdur; zayıf iddialarla yapılan %100 kapsam, ayrıntılı testlerle yapılan %70 kapsamdan daha kötüdür.
---

## Sürekli Entegrasyon ve Test
| Alıştırma | Açıklama |
|----------|----------------|
| **Her işlemde tüm birim testlerini çalıştırın** | Hızlı geri bildirim; gerilemeleri hemen yakalar |
| **PR'de entegrasyon testleri çalıştırın** | Birim testlerinin gözden kaçırdığı sorunları yakalar |
| **E2E testlerini her gece veya ana sayfayla birleştirme sırasında çalıştırın** | Yavaş ama kapsamlı |
| **Hızlı başarısız olun** | Zamandan tasarruf etmek için ilk arızada boru hattını durdurun |
| **Kesintili test politikası** | Kesintili testleri hemen karantinaya alın veya silin; asla görmezden gelme |
| **Test paralelleştirmesi** | CI süresini azaltmak için testleri paralel olarak çalıştırın |
---

## Pratik İpuçları
- **Testleri açıkça adlandırın.**`test_calculates_tax_for_high_earner`size neyin bozulduğunu söyler. `test_1`size hiçbir şey söylemez.
- **Test başına bir iddia (uygulanabilir olduğunda).** Arızaların teşhis edilmesini kolaylaştırır.
- **Uygulama ayrıntılarını test etmeyin.** Davranışı test edin. Dahili öğeleri yeniden düzenlerseniz testler bozulmamalıdır.
- **Üçüncü taraf kodlarını test etmekten kaçının.** Sahte harici kitaplıklar; kodunuzun onlarla etkileşimini test edin.
- **Testleri hızlandırın.** Test paketiniz 10 dakika sürerse geliştiriciler onu çalıştırmayı durdurur. Durmaksızın optimize edin.
- **Ölü testleri silin.** Her zaman başarılı olan veya kaldırılan kodu test eden testler gürültüdür.
- **Test koduna üretim kodu gibi davranın.** Okunabilir, bakımı yapılabilir ve iyi yapılandırılmış olmalıdır.
---

## Özet
Test etmek isteğe bağlı değildir; bozulmayan yazılımı nasıl geliştirdiğinizdir. Test piramidi sizi birçok hızlı birim testine, bazı entegrasyon testlerine ve birkaç E2E testine yönlendirir. TDD ve BDD yapılandırılmış yaklaşımlar sağlar. Alay etmek birimleri test için izole eder. Kod kapsamı genişliği ölçer ancak derinliği ölçmez. En önemli prensip şudur: eğer test edilmemişse bozuktur; sadece bunu henüz bilmiyorsunuz.