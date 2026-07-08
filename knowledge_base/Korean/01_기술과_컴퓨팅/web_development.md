<!-- 
This file was automatically translated from English to Korean.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 웹 개발

## Frontend 개발

### Core Technologies

#### HTML (HyperText Markup 언어)
- **Semantic HTML**: Using meaningful tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embedding
- **Meta Tags**: SEO, viewport, character encoding
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, 웹 sockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **Layout 시스템**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties 위한 theming
- **Animations**: Transitions, keyframes, transforms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipulation**: Selecting, creating, modifying elements
- **이벤트**: Click, submit, keyboard, custom 이벤트, event delegation
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typing, interfaces, generics, decorators

### Modern Frontend Frameworks

#### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State 관리**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient rendering through diffing algorithm

#### Vue.js
- **Options API**: 데이터, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-위한, v-bind, v-on, v-model
- **Vuex/Pinia**: State 관리
- **Vue Router**: Client-side routing
- **Nuxt.js**: Server-side rendering framework

#### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency injection, singleton pattern
- **RxJS**: Reactive programming, observables
- **Routing**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive forms
- **NgRx**: Redux-style state 관리

### Build Tools 와 Bundlers
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Fast build tool using native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized 위한 libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler 위한 backward compatibility
- **PostCSS**: CSS processing 와 함께 plugins

### CSS Frameworks 와 Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-에서-JS library
- **Emotion**: CSS-에서-JS 와 함께 source maps

## Backend 개발

### Server-Side Languages

#### Node.js
- **Runtime**: JavaScript on 그 server (V8 engine)
- **Express.js**: Minimal 웹 framework, middleware 아키텍처
- **NestJS**: Angular-inspired 아키텍처, TypeScript
- **Fastify**: High-성능 framework
- **Koa**: Modern Express by same creators
- **Package 관리**: npm, yarn, pnpm

#### Python
- **Django**: Full-featured framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

#### Other Backend Languages
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant 구문, Eloquent ORM, Blade templating
- **Go Gin**: High 성능, minimal framework
- **Rust Actix**: Memory safety, 성능
- **C# ASP.NET Core**: Cross-platform, enterprise features

### 데이터베이스 Integration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM 위한 SQL databases
- **Prisma**: Type-안전한 데이터베이스 access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit 와 ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### 데이터베이스 Drivers
- **pg**: PostgreSQL client 위한 Node.js
- **mysql2**: MySQL client 와 함께 promises
- **pymongo**: MongoDB driver 위한 Python
- **redis**: Redis client 위한 multiple languages

### API 개발

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Nouns, plural, hierarchical
- **Versioning**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level 데이터 fetching
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetching, single endpoint, strong typing

#### gRPC
- **Protocol Buffers**: Interface definition 언어
- **HTTP/2**: Bidirectional streaming
- **Use Cases**: Microservices 의사소통, real-time applications

### Authentication 와 Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON 웹 Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party login
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, email codes

## DevOps 와 배포

### Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hosting
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based 개발
- **CI/CD**: Automated 테스트 와 배포 pipelines

### Containerization
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Multi-container orchestration
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **모범 사례**: Multi-stage builds, minimal base images

### Orchestration
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Linkerd 위한 microservices networking

### Cloud Platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend 배포, serverless functions
- **Netlify**: Static site hosting, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Simplified cloud infrastructure

### CI/CD Pipelines
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-에서 continuous integration
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Continuous integration service
- **ArgoCD**: GitOps continuous delivery 위한 Kubernetes

### Monitoring 와 Logging
- **Application 성능**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## 웹 성능

### Optimization Techniques
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Removing unused code
- **Minification**: Reducing file sizes
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Inlining above-그-fold styles
- **데이터베이스 Optimization**: Indexing, query optimization, connection pooling

### Core 웹 Vitals
- **LCP (Largest Contentful Paint)**: Loading 성능 (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **INP (Interaction to Next Paint)**: Responsiveness metric

### Content Delivery Networks (CDNs)
- **Cloudflare**: 보안, 성능, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platform
- **StackPath**: Edge services

## 웹 보안

### Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Session hijacking, credential stuffing
- **Sensitive 데이터 Exposure**: Unencrypted 데이터, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **보안 Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object injection attacks
- **Using Components 와 함께 Known Vulnerabilities**: Outdated dependencies
- **Insufficient Logging & Monitoring**: Undetected breaches

### 보안 모범 사례
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content 보안 Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user input
- **Output Encoding**: Prevent injection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Prevent brute force attacks
- **보안 Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## 테스트

### 테스트 Types
- **Unit 테스트**: Individual components/functions
- **Integration 테스트**: Component interactions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **성능 테스트**: Load, stress, spike 테스트
- **Accessibility 테스트**: WCAG compliance

### 테스트 Frameworks
- **Jest**: JavaScript 테스트 framework
- **Mocha**: Flexible test runner
- **pytest**: Python 테스트 framework
- **RSpec**: Ruby 테스트 framework
- **JUnit**: Java 테스트 framework

### E2E 테스트 Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E 테스트
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

## Accessibility (a11y)

### WCAG Guidelines
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understandable**: Readable, predictable, input assistance
- **Robust**: Compatible 와 함께 assistive technologies

### Implementation
- **Semantic HTML**: Proper heading hierarchy, landmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus 관리**: Visible focus indicators, logical tab order
- **Color Contrast**: Minimum 4.5:1 ratio 위한 text
- **Screen Reader 테스트**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All interactive elements accessible

## Progressive 웹 Apps (PWAs)

### PWA Features
- **Service Workers**: Offline functionality, background sync
- **웹 App Manifest**: Install prompt, icons, theme colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

### Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditing
- **PWA Builder**: Generate manifests 와 icons

## Emerging Technologies

### WebAssembly (Wasm)
- **Purpose**: Run compiled code 에서 browser at near-native speed
- **Languages**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editing, cryptography, ML inference

### Serverless 아키텍처
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server 관리, auto-scaling, pay-per-use
- **고려사항**: Cold starts, vendor lock-in, 디버깅 복잡성

### Jamstack 아키텍처
- **JavaScript**: Client-side interactivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: 성능, 보안, scalability, developer experience

### Real-Time 의사소통
- **WebSockets**: Bidirectional 의사소통
- **Server-Sent 이벤트**: Server-to-client streaming
- **WebRTC**: Peer-to-peer video, audio, 데이터
- **Use Cases**: Chat, collaboration, live streaming, gaming

### Micro Frontends
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Independent deployments, team autonomy
- **Challenges**: Consistency, 성능, complexity
