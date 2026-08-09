---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teknoloji ve Bilgisayar
Bilgisayar her yerde; telefonunuzda, arabanızda, buzdolabınızda, tıbbi cihazlarınızda ve modern toplumu yöneten altyapıda. Her şeyin nasıl çalıştığını anlamaktan yararlanmak için programcı olmanıza gerek yok. Bu dosya temel bilgileri kapsar: bilgisayar nedir, internet nasıl çalışır, yazılım nasıl oluşturulur ve dijital dünyayı şekillendiren kavramlar.
> **Daha derine inmek mi istiyorsunuz?** Bu dosya geniş bir genel bakıştır. Herhangi bir konunun ayrıntılı kapsamı için, [web development](../01_coding_and_technology/web_development.md), [database systems](../01_coding_and_technology/database_systems.md), [cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)ve[security](../01_coding_and_technology/security_best_practices.md)dahil olmak üzere [`01_coding_and_technology/`](../01_coding_and_technology/)'deki özel dosyalara bakın.
---

## Bilgisayar Nedir?
Özünde, akıllı telefondan süper bilgisayara kadar her bilgisayar aynı şeyi yapar: girdiyi alır, onu talimatlara (bir programa) göre işler ve çıktı üretir. Sihir hız ve ölçektedir.
### Von Neumann Mimarisi
Hemen hemen tüm modern bilgisayarlar bu temel tasarımı izler:
| Bileşen | Ne İşe Yarar | Analoji |
|-----------|----------------|-----------|
| **CPU** (Merkezi İşlem Birimi) | Talimatları yürütür; "beyin" | Şef tarifi takip ediyor |
| **RAM** (Bellek) | CPU'nun aktif olarak kullandığı verileri depolar; güç kapatıldığında kayboluyor | Tezgah — hızlı erişim, sınırlı alan |
| **Depolama** (SSD/HDD) | Verileri kalıcı olarak saklar | Kiler — daha yavaş erişim, çok daha fazla alan |
| **Giriş/Çıkış** | Klavye, fare, ekran, ağ | Şef siparişleri nasıl alır ve yiyecekleri nasıl teslim eder?
| **GPU** (Grafik İşleme Birimi) | Paralel görevler için özel işlemci (grafik, yapay zeka) | Hepsi aynı görevi aynı anda yapan asistanlardan oluşan bir ekip |
**Önemli bilgi**: RAM hızlıdır ancak geçicidir. Depolama yavaş ama kalıcıdır. Bilgisayarınız "yavaş hissettiğinde" bunun nedeni genellikle RAM'in bitmesi ve depolamayı geçici bellek (değiştirme) olarak kullanmak zorunda olmasıdır; bu da çok daha yavaştır.
---

## Programlama Dilleri — Bilgisayarlarla Konuşmak
Programlama dili, bir bilgisayarın yürütebileceği bir dizi talimattır. Farklı diller farklı amaçlar için tasarlanmıştır. 34 ayrı dilin ayrıntılı kapsamı için[`programming_languages/`](../01_coding_and_technology/programming_languages/)klasörüne bakın.
| Dil | En İyisi | Neden Onu Seçmelisiniz |
|----------|------------|---------------|
| **Python** | Veri bilimi, yapay zeka, otomasyon, web arka uçları | Basit sözdizimi; devasa ekosistem; yeni başlayanlar için harika |
| **JavaScript** | Web ön uçları, tam yığın (Node.js) | Her tarayıcıda çalışır; web geliştirme için gerekli |
| **Java** | Kurumsal yazılım, Android uygulamaları | Platformdan bağımsız (JVM); büyük ekosistem |
| **C/C++** | Sistem programlama, oyunlar, gömülü | Maksimum performans; doğrudan donanım kontrolü |
| **Pas** | Güvenlik garantili sistem programlama | Çöp toplamaya gerek kalmadan hafıza güvenliği |
| **Git** | Bulut hizmetleri, mikro hizmetler, CLI araçları | Basit; mükemmel eşzamanlılık; hızlı derleme |
| **SQL** | Veritabanı sorguları | Verilerle çalışmak için evrensel dil |
| **TypeScript** | Büyük ölçekli web uygulamaları | Tür denetimli JavaScript; böcekleri erken yakalar |
---

