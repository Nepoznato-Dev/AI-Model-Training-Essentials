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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# 普罗米修斯和格拉法纳
Prometheus 是一个开源监控和警报工具包，旨在提高可靠性和可扩展性。 Grafana 是领先的可视化时间序列数据的开源平台。它们共同构成了现代基础设施和应用程序最流行的监控堆栈。 Prometheus 收集并存储指标； Grafana 在仪表板中显示它们。
---

## 普罗米修斯架构
|组件|描述 |
|------------|-------------|
| **普罗米修斯服务器** |从目标中抓取指标；存储时间序列数据；评估警报规则 |
| **出口商** |公开系统（Node Exporter、cAdvisor 等）的指标 |
| **推送网关** |从短期作业（批处理作业、CI）接收指标 |
| **警报管理器** |处理警报：分组、静音、路由、抑制 |
| **服务发现** |自动发现目标（Kubernetes、Consul、EC2 等）|
---

## 关键概念
|概念 |描述 |
|---------|-------------|
| **公制** |具有可选标签和值的命名测量 |
| **时间序列** |特定指标 + 标签组合的数据点流 |
| **工作** |具有相同目的的目标集合 |
| **实例** |要抓取的单个目标（通常是一个进程）|
| **刮** | Prometheus 定期从目标提取指标 |
| **标签** |确定指标维度的键值对（例如`method="GET"`）|
| **样品** |某个时间点的值：（时间戳，值）|
---

## 指标类型
|类型 |描述 |使用案例|
|------|-------------|----------|
| **柜台** |单调递增值（仅上升）|请求计数；错误；任务完成 |
| **仪表** |可升可降的价值 |温度;内存使用情况；队列长度|
| **直方图** |按价值划分的观察结果 |请求延迟；响应大小 |
| **总结** |类似于直方图；计算客户端分位数 |延迟百分位数 |
---

## PromQL（查询语言）
### 基本查询
|查询 |描述 |
|--------|-------------|
| `http_requests_total`|原始时间序列 |
| `http_requests_total{method="GET"}`|按标签过滤 |
| `http_requests_total{method="GET", status="200"}`|多标签过滤器 |
| `rate(http_requests_total[5m])`| 5 分钟内的每秒速率 |
| `increase(http_requests_total[1h])`| 1小时内总涨幅|
| `sum(rate(http_requests_total[5m])) by (status)`|按状态划分的总费率 |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`|第 95 个百分位延迟 |
| `avg(node_cpu_seconds_total{mode="idle"})`|平均 CPU 空闲时间 |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| CPU 利用率 |
### 常用函数
|功能|描述 |示例|
|----------|-------------|---------|
| `rate()`|每秒平均增长率| `rate(requests_total[5m])`|
| `irate()`|基于最后两个数据点的每秒速率 | `irate(requests_total[1m])`|
| `increase()`|随时间范围的总增长 | `increase(errors_total[1h])`|
| `sum()`|系列总和 | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`|系列平均 | `avg(node_memory_usage)`|
| `histogram_quantile()`|从直方图计算分位数 | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`|价值最高的 K 系列 | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`|线性预测 | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`|检查指标是否缺失 | `absent(up{job="myapp"})`|
---

## 常见出口商
|出口商|它监控什么 |
|----------|-----------------|
| **节点导出器** | Linux/Unix 主机指标（CPU、内存、磁盘、网络）|
| **cAdvisor** |容器指标（CPU、内存、网络、文件系统）|
| **MySQL 导出器** | MySQL 数据库指标 |
| **PostgreSQL 导出器** | PostgreSQL 数据库指标 |
| **Redis 导出器** | Redis 指标 |
| **黑盒导出器** |通过 HTTP、HTTPS、DNS、TCP、ICMP 探测端点 |
| **SNMP 导出器** |通过 SNMP 的网络设备指标 |
| **JSON 导出器** |来自 JSON API 的自定义指标 |
---

## 格拉法纳
### 关键概念
|概念 |描述 |
|---------|-------------|
| **数据来源** |连接到 Prometheus（或其他后端）|
| **仪表板** |按布局排列的面板集合 |
| **面板** |单一可视化（图形、仪表、表格、热图）|
| **变量** |仪表板的动态过滤器（例如，选择实例）|
| **注释** |在图表上标记事件（部署、事件）|
| **警报规则** | Grafana 中基于阈值的警报 |
| **模板** |带有变量的可重用仪表板模式
### 有用的仪表板模式
|图案|描述 |
|---------|-------------|
| **概览行** |关键指标一览：错误率、延迟、吞吐量 |
| **深入分析** |使用变量从摘要视图单击到详细视图 |
| **红色方法** |速率、错误、持续时间——三个关键服务指标 |
| **使用方法** |基础设施的利用率、饱和度、错误
| **黄金信号** |延迟、流量、错误、饱和度（Google 的 SRE 书籍）|
---

## 警报
### 警报规则结构
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
| **组** |将类似的警报合并到一个通知中 |
| **路线** |确定警报去向的匹配器树 |
| **接收器** |在哪里发送警报（电子邮件、Slack、PagerDuty、webhook）|
| **抑制** |当另一个警报触发时抑制警报 |
| **沉默** |通过标签匹配器暂时静音警报 |
---

## 故障排除
|问题 |解决方案 |
|---------|----------|
| **目标下调** |检查导出器是否正在运行；检查网络/防火墙；验证抓取配置 |
| **没有数据** |检查指标名称拼写；检查标签过滤器；验证时间范围 |
| **高基数** |标签组合过多；减少标签值；使用记录规则|
| **查询速度慢** |对复杂查询使用记录规则；增加刮擦间隔|
| **警报疲劳** |调整阈值；添加`for`持续时间；群组相关警报 |
| **重新启动后缺少指标** | Prometheus将数据存储在本地；检查保留设置 |
---

＃＃ 概括
Prometheus 通过定期从导出器抓取指标来监控系统。指标有四种类型：计数器（仅上升）、仪表（上升和下降）、直方图（分桶观察）和摘要（分位数）。 PromQL 是查询语言 —`rate()`、`increase()`、`histogram_quantile()`和聚合函数（`sum`、`avg`）是最常见的操作。 Grafana 通过面板、变量和注释在仪表板中可视化 Prometheus 数据。警报使用 Alertmanager 进行分组、路由、静默和抑制警报。关键的监控模式是 Google 的黄金信号（延迟、流量、错误、饱和度）和针对服务的 RED 方法（速率、错误、持续时间）以及针对基础设施的 USE 方法（利用率、饱和度、错误）。