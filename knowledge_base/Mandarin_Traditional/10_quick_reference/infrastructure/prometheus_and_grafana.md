---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
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
tags: [prometheus, grafana, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 普羅米修斯與格拉法納
Prometheus 是一個開源監控和警報工具包，旨在提高可靠性和可擴展性。 Grafana 是領先的可視化時間序列資料的開源平台。它們共同構成了現代基礎設施和應用程式最受歡迎的監控堆疊。 Prometheus 收集並儲存指標； Grafana 在儀表板中顯示它們。
---

## 普羅米修斯架構
|組件|描述 |
|------------|-------------|
| **普羅米修斯伺服器** |從目標中抓取指標；儲存時間序列資料；評估警報規則 |
| **出口商** |公開系統（Node Exporter、cAdvisor 等）的指標 |
| **推送網關** |從短期作業（批次作業、CI）接收指標 |
| **警報管理器** |處理警報：分組、靜音、路由、抑制 |
| **服務發現** |自動發現目標（Kubernetes、Consul、EC2 等）|
---

## 關鍵概念
|概念 |描述 |
|---------|-------------|
| **公制** |具有可選標籤和值的命名測量 |
| **時間序列** |特定指標 + 標籤組合的資料點流 |
| **工作** |具有相同目的的目標集合 |
| **實例** |要抓取的單一目標（通常是一個行程）|
| **刮** | Prometheus 定期從目標擷取指標 |
| **標籤** |決定指標維度的鍵值對（例如`method="GET"`）|
| **樣品** |某個時間點的值：（時間戳，值）|
---

## 指標類型
|類型 |描述 |使用案例|
|------|-------------|----------|
| **柜台** |单调递增值（仅上升）|请求计数；错误；任务完成 |
| **仪表** |可升可降的价值 |温度;内存使用情况；队列长度|
| **直方图** |按价值划分的观察结果 |请求延迟；响应大小 |
| **总结** |类似于直方图；计算客户端分位数 |延迟百分位数 |
---

## PromQL（查詢語言）
### 基本查詢
|查詢 |說明 |
|--------|-------------|
|`http_requests_total`|原始時間序列 |
|`http_requests_total{method="GET"}`|按標籤過濾 |
|`http_requests_total{method="GET", status="200"}`|多標籤過濾器 |
|`rate(http_requests_total[5m])`| 5 分鐘內的每秒速率 |
|`increase(http_requests_total[1h])`| 1小時內總漲幅|
|`sum(rate(http_requests_total[5m])) by (status)`|按狀態劃分的總費率 |
|`histogram_quantile(0.95, rate(http_duration_bucket[5m]))`|第 95 個百分位延遲 |
|`avg(node_cpu_seconds_total{mode="idle"})`|平均 CPU 閒置時間 |
|`1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| CPU 使用率 |
### 常用函數
|功能|描述 |範例|
|----------|-------------|---------|
|`rate()`|每秒平均成長率|`rate(requests_total[5m])`|
|`irate()`|基於最後兩個資料點的每秒速率 |`irate(requests_total[1m])`|
|`increase()`|隨時間範圍的總成長 |`increase(errors_total[1h])`|
|`sum()`|系列總和 |`sum(rate(requests_total[5m])) by (service)`|
|`avg()`|系列平均 |`avg(node_memory_usage)`|
|`histogram_quantile()`|從直方圖計算分位數 |`histogram_quantile(0.99, rate(duration_bucket[5m]))`|
|`topk()`|價值最高的 K 系列 |`topk(5, rate(requests_total[5m]))`|
|`predict_linear()`|線性預測 |`predict_linear(disk_usage[1h], 4*3600)`|
|`absent()`|檢查指標是否缺失 |`absent(up{job="myapp"})`|
---

## 常見出口商
|出口商|它監控什麼 |
|----------|-----------------|
| **節點導出器** | Linux/Unix 主機指標（CPU、記憶體、磁碟、網路）|
| **cAdvisor** |容器指標（CPU、記憶體、網路、檔案系統）|
| **MySQL 導出器** | MySQL 資料庫指標 |
| **PostgreSQL 導出器** | PostgreSQL 資料庫指標 |
| **Redis 導出器** | Redis 指標 |
| **黑盒子導出器** |透過 HTTP、HTTPS、DNS、TCP、ICMP 偵測端點 |
| **SNMP 導出器** |透過 SNMP 的網路設備指標 |
| **JSON 導出器** |來自 JSON API 的自訂指標 |
---

## 格拉法納
### 關鍵概念
|概念 |描述 |
|---------|-------------|
| **資料來源** |連接到 Prometheus（或其他後端）|
| **儀表板** |按佈局排列的面板集合 |
| **面板** |單一視覺化（圖形、儀表、表格、熱圖）|
| **變數** |儀表板的動態篩選器（例如，選擇實例）|
| **註釋** |在圖表上標記事件（部署、事件）|
| **警報規則** | Grafana 中基於閾值的警報 |
| **範本** |具有變數的可重複使用儀表板模式
### 有用的儀表板模式
|圖案|描述 |
|---------|-------------|
| **概覽行** |關鍵指標一覽：錯誤率、延遲、吞吐量 |
| **深入分析** |使用變數從摘要視圖點選到詳細視圖 |
| **紅色方法** |速率、錯誤、持續時間－三個關鍵服務指標 |
| **使用方法** |基礎設施的使用率、飽和度、錯誤
| **黃金訊號** |延遲、流量、錯誤、飽和度（Google 的 SRE 書籍）|
---

## 警報
### 警報規則結構
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Alertmanager 路由
|概念 |描述 |
|---------|-------------|
| **群組** |將類似的警報合併到一個通知中 |
| **路線** |確定警報去向的匹配器樹 |
| **接收器** |在哪裡發送警報（電子郵件、Slack、PagerDuty、webhook）|
| **抑制** |當另一個警報觸發時抑制警報 |
| **沉默** |透過標籤匹配器暫時靜音警報 |
---

## 故障排除
|問題 |解決方案 |
|---------|----------|
| **目標下調** |檢查導出器是否正在運作；檢查網路/防火牆；驗證抓取配置 |
| **沒有資料** |檢查指標名稱拼字；檢查標籤過濾器；驗證時間範圍 |
| **高基數** |標籤組合過多；減少標籤值；使用記錄規則|
| **查詢速度慢** |對複雜查詢使用記錄規則；增加刮擦間隔|
| **警報疲勞** |調整閾值；增加`for`持續時間；群組相關警報 |
| **重新啟動後缺少指標** | Prometheus將資料儲存在本機；檢查保留設定 |
---

＃＃ 概括
Prometheus 透過定期從導出器抓取指標來監控系統。指標有四種：計數器（僅上升）、儀表（上升和下降）、直方圖（分桶觀察）和摘要（分位數）。 PromQL 是查詢語言 —`rate()`、`increase()`、`histogram_quantile()`和聚合函數（`sum`、`avg`）是最常見的操作。 Grafana 透過面板、變數和註釋在儀表板中視覺化 Prometheus 資料。警報使用 Alertmanager 進行分組、路由、靜默和抑制警報。關鍵的監控模式是 Google 的黃金訊號（延遲、流量、錯誤、飽和度）和針對服務的 RED 方法（速率、錯誤、持續時間）以及針對基礎設施的 USE 方法（利用率、飽和度、錯誤）。