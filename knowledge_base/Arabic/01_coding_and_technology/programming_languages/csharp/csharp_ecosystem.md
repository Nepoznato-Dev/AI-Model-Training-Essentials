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
#C# - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية الأساسية الأساسية في النظام البيئي C# / .NET.
---

## .NET SDK وسلسلة الأدوات
| أداة | الغرض |
|------|---------|
| **دوت نت سطر الأوامر** | البناء والتشغيل والاختبار والنشر |
| **MSBuild** | محرك البناء الأساسي |
| ** نوجيت كلي ** | إدارة الحزم |
| **تنسيق الدوت نت** | تنسيق الكود |
| **دوت نت-إف** | أدوات إطار الكيان |
| ** الدوت نت قديم ** | البحث عن الحزم القديمة |
| **دوت نت سكريبت** | قم بتشغيل البرامج النصية C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## أوقات التشغيل والتطبيقات
| وقت التشغيل | ملاحظات |
|---------|------|
| **.نت 8/9** | LTS / STS الحالي، عبر الأنظمة الأساسية |
| **.NET Framework** | نظام التشغيل Windows فقط، الإصدار القديم (4.8.x) |
| **مونو** | مفتوح المصدر .NET Framework (Xamarin) |
| **الوحدة (IL2CPP/مونو)** | وقت تشغيل محرك اللعبة |
| **جودو (.NET)** | محرك اللعبة بدعم C# |
---

## إدارة الحزم
| المصدر | الغرض |
|--------|---------|
| ** NuGet.org ** | تسجيل الحزمة الرسمية |
| ** حزمة إضافة الدوت نت ** | تثبيت حزمة CLI |
| **مرجع الحزمة** | تنسيق .csproj الحديث |
| **خلاصات خاصة** | قطع أثرية من Azure، وحزم GitHub، وMyGet |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| ** ASP.NET كور ** | ويب مكدس كامل | واجهات برمجة التطبيقات، MVC، Blazor |
| ** الحد الأدنى من واجهات برمجة التطبيقات ** | خفيف الوزن | واجهات برمجة التطبيقات البسيطة |
| **خادم بليزور** | واجهة المستخدم التفاعلية | SPA المقدمة من الخادم |
| **Blazor WebAssembly** | من جانب العميل | SPA القائم على المتصفح |
| **جي آر بي سي** | آر بي سي | خدمات عالية الأداء |
| ** سيجنال آر ** | في الوقت الحقيقي | WebSockets، دفع |
| **أوداتا** | ملحقات REST | واجهات برمجة التطبيقات القابلة للاستعلام |
| **نقاط النهاية السريعة** | إطار عمل واجهة برمجة التطبيقات | سريع وبحد أدنى من النموذج |
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

