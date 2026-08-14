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
# C# — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি C# / .NET ইকোসিস্টেমের প্রয়োজনীয় টুলস, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## .NET SDK এবং টুলচেইন
| টুল | উদ্দেশ্য |
|------|---------|
| **ডটনেট CLI** | তৈরি করুন, চালান, পরীক্ষা করুন, প্রকাশ করুন |
| **MSBuild** | অন্তর্নিহিত বিল্ড ইঞ্জিন |
| **NuGet CLI** | প্যাকেজ ব্যবস্থাপনা |
| **ডটনেট-ফরম্যাট** | কোড ফরম্যাটিং |
| **ডটনেট-এফ** | এন্টিটি ফ্রেমওয়ার্ক টুলস |
| **ডটনেট-সেকেলে** | পুরানো প্যাকেজ খুঁজুন |
| **ডটনেট-স্ক্রিপ্ট** | C# স্ক্রিপ্ট চালান (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## রানটাইম এবং বাস্তবায়ন
| রানটাইম | নোট |
|---------|---------|
| **.NET 8/9** | বর্তমান LTS/STS, ক্রস-প্ল্যাটফর্ম |
| **.নেট ফ্রেমওয়ার্ক** | শুধুমাত্র উইন্ডোজ, লিগ্যাসি (4.8.x) |
| **মনো** | ওপেন সোর্স .NET ফ্রেমওয়ার্ক (জামারিন) |
| **ইউনিটি (IL2CPP/Mono)** | গেম ইঞ্জিন রানটাইম |
| **Godot (.NET)** | C# সমর্থন সহ গেম ইঞ্জিন |
---

## প্যাকেজ ব্যবস্থাপনা
| উৎস | উদ্দেশ্য |
|---------|---------|
| **NuGet.org** | অফিসিয়াল প্যাকেজ রেজিস্ট্রি |
| **ডটনেট অ্যাড প্যাকেজ** | CLI প্যাকেজ ইনস্টল |
| **প্যাকেজ রেফারেন্স** | আধুনিক .csproj ফরম্যাট |
| **ব্যক্তিগত ফিড** | Azure Artifacts, GitHub প্যাকেজ, MyGet |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **ASP.NET কোর** | ফুল-স্ট্যাক ওয়েব | APIs, MVC, Blazor |
| **ন্যূনতম APIs** | লাইটওয়েট | সরল APIs |
| **ব্লেজার সার্ভার** | ইন্টারেক্টিভ UI | সার্ভার-রেন্ডার করা SPA |
| **ব্লেজার ওয়েব অ্যাসেম্বলি** | ক্লায়েন্ট-সাইড | ব্রাউজার-ভিত্তিক SPA |
| **gRPC** | আরপিসি | উচ্চ কর্মক্ষমতা সেবা |
| **সিগন্যালআর** | রিয়েল-টাইম | WebSockets, push |
| **OData** | REST এক্সটেনশন | জিজ্ঞাসাযোগ্য APIs |
| **ফাস্টএন্ডপয়েন্ট** | API ফ্রেমওয়ার্ক | দ্রুত, ন্যূনতম বয়লারপ্লেট |
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

