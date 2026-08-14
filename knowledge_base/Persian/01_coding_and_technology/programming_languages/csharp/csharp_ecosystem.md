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
# سی شارپ - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم C#/.NET را پوشش می‌دهد.
---

## NET SDK & Toolchain
| ابزار | هدف |
|------|---------|
| **dotnet CLI** | ساخت، اجرا، تست، انتشار |
| **MSBuild** | موتور ساخت زیرین |
| **NuGet CLI** | مدیریت پکیج |
| **دات نت-فرمت** | قالب بندی کد |
| **dotnet-ef** | ابزار Entity Framework |
| **dotnet- قدیمی** | یافتن بسته های قدیمی |
| **dotnet-script** | اجرای اسکریپت های C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## زمان اجرا و پیاده سازی
| زمان اجرا | یادداشت ها |
|---------|-------|
| **.NET 8/9** | LTS / STS فعلی، کراس پلتفرم |
| **.NET Framework** | فقط ویندوز، قدیمی (4.8.x) |
| **مونو** | متن باز .NET Framework (Xamarin) |
| **یونیتی (IL2CPP/Mono)** | زمان اجرا موتور بازی |
| **گودو (.NET)** | موتور بازی با پشتیبانی سی شارپ |
---

## مدیریت بسته
| منبع | هدف |
|--------|---------|
| **NuGet.org** | رجیستری پکیج رسمی |
| **پکیج اضافه کردن دات نت** | نصب بسته CLI |
| **مرجع بسته** | فرمت مدرن csproj |
| **فیدهای خصوصی** | Azure Artifacts، بسته‌های GitHub، MyGet |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **ASP.NET Core** | وب تمام پشته | API، MVC، Blazor |
| **حداقل API** | سبک | API های ساده |
| **سرور بلزور** | رابط کاربری تعاملی | SPA ارائه شده توسط سرور |
| **Blazor WebAssembly** | سمت مشتری | SPA مبتنی بر مرورگر |
| **gRPC** | RPC | خدمات با کارایی بالا |
| **SignalR** | زمان واقعی | WebSockets، فشار |
| **OData** | پسوندهای REST | APIهای قابل پرس و جو |
| **FastEndpoints** | چارچوب API | دیگ بخار سریع و کمینه |
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

## پایگاه داده و ORM
| فناوری | نوع |
|------------|------|
| ** هسته چارچوب نهاد ** | ORM کامل، مهاجرت |
| **دپر** | Micro-ORM، SQL خام |
| **NHibernate** | ORM بالغ |
| **FreeSql** | ORM سبک |
| **مارتن** | DB سند PostgreSQL |
| **StackExchange.Redis** | مشتری Redis |
| **MongoDB.Driver** | مشتری MongoDB |
| **Npgsql** | درایور PostgreSQL |
| **MySqlConnector** | درایور MySQL |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **xUnit** | محبوب ترین چارچوب تست |
| **NUnit** | چارچوب آزمون کلاسیک |
| **MSTest** | چارچوب تست مایکروسافت |
| **موق** | کتابخانه تمسخر آمیز |
| **NS جایگزین ** | تمسخر دوستانه |
| **FluentAssertions** | ادعاهای روان |
| **باید** | ادعاهای خواندنی |
| **جعلی** | تولید داده های جعلی |
| **AutoFixture** | تست اتوماسیون داده |
| **تست ظروف** | تست های یکپارچه سازی مبتنی بر داکر |
| **BenchmarkDotNet** | Microbenchmarking |
| **روتختی** | پوشش کد |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **آنالایزر Roslyn** | تحلیل کد داخلی |
| **SonarAnalyzer.CSharp** | قوانین SonarQube |
| **StyleCop** | اجرای سبک کدنویسی |
| **دات نت-فرمت** | قالب بندی کد |
| **EditorConfig** | سازگاری بین ویرایشگر |
| **SonarQube / SonarCloud** | پلت فرم کیفیت کد |
| **ReSharper** | تجزیه و تحلیل JetBrains + Refactoring |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **ویژوال استودیو** | Windows IDE با امکانات کامل (Community/Pro/Enterprise) |
| **سوار** | کراس پلتفرم JetBrains C# IDE |
| **VS Code + C# Dev Kit** | سبک، پسوند مایکروسافت |
| **ویژوال استودیو برای مک** | بازنشسته بودن (از Rider یا VS Code استفاده کنید) |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **System.Text.Json** | سریال سازی داخلی JSON |
| **Newtonsoft.Json** | JSON قدیمی (هنوز به طور گسترده استفاده می شود) |
| **Serilog** | ورود به سیستم ساخت یافته |
| **NLog** | چارچوب ورود به سیستم |
| **پولی** | تاب آوری و سیاست های امتحان مجدد |
| **MediatR** | الگوی واسطه (CQRS) |
| **AutoMapper** | نگاشت شیء به شی |
| **FluentValidation** | کتابخانه اعتبار سنجی |
| **MassTransit** | اتوبوس پیام (RabbitMQ، Azure SB) |
| **آتش آتش** | پردازش شغل پیشینه |
| **Quartz.NET** | زمان بندی کار |
| **Spectre.Console** | اپلیکیشن های زیبای کنسول |
| **CommandLineParser** | تجزیه آرگومان CLI |
---

## یکپارچه سازی Cloud & Azure
| خدمات | هدف |
|---------|---------|
| **توابع لاجوردی** | بدون سرور |
| **Azure SDK برای دات نت** | کلیه خدمات لاجورد |
| **AWS SDK برای NET** | خدمات AWS |
| **Google Cloud .NET** | خدمات GCP |
| **Azure Cosmos DB** | پایگاه داده NoSQL |
| **اتوبوس سرویس لاجورد** | پیام رسانی |
| **خزانه کلید لاجوردی** | مدیریت اسرار |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **خودکفا** | باندل زمان اجرا دات نت |
| **وابسته به چارچوب** | نیاز به نصب دات نت |
| **انتشار تک فایل** | `dotnet publish /p:PublishSingleFile=true`|
| **بومی AOT** | `PublishAot=true`(بدون نیاز به JIT) |
| **داکر** | `mcr.microsoft.com/dotnet/aspnet`|
| **سرویس اپلیکیشن آژور** | استقرار PaaS |
| **AWS Lambda** | بدون سرور |
| **IIS** | هاست ویندوز |
| **خرک** | وب سرور کراس پلتفرم داخلی |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## خلاصه
سی شارپ و دات نت یکی از مولدترین اکوسیستم ها را ارائه می دهند. پشته استاندارد عبارتند از: **.NET 8+** به عنوان زمان اجرا، **ASP.NET Core** برای وب، **Entity Framework Core** یا **Dapper** برای دسترسی به داده، **xUnit + Moq** برای آزمایش، **Visual Studio** یا **Rider** به عنوان IDE، و **NuGet** برای بسته ها. سی شارپ مدرن با سوابق، تطبیق الگو، انواع مرجع باطل و حداقل API مختصر و رسا است. ** کامپایل Native AOT ** راه اندازی سریع و باینری های کوچک را امکان پذیر می کند. این اکوسیستم در سازمانی، ابری (Azure)، توسعه بازی (Unity، Godot) و برنامه های کاربردی بین پلتفرم برتری دارد.