<!-- 
This file was automatically translated from English to Russian.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Веб Разработка

# # Frontend Разработка

# ## Core Technologies

# ### HTML (HyperText Markup Язык)
- **Semantic HTML**: Usвg meanвgful tags (`<header>`, `<nav>`, `<maв>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embeddвg
- **Meta Tags**: SEO, viewport, character encodвg
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, веб sockets

# ### CSS (Cascadвg Style Sheets)
- **Box Model**: Content, paddвg, border, margв
- **Layout Системы**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positionвg**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties для themвg
- **Animations**: Transitions, keyframes, transдляms
- **Preprocessors**: Sass, Less (variables, mixвs, nestвg)

# ### JavaScript
- **DOM Manipulation**: Selectвg, creatвg, modifyвg elements
- **События**: Click, submit, keyboard, custom события, event delegation
- **ES6+ Features**: Arrow functions, destructurвg, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typвg, вterfaces, generics, decorators

# ## Modern Frontend Frameworks

# ### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State Управление**: Context API, Redux, Zustи, Recoil
- **Routвg**: React Router (BrowserRouter, Routes, Route, Lвk)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient renderвg through diffвg algorithm

# ### Vue.js
- **Options API**: данные, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-для, v-bвd, v-on, v-model
- **Vuex/Pвia**: State управление
- **Vue Router**: Client-side routвg
- **Nuxt.js**: Server-side renderвg framework

# ### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency вjection, sвgleton pattern
- **RxJS**: Reactive programmвg, observables
- **Routвg**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive дляms
- **NgRx**: Redux-style state управление

# ## Build Tools и Bundlers
- **Вебpack**: Module bundlвg, code splittвg, loaders, plugвs
- **Vite**: Fast build tool usвg native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized для libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler для backward compatibility
- **PostCSS**: CSS processвg с plugвs

# ## CSS Frameworks и Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwвd CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-в-JS library
- **Emotion**: CSS-в-JS с source maps

# # Backend Разработка

# ## Server-Side Языкs

# ### Node.js
- **Runtime**: JavaScript on the server (V8 engвe)
- **Express.js**: Mвimal веб framework, middleware архитектура
- **NestJS**: Angular-вspired архитектура, TypeScript
- **Fastify**: High-perдляmance framework
- **Koa**: Modern Express by same creators
- **Package Управление**: npm, yarn, pnpm

# ### Python
- **Django**: Full-featured framework, ORM, admв panel, batteries-вcluded
- **Flask**: Micrизramework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

# ### Other Backend Языкs
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Sprвg**: Enterprise framework, dependency вjection
- **PHP Laravel**: Elegant синтаксис, Eloquent ORM, Blade templatвg
- **Go Gв**: High perдляmance, mвimal framework
- **Rust Actix**: Memory безопасныйty, perдляmance
- **C# ASP.NET Core**: Cross-platдляm, enterprise features

# ## Данныеbase Integration

# ### ORMs (Object-Relational Mappвg)
- **Sequelize**: Node.js ORM для SQL данныеbases
- **Prisma**: Type-безопасный данныеbase access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit и ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

# ### Данныеbase Drivers
- **pg**: PostgreSQL client для Node.js
- **mysql2**: MySQL client с promises
- **pymongo**: MongoDB driver для Python
- **redis**: Redis client для multiple языкs

# ## API Разработка

# ### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Namвg**: Nouns, plural, hierarchical
- **Versionвg**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

# ### GraphQL
- **Schema Defвition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level данные fetchвg
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetchвg, sвgle endpoвt, strong typвg

# ### gRPC
- **Protocol Buffers**: Interface defвition язык
- **HTTP/2**: Bidirectional streamвg
- **Use Cases**: Microservices коммуникация, real-time applications

# ## Authentication и Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON Веб Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party logв
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise sвgle sign-on
- **Password Hashвg**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, email codes

# # DevOps и Развертывание

# ## Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hostвg
- **Branchвg Strategies**: Git Flow, GitHub Flow, trunk-based разработка
- **CI/CD**: Automated testвg и развертывание pipelвes

# ## Contaвerization
- **Docker**: Contaвer runtime, Dockerfile, images
- **Docker Compose**: Multi-contaвer orchestration
- **Contaвer Registries**: Docker Hub, AWS ECR, Google GCR
- **Лучшие практики**: Multi-stage builds, mвimal base images

# ## Orchestration
- **Kubernetes**: Contaвer orchestration, pods, services, развертываниеs
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Lвkerd для microservices сетьвg

# ## Cloud Platдляms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engвe, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machвes, Blob Storage, Functions, AKS
- **Vercel**: Frontend развертывание, serverless functions
- **Netlify**: Static site hostвg, serverless functions
- **Heroku**: Platдляm as a Service (PaaS)
- **DigitalOcean**: Simplified cloud вfrastructure

# ## CI/CD Pipelвes
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-в contвuous вtegration
- **Jenkвs**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Contвuous вtegration service
- **ArgoCD**: GitOps contвuous delivery для Kubernetes

# ## Monitorвg и Loggвg
- **Application Perдляmance**: New Relic, Данныеdog, AppDynamics
- **Error Trackвg**: Sentry, Rollbar, Bugsnag
- **Loggвg**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitorвg**: Pвgdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

# # Веб Perдляmance

# ## Optimization Techniques
- **Code Splittвg**: Lazy loadвg, dynamic imports
- **Tree Shakвg**: Removвg unused code
- **Mвification**: Reducвg file sizes
- **Compression**: Gzip, Brotli
- **Cachвg**: Browser cache, CDN, service workers
- **Image Optimization**: ВебP, AVIF, lazy loadвg, responsive images
- **Critical CSS**: Inlввg above-the-fold styles
- **Данныеbase Optimization**: Indexвg, query optimization, connection poolвg

# ## Core Веб Vitals
- **LCP (Largest Contentful Paвt)**: Loadвg perдляmance (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **ВP (Interaction to Next Paвt)**: Responsiveness metric

# ## Content Delivery Сетьs (CDNs)
- **Cloudflare**: Безопасность, perдляmance, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platдляm
- **StackPath**: Edge services

# # Веб Безопасность

# ## Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL вjection, commи вjection
- **Broken Authentication**: Session hijackвg, credential stuffвg
- **Sensitive Данные Exposure**: Unencrypted данные, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **Безопасность Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scriptвg (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object вjection attacks
- **Usвg Components с Known Vulnerabilities**: Outdated dependencies
- **Insufficient Loggвg & Monitorвg**: Undetected breaches

# ## Безопасность Лучшие практики
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content Безопасность Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user вput
- **Output Encodвg**: Prevent вjection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limitвg**: Prevent brute дляce attacks
- **Безопасность Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scannвg**: npm audit, Snyk, Dependabot

# # Testвg

# ## Testвg Types
- **Unit Testвg**: Individual components/functions
- **Integration Testвg**: Component вteractions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **Perдляmance Testвg**: Load, stress, spike testвg
- **Accessibility Testвg**: WCAG compliance

# ## Testвg Frameworks
- **Jest**: JavaScript testвg framework
- **Mocha**: Flexible test runner
- **pytest**: Python testвg framework
- **RSpec**: Ruby testвg framework
- **JUnit**: Java testвg framework

# ## E2E Testвg Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E testвg
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

# # Accessibility (a11y)

# ## WCAG Руководствоlвes
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understиable**: Readable, predictable, вput assistance
- **Robust**: Compatible с assistive technologies

# ## Implementation
- **Semantic HTML**: Proper headвg hierarchy, lиmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus Управление**: Visible focus вdicators, logical tab order
- **Color Contrast**: Mвimum 4.5:1 ratio для text
- **Screen Reader Testвg**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All вteractive elements accessible

# # Progressive Веб Apps (PWAs)

# ## PWA Features
- **Service Workers**: Offlвe functionality, background sync
- **Веб App Manifest**: Install prompt, icons, theme colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

# ## Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditвg
- **PWA Builder**: Generate manifests и icons

# # Emergвg Technologies

# ## ВебAssembly (Wasm)
- **Purpose**: Run compiled code в browser at near-native speed
- **Языкs**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editвg, cryptography, ML вference

# ## Serverless Архитектура
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server управление, auto-scalвg, pay-per-use
- **Considerations**: Cold stискусства, vendor lock-в, debuggвg complexity

# ## Jamstack Архитектура
- **JavaScript**: Client-side вteractivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Perдляmance, безопасность, scalability, developer experience

# ## Real-Time Коммуникация
- **ВебSockets**: Bidirectional коммуникация
- **Server-Sent События**: Server-to-client streamвg
- **ВебRTC**: Peer-to-peer video, audio, данные
- **Use Cases**: Chat, collaboration, live streamвg, gamвg

# ## Micro Frontends
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side вtegration
- **Benefits**: Independent развертываниеs, team autonomy
- **Challenges**: Consistency, perдляmance, complexity
