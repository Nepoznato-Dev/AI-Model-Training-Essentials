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
# 网页开发
## 前端开发
### 核心技术
#### HTML（超文本标记语言）
- **语义 HTML**：使用有意义的标签（`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`）
- **表单**：输入类型、验证、辅助功能标签
- **媒体**：图像、视频、音频嵌入
- **元标签**：SEO、视口、字符编码
- **HTML5 功能**：Canvas、SVG、本地存储、地理定位、网络套接字
#### CSS（层叠样式表）
- **盒子模型**：内容、填充、边框、边距
- **布局系统**：
  - **Flexbox**：一维布局、对齐内容、对齐项目
  - **网格**：二维布局、网格模板、网格区域
  - **定位**：静态、相对、绝对、固定、粘性
- **响应式设计**：媒体查询、移动优先方法
- **CSS 变量**：主题的自定义属性
- **动画**：过渡、关键帧、变换
- **预处理器**：Sass、Less（变量、mixin、嵌套）
#### JavaScript
- **DOM操作**：选择、创建、修改元素
- **事件**：点击、提交、键盘、自定义事件、事件委托
- **ES6+ 功能**：箭头函数、解构、展开/休息、模块、异步/等待
- **API**：Fetch、XMLHttpRequest、localStorage、sessionStorage
- **TypeScript**：静态类型、接口、泛型、装饰器
### 现代前端框架
#### 反应
- **组件**：功能组件、类组件
- **钩子**：useState、useEffect、useContext、useReducer、自定义钩子
- **状态管理**：Context API、Redux、Zustand、Recoil
- **路由**：React Router（BrowserRouter、路由、路由、链接）
- **生态系统**：Next.js（SSR、SSG）、Remix、Gatsby
- **虚拟 DOM**：通过 diff 算法高效渲染
#### Vue.js
- **选项 API**：数据、方法、计算、监视
- **组合 API**：setup()、ref、reactive、compute
- **指令**：v-if、v-for、v-bind、v-on、v-model
- **Vuex/Pinia**：状态管理
- **Vue Router**：客户端路由
- **Nuxt.js**：服务器端渲染框架
#### 角度
- **组件**：装饰器、模板、生命周期挂钩
- **服务**：依赖注入，单例模式
- **RxJS**：反应式编程，可观察量
- **路由**：RouterModule、守卫、解析器
- **表单**：模板驱动的反应式表单
- **NgRx**：Redux 风格的状态管理
### 构建工具和捆绑器
- **Webpack**：模块捆绑、代码分割、加载器、插件
- **Vite**：使用原生 ES 模块的快速构建工具
- **Parcel**：零配置捆绑器
- **Rollup**：针对库进行了优化
- **esbuild**：极快的 JavaScript 捆绑器
- **Babel**：用于向后兼容的 JavaScript 转译器
- **PostCSS**：使用插件进行 CSS 处理
### CSS 框架和库
- **Bootstrap**：组件库、网格系统、实用程序
- **Tailwind CSS**：实用优先的 CSS 框架
- **Material UI**：Google 的 Material Design 实现
- **Chakra UI**：可访问的组件库
- **Ant Design**：企业级 UI 组件
- **样式组件**：CSS-in-JS 库
- **情感**：带有源映射的 CSS-in-JS
## 后端开发
### 服务器端语言
#### Node.js
- **运行时**：服务器上的 JavaScript（V8 引擎）
- **Express.js**：最小的Web框架，中间件架构
- **NestJS**：Angular 启发的架构，TypeScript
- **Fastify**：高性能框架
- **Koa**：同一创作者的《现代快车》
- **包管理**：npm、yarn、pnpm
####Python
- **Django**：全功能框架、ORM、管理面板、包含电池
- **Flask**：微框架，扩展生态系统
- **FastAPI**：现代、异步、自动 API 文档
- **金字塔**：灵活、可扩展的框架
#### 其他后端语言
- **Ruby on Rails**：约定优于配置，ActiveRecord ORM
- **Java Spring**：企业框架，依赖注入
- **PHP Laravel**：优雅的语法、雄辩的 ORM、Blade 模板
- **Go Gin**：高性能，最小框架
- **Rust Actix**：内存安全、性能
- **C# ASP.NET Core**：跨平台、企业功能
### 数据库集成
#### ORM（对象关系映射）
- **Sequelize**：用于 SQL 数据库的 Node.js ORM
- **Prisma**：类型安全的数据库访问，自动生成的客户端
- **SQLAlchemy**：Python SQL 工具包和 ORM
- **ActiveRecord**：Ruby on Rails ORM
- **Hibernate**：Java ORM
- **实体框架**：.NET ORM
#### 数据库驱动程序
- **pg**：Node.js 的 PostgreSQL 客户端
- **mysql2**：带有承诺的 MySQL 客户端
- **pymongo**：Python 的 MongoDB 驱动程序
- **redis**：多种语言的Redis客户端
### API开发
#### REST API
- **HTTP 方法**：GET、POST、PUT、PATCH、DELETE
- **状态代码**：200、201、400、401、403、404、500
- **资源命名**：名词，复数，分层
- **版本控制**：URL 路径、标头、查询参数
- **身份验证**：JWT、OAuth、API 密钥
- **文档**：OpenAPI/Swagger、Postman
#### GraphQL
- **模式定义**：类型、查询、突变、订阅
- **解析器**：字段级数据获取
- **Apollo 服务器**：GraphQL 服务器实现
- **Relay**：Facebook 的 GraphQL 客户端
- **优点**：无过度获取、单端点、强类型
#### gRPC
- **协议缓冲区**：接口定义语言
- **HTTP/2**：双向流式传输
- **用例**：微服务通信、实时应用程序
### 身份验证和授权
- **基于会话**：Cookie、服务器端会话
- **基于令牌**：JWT（JSON Web 令牌），无状态
- **OAuth 2.0**：授权框架，第三方登录
- **OpenID Connect**：OAuth 2.0 上的身份层
- **SAML**：企业单点登录
- **密码哈希**：bcrypt、argon2、scrypt
- **多重身份验证**：TOTP、短信、电子邮件代码
## DevOps 和部署
### 版本控制
- **Git**：分布式版本控制
- **GitHub/GitLab/Bitbucket**：存储库托管
- **分支策略**：Git Flow、GitHub Flow、基于主干的开发
- **CI/CD**：自动化测试和部署管道
### 容器化
- **Docker**：容器运行时、Dockerfile、图像
- **Docker Compose**：多容器编排
- **容器注册表**：Docker Hub、AWS ECR、Google GCR
- **最佳实践**：多阶段构建，最少的基础镜像
### 编排
- **Kubernetes**：容器编排、pod、服务、部署
- **Helm**：Kubernetes 包管理器
- **服务网格**：用于微服务网络的 Istio、Linkerd
### 云平台
- **AWS**：EC2、S3、Lambda、RDS、CloudFront、ECS/EKS
- **Google Cloud**：计算引擎、云存储、云功能、GKE
- **Azure**：虚拟机、Blob 存储、函数、AKS
- **Vercel**：前端部署、无服务器功能
- **Netlify**：静态站点托管，无服务器功能
- **Heroku**：平台即服务 (PaaS)
- **DigitalOcean**：简化的云基础设施
### CI/CD 管道
- **GitHub Actions**：工作流程自动化
- **GitLab CI**：内置持续集成
- **Jenkins**：可扩展的自动化服务器
- **CircleCI**：基于云的 CI/CD
- **Travis CI**：持续集成服务
- **ArgoCD**：Kubernetes 的 GitOps 持续交付
### 监控和日志记录
- **应用程序性能**：New Relic、Datadog、AppDynamics
- **错误跟踪**：Sentry、Rollbar、Bugsnag
- **日志记录**：ELK Stack（Elasticsearch、Logstash、Kibana）、Splunk
- **正常运行时间监控**：Pingdom、UptimeRobot
- **分析**：Google Analytics、Mixpanel、Amplitude
## 网络性能
### 优化技术
- **代码分割**：延迟加载、动态导入
- **Tree Shaking**：删除未使用的代码
- **缩小**：减小文件大小
- **压缩**：Gzip、Brotli
- **缓存**：浏览器缓存、CDN、服务工作者
- **图像优化**：WebP、AVIF、延迟加载、响应式图像
- **关键 CSS**：内联首屏样式
- **数据库优化**：索引、查询优化、连接池
### 核心网络生命力
- **LCP（最大内容涂料）**：加载性能（<2.5s）
- **FID（首次输入延迟）**：交互性（<100ms）
- **CLS（累积布局偏移）**：视觉稳定性（<0.1）
- **INP（与下一个绘画的交互）**：响应度指标
### 内容交付网络 (CDN)
- **Cloudflare**：安全性、性能、DNS
- **Akamai**：企业 CDN
- **Amazon CloudFront**：AWS CDN
- **Fastly**：边缘云平台
- **StackPath**：边缘服务
## 网络安全
### 常见漏洞（OWASP 前 10 名）
- **注入**：SQL注入、命令注入
- **损坏的身份验证**：会话劫持、凭证填充
- **敏感数据暴露**：未加密的数据，弱加密
- **XML 外部实体 (XXE)**：XML 解析器漏洞
- **访问控制失效**：权限升级、未经授权的访问
- **安全配置错误**：默认凭据、详细错误
- **跨站脚本 (XSS)**：反射、存储、基于 DOM
- **不安全的反序列化**：对象注入攻击
- **使用具有已知漏洞的组件**：过时的依赖项
- **日志记录和监控不足**：未检测到的违规行为
### 安全最佳实践
- **HTTPS**：TLS/SSL 加密、HSTS
- **内容安全策略（CSP）**：防止 XSS 攻击
- **输入验证**：清理用户输入
- **输出编码**：防止注入攻击
- **CSRF 保护**：反 CSRF 令牌、SameSite cookie
- **速率限制**：防止暴力攻击
- **安全标头**：X-Frame-Options、X-Content-Type-Options
- **依赖关系扫描**：npm 审核、Snyk、Dependabot
## 测试
### 测试类型
- **单元测试**：单个组件/功能
- **集成测试**：组件交互
- **端到端 (E2E)**：完整的用户工作流程
- **视觉回归**：UI 变化检测
- **性能测试**：负载、压力、尖峰测试
- **辅助功能测试**：WCAG 合规性
### 测试框架
- **Jest**：JavaScript 测试框架
- **Mocha**：灵活的测试运行器
- **pytest**：Python 测试框架
- **RSpec**：Ruby 测试框架
- **JUnit**：Java 测试框架
### E2E测试工具
- **Selenium**：浏览器自动化
- **赛普拉斯**：现代 E2E 测试
- **剧作家**：跨浏览器自动化
- **Puppeteer**：无头 Chrome 控件
## 辅助功能 (a11y)
### WCAG 指南
- **可感知**：文本替代、标题、可调整内容
- **可操作**：键盘导航，时间充足，无癫痫发作
- **可理解**：可读、可预测、输入辅助
- **稳健**：与辅助技术兼容
### 实施
- **语义 HTML**：正确的标题层次结构、地标
- **ARIA 属性**：角色、状态、属性
- **焦点管理**：可见的焦点指示器，逻辑选项卡顺序
- **颜色对比度**：文本比例至少为 4.5:1
- **屏幕阅读器测试**：NVDA、JAWS、VoiceOver
- **键盘导航**：所有交互元素均可访问
## 渐进式 Web 应用程序 (PWA)
### PWA 功能
- **Service Workers**：离线功能、后台同步
- **Web App Manifest**：安装提示、图标、主题颜色
- **App Shell**：缓存的 UI 骨架
- **推送通知**：用户参与度
- **响应式设计**：适用于所有设备
- **需要 HTTPS**：安全上下文
### 工具
- **Workbox**：服务工作者库
- **灯塔**：PWA 审计
- **PWA Builder**：生成清单和图标
## 新兴技术
### WebAssembly (Wasm)
- **目的**：以接近本机的速度在浏览器中运行编译后的代码
- **语言**：C++、Rust、Go 编译目标
- **用例**：游戏、视频编辑、密码学、机器学习推理
### 无服务器架构
- **函数即服务**：AWS Lambda、Azure Functions、Google Cloud Functions
- **优点**：无需服务器管理、自动扩展、按使用付费
- **注意事项**：冷启动、供应商锁定、调试复杂性
### Jamstack 架构
- **JavaScript**：客户端交互
- **API**：无服务器功能、第三方服务
- **标记**：预构建的静态文件
- **工具**：Next.js、Gatsby、Hugo、Eleventy
- **优点**：性能、安全性、可扩展性、开发人员体验
### 实时通讯
- **WebSockets**：双向通信
- **服务器发送事件**：服务器到客户端流式传输
- **WebRTC**：点对点视频、音频、数据
- **用例**：聊天、协作、直播、游戏
### 微前端
- **概念**：将微服务扩展到前端
- **方法**：构建时、运行时、边缘集成
- **好处**：独立部署、团队自治
- **挑战**：一致性、性能、复杂性