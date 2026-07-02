# Webentwicklung

## Frontend-Entwicklung

### Kerntechnologien

#### HTML (HyperText Markup Language)
- **Semantic HTML**: Aussagekräftige Tags verwenden (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms**: Input-Typen, Validierung, Accessibility-Labels
- **Media**: Einbettung von Bildern, Video und Audio
- **Meta Tags**: SEO, Viewport, Zeichenkodierung
- **HTML5-Funktionen**: Canvas, SVG, Local Storage, Geolocation, WebSockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Inhalt, Padding, Border, Margin
- **Layout-Systeme**:
  - **Flexbox**: Eindimensionale Layouts, justify-content, align-items
  - **Grid**: Zweidimensionale Layouts, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Responsives Design**: Media Queries, Mobile-First-Ansatz
- **CSS-Variablen**: Custom Properties für Themes
- **Animationen**: Transitions, Keyframes, Transforms
- **Präprozessoren**: Sass, Less (Variablen, Mixins, Verschachtelung)

#### JavaScript
- **DOM-Manipulation**: Elemente auswählen, erstellen, ändern
- **Events**: Click, submit, Tastatur, benutzerdefinierte Events, Event Delegation
- **ES6+-Funktionen**: Arrow Functions, Destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Statische Typisierung, Interfaces, Generics, Decorators

### Moderne Frontend-Frameworks

#### React
- **Components**: Funktionale Komponenten, Klassenkomponenten
- **Hooks**: useState, useEffect, useContext, useReducer, benutzerdefinierte Hooks
- **Zustandsverwaltung**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ökosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Effizientes Rendering durch einen Diffing-Algorithmus

#### Vue.js
- **Options API**: data, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Zustandsverwaltung
- **Vue Router**: Client-Side-Routing
- **Nuxt.js**: Framework für Server-Side Rendering

#### Angular
- **Components**: Decorators, Templates, Lifecycle Hooks
- **Services**: Dependency Injection, Singleton-Muster
- **RxJS**: Reaktive Programmierung, Observables
- **Routing**: RouterModule, Guards, Resolver
- **Forms**: Template-driven, reactive forms
- **NgRx**: Redux-artige Zustandsverwaltung

### Build-Tools und Bundler
- **Webpack**: Modul-Bundling, Code Splitting, Loader, Plugins
- **Vite**: Schnelles Build-Tool mit nativen ES-Modulen
- **Parcel**: Bundler ohne Konfiguration
- **Rollup**: Für Bibliotheken optimiert
- **esbuild**: Extrem schneller JavaScript-Bundler
- **Babel**: JavaScript-Transpiler für Abwärtskompatibilität
- **PostCSS**: CSS-Verarbeitung mit Plugins

### CSS-Frameworks und Bibliotheken
- **Bootstrap**: Komponentenbibliothek, Grid-System, Utilities
- **Tailwind CSS**: Utility-First-CSS-Framework
- **Material UI**: Googles Material-Design-Implementierung
- **Chakra UI**: Barrierefreie Komponentenbibliothek
- **Ant Design**: UI-Komponenten auf Enterprise-Niveau
- **Styled Components**: CSS-in-JS-Bibliothek
- **Emotion**: CSS-in-JS mit Source Maps

## Backend-Entwicklung

### Serverseitige Sprachen

#### Node.js
- **Runtime**: JavaScript auf dem Server (V8-Engine)
- **Express.js**: Minimales Web-Framework, Middleware-Architektur
- **NestJS**: Von Angular inspirierte Architektur, TypeScript
- **Fastify**: Hochperformantes Framework
- **Koa**: Modernes Express von denselben Entwicklern
- **Paketverwaltung**: npm, yarn, pnpm

#### Python
- **Django**: Funktionsreiches Framework, ORM, Admin-Panel, batteries-included
- **Flask**: Microframework, Ökosystem aus Erweiterungen
- **FastAPI**: Modern, asynchron, automatische API-Dokumentation
- **Pyramid**: Flexibles, skalierbares Framework

#### Weitere Backend-Sprachen
- **Ruby on Rails**: Convention over Configuration, ActiveRecord ORM
- **Java Spring**: Enterprise-Framework, Dependency Injection
- **PHP Laravel**: Elegante Syntax, Eloquent ORM, Blade-Templating
- **Go Gin**: Hohe Performance, minimales Framework
- **Rust Actix**: Speichersicherheit, Performance
- **C# ASP.NET Core**: Plattformübergreifend, Enterprise-Funktionen

### Datenbankintegration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js-ORM für SQL-Datenbanken
- **Prisma**: Typensicherer Datenbankzugriff, automatisch generierter Client
- **SQLAlchemy**: Python-SQL-Toolkit und ORM
- **ActiveRecord**: Ruby-on-Rails-ORM
- **Hibernate**: Java-ORM
- **Entity Framework**: .NET-ORM

#### Datenbanktreiber
- **pg**: PostgreSQL-Client für Node.js
- **mysql2**: MySQL-Client mit Promises
- **pymongo**: MongoDB-Treiber für Python
- **redis**: Redis-Client für mehrere Sprachen

### API-Entwicklung

#### REST-APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: Substantive, Plural, hierarchisch
- **Versioning**: URL-Pfad, Header, Query-Parameter
- **Authentifizierung**: JWT, OAuth, API keys
- **Dokumentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schemadefinition**: Types, Queries, Mutations, Subscriptions
- **Resolvers**: Datenabruf auf Feldebene
- **Apollo Server**: GraphQL-Server-Implementierung
- **Relay**: Facebooks GraphQL-Client
- **Vorteile**: Kein Over-Fetching, ein Endpunkt, starke Typisierung

#### gRPC
- **Protocol Buffers**: Interface-Definition-Sprache
- **HTTP/2**: Bidirektionales Streaming
- **Anwendungsfälle**: Microservices-Kommunikation, Echtzeitanwendungen

### Authentifizierung und Autorisierung
- **Session-based**: Cookies, serverseitige Sessions
- **Token-based**: JWT (JSON Web Tokens), zustandslos
- **OAuth 2.0**: Autorisierungs-Framework, Third-Party-Login
- **OpenID Connect**: Identitätsschicht auf OAuth 2.0
- **SAML**: Enterprise-Single-Sign-On
- **Password Hashing**: bcrypt, argon2, scrypt
- **Multi-Factor Authentication**: TOTP, SMS, E-Mail-Codes

## DevOps und Deployment

### Versionskontrolle
- **Git**: Verteilte Versionskontrolle
- **GitHub/GitLab/Bitbucket**: Repository-Hosting
- **Branching-Strategien**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Automatisierte Test- und Deployment-Pipelines

### Containerisierung
- **Docker**: Container-Runtime, Dockerfile, Images
- **Docker Compose**: Multi-Container-Orchestrierung
- **Container-Registries**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Multi-Stage-Builds, minimale Base-Images

### Orchestrierung
- **Kubernetes**: Container-Orchestrierung, Pods, Services, Deployments
- **Helm**: Kubernetes-Paketmanager
- **Service Mesh**: Istio, Linkerd für Microservices-Netzwerke

### Cloud-Plattformen
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend-Deployment, Serverless Functions
- **Netlify**: Hosting für statische Sites, Serverless Functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Vereinfachte Cloud-Infrastruktur

### CI/CD-Pipelines
- **GitHub Actions**: Workflow-Automatisierung
- **GitLab CI**: Eingebaute Continuous Integration
- **Jenkins**: Erweiterbarer Automatisierungsserver
- **CircleCI**: Cloud-basiertes CI/CD
- **Travis CI**: Dienst für Continuous Integration
- **ArgoCD**: GitOps Continuous Delivery für Kubernetes

### Monitoring und Logging
- **Anwendungsleistung**: New Relic, Datadog, AppDynamics
- **Fehlerverfolgung**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime-Monitoring**: Pingdom, UptimeRobot
- **Analytik**: Google Analytics, Mixpanel, Amplitude

## Web-Performance

### Optimierungstechniken
- **Code Splitting**: Lazy Loading, dynamische Imports
- **Tree Shaking**: Ungenutzten Code entfernen
- **Minification**: Dateigrößen reduzieren
- **Compression**: Gzip, Brotli
- **Caching**: Browser-Cache, CDN, Service Workers
- **Bildoptimierung**: WebP, AVIF, Lazy Loading, responsive Bilder
- **Critical CSS**: Above-the-Fold-Styles inline einbetten
- **Datenbankoptimierung**: Indexierung, Query-Optimierung, Connection Pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Ladeleistung (<2.5s)
- **FID (First Input Delay)**: Interaktivität (<100ms)
- **CLS (Cumulative Layout Shift)**: Visuelle Stabilität (<0.1)
- **INP (Interaction to Next Paint)**: Responsiveness-Metrik

### Content Delivery Networks (CDNs)
- **Cloudflare**: Sicherheit, Performance, DNS
- **Akamai**: Enterprise-CDN
- **Amazon CloudFront**: AWS-CDN
- **Fastly**: Edge-Cloud-Plattform
- **StackPath**: Edge-Services

## Web-Sicherheit

### Häufige Schwachstellen (OWASP Top 10)
- **Injection**: SQL Injection, Command Injection
- **Broken Authentication**: Session Hijacking, Credential Stuffing
- **Sensitive Data Exposure**: Unverschlüsselte Daten, schwache Kryptografie
- **XML External Entities (XXE)**: Schwachstellen in XML-Parsern
- **Broken Access Control**: Privilege Escalation, unbefugter Zugriff
- **Security Misconfiguration**: Standard-Anmeldedaten, ausführliche Fehlermeldungen
- **Cross-Site Scripting (XSS)**: Reflected, Stored, DOM-basiert
- **Insecure Deserialization**: Object-Injection-Angriffe
- **Using Components with Known Vulnerabilities**: Veraltete Abhängigkeiten
- **Insufficient Logging & Monitoring**: Nicht erkannte Sicherheitsverletzungen

### Sicherheits-Best-Practices
- **HTTPS**: TLS/SSL-Verschlüsselung, HSTS
- **Content Security Policy (CSP)**: XSS-Angriffe verhindern
- **Eingabevalidierung**: Benutzereingaben bereinigen
- **Ausgabekodierung**: Injection-Angriffe verhindern
- **CSRF Protection**: Anti-CSRF-Tokens, SameSite-Cookies
- **Rate Limiting**: Brute-Force-Angriffe verhindern
- **Sicherheitsheader**: X-Frame-Options, X-Content-Type-Options
- **Abhängigkeits-Scanning**: npm audit, Snyk, Dependabot

## Testing

### Testarten
- **Unit Testing**: Einzelne Komponenten/Funktionen
- **Integration Testing**: Interaktionen zwischen Komponenten
- **End-to-End (E2E)**: Vollständige Benutzerabläufe
- **Visual Regression**: Erkennung von UI-Änderungen
- **Performance Testing**: Last-, Stress- und Spike-Tests
- **Accessibility Testing**: WCAG-Konformität

### Test-Frameworks
- **Jest**: JavaScript-Test-Framework
- **Mocha**: Flexibler Test-Runner
- **pytest**: Python-Test-Framework
- **RSpec**: Ruby-Test-Framework
- **JUnit**: Java-Test-Framework

### E2E-Testwerkzeuge
- **Selenium**: Browser-Automatisierung
- **Cypress**: Modernes E2E-Testing
- **Playwright**: Browserübergreifende Automatisierung
- **Puppeteer**: Steuerung von Headless Chrome

## Accessibility (a11y)

### WCAG-Richtlinien
- **Perceivable**: Textalternativen, Untertitel, anpassbare Inhalte
- **Operable**: Tastaturnavigation, ausreichende Zeit, keine Anfälle
- **Understandable**: Lesbar, vorhersehbar, Eingabeunterstützung
- **Robust**: Kompatibel mit assistiven Technologien

### Umsetzung
- **Semantic HTML**: Korrekte Überschriftenhierarchie, Landmarks
- **ARIA-Attribute**: Rollen, Zustände, Eigenschaften
- **Fokusmanagement**: Sichtbare Fokusindikatoren, logische Tab-Reihenfolge
- **Farbkontrast**: Mindestverhältnis von 4.5:1 für Text
- **Screen-Reader-Tests**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: Alle interaktiven Elemente zugänglich

## Progressive Web Apps (PWAs)

### PWA-Funktionen
- **Service Workers**: Offline-Funktionalität, Background Sync
- **Web App Manifest**: Installationsaufforderung, Icons, Theme Colors
- **App Shell**: Gecachtes UI-Grundgerüst
- **Push Notifications**: Nutzerinteraktion
- **Responsive Design**: Funktioniert auf allen Geräten
- **HTTPS Required**: Sicherer Kontext

### Werkzeuge
- **Workbox**: Bibliotheken für Service Workers
- **Lighthouse**: PWA-Auditing
- **PWA Builder**: Manifeste und Icons erzeugen

## Neue Technologien

### WebAssembly (Wasm)
- **Zweck**: Kompilierten Code im Browser nahezu mit nativer Geschwindigkeit ausführen
- **Sprachen**: C++, Rust, Go als Kompilierungsziele
- **Anwendungsfälle**: Spiele, Videobearbeitung, Kryptografie, ML-Inferenz

### Serverless-Architektur
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Vorteile**: Kein Server-Management, Auto-Scaling, nutzungsbasierte Bezahlung
- **Zu beachten**: Cold Starts, Vendor Lock-in, Debugging-Komplexität

### Jamstack-Architektur
- **JavaScript**: Interaktivität auf Client-Seite
- **APIs**: Serverless Functions, Dienste von Drittanbietern
- **Markup**: Vorab gebaute statische Dateien
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Vorteile**: Performance, Sicherheit, Skalierbarkeit, Developer Experience

### Echtzeitkommunikation
- **WebSockets**: Bidirektionale Kommunikation
- **Server-Sent Events**: Streaming vom Server zum Client
- **WebRTC**: Peer-to-Peer-Video, -Audio und -Daten
- **Anwendungsfälle**: Chat, Zusammenarbeit, Live-Streaming, Gaming

### Micro Frontends
- **Konzept**: Microservices auf das Frontend ausweiten
- **Ansätze**: Build-Time-, Run-Time- und Edge-Side-Integration
- **Vorteile**: Unabhängige Deployments, Teamautonomie
- **Herausforderungen**: Konsistenz, Performance, Komplexität
