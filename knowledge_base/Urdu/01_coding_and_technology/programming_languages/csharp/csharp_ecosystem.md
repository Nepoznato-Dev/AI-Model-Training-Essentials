<!--
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

-->
# C# — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ C# / .NET ایکو سسٹم میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## .NET SDK اور ٹول چین
| ٹول | مقصد |
|------|---------|
| **ڈاٹ نیٹ CLI** | بنائیں، چلائیں، ٹیسٹ کریں، شائع کریں |
| **MSBuild** | بنیادی تعمیراتی انجن |
| **NuGet CLI** | پیکیج مینجمنٹ |
| **ڈاٹ نیٹ فارمیٹ** | کوڈ فارمیٹنگ |
| **dotnet-ef** | ہستی کے فریم ورک کے اوزار |
| **ڈاٹ نیٹ فرسودہ** | پرانے پیکجز تلاش کریں |
| **ڈاٹ نیٹ اسکرپٹ** | C# اسکرپٹ (.csx) چلائیں |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## رن ٹائمز اور عمل درآمد
| رن ٹائم | نوٹس |
|---------|---------|
| **.NET 8/9** | موجودہ LTS/STS، کراس پلیٹ فارم |
| **.NET فریم ورک** | صرف ونڈوز، میراث (4.8.x) |
| **مونو** | اوپن سورس .NET فریم ورک (Xamarin) |
| **Unity (IL2CPP/Mono)** | گیم انجن رن ٹائم |
| **Godot (.NET)** | C# سپورٹ کے ساتھ گیم انجن |
---

## پیکیج مینجمنٹ
| ماخذ | مقصد |
|---------|---------|
| **NuGet.org** | سرکاری پیکج رجسٹری |
| **ڈاٹ نیٹ پیکج شامل کریں** | CLI پیکیج انسٹال |
| **پیکیج کا حوالہ** | جدید .csproj فارمیٹ |
| **نجی فیڈ** | Azure Artifacts, GitHub Packages, MyGet |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **ASP.NET کور** | مکمل اسٹیک ویب | APIs، MVC، Blazor |
| **کم سے کم APIs** | ہلکا پھلکا | سادہ APIs |
| **بلیزر سرور** | انٹرایکٹو UI | سرور کی طرف سے فراہم کردہ SPA |
| **بلیزر ویب اسمبلی** | کلائنٹ کی طرف | براؤزر پر مبنی SPA |
| **gRPC** | RPC | اعلی کارکردگی کی خدمات |
| **سگنل آر** | ریئل ٹائم | ویب ساکٹس، پش |
| **OData** | ریسٹ ایکسٹینشنز | قابل استفسار APIs |
| **فاسٹ اینڈ پوائنٹس** | API فریم ورک | تیز، کم سے کم بوائلر پلیٹ |
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

