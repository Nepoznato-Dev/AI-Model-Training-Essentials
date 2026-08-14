<!--
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

-->
#Ada — دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والمكتبات والبنية التحتية الأساسية في نظام Ada البيئي.
---

## المترجمون والتطبيقات
| مترجم | اكتب | ملاحظات |
|----------|------|-------|
| **جنات** | مفتوح المصدر | مقرها في دول مجلس التعاون الخليجي، والأكثر استخدامًا |
| **مجتمع GNAT** | مجاني | النسخة المجانية من AdaCore |
| **جنات برو** | تجاري | شهادة السلامة، AdaCore |
| **ObjectAda** | تجاري | نوافذ ذات أهمية كبيرة للسلامة |
| ** يانوس / آدا ** | تجاري | الأنظمة المدمجة |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## بناء الأنظمة وإدارة الحزم
| أداة | الغرض |
|------|---------|
| **علي** | مدير الحزم الحديث (مستحسن) |
| ** جي بي آر بيلد ** | أداة بناء المشروع |
| **GPR (مشروع GNAT)** | تنسيق ملف المشروع |
| **اصنع** | بنيات كلاسيكية |
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

## السلامة والتحقق
| أداة | الغرض |
|------|---------|
| **GNATprove** | التحقق الرسمي |
| **سبارك** | مجموعة فرعية حرجة للسلامة |
| **كود بير** | التحليل الساكن |
| **بولي سبيس** | التحقق من وقت التشغيل |
| **التغطية** | التحليل الساكن |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **وحدة** | إطار اختبار الوحدة |
| **أهفن** | اختبار بسيط |
| ** اختبار GNAT ** | الاختبار القائم على الكود |
| **gprbuild** | بناء واختبار |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **Ada.Containers** | المتجهات، الخرائط، المجموعات |
| **Ada.Strings** | التعامل مع السلسلة |
| **Ada.Text_IO** | وحدة الإدخال / الإخراج |
| **Ada.Calendar** | التاريخ/الوقت |
| **جناتكول** | المرافق GNAT |
| ** أوس ** | خادم الويب آدا |
| **XML/Ada** | تحليل XML |
| ** دائرة المخابرات العامة ** | فك تشفير الصور |
| **SDLAda** | روابط SDL2 |
| **جلفو** | نوافذ برنامج OpenGL |
| ** وقت تشغيل Cortex GNAT ** | مضمن (ARM) |
---

## التزامن
| ميزة | الغرض |
|---------|--------|
| **المهام** | المواضيع المتزامنة |
| **الكائنات المحمية** | البيانات المتزامنة |
| **اختر البيانات** | موعد |
| **مكالمات الدخول** | التزامن |
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

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **GPS (استوديو برمجة GNAT)** | بيئة تطوير متكاملة لـ AdaCore |
| **رمز VS + Ada** | دعم لغة آدا |
| ** إيماكس + وضع آدا ** | بيئة آدا الكلاسيكية |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **ثنائي ثابت** | GNAT تنتج ثنائيات ثابتة |
| ** الترجمة المتقاطعة ** | GNAT عبر تجميع |
| **مضمن** | المعدن العاري، RTOS (Ravenscar) |
| ** عامل الميناء ** | في حاويات |
| **شهادة السلامة** | DO-178C، IEC 61508، المعايير المشتركة |
---

## ملخص
تم تصميم نظام Ada البيئي خصيصًا لأنظمة السلامة الحرجة وذات الموثوقية العالية. سلسلة الأدوات القياسية هي: **GNAT** (المعتمدة على دول مجلس التعاون الخليجي) للتجميع، **Alire** لإدارة الحزم، **GPRbuild** للبنيات، **GNATprove** و **SPARK** للتحقق الرسمي، و **AUnit** للاختبار. تتفوق Ada في مجال الطيران (DO-178C)، والدفاع، والسكك الحديدية، والأجهزة الطبية، وأي مجال تكون فيه الصحة أمرًا بالغ الأهمية. تتمثل نقاط قوة Ada في الكتابة القوية، والتزامن (المهام، والكائنات المحمية)، والتحقق الرسمي (SPARK)، وشهادة السلامة. يعد النظام البيئي ضروريًا للأنظمة المدمجة ذات الأهمية الحيوية للسلامة.