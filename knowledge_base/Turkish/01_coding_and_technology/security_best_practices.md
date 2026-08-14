<!--
---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
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

-->
# En İyi Güvenlik Uygulamaları
Geliştirmeden üretime kadar uygulamaları, altyapıyı ve verileri korumaya yönelik pratik bir kılavuz.
---

## OWASP İlk 10 (2021) — Genel Bakış
1. **Kötü Erişim Kontrolü**: Kullanıcılar, erişmemeleri gereken kaynaklara erişebilir.
2. **Şifreleme Hataları**: Zayıf veya eksik şifreleme.
3. **Enjeksiyon**: SQL, NoSQL, OS komutu veya LDAP enjeksiyonu.
4. **Güvensiz Tasarım**: Mimari kusurlar.
5. **Yanlış Güvenlik Yapılandırması**: Varsayılan şifreler, açık bağlantı noktaları, ayrıntılı hatalar.
6. **Hassas ve Eski Bileşenler**: Bağımlılıklarda bilinen CVE'ler.
7. **Tanımlama ve Kimlik Doğrulama Hataları**: Zayıf şifreler, yanlış oturum yönetimi.
8. **Yazılım ve Veri Bütünlüğü Arızaları**: Tedarik zinciri saldırıları, imzasız güncellemeler.
9. **Güvenlik Günlüğü Kaydı ve İzleme Hataları**: İhlal tespiti yok.
10. **Sunucu Tarafı İstek Sahteciliği (SSRF)**: Dahili sistemlere istekte bulunmak için sunucunun kötüye kullanılması.
---

