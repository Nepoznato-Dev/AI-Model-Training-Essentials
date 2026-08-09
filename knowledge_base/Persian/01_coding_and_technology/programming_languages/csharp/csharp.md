---
# فراداده
عنوان: "C#"
توضیحات: "مرجع جامع برای زبان برنامه نویسی C# که شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن است."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [csharp، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "29 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
#C#
سی شارپ (با تلفظ C-sharp) یک زبان برنامه نویسی مدرن، شی گرا و ایمن است که توسط مایکروسافت تحت رهبری آندرس هیلسبرگ توسعه یافته و اولین بار در سال 2002 منتشر شد. این زبان بر روی پلت فرم دات نت اجرا می شود و برای ترکیب قدرت C++ با بهره وری ویژوال بیسیک طراحی شده است. امروزه سی شارپ یک زبان همه کاره و چند پلتفرمی است که برای برنامه های کاربردی وب (ASP.NET)، نرم افزار دسکتاپ (ویندوز)، توسعه بازی (Unity)، برنامه های موبایل (MAUI)، خدمات ابری (Azure) و غیره استفاده می شود.
C# به طور پیوسته بهترین ایده‌ها را از زبان‌های دیگر جذب کرده است - LINQ، async/wait، رکوردها، تطبیق الگوها - آن را به یکی از غنی‌ترین و توسعه‌دهنده‌ترین زبان‌های موجود تبدیل کرده است.
---

## چرا C# مهم است
- **موتور بازی Unity**: زبان اصلی Unity، محبوب ترین موتور بازی جهان بر اساس تعداد توسعه دهندگان.
- **توسعه سازمانی**: ASP.NET Core یکی از سریع ترین چارچوب های وب موجود است (به طور مداوم از معیارهای TechEmpower برتر است).
- **Cross-platform**: .NET 5+ روی Windows، macOS و Linux اجرا می شود. دیگر فقط ویندوز نیست.
- ** بهره وری **: پشتیبانی عالی از IDE (Visual Studio، Rider)، سیستم نوع قوی و ویژگی های نحو مدرن.
- **async/await pioneer**: C# در سال 2012 async/await را معرفی کرد – سالها قبل از اینکه زبان های دیگر این الگو را بپذیرند.
- **LINQ**: پرس و جوی یکپارچه زبان به شما امکان می دهد پرس و جوهایی شبیه به SQL را مستقیماً در سی شارپ در برابر هر منبع داده بنویسید.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **وابسته ویندوز** | از لحاظ تاریخی به ویندوز گره خورده است. ادراک از واقعیت عقب می ماند | NET 6+ کاملاً چند پلتفرمی است |
| **اکوسیستم کوچکتر از جاوا** | کتابخانه های شخص ثالث کمتر از Maven/PyPI | NuGet در حال رشد است. بسیاری از کتابخانه های جاوا دارای معادل های سی شارپ |
| **در استارتاپ ها کمتر رایج است** | در شرکت های تجاری محبوب تر از دره سیلیکون | برو، Rust، Node.js برای میکروسرویس های بومی ابری |
| **موبایل (MAUI)** | Xamarin/MAUI نسبت به Native یا Flutter | بالغ کمتر است از Swift/Kotlin یا Flutter بومی برای برنامه های تلفن همراه پیچیده استفاده کنید |
| ** رابط کاربری گرافیکی لینوکس ** | گزینه های محدود بومی رابط کاربری گرافیکی در لینوکس | از UI های مبتنی بر وب (Blazor) یا Avalonia | استفاده کنید
---

## اصول نحو
### ساختار اساسی
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace MyApp;

// Top-level statements (C# 9+) — no Main method needed for simple programs
Console.WriteLine("Hello, World!");

var name = "Alice";
var age = 30;
var scores = new List<double> { 9.5, 8.0, 7.5 };

// String interpolation
Console.WriteLine($"Name: {name}, Age: {age}, Average: {scores.Average():F1}");
```

### برنامه نویسی شی گرا
```csharp
public abstract class Animal
{
    public string Name { get; }
    protected Animal(string name) => Name = name;
    public abstract string Speak();
}

public class Dog : Animal
{
    public Dog(string name) : base(name) { }
    public override string Speak() => $"{Name} says woof";
}

public interface ISerializable
{
    string ToJson();
}

public class User : ISerializable, IComparable<User>
{
    public string Name { get; init; }
    public int Age { get; init; }
    
    public string ToJson() => $"{{\"name\":\"{Name}\",\"age\":{Age}}}";
    public int CompareTo(User? other) => Age.CompareTo(other?.Age ?? 0);
}
```

### رکوردها (C# 9+) - انواع داده های تغییرناپذیر
```csharp
public record Point(double X, double Y)
{
    public double DistanceTo(Point other) =>
        Math.Sqrt(Math.Pow(X - other.X, 2) + Math.Pow(Y - other.Y, 2));
}

var p1 = new Point(3.0, 4.0);
var p2 = new Point(0.0, 0.0);
Console.WriteLine(p1.DistanceTo(p2));  // 5.0

var p3 = p1 with { X = 6.0 };  // New record: Point(6.0, 4.0)
Console.WriteLine(p1 == p3);   // False (different X)
```

### LINQ - پرس و جو یکپارچه با زبان
```csharp
var users = new List<User>
{
    new User { Name = "Alice", Age = 30 },
    new User { Name = "Bob", Age = 25 },
    new User { Name = "Charlie", Age = 35 },
};

// Method syntax
var adults = users.Where(u => u.Age >= 28).OrderBy(u => u.Name).Select(u => u.Name).ToList();

// Query syntax (SQL-like)
var query = from u in users where u.Age >= 28 orderby u.Name select u.Name;

// Grouping and aggregation
var byAgeGroup = users.GroupBy(u => u.Age < 30 ? "Under 30" : "30 and over");
var averageAge = users.Average(u => u.Age);
```

### Async/Await
```csharp
public async Task<string> FetchPageAsync(string url)
{
    using var client = new HttpClient();
    return await client.GetStringAsync(url);
}

public async Task FetchAllAsync(IEnumerable<string> urls)
{
    var tasks = urls.Select(url => FetchPageAsync(url));
    var results = await Task.WhenAll(tasks);
    foreach (var result in results)
        Console.WriteLine($"Fetched {result.Length} characters");
}

public async Task DownloadAsync(string url, CancellationToken ct)
{
    using var client = new HttpClient();
    var data = await client.GetByteArrayAsync(url, ct);
    await File.WriteAllBytesAsync("download.bin", data, ct);
}
```

### تطبیق الگو (C# 7-13)
```csharp
public string Describe(object obj) => obj switch
{
    int n when n > 0 => $"Positive integer: {n}",
    int n => $"Non-positive integer: {n}",
    string s => $"String of length {s.Length}",
    null => "Nothing",
    _ => "Something else"
};

// Property patterns
public decimal CalculateDiscount(Customer c) => c switch
{
    { IsVip: true, TotalSpent: > 10000 } => 0.20m,
    { IsVip: true } => 0.10m,
    { TotalSpent: > 5000 } => 0.05m,
    _ => 0m
};

// List patterns (C# 11+)
public string Classify(int[] numbers) => numbers switch
{
    [] => "Empty",
    [var single] => $"Single: {single}",
    [var first, .., var last] => $"First: {first}, Last: {last}",
};
```

---

## نحو و الگوهای پیشرفته
### ژنریک
```csharp
// Generic class with constraints
public class Repository<T> where T : class, IEntity
{
    private readonly List<T> _items = new();
    
    public void Add(T item) => _items.Add(item);
    public T? FindById(int id) => _items.FirstOrDefault(i => i.Id == id);
    public IEnumerable<T> Find(Func<T, bool> predicate) => _items.Where(predicate);
}

// Generic constraints
public T Max<T>(T a, T b) where T : IComparable<T> => a.CompareTo(b) >= 0 ? a : b;

// Covariance and contravariance
public interface IProducer<out T>  // covariant — can return T or derived
{
    T Produce();
}

public interface IConsumer<in T>  // contravariant — can accept T or base
{
    void Consume(T item);
}
```

### نمایندگان، رویدادها و عبارات لامبدا
```csharp
// Delegate — type-safe function pointer
public delegate double MathOperation(double a, double b);

MathOperation add = (a, b) => a + b;
MathOperation multiply = (a, b) => a * b;
Console.WriteLine(add(3, 5));       // 8
Console.WriteLine(multiply(3, 5));  // 15

// Built-in delegates
Func<int, int, int> addFunc = (a, b) => a + b;
Action<string> print = s => Console.WriteLine(s);
Predicate<int> isPositive = n => n > 0;

// Events — type-safe pub/sub
public class Button
{
    public event EventHandler<ClickEventArgs>? Clicked;
    
    public void OnClick() => Clicked?.Invoke(this, new ClickEventArgs(DateTime.Now));
}

public class ClickEventArgs : EventArgs
{
    public DateTime Timestamp { get; }
    public ClickEventArgs(DateTime ts) => Timestamp = ts;
}

// Usage
var button = new Button();
button.Clicked += (sender, args) => Console.WriteLine($"Clicked at {args.Timestamp}");
button.OnClick();
```

### سلسله مراتب استثنای سفارشی
```csharp
public class AppException : Exception
{
    public string Code { get; }
    public AppException(string message, string code = "UNKNOWN")
        : base(message) { Code = code; }
}

public class ValidationException : AppException
{
    public string Field { get; }
    public ValidationException(string field, string message)
        : base($"Validation failed for '{field}': {message}", "VALIDATION")
    { Field = field; }
}

public class NotFoundException : AppException
{
    public NotFoundException(string resource, object id)
        : base($"{resource} not found: {id}", "NOT_FOUND") { }
}

// Usage
try { throw new ValidationException("email", "must contain @"); }
catch (ValidationException ex) { Console.WriteLine($"Bad input: {ex.Field}"); }
catch (AppException ex) { Console.WriteLine($"Error [{ex.Code}]: {ex.Message}"); }
```

### بارگذاری بیش از حد اپراتور
```csharp
public record struct Vector2D(double X, double Y)
{
    public static Vector2D operator +(Vector2D a, Vector2D b) => new(a.X + b.X, a.Y + b.Y);
    public static Vector2D operator -(Vector2D a, Vector2D b) => new(a.X - b.X, a.Y - b.Y);
    public static Vector2D operator *(Vector2D v, double s) => new(v.X * s, v.Y * s);
    public static Vector2D operator *(double s, Vector2D v) => v * s;
    public static Vector2D operator -(Vector2D v) => new(-v.X, -v.Y);
    
    public double Magnitude => Math.Sqrt(X * X + Y * Y);
    
    public static implicit operator (double X, double Y)(Vector2D v) => (v.X, v.Y);
}

var v1 = new Vector2D(3, 4);
var v2 = new Vector2D(1, 2);
Console.WriteLine(v1 + v2);        // (4, 6)
Console.WriteLine(v1 * 2);         // (6, 8)
Console.WriteLine(v1.Magnitude);   // 5
```

---

## همزمانی و موازی
### ناهمگام/انتظار داخلی
```csharp
// The state machine behind async/await
// When you write async/await, the compiler generates a state machine
// that suspends and resumes the method at each await point.

// Parallel async with structured concurrency
public async Task ProcessBatchAsync(IEnumerable<string> urls)
{
    using var semaphore = new SemaphoreSlim(10);  // Limit concurrency to 10
    var tasks = urls.Select(async url =>
    {
        await semaphore.WaitAsync();
        try
        {
            using var client = new HttpClient();
            var data = await client.GetStringAsync(url);
            Console.WriteLine($"Fetched {data.Length} chars from {url}");
        }
        finally
        {
            semaphore.Release();
        }
    });
    await Task.WhenAll(tasks);
}

// Channels — producer/consumer pattern
public async Task ProcessWithChannel()
{
    var channel = Channel.CreateBounded<string>(new BoundedChannelOptions(100)
    {
        FullMode = BoundedChannelFullMode.Wait
    });

    // Producer
    _ = Task.Run(async () =>
    {
        for (int i = 0; i < 1000; i++)
        {
            await channel.Writer.WriteAsync($"item-{i}");
            await Task.Delay(10);
        }
        channel.Writer.Complete();
    });

    // Consumer
    await foreach (var item in channel.Reader.ReadAllAsync())
    {
        Console.WriteLine($"Processing: {item}");
    }
}
```

### LINQ موازی و کتابخانه موازی کار
```csharp
// PLINQ — parallel data processing
var numbers = Enumerable.Range(1, 10_000_000);
var primes = numbers.AsParallel()
    .Where(n => IsPrime(n))
    .ToList();

// Parallel.ForEach — CPU-bound work across cores
Parallel.ForEach(files, new ParallelOptions { MaxDegreeOfParallelism = 4 }, file =>
{
    var content = File.ReadAllText(file);
    ProcessContent(content);
});

// ValueTask — allocation-free async for hot paths
public async ValueTask<int> GetCountAsync()
{
    if (_cache != null) return _cache.Count;  // Synchronous fast path
    return await LoadFromDatabaseAsync();      // Async slow path
}
```

---

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
```
MyCSharpProject/
├── src/
│   ├── MyProject/
│   │   ├── MyProject.csproj
│   │   ├── Program.cs
│   │   ├── Models/
│   │   ├── Services/
│   │   └── Controllers/
│   └── MyProject.Tests/
│       ├── MyProject.Tests.csproj
│       └── Services/
├── MyProject.sln
├── .editorconfig
├── Directory.Build.props
├── .github/workflows/ci.yml
└── README.md
```

### فایل csproj
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.Extensions.Logging" Version="8.0.0" />
  </ItemGroup>
</Project>
```

### تست با xUnit
```csharp
public class UserServiceTests
{
    private readonly Mock<IUserRepository> _mockRepo;
    private readonly UserService _service;

    public UserServiceTests()
    {
        _mockRepo = new Mock<IUserRepository>();
        _service = new UserService(_mockRepo.Object);
    }

    [Fact]
    public void Create_ValidData_ReturnsUser()
    {
        _mockRepo.Setup(r => r.Save(It.IsAny<User>()))
            .ReturnsAsync(new User { Id = 1, Name = "Alice" });

        var user = _service.Create("Alice", "alice@example.com");

        Assert.Equal("Alice", user.Name);
        _mockRepo.Verify(r => r.Save(It.IsAny<User>()), Times.Once);
    }

    [Theory]
    [InlineData("")]
    [InlineData("  ")]
    [InlineData(null)]
    public void Create_InvalidName_Throws(string? name)
    {
        Assert.Throws<ArgumentException>(() => _service.Create(name!, "a@b.com"));
    }
}
```

### خط لوله CI/CD
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: "8.0.x"
      - run: dotnet restore
      - run: dotnet build --no-restore
      - run: dotnet test --no-build --verbosity normal
      - run: dotnet publish src/MyProject -c Release -o publish
```

---

## قابلیت همکاری
### P/Invoke - فراخوانی کتابخانه های C
```csharp
using System.Runtime.InteropServices;

// Call C functions from native libraries
[DllImport("libc", SetLastError = true)]
private static extern int getpid();

[DllImport("user32.dll", CharSet = CharSet.Unicode)]
private static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);

