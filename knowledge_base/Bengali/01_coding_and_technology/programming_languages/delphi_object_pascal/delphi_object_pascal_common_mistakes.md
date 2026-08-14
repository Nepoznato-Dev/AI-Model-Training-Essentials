<!--
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

-->
# ডেলফি / অবজেক্ট প্যাসকেল — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ ডেলফি/অবজেক্ট প্যাসকেলের সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. অবজেক্ট মুক্ত না করা (মেমরি লিক)
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

## 2.`=`বনাম `:=`
```pascal
// ❌ WRONG — confusing assignment and comparison
if x = 5 then  // comparison, not assignment!
  x := 10;     // this is assignment
```

---

## 3. স্ট্রিং ইন্ডেক্সিং (1-ভিত্তিক)
```pascal
// ❌ WRONG — 0-based indexing
var s: string;
s := 'Hello';
s[0]  // Error or unexpected!

// ✅ CORRECT — Delphi strings are 1-indexed
s[1]  // 'H'
```

---

## 4. কনস্ট্রাক্টরগুলিতে`inherited`ব্যবহার করা হচ্ছে না
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

## 5. অ্যান্টি-প্যাটার্ন: ফর্মগুলিতে ব্যবসায়িক যুক্তি
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

## সারাংশ
ডেলফি ফাঁদ: সর্বদা মুক্ত বস্তুগুলি চেষ্টা করে/শেষে,`=`(তুলনা) থেকে`:=`(অ্যাসাইনমেন্ট) আলাদা করুন, স্ট্রিংগুলি 1-সূচীযুক্ত, কনস্ট্রাক্টরগুলিতে`inherited`কল করুন এবং UI থেকে পৃথক ব্যবসায়িক যুক্তি। ডেলফির ভিসিএল/এফএমএক্স কাঠামো উদ্বেগের পরিষ্কার বিচ্ছেদকে পুরস্কৃত করে।