---
# Metadata
title: "C# — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in C# that catch even experienced developers, with explanations and corrections."
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
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [csharp, common-mistakes, anti-patterns, pitfalls, best-practices, dotnet, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# C# — 常見錯誤與反模式
本文檔列出了 C# 中最常見的錯誤、陷阱和反模式。每個條目都會顯示錯誤的方法，解釋其失敗的原因，並提供正確的解決方案。
---

## 1. 不處理`IDisposable`對象
```csharp
// ❌ WRONG — resource leak
var stream = new FileStream("data.txt", FileMode.Open);
var reader = new StreamReader(stream);
string data = reader.ReadToEnd();
reader.Close();  // skipped if ReadToEnd throws

// ✅ CORRECT — using statement (C# 8+ using declaration)
using var stream = new FileStream("data.txt", FileMode.Open);
using var reader = new StreamReader(stream);
string data = reader.ReadToEnd();
// automatically disposed
```

---

## 2. 字串的`==`與 `Equals()`
```csharp
// ❌ WRONG — reference comparison for boxed strings
object a = "hello";
object b = new string("hello".ToCharArray());
a == b       // false (reference comparison)
a.Equals(b)  // true (value comparison)

// ✅ CORRECT — use == for strings (it's overloaded correctly)
string x = "hello";
string y = "hello";
x == y  // true

// ✅ CORRECT — explicit comparison
string.Equals(x, y, StringComparison.OrdinalIgnoreCase)
```

---

## 3. 非同步空方法
```csharp
// ❌ WRONG — exceptions can't be caught, fire-and-forget
public async void DoWork() {
    await Task.Delay(1000);
    throw new Exception("oops");  // crashes process!
}

// ✅ CORRECT — always return Task
public async Task DoWork() {
    await Task.Delay(1000);
    // exceptions propagate to caller
}

// Exception: async void is OK for event handlers
private async void OnButtonClick(object sender, EventArgs e) { ... }
```

---

## 4. LINQ`.ToList()`不必要的分配
```csharp
// ❌ WRONG — materializing when not needed
var result = items
    .Where(x => x.IsActive)
    .ToList()
    .Select(x => x.Name)
    .ToList();  // two unnecessary allocations

// ✅ CORRECT — defer materialization
var result = items
    .Where(x => x.IsActive)
    .Select(x => x.Name)
    .ToList();  // single allocation at the end
```

---

## 5. 捕捉循環變數（C# 5.0 之前的版本）
```csharp
// ❌ WRONG — pre-C# 5.0, all delegates share the same variable
var actions = new List<Action>();
for (int i = 0; i < 5; i++) {
    actions.Add(() => Console.WriteLine(i));
}
foreach (var action in actions) action();
// C# 4: prints 5,5,5,5,5
// C# 5+: prints 0,1,2,3,4 (fixed)

// ✅ CORRECT — explicit capture (works in all versions)
for (int i = 0; i < 5; i++) {
    int captured = i;
    actions.Add(() => Console.WriteLine(captured));
}
```

---

## 6. 不使用模式匹配
```csharp
// ❌ WRONG — verbose type checking
object value = GetValue();
if (value is string) {
    string s = (string)value;
    Console.WriteLine(s.Length);
}

// ✅ CORRECT — pattern matching (C# 7+)
if (GetValue() is string s) {
    Console.WriteLine(s.Length);
}

// ✅ CORRECT — switch expression (C# 8+)
string description = shape switch {
    Circle c => $"Circle with radius {c.Radius}",
    Rectangle r => $"Rectangle {r.Width}x{r.Height}",
    _ => "Unknown shape"
};
```

---

## 7. 反模式：上帝類別/服務定位器
```csharp
// ❌ WRONG — service locator anti-pattern
public class UserService {
    public void CreateUser() {
        var db = ServiceLocator.Resolve<IDatabase>();
        var email = ServiceLocator.Resolve<IEmailService>();
        // dependencies hidden, hard to test
    }
}

// ✅ CORRECT — constructor injection
public class UserService {
    private readonly IDatabase _db;
    private readonly IEmailService _email;

    public UserService(IDatabase db, IEmailService email) {
        _db = db;
        _email = email;
    }
}
```

---

## 8. 空引用異常
```csharp
// ❌ WRONG — not checking for null
public string GetUserName(User user) {
    return user.Address.City;  // NullReferenceException chain
}

// ✅ CORRECT — null-conditional operator
public string GetUserName(User user) {
    return user?.Address?.City ?? "Unknown";
}

// ✅ CORRECT — nullable reference types (C# 8+)
#nullable enable
public string? FindEmail(string name) { ... }
// Compiler warns on unchecked null access
```

---

## 9. 循環中的字串連接
```csharp
// ❌ WRONG — creates new string each iteration
string result = "";
foreach (var word in words) {
    result += word + " ";  // O(n²)
}

// ✅ CORRECT — StringBuilder
var sb = new StringBuilder();
foreach (var word in words) {
    sb.Append(word).Append(' ');
}
string result = sb.ToString();

// ✅ CORRECT — string.Join
string result = string.Join(" ", words);
```

---

## 10. 不使用記錄作為資料類型
```csharp
// ❌ WRONG — class for immutable data (lots of boilerplate)
public class Point {
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
    // need to manually implement Equals, GetHashCode, ToString...
}

// ✅ CORRECT — record type (C# 9+)
public record Point(int X, int Y);
// auto-generates Equals, GetHashCode, ToString, deconstruct
```

---

## 11. 異常過濾器濫用
```csharp
// ❌ WRONG — catching Exception and checking type
try {
    DoWork();
} catch (Exception ex) {
    if (ex is IOException) { /* handle */ }
    else if (ex is SqlException) { /* handle */ }
    else throw;
}

// ✅ CORRECT — catch specific exceptions
try {
    DoWork();
} catch (IOException ex) {
    // handle IO
} catch (SqlException ex) {
    // handle SQL
}
```

---

＃＃ 概括
C# 是一種設計良好的語言，但也有陷阱：不處理`IDisposable`物件、async void 方法、不必要的 LINQ 分配和空引用異常。現代 C# (8+) 提供了強大的工具：可空引用類型、模式比對、記錄、using 宣告和 switch 表達式。關鍵原則：始終處置資源，從不使用 async void（事件處理程序除外），使用構造函數注入，更喜歡資料記錄，並啟用可空引用類型以在編譯時捕獲空錯誤。