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
# ویژوال بیسیک - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم ویژوال بیسیک (.NET) را پوشش می‌دهد.
---

## نسخه های ویژوال بیسیک
| نسخه | یادداشت ها |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | فعلی، دات نت 8+ |
| **VB6** | کلاسیک ویژوال بیسیک (میراث) |
| **VBA** | Visual Basic for Applications (Office) |
| **VBScript** | زبان اسکریپت (منسوخ شده) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## ابزارهای ساخت
| ابزار | هدف |
|------|---------|
| **dotnet CLI** | .NET ساخت، تست، انتشار |
| **MSBuild** | ساخت موتور |
| **ویژوال استودیو** | IDE کامل |
| **NuGet** | مدیریت پکیج |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **ASP.NET Core** | تمام پشته | APIs، MVC، Razor Pages |
| **حداقل API** | سبک | API های ساده |
| **بلازور** | رابط کاربری وب | UI مبتنی بر مؤلفه |
| **SignalR** | زمان واقعی | WebSockets |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| ** هسته چارچوب نهاد ** | ORM کامل |
| **دپر** | Micro-ORM |
| **ADO.NET** | دسترسی به داده های سطح پایین |
| **OleDb** | دسترسی به داده های قدیمی |
| **MySql.Data** | رابط MySQL |
| **Npgsql** | کانکتور PostgreSQL |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **xUnit** | چارچوب تست |
| **NUnit** | چارچوب تست |
| **MSTest** | چارچوب تست مایکروسافت |
| **موق** | تمسخر |
| **NS جایگزین ** | تمسخر |
| **FluentAssertions** | ادعاهای روان |
| **BenchmarkDotNet** | محک زدن |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **آنالایزر Roslyn** | تحلیل داخلی |
| **SonarAnalyzer** | قوانین SonarQube |
| **دات نت-فرمت** | قالب بندی کد |
| **EditorConfig** | سبک منسجم |
| **SonarQube** | پلت فرم کیفیت کد |
---

## رومیزی (WinForms / WPF)
| چارچوب | هدف |
|-----------|---------|
| **WinForms** | فرم های کلاسیک ویندوز |
| **WPF** | رابط کاربری مدرن ویندوز (XAML) |
| **MAUI** | کراس پلتفرم (جانشین Xamarin) |
| **آوالونیا** | کراس پلتفرم WPF مانند |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **System.Text.Json** | سریال سازی JSON |
| **Newtonsoft.Json** | JSON (میراث) |
| **Serilog** | ورود به سیستم |
| **پولی** | سیاست های تاب آوری |
| **AutoMapper** | نقشه برداری شی |
| **FluentValidation** | اعتبار سنجی |
| **MassTransit** | اتوبوس پیام |
| **آتش آتش** | مشاغل پیشینه |
| **Spectre.Console** | رابط کاربری کنسول |
---

## اتوماسیون اداری (VBA)
| فناوری | هدف |
|------------|---------|
| **اکسل VBA** | اتوماسیون اکسل |
| **ورد VBA** | اتوماسیون ورد |
| **دسترسی به VBA** | اتوماسیون دسترسی |
| **Outlook VBA** | اتوماسیون چشم انداز |
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

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **ویژوال استودیو** | IDE کامل VB.NET (Community/Pro/Enterprise) |
| ** کد VS ** | سبک با پسوند دات نت |
| **ویرایشگر VBA** | تعبیه شده در برنامه های آفیس |
| **سوار** | JetBrains (پشتیبانی محدود VB) |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **خودکفا** | باندل زمان اجرا دات نت |
| **وابسته به چارچوب** | نیاز به نصب دات نت |
| **تک فایل** | `PublishSingleFile`|
| **داکر** | کانتینری |
| **MSI / ClickOnce** | نصب کننده ویندوز |
| **سرویس اپلیکیشن آژور** | هاست ابری |
| **IIS** | هاست ویندوز |
---

## خلاصه
اکوسیستم ویژوال بیسیک زیرساخت گسترده دات نت را به اشتراک می گذارد. پشته استاندارد عبارتند از: **.NET 8+** به عنوان زمان اجرا، **Visual Studio** به عنوان IDE، **ASP.NET Core** برای وب، **Entity Framework Core** یا **Dapper** برای دسترسی به داده، **xUnit** برای آزمایش، و **NuGet** برای بسته ها. VB.NET برای توسعه دهندگانی که از نحو BASIC راحت هستند و نیاز به دسترسی به اکوسیستم دات نت دارند ایده آل است. **VBA** برای اتوماسیون آفیس ضروری است - میلیون ها کاربر تجاری به ماکروهای Excel و Access متکی هستند. این اکوسیستم برای برنامه‌های دسکتاپ ویندوز، اتوماسیون آفیس و برنامه‌های کاربردی شرکتی مناسب است.