# वेब विकास

## फ्रंटएंड विकास

### मुख्य तकनीकें

#### HTML (HyperText Markup Language)
- **Semantic HTML**: अर्थपूर्ण tags का उपयोग (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input के प्रकार, validation, accessibility labels
- **Media**: Images, video, audio को embed करना
- **Meta Tags**: SEO, viewport, character encoding
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, web sockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **Layout Systems**:
  - **Flexbox**: एक-आयामी layouts, justify-content, align-items
  - **Grid**: द्वि-आयामी layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Theme बनाने के लिए custom properties
- **Animations**: Transitions, keyframes, transforms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipulation**: Elements का चयन, निर्माण, और संशोधन
- **Events**: Click, submit, keyboard, custom events, event delegation
- **ES6+ Features**: Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Static typing, interfaces, generics, decorators

### आधुनिक फ्रंटएंड frameworks

#### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **State Management**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Diffing algorithm के माध्यम से कुशल rendering

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
- **NgRx**: Redux-style state management

### Build tools और bundlers
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Native ES modules का उपयोग करने वाला तेज़ build tool
- **Parcel**: Zero-configuration bundler
- **Rollup**: Libraries के लिए optimized
- **esbuild**: अत्यंत तेज़ JavaScript bundler
- **Babel**: Backward compatibility के लिए JavaScript transpiler
- **PostCSS**: Plugins के साथ CSS processing

### CSS frameworks और libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google की Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-in-JS library
- **Emotion**: Source maps के साथ CSS-in-JS

## बैकएंड विकास

### Server-side भाषाएँ

#### Node.js
- **Runtime**: Server पर JavaScript (V8 engine)
- **Express.js**: Minimal web framework, middleware architecture
- **NestJS**: Angular-प्रेरित architecture, TypeScript
- **Fastify**: High-performance framework
- **Koa**: उन्हीं creators द्वारा बनाया गया आधुनिक Express
- **Package Management**: npm, yarn, pnpm

#### Python
- **Django**: पूर्ण-विशेषताओं वाला framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, extensions ecosystem
- **FastAPI**: आधुनिक, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

#### अन्य बैकएंड भाषाएँ
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant syntax, Eloquent ORM, Blade templating
- **Go Gin**: High performance, minimal framework
- **Rust Actix**: Memory safety, performance
- **C# ASP.NET Core**: cross-platform समर्थन, enterprise सुविधाएँ

### Database integration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: SQL databases के लिए Node.js ORM
- **Prisma**: type-safe database access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit और ORM
- **ActiveRecord**: Ruby on Rails का ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### Database drivers
- **pg**: Node.js के लिए PostgreSQL client
- **mysql2**: Promises के साथ MySQL client
- **pymongo**: Python के लिए MongoDB driver
- **redis**: कई भाषाओं के लिए Redis client

### API विकास

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Nouns, plural, hierarchical naming
- **Versioning**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level data fetching
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook का GraphQL client
- **Advantages**: अनावश्यक data over-fetching नहीं, single endpoint, strong typing

#### gRPC
- **Protocol Buffers**: Interface definition language
- **HTTP/2**: Bidirectional streaming
- **Use Cases**: Microservices communication, real-time applications

### Authentication और authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party login
- **OpenID Connect**: OAuth 2.0 पर identity layer
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, email codes

## DevOps और deployment

### Version control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hosting
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Automated testing और deployment pipelines

### Containerization
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Multi-container orchestration
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Multi-stage builds, minimal base images

### Orchestration
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes package manager
- **Service Mesh**: Microservices networking के लिए Istio, Linkerd

### Cloud platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend deployment, serverless functions
- **Netlify**: Static site hosting, serverless functions
- **Heroku**: Platform as a Service (PaaS) मंच
- **DigitalOcean**: सरल cloud infrastructure

### CI/CD pipelines
- **GitHub Actions**: workflow automation
- **GitLab CI**: built-in continuous integration
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Continuous integration service
- **ArgoCD**: Kubernetes के लिए GitOps continuous delivery

### Monitoring और logging
- **Application Performance**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## वेब प्रदर्शन

### अनुकूलन तकनीकें
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Unused code हटाना
- **Minification**: File sizes कम करना
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Above-the-fold styles को inline करना
- **Database Optimization**: Indexing, query optimization, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Loading performance (<2.5s)
- **FID (First Input Delay)**: Interactivity (<100ms)
- **CLS (Cumulative Layout Shift)**: Visual stability (<0.1)
- **INP (Interaction to Next Paint)**: Responsiveness metric

### Content Delivery Networks (CDNs)
- **Cloudflare**: Security, performance, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: Edge cloud platform
- **StackPath**: Edge services

## वेब सुरक्षा

### सामान्य कमजोरियाँ (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Session hijacking, credential stuffing
- **Sensitive Data Exposure**: बिना एन्क्रिप्ट किया गया data, कमज़ोर cryptography
- **XML External Entities (XXE)**: XML parser की कमजोरियाँ
- **Broken Access Control**: privilege escalation, अनधिकृत access
- **Security Misconfiguration**: default credentials, अत्यधिक verbose errors
- **Cross-Site Scripting (XSS)**: reflected, stored, DOM-based
- **Insecure Deserialization**: object injection attacks
- **Using Components with Known Vulnerabilities**: ज्ञात कमजोरियों वाली पुरानी dependencies का उपयोग
- **Insufficient Logging & Monitoring**: ऐसी breaches जो पकड़ी न जाएँ

### सुरक्षा की सर्वोत्तम प्रथाएँ
- **HTTPS**: TLS/SSL एन्क्रिप्शन, HSTS
- **Content Security Policy (CSP)**: XSS attacks को रोकना
- **Input Validation**: User input को sanitize करना
- **Output Encoding**: Injection attacks को रोकना
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Brute force attacks को रोकना
- **Security Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Testing

### Testing के प्रकार
- **Unit Testing**: व्यक्तिगत components/functions
- **Integration Testing**: Components के बीच interactions
- **End-to-End (E2E)**: पूर्ण user workflows
- **Visual Regression**: UI changes का पता लगाना
- **Performance Testing**: Load, stress, spike testing
- **Accessibility Testing**: WCAG compliance

### Testing frameworks
- **Jest**: JavaScript testing framework
- **Mocha**: Flexible test runner
- **pytest**: Python testing framework
- **RSpec**: Ruby testing framework
- **JUnit**: Java testing framework

### E2E testing tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E testing
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

## Accessibility (a11y)

### WCAG guidelines
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, पर्याप्त समय, no seizures
- **Understandable**: Readable, predictable, input assistance
- **Robust**: Assistive technologies के साथ compatible

### Implementation
- **Semantic HTML**: उचित heading hierarchy, landmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus Management**: Visible focus indicators, logical tab order
- **Color Contrast**: Text के लिए न्यूनतम 4.5:1 ratio
- **Screen Reader Testing**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: सभी interactive elements accessible

## Progressive Web Apps (PWAs)

### PWA features
- **Service Workers**: Offline functionality, background sync
- **Web App Manifest**: Install prompt, icons, theme colors
- **App Shell**: Cached UI skeleton
- **Push Notifications**: User engagement
- **Responsive Design**: सभी devices पर काम करता है
- **HTTPS Required**: Secure context

### Tools
- **Workbox**: Service worker libraries
- **Lighthouse**: PWA auditing
- **PWA Builder**: Manifests और icons generate करना

## उभरती हुई तकनीकें

### WebAssembly (Wasm)
- **Purpose**: Browser में near-native speed पर compiled code चलाना
- **Languages**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editing, cryptography, ML inference

### Serverless Architecture
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: Server management की आवश्यकता नहीं, auto-scaling, pay-per-use
- **Considerations**: Cold starts, vendor lock-in, debugging complexity

### Jamstack Architecture
- **JavaScript**: Client-side interactivity
- **APIs**: Serverless functions, third-party services
- **Markup**: Pre-built static files
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: Performance, security, scalability, developer experience

### Real-Time Communication
- **WebSockets**: Bidirectional communication
- **Server-Sent Events**: Server-to-client streaming
- **WebRTC**: Peer-to-peer video, audio, data
- **Use Cases**: Chat, collaboration, live streaming, gaming

### Micro Frontends
- **Concept**: Microservices को frontend तक विस्तारित करना
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Independent deployments, team autonomy
- **Challenges**: Consistency, performance, complexity
