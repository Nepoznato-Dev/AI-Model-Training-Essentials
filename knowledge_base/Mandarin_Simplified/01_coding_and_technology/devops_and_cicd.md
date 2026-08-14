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
DevOps 是文化理念、实践和工具的结合，使团队能够更快、更可靠地交付软件。它打破了开发人员（想要发布更改）和运营人员（想要稳定性）之间的壁垒。 CI/CD（持续集成和持续交付）是使之成为可能的自动化支柱。
---

## CI/CD 管道
### CI/CD 的实际含义
|术语 |它有什么作用 |
|------|-------------|
| **持续集成（CI）** |开发人员经常合并代码；每次合并都会触发自动构建和测试|
| **持续交付（CD）** |代码始终处于可部署状态；发布到生产环境是一个手动决定|
| **持续部署** |通过测试的每项更改都会自动投入生产——无需手动控制 |
### 典型的管道阶段
|舞台|发生了什么 |工具|
|--------|-------------|--------|
| **来源** |开发人员将代码推送到 Git | GitHub、GitLab、Bitbucket |
| **构建** |编译代码，安装依赖 | Maven、Gradle、npm、pip |
| **测试** |运行单元、集成、lint 检查 |玩笑、pytest、JUnit |
| **套餐** |构建 Docker 镜像或工件 | Docker、构建包 |
| **部署（暂存）** |部署到暂存环境 | Kubernetes、ECS、虚拟机 |
| **测试（分期）** |集成测试、冒烟测试|硒，邮差 |
| **部署（生产）** |发布到生产环境 |蓝绿色，金丝雀，滚动|
| **监控** |观察运行状况、错误、性能 |普罗米修斯、Grafana、Datadog |
### CI/CD 工具比较
|工具|类型 |实力|
|------|------|----------|
| **GitHub 操作** |云 CI/CD |与GitHub深度集成； YAML 工作流程 |
| **亚搏体育appGitLab CI** |内置 CI/CD |回购 + 管道的单一平台 |
| **詹金斯** |自托管 CI/CD |高度可配置；庞大的插件生态系统 |
| **圆CI** |云 CI/CD |快速地;适合容器化工作流程|
| **ArgoCD** | Kubernetes 的 GitOps |声明式、Git 驱动的部署 |
---

## Docker 和容器
### 为什么选择容器？
在容器出现之前，典型的问题是“它可以在我的机器上运行”。容器通过将应用程序及其所有依赖项（库、运行时、配置）打包到一个可在任何地方相同地运行的单个便携式单元中来解决这个问题。
### Docker 基础知识
|概念 |描述 |
|---------|-------------|
| **图片** |具有应用程序+依赖项的只读模板 |
| **集装箱** |运行图像实例 |
| **Dockerfile** |构建图像的秘诀|
| **注册表** |图像存储（Docker Hub、ECR、GCR）|
| **成交量** |容器重启后仍然存在的持久存储 |
| **网络** |容器的隔离网络层|
### Dockerfile 最佳实践
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

关键实践：使用 slim/alpine 基础镜像、以非 root 身份运行、利用层缓存、使用`.dockerignore`、扫描镜像是否存在漏洞（`trivy`、`docker scan`）以及设置资源限制。
### Docker 组合
用于一起运行多个容器（应用程序+数据库+缓存）：
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
Kubernetes 是行业标准的容器编排器。它管理容器化应用程序的部署、扩展和操作。
### 核心架构
|组件|角色 |
|------------|------|
| **控制平面** |管理集群（API 服务器、调度程序、etcd、控制器管理器）|
| **节点** |运行容器的工作机器（VM 或物理）|
| **吊舱** |最小的可部署单位；一个或多个共享网络的容器|
| **服务** |将流量路由到 Pod 的稳定网络端点 |
| **部署** |所需 Pod 状态的声明式定义（副本、映像等）|
| **入口** |外部流量的HTTP路由规则|
| **配置映射/秘密** |注入 Pod 的配置和敏感数据 |
### 基本 kubectl 命令
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

