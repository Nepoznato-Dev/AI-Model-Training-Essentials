---
# Metadata
title: "Visual Basic — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean Visual Basic (.NET) code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [visual-basic, vb-net, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Visual Basic — 慣用模式與最佳實踐
本指南介紹了編寫乾淨的 Visual Basic (.NET) 程式碼的慣用模式。
---

## 選項嚴格和類型安全
```vb
' ✅ Always enable Option Strict
Option Strict On
Option Infer On
Option Explicit On

' ✅ Use type inference with Option Infer
Dim count = 42                  ' inferred as Integer
Dim name = "Alice"              ' inferred as String
Dim items = New List(Of String) ' inferred as List(Of String)

' ❌ Avoid late binding
Dim obj As Object = GetWidget()
obj.DoWork()                    ' ❌ late binding — no compile-time check

' ✅ Use specific types
Dim widget As Widget = GetWidget()
widget.DoWork()                 ' ✅ early binding — type-safe
```

---

## 資源管理
```vb
' ✅ Using block for IDisposable resources
Using reader As New StreamReader("data.txt")
    Dim content = reader.ReadToEnd()
    ProcessContent(content)
End Using
' reader is automatically disposed

' ✅ Nested Using blocks
Using connection As New SqlConnection(connString)
    Using command As New SqlCommand(sql, connection)
        connection.Open()
        Using reader = command.ExecuteReader()
            While reader.Read()
                ProcessRow(reader)
            End While
        End Using
    End Using
End Using
```

---

## 字串處理
```vb
' ✅ String interpolation (VB 14+)
Dim message = $"Hello, {userName}! You have {count} messages."

' ✅ String.Concat for simple joins
Dim full = String.Concat(firstName, " ", lastName)

' ✅ StringBuilder for loops
Dim sb As New StringBuilder()
For Each item In items
    If sb.Length > 0 Then sb.Append(", ")
    sb.Append(item.Name)
Next
Dim result = sb.ToString()

' ✅ String.IsNullOrEmpty / IsNullOrWhiteSpace
If String.IsNullOrWhiteSpace(input) Then
    Throw New ArgumentException("Input cannot be empty", NameOf(input))
End If
```

---

## LINQ 與集合模式
```vb
' ✅ LINQ query syntax for complex queries
Dim adults = From p In people
             Where p.Age >= 18
             Order By p.LastName, p.FirstName
             Select p.FullName

' ✅ LINQ method syntax for simple operations
Dim total = orders.Where(Function(o) o.Status = "Active").
                   Sum(Function(o) o.Amount)

' ✅ Collection initializers
Dim scores As New List(Of Integer) From {95, 87, 72, 100, 63}

Dim lookup As New Dictionary(Of String, Integer) From {
    {"Alice", 95},
    {"Bob", 87},
    {"Charlie", 72}
}
```

---

## 非同步/等待模式
```vb
' ✅ Async all the way down
Public Async Function GetUserAsync(userId As Integer) As Task(Of User)
    Using client As New HttpClient()
        Dim response = Await client.GetAsync($"api/users/{userId}")
        response.EnsureSuccessStatusCode()
        Return Await response.Content.ReadAsAsync(Of User)()
    End Using
End Function

' ✅ Avoid .Result or .Wait() — use Await
' ❌ Bad: blocking async
Dim user = GetUserAsync(1).Result

' ✅ Good: proper async
Dim user = Await GetUserAsync(1)

' ✅ ConfigureAwait(false) in library code
Dim data = Await FetchDataAsync().ConfigureAwait(False)
```

---

## 錯誤處理
```vb
' ✅ Try/Catch with specific exceptions
Try
    Dim result = Calculate(value)
Catch ex As DivideByZeroException
    Logger.LogWarning("Division by zero in Calculate")
    Return 0
Catch ex As OverflowException
    Logger.LogError(ex, "Overflow in Calculate")
    Throw New BusinessException("Calculation overflow", ex)
End Try

' ✅ Throw with context
If value < 0 Then
    Throw New ArgumentOutOfRangeException(
        NameOf(value), value, "Value must be non-negative")
End If

' ✅ Using Throw for re-throw (preserves stack trace)
Catch ex As IOException
    Logger.LogError(ex, "File read failed")
    Throw  ' ✅ preserves original stack trace
```

---

## 現代 VB 功能
```vb
' ✅ Tuple deconstruction
Dim (name, age) = GetPersonInfo()

' ✅ Pattern matching (VB 15+)
Select Case shape
    Case c As Circle
        area = Math.PI * c.Radius ^ 2
    Case r As Rectangle
        area = r.Width * r.Height
    Case Nothing
        Throw New ArgumentNullException(NameOf(shape))
End Select

' ✅ Null-conditional operators
Dim length = customer?.Address?.Street?.Length
Dim first = items?(0)

' ✅ With block for multiple property access
With employee
    .Name = "Alice"
    .Department = "Engineering"
    .Salary = 95000
End With
```

---

＃＃ 概括
Visual Basic 习惯用法强调：用于类型安全的 `Option Strict On`、用于资源管理的`Using`块、字符串插值、用于集合的 LINQ、贯穿始终的 `Async/Await`、特定异常处理以及模式匹配和 null 条件运算符等现代功能。 VB 重視可讀性——“程式碼讀起來應該像組織良好的規範。”