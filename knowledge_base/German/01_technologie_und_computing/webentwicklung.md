<!-- 
This file was automatically translated from English to German.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Webentwicklung

## Frontend-Entwicklung

### Kerntechnologien

#### HTML (HyperText Markup Language)
- **Semantisches HTML**: Verwendung aussagekräftiger Tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Formulare**: Eingabetypen, Validierung, Barrierefreiheits-Labels
- **Medien**: Bilder, Video, Audio-Einbettung
- **Meta-Tags**: SEO, Viewport, Zeichenkodierung
- **HTML5-Features**: Canvas, SVG, Local Storage, Geolocation, WebSockets

#### CSS (Cascading Style Sheets)
- **Box-Modell**: Content, Padding, Border, Margin
- **Layout-Systeme**:
  - **Flexbox**: Eindimensionale Layouts, justify-content, align-items
  - **Grid**: Zweidimensionale Layouts, grid-template, grid-area
  - **Positionierung**: Static, Relative, Absolute, Fixed, Sticky
- **Responsive Design**: Media Queries, Mobile-First-Ansatz
- **CSS-Variablen**: Custom Properties für Theming
- **Animationen**: Transitions, Keyframes, Transforms
- **Preprozessoren**: Sass, Less (Variablen, Mixins, Nesting)

#### JavaScript
- **DOM-Manipulation**: Auswählen, Erstellen, Modifizieren von Elementen
- **Ereignisse**: Click, Submit, Keyboard, Custom Events, Event Delegation
- **ES6+-Features**: Arrow Functions, Destructuring, Spread/Rest, Modules, Async/Await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Statische Typisierung, Interfaces, Generics, Decorators

### Moderne Frontend-Frameworks

#### React
- **Komponenten**: Funktionale Komponenten, Klassen-Komponenten
- **Hooks**: useState, useEffect, useContext, useReducer, Custom Hooks
- **State-Verwaltung**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ökosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Effizientes Rendering durch Diffing-Algorithmus

#### Vue.js
- **Options API**: Data, Methods, Computed, Watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: State-Verwaltung
- **Vue Router**: Client-seitiges Routing
- **Nuxt.js**: Server-side Rendering Framework

#### Angular
- **Komponenten**: Decorators, Templates, Lifecycle-Hooks
- **Services**: Dependency Injection, Singleton-Pattern
- **RxJS**: Reactive Programming, Observables
- **Routing**: RouterModule, Guards, Resolvers
- **Formulare**: Template-driven, Reactive Forms
- **NgRx**: Redux-artige State-Verwaltung

### Build-Tools und Bundler
- **Webpack**: Module-Bundling, Code-Splitting, Loader, Plugins
- **Vite**: Schnelles Build-Tool mit nativen ES-Modulen
- **Parcel**: Zero-Configuration-Bundler
- **Rollup**: Optimiert für Bibliotheken
- **esbuild**: Extrem schneller JavaScript-Bundler
- **Babel**: JavaScript-Transpiler für Abwärtskompatibilität
- **PostCSS**: CSS-Verarbeitung mit Plugins

### CSS-Frameworks und Bibliotheken
- **Bootstrap**: Komponenten-Bibliothek, Grid-System, Utilities
- **Tailwind CSS**: Utility-First-CSS-Framework
- **Material UI**: Google's Material-Design-Implementierung
- **Chakra UI**: Barrierefreie Komponenten-Bibliothek
- **Ant Design**: UI-Komponenten auf Enterprise-Niveau
- **Styled Components**: CSS-in-JS-Bibliothek
- **Emotion**: CSS-in-JS mit Source Maps

## Backend-Entwicklung

### Serverseitige Sprachen

#### Node.js
- **Runtime**: JavaScript auf dem Server (V8-Engine)
- **Express.js**: Minimales Web-Framework, Middleware-Architektur
- **NestJS**: Angular-inspirierte Architektur, TypeScript
- **Fastify**: Hochleistungs-Framework
- **Koa**: Modernes Express von denselben Entwicklern
- **Paketverwaltung**: npm, yarn, pnpm

#### Python
- **Django**: Vollständiges Framework, ORM, Admin-Panel, Batteries-Included
- **Flask**: Microframework, Erweiterungs-Ökosystem
- **FastAPI**: Modern, asynchron, automatische API-Dokumentation
- **Pyramid**: Flexibles, skalierbares Framework

#### Andere Backend-Sprachen
- **Ruby on Rails**: Convention over Configuration, ActiveRecord-ORM
- **Java Spring**: Enterprise-Framework, Dependency Injection
- **PHP Laravel**: Elegante Syntax, Eloquent-ORM, Blade-Templating
- **Go Gin**: Hohe Leistung, minimales Framework
- **Rust Actix**: Speichersicherheit, Leistung
- **C# ASP.NET Core**: Plattformübergreifend, Enterprise-Features

### Datenbank-Integration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js-ORM für SQL-Datenbanken
- **Prisma**: Typsicherer Datenbankzugriff, auto-generierter Client
- **SQLAlchemy**: Python-SQL-Toolkit und ORM
- **ActiveRecord**: Ruby-on-Rails-ORM
- **Hibernate**: Java-ORM
- **Entity Framework**: .NET-ORM

