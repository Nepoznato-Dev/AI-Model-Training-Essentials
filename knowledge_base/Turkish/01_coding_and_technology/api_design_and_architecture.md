---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
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
# API Tasarımı ve Mimarisi
API (Uygulama Programlama Arayüzü), yazılım bileşenlerinin birbirleriyle nasıl konuştuğudur. İyi tasarlanmış bir API sezgiseldir, tutarlıdır ve birlikte çalışması keyiflidir. Kötü tasarlanmış bir model kafa karışıklığına, hatalara ve hayal kırıklığına neden olur. Bu dosya, geliştiricilerin gerçekten kullanmak istediği API'leri oluşturmaya yönelik ilkeleri, kalıpları ve uygulamaları kapsar.
---

## REST API Prensipleri
REST (Temsili Durum Transferi), web API'leri için baskın mimari tarzdır. Verileri URL'ler tarafından tanımlanan **kaynaklar** olarak ele alır ve bunlar üzerinde çalışmak için HTTP yöntemlerini kullanır.
### Temel İlkeler
| Prensip | Açıklama |
|-----------|----------------|
| **Kaynaklar** | Her şey URI'ye sahip bir kaynaktır (`/users/123`, `/orders/456`) |
| **HTTP Yöntemleri** | GET (oku), POST (oluştur), PUT (değiştir), PATCH (kısmi güncelleme), DELETE (kaldır) |
| **Vatansızlık** | Her istek ihtiyaç duyulan tüm bilgileri içerir; sunucu tarafı oturum durumu yok |
| **Tekdüze Arayüz** | Tutarlı kaynak adlandırma, standart yöntemler, standart durum kodları |
| **Temsil** | Kaynaklar birden fazla formatta (JSON, XML) temsil edilebilir |
### Kaynak Adlandırma Kuralları
| Yap | Yapma |
|----|-------|
| `/users`(çoğul isim) | `/user`(tekil) |
| `/users/123/orders`(yuvalanmış) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(filtreleme için sorgu parametreleri) | `/productsByCategory/electronics`|
| Kısa çizgi kullanın:`/user-profiles`| Alt çizgi kullanın:`/user_profiles`|
### HTTP Yöntemleri ve Kimlik Belirsizliği
| Yöntem | Amaç | İdemsiz mi? | Güvenli? |
|----------|------------|-------------|-------|
| **ALIN** | Bir kaynağı okuyun | ✅ Evet | ✅ Evet |
| **GÖNDERİ** | Kaynak oluşturun | ❌ Hayır | ❌ Hayır |
| **koy** | Kaynağı tamamen değiştirme | ✅ Evet | ❌ Hayır |
| **YAMA** | Kaynağı kısmen güncelleme | ❌ Hayır* | ❌ Hayır |
| **SİL** | Kaynağı kaldırma | ✅ Evet | ❌ Hayır |
*PATCH dikkatli bir tasarımla idempotent hale getirilebilir.
### HTTP Durum Kodları
| Kod | Anlamı | Ne Zaman Kullanılmalı |
|------|---------|------------|
| **200** | tamam | Başarılı AL, KOY, YAMA, SİL |
| **201** | Oluşturuldu | Başarılı POST (kaynak oluşturuldu) |
| **204** | İçerik Yok | Başarılı SİLME (döndürülecek bir şey yok) |
| **400** | Hatalı İstek | Geçersiz giriş veya hatalı biçimlendirilmiş istek |
| **401** | Yetkisiz | Eksik veya geçersiz kimlik doğrulama |
| **403** | Yasak | Kimliği doğrulanmış ancak yetkili değil |
| **404** | Bulunamadı | Kaynak mevcut değil |
| **409** | Çatışma | Yinelenen kaynak veya durum çakışması |
| **422** | İşlenemeyen Varlık | Geçerli JSON ancak anlamsal hatalar |
| **429** | Çok Fazla İstek | Oran sınırı aşıldı |
| **500** | Dahili Sunucu Hatası | Beklenmeyen sunucu hatası |
| **502** | Kötü Ağ Geçidi | Yukarı akış hizmet hatası |
| **503** | Hizmet Kullanılamıyor | Geçici aşırı yük veya bakım |
---

