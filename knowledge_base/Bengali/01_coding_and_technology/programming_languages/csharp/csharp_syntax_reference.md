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

# C# — সিনট্যাক্স রেফারেন্স
এই নথিটি আধুনিক C# (.NET 7/8-এ C# 10/11/12) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, LINQ, অ্যাসিঙ্ক/ওয়েট, প্যাটার্ন ম্যাচিং এবং আধুনিক বৈশিষ্ট্যগুলিতে ফোকাস করে প্রধান C# রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``%`| পাটিগণিত | `a + b`| `+`এছাড়াও স্ট্রিংগুলিকে সংযুক্ত করে |
| `++``--` | বৃদ্ধি/হ্রাস | `++i`| প্রাক-বৃদ্ধি পছন্দ করুন |
| `==``!=` | সমতা | `a == b`| ওভাররিডেবল; রেকর্ড মান সমতা ব্যবহার করে |
| `<``>``<=``>=` | সম্পর্কীয় | `a >= b`| |
| `&&``\|\|``!`| যৌক্তিক | `a && b`| শর্ট সার্কিট |
| `&``\|``^``~` | বিটওয়াইজ | `a & b`| |
| `<<``>>``>>>`| শিফট | `a << 2`| `>>>`স্বাক্ষরবিহীন ডান শিফট (C# 11) |
| `??`| নাল কোলেসিং | `a ?? b`|`a`শূন্য হলে`b`ফেরত দেয় |
| `?.`| শূন্য শর্তাধীন | `a?.B`| যদি`a`শূন্য হয় |
| `!`| শূন্য-ক্ষমাকারী | `a!.B`| বাতিলযোগ্য সতর্কতা দমন করে |
| `is`| টাইপ প্যাটার্ন | `x is string s`| প্যাটার্ন ম্যাচিং |
| `as`| নিরাপদ কাস্ট | `x as string`| ব্যর্থ হলে শূন্য ফেরত দেয় |
| `nameof`| নাম আক্ষরিক | `nameof(x)`| `"x"`— কম্পাইল-টাইম |
| `typeof`| টাইপ অবজেক্ট | `typeof(int)`| `System.Int32`|
| `sizeof`| বাইটে আকার | `sizeof(int)`| `4`(অনিরাপদ প্রসঙ্গ) |
### অপারেটর অগ্রাধিকার (সর্বোচ্চ থেকে সর্বনিম্ন)
| অগ্রাধিকার | অপারেটর |
|------------|------------|
| 1 (সর্বোচ্চ) | প্রাথমিক:`()``.``?.``[]``()`(আমন্ত্রণ)`++``--` (পোস্টফিক্স) XQZMARKER7XQXMARKZ9XQZMARKZ8
| 2 | ইউনারি:`+``-``!``~``++``--` (উপসর্গ)`(T)x``await` |
| 3 | গুণক:`*``/``%`|
| 4 | সংযোজন:`+``-` |
| 5 | শিফট:`<<``>>``>>>`|
| 6 | সম্পর্কীয়:`<``>``<=``>=``is``as` |
| 7 | সমতা:`==``!=` |
| 8 | বিটওয়াইজ এবং:`&`|
| 9 | Bitwise XOR:`^`|
| 10 | বিটওয়াইজ বা:`\|`|
| 11 | শর্তসাপেক্ষ এবং:`&&`|
| 12 | শর্তাধীন বা:`\|\|`|
| 13 | নাল কোলেসিং:`??`|
| 14 | শর্তাধীন:`? :`|
| 15 | অ্যাসাইনমেন্ট:`=``+=``-=``??=` ইত্যাদি |
---

## নিয়ন্ত্রণ প্রবাহ
### প্যাটার্ন ম্যাচিং (C# 8-12)
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

### আধুনিক লুপ প্যাটার্ন
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

## লিঙ্ক
### ক্যোয়ারী সিনট্যাক্স বনাম পদ্ধতি সিনট্যাক্স
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

## অ্যাসিঙ্ক/অপেক্ষা করুন
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

## ক্লাস, রেকর্ড এবং কাঠামো
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

## জেনেরিক এবং সীমাবদ্ধতা
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

## কালেকশন এক্সপ্রেশন (C# 12)
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

## স্ট্রিং ইন্টারপোলেশন এবং ফরম্যাটিং
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

## সারাংশ
আধুনিক C# হল একটি মাল্টি-প্যারাডাইম ল্যাঙ্গুয়েজ যা অবজেক্ট-ওরিয়েন্টেড, ফাংশনাল এবং কম্পোনেন্ট-ওরিয়েন্টেড প্রোগ্রামিং এর সেরা সমন্বয় করে। এর সিনট্যাক্স নাটকীয়ভাবে বিকশিত হয়েছে — ভার্বোস জাভা-এর মতো কোড থেকে প্যাটার্ন ম্যাচিং, রেকর্ড, সংগ্রহ এক্সপ্রেশন এবং প্রাথমিক কনস্ট্রাক্টর সহ সংক্ষিপ্ত এক্সপ্রেশন পর্যন্ত। LINQ সমস্ত সংগ্রহ জুড়ে একটি অভিন্ন ক্যোয়ারী API প্রদান করে। Async/await অ্যাসিঙ্ক্রোনাস প্রোগ্রামিংকে স্বাভাবিক করে তোলে। টাইপ সিস্টেম ব্যবহারবাদের সাথে নিরাপত্তার ভারসাম্য রক্ষা করে শূন্য রেফারেন্স টাইপ, সীমাবদ্ধতা সহ জেনেরিক এবং প্যাটার্ন ম্যাচিংয়ের মাধ্যমে। C# দ্রুত বিকশিত হতে থাকে, প্রতিটি রিলিজের সাথে এমন বৈশিষ্ট্য যোগ করে যা বয়লারপ্লেট হ্রাস করে এবং পশ্চাদগামী সামঞ্জস্য বজায় রাখে।