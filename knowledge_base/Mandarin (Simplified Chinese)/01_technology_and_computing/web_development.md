# Web 开发

## 前端开发

### 核心技术

#### HTML（超文本标记语言）
- **语义化 HTML**：使用具有明确含义的标签（`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`）
- **表单**：输入类型、校验、无障碍标签
- **媒体**：图片、视频、音频嵌入
- **Meta 标签**：SEO、viewport、字符编码
- **HTML5 特性**：Canvas、SVG、本地存储、地理定位、WebSocket

#### CSS（层叠样式表）
- **盒模型**：内容、内边距、边框、外边距
- **布局系统**：
  - **Flexbox**：一维布局、justify-content、align-items
  - **Grid**：二维布局、grid-template、grid-area
  - **定位**：static、relative、absolute、fixed、sticky
- **响应式设计**：媒体查询、移动优先方法
- **CSS 变量**：用于主题定制的自定义属性
- **动画**：过渡、关键帧、变换
- **预处理器**：Sass、Less（变量、混入、嵌套）

#### JavaScript
- **DOM 操作**：选择、创建、修改元素
- **事件**：点击、提交、键盘、自定义事件、事件委托
- **ES6+ 特性**：箭头函数、解构、展开/剩余、模块、async/await
- **API**：Fetch、XMLHttpRequest、localStorage、sessionStorage
- **TypeScript**：静态类型、接口、泛型、装饰器

### 现代前端框架

#### React
- **组件**：函数组件、类组件
- **Hooks**：useState、useEffect、useContext、useReducer、自定义 Hook
- **状态管理**：Context API、Redux、Zustand、Recoil
- **路由**：React Router（BrowserRouter、Routes、Route、Link）
- **生态系统**：Next.js（SSR、SSG）、Remix、Gatsby
- **虚拟 DOM**：通过 diff 算法实现高效渲染

#### Vue.js
- **Options API**：data、methods、computed、watch
- **Composition API**：setup()、ref、reactive、computed
- **指令**：v-if、v-for、v-bind、v-on、v-model
- **Vuex/Pinia**：状态管理
- **Vue Router**：客户端路由
- **Nuxt.js**：服务端渲染框架

#### Angular
- **组件**：装饰器、模板、生命周期钩子
- **服务**：依赖注入、单例模式
- **RxJS**：响应式编程、可观察对象
- **路由**：RouterModule、守卫、解析器
- **表单**：模板驱动表单、响应式表单
- **NgRx**：Redux 风格的状态管理

### 构建工具与打包器
- **Webpack**：模块打包、代码分割、loader、插件
- **Vite**：基于原生 ES 模块的高速构建工具
- **Parcel**：零配置打包器
- **Rollup**：针对库构建优化
- **esbuild**：极快的 JavaScript 打包器
- **Babel**：用于向后兼容的 JavaScript 转译器
- **PostCSS**：基于插件的 CSS 处理工具

### CSS 框架与库
- **Bootstrap**：组件库、栅格系统、工具类
- **Tailwind CSS**：实用优先的 CSS 框架
- **Material UI**：Google Material Design 的实现
- **Chakra UI**：无障碍组件库
- **Ant Design**：企业级 UI 组件
- **Styled Components**：CSS-in-JS 库
- **Emotion**：支持 source map 的 CSS-in-JS

## 后端开发

### 服务端语言

#### Node.js
- **运行时**：服务端 JavaScript（V8 引擎）
- **Express.js**：极简 Web 框架、中间件架构
- **NestJS**：受 Angular 启发的架构、TypeScript
- **Fastify**：高性能框架
- **Koa**：由同一批作者打造的现代版 Express
- **包管理**：npm、yarn、pnpm

#### Python
- **Django**：功能完整的框架、ORM、管理后台、开箱即用
- **Flask**：微框架、扩展生态
- **FastAPI**：现代化、异步、自动生成 API 文档
- **Pyramid**：灵活、可扩展的框架

#### 其他后端语言
- **Ruby on Rails**：约定优于配置、ActiveRecord ORM
- **Java Spring**：企业级框架、依赖注入
- **PHP Laravel**：优雅语法、Eloquent ORM、Blade 模板
- **Go Gin**：高性能、极简框架
- **Rust Actix**：内存安全、性能出色
- **C# ASP.NET Core**：跨平台、具备企业级特性

### 数据库集成