## İnternet Nasıl Çalışır?
İnternet, web ile aynı şey değildir. İnternet, milyarlarca cihazı birbirine bağlayan kablolar, yönlendiriciler, sunucular ve protokollerden oluşan fiziksel bir ağdır. World Wide Web, internette çalışan bir hizmettir (e-posta, dosya aktarımı, akış, oyun vb. ile birlikte).
### Bir Web İsteğinin Yolculuğu
Tarayıcınıza`https://www.example.com`yazdığınızda:
1. **DNS araması**: Tarayıcınız bir DNS sunucusundan "www.example.com" adresini bir IP adresine (93.184.216.34 gibi) çevirmesini ister.
2. **TCP bağlantısı**: Cihazınız, TCP'yi (güvenilir teslimatı garanti eden bir protokol) kullanarak bu IP adresiyle bağlantı kurar.
3. **TLS anlaşması**: HTTPS kullanıyorsanız, tarayıcınız ve sunucunuz şifreli bir bağlantı kurar.
4. **HTTP isteği**: Tarayıcınız bir istek gönderir: "Bana /index.html adresindeki sayfayı ver."
5. **Sunucu işleme**: Web sunucusu sayfayı bulur, muhtemelen bir veritabanını sorgular ve bir yanıt hazırlar.
6. **HTTP yanıtı**: Sunucu HTML, CSS ve JavaScript'i geri gönderir.
7. **Oluşturma**: Tarayıcınız HTML'yi ayrıştırır, CSS stillerini uygular ve sayfayı görüntülemek için JavaScript'i çalıştırır.
Bu sürecin tamamı genellikle bir saniyeden az sürer.
### Anahtar Protokoller
| Protokol | Ne İşe Yarar | Katman |
|----------|----------------|-------|
| **IP** (İnternet Protokolü) | Paketleri ağlar arasında yönlendirir | Ağ |
| **TCP** | Güvenilir, düzenli teslimat (kayıp paketleri yeniden iletir) | Taşıma |
| **UDP** | Hızlı, güvenilmez teslimat (yeniden iletim yok) | Taşıma |
| **HTTP/HTTPS** | Web sayfası aktarımı (HTTPS şifreleme ekler) | Başvuru |
| **DNS** | Alan adlarını IP adreslerine çevirir | Başvuru |
| **SSH** | Bilgisayarlara güvenli uzaktan erişim | Başvuru |
| **SMTP/IMAP** | E-posta gönderme ve alma | Başvuru |
---

## Yazılım Geliştirme — Programlar Nasıl Oluşturulur?
### Geliştirme Süreci
1. **Kod yazın**: Geliştiriciler talimatları bir programlama dilinde yazar.
2. **Test kodu**: Doğru çalıştığını doğrulamak için kodu çalıştırın.
3. **Sürüm kontrolü**: Evrensel standart olan Git'i kullanarak değişiklikleri izleyin.
4. **İnceleme**: Diğer geliştiriciler kodda hatalar ve kalite olup olmadığını kontrol eder.
5. **Derleme**: Kaynak kodunu çalıştırılabilir bir programa (derleme) dönüştürün.
6. **Dağıt**: Programı kullanıcılara (sunucular, uygulama mağazaları vb.) yayınlayın.
7. **İzleyici**: Üretimdeki hataları ve performans sorunlarını izleyin.
### Temel Kavramlar
| Konsept | Ne Anlama Geliyor | Neden Önemlidir |
|-----------|---------------|----------------|
| **Sürüm kontrolü (Git)** | Zaman içinde kodda yapılan her değişikliği izleyin | İşbirliği; hataları geri alma yeteneği |
| **API** (Uygulama Programlama Arayüzü) | Yazılım bileşenlerinin iletişim kurmasının tanımlanmış bir yolu | Farklı sistemlerin birlikte çalışmasına olanak tanır |
| **Veritabanı** | Veriler için organize depolama | Her uygulamanın verileri depolaması ve alması gerekir |
| **Test etme** | Kodun düzgün çalışıp çalışmadığını otomatik olarak kontrol eder | Hataların kullanıcılara ulaşmasını engeller |
| **CI/CD** (Sürekli Entegrasyon/Teslim) | Kod taahhüdünden üretime kadar otomatik boru hattı | Daha hızlı, daha güvenli sürümler |
| **Konteynerleştirme (Docker)** | Bir uygulamayı tüm bağımlılıklarıyla birlikte paketleme | "Makinemde çalışıyor", "her yerde çalışıyor" olur |
---

