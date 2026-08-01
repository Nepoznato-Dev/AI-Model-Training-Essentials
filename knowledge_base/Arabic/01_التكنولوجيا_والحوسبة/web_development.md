<!-- 
This file was automatically translated from English to Arabic.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# تطوير الويب

## تطوير الواجهة الأمامية

### التقنيات الأساسية

#### HTML (HyperText Markup Language)
- **Semantic HTML**: استخدام وسوم ذات معنى مثل (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: أنواع الإدخال، التحقق، وتسميات إتاحة الوصول
- **Media**: تضمين الصور والفيديو والصوت
- **Meta Tags**: تحسين SEO، إطار العرض، وترميز المحارف
- **HTML5 Features**: Canvas وSVG والتخزين المحلي وتحديد الموقع الجغرافي وWebSockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **أنظمة التخطيط**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: خصائص مخصصة للسمات
- **Animations**: Transitions, keyframes, transforms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipulation**: تحديد العناصر وإنشاؤها وتعديلها
- **الأحداث**: Click, submit, keyboard, custom الأحداث, event delegation
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/await
- **واجهات البرمجة**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typing, interfaces, generics, decorators

### أطر الواجهة الأمامية الحديثة

#### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **إدارة الحالة**: Context API وRedux وZustand وRecoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient rendering through diffing algorithm

#### Vue.js
- **Options API**: البيانات, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-لأجل, v-bind, v-on, v-model
- **Vuex/Pinia**: State الإدارة
- **Vue Router**: Client-side routing
- **Nuxt.js**: Server-side rendering framework

#### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency injection, singleton pattern
- **RxJS**: Reactive programming, observables
- **Routing**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive forms
- **NgRx**: Redux-style state الإدارة

### أدوات البناء والحزم
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Fast build tool using native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized لـlibraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler لـbackward compatibility
- **PostCSS**: CSS processing مع plugins

### أطر ومكتبات CSS
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: مكتبة CSS-in-JS
- **Emotion**: CSS-in-JS مع خرائط المصدر

## تطوير الواجهة الخلفية

### لغات جانب الخادم

#### Node.js
- **Runtime**: تشغيل JavaScript على الخادم (محرك V8)
- **Express.js**: إطار ويب خفيف وبنية للبرمجيات الوسيطة
- **NestJS**: Angular-inspired العمارة, TypeScript
- **Fastify**: High-الأداء framework
- **Koa**: Modern Express by same creators
- **Package الإدارة**: npm, yarn, pnpm

#### Python
- **Django**: Full-featured framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

#### لغات خلفية أخرى
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant بناء الجملة, Eloquent ORM, Blade templating
- **Go Gin**: High الأداء, minimal framework
- **Rust Actix**: Memory safety, الأداء
- **C# ASP.NET Core**: Cross-platform, enterprise features

### تكامل قواعد البيانات

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM لـSQL databases
- **Prisma**: Type-آمن قاعدة البيانات access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit وORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### مشغلات قواعد البيانات
- **pg**: PostgreSQL client لـNode.js
- **mysql2**: MySQL client مع promises
- **pymongo**: MongoDB driver لـPython
- **redis**: Redis client لـmultiple languages

### تطوير API

#### REST واجهات البرمجة
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Nouns, plural, hierarchical
- **Versioning**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level البيانات fetching
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetching, single endpoint, strong typing

#### gRPC
- **Protocol Buffers**: Interface definition اللغة
- **HTTP/2**: Bidirectional streaming
- **حالات الاستخدام**: Microservices التواصل, real-time applications

### المصادقة والتفويض
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON الويب Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party login
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, email codes

## DevOps والنشر

### إدارة الإصدارات
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hosting
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based التطوير
- **CI/CD**: Automated الاختبار والنشر pipelines

### Containerization
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Multi-container orchestration
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **أفضل الممارسات**: Multi-stage builds, minimal base images

### Orchestration
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Linkerd لـالخدمات المصغرة networking

### Cloud Platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend النشر, serverless functions
- **Netlify**: Static site hosting, serverless functions
- **Heroku**: المنصة كخدمة (PaaS)
- **DigitalOcean**: Simplified cloud infrastructure

### CI/CD Pipelines
- **GitHub Actions**: Workflow automation
- **GitLab CI**: مدمج continuous integration
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Continuous integration service
- **ArgoCD**: GitOps continuous delivery لـKubernetes

### المراقبة وتسجيل السجلات
- **Application الأداء**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## أداء الويب

### تقنيات التحسين
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Removing unused code
- **Minification**: Reducing file sizes
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Inlining الجزء المرئي الأول styles
- **قاعدة البيانات Optimization**: Indexing, query optimization, connection pooling

### مؤشرات Core Web Vitals
- **LCP (Largest Contentful Paint)**: Loading الأداء (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **INP (Interaction to Next Paint)**: Responsiveness metric

### Content Delivery Networks (CDNs)
- **Cloudflare**: الأمان, الأداء, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platform
- **StackPath**: Edge services

## أمان الويب

### الثغرات الشائعة (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Session hijacking, credential stuffing
- **Sensitive البيانات Exposure**: Unencrypted البيانات, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **الأمان Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object injection attacks
- **Using Components مع Known Vulnerabilities**: Outdated dependencies
- **Insufficient Logging & Monitoring**: Undetected breaches

### أفضل ممارسات الأمان
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content الأمان Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user input
- **Output Encoding**: Prevent injection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Prevent brute force attacks
- **الأمان Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## الاختبار

### أنواع الاختبار
- **Unit الاختبار**: Individual components/functions
- **Integration الاختبار**: Component interactions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **الأداء الاختبار**: Load, stress, spike الاختبار
- **Accessibility الاختبار**: WCAG compliance

### أطر الاختبار
- **Jest**: JavaScript الاختبار framework
- **Mocha**: Flexible test runner
- **pytest**: Python الاختبار framework
- **RSpec**: Ruby الاختبار framework
- **JUnit**: Java الاختبار framework

### E2E الاختبار Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E الاختبار
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

## إتاحة الوصول (a11y)

### WCAG Guidelines
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understandable**: Readable, predictable, input assistance
- **Robust**: Compatible مع assistive technologies

### Implementation
- **Semantic HTML**: Proper heading hierarchy, landmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus الإدارة**: Visible focus indicators, logical tab order
- **Color Contrast**: Minimum 4.5:1 ratio لـtext
- **Screen Reader الاختبار**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All interactive elements accessible

## تطبيقات الويب التقدمية (PWAs)

### PWA Features
- **Service Workers**: Offline functionality, background sync
- **الويب App Manifest**: Install prompt, icons, theme colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

### Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditing
- **PWA Builder**: Generate manifests وicons

## التقنيات الناشئة

### WebAssembly (Wasm)
- **Purpose**: Run compiled code في browser at near-native speed
- **Languages**: C++, Rust, Go compilation targets
- **حالات الاستخدام**: Games, video editing, cryptography, ML inference

### البنية عديمة الخوادم
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server الإدارة, auto-scaling, pay-per-use
- **الاعتبارات**: البدء البارد، الارتباط بالمورّد، وتعقيد تصحيح الأخطاء

### بنية Jamstack
- **JavaScript**: Client-side interactivity
- **واجهات البرمجة**: بدون خادم functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: الأداء, الأمان, scalability, developer experience

### التواصل في الوقت الحقيقي
- **WebSockets**: Bidirectional التواصل
- **Server-Sent الأحداث**: Server-to-client streaming
- **WebRTC**: Peer-to-peer video, audio, البيانات
- **حالات الاستخدام**: Chat, التعاون, live streaming, gaming

### Micro Frontends
- **Concept**: Extend الخدمات المصغرة to frontend
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Independent deployments, team autonomy
- **Challenges**: Consistency, الأداء, complexity
