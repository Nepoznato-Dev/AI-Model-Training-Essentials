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

# C# - การอ้างอิงไวยากรณ์
เอกสารนี้ให้การอ้างอิงไวยากรณ์ที่มีโครงสร้างและครอบคลุมสำหรับ Modern C# (C# 10/11/12 บน .NET 7/8) มันเสริมการอ้างอิง C# หลักโดยมุ่งเน้นไปที่รูปแบบไวยากรณ์ที่ละเอียดถี่ถ้วน, LINQ, async/await, การจับคู่รูปแบบ และคุณสมบัติที่ทันสมัย
---

## ตัวดำเนินการและนิพจน์
### ผู้ประกอบการหลัก
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `+``-``*``/``%`| เลขคณิต | `a + b`| `+`ยังเชื่อมสตริง |
| `++``--` | เพิ่ม/ลด | `++i`| ต้องการเพิ่มล่วงหน้า |
| `==``!=` | ความเท่าเทียมกัน | `a == b`| เอาชนะได้; บันทึกใช้ความเท่าเทียมกันของค่า |
| `<``>``<=``>=` | เชิงสัมพันธ์ | `a >= b`| |
| `&&``\|\|``!`| ตรรกะ | `a && b`| ลัดวงจร |
| `&``\|``^``~` | ระดับบิต | `a & b`| |
| `<<``>>``>>>`| กะ | `a << 2`| `>>>`กะขวาที่ไม่ได้ลงนาม (C# 11) |
| `??`| การรวมตัวกันเป็นโมฆะ | `a ?? b`| ส่งกลับ`b`ถ้า`a`เป็น null |
| `?.`| เงื่อนไขว่าง | `a?.B`| ส่งกลับค่า null ถ้า`a`เป็น null |
| `!`| การให้อภัยเป็นโมฆะ | `a!.B`| ระงับคำเตือนที่เป็นโมฆะ |
| `is`| พิมพ์รูปแบบ | `x is string s`| การจับคู่รูปแบบ |
| `as`| โยนอย่างปลอดภัย | `x as string`| ส่งคืนค่าว่างเมื่อล้มเหลว |
| `nameof`| ชื่อตามตัวอักษร | `nameof(x)`| `"x"`— เวลาคอมไพล์ |
| `typeof`| พิมพ์วัตถุ | `typeof(int)`| `System.Int32`|
| `sizeof`| ขนาดเป็นไบต์ | `sizeof(int)`| `4`(บริบทที่ไม่ปลอดภัย) |
### ลำดับความสำคัญของตัวดำเนินการ (สูงสุดไปต่ำสุด)
| ลำดับความสำคัญ | ตัวดำเนินการ |
|------------|-----------|
| 1 (สูงสุด) | หลัก:`()``.``?.``[]``()`(เรียกใช้)`++``--` (postfix)`new``typeof``sizeof`|
| 2 | เอกพจน์:`+``-``!``~``++``--` (คำนำหน้า)`(T)x``await` |
| 3 | การคูณ:`*``/``%`|
| 4 | สารเติมแต่ง:`+``-` |
| 5 | ชิฟต์:`<<``>>``>>>`|
| 6 | ความสัมพันธ์:`<``>``<=``>=``is``as` |
| 7 | ความเท่าเทียมกัน:`==``!=` |
| 8 | ระดับบิตและ:`&`|
| 9 | XOR ระดับบิต:`^`|
| 10 | ระดับบิตหรือ:`\|`|
| 11 | มีเงื่อนไขและ:`&&`|
| 12 | มีเงื่อนไข หรือ:`\|\|`|
| 13 | การรวมตัวกันเป็นศูนย์:`??`|
| 14 | มีเงื่อนไข:`? :`|
| 15 | การมอบหมาย:`=``+=``-=``??=` ฯลฯ |
---

## การควบคุมการไหล
### การจับคู่รูปแบบ (C# 8–12)
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

### รูปแบบห่วงที่ทันสมัย
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

## ลิงค์
### ไวยากรณ์แบบสอบถามเทียบกับไวยากรณ์วิธี
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

## อะซิงก์/รอสักครู่
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

## ชั้นเรียน บันทึก และโครงสร้าง
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

## ข้อมูลทั่วไปและข้อจำกัด
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

## นิพจน์คอลเลกชัน (C# 12)
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

## การแก้ไขสตริงและการจัดรูปแบบ
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

## สรุป
Modern C# เป็นภาษาหลายกระบวนทัศน์ที่ผสมผสานสิ่งที่ดีที่สุดของการเขียนโปรแกรมเชิงวัตถุ เชิงฟังก์ชัน และเชิงองค์ประกอบ ไวยากรณ์ของมันมีการพัฒนาอย่างมาก ตั้งแต่โค้ดที่คล้ายกับ Java แบบละเอียดไปจนถึงนิพจน์ที่กระชับด้วยการจับคู่รูปแบบ บันทึก นิพจน์คอลเลกชัน และตัวสร้างหลัก LINQ มี API การสืบค้นที่เหมือนกันในทุกคอลเลกชัน Async/await ทำให้การเขียนโปรแกรมแบบอะซิงโครนัสเป็นธรรมชาติ ระบบประเภทจะรักษาสมดุลระหว่างความปลอดภัยกับลัทธิปฏิบัตินิยมผ่านประเภทการอ้างอิงที่เป็นโมฆะ ข้อมูลทั่วไปที่มีข้อจำกัด และการจับคู่รูปแบบ C# ยังคงพัฒนาอย่างรวดเร็ว โดยแต่ละรุ่นได้เพิ่มคุณสมบัติที่ลดรูปแบบสำเร็จรูปในขณะที่ยังคงความเข้ากันได้แบบย้อนหลัง