## Veritabanları — Verilerin Yaşadığı Yer
Her uygulamanın veri depolaması gerekir. Veritabanları bunu verimli ve güvenilir bir şekilde yapan sistemlerdir.
| Tür | Veriler Nasıl Saklanıyor | En İyisi | Örnekler |
|----------|-----------|----------|-----------|
| **İlişkisel (SQL)** | Satır ve sütunlu tablolar; katı şema | Yapılandırılmış veriler; karmaşık sorgular; işlemler | PostgreSQL, MySQL, SQLite |
| **Belge (NoSQL)** | JSON benzeri belgeler; esnek şema | Yarı yapılandırılmış veriler; hızlı yineleme | MongoDB, CouchDB |
| **Anahtar/değer çifti** | Basit anahtar → değer çiftleri | Önbelleğe alma; oturum depolama; hızlı aramalar | Redis, DynamoDB |
| **Grafik** | Düğümler ve kenarlar (ilişkiler) | Sosyal ağlar; öneri motorları | Neo4j, JanusGraph |
| **Zaman serisi** | Zaman damgalı veriler için optimize edildi | İzleme; analitik; Nesnelerin İnterneti | InfluxDB, TimescaleDB |
**SQL** (Yapılandırılmış Sorgu Dili), ilişkisel veritabanları için standart dildir. Öğrenebileceğiniz en değerli teknik becerilerden biridir; hemen hemen her kuruluş veritabanlarını kullanır ve SQL, onlarla konuşma şeklinizdir.
---

## İşletim Sistemleri
İşletim sistemi (OS), siz (ve programlarınız) ile donanım arasındaki yazılım katmanıdır. Belleği, işlemleri, dosyaları ve cihazları yönetir.
| İşletim Sistemi | Hakim Olduğu Yer | Temel Özellik |
|----|---------|-------------|
| **Pencereler** | Masaüstü/dizüstü bilgisayarlar (~%72 pazar payı) | En geniş yazılım/donanım uyumluluğu |
| **macOS** | Yaratıcı profesyoneller, geliştiriciler | Unix tabanlı; cilalanmış kullanıcı arayüzü; Apple ekosistemi |
| **Linux** | Sunucular (~%96), süper bilgisayarlar (%100), yerleşik, geliştiriciler | Açık kaynak; özgür; son derece özelleştirilebilir |
| **Android** | Mobil (~%72 küresel pazar payı) | Linux çekirdeğine dayalı; açık kaynak |
| **iOS** | Mobil (~%27 küresel, ancak daha yüksek gelir) | Kapalı ekosistem; cilalı; gizlilik odaklı |
Linux özel olarak anılmayı hak ediyor: İnternetin çoğuna, en iyi 500 süper bilgisayarın tümüne, bulut altyapısının çoğuna ve tüm Android telefonlara güç veriyor. Ücretsizdir, açık kaynaktır ve küresel bir topluluk tarafından korunur.
---

