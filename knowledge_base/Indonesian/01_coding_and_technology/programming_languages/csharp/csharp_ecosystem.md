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
# C# — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem C#/.NET.
---

## .NET SDK & Rantai Alat
| Alat | Tujuan |
|------|---------|
| **CLI dotnet** | Bangun, jalankan, uji, publikasikan |
| **MSBuild** | Mesin build yang mendasari |
| **NuGet CLI** | Manajemen paket |
| **format dotnet** | Pemformatan kode |
| **dotnet-ef** | Alat Kerangka Entitas |
| **dotnet-ketinggalan jaman** | Temukan paket usang |
| **skrip dotnet** | Jalankan skrip C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Waktu Proses & Implementasi
| Waktu proses | Catatan |
|---------|-------|
| **.NET 8/9** | LTS / STS saat ini, lintas platform |
| **.NET Framework** | Khusus Windows, lawas (4.8.x) |
| **Mono** | .NET Framework (Xamarin) sumber terbuka |
| **Persatuan (IL2CPP/Mono)** | Waktu pengoperasian mesin game |
| **Godot (.NET)** | Mesin permainan dengan dukungan C# |
---

## Manajemen Paket
| Sumber | Tujuan |
|--------|---------|
| **NuGet.org** | Registri paket resmi |
| **dotnet tambahkan paket** | Instalasi paket CLI |
| **ReferensiPaket** | Format .csproj modern |
| **Umpan pribadi** | Artefak Azure, Paket GitHub, MyGet |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **ASP.NET Inti** | Web tumpukan penuh | API, MVC, Blazor |
| **API Minimal** | Ringan | API Sederhana |
| **Server Blazor** | UI Interaktif | SPA yang dirender oleh server |
| **Perakitan Web Blazor** | Sisi klien | SPA berbasis browser |
| **gRPC** | RPC | Layanan berkinerja tinggi |
| **SinyalR** | Waktu nyata | WebSockets, tekan |
| **Data** | Ekstensi REST | API yang Dapat Dikueri |
| **Titik Akhir Cepat** | Kerangka API | Cepat, boilerplate minimal |
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

## Basis Data & ORM
| Teknologi | Ketik |
|------------|------|
| **Inti Kerangka Entitas** | ORM penuh, migrasi |
| **Necis** | Mikro-ORM, SQL mentah |
| **NHibernasi** | ORM matang |
| **GratisSql** | ORM Ringan |
| **Marten** | DB dokumen PostgreSQL |
| **StackExchange.Redis** | Klien Redis |
| **MongoDB.Driver** | Klien MongoDB |
| **Npgsql** | Pengandar PostgreSQL |
| **Konektor MySql** | Pengandar MySQL |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **xUnit** | Kerangka pengujian paling populer |
| **NUnit** | Kerangka pengujian klasik |
| **Tes MST** | Kerangka pengujian Microsoft |
| **Moq** | Perpustakaan mengejek |
| **NPengganti** | Ejekan ramah |
| **Pernyataan Lancar** | Pernyataan lancar |
| **Seharusnya** | Pernyataan yang dapat dibaca |
| **Palsu** | Pembuatan data palsu |
| **Perlengkapan Otomatis** | Uji otomatisasi data |
| **Wadah uji** | Tes integrasi berbasis Docker |
| **BenchmarkDotNet** | Benchmarking Mikro |
| **selimut** | Cakupan kode |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **Penganalisis Roslyn** | Analisis kode bawaan |
| **SonarAnalyzer.CSharp** | Aturan SonarQube |
| **Polisi Gaya** | Penegakan gaya pengkodean |
| **format dotnet** | Pemformatan kode |
| **Konfigurasi Editor** | Konsistensi lintas editor |
| **SonarQube / SonarCloud** | Platform kualitas kode |
| **Lebih Tajam** | Analisis JetBrains + pemfaktoran ulang |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Studio Visual** | IDE Windows berfitur lengkap (Komunitas/Pro/Perusahaan) |
| **Pengendara** | JetBrains C# IDE lintas platform |
| **Kode VS + Kit Pengembang C#** | Ringan, ekstensi Microsoft |
| **Visual Studio untuk Mac** | Sudah pensiun (gunakan Rider atau VS Code) |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Sistem.Teks.Json** | Serialisasi JSON bawaan |
| **Newtonsoft.Json** | JSON lama (masih banyak digunakan) |
| **Serilog** | Pencatatan log terstruktur |
| **NLog** | Kerangka logging |
| **Poli** | Kebijakan ketahanan dan percobaan ulang |
| **MediaR** | Pola mediator (CQRS) |
| **Pemeta Otomatis** | Pemetaan objek-ke-objek |
| **Validasi Lancar** | Perpustakaan validasi |
| **Transit Massal** | Bus pesan (RabbitMQ, Azure SB) |
| **Hangtung** | Pemrosesan pekerjaan latar belakang |
| **Kuarsa.NET** | Penjadwalan pekerjaan |
| **Spectre.Console** | Aplikasi konsol yang indah |
| **CommandLineParser** | Penguraian argumen CLI |
---

## Integrasi Cloud & Azure
| Layanan | Tujuan |
|---------|---------|
| **Fungsi Azure** | Tanpa server |
| **Azure SDK untuk .NET** | Semua layanan Azure |
| **AWS SDK untuk .NET** | Layanan AWS |
| **Google Cloud .NET** | Layanan GCP |
| **Azure Cosmos DB** | Basis data NoSQL |
| **Bus Layanan Azure** | Pesan |
| **Gudang Kunci Azure** | Manajemen rahasia |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Mandiri** | Bundel runtime .NET |
| **Bergantung pada kerangka kerja** | Memerlukan instalasi .NET |
| **Publikasi file tunggal** | `dotnet publish /p:PublishSingleFile=true`|
| **AOT Asli** | `PublishAot=true`(tidak perlu JIT) |
| **Buruh pelabuhan** | `mcr.microsoft.com/dotnet/aspnet`|
| **Layanan Aplikasi Azure** | Penerapan PaaS |
| **AWS Lambda** | Tanpa server |
| **IIS** | hosting Windows |
| **Kestrel** | Server web lintas platform bawaan |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Ringkasan
C# dan .NET menawarkan salah satu ekosistem paling produktif. Tumpukan standarnya adalah: **.NET 8+** sebagai runtime, **ASP.NET Core** untuk web, **Entity Framework Core** atau **Dapper** untuk akses data, **xUnit + Moq** untuk pengujian, **Visual Studio** atau **Rider** sebagai IDE, dan **NuGet** untuk paket. C# modern dengan catatan, pencocokan pola, tipe referensi yang dapat dibatalkan, dan API minimal bersifat ringkas dan ekspresif. Kompilasi **Native AOT** memungkinkan startup yang sangat cepat dan biner kecil. Ekosistemnya unggul dalam aplikasi perusahaan, cloud (Azure), pengembangan game (Unity, Godot), dan lintas platform.