### 头盔
Helm 是 Kubernetes 的包管理器。 **图表**是一组预先配置的 Kubernetes 资源。对于 K8s，可以将其视为`apt`或 `brew`。
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## 基础设施即代码 (IaC)
IaC 对待基础设施配置的方式与对待应用程序代码的方式相同：通过管道进行版本控制、测试和部署。
### Terraform 与 A​​nsible
|工具|类型 |方法|最适合 |
|------|------|----------|----------|
| **地形** |供应|声明式（HCL）；基于国家的|创建云资源（VPC、虚拟机、数据库）|
| **Ansible** |配置|声明式（YAML）；无代理 |配置服务器、安装软件|
| **普鲁米** |供应|命令式（Python、Go、TS）|更喜欢真正的编程语言的团队|
| **云形成** |供应|声明式（YAML/JSON）； AWS 原生 |仅限 AWS 的基础设施 |
### 地形示例
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

最佳实践：使用模块实现可重用性、远程存储状态（S3 + DynamoDB 用于锁定）、从不硬编码机密以及对所有内容进行版本控制。
---

## 监控和可观察性
### 三大支柱
|支柱|它告诉你什么 |工具|
|--------|--------------------|--------|
| **指标** |一段时间内的数值测量（CPU、请求率、错误率）|普罗米修斯、CloudWatch、Datadog |
| **日志** |具有上下文的离散事件（错误、请求、状态更改）| ELK Stack、Loki、CloudWatch 日志 |
| **痕迹** |跨服务的端到端请求旅程 | Jaeger、X 射线、Zipkin |
### Prometheus + Grafana 堆栈
标准开源监控堆栈：
|组件|角色 |
|------------|------|
| **普罗米修斯** |时间序列数据库；从服务中提取指标|
| **格拉法纳** |可视化和仪表板|
| **警报管理器** |将警报路由至 Slack、PagerDuty、电子邮件 |
| **节点导出器** |公开系统级指标（CPU、RAM、磁盘）|
| **黑盒导出器** |探测端点（HTTP、TCP、ICMP）|
### 要跟踪的关键指标
|类别 |指标|
|----------|---------|
| **基础设施** | CPU、RAM、磁盘使用情况、网络 I/O |
| **应用** |请求率、延迟（p50、p95、p99）、错误率 |
| **数据库** |查询计数、慢查询、连接池使用情况 |
| **业务** |注册量、转化量、收入 |
---

## 部署策略
|策略|它是如何运作的 |风险|回滚 |
|----------|-------------|------|----------|
| **滚动更新** |逐步更换旧实例 |一些用户使用旧版本，一些用户使用新版本 |恢复到上一张图片 |
| **蓝绿** |运行两个相同的环境；切换流量 |转型期间基础设施成本翻倍|即时切换回来 |
| **金丝雀** |将一小部分流量路由到新版本；逐渐增加|复杂的交通管理 |路由流量恢复稳定 |
| **功能标志** |部署代码但隐藏切换后面的功能 |条件逻辑的代码复杂性 |关闭 |
---

## GitOps
GitOps 将 IaC 推向逻辑结论：Git 存储库是基础设施和应用程序所需状态的唯一事实来源。
|原理|描述 |
|------------|-------------|
| **声明式** |一切都被描述为代码（YAML、HCL）|
| **版本化** | Git 是真理之源 |
| **自动化** |工具不断协调期望状态与实际状态 |
| **可审计** |每个更改都是一次 Git 提交 |
**ArgoCD** 和 **Flux** 是 Kubernetes 的领先 GitOps 工具。您将更改推送到 Git 存储库，该工具会自动将其部署到集群。
---

## 事件响应
当凌晨 3 点发生故障时：
1. **确认**警报。
2. **评估范围**：哪些服务、用户和数据受到影响？
3. **确定**根本原因 - 检查日志、指标、最近的部署。
4. **如果可能的话，包含** — 断路器、功能标志、流量转移。
5. **修复** — 回滚或向前打补丁。
6. **沟通**​​ — 更新利益相关者和用户（状态页面）。
7. **事后分析** — 在 24-48 小时内，记录根本原因和行动项目。
目的不仅是解决事件，而且确保同一事件不会再次发生。