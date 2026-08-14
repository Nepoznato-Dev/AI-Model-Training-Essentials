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
# Visual Basic — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz, Visual Basic (.NET) ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Visual Basic Sürümleri
| Sürüm | Notlar |
|-----------|----------|
| **VB.NET (Visual Basic 2022)** | Güncel, .NET 8+ |
| **VB6** | Klasik Visual Basic (eski) |
| **VBA** | Uygulamalar için Visual Basic (Ofis) |
| **VBScript** | Komut dosyası dili (kullanımdan kaldırıldı) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Oluşturma Araçları
| Araç | Amaç |
|------|------------|
| **dotnet CLI** | .NET oluşturun, test edin, yayınlayın |
| **MSBuild** | Motor oluştur |
| **Görsel Stüdyo** | Tam IDE |
| **NuGet** | Paket yönetimi |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **ASP.NET Çekirdeği** | Tam yığın | API'ler, MVC, Razor Sayfaları |
| **Minimum API'ler** | Hafif | Basit API'ler |
| **Blazor** | Web kullanıcı arayüzü | Bileşen tabanlı kullanıcı arayüzü |
| **SinyalR** | Gerçek zamanlı | WebSoketleri |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **Varlık Çerçevesi Çekirdeği** | Tam ORM |
| **Şık** | Mikro-ORM |
| **ADO.NET** | Düşük seviyeli veri erişimi |
| **OleDb** | Eski veri erişimi |
| **MySql.Data** | MySQL bağlayıcı |
| **Npgsql** | PostgreSQL bağlayıcı |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **xBirim** | Test çerçevesi |
| **NUbirim** | Test çerçevesi |
| **MSTest** | Microsoft test çerçevesi |
| **Adedi** | Alaycı |
| **NSyedek** | Alaycı |
| **Akıcı İddialar** | Akıcı iddialar |
| **BenchmarkDotNet** | Karşılaştırma |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **Roslyn Analizörleri** | Dahili analiz |
| **SonarAnalizörü** | SonarQube kuralları |
| **dotnet formatı** | Kod biçimlendirme |
| **EditorConfig** | Tutarlı stil |
| **SonarQube** | Kod kalitesi platformu |
---

## Masaüstü (WinForms / WPF)
| Çerçeve | Amaç |
|-----------|------------|
| **WinFormları** | Klasik Windows formları |
| **WPF** | Modern Windows Kullanıcı Arayüzü (XAML) |
| **MAUI** | Çapraz platform (Xamarin'in halefi) |
| **Avalonya** | Platformlar arası WPF benzeri |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **System.Text.Json** | JSON serileştirme |
| **Newtonsoft.Json** | JSON (eski) |
| **Serilog** | Günlük |
| **Polly** | Dayanıklılık politikaları |
| **OtoMapper** | Nesne eşleme |
| **Akıcı Doğrulama** | Doğrulama |
| **Toplu Taşıma** | Mesaj otobüsü |
| **Ateş** | Arka plan işleri |
| **Spectre.Console** | Konsol Kullanıcı Arayüzü |
---

## Ofis Otomasyonu (VBA)
| Teknoloji | Amaç |
|---------------|-----------|
| **Excel VBA** | Excel otomasyonu |
| **Word VBA** | Kelime otomasyonu |
| **VBA'ya erişim** | Erişim otomasyonu |
| **Outlook VBA** | Outlook otomasyonu |
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

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **Görsel Stüdyo** | Tam VB.NET IDE (Topluluk/Pro/Kurumsal) |
| **VS Kodu** | .NET uzantılarıyla hafif |
| **VBA Düzenleyici** | Office uygulamalarında yerleşik |
| **binici** | JetBrains (sınırlı VB desteği) |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Kendi kendine yeten** | Paketler .NET çalışma zamanı |
| **Çerçeveye bağımlı** | .NET'in yüklü olmasını gerektirir |
| **Tek dosya** | `PublishSingleFile`|
| **Docker** | Konteynerde |
| **MSI / ClickOnce** | Windows yükleyici |
| **Azure Uygulama Hizmeti** | Bulut barındırma |
| **IIS** | Windows barındırma |
---

## Özet
Visual Basic'in ekosistemi .NET'in geniş altyapısını paylaşır. Standart yığın şunlardır: çalışma zamanı olarak **.NET 8+**, IDE olarak **Visual Studio**, web için **ASP.NET Core**, veri erişimi için **Entity Framework Core** veya **Dapper**, test için **xUnit** ve paketler için **NuGet**. VB.NET, .NET ekosistemine erişmesi gereken BASIC söz dizimi konusunda deneyimli geliştiriciler için idealdir. **VBA** Office otomasyonu için vazgeçilmez olmaya devam ediyor; milyonlarca iş kullanıcısı Excel ve Access makrolarına güveniyor. Ekosistem, Windows masaüstü uygulamaları, Office otomasyonu ve kurumsal iş kolu uygulamaları için en uygunudur.