## API Sürümü Oluşturma
API'ler gelişiyor. Son derece önemli değişiklikler yapmanız gerektiğinde sürüm oluşturma, mevcut istemcilerin çalışmaya devam etmesini sağlar.
| Strateji | Örnek | Artıları | Eksileri |
|----------|------------|------|------|
| **URL yolu** | `/v1/users`,`/v2/users`| Basit, açık | Sürüm başına URL değişiklikleri |
| **Sorgu parametresi** | `/users?version=2`| Esnek | Unutulması kolay |
| **Başlık** | `Accept: application/vnd.myapi.v2+json`| URL'leri temizle | Daha az keşfedilebilir |
| **Sürüm oluşturma yok** | Yalnızca şema gelişimi | En basit | Son dakika değişiklikleri herkesi etkiliyor |
**En iyi uygulama**: Netlik sağlamak için URL yolu sürümlendirmesini (`/v1/`) kullanın. En az bir önceki sürümü destekleyin. Açık zaman çizelgeleri olan eski sürümleri kullanımdan kaldırın.
---

## Kimlik Doğrulama Yöntemleri
| Yöntem | Nasıl Çalışır | En İyisi |
|----------|----------------|----------|
| **API Anahtarları** | Başlıktaki gizli anahtar (`X-API-Key: abc123`) | Sunucudan sunucuya, basit entegrasyonlar |
| **OAuth2** | Kapsamlı belirteç tabanlı yetkilendirme | Üçüncü taraf erişimi, kullanıcı tarafından yetkilendirilen uygulamalar |
| **JWT** | Talepleri olan bağımsız belirteç | Hizmetler arasında durum bilgisi olmayan kimlik doğrulama |
| **Temel Kimlik Doğrulama** | Base64 kodlu kullanıcı adı:şifre | Yalnızca geliştirme — asla TLS olmadan üretim |
| **Oturum çerezleri** | Yalnızca HTTP tanımlama bilgisinde sunucu tarafı oturum kimliği | Geleneksel web uygulamaları |
### OAuth2 Akışı (Basitleştirilmiş)
1. İstemci, kullanıcıyı yetkilendirme sunucusuna yönlendirir.
2. Kullanıcı oturum açar ve izin verir.
3. Yetkilendirme sunucusu bir yetkilendirme kodu döndürür.
4. Müşteri, erişim belirteci için kod alışverişinde bulunur (ve isteğe bağlı olarak belirteci yeniler).
5. Müşteri, API'yi çağırmak için erişim belirtecini kullanır.
6. Erişim belirtecinin süresi dolduğunda, yenisini almak için yenileme belirtecini kullanın.
---

## API Stilleri: REST vs GraphQL vs gRPC
| Özellik | DİNLENME | GraphQL | gRPC |
|-----------|------|-----------|------|
| **Veri Formatı** | JSON (tipik olarak) | JSON | Protobuf (ikili) |
| **Uç noktalar** | Çoklu (kaynak başına bir) | Tek uç nokta | .proto dosyası tarafından tanımlanmış |
| **Aşırı getirme** | Ortak (gereğinden fazlasını alın) | Yok (istemci alanları belirtir) | Yok (şema tanımlı) |
| **Yetersiz getiriliyor** | Birden fazla çağrı gerektirir | Yok (tam olarak ihtiyaç duyulanı alın) | Yok |
| **Gerçek zamanlı** | WebSocket'ler gerekli | Abonelikler yerleşik | Dahili akış |
| **Önbelleğe alma** | HTTP önbelleğe alma doğal olarak çalışır | Önbelleğe alınması daha zor | Sınırlı |
| **Öğrenme Eğrisi** | Düşük | Orta | Orta–Yüksek |
| **En İyisi** | Genel API'ler, CRUD uygulamaları | Karmaşık kullanıcı arayüzleri, mobil uygulamalar | Dahili mikro hizmetler, yüksek performanslı |
---

## Sayfalandırma, Filtreleme ve Sıralama
Listeleri döndüren uç noktalar için:
| Tekniği | Örnek | Ne Zaman Kullanılmalı |
|-----------|------------|-------------|
| **Ofset/Sınır** | `?offset=20&limit=10`| Basit; küçük veri kümeleri için çalışır |
| **İmleç tabanlı** | `?cursor=abc123&limit=10`| Büyük veri kümeleri; tutarlı sonuçlar |
| **Anahtar takımı** | `?created_after=2024-01-01&limit=10`| Çok verimli; benzersiz anahtar gerektirir |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Hız Sınırlaması
API'nizi kötüye kullanıma karşı koruyun ve adil kullanımı sağlayın.
| Strateji | Nasıl Çalışır |
|----------|----------------|
| **Sabit pencere** | Zaman aralığı başına N istek (ör. 100/saat) |
| **Sürgülü pencere** | Daha ayrıntılı; değişen pencerede istekleri sayar |
| **Jeton kovası** | Sabit oranda eklenen jetonlar; her istek bir jeton tüketir |
Başlıklarla birlikte `429 Too Many Requests`'yi döndürün:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Hata İşleme
Tutarlı hata yanıtları API'lerle çalışmayı çok daha kolay hale getirir:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**İlkeler**: Tutarlı hata yapısı kullanın, işlem yapılabilir mesajlar ekleyin, standart HTTP durum kodları kullanın, hataları korelasyon kimlikleriyle sunucu tarafında günlüğe kaydedin ve yığın izlerini veya dahili ayrıntıları asla açığa çıkarmayın.
---

