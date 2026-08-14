---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Ada - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، کتابخانه ها و زیرساخت های ضروری در اکوسیستم آدا را پوشش می دهد.
---

## کامپایلرها و پیاده سازی ها
| کامپایلر | نوع | یادداشت ها |
|----------|------|-------|
| **GNAT** | منبع باز | مبتنی بر GCC، پرکاربردترین |
| ** انجمن GNAT ** | رایگان | نسخه رایگان AdaCore |
| **GNAT Pro** | تجاری | دارای گواهینامه ایمنی، AdaCore |
| **ObjectAda** | تجاری | ویندوز، ایمنی حیاتی |
| **ژانوس/آدا** | تجاری | سیستم های تعبیه شده |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## ساخت سیستم ها و مدیریت بسته
| ابزار | هدف |
|------|---------|
| **علی** | مدیر بسته مدرن (توصیه می شود) |
| **GPRbuild** | ابزار ساخت پروژه |
| **GPR (پروژه GNAT)** | فرمت فایل پروژه |
| **ساخت ** | سازهای کلاسیک |
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

## ایمنی و تأیید
| ابزار | هدف |
|------|---------|
| **GNATprove** | تایید رسمی |
| **اسپارک** | زیر مجموعه ایمنی حیاتی |
| **CodePeer** | تجزیه و تحلیل استاتیک |
| **Polyspace** | تایید زمان اجرا |
| **پوشش** | تجزیه و تحلیل استاتیک |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **واحد** | چارچوب تست واحد |
| **آهون** | تست ساده |
| **تست GNAT** | تست مبتنی بر کد |
| **gprbuild** | ساخت و تست |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **Ada.Containers** | وکتورها، نقشه ها، مجموعه ها |
| **Ada.Strings** | هندلینگ رشته |
| **Ada.Text_IO** | ورودی/خروجی کنسول |
| **Ada.Calendar** | تاریخ/زمان |
| **GNATcoll** | ابزارهای GNAT |
| **AWS** | وب سرور آدا |
| **XML/Ada** | تجزیه XML |
| **GID** | رمزگشایی تصویر |
| **SDLAda** | اتصالات SDL2 |
| **GLFW** | پنجره OpenGL |
| **Cortex GNAT Runtime** | تعبیه شده (ARM) |
---

## همزمانی
| ویژگی | هدف |
|---------|---------|
| **وظایف** | موضوعات همزمان |
| **اشیاء محافظت شده** | داده های همگام شده |
| **انتخاب عبارات** | میعادگاه |
| **تماس های ورودی ** | همگام سازی |
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

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **GPS (استودیو برنامه نویسی GNAT)** | IDE AdaCore |
| **VS Code + Ada** | پشتیبانی از زبان آدا |
| **Emacs + ada-mode** | محیط کلاسیک آدا |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **باینری استاتیک** | GNAT باینری های ثابت تولید می کند |
| **تقاطع کامپایل** | کامپایل متقابل GNAT |
| **جاسازی شده** | فلز لخت، RTOS (Ravenscar) |
| **داکر** | کانتینری |
| **گواهینامه ایمنی** | DO-178C، IEC 61508، معیارهای رایج |
---

## خلاصه
اکوسیستم Ada برای سیستم‌های ایمنی حیاتی و با قابلیت اطمینان بالا ساخته شده است. زنجیره ابزار استاندارد عبارتند از: **GNAT** (مبتنی بر GCC) برای کامپایل، **Alire** برای مدیریت بسته، **GPRbuild** برای ساخت، **GNATprove** و **SPARK** برای تأیید رسمی، و **AUnit** برای آزمایش. Ada در هوافضا (DO-178C)، دفاع، راه‌آهن، دستگاه‌های پزشکی و هر حوزه‌ای که صحت آن در اولویت است، برتری دارد. نقاط قوت Ada عبارتند از تایپ قوی، همزمانی (وظایف، اشیاء محافظت شده)، تأیید رسمی (SPARK) و گواهی ایمنی. اکوسیستم برای سیستم های تعبیه شده از نظر ایمنی ضروری است.