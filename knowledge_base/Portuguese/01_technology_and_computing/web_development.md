# Desenvolvimento Web

## Desenvolvimento Frontend

### Tecnologias Fundamentais

#### HTML (HyperText Markup Language)
- **HTML Semântico**: Uso de tags significativas (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Formulários**: Tipos de input, validação, labels de acessibilidade
- **Mídia**: Incorporação de imagens, vídeo e áudio
- **Meta Tags**: SEO, viewport, codificação de caracteres
- **Recursos do HTML5**: Canvas, SVG, local storage, geolocalização, web sockets

#### CSS (Cascading Style Sheets)
- **Box Model**: Conteúdo, padding, border, margin
- **Sistemas de Layout**:
  - **Flexbox**: Layouts unidimensionais, justify-content, align-items
  - **Grid**: Layouts bidimensionais, grid-template, grid-area
  - **Positioning**: Static, relative, absolute, fixed, sticky
- **Design Responsivo**: Media queries, abordagem mobile-first
- **Variáveis CSS**: Propriedades customizadas para temas
- **Animações**: Transitions, keyframes, transforms
- **Pré-processadores**: Sass, Less (variáveis, mixins, aninhamento)

#### JavaScript
- **Manipulação do DOM**: Selecionar, criar e modificar elementos
- **Eventos**: Click, submit, teclado, eventos customizados, event delegation
- **Recursos ES6+**: Arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Tipagem estática, interfaces, generics, decorators

### Frameworks Frontend Modernos

#### React
- **Components**: Functional components, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **Gerenciamento de Estado**: Context API, Redux, Zustand, Recoil
- **Roteamento**: React Router (BrowserRouter, Routes, Route, Link)
- **Ecossistema**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Renderização eficiente por meio do algoritmo de diff

#### Vue.js
- **Options API**: data, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Directives**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Gerenciamento de estado
- **Vue Router**: Roteamento no lado do cliente
- **Nuxt.js**: Framework para server-side rendering

#### Angular
- **Components**: Decorators, templates, lifecycle hooks
- **Services**: Injeção de dependência, padrão singleton
- **RxJS**: Programação reativa, observables
- **Routing**: RouterModule, guards, resolvers
- **Forms**: Template-driven, reactive forms
- **NgRx**: Gerenciamento de estado no estilo Redux

### Ferramentas de Build e Bundlers
- **Webpack**: Empacotamento de módulos, code splitting, loaders, plugins
- **Vite**: Ferramenta de build rápida usando ES modules nativos
- **Parcel**: Bundler com configuração zero
- **Rollup**: Otimizado para bibliotecas
- **esbuild**: Bundler JavaScript extremamente rápido
- **Babel**: Transpilador JavaScript para compatibilidade retroativa
- **PostCSS**: Processamento de CSS com plugins

### Frameworks e Bibliotecas CSS
- **Bootstrap**: Biblioteca de componentes, grid system, utilitários
- **Tailwind CSS**: Framework CSS utility-first
- **Material UI**: Implementação do Material Design do Google
- **Chakra UI**: Biblioteca de componentes acessível
- **Ant Design**: Componentes de UI em nível corporativo
- **Styled Components**: Biblioteca CSS-in-JS
- **Emotion**: CSS-in-JS com source maps

## Desenvolvimento Backend

### Linguagens Server-Side

#### Node.js
- **Runtime**: JavaScript no servidor (engine V8)
- **Express.js**: Framework web minimalista, arquitetura de middleware
- **NestJS**: Arquitetura inspirada em Angular, TypeScript
- **Fastify**: Framework de alto desempenho
- **Koa**: Express moderno dos mesmos criadores
- **Gerenciamento de Pacotes**: npm, yarn, pnpm

#### Python
- **Django**: Framework completo, ORM, painel admin, batteries-included
- **Flask**: Microframework, ecossistema de extensões
- **FastAPI**: Moderno, assíncrono, documentação automática de API
- **Pyramid**: Framework flexível e escalável

#### Outras Linguagens de Backend
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Framework corporativo, injeção de dependência
- **PHP Laravel**: Sintaxe elegante, Eloquent ORM, templates Blade
- **Go Gin**: Alto desempenho, framework minimalista
- **Rust Actix**: Segurança de memória, desempenho
- **C# ASP.NET Core**: Multiplataforma, recursos corporativos

### Integração com Banco de Dados

#### ORMs (Object-Relational Mapping)
- **Sequelize**: ORM de Node.js para bancos SQL
- **Prisma**: Acesso ao banco com type safety, client gerado automaticamente
- **SQLAlchemy**: Toolkit SQL e ORM para Python
- **ActiveRecord**: ORM do Ruby on Rails
- **Hibernate**: ORM para Java
- **Entity Framework**: ORM para .NET

#### Drivers de Banco de Dados
- **pg**: Cliente PostgreSQL para Node.js
- **mysql2**: Cliente MySQL com promises
- **pymongo**: Driver MongoDB para Python
- **redis**: Cliente Redis para várias linguagens

### Desenvolvimento de APIs

#### APIs REST
- **Métodos HTTP**: GET, POST, PUT, PATCH, DELETE
- **Códigos de Status**: 200, 201, 400, 401, 403, 404, 500
- **Nomeação de Recursos**: Substantivos, plural, hierárquica
- **Versionamento**: Caminho na URL, headers, query parameters
- **Autenticação**: JWT, OAuth, chaves de API
- **Documentação**: OpenAPI/Swagger, Postman

#### GraphQL
- **Definição de Schema**: Types, queries, mutations, subscriptions
- **Resolvers**: Busca de dados no nível de campo
- **Apollo Server**: Implementação de servidor GraphQL
- **Relay**: Cliente GraphQL do Facebook
- **Vantagens**: Sem over-fetching, endpoint único, tipagem forte

#### gRPC
- **Protocol Buffers**: Linguagem de definição de interfaces
- **HTTP/2**: Streaming bidirecional
- **Casos de Uso**: Comunicação entre microservices, aplicações em tempo real

### Autenticação e Autorização
- **Baseada em Sessão**: Cookies, sessões no lado do servidor
- **Baseada em Token**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Framework de autorização, login de terceiros
- **OpenID Connect**: Camada de identidade sobre OAuth 2.0
- **SAML**: Single sign-on corporativo
- **Hash de Senhas**: bcrypt, argon2, scrypt
- **Autenticação Multifator**: TOTP, SMS, códigos por e-mail

## DevOps e Deploy

### Controle de Versão
- **Git**: Controle de versão distribuído
- **GitHub/GitLab/Bitbucket**: Hospedagem de repositórios
- **Estratégias de Branching**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Pipelines automatizados de teste e deploy

### Containerização
- **Docker**: Runtime de containers, Dockerfile, images
- **Docker Compose**: Orquestração de múltiplos containers
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **Boas Práticas**: Multi-stage builds, imagens base mínimas

### Orquestração
- **Kubernetes**: Orquestração de containers, pods, services, deployments
- **Helm**: Gerenciador de pacotes do Kubernetes
- **Service Mesh**: Istio, Linkerd para rede de microservices

### Plataformas de Nuvem
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Deploy de frontend, funções serverless
- **Netlify**: Hospedagem de sites estáticos, funções serverless
- **Heroku**: Plataforma como Serviço (PaaS)
- **DigitalOcean**: Infraestrutura de nuvem simplificada

### Pipelines de CI/CD
- **GitHub Actions**: Automação de workflows
- **GitLab CI**: Integração contínua embutida
- **Jenkins**: Servidor de automação extensível
- **CircleCI**: CI/CD baseado em nuvem
- **Travis CI**: Serviço de integração contínua
- **ArgoCD**: Entrega contínua GitOps para Kubernetes

### Monitoramento e Logging
- **Desempenho de Aplicações**: New Relic, Datadog, AppDynamics
- **Rastreamento de Erros**: Sentry, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Monitoramento de Uptime**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Performance Web

### Técnicas de Otimização
- **Code Splitting**: Lazy loading, imports dinâmicos
- **Tree Shaking**: Remoção de código não utilizado
- **Minification**: Redução do tamanho dos arquivos
- **Compression**: Gzip, Brotli
- **Caching**: Cache do navegador, CDN, service workers
- **Otimização de Imagens**: WebP, AVIF, lazy loading, imagens responsivas
- **Critical CSS**: Inline dos estilos above-the-fold
- **Otimização de Banco de Dados**: Indexação, otimização de consultas, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Desempenho de carregamento (<2.5s)
- **FID (First Input Delay)**: Interatividade (<100ms)
- **CLS (Cumulative Layout Shift)**: Estabilidade visual (<0.1)
- **INP (Interaction to Next Paint)**: Métrica de responsividade

### Redes de Entrega de Conteúdo (CDNs)
- **Cloudflare**: Segurança, desempenho, DNS
- **Akamai**: CDN corporativa
- **Amazon CloudFront**: CDN da AWS
- **Fastly**: Plataforma de edge cloud
- **StackPath**: Serviços de edge

## Segurança Web

### Vulnerabilidades Comuns (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Sequestro de sessão, credential stuffing
- **Sensitive Data Exposure**: Dados não criptografados, criptografia fraca
- **XML External Entities (XXE)**: Vulnerabilidades em parsers XML
- **Broken Access Control**: Escalonamento de privilégio, acesso não autorizado
- **Security Misconfiguration**: Credenciais padrão, erros detalhados demais
- **Cross-Site Scripting (XSS)**: Refletido, armazenado, baseado em DOM
- **Insecure Deserialization**: Ataques de object injection
- **Using Components with Known Vulnerabilities**: Dependências desatualizadas
- **Insufficient Logging & Monitoring**: Violações não detectadas

### Boas Práticas de Segurança
- **HTTPS**: Criptografia TLS/SSL, HSTS
- **Content Security Policy (CSP)**: Prevenir ataques XSS
- **Validação de Entrada**: Sanitizar dados fornecidos pelo usuário
- **Codificação de Saída**: Prevenir ataques de injeção
- **Proteção contra CSRF**: Tokens anti-CSRF, cookies SameSite
- **Rate Limiting**: Prevenir ataques de força bruta
- **Security Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Testes

### Tipos de Teste
- **Testes Unitários**: Componentes/funções individuais
- **Testes de Integração**: Interações entre componentes
- **End-to-End (E2E)**: Fluxos completos de usuário
- **Regressão Visual**: Detecção de mudanças na UI
- **Testes de Performance**: Testes de carga, estresse e pico
- **Testes de Acessibilidade**: Conformidade com WCAG

### Frameworks de Teste
- **Jest**: Framework de testes para JavaScript
- **Mocha**: Test runner flexível
- **pytest**: Framework de testes para Python
- **RSpec**: Framework de testes para Ruby
- **JUnit**: Framework de testes para Java

### Ferramentas de Teste E2E
- **Selenium**: Automação de navegador
- **Cypress**: Testes E2E modernos
- **Playwright**: Automação cross-browser
- **Puppeteer**: Controle de Chrome headless

## Acessibilidade (a11y)

### Diretrizes WCAG
- **Perceptível**: Alternativas em texto, legendas, conteúdo adaptável
- **Operável**: Navegação por teclado, tempo suficiente, sem convulsões
- **Compreensível**: Legível, previsível, ajuda na entrada de dados
- **Robusto**: Compatível com tecnologias assistivas

### Implementação
- **HTML Semântico**: Hierarquia correta de headings, landmarks
- **Atributos ARIA**: Roles, states, properties
- **Gerenciamento de Foco**: Indicadores visíveis de foco, ordem lógica de tabulação
- **Contraste de Cor**: Proporção mínima de 4.5:1 para texto
- **Teste com Leitores de Tela**: NVDA, JAWS, VoiceOver
- **Navegação por Teclado**: Todos os elementos interativos acessíveis

## Progressive Web Apps (PWAs)

### Recursos de PWA
- **Service Workers**: Funcionalidade offline, sincronização em segundo plano
- **Web App Manifest**: Prompt de instalação, ícones, cores de tema
- **App Shell**: Esqueleto de UI em cache
- **Push Notifications**: Engajamento do usuário
- **Design Responsivo**: Funciona em todos os dispositivos
- **HTTPS Required**: Contexto seguro

### Ferramentas
- **Workbox**: Bibliotecas para service worker
- **Lighthouse**: Auditoria de PWA
- **PWA Builder**: Geração de manifests e ícones

## Tecnologias Emergentes

### WebAssembly (Wasm)
- **Objetivo**: Executar código compilado no navegador com velocidade próxima à nativa
- **Linguagens**: Alvos de compilação em C++, Rust e Go
- **Casos de Uso**: Jogos, edição de vídeo, criptografia, inferência de ML

### Arquitetura Serverless
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefícios**: Sem gerenciamento de servidores, auto-scaling, pagamento por uso
- **Considerações**: Cold starts, vendor lock-in, complexidade de depuração

### Arquitetura Jamstack
- **JavaScript**: Interatividade no lado do cliente
- **APIs**: Funções serverless, serviços de terceiros
- **Markup**: Arquivos estáticos pré-construídos
- **Ferramentas**: Next.js, Gatsby, Hugo, Eleventy
- **Benefícios**: Performance, segurança, escalabilidade, experiência do desenvolvedor

### Comunicação em Tempo Real
- **WebSockets**: Comunicação bidirecional
- **Server-Sent Events**: Streaming do servidor para o cliente
- **WebRTC**: Vídeo, áudio e dados peer-to-peer
- **Casos de Uso**: Chat, colaboração, live streaming, jogos

### Micro Frontends
- **Conceito**: Estender microservices ao frontend
- **Abordagens**: Integração em build-time, run-time e edge-side
- **Benefícios**: Implantações independentes, autonomia das equipes
- **Desafios**: Consistência, desempenho, complexidade
