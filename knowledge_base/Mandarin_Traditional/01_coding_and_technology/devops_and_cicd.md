<!--
---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
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
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# DevOps 和 CI/CD
DevOps 是文化理念、實踐和工具的結合，使團隊能夠更快、更可靠地交付軟體。它打破了開發人員（想要發布更改）和營運人員（想要穩定性）之間的障礙。 CI/CD（持續整合和持續交付）是使其成為可能的自動化支柱。
---

## CI/CD 管道
### CI/CD 的實際意義
|名詞 |它有什麼作用 |
|------|-------------|
| **持續整合（CI）** |開發人員經常合併程式碼；每次合併都會觸發自動建置和測試|
| **持續交付（CD）** |程式碼始終處於可部署狀態；發佈到生產環境是一個手動決定|
| **持續部署** |通過測試的每項變更都會自動投入生產－無需手動控制 |
### 典型的管道階段
|舞台|發生了什麼事 |工具|
|--------|-------------|--------|
| **來源** |開發人員將程式碼推送到 Git | GitHub、GitLab、Bitbucket |
| **建置** |編譯程式碼，安裝依賴 | Maven、Gradle、npm、pip |
| **測試** |運行單元、整合、lint 檢查 |笑話、pytest、JUnit |
| **套餐** |建置 Docker 映像或工件 | Docker、建置包 |
| **部署（暫存）** |部署到暫存環境 | Kubernetes、ECS、虛擬機器 |
| **測試（分期）** |整合測試、冒煙測試|硒，郵差 |
| **部署（生產）** |發佈到生產環境 |藍綠色，金絲雀，滾動|
| **監控** |觀察運行狀況、錯誤、效能 |普羅米修斯、Grafana、Datadog |
### CI/CD 工具比較
|工具|類型 |實力|
|------|------|----------|
| **GitHub 操作** |雲 CI/CD |與GitHub深度整合； YAML 工作流程 |
| **亞搏體育appGitLab CI** |內建 CI/CD |回購 + 管道的單一平台 |
| **詹金斯** |自架 CI/CD |高度可配置；龐大的插件生態系統 |
| **圓CI** |雲 CI/CD |快速地;適合容器化工作流程|
| **ArgoCD** | Kubernetes 的 GitOps |宣告式、Git 驅動的部署 |
---

## Docker 和容器
### 為什麼選擇容器？
在容器出現之前，典型的問題是「它可以在我的機器上運行」。容器透過將應用程式及其所有依賴項（庫、運行時、配置）打包到一個可在任何地方相同地運行的單一便攜式單元中來解決這個問題。
### Docker 基礎知識
|概念 |描述 |
|---------|-------------|
| **圖片** |具有應用程式+相依性的唯讀範本 |
| **集裝箱** |運行圖像實例 |
| **Dockerfile** |建構映像的秘訣|
| **註冊表** |映像儲存（Docker Hub、ECR、GCR）|
| **成交量** |容器重新啟動後仍然存在的持久存儲 |
| **網路** |容器的隔離網路層|
### Dockerfile 最佳實踐
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

關鍵實務：使用 slim/alpine 基礎映像、以非 root 身分運作、利用層快取、使用`.dockerignore`、掃描鏡像是否有漏洞（`trivy`、`docker scan`）以及設定資源限制。
### Docker 組合
用於一起運行多個容器（應用程式+資料庫+快取）：
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8s)
Kubernetes 是業界標準的容器編排器。它管理容器化應用程式的部署、擴充和操作。
### 核心架構
|組件|角色 |
|------------|------|
| **控制平面** |管理叢集（API 伺服器、排程器、etcd、控制器管理器）|
| **節點** |運作容器的工作機器（VM 或實體）|
| **吊艙** |最小的可部署單位；一個或多個共享網路的容器|
| **服務** |將流量路由至 Pod 的穩定網路端點 |
| **部署** |所需 Pod 狀態的宣告式定義（副本、映像等）|
| **入口** |外部流量的HTTP路由規則|
| **配置映射/秘密** |注入 Pod 的配置和敏感資料 |
### 基本 kubectl 指令
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### 頭盔
Helm 是 Kubernetes 的套件管理器。 **圖表**是一組預先設定的 Kubernetes 資源。對於 K8s，可以將其視為`apt`或 `brew`。
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## 基礎架構即程式碼 (IaC)
IaC 對待基礎架構配置的方式與對待應用程式程式碼的方式相同：透過管道進行版本控制、測試和部署。
### Terraform 與 Ansible
|工具|類型 |方法|最適合 |
|------|------|----------|----------|
| **地形** |供應|聲明式（HCL）；基於國家的|建立雲端資源（VPC、虛擬機器、資料庫）|
| **Ansible** |設定|聲明式（YAML）；無代理程式 |設定伺服器、安裝軟體|
| **普魯米** |供應|命令式（Python、Go、TS）|更喜歡真正的程式語言的團隊|
| **雲端形成** |供應|宣告式（YAML/JSON）； AWS 原生 |僅限 AWS 的基礎架構 |
### 地形範例
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

