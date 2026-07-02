# Développement web

## Développement frontend

### Technologies fondamentales

#### HTML (HyperText Markup Language)
- **Semantic HTML** : Utilisation de balises significatives (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Forms** : Types de champs, validation, labels d'accessibilité
- **Media** : Intégration d'images, de vidéo et d'audio
- **Meta Tags** : SEO, viewport, encodage des caractères
- **HTML5 Features** : Canvas, SVG, local storage, geolocation, web sockets

#### CSS (Cascading Style Sheets)
- **Box Model** : Contenu, padding, bordure, marge
- **Layout Systems** :
  - **Flexbox** : Mises en page unidimensionnelles, justify-content, align-items
  - **Grid** : Mises en page bidimensionnelles, grid-template, grid-area
  - **Positioning** : Static, relative, absolute, fixed, sticky
- **Responsive Design** : Media queries, approche mobile-first
- **CSS Variables** : Propriétés personnalisées pour les thèmes
- **Animations** : Transitions, keyframes, transforms
- **Preprocessors** : Sass, Less (variables, mixins, imbrication)

#### JavaScript
- **DOM Manipulation** : Sélection, création et modification d'éléments
- **Events** : Click, submit, clavier, événements personnalisés, délégation d'événements
- **ES6+ Features** : Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs** : Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript** : Typage statique, interfaces, génériques, décorateurs

### Frameworks frontend modernes

#### React
- **Components** : Composants fonctionnels, composants de classe
- **Hooks** : useState, useEffect, useContext, useReducer, custom hooks
- **State Management** : Context API, Redux, Zustand, Recoil
- **Routing** : React Router (BrowserRouter, Routes, Route, Link)
- **Ecosystem** : Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM** : Rendu efficace grâce à l'algorithme de diff

#### Vue.js
- **Options API** : data, methods, computed, watch
- **Composition API** : setup(), ref, reactive, computed
- **Directives** : v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia** : Gestion d'état
- **Vue Router** : Routage côté client
- **Nuxt.js** : Framework de rendu côté serveur

#### Angular
- **Components** : Décorateurs, templates, hooks de cycle de vie
- **Services** : Injection de dépendances, singleton pattern
- **RxJS** : Programmation réactive, observables
- **Routing** : RouterModule, guards, resolvers
- **Forms** : Template-driven, reactive forms
- **NgRx** : Gestion d'état de style Redux

### Outils de build et bundlers
- **Webpack** : Bundling de modules, code splitting, loaders, plugins
- **Vite** : Outil de build rapide utilisant les modules ES natifs
- **Parcel** : Bundler sans configuration
- **Rollup** : Optimisé pour les bibliothèques
- **esbuild** : Bundler JavaScript extrêmement rapide
- **Babel** : Transpileur JavaScript pour la rétrocompatibilité
- **PostCSS** : Traitement CSS avec plugins

### Frameworks et bibliothèques CSS
- **Bootstrap** : Bibliothèque de composants, système de grille, utilitaires
- **Tailwind CSS** : Framework CSS orienté utilitaires
- **Material UI** : Implémentation du Material Design de Google
- **Chakra UI** : Bibliothèque de composants accessible
- **Ant Design** : Composants UI de niveau entreprise
- **Styled Components** : Bibliothèque CSS-in-JS
- **Emotion** : CSS-in-JS avec source maps

## Développement backend

### Langages côté serveur

#### Node.js
- **Runtime** : JavaScript côté serveur (moteur V8)
- **Express.js** : Framework web minimal, architecture middleware
- **NestJS** : Architecture inspirée d'Angular, TypeScript
- **Fastify** : Framework haute performance
- **Koa** : Express moderne par les mêmes créateurs
- **Package Management** : npm, yarn, pnpm

#### Python
- **Django** : Framework complet, ORM, panneau d'administration, batteries incluses
- **Flask** : Microframework, écosystème d'extensions
- **FastAPI** : Moderne, async, documentation d'API automatique
- **Pyramid** : Framework flexible et scalable

#### Autres langages backend
- **Ruby on Rails** : Convention over configuration, ORM ActiveRecord
- **Java Spring** : Framework entreprise, injection de dépendances
- **PHP Laravel** : Syntaxe élégante, ORM Eloquent, templating Blade
- **Go Gin** : Haute performance, framework minimal
- **Rust Actix** : Sécurité mémoire, performance
- **C# ASP.NET Core** : Multiplateforme, fonctionnalités entreprise

### Intégration des bases de données

#### ORMs (Object-Relational Mapping)
- **Sequelize** : ORM Node.js pour bases de données SQL
- **Prisma** : Accès base de données type-safe, client généré automatiquement
- **SQLAlchemy** : Toolkit SQL Python et ORM
- **ActiveRecord** : ORM Ruby on Rails
- **Hibernate** : ORM Java
- **Entity Framework** : ORM .NET

#### Drivers de base de données
- **pg** : Client PostgreSQL pour Node.js
- **mysql2** : Client MySQL avec promises
- **pymongo** : Driver MongoDB pour Python
- **redis** : Client Redis pour plusieurs langages

### Développement d'API

#### REST APIs
- **HTTP Methods** : GET, POST, PUT, PATCH, DELETE
- **Status Codes** : 200, 201, 400, 401, 403, 404, 500
- **Resource Naming** : Substantifs, pluriel, hiérarchique
- **Versioning** : Chemin d'URL, headers, query parameters
- **Authentication** : JWT, OAuth, API keys
- **Documentation** : OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition** : Types, queries, mutations, subscriptions
- **Resolvers** : Récupération de données au niveau des champs
- **Apollo Server** : Implémentation de serveur GraphQL
- **Relay** : Client GraphQL de Facebook
- **Advantages** : Pas de sur-récupération, endpoint unique, typage fort

#### gRPC
- **Protocol Buffers** : Langage de définition d'interface
- **HTTP/2** : Streaming bidirectionnel
- **Use Cases** : Communication entre microservices, applications temps réel

### Authentication and Authorization
- **Session-based** : Cookies, sessions côté serveur
- **Token-based** : JWT (JSON Web Tokens), sans état
- **OAuth 2.0** : Cadre d'autorisation, connexion via tiers
- **OpenID Connect** : Couche d'identité sur OAuth 2.0
- **SAML** : Single sign-on d'entreprise
- **Password Hashing** : bcrypt, argon2, scrypt
- **Multi-Factor Authentication** : TOTP, codes SMS, codes e-mail

## DevOps et déploiement

### Contrôle de version
- **Git** : Contrôle de version distribué
- **GitHub/GitLab/Bitbucket** : Hébergement de dépôts
- **Branching Strategies** : Git Flow, GitHub Flow, trunk-based development
- **CI/CD** : Pipelines automatisés de test et de déploiement

### Conteneurisation
- **Docker** : Runtime de conteneurs, Dockerfile, images
- **Docker Compose** : Orchestration multi-conteneurs
- **Container Registries** : Docker Hub, AWS ECR, Google GCR
- **Best Practices** : Builds multi-stage, images de base minimales

### Orchestration
- **Kubernetes** : Orchestration de conteneurs, pods, services, deployments
- **Helm** : Gestionnaire de packages Kubernetes
- **Service Mesh** : Istio, Linkerd pour le réseau de microservices

### Plateformes cloud
- **AWS** : EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud** : Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure** : Virtual Machines, Blob Storage, Functions, AKS
- **Vercel** : Déploiement frontend, serverless functions
- **Netlify** : Hébergement de sites statiques, serverless functions
- **Heroku** : Platform as a Service (PaaS)
- **DigitalOcean** : Infrastructure cloud simplifiée

### Pipelines CI/CD
- **GitHub Actions** : Automatisation des workflows
- **GitLab CI** : Intégration continue intégrée
- **Jenkins** : Serveur d'automatisation extensible
- **CircleCI** : CI/CD dans le cloud
- **Travis CI** : Service d'intégration continue
- **ArgoCD** : GitOps continuous delivery pour Kubernetes

### Monitoring et logging
- **Application Performance** : New Relic, Datadog, AppDynamics
- **Error Tracking** : Sentry, Rollbar, Bugsnag
- **Logging** : ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Uptime Monitoring** : Pingdom, UptimeRobot
- **Analytics** : Google Analytics, Mixpanel, Amplitude

## Performance web

### Techniques d'optimisation
- **Code Splitting** : Chargement différé, imports dynamiques
- **Tree Shaking** : Suppression du code inutilisé
- **Minification** : Réduction de la taille des fichiers
- **Compression** : Gzip, Brotli
- **Caching** : Cache navigateur, CDN, service workers
- **Image Optimization** : WebP, AVIF, lazy loading, images responsives
- **Critical CSS** : Inline des styles above-the-fold
- **Database Optimization** : Indexation, optimisation des requêtes, pooling de connexions

### Core Web Vitals
- **LCP (Largest Contentful Paint)** : Performance de chargement (<2.5s)
- **FID (First Input Delay)** : Interactivité (<100ms)
- **CLS (Cumulative Layout Shift)** : Stabilité visuelle (<0.1)
- **INP (Interaction to Next Paint)** : Indicateur de réactivité

### Content Delivery Networks (CDNs)
- **Cloudflare** : Sécurité, performance, DNS
- **Akamai** : CDN d'entreprise
- **Amazon CloudFront** : CDN AWS
- **Fastly** : Plateforme edge cloud
- **StackPath** : Services edge

## Sécurité web

### Vulnérabilités courantes (OWASP Top 10)
- **Injection** : Injection SQL, injection de commandes
- **Broken Authentication** : Détournement de session, credential stuffing
- **Sensitive Data Exposure** : Données non chiffrées, cryptographie faible
- **XML External Entities (XXE)** : Vulnérabilités des parseurs XML
- **Broken Access Control** : Escalade de privilèges, accès non autorisé
- **Security Misconfiguration** : Identifiants par défaut, erreurs trop verbeuses
- **Cross-Site Scripting (XSS)** : Réfléchi, stocké, basé sur le DOM
- **Insecure Deserialization** : Attaques par injection d'objets
- **Using Components with Known Vulnerabilities** : Dépendances obsolètes
- **Insufficient Logging & Monitoring** : Violations non détectées

### Bonnes pratiques de sécurité
- **HTTPS** : Chiffrement TLS/SSL, HSTS
- **Content Security Policy (CSP)** : Empêcher les attaques XSS
- **Input Validation** : Assainir les entrées utilisateur
- **Output Encoding** : Empêcher les attaques par injection
- **CSRF Protection** : Tokens anti-CSRF, cookies SameSite
- **Rate Limiting** : Empêcher les attaques par force brute
- **Security Headers** : X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning** : npm audit, Snyk, Dependabot

## Tests

### Types de tests
- **Unit Testing** : Composants/fonctions individuels
- **Integration Testing** : Interactions entre composants
- **End-to-End (E2E)** : Parcours utilisateur complets
- **Visual Regression** : Détection des changements d'interface
- **Performance Testing** : Tests de charge, de stress, de pic
- **Accessibility Testing** : Conformité WCAG

### Frameworks de test
- **Jest** : Framework de test JavaScript
- **Mocha** : Test runner flexible
- **pytest** : Framework de test Python
- **RSpec** : Framework de test Ruby
- **JUnit** : Framework de test Java

### Outils de test E2E
- **Selenium** : Automatisation de navigateur
- **Cypress** : Test E2E moderne
- **Playwright** : Automatisation cross-browser
- **Puppeteer** : Contrôle headless de Chrome

## Accessibilité (a11y)

### Directives WCAG
- **Perceivable** : Alternatives textuelles, sous-titres, contenu adaptable
- **Operable** : Navigation clavier, temps suffisant, absence de crises
- **Understandable** : Lisible, prévisible, aide à la saisie
- **Robust** : Compatible avec les technologies d'assistance

### Mise en œuvre
- **Semantic HTML** : Hiérarchie correcte des titres, landmarks
- **ARIA Attributes** : Rôles, états, propriétés
- **Focus Management** : Indicateurs de focus visibles, ordre de tabulation logique
- **Color Contrast** : Ratio minimal de 4.5:1 pour le texte
- **Screen Reader Testing** : NVDA, JAWS, VoiceOver
- **Keyboard Navigation** : Tous les éléments interactifs accessibles

## Progressive Web Apps (PWAs)

### Fonctionnalités PWA
- **Service Workers** : Fonctionnement hors ligne, synchronisation en arrière-plan
- **Web App Manifest** : Invite d'installation, icônes, couleurs de thème
- **App Shell** : Squelette d'interface mis en cache
- **Push Notifications** : Engagement utilisateur
- **Responsive Design** : Fonctionne sur tous les appareils
- **HTTPS Required** : Contexte sécurisé

### Outils
- **Workbox** : Bibliothèques de service workers
- **Lighthouse** : Audit PWA
- **PWA Builder** : Génération de manifests et d'icônes

## Technologies émergentes

### WebAssembly (Wasm)
- **Purpose** : Exécuter du code compilé dans le navigateur à une vitesse proche du natif
- **Languages** : C++, Rust, Go comme cibles de compilation
- **Use Cases** : Jeux, montage vidéo, cryptographie, inférence ML

### Architecture serverless
- **Functions as a Service** : AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits** : Aucune gestion de serveur, auto-scaling, paiement à l'usage
- **Considerations** : Démarrages à froid, verrouillage fournisseur, complexité du débogage

### Architecture Jamstack
- **JavaScript** : Interactivité côté client
- **APIs** : Serverless functions, services tiers
- **Markup** : Fichiers statiques préconstruits
- **Tools** : Next.js, Gatsby, Hugo, Eleventy
- **Benefits** : Performance, sécurité, scalabilité, expérience développeur

### Communication en temps réel
- **WebSockets** : Communication bidirectionnelle
- **Server-Sent Events** : Streaming du serveur vers le client
- **WebRTC** : Vidéo, audio et données peer-to-peer
- **Use Cases** : Chat, collaboration, live streaming, gaming

### Micro frontends
- **Concept** : Étendre les microservices au frontend
- **Approaches** : Intégration au build time, run-time, edge-side
- **Benefits** : Déploiements indépendants, autonomie des équipes
- **Challenges** : Cohérence, performance, complexité
