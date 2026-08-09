---
# मेटाडेटा
शीर्षक: "सी#"
विवरण: "सी# प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [csharp, प्रोग्रामिंग-भाषा, वाक्यविन्यास, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "29 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# सी#
C# (उच्चारण "सी-शार्प") एक आधुनिक, ऑब्जेक्ट-ओरिएंटेड, टाइप-सुरक्षित प्रोग्रामिंग भाषा है जिसे माइक्रोसॉफ्ट द्वारा एंडर्स हेजलबर्ग के नेतृत्व में विकसित किया गया था और पहली बार 2002 में जारी किया गया था। यह .NET प्लेटफ़ॉर्म पर चलता है और इसे विज़ुअल बेसिक की उत्पादकता के साथ C++ की शक्ति को संयोजित करने के लिए डिज़ाइन किया गया था। आज, C# एक बहुमुखी, क्रॉस-प्लेटफ़ॉर्म भाषा है जिसका उपयोग वेब एप्लिकेशन (ASP.NET), डेस्कटॉप सॉफ़्टवेयर (Windows), गेम डेवलपमेंट (यूनिटी), मोबाइल ऐप्स (MAUI), क्लाउड सर्विसेज (Azure) और बहुत कुछ के लिए किया जाता है।
C# ने लगातार अन्य भाषाओं - LINQ, async/await, रिकॉर्ड्स, पैटर्न मिलान - से सर्वोत्तम विचारों को अवशोषित किया है, जिससे यह उपलब्ध सबसे अधिक सुविधा संपन्न और डेवलपर-अनुकूल भाषाओं में से एक बन गई है।
---

## सी# क्यों मायने रखता है
- **यूनिटी गेम इंजन**: यूनिटी के लिए प्राथमिक भाषा, डेवलपर गणना के अनुसार दुनिया का सबसे लोकप्रिय गेम इंजन।
- **उद्यम विकास**: ASP.NET कोर उपलब्ध सबसे तेज़ वेब फ्रेमवर्क में से एक है (टेकएम्पॉवर बेंचमार्क में लगातार शीर्ष पर है)।
- **क्रॉस-प्लेटफ़ॉर्म**: .NET 5+ विंडोज़, मैकओएस और लिनक्स पर चलता है। अब केवल विंडोज़ नहीं।
- **उत्पादकता**: उत्कृष्ट आईडीई समर्थन (विजुअल स्टूडियो, राइडर), मजबूत प्रकार की प्रणाली और आधुनिक सिंटैक्स विशेषताएं।
- **async/await अग्रणी**: C# ने 2012 में async/await की शुरुआत की - अन्य भाषाओं द्वारा इस पैटर्न को अपनाने से कई साल पहले।
- **LINQ**: भाषा-एकीकृत क्वेरी आपको किसी भी डेटा स्रोत के विरुद्ध सीधे C# में SQL जैसी क्वेरी लिखने की सुविधा देती है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **विंडोज एसोसिएशन** | ऐतिहासिक रूप से विंडोज़ से जुड़ा हुआ; धारणा वास्तविकता से पीछे है | .NET 6+ पूरी तरह से क्रॉस-प्लेटफॉर्म है |
| **जावा से छोटा पारिस्थितिकी तंत्र** | Maven/PyPI | की तुलना में कम तृतीय-पक्ष लाइब्रेरीज़ नुगेट बढ़ रहा है; कई जावा पुस्तकालयों में C# समकक्ष हैं |
| **स्टार्टअप में कम आम** | सिलिकॉन वैली की तुलना में उद्यम में अधिक लोकप्रिय | क्लाउड-नेटिव माइक्रोसर्विसेज के लिए गो, रस्ट, नोड.जेएस |
| **मोबाइल (MAUI)** | Xamarin/MAUI नेटिव या फ़्लटर | की तुलना में कम परिपक्व है जटिल मोबाइल ऐप्स के लिए देशी स्विफ्ट/कोटलिन या फ़्लटर का उपयोग करें |
| **लिनक्स जीयूआई** | Linux पर सीमित देशी GUI विकल्प | वेब-आधारित यूआई (ब्लेज़र) या एवलोनिया | का उपयोग करें
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
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

### ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग
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

### रिकॉर्ड्स (सी# 9+) - अपरिवर्तनीय डेटा प्रकार
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

### LINQ - भाषा-एकीकृत क्वेरी
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

### एसिंक/प्रतीक्षा करें
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

### पैटर्न मिलान (सी# 7-13)
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

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक
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

### प्रतिनिधि, घटनाएँ, और लैम्ब्डा अभिव्यक्तियाँ
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

### कस्टम अपवाद पदानुक्रम
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

### ऑपरेटर ओवरलोडिंग
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

## समवर्ती एवं समांतरता
### एसिंक/प्रतीक्षा आंतरिक
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

### समानांतर LINQ और कार्य समानांतर लाइब्रेरी
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### .csproj फ़ाइल
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

### xUnit के साथ परीक्षण
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

### सीआई/सीडी पाइपलाइन
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

## अंतरसंचालनीयता
### पी/इनवोक - सी लाइब्रेरीज़ को कॉल करना
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

### सी++/सीएलआई इंटरऑप
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

## डिज़ाइन पैटर्न
### बिल्डर पैटर्न (धाराप्रवाह एपीआई)
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

### प्रतिनिधियों के साथ रणनीति पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

## तैनाती
### डॉकरफ़ाइल
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

