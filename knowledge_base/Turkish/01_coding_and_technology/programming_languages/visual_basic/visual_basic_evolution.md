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

# Visual Basic — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| TEMEL | 1964 | **Orijinal BASIC** (Kemeny ve Kurtz, Dartmouth) |
| GW-TEMEL | 1983 | IBM PC için Microsoft'un BASIC'i |
| QuickBASIC | 1985 | Yapılandırılmış BASIC, IDE, derleyici |
| VB1.0 | 1991 | **Visual Basic 1.0** — Windows için görsel programlama |
| VB2.0 | 1992 | Daha hızlı, nesne tabanlı formlar |
| VB3.0 | 1993 | **Veritabanı desteği** (Veri Kontrolü), Jet motoru |
| VB4.0 | 1995 | 32 bit, sınıflar (kalıtım yok) |
| VB5.0 | 1997 | **COM bileşenleri**, kullanıcı tarafından çizilen kontroller |
| VB6.0 | 1998 | **Binbaşı**: COM, ADO, DCOM, WebClass — klasik VB |
| VB.NET | 2002 | **Ana**: .NET Framework — OOP, miras, GC |
| VB.NET 2003 | 2003 | .NET 1.1, geliştirilmiş IDE |
| VB 2005 | 2005 | **Ad alanım**,`Using`,`Continue`, düzenle ve devam et |
| VB 2008 | 2008 | **LINQ**, XML değişmezleri, anonim türler,`If`operatörü |
| VB 2010 | 2010 | Çok satırlı lambdalar, dinamik, eş/karşıt varyans |
| VB 2012 | 2012 | `Async`/ `Await`, yineleyiciler |
| VB 2015 | 2015 | Dize enterpolasyonu `$""`, boş koşullu `?.`, nameof |
| VB 2017 | 2017 | Tuple'lar, referans dönüşleri, desen eşleştirme |
| VB15.3 | 2017 | İkili olmayan yapısöküm |
| VB15.5 | 2017 | Yerellere, salt okunur üyelere başvurun |
| VB16.0 | 2019 | **Null yapılabilir başvuru türleri**,`Switch`ifadeleri |
| VB16.9 | 2021 | `OrElse`iyileştirmeleri |
| VB17.0 | 2022 | **Ham dize değişmezleri**, otomatik varsayılan yapılar,`Module`iyileştirmeleri |
| VB 17.7 | 2024 | Daha fazla ayrıntılandırma |
## Önemli Kilometre Taşları
### TEMEL Kökenler (1964–1990)
- **1964**: John Kemeny ve Thomas Kurtz, Dartmouth College'da BASIC'i yarattı
- **Hedef**: Programlamayı fen bilimleri dışındaki öğrenciler için de erişilebilir hale getirmek
- **1983**: GW-BASIC — IBM PC için Microsoft'un BASIC'i
- **1985**: QuickBASIC — yapılandırılmış programlama, IDE, derleyici
- Temel özellikler:`GOTO`,`GOSUB`,`LET`,`INPUT`,`PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: Klasik Çağ (1991–2001)
- **1.0 (1991)**: Görsel programlama — Windows için sürükle ve bırak özellikli GUI oluşturucu
- **2.0 (1992)**: Daha hızlı, nesne tabanlı formlar
- **3.0 (1993)**: Veritabanı desteği — Veri Kontrolü, Jet motoru
- **4.0 (1995)**: 32 bit (Windows 95), sınıflar
- **5.0 (1997)**: COM bileşenleri, kullanıcı tarafından çizilen kontroller
- **6.0 (1998)**: **Klasik VB** — COM, ADO, DCOM, WebClass
  - En yaygın kullanılan versiyon
  - Hızlı Uygulama Geliştirme (RAD)
  - Hala milyonlarca eski uygulamayı çalıştırıyor
### VB.NET: .NET Devrimi (2002 – günümüz)
- **2002**: VB.NET — .NET Framework'te tamamen yeniden yazma
  - Gerçek OOP — kalıtım, arayüzler, polimorfizm
  - Çöp toplama
  - .NET sınıf kütüphanesinin tamamına erişim
- **2005**:`My`ad alanı (ortak işlemlere kolay erişim)
- **2008**: **LINQ** — dile entegre edilmiş sorgu sözdizimi
- **2012**:`Async`/`Await`— eşzamansız programlama
- **2015**: Dize enterpolasyonu `$""`, boş koşullu`?.`
- **2017**: Demetler, desen eşleştirme
- **2019**: Null yapılabilir referans türleri
- **2022**: Ham dize değişmezleri, modern sözdizimi
## Söz Dizimi Gelişimi
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

## Özellik Gelişimi
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

## Temel Tasarım İlkeleri
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Ekosistem Büyümesi
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
