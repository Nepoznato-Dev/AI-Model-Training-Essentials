<!--
---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
difficulty_level: "advanced"
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
# API Tasarımı ve Entegrasyon Hataları
API'ler (Uygulama Programlama Arayüzleri) modern yazılımın bağ dokusudur; hizmetlerin iletişim kurmasına, üçüncü tarafların entegre olmasına ve ekiplerin bağımsız çalışmasına olanak tanır. API tasarımı yanlış gittiğinde sonuçları ona bağlı olan her sisteme yayılır: bozulan entegrasyonlar, güvenlik açıkları, geliştiricinin hayal kırıklığı ve maliyetli yeniden yazma işlemleri. Sistemlerin güvenilir bir şekilde iletişim kuramadığı entegrasyon hataları, üretim olaylarının en yaygın kaynakları arasındadır.
---

## Yaygın API Tasarım Hataları
### Tasarım Hataları
| Hata | Açıklama | Sonuç |
|-----------|---------------|------------|
| **Tutarsız adlandırma** | `/getUsers`vs`/list_users`vs`/fetch-users`| Bilinç bulanıklığı, konfüzyon; hatalar; yavaş gelişme |
| **Aşırı yüklenmiş uç noktalar** | Parametrelere dayalı olarak 10 farklı şey yapan tek bir uç nokta | Anlamak zor; test edilmesi zor; değiştirmek zor |
| **Yetersiz getiriliyor** | İlgili verileri almak için istemcinin 5 API çağrısı yapması gerekir | Yavaş; israf; karmaşık müşteri kodu |
| **Aşırı getirme** | API, istemcinin yalnızca 2 | Boşa harcanan bant genişliği; mobilde yavaş; güvenlik riski (gereksiz verilerin açığa çıkması) |
| **Sürüm oluşturma yok** | Son dakika değişiklikleri uyarı yapılmadan dağıtıldı | Müşteriler bozulur; kızgın geliştiriciler |
| **Belirsiz hata mesajları** | "Hata 500: Dahili Sunucu Hatası", ayrıntısız | Hata ayıklamak imkansız; yavaş çözünürlük |
| **Eksik sayfalandırma** | Uç nokta tüm kayıtları döndürür (milyonlarca olabilir) | Zaman aşımları; hafıza yorgunluğu; çöken istemciler |
| **Tutarsız durum kodları** | Hatalar için 200 Tamam; Müşteri hataları için 500 | Müşteriler başarıyı başarısızlıktan ayıramaz |
### REST API Anti-Desenleri
| Anti-Desen | Açıklama | Daha İyi Yaklaşım |
|---------------|---------------|-----------------|
| **Mutasyonlar için GET'i kullanma** | `GET /delete-user?id=5`| DELETE yöntemini kullanın |
| **Her şey için POST'u kullanma** | `POST /get-users`; `POST /update-user`| Uygun HTTP yöntemlerini kullanın (GET, POST, PUT, PATCH, DELETE) |
| **API'den HTML döndürme** | API, HTML parçalarını döndürür | JSON'u döndürün; istemcinin oluşturmasına izin ver |
| **URL'lerdeki iş mantığı** | `/users/active/premium/from-2023`| Karmaşık filtreler için sorgu parametrelerini veya istek gövdesini kullanın |
| **Veritabanı şeması gösteriliyor** | `/api/table_name/column`| API'yi tablolara değil, kaynaklara ve etki alanı kavramlarına göre tasarlayın |
| **HATEOAS / bağlantı yok** | İstemci tüm URL'leri sabit kodlar | Yanıtlara ilgili kaynaklara bağlantılar ekleyin |
---

