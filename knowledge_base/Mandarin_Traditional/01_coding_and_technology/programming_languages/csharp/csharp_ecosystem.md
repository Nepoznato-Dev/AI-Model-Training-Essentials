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

# C# — 生態系與工具指南
本指南涵蓋了 C# / .NET 生態系統中的基本工具、框架和基礎設施。
---

## .NET SDK 和工具鏈
|工具|目的|
|------|---------|
| **dotnet CLI** |建置、運行、測試、發布 |
| **MSBuild** |底層建置引擎|
| **NuGet CLI** |套件管理 |
| **dotnet 格式** |程式碼格式化 |
| **dotnet-ef** |實體框架工具 |
| **dotnet 已過時** |尋找過時的軟體包 |
| **dotnet 腳本** |執行 C# 腳本 (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## 運行時和實現
|運行時 |筆記|
|--------|--------|
| **.NET 8/9** |目前 LTS / STS，跨平台 |
| **.NET 框架** |僅適用於 Windows，舊版 (4.8.x) |
| **單聲道** |開源 .NET 框架 (Xamarin) |
| **Unity（IL2CPP/Mono）** |遊戲引擎運行時|
| **戈多 (.NET)** |支援 C# 的遊戲引擎 |
---

## 套件管理
|來源 |目的|
|--------|---------|
| **NuGet.org** |官方包註冊表 |
| **dotnet 新增套件** | CLI 軟體包安裝 |
| **封裝參考** |現代 .csproj 格式 |
| **私人提要** | Azure Artifacts、GitHub 套件、MyGet |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **ASP.NET 核心** |全端網路 | API、MVC、Blazor |
| **最少的 API** |輕量化|簡單的 API |
| **Blazor 伺服器** |互動式使用者介面 |伺服器渲染的 SPA |
| **Blazor WebAssembly** |客戶端|基於瀏覽器的 SPA |
| **gRPC** |遠端過程呼叫 |高效能服務|
| **訊號R** |即時| WebSockets，推播 |
| **OData** | REST 擴充 |可查詢的API |
| **FastEndpoints** | API框架|快速、最少的樣板 |
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

## 資料庫和 ORM
|技術 |類型 |
|------------|------|
| **實體架構核心** |完整的 ORM、遷移 |
| **精巧** |微 ORM、原始 SQL |
| **NHibernate** |成熟的ORM |
| **FreeSql** |輕量級 ORM |
| **貂** | PostgreSQL 文檔資料庫 |
| **StackExchange.Redis** | Redis 用戶端 |
| **MongoDB.驅動程式** | MongoDB 用戶端 |
| **Npgsql** | PostgreSQL 驅動程式 |
| **MySql連接器** | MySQL 驅動程式 |
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

## 測試
|框架|目的|
|------------|---------|
| **x單位** |最受歡迎的測試框架 |
| **NUnit** |經典測試框架 |
| **MS測試** |微軟的測試框架|
| **起訂量** |模擬庫 |
| **N替補** |友善的嘲笑|
| **流暢的斷言** |流暢的斷言 |
| **應該** |可讀的斷言 |
| **偽造** |虛假資料產生 |
| **自動夾具** |測試資料自動化 |
| **測試容器** |基於 Docker 的整合測試 |
| **基準DotNet** |微基準測試 |
| **被單一** |程式碼覆蓋率|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **Roslyn 分析儀** |內建程式碼分析 |
| **SonarAnalyzer.CSharp** | SonarQube 規則 |
| **風格警察** |編碼風格強制 |
| **dotnet 格式** |程式碼格式化 |
| **編輯器配置** |跨編輯器一致性 |
| **SonarQube / SonarCloud** |程式碼品質平台|
| **ReSharper** | JetBrains 分析 + 重構 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **視覺工作室** |全功能 Windows IDE（社群/專業版/企業版）|
| **騎士** |跨平台 JetBrains C# IDE |
| **VS Code + C# 開發套件** |輕量級的 Microsoft 擴充 |
| **Visual Studio for Mac** |退休（使用 Rider 或 VS Code）|
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **系統.Text.Json** |內建 JSON 序列化 |
| **Newtonsoft.Json** |舊版 JSON（仍廣泛使用）|
| **Serilog** |結構化日誌記錄 |
| **NLog** |日誌框架 |
| **波莉** |彈性與重試策略|
| **MediatR** |中介模式 (CQRS) |
| **自動映射器** |物件到物件映射 |
| **FluentValidation** |驗證庫 |
| **公共交通** |訊息匯流排（RabbitMQ、Azure SB）|
| **絞火** |後台作業處理 |
| **石英.NET** |作業排程|
| **幽靈.控制台** |漂亮的控制台應用程式 |
| **命令列解析器** | CLI 參數解析 |
---

## 雲端和 Azure 集成
|服務 |目的|
|---------|---------|
| **Azure 函數** |無伺服器|
| **適用於 .NET 的 Azure SDK** |所有 Azure 服務 |
| **適用於 .NET 的 AWS 開發工具包** | AWS 服務 |
| **Google雲端.NET** | GCP 服務 |
| **Azure Cosmos DB** | NoSQL 資料庫 |
| **Azure 服務總線** |訊息 |
| **Azure 金鑰保管庫** |保密管理|
---

## 部署
|方法|筆記|
|--------|--------|
| **獨立** | .NET 運行時捆綁包 |
| **依賴框架** |需要安裝.NET |
| **單一文件發布** |`dotnet publish /p:PublishSingleFile=true`|
| **本機 AOT** | `PublishAot=true`（無需 JIT）|
| **碼頭工人** |`mcr.microsoft.com/dotnet/aspnet`|
| **Azure 應用程式服務** | PaaS部署|
| **AWS Lambda** |無伺服器|
| **IIS** | Windows 主機 |
| **紅隼** |內建跨平台Web伺服器|
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

＃＃ 概括
C# 和 .NET 提供了最高效的生態系統之一。標準堆疊是：**.NET 8+** 作為運行時，**ASP.NET Core** 用於 Web，**Entity Framework Core** 或 **Dapper** 用於資料訪問，**xUnit + Moq** 用於測試，**Visual Studio** 或 **Rider** 作為 IDE，以及 **NuGet** 用於套件。現代 C# 具有記錄、模式匹配、可為 null 的引用類型和最少的 API，簡潔且富有表現力。 **本機 AOT** 編譯可達到極快的啟動速度和小型二進位。該生態系統在企業、雲端（Azure）、遊戲開發（Unity、Godot）和跨平台應用程式方面表現出色。