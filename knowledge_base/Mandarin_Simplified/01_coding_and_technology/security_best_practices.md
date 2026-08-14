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
# 安全最佳实践
保护应用程序、基础设施和数据（从开发到生产）的实用指南。
---

## OWASP 前 10 名 (2021) — 概述
1. **访问控制被破坏**：用户可以访问他们不应该访问的资源。
2. **加密失败**：加密较弱或缺失。
3. **注入**：SQL、NoSQL、操作系统命令或 LDAP 注入。
4. **不安全的设计**：架构缺陷。
5. **安全配置错误**：默认密码、开放端口、详细错误。
6. **易受攻击和过时的组件**：依赖项中的已知 CVE。
7. **身份和验证失败**：密码弱、会话管理不善。
8. **软件和数据完整性故障**：供应链攻击、未签名的更新。
9. **安全日志记录和监控失败**：未检测到违规行为。
10. **服务器端请求伪造 (SSRF)**：滥用服​​务器向内部系统发出请求。
---

## 输入验证和输出编码
### 验证规则
- **白名单>黑名单**：定义允许的模式（例如电子邮件的正则表达式）而不是阻止已知的不良模式。
- **长度限制**：强制执行最大长度以防止缓冲区溢出和 DoS。
- **类型检查**：确保整数是整数，布尔值是布尔值。
- **使用经过良好测试的库**：对于电子邮件、URL 和日期验证，请使用标准库（例如，Python 中的 `email-validator`、Node 中的 `validator.js`）。
### 输出编码
- **HTML 编码**：编码`<`、`>`、`&`、`"`、`'`以防止 XSS。
- **SQL 参数化**：切勿将用户输入连接到 SQL 查询中。使用参数化查询（准备好的语句）或 ORM。
- **Shell 转义**：避免从用户输入构建 shell 命令；如果不可避免，请使用`shlex.quote()`或类似的。
---

## 身份验证和授权
### 密码管理
- **散列**：使用强而慢的散列算法存储密码：**Argon2id**（首选）、**bcrypt**、**scrypt** 或 **PBKDF2**。
- **加盐**：添加独特的每用户盐。
- **最小长度**：强制至少 12–16 个字符。
- **MFA（多重身份验证）**：敏感操作需要第二个因素（TOTP、SMS、硬件密钥）。
- **速率限制**：防止登录端点上的暴力尝试（例如，每个 IP/用户每 5 分钟 5 次尝试）。
### 会话管理
- 使用安全、仅限 HTTP、SameSite cookie 作为会话令牌。
- 设置适当的到期时间。
- 注销和更改密码时会话无效。
- 避免在 URL 中暴露会话 ID。
### OAuth2 / OIDC
- 使用成熟的库（例如 Authlib、PyJWT、Passport.js、Spring Security）。
- 彻底验证 ID 令牌（签名、发行者、受众、过期）。
- 使用状态参数来防止CSRF。
- 保守客户秘密。
### JWT（JSON Web 令牌）
- **签名**：使用RS256或ES256（非对称）以获得更好的安全性；如果共享密钥管理得当，HS256（对称）是可以接受的。
- **验证**：始终验证签名、颁发者 (`iss`)、受众 (`aud`) 和过期 (`exp`)。
- **保持较短的有效期**：访问令牌为 15-60 分钟；对于较长的会话使用刷新令牌。
- **安全存储**：切勿将 JWT 存储在 localStorage 中（容易受到 XSS 攻击）；请改用仅 HTTP 的 cookie。
---

## API 安全
### 身份验证
- 始终对 API 调用进行身份验证（公共端点除外）。
- 优先使用 API 密钥或 OAuth2 令牌而不是基本身份验证（基本身份验证在每个请求上发送凭据）。
### 速率限制和节流
- 应用每个用户和每个 IP 的速率限制以防止滥用和 DoS。
- 返回带有`Retry-After`标头的 `429 Too Many Requests`。
### CORS（跨源资源共享）
- 仅允许特定来源（生产中绝不允许 `*`）。
- 在服务器端验证`Origin`标头。
### 输入验证
- 验证所有请求参数，包括标头和正文。
- 拒绝意外字段（JSON 架构中的`"strict": true`或 `additionalProperties: false`）。
### HTTPS / TLS
- 在生产中强制执行 HTTPS。
- 使用 HSTS（HTTP 严格传输安全）强制浏览器使用 HTTPS。
- 使用 TLS 1.2 或 1.3（禁用 TLS 1.0/1.1）。
---

