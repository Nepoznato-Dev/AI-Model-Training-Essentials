---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
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
tags: [cybersecurity, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Siber Güvenliğin Temelleri
Güvenlik, sonradan akla gelen bir düşünce olarak değil, sistemin her katmanına en başından itibaren entegre edilmesi gereken bir disiplindir. Bir web uygulaması oluşturmak, altyapıyı yönetmek veya bir API göndermek olsun, tehdit ortamını ve savunmanın temellerini anlamak çok önemlidir.
---

## Şifreleme ve Kriptografi
### Simetrik ve Asimetrik Şifreleme
| Tür | Nasıl Çalışır | Hız | Anahtar Dağıtımı | Örnekler |
|------|-------------|-------|------|----------|
| **Simetrik** | Şifreleme ve şifre çözme için aynı anahtar | Hızlı | Zorluk: Anahtar nasıl paylaşılır? | AES-256, ChaCha20 |
| **Asimetrik** | Genel anahtar şifreler, özel anahtar şifreyi çözer | Daha yavaş | Ortak anahtar açıkça paylaşılabilir | RSA, ECC (Eliptik Eğri) |
Pratikte çoğu sistem **her ikisini de** kullanır: simetrik bir anahtarın güvenli bir şekilde değişimi için asimetrik şifreleme, ardından verilerin büyük kısmı için simetrik şifreleme. TLS/HTTPS bu şekilde çalışır.
### Hashing
Karma tek yönlü bir işlevdir: girişi sabit boyutlu bir dizeye dönüştürür. Bunu tersine çeviremezsiniz ama aynı girdi her zaman aynı çıktıyı üretir.
| Kullanım Örneği | Önerilen Algoritma | Kaçının |
|----------|---------------|----------|
| **Şifre saklama** | Argon2id, bcrypt, scrypt | MD5, SHA-1, düz SHA-256 (çok hızlı) |
| **Veri bütünlüğü** | SHA-256, SHA-3 | MD5 (bozuk), SHA-1 (bozuk) |
| **Dijital imzalar** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS, TLS üzerinden HTTP'dir (Aktarım Katmanı Güvenliği). Şunları sağlar:
- **Şifreleme**: Aktarılan veriler, dinleyiciler tarafından okunamaz.
- **Kimlik Doğrulama**: Sunucu kimliğini bir sertifika aracılığıyla kanıtlar.
- **Bütünlük**: Veriler aktarım sırasında tespit edilmeden değiştirilemez.
TLS 1.2 veya 1.3'ü kullanın. TLS 1.0 ve 1.1'i devre dışı bırakın. Tarayıcıları her zaman HTTPS kullanmaya zorlamak için HSTS'yi (HTTP Sıkı Aktarım Güvenliği) etkinleştirin.
---

## Kimlik Doğrulama ve Yetkilendirme
### Kimlik Doğrulama: Sen Kimsin?
| Yöntem | Güvenlik Düzeyi | Kullanım Örneği |
|----------|---------------|----------|
| **Şifre** | Düşük-Orta | Temel hesaplar (12+ karakter kullanın, ihlalleri kontrol edin) |
| **MFA (TOTP)** | Yüksek | Hassas hesaplar için standart (Google Authenticator, Authy) |
| **Donanım anahtarı (FIDO2/WebAuthn)** | Çok Yüksek | Yüksek güvenlikli hesaplar (YubiKey) |
| **Biyometrik** | Orta–Yüksek | Cihazın kilidini açma (parmak izi, yüz) — tek faktör olarak pek iyi değil |
| **OAuth2 / OIDC** | Yüksek | Üçüncü taraf girişi ("Google ile Oturum Açın") |
**Şifre kuralları**: Minimum uzunluğu zorunlu kılın (12-16 karakter), ihlal edilen şifre listelerini kontrol edin, kullanıcı başına tuzlarla karma işlemi yapmak için Argon2id veya bcrypt kullanın.
### Yetkilendirme: Ne Yapabilirsiniz?
| Modeli | Açıklama | Örnek |
|----------|----------------|-----------|
| **RBAC** (Rol Tabanlı Erişim Kontrolü) | Rollere atanan izinler; kullanıcılar rol alır | Yönetici, Editör, Görüntüleyici |
| **ABAC** (Özellik Tabanlı) | Kullanıcı niteliklerine, kaynağa ve ortama dayalı kurallar | "Yöneticiler takımlarının isteklerini onaylayabilir" |
| **ACL** (Erişim Kontrol Listesi) | Kullanıcı/kaynak başına açık izinler | Dosya izinleri (okuma/yazma/yürütme) |
**En az ayrıcalık ilkesi**: Her kullanıcıya, hizmete ve işleme yalnızca ihtiyaç duydukları minimum erişimi verin.
### JWT (JSON Web Belirteçleri)
| Görünüş | Tavsiye |
|----------|---------------|
| **İmzalanıyor** | RS256 veya ES256 (asimetrik) tercih edilir; Yönetilen sırlarla kabul edilebilir HS256 |
| **Son kullanma tarihi** | Erişim belirteçleri için 15-60 dakika; daha uzun oturumlar için yenileme belirteçlerini kullanın |
| **Depolama** | Yalnızca HTTP çerezleri (localStorage değil — XSS'ye karşı savunmasız) |
| **Doğrulama** | Her zaman imzayı, vereni, hedef kitleyi ve son kullanma tarihini doğrulayın |
---

## OWASP İlk 10 (2021)
OWASP Top 10, web uygulaması güvenliğine yönelik standart farkındalık belgesidir. En kritik riskleri temsil eder:
| # | Risk | Ne Anlama Geliyor |
|---|------|-------------|
| 1 | **Bozuk Erişim Kontrolü** | Kullanıcılar erişmemeleri gereken kaynaklara erişebilir |
| 2 | **Şifreleme Hataları** | Hassas veriler için zayıf veya eksik şifreleme |
| 3 | **Enjeksiyon** | SQL, NoSQL, OS komutu veya LDAP enjeksiyonu |
| 4 | **Güvensiz Tasarım** | Uygulamayla düzeltilemeyen mimari kusurlar |
| 5 | **Güvenlik Yanlış Yapılandırması** | Varsayılan şifreler, açık bağlantı noktaları, ayrıntılı hata mesajları |
| 6 | **Hassas Bileşenler** | Bağımlılıklarda bilinen CVE'ler |
| 7 | **Kimlik Doğrulama Hataları** | Zayıf şifreler, yanlış oturum yönetimi |
| 8 | **Bütünlük Başarısızlıkları** | Tedarik zinciri saldırıları, imzasız güncellemeler |
| 9 | **Günlüğe Kaydetme/İzleme Arızaları** | İhlal tespiti yok |
| 10 | **SSRF** | Sunucu, dahili sistemlere istekte bulunmak için kandırıldı |
---

## Güvenli Kodlama Uygulamaları
### Giriş Doğrulaması
| Kural | Neden |
|----------|-----|
| **Beyaz liste > Kara liste** | Nelerin engellendiğini değil, nelere izin verildiğini tanımlayın |
| **Parametreli sorgular** | Kullanıcı girişini hiçbir zaman SQL'de birleştirmeyin; hazırlanmış ifadeleri veya ORM'yi kullanın |
| **HTML kodlaması** | XSS'yi önlemek için`<`,`>`,`&`,`"`,`'`kodlayın |
| **Kabuk kaçıyor** | Kullanıcı girişinden kabuk komutları oluşturmaktan kaçının;`shlex.quote()`kullanın |
| **Uzunluk sınırları** | Arabellek taşmalarını ve DoS'yi önlemek için maksimum uzunlukları uygulayın |
| **Tür kontrolü** | Tam sayıların tam sayı, booleanların boolean olduğundan emin olun |
### Yaygın Güvenlik Açıkları
| Güvenlik Açığı | Saldırı | Savunma |
|----------------|-----------|------------|
| **SQL Enjeksiyonu** |  Giriş formunda`' OR 1=1 --`| Parametreli sorgular |
| **XSS** |  Yorum alanında`<script>alert('hacked')</script>`| Çıktı kodlaması, İçerik Güvenliği Politikası |
| **CSRF** | Kullanıcının tarayıcısını yetkisiz istekte bulunması için kandırmak | CSRF belirteçleri, SameSite çerezleri |
| **Yol Geçişi** | `../../etc/passwd`dosya parametresinde | Dosya yollarını doğrulayın ve temizleyin |
| **IDOR** | Başka birinin verilerini görmek için `/user/123`'yi`/user/124`olarak değiştirin | Her istekte yetkilendirme kontrolleri |
---

## Ağ Güvenliği
### Güvenlik Duvarları
| Tür | Açıklama |
|------|-----------------|
| **Paket filtreleme** | IP, bağlantı noktası ve protokole dayalı kurallar |
| **Durum bilgisi olan** | Bağlantı durumlarını izler; daha akıllı filtreleme |
| **Uygulama düzeyinde (WAF)** | HTTP trafiğini denetler; SQL enjeksiyonunu, XSS'yi vb. engeller |
| **Bulut güvenlik grupları** | Bulut örnekleri için sanal güvenlik duvarları (AWS SG'ler, Azure NSG'ler) |
**Genel kural**: tüm gelen trafiği varsayılan olarak engelleyin; yalnızca açıkça ihtiyaç duyulanları açın (web için 80, 443).
### Ağ Segmentasyonu
Veritabanlarını ve önbellekleri doğrudan internet erişimi olmayan özel alt ağlara yerleştirin. Herkese açık hizmetler (web sunucuları, yük dengeleyiciler) için bir DMZ kullanın. Ağ erişimine en az ayrıcalık ilkesini uygulayın.
---

## Sırlar Yönetimi
### Altın Kural
**Asla sırları sabit kodla yazmayın.** Kaynak kodunda API anahtarı, şifre veya veritabanı URL'si yoktur. Git'e taahhüt edilen ortam değişkenlerinde sır yoktur. Docker görüntülerinde sır yoktur.
### Aletler
| Araç | Tür | En İyisi |
|------|----------|----------|
| **HashiCorp Kasası** | Kurumsal sırlar yöneticisi | Dinamik sırlar, hizmet olarak şifreleme |
| **AWS Sırları Yöneticisi** | Bulutta yerel | AWS ortamları |
| **Azure Anahtar Kasası** | Bulutta yerel | Azure ortamları |
| **SOPS** | Şifrelenmiş dosyalar | Git'te sırları şifreleyin (KMS veya GPG ile) |
| **Docker'ın Sırları** | Konteyner yerlisi | Docker Swarm (K8'ler için Secrets Store CSI'yi düşünün) |
| **dotenv (.env)** | Yerel kalkınma | Yalnızca geliştirme — hiçbir zaman üretimde veya taahhütte bulunulmamıştır |
### Döndürme
Sırları düzenli ve otomatik olarak döndürün. Bir sır sızdırılırsa (örneğin, halka açık bir depoya aktarılırsa), kimsenin görmediğini düşünseniz bile, onu hemen döndürün.
---

## Bağımlılık Güvenliği
Uygulamanız yalnızca en zayıf bağımlılığı kadar güvenlidir.
### Tarama Araçları
| Dil | Araçlar |
|----------|----------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Pas** | `cargo audit`|
| **Git** | `govulncheck`|
| **Genel** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Tedarik Zinciri Bütünlüğü
- Tekrarlanabilir yapılar için kilit dosyalarını (`package-lock.json`,`Cargo.lock`,`go.sum`) kullanın.
- İndirilen bağımlılıkların sağlama toplamlarını doğrulayın.
- Resmi tescilli ve doğrulanmış yayıncıları tercih edin.
- Dependabot veya Renovate aracılığıyla küçük/yama güncellemelerini otomatikleştirin.
---

## Güvenlik Geliştirme Yaşam Döngüsü (SDL)
| Aşama | Etkinlik |
|----------|----------|
| **Eğitim** | Geliştiricilerin yaygın güvenlik açıklarını anladığından emin olun |
| **Tehdit Modellemesi** | Tasarım sırasında potansiyel tehditleri belirleyin |
| **Güvenli Kodlama Standartları** | Linterler ve kod inceleme kontrol listeleri aracılığıyla zorunlu kılın |
| **SAST** | Kaynak kodunun statik analizi (SonarQube, CodeQL) |
| **DAST** | Çalışan uygulamanın dinamik analizi (OWASP ZAP, Burp Suite) |
| **SCA** | Yazılım bileşimi analizi — tarama bağımlılıkları |
| **Sızma Testi** | Düzenli etik hackleme egzersizleri |
| **Hata Ödülü** | Harici araştırmacıları güvenlik açıklarını bulmaya teşvik edin |
| **Olay Müdahale Planı** | Bir ihlalin ne zaman tespit edileceğine dair net bir planınız olsun |
---

## Acil Durum Kontrol Listesi
Bir ihlalden şüphelendiğinizde:
1. **Panik yapmayın** — ancak hızlı hareket edin.
2. **Etkilenen sistemleri izole edin** (gerekirse ağ bağlantısını kesin).
3. **Kanıtları koruyun**: günlükleri, bellek dökümlerini, disk görüntülerini yakalayın.
4. **Kapsamın belirlenmesi**: hangi sistemler, hangi veriler?
5. Güvenliği ihlal edilmiş tüm kimlik bilgilerini ve sırları **döndürün**.
6. Güvenlik açığını **yama** uygulayın.
7. Gerekirse etkilenen kullanıcıları ve düzenleyicileri **bilgilendirin** (yasal süreler dahilinde).
8. **Opsi sonrası**: Temel nedeni ve eylem öğelerini 24-48 saat içinde belgeleyin.