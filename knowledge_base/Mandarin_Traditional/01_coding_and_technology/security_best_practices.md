---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 安全最佳實踐
保護應用程式、基礎設施和資料（從開發到生產）的實用指南。
---

## OWASP 前 10 名 (2021) — 概述
1. **存取控制被破壞**：使用者可以存取他們不應該存取的資源。
2. **加密失敗**：加密較弱或缺失。
3. **注入**：SQL、NoSQL、作業系統指令或 LDAP 注入。
4. **不安全的設計**：架構缺陷。
5. **安全配置錯誤**：預設密碼、開放連接埠、詳細錯誤。
6. **易受攻擊和過時的元件**：依賴項中的已知 CVE。
7. **身分和驗證失敗**：密碼弱、會話管理不善。
8. **軟體和資料完整性故障**：供應鏈攻擊、未簽署的更新。
9. **安全日誌記錄和監控失敗**：未偵測到違規行為。
10. **伺服器端請求偽造 (SSRF)**：濫用伺服器向內部系統發出請求。
---

## 輸入驗證和輸出編碼
### 驗證規則
- **白名單>黑名單**：定義允許的模式（例如電子郵件的正規表示式）而不是阻止已知的不良模式。
- **長度限制**：強制執行最大長度以防止緩衝區溢位和 DoS。
- **類型檢查**：確保整數是整數，布林值是布林值。
- **使用經過良好測試的函式庫**：對於電子郵件、URL 和日期驗證，請使用標準函式庫（例如，Python 中的 `email-validator`、Node 中的 `validator.js`）。
### 輸出編碼
- **HTML 編碼**：編碼`<`、`>`、`&`、`"`、`'`以防止 XSS。
- **SQL 參數化**：切勿將使用者輸入連接到 SQL 查詢。使用參數化查詢（準備好的語句）或 ORM。
- **Shell 轉義**：避免從使用者輸入建置 shell 命令；如果不可避免，請使用`shlex.quote()`或類似的。
---

## 身份驗證和授權
### 密碼管理
- **雜湊**：使用強而慢的雜湊演算法儲存密碼：**Argon2id**（首選）、**bcrypt**、**scrypt** 或 **PBKDF2**。
- **加鹽**：添加獨特的每用戶鹽。
- **最小長度**：強制至少 12–16 個字元。
- **MFA（多重驗證）**：敏感操作需要第二個因素（TOTP、SMS、硬體金鑰）。
- **速率限制**：防止登入端點上的暴力嘗試（例如，每個 IP/使用者每 5 分鐘 5 次嘗試）。
### 會話管理
- 使用安全性、僅限 HTTP、SameSite cookie 作為會話令牌。
- 設定適當的到期時間。
- 登出和更改密碼時會話無效。
- 避免在 URL 中暴露會話 ID。
### OAuth2 / OIDC
- 使用成熟的函式庫（例如 Authlib、PyJWT、Passport.js、Spring Security）。
- 徹底驗證 ID 令牌（簽名、發行者、受眾、過期）。
- 使用狀態參數來防止CSRF。
- 保守客戶秘密。
### JWT（JSON Web 令牌）
- **簽章**：使用RS256或ES256（非對稱）以獲得更好的安全性；如果共用金鑰管理得當，HS256（對稱）是可以接受的。
- **驗證**：始終驗證簽名、發行者 (`iss`)、受眾 (`aud`) 和過期 (`exp`)。
- **保持較短的有效期**：存取權杖為 15-60 分鐘；對於較長的會話使用刷新令牌。
- **安全儲存**：切勿將 JWT 儲存在 localStorage 中（容易受到 XSS 攻擊）；請改用僅 HTTP 的 cookie。
---

## API 安全
### 身份驗證
- 始終對 API 呼叫進行身份驗證（公共端點除外）。
- 優先使用 API 金鑰或 OAuth2 令牌而不是基本驗證（基本驗證在每個請求上發送憑證）。
### 速率限制與節流
- 應用每個使用者和每個 IP 的速率限制以防止濫用和 DoS。
- 傳回帶有​​`Retry-After`標頭的 `429 Too Many Requests`。
### CORS（跨源資源共享）
- 僅允許特定來源（生產中絕不允許 `*`）。
- 在伺服器端驗證`Origin`標頭。
### 輸入驗證
- 驗證所有請求參數，包括標頭和正文。
- 拒絕意外欄位（JSON 架構中的`"strict": true`或 `additionalProperties: false`）。
### HTTPS / TLS
- 在生產中強制執行 HTTPS。
- 使用 HSTS（HTTP 嚴格傳輸安全性）強制瀏覽器使用 HTTPS。
- 使用 TLS 1.2 或 1.3（停用 TLS 1.0/1.1）。
---