## 秘密管理
### 永远不要对秘密进行硬编码
- 不要将机密（API 密钥、密码、数据库 URL）提交给源代码管理。
- 使用环境变量或秘密管理工具。
＃＃＃ 工具
|工具|描述 |
|------|-------------|
| **HashiCorp 金库** |企业级动态机密 |
| **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager** |云原生 |
| **标准操作规程** |加密文件中的机密并提交它们（使用 KMS 或 GPG） |
| **Docker 的秘密** |对于群体模式； Kubernetes 机密（考虑外部 Secrets Store CSI 驱动程序）|
### 旋转
- 定期轮换机密和服务帐户。
- 尽可能自动轮换。
---

## 依赖管理
### 漏洞扫描
|语言/平台 |工具|
|--------------------|--------|
| **Python** |  `safety`、`pip-audit`、`bandit` |
| **节点** |  `npm audit`、`yarn audit`、`snyk` |
| **生锈** | `cargo audit`|
| **去** | `govulncheck`|
| **一般** | `Dependabot`(GitHub)、`Renovate`、`Trivy` |
### 修补
- 保持依赖项更新到已修补的版本。
- 为次要/补丁更新设置自动拉取请求。
- 查看变更日志以了解重大变更。
### 供应链完整性
- 使用包锁定文件（`package-lock.json`、`Cargo.lock`、`go.sum`）来确保可重现的构建。
- 验证下载的依赖项的校验和。
- 更喜欢官方注册并仅信任经过验证的发布商。
---

## 基础设施安全
### 防火墙
- 阻止除明确需要的端口（例如 80、443）之外的所有入站端口。
- 将 SSH 访问限制为特定 IP 范围（或使用 VPN/堡垒主机）。
- 使用安全组 (AWS) 或 NSG (Azure) 进行细粒度控制。
### 操作系统强化
- 定期应用安全更新（`sudo apt upgrade`、`yum update`）。
- 禁用不必要的服务和默认帐户。
- 使用fail2ban 阻止 SSH 上的暴力尝试。
- 强化 SSH：禁用 root 登录、使用基于密钥的身份验证、更改默认端口（可选）。
### 网络分段
- 将数据库和缓存放置在无法访问互联网的私有子网中。
- 使用 DMZ 提供面向公众的服务。
- 对网络访问应用最小权限原则。
### 基础设施中的秘密
- 除非加密，否则切勿将机密存储在 CI/CD 环境变量中。
- 对 EC2/VM 实例使用云提供商的 IAM 角色，而不是长期密钥。
---

## 日志记录和监控
### 记录什么
- 身份验证事件（成功/失败）。
- 访问控制决策（授权失败）。
- 管理操作（用户创建、删除、权限更改）。
- 数据库架构更改。
- 系统错误和异常。
- API 请求和响应（编辑敏感数据）。
### 不记录什么
- 密码、秘密、令牌、PII（个人身份信息），除非经过散列/编辑。
- 完整的信用卡号码。
### 警报
- 设置警报：
  - 多次登录失败（潜在的暴力破解）。
  - 不寻常的访问模式（例如，从新地点、在奇怪的时间）。
  - 创建新的管理员帐户。
  - 高错误率或延迟峰值。
- 使用 SIEM（安全信息和事件管理）进行高级关联。
### 日志保留
- 根据监管要求，将日志保留至少 30-90 天。
- 将日志存储在集中式防篡改系统中（例如 ELK Stack、Splunk、Datadog）。
---

## 安全开发生命周期 (SDL)
1. **培训**：确保开发人员了解常见漏洞。
2. **威胁建模**：在设计初期识别潜在威胁。
3. **安全编码标准**：通过检查和代码审查清单强制执行。
4. **SAST**（静态应用程序安全测试）：扫描源代码中的漏洞（SonarQube、CodeQL）。
5. **DAST**（动态应用程序安全测试）：扫描正在运行的应用程序（OWASP ZAP、Burp Suite）。
6. **SCA**（软件构成分析）：扫描依赖关系。
7. **渗透测试**：定期进行道德黑客攻击练习。
8. **错误赏金**：鼓励外部研究人员负责任地发现漏洞。
9. **事件响应计划**：针对检测到违规行为制定明确的计划。
---

## 紧急检查表（怀疑存在违规时）
1. **不要惊慌**——但要迅速采取行动。
2. **隔离**受影响的系统（如果需要，请断开网络连接）。
3. **保留证据**：捕获日志、内存转储和磁盘映像。
4. **确定**范围：哪些系统、哪些数据。
5. **轮换**所有泄露的凭证和机密。
6. **修补**漏洞。
7. 如果需要，**通知**受影响的用户和监管机构（在法定期限内）。
8. **进行事后分析**以了解根本原因并改进流程。