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
# API 设计和架构
API（应用程序编程接口）是软件组件相互通信的方式。设计良好的 API 直观、一致并且使用起来很愉快。设计不当会导致混乱、错误和挫败感。该文件涵盖了构建开发人员实际想要使用的 API 的原则、模式和实践。
---

## REST API 原则
REST（表述性状态传输）是 Web API 的主要架构风格。它将数据视为由 URL 标识的**资源**，并使用 HTTP 方法对其进行操作。
### 核心原则
|原理|描述 |
|------------|-------------|
| **资源** |一切都是带有 URI 的资源 (`/users/123`,`/orders/456`) |
| **HTTP 方法** | GET（读取）、POST（创建）、PUT（替换）、PATCH（部分更新）、DELETE（删除）|
| **无国籍** |每个请求包含所需的所有信息；没有服务器端会话状态|
| **统一界面** |一致的资源命名、标准方法、标准状态码|
| **代表** |资源可以用多种格式表示（JSON、XML）|
### 资源命名约定
|做|不要 |
|----|--------|
|  `/users`（复数名词）|  `/user`（单数）|
|  `/users/123/orders`（嵌套）|  __受保护_3__ |
|  `/products?category=electronics`（用于过滤的查询参数）|  __受保护_5__ |
|使用连字符：`/user-profiles` |使用下划线：`/user_profiles` |
### HTTP 方法和幂等性
|方法|目的|幂等？ |安全的？ |
|--------|---------|-------------|--------|
| **获取** |阅读资源 | ✅ 是的 | ✅ 是的 |
| **发布** |创建资源 | ❌ 否 | ❌ 否 |
| **放置** |完全替换资源 | ✅ 是的 | ❌ 否 |
| **补丁** |部分更新资源 | ❌ 否* | ❌ 否 |
| **删除** |删除资源 | ✅ 是的 | ❌ 否 |
*通过精心设计，PATCH 可以成为幂等的。
### HTTP 状态代码
|代码|意义|何时使用 |
|------|---------|-------------|
| **200** |好的 |成功获取、放置、修补、删除 |
| **201** |创建 |成功 POST（已创建资源）|
| **204** |没有内容 |成功删除（无返回值）|
| **400** |错误的请求 |输入无效或格式错误的请求 |
| **401** |未经授权 |身份验证缺失或无效 |
| **403** |禁止 |已认证但未授权 |
| **404** |未找到 |资源不存在 |
| **409** |冲突|重复资源或状态冲突 |
| **422** |无法处理的实体 |有效的 JSON 但语义错误 |
| **429** |太多请求 |超出速率限制 |
| **500** |内部服务器错误 |意外的服务器错误 |
| **502** |错误网关 |上游服务故障 |
| **503** |服务不可用 |暂时超载或维护|
---

## API 版本控制
API 不断发展。当您需要进行重大更改时，版本控制可以让现有客户端继续工作。
|战略|示例|优点 |缺点 |
|----------|---------|------|-----|
| **URL 路径** | `/v1/users`、`/v2/users`|简单、明确 |每个版本的 URL 变化 |
| **查询参数** |  __受保护_2__ |灵活|容易忘记|
| **标题** |  __受保护_3__ |干净的网址 |不易被发现 |
| **无版本控制** |仅架构演变 |最简单|重大变化影响每个人 |
**最佳实践**：为了清晰起见，使用 URL 路径版本控制 (`/v1/`)。至少支持一个以前的版本。弃用具有明确时间表的旧版本。
---

## 验证方法
|方法|它是如何运作的 |最适合 |
|--------|-------------|----------|
| **API 密钥** |标头中的密钥 (`X-API-Key: abc123`) |服务器到服务器的简单集成 |
| **OAuth2** |具有范围的基于令牌的委托 |第三方访问、用户授权的应用程序 |
| **智威汤逊** |带有声明的独立令牌 |跨服务的无状态身份验证 |
| **基本身份验证** | Base64 编码的用户名:密码 |仅限开发 — 没有 TLS 绝不进行生产 |
| **会话cookie** |仅 HTTP cookie 中的服务器端会话 ID |传统Web应用|
### OAuth2 流程（简化）
1. 客户端将用户重定向到授权服务器。
2. 用户登录并授予权限。
3. 授权服务器返回授权码。
4. 客户端用代码交换访问令牌（以及可选的刷新令牌）。
5. 客户端使用访问令牌调用 API。
6. 当访问令牌过期时，使用刷新令牌获取新的令牌。
---

