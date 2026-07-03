# Web 開發

## 前端開發

### 核心技術

#### HTML (HyperText Markup Language)
- **語意化 HTML**:使用有意義的標籤(`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **表單**:輸入類型、驗證、無障礙標籤
- **媒體**:圖片、影片、音訊嵌入
- **Meta 標籤**:SEO、viewport、字元編碼
- **HTML5 功能**:Canvas、SVG、本地儲存、地理位置、Web Socket

#### CSS (Cascading Style Sheets)
- **盒模型**:內容、內距、邊框、外距
- **排版系統**:
  - **Flexbox**:一維排版、justify-content、align-items
  - **Grid**:二維排版、grid-template、grid-area
  - **定位**:靜態、相對、絕對、固定、黏性
- **響應式設計**:媒體查詢、行動優先方法
- **CSS 變數**:自訂屬性用於主題設計
- **動畫**:過渡效果、關鍵影格、轉換
- **預處理器**:Sass、Less(變數、混合、巢狀)

#### JavaScript
- **DOM 操作**:選取、建立、修改元素
- **事件**:點擊、提交、鍵盤、自訂事件、事件委派
- **ES6+ 功能**:箭頭函式、解構、展開/其餘運算子、模組、async/await
- **API**:Fetch、XMLHttpRequest、localStorage、sessionStorage
- **TypeScript**:靜態類型、介面、泛型、裝飾器

### 現代前端框架

#### React
- **元件**:函式元件、類別元件
- **Hooks**:useState、useEffect、useContext、useReducer、自訂 hooks
- **狀態管理**:Context API、Redux、Zustand、Recoil
- **路由**:React Router(BrowserRouter、Routes、Route、Link)
- **生態系統**:Next.js(SSR、SSG)、Remix、Gatsby
- **虛擬 DOM**:透過差異演算法實現高效渲染

#### Vue.js
- **Options API**:data、methods、computed、watch
- **Composition API**:setup()、ref、reactive、computed
- **指令**:v-if、v-for、v-bind、v-on、v-model
- **Vuex/Pinia**:狀態管理
- **Vue Router**:客戶端路由
- **Nuxt.js**:伺服器端渲染框架

#### Angular
- **元件**:裝飾器、模板、生命週期鉤子
- **服務**:依賴注入、單例模式
- **RxJS**:反應式程式設計、可觀察物件
- **路由**:RouterModule、守衛、解析器
- **表單**:模板驅動表單、反應式表單
- **NgRx**:Redux 風格的狀態管理

### 建構工具與打包器
- **Webpack**:模組打包、程式碼分割、載入器、外掛
- **Vite**:使用原生 ES 模組的快速建構工具
- **Parcel**:零配置打包器
- **Rollup**:針對函式庫最佳化
- **esbuild**:極快的 JavaScript 打包器
- **Babel**:JavaScript 轉譯器,用於向後相容
- **PostCSS**:使用外掛進行 CSS 處理

### CSS 框架與函式庫
- **Bootstrap**:元件庫、網格系統、實用工具
- **Tailwind CSS**:實用工具優先的 CSS 框架
- **Material UI**:Google Material Design 實作
- **Chakra UI**:無障礙元件庫
- **Ant Design**:企業級 UI 元件
- **Styled Components**:CSS-in-JS 函式庫
- **Emotion**:帶來源映射的 CSS-in-JS

## 後端開發

### 伺服器端語言

#### Node.js
- **執行環境**:伺服器上的 JavaScript(V8 引擎)
- **Express.js**:極簡 Web 框架、中介軟體架構
- **NestJS**:受 Angular 啟發的架構、TypeScript
- **Fastify**:高效能框架
- **Koa**:由同一創建者打造的現代版 Express
- **套件管理**:npm、yarn、pnpm

#### Python
- **Django**:功能完整的框架、ORM、管理面板、內建電池
- **Flask**:微框架、擴充套件生態系統
- **FastAPI**:現代、非同步、自動產生 API 文件
- **Pyramid**:靈活、可擴展的框架

#### 其他後端語言
- **Ruby on Rails**:慣例優於配置、ActiveRecord ORM
- **Java Spring**:企業級框架、依賴注入
- **PHP Laravel**:優雅語法、Eloquent ORM、Blade 模板
- **Go Gin**:高效能、極簡框架
- **Rust Actix**:記憶體安全、效能
- **C# ASP.NET Core**:跨平台、企業級功能

### 資料庫整合

#### ORM (物件關聯映射)
- **Sequelize**:Node.js 的 SQL 資料庫 ORM
- **Prisma**:類型安全的資料庫存取、自動產生客戶端
- **SQLAlchemy**:Python SQL 工具套件與 ORM
- **ActiveRecord**:Ruby on Rails ORM
- **Hibernate**:Java ORM
- **Entity Framework**:.NET ORM

#### 資料庫驅動程式
- **pg**:Node.js 的 PostgreSQL 客戶端
- **mysql2**:支援 Promise 的 MySQL 客戶端
- **pymongo**:Python 的 MongoDB 驅動程式
- **redis**:多語言的 Redis 客戶端

### API 開發

#### REST API
- **HTTP 方法**:GET、POST、PUT、PATCH、DELETE
- **狀態碼**:200、201、400、401、403、404、500
- **資源命名**:名詞、複數、階層式
- **版本控制**:URL 路徑、標頭、查詢參數
- **身份驗證**:JWT、OAuth、API 金鑰
- **文件**:OpenAPI/Swagger、Postman

#### GraphQL
- **結構定義**:類型、查詢、變更、訂閱
- **解析器**:欄位層級資料擷取
- **Apollo Server**:GraphQL 伺服器實作
- **Relay**:Facebook 的 GraphQL 客戶端
- **優勢**:無過度擷取、單一端點、強類型

#### gRPC
- **Protocol Buffers**:介面定義語言
- **HTTP/2**:雙向串流
- **使用場景**:微服務通訊、即時應用程式

### 身份驗證與授權
- **基於 Session**:Cookie、伺服器端 Session
- **基於 Token**:JWT(JSON Web Token)、無狀態
- **OAuth 2.0**:授權框架、第三方登入
- **OpenID Connect**:OAuth 2.0 上的身份層
- **SAML**:企業單一登入
- **密碼雜湊**:bcrypt、argon2、scrypt
- **多重要素驗證**:TOTP、簡訊、電子郵件驗證碼

## DevOps 與部署

### 版本控制
- **Git**:分散式版本控制
- **GitHub/GitLab/Bitbucket**:儲存庫託管
- **分支策略**:Git Flow、GitHub Flow、基於主幹的開發
- **CI/CD**:自動化測試與部署管道

### 容器化
- **Docker**:容器執行環境、Dockerfile、映像檔
- **Docker Compose**:多容器編排
- **容器儲存庫**:Docker Hub、AWS ECR、Google GCR
- **最佳實踐**:多階段建構、最小化基礎映像檔

### 編排
- **Kubernetes**:容器編排、Pod、服務、部署
- **Helm**:Kubernetes 套件管理器
- **服務網格**:Istio、Linkerd 用於微服務網路

### 雲端平台
- **AWS**:EC2、S3、Lambda、RDS、CloudFront、ECS/EKS
- **Google Cloud**:Compute Engine、Cloud Storage、Cloud Functions、GKE
- **Azure**:虛擬機器、Blob 儲存、Functions、AKS
- **Vercel**:前端部署、無伺服器函式
- **Netlify**:靜態網站託管、無伺服器函式
- **Heroku**:平台即服務(PaaS)
- **DigitalOcean**:簡化的雲端基礎架構

### CI/CD 管道
- **GitHub Actions**:工作流程自動化
- **GitLab CI**:內建的持續整合
- **Jenkins**:可擴展的自動化伺服器
- **CircleCI**:雲端 CI/CD
- **Travis CI**:持續整合服務
- **ArgoCD**:Kubernetes 的 GitOps 持續交付

### 監控與日誌記錄
- **應用程式效能**:New Relic、Datadog、AppDynamics
- **錯誤追蹤**:Sentry、Rollbar、Bugsnag
- **日誌記錄**:ELK Stack(Elasticsearch、Logstash、Kibana)、Splunk
- **正常運作時間監控**:Pingdom、UptimeRobot
- **分析**:Google Analytics、Mixpanel、Amplitude

## Web 效能

### 最佳化技術
- **程式碼分割**:延遲載入、動態匯入
- **Tree Shaking**:移除未使用的程式碼
- **最小化**:減少檔案大小
- **壓縮**:Gzip、Brotli
- **快取**:瀏覽器快取、CDN、Service Worker
- **圖片最佳化**:WebP、AVIF、延遲載入、響應式圖片
- **關鍵 CSS**:內聯首屏樣式
- **資料庫最佳化**:索引、查詢最佳化、連線池

### 核心 Web 指標
- **LCP (最大內容繪製)**:載入效能(<2.5s)
- **FID (首次輸入延遲)**:互動性(<100ms)
- **CLS (累積版面配置位移)**:視覺穩定性(<0.1)
- **INP (互動到下一次繪製)**:響應性指標

### 內容傳遞網路(CDN)
- **Cloudflare**:安全、效能、DNS
- **Akamai**:企業級 CDN
- **Amazon CloudFront**:AWS CDN
- **Fastly**:邊緣雲端平台
- **StackPath**:邊緣服務

## Web 安全

### 常見漏洞(OWASP Top 10)
- **注入**:SQL 注入、命令注入
- **身份驗證失效**:Session 劫持、憑證填充
- **敏感資料外洩**:未加密資料、弱加密
- **XML 外部實體(XXE)**:XML 解析器漏洞
- **存取控制失效**:權限提升、未授權存取
- **安全設定錯誤**:預設憑證、詳細錯誤訊息
- **跨站腳本攻擊(XSS)**:反射型、儲存型、DOM 型
- **不安全的反序列化**:物件注入攻擊
- **使用已知漏洞的元件**:過時的依賴套件
- **日誌記錄與監控不足**:未偵測到的入侵

### 安全最佳實踐
- **HTTPS**:TLS/SSL 加密、HSTS
- **內容安全政策(CSP)**:防止 XSS 攻擊
- **輸入驗證**:清理使用者輸入
- **輸出編碼**:防止注入攻擊
- **CSRF 防護**:反 CSRF Token、SameSite Cookie
- **速率限制**:防止暴力破解攻擊
- **安全標頭**:X-Frame-Options、X-Content-Type-Options
- **依賴項掃描**:npm audit、Snyk、Dependabot

## 測試

### 測試類型
- **單元測試**:個別元件/函式
- **整合測試**:元件互動
- **端對端測試(E2E)**:完整的使用者工作流程
- **視覺回歸測試**:UI 變更偵測
- **效能測試**:負載、壓力、尖峰測試
- **無障礙測試**:WCAG 合規性

### 測試框架
- **Jest**:JavaScript 測試框架
- **Mocha**:靈活的測試執行器
- **pytest**:Python 測試框架
- **RSpec**:Ruby 測試框架
- **JUnit**:Java 測試框架

### E2E 測試工具
- **Selenium**:瀏覽器自動化
- **Cypress**:現代 E2E 測試
- **Playwright**:跨瀏覽器自動化
- **Puppeteer**:無頭 Chrome 控制

## 無障礙(a11y)

### WCAG 指南
- **可感知**:文字替代、字幕、可調整內容
- **可操作**:鍵盤導航、足夠時間、無癲癇發作風險
- **可理解**:可讀、可預測、輸入協助
- **健全**:與輔助技術相容

### 實作
- **語意化 HTML**:適當的標題階層、地標
- **ARIA 屬性**:角色、狀態、屬性
- **焦點管理**:可見的焦點指示器、合理的 Tab 順序
- **色彩對比**:文字最低 4.5:1 比例
- **螢幕閱讀器測試**:NVDA、JAWS、VoiceOver
- **鍵盤導航**:所有互動元素可存取

## 漸進式 Web 應用程式(PWA)

### PWA 功能
- **Service Worker**:離線功能、背景同步
- **Web App Manifest**:安裝提示、圖示、主題色彩
- **App Shell**:快取的 UI 骨架
- **推播通知**:使用者參與
- **響應式設計**:在所有裝置上運作
- **需要 HTTPS**:安全環境

### 工具
- **Workbox**:Service Worker 函式庫
- **Lighthouse**:PWA 稽核
- **PWA Builder**:產生 Manifest 與圖示

## 新興技術

### WebAssembly (Wasm)
- **目的**:在瀏覽器中以接近原生速度執行編譯後的程式碼
- **語言**:C++、Rust、Go 編譯目標
- **使用場景**:遊戲、影片編輯、密碼學、機器學習推論

### 無伺服器架構
- **函式即服務**:AWS Lambda、Azure Functions、Google Cloud Functions
- **優勢**:無伺服器管理、自動擴展、按使用付費
- **考量因素**:冷啟動、供應商鎖定、除錯複雜度

### Jamstack 架構
- **JavaScript**:客戶端互動
- **API**:無伺服器函式、第三方服務
- **Markup**:預先建構的靜態檔案
- **工具**:Next.js、Gatsby、Hugo、Eleventy
- **優勢**:效能、安全、可擴展性、開發體驗

### 即時通訊
- **WebSocket**:雙向通訊
- **Server-Sent Events**:伺服器到客戶端串流
- **WebRTC**:點對點視訊、音訊、資料
- **使用場景**:聊天、協作、直播、遊戲

### 微前端
- **概念**:將微服務擴展到前端
- **方法**:建構時間、執行時間、邊緣整合
- **優勢**:獨立部署、團隊自主
- **挑戰**:一致性、效能、複雜度
