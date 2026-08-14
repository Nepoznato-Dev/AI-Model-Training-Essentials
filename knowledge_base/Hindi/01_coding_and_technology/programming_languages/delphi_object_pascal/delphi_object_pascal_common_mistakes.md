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
# डेल्फ़ी / ऑब्जेक्ट पास्कल - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ डेल्फ़ी/ऑब्जेक्ट पास्कल में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1. वस्तुओं को मुक्त नहीं करना (मेमोरी लीक)
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

## 2.`=`बनाम `:=`
```pascal
// ❌ WRONG — confusing assignment and comparison
if x = 5 then  // comparison, not assignment!
  x := 10;     // this is assignment
```

---

## 3. स्ट्रिंग इंडेक्सिंग (1-आधारित)
```pascal
// ❌ WRONG — 0-based indexing
var s: string;
s := 'Hello';
s[0]  // Error or unexpected!

// ✅ CORRECT — Delphi strings are 1-indexed
s[1]  // 'H'
```

---

## 4. कंस्ट्रक्टर्स में`inherited`का उपयोग नहीं करना
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

## 5. एंटी-पैटर्न: फॉर्म में बिजनेस लॉजिक
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

## सारांश
डेल्फ़ी जाल: प्रयास/अंत में हमेशा मुक्त ऑब्जेक्ट,`=`(तुलना) को`:=`(असाइनमेंट) से अलग करें, स्ट्रिंग्स 1-अनुक्रमित हैं, कंस्ट्रक्टर्स में`inherited`को कॉल करें, और यूआई से व्यावसायिक तर्क को अलग करें। डेल्फ़ी का वीसीएल/एफएमएक्स ढांचा चिंताओं के स्पष्ट पृथक्करण को पुरस्कृत करता है।