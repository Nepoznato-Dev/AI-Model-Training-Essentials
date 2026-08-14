---
# Metadata
title: "Visual Basic — Version History & Evolution"
description: "Comprehensive version history and evolution of Visual Basic from VB 1.0 to modern VB.NET."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Visual Basic — 버전 기록 및 발전
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 기본 | 1964년 | **오리지널 베이직** (Kemeny & Kurtz, 다트머스) |
| GW-베이직 | 1983년 | IBM PC용 Microsoft BASIC |
| 퀵베이직 | 1985 | 구조화된 BASIC, IDE, 컴파일러 |
| VB 1.0 | 1991 | **Visual Basic 1.0** — Windows용 시각적 프로그래밍 |
| VB 2.0 | 1992 | 더욱 빨라진 객체 기반 양식 |
| VB 3.0 | 1993년 | **데이터베이스 지원**(데이터 제어), 제트 엔진 |
| 비주얼 베이직 4.0 | 1995 | 32비트, 클래스(상속 없음) |
| VB 5.0 | 1997 | **COM 구성요소**, 사용자가 그린 컨트롤 |
| VB 6.0 | 1998 | **주요**: COM, ADO, DCOM, WebClass — 클래식 VB |
| VB.NET | 2002 | **주요**: .NET Framework — OOP, 상속, GC |
| VB.NET 2003 | 2003년 | .NET 1.1, 향상된 IDE |
| VB 2005 | 2005년 | **내 네임스페이스**,`Using`,`Continue`, 편집하고 계속하기 |
| VB 2008 | 2008 | **LINQ**, XML 리터럴, 익명 유형,`If`연산자 |
| VB 2010 | 2010 | 여러 줄 람다, 동적, 공분산/반분산 |
| VB 2012 | 2012 | `Async`/`Await`, 반복자 |
| VB 2015 | 2015 | 문자열 보간`$""`, null 조건부`?.`, nameof |
| VB 2017 | 2017 | 튜플, 참조 반환, 패턴 일치 |
| VB 15.3 | 2017 | 비튜플 분해 |
| VB 15.5 | 2017 | 참조 로컬, 읽기 전용 회원 |
| VB 16.0 | 2019 | **Nullable 참조 유형**,`Switch`표현식 |
| VB 16.9 | 2021 | `OrElse`개선 |
| VB 17.0 | 2022 | **원시 문자열 리터럴**, 자동 기본 구조체,`Module`개선 |
| VB 17.7 | 2024 | 추가 개선 |
## 주요 이정표
### 기본 기원(1964~1990)
- **1964**: John Kemeny와 Thomas Kurtz가 Dartmouth College에서 BASIC을 창안함
- **목표**: 과학을 전공하지 않은 학생들도 프로그래밍에 접근할 수 있도록 합니다.
- **1983**: GW-BASIC — IBM PC용 Microsoft BASIC
- **1985**: QuickBASIC — 구조적 프로그래밍, IDE, 컴파일러
- 주요 기능:`GOTO`,`GOSUB`,`LET`,`INPUT`,`PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: 고전 시대(1991–2001)
- **1.0(1991)**: 시각적 프로그래밍 — Windows용 끌어서 놓기 GUI 빌더
- **2.0(1992)**: 더욱 빨라진 객체 기반 양식
- **3.0(1993)**: 데이터베이스 지원 — 데이터 제어, 제트 엔진
- **4.0(1995)**: 32비트(Windows 95), 클래스
- **5.0(1997)**: COM 구성 요소, 사용자가 그린 컨트롤
- **6.0(1998)**: **클래식 VB** — COM, ADO, DCOM, WebClass
  - 가장 널리 사용되는 버전
  - 신속한 애플리케이션 개발(RAD)
  - 여전히 수백만 개의 레거시 애플리케이션을 실행하고 있습니다.
### VB.NET: .NET 혁명(2002~현재)
- **2002**: VB.NET — .NET Framework에서 전체 재작성
  - 진정한 OOP — 상속, 인터페이스, 다형성
  - 쓰레기 수거
  - 전체 .NET 클래스 라이브러리에 액세스
- **2005**:`My`네임스페이스(일반 작업에 쉽게 접근)
- **2008**: **LINQ** — 언어에 통합된 쿼리 구문
- **2012**:`Async`/`Await`— 비동기 프로그래밍
- **2015**: 문자열 보간`$""`, null 조건부`?.`
- **2017**: 튜플, 패턴 일치
- **2019**: Null 허용 참조 유형
- **2022**: 원시 문자열 리터럴, 최신 구문
## 구문 진화
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

## 기능 진화
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

## 주요 디자인 원칙
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## 생태계 성장
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
