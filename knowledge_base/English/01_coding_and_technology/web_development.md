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
# Web Development

## Frontend Development

### Core Technologies

#### HTML (HyperText Markup Language)
- **Semantic HTML**: Using meaningful tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input types, validation, accessibility labels
- **Media**: Images, video, audio embedding
- **Meta Tags**: SEO, viewport, character encoding
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, web sockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Content, padding, border, margin
- **Layout Systems**:
  - **Flexbox**: One-dimensional layouts, justify-content, align-items
  - **Grid**: Two-dimensional layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsive Design**: Media queries, mobile-first approach
- **CSS Variables**: Custom properties for theming
- **Animations**: Transitions, keyframes, transforms
- **Preprocessors**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **DOM Manipulation**: Selecting, creating, modifying elements
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
- **Virtual DOM**: Efficient rendering through diffing algorithm

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

### Build Tools and Bundlers
- **Webpack**: Module bundling, code splitting, loaders, plugins
- **Vite**: Fast build tool using native ES modules
- **Parcel**: Zero-configuration bundler
- **Rollup**: Optimized for libraries
- **esbuild**: Extremely fast JavaScript bundler
- **Babel**: JavaScript transpiler for backward compatibility
- **PostCSS**: CSS processing with plugins

### CSS Frameworks and Libraries
- **Bootstrap**: Component library, grid system, utilities
- **Tailwind CSS**: Utility-first CSS framework
- **Material UI**: Google's Material Design implementation
- **Chakra UI**: Accessible component library
- **Ant Design**: Enterprise-level UI components
- **Styled Components**: CSS-in-JS library
- **Emotion**: CSS-in-JS with source maps

## Backend Development

### Server-Side Languages

#### Node.js
- **Runtime**: JavaScript on the server (V8 engine)
- **Express.js**: Minimal web framework, middleware architecture
- **NestJS**: Angular-inspired architecture, TypeScript
- **Fastify**: High-performance framework
- **Koa**: Modern Express by same creators
- **Package Management**: npm, yarn, pnpm

#### Python
- **Django**: Full-featured framework, ORM, admin panel, batteries-included
- **Flask**: Microframework, extensions ecosystem
- **FastAPI**: Modern, async, automatic API documentation
- **Pyramid**: Flexible, scalable framework

#### Other Backend Languages
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise framework, dependency injection
- **PHP Laravel**: Elegant syntax, Eloquent ORM, Blade templating
- **Go Gin**: High performance, minimal framework
- **Rust Actix**: Memory safety, performance
- **C# ASP.NET Core**: Cross-platform, enterprise features

### Database Integration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM for SQL databases
- **Prisma**: Type-safe database access, auto-generated client
- **SQLAlchemy**: Python SQL toolkit and ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### Database Drivers
- **pg**: PostgreSQL client for Node.js
- **mysql2**: MySQL client with promises
- **pymongo**: MongoDB driver for Python
- **redis**: Redis client for multiple languages

### API Development

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Nouns, plural, hierarchical
- **Versioning**: URL path, headers, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolvers**: Field-level data fetching
- **Apollo Server**: GraphQL server implementation
- **Relay**: Facebook's GraphQL client
- **Advantages**: No over-fetching, single endpoint, strong typing

#### gRPC
- **Protocol Buffers**: Interface definition language
- **HTTP/2**: Bidirectional streaming
- **Use Cases**: Microservices communication, real-time applications

### Authentication and Authorization
- **Session-based**: Cookies, server-side sessions
- **Token-based**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Authorization framework, third-party login
- **OpenID Connect**: Identity layer on OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, email codes

## DevOps and Deployment

### Version Control
- **Git**: Distributed version control
- **GitHub/GitLab/Bitbucket**: Repository hosting
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Automated testing and deployment pipelines

### Containerization
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Multi-container orchestration
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Multi-stage builds, minimal base images

### Orchestration
- **Kubernetes**: Container orchestration, pods, services, deployments
- **Helm**: Kubernetes package manager
- **Service Mesh**: Istio, Linkerd for microservices networking

### Cloud Platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend deployment, serverless functions
- **Netlify**: Static site hosting, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Simplified cloud infrastructure

### CI/CD Pipelines
- **GitHub Actions**: Workflow automation
- **GitLab CI**: Built-in continuous integration
- **Jenkins**: Extensible automation server
- **CircleCI**: Cloud-based CI/CD
- **Travis CI**: Continuous integration service
- **ArgoCD**: GitOps continuous delivery for Kubernetes

### Monitoring and Logging
- **Application Performance**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Web Performance

### Optimization Techniques
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Removing unused code
- **Minification**: Reducing file sizes
- **Compression**: Gzip, Brotli
- **Caching**: Browser cache, CDN, service workers
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Inlining above-the-fold styles
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

## Web Security

### Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Session hijacking, credential stuffing
- **Sensitive Data Exposure**: Unencrypted data, weak cryptography
- **XML External Entities (XXE)**: XML parser vulnerabilities
- **Broken Access Control**: Privilege escalation, unauthorized access
- **Security Misconfiguration**: Default credentials, verbose errors
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Object injection attacks
- **Using Components with Known Vulnerabilities**: Outdated dependencies
- **Insufficient Logging & Monitoring**: Undetected breaches

### Security Best Practices
- **HTTPS**: TLS/SSL encryption, HSTS
- **Content Security Policy (CSP)**: Prevent XSS attacks
- **Input Validation**: Sanitize user input
- **Output Encoding**: Prevent injection attacks
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Prevent brute force attacks
- **Security Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Testing

### Testing Types
- **Unit Testing**: Individual components/functions
- **Integration Testing**: Component interactions
- **End-to-End (E2E)**: Full user workflows
- **Visual Regression**: UI change detection
- **Performance Testing**: Load, stress, spike testing
- **Accessibility Testing**: WCAG compliance

### Testing Frameworks
- **Jest**: JavaScript testing framework
- **Mocha**: Flexible test runner
- **pytest**: Python testing framework
- **RSpec**: Ruby testing framework
- **JUnit**: Java testing framework

### E2E Testing Tools
- **Selenium**: Browser automation
- **Cypress**: Modern E2E testing
- **Playwright**: Cross-browser automation
- **Puppeteer**: Headless Chrome control

## Accessibility (a11y)

### WCAG Guidelines
- **Perceivable**: Text alternatives, captions, adaptable content
- **Operable**: Keyboard navigation, sufficient time, no seizures
- **Understandable**: Readable, predictable, input assistance
- **Robust**: Compatible with assistive technologies

### Implementation
- **Semantic HTML**: Proper heading hierarchy, landmarks
- **ARIA Attributes**: Roles, states, properties
- **Focus Management**: Visible focus indicators, logical tab order
- **Color Contrast**: Minimum 4.5:1 ratio for text
- **Screen Reader Testing**: NVDA, JAWS, VoiceOver
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
- **PWA Builder**: Generate manifests and icons

## Emerging Technologies

### WebAssembly (Wasm)
- **Purpose**: Run compiled code in browser at near-native speed
- **Languages**: C++, Rust, Go compilation targets
- **Use Cases**: Games, video editing, cryptography, ML inference

### Serverless Architecture
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: No server management, auto-scaling, pay-per-use
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
- **Concept**: Extend microservices to frontend
- **Approaches**: Build-time, run-time, edge-side integration
- **Benefits**: Independent deployments, team autonomy
- **Challenges**: Consistency, performance, complexity
