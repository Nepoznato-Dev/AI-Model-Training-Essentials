---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ada, ecosystem, tooling, compilers, safety-critical, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Ada — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ اڈا ماحولیاتی نظام میں ضروری ٹولز، لائبریریوں اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## مرتب کرنے والے اور عمل درآمد
| مرتب کرنے والا | قسم | نوٹس |
|------------|------|------|
| **GNAT** | اوپن سورس | GCC پر مبنی، سب سے زیادہ استعمال ہونے والا |
| **GNAT کمیونٹی** | مفت | اڈا کور کا مفت ایڈیشن |
| **GNAT پرو** | کمرشل | سیفٹی سے تصدیق شدہ، AdaCore |
| **ObjectAda** | کمرشل | ونڈوز، حفاظت کے لیے اہم |
| **جانس/اڈا** | کمرشل | ایمبیڈڈ سسٹمز |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## سسٹمز اور پیکیج مینجمنٹ بنائیں
| ٹول | مقصد |
|------|---------|
| **الیرے** | جدید پیکیج مینیجر (تجویز کردہ) |
| **GPRbuild** | پروجیکٹ کی تعمیر کا آلہ |
| **GPR (GNAT پروجیکٹ)** | پروجیکٹ فائل فارمیٹ |
| **بناؤ** | کلاسیکی تعمیرات |
```toml
# alire.toml
name = "myapp"
description = "My Ada application"
version = "0.1.0"

[[depends-on]]
gnat = "^13"
gnatcoll = "^24"

[[pins]]
```

```bash
alr init --bin myapp      # create project
alr build                 # build
alr run                   # run
alr get --build gnatcoll  # get dependency
alr search                # search packages
alr index                 # update index
```

```gpr
-- myproject.gpr
project Myproject is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Main use ("main.adb");
   
   package Compiler is
      for Default_Switches ("Ada") use ("-gnatwa", "-gnatVa", "-O2");
   end Compiler;
   
   package Binder is
      for Default_Switches ("Ada") use ("-E");  -- store exceptions
   end Binder;
end Myproject;
```

---

## حفاظت اور تصدیق
| ٹول | مقصد |
|------|---------|
| **GNATprove** | رسمی تصدیق |
| **چنگاری** | حفاظتی اہم ذیلی سیٹ |
| **CodePeer** | جامد تجزیہ |
| **پولی اسپیس** | رن ٹائم تصدیق |
| **کوریت** | جامد تجزیہ |
```ada
-- SPARK example
package Stack with
   SPARK_Mode
is
   type Bounded_Stack (Capacity : Positive) is tagged private;
   
   procedure Push (S : in out Bounded_Stack; Element : Integer)
      with Pre  => not S.Is_Full,
           Post => not S.Is_Empty and S.Top = Element;
   
   function Is_Full (S : Bounded_Stack) return Boolean;
   function Is_Empty (S : Bounded_Stack) return Boolean;
   
private
   type Bounded_Stack (Capacity : Positive) is tagged record
      Data : array (1 .. Capacity) of Integer;
      Top_Index : Natural := 0;
   end record;
end Stack;
```

---

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **AUnit** | یونٹ ٹیسٹنگ فریم ورک |
| **احون** | سادہ ٹیسٹنگ |
| **GNATtest** | کوڈ پر مبنی ٹیسٹنگ |
| **gprbuild** | تعمیر اور جانچ |
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Stack_Test is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;
   
   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Stack_Test;

package body Stack_Test is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("Stack Tests");
   end Name;
   
   procedure Run_Test (T : in out Test_Case) is
      S : Bounded_Stack (10);
   begin
      Push (S, 42);
      AUnit.Assertions.Assert (Top (S) = 42, "Top should be 42");
      AUnit.Assertions.Assert (not Is_Empty (S), "Should not be empty");
   end Run_Test;
end Stack_Test;
```

---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **Ada.Containers** | ویکٹر، نقشے، سیٹ |
| **Ada.Strings** | سٹرنگ ہینڈلنگ |
| **Ada.Text_IO** | کنسول I/O |
| **Ada.Calendar** | تاریخ/وقت |
| **GNATcoll** | GNAT افادیت |
| **AWS** | اڈا ویب سرور |
| **XML/Ada** | XML پارسنگ |
| **GID** | تصویر کی ضابطہ کشائی |
| **SDLAda** | SDL2 پابندیاں |
| **GLFW** | اوپن جی ایل ونڈونگ |
| **Cortex GNAT رن ٹائم** | ایمبیڈڈ (ARM) |
---

## ہم آہنگی۔
| خصوصیت | مقصد |
|---------|---------|
| **ٹاسک** | کنکرنٹ تھریڈز |
| **محفوظ اشیاء** | مطابقت پذیر ڈیٹا |
| **بیانات کو منتخب کریں** | ملاقات |
| **انٹری کالز** | ہم وقت سازی |
```ada
task type Worker is
   entry Do_Work (Item : in Integer);
end Worker;

task body Worker is
   Value : Integer;
begin
   loop
      select
         accept Do_Work (Item : in Integer) do
            Value := Item;
         end Do_Work;
         Process (Value);
      or
         terminate;
      end select;
   end loop;
end Worker;
```

---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **GPS (GNAT پروگرامنگ اسٹوڈیو)** | اڈا کور کا IDE |
| **VS کوڈ + Ada** | اڈا زبان کی حمایت |
| **Emacs + ada-mode** | کلاسیکی اڈا ماحول |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **جامد بائنری** | GNAT جامد بائنریز تیار کرتا ہے |
| **کراس کمپائل** | GNAT کراس تالیف |
| **ایمبیڈڈ** | ننگی دھات، RTOS (Ravenscar) |
| **ڈوکر** | کنٹینرائزڈ |
| **حفاظتی سرٹیفیکیشن** | DO-178C, IEC 61508, مشترکہ معیار |
---

## خلاصہ
Ada کا ماحولیاتی نظام حفاظت کے لیے اہم اور اعلیٰ قابل اعتماد نظاموں کے لیے بنایا گیا ہے۔ معیاری ٹول چین یہ ہے: تالیف کے لیے **GNAT** (GCC-based)، **Alire** پیکج کے انتظام کے لیے، **GPRbuild** تعمیرات کے لیے، **GNATprove** اور **SPARK** رسمی تصدیق کے لیے، اور **AUnit** جانچ کے لیے۔ Ada ایرو اسپیس (DO-178C)، دفاع، ریلوے، طبی آلات، اور کسی بھی ڈومین میں جہاں درستگی سب سے اہم ہے۔ Ada کی طاقتیں مضبوط ٹائپنگ، ہم آہنگی (ٹاسک، محفوظ اشیاء)، رسمی تصدیق (SPARK)، اور حفاظتی سرٹیفیکیشن ہیں۔ ماحولیاتی نظام حفاظتی اہم ایمبیڈڈ سسٹمز کے لیے ضروری ہے۔