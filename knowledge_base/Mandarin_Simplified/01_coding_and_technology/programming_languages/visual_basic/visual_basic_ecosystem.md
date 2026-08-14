---
# Metadata
title: "Visual Basic — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Visual Basic ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Visual Basic — 生态系统和工具指南
本指南涵盖了 Visual Basic (.NET) 生态系统中的基本工具、框架和基础结构。
---

## Visual Basic 版本
|版本 |笔记|
|--------|--------|
| **VB.NET (Visual Basic 2022)** |当前，.NET 8+ |
| **VB6** |经典 Visual Basic（遗留）|
| **VBA** | Visual Basic 应用程序（Office） |
| **VBScript** |脚本语言（已弃用）|
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## 构建工具
|工具|目的|
|------|---------|
| **dotnet CLI** | .NET 构建、测试、发布 |
| **MSBuild** |构建引擎 |
| **视觉工作室** |完整的IDE |
| **NuGet** |包管理 |
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

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **ASP.NET 核心** |全栈| API、MVC、Razor 页面 |
| **最少的 API** |轻量化|简单的 API |
| **开拓者** |网页用户界面 |基于组件的用户界面 |
| **信号R** |实时| WebSockets |
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **实体框架核心** |完整的 ORM |
| **精巧** |微 ORM |
| **ADO.NET** |低级数据访问 |
| **OleDb** |旧数据访问 |
| **MySql.Data** | MySQL 连接器 |
| **Npgsql** | PostgreSQL 连接器 |
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

## 测试
|框架|目的|
|------------|---------|
| **x单位** |测试框架 |
| **NUnit** |测试框架 |
| **MS测试** |微软测试框架|
| **起订量** |嘲笑|
| **N替补** |嘲笑|
| **流利的断言** |流畅的断言 |
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

## 代码质量
|工具|目的|
|------|---------|
| **Roslyn 分析仪** |内置分析|
| **声纳分析仪** | SonarQube 规则 |
| **dotnet 格式** |代码格式化 |
| **编辑器配置** |风格一致 |
| **SonarQube** |代码质量平台|
---

## 桌面（WinForms / WPF）
|框架|目的|
|------------|---------|
| **WinForms** |经典 Windows 窗体 |
| **WPF** |现代 Windows UI (XAML) |
| **毛伊岛** |跨平台（Xamarin 的继承者）|
| **阿瓦隆尼亚** |类似 WPF 的跨平台 |
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

## 关键库
|图书馆 |目的|
|---------|---------|
| **系统.Text.Json** | JSON 序列化 |
| **Newtonsoft.Json** | JSON（旧版）|
| **Serilog** |记录 |
| **波莉** |弹性政策|
| **自动映射器** |对象映射|
| **FluentValidation** |验证 |
| **公共交通** |消息总线|
| **绞火** |后台工作 |
| **幽灵.控制台** |控制台用户界面 |
---

## 办公自动化（VBA）
|技术 |目的|
|------------|---------|
| **Excel VBA** | Excel自动化|
| **Word VBA** |文字自动化 |
| **访问 VBA** |门禁自动化|
| **Outlook VBA** | Outlook 自动化 |
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

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **视觉工作室** |完整的 VB.NET IDE（社区/专业版/企业版）|
| **VS 代码** |具有 .NET 扩展的轻量级 |
| **VBA 编辑器** |内置于 Office 应用程序 |
| **骑手** | JetBrains（有限的 VB 支持）|
---

## 部署
|方法|笔记|
|--------|--------|
| **独立** | .NET 运行时捆绑包 |
| **依赖于框架** |需要安装.NET |
| **单文件** | `PublishSingleFile`|
| **码头工人** |集装箱式|
| **MSI / ClickOnce** | Windows 安装程序 |
| **Azure 应用服务** |云托管 |
| **IIS** | Windows 主机 |
---

＃＃ 概括
Visual Basic 的生态系统共享.NET 庞大的基础设施。标准堆栈是：**.NET 8+** 作为运行时、**Visual Studio** 作为 IDE、**ASP.NET Core** 用于 Web、**Entity Framework Core** 或 **Dapper** 用于数据访问、**xUnit** 用于测试以及 **NuGet** 用于包。 VB.NET 非常适合熟悉 BASIC 语法并需要访问 .NET 生态系统的开发人员。 **VBA** 对于办公自动化仍然至关重要 - 数百万企业用户依赖 Excel 和 Access 宏。该生态系统最适合 Windows 桌面应用程序、办公自动化和企业业务线应用程序。