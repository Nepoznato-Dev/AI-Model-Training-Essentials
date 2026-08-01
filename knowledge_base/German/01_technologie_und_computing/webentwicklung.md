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
- **Box-Modell**: Inhalt, Innenabstand, Rahmen, Außenabstand
- **Layout-Systeme**:
  - **Flexbox**: Eindimensionale Layouts, justify-content, align-items
  - **Grid**: Zweidimensionale Layouts, grid-template, grid-area
  - **Positionierung**: Static, Relative, Absolute, Fixed, Sticky
- **Responsive Design**: Media Queries, Mobile-First-Ansatz
- **CSS-Variablen**: Custom Properties für Themes
- **Animationen**: Übergänge, Keyframes, Transformationen
- **Preprozessoren**: Sass, Less (Variablen, Mixins, Verschachtelung)

#### JavaScript
- **DOM-Manipulation**: Auswählen, Erstellen, Modifizieren von Elementen
- **Ereignisse**: Click, Submit, Tastaturereignisse, Custom Events, Event Delegation
- **ES6+-Features**: Arrow Functions, Destructuring, Spread/Rest, Module, Async/Await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Statische Typisierung, Interfaces, Generics, Decorators

### Moderne Frontend-Frameworks

#### React
- **Komponenten**: Funktionale Komponenten, Klassenkomponenten
- **Hooks**: useState, useEffect, useContext, useReducer, benutzerdefinierte Hooks
- **State-Verwaltung**: Context API, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ökosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Effizientes Rendering durch einen Diffing-Algorithmus

#### Vue.js
- **Options API**: Data, Methods, Computed, Watch
- **Composition API**: setup(), ref, reactive, computed
- **Direktiven**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: State-Verwaltung
- **Vue Router**: Client-seitiges Routing
- **Nuxt.js**: Framework für Server-side Rendering

#### Angular
- **Komponenten**: Decorators, Templates, Lifecycle-Hooks
- **Services**: Dependency Injection, Singleton-Muster
- **RxJS**: Reaktive Programmierung, Observables
- **Routing**: RouterModule, Guards, Resolvers
- **Formulare**: Template-driven, Reactive Forms
- **NgRx**: Redux-artige State-Verwaltung

### Build-Tools und Bündler
- **Webpack**: Module-Bundling, Code-Splitting, Loader, Plugins
- **Vite**: Schnelles Build-Tool mit nativen ES-Modulen
- **Parcel**: Bündler ohne zusätzliche Konfiguration
- **Rollup**: Optimiert für Bibliotheken
- **esbuild**: Extrem schneller JavaScript-Bundler
- **Babel**: JavaScript-Transpiler für Abwärtskompatibilität
- **PostCSS**: CSS-Verarbeitung mit Plugins

### CSS-Frameworks und Bibliotheken
- **Bootstrap**: Komponenten-Bibliothek, Grid-System, Utilities
- **Tailwind CSS**: Utility-First-CSS-Framework
- **Material UI**: Googles Material-Design-Implementierung
- **Chakra UI**: Barrierefreie Komponenten-Bibliothek
- **Ant Design**: UI-Komponenten auf Enterprise-Niveau
- **Styled Components**: CSS-in-JS-Bibliothek
- **Emotion**: CSS-in-JS mit Quellzuordnungen

## Backend-Entwicklung

### Serverseitige Sprachen

#### Node.js
- **Laufzeitumgebung**: JavaScript auf dem Server (V8-Engine)
- **Express.js**: Minimales Web-Framework, Middleware-Architektur
- **NestJS**: Angular-inspirierte Architektur, TypeScript
- **Fastify**: Hochleistungs-Framework
- **Koa**: Modernes Express von denselben Entwicklern
- **Paketverwaltung**: npm, yarn, pnpm

#### Python
- **Django**: Vollständiges Framework, ORM, Admin-Panel, viele Funktionen bereits eingebaut
- **Flask**: Mikro-Framework, reiches Erweiterungsökosystem
- **FastAPI**: Modern, asynchron, automatische API-Dokumentation
- **Pyramid**: Flexibles, skalierbares Framework

#### Andere Backend-Sprachen
- **Ruby on Rails**: Convention over Configuration, ActiveRecord-ORM
- **Java Spring**: Enterprise-Framework, Dependency Injection
- **PHP Laravel**: Elegante Syntax, Eloquent-ORM, Blade-Templates
- **Go Gin**: Hohe Leistung, minimales Framework
- **Rust Actix**: Speichersicherheit, Leistung
- **C# ASP.NET Core**: Plattformübergreifend, Funktionen für Unternehmen