// Modern approach — LibraryImport (C# 12+, source-generated)
[LibraryImport("nativeLib.dll")]
private static partial int Add(int a, int b);

Console.WriteLine($"Process ID: {getpid()}");
```

### C++/CLI Interop
```csharp
// Using SWIG to wrap C++ for C#
// 1. Define interface file
// 2. Run SWIG to generate C# wrapper
// 3. Use the generated C# classes directly

// Example: wrapping a C++ class
// geometry.h: class Circle { public: double Area() const; };
// After SWIG:
// var circle = new Circle(5.0);
// Console.WriteLine(circle.Area());
```

---

## الگوهای طراحی
### Builder Pattern (Fluent API)
```csharp
public class HttpRequest
{
    public string Method { get; init; } = "GET";
    public string Url { get; init; } = "";
    public Dictionary<string, string> Headers { get; init; } = new();
    public string? Body { get; init; }
}

public class HttpRequestBuilder
{
    private string _method = "GET";
    private string _url = "";
    private readonly Dictionary<string, string> _headers = new();
    private string? _body;

    public HttpRequestBuilder Method(string m) { _method = m; return this; }
    public HttpRequestBuilder Url(string u) { _url = u; return this; }
    public HttpRequestBuilder Header(string k, string v) { _headers[k] = v; return this; }
    public HttpRequestBuilder Body(string b) { _body = b; return this; }
    public HttpRequest Build() => new() { Method = _method, Url = _url, Headers = _headers, Body = _body };
}

