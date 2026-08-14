<!--
---
# Metadata
title: "C#"
description: "Comprehensive reference for the C# programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [csharp, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# C#
C# (diucapkan "C-sharp") adalah bahasa pemrograman modern, berorientasi objek, dan aman untuk tipe yang dikembangkan oleh Microsoft di bawah kepemimpinan Anders Hejlsberg dan pertama kali dirilis pada tahun 2002. C# berjalan pada platform .NET dan dirancang untuk menggabungkan kekuatan C++ dengan produktivitas Visual Basic. Saat ini, C# adalah bahasa lintas platform serbaguna yang digunakan untuk aplikasi web (ASP.NET), perangkat lunak desktop (Windows), pengembangan game (Unity), aplikasi seluler (MAUI), layanan cloud (Azure), dan banyak lagi.
C# terus menyerap ide-ide terbaik dari bahasa lain — LINQ, async/await, record, pencocokan pola — menjadikannya salah satu bahasa paling kaya fitur dan ramah pengembang yang tersedia.
---

## Mengapa C# Penting
- **Mesin game Unity**: Bahasa utama untuk Unity, mesin game paling populer di dunia menurut jumlah pengembang.
- **Pengembangan perusahaan**: ASP.NET Core adalah salah satu kerangka web tercepat yang tersedia (secara konsisten berada di puncak tolok ukur TechEmpower).
- **Lintas platform**: .NET 5+ berjalan di Windows, macOS, dan Linux. Tidak lagi hanya untuk Windows.
- **Produktivitas**: Dukungan IDE luar biasa (Visual Studio, Rider), sistem tipe yang kuat, dan fitur sintaksis modern.
- **async/await Pioneer**: C# memperkenalkan async/await pada tahun 2012 — bertahun-tahun sebelum bahasa lain mengadopsi pola ini.
- **LINQ**: Kueri Terintegrasi Bahasa memungkinkan Anda menulis kueri mirip SQL langsung di C# terhadap sumber data apa pun.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Asosiasi Windows** | Secara historis terkait dengan Windows; persepsi tertinggal dari kenyataan | .NET 6+ sepenuhnya lintas platform |
| **Ekosistem lebih kecil dari Jawa** | Lebih sedikit perpustakaan pihak ketiga dibandingkan Maven/PyPI | NuGet sedang berkembang; banyak perpustakaan Java memiliki padanan C# |
| **Kurang umum di startup** | Lebih populer di kalangan perusahaan dibandingkan di Silicon Valley | Go, Rust, Node.js untuk layanan mikro cloud-native |
| **Seluler (MAUI)** | Xamarin/MAUI kurang matang dibandingkan native atau Flutter | Gunakan Swift/Kotlin atau Flutter asli untuk aplikasi seluler yang kompleks |
| **GUI Linux** | Opsi GUI asli terbatas di Linux | Gunakan UI berbasis web (Blazor) atau Avalonia |
---

## Dasar Sintaks
### Struktur Dasar
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

### Pemrograman Berorientasi Objek
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

### Catatan (C# 9+) — Tipe Data yang Tidak Dapat Diubah
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

### LINQ — Kueri Terintegrasi Bahasa
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

### Asinkron/Tunggu
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

### Pencocokan Pola (C# 7-13)
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

## Sintaks & Pola Tingkat Lanjut
### Generik
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

### Delegasi, Acara, dan Ekspresi Lambda
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

### Hirarki Pengecualian Khusus
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

### Operator Kelebihan Beban
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

## Konkurensi & Paralelisme
### async/menunggu Internal
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

### LINQ Paralel dan Perpustakaan Paralel Tugas
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek
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

### Berkas .csproj
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

### Menguji dengan xUnit
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

### Saluran CI/CD
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

## Interoperabilitas
### P/Invoke — Memanggil Perpustakaan C
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

### Interop C++/CLI
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

## Pola Desain
### Pola Pembuat (API Lancar)
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

### Pola Strategi dengan Delegasi
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

## Kinerja & Optimasi
### Alat Pembuatan Profil
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

## Penerapan
### File Docker
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

### Penerapan Khusus Platform
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

