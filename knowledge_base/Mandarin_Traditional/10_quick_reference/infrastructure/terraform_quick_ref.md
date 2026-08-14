<!--
---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Terraform 和基礎架構即程式碼
Terraform 是使用最廣泛的基礎設施即程式碼 (IaC) 工具 - 它允許您在聲明性設定檔中定義雲端基礎架構（伺服器、資料庫、網路、權限），這些檔案可以進行版本控制、審查、測試和自動化。您无需单击云控制台，而是编写描述基础设施所需状态的代码，然后 Terraform 确定要进行哪些更改。
---

## 核心概念
|概念 |描述 |
|---------|-------------|
| **提供者** |管理特定雲端平台（AWS、Azure、GCP 等）的插件 |
| **資源** |基礎設施物件（伺服器、資料庫、網路）|
| **狀態** | Terraform 對現有基礎架構的記錄；儲存在狀態檔案中|
| **計畫** |預覽 Terraform 將做出哪些改變 |
| **申請** |執行計劃；創建/更新/銷毀基礎設施|
| **模組** |可重複使用的資源集合|
| **變數** |配置的輸入參數 |
| **輸出** |從模組或組態匯出的值 |
| **資料來源** |從現有基礎設施讀取資訊 |
---

## 基本工作流程
|步驟|命令 |描述 |
|------|---------|-------------|
| **1.寫入設定** |建立`.tf`檔案 |定義提供者、資源、變數 |
| **2.初始化** |`terraform init`|下載提供者；設定後台 |
| **3.格式** |`terraform fmt`|標準化格式 |
| **4.驗證** |`terraform validate`|檢查語法與設定 |
| **5.計劃** |`terraform plan`|預覽更改（試運行）|
| **6。申請** |`terraform apply`|建立或更新基礎設施 |
| **7.摧毀** |`terraform destroy`|拆除所有託管基礎設施|
---

## 常用指令
|命令 |描述 |
|---------|-------------|
|`terraform init`|初始化工作目錄；下載提供者和模組|
|`terraform plan`|顯示將進行哪些變更 |
|`terraform apply`|應用變更；新增`-auto-approve`跳過確認 |
|`terraform destroy`|銷毀所有託管資源 |
|`terraform fmt`|將設定檔格式化為標準樣式 |
|`terraform validate`|驗證設定語法 |
|`terraform output`|顯示輸出值 |
|`terraform state list`|列出狀態 | 的所有資源
|`terraform state show <resource>`|顯示特定資源的詳細資訊 |
|`terraform import <resource> <id>`|將現有基礎設施導入州政府 |
|`terraform taint <resource>`|下次申請時標記供娛樂的資源 |
|`terraform refresh`|更新狀態以符合真實的基礎設施 |
|`terraform graph`|產生視覺化依賴圖（DOT 格式） |
|`terraform console`|用於測試表達式的互動式控制台 |
---

## 狀態管理
|最佳實踐|描述 |
|--------------|-------------|
| **遠端狀態** |將狀態儲存在 S3、GCS、Azure Blob 或 Terraform Cloud 中 — 絕不在本機 |
| **狀態鎖定** |使用 DynamoDB（S3 後端）或本機鎖定來防止並發修改 |
| **狀態加密** |為狀態檔案啟用靜態加密（它們包含敏感資料）|
| **狀態分離** |為不同的環境或團隊使用單獨的狀態檔案 |
| **狀態備份** |遠端後端自動版本狀態；保持啟用 |
| **切勿手動編輯狀態** |使用`terraform state mv`、`rm`、`import`取代 |
---

## 模組結構
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## 變數類型
|類型 |範例|使用案例|
|------|---------|----------|
| **字串** |`variable "region" { type = string }`|單一文字值 |
| **數量** |`variable "count" { type = number }`|數值 |
| **布爾** |`variable "enable" { type = bool }`|真/假標誌 |
| **清單** |`variable "zones" { type = list(string) }`|已訂購收藏|
| **地圖** |`variable "tags" { type = map(string) }`|鍵值對 |
| **物件** |`variable "config" { type = object({...}) }`|結構化設定|
---

## 常見模式
|圖案|描述 |
|---------|-------------|
| **計數** |`count = 3`建立資源的多個實例 |
| **對於每個** |`for_each = var.items`迭代映射或集合 |
| **動態區塊** |產生重複的巢狀區塊（例如入口規則）|
| **當地價值** |`locals { ... }`用於計算值並減少重複 |
| **資料來源** |讀取現有基礎架構（例如，尋找現有 VPC）|
| **供應商** |創建後在資源上運行腳本（謹慎使用）|
| **工作空間** |同一配置中不同環境的單獨狀態 |
---

## 故障排除
|問題 |解決方案 |
|---------|----------|
| **狀態漂移** |運行`terraform plan` 查看差異；`terraform apply` 調和|
| **鎖定狀態** |檢查誰擁有鎖；如果安全，請使用`terraform force-unlock`|
| **提供者錯誤** |檢查憑證；更新提供者版本；檢查 API 限制 |
| **導入衝突** |資源已處於狀態；首先使用`terraform state rm` |
| **循環依賴** |重組資源；小心使用`depends_on` |
| **大州** |分割模組；使用`-target`進行部分操作 |
---

＃＃ 概括
Terraform 透過聲明性設定檔管理基礎架構。工作流程為：撰寫設定→初始化→計畫→應用程式。狀態追蹤存在的內容並且必須透過鎖定遠端儲存。模組可實現重複使用。變數參數化配置。關鍵原則是： 將基礎設施視為代碼（版本控制；審查；測試）；切勿手動編輯狀態；申請前做好計劃；使用帶有鎖定的遠端狀態；以及具有可維護性模組的結構配置。