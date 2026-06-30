<!-- 
This file was automatically translated from English to German.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Web Entwicklung

# # Frontend Entwicklung

# ## Core Technologies

# ### HTML (HyperText Markup Sprache)
- **Semantic HTML**: Using meaningful tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embedding
- **Meta Tags**: SEO, viewport, character encoding
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, web sockets

# ### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **Layout Systeme**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties für der/die/dasming
- **Animations**: Transitions, keyframes, transfürms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

# ### JavaScript
- **DOM Manipulation**: Selecting, creating, modifying elements
- **Ereignisse**: Click, submit, keyboard, custom ereignisse, event delegation
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typing, interfaces, generics, decorators

# ## Modern Frontend Frameworks

# ### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State Verwaltung**: Context API, Redux, Zustund, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Efficient rendering through diffing algorithm

# ### Vue.js
- **Options API**: daten, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-für, v-bind, v-on, v-model
- **Vuex/Pinia**: State verwaltung
- **Vue Router**: Client-side routing
- **Nuxt.js**: Server-side rendering framework

# ### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Dependency injection, singleton pattern
- **RxJS**: Reactive programming, observables
- **Routing**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive fürms
- **NgRx**: Redux-style state verwaltung

# ## Build Tools und Bundlers
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Fast build tool using native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized für libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler für backward compatibility
- **PostCSS**: CSS processing mit plugins

# ## CSS Frameworks und Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-in-JS library
- **Emotion**: CSS-in-JS mit source maps

# # Backend Entwicklung

# ## Server-Side Spraches

# ### Node.js
- **Runtime**: JavaScript on der/die/das server (V8 engine)
- **Express.js**: Minimal web framework, middleware architektur
- **NestJS**: Angular-inspired architektur, TypeScript
- **Fastify**: High-perfürmance framework
- **Koa**: Modern Express by same creators
- **Package Verwaltung**: npm, yarn, pnpm

# ### Python
- **Django**: Full-featured framework, ORM, admin panel, batteries-included
- **Flask**: Micrvonramework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

# ### Oder/die/dasr Backend Spraches
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant syntax, Eloquent ORM, Blade templating
- **Go Gin**: High perfürmance, minimal framework
- **Rust Actix**: Memory sicherty, perfürmance
- **C# ASP.NET Core**: Cross-platfürm, enterprise features

# ## Datenbase Integration

# ### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM für SQL datenbases
- **Prisma**: Type-sicher datenbase access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit und ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

# ### Datenbase Drivers
- **pg**: PostgreSQL client für Node.js
- **mysql2**: MySQL client mit promises
- **pymongo**: MongoDB driver für Python
- **redis**: Redis client für multiple spraches

# ## API Entwicklung

# ### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Nouns, plural, hierarchical
- **Versioning**: URL path, headers, query parameters
- **Auder/die/dasntication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

# ### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level daten fetching
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetching, single endpoint, strong typing

# ### gRPC
- **Protocol Buffers**: Interface definition sprache
- **HTTP/2**: Bidirectional streaming
- **Use Cases**: Microservices kommunikation, real-time applications

# ## Auder/die/dasntication und Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party login
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Auder/die/dasntication**: TOTP, SMS, email codes

# # DevOps und Bereitstellung

# ## Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hosting
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based entwicklung
- **CI/CD**: Automated testen und bereitstellung pipelines

# ## Containerization
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Multi-container orchestration
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Multi-stage builds, minimal base images

# ## Orchestration
- **Kubernetes**: Container orchestration, pods, services, bereitstellungs
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Linkerd für microservices netzwerking

# ## Cloud Platfürms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend bereitstellung, serverless functions
- **Netlify**: Static site hosting, serverless functions
- **Heroku**: Platfürm as a Service (PaaS)
- **DigitalOcean**: Simplified cloud infrastructure

# ## CI/CD Pipelines
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-in continuous integration
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Continuous integration service
- **ArgoCD**: GitOps continuous delivery für Kubernetes

# ## Monitoring und Logging
- **Application Perfürmance**: New Relic, Datendog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

# # Web Perfürmance

# ## Optimization Techniques
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Removing unused code
- **Minification**: Reducing file sizes
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Inlining above-der/die/das-fold styles
- **Datenbase Optimization**: Indexing, query optimization, connection pooling

# ## Core Web Vitals
- **LCP (Largest Contentful Paint)**: Loading perfürmance (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **INP (Interaction to Next Paint)**: Responsiveness metric

# ## Content Delivery Netzwerks (CDNs)
- **Cloudflare**: Sicherheit, perfürmance, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platfürm
- **StackPath**: Edge services

# # Web Sicherheit

# ## Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL injection, commund injection
- **Broken Auder/die/dasntication**: Session hijacking, credential stuffing
- **Sensitive Daten Exposure**: Unencrypted daten, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **Sicherheit Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object injection attacks
- **Using Components mit Known Vulnerabilities**: Outdated dependencies
- **Insufficient Logging & Monitoring**: Undetected breaches

# ## Sicherheit Best Practices
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content Sicherheit Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user input
- **Output Encoding**: Prevent injection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Prevent brute fürce attacks
- **Sicherheit Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

# # Testen

# ## Testen Types
- **Unit Testen**: Individual components/functions
- **Integration Testen**: Component interactions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **Perfürmance Testen**: Load, stress, spike testen
- **Accessibility Testen**: WCAG compliance

# ## Testen Frameworks
- **Jest**: JavaScript testen framework
- **Mocha**: Flexible test runner
- **pytest**: Python testen framework
- **RSpec**: Ruby testen framework
- **JUnit**: Java testen framework

# ## E2E Testen Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E testen
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

# # Accessibility (a11y)

# ## WCAG Leitfadenlines
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understundable**: Readable, predictable, input assistance
- **Robust**: Compatible mit assistive technologies

# ## Implementation
- **Semantic HTML**: Proper heading hierarchy, lundmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus Verwaltung**: Visible focus indicators, logical tab order
- **Color Contrast**: Minimum 4.5:1 ratio für text
- **Screen Reader Testen**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: All interactive elements accessible

# # Progressive Web Apps (PWAs)

# ## PWA Features
- **Service Workers**: Offline functionality, background sync
- **Web App Manifest**: Install prompt, icons, der/die/dasme colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: Works on all devices
- **HTTPS Required**: Secure context

# ## Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditing
- **PWA Builder**: Generate manifests und icons

# # Emerging Technologies

# ## WebAssembly (Wasm)
- **Purpose**: Run compiled code in browser at near-native speed
- **Spraches**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editing, cryptography, ML inference

# ## Serverless Architektur
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server verwaltung, auto-scaling, pay-per-use
- **Considerations**: Cold stkünste, vendor lock-in, debugging complexity

# ## Jamstack Architektur
- **JavaScript**: Client-side interactivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Perfürmance, sicherheit, scalability, developer experience

# ## Real-Time Kommunikation
- **WebSockets**: Bidirectional kommunikation
- **Server-Sent Ereignisse**: Server-to-client streaming
- **WebRTC**: Peer-to-peer video, audio, daten
- **Use Cases**: Chat, collaboration, live streaming, gaming

# ## Micro Frontends
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Independent bereitstellungs, team autonomy
- **Challenges**: Consistency, perfürmance, complexity