## Ekosistem .NET
### Kerangka dan Platform
| Kerangka | Domain | Deskripsi |
|-----------|--------|-------------|
| **ASP.NET Inti** | jaringan | Kerangka web berkinerja tinggi untuk API dan aplikasi web |
| **Blazor** | Web (bagian depan) | Bangun UI web interaktif dengan C#, bukan JavaScript |
| **Inti Kerangka Entitas** | ORM | Akses basis data dengan LINQ; migrasi kode pertama |
| **Persatuan** | Permainan | Mesin permainan terpopuler di dunia (skrip C#) |
| **.NET MAUI** | Seluler/Desktop | Aplikasi lintas platform untuk iOS, Android, macOS, Windows |
| **Avalonia** | Desktop | UI desktop lintas platform (seperti WPF untuk semua platform) |
### Pembuatan dan Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **CLI dotnet** | Bangun, jalankan, uji, publikasikan dari baris perintah |
| **NuGet** | Manajer paket |
| **MSBuild** | Sistem pembangunan yang mendasari |
| **Visual Studio / Pengendara** | IDE |
```bash
dotnet new webapi -n MyApi
dotnet build
dotnet run
dotnet add package Newtonsoft.Json
dotnet publish -c Release -r linux-x64
```

---

## Versi Bahasa C#
| Versi | Tahun | Fitur Utama |
|---------|------|-------------|
| C#7| 2017 | Pencocokan pola, tupel, variabel `out`, fungsi lokal |
| C#8| 2019 | Tipe referensi nullable, ekspresi `switch`, aliran asinkron |
| C#9| 2020 | **Catatan**, pernyataan tingkat atas, properti`init`|
| C#10 | 2021 | Rekam struct,`using`global, ruang nama cakupan file |
| C#11 | 2022 | Literal string mentah, pola daftar, anggota `required`, matematika generik |
| C#12| 2023 | Konstruktor utama, ekspresi koleksi, array inline |
| C#13| 2024 |  Koleksi `params`, tipe kunci baru, bentang kelas satu |
---

## Kapan Menggunakan C#
| Skenario | Mengapa C# | Alternatif Lebih Baik |
|----------|--------|-------------------|
| Pengembangan game (Persatuan) | Bahasa skrip Unity standar | -- |
| Backend web perusahaan | ASP.NET Core cepat, matang, didukung dengan baik | Java (Boot Musim Semi) |
| Aplikasi desktop Windows | WPF, WinForms, WinUI sudah matang | -- |
| Desktop lintas platform | Avalonia atau MAUI | Elektron (berbasis web) |
| Bagian depan web (Blazor) | C# tumpukan penuh — tidak memerlukan JavaScript | React/Vue/Angular untuk ekosistem SPA yang lebih kaya |
| Layanan cloud (Azure) | Integrasi Azure Mendalam | -- |
| Aplikasi seluler (MAUI) | Lintas platform dengan C# | Flutter, React Native, atau Swift/Kotlin |
| AI/ML | Mungkin dengan ML.NET | Python (sangat disukai) |
| Alat/skrip CLI | Mungkin tapi bertele-tele | Ayo, Karat, Python |
---

## Tanya Jawab Sintetis
### Q1: Apa perbedaan antara`class`dan`record`di C#?
**A:**`class`adalah tipe referensi dengan properti yang dapat diubah secara default — dua variabel dapat mereferensikan objek yang sama.`record`(C# 9+) adalah tipe referensi dengan kesetaraan berbasis nilai — dua catatan dengan data yang sama dianggap sama. Catatan memiliki properti init-only,`ToString`bawaan, dan mendukung ekspresi`with`untuk mutasi non-destruktif. Gunakan catatan untuk pembawa data (DTO, objek nilai); gunakan kelas untuk entitas kaya perilaku dengan identitas.
```csharp
// Class — reference equality, mutable
public class User { public string Name { get; set; } public int Age { get; set; } }
var u1 = new User { Name = "Alice", Age = 30 };
var u2 = u1;  // Same reference
u2.Name = "Bob";
Console.WriteLine(u1.Name);  // "Bob" — both point to same object

// Record — value equality, immutable by default
public record Person(string Name, int Age);
var p1 = new Person("Alice", 30);
var p2 = p1 with { Name = "Bob" };  // New record, p1 unchanged
Console.WriteLine(p1.Name);          // "Alice"
Console.WriteLine(p1 == new Person("Alice", 30));  // true — value equality
```

### Q2: Bagaimana cara kerja async/await dan`Task`secara internal?
**A:**`async/await`adalah gula sintaksis pada mesin status yang dihasilkan oleh kompiler. Saat Anda`await`dan`Task`, metode ini dibagi pada titik menunggu: semuanya sebelumnya dieksekusi secara sinkron, lalu sisanya didaftarkan sebagai kelanjutan. Thread dibebaskan untuk melakukan pekerjaan lain. `Task<T>`mewakili nilai masa depan. `ValueTask<T>`adalah alternatif struct untuk hot path yang menghindari alokasi heap ketika hasilnya sudah tersedia.
```csharp
// Async method — returns Task<T>
public async Task<User> GetUserAsync(string id)
{
    using var client = new HttpClient();
    var response = await client.GetAsync($"/api/users/{id}");
    response.EnsureSuccessStatusCode();
    return await response.Content.ReadFromJsonAsync<User>();
}

// Concurrent execution
var userTask = GetUserAsync("1");
var postsTask = GetPostsAsync("1");
var user = await userTask;
var posts = await postsTask;
// Or: await Task.WhenAll(userTask, postsTask);

// ValueTask for high-performance scenarios
public ValueTask<int> GetCachedCount() =>
    _cached.HasValue ? new ValueTask<int>(_cached.Value) : new ValueTask<int>(ComputeCountAsync());
```

### Q3: Apa itu metode ekstensi, dan kapan saya harus menggunakannya?
**A:** Metode ekstensi menambahkan metode ke tipe yang sudah ada tanpa mengubahnya. Itu adalah metode statis di kelas statis, dengan kata kunci`this`pada parameter pertama. Mereka mengaktifkan API yang lancar dan dapat dirantai. Gunakan metode tersebut untuk menambahkan metode utilitas ke tipe yang tidak Anda miliki (seperti`string`atau`IEnumerable<T>`). Hindari menggunakannya secara berlebihan — karena dapat membuat kode sulit ditemukan.
```csharp
public static class StringExtensions
{
    public static string Truncate(this string s, int maxLength) =>
        s.Length <= maxLength ? s : s[..maxLength] + "...";

    public static bool IsEmail(this string s) =>
        s.Contains('@') && s.Contains('.');
}

// Usage — looks like a native method
"Hello, World!".Truncate(8);  // "Hello..."
"test@example.com".IsEmail();  // true

// LINQ is built entirely on extension methods
var adults = people.Where(p => p.Age >= 18).OrderBy(p => p.Name).ToList();
```

### Q4: Bagaimana cara kerja pencocokan pola di C# modern?
**A:** C# secara bertahap menambahkan pencocokan pola yang lebih canggih. Beralih ekspresi (C# 8), pola tipe, pola properti, pola relasional, dan pola daftar (C# 11) memungkinkan logika kondisional yang ringkas dan ekspresif. Pencocokan pola menggantikan rantai if/else yang panjang dan diperiksa secara menyeluruh oleh kompiler.
```csharp
// Switch expression with patterns
string Describe(object obj) => obj switch
{
    null => "nothing",
    int n when n > 0 => $"positive integer: {n}",
    int n => $"non-positive integer: {n}",
    string { Length: 0 } => "empty string",
    string s => $"string of length {s.Length}",
    Person { Age: >= 18 } p => $"adult: {p.Name}",
    Person { Age: < 18 } p => $"minor: {p.Name}",
    int[] { Length: 0 } => "empty array",
    int[] [var first, ..] => $"array starting with {first}",
    _ => $"unknown: {obj.GetType().Name}"
};

// if with pattern matching
if (obj is Person { Age: >= 18 } adult)
{
    Console.WriteLine($"Adult: {adult.Name}");
}
```

### Q5: Apa itu injeksi ketergantungan di .NET, dan bagaimana cara menggunakannya?
**A:** .NET memiliki dukungan DI bawaan melalui`Microsoft.Extensions.DependencyInjection`. Anda mendaftarkan layanan dengan masa pakainya (Singleton, Scoped, Transient), dan container memasukkannya melalui parameter konstruktor. Singleton: satu contoh untuk aplikasi. Cakupan: satu per permintaan HTTP. Sementara: instance baru setiap saat.
```csharp
// Registration (Program.cs)
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddTransient<IEmailSender, SmtpEmailSender>();
builder.Services.AddScoped<IUserRepository, SqlUserRepository>();
builder.Services.AddSingleton<ICache, InMemoryCache>();

// Consumption via constructor injection
public class UserController : ControllerBase
{
    private readonly IUserRepository _users;
    private readonly IEmailSender _email;

    public UserController(IUserRepository users, IEmailSender email)
    {
        _users = users;
        _email = email;
    }

    [HttpPost]
    public async Task<IActionResult> Create(CreateUserDto dto)
    {
        var user = await _users.CreateAsync(dto);
        await _email.SendWelcomeAsync(user.Email);
        return Ok(user);
    }
}
```

---

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membangun Repositori Generik dengan Caching
**Pernyataan Masalah:** Menerapkan pola repositori umum dengan dekorator yang menambahkan caching. Repositori harus mendukung operasi CRUD, dan dekorator caching harus melakukan cache pembacaan dan pembatalan penulisan.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) antarmuka`IRepository<T>`generik, (2) implementasi konkret (misalnya, dalam memori), (3) dekorator cache yang membungkus repositori apa pun, (4) pembatalan cache pada operasi penulisan. Pola dekorator menjaga cache tetap ortogonal dengan logika akses data.
**Langkah 2 — Identifikasi Pendekatannya:**
- Tentukan`IRepository<T>`dengan`Get`,`GetAll`,`Add`,`Update`,`Delete`.
- Buat`CachingRepository<T>`yang membungkus`IRepository<T>`dan menggunakan`IMemoryCache`.
- Kunci cache: `typeof(T).Name:{id}`.
- Pada operasi tulis, batalkan entri cache.
**Langkah 3 — Terapkan Solusi:**
```csharp
public interface IRepository<T> where T : class
{
    Task<T?> GetByIdAsync(string id);
    Task<IReadOnlyList<T>> GetAllAsync();
    Task AddAsync(T entity);
    Task UpdateAsync(T entity);
    Task DeleteAsync(string id);
}

public interface IEntity { string Id { get; } }

public class CachingRepository<T> : IRepository<T> where T : class, IEntity
{
    private readonly IRepository<T> _inner;
    private readonly IMemoryCache _cache;
    private readonly TimeSpan _ttl;

    public CachingRepository(IRepository<T> inner, IMemoryCache cache,
                             TimeSpan? ttl = null)
    {
        _inner = inner;
        _cache = cache;
        _ttl = ttl ?? TimeSpan.FromMinutes(5);
    }

    public Task<T?> GetByIdAsync(string id)
    {
        var key = $"{typeof(T).Name}:{id}";
        return _cache.GetOrCreateAsync(key, entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = _ttl;
            return _inner.GetByIdAsync(id);
        })!;
    }

    public Task<IReadOnlyList<T>> GetAllAsync() =>
        _cache.GetOrCreateAsync($"{typeof(T).Name}:all", entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = _ttl;
            return _inner.GetAllAsync();
        })!;

    public async Task AddAsync(T entity)
    {
        await _inner.AddAsync(entity);
        Invalidate(entity.Id);
    }

    public async Task UpdateAsync(T entity)
    {
        await _inner.UpdateAsync(entity);
        Invalidate(entity.Id);
    }

    public async Task DeleteAsync(string id)
    {
        await _inner.DeleteAsync(id);
        Invalidate(id);
    }

    private void Invalidate(string id)
    {
        _cache.Remove($"{typeof(T).Name}:{id}");
        _cache.Remove($"{typeof(T).Name}:all");
    }
}
```

**Langkah 4 — Verifikasi dan Optimalkan:**
- Pemisahan masalah: caching adalah dekorator, tidak dicampur ke dalam repositori.
- Pendaftaran DI:`services.Decorate<IRepository<User>, CachingRepository<User>>()`(menggunakan Scrutor).
- Produksi: gunakan`IDistributedCache`(Redis) untuk skenario multi-server, dan tambahkan pola penyisihan cache dengan perlindungan `CacheStampede`.
### Masalah 2: Menerapkan Pipeline Middleware
**Pernyataan Masalah:** Membangun pipeline middleware yang serupa dengan pipeline permintaan ASP.NET Core. Setiap middleware dapat memproses permintaan, memanggil middleware berikutnya, dan memproses responsnya.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) tipe`RequestDelegate`yang mewakili pipeline, (2) middleware yang membungkus delegasi berikutnya, (3) API pembangun untuk membuat middleware. Ini adalah pola Rantai Tanggung Jawab yang diterapkan dengan delegasi.
**Langkah 2 — Identifikasi Pendekatannya:**
-`RequestDelegate`adalah`Func<Context, RequestDelegate, Task>`.
- Setiap middleware menerima konteks dan fungsi `next`.
-`Use`menambahkan middleware; `Build`menyusunnya menjadi satu delegasi.
**Langkah 3 — Terapkan Solusi:**
```csharp
public class Context
{
    public string Method { get; init; } = "GET";
    public string Path { get; init; } = "/";
    public Dictionary<string, string> Headers { get; } = new();
    public int StatusCode { get; set; } = 200;
    public string Body { get; set; } = "";
}

public delegate Task RequestDelegate(Context context);

public class PipelineBuilder
{
    private readonly List<Func<RequestDelegate, RequestDelegate>> _middlewares = new();

    public PipelineBuilder Use(Func<Context, RequestDelegate, Task> middleware)
    {
        _middlewares.Add(next => async ctx => await middleware(ctx, next));
        return this;
    }

    public PipelineBuilder Use(Func<Context, Task> handler)
    {
        _middlewares.Add(next => async ctx =>
        {
            await handler(ctx);
            // Terminal middleware — does not call next
        });
        return this;
    }

    public RequestDelegate Build()
    {
        RequestDelegate app = _ => Task.CompletedTask;  // Terminal
        for (int i = _middlewares.Count - 1; i >= 0; i--)
        {
            app = _middlewares[i](app);
        }
        return app;
    }
}

// Usage
var pipeline = new PipelineBuilder()
    .Use(async (ctx, next) =>
    {
        Console.WriteLine($"[{DateTime.Now:HH:mm:ss}] {ctx.Method} {ctx.Path}");
        var sw = Stopwatch.StartNew();
        await next(ctx);
        Console.WriteLine($"Completed in {sw.ElapsedMilliseconds}ms — {ctx.StatusCode}");
    })
    .Use(async (ctx, next) =>
    {
        ctx.Headers["X-Powered-By"] = "MyFramework";
        await next(ctx);
    })
    .Use(async ctx =>
    {
        if (ctx.Path == "/hello")
            ctx.Body = "Hello, World!";
        else
        {
            ctx.StatusCode = 404;
            ctx.Body = "Not Found";
        }
    })
    .Build();

await pipeline(new Context { Method = "GET", Path = "/hello" });
```

**Langkah 4 — Verifikasi dan Optimalkan:**
- Urutan middleware penting: pertama ditambahkan = terluar (dieksekusi pertama berdasarkan permintaan, terakhir berdasarkan respons).
- Terminal middleware (tidak ada panggilan `next`) menyebabkan hubungan arus pendek pada pipa.
- Produksi: Saluran pipa ASP.NET Core memiliki pola yang persis seperti ini, dioptimalkan dengan pohon ekspresi yang dikompilasi untuk alokasi nol.
---

## Ringkasan
C# adalah bahasa yang canggih, modern, dan bertujuan umum dengan peralatan yang sangat baik dan ekosistem yang kuat. Ia unggul dalam pengembangan perusahaan, pengembangan game (Unity), dan aplikasi lintas platform. Bahasanya telah berkembang pesat — C# modern ringkas, ekspresif, dan aman untuk diketik. Meskipun tidak memiliki ukuran ekosistem seperti Java atau Python, kualitas dan konsistensi .NET menjadikan C# bahasa yang produktif dan menyenangkan untuk berbagai aplikasi.