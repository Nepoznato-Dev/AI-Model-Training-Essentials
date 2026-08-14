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
# بصری بنیادی — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ Visual Basic (.NET) ایکو سسٹم میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## بصری بنیادی ورژن
| ورژن | نوٹس |
|---------|---------|
| **VB.NET (Visual Basic 2022)** | موجودہ، .NET 8+ |
| **VB6** | کلاسیکی بصری بنیادی (وراثت) |
| **VBA** | بصری بنیادی برائے درخواستیں (آفس) |
| **VBScript** | اسکرپٹ کی زبان (فرسودہ) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## ٹولز بنائیں
| ٹول | مقصد |
|------|---------|
| **ڈاٹ نیٹ CLI** | .NET کی تعمیر، جانچ، شائع |
| **MSBuild** | انجن بنائیں |
| **بصری اسٹوڈیو** | مکمل IDE |
| **NuGet** | پیکیج مینجمنٹ |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **ASP.NET کور** | مکمل اسٹیک | APIs, MVC, Razor Pages |
| **کم سے کم APIs** | ہلکا پھلکا | سادہ APIs |
| **بلیزر** | ویب UI | اجزاء پر مبنی UI |
| **سگنل آر** | ریئل ٹائم | ویب ساکٹس |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **اینٹیٹی فریم ورک کور** | مکمل ORM |
| **ڈیپر** | مائیکرو-ORM |
| **ADO.NET** | کم سطح کے ڈیٹا تک رسائی |
| **OleDb** | میراثی ڈیٹا تک رسائی |
| **MySql.Data** | MySQL کنیکٹر |
| **Npgsql** | PostgreSQL کنیکٹر |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **xUnit** | ٹیسٹ فریم ورک |
| **NUnit** | ٹیسٹ فریم ورک |
| **MSTest** | مائیکروسافٹ ٹیسٹ فریم ورک |
| **Moq** | طنز |
| **این ایس متبادل** | طنز |
| **روانی بیانات** | روانی کے دعوے |
| **بینچ مارک ڈاٹ نیٹ** | بینچ مارکنگ |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **روزلن تجزیہ کار** | بلٹ ان تجزیہ |
| **سونار اینالائزر** | سونار کیوب کے قواعد |
| **ڈاٹ نیٹ فارمیٹ** | کوڈ فارمیٹنگ |
| **EditorConfig** | مستقل انداز |
| **سونار کیوب** | کوڈ کوالٹی پلیٹ فارم |
---

## ڈیسک ٹاپ (WinForms / WPF)
| فریم ورک | مقصد |
|------------|---------|
| **WinForms** | کلاسک ونڈوز فارمز |
| **WPF** | جدید ونڈوز UI (XAML) |
| **MAUI** | کراس پلیٹ فارم (زامارین کا جانشین) |
| **ایولونیا** | کراس پلیٹ فارم WPF کی طرح |
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

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **System.Text.Json** | JSON سیریلائزیشن |
| **Newtonsoft.Json** | JSON (وراثت) |
| **سیریلوگ** | لاگنگ |
| **پولی** | لچک کی پالیسیاں |
| **آٹو میپر** | آبجیکٹ میپنگ |
| **روانی توثیق** | توثیق |
| **ماس ٹرانزٹ** | پیغام بس |
| **ہنگ فائر** | پس منظر کی نوکریاں |
| **Sspectre.Console** | کنسول UI |
---

## آفس آٹومیشن (VBA)
| ٹیکنالوجی | مقصد |
|------------|---------|
| **Excel VBA** | ایکسل آٹومیشن |
| **لفظ VBA** | لفظ آٹومیشن |
| **VBA تک رسائی حاصل کریں** | رسائی آٹومیشن |
| **Outlook VBA** | آؤٹ لک آٹومیشن |
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

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **بصری اسٹوڈیو** | مکمل VB.NET IDE (کمیونٹی/پرو/انٹرپرائز) |
| ** VS کوڈ** | .NET ایکسٹینشن کے ساتھ ہلکا پھلکا |
| **VBA ایڈیٹر** | آفس ایپس میں بنایا گیا |
| **سوار** | JetBrains (محدود VB سپورٹ) |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **خود موجود** | بنڈلز .NET رن ٹائم |
| **فریم ورک پر منحصر** | .NET انسٹال کی ضرورت ہے |
| **سنگل فائل** | `PublishSingleFile`|
| **ڈوکر** | کنٹینرائزڈ |
| **MSI / ClickOnce** | ونڈوز انسٹالر |
| **Azure ایپ سروس** | کلاؤڈ ہوسٹنگ |
| **IIS** | ونڈوز ہوسٹنگ |
---

## خلاصہ
Visual Basic کا ماحولیاتی نظام .NET کا وسیع انفراسٹرکچر شیئر کرتا ہے۔ معیاری اسٹیک یہ ہے: **.NET 8+** رن ٹائم کے طور پر، **Visual Studio** بطور IDE، **ASP.NET Core** ویب کے لیے، **Entity Framework Core** یا **Dapper** ڈیٹا تک رسائی کے لیے، **xUnit** ٹیسٹنگ کے لیے، اور **NuGet** پیکجز کے لیے۔ VB.NET ان ڈویلپرز کے لیے مثالی ہے جو بنیادی نحو سے مطمئن ہیں جنہیں .NET ایکو سسٹم تک رسائی کی ضرورت ہے۔ **VBA** آفس آٹومیشن کے لیے ضروری ہے — لاکھوں کاروباری صارفین Excel اور Access میکرو پر انحصار کرتے ہیں۔ ماحولیاتی نظام ونڈوز ڈیسک ٹاپ ایپلی کیشنز، آفس آٹومیشن، اور انٹرپرائز لائن آف بزنس ایپلی کیشنز کے لیے بہترین موزوں ہے۔