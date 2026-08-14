<!--
---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# API 設計和架構
API（應用程式介面）是軟體元件相互通訊的方式。設計良好的 API 直覺、一致且使用起來很愉快。設計不當會導致混亂、錯誤和挫折感。該文件涵蓋了建立開發人員實際想要使用的 API 的原則、模式和實踐。
---

## REST API 原則
REST（表述性狀態傳輸）是 Web API 的主要架構風格。它將資料視為由 URL 標識的**資源**，並使用 HTTP 方法對其進行操作。
### 核心原則
|原理|說明 |
|------------|-------------|
| **資源** |一切都是帶有 URI 的資源（`/users/123`、`/orders/456`） |
| **HTTP 方法** | GET（讀取）、POST（建立）、PUT（替換）、PATCH（部分更新）、DELETE（刪除）|
| **無國籍** |每個請求包含所需的所有資訊；沒有伺服器端會話狀態|
| **統一介面** |一致的資源命名、標準方法、標準狀態碼|
| **代表** |資源可以用多種格式表示（JSON、XML）|
### 資源命名約定
|做|不要 |
|----|--------|
| `/users`（複數名詞）| `/user`（單數）|
| `/users/123/orders`（嵌套）|`/getOrdersForUser?id=123`|
| `/products?category=electronics`（用於過濾的查詢參數）|`/productsByCategory/electronics`|
|使用連字號：`/user-profiles` |使用底線：`/user_profiles` |
### HTTP 方法和冪等性
|方法|目的|冪等？ |安全的？ |
|--------|---------|-------------|--------|
| **取得** |閱讀資源 | ✅ 是的 | ✅ 是的 |
| **發佈** |建立資源 | ❌ 否 | ❌ 否 |
| **放置** |完全替換資源 | ✅ 是的 | ❌ 否 |
| **補丁** |部分更新資源 | ❌ 否* | ❌ 否 |
| **刪除** |刪除資源 | ✅ 是的 | ❌ 否 |
*透過精心設計，PATCH 可以成為冪等的。
### HTTP 狀態碼
|程式碼|意義|何時使用 |
|------|---------|-------------|
| **200** |好的 |成功取得、放置、修補、刪除 |
| **201** |建立 |成功 POST（已建立資源）|
| **204** |沒有內容 |成功刪除（無回傳值）|
| **400** |錯誤的請求 |輸入無效或格式錯誤的請求 |
| **401** |未經授權 |驗證缺失或無效 |
| **403** |禁止 |已認證但未授權 |
| **404** |未找到 |資源不存在 |
| **409** |衝突|重複資源或狀態衝突 |
| **422** |無法處理的實體 |有效的 JSON 但語意錯誤 |
| **429** |太多請求 |超出速率限制 |
| **500** |內部伺服器錯誤 |意外的伺服器錯誤 |
| **502** |錯誤網關 |上游服務故障 |
| **503** |服務無法使用 |暫時超載或維護|
---

## API 版本控制
API 不斷發展。當您需要進行重大變更時，版本控制可讓現有客戶端繼續運作。
|戰略|範例|優點 |缺點 |
|----------|---------|------|-----|
| **URL 路徑** |`/v1/users`,`/v2/users`|簡單、明確 |每個版本的 URL 變更 |
| **查詢參數** |`/users?version=2`|彈性|容易忘記|
| **標題** |`Accept: application/vnd.myapi.v2+json`|乾淨的網址 |不易被發現 |
| **無版本控制** |僅架構演進 |最簡單|重大變更影響每個人 |
**最佳實務**：為了清晰起見，使用 URL 路徑版本控制 (`/v1/`)。至少支援一個以前的版本。棄用具有明確時間表的舊版本。
---

## 驗證方法
|方法|它是如何運作的 |最適合 |
|--------|-------------|----------|
| **API 金鑰** |標頭中的金鑰 (`X-API-Key: abc123`) |伺服器到伺服器的簡單整合 |
| **OAuth2** |具有範圍的基於令牌的委託 |第三方存取、用戶授權的應用程式 |
| **智威湯遜** |帶有聲明的獨立令牌 |跨服務的無狀態身份驗證 |
| **基本驗證** | Base64 編碼的使用者名稱:密碼 |僅限開發 — 沒有 TLS 絕不進行生產 |
| **會話cookie** |僅 HTTP cookie 中的伺服器端會話 ID |傳統網頁應用程式|
### OAuth2 流程（簡化）
1. 用戶端將使用者重新導向到授權伺服器。
2. 使用者登入並授予權限。
3. 授權伺服器傳回授權碼。
4. 用戶端用程式碼交換存取權杖（以及可選的刷新令牌）。
5. 客戶端使用存取令牌呼叫 API。
6. 當存取令牌過期時，使用刷新令牌取得新的令牌。
---

