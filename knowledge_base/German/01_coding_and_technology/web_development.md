<!--
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

-->
# Webentwicklung
## Frontend-Entwicklung
### Kerntechnologien
#### HTML (HyperText Markup Language)
- **Semantisches HTML**: Verwendung aussagekräftiger Tags (`<header>`,`<nav>`,`<main>`,`<article>`,`<section>`,`<aside>`,`<footer>`)
- **Formulare**: Eingabetypen, Validierung, Barrierefreiheitsbezeichnungen
- **Medien**: Bilder, Videos, Audioeinbettung
- **Meta-Tags**: SEO, Ansichtsfenster, Zeichenkodierung
- **HTML5-Funktionen**: Canvas, SVG, lokaler Speicher, Geolokalisierung, Web-Sockets
#### CSS (Cascading Style Sheets)
- **Box-Modell**: Inhalt, Polsterung, Rahmen, Rand
- **Layoutsysteme**:
  - **Flexbox**: Eindimensionale Layouts, Justify-Content, Align-Items
  - **Raster**: Zweidimensionale Layouts, Rastervorlage, Rasterbereich
  - **Positionierung**: Statisch, relativ, absolut, fest, klebrig
- **Responsive Design**: Medienabfragen, Mobile-First-Ansatz
- **CSS-Variablen**: Benutzerdefinierte Eigenschaften für die Themengestaltung
- **Animationen**: Übergänge, Keyframes, Transformationen
- **Präprozessoren**: Sass, Less (Variablen, Mixins, Verschachtelung)
#### JavaScript
- **DOM-Manipulation**: Elemente auswählen, erstellen, ändern
- **Ereignisse**: Klicken, Senden, Tastatur, benutzerdefinierte Ereignisse, Ereignisdelegation
- **ES6+-Funktionen**: Pfeilfunktionen, Destrukturierung, Spread/Rest, Module, Async/Warten
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Statische Typisierung, Schnittstellen, Generika, Dekoratoren
### Moderne Frontend-Frameworks
#### Reagieren
- **Komponenten**: Funktionskomponenten, Klassenkomponenten
- **Hooks**: useState, useEffect, useContext, useReducer, benutzerdefinierte Hooks
- **Zustandsverwaltung**: Kontext-API, Redux, Zustand, Recoil
- **Routing**: Router reagieren (BrowserRouter, Routen, Route, Link)
- **Ökosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtuelles DOM**: Effizientes Rendering durch unterschiedliche Algorithmen
#### Vue.js
- **Options-API**: Daten, Methoden, berechnet, überwachen
- **Kompositions-API**: setup(), ref, reaktiv, berechnet
- **Anweisungen**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Staatsverwaltung
- **Vue Router**: Clientseitiges Routing
- **Nuxt.js**: Serverseitiges Rendering-Framework
#### Eckig
- **Komponenten**: Dekoratoren, Vorlagen, Lebenszyklus-Hooks
- **Dienste**: Abhängigkeitsinjektion, Singleton-Muster
- **RxJS**: Reaktive Programmierung, Observablen
- **Routing**: RouterModule, Guards, Resolver
- **Formulare**: Vorlagengesteuerte, reaktive Formulare
- **NgRx**: Zustandsverwaltung im Redux-Stil
### Build-Tools und Bundler
- **Webpack**: Modulbündelung, Codeaufteilung, Loader, Plugins
- **Vite**: Schnelles Build-Tool mit nativen ES-Modulen
- **Paket**: Bundler ohne Konfiguration
- **Rollup**: Optimiert für Bibliotheken
- **esbuild**: Extrem schneller JavaScript-Bundler
- **Babel**: JavaScript-Transpiler für Abwärtskompatibilität
- **PostCSS**: CSS-Verarbeitung mit Plugins
### CSS-Frameworks und -Bibliotheken
- **Bootstrap**: Komponentenbibliothek, Grid-System, Dienstprogramme
- **Tailwind CSS**: Utility-First-CSS-Framework
- **Material UI**: Googles Material Design-Implementierung
- **Chakra-Benutzeroberfläche**: Zugängliche Komponentenbibliothek
- **Ant Design**: UI-Komponenten auf Unternehmensebene
- **Styled Components**: CSS-in-JS-Bibliothek
- **Emotion**: CSS-in-JS mit Quellkarten
## Backend-Entwicklung
### Serverseitige Sprachen
#### Node.js
- **Laufzeit**: JavaScript auf dem Server (V8-Engine)
- **Express.js**: Minimales Web-Framework, Middleware-Architektur
- **NestJS**: Angular-inspirierte Architektur, TypeScript
- **Fastify**: Hochleistungs-Framework
- **Koa**: Modern Express von denselben Machern
- **Paketverwaltung**: npm, Yarn, pnpm
#### Python
- **Django**: Voll ausgestattetes Framework, ORM, Admin-Panel, Batterien im Lieferumfang enthalten
- **Flask**: Mikroframework, Erweiterungsökosystem
- **FastAPI**: Moderne, asynchrone, automatische API-Dokumentation
- **Pyramide**: Flexibles, skalierbares Framework
#### Andere Backend-Sprachen
- **Ruby on Rails**: Konvention über Konfiguration, ActiveRecord ORM
- **Java Spring**: Unternehmensframework, Abhängigkeitsinjektion
- **PHP Laravel**: Elegante Syntax, eloquentes ORM, Blade-Templating
- **Go Gin**: Hohe Leistung, minimales Framework
- **Rust Actix**: Speichersicherheit, Leistung
- **C# ASP.NET Core**: Plattformübergreifende Unternehmensfunktionen
### Datenbankintegration
#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM für SQL-Datenbanken
- **Prisma**: Typsicherer Datenbankzugriff, automatisch generierter Client
- **SQLAlchemy**: Python SQL-Toolkit und ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Ruhezustand**: Java ORM
- **Entity Framework**: .NET ORM
#### Datenbanktreiber
- **pg**: PostgreSQL-Client für Node.js
- **mysql2**: MySQL-Client mit Versprechen
- **pymongo**: MongoDB-Treiber für Python
- **redis**: Redis-Client für mehrere Sprachen
### API-Entwicklung
#### REST-APIs
- **HTTP-Methoden**: GET, POST, PUT, PATCH, DELETE
- **Statuscodes**: 200, 201, 400, 401, 403, 404, 500
- **Ressourcenbenennung**: Substantive, Plural, hierarchisch
- **Versionierung**: URL-Pfad, Header, Abfrageparameter
- **Authentifizierung**: JWT, OAuth, API-Schlüssel
- **Dokumentation**: OpenAPI/Swagger, Postman
#### GraphQL
- **Schemadefinition**: Typen, Abfragen, Mutationen, Abonnements
- **Resolver**: Datenabruf auf Feldebene
- **Apollo Server**: GraphQL-Serverimplementierung
- **Relay**: Facebooks GraphQL-Client
- **Vorteile**: Kein übermäßiges Abrufen, einzelner Endpunkt, starke Typisierung
#### gRPC
- **Protokollpuffer**: Schnittstellendefinitionssprache
- **HTTP/2**: Bidirektionales Streaming
- **Anwendungsfälle**: Microservices-Kommunikation, Echtzeitanwendungen
### Authentifizierung und Autorisierung
- **Sitzungsbasiert**: Cookies, serverseitige Sitzungen
- **Tokenbasiert**: JWT (JSON Web Tokens), zustandslos
- **OAuth 2.0**: Autorisierungsframework, Anmeldung von Drittanbietern
- **OpenID Connect**: Identitätsschicht auf OAuth 2.0
- **SAML**: Einmaliges Anmelden für Unternehmen
- **Passwort-Hashing**: bcrypt, argon2, scrypt
- **Multi-Faktor-Authentifizierung**: TOTP, SMS, E-Mail-Codes
## DevOps und Bereitstellung
### Versionskontrolle
- **Git**: Verteilte Versionskontrolle
- **GitHub/GitLab/Bitbucket**: Repository-Hosting
- **Verzweigungsstrategien**: Git Flow, GitHub Flow, Trunk-basierte Entwicklung
- **CI/CD**: Automatisierte Test- und Bereitstellungspipelines
### Containerisierung
- **Docker**: Container-Laufzeit, Docker-Datei, Bilder
- **Docker Compose**: Multi-Container-Orchestrierung
- **Containerregister**: Docker Hub, AWS ECR, Google GCR
- **Best Practices**: Mehrstufige Builds, minimale Basis-Images
### Orchestrierung
- **Kubernetes**: Container-Orchestrierung, Pods, Dienste, Bereitstellungen
- **Helm**: Kubernetes-Paketmanager
- **Service Mesh**: Istio, Linkerd für Microservices-Netzwerke
### Cloud-Plattformen
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtuelle Maschinen, Blobspeicher, Funktionen, AKS
- **Vercel**: Frontend-Bereitstellung, serverlose Funktionen
- **Netlify**: Statisches Site-Hosting, serverlose Funktionen
- **Heroku**: Plattform als Service (PaaS)
- **DigitalOcean**: Vereinfachte Cloud-Infrastruktur
### CI/CD-Pipelines
- **GitHub-Aktionen**: Workflow-Automatisierung
- **GitLab CI**: Integrierte kontinuierliche Integration
- **Jenkins**: Erweiterbarer Automatisierungsserver
- **CircleCI**: Cloudbasiertes CI/CD
- **Travis CI**: Kontinuierlicher Integrationsdienst
- **ArgoCD**: GitOps Continuous Delivery für Kubernetes
### Überwachung und Protokollierung
- **Anwendungsleistung**: New Relic, Datadog, AppDynamics
- **Fehlerverfolgung**: Sentry, Rollbar, Bugsnag
- **Protokollierung**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Verfügbarkeitsüberwachung**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude
## Webleistung
### Optimierungstechniken
- **Code-Splitting**: Lazy Loading, dynamische Importe
- **Tree Shaking**: Nicht verwendeter Code wird entfernt
- **Minimierung**: Reduzierung der Dateigröße
- **Komprimierung**: Gzip, Brotli
- **Caching**: Browser-Cache, CDN, Servicemitarbeiter
- **Bildoptimierung**: WebP, AVIF, Lazy Loading, reaktionsfähige Bilder
- **Kritisches CSS**: Inlining-Above-the-Fold-Stile
- **Datenbankoptimierung**: Indizierung, Abfrageoptimierung, Verbindungspooling
### Kern-Web-Vitals
- **LCP (Largest Contentful Paint)**: Ladeleistung (<2,5 s)
- **FID (First Input Delay)**: Interaktivität (<100 ms)
- **CLS (Cumulative Layout Shift)**: Visuelle Stabilität (<0,1)
- **INP (Interaction to Next Paint)**: Reaktionsmetrik
### Content Delivery Networks (CDNs)
- **Cloudflare**: Sicherheit, Leistung, DNS
- **Akamai**: Unternehmens-CDN
- **Amazon CloudFront**: AWS CDN
- **Schnell**: Edge-Cloud-Plattform
- **StackPath**: Edge-Dienste
## Web-Sicherheit
### Häufige Sicherheitslücken (OWASP Top 10)
- **Injection**: SQL-Injection, Befehlsinjection
- **Fehlerhafte Authentifizierung**: Session-Hijacking, Credential Stuffing
- **Offenlegung sensibler Daten**: Unverschlüsselte Daten, schwache Kryptografie
- **XML External Entities (XXE)**: Schwachstellen im XML-Parser
- **Defekte Zugriffskontrolle**: Rechteausweitung, unbefugter Zugriff
– **Sicherheitsfehlkonfiguration**: Standardanmeldeinformationen, ausführliche Fehler
- **Cross-Site Scripting (XSS)**: Reflektiert, gespeichert, DOM-basiert
- **Unsichere Deserialisierung**: Object-Injection-Angriffe
- **Verwendung von Komponenten mit bekannten Schwachstellen**: Veraltete Abhängigkeiten
- **Unzureichende Protokollierung und Überwachung**: Unentdeckte Verstöße
### Best Practices für die Sicherheit
- **HTTPS**: TLS/SSL-Verschlüsselung, HSTS
- **Content Security Policy (CSP)**: XSS-Angriffe verhindern
- **Eingabevalidierung**: Benutzereingaben bereinigen
- **Ausgabekodierung**: Injektionsangriffe verhindern
- **CSRF-Schutz**: Anti-CSRF-Tokens, SameSite-Cookies
- **Ratenbegrenzung**: Verhindern Sie Brute-Force-Angriffe
- **Sicherheitsheader**: X-Frame-Options, X-Content-Type-Options
- **Abhängigkeitsscan**: npm audit, Snyk, Dependabot
## Testen
### Testtypen
- **Unit Testing**: Einzelne Komponenten/Funktionen
- **Integrationstests**: Komponenteninteraktionen
- **End-to-End (E2E)**: Vollständige Benutzerworkflows
- **Visuelle Regression**: Erkennung von UI-Änderungen
- **Leistungstests**: Belastungs-, Stress- und Spitzentests
- **Barrierefreiheitstests**: WCAG-Konformität
### Frameworks testen
- **Jest**: JavaScript-Testframework
- **Mocha**: Flexibler Testläufer
- **pytest**: Python-Testframework
- **RSpec**: Ruby-Test-Framework
- **JUnit**: Java-Testframework
### E2E-Testtools
- **Selenium**: Browser-Automatisierung
- **Cypress**: Moderne E2E-Tests
- **Playwright**: Browserübergreifende Automatisierung
- **Puppenspieler**: Headless Chrome-Steuerung
## Barrierefreiheit (a11y)
### WCAG-Richtlinien
- **Wahrnehmbar**: Textalternativen, Bildunterschriften, anpassbare Inhalte
- **Bedienbar**: Tastaturnavigation, ausreichend Zeit, keine Anfälle
- **Verständlich**: Lesbar, vorhersehbar, Eingabehilfe
- **Robust**: Kompatibel mit unterstützenden Technologien
### Implementierung
- **Semantisches HTML**: Richtige Überschriftenhierarchie, Orientierungspunkte
- **ARIA-Attribute**: Rollen, Zustände, Eigenschaften
- **Fokusverwaltung**: Sichtbare Fokusindikatoren, logische Tab-Reihenfolge
- **Farbkontrast**: Mindestverhältnis 4,5:1 für Text
- **Screenreader-Tests**: NVDA, JAWS, VoiceOver
- **Tastaturnavigation**: Alle interaktiven Elemente zugänglich
## Progressive Web Apps (PWAs)
### PWA-Funktionen
- **Servicemitarbeiter**: Offline-Funktionalität, Hintergrundsynchronisierung
- **Web-App-Manifest**: Installationsaufforderung, Symbole, Designfarben
- **App Shell**: Zwischengespeichertes UI-Gerüst
- **Push-Benachrichtigungen**: Benutzerinteraktion
- **Responsive Design**: Funktioniert auf allen Geräten
- **HTTPS erforderlich**: Sicherer Kontext
### Werkzeuge
- **Workbox**: Service-Worker-Bibliotheken
- **Leuchtturm**: PWA-Prüfung
- **PWA Builder**: Manifeste und Symbole generieren
## Neue Technologien
### WebAssembly (Wasm)
- **Zweck**: Kompilierten Code im Browser mit nahezu nativer Geschwindigkeit ausführen
- **Sprachen**: C++, Rust, Go-Kompilierungsziele
- **Anwendungsfälle**: Spiele, Videobearbeitung, Kryptographie, ML-Inferenz
### Serverlose Architektur
- **Funktionen als Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Vorteile**: Keine Serververwaltung, automatische Skalierung, Pay-per-Use
- **Überlegungen**: Kaltstarts, Anbieterabhängigkeit, Debugging-Komplexität
### Jamstack-Architektur
- **JavaScript**: Clientseitige Interaktivität
- **APIs**: Serverlose Funktionen, Dienste von Drittanbietern
- **Markup**: Vorgefertigte statische Dateien
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Vorteile**: Leistung, Sicherheit, Skalierbarkeit, Entwicklererfahrung
### Echtzeitkommunikation
- **WebSockets**: Bidirektionale Kommunikation
- **Vom Server gesendete Ereignisse**: Server-zu-Client-Streaming
- **WebRTC**: Peer-to-Peer-Video, Audio, Daten
- **Anwendungsfälle**: Chat, Zusammenarbeit, Live-Streaming, Gaming
### Mikro-Frontends
- **Konzept**: Microservices auf das Frontend erweitern
- **Ansätze**: Build-Time, Run-Time, Edge-Side-Integration
- **Vorteile**: Unabhängige Einsätze, Teamautonomie
- **Herausforderungen**: Konsistenz, Leistung, Komplexität