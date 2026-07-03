# Веб-разработка

## Фронтенд-разработка

### Основные технологии

#### HTML (HyperText Markup Language)
- **Семантический HTML**: Использование осмысленных тегов (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Формы**: Типы полей ввода, валидация, метки доступности
- **Медиа**: Встраивание изображений, видео и аудио
- **Мета-теги**: SEO, viewport, кодировка символов
- **Возможности HTML5**: Canvas, SVG, local storage, geolocation, web sockets

#### CSS (Cascading Style Sheets)
- **Блочная модель**: Content, padding, border, margin
- **Системы раскладки**:
  - **Flexbox**: Одномерные макеты, justify-content, align-items
  - **Grid**: Двумерные макеты, grid-template, grid-area
  - **Позиционирование**: Static, relative, absolute, fixed, sticky
- **Адаптивный дизайн**: Media queries, подход mobile-first
- **Переменные CSS**: Custom properties для темизации
- **Анимации**: Transitions, keyframes, transforms
- **Препроцессоры**: Sass, Less (variables, mixins, nesting)

#### JavaScript
- **Манипуляция DOM**: Выбор, создание и изменение элементов
- **События**: Click, submit, keyboard, custom events, event delegation
- **Возможности ES6+**: Arrow functions, destructuring, spread/rest, modules, async/await
- **API**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Статическая типизация, interfaces, generics, decorators

### Современные frontend-фреймворки

#### React
- **Компоненты**: Функциональные компоненты, классовые компоненты
- **Hooks**: useState, useEffect, useContext, useReducer, custom hooks
- **Управление состоянием**: Context API, Redux, Zustand, Recoil
- **Маршрутизация**: React Router (BrowserRouter, Routes, Route, Link)
- **Экосистема**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Эффективный рендеринг за счёт алгоритма diffing

#### Vue.js
- **Options API**: data, methods, computed, watch
- **Composition API**: setup(), ref, reactive, computed
- **Директивы**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Управление состоянием
- **Vue Router**: Клиентская маршрутизация
- **Nuxt.js**: Фреймворк для server-side rendering

#### Angular
- **Компоненты**: Decorators, templates, lifecycle hooks
- **Сервисы**: Dependency injection, паттерн singleton
- **RxJS**: Реактивное программирование, observables
- **Маршрутизация**: RouterModule, guards, resolvers
- **Формы**: Template-driven, reactive forms
- **NgRx**: Управление состоянием в стиле Redux

### Инструменты сборки и bundlers
- **Webpack**: Сборка модулей, code splitting, loaders, plugins
- **Vite**: Быстрый инструмент сборки на основе native ES modules
- **Parcel**: Bundler с нулевой конфигурацией
- **Rollup**: Оптимизирован для библиотек
- **esbuild**: Очень быстрый JavaScript bundler
- **Babel**: JavaScript-транспайлер для обратной совместимости
- **PostCSS**: Обработка CSS с plugins

### CSS-фреймворки и библиотеки
- **Bootstrap**: Библиотека компонентов, grid system, utilities
- **Tailwind CSS**: CSS-фреймворк в стиле utility-first
- **Material UI**: Реализация Material Design от Google
- **Chakra UI**: Библиотека доступных компонентов
- **Ant Design**: UI-компоненты уровня enterprise
- **Styled Components**: Библиотека CSS-in-JS
- **Emotion**: CSS-in-JS с source maps

## Бэкенд-разработка

### Server-side языки

#### Node.js
- **Runtime**: JavaScript на сервере (движок V8)
- **Express.js**: Минималистичный web-фреймворк, архитектура middleware
- **NestJS**: Архитектура в духе Angular, TypeScript
- **Fastify**: Высокопроизводительный фреймворк
- **Koa**: Современный Express от тех же создателей
- **Управление пакетами**: npm, yarn, pnpm

#### Python
- **Django**: Полнофункциональный фреймворк, ORM, admin panel, подход batteries-included
- **Flask**: Микрофреймворк, экосистема расширений
- **FastAPI**: Современный async-фреймворк с автоматической документацией API
- **Pyramid**: Гибкий, масштабируемый фреймворк

#### Другие backend-языки
- **Ruby on Rails**: Convention over configuration, ActiveRecord ORM
- **Java Spring**: Enterprise-фреймворк, dependency injection
- **PHP Laravel**: Элегантный синтаксис, Eloquent ORM, Blade templating
- **Go Gin**: Высокая производительность, минималистичный фреймворк
- **Rust Actix**: Безопасность памяти, производительность
- **C# ASP.NET Core**: Cross-platform, enterprise-возможности

### Интеграция с базами данных

#### ORMs (Object-Relational Mapping)
- **Sequelize**: Node.js ORM для SQL-баз данных
- **Prisma**: Type-safe доступ к базе данных, auto-generated client
- **SQLAlchemy**: Python SQL toolkit и ORM
- **ActiveRecord**: ORM в Ruby on Rails
- **Hibernate**: Java ORM
- **Entity Framework**: .NET ORM

#### Драйверы баз данных
- **pg**: PostgreSQL-клиент для Node.js
- **mysql2**: MySQL-клиент с promises
- **pymongo**: MongoDB-драйвер для Python
- **redis**: Redis-клиент для нескольких языков

### Разработка API

#### REST APIs
- **HTTP-методы**: GET, POST, PUT, PATCH, DELETE
- **Коды состояния**: 200, 201, 400, 401, 403, 404, 500
- **Именование ресурсов**: Существительные, множественное число, иерархическая структура
- **Версионирование**: URL path, headers, query parameters
- **Аутентификация**: JWT, OAuth, API keys
- **Документация**: OpenAPI/Swagger, Postman

#### GraphQL
- **Определение схемы**: Types, queries, mutations, subscriptions
- **Resolvers**: Получение данных на уровне полей
- **Apollo Server**: Реализация GraphQL-сервера
- **Relay**: GraphQL-клиент от Facebook
- **Преимущества**: Нет over-fetching, единая endpoint, строгая типизация

#### gRPC
- **Protocol Buffers**: Язык описания интерфейсов
- **HTTP/2**: Двунаправленный streaming
- **Сценарии использования**: Взаимодействие микросервисов, приложения реального времени

### Аутентификация и авторизация
- **На основе сессий**: Cookies, server-side sessions
- **На основе токенов**: JWT (JSON Web Tokens), stateless
- **OAuth 2.0**: Фреймворк авторизации, сторонний вход
- **OpenID Connect**: Уровень идентификации поверх OAuth 2.0
- **SAML**: Enterprise single sign-on
- **Хеширование паролей**: bcrypt, argon2, scrypt
- **Многофакторная аутентификация**: TOTP, SMS, коды по email

## DevOps и развёртывание

### Контроль версий
- **Git**: Распределённая система контроля версий
- **GitHub/GitLab/Bitbucket**: Хостинг репозиториев
- **Стратегии ветвления**: Git Flow, GitHub Flow, trunk-based development
- **CI/CD**: Автоматизированные конвейеры тестирования и развёртывания

### Контейнеризация
- **Docker**: Container runtime, Dockerfile, images
- **Docker Compose**: Оркестрация нескольких контейнеров
- **Реестры контейнеров**: Docker Hub, AWS ECR, Google GCR
- **Лучшие практики**: Multi-stage builds, минимальные base images

### Оркестрация
- **Kubernetes**: Оркестрация контейнеров, pods, services, deployments
- **Helm**: Менеджер пакетов для Kubernetes
- **Service Mesh**: Istio, Linkerd для сетевого взаимодействия микросервисов

### Облачные платформы
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: Virtual Machines, Blob Storage, Functions, AKS
- **Vercel**: Развёртывание frontend-приложений, serverless functions
- **Netlify**: Хостинг статических сайтов, serverless functions
- **Heroku**: Platform as a Service (PaaS)
- **DigitalOcean**: Упрощённая облачная инфраструктура

### CI/CD-конвейеры
- **GitHub Actions**: Автоматизация workflows
- **GitLab CI**: Встроенная continuous integration
- **Jenkins**: Расширяемый сервер автоматизации
- **CircleCI**: Облачный CI/CD
- **Travis CI**: Сервис continuous integration
- **ArgoCD**: GitOps continuous delivery для Kubernetes

### Мониторинг и логирование
- **Производительность приложений**: New Relic, Datadog, AppDynamics
- **Отслеживание ошибок**: Sentry, Rollbar, Bugsnag
- **Логирование**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Мониторинг доступности**: Pingdom, UptimeRobot
- **Аналитика**: Google Analytics, Mixpanel, Amplitude

## Производительность веб-приложений

### Техники оптимизации
- **Code Splitting**: Lazy loading, dynamic imports
- **Tree Shaking**: Удаление неиспользуемого кода
- **Минификация**: Уменьшение размера файлов
- **Сжатие**: Gzip, Brotli
- **Кэширование**: Browser cache, CDN, service workers
- **Оптимизация изображений**: WebP, AVIF, lazy loading, responsive images
- **Critical CSS**: Встраивание стилей для области above the fold
- **Оптимизация базы данных**: Indexing, query optimization, connection pooling

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Производительность загрузки (<2.5s)
- **FID (First Input Delay)**: Интерактивность (<100ms)
- **CLS (Cumulative Layout Shift)**: Визуальная стабильность (<0.1)
- **INP (Interaction to Next Paint)**: Метрика отзывчивости

### Content Delivery Networks (CDNs)
- **Cloudflare**: Безопасность, производительность, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: CDN от AWS
- **Fastly**: Edge cloud platform
- **StackPath**: Edge-сервисы

## Веб-безопасность

### Распространённые уязвимости (OWASP Top 10)
- **Injection**: SQL injection, command injection
- **Broken Authentication**: Захват сессии, credential stuffing
- **Sensitive Data Exposure**: Незашифрованные данные, слабая криптография
- **XML External Entities (XXE)**: Уязвимости XML-парсеров
- **Broken Access Control**: Эскалация привилегий, несанкционированный доступ
- **Security Misconfiguration**: Учётные данные по умолчанию, слишком подробные ошибки
- **Cross-Site Scripting (XSS)**: Reflected, stored, DOM-based
- **Insecure Deserialization**: Атаки через внедрение объектов
- **Using Components with Known Vulnerabilities**: Устаревшие зависимости
- **Insufficient Logging & Monitoring**: Незамеченные нарушения безопасности

### Лучшие практики безопасности
- **HTTPS**: TLS/SSL-шифрование, HSTS
- **Content Security Policy (CSP)**: Защита от XSS-атак
- **Валидация ввода**: Очистка пользовательского ввода
- **Output Encoding**: Защита от атак внедрения
- **CSRF Protection**: Anti-CSRF tokens, SameSite cookies
- **Rate Limiting**: Защита от brute force-атак
- **Security Headers**: X-Frame-Options, X-Content-Type-Options
- **Сканирование зависимостей**: npm audit, Snyk, Dependabot

## Тестирование

### Виды тестирования
- **Unit Testing**: Отдельные компоненты/функции
- **Integration Testing**: Взаимодействие компонентов
- **End-to-End (E2E)**: Полные пользовательские сценарии
- **Visual Regression**: Обнаружение изменений в UI
- **Performance Testing**: Load, stress, spike testing
- **Accessibility Testing**: Соответствие WCAG

### Фреймворки для тестирования
- **Jest**: JavaScript testing framework
- **Mocha**: Гибкий test runner
- **pytest**: Python testing framework
- **RSpec**: Ruby testing framework
- **JUnit**: Java testing framework

### Инструменты E2E-тестирования
- **Selenium**: Автоматизация браузера
- **Cypress**: Современное E2E-тестирование
- **Playwright**: Кросс-браузерная автоматизация
- **Puppeteer**: Управление Headless Chrome

## Доступность (a11y)

### Рекомендации WCAG
- **Воспринимаемость**: Текстовые альтернативы, субтитры, адаптируемый контент
- **Управляемость**: Навигация с клавиатуры, достаточное время, отсутствие провоцирующих приступы элементов
- **Понятность**: Читаемость, предсказуемость, помощь при вводе
- **Надёжность**: Совместимость со вспомогательными технологиями

### Реализация
- **Семантический HTML**: Корректная иерархия заголовков, landmarks
- **ARIA Attributes**: Roles, states, properties
- **Управление фокусом**: Видимые индикаторы фокуса, логичный порядок табуляции
- **Контрастность цветов**: Минимальное соотношение 4.5:1 для текста
- **Тестирование со screen reader**: NVDA, JAWS, VoiceOver
- **Навигация с клавиатуры**: Доступность всех интерактивных элементов

## Progressive Web Apps (PWAs)

### Возможности PWA
- **Service Workers**: Офлайн-функциональность, фоновая синхронизация
- **Web App Manifest**: Приглашение к установке, иконки, цвета темы
- **App Shell**: Кэшируемый каркас UI
- **Push Notifications**: Вовлечение пользователей
- **Адаптивный дизайн**: Работает на всех устройствах
- **HTTPS Required**: Безопасный контекст

### Инструменты
- **Workbox**: Библиотеки для service worker
- **Lighthouse**: Аудит PWA
- **PWA Builder**: Генерация manifests и icons

## Новые технологии

### WebAssembly (Wasm)
- **Назначение**: Запуск скомпилированного кода в браузере почти с нативной скоростью
- **Языки**: Цели компиляции для C++, Rust, Go
- **Сценарии использования**: Игры, видеомонтаж, криптография, ML inference

### Serverless Architecture
- **Functions as a Service**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Преимущества**: Не нужно управлять серверами, auto-scaling, pay-per-use
- **Особенности**: Cold starts, vendor lock-in, сложность отладки

### Jamstack Architecture
- **JavaScript**: Интерактивность на стороне клиента
- **APIs**: Serverless functions, сторонние сервисы
- **Markup**: Предварительно собранные статические файлы
- **Инструменты**: Next.js, Gatsby, Hugo, Eleventy
- **Преимущества**: Производительность, безопасность, масштабируемость, удобство для разработчиков

### Real-Time Communication
- **WebSockets**: Двунаправленная связь
- **Server-Sent Events**: Потоковая передача от сервера к клиенту
- **WebRTC**: Peer-to-peer видео, аудио, данные
- **Сценарии использования**: Чат, совместная работа, live streaming, gaming

### Micro Frontends
- **Концепция**: Расширение идеи микросервисов на frontend
- **Подходы**: Build-time, run-time, edge-side integration
- **Преимущества**: Независимые развёртывания, автономность команд
- **Сложности**: Согласованность, производительность, сложность
