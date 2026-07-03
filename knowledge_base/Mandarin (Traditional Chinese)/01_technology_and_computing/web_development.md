# Web 開發

## 前端開發

### 核心技術

#### HTML（超文本標記語言）
- **語義化 HTML**：使用有意義的標籤（`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`）
- **表單**：輸入類型、驗證、無障礙標籤
- **媒體**：圖片、影片、音訊嵌入
- **Meta 標籤**：SEO、視窗、字元編碼
- **HTML5 功能**：Canvas、SVG、本地儲存、地理位置、Web Sockets

#### CSS（層疊樣式表）
- **盒模型**：內容、內距、邊框、外距
- **版面配置系統**：
  - **Flexbox**：一維版面配置、justify-content、align-items
  - **Grid**：二維版面配置、grid-template、grid-area
  - **定位**：靜態、相對、絕對、固定、黏性
- **響應式設計**：媒體查詢、行動優先方法
- **CSS 變數**：用於主題的自訂屬性
- **動畫**：過渡、關鍵影格、變形
- **預處理器**：Sass、Less（變數、混合、巢狀）

#### JavaScript
- **DOM 操作**：選擇、建立、修改元素
- **事件**：點擊、提交、鍵盤、自訂事件、事件委派
- **ES6+ 功能**：箭頭函式、解構、展開/剩餘、模組、async/await
- **API**：Fetch、XMLHttpRequest、localStorage、sessionStorage
- **TypeScript**：靜態型別、介面、泛型、裝飾器

### 現代前端框架

#### React
- **元件**：函式元件、類別元件
- **Hooks**：useState、useEffect、useContext、useReducer、自訂 hooks
- **狀態管理**：Context API、Redux、Zustand、Recoil
- **路由**：React Router（BrowserRouter、Routes、Route、Link）
- **生態系統**：Next.js（SSR、SSG）、Remix、Gatsby
- **虛擬 DOM**：透過差異演算法實現高效渲染

#### Vue.js
- **Options API**：data、methods、computed、watch
- **Composition API**：setup()、ref、reactive、computed
- **指令**：v-if、v-for、v-bind、v-on、v-model
- **Vuex/Pinia**：狀態管理
- **Vue Router**：客戶端路由
- **Nuxt.js**：伺服器端渲染框架

#### Angular
- **元件**：裝飾器、模板、生命週期掛鉤
- **服務**：依賴注入、單例模式
- **RxJS**：響應式程式設計、可觀察物件
- **路由**：RouterModule、守衛、解析器
- **表單**：範本驅動、響應式表單
- **NgRx**：Redux 風格狀態管理

### 建置工具和打包器
- **Webpack**：模組打包、程式碼分割、載入器、外掛
- **Vite**：使用原生 ES 模組的快速建置工具
- **Parcel**：零配置打包器
- **Rollup**：針對函式庫最佳化
- **esbuild**：極快的 JavaScript 打包器
- **Babel**：JavaScript 轉譯器，用於向後相容
- **PostCSS**：使用外掛進行 CSS 處理

### CSS 框架和函式庫
- **Bootstrap**：元件庫、網格系統、工具程式
- **Tailwind CSS**：工具優先的 CSS 框架
- **Material UI**：Google Material Design 實作
- **Chakra UI**：無障礙元件庫
- **Ant Design**：企業級 UI 元件
- **Styled Components**：CSS-in-JS 函式庫
- **Emotion**：具有 source maps 的 CSS-in-JS

## 後端開發

### 伺服器端語言

#### Node.js
- **執行環境**：伺服器上的 JavaScript（V8 引擎）
- **Express.js**：極簡 Web 框架、中介軟體架構
- **NestJS**：受 Angular 啟發的架構、TypeScript
- **Fastify**：高效能框架
- **Koa**：由相同創作者打造的現代 Express
- **套件管理**：npm、yarn、pnpm

#### Python
- **Django**：功能完整的框架、ORM、管理面板、內建豐富
- **Flask**：微框架、擴充生態系統
- **FastAPI**：現代、非同步、自動 API 文件
- **Pyramid**：靈活、可擴展的框架

#### 其他後端語言
- **Ruby on Rails**：約定優於配置、ActiveRecord ORM
- **Java Spring**：企業框架、依賴注入
- **PHP Laravel**：優雅的語法、Eloquent ORM、Blade 範本
- **Go Gin**：高效能、極簡框架
- **Rust Actix**：記憶體安全、效能
- **C# ASP.NET Core**：跨平台、企業功能

### 資料庫整合