## API 风格：REST、GraphQL、gRPC
|特色 |休息 | GraphQL | gRPC |
|--------|------|---------|-----|
| **数据格式** | JSON（通常）| JSON | Protobuf（二进制）|
| **端点** |多个（每个资源一个）|单端点|由.proto文件定义 |
| **过度获取** |常见（获得超出需要的数量）|无（客户端指定字段）|无（架构定义）|
| **获取不足** |需要多次通话 |无（准确获取所需内容）|无 |
| **实时** |需要 WebSockets |内置订阅 |内置流媒体|
| **缓存** | HTTP 缓存自然而然地发挥作用 |更难缓存|有限公司|
| **学习曲线** |低|中等|中-高|
| **最适合** |公共 API、CRUD 应用程序 |复杂的用户界面、移动应用程序 |内部微服务，高性能 |
---

## 分页、过滤和排序
对于返回列表的端点：
|技术|示例|何时使用 |
|------------|---------|-------------|
| **偏移/限制** |  __受保护_0__ |简单的;适用于小型数据集 |
| **基于光标** |  __受保护_1__ |大型数据集；一致的结果 |
| **按键组** |  __受保护_2__ |非常高效；需要唯一的密钥 |
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
保护您的 API 免遭滥用并确保公平使用。
|战略|它是如何运作的 |
|----------|-------------|
| **固定窗口** |每个时间窗口 N 个请求（例如 100 个/小时）|
| **滑动窗** |更细粒度；计算滚动窗口中的请求数 |
| **令牌桶** |以固定比率添加代币；每个请求消耗一个令牌 |
返回带有标头的`429 Too Many Requests`：```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## 错误处理
一致的错误响应使 API 更易于使用：
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

**原则**：使用一致的错误结构，包括可操作的消息，使用标准 HTTP 状态代码，使用相关 ID 在服务器端记录错误，并且绝不公开堆栈跟踪或内部详细信息。
---

## API 文档
|工具|描述 |
|------|-------------|
| **OpenAPI (Swagger)** | REST API 文档的行业标准 |
| **Swagger 用户界面** | OpenAPI 规范中的交互式 API 文档 |
| **邮递员** | API 测试、文档和集合共享 |
| **重做** | OpenAPI 规范中精美的 API 参考文档 |
| **GraphQL 游乐场 / GraphiQL** |交互式 GraphQL 探索 |
**最佳实践**：首先编写 OpenAPI 规范（规范驱动开发），然后从中生成文档和客户端 SDK。
---

## API 网关模式
API 网关位于客户端和后端服务之间，提供单一入口点。
|责任|描述 |
|----------------|-------------|
| **路由** |将请求直接发送到适当的后端服务 |
| **身份验证** |在网关级别验证令牌 |
| **速率限制** |应用全局或每个客户端限制 |
| **转型** |协议之间转换 (REST ↔ gRPC) |
| **缓存** |缓存常见响应 |
| **监控** |集中式日志记录和指标 |
| **负载平衡** |跨服务实例分配流量 |
|工具|类型 |
|------|------|
| **孔** |开源API网关（基于Nginx）|
| **AWS API 网关** |完全托管，与 AWS 集成 |
| **Azure API 管理** |带有开发者门户的托管网关 |
| **特使/Istio** |具有API网关功能的服务网格|
| **Traefik** |自动发现、Let's Encrypt 集成 |
---

## 网络钩子
Webhooks 让您的 API 将事件实时推送到客户端，而不是让客户端轮询更改。
|方面|最佳实践|
|--------|--------------|
| **交货** |将带有 JSON 负载的 POST 请求发送到客户端的 URL |
| **安全** |使用 HMAC 对有效负载进行签名；客户验证签名|
| **可靠性** |使用指数退避重试失败的交付 |
| **幂等性** |包含唯一的事件 ID；客户端处理重复项 |
| **版本控制** |在 webhook 负载中包含 API 版本 |
---

## 设计清单
- [ ] 资源是复数名词（`/users`，而不是`/getUser`）
- [ ] 正确使用 HTTP 方法（GET 用于读取，POST 用于创建等）
- [ ] 一致的错误响应格式
- [ ] 所有列表端点的分页
- [ ] 具有清晰标头的速率限制
- [ ] 定义 API 版本控制策略
- [ ] 身份验证和授权到位
- [ ] 所有端点上的输入验证
- [ ] OpenAPI/Swagger 文档已维护
- [ ] CORS 配置正确
- [ ] 在生产中强制执行 HTTPS
- [ ] 需要时用于 POST 操作的幂等密钥