## ڈیٹا بیس اور ORM
| ٹیکنالوجی | قسم |
|------------|------|
| **اینٹیٹی فریم ورک کور** | مکمل ORM، منتقلی |
| **ڈیپر** | مائیکرو-ORM، خام SQL |
| **NHibernate** | بالغ ORM |
| **فری ایس کیو ایل** | ہلکا پھلکا ORM |
| **مارٹن** | PostgreSQL دستاویز DB |
| **StackExchange.Redis** | Redis کلائنٹ |
| **MongoDB.Driver** | MongoDB کلائنٹ |
| **Npgsql** | PostgreSQL ڈرائیور |
| **MySqlConnector** | MySQL ڈرائیور |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **xUnit** | سب سے زیادہ مقبول ٹیسٹ فریم ورک |
| **NUnit** | کلاسک ٹیسٹ فریم ورک |
| **MSTest** | مائیکروسافٹ کا ٹیسٹ فریم ورک |
| **Moq** | طنزیہ لائبریری |
| **این ایس متبادل** | دوستانہ مذاق |
| **روانی بیانات** | روانی کے دعوے |
| **چاہیے** | پڑھنے کے قابل دعوے |
| **بوگس** | جعلی ڈیٹا جنریشن |
| **آٹو فکسچر** | ٹیسٹ ڈیٹا آٹومیشن |
| **ٹیسٹ کنٹینرز** | ڈوکر پر مبنی انضمام ٹیسٹ |
| **بینچ مارک ڈاٹ نیٹ** | مائیکرو بینچ مارکنگ |
| ** کورلیٹ** | کوڈ کوریج |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **روزلن تجزیہ کار** | بلٹ ان کوڈ تجزیہ |
| **SonarAnalyzer.CSharp** | سونار کیوب کے قواعد |
| **StyleCop** | کوڈنگ سٹائل کا نفاذ |
| **ڈاٹ نیٹ فارمیٹ** | کوڈ فارمیٹنگ |
| **EditorConfig** | کراس ایڈیٹر کی مستقل مزاجی |
| **سونار کیوب / سونار کلاؤڈ** | کوڈ کوالٹی پلیٹ فارم |
| **ری شارپر** | جیٹ برینز کا تجزیہ + ری فیکٹرنگ |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **بصری اسٹوڈیو** | مکمل خصوصیات والے ونڈوز IDE (کمیونٹی/پرو/انٹرپرائز) |
| **سوار** | کراس پلیٹ فارم JetBrains C# IDE |
| **VS کوڈ + C# دیو کٹ** | ہلکا پھلکا، مائیکروسافٹ ایکسٹینشن |
| **بصری اسٹوڈیو برائے میک** | ریٹائرڈ ہونا (رائیڈر یا VS کوڈ استعمال کریں) |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **System.Text.Json** | بلٹ ان JSON سیریلائزیشن |
| **Newtonsoft.Json** | لیگیسی JSON (اب بھی وسیع پیمانے پر استعمال کیا جاتا ہے) |
| **سیریلوگ** | سٹرکچرڈ لاگنگ |
| **NLog** | لاگنگ فریم ورک |
| **پولی** | لچک اور دوبارہ کوشش کی پالیسیاں |
| **میڈیاٹ آر** | ثالثی پیٹرن (CQRS) |
| **آٹو میپر** | آبجیکٹ سے آبجیکٹ میپنگ |
| **روانی توثیق** | توثیق لائبریری |
| **ماس ٹرانزٹ** | پیغام بس (RabbitMQ, Azure SB) |
| **ہنگ فائر** | بیک گراؤنڈ جاب پروسیسنگ |
| **Quartz.NET** | ملازمت کا شیڈولنگ |
| **Sspectre.Console** | خوبصورت کنسول ایپس |
| **کمانڈ لائن پارسر** | CLI دلیل کی تجزیہ |
---

## کلاؤڈ اور ایزور انٹیگریشن
| سروس | مقصد |
|---------|---------|
| **آزور فنکشنز** | بے سرور |
| ** Azure SDK برائے .NET** | تمام Azure سروسز |
| **AWS SDK برائے .NET** | AWS خدمات |
| **Google Cloud .NET** | GCP خدمات |
| **Azure Cosmos DB** | NoSQL ڈیٹا بیس |
| **ازور سروس بس** | پیغام رسانی |
| **Azure Key Vault** | راز کا انتظام |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **خود موجود** | بنڈلز .NET رن ٹائم |
| **فریم ورک پر منحصر** | .NET انسٹال کی ضرورت ہے |
| **سنگل فائل پبلش** | `dotnet publish /p:PublishSingleFile=true`|
| **آبائی AOT** | `PublishAot=true`(کوئی جے آئی ٹی کی ضرورت نہیں) |
| **ڈوکر** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure ایپ سروس** | PaaS تعیناتی |
| **AWS Lambda** | بے سرور |
| **IIS** | ونڈوز ہوسٹنگ |
| **کیسٹریل** | بلٹ ان کراس پلیٹ فارم ویب سرور |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## خلاصہ
C# اور .NET سب سے زیادہ پیداواری ماحولیاتی نظام میں سے ایک پیش کرتے ہیں۔ معیاری اسٹیک یہ ہے: **.NET 8+** بطور رن ٹائم، **ASP.NET Core** ویب کے لیے، **Entity Framework Core** یا **Dapper** ڈیٹا تک رسائی کے لیے، **xUnit + Moq** ٹیسٹنگ کے لیے، **Visual Studio** یا **Rider** بطور IDE، اور **NuGet** پیکجز کے لیے۔ ریکارڈز، پیٹرن کی مماثلت، غیر قابل حوالہ قسمیں، اور کم سے کم APIs کے ساتھ جدید C# جامع اور اظہار خیال ہے۔ **مقامی AOT** تالیف تیز رفتار اسٹارٹ اپ اور چھوٹی بائنریز کو قابل بناتی ہے۔ ماحولیاتی نظام انٹرپرائز، کلاؤڈ (Azure)، گیم ڈیولپمنٹ (Unity، Godot) اور کراس پلیٹ فارم ایپلی کیشنز میں بہترین ہے۔