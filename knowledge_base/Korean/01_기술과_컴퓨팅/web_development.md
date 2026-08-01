<!-- 
This file was automatically translated from English to Korean.
Source: web_development.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 웹 개발

## Frontend 개발

### 핵심 기술

#### HTML (HyperText Markup Language)
- **Semantic HTML**: 의미에 맞는 태그를 사용합니다 (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`).
- **Forms**: 입력 유형, 유효성 검사, 접근성 레이블을 다룹니다.
- **Media**: 이미지, 비디오, 오디오를 문서에 삽입합니다.
- **Meta Tags**: SEO, viewport, 문자 인코딩 등을 설정합니다.
- **HTML5 Features**: Canvas, SVG, local storage, geolocation, WebSockets 등을 포함합니다.

#### CSS (Cascading Style Sheets)
- **Box Model**: content, padding, border, margin으로 구성됩니다.
- **Layout 시스템**:
  - **Flexbox**: 한 방향 레이아웃에 적합하며 `justify-content`, `align-items` 등을 사용합니다.
  - **Grid**: 2차원 레이아웃에 적합하며 `grid-template`, `grid-area` 등을 사용합니다.
  - **Positioning**: static, relative, absolute, fixed, sticky 배치를 지원합니다.
- **Responsive Design**: media query와 mobile-first 접근 방식을 사용합니다.
- **CSS Variables**: 테마 구성을 위해 사용하는 custom properties입니다.
- **Animations**: transition, keyframes, transform 등을 활용합니다.
- **Preprocessors**: Sass, Less를 사용해 variables, mixins, nesting을 지원합니다.

#### JavaScript
- **DOM Manipulation**: 요소를 선택하고, 생성하고, 수정합니다.
- **이벤트**: click, submit, keyboard, custom event, event delegation을 다룹니다.
- **ES6+ Features**: arrow function, destructuring, spread/rest, modules, async/await를 포함합니다.
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage 등을 사용합니다.
- **TypeScript**: 정적 타이핑, interfaces, generics, decorators를 제공합니다.

### 현대적인 Frontend Frameworks

#### React
- **Components**: functional components와 class components를 사용합니다.
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks를 포함합니다.
- **State 관리**: Context API, Redux, Zustand, Recoil을 활용합니다.
- **Routing**: React Router (BrowserRouter, Routes, Route, Link)를 사용합니다.
- **Ecosystem**: Next.js (SSR, SSG), Remix, Gatsby 등이 있습니다.
- **Virtual DOM**: diffing algorithm을 통해 효율적으로 렌더링합니다.

#### Vue.js
- **Options API**: data, methods, computed, watch를 사용합니다.
- **Composition API**: setup(), ref, reactive, computed를 사용합니다.
- **Directives**: v-if, v-for, v-bind, v-on, v-model을 제공합니다.
- **Vuex/Pinia**: state 관리 도구입니다.
- **Vue Router**: 클라이언트 사이드 라우팅을 담당합니다.
- **Nuxt.js**: server-side rendering을 지원하는 프레임워크입니다.

#### Angular
- **Components**: decorators, templates, lifecycle hooks를 사용합니다.
- **Services**: dependency injection과 singleton pattern을 지원합니다.
- **RxJS**: reactive programming과 observables를 제공합니다.
- **Routing**: RouterModule, guards, resolvers를 사용합니다.
- **Forms**: template-driven forms와 reactive forms를 지원합니다.
- **NgRx**: Redux 스타일의 state 관리 도구입니다.

### Build Tools와 Bundlers
- **Webpack**: module bundling, code splitting, loaders, plugins를 제공합니다.
- **Vite**: native ES modules를 활용하는 빠른 build tool입니다.
- **Parcel**: 별도 설정이 거의 필요 없는 bundler입니다.
- **Rollup**: library 번들링에 최적화되어 있습니다.
- **esbuild**: 매우 빠른 JavaScript bundler입니다.
- **Babel**: 하위 호환성을 위해 JavaScript 코드를 변환하는 transpiler입니다.
- **PostCSS**: plugin 기반 CSS processing 도구입니다.

### CSS Frameworks와 Libraries
- **Bootstrap**: component library, grid system, utilities를 제공합니다.
- **Tailwind CSS**: utility-first CSS framework입니다.
- **Material UI**: Google의 Material Design 구현체입니다.
- **Chakra UI**: 접근성을 고려한 component library입니다.
- **Ant Design**: 엔터프라이즈급 UI components를 제공합니다.
- **Styled Components**: CSS-in-JS library입니다.
- **Emotion**: source maps를 지원하는 CSS-in-JS 도구입니다.

## Backend 개발

### Server-Side Languages

#### Node.js
- **Runtime**: 서버에서 JavaScript를 실행하는 환경입니다 (V8 engine).
- **Express.js**: middleware 아키텍처를 사용하는 최소한의 web framework입니다.
- **NestJS**: Angular에서 영감을 받은 TypeScript 기반 아키텍처를 제공합니다.
- **Fastify**: 높은 성능을 목표로 하는 framework입니다.
- **Koa**: Express 제작진이 만든 현대적인 framework입니다.
- **Package 관리**: npm, yarn, pnpm을 사용합니다.

#### Python
- **Django**: ORM, admin panel, batteries-included 철학을 갖춘 풀스택 framework입니다.
- **Flask**: 확장 생태계가 풍부한 microframework입니다.
- **FastAPI**: async 지원과 자동 API documentation이 강점인 현대적 framework입니다.
- **Pyramid**: 유연성과 확장성이 높은 framework입니다.

#### 기타 Backend Languages
- **Ruby on Rails**: convention over configuration과 ActiveRecord ORM이 특징입니다.
- **Java Spring**: 엔터프라이즈 환경에서 널리 쓰이는 dependency injection framework입니다.
- **PHP Laravel**: 우아한 문법, Eloquent ORM, Blade templating을 제공합니다.
- **Go Gin**: 높은 성능의 경량 framework입니다.
- **Rust Actix**: 메모리 안정성과 성능이 강점입니다.
- **C# ASP.NET Core**: 크로스플랫폼과 엔터프라이즈 기능을 모두 제공합니다.

### 데이터베이스 연동

#### ORMs (Object-Relational Mapping)
- **Sequelize**: SQL 데이터베이스용 Node.js ORM입니다.
- **Prisma**: type-safe 데이터베이스 접근과 자동 생성 client를 제공합니다.
- **SQLAlchemy**: Python용 SQL toolkit이자 ORM입니다.
- **ActiveRecord**: Ruby on Rails의 ORM입니다.
- **Hibernate**: Java ORM입니다.
- **Entity Framework**: .NET ORM입니다.

#### 데이터베이스 Drivers
- **pg**: Node.js용 PostgreSQL client입니다.
- **mysql2**: promise를 지원하는 MySQL client입니다.
- **pymongo**: Python용 MongoDB driver입니다.
- **redis**: 여러 언어에서 사용하는 Redis client입니다.

### API 개발

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Resource Naming**: 명사형, 복수형, 계층형 구조를 권장합니다.
- **Versioning**: URL path, headers, query parameters로 관리할 수 있습니다.
- **Authentication**: JWT, OAuth, API keys를 사용합니다.
- **Documentation**: OpenAPI/Swagger, Postman 등을 활용합니다.

#### GraphQL
- **Schema Definition**: types, queries, mutations, subscriptions를 정의합니다.
- **Resolvers**: field 단위로 데이터를 조회합니다.
- **Apollo Server**: GraphQL server 구현체입니다.
- **Relay**: Facebook의 GraphQL client입니다.
- **Advantages**: over-fetching이 없고, 단일 endpoint와 강한 typing을 제공합니다.

#### gRPC
- **Protocol Buffers**: interface definition language로 사용됩니다.
- **HTTP/2**: 양방향 streaming을 지원합니다.
- **Use Cases**: microservices 간 통신, 실시간 애플리케이션에 적합합니다.

### Authentication과 Authorization
- **Session-based**: cookies와 server-side sessions를 사용합니다.
- **Token-based**: JWT(JSON Web Tokens) 기반의 stateless 방식입니다.
- **OAuth 2.0**: 제3자 로그인을 포함한 authorization framework입니다.
- **OpenID Connect**: OAuth 2.0 위에 identity layer를 추가한 규격입니다.
- **SAML**: 엔터프라이즈 single sign-on에 자주 사용됩니다.
- **Password Hashing**: bcrypt, argon2, scrypt를 사용합니다.
- **Multi-Factor Authentication**: TOTP, SMS, email code 등을 활용합니다.

## DevOps와 배포

### Version Control
- **Git**: 분산 버전 관리 시스템입니다.
- **GitHub/GitLab/Bitbucket**: 저장소 호스팅 서비스입니다.
- **Branching Strategies**: Git Flow, GitHub Flow, trunk-based development가 있습니다.
- **CI/CD**: 테스트와 배포 파이프라인을 자동화합니다.

### Containerization
- **Docker**: container runtime과 Dockerfile, image 생태계를 제공합니다.
- **Docker Compose**: 여러 container를 함께 오케스트레이션합니다.
- **Container Registries**: Docker Hub, AWS ECR, Google GCR 등을 사용합니다.
- **모범 사례**: multi-stage build와 최소한의 base image를 권장합니다.

### Orchestration
- **Kubernetes**: pods, services, deployments를 기반으로 하는 container orchestration 플랫폼입니다.
- **Helm**: Kubernetes용 package manager입니다.
- **Service Mesh**: Istio, Linkerd를 통해 microservices 네트워킹을 관리합니다.

### Cloud Platforms
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: frontend 배포와 serverless functions에 강점이 있습니다.
- **Netlify**: 정적 사이트 호스팅과 serverless functions를 지원합니다.
- **Heroku**: Platform as a Service (PaaS)입니다.
- **DigitalOcean**: 단순한 클라우드 인프라를 제공합니다.

### CI/CD Pipelines
- **GitHub Actions**: workflow automation 도구입니다.
- **GitLab CI**: GitLab에 내장된 continuous integration 도구입니다.
- **Jenkins**: 확장성이 높은 automation server입니다.
- **CircleCI**: 클라우드 기반 CI/CD 서비스입니다.
- **Travis CI**: continuous integration 서비스입니다.
- **ArgoCD**: Kubernetes용 GitOps continuous delivery 도구입니다.

### Monitoring과 Logging
- **Application 성능**: New Relic, Datadog, AppDynamics를 사용합니다.
- **Error Tracking**: Sentry, Rollbar, Bugsnag이 대표적입니다.
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk 등을 활용합니다.
- **Uptime Monitoring**: Pingdom, UptimeRobot으로 가용성을 확인합니다.
- **Analytics**: Google Analytics, Mixpanel, Amplitude 등을 사용합니다.

## 웹 성능

### Optimization Techniques
- **Code Splitting**: lazy loading과 dynamic imports를 사용합니다.
- **Tree Shaking**: 사용하지 않는 코드를 제거합니다.
- **Minification**: 파일 크기를 줄입니다.
- **Compression**: Gzip, Brotli를 사용합니다.
- **Caching**: browser cache, CDN, service workers를 활용합니다.
- **Image Optimization**: WebP, AVIF, lazy loading, responsive images를 적용합니다.
- **Critical CSS**: above-the-fold 스타일을 인라인으로 넣습니다.
- **데이터베이스 Optimization**: indexing, query optimization, connection pooling을 수행합니다.

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: 로딩 성능 지표입니다 (<2.5s).
- **FID (First Input Delay)**: 상호작용 지표입니다 (<100ms).
- **CLS (Cumulative Layout Shift)**: 시각적 안정성 지표입니다 (<0.1).
- **INP (Interaction to Next Paint)**: 반응성을 측정하는 지표입니다.

### Content Delivery Networks (CDNs)
- **Cloudflare**: 보안, 성능, DNS 기능에 강점이 있습니다.
- **Akamai**: 엔터프라이즈급 CDN입니다.
- **Amazon CloudFront**: AWS의 CDN 서비스입니다.
- **Fastly**: edge cloud platform입니다.
- **StackPath**: edge services를 제공합니다.

## 웹 보안

### Common Vulnerabilities (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: session hijacking, credential stuffing
- **Sensitive Data Exposure**: 암호화되지 않은 데이터, 약한 암호화 방식
- **XML External Entities (XXE)**: XML parser 취약점
- **Broken Access Control**: privilege escalation, unauthorized access
- **Security Misconfiguration**: 기본 자격 증명, 지나치게 자세한 오류 메시지
- **Cross-Site Scripting (XSS)**: reflected, stored, DOM-based
- **Insecure Deserialization**: 객체 주입 공격
- **Using Components with Known Vulnerabilities**: 오래된 dependency 사용
- **Insufficient Logging & Monitoring**: 침해를 제때 탐지하지 못하는 상태

### 보안 모범 사례
- **HTTPS**: TLS/SSL encryption, HSTS를 사용합니다.
- **Content Security Policy (CSP)**: XSS 공격을 예방합니다.
- **Input Validation**: 사용자 입력을 검증하고 정제합니다.
- **Output Encoding**: injection 공격을 방지합니다.
- **CSRF Protection**: anti-CSRF token, SameSite cookie 등을 사용합니다.
- **Rate Limiting**: brute force 공격을 완화합니다.
- **보안 Headers**: X-Frame-Options, X-Content-Type-Options 등을 설정합니다.
- **Dependency Scanning**: npm audit, Snyk, Dependabot 등을 활용합니다.

## 테스트

### 테스트 유형
- **Unit 테스트**: 개별 component나 function을 검증합니다.
- **Integration 테스트**: component 간 상호작용을 검증합니다.
- **End-to-End (E2E)**: 실제 사용자 흐름 전체를 검증합니다.
- **Visual Regression**: UI 변경을 감지합니다.
- **성능 테스트**: load, stress, spike 테스트를 수행합니다.
- **Accessibility 테스트**: WCAG 준수 여부를 확인합니다.

### 테스트 Frameworks
- **Jest**: JavaScript 테스트 framework입니다.
- **Mocha**: 유연한 test runner입니다.
- **pytest**: Python 테스트 framework입니다.
- **RSpec**: Ruby 테스트 framework입니다.
- **JUnit**: Java 테스트 framework입니다.

### E2E 테스트 Tools
- **Selenium**: browser automation 도구입니다.
- **Cypress**: 현대적인 E2E 테스트 도구입니다.
- **Playwright**: cross-browser automation 도구입니다.
- **Puppeteer**: headless Chrome 제어 도구입니다.

## Accessibility (a11y)

### WCAG Guidelines
- **Perceivable**: 텍스트 대체 수단, 자막, 적응형 콘텐츠를 제공합니다.
- **Operable**: 키보드 내비게이션이 가능하고, 충분한 시간을 제공하며, 발작을 유발하지 않아야 합니다.
- **Understandable**: 읽기 쉽고 예측 가능하며 입력 보조가 제공되어야 합니다.
- **Robust**: assistive technologies와 호환되어야 합니다.

### Implementation
- **Semantic HTML**: 올바른 heading hierarchy와 landmarks를 사용합니다.
- **ARIA Attributes**: roles, states, properties를 적절히 사용합니다.
- **Focus 관리**: 눈에 보이는 focus indicator와 논리적인 tab order를 제공합니다.
- **Color Contrast**: 텍스트에 최소 4.5:1 대비를 유지합니다.
- **Screen Reader 테스트**: NVDA, JAWS, VoiceOver 등으로 확인합니다.
- **Keyboard Navigation**: 모든 상호작용 요소가 키보드로 접근 가능해야 합니다.

## Progressive Web Apps (PWAs)

### PWA Features
- **Service Workers**: 오프라인 기능과 background sync를 제공합니다.
- **Web App Manifest**: 설치 프롬프트, 아이콘, 테마 색상을 정의합니다.
- **App Shell**: 캐시된 UI 골격을 제공합니다.
- **Push Notifications**: 사용자 참여를 높입니다.
- **Responsive Design**: 모든 기기에서 동작합니다.
- **HTTPS Required**: 보안 컨텍스트가 필수입니다.

### Tools
- **Workbox**: service worker library입니다.
- **Lighthouse**: PWA 품질을 점검하는 auditing 도구입니다.
- **PWA Builder**: manifest와 icon 생성을 돕습니다.

## Emerging Technologies

### WebAssembly (Wasm)
- **Purpose**: 브라우저에서 거의 네이티브에 가까운 속도로 컴파일된 코드를 실행합니다.
- **Languages**: C++, Rust, Go 등을 컴파일 타깃으로 사용할 수 있습니다.
- **Use Cases**: 게임, 비디오 편집, 암호화, ML inference 등에 활용됩니다.

### Serverless 아키텍처
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Benefits**: 서버 관리가 필요 없고, 자동 확장되며, 사용량 기반으로 과금됩니다.
- **고려사항**: cold start, vendor lock-in, 디버깅 복잡성이 있습니다.

### Jamstack 아키텍처
- **JavaScript**: 클라이언트 측 상호작용을 담당합니다.
- **APIs**: serverless functions와 third-party services를 활용합니다.
- **Markup**: 미리 빌드된 정적 파일을 사용합니다.
- **Tools**: Next.js, Gatsby, Hugo, Eleventy
- **Benefits**: 성능, 보안, 확장성, developer experience를 향상시킵니다.

### Real-Time 의사소통
- **WebSockets**: 양방향 의사소통을 지원합니다.
- **Server-Sent Events**: 서버에서 클라이언트로의 스트리밍을 지원합니다.
- **WebRTC**: peer-to-peer video, audio, data 통신을 지원합니다.
- **Use Cases**: 채팅, 협업, 라이브 스트리밍, 게임 등에 적합합니다.

### Micro Frontends
- **Concept**: microservices 개념을 frontend까지 확장한 방식입니다.
- **Approaches**: build-time, run-time, edge-side integration 방식이 있습니다.
- **Benefits**: 독립적인 배포와 팀 자율성을 높여 줍니다.
- **Challenges**: 일관성 유지, 성능, 복잡성 관리가 필요합니다.