## API Belgeleri
| Araç | Açıklama |
|------|-----------------|
| **OpenAPI (Swagger)** | REST API belgeleri için endüstri standardı |
| **Swagger kullanıcı arayüzü** | OpenAPI spesifikasyonundan etkileşimli API belgeleri |
| **Postacı** | API testi, dokümantasyon ve koleksiyon paylaşımı |
| **Yinele** | OpenAPI spesifikasyonundan güzel API referans belgeleri |
| **GraphQL Oyun Alanı / GraphiQL** | İnteraktif GraphQL keşfi |
**En iyi uygulama**: Önce OpenAPI spesifikasyonunu yazın (özellik odaklı geliştirme), ardından bundan belgeler ve istemci SDK'ları oluşturun.
---

## API Ağ Geçidi Kalıpları
Bir API ağ geçidi, istemciler ve arka uç hizmetleri arasında yer alır ve tek bir giriş noktası sağlar.
| Sorumluluk | Açıklama |
|---------------|---------------|
| **Yönlendirme** | Uygun arka uç hizmetlerine yönelik doğrudan talepler |
| **Kimlik doğrulama** | Belirteçleri ağ geçidi düzeyinde doğrulayın |
| **Hız Sınırlaması** | Genel veya müşteri başına sınırlar uygulayın |
| **Dönüşüm** | Protokoller arasında dönüştürme (REST ↔ gRPC) |
| **Önbelleğe alma** | Yaygın yanıtları önbelleğe al |
| **İzleme** | Merkezi kayıt ve ölçümler |
| **Yük Dengeleme** | Trafiği hizmet örnekleri arasında dağıtın |
| Araç | Tür |
|------|------|
| **Kong** | Açık kaynaklı API ağ geçidi (Nginx tabanlı) |
| **AWS API Ağ Geçidi** | Tümüyle yönetilen, AWS ile entegre |
| **Azure API Yönetimi** | Geliştirici portalıyla yönetilen ağ geçidi |
| **Elçi / Istio** | API ağ geçidi özelliklerine sahip hizmet ağı |
| **Trafik** | Otomatik keşif, Haydi Şifreleyelim entegrasyonu |
---

## Web kancaları
Web kancaları, istemcilerin değişiklikler için anket yapmasını sağlamak yerine, API'nizin istemcilere olayları gerçek zamanlı olarak göndermesine olanak tanır.
| Görünüş | En İyi Uygulama |
|----------|-----------------|
| **Teslimat** | JSON yüküyle müşterinin URL'sine POST isteği |
| **Güvenlik** | Yükleri HMAC ile imzalayın; istemci imzayı doğruluyor |
| **Güvenilirlik** | Üstel geri çekilmeyle başarısız teslimatları yeniden deneyin |
| **İdempotans** | Benzersiz etkinlik kimliğini ekleyin; istemci kopyaları yönetir |
| **Sürüm oluşturma** | API sürümünü web kancası yüküne dahil edin |
---

## Tasarım Kontrol Listesi
- [ ] Kaynaklar çoğul isimlerdir (`/getUser`değil,`/users`)
- [ ] HTTP yöntemlerinin doğru kullanılması (okuma için GET, oluşturma için POST vb.)
- [ ] Tutarlı hata yanıt formatı
- [ ] Tüm liste uç noktaları için sayfalandırma
- [ ] Anlaşılır başlıklarla hız sınırlaması
- [ ] API sürüm oluşturma stratejisi tanımlandı
- [ ] Kimlik doğrulama ve yetkilendirme mevcut
- [ ] Tüm uç noktalarda giriş doğrulaması
- [ ] OpenAPI/Swagger belgelerinin bakımı yapıldı
- [ ] CORS doğru şekilde yapılandırıldı
- [ ] HTTPS üretimde uygulandı
- [ ] Gerektiğinde POST işlemleri için kimlik anahtarları