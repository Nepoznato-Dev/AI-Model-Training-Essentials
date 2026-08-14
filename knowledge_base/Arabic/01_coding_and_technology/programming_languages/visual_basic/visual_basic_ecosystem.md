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
# فيجوال بيسك – دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية الأساسية الأساسية في النظام البيئي Visual Basic (.NET).
---

## إصدارات فيجوال بيسك
| النسخة | ملاحظات |
|---------|------|
| **VB.NET (فيجوال بيسك 2022)** | الحالي، .NET 8+ |
| **VB6** | الكلاسيكية فيجوال بيسك (قديمة) |
| ** فبا ** | فيجوال بيسك للتطبيقات (أوفيس) |
| ** فبسكريبت ** | لغة البرمجة النصية (مهجورة) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## أدوات البناء
| أداة | الغرض |
|------|---------|
| **دوت نت سطر الأوامر** | بناء .NET واختباره ونشره |
| **MSBuild** | بناء المحرك |
| **فيجوال ستوديو** | بيئة تطوير متكاملة كاملة |
| ** نوجيت ** | إدارة الحزم |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| ** ASP.NET كور ** | مكدس كامل | واجهات برمجة التطبيقات، MVC، صفحات الحلاقة |
| ** الحد الأدنى من واجهات برمجة التطبيقات ** | خفيف الوزن | واجهات برمجة التطبيقات البسيطة |
| **بلازور** | واجهة مستخدم الويب | واجهة المستخدم القائمة على المكونات |
| ** سيجنال آر ** | في الوقت الحقيقي | ويب سوكيتس |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| ** إطار عمل الكيان ** | ORM كامل |
| ** دابر ** | مايكرو أورم |
| **أدو.نت** | الوصول إلى البيانات على مستوى منخفض |
| **OleDb** | الوصول إلى البيانات القديمة |
| **MySql.Data** | موصل MySQL |
| **نبجسقل** | موصل PostgreSQL |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **xUnit** | إطار الاختبار |
| ** وحدة ** | إطار الاختبار |
| **MSTest** | إطار اختبار مايكروسوفت |
| **موك** | استهزاء |
| **نبديل** | استهزاء |
| ** التأكيدات بطلاقة ** | التأكيدات بطلاقة |
| ** بنشماركدوت نت ** | المقارنة المعيارية |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **محللات روزلين** | تحليل مدمج |
| **محلل السونار** | قواعد سونار كيوب |
| **تنسيق الدوت نت** | تنسيق الكود |
| ** تكوين المحرر ** | أسلوب متسق |
| **سوناركيوب** | منصة جودة الكود |
---

## سطح المكتب (WinForms / WPF)
| الإطار | الغرض |
|-----------|--------|
| ** وينفورمز ** | نماذج ويندوز الكلاسيكية |
| **WPF** | واجهة مستخدم Windows الحديثة (XAML) |
| **ماوي** | عبر الأنظمة الأساسية (خلف Xamarin) |
| **أفالونيا** | عبر منصة تشبه WPF |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **System.Text.Json** | تسلسل JSON |
| **Newtonsoft.Json** | JSON (قديم) |
| **سيريلوج** | تسجيل |
| **بولي** | سياسات المرونة |
| **AutoMapper** | تعيين الكائنات |
| **التحقق بطلاقة** | التحقق من الصحة |
| **النقل الجماعي** | حافلة الرسائل |
| **هانج فاير** | وظائف الخلفية |
| **Spectre.Console** | واجهة مستخدم وحدة التحكم |
---

## أتمتة المكاتب (VBA)
| تكنولوجيا | الغرض |
|------------|---------|
| **اكسل VBA** | أتمتة إكسل |
| **كلمة VBA** | أتمتة الكلمات |
| **الوصول إلى VBA** | أتمتة الوصول |
| ** أوتلوك VBA ** | أتمتة التوقعات |
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

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **فيجوال ستوديو** | كامل VB.NET IDE (المجتمع/المحترف/المؤسسة) |
| **رمز VS** | خفيف الوزن مع امتدادات .NET |
| ** محرر VBA ** | مدمج في تطبيقات Office |
| **الراكب** | JetBrains (دعم VB محدود) |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **مكتفٍ بذاته** | حزم .NET وقت التشغيل |
| **تعتمد على الإطار** | يتطلب تثبيت .NET |
| **ملف واحد** | `PublishSingleFile`|
| ** عامل الميناء ** | في حاويات |
| **MSI / ClickOnce** | مثبت ويندوز |
| ** خدمة تطبيقات Azure ** | استضافة سحابية |
| **إي آي إس** | استضافة ويندوز |
---

## ملخص
يشترك النظام البيئي لـ Visual Basic في البنية التحتية الواسعة لـ .NET. المكدس القياسي هو: **.NET 8+** كوقت تشغيل، **Visual Studio** كـ IDE، **ASP.NET Core** للويب، **Entity Framework Core** أو **Dapper** للوصول إلى البيانات، **xUnit** للاختبار، و **NuGet** للحزم. يعد VB.NET مثاليًا للمطورين الذين يتعاملون مع بناء الجملة BASIC والذين يحتاجون إلى الوصول إلى النظام البيئي .NET. يظل **VBA** ضروريًا لأتمتة Office — حيث يعتمد الملايين من مستخدمي الأعمال على وحدات ماكرو Excel وAccess. يعد النظام البيئي مناسبًا بشكل أفضل لتطبيقات سطح مكتب Windows وأتمتة Office وتطبيقات خط الأعمال الخاصة بالمؤسسات.