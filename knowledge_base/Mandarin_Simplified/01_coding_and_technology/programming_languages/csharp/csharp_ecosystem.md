---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [csharp, ecosystem, tooling, dotnet, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C# — 生态系统和工具指南
本指南涵盖了 C# / .NET 生态系统中的基本工具、框架和基础设施。
---

## .NET SDK 和工具链
|工具|目的|
|------|---------|
| **dotnet CLI** |构建、运行、测试、发布 |
| **MSBuild** |底层构建引擎|
| **NuGet CLI** |包管理 |
| **dotnet 格式** |代码格式化 |
| **dotnet-ef** |实体框架工具 |
| **dotnet 已过时** |查找过时的软件包 |
| **dotnet 脚本** |运行 C# 脚本 (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## 运行时和实现
|运行时 |笔记|
|--------|--------|
| **.NET 8/9** |当前 LTS / STS，跨平台 |
| **.NET 框架** |仅适用于 Windows，旧版 (4.8.x) |
| **单声道** |开源 .NET 框架 (Xamarin) |
| **Unity（IL2CPP/Mono）** |游戏引擎运行时|
| **戈多 (.NET)** |支持 C# 的游戏引擎 |
---

## 包管理
|来源 |目的|
|--------|---------|
| **NuGet.org** |官方包注册表 |
| **dotnet 添加包** | CLI 软件包安装 |
| **封装参考** |现代 .csproj 格式 |
| **私人提要** | Azure Artifacts、GitHub 包、MyGet |
```xml
<!-- .csproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Dapper" Version="2.1.0" />
  </ItemGroup>
</Project>
```

---

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **ASP.NET 核心** |全栈网络 | API、MVC、Blazor |
| **最少的 API** |轻量化|简单的 API |
| **Blazor 服务器** |交互式用户界面 |服务器渲染的 SPA |
| **Blazor WebAssembly** |客户端|基于浏览器的 SPA |
| **gRPC** |远程过程调用 |高性能服务|
| **信号R** |实时| WebSockets，推送 |
| **OData** | REST 扩展 |可查询的API |
| **FastEndpoints** | API框架|快速、最少的样板 |
```csharp
// Minimal API example
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/hello", () => "Hello, World!");
app.MapGet("/users/{id}", async (int id, UserDb db) =>
    await db.Users.FindAsync(id) is User u ? Results.Ok(u) : Results.NotFound());

app.Run();
```

---

## 数据库和 ORM
|技术 |类型 |
|------------|------|
| **实体框架核心** |完整的 ORM、迁移 |
| **精巧** |微 ORM、原始 SQL |
| **NHibernate** |成熟的ORM |
| **FreeSql** |轻量级 ORM |
| **貂** | PostgreSQL 文档数据库 |
| **StackExchange.Redis** | Redis 客户端 |
| **MongoDB.驱动程序** | MongoDB 客户端 |
| **Npgsql** | PostgreSQL 驱动程序 |
| **MySql连接器** | MySQL 驱动程序 |
```csharp
// EF Core example
public class AppDbContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    protected override void OnConfiguring(DbContextOptionsBuilder o)
        => o.UseSqlServer("connection-string");
}

var users = await db.Users
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name)
    .ToListAsync();
```

---

## 测试
|框架|目的|
|------------|---------|
| **x单位** |最流行的测试框架 |
| **NUnit** |经典测试框架 |
| **MS测试** |微软的测试框架|
| **起订量** |模拟库 |
| **N替补** |友善的嘲笑|
| **流利的断言** |流畅的断言 |
| **应该** |可读的断言 |
| **伪造** |虚假数据生成 |
| **自动夹具** |测试数据自动化 |
| **测试容器** |基于 Docker 的集成测试 |
| **基准DotNet** |微基准测试 |
| **被单** |代码覆盖率|
```csharp
// xUnit + FluentAssertions
public class UserServiceTests
{
    [Fact]
    public async Task Should_Find_User_By_Id()
    {
        var mockRepo = Substitute.For<IUserRepository>();
        mockRepo.GetByIdAsync(1).Returns(new User("Alice"));
        var service = new UserService(mockRepo);

        var user = await service.GetByIdAsync(1);

        user.Name.Should().Be("Alice");
    }
}
```

---

## 代码质量
|工具|目的|
|------|---------|
| **Roslyn 分析仪** |内置代码分析 |
| **SonarAnalyzer.CSharp** | SonarQube 规则 |
| **风格警察** |编码风格强制 |
| **dotnet 格式** |代码格式化 |
| **编辑器配置** |跨编辑器一致性 |
| **SonarQube / SonarCloud** |代码质量平台|
| **ReSharper** | JetBrains 分析 + 重构 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **视觉工作室** |全功能 Windows IDE（社区/专业版/企业版）|
| **骑手** |跨平台 JetBrains C# IDE |
| **VS Code + C# 开发套件** |轻量级的 Microsoft 扩展 |
| **Visual Studio for Mac** |退休（使用 Rider 或 VS Code）|
---

## 关键库
|图书馆 |目的|
|---------|---------|
| **系统.Text.Json** |内置 JSON 序列化 |
| **Newtonsoft.Json** |旧版 JSON（仍然广泛使用）|
| **Serilog** |结构化日志记录 |
| **NLog** |日志框架 |
| **波莉** |弹性和重试策略|
| **MediatR** |中介模式 (CQRS) |
| **自动映射器** |对象到对象映射 |
| **FluentValidation** |验证库 |
| **公共交通** |消息总线（RabbitMQ、Azure SB）|
| **绞火** |后台作业处理 |
| **石英.NET** |作业调度|
| **幽灵.控制台** |漂亮的控制台应用程序 |
| **命令行解析器** | CLI 参数解析 |
---

## 云和 Azure 集成
|服务 |目的|
|---------|---------|
| **Azure 函数** |无服务器|
| **适用于 .NET 的 Azure SDK** |所有 Azure 服务 |
| **适用于 .NET 的 AWS 开发工具包** | AWS 服务 |
| **谷歌云.NET** | GCP 服务 |
| **Azure Cosmos DB** | NoSQL 数据库 |
| **Azure 服务总线** |消息 |
| **Azure 密钥保管库** |保密管理|
---

## 部署
|方法|笔记|
|--------|--------|
| **独立** | .NET 运行时捆绑包 |
| **依赖于框架** |需要安装.NET |
| **单文件发布** | `dotnet publish /p:PublishSingleFile=true`|
| **本机 AOT** |  `PublishAot=true`（无需 JIT）|
| **码头工人** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure 应用服务** | PaaS部署|
| **AWS Lambda** |无服务器|
| **IIS** | Windows 主机 |
| **红隼** |内置跨平台Web服务器|
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

＃＃ 概括
C# 和 .NET 提供了最高效的生态系统之一。标准堆栈是：**.NET 8+** 作为运行时，**ASP.NET Core** 用于 Web，**Entity Framework Core** 或 **Dapper** 用于数据访问，**xUnit + Moq** 用于测试，**Visual Studio** 或 **Rider** 作为 IDE，以及 **NuGet** 用于包。现代 C# 具有记录、模式匹配、可为 null 的引用类型和最少的 API，简洁且富有表现力。 **本机 AOT** 编译可实现极快的启动速度和小型二进制文件。该生态系统在企业、云（Azure）、游戏开发（Unity、Godot）和跨平台应用程序方面表现出色。