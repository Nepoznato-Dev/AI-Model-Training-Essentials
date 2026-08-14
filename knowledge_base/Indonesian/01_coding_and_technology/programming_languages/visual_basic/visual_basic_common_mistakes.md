<!--
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

-->
# Visual Basic — Kesalahan Umum & Anti-Pola
Dokumen ini berisi katalog kesalahan, jebakan, dan anti-pola yang paling umum dalam Visual Basic (VB.NET) beserta koreksinya.
---

## 1. Tidak Membuang Sumber Daya
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

## 2.`=`vs`Is`untuk Perbandingan Objek
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

## 3. Opsi Ketat
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

## 4. Tidak Menggunakan`Using`untuk Koneksi Database
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

## 5. Anti-Pola: Logika Bisnis dalam Pengendali Peristiwa
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

## Ringkasan
Perangkap VB.NET: selalu gunakan`Using`untuk sumber daya sekali pakai, bedakan`=`(nilai) dari`Is`(referensi), aktifkan`Option Strict On`, gunakan blok`Using`untuk koneksi database, dan pisahkan logika bisnis dari event handler UI. VB.NET modern adalah bahasa .NET yang kuat — gunakan fitur-fiturnya dengan benar.