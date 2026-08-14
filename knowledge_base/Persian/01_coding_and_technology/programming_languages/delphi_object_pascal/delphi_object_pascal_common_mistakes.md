---
# Metadata
title: "Delphi / Object Pascal — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Delphi/Object Pascal with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# دلفی / آبجکت پاسکال - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها در دلفی/ابجکت پاسکال را با اصلاحات فهرست می کند.
---

## 1. آزاد نکردن اشیا (نشت حافظه)
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

## 2.`=`در مقابل `:=`
```pascal
// ❌ WRONG — confusing assignment and comparison
if x = 5 then  // comparison, not assignment!
  x := 10;     // this is assignment
```

---

## 3. فهرست بندی رشته ای (بر اساس 1)
```pascal
// ❌ WRONG — 0-based indexing
var s: string;
s := 'Hello';
s[0]  // Error or unexpected!

// ✅ CORRECT — Delphi strings are 1-indexed
s[1]  // 'H'
```

---

## 4. عدم استفاده از`inherited`در سازنده ها
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

## 5. ضد الگو: منطق تجاری در اشکال
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

## خلاصه
تله‌های دلفی: همیشه اشیاء را با try/finally آزاد کنید،`=`(مقایسه) را از`:=`(تخصیص) متمایز کنید، رشته‌ها ۱-شاخص هستند،`inherited`را در سازنده‌ها فراخوانی کنید، و منطق تجاری را از UI جدا کنید. چارچوب VCL/FMX دلفی به تفکیک دقیق نگرانی ها پاداش می دهد.