var request = new HttpRequestBuilder()
    .Method("POST").Url("/api/users")
    .Header("Content-Type", "application/json")
    .Body("{\"name\":\"Alice\"}")
    .Build();
```

### الگوی استراتژی با نمایندگان
```csharp
public class DataProcessor
{
    private readonly Func<string, string> _transform;

    public DataProcessor(Func<string, string> transform) => _transform = transform;

    public string Process(string input) => _transform(input);
}

// Usage — swap strategies with lambdas
var upper = new DataProcessor(s => s.ToUpper());
var reversed = new DataProcessor(s => new string(s.Reverse().ToArray()));

Console.WriteLine(upper.Process("hello"));     // "HELLO"
Console.WriteLine(reversed.Process("hello"));  // "olleh"
```

---

## عملکرد و بهینه سازی
### ابزارهای پروفایل
```bash
# dotnet-trace — CPU and event tracing
dotnet tool install -g dotnet-trace
dotnet-trace collect --process-id <PID>

# dotnet-counters — real-time performance counters
dotnet-counters monitor --process-id <PID>

# BenchmarkDotNet — micro-benchmarking
dotnet add package BenchmarkDotNet
```

```csharp
// BenchmarkDotNet example
[MemoryDiagnoser]
public class StringBenchmarks
{
    [Benchmark(Baseline = true)]
    public string Concatenation()
    {
        string result = "";
        for (int i = 0; i < 100; i++) result += i.ToString();
        return result;
    }