## Giriş Doğrulaması ve Çıkış Kodlaması
### Doğrulama Kuralları
- **Beyaz Liste > Kara Liste**: Bilinen kötü kalıpları engellemek yerine izin verilen kalıpları (ör. e-posta için normal ifadeler) tanımlayın.
- **Uzunluk sınırları**: Arabellek taşmalarını ve DoS'yi önlemek için maksimum uzunlukları zorunlu kılın.
- **Tür kontrolü**: Tamsayıların tamsayı, booleanların boolean olduğundan emin olun.
- **İyi test edilmiş kitaplıkları kullanın**: E-posta, URL ve tarih doğrulama için standart kitaplıkları kullanın (ör. Python'da `email-validator`, Node'da `validator.js`).
### Çıkış Kodlaması
- **HTML kodlama**: XSS'yi önlemek için`<`,`>`,`&`,`"`, `'`'yi kodlayın.
- **SQL parametreleştirme**: Kullanıcı girişini hiçbir zaman SQL sorgularına birleştirmeyin. Parametreli sorgular (hazır ifadeler) veya bir ORM kullanın.
- **Kabuktan kaçış**: Kullanıcı girişinden kabuk komutları oluşturmaktan kaçının; kaçınılmazsa`shlex.quote()`veya benzerini kullanın.
---

## Kimlik Doğrulama ve Yetkilendirme
### Şifre Yönetimi
- **Karma**: Şifreleri güçlü, yavaş bir karma algoritmasıyla saklayın: **Argon2id** (tercih edilir), **bcrypt**, **scrypt** veya **PBKDF2**.
- **Tuzlama**: Kullanıcı başına benzersiz bir tuz ekleyin.
- **Minimum uzunluk**: En az 12-16 karakter zorunlu kılın.
- **MFA (Multi-Factor Authentication)**: Hassas işlemler için ikinci bir faktör (TOTP, SMS, donanım anahtarı) gerektirir.
- **Hız sınırlama**: Oturum açma uç noktalarında kaba kuvvet girişimlerini önleyin (ör. IP/kullanıcı başına 5 dakikada 5 deneme).
### Oturum Yönetimi
- Oturum belirteçleri için güvenli, yalnızca HTTP'ye yönelik SameSite çerezlerini kullanın.
- Uygun son kullanma sürelerini ayarlayın.
- Oturumu kapatma ve şifre değiştirme sırasında oturumları geçersiz kılın.
- URL'lerde oturum kimliklerini göstermekten kaçının.
### OAuth2 / OIDC
- Köklü kütüphaneleri kullanın (örn. Authlib, PyJWT, Passport.js, Spring Security).
- Kimlik belirteçlerini iyice doğrulayın (imza, veren kuruluş, hedef kitle, son kullanma tarihi).
- CSRF'yi önlemek için durum parametrelerini kullanın.
- Müşteri sırlarını gizli tutun.
### JWT (JSON Web Belirteçleri)
- **İmza**: Daha iyi güvenlik için RS256 veya ES256 (asimetrik) kullanın; Paylaşılan sırlar iyi yönetilirse HS256 (simetrik) kabul edilebilir.
- **Doğrula**: Her zaman imzayı, vereni (`iss`), hedef kitleyi (`aud`) ve son kullanma tarihini (`exp`) doğrulayın.
- **Son kullanma süresinin kısa olmasını sağlayın**: Erişim belirteçleri için 15–60 dakika; daha uzun oturumlar için yenileme belirteçlerini kullanın.
- **Güvenli bir şekilde saklayın**: JWT'leri hiçbir zaman localStorage'da saklamayın (XSS'e karşı savunmasızdır); bunun yerine yalnızca HTTP çerezlerini kullanın.
---

## API Güvenliği
### Kimlik Doğrulaması
- API çağrılarının kimliğini her zaman doğrulayın (genel uç noktalar hariç).
- Temel kimlik doğrulama (her istekte kimlik bilgilerini gönderen) yerine API anahtarlarını veya OAuth2 belirteçlerini tercih edin.
### Hız Sınırlama ve Azaltma
- Kötüye kullanımı ve DoS'yi önlemek için kullanıcı başına ve IP başına hız sınırları uygulayın.
-`Retry-After`başlığıyla `429 Too Many Requests`'yi döndürün.
### CORS (Çapraz Kökenli Kaynak Paylaşımı)
- Yalnızca belirli kaynaklara izin verin (üretimde asla`*`kullanmayın).
- Sunucu tarafında`Origin`başlığını doğrulayın.
### Giriş Doğrulaması
- Başlıklar ve gövde dahil tüm istek parametrelerini doğrulayın.
- Beklenmeyen alanları reddedin (JSON Şemasında`"strict": true`veya `additionalProperties: false`).
### HTTPS / TLS
- Üretimde HTTPS'yi zorunlu kılın.
- Tarayıcıları HTTPS kullanmaya zorlamak için HSTS'yi (HTTP Sıkı Aktarım Güvenliği) kullanın.
- TLS 1.2 veya 1.3 kullanın (TLS 1.0/1.1'i devre dışı bırakın).
---

## Sırlar Yönetimi
### Asla Sırları Sabit Kodlama
- Kaynak kontrolüne sırlar (API anahtarları, şifreler, veritabanı URL'leri) vermeyin.
- Ortam değişkenlerini veya gizli yönetim araçlarını kullanın.
### Aletler
| Araç | Açıklama |
|------|-----------------|
| **HashiCorp Kasası** | Kurumsal düzeyde, dinamik sırlar |
| **AWS Secrets Manager / Azure Key Vault / GCP Secrets Manager** | Bulutta yerel |
| **SOPS** | Dosyalardaki sırları şifreleyin ve kaydedin (KMS veya GPG ile) |
| **Docker'ın sırları** | Swarm modu için; Kubernetes sırları (harici Secrets Store CSI sürücüsünü düşünün) |
### Döndürme
- Sırları ve hizmet hesaplarını düzenli olarak değiştirin.
- Mümkün olduğunda döndürmeyi otomatikleştirin.
---

## Bağımlılık Yönetimi
### Güvenlik Açığı Taraması
| Dil/Platform | Araçlar |
|---------------------|----------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Düğüm** | `npm audit`,`yarn audit`,`snyk`|
| **Pas** | `cargo audit`|
| **Git** | `govulncheck`|
| **Genel** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Yamalama
- Bağımlılıkları yamalı sürümlere güncel tutun.
- Küçük/yama güncellemeleri için otomatik çekme isteklerini ayarlayın.
- Değişiklikleri bozmak için değişiklik günlüklerini inceleyin.
### Tedarik Zinciri Bütünlüğü
- Tekrarlanabilir yapılar sağlamak için paket kilit dosyalarını (`package-lock.json`,`Cargo.lock`,`go.sum`) kullanın.
- İndirilen bağımlılıkların sağlama toplamlarını doğrulayın.
- Resmi kayıtları tercih edin ve yalnızca doğrulanmış yayıncılara güvenin.
---

## Altyapı Güvenliği
### Güvenlik Duvarları
- Açıkça ihtiyaç duyulanlar (ör. 80, 443) dışındaki tüm gelen bağlantı noktalarını engelleyin.
- SSH erişimini belirli IP aralıklarıyla sınırlandırın (veya bir VPN/bastion ana bilgisayarı kullanın).
- Ayrıntılı denetim için güvenlik gruplarını (AWS) veya NSG'leri (Azure) kullanın.
### İşletim Sistemi Sağlamlaştırma
- Güvenlik güncellemelerini düzenli olarak uygulayın (`sudo apt upgrade`,`yum update`).
- Gereksiz hizmetleri ve varsayılan hesapları devre dışı bırakın.
- SSH'deki kaba kuvvet girişimlerini engellemek için fail2ban'ı kullanın.
- SSH'yi güçlendirin: kök oturum açmayı devre dışı bırakın, anahtar tabanlı kimlik doğrulamayı kullanın, varsayılan bağlantı noktasını değiştirin (isteğe bağlı).
### Ağ Segmentasyonu
- Veritabanlarını ve önbellekleri internet erişimi olmayan özel alt ağlara yerleştirin.
- Halka açık hizmetler için DMZ kullanın.
- Ağ erişimine en az ayrıcalık ilkesini uygulayın.
### Altyapıdaki Sırlar
- Şifrelenmedikçe sırları asla CI/CD ortam değişkenlerinde saklamayın.
- EC2/VM örnekleri için uzun ömürlü anahtarlar yerine bulut sağlayıcının IAM rollerini kullanın.
---

## Günlük Kaydı ve İzleme
### Neler Günlüğe Kaydedilir
- Kimlik doğrulama olayları (başarılı/başarısız).
- Erişim kontrolü kararları (yetkilendirme hataları).
- Yönetici eylemleri (kullanıcı oluşturma, silme, izin değişiklikleri).
- Veritabanı şeması değişiklikleri.
- Sistem hataları ve istisnalar.
- API istekleri ve yanıtları (hassas verileri çıkarın).
### Neleri Günlüğe Kaydetmemelisiniz
- Karma hale getirilmediği/düzenlenmediği sürece şifreler, sırlar, jetonlar, PII (Kişisel Tanımlanabilir Bilgiler).
- Tam kredi kartı numaraları.
### Uyarı
- Aşağıdakiler için uyarılar ayarlayın:
  - Birden fazla başarısız oturum açma (olası kaba kuvvet).
  - Olağandışı erişim modelleri (örneğin yeni konumlardan, tuhaf saatlerde).
  - Yeni yönetici hesapları oluşturuldu.
  - Yüksek hata oranları veya gecikme artışları.
- Gelişmiş korelasyon için SIEM (Güvenlik Bilgileri ve Olay Yönetimi) kullanın.
### Günlük Tutma
- Yasal gerekliliklere bağlı olarak günlükleri en az 30–90 gün saklayın.
- Günlükleri merkezi, kurcalanmaya karşı korumalı bir sistemde saklayın (ör. ELK Stack, Splunk, Datadog).
---

## Güvenli Geliştirme Yaşam Döngüsü (SDL)
1. **Eğitim**: Geliştiricilerin yaygın güvenlik açıklarını anladığından emin olun.
2. **Tehdit modelleme**: Potansiyel tehditleri tasarımın erken safhalarında belirleyin.
3. **Güvenli kodlama standartları**: Linterler ve kod inceleme kontrol listeleri aracılığıyla zorunlu kılın.
4. **SAST** (Statik Uygulama Güvenliği Testi): Kaynak kodunu güvenlik açıklarına karşı tarayın (SonarQube, CodeQL).
5. **DAST** (Dinamik Uygulama Güvenliği Testi): Çalışan uygulamaları tarayın (OWASP ZAP, Burp Suite).
6. **SCA** (Yazılım Bileşimi Analizi): Tarama bağımlılıkları.
7. **Sızma testi**: Düzenli etik hackleme egzersizleri.
8. **Hata ödülü**: Harici araştırmacıları güvenlik açıklarını sorumlu bir şekilde bulmaya teşvik edin.
9. **Olay müdahale planı**: Bir ihlalin ne zaman tespit edileceğine dair net bir planınız olsun.
---

## Acil Durum Kontrol Listesi (Bir İhlalden Şüphelenildiğinde)
1. **Panik yapmayın** — ancak hızlı hareket edin.
2. Etkilenen sistemleri **izole edin** (gerekirse ağ bağlantısını kesin).
3. **Kanıtları koruyun**: Günlükleri, bellek dökümlerini ve disk görüntülerini yakalayın.
4. **Kapsamını belirleyin**: hangi sistemler, hangi veriler.
5. Güvenliği ihlal edilen tüm kimlik bilgilerini ve sırları **döndürün**.
6. Güvenlik açığını **yama** uygulayın.
7. Gerekirse etkilenen kullanıcıları ve düzenleyici kurumları **bilgilendirin** (yasal süreler içinde).
8. **Temel nedeni anlamak ve süreçleri iyileştirmek için bir otopsi yapın**.