### प्लेटफ़ॉर्म-विशिष्ट परिनियोजन
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

## .NET पारिस्थितिकी तंत्र
### फ्रेमवर्क और प्लेटफार्म
| ढाँचा | डोमेन | विवरण |
|----|-------|----|
| **एएसपी.नेट कोर** | वेब | एपीआई और वेब ऐप्स के लिए उच्च-प्रदर्शन वेब फ्रेमवर्क |
| **ब्लेज़र** | वेब (फ्रंटएंड) | जावास्क्रिप्ट | के बजाय C# के साथ इंटरैक्टिव वेब यूआई बनाएं
| **एंटिटी फ्रेमवर्क कोर** | ओआरएम | LINQ के साथ डेटाबेस का उपयोग; कोड-प्रथम माइग्रेशन |
| **एकता** | खेल | दुनिया का सबसे लोकप्रिय गेम इंजन (सी# स्क्रिप्टिंग) |
| **.नेट माउई** | मोबाइल/डेस्कटॉप | iOS, Android, macOS, Windows के लिए क्रॉस-प्लेटफ़ॉर्म ऐप्स |
| **एवलोनिया** | डेस्कटॉप | क्रॉस-प्लेटफ़ॉर्म डेस्कटॉप यूआई (जैसे सभी प्लेटफ़ॉर्म के लिए WPF) |
### निर्माण और पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **डॉटनेट सीएलआई** | कमांड लाइन से बनाएं, चलाएं, परीक्षण करें, प्रकाशित करें |
| **नुगेट** | पैकेज मैनेजर |
| **एमएसबिल्ड** | अंतर्निहित निर्माण प्रणाली |
| **विजुअल स्टूडियो/राइडर** | आईडीई |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## सी# भाषा संस्करण
| संस्करण | वर्ष | प्रमुख विशेषताएँ |
|------|------|----------------|
| सी# 7 | 2017 | पैटर्न मिलान, टुपल्स,`out`वेरिएबल, स्थानीय फ़ंक्शन |
| सी# 8 | 2019 | निरर्थक संदर्भ प्रकार,`switch`अभिव्यक्ति, एसिंक स्ट्रीम |
| सी#9 | 2020 | **रिकॉर्ड**, शीर्ष-स्तरीय विवरण,`init`संपत्तियाँ |
| सी#10 | 2021 | रिकॉर्ड संरचनाएं, वैश्विक `using`, फ़ाइल-स्कोप्ड नेमस्पेस |
| सी#11 | 2022 | कच्चे स्ट्रिंग अक्षर, सूची पैटर्न,`required`सदस्य, सामान्य गणित |
| सी#12 | 2023 | प्राथमिक कंस्ट्रक्टर, संग्रह अभिव्यक्ति, इनलाइन सरणियाँ |
| सी#13 | 2024 |  __संरक्षित_5__ संग्रह, नए लॉक प्रकार, प्रथम श्रेणी स्पैन |
---

## सी# का उपयोग कब करें
| परिदृश्य | सी# क्यों | बेहतर विकल्प |
|---|--------|-----|
| खेल विकास (एकता) | मानक यूनिटी स्क्रिप्टिंग भाषा | -- |
| एंटरप्राइज़ वेब बैकएंड | ASP.NET कोर तेज़, परिपक्व, अच्छी तरह से समर्थित है | जावा (स्प्रिंग बूट) |
| विंडोज़ डेस्कटॉप अनुप्रयोग | WPF, WinForms, WinUI परिपक्व हैं | -- |
| क्रॉस-प्लेटफ़ॉर्म डेस्कटॉप | एवलोनिया या माउई | इलेक्ट्रॉन (वेब-आधारित) |
| वेब फ्रंटएंड (ब्लेज़र) | पूर्ण-स्टैक C# - कोई जावास्क्रिप्ट की आवश्यकता नहीं | समृद्ध एसपीए पारिस्थितिकी तंत्र के लिए प्रतिक्रिया/व्यू/कोणीय |
| क्लाउड सेवाएँ (एज़्योर) | डीप एज़्योर एकीकरण | -- |
| मोबाइल ऐप्स (MAUI) | C# | के साथ क्रॉस-प्लेटफ़ॉर्म फ़्लटर, रिएक्ट नेटिव, या नेटिव स्विफ्ट/कोटलिन |
| एआई/एमएल | ML.NET के साथ संभव | पायथन (अत्यधिक पसंदीदा) |
| सीएलआई उपकरण/स्क्रिप्ट | संभव लेकिन क्रियात्मक | जाओ, जंग, अजगर |
---

## सारांश
C# उत्कृष्ट टूलींग और एक मजबूत पारिस्थितिकी तंत्र के साथ एक परिष्कृत, आधुनिक, सामान्य प्रयोजन वाली भाषा है। यह उद्यम विकास, खेल विकास (यूनिटी), और क्रॉस-प्लेटफ़ॉर्म अनुप्रयोगों में उत्कृष्टता प्राप्त करता है। भाषा तेजी से विकसित हुई है - आधुनिक C# संक्षिप्त, अभिव्यंजक और प्रकार-सुरक्षित है। हालाँकि इसमें जावा या पायथन का पारिस्थितिकी तंत्र आकार नहीं है, .NET की गुणवत्ता और स्थिरता C# को अनुप्रयोगों की एक विस्तृत श्रृंखला के लिए एक उत्पादक और आनंददायक भाषा बनाती है।