    [Benchmark]
    public string StringBuilder()
    {
        var sb = new StringBuilder();
        for (int i = 0; i < 100; i++) sb.Append(i);
        return sb.ToString();
    }
}
// Run: dotnet run -c Release
```

---

## استقرار
### Dockerfile
```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish src/MyProject -c Release -o /app

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app .
EXPOSE 8080
ENTRYPOINT ["dotnet", "MyProject.dll"]
```

### استقرار ویژه پلتفرم
```bash
# Self-contained deployment (no .NET runtime needed on target)
dotnet publish -c Release -r linux-x64 --self-contained true

# Single-file executable
dotnet publish -c Release -r win-x64 -p:PublishSingleFile=true

# Azure App Service
az webapp up --name my-app --runtime DOTNET:8.0

# AWS Lambda
dotnet lambda deploy-function my-function
```

---

## اکوسیستم دات نت
### چارچوب ها و پلتفرم ها
| چارچوب | دامنه | توضیحات |
|-----------|--------|-------------|
| **ASP.NET Core** | وب | چارچوب وب با کارایی بالا برای API ها و برنامه های وب |
| **بلازور** | وب (فرانت اند) | بجای جاوا اسکریپت، رابط های وب تعاملی با C# بسازید
| ** هسته چارچوب نهاد ** | ORM | دسترسی به پایگاه داده با LINQ؛ مهاجرت های کد اول |
| **وحدت** | بازی ها | محبوب ترین موتور بازی سازی جهان (سی شارپ اسکریپت) |
| **.NET MAUI** | موبایل/رومیزی | برنامه های چند پلتفرمی برای iOS، Android، macOS، Windows |
| **آوالونیا** | رومیزی | رابط کاربری دسکتاپ کراس پلتفرم (مانند WPF برای همه پلتفرم ها) |
### مدیریت ساخت و بسته
| ابزار | هدف |
|------|---------|
| **dotnet CLI** | ساخت، اجرا، تست، انتشار از خط فرمان |
| **NuGet** | مدیر بسته |
| **MSBuild** | سیستم ساخت زیرین |
| **ویژوال استودیو / رایدر** | IDE ها |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## نسخه های زبان C#
| نسخه | سال | ویژگی های کلیدی |
|---------|------|-------------|
| سی شارپ 7 | 2017 | تطبیق الگو، تاپل ها، متغیرهای `out`، توابع محلی |
| سی شارپ 8 | 2019 | انواع مرجع قابل تهی، عبارات `switch`، جریان های ناهمگام |
| سی شارپ 9 | 2020 | **سوابق**، بیانیه های سطح بالا، ویژگی های`init`|
| سی شارپ 10 | 2021 | ساختارهای ضبط، جهانی `using`، فضاهای نام با دامنه فایل |
| سی شارپ 11 | 2022 | حرفهای رشته خام، الگوهای فهرست، اعضای `required`، ریاضی عمومی |
| سی شارپ 12 | 2023 | سازنده های اولیه، عبارات مجموعه، آرایه های درون خطی |
| سی شارپ 13 | 2024 |  مجموعه های `params`، انواع قفل های جدید، دهانه های درجه یک |
---

## چه زمانی از سی شارپ استفاده کنیم
| سناریو | چرا سی شارپ | جایگزین بهتر |
|----------|--------|-------------------|
| توسعه بازی (یونیتی) | زبان برنامه نویسی استاندارد Unity | -- |
| پشتیبان های وب سازمانی | ASP.NET Core سریع، بالغ، به خوبی پشتیبانی می شود | جاوا (چکمه بهاره) |
| برنامه های دسکتاپ ویندوز | WPF، WinForms، WinUI بالغ هستند | -- |
| دسکتاپ کراس پلتفرم | آوالونیا یا MAUI | الکترون (مبتنی بر وب) |
| وب سایت (Blazor) | فول پشته سی شارپ — بدون نیاز به جاوا اسکریپت | React/Vue/Angular برای اکوسیستم های غنی تر SPA |
| خدمات ابری (آژور) | ادغام Deep Azure | -- |
| برنامه های موبایل (MAUI) | کراس پلتفرم با سی شارپ | Flutter، React Native یا Swift/Kotlin بومی |
| AI/ML | با ML.NET امکان پذیر است | پایتون (بیشتر ترجیح داده می شود) |
| ابزار / اسکریپت های CLI | ممکن است اما پرمخاطب | برو، رست، پایتون |
---

## خلاصه
سی شارپ یک زبان پیشرفته، مدرن و همه منظوره با ابزار عالی و اکوسیستم قوی است. در توسعه سازمانی، توسعه بازی (Unity) و برنامه های کاربردی بین پلتفرم برتری دارد. زبان به سرعت تکامل یافته است - سی شارپ مدرن مختصر، رسا و ایمن است. در حالی که اندازه اکوسیستم جاوا یا پایتون را ندارد، کیفیت و ثبات دات نت C# را به زبانی سازنده و لذت بخش برای طیف وسیعی از برنامه ها تبدیل کرده است.