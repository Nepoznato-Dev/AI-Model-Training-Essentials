---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C# — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz, C# / .NET ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## .NET SDK ve Araç Zinciri
| Araç | Amaç |
|------|------------|
| **dotnet CLI** | Derleyin, çalıştırın, test edin, yayınlayın |
| **MSBuild** | Temel yapı motoru |
| **NuGet CLI** | Paket yönetimi |
| **dotnet formatı** | Kod biçimlendirme |
| **dotnet-ef** | Varlık Çerçevesi araçları |
| **dotnet güncelliğini kaybetmiş** | Güncelliğini yitirmiş paketleri bulun |
| **dotnet-komut dosyası** | C# betiklerini (.csx) çalıştırın |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Çalışma Zamanları ve Uygulamalar
| Çalışma zamanı | Notlar |
|-----------|----------|
| **.NET 8/9** | Güncel LTS / STS, platformlar arası |
| **.NET Çerçevesi** | Yalnızca Windows, eski (4.8.x) |
| **Tek renkli** | Açık kaynaklı .NET Framework (Xamarin) |
| **Birlik (IL2CPP/Mono)** | Oyun motoru çalışma zamanı |
| **Godot (.NET)** | C# destekli oyun motoru |
---

## Paket Yönetimi
| Kaynak | Amaç |
|----------|------------|
| **NuGet.org** | Resmi paket kaydı |
| **dotnet paket ekleme** | CLI paketi kurulumu |
| **Paket Referansı** | Modern .csproj biçimi |
| **Özel yayınlar** | Azure Artifacts, GitHub Paketleri, MyGet |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **ASP.NET Çekirdeği** | Tam yığın web | API'ler, MVC, Blazor |
| **Minimum API'ler** | Hafif | Basit API'ler |
| **Blazor Sunucusu** | Etkileşimli Kullanıcı Arayüzü | Sunucu tarafından oluşturulan SPA |
| **Blazor Web Montajı** | İstemci tarafı | Tarayıcı tabanlı SPA |
| **gRPC** | RPC | Yüksek performanslı hizmetler |
| **SinyalR** | Gerçek zamanlı | WebSockets, itin |
| **OVeri** | REST uzantıları | Sorgulanabilir API'ler |
| **Hızlı Uç Noktalar** | API çerçevesi | Hızlı, minimal standartlar |
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

## Veritabanı ve ORM
| Teknoloji | Tür |
|---------------|------|
| **Varlık Çerçevesi Çekirdeği** | Tam ORM, geçişler |
| **Şık** | Mikro-ORM, ham SQL |
| **NHazırda Bekletme** | Olgun ORM |
| **FreeSql** | Hafif ORM |
| **sansar** | PostgreSQL belgesi Veritabanı |
| **StackExchange.Redis** | Redis istemcisi |
| **MongoDB.Sürücü** | MongoDB istemcisi |
| **Npgsql** | PostgreSQL sürücüsü |
| **MySqlConnector** | MySQL sürücüsü |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **xBirim** | En popüler test çerçevesi |
| **NUbirim** | Klasik test çerçevesi |
| **MSTest** | Microsoft'un test çerçevesi |
| **Adedi** | Alaycı kütüphane |
| **NSyedek** | Dostça alay |
| **Akıcı İddialar** | Akıcı iddialar |
| **Gerekir** | Okunabilir iddialar |
| **Sahte** | Sahte veri üretimi |
| **Otomatik Fikstür** | Test verileri otomasyonu |
| **Test kapsayıcıları** | Docker tabanlı entegrasyon testleri |
| **BenchmarkDotNet** | Mikro kıyaslama |
| **yatak örtüsü** | Kod kapsamı |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **Roslyn Analizörleri** | Yerleşik kod analizi |
| **SonarAnalyzer.CSharp** | SonarQube kuralları |
| **Stil Polisi** | Kodlama stilinin uygulanması |
| **dotnet formatı** | Kod biçimlendirme |
| **EditorConfig** | Çapraz editör tutarlılığı |
| **SonarQube / SonarCloud** | Kod kalitesi platformu |
| **Yeniden Keskinleştirici** | JetBrains analizi + yeniden düzenleme |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **Görsel Stüdyo** | Tam özellikli Windows IDE (Topluluk/Pro/Kurumsal) |
| **binici** | Platformlar arası JetBrains C# IDE |
| **VS Kodu + C# Geliştirme Seti** | Hafif, Microsoft uzantısı |
| **Mac için Visual Studio** | Emekli olmak (Rider veya VS Kodunu kullanın) |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **System.Text.Json** | Yerleşik JSON serileştirme |
| **Newtonsoft.Json** | Eski JSON (hala yaygın olarak kullanılmaktadır) |
| **Serilog** | Yapılandırılmış günlük kaydı |
| **NLog** | Günlüğe kaydetme çerçevesi |
| **Polly** | Dayanıklılık ve yeniden deneme politikaları |
| **MedyaR** | Aracı modeli (CQRS) |
| **OtoMapper** | Nesneden nesneye eşleme |
| **Akıcı Doğrulama** | Doğrulama kitaplığı |
| **Toplu Taşıma** | Mesaj veri yolu (RabbitMQ, Azure SB) |
| **Ateş** | Arka planda iş işleme |
| **Quartz.NET** | İş planlama |
| **Spectre.Console** | Güzel konsol uygulamaları |
| **CommandLineParser** | CLI bağımsız değişkeni ayrıştırma |
---

## Bulut ve Azure Entegrasyonu
| Hizmet | Amaç |
|-----------|-----------|
| **Azure İşlevleri** | Sunucusuz |
| **.NET için Azure SDK'sı** | Tüm Azure hizmetleri |
| **.NET için AWS SDK** | AWS hizmetleri |
| **Google Bulut .NET** | GCP hizmetleri |
| **Azure Cosmos DB** | NoSQL veritabanı |
| **Azure Hizmet Otobüsü** | Mesajlaşma |
| **Azure Anahtar Kasası** | Sırlar yönetimi |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Kendi kendine yeten** | Paketler .NET çalışma zamanı |
| **Çerçeveye bağımlı** | .NET'in yüklü olmasını gerektirir |
| **Tek dosya yayınlama** | `dotnet publish /p:PublishSingleFile=true`|
| **Yerel AOT** | `PublishAot=true`(JIT gerekmez) |
| **Docker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure Uygulama Hizmeti** | PaaS dağıtımı |
| **AWS Lambda** | Sunucusuz |
| **IIS** | Windows barındırma |
| **Kestrel** | Yerleşik çapraz platform web sunucusu |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Özet
C# ve .NET en üretken ekosistemlerden birini sunar. Standart yığın şunlardır: çalışma zamanı olarak **.NET 8+**, web için **ASP.NET Core**, veri erişimi için **Entity Framework Core** veya **Dapper**, test için **xUnit + Moq**, IDE olarak **Visual Studio** veya **Rider** ve paketler için **NuGet**. Kayıtlar, kalıp eşleştirme, null yapılabilir referans türleri ve minimal API'ler içeren modern C# kısa ve özdür. **Yerel AOT** derlemesi, olağanüstü hızlı başlatmaya ve küçük ikili dosyalara olanak tanır. Ekosistem kurumsal, bulut (Azure), oyun geliştirme (Unity, Godot) ve platformlar arası uygulamalarda öne çıkıyor.