## API 風格：REST、GraphQL、gRPC
|特色 |休息 | GraphQL | gRPC |
|--------|------|---------|-----|
| **資料格式** | JSON（通常）| JSON | Protobuf（二進位）|
| **端點** |多個（每個資源一個）|單端點|由.proto檔案定義 |
| **過度取得** |常見（獲得超出所需的數量）|無（客戶端指定欄位）|無（架構定義）|
| **取得不足** |需要多次通話 |無（準確取得所需內容）|無 |
| **即時** |需要 WebSockets |內建訂閱 |內建串流|
| **快取** | HTTP 快取自然而然地發揮作用 |更難緩存|有限公司|
| **學習曲線** |低|中|中-高|
| **最適合** |公共 API、CRUD 應用程式 |複雜的使用者介面、行動應用程式 |內部微服務，高效能 |
---

## 分頁、過濾和排序
對於傳回清單的端點：
|技術|範例|何時使用 |
|------------|---------|-------------|
| **偏移/限制** |`?offset=20&limit=10`|簡單的;適用於小型資料集 |
| **基於遊標** |`?cursor=abc123&limit=10`|大型資料集；一致的結果 |
| **按鍵組** |`?created_after=2024-01-01&limit=10`|非常有效率；需要唯一的金鑰 |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## 速率限制
保護您的 API 免於濫用並確保公平使用。
|戰略|它是如何運作的 |
|----------|-------------|
| **固定視窗** |每個時間窗口 N 個請求（例如 100 個/小時）|
| **滑動窗** |更細粒度；計算滾動視窗中的請求數 |
| **令牌桶** |以固定比率添加代幣；每個請求消耗一個令牌 |
傳回帶有標頭的 `429 Too Many Requests`：```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## 錯誤處理
一致的錯誤回應使 API 更易於使用：
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**原則**：使用一致的錯誤結構，包括可操作的訊息，使用標準 HTTP 狀態代碼，使用相關 ID 在伺服器端記錄錯誤，並且絕不公開堆疊追蹤或內部詳細資訊。
---

## API 文檔
|工具|描述 |
|------|-------------|
| **OpenAPI (Swagger)** | REST API 文件的業界標準 |
| **Swagger 使用者介面** | OpenAPI 規格中的互動式 API 文件 |
| **郵差** | API 測試、文件和集合共用 |
| **重做** | OpenAPI 規格中精美的 API 參考文件 |
| **GraphQL 遊樂場 / GraphiQL** |互動式 GraphQL 探索 |
**最佳實務**：先編寫 OpenAPI 規格（規格驅動開發），然後從中產生文件和用戶端 SDK。
---

## API 閘道模式
API 閘道位於客戶端和後端服務之間，提供單一入口點。
|責任|描述 |
|----------------|-------------|
| **路由** |將請求直接傳送到適當的後端服務 |
| **身份驗證** |在網關層級驗證令牌 |
| **速率限制** |應用全域或每個客戶端限制 |
| **轉型** |協定之間轉換 (REST ↔ gRPC) |
| **快取** |快取常見回應 |
| **監控** |集中式日誌記錄與指標 |
| **負載平衡** |跨服務實例分配流量 |
|工具|類型 |
|------|------|
| **孔** |開源API網關（基於Nginx）|
| **AWS API 閘道** |完全託管，與 AWS 整合 |
| **Azure API 管理** |具有開發者入口網站的託管網關 |
| **特使/Istio** |具有API網關功能的服務網格|
| **Traefik** |自動發現、Let's Encrypt 整合 |
---

## 網路鉤子
Webhooks 讓您的 API 將事件即時推送到客戶端，而不是讓客戶端輪詢變更。
|方面|最佳實務|
|--------|--------------|
| **交貨** |將帶有 JSON 負載的 POST 請求傳送到客戶端的 URL |
| **安全性** |使用 HMAC 對有效負載進行簽章；客戶驗證簽章|
| **可靠性** |使用指數退避重試失敗的交付 |
| **冪等性** |包含唯一的事件 ID；客戶端處理重複項 |
| **版本控制** |在 webhook 負載中包含 API 版本 |
---

## 設計清單
- [ ] 資源是複數名詞（`/users`，而不是`/getUser`）
- [ ] 正確使用 HTTP 方法（GET 用於讀取，POST 用於建立等）
- [ ] 一致的錯誤回應格式
- [ ] 所有清單端點的分頁
- [ ] 具有清晰標頭的速率限制
- [ ] 定義 API 版本控制策略
- [ ] 身分驗證與授權到位
- [ ] 所有端點上的輸入驗證
- [ ] OpenAPI/Swagger 文件已維護
- [ ] CORS 配置正確
- [ ] 在生產中強制執行 HTTPS
- [ ] 需要時用於 POST 運算的冪等金鑰