<!--
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

-->
# Web Development
## Pag-unlad ng Frontend
### Mga Pangunahing Teknolohiya
#### HTML (HyperText Markup Language)
- **Semantic HTML**: Paggamit ng mga makabuluhang tag (`<header>`,`<nav>`,`<main>`,`<article>`,`<section>`,`<aside>`,`<footer>`)
- **Mga Form**: Mga uri ng input, pagpapatunay, mga label ng pagiging naa-access
- **Media**: Mga larawan, video, audio embed
- **Meta Tags**: SEO, viewport, pag-encode ng character
- **Mga Tampok ng HTML5**: Canvas, SVG, lokal na storage, geolocation, mga web socket
#### CSS (Cascading Style Sheet)
- **Modelo ng Kahon**: Nilalaman, padding, border, margin
- **Layout System**:
  - **Flexbox**: Mga one-dimensional na layout, justify-content, align-item
  - **Grid**: Mga two-dimensional na layout, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Tumugon na Disenyo**: Mga query sa media, mobile-first approach
- **CSS Variable**: Mga custom na property para sa theming
- **Animations**: Mga Transition, keyframe, transforms
- **Preprocessors**: Sass, Less (mga variable, mixin, nesting)
#### JavaScript
- **DOM Manipulation**: Pagpili, paggawa, pagbabago ng mga elemento
- **Mga Kaganapan**: I-click, isumite, keyboard, mga custom na kaganapan, delegasyon ng kaganapan
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/wait
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static na pagta-type, mga interface, generic, mga dekorador
### Mga Makabagong Frontend Framework
#### React
- **Mga Bahagi**: Mga functional na bahagi, mga bahagi ng klase
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **Pamamahala ng Estado**: Context API, Redux, Zustand, Recoil
- **Pagruruta**: React Router (BrowserRouter, Mga Ruta, Ruta, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Mahusay na pag-render sa pamamagitan ng diffing algorithm
#### Vue.js
- **Options API**: data, method, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Mga Direktiba**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Pamamahala ng estado
- **Vue Router**: Pagruruta sa panig ng kliyente
- **Nuxt.js**: Framework ng pag-render sa gilid ng server
#### Angular
- **Mga Bahagi**: Mga dekorador, template, lifecycle hook
- **Mga Serbisyo**: Dependency injection, singleton pattern
- **RxJS**: Reaktibong programming, mga napapansin
- **Pagruruta**: RouterModule, mga bantay, mga solver
- **Mga Form**: Mga form na batay sa template, reaktibo
- **NgRx**: Redux-style na pamamahala ng estado
### Bumuo ng Mga Tool at Bundler
- **Webpack**: Pag-bundle ng module, paghahati ng code, mga loader, mga plugin
- **Vite**: Fast build tool gamit ang native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Na-optimize para sa mga library
- **esbuild**: Napakabilis na JavaScript bundler
- **Babel**: JavaScript transpiler para sa backward compatibility
- **PostCSS**: Pagproseso ng CSS gamit ang mga plugin
### CSS Frameworks at Mga Aklatan
- **Bootstrap**: Component library, grid system, mga utility
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Pagpapatupad ng Material Design ng Google
- **Chakra UI**: Maa-access na library ng bahagi
- **Disenyo ng Langgam**: Mga bahagi ng UI sa antas ng enterprise
- **Mga Naka-istilong Bahagi**: CSS-in-JS library
- **Emosyon**: CSS-in-JS na may mga mapagkukunang mapa
## Pag-unlad ng Backend
### Mga Wika sa Gilid ng Server
#### Node.js
- **Runtime**: JavaScript sa server (V8 engine)
- **Express.js**: Minimal na web framework, middleware architecture
- **NestJS**: Angular-inspired na arkitektura, TypeScript
- **Fastify**: Framework na mataas ang performance
- **Koa**: Modern Express ng parehong mga creator
- **Package Management**: npm, yarn, pnpm
#### Python
- **Django**: Full-feature na framework, ORM, admin panel, mga baterya-kasama
- **Flask**: Microframework, ecosystem ng mga extension
- **FastAPI**: Moderno, async, awtomatikong dokumentasyon ng API
- **Pyramid**: Flexible, nasusukat na framework
#### Iba pang mga Backend na Wika
- **Ruby on Rails**: Convention sa pagsasaayos, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant syntax, Eloquent ORM, Blade templating
- **Go Gin**: Mataas na performance, minimal na framework
- **Rust Actix**: Kaligtasan ng memorya, pagganap
- **C# ASP.NET Core**: Cross-platform, mga feature ng enterprise
### Pagsasama ng Database
#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM para sa mga SQL database
- **Prisma**: Uri-safe na pag-access sa database, awtomatikong nabuong kliyente
- **SQLAlchemy**: Python SQL toolkit at ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM
#### Mga Driver ng Database
- **pg**: PostgreSQL client para sa Node.js
- **mysql2**: MySQL client na may mga pangako
- **pymongo**: MongoDB driver para sa Python
- **redis**: Redis client para sa maraming wika
### Pag-unlad ng API
#### REST API
- **Mga Paraan ng HTTP**: GET, POST, PUT, PATCH, DELETE
- **Mga Code ng Katayuan**: 200, 201, 400, 401, 403, 404, 500
- **Pagpapangalan ng Resource**: Mga Pangngalan, maramihan, hierarchical
- **Bersyon**: URL path, mga header, mga parameter ng query
- **Authentication**: JWT, OAuth, mga API key
- **Dokumentasyon**: OpenAPI/Swagger, Postman
#### GraphQL
- **Schema Definition**: Mga uri, query, mutations, subscription
- **Mga Resolver**: Pagkuha ng data sa antas ng field
- **Apollo Server**: Pagpapatupad ng GraphQL server
- **Relay**: GraphQL client ng Facebook
- **Mga Pakinabang**: Walang labis na pagkuha, nag-iisang endpoint, malakas na pag-type
#### gRPC
- **Protocol Buffers**: Interface definition language
- **HTTP/2**: Bidirectional streaming
- **Mga Kaso ng Paggamit**: Komunikasyon ng Microservices, mga real-time na application
### Pagpapatunay at Awtorisasyon
- **Batay sa session**: Cookies, mga session sa gilid ng server
- **Batay sa Token**: JWT (JSON Web Tokens), walang estado
- **OAuth 2.0**: Framework ng awtorisasyon, third-party na login
- **OpenID Connect**: Layer ng pagkakakilanlan sa OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, mga email code
## DevOps at Deployment
### Kontrol sa Bersyon
- **Git**: Ibinahagi ang kontrol sa bersyon
- **GitHub/GitLab/Bitbucket**: Pagho-host ng repositoryo
- **Branching Strategy**: Git Flow, GitHub Flow, trunk-based na development
- **CI/CD**: Automated testing at deployment pipelines
### Containerization
- **Docker**: Container runtime, Dockerfile, mga larawan
- **Docker Compose**: Multi-container orchestration
- **Container Registry**: Docker Hub, AWS ECR, Google GCR
- **Pinakamahuhusay na Kasanayan**: Mga multi-stage na build, kaunting mga base na larawan
### Orkestrasyon
- **Kubernetes**: Container orchestration, pod, serbisyo, deployment
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Linkerd para sa microservices networking
### Mga Cloud Platform
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Mga Virtual Machine, Blob Storage, Function, AKS
- **Vercel**: Pag-deploy ng frontend, mga function na walang server
- **Netlify**: Static na pagho-host ng site, mga function na walang server
- **Heroku**: Platform bilang isang Serbisyo (PaaS)
- **DigitalOcean**: Pinasimpleng imprastraktura ng ulap
### CI/CD Pipelines
- **Mga Pagkilos sa GitHub**: Automation ng daloy ng trabaho
- **GitLab CI**: Built-in na tuluy-tuloy na pagsasama
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Tuloy-tuloy na serbisyo sa pagsasama
- **ArgoCD**: tuloy-tuloy na paghahatid ng GitOps para sa Kubernetes
### Pagsubaybay at Pag-log
- **Pagganap ng Application**: Bagong Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Pag-log**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude
## Pagganap sa Web
### Mga Teknik sa Pag-optimize
- **Paghahati ng Code**: Tamad na pag-load, dynamic na pag-import
- **Tree Shaking**: Pag-alis ng hindi nagamit na code
- **Minification**: Pagbabawas ng mga laki ng file
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, mga service worker
- **Pag-optimize ng Larawan**: WebP, AVIF, tamad na pag-load, tumutugon na mga larawan
- **Critical CSS**: Inlining above-the-fold styles
- **Database Optimization**: Pag-index, pag-optimize ng query, pagsasama-sama ng koneksyon
### Mga Pangunahing Web Vitals
- **LCP (Largest Contentful Paint)**: Naglo-load ng performance (<2.5s)
- **FID (Unang Input Delay)**: Interaktibidad (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **INP (Interaction to Next Paint)**: Sukat ng pagtugon
### Content Delivery Networks (CDNs)
- **Cloudflare**: Seguridad, pagganap, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Mabilis**: Edge cloud platform
- **StackPath**: Mga serbisyo sa gilid
## Seguridad sa Web
### Mga Karaniwang Kahinaan (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Pag-hijack ng session, pagpupuno ng kredensyal
- **Sensitive Data Exposure**: Hindi naka-encrypt na data, mahinang cryptography
- **XML External Entities (XXE)**: Mga kahinaan ng XML parser
- **Broken Access Control**: Pagtaas ng pribilehiyo, hindi awtorisadong pag-access
- **Misconfiguration ng Seguridad**: Mga default na kredensyal, mga verbose error
- **Cross-Site Scripting (XSS)**: Sinasalamin, nakaimbak, nakabatay sa DOM
- **Insecure Deserialization**: Mga pag-atake ng Object injection
- **Paggamit ng Mga Bahagi na may Kilalang Mga Kahinaan**: Mga lumang dependency
- **Hindi Sapat na Pag-log at Pagsubaybay**: Mga hindi natukoy na paglabag
### Pinakamahusay na Kasanayan sa Seguridad
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content Security Policy (CSP)**: Pigilan ang mga pag-atake ng XSS
- **Pagpapatunay ng Input**: I-sanitize ang input ng user
- **Pag-encode ng Output**: Pigilan ang mga pag-atake ng injection
- **CSRF Protection**: Anti-CSRF token, SameSite cookies
- **Paglilimita sa Rate**: Pigilan ang mga malupit na pag-atake
- **Mga Header ng Seguridad**: X-Frame-Options, X-Content-Type-Options
- **Pag-scan ng Dependency**: npm audit, Snyk, Dependabot
## Pagsubok
### Mga Uri ng Pagsubok
- **Pagsusuri ng Unit**: Mga indibidwal na bahagi/function
- **Pagsusuri sa Pagsasama**: Mga pakikipag-ugnayan sa bahagi
- **End-to-End (E2E)**: Mga buong workflow ng user
- **Visual Regression**: Pagtukoy sa pagbabago ng UI
- **Pagsusuri sa Pagganap**: Pag-load, stress, pagsubok ng spike
- **Pagsusuri sa Pagiging Accessible**: Pagsunod sa WCAG
### Mga Framework ng Pagsubok
- **Jest**: JavaScript testing framework
- **Mocha**: Flexible test runner
- **pytest**: Python testing framework
- **RSpec**: Ruby testing framework
- **JUnit**: Java testing framework
### Mga Tool sa Pagsubok ng E2E
- **Selenium**: Pag-automate ng browser
- **Cypress**: Modernong pagsubok sa E2E
- **Playwright**: Cross-browser automation
- **Puppeteer**: Walang ulo na kontrol ng Chrome
## Accessibility (a11y)
### Mga Alituntunin ng WCAG
- **Perceivable**: Mga alternatibong teksto, mga caption, naaangkop na nilalaman
- **Operable**: Keyboard navigation, sapat na oras, walang seizure
- **Maiintindihan**: Nababasa, nahuhulaan, tulong sa pag-input
- **Robust**: Tugma sa mga pantulong na teknolohiya
### Pagpapatupad
- **Semantic HTML**: Wastong heading hierarchy, mga landmark
- **ARIA Attributes**: Mga tungkulin, estado, pag-aari
- **Pamamahala ng Focus**: Nakikitang mga indicator ng focus, lohikal na pagkakasunud-sunod ng tab
- **Contrast ng Kulay**: Minimum na 4.5:1 na ratio para sa text
- **Pagsubok sa Screen Reader**: NVDA, JAWS, VoiceOver
- **Navigation sa Keyboard**: Naa-access ang lahat ng interactive na elemento
## Progressive Web Apps (PWAs)
### Mga Tampok ng PWA
- **Mga Manggagawa ng Serbisyo**: Offline na pag-andar, pag-sync sa background
- **Web App Manifest**: I-install ang prompt, mga icon, kulay ng tema
- **App Shell**: Naka-cache na UI skeleton
- **Mga Push Notification**: Pakikipag-ugnayan ng user
- **Responsive Design**: Gumagana sa lahat ng device
- **Kinakailangan ang HTTPS**: Secure na konteksto
### Mga tool
- **Workbox**: Mga library ng service worker
- **Lighthouse**: Pag-audit ng PWA
- **PWA Builder**: Bumuo ng mga manifest at icon
## Mga Umuusbong na Teknolohiya
### WebAssembly (Wasm)
- **Layunin**: Patakbuhin ang pinagsama-samang code sa browser sa halos katutubong bilis
- **Mga Wika**: Mga target ng compilation ng C++, Rust, Go
- **Mga Kaso ng Paggamit**: Mga laro, pag-edit ng video, cryptography, ML inference
### Arkitekturang Walang Server
- **Mga Pag-andar bilang Serbisyo**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Mga Benepisyo**: Walang pamamahala sa server, auto-scaling, pay-per-use
- **Mga Pagsasaalang-alang**: Cold starts, vendor lock-in, debugging complexity
### Arkitektura ng Jamstack
- **JavaScript**: Interaktibidad sa panig ng kliyente
- **Mga API**: Mga function na walang server, mga serbisyo ng third-party
- **Markup**: Pre-built na mga static na file
- **Mga Tool**: Next.js, Gatsby, Hugo, Eleventy
- **Mga Benepisyo**: Pagganap, seguridad, scalability, karanasan ng developer
### Real-Time na Komunikasyon
- **WebSockets**: Bidirectional na komunikasyon
- **Server-Sent Events**: Server-to-client streaming
- **WebRTC**: Peer-to-peer na video, audio, data
- **Mga Kaso ng Paggamit**: Chat, collaboration, live streaming, gaming
### Mga Micro Frontend
- **Konsepto**: Palawakin ang mga microservice sa frontend
- **Mga Pagdulog**: Build-time, run-time, edge-side integration
- **Mga Benepisyo**: Mga independiyenteng deployment, awtonomiya ng koponan
- **Mga Hamon**: Consistency, performance, complexity