<!--
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

-->
# Visual Basic — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔한 Visual Basic(.NET) 코드를 작성하기 위한 관용적 패턴을 다룹니다.
---

## 옵션 엄격 및 유형 안전성
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

## 자원 관리
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

## 문자열 처리
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

## LINQ 및 컬렉션 패턴
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

## 비동기/대기 패턴
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

## 오류 처리
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

## 최신 VB 기능
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

## 요약
Visual Basic 관용구는 유형 안전성을 위한 `Option Strict On`, 리소스 관리를 위한`Using`블록, 문자열 보간, 컬렉션을 위한 LINQ, 전체 `Async/Await`, 특정 예외 처리, 패턴 일치 및 null 조건부 연산자와 같은 최신 기능을 강조합니다. VB 가치 가독성 — "코드는 잘 구성된 사양처럼 읽어야 합니다."