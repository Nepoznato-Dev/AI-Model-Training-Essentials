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
# অ্যাডা — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি অ্যাডা ইকোসিস্টেমের প্রয়োজনীয় সরঞ্জাম, লাইব্রেরি এবং অবকাঠামো কভার করে।
---

## কম্পাইলার এবং বাস্তবায়ন
| কম্পাইলার | প্রকার | নোট |
|----------|------|-------|
| **GNAT** | ওপেন সোর্স | GCC-ভিত্তিক, সর্বাধিক ব্যবহৃত |
| **GNAT সম্প্রদায়** | বিনামূল্যে | AdaCore এর বিনামূল্যের সংস্করণ |
| **GNAT প্রো** | বাণিজ্যিক | নিরাপত্তা-প্রত্যয়িত, AdaCore |
| **অবজেক্টএডা** | বাণিজ্যিক | উইন্ডোজ, নিরাপত্তা-সমালোচনা |
| **জানুস/আদা** | বাণিজ্যিক | এমবেডেড সিস্টেম |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## সিস্টেম এবং প্যাকেজ ম্যানেজমেন্ট তৈরি করুন
| টুল | উদ্দেশ্য |
|------|---------|
| **আলিরে** | আধুনিক প্যাকেজ ম্যানেজার (প্রস্তাবিত) |
| **জিপিআরবিল্ড** | প্রকল্প নির্মাণ টুল |
| **GPR (GNAT প্রকল্প)** | প্রকল্প ফাইল বিন্যাস |
| **বানান** | ক্লাসিক নির্মাণ |
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

## নিরাপত্তা ও যাচাইকরণ
| টুল | উদ্দেশ্য |
|------|---------|
| **GNATপ্রমাণ** | আনুষ্ঠানিক যাচাই |
| **স্পার্ক** | নিরাপত্তা-গুরুত্বপূর্ণ উপসেট |
| **কোডপিয়ার** | স্ট্যাটিক বিশ্লেষণ |
| **পলিস্পেস** | রানটাইম যাচাইকরণ |
| **আচ্ছন্নতা** | স্ট্যাটিক বিশ্লেষণ |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **AUnit** | ইউনিট টেস্টিং ফ্রেমওয়ার্ক |
| **আহভেন** | সহজ পরীক্ষা |
| **GNATtest** | কোড ভিত্তিক পরীক্ষা |
| **gprbuild** | নির্মাণ এবং পরীক্ষা |
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

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **Ada.Containers** | ভেক্টর, মানচিত্র, সেট |
| **Ada.Strings** | স্ট্রিং হ্যান্ডলিং |
| **Ada.Text_IO** | কনসোল I/O |
| **Ada.Calendar** | তারিখ/সময় |
| **GNATcoll** | GNAT ইউটিলিটিস |
| **AWS** | অ্যাডা ওয়েব সার্ভার |
| **XML/Ada** | XML পার্সিং |
| **GID** | ইমেজ ডিকোডিং |
| **SDLAda** | SDL2 বাইন্ডিং |
| **GLFW** | OpenGL windowing |
| **কর্টেক্স GNAT রানটাইম** | এমবেডেড (ARM) |
---

## সামঞ্জস্য
| বৈশিষ্ট্য | উদ্দেশ্য |
|---------|---------|
| **কাজ** | সমবর্তী থ্রেড |
| **সুরক্ষিত বস্তু** | সিঙ্ক্রোনাইজড ডেটা |
| **বিবৃতি নির্বাচন করুন** | মিলনমেলা |
| **এন্ট্রি কল** | সিঙ্ক্রোনাইজেশন |
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

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **GPS (GNAT প্রোগ্রামিং স্টুডিও)** | AdaCore এর IDE |
| **ভিএস কোড + অ্যাডা** | অ্যাডা ভাষা সমর্থন |
| **Emacs + অ্যাডা-মোড** | ক্লাসিক অ্যাডা পরিবেশ |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **স্ট্যাটিক বাইনারি** | GNAT স্ট্যাটিক বাইনারি তৈরি করে |
| **ক্রস-কম্পাইল** | GNAT ক্রস-সংকলন |
| **এম্বেড করা** | বেয়ার-মেটাল, RTOS (Ravenscar) |
| **ডকার** | কন্টেইনারাইজড |
| **নিরাপত্তা শংসাপত্র** | DO-178C, IEC 61508, সাধারণ মানদণ্ড |
---

## সারাংশ
Ada এর ইকোসিস্টেম নিরাপত্তা-সমালোচনামূলক এবং উচ্চ-নির্ভরযোগ্য সিস্টেমের জন্য উদ্দেশ্য-নির্মিত। স্ট্যান্ডার্ড টুলচেন হল: সংকলনের জন্য **GNAT** (GCC-ভিত্তিক), প্যাকেজ পরিচালনার জন্য **Alire**, বিল্ডের জন্য **GPRbuild**, আনুষ্ঠানিক যাচাইয়ের জন্য **GNATprove** এবং **SPARK** এবং পরীক্ষার জন্য **AUnit**। Ada মহাকাশ মহাকাশে (DO-178C), প্রতিরক্ষা, রেলপথ, চিকিৎসা ডিভাইস এবং যে কোনো ডোমেনে পারদর্শী যেখানে সঠিকতা সর্বাগ্রে। Ada এর শক্তিগুলি হল শক্তিশালী টাইপিং, একযোগে (কাজ, সুরক্ষিত বস্তু), আনুষ্ঠানিক যাচাইকরণ (SPARK), এবং নিরাপত্তা শংসাপত্র। নিরাপত্তা-গুরুত্বপূর্ণ এমবেডেড সিস্টেমের জন্য ইকোসিস্টেম অপরিহার্য।