## Güvenlik Arızaları
### Yaygın API Güvenlik Açıkları
| Güvenlik Açığı | Açıklama | Örnek |
|-------------|------------|------------|
| **Kötü kimlik doğrulama** | API, kimliği düzgün şekilde doğrulamıyor | Belirteç doğrulamasının eksik olması; süresi dolmuş jetonlar kabul edildi |
| **Aşırı veri açığa çıkması** | API, müşterinin ihtiyaç duyduğundan daha fazla veri döndürüyor | Kullanıcı uç noktası şifre karmalarını ve dahili kimlikleri döndürür |
| **Toplu atama** | Müşteri, yapmaması gereken alanları ayarlayabilir |  `PATCH /user`,`role: "admin"`|
| **Enjeksiyon** | Kullanıcı girişi kod olarak yorumlandı | SQL enjeksiyonu; NoSQL enjeksiyonu; komut enjeksiyonu |
| **IDOR** (Güvensiz Doğrudan Nesne Referansı) | URL'deki kimliği değiştirerek kaynaklara erişme | `/api/users/5`→ başka birinin verilerini görmek için`/api/users/6`olarak değiştirin |
| **Hız sınırlaması eksik** | API çağrılarında sınır yok | Kaba kuvvet; hizmet reddi; kazıma |
| **CORS yanlış yapılandırması** | Aşırı hoşgörülü çapraz kaynak erişimi |  Kimliği doğrulanmış uç noktalarda`Access-Control-Allow-Origin: *`|
### Kimlik Doğrulama ve Yetkilendirme Hataları
| Başarısızlık | Açıklama | Etki |
|-----------|------------|-----------|
| **Sabit kodlanmış kimlik bilgileri** | Kaynak kodundaki API anahtarları veya şifreleri | Sürüm kontrolünden sızdırıldı; tüm geliştiricilerin erişimine açıktır |
| **Jetonun geçerlilik süresi yok** | Jetonların süresi hiçbir zaman dolmaz | Çalınan token kalıcı erişim sağlıyor |
| **Zayıf gizli anahtarlar** | Kısa veya öngörülebilir imzalama anahtarları | Jetonlar sahte olabilir |
| **Kapsam/izin yok** | Tüm jetonlar tam erişime sahiptir | Güvenliği ihlal edilmiş jeton = tam sistem erişimi |
| **Hassas verileri günlüğe kaydetme** | Günlüklerdeki jetonlar veya şifreler | Günlük erişimi olan herkes erişebilir |
| **Tutarsız yetkilendirme** | Bazı uç noktalar izinleri kontrol eder; diğerleri bunu yapmıyor | Korumasız uç noktalar üzerinden yetkisiz erişim |
---

## Entegrasyon Hataları
### Dağıtılmış Sistem Entegrasyon Sorunları
| Başarısızlık | Açıklama | Örnek |
|-----------|------------|------------|
| **Sıkı bağlantı** | Hizmetler birbirinin dahili uygulama ayrıntılarına bağlıdır | Bir hizmetin veritabanını değiştirmek diğer üç hizmetin veri tabanını bozar |
| **Senkron zincirler** | A Servisi B'yi arar C D'yi arar; gecikme birikir | 200ms + 300ms + 500ms = 1 saniye tepki süresi |
| **Devre kesici yok** | Başarısız hizmet, ardışık arızalara neden olur | Servis D yavaştır; tüm yukarı akış hizmetleri bekleyen iş parçacıklarını tüketiyor |
| **Yeniden deneme mantığı yok** | Geçici arızalar kalıcı hale geliyor | Ağ kesintisi = başarısız işlem; kullanıcının manuel olarak yeniden denemesi gerekiyor |
| **Aşırı sayıda yeniden deneme** | Geri çekilmeden yapılan yeniden denemeler, kurtarma hizmetlerini zorluyor | Gürleyen sürü sorunu |
| **İdempotans yok** | İdempotent olmayan bir işlemi yeniden denemek kopyalar oluşturur | Ödeme iki kez tahsil edildi; sipariş iki kez oluşturuldu |
| **Nihai tutarlılık sürprizleri** | İstemci bir yazma işleminden sonra eski verileri okuyor | Kullanıcı profilini günceller; sayfayı yeniler; eski veriler hâlâ gösteriliyor |
### Üçüncü Taraf Entegrasyon Hataları
| Başarısızlık | Açıklama | Azaltma |
|-----------|------------|------------|
| **Satıcı API değişiklikleri** | Üçüncü taraflar API'lerini bildirimde bulunmaksızın değiştirir | Sürüm sabitleme; soyutlama katmanı; satıcı değişiklik günlüklerinin izlenmesi |
| **Hız sınırlama** | Üçüncü taraf isteklerinizi kısıtlıyor | Önbelleğe alma; sıraya girme isteği; daha yüksek limitlerin müzakeresi |
| **Satıcının aksama süresi** | Üçüncü taraf hizmeti mevcut değil | Devre kesiciler; geri çekilme davranışı; çok tedarikçili strateji |
| **Veri biçimi değişiklikleri** | Üçüncü taraf yanıt biçimini değiştiriyor | Şema doğrulaması; dönüşüm katmanı; format değişiklikleriyle ilgili uyarılar |
| **Geçiş yolu olmadan kullanımdan kaldırılma** | Satıcı, eşdeğeri olmayan uç noktayı kullanımdan kaldırıyor | Haberdar olun; soyutlamayı sürdürün; geçişleri erken planlayın |
---