## قاعدة البيانات وORM
| تكنولوجيا | اكتب |
|------------|------|
| ** إطار عمل الكيان ** | ORM الكامل، الهجرات |
| ** دابر ** | مايكرو ORM، SQL الخام |
| ** ن السبات ** | ناضجة ORM |
| **FreeSql** | ORM خفيف الوزن |
| **مارتن** | مستند PostgreSQL DB |
| **StackExchange.Redis** | عميل ريديس |
| **MongoDB.Driver** | عميل MongoDB |
| **نبجسقل** | برنامج تشغيل PostgreSQL |
| **MySqlConnector** | برنامج تشغيل MySQL |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **xUnit** | إطار الاختبار الأكثر شعبية |
| ** وحدة ** | إطار الاختبار الكلاسيكي |
| **MSTest** | إطار اختبار مايكروسوفت |
| **موك** | المكتبة الساخرة |
| **نبديل** | السخرية الودية |
| ** التأكيدات بطلاقة ** | التأكيدات بطلاقة |
| **ينبغي** | تأكيدات مقروءة |
| **زائف** | توليد بيانات وهمية |
| **التثبيت التلقائي** | أتمتة بيانات الاختبار |
| **حاويات الاختبار** | اختبارات التكامل المستندة إلى عامل الميناء |
| ** بنشماركدوت نت ** | العلامات المعيارية الدقيقة |
| **غطاء** | تغطية الكود |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **محللات روزلين** | تحليل الكود المدمج |
| **SonarAnalyzer.CSharp** | قواعد سونار كيوب |
| ** ستايل كوب ** | إنفاذ أسلوب الترميز |
| **تنسيق الدوت نت** | تنسيق الكود |
| ** تكوين المحرر ** | الاتساق بين المحررين |
| **سوناركيوب /سوناركلاود** | منصة جودة الكود |
| ** ريشاربر ** | تحليل JetBrains + إعادة البناء |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **فيجوال ستوديو** | Windows IDE كامل المواصفات (المجتمع/المحترف/المؤسسة) |
| **الراكب** | عبر منصة JetBrains C# IDE |
| **VS Code + C# Dev Kit** | خفيف الوزن، امتداد مايكروسوفت |
| **فيجوال ستوديو لنظام التشغيل Mac** | أن تكون متقاعدًا (استخدم Rider أو VS Code) |
---

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **System.Text.Json** | تسلسل JSON مدمج |
| **Newtonsoft.Json** | Legacy JSON (لا يزال مستخدمًا على نطاق واسع) |
| **سيريلوج** | التسجيل المنظم |
| **نلوج** | إطار التسجيل |
| **بولي** | سياسات المرونة وإعادة المحاولة |
| **ميدياتر** | نمط الوسيط (CQRS) |
| **AutoMapper** | تعيين كائن إلى كائن |
| **التحقق بطلاقة** | مكتبة التحقق |
| **النقل الجماعي** | ناقل الرسائل (RabbitMQ، Azure SB) |
| **هانج فاير** | معالجة الوظائف الخلفية |
| **كوارتز.نت** | جدولة الوظائف |
| **Spectre.Console** | تطبيقات وحدة التحكم الجميلة |
| **CommandLineParser** | تحليل وسيطة CLI |
---

## التكامل السحابي مع Azure
| الخدمة | الغرض |
|---------|--------|
| ** وظائف أزور ** | بدون خادم |
| **Azure SDK لـ .NET** | جميع خدمات أزور |
| **AWS SDK لـ .NET** | خدمات AWS |
| ** جوجل كلاود .NET ** | خدمات جي سي بي |
| **أزور كوزموس دي بي** | قاعدة بيانات NoSQL |
| **حافلة خدمة Azure** | المراسلة |
| ** Azure Key Vault ** | إدارة الأسرار |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **مكتفٍ بذاته** | حزم .NET وقت التشغيل |
| **تعتمد على الإطار** | يتطلب تثبيت .NET |
| **نشر ملف واحد** | `dotnet publish /p:PublishSingleFile=true`|
| ** AOT الأصلي ** | `PublishAot=true`(لا حاجة إلى JIT) |
| ** عامل الميناء ** | `mcr.microsoft.com/dotnet/aspnet`|
| ** خدمة تطبيقات Azure ** | نشر PaaS |
| **AWS لامدا** | بدون خادم |
| **إي آي إس** | استضافة ويندوز |
| **العسوق** | خادم ويب مدمج عبر الأنظمة الأساسية |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## ملخص
تقدم C# و.NET واحدة من أكثر الأنظمة البيئية إنتاجية. المكدس القياسي هو: **.NET 8+** كوقت تشغيل، **ASP.NET Core** للويب، **Entity Framework Core** أو **Dapper** للوصول إلى البيانات، **xUnit + Moq** للاختبار، **Visual Studio** أو **Rider** مثل IDE، و **NuGet** للحزم. تعد لغة C# الحديثة مع السجلات ومطابقة الأنماط وأنواع المراجع الخالية والحد الأدنى من واجهات برمجة التطبيقات موجزة ومعبرة. يتيح تجميع **AOT الأصلي** إمكانية بدء التشغيل بسرعة فائقة والثنائيات الصغيرة. يتفوق النظام البيئي في تطبيقات المؤسسات والسحابة (Azure) وتطوير الألعاب (Unity وGodot) والتطبيقات عبر الأنظمة الأساسية.