最佳實務：使用模組實現可重複使用性、遠端儲存狀態（S3 + DynamoDB 用於鎖定）、從不硬編碼機密以及對所有內容進行版本控制。
---

## 監控和可觀察性
### 三大支柱
|支柱|它告诉你什么 |工具|
|--------|--------------------|--------|
| **指標** |一段時間內的數值測量（CPU、請求率、錯誤率）|普羅米修斯、CloudWatch、Datadog |
| **日誌** |具有上下文的離散事件（錯誤、請求、狀態變更）| ELK Stack、Loki、CloudWatch 日誌 |
| **痕跡** |跨服務的端到端請求旅程 | Jaeger、X 光、Zipkin |
### Prometheus + Grafana 堆疊
標準開源監控堆疊：
|組件|角色 |
|------------|------|
| **普羅米修斯** |時間序列資料庫；從服務中提取指標|
| **格拉法納** |視覺化與儀表板|
| **警報管理器** |將警報路由至 Slack、PagerDuty、電子郵件 |
| **節點導出器** |公開系統層級指標（CPU、RAM、磁碟）|
| **黑盒子導出器** |探測端點（HTTP、TCP、ICMP）|
### 要追蹤的關鍵指標
|類別 |指標|
|----------|---------|
| **基礎架構** | CPU、RAM、磁碟使用情況、網路 I/O |
| **應用程式** |請求率、延遲（p50、p95、p99）、錯誤率 |
| **資料庫** |查詢計數、慢查詢、連線池使用情況 |
| **業務** |註冊量、轉換量、收入 |
---

## 部署策略
|策略|它是如何運作的 |風險|回滾 |
|----------|-------------|------|----------|
| **滾動更新** |逐步更換舊實例 |一些用戶使用舊版本，一些用戶使用新版本 |恢復到上一張圖片 |
| **藍綠** |運行兩個相同的環境；切換流量 |轉型期間基礎設施成本翻倍|即時切換回來 |
| **金絲雀** |將一小部分流量路由到新版本；逐漸增加|複雜的交通管理 |路由流量恢復穩定 |
| **功能標誌** |部署程式碼但隱藏切換後面的功能 |條件邏輯的程式碼複雜度 |關閉 |
---

## GitOps
GitOps 將 IaC 推向邏輯結論：Git 儲存庫是基礎架構和應用程式所需狀態的唯一事實來源。
|原理|說明 |
|------------|-------------|
| **聲明式** |一切都被描述為代碼（YAML、HCL）|
| **版本化** | Git 是真理之源 |
| **自動化** |工具不斷協調期望狀態與實際狀態 |
| **可審計** |每個更改都是一次 Git 提交 |
**ArgoCD** 和 **Flux** 是 Kubernetes 的領先 GitOps 工具。您將變更推送到 Git 儲存庫，該工具會自動將其部署到叢集。
---

## 事件回應
當凌晨 3 點發生故障時：
1. **確認**警報。
2. **評估範圍**：哪些服務、使用者和資料受到影響？
3. **確定**根本原因 - 檢查日誌、指標、最近的部署。
4. **如果可能的話，包含** — 斷路器、功能標誌、流量轉移。
5. **修復** — 回滾或向前打補丁。
6. **溝通** — 更新利害關係人和使用者（狀態頁面）。
7. **事後分析** — 在 24-48 小時內，記錄根本原因和行動項目。
目的不僅是解決事件，而且確保同一事件不會再次發生。