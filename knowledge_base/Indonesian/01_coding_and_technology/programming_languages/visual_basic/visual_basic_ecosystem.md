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

# Visual Basic — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Visual Basic (.NET).
---

## Versi Visual Basic
| Versi | Catatan |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Saat ini, .NET 8+ |
| **VB6** | Visual Basic Klasik (warisan) |
| **VBA** | Visual Basic untuk Aplikasi (Kantor) |
| **VBScript** | Bahasa skrip (tidak digunakan lagi) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Alat Bangun
| Alat | Tujuan |
|------|---------|
| **CLI dotnet** | .NET membangun, menguji, menerbitkan |
| **MSBuild** | Bangun mesin |
| **Studio Visual** | IDE Lengkap |
| **NuGet** | Manajemen paket |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **ASP.NET Inti** | Tumpukan penuh | API, MVC, Halaman Razor |
| **API Minimal** | Ringan | API Sederhana |
| **Blazor** | UI Web | UI berbasis komponen |
| **SinyalR** | Waktu nyata | Soket Web |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **Inti Kerangka Entitas** | ORM penuh |
| **Necis** | Mikro-ORM |
| **ADO.NET** | Akses data tingkat rendah |
| **OleDb** | Akses data lama |
| **MySql.Data** | Konektor MySQL |
| **Npgsql** | Konektor PostgreSQL |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **xUnit** | Kerangka uji |
| **NUnit** | Kerangka uji |
| **Tes MST** | Kerangka uji Microsoft |
| **Moq** | Mengejek |
| **NPengganti** | Mengejek |
| **Pernyataan Lancar** | Pernyataan lancar |
| **BenchmarkDotNet** | Pembandingan |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **Penganalisis Roslyn** | Analisis bawaan |
| **Penganalisis Sonar** | Aturan SonarQube |
| **format dotnet** | Pemformatan kode |
| **Konfigurasi Editor** | Gaya yang konsisten |
| **SonarQube** | Platform kualitas kode |
---

## Desktop (WinForm/WPF)
| Kerangka | Tujuan |
|-----------|---------|
| **WinFormulir** | Bentuk Windows klasik |
| **WPF** | UI Windows Modern (XAML) |
| **MAUI** | Lintas platform (penerus Xamarin) |
| **Avalonia** | Seperti WPF lintas platform |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Sistem.Teks.Json** | Serialisasi JSON |
| **Newtonsoft.Json** | JSON (warisan) |
| **Serilog** | Pencatatan |
| **Poli** | Kebijakan ketahanan |
| **Pemeta Otomatis** | Pemetaan objek |
| **Validasi Lancar** | Validasi |
| **Transit Massal** | Bis pesan |
| **Hangtung** | Pekerjaan latar belakang |
| **Spectre.Console** | UI Konsol |
---

## Otomatisasi Kantor (VBA)
| Teknologi | Tujuan |
|------------|---------|
| **VBA Excel** | Otomatisasi Excel |
| **Kata VBA** | Otomatisasi kata |
| **Akses VBA** | Akses otomatisasi |
| **Pandangan VBA** | Otomatisasi Outlook |
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

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Studio Visual** | IDE VB.NET Lengkap (Komunitas/Pro/Perusahaan) |
| **Kode VS** | Ringan dengan ekstensi .NET |
| **Editor VBA** | Dibangun ke dalam aplikasi Office |
| **Pengendara** | JetBrains (dukungan VB terbatas) |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Mandiri** | Bundel runtime .NET |
| **Bergantung pada kerangka kerja** | Memerlukan instalasi .NET |
| **File tunggal** | `PublishSingleFile`|
| **Buruh pelabuhan** | dalam kontainer |
| **MSI / KlikSekali** | Pemasang Windows |
| **Layanan Aplikasi Azure** | Hosting awan |
| **IIS** | hosting Windows |
---

## Ringkasan
Ekosistem Visual Basic berbagi infrastruktur .NET yang luas. Tumpukan standarnya adalah: **.NET 8+** sebagai runtime, **Visual Studio** sebagai IDE, **ASP.NET Core** untuk web, **Entity Framework Core** atau **Dapper** untuk akses data, **xUnit** untuk pengujian, dan **NuGet** untuk paket. VB.NET sangat ideal bagi pengembang yang terbiasa dengan sintaks BASIC yang membutuhkan akses ke ekosistem .NET. **VBA** tetap penting untuk otomatisasi Office — jutaan pengguna bisnis mengandalkan makro Excel dan Access. Ekosistem ini paling cocok untuk aplikasi desktop Windows, otomatisasi Office, dan aplikasi lini bisnis perusahaan.