#### ORM（对象关系映射）
- **Sequelize**：Node.js 的 SQL 数据库 ORM
- **Prisma**：类型安全的数据库访问、自动生成客户端
- **SQLAlchemy**：Python SQL 工具包与 ORM
- **ActiveRecord**：Ruby on Rails ORM
- **Hibernate**：Java ORM
- **Entity Framework**：.NET ORM

#### 数据库驱动
- **pg**：Node.js 的 PostgreSQL 客户端
- **mysql2**：支持 Promise 的 MySQL 客户端
- **pymongo**：Python 的 MongoDB 驱动
- **redis**：适用于多种语言的 Redis 客户端

### API 开发

#### REST API
- **HTTP 方法**：GET、POST、PUT、PATCH、DELETE
- **状态码**：200、201、400、401、403、404、500
- **资源命名**：使用名词、复数、层级结构
- **版本控制**：URL 路径、请求头、查询参数
- **身份验证**：JWT、OAuth、API 密钥
- **文档**：OpenAPI/Swagger、Postman

#### GraphQL
- **Schema 定义**：类型、查询、变更、订阅
- **解析器**：字段级数据获取
- **Apollo Server**：GraphQL 服务端实现
- **Relay**：Facebook 的 GraphQL 客户端
- **优势**：避免过度获取、单一端点、强类型

#### gRPC
- **Protocol Buffers**：接口定义语言
- **HTTP/2**：双向流
- **使用场景**：微服务通信、实时应用

### 身份验证与授权
- **基于会话**：Cookie、服务端会话
- **基于令牌**：JWT（JSON Web Token）、无状态
- **OAuth 2.0**：授权框架、第三方登录
- **OpenID Connect**：构建在 OAuth 2.0 之上的身份层
- **SAML**：企业级单点登录
- **密码哈希**：bcrypt、argon2、scrypt
- **多因素认证**：TOTP、短信、电子邮件验证码

## DevOps 与部署

### 版本控制
- **Git**：分布式版本控制
- **GitHub/GitLab/Bitbucket**：代码仓库托管
- **分支策略**：Git Flow、GitHub Flow、主干开发
- **CI/CD**：自动化测试与部署流水线

### 容器化
- **Docker**：容器运行时、Dockerfile、镜像
- **Docker Compose**：多容器编排
- **容器镜像仓库**：Docker Hub、AWS ECR、Google GCR
- **最佳实践**：多阶段构建、精简基础镜像

### 编排
- **Kubernetes**：容器编排、Pod、Service、Deployment
- **Helm**：Kubernetes 包管理器
- **Service Mesh**：用于微服务网络的 Istio、Linkerd

### 云平台
- **AWS**：EC2、S3、Lambda、RDS、CloudFront、ECS/EKS
- **Google Cloud**：Compute Engine、Cloud Storage、Cloud Functions、GKE
- **Azure**：Virtual Machines、Blob Storage、Functions、AKS
- **Vercel**：前端部署、无服务器函数
- **Netlify**：静态站点托管、无服务器函数
- **Heroku**：平台即服务（PaaS）
- **DigitalOcean**：简化的云基础设施

### CI/CD 流水线
- **GitHub Actions**：工作流自动化
- **GitLab CI**：内建持续集成
- **Jenkins**：可扩展的自动化服务器
- **CircleCI**：基于云的 CI/CD
- **Travis CI**：持续集成服务
- **ArgoCD**：面向 Kubernetes 的 GitOps 持续交付

### 监控与日志
- **应用性能**：New Relic、Datadog、AppDynamics
- **错误追踪**：Sentry、Rollbar、Bugsnag
- **日志**：ELK Stack（Elasticsearch、Logstash、Kibana）、Splunk
- **可用性监控**：Pingdom、UptimeRobot
- **分析**：Google Analytics、Mixpanel、Amplitude

## Web 性能

### 优化技术
- **代码分割**：懒加载、动态导入
- **Tree Shaking**：移除未使用代码
- **压缩与最小化**：减小文件体积
- **压缩传输**：Gzip、Brotli
- **缓存**：浏览器缓存、CDN、Service Worker
- **图像优化**：WebP、AVIF、懒加载、响应式图片
- **关键 CSS**：内联首屏样式
- **数据库优化**：索引、查询优化、连接池

### Core Web Vitals
- **LCP（Largest Contentful Paint）**：加载性能（<2.5s）
- **FID（First Input Delay）**：交互性（<100ms）
- **CLS（Cumulative Layout Shift）**：视觉稳定性（<0.1）
- **INP（Interaction to Next Paint）**：响应性指标

