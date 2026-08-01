<!-- 
This file was automatically translated from English to French.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Développement web

## Développement frontend

### Technologies de base

#### HTML (langage de balisage hypertexte)
- **HTML sémantique** : utilisation de balises porteuses de sens (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Formulaires** : types de champs, validation, libellés d'accessibilité
- **Médias** : intégration d'images, de vidéos et d'audio
- **Balises meta** : SEO, viewport, encodage des caractères
- **Fonctionnalités HTML5** : canvas, SVG, stockage local, géolocalisation, WebSockets

#### CSS (feuilles de style en cascade)
- **Modèle de boîte** : contenu, padding, bordure, marge
- **Systèmes de mise en page** :
  - **Flexbox** : mises en page unidimensionnelles, `justify-content`, `align-items`
  - **Grid** : mises en page bidimensionnelles, `grid-template`, `grid-area`
  - **Positionnement** : statique, relatif, absolu, fixe, sticky
- **Conception adaptative** : media queries, approche mobile-first
- **Variables CSS** : propriétés personnalisées pour les thèmes
- **Animations** : transitions, keyframes, transformations
- **Préprocesseurs** : Sass, Less (variables, mixins, imbrication)

#### JavaScript
- **Manipulation du DOM** : sélection, création et modification d'éléments
- **Événements** : clic, soumission, clavier, événements personnalisés, délégation d'événements
- **Fonctionnalités ES6+** : fonctions fléchées, destructuration, spread/rest, modules, async/await
- **API** : Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript** : typage statique, interfaces, génériques, décorateurs

### Frameworks frontend modernes

#### React
- **Composants** : composants fonctionnels, composants de classe
- **Hooks** : useState, useEffect, useContext, useReducer, hooks personnalisés
- **Gestion d'état** : Context API, Redux, Zustand, Recoil
- **Routage** : React Router (BrowserRouter, Routes, Route, Link)
- **Écosystème** : Next.js (SSR, SSG), Remix, Gatsby
- **DOM virtuel** : rendu efficace grâce à l'algorithme de diff

#### Vue.js
- **Options API** : données, methods, computed, watch
- **Composition API** : setup(), ref, reactive, computed
- **Directives** : v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia** : gestion d'état
- **Vue Router** : routage côté client
- **Nuxt.js** : framework de rendu côté serveur

#### Angular
- **Composants** : décorateurs, templates, hooks du cycle de vie
- **Services** : injection de dépendances, pattern singleton
- **RxJS** : programmation réactive, observables
- **Routage** : RouterModule, guards, resolvers
- **Formulaires** : pilotés par template, formulaires réactifs
- **NgRx** : gestion d'état de style Redux

### Outils de compilation et assembleurs de modules
- **Webpack** : empaquetage de modules, code splitting, loaders, plugins
- **Vite** : outil de compilation rapide utilisant les modules ES natifs
- **Parcel** : assembleur de modules sans configuration
- **Rollup** : optimisé pour les bibliothèques
- **esbuild** : assembleur JavaScript extrêmement rapide
- **Babel** : transpileur JavaScript pour la rétrocompatibilité
- **PostCSS** : traitement CSS avec des plugins

### Frameworks et bibliothèques CSS
- **Bootstrap** : bibliothèque de composants, système de grille, utilitaires
- **Tailwind CSS** : framework CSS orienté utilitaires
- **Material UI** : implémentation du Material Design de Google
- **Chakra UI** : bibliothèque de composants accessible
- **Ant Design** : composants UI de niveau entreprise
- **Styled Components** : bibliothèque CSS-in-JS
- **Emotion** : CSS-in-JS avec source maps

## Développement backend

### Langages côté serveur

#### Node.js
- **Runtime** : JavaScript côté serveur (moteur V8)
- **Express.js** : framework web minimaliste, architecture à base de middleware
- **NestJS** : architecture inspirée d'Angular, TypeScript
- **Fastify** : framework haute performance
- **Koa** : version moderne d'Express par les mêmes créateurs
- **Gestion de paquets** : npm, yarn, pnpm

#### Python
- **Django** : framework complet, ORM, panneau d'administration, batteries incluses
- **Flask** : microframework, écosystème d'extensions
- **FastAPI** : framework moderne, asynchrone, documentation d'API automatique
- **Pyramid** : framework flexible et évolutif

#### Autres langages backend
- **Ruby on Rails** : convention plutôt que configuration, ORM ActiveRecord
- **Java Spring** : framework d'entreprise, injection de dépendances
- **PHP Laravel** : syntaxe élégante, ORM Eloquent, moteur de templates Blade
- **Go Gin** : hautes performances, framework minimaliste
- **Rust Actix** : sûreté mémoire, performance
- **C# ASP.NET Core** : multiplateforme, fonctionnalités d'entreprise

### Intégration des bases de données

#### ORMs (mapping objet-relationnel)
- **Sequelize** : ORM Node.js pour les bases SQL
- **Prisma** : accès à la base de données typé et client généré automatiquement
- **SQLAlchemy** : boîte à outils SQL et ORM pour Python
- **ActiveRecord** : ORM de Ruby on Rails
- **Hibernate** : ORM Java
- **Entity Framework** : ORM .NET

#### Pilotes de base de données
- **pg** : client PostgreSQL pour Node.js
- **mysql2** : client MySQL avec promises
- **pymongo** : driver MongoDB pour Python
- **redis** : client Redis pour plusieurs langages

### Développement d'API

#### API REST
- **Méthodes HTTP** : GET, POST, PUT, PATCH, DELETE
- **Codes de statut** : 200, 201, 400, 401, 403, 404, 500
- **Nommage des ressources** : noms, pluriels, structure hiérarchique
- **Versionnement** : chemin d'URL, en-têtes, paramètres de requête
- **Authentification** : JWT, OAuth, clés API
- **Documentation** : OpenAPI/Swagger, Postman

#### GraphQL
- **Définition du schéma** : types, queries, mutations, subscriptions
- **Resolvers** : récupération de données au niveau des champs
- **Apollo Server** : implémentation de serveur GraphQL
- **Relay** : client GraphQL de Facebook
- **Avantages** : pas de sur-récupération, point d'entrée unique, typage fort

#### gRPC
- **Protocol Buffers** : langage de définition d'interface
- **HTTP/2** : streaming bidirectionnel
- **Cas d'utilisation** : communication entre microservices, applications temps réel

### Authentification et autorisation
- **Basée sur les sessions** : cookies, sessions côté serveur
- **Basée sur les jetons** : JWT (JSON Web Tokens), sans état
- **OAuth 2.0** : framework d'autorisation, connexion via des tiers
- **OpenID Connect** : couche d'identité au-dessus d'OAuth 2.0
- **SAML** : authentification unique d'entreprise
- **Hachage des mots de passe** : bcrypt, argon2, scrypt
- **Authentification multifacteur** : TOTP, SMS, codes par e-mail

## DevOps et déploiement

### Contrôle de version
- **Git** : système de contrôle de version distribué
- **GitHub/GitLab/Bitbucket** : hébergement de dépôts
- **Stratégies de branchement** : Git Flow, GitHub Flow, développement basé sur le trunk
- **CI/CD** : pipelines automatisés de test et de déploiement

### Conteneurisation
- **Docker** : runtime de conteneurs, Dockerfile, images
- **Docker Compose** : orchestration multi-conteneurs
- **Registres de conteneurs** : Docker Hub, AWS ECR, Google GCR
- **Meilleures pratiques** : builds multi-étapes, images de base minimales

### Orchestration
- **Kubernetes** : orchestration de conteneurs, pods, services, deployments
- **Helm** : gestionnaire de paquets pour Kubernetes
- **Service Mesh** : Istio, Linkerd pour le réseau des microservices

### Plateformes cloud
- **AWS** : EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud** : Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure** : Virtual Machines, Blob Storage, Functions, AKS
- **Vercel** : déploiement frontend, fonctions serverless
- **Netlify** : hébergement de sites statiques, fonctions serverless
- **Heroku** : plateforme en tant que service (PaaS)
- **DigitalOcean** : infrastructure cloud simplifiée

### Pipelines CI/CD
- **GitHub Actions** : automatisation des workflows
- **GitLab CI** : intégration continue intégrée
- **Jenkins** : serveur d'automatisation extensible
- **CircleCI** : CI/CD dans le cloud
- **Travis CI** : service d'intégration continue
- **ArgoCD** : livraison continue GitOps pour Kubernetes

### Supervision et journalisation
- **Performance applicative** : New Relic, Datadog, AppDynamics
- **Suivi des erreurs** : Sentry, Rollbar, Bugsnag
- **Journalisation** : ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Supervision de disponibilité** : Pingdom, UptimeRobot
- **Analytique** : Google Analytics, Mixpanel, Amplitude

## Performances web

### Techniques d'optimisation
- **Code splitting** : chargement différé, imports dynamiques
- **Tree shaking** : suppression du code inutilisé
- **Minification** : réduction de la taille des fichiers
- **Compression** : Gzip, Brotli
- **Mise en cache** : cache navigateur, CDN, service workers
- **Optimisation des images** : WebP, AVIF, chargement différé, images responsives
- **CSS critique** : intégration en ligne des styles au-dessus de la ligne de flottaison
- **Optimisation des bases de données** : indexation, optimisation des requêtes, pool de connexions

### Core Web Vitals
- **LCP (Largest Contentful Paint)** : performance de chargement (< 2,5 s)
- **FID (First Input Delay)** : interactivité (< 100 ms)
- **CLS (Cumulative Layout Shift)** : stabilité visuelle (< 0,1)
- **INP (Interaction to Next Paint)** : métrique de réactivité

### Réseaux de diffusion de contenu (CDN)
- **Cloudflare** : sécurité, performance, DNS
- **Akamai** : CDN d'entreprise
- **Amazon CloudFront** : CDN d'AWS
- **Fastly** : plateforme cloud edge
- **StackPath** : services edge

## Sécurité web

### Vulnérabilités courantes (OWASP Top 10)
- **Injection** : injection SQL, injection de commandes
- **Authentification défaillante** : détournement de session, credential stuffing
- **Exposition de données sensibles** : données non chiffrées, cryptographie faible
- **Entités externes XML (XXE)** : vulnérabilités des parseurs XML
- **Contrôle d'accès défaillant** : élévation de privilèges, accès non autorisé
- **Mauvaise configuration de sécurité** : identifiants par défaut, erreurs trop verbeuses
- **Cross-Site Scripting (XSS)** : réfléchi, stocké, basé sur le DOM
- **Désérialisation non sécurisée** : attaques par injection d'objets
- **Utilisation de composants présentant des vulnérabilités connues** : dépendances obsolètes
- **Journalisation et supervision insuffisantes** : intrusions non détectées

### Bonnes pratiques de sécurité
- **HTTPS** : chiffrement TLS/SSL, HSTS
- **Content Security Policy (CSP)** : prévention des attaques XSS
- **Validation des entrées** : assainir les données utilisateur
- **Encodage des sorties** : prévenir les attaques par injection
- **Protection CSRF** : jetons anti-CSRF, cookies SameSite
- **Rate limiting** : prévention des attaques par force brute
- **En-têtes de sécurité** : X-Frame-Options, X-Content-Type-Options
- **Analyse des dépendances** : npm audit, Snyk, Dependabot

## Tests

### Types de tests
- **Test unitaire** : composants ou fonctions individuels
- **Test d'intégration** : interactions entre composants
- **Test de bout en bout (E2E)** : parcours utilisateur complets
- **Régression visuelle** : détection des changements d'interface
- **Test de performance** : tests de charge, de stress et de pic
- **Test d'accessibilité** : conformité WCAG

### Frameworks de test
- **Jest** : framework de test JavaScript
- **Mocha** : exécuteur de tests flexible
- **pytest** : framework de test Python
- **RSpec** : framework de test Ruby
- **JUnit** : framework de test Java

### Outils de test E2E
- **Selenium** : automatisation du navigateur
- **Cypress** : outil moderne de test E2E
- **Playwright** : automatisation multi-navigateurs
- **Puppeteer** : pilotage de Chrome sans interface

## Accessibilité (a11y)

### Directives WCAG
- **Perceptible** : alternatives textuelles, sous-titres, contenu adaptable
- **Utilisable** : navigation au clavier, temps suffisant, absence de contenu provoquant des crises
- **Compréhensible** : lisible, prévisible, aide à la saisie
- **Robuste** : compatible avec les technologies d'assistance

### Mise en œuvre
- **HTML sémantique** : hiérarchie correcte des titres, points de repère
- **Attributs ARIA** : rôles, états, propriétés
- **Gestion du focus** : indicateurs de focus visibles, ordre de tabulation logique
- **Contraste des couleurs** : ratio minimal de 4,5:1 pour le texte
- **Test avec lecteur d'écran** : NVDA, JAWS, VoiceOver
- **Navigation au clavier** : tous les éléments interactifs doivent être accessibles

## Applications web progressives (PWA)

### Fonctionnalités des PWA
- **Service workers** : fonctionnement hors ligne, synchronisation en arrière-plan
- **Web App Manifest** : invite d'installation, icônes, couleurs de thème
- **App Shell** : squelette d'interface mis en cache
- **Notifications push** : engagement des utilisateurs
- **Responsive design** : fonctionnement sur tous les appareils
- **HTTPS obligatoire** : contexte sécurisé

### Outils
- **Workbox** : bibliothèques pour service workers
- **Lighthouse** : audit PWA
- **PWA Builder** : génération de manifests et d'icônes

## Technologies émergentes

### WebAssembly (Wasm)
- **Objectif** : exécuter du code compilé dans le navigateur à une vitesse proche du natif
- **Langages** : cibles de compilation pour C++, Rust, Go
- **Cas d'utilisation** : jeux, montage vidéo, cryptographie, inférence ML

### Architecture sans serveur
- **Fonctions en tant que service** : AWS Lambda, Azure Functions, Google Cloud Functions
- **Avantages** : aucune gestion de serveur, mise à l'échelle automatique, paiement à l'usage
- **Considérations** : démarrages à froid, dépendance fournisseur, complexité du débogage

### Architecture Jamstack
- **JavaScript** : interactivité côté client
- **API** : fonctions serverless, services tiers
- **Markup** : fichiers statiques préconstruits
- **Outils** : Next.js, Gatsby, Hugo, Eleventy
- **Avantages** : performance, sécurité, évolutivité, expérience développeur

### Communication en temps réel
- **WebSockets** : communication bidirectionnelle
- **Server-Sent Events** : diffusion du serveur vers le client
- **WebRTC** : vidéo, audio et données en pair à pair
- **Cas d'utilisation** : chat, collaboration, diffusion en direct, jeux

### Frontends modulaires
- **Concept** : appliquer les principes des microservices au frontend
- **Approches** : intégration au build, à l'exécution ou en edge
- **Avantages** : déploiements indépendants, autonomie des équipes
- **Défis** : cohérence, performance, complexité