#### Datenbank-Treiber
- **pg**: PostgreSQL-Client für Node.js
- **mysql2**: MySQL-Client mit Promises
- **pymongo**: MongoDB-Treiber für Python
- **redis**: Redis-Client für mehrere Sprachen

### API-Entwicklung

#### REST-APIs
- **HTTP-Methoden**: GET, POST, PUT, PATCH, DELETE
- **Status-Codes**: 200, 201, 400, 401, 403, 404, 500
- **Ressourcen-Benennung**: Substantive, Plural, hierarchisch
- **Versionierung**: URL-Pfad, Header, Query-Parameter
- **Authentifizierung**: JWT, OAuth, API-Keys
- **Dokumentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema-Definition**: Types, Queries, Mutations, Subscriptions
- **Resolver**: Feldweises Daten-Fetching
- **Apollo Server**: GraphQL-Server-Implementierung
- **Relay**: Facebooks GraphQL-Client
- **Vorteile**: Kein Over-Fetching, einzelner Endpunkt, starke Typisierung

#### gRPC
- **Protocol Buffers**: Interface-Definitionssprache
- **HTTP/2**: Bidirektionales Streaming
- **Anwendungsfälle**: Microservices-Kommunikation, Echtzeitanwendungen

### Authentifizierung und Autorisierung
- **Session-basiert**: Cookies, serverseitige Sessions
- **Token-basiert**: JWT (JSON Web Tokens), zustandslos
- **OAuth 2.0**: Autorisierungs-Framework, Drittanbieter-Login
- **OpenID Connect**: Identitätsschicht auf OAuth 2.0
- **SAML**: Enterprise Single Sign-On
- **Passwort-Hashing**: bcrypt, argon2, scrypt
- **Multi-Faktor-Authentifizierung**: TOTP, SMS, E-Mail-Codes

## DevOps und Bereitstellung

### Versionskontrolle
- **Git**: Distribuierte Versionskontrolle
- **GitHub/GitLab/Bitbucket**: Repository-Hosting
- **Branching-Strategien**: Git Flow, GitHub Flow, Trunk-Based Development
- **CI/CD**: Automatisiertes Testen und Bereitstellungs-Pipelines

### Containerisierung
- **Docker**: Container-Runtime, Dockerfile, Images
- **Docker Compose**: Multi-Container-Orchestrierung
- **Container-Registries**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Multi-Stage-Builds, minimale Basis-Images

### Orchestrierung
- **Kubernetes**: Container-Orchestrierung, Pods, Services, Deployments
- **Helm**: Kubernetes-Paketmanager
- **Service Mesh**: Istio, Linkerd für Microservices-Networking

### Cloud-Plattformen
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend-Bereitstellung, Serverless-Funktionen
- **Netlify**: Static-Site-Hosting, Serverless-Funktionen
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Vereinfachte Cloud-Infrastruktur

### CI/CD-Pipelines
- **GitHub Actions**: Workflow-Automatisierung
- **GitLab CI**: Integrierte Continuous Integration
- **Jenkins**: Erweiterbarer Automation-Server
- **CircleCI**: Cloud-basierte CI/CD
- **Travis CI**: Continuous-Integration-Service
- **ArgoCD**: GitOps Continuous Delivery für Kubernetes

### Monitoring und Logging
- **Application Performance**: New Relic, Datadog, AppDynamics
- **Error Tracking**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime-Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Web-Performance

### Optimierungstechniken
- **Code-Splitting**: Lazy Loading, Dynamic Imports
- **Tree Shaking**: Entfernen ungenutzten Codes
- **Minifizierung**: Reduzierung der Dateigrößen
- **Komprimierung**: Gzip, Brotli
- **Caching**: Browser-Cache, CDN, Service Workers
- **Bildoptimierung**: WebP, AVIF, Lazy Loading, Responsive Images
- **Critical CSS**: Inline-Styling für Above-the-Fold-Bereiche
- **Datenbankoptimierung**: Indexierung, Query-Optimierung, Connection Pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Ladeleistung (<2,5s)
- **FID (First Input Delay)**: Interaktivität (<100ms)
- **CLS (Cumulative Layout Shift)**: Visuelle Stabilität (<0,1)
- **INP (Interaction to Next Paint)**: Responsiveness-Metrik

### Content Delivery Networks (CDNs)
- **Cloudflare**: Sicherheit, Performance, DNS
- **Akamai**: Enterprise-CDN
- **Amazon CloudFront**: AWS-CDN
- **Fastly**: Edge-Cloud-Plattform
- **StackPath**: Edge-Services

## Websicherheit

