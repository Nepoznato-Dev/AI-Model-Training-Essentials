---
# Metadata
title: "Visual Basic — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Visual Basic (VB.NET) with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [visual-basic, vbnet, common-mistakes, anti-patterns, pitfalls, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Visual Basic — Những lỗi thường gặp & mẫu phản đối
Tài liệu này liệt kê các lỗi, bẫy và phản mẫu phổ biến nhất trong Visual Basic (VB.NET) kèm theo các bản sửa lỗi.
---

## 1. Không thải bỏ tài nguyên
```vb
' ❌ WRONG — resource leak
Dim reader As New StreamReader("data.txt")
Dim data As String = reader.ReadToEnd()
reader.Close()  ' skipped if ReadToEnd throws

' ✅ CORRECT — Using block
Using reader As New StreamReader("data.txt")
    Dim data As String = reader.ReadToEnd()
End Using  ' automatically disposed
```

---

## 2.`=`và`Is`để so sánh đối tượng
```vb
' ❌ WRONG — = for reference comparison
Dim a As Object = "hello"
Dim b As Object = "hello"
If a = b Then  ' value comparison, not reference
If a Is b Then  ' reference comparison
End If

' ✅ CORRECT — use Is for reference, = for value
If name = "Alice" Then  ' string value comparison
If obj1 Is obj2 Then    ' same object?
If obj1 Is Nothing Then ' null check
End If
```

---

## 3. Tùy chọn Tắt nghiêm ngặt
```vb
' ❌ WRONG — late binding and implicit conversions
Option Strict Off
Dim x As Integer = "42"  ' implicit conversion
Dim obj As Object = "hello"
Dim len As Integer = obj.Length  ' late binding

' ✅ CORRECT — enable Option Strict
Option Strict On
Dim x As Integer = Integer.Parse("42")
Dim s As String = "hello"
Dim len As Integer = s.Length
```

---

## 4. Không sử dụng`Using`để kết nối cơ sở dữ liệu
```vb
' ❌ WRONG — connection not closed on error
Dim conn As New SqlConnection(connString)
conn.Open()
Dim cmd As New SqlCommand("SELECT * FROM Users", conn)
Dim reader As SqlDataReader = cmd.ExecuteReader()
' ... use reader ...
conn.Close()  ' never reached on exception

' ✅ CORRECT — nested Using blocks
Using conn As New SqlConnection(connString)
    conn.Open()
    Using cmd As New SqlCommand("SELECT * FROM Users", conn)
        Using reader As SqlDataReader = cmd.ExecuteReader()
            ' ... use reader ...
        End Using
    End Using
End Using
```

---

## 5. Anti-Pattern: Business Logic trong Trình xử lý sự kiện
```vb
' ❌ WRONG — everything in button click
Private Sub btnSave_Click(sender As Object, e As EventArgs)
    ' validation, database access, email, all here
End Sub

' ✅ CORRECT — separate concerns
Private Sub btnSave_Click(sender As Object, e As EventArgs)
    UserService.Save(txtName.Text, txtEmail.Text)
End Sub
```

---

## Bản tóm tắt
Bẫy VB.NET: luôn sử dụng`Using`cho các tài nguyên dùng một lần, phân biệt`=`(giá trị) với`Is`(tham khảo), bật `Option Strict On`, sử dụng các khối`Using`để kết nối cơ sở dữ liệu và tách logic nghiệp vụ khỏi trình xử lý sự kiện giao diện người dùng. VB.NET hiện đại là một ngôn ngữ .NET mạnh mẽ — hãy sử dụng đúng các tính năng của nó.