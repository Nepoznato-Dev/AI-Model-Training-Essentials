# Web Geliştirme

## Frontend Geliştirme

### Temel Teknolojiler

#### HTML (HyperText Markup Language)
- **Anlamsal HTML**: Anlamlı etiketler kullanma (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Formlar**: Input türleri, doğrulama, erişilebilirlik etiketleri
- **Medya**: Görsel, video ve ses gömme
- **Meta Etiketleri**: SEO, viewport, karakter kodlaması
- **HTML5 Özellikleri**: Canvas, SVG, local storage, geolocation, web sockets

#### CSS (Cascading Style Sheets)
- **Kutu Modeli**: Content, padding, border, margin
- **Yerleşim Sistemleri**:
  - **Flexbox**: Tek boyutlu düzenler, justify-content, align-items
  - **Grid**: İki boyutlu düzenler, grid-template, grid-area
  - **Konumlandırma**: Static, relative, absolute, fixed, sticky
- **Duyarlı Tasarım**: Media query'ler, mobile-first yaklaşım
- **CSS Değişkenleri**: Tema oluşturmak için custom property'ler
- **Animasyonlar**: Transitions, keyframes, transforms
- **Önişlemciler**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipülasyonu**: Öğeleri seçme, oluşturma, değiştirme
- **Olaylar**: Click, submit, keyboard, custom events, event delegation
- **ES6+ Özellikleri**: Arrow functions, destructuring, spread/rest, modules, async/await
- **API'ler**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Statik türleme, interfaces, generics, decorators

### Modern Frontend Çatıları

#### React
- **Bileşenler**: Fonksiyonel bileşenler, sınıf bileşenleri
- **Hook'lar**: useState, useEffect, useContext, useReducer, custom hooks
- **Durum Yönetimi**: Context API, Redux, Zustand, Recoil
- **Yönlendirme**: React Router (BrowserRouter, Routes, Route, Link)
- **Ekosistem**: Next.js (SSR, SSG), Remix, Gatsby
- **Sanal DOM**: Diffing algoritmasıyla verimli render

#### Vue.js
- **Options API**: data, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Yönergeler**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Durum yönetimi
- **Vue Router**: İstemci tarafı yönlendirme
- **Nuxt.js**: Sunucu tarafı render çerçevesi

#### Angular
- **Bileşenler**: Decorators, templates, lifecycle hooks
- **Servisler**: Dependency injection, singleton pattern
- **RxJS**: Reaktif programlama, observables
- **Yönlendirme**: RouterModule, guards, resolvers
- **Formlar**: Template-driven, reactive forms
- **NgRx**: Redux tarzı durum yönetimi

### Derleme Araçları ve Paketleyiciler
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Native ES modules kullanan hızlı build aracı
- **Parcel**: Sıfır yapılandırmalı paketleyici
- **Rollup**: Kütüphaneler için optimize edilmiştir
- **esbuild**: Son derece hızlı JavaScript paketleyicisi
- **Babel**: Geriye dönük uyumluluk için JavaScript dönüştürücüsü
- **PostCSS**: Eklentilerle CSS işleme aracı

### CSS Çatıları ve Kütüphaneleri
- **Bootstrap**: Bileşen kütüphanesi, grid sistemi, yardımcı sınıflar
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google'ın Material Design uygulaması
- **Chakra UI**: Erişilebilir bileşen kütüphanesi
- **Ant Design**: Kurumsal düzeyde UI bileşenleri
- **Styled Components**: CSS-in-JS kütüphanesi
- **Emotion**: Source map destekli CSS-in-JS

## Backend Geliştirme

### Sunucu Tarafı Dilleri

#### Node.js
- **Çalışma Ortamı**: Sunucu tarafında JavaScript (V8 engine)
- **Express.js**: Minimal web framework, middleware mimarisi
- **NestJS**: Angular'dan ilham alan mimari, TypeScript
- **Fastify**: Yüksek performanslı framework
- **Koa**: Aynı yaratıcılar tarafından geliştirilen modern Express
- **Paket Yönetimi**: npm, yarn, pnpm

#### Python
- **Django**: Kapsamlı framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, eklenti ekosistemi
- **FastAPI**: Modern, async, otomatik API dokümantasyonu
- **Pyramid**: Esnek, ölçeklenebilir framework

#### Diğer Backend Dilleri
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Kurumsal framework, dependency injection
- **PHP Laravel**: Zarif söz dizimi, Eloquent ORM, Blade templating
- **Go Gin**: Yüksek performans, minimal framework
- **Rust Actix**: Bellek güvenliği, performans
- **C# ASP.NET Core**: Cross-platform, kurumsal özellikler

### Veritabanı Entegrasyonu

#### ORMs (Object-Relational Mapping)
- **Sequelize**: SQL veritabanları için Node.js ORM'si
- **Prisma**: Type-safe veritabanı erişimi, otomatik üretilen istemci
- **SQLAlchemy**: Python SQL toolkit ve ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### Veritabanı Sürücüleri
- **pg**: Node.js için PostgreSQL istemcisi
- **mysql2**: Promise destekli MySQL istemcisi
- **pymongo**: Python için MongoDB sürücüsü
- **redis**: Birden çok dil için Redis istemcisi

### API Geliştirme

#### REST API'leri
- **HTTP Yöntemleri**: GET, POST, PUT, PATCH, DELETE
- **Durum Kodları**: 200, 201, 400, 401, 403, 404, 500
- **Kaynak Adlandırma**: İsimler, çoğul yapı, hiyerarşi
- **Sürümleme**: URL path, headers, query parameters
- **Kimlik Doğrulama**: JWT, OAuth, API keys
- **Dokümantasyon**: OpenAPI/Swagger, Postman

#### GraphQL
- **Şema Tanımı**: Types, queries, mutations, subscriptions
- **Resolver'lar**: Alan düzeyinde veri getirme
- **Apollo Server**: GraphQL sunucu uygulaması
- **Relay**: Facebook'un GraphQL istemcisi
- **Avantajlar**: Over-fetching yok, tek endpoint, güçlü türleme

#### gRPC
- **Protocol Buffers**: Arayüz tanım dili
- **HTTP/2**: Çift yönlü akış
- **Kullanım Alanları**: Mikroservis iletişimi, gerçek zamanlı uygulamalar

### Kimlik Doğrulama ve Yetkilendirme
- **Oturum Tabanlı**: Cookies, server-side session'lar
- **Token Tabanlı**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Yetkilendirme çerçevesi, üçüncü taraf giriş
- **OpenID Connect**: OAuth 2.0 üzerindeki kimlik katmanı
- **SAML**: Kurumsal single sign-on
- **Parola Özetleme**: bcrypt, argon2, scrypt
- **Çok Faktörlü Kimlik Doğrulama**: TOTP, SMS, e-posta kodları

## DevOps ve Dağıtım

### Sürüm Kontrolü
- **Git**: Dağıtık sürüm kontrolü
- **GitHub/GitLab/Bitbucket**: Depo barındırma
- **Dallanma Stratejileri**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Otomatik test ve dağıtım pipeline'ları

### Konteynerleştirme
- **Docker**: Container runtime, Dockerfile, image'lar
- **Docker Compose**: Çok container'lı orkestrasyon
- **Container Registry'leri**: Docker Hub, AWS ECR, Google GCR
- **En İyi Uygulamalar**: Multi-stage build'ler, minimal base image'lar

### Orkestrasyon
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes paket yöneticisi
- **Service Mesh**: Mikroservis ağı için Istio, Linkerd

### Bulut Platformları
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend dağıtımı, serverless functions
- **Netlify**: Statik site barındırma, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Sadeleştirilmiş bulut altyapısı

### CI/CD Pipeline'ları
- **GitHub Actions**: Workflow otomasyonu
- **GitLab CI**: Yerleşik continuous integration
- **Jenkins**: Genişletilebilir otomasyon sunucusu
- **CircleCI**: Cloud tabanlı CI/CD
- **Travis CI**: Continuous integration hizmeti
- **ArgoCD**: Kubernetes için GitOps continuous delivery

### İzleme ve Günlükleme
- **Uygulama Performansı**: New Relic, Datadog, AppDynamics
- **Hata Takibi**: Sentry, Rollbar, Bugsnag
- **Günlükleme**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Çalışır Durum İzleme**: Pingdom, UptimeRobot
- **Analitik**: Google Analytics, Mixpanel, Amplitude

## Web Performansı

### Optimizasyon Teknikleri
- **Kod Bölme**: Lazy loading, dynamic imports
- **Tree Shaking**: Kullanılmayan kodu kaldırma
- **Minification**: Dosya boyutlarını küçültme
- **Sıkıştırma**: Gzip, Brotli
- **Önbellekleme**: Tarayıcı önbelleği, CDN, service worker'lar
- **Görsel Optimizasyonu**: WebP, AVIF, lazy loading, responsive images
- **Kritik CSS**: Above-the-fold stillerin satır içine alınması
- **Veritabanı Optimizasyonu**: Indexing, query optimization, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Yükleme performansı (<2.5s)
- **FID (First Input Delay)**: Etkileşimlilik (<100ms)
- **CLS (Cumulative Layout Shift)**: Görsel kararlılık (<0.1)
- **INP (Interaction to Next Paint)**: Yanıt verebilirlik metriği

### İçerik Dağıtım Ağları (CDN'ler)
- **Cloudflare**: Güvenlik, performans, DNS
- **Akamai**: Kurumsal CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Uç bulut platformu
- **StackPath**: Uç hizmetleri

## Web Güvenliği

### Yaygın Açıklar (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Session hijacking, credential stuffing
- **Sensitive Data Exposure**: Şifrelenmemiş veri, zayıf kriptografi
- **XML External Entities (XXE)**: XML parser açıkları
- **Broken Access Control**: Privilege escalation, yetkisiz erişim
- **Security Misconfiguration**: Varsayılan kimlik bilgileri, ayrıntılı hata çıktıları
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object injection saldırıları
- **Using Components with Known Vulnerabilities**: Güncel olmayan bağımlılıklar
- **Insufficient Logging & Monitoring**: Tespit edilemeyen ihlaller

### Güvenlik İçin En İyi Uygulamalar
- **HTTPS**: TLS/SSL şifrelemesi, HSTS
- **Content Security Policy (CSP)**: XSS saldırılarını önleme
- **Girdi Doğrulama**: Kullanıcı girdisini sanitize etme
- **Çıktı Kodlama**: Injection saldırılarını önleme
- **CSRF Koruması**: Anti-CSRF token'ları, SameSite cookie'leri
- **Oran Sınırlama**: Brute force saldırılarını önleme
- **Güvenlik Başlıkları**: X-Frame-Options, X-Content-Type-Options
- **Bağımlılık Taraması**: npm audit, Snyk, Dependabot

## Testing

### Test Türleri
- **Birim Testi**: Tekil bileşenler/fonksiyonlar
- **Entegrasyon Testi**: Bileşenler arası etkileşimler
- **End-to-End (E2E)**: Uçtan uca kullanıcı akışları
- **Görsel Gerileme Testi**: UI değişikliği tespiti
- **Performans Testi**: Load, stress, spike testleri
- **Erişilebilirlik Testi**: WCAG uyumluluğu

### Test Çerçeveleri
- **Jest**: JavaScript test framework'ü
- **Mocha**: Esnek test çalıştırıcısı
- **pytest**: Python test framework'ü
- **RSpec**: Ruby test framework'ü
- **JUnit**: Java test framework'ü

### E2E Test Araçları
- **Selenium**: Tarayıcı otomasyonu
- **Cypress**: Modern E2E test aracı
- **Playwright**: Çapraz tarayıcı otomasyonu
- **Puppeteer**: Headless Chrome kontrolü

## Erişilebilirlik (a11y)

### WCAG Rehberi
- **Algılanabilir**: Metin alternatifleri, altyazılar, uyarlanabilir içerik
- **Kullanılabilir**: Klavye ile gezinme, yeterli zaman, nöbet tetiklememe
- **Anlaşılabilir**: Okunabilirlik, öngörülebilirlik, giriş yardımı
- **Sağlam**: Yardımcı teknolojilerle uyumluluk

### Uygulama
- **Anlamsal HTML**: Doğru başlık hiyerarşisi, landmarks
- **ARIA Nitelikleri**: Roller, durumlar, özellikler
- **Odak Yönetimi**: Görünür focus göstergeleri, mantıklı tab sırası
- **Renk Kontrastı**: Metin için minimum 4.5:1 oranı
- **Ekran Okuyucu Testi**: NVDA, JAWS, VoiceOver
- **Klavye ile Gezinme**: Tüm etkileşimli öğelerin erişilebilir olması

## Progressive Web Apps (PWAs)

### PWA Özellikleri
- **Service Workers**: Çevrimdışı işlevsellik, background sync
- **Web App Manifest**: Kurulum istemi, ikonlar, tema renkleri
- **App Shell**: Önbelleğe alınmış UI iskeleti
- **Push Notifications**: Kullanıcı etkileşimi
- **Duyarlı Tasarım**: Tüm cihazlarda çalışır
- **HTTPS Zorunluluğu**: Güvenli bağlam gereklidir

### Araçlar
- **Workbox**: Service worker kütüphaneleri
- **Lighthouse**: PWA denetimi
- **PWA Builder**: Manifest ve ikon üretimi

## Yükselen Teknolojiler

### WebAssembly (Wasm)
- **Amaç**: Derlenmiş kodu tarayıcıda yerel hıza yakın çalıştırmak
- **Diller**: C++, Rust, Go derleme hedefleri
- **Kullanım Alanları**: Oyunlar, video düzenleme, kriptografi, ML çıkarımı

### Sunucusuz Mimari
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Avantajlar**: Sunucu yönetimi yok, auto-scaling, kullandıkça öde
- **Dikkat Edilmesi Gerekenler**: Cold start'lar, üreticiye bağımlılık, hata ayıklama karmaşıklığı

### Jamstack Mimarisi
- **JavaScript**: İstemci tarafı etkileşim
- **API'ler**: Serverless functions, üçüncü taraf hizmetler
- **Markup**: Önceden oluşturulmuş statik dosyalar
- **Araçlar**: Next.js, Gatsby, Hugo, Eleventy
- **Avantajlar**: Performans, güvenlik, ölçeklenebilirlik, geliştirici deneyimi

### Gerçek Zamanlı İletişim
- **WebSockets**: Çift yönlü iletişim
- **Server-Sent Events**: Sunucudan istemciye akış
- **WebRTC**: Eşler arası video, ses, veri
- **Kullanım Alanları**: Sohbet, iş birliği, canlı yayın, oyun

### Micro Frontends
- **Kavram**: Mikroservis yaklaşımını frontend'e genişletmek
- **Yaklaşımlar**: Build-time, run-time, uç katman entegrasyonu
- **Avantajlar**: Bağımsız dağıtımlar, ekip özerkliği
- **Zorluklar**: Tutarlılık, performans, karmaşıklık
