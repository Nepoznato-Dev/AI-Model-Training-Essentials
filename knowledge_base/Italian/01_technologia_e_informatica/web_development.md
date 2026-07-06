#Sviluppo Web

## Sviluppo frontend

### Tecnologie principali

#### HTML (linguaggio di markup per ipertesto)
- **HTML semantico**: utilizzo di tag significativi (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Moduli**: tipi di input, convalida, etichette di accessibilità
- **Media**: immagini, video, incorporamento audio
- **Meta tag**: SEO, viewport, codifica dei caratteri
- **Funzionalità HTML5**: Canvas, SVG, archiviazione locale, geolocalizzazione, socket web

#### CSS (fogli di stile a cascata)
- **Box Model**: contenuto, riempimento, bordo, margine
- **Sistemi di layout**:
  - **Flexbox**: layout unidimensionali, giustificazione del contenuto, allineamento degli elementi
  - **Griglia**: layout bidimensionali, modello di griglia, area di griglia
  - **Posizionamento**: statico, relativo, assoluto, fisso, appiccicoso
- **Responsive Design**: query multimediali, approccio mobile-first
- **Variabili CSS**: proprietà personalizzate per i temi
- **Animazioni**: transizioni, fotogrammi chiave, trasformazioni
- **Preprocessori**: Sass, Less (variabili, mixin, nidificazione)

#### JavaScript
- **Manipolazione DOM**: selezione, creazione, modifica di elementi
- **Eventi**: clic, invio, tastiera, eventi personalizzati, delega di eventi
- **Caratteristiche ES6+**: funzioni freccia, destrutturazione, diffusione/riposo, moduli, asincrono/attesa
- **API**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: digitazione statica, interfacce, generici, decoratori

### Framework frontend moderni

#### Reagisci
- **Componenti**: componenti funzionali, componenti di classe
- **Hook**: useState, useEffect, useContext, useReducer, hook personalizzati
- **Gestione dello stato**: API contesto, Redux, Zustand, Recoil
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecosistema**: Next.js (SSR, SSG), Remix, Gatsby
- ** DOM virtuale **: rendering efficiente tramite algoritmo di differenza

#### Vue.js
- **API Opzioni**: dati, metodi, calcolati, guarda
- **API di composizione**: setup(), ref, reattivo, calcolato
- **Direttive**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: gestione statale
- **Vue Router**: routing lato client
- **Nuxt.js**: framework di rendering lato server

#### Angolare
- **Componenti**: decoratori, modelli, ganci del ciclo di vita
- **Servizi**: inserimento delle dipendenze, modello singleton
- **RxJS**: programmazione reattiva, osservabili
- **Routing**: RouterModule, guardie, risolutori
- **Moduli**: moduli reattivi basati su modelli
- **NgRx**: gestione dello stato in stile Redux

### Crea strumenti e bundler
- **Webpack**: raggruppamento di moduli, suddivisione del codice, caricatori, plug-in
- **Vite**: strumento di creazione rapida utilizzando moduli ES nativi
- **Parcel**: bundler a configurazione zero
- **Rollup**: ottimizzato per le biblioteche
- **esbuild**: bundler JavaScript estremamente veloce
- **Babel**: transpiler JavaScript per compatibilità con le versioni precedenti
- **PostCSS**: elaborazione CSS con plugin

### Framework e librerie CSS
- **Bootstrap**: libreria di componenti, sistema a griglia, utilità
- **Tailwind CSS**: framework CSS incentrato sull'utilità
- **IU dei materiali**: implementazione del Material Design di Google
- **Chakra UI**: libreria di componenti accessibili
- **Ant Design**: componenti dell'interfaccia utente di livello aziendale
- **Componenti con stile**: libreria CSS-in-JS
- **Emozione**: CSS-in-JS con mappe sorgente

## Sviluppo del back-end

### Lingue lato server

#### Node.js
- **Runtime**: JavaScript sul server (motore V8)
- **Express.js**: framework web minimo, architettura middleware
- **NestJS**: architettura di ispirazione angolare, TypeScript
- **Fastify**: framework ad alte prestazioni
- **Koa**: Modern Express degli stessi creatori
- **Gestione pacchetti**: npm, filato, pnpm

#### Pitone
- **Django**: framework completo, ORM, pannello di amministrazione, batterie incluse
- **Flask**: Microframework, ecosistema di estensioni
- **FastAPI**: documentazione API moderna, asincrona e automatica
- **Piramide**: framework flessibile e scalabile

#### Altri linguaggi di backend
- **Ruby on Rails**: Convenzione sulla configurazione, ActiveRecord ORM
- **Java Spring**: framework aziendale, inserimento delle dipendenze
- **PHP Laravel**: sintassi elegante, ORM eloquente, template Blade
- **Go Gin**: prestazioni elevate, struttura minima
- **Rust Actix**: sicurezza della memoria, prestazioni
- **C# ASP.NET Core**: funzionalità aziendali multipiattaforma

### Integrazione del database

#### ORM (mappatura relazionale a oggetti)
- **Sequelizza**: Node.js ORM per database SQL
- **Prisma**: accesso al database indipendente dai tipi, client generato automaticamente
- **SQLAlchemy**: toolkit SQL Python e ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Ibernazione**: Java ORM
- **Entity Framework**: .NET ORM

#### Driver del database
- **pg**: client PostgreSQL per Node.js
- **mysql2**: client MySQL con promesse
- **pymongo**: driver MongoDB per Python
- **redis**: client Redis per più lingue

### Sviluppo dell'API#### API REST
- **Metodi HTTP**: GET, POST, PUT, PATCH, DELETE
- **Codici di stato**: 200, 201, 400, 401, 403, 404, 500
- **Nominazione delle risorse**: sostantivi, plurale, gerarchico
- **Versione**: percorso URL, intestazioni, parametri di query
- **Autenticazione**: JWT, OAuth, chiavi API
- **Documentazione**: OpenAPI/Swagger, Postman

####GraficoQL
- **Definizione dello schema**: tipi, query, mutazioni, abbonamenti
- **Resolver**: recupero dei dati a livello di campo
- **Apollo Server**: implementazione del server GraphQL
- **Relay**: client GraphQL di Facebook
- **Vantaggi**: nessun recupero eccessivo, endpoint singolo, tipizzazione forte

####gRPC
- **Buffer di protocollo**: linguaggio di definizione dell'interfaccia
- **HTTP/2**: streaming bidirezionale
- **Casi d'uso**: comunicazione di microservizi, applicazioni in tempo reale

### Autenticazione e autorizzazione
- **Basato sulla sessione**: cookie, sessioni lato server
- **Basato su token**: JWT (JSON Web Token), senza stato
- **OAuth 2.0**: framework di autorizzazione, accesso di terze parti
- **OpenID Connect**: livello di identità su OAuth 2.0
- **SAML**: Single Sign-On aziendale
- **Hashing delle password**: bcrypt, argon2, scrypt
- **Autenticazione a più fattori**: TOTP, SMS, codici email

## DevOps e distribuzione

### Controllo della versione
- **Git**: controllo della versione distribuito
- **GitHub/GitLab/Bitbucket**: hosting di repository
- **Strategie di ramificazione**: Git Flow, GitHub Flow, sviluppo basato su trunk
- **CI/CD**: pipeline di test e distribuzione automatizzate

### Containerizzazione
- **Docker**: runtime del contenitore, Dockerfile, immagini
- **Docker Compose**: orchestrazione multi-contenitore
- **Registri dei contenitori**: Docker Hub, AWS ECR, Google GCR
- **Best practice**: build in più fasi, immagini di base minime

### Orchestrazione
- **Kubernetes**: orchestrazione dei contenitori, pod, servizi, distribuzioni
- **Timone**: gestore di pacchetti Kubernetes
- **Service Mesh**: Istio, Linkerd per la rete di microservizi

### Piattaforme cloud
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: macchine virtuali, archiviazione BLOB, funzioni, AKS
- **Vercel**: distribuzione frontend, funzioni serverless
- **Netlify**: hosting di siti statici, funzioni serverless
- **Heroku**: Piattaforma come servizio (PaaS)
- **DigitalOcean**: infrastruttura cloud semplificata

### Pipeline CI/CD
- **Azioni GitHub**: automazione del flusso di lavoro
- **GitLab CI**: integrazione continua integrata
- **Jenkins**: server di automazione estensibile
- **CircleCI**: CI/CD basato su cloud
- **Travis CI**: servizio di integrazione continua
- **ArgoCD**: distribuzione continua GitOps per Kubernetes

### Monitoraggio e registrazione
- **Prestazioni dell'applicazione**: New Relic, Datadog, AppDynamics
- **Tracciamento errori**: Sentinella, Rollbar, Bugsnag
- **Registrazione**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Monitoraggio del tempo di attività**: Pingdom, UptimeRobot
- **Analisi**: Google Analytics, Mixpanel, Amplitude

## Prestazioni web

### Tecniche di ottimizzazione
- **Suddivisione del codice**: caricamento lento, importazioni dinamiche
- **Tree Shaking**: rimozione del codice inutilizzato
- **Minificazione**: riduzione delle dimensioni dei file
- **Compressione**: Gzip, Brotli
- **Caching**: cache del browser, CDN, addetti ai servizi
- **Ottimizzazione delle immagini**: WebP, AVIF, caricamento lento, immagini reattive
- **CSS critici**: incorporazione di stili Above the Fold
- **Ottimizzazione del database**: indicizzazione, ottimizzazione delle query, pooling delle connessioni

### Segnali web fondamentali
- **LCP (Largest Contentful Paint)**: prestazioni di caricamento (<2,5 s)
- **FID (First Input Delay)**: Interattività (<100ms)
- **CLS (Cumulative Layout Shift)**: stabilità visiva (<0,1)
- **INP (Interazione con Next Paint)**: metrica di reattività

### Reti per la distribuzione di contenuti (CDN)
- **Cloudflare**: sicurezza, prestazioni, DNS
- **Akamai**: CDN aziendale
- **Amazon CloudFront**: CDN AWS
- **Fastly**: piattaforma cloud Edge
- **StackPath**: servizi Edge

##Sicurezza web

### Vulnerabilità comuni (Top 10 OWASP)
- **Iniezione**: iniezione SQL, iniezione di comandi
- **Autenticazione interrotta**: dirottamento della sessione, riempimento di credenziali
- **Esposizione di dati sensibili**: dati non crittografati, crittografia debole
- **Entità esterne XML (XXE)**: vulnerabilità del parser XML
- **Controllo accesso interrotto**: escalation di privilegi, accesso non autorizzato
- **Errore di configurazione della sicurezza**: credenziali predefinite, errori dettagliati
- **Cross-Site Scripting (XSS)**: riflesso, archiviato, basato su DOM
- **Deserializzazione non sicura**: attacchi con iniezione di oggetti
- **Utilizzo di componenti con vulnerabilità note**: dipendenze obsolete
- **Registrazione e monitoraggio insufficienti**: violazioni non rilevate

### Migliori pratiche di sicurezza
- **HTTPS**: crittografia TLS/SSL, HSTS
- **Politica di sicurezza dei contenuti (CSP)**: previeni gli attacchi XSS
- **Convalida input**: disinfetta l'input dell'utente
- **Codifica output**: previene gli attacchi injection
- **Protezione CSRF**: token anti-CSRF, cookie SameSite
- **Limitazione della velocità**: previene gli attacchi di forza bruta
- **Intestazioni di sicurezza**: Opzioni X-Frame, Opzioni X-Content-Type
- **Scansione delle dipendenze**: audit npm, Snyk, Dependabot

## Test### Tipi di test
- **Test unitario**: singoli componenti/funzioni
- **Test di integrazione**: interazioni dei componenti
- **End-to-End (E2E)**: flussi di lavoro utente completi
- **Regressione visiva**: rilevamento delle modifiche all'interfaccia utente
- **Test delle prestazioni**: test di carico, stress, picchi
- **Test di accessibilità**: conformità WCAG

### Strutture di test
- **Jest**: framework di test JavaScript
- **Mocha**: test runner flessibile
- **pytest**: framework di test Python
- **RSpec**: framework di test Ruby
- **JUnit**: framework di test Java

### Strumenti di test E2E
- **Selenio**: automazione del browser
- **Cypress**: test E2E moderni
- **Drammaturgo**: automazione cross-browser
- **Burattinaio**: controllo di Chrome senza testa

## Accessibilità (a11a)

### Linee guida WCAG
- **Percepibile**: alternative testuali, didascalie, contenuti adattabili
- **Operabile**: navigazione tramite tastiera, tempo sufficiente, nessun attacco
- **Comprensibile**: leggibile, prevedibile, assistenza all'immissione
- **Robusto**: compatibile con le tecnologie assistive

### Implementazione
- **HTML semantico**: corretta gerarchia delle intestazioni, punti di riferimento
- **Attributi ARIA**: Ruoli, stati, proprietà
- **Gestione focus**: indicatori focus visibili, ordine logico delle schede
- **Contrasto colore**: rapporto minimo 4,5:1 per il testo
- **Test del lettore di schermo**: NVDA, JAWS, VoiceOver
- **Navigazione tramite tastiera**: tutti gli elementi interattivi accessibili

## App Web progressive (PWA)

### Funzionalità PWA
- **Operatori di servizio**: funzionalità offline, sincronizzazione in background
- **Manifesto app Web**: installazione di prompt, icone e colori del tema
- **App Shell**: scheletro dell'interfaccia utente memorizzato nella cache
- **Notifiche push**: coinvolgimento degli utenti
- **Design reattivo**: funziona su tutti i dispositivi
- **HTTPS obbligatorio**: contesto protetto

### Strumenti
- **Workbox**: librerie dei lavoratori del servizio
- **Faro**: controllo PWA
- **PWA Builder**: genera manifest e icone

## Tecnologie emergenti

### WebAssembly (Wasm)
- **Scopo**: esegui il codice compilato nel browser a una velocità quasi nativa
- **Lingue**: target di compilazione C++, Rust, Go
- **Casi d'uso**: giochi, editing video, crittografia, inferenza ML

### Architettura senza server
- **Funzioni come servizio**: AWS Lambda, Funzioni di Azure, Funzioni Google Cloud
- **Vantaggi**: nessuna gestione del server, scalabilità automatica, pagamento in base all'uso
- **Considerazioni**: avviamenti a freddo, vincoli al fornitore, complessità del debug

### Architettura Jamstack
- **JavaScript**: interattività lato client
- **API**: funzioni serverless, servizi di terze parti
- **Markup**: file statici predefiniti
- **Strumenti**: Next.js, Gatsby, Hugo, Eleventy
- **Vantaggi**: prestazioni, sicurezza, scalabilità, esperienza degli sviluppatori

### Comunicazione in tempo reale
- **WebSocket**: comunicazione bidirezionale
- **Eventi inviati dal server**: streaming da server a client
- **WebRTC**: video, audio e dati peer-to-peer
- **Casi d'uso**: chat, collaborazione, streaming live, giochi

### Microfrontend
- **Concetto**: estendere i microservizi al frontend
- **Approcci**: integrazione build-time, runtime, edge-side
- **Vantaggi**: implementazioni indipendenti, autonomia del team
- **Sfide**: coerenza, prestazioni, complessità