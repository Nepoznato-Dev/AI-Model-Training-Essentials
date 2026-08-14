---
# Metadata
title: "C# — Syntax Reference"
description: "Detailed syntax reference for C# covering operators, control flow, classes, LINQ, async, generics, pattern matching, records, and modern C# features."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [csharp, syntax-reference, operators, linq, async, generics, pattern-matching, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# سی شارپ - مرجع نحو
این سند یک مرجع جامع و ساختارمند برای سی شارپ مدرن ارائه می‌کند (C# 10/11/12 در NET 7/8). این مرجع اصلی C# را با تمرکز بر الگوهای نحوی جامع، LINQ، async/wait، تطبیق الگو، و ویژگی‌های مدرن تکمیل می‌کند.
---

## اپراتورها و عبارات
### اپراتورهای اصلی
| اپراتور | نام | مثال | یادداشت ها |
|----------|------|---------|-------|
| `+``-``*``/``%`| حسابی | `a + b`| `+`همچنین رشته ها را به هم متصل می کند |
| `++``--` | افزایش/کاهش | `++i`| ترجیح پیش افزایش |
| `==``!=` | برابری | `a == b`| قابل جبران؛ سوابق برابری ارزش مصرف |
| `<``>``<=``>=` | رابطه ای | `a >= b`| |
| `&&``\|\|``!`| منطقی | `a && b`| اتصال کوتاه |
| `&``\|``^``~` | بیتی | `a & b`| |
| `<<``>>``>>>`| شیفت | `a << 2`|  شیفت سمت راست بدون علامت`>>>`(C# 11) |
| `??`| ادغام تهی | `a ?? b`| اگر`a`تهی باشد،`b`را برمی گرداند |
| `?.`| تهی شرطی | `a?.B`| اگر`a`پوچ باشد |
| `!`| باطل بخشنده | `a!.B`| اخطار باطل شدنی را سرکوب می کند |
| `is`| الگوی تایپ | `x is string s`| تطبیق الگو |
| `as`| بازیگران ایمن | `x as string`| در صورت عدم موفقیت |
| `nameof`| نام تحت اللفظی | `nameof(x)`| `"x"`— زمان کامپایل |
| `typeof`| تایپ شی | `typeof(int)`| `System.Int32`|
| `sizeof`| اندازه بر حسب بایت | `sizeof(int)`| `4`(زمینه ناامن) |
### اولویت اپراتور (بیشترین به کمترین)
| تقدم | اپراتورها |
|------------|-----------|
| 1 (بالاترین) | اصلی:`()``.``?.``[]``()`(فراخوانی)`++``--` (پست رفع)
| 2 | Unary:`+``-``!``~``++``--` (پیشوند)`(T)x``await` |
| 3 | ضرب:`*``/``%`|
| 4 | افزودنی:`+``-` |
| 5 | Shift:`<<``>>``>>>`|
| 6 | رابطه ای:`<``>``<=``>=``is``as` |
| 7 | برابری:`==``!=` |
| 8 | بیتی و:`&`|
| 9 | XOR بیتی:`^`|
| 10 | بیتی OR:`\|`|
| 11 | شرطی و:`&&`|
| 12 | شرطی OR:`\|\|`|
| 13 | ادغام تهی:`??`|
| 14 | مشروط:`? :`|
| 15 | تکلیف:`=``+=``-=``??=` و غیره |
---

## جریان را کنترل کنید
### تطبیق الگو (C# 8-12)
```csharp
// Switch expression
string GetStatus(HttpStatusCode code) => code switch
{
    >= 200 and < 300 => "Success",
    >= 300 and < 400 => "Redirect",
    >= 400 and < 500 => "Client Error",
    >= 500 => "Server Error",
    _ => "Unknown"
};

// Type patterns
object Describe(object obj) => obj switch
{
    null => "null",
    int n => $"integer: {n}",
    string { Length: 0 } => "empty string",
    string s => $"string({s.Length}): \"{s}\"",
    IList<int> { Count: > 10 } list => $"large int list with {list.Count} items",
    (int x, int y) => $"tuple: ({x}, {y})",
    _ => $"other: {obj.GetType().Name}"
};

// if with patterns
if (obj is Person { Age: >= 18, Name: not null } adult)
{
    Console.WriteLine($"Adult: {adult.Name}");
}

// List patterns (C# 11)
int[] numbers = { 1, 2, 3, 4, 5 };
string desc = numbers switch
{
    [] => "empty",
    [var single] => $"single: {single}",
    [var first, .., var last] => $"first: {first}, last: {last}",
    [_, _, ..] => "at least two elements"
};
```

### الگوهای حلقه مدرن
```csharp
// foreach with deconstruction
foreach (var (key, value) in dictionary) { }
foreach (var (index, item) in list.Select((item, i) => (i, item))) { }

// Range and indices (C# 8)
int[] arr = { 0, 1, 2, 3, 4, 5 };
var slice = arr[1..4];      // { 1, 2, 3 }
var last = arr[^1];          // 5 (last element)
var tail = arr[^3..];        // { 3, 4, 5 }
```

---

## LINQ
### نحو پرس و جو در مقابل نحو روش
```csharp
// Method syntax (most common)
var adults = people
    .Where(p => p.Age >= 18)
    .OrderByDescending(p => p.Age)
    .Select(p => p.Name)
    .ToList();

// Query syntax (SQL-like)
var adults2 = from p in people
              where p.Age >= 18
              orderby p.Age descending
              select p.Name;

// Group by
var byCity = people.GroupBy(p => p.City);
foreach (var group in byCity)
{
    Console.WriteLine($"{group.Key}: {group.Count()} people");
}

// Aggregate
int total = numbers.Aggregate(0, (acc, n) => acc + n);
string csv = names.Aggregate("", (acc, name) => acc == "" ? name : $\"{acc}, {name}\");

// Common operations
var distinct = items.Distinct().ToList();
var union = list1.Union(list2);
var intersection = list1.Intersect(list2);
var difference = list1.Except(list2);
var zipped = names.Zip(scores, (n, s) => $\"{n}: {s}\");
bool any = people.Any(p => p.Age > 60);
bool all = people.All(p => p.Age >= 0);
int count = people.Count(p => p.IsActive);
```

---

## Async/Await
```csharp
// Basic async method
public async Task<string> FetchAsync(string url)
{
    using var client = new HttpClient();
    var response = await client.GetAsync(url);
    response.EnsureSuccessStatusCode();
    return await response.Content.ReadAsStringAsync();
}

// Concurrent execution
var task1 = FetchAsync(url1);
var task2 = FetchAsync(url2);
var (result1, result2) = (await task1, await task2);

// Task.WhenAll — true parallel await
var results = await Task.WhenAll(
    urls.Select(url => FetchAsync(url))
);

// CancellationToken support
public async Task<string> FetchAsync(string url, CancellationToken ct)
{
    using var client = new HttpClient();
    var response = await client.GetAsync(url, ct);
    return await response.Content.ReadAsStringAsync(ct);
}

// IAsyncEnumerable — async streaming
public async IAsyncEnumerable<int> GenerateNumbers(
    [EnumeratorCancellation] CancellationToken ct = default)
{
    for (int i = 0; ; i++)
    {
        ct.ThrowIfCancellationRequested();
        await Task.Delay(100, ct);
        yield return i;
    }
}

// Consume async stream
await foreach (var number in GenerateNumbers(ct))
{
    Console.WriteLine(number);
}
```

---

## کلاس ها، سوابق و ساختارها
```csharp
// Record — value equality, immutable
public record Person(string FirstName, string LastName, int Age)
{
    public string FullName => $\"{FirstName} {LastName}\";
}

var p1 = new Person(\"Alice\", \"Smith\", 30);
var p2 = p1 with { LastName = \"Jones\" };  // Non-destructive mutation

// Record struct (C# 10) — value type with value equality
public record struct Point(double X, double Y);

// Primary constructor (C# 12)
public class UserController(IUserRepository repo, ILogger logger) : ControllerBase
{
    [HttpGet(\"{id}\")]
    public async Task<User> Get(string id) => await repo.GetByIdAsync(id);
}

// Sealed class — cannot be inherited
public sealed class Singleton { /* ... */ }

// Abstract class with abstract members
public abstract class Shape
{
    public abstract double Area { get; }
    public virtual string Describe() => $\"Shape with area {Area:F2}\";
}

// Interface with default implementation
public interface ILogger
{
    void Log(string message);
    void LogError(Exception ex) => Log($\"ERROR: {ex.Message}\");  // Default impl
}

// Partial methods and classes (source generators)
public partial class GeneratedService
{
    partial void ValidateInput(CreateDto dto);  // Implemented by source generator
}
```

---

## ژنریک و محدودیت ها
```csharp
// Generic class with constraints
public class Repository<T> where T : class, IEntity, new()
{
    private readonly Dictionary<string, T> _store = new();

    public T? Get(string id) => _store.GetValueOrDefault(id);
    public void Save(T entity) => _store[entity.Id] = entity;
}

// Generic method
public T Max<T>(T a, T b) where T : IComparable<T> =>
    a.CompareTo(b) >= 0 ? a : b;

// Covariance and contravariance
IEnumerable<out T>    // Covariant — can use derived type
IComparer<in T>       // Contravariant — can use base type

// Generic constraints reference
// where T : struct        — value type
// where T : class         — reference type
// where T : notnull       — non-nullable
// where T : unmanaged     — unmanaged type
// where T : new()         — parameterless constructor
// where T : BaseType      — must inherit
// where T : IInterface    — must implement
```

---

## عبارات مجموعه (C# 12)
```csharp
// Collection expressions
int[] arr = [1, 2, 3, 4, 5];
List<string> names = [\"Alice\", \"Bob\", \"Charlie\"];
Span<int> span = [10, 20, 30];

// Spread operator
int[] combined = [..arr, 6, 7, ..new[] { 8, 9 }];

// With LINQ
var squares = [..Enumerable.Range(1, 10).Select(x => x * x)];
```

---

## درون یابی و قالب بندی رشته ها
```csharp
// Raw string literals (C# 11)
var json = \"\"\"
    {
        \"name\": \"Alice\",
        \"age\": 30
    }
    \"\"\";

// Interpolated raw strings
var name = \"Alice\";
var greeting = \"\"\"
    Hello, {name}!
    Welcome to the system.
    \"\"\";

// Format strings
Console.WriteLine($\"{price:C2}\");     // $1,234.56
Console.WriteLine($\"{ratio:P1}\");     // 45.6%
Console.WriteLine($\"{value,10:F2}\");  // Right-aligned, 2 decimals
```

---

## خلاصه
سی شارپ مدرن یک زبان چند پارادایم است که بهترین برنامه نویسی شی گرا، تابعی و جزء گرا را با هم ترکیب می کند. نحو آن به طرز چشمگیری تکامل یافته است - از کدهای پرمخاطب جاوا مانند تا عبارات مختصر با تطبیق الگو، رکوردها، عبارات مجموعه و سازنده های اولیه. LINQ یک API پرس و جو یکنواخت را در تمام مجموعه ها ارائه می دهد. Async/wait برنامه نویسی ناهمزمان را طبیعی می کند. سیستم نوع از طریق انواع مرجع باطل، ژنریک با محدودیت ها و تطبیق الگو، ایمنی را با عمل گرایی متعادل می کند. سی شارپ به سرعت به تکامل خود ادامه می‌دهد و هر نسخه ویژگی‌هایی را اضافه می‌کند که صفحه دیگ را کاهش می‌دهد و در عین حال سازگاری با عقب را حفظ می‌کند.