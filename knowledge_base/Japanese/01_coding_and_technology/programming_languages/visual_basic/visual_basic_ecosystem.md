<!--
---
# Metadata
title: "Visual Basic — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Visual Basic ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [visual-basic, vbnet, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Visual Basic — エコシステムとツールのガイド
このガイドでは、Visual Basic (.NET) エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## Visual Basic のバージョン
|バージョン |メモ |
|----------|----------|
| **VB.NET (Visual Basic 2022)** |現在、.NET 8+ |
| **VB6** |クラシック Visual Basic (レガシー) |
| **VBA** | Visual Basic for Applications (Office) |
| **VBScript** |スクリプト言語 (非推奨) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## ビルドツール
|ツール |目的 |
|-----|----------|
| **ドットネット CLI** | .NET のビルド、テスト、公開 |
| **MSBuild** |ビルドエンジン |
| **ビジュアルスタジオ** |完全な IDE |
| **NuGet** |パッケージ管理 |
```xml
<!-- .vbproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <RootNamespace>MyApp</RootNamespace>
    <TargetFramework>net8.0</TargetFramework>
    <OptionStrict>On</OptionStrict>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  </ItemGroup>
</Project>
```

---

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **ASP.NET コア** |フルスタック | API、MVC、Razor ページ |
| **最小限の API** |軽量 |シンプルな API |
| **ブレザー** |ウェブUI |コンポーネントベースの UI |
| **シグナルR** |リアルタイム |ウェブソケット |
```vb
' ASP.NET Core Minimal API
Imports Microsoft.AspNetCore.Builder
Imports Microsoft.Extensions.DependencyInjection

Dim builder = WebApplication.CreateBuilder(args)
Dim app = builder.Build()

app.MapGet("/hello", Function() "Hello, World!")

app.MapGet("/users/{id}", Async Function(id As Integer)
    Dim user = Await UserService.FindById(id)
    If user Is Nothing Then
        Return Results.NotFound()
    End If
    Return Results.Ok(user)
End Function)

app.Run()
```

---

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **Entity Framework コア** |完全な ORM |
| **粋な** |マイクロORM |
| **ADO.NET** |低レベルのデータアクセス |
| **OleDb** |レガシー データ アクセス |
| **MySQL.Data** | MySQL コネクタ |
| **Npgsql** | PostgreSQL コネクタ |
```vb
' Dapper example
Imports Dapper
Imports System.Data.SqlClient

Using conn As New SqlConnection("connection-string")
    Dim users = Await conn.QueryAsync(Of User)(
        "SELECT Id, Name, Email FROM Users WHERE Age > @Age",
        New With {.Age = 18}
    )
    For Each user In users
        Console.WriteLine($"{user.Name} ({user.Email})")
    Next
End Using
```

---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **xユニット** |テストフレームワーク |
| **NUnit** |テストフレームワーク |
| **MSTest** | Microsoft テスト フレームワーク |
| **モク** |嘲笑 |
| **N代理** |嘲笑 |
| **FluentAssertions** |流暢な主張 |
| **BenchmarkDotNet** |ベンチマーク |
```vb
' xUnit test
Imports Xunit
Imports NSubstitute

Public Class UserServiceTests
    <Fact>
    Public Async Function FindUser_ReturnsUser() As Task
        ' Arrange
        Dim repo = Substitute.For(Of IUserRepository)()
        repo.GetByIdAsync(1).Returns(New User("Alice"))
        Dim service = New UserService(repo)

        ' Act
        Dim user = Await service.FindByIdAsync(1)

        ' Assert
        Assert.Equal("Alice", user.Name)
    End Function
End Class
```

---

## コードの品質
|ツール |目的 |
|-----|----------|
| **Roslyn アナライザー** |組み込みの分析 |
| **ソナーアナライザー** | SonarQube ルール |
| **ドットネット形式** |コードのフォーマット |
| **EditorConfig** |一貫したスタイル |
| **ソナークベ** |コード品質プラットフォーム |
---

## デスクトップ (WinForms / WPF)
|フレームワーク |目的 |
|----------|----------|
| **WinForms** |クラシック Windows フォーム |
| **WPF** |最新の Windows UI (XAML) |
| **マウイ島** |クロスプラットフォーム (Xamarin の後継) |
| **アバロニア** |クロスプラットフォーム WPF のような |
```vb
' WinForms example
Public Class MainForm
    Inherits Form

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim name = TextBox1.Text
        MessageBox.Show($"Hello, {name}!", "Greeting")
    End Sub
End Class
```

---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **System.Text.Json** | JSON シリアル化 |
| **Newtonsoft.Json** | JSON (レガシー) |
| **セリログ** |ロギング |
| **ポリー** |回復力ポリシー |
| **オートマッパー** |オブジェクトマッピング |
| **FluentValidation** |検証 |
| **公共交通機関** |メッセージバス |
| **ハングファイア** |バックグラウンドジョブ |
| **スペクターコンソール** |コンソール UI |
---

## オフィス オートメーション (VBA)
|テクノロジー |目的 |
|-----------|-----------|
| **エクセル VBA** | Excel オートメーション |
| **Word VBA** |ワードオートメーション |
| **VBA にアクセス** |アクセスの自動化 |
| **Outlook VBA** | Outlook の自動化 |
```vb
' Excel VBA example
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")
    
    ws.Range("A1:D1").Font.Bold = True
    ws.Range("A1:D1").Interior.Color = RGB(0, 112, 192)
    
    ws.Columns("A:D").AutoFit
    
    MsgBox "Report formatted successfully!"
End Sub
```

---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **ビジュアルスタジオ** |完全な VB.NET IDE (コミュニティ/プロ/エンタープライズ) |
| **VS コード** | .NET 拡張機能を備えた軽量 |
| **VBA エディタ** | Office アプリに組み込まれている |
| **ライダー** | JetBrains (限定的な VB サポート) |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **自己完結型** | .NET ランタイムのバンドル |
| **フレームワークに依存** | .NET がインストールされている必要があります |
| **単一ファイル** | `PublishSingleFile`|
| **ドッカー** |コンテナ化 |
| **MSI / ClickOnce** | Windows インストーラー |
| **Azure App Service** |クラウドホスティング |
| **IIS** | Windows ホスティング |
---

＃＃ まとめ
Visual Basic のエコシステムは、.NET の広大なインフラストラクチャを共有しています。標準スタックは、ランタイムとして **.NET 8+**、IDE として **Visual Studio**、Web 用に **ASP.NET Core**、データ アクセス用に **Entity Framework Core** または **Dapper**、テスト用に **xUnit**、パッケージ用に **NuGet** です。 VB.NET は、.NET エコシステムにアクセスする必要がある BASIC 構文に慣れている開発者にとって理想的です。 **VBA** は依然として Office オートメーションにとって不可欠であり、何百万ものビジネス ユーザーが Excel および Access マクロに依存しています。このエコシステムは、Windows デスクトップ アプリケーション、オフィス オートメーション、およびエンタープライズ基幹業務アプリケーションに最適です。