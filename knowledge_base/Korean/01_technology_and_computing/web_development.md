<!-- 
This file was automatically translated from English to Korean.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 웹 개발

# # Frontend 개발

# ## Core Technologies

# ### HTML (HyperText Markup 언어)
- **Semantic HTML**: Us에서g mean에서gful tags (`<header>`, `<nav>`, `<ma에서>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embedd에서g
- **Meta Tags**: SEO, viewport, character encod에서g
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, 웹 sockets

# ### CSS (Cascad에서g Style Sheets)
- **Box Model**: Content, padd에서g, border, marg에서
- **Layout 시스템**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Position에서g**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties 위한 그m에서g
- **Animations**: Transitions, keyframes, trans위한ms
- **Preprocessors**: Sass, Less (variables, mix에서s, nest에서g)

# ### JavaScript
- **DOM Manipulation**: Select에서g, creat에서g, modify에서g elements
- **이벤트**: Click, submit, keyboard, custom 이벤트, event delegation
- **ES6+ Features**: Arrow functions, destructur에서g, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typ에서g, 에서terfaces, generics, decorators

# ## Modern Frontend Frameworks

# ### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State 관리**: Context API, Redux, Zust와, Recoil
- **Rout에서g**: React Router (BrowserRouter, Routes, Route, L에서k)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient render에서g through diff에서g algorithm

# ### Vue.js
- **Options API**: 데이터, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-위한, v-b에서d, v-on, v-model
- **Vuex/P에서ia**: State 관리
- **Vue Router**: Client-side rout에서g
- **Nuxt.js**: Server-side render에서g framework

# ### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency 에서jection, s에서gleton pattern
- **RxJS**: Reactive programm에서g, observables
- **Rout에서g**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive 위한ms
- **NgRx**: Redux-style state 관리

# ## Build Tools 와 Bundlers
- **웹pack**: Module bundl에서g, code splitt에서g, loaders, plug에서s
- **Vite**: Fast build tool us에서g native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized 위한 libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler 위한 backward compatibility
- **PostCSS**: CSS process에서g 와 함께 plug에서s

# ## CSS Frameworks 와 Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailw에서d CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-에서-JS library
- **Emotion**: CSS-에서-JS 와 함께 source maps

# # Backend 개발

# ## Server-Side 언어s

# ### Node.js
- **Runtime**: JavaScript on 그 server (V8 eng에서e)
- **Express.js**: M에서imal 웹 framework, middleware 아키텍처
- **NestJS**: Angular-에서spired 아키텍처, TypeScript
- **Fastify**: High-per위한mance framework
- **Koa**: Modern Express by same creators
- **Package 관리**: npm, yarn, pnpm

# ### Python
- **Django**: Full-featured framework, ORM, adm에서 panel, batteries-에서cluded
- **Flask**: Micr의ramework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

# ### O그r Backend 언어s
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spr에서g**: Enterprise framework, dependency 에서jection
- **PHP Laravel**: Elegant 구문, Eloquent ORM, Blade templat에서g
- **Go G에서**: High per위한mance, m에서imal framework
- **Rust Actix**: Memory 안전한ty, per위한mance
- **C# ASP.NET Core**: Cross-plat위한m, enterprise features

# ## 데이터base Integration

# ### ORMs (Object-Relational Mapp에서g)
- **Sequelize**: Node.js ORM 위한 SQL 데이터bases
- **Prisma**: Type-안전한 데이터base access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit 와 ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

# ### 데이터base Drivers
- **pg**: PostgreSQL client 위한 Node.js
- **mysql2**: MySQL client 와 함께 promises
- **pymongo**: MongoDB driver 위한 Python
- **redis**: Redis client 위한 multiple 언어s

# ## API 개발

# ### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Nam에서g**: Nouns, plural, hierarchical
- **Version에서g**: URL path, headers, query parameters
- **Au그ntication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

# ### GraphQL
- **Schema Def에서ition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level 데이터 fetch에서g
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetch에서g, s에서gle endpo에서t, strong typ에서g

# ### gRPC
- **Protocol Buffers**: Interface def에서ition 언어
- **HTTP/2**: Bidirectional stream에서g
- **Use Cases**: Microservices 의사소통, real-time applications

# ## Au그ntication 와 Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON 웹 Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party log에서
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise s에서gle sign-on
- **Password Hash에서g**: bcrypt, argon2, scrypt
- **Multi-Factor Au그ntication**: TOTP, SMS, email codes

# # DevOps 와 배포

# ## Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository host에서g
- **Branch에서g Strategies**: Git Flow, GitHub Flow, trunk-based 개발
- **CI/CD**: Automated test에서g 와 배포 pipel에서es

# ## Conta에서erization
- **Docker**: Conta에서er runtime, Dockerfile, images
- **Docker Compose**: Multi-conta에서er orchestration
- **Conta에서er Registries**: Docker Hub, AWS ECR, Google GCR
- **모범 사례**: Multi-stage builds, m에서imal base images

# ## Orchestration
- **Kubernetes**: Conta에서er orchestration, pods, services, 배포s
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, L에서kerd 위한 microservices 네트워크에서g

# ## Cloud Plat위한ms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Eng에서e, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Mach에서es, Blob Storage, Functions, AKS
- **Vercel**: Frontend 배포, serverless functions
- **Netlify**: Static site host에서g, serverless functions
- **Heroku**: Plat위한m as a Service (PaaS)
- **DigitalOcean**: Simplified cloud 에서frastructure

# ## CI/CD Pipel에서es
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-에서 cont에서uous 에서tegration
- **Jenk에서s**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Cont에서uous 에서tegration service
- **ArgoCD**: GitOps cont에서uous delivery 위한 Kubernetes

# ## Monitor에서g 와 Logg에서g
- **Application Per위한mance**: New Relic, 데이터dog, AppDynamics
- **Error Track에서g**: Sentry, Rollbar, Bugsnag
- **Logg에서g**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitor에서g**: P에서gdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

# # 웹 Per위한mance

# ## Optimization Techniques
- **Code Splitt에서g**: Lazy load에서g, dynamic imports
- **Tree Shak에서g**: Remov에서g unused code
- **M에서ification**: Reduc에서g file sizes
- **Compression**: Gzip, Brotli
- **Cach에서g**: Browser cache, CDN, service workers
- **Image Optimization**: 웹P, AVIF, lazy load에서g, responsive images
- **Critical CSS**: Inl에서에서g above-그-fold styles
- **데이터base Optimization**: Index에서g, query optimization, connection pool에서g

# ## Core 웹 Vitals
- **LCP (Largest Contentful Pa에서t)**: Load에서g per위한mance (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **에서P (Interaction to Next Pa에서t)**: Responsiveness metric

# ## Content Delivery 네트워크s (CDNs)
- **Cloudflare**: 보안, per위한mance, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud plat위한m
- **StackPath**: Edge services

# # 웹 보안

# ## Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL 에서jection, comm와 에서jection
- **Broken Au그ntication**: Session hijack에서g, credential stuff에서g
- **Sensitive 데이터 Exposure**: Unencrypted 데이터, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **보안 Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Script에서g (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object 에서jection attacks
- **Us에서g Components 와 함께 Known Vulnerabilities**: Outdated dependencies
- **Insufficient Logg에서g & Monitor에서g**: Undetected breaches

# ## 보안 모범 사례
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content 보안 Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user 에서put
- **Output Encod에서g**: Prevent 에서jection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limit에서g**: Prevent brute 위한ce attacks
- **보안 Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scann에서g**: npm audit, Snyk, Dependabot

# # Test에서g

# ## Test에서g Types
- **Unit Test에서g**: Individual components/functions
- **Integration Test에서g**: Component 에서teractions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **Per위한mance Test에서g**: Load, stress, spike test에서g
- **Accessibility Test에서g**: WCAG compliance

# ## Test에서g Frameworks
- **Jest**: JavaScript test에서g framework
- **Mocha**: Flexible test runner
- **pytest**: Python test에서g framework
- **RSpec**: Ruby test에서g framework
- **JUnit**: Java test에서g framework

# ## E2E Test에서g Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E test에서g
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

# # Accessibility (a11y)

# ## WCAG 가이드l에서es
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Underst와able**: Readable, predictable, 에서put assistance
- **Robust**: Compatible 와 함께 assistive technologies

# ## Implementation
- **Semantic HTML**: Proper head에서g hierarchy, l와marks
- **ARIA Attributes**: Roles, states, properties
- **Focus 관리**: Visible focus 에서dicators, logical tab order
- **Color Contrast**: M에서imum 4.5:1 ratio 위한 text
- **Screen Reader Test에서g**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All 에서teractive elements accessible

# # Progressive 웹 Apps (PWAs)

# ## PWA Features
- **Service Workers**: Offl에서e functionality, background sync
- **웹 App Manifest**: Install prompt, icons, 그me colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

# ## Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA audit에서g
- **PWA Builder**: Generate manifests 와 icons

# # Emerg에서g Technologies

# ## 웹Assembly (Wasm)
- **Purpose**: Run compiled code 에서 browser at near-native speed
- **언어s**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video edit에서g, cryptography, ML 에서ference

# ## Serverless 아키텍처
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server 관리, auto-scal에서g, pay-per-use
- **Considerations**: Cold st예술, vendor lock-에서, debugg에서g complexity

# ## Jamstack 아키텍처
- **JavaScript**: Client-side 에서teractivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Per위한mance, 보안, scalability, developer experience

# ## Real-Time 의사소통
- **웹Sockets**: Bidirectional 의사소통
- **Server-Sent 이벤트**: Server-to-client stream에서g
- **웹RTC**: Peer-to-peer video, audio, 데이터
- **Use Cases**: Chat, collaboration, live stream에서g, gam에서g

# ## Micro Frontends
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side 에서tegration
- **Benefits**: Independent 배포s, team autonomy
- **Challenges**: Consistency, per위한mance, complexity
