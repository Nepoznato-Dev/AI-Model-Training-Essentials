<!--
---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# C# — エコシステムとツールのガイド
このガイドでは、C# / .NET エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## .NET SDK とツールチェーン
|ツール |目的 |
|-----|----------|
| **ドットネット CLI** |ビルド、実行、テスト、公開 |
| **MSBuild** |基礎となるビルド エンジン |
| **NuGet CLI** |パッケージ管理 |
| **ドットネット形式** |コードのフォーマット |
| **dotnet-ef** | Entity Framework ツール |
| **ドットネットが古い** |古いパッケージを見つける |
| **ドットネットスクリプト** | C# スクリプト (.csx) を実行する |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## ランタイムと実装
|ランタイム |メモ |
|----------|----------|
| **.NET 8/9** |現在の LTS / STS、クロスプラットフォーム |
| **.NET フレームワーク** | Windows のみ、レガシー (4.8.x) |
| **モノラル** |オープンソースの .NET Framework (Xamarin) |
| **Unity (IL2CPP/モノラル)** |ゲーム エンジン ランタイム |
| **Godot (.NET)** | C# をサポートするゲーム エンジン |
---

## パッケージ管理
|出典 |目的 |
|--------|--------|
| **NuGet.org** |公式パッケージレジストリ |
| **dotnet 追加パッケージ** | CLI パッケージのインストール |
| **パッケージ参照** |最新の .csproj 形式 |
| **プライベート フィード** | Azure アーティファクト、GitHub パッケージ、MyGet |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **ASP.NET コア** |フルスタックウェブ | API、MVC、Blazor |
| **最小限の API** |軽量 |シンプルな API |
| **Blazor サーバー** |インタラクティブ UI |サーバーレンダリングされた SPA |
| **Blazor WebAssembly** |クライアント側 |ブラウザベースの SPA |
| **gRPC** | RPC |高性能サービス |
| **シグナルR** |リアルタイム | WebSocket、プッシュ |
| **OData** | REST 拡張機能 |クエリ可能な API |
| **高速エンドポイント** | API フレームワーク |高速かつ最小限の定型文 |
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

## データベースと ORM
|テクノロジー |タイプ |
|-----------|------|
| **Entity Framework コア** |完全な ORM、移行 |
| **粋な** |マイクロ ORM、生の SQL |
| **NHibernate** |成熟した ORM |
| **フリーSQL** |軽量 ORM |
| **マーテン** | PostgreSQLドキュメントDB |
| **StackExchange.Redis** | Redis クライアント |
| **MongoDB.ドライバー** | MongoDB クライアント |
| **Npgsql** | PostgreSQLドライバー |
| **MySqlConnector** | MySQLドライバー |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **xユニット** |最も人気のあるテスト フレームワーク |
| **NUnit** |古典的なテスト フレームワーク |
| **MSTest** | Microsoft のテスト フレームワーク |
| **モク** |モッキングライブラリ |
| **N代理** |フレンドリーな嘲笑 |
| **FluentAssertions** |流暢な主張 |
| **そうあるべき** |読みやすいアサーション |
| **インチキ** |偽のデータの生成 |
| **オートフィクスチャ** |テストデータの自動化 |
| **テストコンテナ** | Docker ベースの統合テスト |
| **BenchmarkDotNet** |マイクロベンチマーク |
| **カバーレット** |コードカバレッジ |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **Roslyn アナライザー** |組み込みコード分析 |
| **SonarAnalyzer.CSharp** | SonarQube ルール |
| **スタイルコップ** |コーディングスタイルの強制 |
| **ドットネット形式** |コードのフォーマット |
| **EditorConfig** |エディタ間の一貫性 |
| **SonarQube / SonarCloud** |コード品質プラットフォーム |
| **ReSharper** | JetBrains 分析 + リファクタリング |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **ビジュアルスタジオ** |フル機能の Windows IDE (コミュニティ/プロ/エンタープライズ) |
| **ライダー** |クロスプラットフォーム JetBrains C# IDE |
| **VS コード + C# 開発キット** |軽量の Microsoft 拡張機能 |
| **Visual Studio for Mac** |引退した場合 (Rider または VS Code を使用) |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **System.Text.Json** |組み込みの JSON シリアル化 |
| **Newtonsoft.Json** |レガシー JSON (現在でも広く使用されています) |
| **セリログ** |構造化されたログ |
| **NLog** |ロギングフレームワーク |
| **ポリー** |回復力と再試行ポリシー |
| **メディアR** |メディエーター パターン (CQRS) |
| **オートマッパー** |オブジェクト間のマッピング |
| **FluentValidation** |検証ライブラリ |
| **公共交通機関** |メッセージ バス (RabbitMQ、Azure SB) |
| **ハングファイア** |バックグラウンドジョブ処理 |
| **Quartz.NET** |ジョブのスケジュール設定 |
| **スペクターコンソール** |美しいコンソール アプリ |
| **CommandLineParser** | CLI 引数の解析 |
---

## クラウドと Azure の統合
|サービス |目的 |
|----------|----------|
| **Azure 関数** |サーバーレス |
| **Azure SDK for .NET** |すべての Azure サービス |
| **AWS SDK for .NET** | AWS のサービス |
| **Google Cloud .NET** | GCP サービス |
| **Azure Cosmos DB** | NoSQLデータベース |
| **Azure サービス バス** |メッセージ |
| **Azure Key Vault** |秘密管理 |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **自己完結型** | .NET ランタイムのバンドル |
| **フレームワークに依存** | .NET がインストールされている必要があります |
| **単一ファイルのパブリッシュ** | `dotnet publish /p:PublishSingleFile=true`|
| **ネイティブ AOT** | `PublishAot=true`(JIT は必要ありません) |
| **ドッカー** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure App Service** | PaaS 導入 |
| **AWS Lambda** |サーバーレス |
| **IIS** | Windows ホスティング |
| **ケストレル** |組み込みのクロスプラットフォーム Web サーバー |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

＃＃ まとめ
C# と .NET は、最も生産的なエコシステムの 1 つを提供します。標準スタックは次のとおりです。ランタイムとして **.NET 8+**、Web として **ASP.NET Core**、データ アクセスとして **Entity Framework Core** または **Dapper**、テスト用として **xUnit + Moq**、IDE として **Visual Studio** または **Rider**、パッケージとして **NuGet**。レコード、パターン マッチング、Null 許容参照型、最小限の API を備えた最新の C# は、簡潔で表現力豊かです。 **ネイティブ AOT** コンパイルにより、非常に高速な起動と小さなバイナリが可能になります。このエコシステムは、エンタープライズ、クラウド (Azure)、ゲーム開発 (Unity、Godot)、およびクロスプラットフォーム アプリケーションに優れています。