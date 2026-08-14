---
# Metadata
title: "Delphi / Object Pascal — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Delphi/Object Pascal with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [delphi, object-pascal, common-mistakes, anti-patterns, pitfalls, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Delphi / Object Pascal — 常见错误和反模式
本文档列出了 Delphi/Object Pascal 中最常见的错误、陷阱和反模式，并进行了更正。
---

## 1. 不释放对象（内存泄漏）
```pascal
// ❌ WRONG — object never freed
procedure Process;
var
  List: TStringList;
begin
  List := TStringList.Create;
  List.Add('data');
  // List is never freed!
end;

// ✅ CORRECT — try/finally
procedure Process;
var
  List: TStringList;
begin
  List := TStringList.Create;
  try
    List.Add('data');
  finally
    List.Free;
  end;
end;
```

---

## 2.`=`与 `:=`
```pascal
// ❌ WRONG — confusing assignment and comparison
if x = 5 then  // comparison, not assignment!
  x := 10;     // this is assignment
```

---

## 3. 字符串索引（从 1 开始）
```pascal
// ❌ WRONG — 0-based indexing
var s: string;
s := 'Hello';
s[0]  // Error or unexpected!

// ✅ CORRECT — Delphi strings are 1-indexed
s[1]  // 'H'
```

---

## 4. 在构造函数中不使用 `inherited`
```pascal
// ❌ WRONG — skipping parent constructor
constructor TMyClass.Create(AName: string);
begin
  FName := AName;  // parent's Create never called!
end;

// ✅ CORRECT — call inherited
constructor TMyClass.Create(AName: string);
begin
  inherited Create;  // or inherited Create(AName)
  FName := AName;
end;
```

---

## 5. 反模式：表单中的业务逻辑
```pascal
// ❌ WRONG — all logic in form events
procedure TForm1.btnSaveClick(Sender: TObject);
begin
  // database access, validation, email sending, all here
end;

// ✅ CORRECT — separate business logic
procedure TForm1.btnSaveClick(Sender: TObject);
begin
  UserService.Save(edtName.Text, edtEmail.Text);
end;
```

---

＃＃ 概括
Delphi 陷阱：始终使用 try/finally 释放对象，区分 `=`（比较）和 `:=`（赋值），字符串索引为 1，在构造函数中调用 `inherited`，并将业务逻辑与 UI 分开。 Delphi 的 VCL/FMX 框架奖励干净的关注点分离。