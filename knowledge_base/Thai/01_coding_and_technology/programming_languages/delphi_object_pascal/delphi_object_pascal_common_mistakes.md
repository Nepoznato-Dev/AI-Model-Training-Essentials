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
# Delphi / Object Pascal - ข้อผิดพลาดทั่วไปและรูปแบบการต่อต้าน
เอกสารนี้รวบรวมข้อผิดพลาด กับดัก และรูปแบบการต่อต้านที่พบบ่อยที่สุดใน Delphi/Object Pascal พร้อมการแก้ไข
---

## 1. ไม่ปล่อยวัตถุ (หน่วยความจำรั่ว)
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

## 2.`=`กับ `:=`
```pascal
// ❌ WRONG — confusing assignment and comparison
if x = 5 then  // comparison, not assignment!
  x := 10;     // this is assignment
```

---

## 3. การจัดทำดัชนีสตริง (1-Based)
```pascal
// ❌ WRONG — 0-based indexing
var s: string;
s := 'Hello';
s[0]  // Error or unexpected!

// ✅ CORRECT — Delphi strings are 1-indexed
s[1]  // 'H'
```

---

## 4. ไม่ได้ใช้`inherited`ในตัวสร้าง
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

## 5. การต่อต้านรูปแบบ: ตรรกะทางธุรกิจในรูปแบบ
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

## สรุป
Delphi traps: ปล่อยวัตถุด้วยการลอง/สุดท้ายเสมอ แยก`=`(การเปรียบเทียบ) จาก`:=`(การกำหนด) สตริงเป็น 1 ดัชนี เรียก`inherited`ในตัวสร้าง และแยกตรรกะทางธุรกิจออกจาก UI กรอบงาน VCL/FMX ของ Delphi ตอบแทนการแยกข้อกังวลอย่างชัดเจน