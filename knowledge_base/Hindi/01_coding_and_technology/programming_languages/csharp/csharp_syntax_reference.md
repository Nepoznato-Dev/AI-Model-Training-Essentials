---
# Metadata
title: "C# — Syntax Reference"
description: "Detailed syntax reference for C# covering operators, control flow, classes, LINQ, async, generics, pattern matching, records, and modern C# features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
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
# सी# - सिंटैक्स संदर्भ
यह दस्तावेज़ आधुनिक C# (.NET 7/8 पर C# 10/11/12) के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, LINQ, async/प्रतीक्षा, पैटर्न मिलान और आधुनिक सुविधाओं पर ध्यान केंद्रित करके मुख्य C# संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
### कोर ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `+``-``*``/``%`| अंकगणित | `a + b`| `+`स्ट्रिंग्स को भी जोड़ता है |
| `++``--` | वृद्धि/कमी | `++i`| पूर्व-वृद्धि को प्राथमिकता दें |
| `==``!=` | समानता | `a == b`| अतिरंजित; रिकॉर्ड मूल्य समानता का उपयोग करते हैं |
| `<``>``<=``>=` | संबंधपरक | `a >= b`| |
| `&&``\|\|``!`| तार्किक | `a && b`| शॉर्ट-सर्किट |
| `&``\|``^``~` | बिटवाइज़ | `a & b`| |
| `<<``>>``>>>`| शिफ्ट | `a << 2`| `>>>`अहस्ताक्षरित दायां शिफ्ट (C# 11) |
| `??`| अशक्त संलयन | `a ?? b`| यदि`a`शून्य है तो`b`लौटाता है |
| `?.`| शून्य सशर्त | `a?.B`| यदि`a`शून्य है तो शून्य लौटता है |
| `!`| शून्य-क्षमा | `a!.B`| निरर्थक चेतावनी को दबा देता है |
| `is`| पैटर्न टाइप करें | `x is string s`| पैटर्न मिलान |
| `as`| सुरक्षित कास्ट | `x as string`| विफलता पर शून्य रिटर्न |
| `nameof`| नाम शाब्दिक | `nameof(x)`| `"x"`— संकलन-समय |
| `typeof`| ऑब्जेक्ट टाइप करें | `typeof(int)`| `System.Int32`|
| `sizeof`| आकार बाइट्स में | `sizeof(int)`| `4`(असुरक्षित संदर्भ) |
### ऑपरेटर प्राथमिकता (उच्चतम से निम्नतम)
| वरीयता | संचालक |
|-------|
| 1 (सर्वोच्च) | प्राथमिक:`()``.``?.``[]``()`(आह्वान)
| 2 | यूनरी:`+``-``!``~``++``--` (उपसर्ग)
| 3 | गुणक:`*``/``%`|
| 4 | योजक:`+``-` |
| 5 | शिफ्ट:`<<``>>``>>>`|
| 6 | संबंधपरक:`<``>``<=``>=` `is`
| 7 | समानता:`==``!=` |
| 8 | बिटवाइज और:`&`|
| 9 | बिटवाइज़ XOR:`^`|
| 10 | बिटवाइज या:`\|`|
| 11 | सशर्त और:`&&`|
| 12 | सशर्त या:`\|\|`|
| 13 | अशक्त संलयन:`??`|
| 14 | सशर्त:`? :`|
| 15 | असाइनमेंट:`=``+=``-=``??=` आदि |
---

## प्रवाह को नियंत्रित करें
### पैटर्न मिलान (सी# 8-12)
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

### आधुनिक लूप पैटर्न
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

## लिंक
### क्वेरी सिंटेक्स बनाम मेथड सिंटेक्स
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

## एसिंक/प्रतीक्षा करें
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

## कक्षाएं, रिकॉर्ड और संरचनाएं
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

## जेनेरिक और बाधाएँ
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

## संग्रह अभिव्यक्तियाँ (सी#12)
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

## स्ट्रिंग इंटरपोलेशन और फ़ॉर्मेटिंग
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

## सारांश
आधुनिक सी# एक बहु-प्रतिमान भाषा है जो ऑब्जेक्ट-ओरिएंटेड, कार्यात्मक और घटक-उन्मुख प्रोग्रामिंग का सर्वोत्तम संयोजन करती है। इसका सिंटैक्स नाटकीय रूप से विकसित हुआ है - वर्बोज़ जावा-जैसे कोड से लेकर पैटर्न मिलान, रिकॉर्ड, संग्रह अभिव्यक्ति और प्राथमिक कंस्ट्रक्टर के साथ संक्षिप्त अभिव्यक्ति तक। LINQ सभी संग्रहों में एक समान क्वेरी API प्रदान करता है। Async/प्रतीक्षा असिंक्रोनस प्रोग्रामिंग को स्वाभाविक बनाता है। प्रकार प्रणाली अशक्त संदर्भ प्रकारों, बाधाओं के साथ जेनेरिक और पैटर्न मिलान के माध्यम से व्यावहारिकता के साथ सुरक्षा को संतुलित करती है। सी# तेजी से विकसित हो रहा है, प्रत्येक रिलीज में ऐसी विशेषताएं जोड़ी जा रही हैं जो बैकवर्ड संगतता बनाए रखते हुए बॉयलरप्लेट को कम करती हैं।