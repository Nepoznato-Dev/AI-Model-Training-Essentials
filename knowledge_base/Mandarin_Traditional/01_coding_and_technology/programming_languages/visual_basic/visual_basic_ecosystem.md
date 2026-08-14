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
# Visual Basic — 生態系統與工具指南
本指南涵蓋了 Visual Basic (.NET) 生態系統中的基本工具、框架和基礎結構。
---

## Visual Basic 版本
|版本 |筆記|
|--------|--------|
| **VB.NET (Visual Basic 2022)** |目前，.NET 8+ |
| **VB6** |經典 Visual Basic（遺留）|
| **VBA** | Visual Basic 應用程式（Office） |
| **VBScript** |腳本語言（已棄用）|
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## 建置工具
|工具|目的|
|------|---------|
| **dotnet CLI** | .NET 建置、測試、發佈 |
| **MSBuild** |建置引擎 |
| **視覺工作室** |完整的IDE |
| **NuGet** |套件管理 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **ASP.NET 核心** |全端| API、MVC、Razor 頁面 |
| **最少的 API** |輕量化|簡單的 API |
| **開拓者** |網頁使用者介面 |基於元件的使用者介面 |
| **訊號R** |即時| WebSockets |
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

## 資料庫
|技術 |類型 |
|------------|------|
| **實體架構核心** |完整的 ORM |
| **精巧** |微 ORM |
| **ADO.NET** |低階資料存取 |
| **OleDb** |舊資料存取 |
| **MySql.Data** | MySQL 連接器 |
| **Npgsql** | PostgreSQL 連接器 |
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

## 測試
|框架|目的|
|------------|---------|
| **x单位** |测试框架 |
| **NUnit** |测试框架 |
| **MS测试** |微软测试框架|
| **訂購量** |嘲笑|
| **N替補** |嘲笑|
| **流暢的斷言** |流暢的斷言 |
| **基准DotNet** |基准测试 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **Roslyn 分析儀** |內建分析|
| **聲納分析儀** | SonarQube 規則 |
| **dotnet 格式** |程式碼格式化 |
| **編輯器配置** |風格一致 |
| **SonarQube** |程式碼品質平台|
---

## 桌面（WinForms / WPF）
|框架|目的|
|------------|---------|
| **WinForms** |經典 Windows 窗體 |
| **WPF** |現代 Windows UI (XAML) |
| **毛伊島** |跨平台（Xamarin 的繼承者）|
| **阿瓦隆尼亞** |類似 WPF 的跨平台 |
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **系統.Text.Json** | JSON 序列化 |
| **Newtonsoft.Json** | JSON（舊版）|
| **Serilog** |記錄 |
| **波莉** |彈性政策|
| **自動映射器** |物件映射|
| **FluentValidation** |驗證 |
| **公共交通** |訊息總線|
| **絞火** |後台工作 |
| **幽靈.控制台** |控制台使用者介面 |
---

## 辦公室自動化（VBA）
|技術 |目的|
|------------|---------|
| **Excel VBA** | Excel自動化|
| **Word VBA** |文字自動化 |
| **訪問 VBA** |門禁自動化|
| **Outlook VBA** | Outlook 自動化 |
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

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **視覺工作室** |完整的 VB.NET IDE（社群/專業版/企業版）|
| **VS 程式碼** |具有 .NET 擴充功能的輕量級 |
| **VBA 編輯器** |內建於 Office 應用程式 |
| **騎手** | JetBrains（有限的 VB 支援）|
---

## 部署
|方法|筆記|
|--------|--------|
| **獨立** | .NET 運行時捆綁包 |
| **依賴框架** |需要安裝.NET |
| **單一檔案** |`PublishSingleFile`|
| **碼頭工人** |貨櫃式|
| **MSI / ClickOnce** | Windows 安裝程式 |
| **Azure 應用程式服務** |雲端託管 |
| **IIS** | Windows 主機 |
---

＃＃ 概括
Visual Basic 的生態系統共享.NET 龐大的基礎架構。標準堆疊是：**.NET 8+** 作為運行時、**Visual Studio** 作為 IDE、**ASP.NET Core** 用於 Web、**Entity Framework Core** 或 **Dapper** 用於資料存取、**xUnit** 用於測試以及 **NuGet** 用於套件。 VB.NET 非常適合熟悉 BASIC 語法並需要存取 .NET 生態系統的開發人員。 **VBA** 對於辦公室自動化仍然至關重要 - 數百萬企業用戶依賴 Excel 和 Access 巨集。此生態系統最適合 Windows 桌面應用程式、辦公室自動化和企業業務線應用程式。