## Bulut Bilişim
Bulut bilişim, kendi donanımınızı satın almak ve bakımını yapmak yerine, internet üzerinden bilgi işlem kaynaklarının (sunucu, depolama, veritabanları vb.) kiralanması anlamına gelir. Bulut mimarisi, hizmet modelleri ve sağlayıcı karşılaştırmalarına ilişkin kapsamlı bir kılavuz için bkz. [cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Hizmet Modeli | Ne Alırsınız | Analoji | Örnekler |
|---------------|------------|------------|------------|
| **IaaS** (Altyapı) | Sanal sunucular, depolama, ağ iletişimi | Bir arsa kiralamak ve istediğinizi inşa etmek | AWS EC2, Google Hesaplama Motoru |
| **PaaS** (Platform) | Çalışma zamanı ortamı; kodu getiriyorsun | Mobilyalı bir daire kiralamak | Heroku, Google Uygulama Motoru |
| **SaaS** (Yazılım) | Başvuruyu tamamlayın; sadece onu kullan | Otelde kalmak | Gmail, Slack, Salesforce |
Üç büyük bulut sağlayıcısı **AWS** (Amazon, ~%32 pazar payı), **Azure** (Microsoft, ~%23) ve **GCP**'dir (Google, ~%10). Bilgi işlem, depolama, veritabanları, yapay zeka, ağ iletişimi ve daha fazlasını kapsayan yüzlerce hizmet sunarlar.
---

## Siber Güvenlik — Dijital Sistemleri Korumak
Siber güvenlik, bilgisayarları, ağları ve verileri saldırılara karşı koruma uygulamasıdır. Bu önemlidir çünkü her şey birbiriyle bağlantılıdır ve ihlallerin maliyeti çok büyüktür. OWASP Top 10, güvenli geliştirme yaşam döngüsü ve gizli dizi yönetimini kapsayan tam bir kılavuz için bkz. [security best practices](../01_coding_and_technology/security_best_practices.md).
### Yaygın Tehditler
| Tehdit | Nedir | Önleme |
|----------|---------------|-----------|
| **Kötü amaçlı yazılım** | Kötü amaçlı yazılımlar (virüsler, solucanlar, truva atları) | Antivirüs; yazılımı güncel tutun |
| **Kimlik avı** | Bilgiyi açıklamanız için sizi kandıran sahte e-postalar/mesajlar | Eğitim; e-posta filtreleme; şüphecilik |
| **Fidye yazılımı** | Verilerinizi şifreler; anahtar için ödeme talep ediyor | Yedeklemeler; yama sistemleri; ödeme yapma |
| **DDoS** | Bir hizmetin trafiğini bunaltıyor | Trafik filtreleme; CDN koruması |
| **SQL enjeksiyonu** | Giriş alanlarına kötü amaçlı SQL ekleme | Parametreli sorgular; giriş doğrulama |
| **Ortadaki Adam** | İki taraf arasındaki iletişimin kesilmesi | HTTPS/TLS şifrelemesi |
### Güvenlik Temelleri
- **Şifreleme**: Verileri yalnızca yetkili tarafların okuyabileceği şekilde karıştırın. HTTPS, web trafiğini şifrelemek için TLS'yi kullanır.
- **Kimlik doğrulama**: Kimliği doğrulayın. Çok faktörlü kimlik doğrulama (MFA) kullanın - şifre + başka bir şey (kod, biyometrik).
- **Yetkilendirme**: İzinleri doğrulayın. Oturum açmış olmanız her şeye erişmeniz gerektiği anlamına gelmez.
- **En az ayrıcalık ilkesi**: Kullanıcılara ve sistemlere yalnızca ihtiyaç duydukları erişimi verin, daha fazlasını değil.
- **Yama yönetimi**: Yazılımı güncel tutun. Çoğu ihlal, zaten yamaları olan bilinen güvenlik açıklarından yararlanır.
---

## Veri Formatları
Programlar belirli formatlarda veri alışverişinde bulunur. En yaygın olanı:
| Biçim | Yapı | Ne İçin Kullanılır |
|----------|---------------|----------|
| **JSON** | Anahtar-değer çiftleri; insan tarafından okunabilir | API'ler; konfigürasyon; veri alışverişi |
| **XML** | Etiket tabanlı; ayrıntılı ama esnek | Eski sistemler; belgeler; SABUN API'leri |
| **YAML** | Girinti tabanlı; çok okunabilir | Yapılandırma (Docker, Kubernetes, CI/CD) |
| **CSV** | Düz metin satırları ve sütunları | Veri içe/dışa aktarma; elektronik tablolar |
---

## Özet
Bilgisayar sihir değil, mühendisliktir. Bilgisayarlar talimatları inanılmaz bir hızla takip eder. İnternet, milyarlarcasını standartlaştırılmış protokoller kullanarak birbirine bağlar. Yazılım, yinelenen döngüler halinde kod yazan, test eden ve dağıtan kişilerden oluşan ekipler tarafından oluşturulur. Veritabanları verileri saklar ve alır. Bulut bilişim, herkesin talep üzerine büyük bilgi işlem kaynaklarına erişmesine olanak tanır. Ve siber güvenlik, tüm bunları istismar etmek isteyen insanlardan korumak için devam eden bir mücadeledir. Bu temelleri anlamak, ister kullanıcı, ister geliştirici, ister yalnızca modern yaşamı şekillendiren teknolojiyi anlamlandırmaya çalışan biri olun, dijital dünyada gezinmenize yardımcı olur.