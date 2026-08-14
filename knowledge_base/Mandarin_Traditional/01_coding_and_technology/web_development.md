---
# Metadata
title: "Web Development"
description: "Frontend, backend, DevOps, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# 網頁開發
## 前端開發
### 核心技術
#### HTML（超文本標記語言）
- **語意 HTML**：使用有意義的標籤（`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`）
- **表單**：輸入類型、驗證、輔助使用標籤
- **媒體**：圖像、視訊、音訊嵌入
- **元標籤**：SEO、視窗、字元編碼
- **HTML5 功能**：Canvas、SVG、本機儲存、地理定位、網路套接字
#### CSS（層疊樣式表）
- **盒子模型**：內容、填充、邊框、邊距
- **佈局系統**：
  - **Flexbox**：一維版面配置、對齊內容、對齊項目
  - **網格**：二維佈局、網格模板、網格區域
  - **定位**：靜態、相對、絕對、固定、黏性
- **響應式設計**：媒體查詢、行動優先方法
- **CSS 變數**：主題的自訂屬性
- **動畫**：轉換、關鍵影格、變換
- **預處理器**：Sass、Less（變數、mixin、巢狀）
#### JavaScript
- **DOM操作**：選擇、建立、修改元素
- **事件**：點擊、提交、鍵盤、自訂事件、事件委託
- **ES6+ 功能**：箭頭函數、解構、展開/休息、模組、非同步/等待
- **API**：Fetch、XMLHttpRequest、localStorage、sessionStorage
- **TypeScript**：靜態類型、介面、泛型、裝飾器
### 現代前端框架
#### 反應
- **組件**：功能組件、類別組件
- **鉤子**：useState、useEffect、useContext、useReducer、自訂鉤子
- **狀態管理**：Context API、Redux、Zustand、Recoil
- **路由**：React Router（BrowserRouter、路由、路由、連結）
- **生態系**：Next.js（SSR、SSG）、Remix、Gatsby
- **虛擬 DOM**：透過 diff 演算法高效渲染
#### Vue.js
- **選項 API**：資料、方法、運算、監視
- **組合 API**：setup()、ref、reactive、compute
- **指令**：v-if、v-for、v-bind、v-on、v-model
- **Vuex/Pinia**：狀態管理
- **Vue Router**：客戶端路由
- **Nuxt.js**：伺服器端渲染框架
#### 角度
- **組件**：裝飾器、模板、生命週期掛鉤
- **服務**：依賴注入，單例模式
- **RxJS**：反應式編程，可觀察量
- **路由**：RouterModule、守衛、解析器
- **表單**：範本驅動的反應式表單
- **NgRx**：Redux 風格的狀態管理
### 建置工具和捆綁器
- **Webpack**：模組捆綁、程式碼分割、載入器、插件
- **Vite**：使用原生 ES 模組的快速建置工具
- **Parcel**：零配置捆綁器
- **Rollup**：針對函式庫進行了最佳化
- **esbuild**：極快的 JavaScript 捆綁器
- **Babel**：用於向後相容的 JavaScript 轉譯器
- **PostCSS**：使用外掛程式進行 CSS 處理
### CSS 框架和函式庫
- **Bootstrap**：元件庫、網格系統、實用程式
- **Tailwind CSS**：實用優先的 CSS 框架
- **Material UI**：Google 的 Material Design 實現
- **Chakra UI**：可存取的元件庫
- **Ant Design**：企業級 UI 元件
- **樣式元件**：CSS-in-JS 函式庫
- **情感**：帶有來源映射的 CSS-in-JS
## 後端開發
### 伺服器端語言
#### Node.js
- **執行時期**：伺服器上的 JavaScript（V8 引擎）
- **Express.js**：最小的Web框架，中介軟體架構
- **NestJS**：Angular 啟發的架構，TypeScript
- **Fastify**：高效能框架
- **Koa**：同一創作者的《現代快車》
- **套件管理**：npm、yarn、pnpm
####Python
- **Django**：全功能框架、ORM、管理面板、包含電池
- **Flask**：微框架，擴展生態系統
- **FastAPI**：現代、非同步、自動 API 文檔
- **金字塔**：靈活、可擴展的框架
#### 其他後端語言
- **Ruby on Rails**：約定優於配置，ActiveRecord ORM
- **Java Spring**：企業框架，依賴注入
- **PHP Laravel**：優雅的語法、雄辯的 ORM、Blade 模板
- **Go Gin**：高性能，最小框架
- **Rust Actix**：記憶體安全、效能
- **C# ASP.NET Core**：跨平台、企業功能
### 資料庫集成
#### ORM（物件關係映射）
- **Sequelize**：用於 SQL 資料庫的 Node.js ORM
- **Prisma**：類型安全的資料庫訪問，自動生成的客戶端
- **SQLAlchemy**：Python SQL 工具包和 ORM
- **ActiveRecord**：Ruby on Rails ORM
- **Hibernate**：Java ORM
- **實體架構**：.NET ORM
#### 資料庫驅動程式
- **pg**：Node.js 的 PostgreSQL 用戶端
- **mysql2**：帶有承諾的 MySQL 用戶端
- **pymongo**：Python 的 MongoDB 驅動程式
- **redis**：多種語言的Redis客戶端
### API開發
#### REST API
- **HTTP 方法**：GET、POST、PUT、PATCH、DELETE
- **狀態代碼**：200、201、400、401、403、404、500
- **資源命名**：名詞，複數，分層
- **版本控制**：URL 路徑、標頭、查詢參數
- **身份驗證**：JWT、OAuth、API 金鑰
- **文檔**：OpenAPI/Swagger、Postman
#### GraphQL
- **模式定義**：類型、查詢、突變、訂閱
- **解析器**：字段級資料獲取
- **Apollo 伺服器**：GraphQL 伺服器實現
- **Relay**：Facebook 的 GraphQL 用戶端
- **優點**：無過度取得、單端點、強型
#### gRPC
- **協定緩衝區**：介面定義語言
- **HTTP/2**：雙向串流傳輸
- **用例**：微服務通訊、即時應用程式
### 身份驗證和授權
- **基於會話**：Cookie、伺服器端會話
- **基於令牌**：JWT（JSON Web 令牌），無狀態
- **OAuth 2.0**：授權框架，第三方登入
- **OpenID Connect**：OAuth 2.0 上的身分層
- **SAML**：企業單一登入
- **密碼雜湊**：bcrypt、argon2、scrypt
- **多重身份驗證**：TOTP、簡訊、電子郵件代碼
## DevOps 和部署
### 版本控制
- **Git**：分散式版本控制
- **GitHub/GitLab/Bitbucket**：儲存庫託管
- **分支策略**：Git Flow、GitHub Flow、基於主幹的開發
- **CI/CD**：自動化測試和部署管道
### 容器化
- **Docker**：容器執行時間、Dockerfile、映像
- **Docker Compose**：多容器編排
- **容器註冊表**：Docker Hub、AWS ECR、Google GCR
- **最佳實踐**：多階段構建，最少的基礎鏡像
### 編排
- **Kubernetes**：容器編排、pod、服務、部署
- **Helm**：Kubernetes 套件管理器
- **服務網格**：用於微服務網路的 Istio、Linkerd
### 雲端平台
- **AWS**：EC2、S3、Lambda、RDS、CloudFront、ECS/EKS
- **Google Cloud**：運算引擎、雲端儲存、雲端功能、GKE
- **Azure**：虛擬機器、Blob 儲存、函數、AKS
- **Vercel**：前端部署、無伺服器功能
- **Netlify**：靜態網站託管，無伺服器功能
- **Heroku**：平台即服務 (PaaS)
- **DigitalOcean**：簡化的雲端基礎設施
### CI/CD 管道
- **GitHub Actions**：工作流程自動化
- **GitLab CI**：內建持續集成
- **Jenkins**：可擴展的自動化伺服器
- **CircleCI**：基於雲端的 CI/CD
- **Travis CI**：持續整合服務
- **ArgoCD**：Kubernetes 的 GitOps 持續交付
### 監控和日誌記錄
- **應用程式效能**：New Relic、Datadog、AppDynamics
- **錯誤追蹤**：Sentry、Rollbar、Bugsnag
- **日誌記錄**：ELK Stack（Elasticsearch、Logstash、Kibana）、Splunk
- **正常運作時間監控**：Pingdom、UptimeRobot
- **分析**：Google Analytics、Mixpanel、Amplitude
## 網路效能
### 優化技術
- **程式碼分割**：延遲載入、動態導入
- **Tree Shaking**：刪除未使用的程式碼
- **縮小**：減少檔案大小
- **壓縮**：Gzip、Brotli
- **快取**：瀏覽器快取、CDN、服務工作者
- **影像優化**：WebP、AVIF、延遲載入、響應式影像
- **關鍵 CSS**：內嵌首屏樣式
- **資料庫最佳化**：索引、查詢最佳化、連接池
### 核心网络生命力
- **LCP（最大內容塗料）**：載入效能（<2.5s）
- **FID（首次輸入延遲）**：互動性（<100ms）
- **CLS（累積佈局偏移）**：視覺穩定性（<0.1）
- **INP（與下一個繪畫的交互）**：響應度指標
### 內容交付網路 (CDN)
- **Cloudflare**：安全性、效能、DNS
- **Akamai**：企業 CDN
- **Amazon CloudFront**：AWS CDN
- **Fastly**：邊緣雲平台
- **StackPath**：邊緣服務
## 網路安全
### 常見漏洞（OWASP 前 10 名）
- **注入**：SQL注入、指令注入
- **損壞的身份驗證**：會話劫持、憑證填充
- **敏感資料暴露**：未加密的數據，弱加密
- **XML 外部實體 (XXE)**：XML 解析器漏洞
- **存取控制失效**：權限升級、未經授權的訪問
- **安全配置錯誤**：預設憑證、詳細錯誤
- **跨站腳本 (XSS)**：反射、儲存、基於 DOM
- **不安全的反序列化**：物件注入攻擊
- **使用具有已知漏洞的元件**：過時的依賴項
- **日誌記錄和監控不足**：未偵測到的違規行為
### 安全最佳實踐
- **HTTPS**：TLS/SSL 加密、HSTS
- **內容安全策略（CSP）**：防止 XSS 攻擊
- **輸入驗證**：清理使用者輸入
- **輸出編碼**：防止注入攻擊
- **CSRF 保護**：反 CSRF 令牌、SameSite cookie
- **速率限制**：防止暴力攻擊
- **安全標頭**：X-Frame-Options、X-Content-Type-Options
- **依賴關係掃描**：npm 審核、Snyk、Dependabot
## 測試
### 測試類型
- **單元測試**：單一組件/功能
- **整合測試**：元件交互
- **端到端 (E2E)**：完整的使用者工作流程
- **視覺回歸**：UI 變化檢測
- **效能測試**：負載、壓力、尖峰測試
- **輔助功能測試**：WCAG 合規性
### 測試框架
- **Jest**：JavaScript 測試框架
- **Mocha**：靈活的測試運行器
- **pytest**：Python 測試框架
- **RSpec**：Ruby 測試框架
- **JUnit**：Java 測試框架
### E2E測試工具
- **Selenium**：瀏覽器自動化
- **賽普拉斯**：現代 E2E 測試
- **劇作家**：跨瀏覽器自動化
- **Puppeteer**：無頭 Chrome 控件
## 輔助使用 (a11y)
### WCAG 指南
- **可感知**：文字替代、標題、可調整內容
- **可操作**：鍵盤導航，時間充足，無癲癇發作
- **可理解**：可讀、可預測、輸入輔助
- **穩健**：與輔助科技相容
### 實作
- **語意 HTML**：正確的標題層次結構、地標
- **ARIA 屬性**：角色、狀態、屬性
- **焦點管理**：可見的焦點指示器，邏輯標籤順序
- **顏色對比**：文字比例至少為 4.5:1
- **螢幕閱讀器測試**：NVDA、JAWS、VoiceOver
- **鍵盤導航**：所有互動元素均可訪問
## 漸進式 Web 應用程式 (PWA)
### PWA 功能
- **Service Workers**：離線功能、背景同步
- **Web App Manifest**：安裝提示、圖示、主題顏色
- **App Shell**：快取的 UI 骨架
- **推播通知**：用戶參與度
- **響應式設計**：適用於所有設備
- **需要 HTTPS**：安全性上下文
### 工具
- **Workbox**：服務工作者庫
- **燈塔**：PWA 審計
- **PWA Builder**：產生清單和圖標
## 新興技術
### WebAssembly (Wasm)
- **目的**：以接近本機的速度在瀏覽器中執行編譯後的程式碼
- **語言**：C++、Rust、Go 編譯目標
- **用例**：遊戲、影片編輯、密碼學、機器學習推理
### 無伺服器架構
- **函數即服務**：AWS Lambda、Azure Functions、Google Cloud Functions
- **優點**：無需伺服器管理、自動擴充、按使用付費
- **注意事項**：冷啟動、供應商鎖定、調試複雜性
### Jamstack 架構
- **JavaScript**：客戶端交互
- **API**：無伺服器功能、第三方服務
- **標記**：預先建置的靜態文件
- **工具**：Next.js、Gatsby、Hugo、Eleventy
- **優點**：效能、安全性、可擴充性、開發人員體驗
### 即時通訊
- **WebSockets**：雙向通信
- **伺服器發送事件**：伺服器到客戶端串流傳輸
- **WebRTC**：點對點視訊、音訊、數據
- **用例**：聊天、協作、直播、遊戲
### 微前端
- **概念**：將微服務擴展到前端
- **方法**：建置時、執行時間、邊緣集成
- **好處**：獨立部署、團隊自治
- **挑戰**：一致性、效能、複雜性