## Vaka Çalışmaları
### Örnek Olay 1: Her Şeyi Geri Döndüren API
| Görünüş | Açıklama |
|----------|----------------|
| **Senaryo** | Bir SaaS şirketinin kullanıcı API'si, dahili meta veriler de dahil olmak üzere tüm kullanıcı alanlarını döndürdü |
| **Ne yanlış gitti** | Alan filtreleme yok; Yanıt şifre karmalarını, dahili notları ve yönetici işaretlerini içeriyordu |
| **Etki** | Güvenlik araştırmacıları bu ifşayı keşfetti; kamuya açıklama; GDPR araştırması |
| **Temel neden** | API, tüm veritabanı modelini filtrelemeden serileştirdi |
| **Düzeltme** | Açık yanıt modelleri; alan düzeyinde erişim kontrolü; tüm uç noktaların güvenlik incelemesi |
| **Ders** | Veritabanı modelinizi hiçbir zaman doğrudan bir API aracılığıyla açığa çıkarmayın; DTO'ları (Veri Aktarım Nesneleri) kullanın |
### Örnek Olay 2: Basamaklı Başarısızlık
| Görünüş | Açıklama |
|----------|----------------|
| **Senaryo** | Hizmetler arası eşzamanlı iletişime sahip bir mikro hizmet mimarisi |
| **Ne yanlış gitti** | Bir hizmette veritabanı yavaşlaması yaşandı; yukarı akış hizmetleri yanıtları bekledi; iş parçacığı havuzları tükendi |
| **Etki** | 45 dakika boyunca sistem kesintisini tamamlayın; etkilenen tüm hizmetler |
| **Temel neden** | Devre kesici yok; zaman aşımı yok; eşzamanlı bağımlılık zinciri |
| **Düzeltme** | Devre kesiciler; zaman aşımları; mümkün olduğunda eşzamansız iletişim; perdeler |
| **Ders** | Hizmetler arasındaki eşzamanlı çağrılar kırılgan zincirler oluşturur; başarısızlık için tasarım |
---

## En İyi Uygulamalar
### API Tasarım Kontrol Listesi
| Alan | Alıştırma |
|----------|----------|
| **Adlandırma** | Kaynaklar için isimler kullanın; Eylemler için HTTP yöntemleri; tutarlı adlandırma kuralı |
| **Sürüm oluşturma** | İlk günden itibaren sürüm; URL sürümlendirmeyi (`/v1/`) veya başlık sürümlendirmeyi kullanın |
| **Sayfalandırma** | Liste uç noktalarını her zaman sayfalandırın; büyük veri kümeleri için imleç tabanlı sayfalandırmayı kullanın |
| **Hata işleme** | Tutarlı hata formatı; hata kodlarını dahil edin; eyleme dönüştürülebilir mesajlar sağlayın |
| **Hız sınırlama** | Oran limitlerini uygulayın; yeniden dene başlığıyla 429'u döndür |
| **İdempotans** | Mutasyon uç noktaları için idempotency anahtarlarını destekleyin |
| **Belgeler** | OpenAPI / Swagger spesifikasyonu; güncel tutun; örnekler sağlayın |
| **Test etme** | Sözleşme testleri; entegrasyon testleri; tüketici odaklı sözleşme testleri |
| **İzleme** | Gecikmeyi izleyin; hata oranları; verim; bağımlılık sağlığı |
| **kullanımdan kaldırılma** | Kullanımdan kaldırılmaları önceden duyurun; geçiş kılavuzları sağlayın |
---

## Özet
API tasarım hataları, kozmetik (tutarsız adlandırma) ile felaket (güvenlik açıkları, ardışık hatalar) arasında değişir. En yaygın tasarım hataları (aşırı yüklenmiş uç noktalar, aşırı getirme, eksik sayfalandırma, belirsiz hatalar) API'lerin kullanımını ve bakımını zorlaştırır. Güvenlik hataları (bozuk kimlik doğrulama, IDOR, toplu atama, aşırı veri açığa çıkması) sistemleri saldırılara açık hale getirir. Entegrasyon hataları (sıkı bağlantı, senkronize zincirler, eksik devre kesiciler, yetersizlik), bir hatanın hizmetler arasında art arda yayıldığı kırılgan sistemler oluşturur. Üçüncü taraf entegrasyonları harici riskler ekler: API değişiklikleri, hız sınırlaması ve sağlayıcının kapalı kalma süresi. Önleme stratejileri iyi oluşturulmuştur: açık müdahale modellerinin kullanılması; ilk günden itibaren versiyon; devre kesicileri ve zaman aşımlarını uygulayın; idempotens için tasarım; tüm girişleri doğrulamak ve sterilize etmek; her şeyi izleyin; ve API sözleşmelerini, değişim için koordinasyon gerektiren bağlayıcı anlaşmalar olarak değerlendirin. En iyi API'ler sıkıcıdır; öngörülebilir, tutarlı, iyi belgelenmiş ve başarısızlığa karşı dayanıklıdır.