### Häufige Schwachstellen (OWASP Top 10)
- **Injection**: SQL-Injection, Command-Injection
- **Broken Authentication**: Session Hijacking, Credential Stuffing
- **Sensitive Data Exposure**: Unverschlüsselte Daten, schwache Kryptographie
- **XML External Entities (XXE)**: XML-Parser-Schwachstellen
- **Broken Access Control**: Privilege Escalation, unbefugter Zugriff
- **Security Misconfiguration**: Standard-Anmeldedaten, ausführliche Fehlermeldungen
- **Cross-Site Scripting (XSS)**: Reflected, Stored, DOM-based
- **Insecure Deserialization**: Object-Injection-Angriffe
- **Using Components with Known Vulnerabilities**: Veraltete Abhängigkeiten
- **Insufficient Logging & Monitoring**: Unentdeckte Sicherheitsverletzungen

### Sicherheits-Best-Practices
- **HTTPS**: TLS/SSL-Verschlüsselung, HSTS
- **Content Security Policy (CSP)**: XSS-Angriffe verhindern
- **Input-Validierung**: Benutzer-Eingaben bereinigen
- **Output-Encoding**: Injection-Angriffe verhindern
- **CSRF-Schutz**: Anti-CSRF-Tokens, SameSite-Cookies
- **Rate Limiting**: Brute-Force-Angriffe verhindern
- **Security-Header**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Testen

### Testarten
- **Unit-Tests**: Individuelle Komponenten/Funktionen
- **Integrationstests**: Komponenten-Interaktionen
- **End-to-End (E2E)**: Vollständige User-Workflows
- **Visuelle Regression**: UI-Änderungserkennung
- **Leistungstests**: Load-, Stress-, Spike-Tests
- **Barrierefreiheitstests**: WCAG-Compliance

### Test-Frameworks
- **Jest**: JavaScript-Test-Framework
- **Mocha**: Flexibler Test-Runner
- **pytest**: Python-Test-Framework
- **RSpec**: Ruby-Test-Framework
- **JUnit**: Java-Test-Framework

### E2E-Test-Tools
- **Selenium**: Browser-Automatisierung
- **Cypress**: Modernes E2E-Testen
- **Playwright**: Cross-Browser-Automatisierung
- **Puppeteer**: Headless-Chrome-Steuerung

## Barrierefreiheit (a11y)

### WCAG-Richtlinien
- **Wahrnehmbar**: Textalternativen, Untertitel, anpassbare Inhalte
- **Bedienbar**: Tastaturnavigation, ausreichende Zeit, keine Anfälle auslösend
- **Verständlich**: Lesbar, vorhersehbar, Eingabeunterstützung
- **Robust**: Kompatibel mit assistiven Technologien

### Implementierung
- **Semantisches HTML**: Korrekte Überschriftenhierarchie, Landmarks
- **ARIA-Attribute**: Rollen, Zustände, Eigenschaften
- **Focus-Verwaltung**: Sichtbare Focus-Indikatoren, logische Tab-Reihenfolge
- **Farbkontrast**: Mindestens 4,5:1 Verhältnis für Text
- **Screen-Reader-Tests**: NVDA, JAWS, VoiceOver
- **Tastaturnavigation**: Alle interaktiven Elemente zugänglich

## Progressive Web Apps (PWAs)

### PWA-Features
- **Service Workers**: Offline-Funktionalität, Background-Sync
- **Web App Manifest**: Installations-Prompt, Icons, Theme-Farben
- **App Shell**: Zwischengespeichertes UI-Gerüst
- **Push-Benachrichtigungen**: User-Engagement
- **Responsive Design**: Funktioniert auf allen Geräten
- **HTTPS erforderlich**: Sicherer Kontext

### Tools
- **Workbox**: Service-Worker-Bibliotheken
- **Lighthouse**: PWA-Auditing
- **PWA Builder**: Manifeste und Icons generieren

## Aufkommende Technologien

### WebAssembly (Wasm)
- **Zweck**: Kompilierten Code im Browser mit nahezu nativer Geschwindigkeit ausführen
- **Sprachen**: C++, Rust, Go als Kompilierungsziele
- **Anwendungsfälle**: Spiele, Videobearbeitung, Kryptographie, ML-Inferenz

### Serverless-Architektur
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Vorteile**: Keine Server-Verwaltung, Auto-Scaling, Pay-per-Use
- **Überlegungen**: Cold Starts, Vendor Lock-in, Debugging-Komplexität

### Jamstack-Architektur
- **JavaScript**: Client-seitige Interaktivität
- **APIs**: Serverless-Funktionen, Drittanbieter-Services
- **Markup**: Vorab erstellte statische Dateien
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Vorteile**: Performance, Sicherheit, Skalierbarkeit, Developer Experience

### Echtzeit-Kommunikation
- **WebSockets**: Bidirektionale Kommunikation
- **Server-Sent Events**: Server-zu-Client-Streaming
- **WebRTC**: Peer-to-Peer-Video, Audio, Daten
- **Anwendungsfälle**: Chat, Zusammenarbeit, Live-Streaming, Gaming

### Micro Frontends
- **Konzept**: Microservices auf das Frontend erweitern
- **Ansätze**: Build-Time, Run-Time, Edge-Side-Integration
- **Vorteile**: Unabhängige Deployments, Team-Autonomie
- **Herausforderungen**: Konsistenz, Performance, Komplexität