#### ORM（物件關聯對映）
- **Sequelize**：Node.js 的 SQL 資料庫 ORM
- **Prisma**：型別安全的資料庫存取、自動產生的客戶端
- **SQLAlchemy**：Python SQL 工具包和 ORM
- **ActiveRecord**：Ruby on Rails ORM
- **Hibernate**：Java ORM
- **Entity Framework**：.NET ORM

#### 資料庫驅動程式
- **pg**：Node.js 的 PostgreSQL 客戶端
- **mysql2**：支援 promises 的 MySQL 客戶端
- **pymongo**：Python 的 MongoDB 驅動程式
- **redis**：多種語言的 Redis 客戶端

### API 開發

#### REST API
- **HTTP 方法**：GET、POST、PUT、PATCH、DELETE
- **狀態碼**：200、201、400、401、403、404、500
- **資源命名**：名詞、複數、階層式
- **版本控制**：URL 路徑、標頭、查詢參數
- **驗證**：JWT、OAuth、API 金鑰
- **文件**：OpenAPI/Swagger、Postman

#### GraphQL
- **架構定義**：類型、查詢、變更、訂閱
- **解析器**：欄位級資料提取
- **Apollo Server**：GraphQL 伺服器實作
- **Relay**：Facebook 的 GraphQL 客戶端
- **優勢**：無過度提取、單一端點、強型別

#### gRPC
- **Protocol Buffers**：介面定義語言
- **HTTP/2**：雙向串流
- **使用案例**：微服務通訊、即時應用程式

### 驗證和授權
- **基於 session**：Cookies、伺服器端 session
- **基於 token**：JWT（JSON Web Tokens）、無狀態
- **OAuth 2.0**：授權框架、第三方登入
- **OpenID Connect**：OAuth 2.0 上的身分層
- **SAML**：企業單一登入
- **密碼雜湊**：bcrypt、argon2、scrypt
- **多因素驗證**：TOTP、簡訊、電子郵件驗證碼

## DevOps 和部署

### 版本控制
- **Git**：分散式版本控制
- **GitHub/GitLab/Bitbucket**：儲存庫託管
- **分支策略**：Git Flow、GitHub Flow、基於主幹的開發
- **CI/CD**：自動化測試和部署流程

### 容器化
- **Docker**：容器執行環境、Dockerfile、映像檔
- **Docker Compose**：多容器編排
- **容器登錄檔**：Docker Hub、AWS ECR、Google GCR
- **最佳實踐**：多階段建置、最小基礎映像檔

### 編排
- **Kubernetes**：容器編排、pod、服務、部署
- **Helm**：Kubernetes 套件管理器
- **Service Mesh**：Istio、Linkerd 用於微服務網路

### 雲端平台
- **AWS**：EC2、S3、Lambda、RDS、CloudFront、ECS/EKS
- **Google Cloud**：Compute Engine、Cloud Storage、Cloud Functions、GKE
- **Azure**：虛擬機器、Blob Storage、Functions、AKS
- **Vercel**：前端部署、無伺服器函式
- **Netlify**：靜態網站託管、無伺服器函式
- **Heroku**：平台即服務（PaaS）
- **DigitalOcean**：簡化的雲端基礎設施

### CI/CD 流程
- **GitHub Actions**：工作流程自動化
- **GitLab CI**：內建持續整合
- **Jenkins**：可擴展的自動化伺服器
- **CircleCI**：基於雲端的 CI/CD
- **Travis CI**：持續整合服務
- **ArgoCD**：用於 Kubernetes 的 GitOps 持續交付

### 監控和日誌記錄
- **應用程式效能**：New Relic、Datadog、AppDynamics
- **錯誤追蹤**：Sentry、Rollbar、Bugsnag
- **日誌記錄**：ELK Stack（Elasticsearch、Logstash、Kibana）、Splunk
- **運行時間監控**：Pingdom、UptimeRobot
- **分析**：Google Analytics、Mixpanel、Amplitude

## Web 效能

### 最佳化技術
- **程式碼分割**：延遲載入、動態匯入
- **Tree Shaking**：移除未使用的程式碼
- **壓縮**：減少檔案大小
- **壓縮**：Gzip、Brotli
- **快取**：瀏覽器快取、CDN、service workers
- **圖片最佳化**：WebP、AVIF、延遲載入、響應式圖片
- **關鍵 CSS**：內嵌首屏樣式
- **資料庫最佳化**：索引、查詢最佳化、連線池

### 核心 Web 指標
- **LCP（最大內容繪製）**：載入效能（<2.5 秒）
- **FID（首次輸入延遲）**：互動性（<100 毫秒）
- **CLS（累積版面配置位移）**：視覺穩定性（<0.1）
- **INP（互動到下一次繪製）**：響應性指標

