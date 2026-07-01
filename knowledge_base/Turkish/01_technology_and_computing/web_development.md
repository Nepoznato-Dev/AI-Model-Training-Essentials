<!-- 
This file was automatically translated from English to Turkish.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Web Geliştirme

# # Frontend Geliştirme

# ## Core Technologies

# ### HTML (HyperText Markup Dil)
- **Semantic HTML**: Usİçinde meanİçindeful tags (`<header>`, `<nav>`, `<maiçiçindede>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embeddİçinde
- **Meta Tags**: SEO, viewport, character encodİçinde
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, web sockets

# ### CSS (Cascadİçinde Style Sheets)
- **Box Model**: Content, paddİçinde, border, margiçiçindede
- **Layout Sistemler**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positionİçinde**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties için bumİçinde
- **Animations**: Transitions, keyframes, transiçinms
- **Preprocessors**: Sass, Less (variables, mixiçiçindedes, nestİçinde)

# ### JavaScript
- **DOM Manipulation**: Selectİçinde, creatİçinde, modifyİçinde elements
- **Olaylar**: Click, submit, keyboard, custom olaylar, event delegation
- **ES6+ Features**: Arrow functions, destructurİçinde, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typİçinde, içiçindedeterfaces, generics, decorators

# ## Modern Frontend Frameworks

# ### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State Yönetim**: Context API, Redux, Zustve, Recoil
- **Routİçinde**: React Router (BrowserRouter, Routes, Route, Liçiçindedek)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient renderİçinde through diffİçinde algorithm

# ### Vue.js
- **Options API**: veri, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-için, v-biçiçindeded, v-on, v-model
- **Vuex/Piçiçindedeia**: State yönetim
- **Vue Router**: Client-side routİçinde
- **Nuxt.js**: Server-side renderİçinde framework

# ### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency içiçindedejection, sİçindeleton pattern
- **RxJS**: Reactive programmİçinde, observables
- **Routİçinde**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive içinms
- **NgRx**: Redux-style state yönetim

# ## Build Tools ve Bundlers
- **Webpack**: Module bundlİçinde, code splittİçinde, loaders, plugiçiçindedes
- **Vite**: Fast build tool usİçinde native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized için libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler için backward compatibility
- **PostCSS**: CSS processİçinde ile plugiçiçindedes

# ## CSS Frameworks ve Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwiçiçindeded CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-içiçindede-JS library
- **Emotion**: CSS-içiçindede-JS ile source maps

# # Backend Geliştirme

# ## Server-Side Dils

# ### Node.js
- **Runtime**: JavaScript on bu server (V8 engiçiçindedee)
- **Express.js**: Miçiçindedeimal web framework, middleware mimari
- **NestJS**: Angular-içiçindedespired mimari, TypeScript
- **Fastify**: High-periçinmance framework
- **Koa**: Modern Express by same creators
- **Package Yönetim**: npm, yarn, pnpm

# ### Python
- **Django**: Full-featured framework, ORM, admiçiçindede panel, batteries-içiçindedecluded
- **Flask**: Micriçiçindederamework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

# ### Obur Backend Dils
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Sprİçinde**: Enterprise framework, dependency içiçindedejection
- **PHP Laravel**: Elegant sözdizimi, Eloquent ORM, Blade templatİçinde
- **Go Giçiçindede**: High periçinmance, miçiçindedeimal framework
- **Rust Actix**: Memory güvenlity, periçinmance
- **C# ASP.NET Core**: Cross-platiçinm, enterprise features

# ## Veribase Integration

# ### ORMs (Object-Relational Mappİçinde)
- **Sequelize**: Node.js ORM için SQL veribases
- **Prisma**: Type-güvenli veribase access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit ve ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

# ### Veribase Drivers
- **pg**: PostgreSQL client için Node.js
- **mysql2**: MySQL client ile promises
- **pymongo**: MongoDB driver için Python
- **redis**: Redis client için multiple dils

# ## API Geliştirme

# ### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Namİçinde**: Nouns, plural, hierarchical
- **Versionİçinde**: URL path, headers, query parameters
- **Aubuntication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

# ### GraphQL
- **Schema Defiçiçindedeition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level veri fetchİçinde
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetchİçinde, sİçindele endpoiçiçindedet, strong typİçinde

# ### gRPC
- **Protocol Buffers**: Interface defiçiçindedeition dil
- **HTTP/2**: Bidirectional streamİçinde
- **Use Cases**: Microservices i̇letişim, real-time applications

# ## Aubuntication ve Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party logiçiçindede
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise sİçindele sign-on
- **Password Hashİçinde**: bcrypt, argon2, scrypt
- **Multi-Factor Aubuntication**: TOTP, SMS, email codes

# # DevOps ve Dağıtım

# ## Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hostİçinde
- **Branchİçinde Strategies**: Git Flow, GitHub Flow, trunk-based geliştirme
- **CI/CD**: Automated testİçinde ve dağıtım pipeliçiçindedees

# ## Contaiçiçindedeerization
- **Docker**: Contaiçiçindedeer runtime, Dockerfile, images
- **Docker Compose**: Multi-contaiçiçindedeer orchestration
- **Contaiçiçindedeer Registries**: Docker Hub, AWS ECR, Google GCR
- **En İyi Uygulamalar**: Multi-stage builds, miçiçindedeimal base images

# ## Orchestration
- **Kubernetes**: Contaiçiçindedeer orchestration, pods, services, dağıtıms
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Liçiçindedekerd için microservices ağİçinde

# ## Cloud Platiçinms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engiçiçindedee, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machiçiçindedees, Blob Storage, Functions, AKS
- **Vercel**: Frontend dağıtım, serverless functions
- **Netlify**: Static site hostİçinde, serverless functions
- **Heroku**: Platiçinm as a Service (PaaS)
- **DigitalOcean**: Simplified cloud içiçindedefrastructure

# ## CI/CD Pipeliçiçindedees
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-içiçindede contiçiçindedeuous içiçindedetegration
- **Jenkiçiçindedes**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Contiçiçindedeuous içiçindedetegration service
- **ArgoCD**: GitOps contiçiçindedeuous delivery için Kubernetes

# ## Monitorİçinde ve Loggİçinde
- **Application Periçinmance**: New Relic, Veridog, AppDynamics
- **Error Trackİçinde**: Sentry, Rollbar, Bugsnag
- **Loggİçinde**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitorİçinde**: Pİçindedom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

# # Web Periçinmance

# ## Optimization Techniques
- **Code Splittİçinde**: Lazy loadİçinde, dynamic imports
- **Tree Shakİçinde**: Removİçinde unused code
- **Miçiçindedeification**: Reducİçinde file sizes
- **Compression**: Gzip, Brotli
- **Cachİçinde**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loadİçinde, responsive images
- **Critical CSS**: Inliçiçindedeİçinde above-bu-fold styles
- **Veribase Optimization**: Indexİçinde, query optimization, connection poolİçinde

# ## Core Web Vitals
- **LCP (Largest Contentful Paiçiçindedet)**: Loadİçinde periçinmance (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **IÇINDEP (Interaction to Next Paiçiçindedet)**: Responsiveness metric

# ## Content Delivery Ağs (CDNs)
- **Cloudflare**: Güvenlik, periçinmance, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platiçinm
- **StackPath**: Edge services

# # Web Güvenlik

# ## Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL içiçindedejection, commve içiçindedejection
- **Broken Aubuntication**: Session hijackİçinde, credential stuffİçinde
- **Sensitive Veri Exposure**: Unencrypted veri, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **Güvenlik Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scriptİçinde (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object içiçindedejection attacks
- **Usİçinde Components ile Known Vulnerabilities**: Outdated dependencies
- **Insufficient Loggİçinde & Monitorİçinde**: Undetected breaches

# ## Güvenlik En İyi Uygulamalar
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content Güvenlik Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user içiçindedeput
- **Output Encodİçinde**: Prevent içiçindedejection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limitİçinde**: Prevent brute içince attacks
- **Güvenlik Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scannİçinde**: npm audit, Snyk, Dependabot

# # Testİçinde

# ## Testİçinde Types
- **Unit Testİçinde**: Individual components/functions
- **Integration Testİçinde**: Component içiçindedeteractions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **Periçinmance Testİçinde**: Load, stress, spike testİçinde
- **Accessibility Testİçinde**: WCAG compliance

# ## Testİçinde Frameworks
- **Jest**: JavaScript testİçinde framework
- **Mocha**: Flexible test runner
- **pytest**: Python testİçinde framework
- **RSpec**: Ruby testİçinde framework
- **JUnit**: Java testİçinde framework

# ## E2E Testİçinde Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E testİçinde
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

# # Accessibility (a11y)

# ## WCAG Rehberliçiçindedees
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understveable**: Readable, predictable, içiçindedeput assistance
- **Robust**: Compatible ile assistive technologies

# ## Implementation
- **Semantic HTML**: Proper headİçinde hierarchy, lvemarks
- **ARIA Attributes**: Roles, states, properties
- **Focus Yönetim**: Visible focus içiçindededicators, logical tab order
- **Color Contrast**: Miçiçindedeimum 4.5:1 ratio için text
- **Screen Reader Testİçinde**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All içiçindedeteractive elements accessible

# # Progressive Web Apps (PWAs)

# ## PWA Features
- **Service Workers**: Offliçiçindedee functionality, background sync
- **Web App Manifest**: Install prompt, icons, bume colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

# ## Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditİçinde
- **PWA Builder**: Generate manifests ve icons

# # Emergİçinde Technologies

# ## WebAssembly (Wasm)
- **Purpose**: Run compiled code içiçindede browser at near-native speed
- **Dils**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editİçinde, cryptography, ML içiçindedeference

# ## Serverless Mimari
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server yönetim, auto-scalİçinde, pay-per-use
- **Considerations**: Cold stsanat, vendor lock-içiçindede, debuggİçinde complexity

# ## Jamstack Mimari
- **JavaScript**: Client-side içiçindedeteractivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Periçinmance, güvenlik, scalability, developer experience

# ## Real-Time İletişim
- **WebSockets**: Bidirectional i̇letişim
- **Server-Sent Olaylar**: Server-to-client streamİçinde
- **WebRTC**: Peer-to-peer video, audio, veri
- **Use Cases**: Chat, collaboration, live streamİçinde, gamİçinde

# ## Micro Frontends
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side içiçindedetegration
- **Benefits**: Independent dağıtıms, team autonomy
- **Challenges**: Consistency, periçinmance, complexity
