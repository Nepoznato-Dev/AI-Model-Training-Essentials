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

# सी# - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ C# में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है। प्रत्येक प्रविष्टि गलत दृष्टिकोण दिखाती है, बताती है कि यह विफल क्यों होता है, और सही समाधान प्रदान करती है।
---

## 1.`IDisposable`वस्तुओं का निपटान नहीं करना
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

## 2. स्ट्रिंग्स के लिए`==`बनाम `Equals()`
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

## 3. Async शून्य विधियाँ
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

## 4. LINQ`.ToList()`अनावश्यक आवंटन
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

## 5. लूप वेरिएबल कैप्चर करना (प्री-सी# 5.0)
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

## 6. पैटर्न मिलान का उपयोग न करना
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

## 7. एंटी-पैटर्न: गॉड क्लासेस/सर्विस लोकेटर
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

## 8. शून्य संदर्भ अपवाद
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

## 9. लूप्स में स्ट्रिंग कॉन्सटेनेशन
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

## 10. डेटा प्रकारों के लिए रिकॉर्ड्स का उपयोग नहीं करना
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

## 11. अपवाद फ़िल्टर का दुरुपयोग
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

## सारांश
C# एक अच्छी तरह से डिज़ाइन की गई भाषा है, लेकिन इसमें जाल हैं:`IDisposable`ऑब्जेक्ट का निपटान नहीं करना, एसिंक शून्य विधियां, अनावश्यक LINQ आवंटन और शून्य संदर्भ अपवाद। आधुनिक C# (8+) शक्तिशाली उपकरण प्रदान करता है: अशक्त संदर्भ प्रकार, पैटर्न मिलान, रिकॉर्ड, घोषणाओं का उपयोग करना और स्विच अभिव्यक्तियाँ। मुख्य सिद्धांत: हमेशा संसाधनों का निपटान करें, कभी भी एसिंक शून्य (ईवेंट हैंडलर को छोड़कर) का उपयोग न करें, कंस्ट्रक्टर इंजेक्शन का उपयोग करें, डेटा के लिए रिकॉर्ड को प्राथमिकता दें, और संकलन समय पर अशक्त बग को पकड़ने के लिए अशक्त संदर्भ प्रकारों को सक्षम करें।