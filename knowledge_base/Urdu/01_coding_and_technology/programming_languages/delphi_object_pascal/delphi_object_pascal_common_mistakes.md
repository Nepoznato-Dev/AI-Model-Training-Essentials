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
# ڈیلفی / آبجیکٹ پاسکل - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز ڈیلفی/آبجیکٹ پاسکل میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کو تصحیح کے ساتھ کیٹلاگ کرتا ہے۔
---

## 1. اشیاء کو آزاد نہیں کرنا (میموری لیکس)
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

## 2.`=`بمقابلہ `:=`
```pascal
// ❌ WRONG — confusing assignment and comparison
if x = 5 then  // comparison, not assignment!
  x := 10;     // this is assignment
```

---

## 3. اسٹرنگ انڈیکسنگ (1 کی بنیاد پر)
```pascal
// ❌ WRONG — 0-based indexing
var s: string;
s := 'Hello';
s[0]  // Error or unexpected!

// ✅ CORRECT — Delphi strings are 1-indexed
s[1]  // 'H'
```

---

## 4. کنسٹرکٹرز میں`inherited`استعمال نہیں کرنا
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

## 5. اینٹی پیٹرن: فارمز میں بزنس لاجک
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

## خلاصہ
ڈیلفی ٹریپس: ہمیشہ مفت اشیاء کو آزمائیں/آخر میں،`=`(موازنہ) کو`:=`(اسائنمنٹ) سے الگ کریں، سٹرنگز 1-انڈیکسڈ ہیں، کنسٹرکٹرز میں`inherited`کو کال کریں، اور UI سے الگ بزنس منطق۔ ڈیلفی کا VCL/FMX فریم ورک تحفظات کی صاف علیحدگی کا انعام دیتا ہے۔