## 秘密管理
### 永遠不要對秘密進行硬編碼
- 不要將機密（API 金鑰、密碼、資料庫 URL）提交給原始碼管理。
- 使用環境變數或秘密管理工具。
＃＃＃ 工具
|工具|描述 |
|------|-------------|
| **HashiCorp 金庫** |企業級動態機密 |
| **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager** |雲端原生 |
| **標準操作規程** |加密文件中的機密並提交它們（使用 KMS 或 GPG） |
| **Docker 的秘密** |對於群體模式； Kubernetes 機密（考慮外部 Secrets Store CSI 驅動程式）|
### 旋轉
- 定期輪調機密和服務帳戶。
- 盡可能自動輪換。
---

## 依賴管理
### 漏洞掃描
|語言/平台 |工具|
|--------------------|--------|
| **Python** | `safety`、`pip-audit`、`bandit` |
| **節點** | `npm audit`、`yarn audit`、`snyk` |
| **生鏽** |`cargo audit`|
| **去** |`govulncheck`|
| **一般** |`Dependabot`(GitHub)、`Renovate`、`Trivy` |
### 修補
- 保持依賴項更新到已修補的版本。
- 為次要/補丁更新設定自動拉取請求。
- 查看變更日誌以了解重大變更。
### 供應鏈完整性
- 使用套件鎖定檔案（`package-lock.json`、`Cargo.lock`、`go.sum`）來確保可重現的建置。
- 驗證下載的依賴項的校驗和。
- 更喜歡官方註冊並僅信任經過驗證的發布商。
---

## 基礎設施安全
### 防火牆
- 封鎖除明確需要的連接埠（例如 80、443）之外的所有入站連接埠。
- 將 SSH 存取權限限制為特定 IP 範圍（或使用 VPN/堡壘主機）。
- 使用安全性群組 (AWS) 或 NSG (Azure) 進行細微控制。
### 作業系統強化
- 定期应用安全更新（`sudo apt upgrade`、`yum update`）。
- 停用不必要的服務和預設帳戶。
- 使用fail2ban 阻止 SSH 上的暴力尝试。
- 强化 SSH：禁用 root 登录、使用基于密钥的身份验证、更改默认端口（可选）。
### 網路分段
- 將資料庫和快取放置在無法存取網際網路的私有子網路中。
- 使用 DMZ 提供面向公眾的服務。
- 對網路存取應用最小權限原則。
### 基礎設施中的秘密
- 除非加密，否則切勿將機密儲存在 CI/CD 環境變數中。
- 對 EC2/VM 執行個體使用雲端提供者的 IAM 角色，而不是長期金鑰。
---

## 日誌記錄和監控
### 記錄什麼
- 身份驗證事件（成功/失敗）。
- 存取控制決策（授權失敗）。
- 管理操作（使用者建立、刪除、權限變更）。
- 資料庫架構更改。
- 系統錯誤和異常。
- API 請求和回應（編輯敏感資料）。
### 不記錄什麼
- 密碼、秘密、令牌、PII（個人識別資訊），除非經過雜湊/編輯。
- 完整的信用卡號碼。
### 警報
- 設定警報：
  - 多次登入失敗（潛在的暴力破解）。
  - 不尋常的訪問模式（例如，從新地點、在奇怪的時間）。
  - 建立新的管理員帳戶。
  - 高錯誤率或延遲峰值。
- 使用 SIEM（安全資訊和事件管理）進行進階關聯。
### 日誌保留
- 根據監管要求，將日誌保留至少 30-90 天。
- 將日誌儲存在集中式防篡改系統中（例如 ELK Stack、Splunk、Datadog）。
---

## 安全開發生命週期 (SDL)
1. **培訓**：確保開發人員了解常見漏洞。
2. **威脅建模**：在設計初期識別潛在威脅。
3. **安全編碼標準**：透過檢查和代碼審查清單強制執行。
4. **SAST**（靜態應用程式安全測試）：掃描原始程式碼中的漏洞（SonarQube、CodeQL）。
5. **DAST**（動態應用程式安全測試）：掃描正在執行的應用程式（OWASP ZAP、Burp Suite）。
6. **SCA**（軟體構成分析）：掃描依賴關係。
7. **滲透測試**：定期進行道德駭客攻擊練習。
8. **錯誤賞金**：鼓勵外部研究者負責任地發現漏洞。
9. **事件回應計畫**：針對偵測到違規行為制定明確的計畫。
---

## 緊急檢查表（懷疑有違規時）
1. **不要驚慌**－但要迅速採取行動。
2. **隔離**受影響的系統（如果需要，請中斷網路連線）。
3. **保留證據**：捕獲日誌、記憶體轉儲和磁碟映像。
4. **確定**範圍：哪些系統、哪些資料。
5. **輪換**所有洩漏的憑證和機密。
6. **修補**漏洞。
7. 如有需要，**通知**受影響的使用者和監管機構（在法定期限內）。
8. **事後分析**以了解根本原因並改善流程。