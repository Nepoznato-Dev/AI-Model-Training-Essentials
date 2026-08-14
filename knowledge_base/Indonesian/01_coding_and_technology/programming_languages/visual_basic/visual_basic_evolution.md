---
# Metadata
title: "Visual Basic — Version History & Evolution"
description: "Comprehensive version history and evolution of Visual Basic from VB 1.0 to modern VB.NET."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [visual-basic, vb6, vbdotnet, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Visual Basic — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| DASAR | 1964 | **DASAR Asli** (Kemeny & Kurtz, Dartmouth) |
| GW-DASAR | 1983 | BASIC Microsoft untuk IBM PC |
| QuickBASIC | 1985 | BASIC Terstruktur, IDE, kompiler |
| VB 1.0 | 1991 | **Visual Basic 1.0** — pemrograman visual untuk Windows |
| VB 2.0 | 1992 | Formulir berbasis objek yang lebih cepat |
| VB 3.0 | 1993 | **Dukungan basis data** (Kontrol Data), mesin Jet |
| VB 4.0 | 1995 | 32-bit, kelas (tanpa warisan) |
| VB 5.0 | 1997 | **Komponen COM**, kontrol yang dibuat pengguna |
| VB 6.0 | 1998 | **Mayor**: COM, ADO, DCOM, WebClass — VB klasik |
| VB.NET | 2002 | **Utama**: .NET Framework — OOP, warisan, GC |
| VB.NET 2003 | 2003 | .NET 1.1, IDE yang ditingkatkan |
| VB 2005 | 2005 | **Namespace saya**,`Using`,`Continue`, edit-dan-lanjutkan |
| VB 2008 | 2008 | **LINQ**, literal XML, tipe anonim, operator`If`|
| VB 2010 | 2010 | Lambda multi-baris, dinamis, co/contra-variance |
| VB 2012 | 2012 | `Async`/`Await`, iterator |
| VB 2015 | 2015 | Interpolasi string`$""`, kondisional nol`?.`, nameof |
| VB 2017 | 2017 | Tupel, pengembalian ref, pencocokan pola |
| VB 15.3 | 2017 | Dekonstruksi non-tuple |
| VB 15.5 | 2017 | Referensikan penduduk setempat, anggota hanya baca |
| VB 16.0 | 2019 | **Jenis referensi yang tidak dapat dibatalkan**, ekspresi`Switch`|
| VB 16.9 | 2021 |  Peningkatan`OrElse`|
| VB 17.0 | 2022 | **Literal string mentah**, struct default otomatis, penyempurnaan`Module`|
| VB 17.7 | 2024 | Penyempurnaan lebih lanjut |
## Tonggak Penting
### Asal Usul DASAR (1964–1990)
- **1964**: John Kemeny & Thomas Kurtz membuat BASIC di Dartmouth College
- **Sasaran**: Menjadikan pemrograman dapat diakses oleh siswa non-sains
- **1983**: GW-BASIC — BASIC Microsoft untuk IBM PC
- **1985**: QuickBASIC — pemrograman terstruktur, IDE, kompiler
- Fitur utama: `GOTO`, `GOSUB`, `LET`, `INPUT`, `PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: Era Klasik (1991–2001)
- **1.0 (1991)**: Pemrograman visual — pembuat GUI seret dan lepas untuk Windows
- **2.0 (1992)**: Formulir berbasis objek yang lebih cepat
- **3.0 (1993)**: Dukungan basis data — Kontrol Data, mesin Jet
- **4.0 (1995)**: 32-bit (Windows 95), kelas
- **5.0 (1997)**: Komponen COM, kontrol yang dibuat pengguna
- **6.0 (1998)**: **VB klasik** — COM, ADO, DCOM, WebClass
  - Versi yang paling banyak digunakan
  - Pengembangan Aplikasi Cepat (RAD)
  - Masih menjalankan jutaan aplikasi lawas
### VB.NET: Revolusi .NET (2002–sekarang)
- **2002**: VB.NET — menyelesaikan penulisan ulang di .NET Framework
  - OOP Sejati — pewarisan, antarmuka, polimorfisme
  - Pengumpulan sampah
  - Akses ke seluruh perpustakaan kelas .NET
- **2005**: namespace`My`(akses mudah ke operasi umum)
- **2008**: **LINQ** — sintaks kueri terintegrasi ke dalam bahasa
- **2012**:`Async`/`Await`— pemrograman asinkron
- **2015**: Interpolasi string`$""`, kondisional nol`?.`
- **2017**: Tuple, pencocokan pola
- **2019**: Jenis referensi yang tidak dapat dibatalkan
- **2022**: Literal string mentah, sintaksis modern
## Evolusi Sintaks
```vb
' GW-BASIC (1983): Line numbers, GOTO
10 INPUT "Name: "; N$
20 PRINT "Hello, "; N$
30 GOTO 10

' QuickBASIC (1985): Structured programming
INPUT "Name: "; N$
PRINT "Hello, "; N$
FOR I = 1 TO 10
    PRINT I
NEXT I

' Visual Basic 6.0 (1998): Event-driven, GUI
Private Sub Command1_Click()
    Dim name As String
    name = Text1.Text
    MsgBox "Hello, " & name & "!"
End Sub

' VB.NET 2002: OOP, .NET
Class Person
    Public Name As String
    Public Age As Integer

    Sub New(ByVal n As String, ByVal a As Integer)
        Name = n
        Age = a
    End Sub
End Class

' VB 2008: LINQ
Dim query = From p In people
            Where p.Age > 18
            Select p.Name

' VB 2015: String interpolation, null-conditional
Dim message = $"Hello, {person?.Name ?? "Unknown"}!"

' VB 2017: Tuples, pattern matching
Dim result = (Name:="Alice", Age:=30)
Select Case result
    Case ("Alice", 30)
        Console.WriteLine("Found Alice!")
End Select

' VB 17.0 (2022): Raw string literals
Dim json = """
    {
        "name": "Alice",
        "age": 30
    }
    """

' Modern VB.NET: Async/Await
Async Function GetDataAsync() As Task(Of String)
    Dim client As New HttpClient()
    Dim result = Await client.GetStringAsync("https://api.example.com/data")
    Return result
End Function
```

## Evolusi Fitur
```
BASIC (1964):    INPUT, PRINT, LET, FOR/NEXT, GOTO, GOSUB
QuickBASIC (1985): Structured programming, SUB/FUNCTION, TYPE
VB 1.0 (1991):   Visual programming, event-driven, GUI builder
VB 3.0 (1993):   Database (Data Control, Jet)
VB 4.0 (1995):   32-bit, classes
VB 6.0 (1998):   COM, ADO, DCOM, WebClass
VB.NET (2002):   OOP, GC, .NET Framework
VB 2005:         My namespace, Using, edit-and-continue
VB 2008:         LINQ, XML literals, anonymous types
VB 2012:         Async/Await, iterators
VB 2015:         String interpolation, null-conditional
VB 2017:         Tuples, pattern matching
VB 16.0 (2019):  Nullable reference types
VB 17.0 (2022):  Raw string literals, auto-default structs
```

## Prinsip Desain Utama
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Pertumbuhan Ekosistem
```
1964: BASIC created at Dartmouth College
1983: GW-BASIC — Microsoft BASIC for PC
1985: QuickBASIC — structured programming
1991: Visual Basic 1.0 — visual programming
1998: VB 6.0 — classic VB, COM, ADO
2002: VB.NET — .NET Framework, OOP
2008: VB 2008 — LINQ
2012: VB 2012 — async/await
2022: VB 17.0 — raw string literals, modern syntax
2025: Visual Basic (.NET) used in:
       - Windows desktop applications (WinForms, WPF)
       - Legacy VB6 applications (still running in businesses)
       - Office automation (VBA — Visual Basic for Applications)
       - ASP.NET web applications
       Microsoft continues VB.NET alongside C# on .NET
       VBA still embedded in Excel, Word, Access, Outlook
```