### 内容分发网络（CDN）
- **Cloudflare**：安全、性能、DNS
- **Akamai**：企业级 CDN
- **Amazon CloudFront**：AWS CDN
- **Fastly**：边缘云平台
- **StackPath**：边缘服务

## Web 安全

### 常见漏洞（OWASP Top 10）
- **注入**：SQL 注入、命令注入
- **失效的身份验证**：会话劫持、撞库攻击
- **敏感数据泄露**：未加密数据、弱加密
- **XML 外部实体（XXE）**：XML 解析器漏洞
- **失效的访问控制**：权限提升、未授权访问
- **安全配置错误**：默认凭据、冗长错误信息
- **跨站脚本（XSS）**：反射型、存储型、基于 DOM
- **不安全的反序列化**：对象注入攻击
- **使用含已知漏洞的组件**：过时依赖
- **日志记录与监控不足**：未被发现的入侵

### 安全最佳实践
- **HTTPS**：TLS/SSL 加密、HSTS
- **内容安全策略（CSP）**：防止 XSS 攻击
- **输入验证**：清理用户输入
- **输出编码**：防止注入攻击
- **CSRF 防护**：Anti-CSRF 令牌、SameSite Cookie
- **限流**：防止暴力破解攻击
- **安全头**：X-Frame-Options、X-Content-Type-Options
- **依赖扫描**：npm audit、Snyk、Dependabot

## 测试

### 测试类型
- **单元测试**：单个组件/函数
- **集成测试**：组件交互
- **端到端（E2E）测试**：完整用户流程
- **视觉回归测试**：UI 变化检测
- **性能测试**：负载测试、压力测试、峰值测试
- **无障碍测试**：WCAG 合规性

### 测试框架
- **Jest**：JavaScript 测试框架
- **Mocha**：灵活的测试运行器
- **pytest**：Python 测试框架
- **RSpec**：Ruby 测试框架
- **JUnit**：Java 测试框架

### E2E 测试工具
- **Selenium**：浏览器自动化
- **Cypress**：现代 E2E 测试
- **Playwright**：跨浏览器自动化
- **Puppeteer**：无头 Chrome 控制工具

## 无障碍（a11y）

### WCAG 指南
- **可感知**：文本替代、字幕、可适配内容
- **可操作**：键盘导航、充足时间、避免诱发癫痫
- **可理解**：内容可读、行为可预测、输入辅助
- **稳健**：兼容辅助技术

### 实现方式
- **语义化 HTML**：合理的标题层级、页面地标
- **ARIA 属性**：角色、状态、属性
- **焦点管理**：可见的焦点指示器、合乎逻辑的 Tab 顺序
- **颜色对比度**：文本至少达到 4.5:1
- **屏幕阅读器测试**：NVDA、JAWS、VoiceOver
- **键盘导航**：所有可交互元素都可访问

## 渐进式 Web 应用（PWA）

### PWA 特性
- **Service Worker**：离线功能、后台同步
- **Web App Manifest**：安装提示、图标、主题色
- **App Shell**：已缓存的 UI 骨架
- **推送通知**：提升用户参与度
- **响应式设计**：适配所有设备
- **必须使用 HTTPS**：安全上下文

### 工具
- **Workbox**：Service Worker 库
- **Lighthouse**：PWA 审计工具
- **PWA Builder**：生成 manifest 和图标

## 新兴技术

### WebAssembly（Wasm）
- **用途**：在浏览器中以接近原生速度运行编译后的代码
- **语言**：C++、Rust、Go 编译目标
- **使用场景**：游戏、视频编辑、密码学、机器学习推理

### 无服务器架构
- **函数即服务**：AWS Lambda、Azure Functions、Google Cloud Functions
- **优势**：无需管理服务器、自动扩缩容、按使用付费
- **注意事项**：冷启动、供应商锁定、调试复杂度

### Jamstack 架构
- **JavaScript**：客户端交互
- **API**：无服务器函数、第三方服务
- **Markup**：预构建静态文件
- **工具**：Next.js、Gatsby、Hugo、Eleventy
- **优势**：性能、安全性、可扩展性、开发体验

### 实时通信
- **WebSocket**：双向通信
- **Server-Sent Events**：服务端到客户端的流式传输
- **WebRTC**：点对点视频、音频、数据
- **使用场景**：聊天、协作、直播、游戏

### 微前端
- **概念**：将微服务理念扩展到前端
- **实现方式**：构建时集成、运行时集成、边缘侧集成
- **优势**：独立部署、团队自治
- **挑战**：一致性、性能、复杂性
