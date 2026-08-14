---
# Metadata
title: "Web Development"
description: "Frontend, backend, DevOps, security"
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
tags: [web, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Web Geliştirme
## Ön Uç Geliştirme
### Temel Teknolojiler
#### HTML (Köprü Metni İşaretleme Dili)
- **Semantik HTML**: Anlamlı etiketler kullanma (`<header>`,`<nav>`,`<main>`,`<article>`,`<section>`,`<aside>`,`<footer>`)
- **Formlar**: Giriş türleri, doğrulama, erişilebilirlik etiketleri
- **Medya**: Resimler, video, ses yerleştirme
- **Meta Etiketler**: SEO, görünüm, karakter kodlaması
- **HTML5 Özellikleri**: Kanvas, SVG, yerel depolama, coğrafi konum, web soketleri
#### CSS (Basamaklı Stil Sayfaları)
- **Kutu Modeli**: İçerik, dolgu, kenarlık, kenar boşluğu
- **Yerleşim Sistemleri**:
  - **Flexbox**: Tek boyutlu düzenler, içeriği iki yana yaslama, öğeleri hizalama
  - **Izgara**: İki boyutlu düzenler, ızgara şablonu, ızgara alanı
  - **Konumlandırma**: Statik, göreceli, mutlak, sabit, yapışkan
- **Duyarlı Tasarım**: Medya sorguları, mobil öncelikli yaklaşım
- **CSS Değişkenleri**: Temaya yönelik özel özellikler
- **Animasyonlar**: Geçişler, ana kareler, dönüşümler
- **Önişlemciler**: Sass, Less (değişkenler, karışımlar, yuvalama)
#### JavaScript
- **DOM Manipülasyonu**: Öğeleri seçme, oluşturma, değiştirme
- **Etkinlikler**: Tıklama, gönderme, klavye, özel etkinlikler, etkinlik delegasyonu
- **ES6+ Özellikleri**: Ok işlevleri, yok etme, yayma/dinlenme, modüller, eşzamansız/bekleme
- **API'ler**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Statik yazma, arayüzler, jenerikler, dekoratörler
### Modern Ön Uç Çerçeveleri
#### Tepki ver
- **Bileşenler**: İşlevsel bileşenler, sınıf bileşenleri
- **Kancalar**: useState, useEffect, useContext, useReducer, özel kancalar
- **Durum Yönetimi**: Bağlam API'si, Redux, Zustand, Geri Tepme
- **Yönlendirme**: React Router (BrowserRouter, Routes, Route, Link)
- **Ekosistem**: Next.js (SSR, SSG), Remix, Gatsby
- **Sanal DOM**: Farklılaştırma algoritması aracılığıyla verimli oluşturma
#### Vue.js
- **Seçenekler API**: veriler, yöntemler, hesaplanan, izleme
- **Composition API**: setup(), ref, reaktif, bilgisayarlı
- **Direktifler**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Devlet yönetimi
- **Vue Router**: İstemci tarafı yönlendirme
- **Nuxt.js**: Sunucu tarafı oluşturma çerçevesi
#### Açısal
- **Bileşenler**: Dekoratörler, şablonlar, yaşam döngüsü kancaları
- **Hizmetler**: Bağımlılık ekleme, tekil model
- **RxJS**: Reaktif programlama, gözlemlenebilirler
- **Yönlendirme**: RouterModule, korumalar, çözümleyiciler
- **Formlar**: Şablona dayalı, reaktif formlar
- **NgRx**: Redux tarzı durum yönetimi
### Araçlar ve Paketleyiciler Oluşturun
- **Webpack**: Modül birleştirme, kod bölme, yükleyiciler, eklentiler
- **Vite**: Yerel ES modüllerini kullanan hızlı oluşturma aracı
- **Parsel**: Sıfır konfigürasyonlu paketleyici
- **Toplama**: Kitaplıklar için optimize edildi
- **esbuild**: Son derece hızlı JavaScript paketleyicisi
- **Babel**: Geriye dönük uyumluluk için JavaScript aktarıcısı
- **PostCSS**: Eklentilerle CSS işleme
### CSS Çerçeveleri ve Kitaplıkları
- **Bootstrap**: Bileşen kitaplığı, ızgara sistemi, yardımcı programlar
- **Tailwind CSS**: Yardımcı program öncelikli CSS çerçevesi
- **Materyal Kullanıcı Arayüzü**: Google'ın Materyal Tasarımı uygulaması
- **Chakra UI**: Erişilebilir bileşen kitaplığı
- **Karınca Tasarımı**: Kurumsal düzeyde kullanıcı arayüzü bileşenleri
- **Stil Bileşenleri**: JS'de CSS kitaplığı
- **Duygu**: Kaynak haritalarıyla JS'de CSS
## Arka Uç Geliştirme
### Sunucu Tarafı Dilleri
#### Node.js
- **Çalışma zamanı**: Sunucudaki JavaScript (V8 motoru)
- **Express.js**: Minimal web çerçevesi, ara yazılım mimarisi
- **NestJS**: Angular'dan ilham alan mimari, TypeScript
- **Fastify**: Yüksek performanslı çerçeve
- **Koa**: Aynı yaratıcılardan Modern Express
- **Paket Yönetimi**: npm, iplik, pnpm
#### Python
- **Django**: Tam özellikli çerçeve, ORM, yönetici paneli, piller dahil
- **Flask**: Mikro çerçeve, uzantı ekosistemi
- **FastAPI**: Modern, eşzamansız, otomatik API belgeleri
- **Piramit**: Esnek, ölçeklenebilir çerçeve
#### Diğer Arka Uç Dilleri
- **Ruby on Rails**: Yapılandırmaya ilişkin kural, ActiveRecord ORM
- **Java Spring**: Kurumsal çerçeve, bağımlılık ekleme
- **PHP Laravel**: Zarif sözdizimi, Anlamlı ORM, Blade şablonlaması
- **Go Gin**: Yüksek performans, minimum çerçeve
- **Rust Actix**: Bellek güvenliği, performans
- **C# ASP.NET Core**: Platformlar arası, kurumsal özellikler
### Veritabanı Entegrasyonu
#### ORM'ler (Nesne-İlişkisel Haritalama)
- **Sequelize**: SQL veritabanları için Node.js ORM
- **Prisma**: Tür açısından güvenli veritabanı erişimi, otomatik olarak oluşturulan istemci
- **SQLAlchemy**: Python SQL araç seti ve ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hazırda Bekletme**: Java ORM
- **Varlık Çerçevesi**: .NET ORM
#### Veritabanı Sürücüleri
- **pg**: Node.js için PostgreSQL istemcisi
- **mysql2**: vaatleri olan MySQL istemcisi
- **pymongo**: Python için MongoDB sürücüsü
- **redis**: Birden fazla dil için Redis istemcisi
### API Geliştirme
#### REST API'leri
- **HTTP Yöntemleri**: GET, POST, PUT, PATCH, DELETE
- **Durum Kodları**: 200, 201, 400, 401, 403, 404, 500
- **Kaynak Adlandırma**: İsimler, çoğul, hiyerarşik
- **Sürüm oluşturma**: URL yolu, başlıklar, sorgu parametreleri
- **Kimlik doğrulama**: JWT, OAuth, API anahtarları
- **Belgeler**: OpenAPI/Swagger, Postacı
#### GraphQL
- **Şema Tanımı**: Türler, sorgular, mutasyonlar, abonelikler
- **Çözümleyiciler**: Alan düzeyinde veri getirme
- **Apollo Sunucusu**: GraphQL sunucu uygulaması
- **Relay**: Facebook'un GraphQL istemcisi
- **Avantajları**: Aşırı yükleme yok, tek uç nokta, güçlü yazma
#### gRPC
- **Protokol Tamponları**: Arayüz tanımlama dili
- **HTTP/2**: Çift yönlü akış
- **Kullanım Örnekleri**: Mikro hizmet iletişimi, gerçek zamanlı uygulamalar
### Kimlik Doğrulama ve Yetkilendirme
- **Oturum bazlı**: Çerezler, sunucu tarafı oturumları
- **Belirteç tabanlı**: JWT (JSON Web Belirteçleri), durum bilgisi olmayan
- **OAuth 2.0**: Yetkilendirme çerçevesi, üçüncü taraf girişi
- **OpenID Connect**: OAuth 2.0'daki kimlik katmanı
- **SAML**: Kurumsal tek oturum açma
- **Şifre Karmalama**: bcrypt, argon2, scrypt
- **Çok Faktörlü Kimlik Doğrulama**: TOTP, SMS, e-posta kodları
## DevOps ve Dağıtım
### Sürüm Kontrolü
- **Git**: Dağıtılmış sürüm kontrolü
- **GitHub/GitLab/Bitbucket**: Depo barındırma
- **Dallanma Stratejileri**: Git Flow, GitHub Flow, trunk tabanlı geliştirme
- **CI/CD**: Otomatik test ve dağıtım ardışık düzenleri
### Konteynerizasyon
- **Docker**: Konteyner çalışma zamanı, Dockerfile, görüntüler
- **Docker Compose**: Çoklu kapsayıcı orkestrasyonu
- **Konteyner Kayıtları**: Docker Hub, AWS ECR, Google GCR
- **En İyi Uygulamalar**: Çok aşamalı derlemeler, minimum düzeyde temel görüntü
### Düzenleme
- **Kubernetes**: Konteyner düzenlemesi, bölmeler, hizmetler, dağıtımlar
- **Dümen**: Kubernetes paket yöneticisi
- **Hizmet Ağı**: Mikro hizmet ağı için Istio, Linkerd
### Bulut Platformları
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Sanal Makineler, Blob Depolama, İşlevler, AKS
- **Vercel**: Ön uç dağıtımı, sunucusuz işlevler
- **Netlify**: Statik site barındırma, sunucusuz işlevler
- **Heroku**: Hizmet Olarak Platform (PaaS)
- **DigitalOcean**: Basitleştirilmiş bulut altyapısı
### CI/CD İşlem Hatları
- **GitHub Eylemleri**: İş akışı otomasyonu
- **GitLab CI**: Yerleşik sürekli entegrasyon
- **Jenkins**: Genişletilebilir otomasyon sunucusu
- **CircleCI**: Bulut tabanlı CI/CD
- **Travis CI**: Sürekli entegrasyon hizmeti
- **ArgoCD**: Kubernetes için GitOps'un sürekli teslimi
### İzleme ve Günlük Kaydı
- **Uygulama Performansı**: Yeni Relic, Datadog, AppDynamics
- **Hata Takibi**: Sentry, Rollbar, Bugsnag
- **Günlüğe kaydetme**: ELK Yığını (Elasticsearch, Logstash, Kibana), Splunk
- **Çalışma Süresi İzleme**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Genlik
## Web Performansı
### Optimizasyon Teknikleri
- **Kod Bölme**: Geç yükleme, dinamik içe aktarma
- **Ağaç Sallama**: Kullanılmayan kodu kaldırma
- **Küçültme**: Dosya boyutlarının küçültülmesi
- **Sıkıştırma**: Gzip, Brotli
- **Önbelleğe alma**: Tarayıcı önbelleği, CDN, hizmet çalışanları
- **Görüntü Optimizasyonu**: WebP, AVIF, geç yükleme, duyarlı görüntüler
- **Kritik CSS**: Ekranın üst kısmındaki stilleri satır içi oluşturma
- **Veritabanı Optimizasyonu**: Dizin oluşturma, sorgu optimizasyonu, bağlantı havuzu oluşturma
### Önemli Web Verileri
- **LCP (En Büyük İçerikli Boya)**: Yükleme performansı (<2,5s)
- **FID (İlk Giriş Gecikmesi)**: Etkileşim (<100 ms)
- **CLS (Kümülatif Düzen Kayması)**: Görsel stabilite (<0,1)
- **INP (Sonraki Boyayla Etkileşim)**: Yanıt verme metriği
### İçerik Dağıtım Ağları (CDN'ler)
- **Cloudflare**: Güvenlik, performans, DNS
- **Akamai**: Kurumsal CDN
- **Amazon CloudFront**: AWS CDN
- **Hızlı**: Uç bulut platformu
- **StackPath**: Uç hizmetler
## Web Güvenliği
### Yaygın Güvenlik Açıkları (OWASP İlk 10)
- **Enjeksiyon**: SQL enjeksiyonu, komut enjeksiyonu
- **Bozuk Kimlik Doğrulama**: Oturumun ele geçirilmesi, kimlik bilgilerinin doldurulması
- **Hassas Verilerin Açığa Çıkması**: Şifrelenmemiş veriler, zayıf şifreleme
- **XML Harici Varlıklar (XXE)**: XML ayrıştırıcıdaki güvenlik açıkları
- **Kötü Erişim Kontrolü**: Ayrıcalık artışı, yetkisiz erişim
- **Yanlış Güvenlik Yapılandırması**: Varsayılan kimlik bilgileri, ayrıntılı hatalar
- **Siteler Arası Komut Dosyası Çalıştırma (XSS)**: Yansıtılmış, depolanmış, DOM tabanlı
- **Güvensiz Seriden Çıkarma**: Nesne yerleştirme saldırıları
- **Bilinen Güvenlik Açıklarına Sahip Bileşenleri Kullanma**: Güncel olmayan bağımlılıklar
- **Yetersiz Günlük Kaydı ve İzleme**: Tespit edilemeyen ihlaller
### En İyi Güvenlik Uygulamaları
- **HTTPS**: TLS/SSL şifreleme, HSTS
- **İçerik Güvenliği Politikası (CSP)**: XSS saldırılarını önleyin
- **Giriş Doğrulaması**: Kullanıcı girişini sterilize edin
- **Çıktı Kodlaması**: Enjeksiyon saldırılarını önleyin
- **CSRF Koruması**: CSRF karşıtı belirteçler, SameSite çerezleri
- **Hız Sınırlama**: Kaba kuvvet saldırılarını önleyin
- **Güvenlik Başlıkları**: X-Frame-Options, X-Content-Type-Options
- **Bağımlılık Taraması**: npm denetimi, Snyk, Dependabot
## Test etme
### Test Türleri
- **Birim Testi**: Bireysel bileşenler/işlevler
- **Entegrasyon Testi**: Bileşen etkileşimleri
- **Uçtan Uca (E2E)**: Tam kullanıcı iş akışları
- **Görsel Regresyon**: Kullanıcı arayüzü değişikliği tespiti
- **Performans Testi**: Yük, stres, ani artış testleri
- **Erişilebilirlik Testi**: WCAG uyumluluğu
### Çerçeveleri Test Etme
- **Jest**: JavaScript test çerçevesi
- **Mocha**: Esnek test koşucusu
- **pytest**: Python test çerçevesi
- **RSpec**: Ruby test çerçevesi
- **JUnit**: Java test çerçevesi
### E2E Test Araçları
- **Selenyum**: Tarayıcı otomasyonu
- **Selvi**: Modern E2E testleri
- **Oyun Yazarı**: Tarayıcılar arası otomasyon
- **Kuklacı**: Başsız Chrome kontrolü
## Erişilebilirlik (a11y)
### WCAG Yönergeleri
- **Algılanabilir**: Metin alternatifleri, altyazılar, uyarlanabilir içerik
- **Çalıştırılabilir**: Klavyeyle gezinme, yeterli süre, nöbet yok
- **Anlaşılabilir**: Okunabilir, öngörülebilir, giriş yardımı
- **Sağlam**: Yardımcı teknolojilerle uyumlu
### Uygulama
- **Semantik HTML**: Uygun başlık hiyerarşisi, yer işaretleri
- **ARIA Nitelikleri**: Roller, durumlar, özellikler
- **Odak Yönetimi**: Görünür odak göstergeleri, mantıksal sekme sırası
- **Renk Kontrastı**: Metin için minimum 4,5:1 oranı
- **Ekran Okuyucu Testi**: NVDA, JAWS, VoiceOver
- **Klavye Gezintisi**: Tüm etkileşimli öğelere erişilebilir
## Aşamalı Web Uygulamaları (PWA'lar)
### PWA Özellikleri
- **Hizmet Çalışanları**: Çevrimdışı işlevsellik, arka planda senkronizasyon
- **Web Uygulaması Bildirimi**: Kurulum istemi, simgeler, tema renkleri
- **Uygulama Kabuğu**: Önbelleğe alınmış kullanıcı arayüzü iskeleti
- **Anlık Bildirimler**: Kullanıcı etkileşimi
- **Duyarlı Tasarım**: Tüm cihazlarda çalışır
- **HTTPS Gerekli**: Güvenli içerik
### Araçlar
- **Çalışma Kutusu**: Hizmet çalışanı kitaplıkları
- **Deniz Feneri**: PWA denetimi
- **PWA Builder**: Bildirimler ve simgeler oluşturun
## Gelişen Teknolojiler
### WebAssembly (Wasm)
- **Amaç**: Derlenmiş kodu tarayıcıda neredeyse yerel hızda çalıştırmak
- **Diller**: C++, Rust, Go derleme hedefleri
- **Kullanım Örnekleri**: Oyunlar, video düzenleme, şifreleme, makine öğrenimi çıkarımı
### Sunucusuz Mimari
- **Hizmet Olarak İşlevler**: AWS Lambda, Azure İşlevleri, Google Bulut İşlevleri
- **Avantajları**: Sunucu yönetimi yok, otomatik ölçeklendirme, kullanım başına ödeme
- **Düşünülmesi Gereken Noktalar**: Soğuk başlatma, satıcıya bağlılık, hata ayıklama karmaşıklığı
### Jamstack Mimarisi
- **JavaScript**: İstemci tarafı etkileşimi
- **API'ler**: Sunucusuz işlevler, üçüncü taraf hizmetleri
- **İşaretleme**: Önceden oluşturulmuş statik dosyalar
- **Araçlar**: Next.js, Gatsby, Hugo, Eleventy
- **Avantajları**: Performans, güvenlik, ölçeklenebilirlik, geliştirici deneyimi
### Gerçek Zamanlı İletişim
- **WebSockets**: Çift yönlü iletişim
- **Sunucudan Gönderilen Etkinlikler**: Sunucudan istemciye akış
- **WebRTC**: Eşler arası video, ses, veri
- **Kullanım Örnekleri**: Sohbet, ortak çalışma, canlı yayın, oyun
### Mikro Ön Uçlar
- **Konsept**: Mikro hizmetleri ön uca kadar genişletin
- **Yaklaşımlar**: Derleme zamanı, çalışma zamanı, uç tarafı entegrasyonu
- **Avantajları**: Bağımsız dağıtımlar, ekip özerkliği
- **Zorluklar**: Tutarlılık, performans, karmaşıklık