## ডাটাবেস এবং ওআরএম
| প্রযুক্তি | প্রকার |
|------------|------|
| **এন্টিটি ফ্রেমওয়ার্ক কোর** | সম্পূর্ণ ORM, মাইগ্রেশন |
| **ডপার** | মাইক্রো-ORM, কাঁচা SQL |
| **NHibernate** | পরিপক্ক ORM |
| **ফ্রিএসকিউএল** | লাইটওয়েট ORM |
| **মার্টেন** | PostgreSQL নথি DB |
| **StackExchange.Redis** | Redis ক্লায়েন্ট |
| **মঙ্গোডিবি. ড্রাইভার** | MongoDB ক্লায়েন্ট |
| **Npgsql** | PostgreSQL ড্রাইভার |
| **MySqlConnector** | মাইএসকিউএল ড্রাইভার |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **xইউনিট** | সবচেয়ে জনপ্রিয় পরীক্ষার কাঠামো |
| **NUnit** | ক্লাসিক পরীক্ষার কাঠামো |
| **MSTest** | মাইক্রোসফটের পরীক্ষার কাঠামো |
| **Moq** | উপহাস লাইব্রেরী |
| **এনএসবস্টিটিউট** | বন্ধুত্বপূর্ণ উপহাস |
| **সাবলীল বক্তব্য** | সাবলীল দাবী |
| **উচিতভাবে** | পঠনযোগ্য দাবি |
| **বোগাস** | জাল ডেটা জেনারেশন |
| **অটোফিক্সচার** | টেস্ট ডেটা অটোমেশন |
| **পরীক্ষার পাত্র** | ডকার-ভিত্তিক ইন্টিগ্রেশন পরীক্ষা |
| **বেঞ্চমার্কডটনেট** | মাইক্রোবেঞ্চমার্কিং |
| **কভারলেট** | কোড কভারেজ |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **রোজলিন বিশ্লেষক** | অন্তর্নির্মিত কোড বিশ্লেষণ |
| **সোনার অ্যানালাইজার.সিএসশার্প** | সোনারকিউবের নিয়ম |
| **স্টাইলকপ** | কোডিং শৈলী প্রয়োগ |
| **ডটনেট-ফরম্যাট** | কোড ফরম্যাটিং |
| **EditorConfig** | ক্রস-এডিটর ধারাবাহিকতা |
| **সোনারকিউব / সোনারক্লাউড** | কোড মানের প্ল্যাটফর্ম |
| **রিশার্পার** | JetBrains বিশ্লেষণ + রিফ্যাক্টরিং |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ভিজ্যুয়াল স্টুডিও** | সম্পূর্ণ বৈশিষ্ট্যযুক্ত উইন্ডোজ আইডিই (কমিউনিটি/প্রো/এন্টারপ্রাইজ) |
| **রাইডার** | ক্রস-প্ল্যাটফর্ম JetBrains C# IDE |
| **ভিএস কোড + সি# দেব কিট** | লাইটওয়েট, মাইক্রোসফট এক্সটেনশন |
| **ম্যাকের জন্য ভিজ্যুয়াল স্টুডিও** | অবসর নেওয়া হচ্ছে (রাইডার বা ভিএস কোড ব্যবহার করুন) |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **সিস্টেম।টেক্সট।জেসন** | অন্তর্নির্মিত JSON সিরিয়ালাইজেশন |
| **Newtonsoft.Json** | লিগ্যাসি JSON (এখনও ব্যাপকভাবে ব্যবহৃত) |
| **সেরিলগ** | স্ট্রাকচার্ড লগিং |
| **NLog** | লগিং ফ্রেমওয়ার্ক |
| **পলি** | স্থিতিস্থাপকতা এবং পুনরায় চেষ্টা করার নীতি |
| **মিডিয়াটআর** | মধ্যস্থতাকারী প্যাটার্ন (CQRS) |
| **অটোম্যাপার** | অবজেক্ট-টু-অবজেক্ট ম্যাপিং |
| **ফ্লুয়েন্ট ভ্যালিডেশন** | বৈধতা লাইব্রেরি |
| **ম্যাস ট্রানজিট** | বার্তা বাস (RabbitMQ, Azure SB) |
| **হ্যাংফায়ার** | পটভূমি কাজের প্রক্রিয়াকরণ |
| **Quartz.NET** | কাজের সময়সূচী |
| **স্পেক্টার.কনসোল** | সুন্দর কনসোল অ্যাপস |
| **কমান্ডলাইনপার্সার** | CLI যুক্তি পার্সিং |
---

## ক্লাউড এবং অ্যাজুর ইন্টিগ্রেশন
| সেবা | উদ্দেশ্য |
|---------|---------|
| **আজিউর ফাংশন** | সার্ভারহীন |
| **.NET** এর জন্য Azure SDK | সমস্ত Azure পরিষেবা |
| **.NET** এর জন্য AWS SDK | AWS পরিষেবা |
| **গুগল ক্লাউড .নেট** | GCP পরিষেবা |
| ** Azure Cosmos DB** | NoSQL ডাটাবেস |
| **আজিউর সার্ভিস বাস** | মেসেজিং |
| **আজিউর কী ভল্ট** | গোপন ব্যবস্থাপনা |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **স্বয়ংসম্পূর্ণ** | বান্ডেল .NET রানটাইম |
| **ফ্রেমওয়ার্ক-নির্ভর** | .NET ইনস্টল করা প্রয়োজন |
| **একক ফাইল প্রকাশ** | `dotnet publish /p:PublishSingleFile=true`|
| **নেটিভ AOT** | `PublishAot=true`(কোন JIT প্রয়োজন নেই) |
| **ডকার** | `mcr.microsoft.com/dotnet/aspnet`|
| ** Azure অ্যাপ পরিষেবা** | PaaS স্থাপনা |
| **AWS Lambda** | সার্ভারহীন |
| **IIS** | উইন্ডোজ হোস্টিং |
| **কেস্ট্রেল** | অন্তর্নির্মিত ক্রস-প্ল্যাটফর্ম ওয়েব সার্ভার |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## সারাংশ
C# এবং .NET সবচেয়ে উৎপাদনশীল বাস্তুতন্ত্রের একটি অফার করে। স্ট্যান্ডার্ড স্ট্যাক হল: **.NET 8+** রানটাইম হিসাবে, ওয়েবের জন্য **ASP.NET কোর**, **এন্টিটি ফ্রেমওয়ার্ক কোর** বা **ড্যাপার** ডেটা অ্যাক্সেসের জন্য, **xUnit + Moq** পরীক্ষার জন্য, **ভিজ্যুয়াল স্টুডিও** বা **রাইডার** IDE হিসেবে, এবং **NuGet** প্যাকেজগুলির জন্য। রেকর্ড, প্যাটার্ন ম্যাচিং, বাতিলযোগ্য রেফারেন্স প্রকার এবং ন্যূনতম API সহ আধুনিক C# সংক্ষিপ্ত এবং অভিব্যক্তিপূর্ণ। **নেটিভ AOT** সংকলন ব্লেজিং-ফাস্ট স্টার্টআপ এবং ছোট বাইনারি সক্ষম করে। ইকোসিস্টেম এন্টারপ্রাইজ, ক্লাউড (আজিউর), গেম ডেভেলপমেন্ট (ইউনিটি, গডট) এবং ক্রস-প্ল্যাটফর্ম অ্যাপ্লিকেশনে উৎকর্ষ লাভ করে।