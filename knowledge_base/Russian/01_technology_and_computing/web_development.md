# Веб-разработка

## Frontend-разработка

### Базовые технологии

#### HTML (HyperText Markup Language)
- **Семантический HTML**: использование осмысленных тегов (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Формы**: типы input, валидация, метки доступности
- **Медиа**: встраивание изображений, видео и аудио
- **Meta Tags**: SEO, viewport, кодировка символов
- **Возможности HTML5**: Canvas, SVG, локальное хранилище, геолокация, WebSocket

#### CSS (Cascading Style Sheets)
- **Box Model**: content, padding, border, margin
- **Системы компоновки**:
  - **Flexbox**: одномерные макеты, justify-content, align-items
  - **Grid**: двумерные макеты, grid-template, grid-area
  - **Positioning**: static, relative, absolute, fixed, sticky
- **Адаптивный дизайн**: media queries, подход mobile-first
- **CSS Variables**: пользовательские свойства для темизации
- **Анимации**: transitions, keyframes, transforms
- **Препроцессоры**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **Манипуляция DOM**: выбор, создание и изменение элементов
- **События**: click, submit, keyboard, custom events, делегирование событий
- **Возможности ES6+**: arrow functions, destructuring, spread/rest, modules, async/await
- **APIs**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: статическая типизация, interfaces, generics, decorators

### Современные frontend-фреймворки

#### React
- **Компоненты**: функциональные компоненты, class components
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **Управление состоянием**: Context API, Redux, Zustand, Recoil
- **Маршрутизация**: React Router (BrowserRouter, Routes, Route, Link)
- **Экосистема**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: эффективный рендеринг через алгоритм diffing

#### Vue.js
- **Options API**: data, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Директивы**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: управление состоянием
- **Vue Router**: маршрутизация на стороне клиента
- **Nuxt.js**: фреймворк для server-side rendering

#### Angular
- **Компоненты**: decorators, templates, lifecycle hooks
- **Services**: dependency injection, singleton pattern
- **RxJS**: реактивное программирование, observables
- **Маршрутизация**: RouterModule, guards, resolvers
- **Формы**: template-driven, reactive forms
- **NgRx**: управление состоянием в стиле Redux

### Инструменты сборки и bundlers
- **Webpack**: сборка модулей, code splitting, loaders, plugins
- **Vite**: быстрый инструмент сборки на базе нативных ES modules
- **Parcel**: bundler без конфигурации
- **Rollup**: оптимизирован для библиотек
- **esbuild**: чрезвычайно быстрый bundler JavaScript
- **Babel**: transpiler JavaScript для обратной совместимости
- **PostCSS**: обработка CSS с помощью плагинов

### CSS-фреймворки и библиотеки
- **Bootstrap**: библиотека компонентов, grid system, utilities
- **Tailwind CSS**: utility-first CSS-фреймворк
- **Material UI**: реализация Material Design от Google
- **Chakra UI**: доступная библиотека компонентов
- **Ant Design**: UI-компоненты корпоративного уровня
- **Styled Components**: библиотека CSS-in-JS
- **Emotion**: CSS-in-JS с source maps

## Backend-разработка

### Серверные языки

#### Node.js
- **Среда выполнения**: JavaScript на сервере (движок V8)
- **Express.js**: минималистичный web-фреймворк, архитектура middleware
- **NestJS**: архитектура в стиле Angular, TypeScript
- **Fastify**: высокопроизводительный фреймворк
- **Koa**: современный Express от тех же создателей
- **Управление пакетами**: npm, yarn, pnpm

#### Python
- **Django**: полнофункциональный фреймворк, ORM, admin panel, batteries-included
- **Flask**: микрофреймворк, экосистема расширений
- **FastAPI**: современный, async, автоматическая документация API
- **Pyramid**: гибкий и масштабируемый фреймворк

#### Другие backend-языки
- **Ruby on Rails**: convention over configuration, ActiveRecord ORM
- **Java Spring**: корпоративный фреймворк, dependency injection
- **PHP Laravel**: элегантный синтаксис, Eloquent ORM, шаблоны Blade
- **Go Gin**: высокая производительность, минималистичный фреймворк
- **Rust Actix**: безопасность памяти, производительность
- **C# ASP.NET Core**: кроссплатформенность, корпоративные возможности

### Интеграция с базами данных

#### ORMs (Object-Relational Mapping)
- **Sequelize**: ORM для SQL-баз в Node.js
- **Prisma**: типобезопасный доступ к базе данных, автоматически сгенерированный клиент
- **SQLAlchemy**: SQL toolkit и ORM для Python
- **ActiveRecord**: ORM Ruby on Rails
- **Hibernate**: ORM для Java
- **Entity Framework**: ORM для .NET

#### Драйверы баз данных
- **pg**: клиент PostgreSQL для Node.js
- **mysql2**: клиент MySQL с поддержкой promises
- **pymongo**: драйвер MongoDB для Python
- **redis**: клиент Redis для нескольких языков

### Разработка API

#### REST APIs
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: 200, 201, 400, 401, 403, 404, 500
- **Именование ресурсов**: существительные, множественное число, иерархия
- **Versioning**: путь URL, заголовки, query parameters
- **Authentication**: JWT, OAuth, API keys
- **Documentation**: OpenAPI/Swagger, Postman

#### GraphQL
- **Schema Definition**: types, queries, mutations, subscriptions
- **Resolvers**: получение данных на уровне полей
- **Apollo Server**: реализация GraphQL-сервера
- **Relay**: GraphQL-клиент от Facebook
- **Преимущества**: нет over-fetching, единая точка входа, строгая типизация

#### gRPC
- **Protocol Buffers**: язык описания интерфейсов
- **HTTP/2**: двунаправленный стриминг
- **Сценарии использования**: взаимодействие микросервисов, приложения реального времени

### Аутентификация и авторизация
- **На основе сессий**: cookies, серверные сессии
- **На основе токенов**: JWT (JSON Web Tokens), без сохранения состояния
- **OAuth 2.0**: фреймворк авторизации, вход через сторонние сервисы
- **OpenID Connect**: слой идентификации поверх OAuth 2.0
- **SAML**: единый вход для корпоративной среды
- **Хеширование паролей**: bcrypt, argon2, scrypt
- **Многофакторная аутентификация**: TOTP, SMS, коды по email

## DevOps и развертывание

### Контроль версий
- **Git**: распределенный контроль версий
- **GitHub/GitLab/Bitbucket**: хостинг репозиториев
- **Стратегии ветвления**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: автоматизированные конвейеры тестирования и развертывания

### Контейнеризация
- **Docker**: runtime контейнеров, Dockerfile, images
- **Docker Compose**: оркестрация нескольких контейнеров
- **Container Registries**: Docker Hub, AWS ECR, Google GCR
- **Лучшие практики**: multi-stage builds, минимальные базовые образы

### Оркестрация
- **Kubernetes**: оркестрация контейнеров, pods, services, deployments
- **Helm**: менеджер пакетов для Kubernetes
- **Service Mesh**: Istio, Linkerd для сетевого взаимодействия микросервисов

### Облачные платформы
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: развертывание frontend, serverless functions
- **Netlify**: хостинг статических сайтов, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: упрощенная облачная инфраструктура

### CI/CD-конвейеры
- **GitHub Actions**: автоматизация workflow
- **GitLab CI**: встроенная непрерывная интеграция
- **Jenkins**: расширяемый сервер автоматизации
- **CircleCI**: облачный CI/CD
- **Travis CI**: сервис непрерывной интеграции
- **ArgoCD**: GitOps continuous delivery для Kubernetes

### Мониторинг и логирование
- **Производительность приложений**: New Relic, Datadog, AppDynamics
- **Отслеживание ошибок**: Sentry, Rollbar, Bugsnag
- **Логирование**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Мониторинг доступности**: Pingdom, UptimeRobot
- **Аналитика**: Google Analytics, Mixpanel, Amplitude

## Производительность web-приложений

### Методы оптимизации
- **Code Splitting**: lazy loading, dynamic imports
- **Tree Shaking**: удаление неиспользуемого кода
- **Minification**: уменьшение размера файлов
- **Compression**: Gzip, Brotli
- **Caching**: кэш браузера, CDN, service workers
- **Оптимизация изображений**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: встраивание стилей для верхней части страницы
- **Оптимизация базы данных**: индексирование, оптимизация запросов, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: производительность загрузки (<2.5s)
- **FID (First Input Delay)**: интерактивность (<100ms)
- **CLS (Cumulative Layout Shift)**: визуальная стабильность (<0.1)
- **INP (Interaction to Next Paint)**: метрика отзывчивости

### Content Delivery Networks (CDNs)
- **Cloudflare**: безопасность, производительность, DNS
- **Akamai**: CDN корпоративного уровня
- **Amazon CloudFront**: CDN от AWS
- **Fastly**: edge cloud-платформа
- **StackPath**: edge-сервисы

## Безопасность web-приложений

### Распространенные уязвимости (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: угон сессий, credential stuffing
- **Sensitive Data Exposure**: незашифрованные данные, слабая криптография
- **XML External Entities (XXE)**: уязвимости XML-парсеров
- **Broken Access Control**: повышение привилегий, несанкционированный доступ
- **Security Misconfiguration**: учетные данные по умолчанию, чрезмерно подробные ошибки
- **Cross-Site Scripting (XSS)**: reflected, stored, DOM-based
- **Insecure Deserialization**: атаки object injection
- **Using Components with Known Vulnerabilities**: устаревшие зависимости
- **Insufficient Logging & Monitoring**: незамеченные компрометации

### Лучшие практики безопасности
- **HTTPS**: шифрование TLS/SSL, HSTS
- **Content Security Policy (CSP)**: защита от XSS-атак
- **Input Validation**: очистка и проверка пользовательского ввода
- **Output Encoding**: предотвращение атак внедрения
- **CSRF Protection**: anti-CSRF tokens, cookies SameSite
- **Rate Limiting**: защита от brute force-атак
- **Security Headers**: X-Frame-Options, X-Content-Type-Options
- **Dependency Scanning**: npm audit, Snyk, Dependabot

## Тестирование

### Типы тестирования
- **Unit Testing**: отдельные компоненты/функции
- **Integration Testing**: взаимодействие компонентов
- **End-to-End (E2E)**: полные пользовательские сценарии
- **Visual Regression**: обнаружение изменений UI
- **Performance Testing**: load, stress, spike testing
- **Accessibility Testing**: соответствие WCAG

### Фреймворки тестирования
- **Jest**: фреймворк тестирования JavaScript
- **Mocha**: гибкий test runner
- **pytest**: фреймворк тестирования Python
- **RSpec**: фреймворк тестирования Ruby
- **JUnit**: фреймворк тестирования Java

### Инструменты E2E-тестирования
- **Selenium**: автоматизация браузера
- **Cypress**: современное E2E-тестирование
- **Playwright**: кроссбраузерная автоматизация
- **Puppeteer**: управление Headless Chrome

## Доступность (a11y)

### Рекомендации WCAG
- **Perceivable**: текстовые альтернативы, субтитры, адаптируемый контент
- **Operable**: навигация с клавиатуры, достаточное время, отсутствие провоцирования приступов
- **Understandable**: читаемость, предсказуемость, помощь при вводе
- **Robust**: совместимость со вспомогательными технологиями

### Реализация
- **Семантический HTML**: правильная иерархия заголовков, landmarks
- **ARIA Attributes**: роли, состояния, свойства
- **Focus Management**: видимые индикаторы фокуса, логичный порядок tab
- **Color Contrast**: минимальное соотношение 4.5:1 для текста
- **Screen Reader Testing**: NVDA, JAWS, VoiceOver
- **Keyboard Navigation**: все интерактивные элементы доступны с клавиатуры

## Progressive Web Apps (PWAs)

### Возможности PWA
- **Service Workers**: офлайн-работа, фоновая синхронизация
- **Web App Manifest**: предложение установки, иконки, цвета темы
- **App Shell**: закэшированный каркас интерфейса
- **Push Notifications**: вовлечение пользователей
- **Responsive Design**: работа на всех устройствах
- **HTTPS Required**: защищенный контекст

### Инструменты
- **Workbox**: библиотеки для service worker
- **Lighthouse**: аудит PWA
- **PWA Builder**: генерация manifest и иконок

## Новые технологии

### WebAssembly (Wasm)
- **Назначение**: запуск скомпилированного кода в браузере почти на нативной скорости
- **Языки**: цели компиляции для C++, Rust, Go
- **Сценарии использования**: игры, видеомонтаж, криптография, ML inference

### Serverless-архитектура
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Преимущества**: не нужно управлять серверами, auto-scaling, оплата по использованию
- **Что учитывать**: cold starts, vendor lock-in, сложность отладки

### Jamstack-архитектура
- **JavaScript**: интерактивность на стороне клиента
- **APIs**: serverless functions, сторонние сервисы
- **Markup**: заранее собранные статические файлы
- **Инструменты**: Next.js, Gatsby, Hugo, Eleventy
- **Преимущества**: производительность, безопасность, масштабируемость, удобство для разработчиков

### Связь в реальном времени
- **WebSockets**: двунаправленная коммуникация
- **Server-Sent Events**: стриминг от сервера к клиенту
- **WebRTC**: peer-to-peer для видео, аудио и данных
- **Сценарии использования**: чат, совместная работа, live streaming, игры

### Микрофронтенды
- **Концепция**: перенос идей микросервисов на frontend
- **Подходы**: build-time, run-time, edge-side integration
- **Преимущества**: независимые развертывания, автономность команд
- **Сложности**: согласованность, производительность, сложность системы