### Datenbank-Integration

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js-ORM für SQL-Datenbanken
- **Prisma**: Typsicherer Datenbankzugriff, automatisch generierter Client
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
- **Authentifizierung**: JWT, OAuth, API-Schlüssel
- **Dokumentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema-Definition**: Types, Queries, Mutations, Subscriptions
- **Resolver**: Feldweises Abrufen von Daten
- **Apollo Server**: GraphQL-Server-Implementierung
- **Relay**: GraphQL-Client von Facebook
- **Vorteile**: Kein Over-Fetching, ein einzelner Endpunkt, starke Typisierung

#### gRPC
- **Protocol Buffers**: Interface-Definitionssprache
- **HTTP/2**: Bidirektionales Streaming
- **Anwendungsfälle**: Microservices-Kommunikation, Echtzeitanwendungen

### Authentifizierung und Autorisierung
- **Sitzungsbasiert**: Cookies, serverseitige Sitzungen
- **Token-basiert**: JWT (JSON Web Tokens), zustandslos
- **OAuth 2.0**: Autorisierungs-Framework, Anmeldung über Drittanbieter
- **OpenID Connect**: Identitätsschicht auf OAuth 2.0
- **SAML**: Single Sign-On für Unternehmen
- **Passwort-Hashing**: bcrypt, argon2, scrypt
- **Multi-Faktor-Authentifizierung**: TOTP, SMS, E-Mail-Codes

## DevOps und Bereitstellung

### Versionskontrolle
- **Git**: Verteilte Versionskontrolle
- **GitHub/GitLab/Bitbucket**: Repository-Hosting
- **Branching-Strategien**: Git Flow, GitHub Flow, Trunk-Based Development
- **CI/CD**: Automatisierte Test- und Bereitstellungspipelines

### Containerisierung
- **Docker**: Container-Runtime, Dockerfile, Images
- **Docker Compose**: Orchestrierung mehrerer Container
- **Container-Registries**: Docker Hub, AWS ECR, Google GCR
- **Bewährte Praktiken**: Multi-Stage-Builds, minimale Basis-Images

### Orchestrierung
- **Kubernetes**: Container-Orchestrierung, Pods, Services, Deployments
- **Helm**: Kubernetes-Paketmanager
- **Service Mesh**: Istio, Linkerd für die Vernetzung von Microservices

### Cloud-Plattformen
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Frontend-Bereitstellung, Serverless-Funktionen
- **Netlify**: Static-Site-Hosting, Serverless-Funktionen
- **Heroku**: Plattform als Dienst (PaaS)
- **DigitalOcean**: Vereinfachte Cloud-Infrastruktur

### CI/CD-Pipelines
- **GitHub Actions**: Workflow-Automatisierung
- **GitLab CI**: Integrierte kontinuierliche Integration
- **Jenkins**: Erweiterbarer Automatisierungsserver
- **CircleCI**: Cloud-basierte CI/CD
- **Travis CI**: Dienst für kontinuierliche Integration
- **ArgoCD**: GitOps-Continuous-Delivery für Kubernetes

### Monitoring und Logging
- **Anwendungsleistung**: New Relic, Datadog, AppDynamics
- **Fehlerverfolgung**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime-Monitoring**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Leistung im Web

### Optimierungstechniken
- **Code-Splitting**: Lazy Loading, dynamische Importe
- **Tree Shaking**: Entfernen ungenutzten Codes
- **Minifizierung**: Reduzierung der Dateigrößen
- **Komprimierung**: Gzip, Brotli
- **Caching**: Browser-Cache, CDN, Service Worker
- **Bildoptimierung**: WebP, AVIF, Lazy Loading, responsive Bilder
- **Critical CSS**: Inline-Styling für sofort sichtbare Bereiche
- **Datenbankoptimierung**: Indexierung, Abfrageoptimierung, Connection Pooling

### Zentrale Webmetriken (Core Web Vitals)
- **LCP (Largest Contentful Paint)**: Ladeleistung (<2,5s)
- **FID (First Input Delay)**: Interaktivität (<100ms)
- **CLS (Cumulative Layout Shift)**: Visuelle Stabilität (<0,1)
- **INP (Interaction to Next Paint)**: Kennzahl für Reaktionsfähigkeit

### Inhaltsauslieferungsnetzwerke (CDNs)
- **Cloudflare**: Sicherheit, Leistung, DNS
- **Akamai**: CDN für Unternehmen
- **Amazon CloudFront**: AWS-CDN
- **Fastly**: Edge-Cloud-Plattform
- **StackPath**: Edge-Dienste

## Websicherheit