### 內容傳遞網路（CDN）
- **Cloudflare**：安全性、效能、DNS
- **Akamai**：企業 CDN
- **Amazon CloudFront**：AWS CDN
- **Fastly**：邊緣雲端平台
- **StackPath**：邊緣服務

## Web 安全

### 常見漏洞（OWASP Top 10）
- **注入**：SQL 注入、命令注入
- **損壞的驗證**：Session 劫持、憑證填充
- **敏感資料洩漏**：未加密資料、弱加密
- **XML 外部實體（XXE）**：XML 解析器漏洞
- **損壞的存取控制**：權限提升、未經授權的存取
- **安全性配置錯誤**：預設憑證、詳細錯誤
- **跨站指令碼（XSS）**：反射型、儲存型、基於 DOM
- **不安全的反序列化**：物件注入攻擊
- **使用已知漏洞的元件**：過時的依賴項
- **記錄和監控不足**：未偵測到的入侵

### 安全最佳實踐
- **HTTPS**：TLS/SSL 加密、HSTS
- **內容安全政策（CSP）**：防止 XSS 攻擊
- **輸入驗證**：清理使用者輸入
- **輸出編碼**：防止注入攻擊
- **CSRF 保護**：反 CSRF token、SameSite cookies
- **速率限制**：防止暴力破解攻擊
- **安全標頭**：X-Frame-Options、X-Content-Type-Options
- **依賴項掃描**：npm audit、Snyk、Dependabot

## 測試

### 測試類型
- **單元測試**：個別元件/函式
- **整合測試**：元件互動
- **端對端（E2E）**：完整使用者工作流程
- **視覺回歸**：UI 變更偵測
- **效能測試**：負載、壓力、尖峰測試
- **無障礙測試**：WCAG 合規性

### 測試框架
- **Jest**：JavaScript 測試框架
- **Mocha**：靈活的測試執行器
- **pytest**：Python 測試框架
- **RSpec**：Ruby 測試框架
- **JUnit**：Java 測試框架

### E2E 測試工具
- **Selenium**：瀏覽器自動化
- **Cypress**：現代 E2E 測試
- **Playwright**：跨瀏覽器自動化
- **Puppeteer**：無頭 Chrome 控制

## 無障礙（a11y）

### WCAG 指南
- **可感知**：文字替代、字幕、可適應的內容
- **可操作**：鍵盤導航、足夠的時間、無癲癇
- **可理解**：可讀、可預測、輸入協助
- **健壯**：與輔助技術相容

### 實作
- **語義化 HTML**：正確的標題層次、地標
- **ARIA 屬性**：角色、狀態、屬性
- **焦點管理**：可見的焦點指示器、邏輯 tab 順序
- **色彩對比**：文字最小 4.5:1 比例
- **螢幕閱讀器測試**：NVDA、JAWS、VoiceOver
- **鍵盤導航**：所有互動元素可存取

## 漸進式 Web 應用程式（PWA）

### PWA 功能
- **Service Workers**：離線功能、背景同步
- **Web App Manifest**：安裝提示、圖示、主題顏色
- **App Shell**：快取的 UI 骨架
- **推播通知**：使用者互動
- **響應式設計**：適用於所有裝置
- **需要 HTTPS**：安全情境

### 工具
- **Workbox**：Service worker 函式庫
- **Lighthouse**：PWA 稽核
- **PWA Builder**：產生 manifest 和圖示

## 新興技術

### WebAssembly（Wasm）
- **目的**：在瀏覽器中以接近原生速度執行編譯後的程式碼
- **語言**：C++、Rust、Go 編譯目標
- **使用案例**：遊戲、影片編輯、加密、ML 推論

### 無伺服器架構
- **函式即服務**：AWS Lambda、Azure Functions、Google Cloud Functions
- **優勢**：無需管理伺服器、自動擴展、按使用付費
- **考量**：冷啟動、供應商鎖定、除錯複雜性

### Jamstack 架構
- **JavaScript**：客戶端互動性
- **API**：無伺服器函式、第三方服務
- **Markup**：預建靜態檔案
- **工具**：Next.js、Gatsby、Hugo、Eleventy
- **優勢**：效能、安全性、可擴展性、開發者體驗

### 即時通訊
- **WebSockets**：雙向通訊
- **Server-Sent Events**：伺服器到客戶端串流
- **WebRTC**：點對點影片、音訊、資料
- **使用案例**：聊天、協作、直播串流、遊戲

### 微前端
- **概念**：將微服務擴展到前端
- **方法**：建置時、執行時、邊緣側整合
- **優勢**：獨立部署、團隊自主
- **挑戰**：一致性、效能、複雜性
