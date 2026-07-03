# Web Geliştirme

## Frontend Geliştirme

### Temel Teknolojiler

#### HTML (HyperText Markup Language)
- **Semantic HTML**: Anlamlı etiketler kullanma (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input türleri, doğrulama, erişilebilirlik etiketleri
- **Media**: Görsel, video ve ses gömme
- **Meta Tags**: SEO, viewport, karakter kodlaması
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, web sockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **Layout Systems**:
  - **Flexbox**: Tek boyutlu düzenler, justify-content, align-items
  - **Grid**: İki boyutlu düzenler, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media query'ler, mobile-first yaklaşım
- **CSS Variables**: Tema oluşturmak için custom property'ler
- **Animations**: Transitions, keyframes, transforms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipulation**: Öğeleri seçme, oluşturma, değiştirme
- **Events**: Click, submit, keyboard, custom events, event delegation
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typing, interfaces, generics, decorators

### Modern Frontend Frameworks

#### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State Management**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Diffing algoritmasıyla verimli render

#### Vue.js
- **Options API**: data, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: State management
- **Vue Router**: Client-side routing
- **Nuxt.js**: Server-side rendering framework

#### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency injection, singleton pattern
- **RxJS**: Reactive programming, observables
- **Routing**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive forms
- **NgRx**: Redux tarzı state management

### Build Tools ve Bundlers
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Native ES modules kullanan hızlı build aracı
- **Parcel**: Zero-configuration bundler
- **Rollup**: Library'ler için optimize edilmiştir
- **esbuild**: Son derece hızlı JavaScript bundler'ı
- **Babel**: Geriye dönük uyumluluk için JavaScript transpiler'ı
- **PostCSS**: Plugin'lerle CSS işleme aracı

### CSS Frameworks ve Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google'ın Material Design uygulaması
- **Chakra UI**: Erişilebilir component library
- **Ant Design**: Kurumsal düzeyde UI bileşenleri
- **Styled Components**: CSS-in-JS library
- **Emotion**: Source map destekli CSS-in-JS

## Backend Geliştirme

### Server-Side Languages

#### Node.js
- **Runtime**: Sunucu tarafında JavaScript (V8 engine)
- **Express.js**: Minimal web framework, middleware mimarisi
- **NestJS**: Angular'dan ilham alan mimari, TypeScript
- **Fastify**: Yüksek performanslı framework
- **Koa**: Aynı yaratıcılar tarafından geliştirilen modern Express
- **Package Management**: npm, yarn, pnpm

#### Python
- **Django**: Full-featured framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, extension ekosistemi
- **FastAPI**: Modern, async, otomatik API dokümantasyonu
- **Pyramid**: Esnek, ölçeklenebilir framework

#### Other Backend Languages
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Kurumsal framework, dependency injection
- **PHP Laravel**: Zarif söz dizimi, Eloquent ORM, Blade templating
- **Go Gin**: Yüksek performans, minimal framework
- **Rust Actix**: Bellek güvenliği, performans
- **C# ASP.NET Core**: Cross-platform, kurumsal özellikler

### Veritabanı Entegrasyonu

#### ORMs (Object-Relational Mapping)
- **Sequelize**: SQL veritabanları için Node.js ORM'si
- **Prisma**: Type-safe veritabanı erişimi, otomatik üretilen client
- **SQLAlchemy**: Python SQL toolkit ve ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### Database Drivers
- **pg**: Node.js için PostgreSQL istemcisi
- **mysql2**: Promise destekli MySQL istemcisi
- **pymongo**: Python için MongoDB driver'ı
- **redis**: Birden çok dil için Redis istemcisi

### API Geliştirme

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: İsimler, çoğul yapı, hiyerarşi
- **Versioning**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Alan düzeyinde veri getirme
- **Apollo Server**: GraphQL sunucu uygulaması
- **Relay**: Facebook'un GraphQL istemcisi
- **Advantages**: Over-fetching yok, tek endpoint, güçlü türleme

#### gRPC
- **Protocol Buffers**: Interface tanım dili
- **HTTP/2**: Çift yönlü akış
- **Use Cases**: Microservices iletişimi, gerçek zamanlı uygulamalar

### Authentication ve Authorization
- **Session-based**: Cookies, server-side session'lar
- **Token-based**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Yetkilendirme framework'ü, üçüncü taraf giriş
- **OpenID Connect**: OAuth 2.0 üzerindeki kimlik katmanı
- **SAML**: Kurumsal single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, e-posta kodları

## DevOps ve Dağıtım

### Version Control
- **Git**: Dağıtık sürüm kontrolü
- **GitHub/GitLab/Bitbucket**: Repo barındırma
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Otomatik test ve dağıtım pipeline'ları

### Containerization
- **Docker**: Container runtime, Dockerfile, image'lar
- **Docker Compose**: Çok container'lı orkestrasyon
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Multi-stage build'ler, minimal base image'lar

### Orchestration
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes paket yöneticisi
- **Service Mesh**: Microservices ağı için Istio, Linkerd

### Cloud Platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend dağıtımı, serverless functions
- **Netlify**: Statik site barındırma, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Sadeleştirilmiş bulut altyapısı

### CI/CD Pipelines
- **GitHub Actions**: Workflow otomasyonu
- **GitLab CI**: Yerleşik continuous integration
- **Jenkins**: Genişletilebilir otomasyon sunucusu
- **CircleCI**: Cloud tabanlı CI/CD
- **Travis CI**: Continuous integration hizmeti
- **ArgoCD**: Kubernetes için GitOps continuous delivery

### Monitoring ve Logging
- **Application Performance**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Web Performansı

### Optimization Techniques
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Kullanılmayan kodu kaldırma
- **Minification**: Dosya boyutlarını küçültme
- **Compression**: Gzip, Brotli
- **Caching**: Tarayıcı önbelleği, CDN, service worker'lar
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Above-the-fold stillerin satır içine alınması
- **Database Optimization**: Indexing, query optimization, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Yükleme performansı (<2.5s)
- **FID (First Input Delay)**: Etkileşimlilik (<100ms)
- **CLS (Cumulative Layout Shift)**: Görsel kararlılık (<0.1)
- **INP (Interaction to Next Paint)**: Yanıt verebilirlik metriği

### Content Delivery Networks (CDNs)
- **Cloudflare**: Güvenlik, performans, DNS
- **Akamai**: Kurumsal CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platformu
- **StackPath**: Edge hizmetleri

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
- **Input Validation**: Kullanıcı girdisini sanitize etme
- **Output Encoding**: Injection saldırılarını önleme
- **CSRF Protection**: Anti-CSRF token'ları, SameSite cookie'leri
- **Rate Limiting**: Brute force saldırılarını önleme
- **Security Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Testing

### Test Türleri
- **Unit Testing**: Tekil bileşenler/fonksiyonlar
- **Integration Testing**: Bileşenler arası etkileşimler
- **End-to-End (E2E)**: Uçtan uca kullanıcı akışları
- **Visual Regression**: UI değişikliği tespiti
- **Performance Testing**: Load, stress, spike testleri
- **Accessibility Testing**: WCAG uyumluluğu

### Testing Frameworks
- **Jest**: JavaScript test framework'ü
- **Mocha**: Esnek test çalıştırıcısı
- **pytest**: Python test framework'ü
- **RSpec**: Ruby test framework'ü
- **JUnit**: Java test framework'ü

### E2E Testing Tools
- **Selenium**: Tarayıcı otomasyonu
- **Cypress**: Modern E2E test aracı
- **Playwright**: Çapraz tarayıcı otomasyonu
- **Puppeteer**: Headless Chrome kontrolü

## Accessibility (a11y)

### WCAG Guidelines
- **Perceivable**: Metin alternatifleri, altyazılar, uyarlanabilir içerik
- **Operable**: Klavye ile gezinme, yeterli zaman, nöbet tetiklememe
- **Understandable**: Okunabilirlik, öngörülebilirlik, giriş yardımı
- **Robust**: Yardımcı teknolojilerle uyumluluk

### Uygulama
- **Semantic HTML**: Doğru başlık hiyerarşisi, landmarks
- **ARIA Attributes**: Roller, durumlar, özellikler
- **Focus Management**: Görünür focus göstergeleri, mantıklı tab sırası
- **Color Contrast**: Metin için minimum 4.5:1 oranı
- **Screen Reader Testing**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: Tüm etkileşimli öğelerin erişilebilir olması

## Progressive Web Apps (PWAs)

### PWA Features
- **Service Workers**: Offline işlevsellik, background sync
- **Web App Manifest**: Kurulum istemi, ikonlar, tema renkleri
- **App Shell**: Önbelleğe alınmış UI iskeleti
- **Push Notifications**: Kullanıcı etkileşimi
- **Responsive Design**: Tüm cihazlarda çalışır
- **HTTPS Required**: Güvenli bağlam zorunluluğu

### Araçlar
- **Workbox**: Service worker kütüphaneleri
- **Lighthouse**: PWA denetimi
- **PWA Builder**: Manifest ve ikon üretimi

## Yükselen Teknolojiler

### WebAssembly (Wasm)
- **Purpose**: Derlenmiş kodu tarayıcıda yerel hıza yakın çalıştırmak
- **Languages**: C++, Rust, Go derleme hedefleri
- **Use Cases**: Oyunlar, video düzenleme, kriptografi, ML inference

### Serverless Mimari
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: Sunucu yönetimi yok, auto-scaling, kullandıkça öde
- **Considerations**: Cold start'lar, vendor lock-in, debugging karmaşıklığı

### Jamstack Mimarisi
- **JavaScript**: İstemci tarafı etkileşim
- **APIs**: Serverless functions, üçüncü taraf hizmetler
- **Markup**: Önceden oluşturulmuş statik dosyalar
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Performans, güvenlik, ölçeklenebilirlik, geliştirici deneyimi

### Real-Time Communication
- **WebSockets**: Çift yönlü iletişim
- **Server-Sent Events**: Sunucudan istemciye akış
- **WebRTC**: Eşler arası video, ses, veri
- **Use Cases**: Sohbet, iş birliği, canlı yayın, oyun

### Micro Frontends
- **Concept**: Microservices yaklaşımını frontend'e genişletmek
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Bağımsız dağıtımlar, ekip özerkliği
- **Challenges**: Tutarlılık, performans, karmaşıklık
