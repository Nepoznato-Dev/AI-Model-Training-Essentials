<!-- 
This file was automatically translated from English to Turkish.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Web Geliştirme

## Frontend Geliştirme

### Core Technologies

#### HTML (HyperText Markup Dil)
- **Semantic HTML**: Using meaningful tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embedding
- **Meta Tags**: SEO, viewport, character encoding
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, Web sockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **Layout Sistemler**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties için theming
- **Animations**: Transitions, keyframes, transforms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipulation**: Selecting, creating, modifying elements
- **Olaylar**: Click, submit, keyboard, custom Olaylar, event delegation
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typing, interfaces, generics, decorators

### Modern Frontend Frameworks

#### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State Yönetim**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient rendering through diffing algorithm

#### Vue.js
- **Options API**: Veri, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-için, v-bind, v-on, v-model
- **Vuex/Pinia**: State Yönetim
- **Vue Router**: Client-side routing
- **Nuxt.js**: Server-side rendering framework

#### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency injection, singleton pattern
- **RxJS**: Reactive programming, observables
- **Routing**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive forms
- **NgRx**: Redux-style state Yönetim

### Build Tools ve Bundlers
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Fast build tool using native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized için libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler için backward compatibility
- **PostCSS**: CSS processing ile plugins

### CSS Frameworks ve Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-içinde-JS library
- **Emotion**: CSS-içinde-JS ile source maps

## Backend Geliştirme

### Server-Side Languages

#### Node.js
- **Runtime**: JavaScript on bu server (V8 engine)
- **Express.js**: Minimal Web framework, middleware Mimari
- **NestJS**: Angular-inspired Mimari, TypeScript
- **Fastify**: High-Performans framework
- **Koa**: Modern Express by same creators
- **Package Yönetim**: npm, yarn, pnpm

#### Python
- **Django**: Full-featured framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

#### Other Backend Languages
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant Sözdizimi, Eloquent ORM, Blade templating
- **Go Gin**: High Performans, minimal framework
- **Rust Actix**: Memory safety, Performans
- **C# ASP.NET Core**: Cross-platform, enterprise features

### Veritabanı Integration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM için SQL databases
- **Prisma**: Type-Güvenli Veritabanı access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit ve ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### Veritabanı Drivers
- **pg**: PostgreSQL client için Node.js
- **mysql2**: MySQL client ile promises
- **pymongo**: MongoDB driver için Python
- **redis**: Redis client için multiple languages

### API Geliştirme

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Nouns, plural, hierarchical
- **Versioning**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level Veri fetching
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetching, single endpoint, strong typing

#### gRPC
- **Protocol Buffers**: Interface definition Dil
- **HTTP/2**: Bidirectional streaming
- **Use Cases**: Microservices İletişim, real-time applications

### Authentication ve Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party login
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, email codes

## DevOps ve Dağıtım

### Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hosting
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based Geliştirme
- **CI/CD**: Automated Test Etme ve Dağıtım pipelines

### Containerization
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Multi-container orchestration
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **En İyi Uygulamalar**: Multi-stage builds, minimal base images

### Orchestration
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Linkerd için microservices networking

### Cloud Platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend Dağıtım, serverless functions
- **Netlify**: Static site hosting, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Simplified cloud infrastructure

### CI/CD Pipelines
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-içinde continuous integration
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Continuous integration service
- **ArgoCD**: GitOps continuous delivery için Kubernetes

### Monitoring ve Logging
- **Application Performans**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Web Performans

### Optimization Techniques
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Removing unused code
- **Minification**: Reducing file sizes
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Inlining above-bu-fold styles
- **Veritabanı Optimization**: Indexing, query optimization, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Loading Performans (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **INP (Interaction to Next Paint)**: Responsiveness metric

### Content Delivery Networks (CDNs)
- **Cloudflare**: Güvenlik, Performans, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platform
- **StackPath**: Edge services

## Web Güvenlik

### Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Session hijacking, credential stuffing
- **Sensitive Veri Exposure**: Unencrypted Veri, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **Güvenlik Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object injection attacks
- **Using Components ile Known Vulnerabilities**: Outdated dependencies
- **Insufficient Logging & Monitoring**: Undetected breaches

### Güvenlik En İyi Uygulamalar
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content Güvenlik Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user input
- **Output Encoding**: Prevent injection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Prevent brute force attacks
- **Güvenlik Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Test Etme

### Test Etme Types
- **Unit Test Etme**: Individual components/functions
- **Integration Test Etme**: Component interactions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **Performans Test Etme**: Load, stress, spike Test Etme
- **Accessibility Test Etme**: WCAG compliance

### Test Etme Frameworks
- **Jest**: JavaScript Test Etme framework
- **Mocha**: Flexible test runner
- **pytest**: Python Test Etme framework
- **RSpec**: Ruby Test Etme framework
- **JUnit**: Java Test Etme framework

### E2E Test Etme Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E Test Etme
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

## Accessibility (a11y)

### WCAG Guidelines
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understandable**: Readable, predictable, input assistance
- **Robust**: Compatible ile assistive technologies

### Implementation
- **Semantic HTML**: Proper heading hierarchy, landmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus Yönetim**: Visible focus indicators, logical tab order
- **Color Contrast**: Minimum 4.5:1 ratio için text
- **Screen Reader Test Etme**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All interactive elements accessible

## Progressive Web Apps (PWAs)

### PWA Features
- **Service Workers**: Offline functionality, background sync
- **Web App Manifest**: Install prompt, icons, theme colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

### Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditing
- **PWA Builder**: Generate manifests ve icons

## Emerging Technologies

### WebAssembly (Wasm)
- **Purpose**: Run compiled code içinde browser at near-native speed
- **Languages**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editing, cryptography, ML inference

### Serverless Mimari
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server Yönetim, auto-scaling, pay-per-use
- **Considerations**: Cold starts, vendor lock-içinde, debugging complexity

### Jamstack Mimari
- **JavaScript**: Client-side interactivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Performans, Güvenlik, scalability, developer experience

### Real-Time İletişim
- **WebSockets**: Bidirectional İletişim
- **Server-Sent Olaylar**: Server-to-client streaming
- **WebRTC**: Peer-to-peer video, audio, Veri
- **Use Cases**: Chat, collaboration, live streaming, gaming

### Micro Frontends
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Independent deployments, team autonomy
- **Challenges**: Consistency, Performans, complexity