### Häufige Schwachstellen (OWASP Top 10)
- **Injection-Angriffe**: SQL-Injection, Command-Injection
- **Fehlerhafte Authentifizierung**: Session Hijacking, Credential Stuffing
- **Offenlegung sensibler Daten**: Unverschlüsselte Daten, schwache Kryptografie
- **XML External Entities (XXE)**: XML-Parser-Schwachstellen
- **Fehlerhafte Zugriffskontrolle**: Privilegienausweitung, unbefugter Zugriff
- **Sicherheitsfehlkonfiguration**: Standard-Anmeldedaten, ausführliche Fehlermeldungen
- **Cross-Site Scripting (XSS)**: Reflected, Stored, DOM-based
- **Unsichere Deserialisierung**: Angriffe durch Object Injection
- **Verwendung von Komponenten mit bekannten Schwachstellen**: Veraltete Abhängigkeiten
- **Unzureichendes Logging und Monitoring**: Unentdeckte Sicherheitsverletzungen

### Bewährte Sicherheitspraktiken
- **HTTPS**: TLS/SSL-Verschlüsselung, HSTS
- **Content Security Policy (CSP)**: Schutz vor XSS-Angriffen
- **Eingabevalidierung**: Benutzereingaben bereinigen
- **Ausgabekodierung**: Injection-Angriffe verhindern
- **CSRF-Schutz**: Anti-CSRF-Tokens, SameSite-Cookies
- **Rate Limiting**: Brute-Force-Angriffe verhindern
- **Sicherheitsheader**: X-Frame-Options, X-Content-Type-Options
- **Abhängigkeitsprüfung**: npm audit, Snyk, Dependabot

## Testen

### Testarten
- **Unit-Tests**: Individuelle Komponenten/Funktionen
- **Integrationstests**: Komponenten-Interaktionen
- **End-to-End (E2E)**: Vollständige Benutzerabläufe
- **Visuelle Regression**: UI-Änderungserkennung
- **Leistungstests**: Last-, Stress- und Spike-Tests
- **Barrierefreiheitstests**: WCAG-Compliance

### Test-Frameworks
- **Jest**: JavaScript-Test-Framework
- **Mocha**: Flexibler Test-Runner
- **pytest**: Python-Test-Framework
- **RSpec**: Ruby-Test-Framework
- **JUnit**: Java-Test-Framework

### E2E-Test-Werkzeuge
- **Selenium**: Browser-Automatisierung
- **Cypress**: Modernes E2E-Testen
- **Playwright**: Browserübergreifende Automatisierung
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
- **Fokus-Verwaltung**: Sichtbare Fokus-Indikatoren, logische Tab-Reihenfolge
- **Farbkontrast**: Mindestens 4,5:1 Verhältnis für Text
- **Screen-Reader-Tests**: NVDA, JAWS, VoiceOver
- **Tastaturnavigation**: Alle interaktiven Elemente zugänglich

## Progressive-Web-Apps (PWAs)

### PWA-Funktionen
- **Service Worker**: Offline-Funktionalität, Hintergrundsynchronisierung
- **Web-App-Manifest**: Installationsaufforderung, Icons, Theme-Farben
- **App Shell**: Zwischengespeichertes UI-Gerüst
- **Push-Benachrichtigungen**: Nutzerbindung
- **Responsive Design**: Funktioniert auf allen Geräten
- **HTTPS erforderlich**: Sicherer Kontext

### Werkzeuge
- **Workbox**: Service-Worker-Bibliotheken
- **Lighthouse**: PWA-Auditing
- **PWA Builder**: Manifeste und Icons erzeugen

## Aufkommende Technologien

### WebAssembly (Wasm)
- **Zweck**: Kompilierten Code im Browser mit nahezu nativer Geschwindigkeit ausführen
- **Sprachen**: C++, Rust, Go als Zielsprachen der Kompilierung
- **Anwendungsfälle**: Spiele, Videobearbeitung, Kryptographie, ML-Inferenz

### Serverless-Architektur
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Vorteile**: Keine Serververwaltung, automatische Skalierung, nutzungsbasierte Abrechnung
- **Überlegungen**: Cold Starts, Vendor Lock-in, Debugging-Komplexität

### Jamstack-Architektur
- **JavaScript**: Client-seitige Interaktivität
- **APIs**: Serverless-Funktionen, Dienste von Drittanbietern
- **Markup**: Vorab erstellte statische Dateien
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Vorteile**: Hohe Leistung, Sicherheit, Skalierbarkeit, gute Entwicklererfahrung

### Echtzeit-Kommunikation
- **WebSockets**: Bidirektionale Kommunikation
- **Server-Sent Events**: Server-zu-Client-Streaming
- **WebRTC**: Peer-to-Peer-Übertragung von Video, Audio und Daten
- **Anwendungsfälle**: Chat, Zusammenarbeit, Live-Streaming, Gaming

### Micro-Frontends
- **Konzept**: Den Microservices-Ansatz auf das Frontend ausdehnen
- **Ansätze**: Build-Time, Run-Time, Edge-Side-Integration
- **Vorteile**: Unabhängige Bereitstellungen, Teamautonomie
- **Herausforderungen**: Konsistenz, Leistung, Komplexität
