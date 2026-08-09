---
# Metadata
title: "Web Development"
description: "Frontend, backend, DevOps, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# Desenvolvimento Web
## Desenvolvimento de front-end
### Tecnologias Básicas
#### HTML (linguagem de marcação de hipertexto)
- **HTML semântico**: uso de tags significativas (`<header>`,`<nav>`,`<main>`,`<article>`,`<section>`,`<aside>`,`<footer>`)
- **Formulários**: tipos de entrada, validação, rótulos de acessibilidade
- **Mídia**: incorporação de imagens, vídeo e áudio
- **Meta Tags**: SEO, janela de visualização, codificação de caracteres
- **Recursos HTML5**: Canvas, SVG, armazenamento local, geolocalização, web sockets
#### CSS (folhas de estilo em cascata)
- **Modelo de caixa**: conteúdo, preenchimento, borda, margem
- **Sistemas de Layout**:
  - **Flexbox**: layouts unidimensionais, justificar conteúdo, alinhar itens
  - **Grid**: Layouts bidimensionais, modelo de grade, área de grade
  - **Posicionamento**: Estático, relativo, absoluto, fixo, pegajoso
- **Design responsivo**: consultas de mídia, abordagem que prioriza dispositivos móveis
- **Variáveis CSS**: propriedades personalizadas para temas
- **Animações**: transições, quadros-chave, transformações
- **Pré-processadores**: Sass, Less (variáveis, mixins, aninhamento)
#### JavaScript
- **Manipulação de DOM**: Selecionar, criar, modificar elementos
- **Eventos**: clique, envio, teclado, eventos personalizados, delegação de eventos
- **Recursos ES6+**: Funções de seta, desestruturação, propagação/repouso, módulos, assíncrono/aguardar
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: digitação estática, interfaces, genéricos, decoradores
### Estruturas front-end modernas
#### Reagir
- **Componentes**: componentes funcionais, componentes de classe
- **Hooks**: useState, useEffect, useContext, useReducer, ganchos personalizados
- **Gerenciamento de estado**: API de contexto, Redux, Zustand, Recoil
- **Roteamento**: React Router (BrowserRouter, Rotas, Rota, Link)
- **Ecossistema**: Next.js (SSR, SSG), Remix, Gatsby
- **DOM virtual**: renderização eficiente por meio de algoritmo de comparação
####Vue.js
- **API de opções**: dados, métodos, computados, observação
- **API de composição**: setup(), ref, reativo, computado
- **Diretivas**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Gestão estatal
- **Vue Router**: roteamento do lado do cliente
- **Nuxt.js**: estrutura de renderização do lado do servidor
#### angular
- **Componentes**: Decoradores, modelos, ganchos de ciclo de vida
- **Serviços**: injeção de dependência, padrão singleton
- **RxJS**: programação reativa, observáveis
- **Roteamento**: RouterModule, guardas, resolvedores
- **Formulários**: formulários reativos baseados em modelos
- **NgRx**: gerenciamento de estado estilo Redux
### Construir ferramentas e empacotadores
- **Webpack**: agrupamento de módulos, divisão de código, carregadores, plug-ins
- **Vite**: ferramenta de construção rápida usando módulos ES nativos
- **Parcel**: Bundler de configuração zero
- **Rollup**: otimizado para bibliotecas
- **esbuild**: empacotador JavaScript extremamente rápido
- **Babel**: transpilador JavaScript para compatibilidade com versões anteriores
- **PostCSS**: Processamento CSS com plugins
### Frameworks e bibliotecas CSS
- **Bootstrap**: Biblioteca de componentes, sistema de grade, utilitários
- **Tailwind CSS**: estrutura CSS utilitária
- **Material UI**: implementação do Material Design do Google
- **Chakra UI**: biblioteca de componentes acessíveis
- **Ant Design**: componentes de UI de nível empresarial
- **Componentes estilizados**: biblioteca CSS-in-JS
- **Emotion**: CSS-in-JS com mapas de origem
## Desenvolvimento de back-end
### Linguagens do lado do servidor
#### Node.js
- **Tempo de execução**: JavaScript no servidor (mecanismo V8)
- **Express.js**: estrutura web mínima, arquitetura de middleware
- **NestJS**: arquitetura de inspiração angular, TypeScript
- **Fastify**: estrutura de alto desempenho
- **Koa**: Modern Express dos mesmos criadores
- **Gerenciamento de pacotes**: npm, fio, pnpm
####Píton
- **Django**: estrutura completa, ORM, painel de administração, baterias incluídas
- **Flask**: Microframework, ecossistema de extensões
- **FastAPI**: documentação de API moderna, assíncrona e automática
- **Pirâmide**: estrutura flexível e escalável
#### Outras linguagens de back-end
- **Ruby on Rails**: Convenção sobre configuração, ActiveRecord ORM
- **Java Spring**: estrutura empresarial, injeção de dependência
- **PHP Laravel**: Sintaxe elegante, Eloquent ORM, modelos Blade
- **Go Gin**: Alto desempenho, estrutura mínima
- **Rust Actix**: Segurança de memória, desempenho
- **C# ASP.NET Core**: recursos empresariais multiplataforma
### Integração de banco de dados
#### ORMs (Mapeamento Objeto-Relacional)
- **Sequelize**: ORM Node.js para bancos de dados SQL
- **Prisma**: acesso seguro ao banco de dados, cliente gerado automaticamente
- **SQLAlchemy**: kit de ferramentas Python SQL e ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernar**: Java ORM
- **Entity Framework**: .NET ORM
#### Drivers de banco de dados
- **pg**: cliente PostgreSQL para Node.js
- **mysql2**: cliente MySQL com promessas
- **pymongo**: driver MongoDB para Python
- **redis**: cliente Redis para vários idiomas
### Desenvolvimento de APIs
####API REST
- **Métodos HTTP**: GET, POST, PUT, PATCH, DELETE
- **Códigos de status**: 200, 201, 400, 401, 403, 404, 500
- **Nomeação de recursos**: substantivos, plural, hierárquico
- **Versionamento**: caminho de URL, cabeçalhos, parâmetros de consulta
- **Autenticação**: JWT, OAuth, chaves de API
- **Documentação**: OpenAPI/Swagger, Postman
#### Gráfico QL
- **Definição de esquema**: tipos, consultas, mutações, assinaturas
- **Resolvedores**: busca de dados em nível de campo
- **Apollo Server**: implementação do servidor GraphQL
- **Relay**: cliente GraphQL do Facebook
- **Vantagens**: Sem busca excessiva, endpoint único, digitação forte
####gRPC
- **Buffers de protocolo**: linguagem de definição de interface
- **HTTP/2**: streaming bidirecional
- **Casos de uso**: comunicação de microsserviços, aplicações em tempo real
### Autenticação e Autorização
- **Baseado em sessão**: Cookies, sessões do lado do servidor
- **Baseado em token**: JWT (JSON Web Tokens), sem estado
- **OAuth 2.0**: estrutura de autorização, login de terceiros
- **OpenID Connect**: camada de identidade no OAuth 2.0
- **SAML**: logon único empresarial
- **Hashing de senha**: bcrypt, argon2, scrypt
- **Autenticação multifator**: TOTP, SMS, códigos de e-mail
## DevOps e implantação
### Controle de versão
- **Git**: controle de versão distribuído
- **GitHub/GitLab/Bitbucket**: hospedagem de repositório
- **Estratégias de ramificação**: Git Flow, GitHub Flow, desenvolvimento baseado em tronco
- **CI/CD**: testes automatizados e pipelines de implantação
### Conteinerização
- **Docker**: tempo de execução do contêiner, Dockerfile, imagens
- **Docker Compose**: orquestração de vários contêineres
- **Registros de contêineres**: Docker Hub, AWS ECR, Google GCR
- **Práticas recomendadas**: compilações em vários estágios, imagens base mínimas
### Orquestração
- **Kubernetes**: orquestração de contêineres, pods, serviços, implantações
- **Helm**: gerenciador de pacotes Kubernetes
- **Service Mesh**: Istio, Linkerd para redes de microsserviços
### Plataformas em nuvem
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Máquinas Virtuais, Armazenamento de Blobs, Funções, AKS
- **Vercel**: implantação de front-end, funções sem servidor
- **Netlify**: hospedagem de sites estáticos, funções sem servidor
- **Heroku**: Plataforma como Serviço (PaaS)
- **DigitalOcean**: infraestrutura de nuvem simplificada
### Pipelines de CI/CD
- **Ações do GitHub**: automação do fluxo de trabalho
- **GitLab CI**: integração contínua integrada
- **Jenkins**: servidor de automação extensível
- **CircleCI**: CI/CD baseado em nuvem
- **Travis CI**: serviço de integração contínua
- **ArgoCD**: entrega contínua de GitOps para Kubernetes
### Monitoramento e registro
- **Desempenho de aplicativos**: New Relic, Datadog, AppDynamics
- **Rastreamento de erros**: Sentry, Rollbar, Bugsnag
- **Registro**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Monitoramento de tempo de atividade**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude
## Desempenho da Web
### Técnicas de otimização
- **Divisão de código**: carregamento lento, importações dinâmicas
- **Tree Shaking**: Removendo código não utilizado
- **Minificação**: redução do tamanho dos arquivos
- **Compressão**: Gzip, Brotli
- **Cache**: cache do navegador, CDN, service workers
- **Otimização de imagem**: WebP, AVIF, carregamento lento, imagens responsivas
- **CSS crítico**: estilos embutidos acima da dobra
- **Otimização de banco de dados**: indexação, otimização de consulta, pool de conexões
### Principais sinais vitais da Web
- **LCP (maior pintura com conteúdo)**: desempenho de carregamento (<2,5s)
- **FID (atraso na primeira entrada)**: Interatividade (<100ms)
- **CLS (mudança cumulativa de layout)**: estabilidade visual (<0,1)
- **INP (Interação com a próxima pintura)**: métrica de capacidade de resposta
### Redes de distribuição de conteúdo (CDNs)
- **Cloudflare**: Segurança, desempenho, DNS
- **Akamai**: CDN empresarial
- **Amazon CloudFront**: AWS CDN
- **Rápido**: plataforma de nuvem Edge
- **StackPath**: serviços de borda
## Segurança na Web
### Vulnerabilidades comuns (10 principais do OWASP)
- **Injeção**: injeção SQL, injeção de comando
- **Autenticação quebrada**: sequestro de sessão, preenchimento de credenciais
- **Exposição de dados confidenciais**: dados não criptografados, criptografia fraca
- **Entidades XML externas (XXE)**: vulnerabilidades do analisador XML
- **Controle de acesso quebrado**: escalonamento de privilégios, acesso não autorizado
- **Configuração incorreta de segurança**: credenciais padrão, erros detalhados
- **Cross-Site Scripting (XSS)**: refletido, armazenado, baseado em DOM
- **Desserialização insegura**: ataques de injeção de objetos
- **Uso de componentes com vulnerabilidades conhecidas**: dependências desatualizadas
- **Registro e monitoramento insuficientes**: violações não detectadas
### Melhores práticas de segurança
- **HTTPS**: criptografia TLS/SSL, HSTS
- **Política de Segurança de Conteúdo (CSP)**: Prevenir ataques XSS
- **Validação de entrada**: Sanitize a entrada do usuário
- **Codificação de saída**: evita ataques de injeção
- **Proteção CSRF**: tokens anti-CSRF, cookies SameSite
- **Limitação de taxa**: evita ataques de força bruta
- **Cabeçalhos de segurança**: X-Frame-Options, X-Content-Type-Options
- **Verificação de dependências**: auditoria npm, Snyk, Dependabot
## Teste
### Tipos de teste
- **Teste unitário**: componentes/funções individuais
- **Teste de integração**: interações de componentes
- **End-to-End (E2E)**: fluxos de trabalho completos do usuário
- **Regressão visual**: detecção de alterações na IU
- **Testes de desempenho**: testes de carga, estresse e pico
- **Teste de acessibilidade**: conformidade com WCAG
### Estruturas de teste
- **Jest**: estrutura de teste de JavaScript
- **Mocha**: executor de testes flexível
- **pytest**: estrutura de teste Python
- **RSpec**: estrutura de teste Ruby
- **JUnit**: estrutura de teste Java
### Ferramentas de teste E2E
- **Selenium**: automação do navegador
- **Cypress**: testes E2E modernos
- **Dramaturgo**: Automação entre navegadores
- **Marionetista**: controle do Chrome sem cabeça
## Acessibilidade (a11y)
### Diretrizes WCAG
- **Perceptível**: alternativas de texto, legendas, conteúdo adaptável
- **Operável**: Navegação pelo teclado, tempo suficiente, sem convulsões
- **Compreensível**: assistência de entrada legível e previsível
- **Robusto**: Compatível com tecnologias assistivas
### Implementação
- **HTML semântico**: hierarquia de títulos adequada, pontos de referência
- **Atributos ARIA**: funções, estados, propriedades
- **Gerenciamento de foco**: indicadores de foco visíveis, ordem lógica de guias
- **Contraste de cores**: proporção mínima de 4,5:1 para texto
- **Teste de leitor de tela**: NVDA, JAWS, VoiceOver
- **Navegação pelo teclado**: todos os elementos interativos acessíveis
## Aplicativos Web Progressivos (PWAs)
### Recursos do PWA
- **Service Workers**: funcionalidade offline, sincronização em segundo plano
- **Manifesto do aplicativo Web**: prompt de instalação, ícones e cores do tema
- **App Shell**: esqueleto da UI em cache
- **Notificações push**: envolvimento do usuário
- **Design responsivo**: funciona em todos os dispositivos
- **HTTPS obrigatório**: contexto seguro
### Ferramentas
- **Workbox**: bibliotecas de service workers
- **Lighthouse**: auditoria PWA
- **PWA Builder**: Gere manifestos e ícones
## Tecnologias Emergentes
### WebAssembly (Wasm)
- **Objetivo**: Executar código compilado no navegador em velocidade quase nativa
- **Idiomas**: alvos de compilação C++, Rust, Go
- **Casos de uso**: jogos, edição de vídeo, criptografia, inferência de ML
### Arquitetura sem servidor
- **Funções como serviço**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefícios**: Sem gerenciamento de servidor, escalonamento automático, pagamento conforme uso
- **Considerações**: Partidas a frio, dependência de fornecedor, complexidade de depuração
### Arquitetura Jamstack
- **JavaScript**: interatividade do lado do cliente
- **APIs**: funções sem servidor, serviços de terceiros
- **Marcação**: arquivos estáticos pré-construídos
- **Ferramentas**: Next.js, Gatsby, Hugo, Eleventy
- **Benefícios**: desempenho, segurança, escalabilidade, experiência do desenvolvedor
### Comunicação em tempo real
- **WebSockets**: comunicação bidirecional
- **Eventos enviados pelo servidor**: streaming de servidor para cliente
- **WebRTC**: vídeo, áudio e dados ponto a ponto
- **Casos de uso**: bate-papo, colaboração, transmissão ao vivo, jogos
### Microfront-ends
- **Conceito**: Estender microsserviços para front-end
- **Abordagens**: integração em tempo de construção, tempo de execução e borda
- **Benefícios**: Implantações independentes, autonomia da equipe
- **Desafios**: Consistência, desempenho, complexidade