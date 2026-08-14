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

# Visual Basic — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|ベーシック | 1964年 | **オリジナル BASIC** (Kemony & Kurtz、ダートマス) |
| GWベーシック | 1983年 | Microsoft の IBM PC 用 BASIC |
|クイックベーシック | 1985年 |構造化BASIC、IDE、コンパイラ |
| VB1.0 | 1991年 | **Visual Basic 1.0** — Windows 用ビジュアル プログラミング |
| VB2.0 | 1992年 |より高速なオブジェクトベースのフォーム |
| VB3.0 | 1993年 | **データベース サポート** (データ コントロール)、Jet エンジン |
| VB4.0 | 1995年 | 32 ビット、クラス (継承なし) |
| VB5.0 | 1997年 | **COM コンポーネント**、ユーザー描画コントロール |
| VB6.0 | 1998年 | **主要な**: COM、ADO、DCOM、WebClass — 古典的な VB |
| VB.NET | 2002年 | **主な**: .NET Framework — OOP、継承、GC |
| VB.NET 2003 | 2003年 | .NET 1.1、改良された IDE |
| VB2005 | 2005年 | **私の名前空間**、`Using`、`Continue`、編集して続行 |
| VB2008 | 2008年 | **LINQ**、XML リテラル、匿名型、`If` 演算子 |
| VB2010 | 2010年 |複数行のラムダ、動的、共分散/反分散 |
| VB2012 | 2012年 | `Async`/`Await`、イテレータ |
| VB2015 | 2015年 |文字列補間`$""`、null 条件付き`?.`、nameof |
| VB2017 | 2017年 |タプル、ref 戻り値、パターン マッチング |
| VB15.3 | 2017年 |非タプル分解 |
| VB15.5 | 2017年 |参照ローカル、読み取り専用メンバー |
| VB16.0 | 2019年 | **NULL 許容参照型**、`Switch` 式 |
| VB16.9 | 2021年 | `OrElse`の改善 |
| VB17.0 | 2022年 | **生の文字列リテラル**、自動デフォルト構造体、`Module` の改善 |
| VB17.7 | 2024年 |さらなる改良 |
## 主要なマイルストーン
### BASIC の起源 (1964 ～ 1990 年)
- **1964**: ジョン・ケメニーとトーマス・カーツがダートマス大学で BASIC を作成
- **目標**: 理系以外の学生もプログラミングにアクセスできるようにする
- **1983**: GW-BASIC — Microsoft の IBM PC 用 BASIC
- **1985**: QuickBASIC — 構造化プログラミング、IDE、コンパイラー
- 主な機能:`GOTO`、`GOSUB`、`LET`、`INPUT`、`PRINT`、`FOR`/ `NEXT`
### Visual Basic 1 ～ 6: クラシック時代 (1991 ～ 2001)
- **1.0 (1991)**: ビジュアル プログラミング — Windows 用のドラッグ アンド ドロップ GUI ビルダー
- **2.0 (1992)**: より高速なオブジェクトベースのフォーム
- **3.0 (1993)**: データベースのサポート — データ コントロール、ジェット エンジン
- **4.0 (1995)**: 32 ビット (Windows 95)、クラス
- **5.0 (1997)**: COM コンポーネント、ユーザー描画コントロール
- **6.0 (1998)**: **古典的な VB** — COM、ADO、DCOM、WebClass
  - 最も広く使用されているバージョン
  - 迅速なアプリケーション開発 (RAD)
  - 数百万ものレガシー アプリケーションが依然として実行されている
### VB.NET: .NET 革命 (2002 ～現在)
- **2002**: VB.NET — .NET Framework で完全に書き直されました
  - 真の OOP — 継承、インターフェース、ポリモーフィズム
  - ガベージコレクション
  - .NET クラス ライブラリ全体へのアクセス
- **2005**:`My`名前空間 (一般的な操作への簡単なアクセス)
- **2008**: **LINQ** — 言語に統合されたクエリ構文
- **2012**:`Async`/`Await`— 非同期プログラミング
- **2015**: 文字列補間`$""`、null 条件付き`?.`
- **2017**: タプル、パターン マッチング
- **2019**: Null 許容参照型
- **2022**: 生の文字列リテラル、最新の構文
## 構文の進化
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

## 機能の進化
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

## 主要な設計原則
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## エコシステムの成長
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
