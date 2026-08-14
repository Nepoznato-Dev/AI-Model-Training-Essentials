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
# Ada - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ ไลบรารี และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศของ Ada
---

## คอมไพเลอร์และการนำไปใช้งาน
| คอมไพเลอร์ | พิมพ์ | หมายเหตุ |
|----------|-|-------|
| **แมลง** | โอเพ่นซอร์ส | | ที่ใช้ GCC และใช้กันอย่างแพร่หลายมากที่สุด
| **ชุมชน GNAT** | ฟรี | รุ่นฟรีของ AdaCore |
| **GNAT Pro** | เชิงพาณิชย์ | ได้รับการรับรองความปลอดภัย AdaCore |
| **ObjectAda** | เชิงพาณิชย์ | Windows สำคัญด้านความปลอดภัย |
| **เจนัส/เอดา** | เชิงพาณิชย์ | ระบบสมองกลฝังตัว |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## สร้างระบบและการจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **อาลีเร่** | ตัวจัดการแพ็คเกจสมัยใหม่ (แนะนำ) |
| **GPRbuild** | เครื่องมือสร้างโครงการ |
| **GPR (โครงการ GNAT)** | รูปแบบไฟล์โครงการ |
| **ทำ** | งานสร้างคลาสสิก |
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

## ความปลอดภัยและการตรวจสอบ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **GNATพิสูจน์** | การตรวจสอบอย่างเป็นทางการ |
| **สปาร์ก** | เซ็ตย่อยที่มีความสำคัญต่อความปลอดภัย |
| **CodePeer** | การวิเคราะห์แบบคงที่ |
| **โพลีสเปซ** | การตรวจสอบรันไทม์ |
| **ความครอบคลุม** | การวิเคราะห์แบบคงที่ |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **หน่วย** | กรอบการทดสอบหน่วย |
| **อาเวน** | การทดสอบอย่างง่าย |
| **GNATtest** | การทดสอบตามรหัส |
| **gprbuild** | สร้างและทดสอบ |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **Ada.Containers** | เวกเตอร์ แผนที่ เซต |
| **เอด้า.สตริงส์** | การจัดการสตริง |
| **Ada.Text_IO** | คอนโซล I/O |
| **อดา.ปฏิทิน** | วันที่/เวลา |
| **GNATcoll** | ยูทิลิตี้ GNAT |
| **AWS** | เว็บเซิร์ฟเวอร์ Ada |
| **XML/เอดา** | การแยกวิเคราะห์ XML |
| **จีไอดี** | การถอดรหัสภาพ |
| **สดลดา** | การเชื่อมโยง SDL2 |
| **GLFW** | หน้าต่าง OpenGL |
| **รันไทม์ Cortex GNAT** | ฝังตัว (ARM) |
---

## เห็นพ้องต้องกัน
| คุณสมบัติ | วัตถุประสงค์ |
|---------|---------|
| **งาน** | กระทู้ที่เกิดขึ้นพร้อมกัน |
| **วัตถุที่ได้รับการคุ้มครอง** | ข้อมูลที่ซิงโครไนซ์ |
| **เลือกข้อความ** | การพบกัน |
| **โทรเข้า** | การซิงโครไนซ์ |
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

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **GPS (GNAT Programming Studio)** | IDE ของ AdaCore |
| **VS Code + เอด้า** | รองรับภาษา Ada |
| **Emacs + โหมด ada** | สภาพแวดล้อม Ada แบบคลาสสิก |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ไบนารีแบบคงที่** | GNAT สร้างไบนารีแบบคงที่ |
| **ข้ามคอมไพล์** | การรวบรวมข้าม GNAT |
| **ฝังตัว** | โลหะเปลือย, RTOS (เรเวนสการ์) |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **ใบรับรองความปลอดภัย** | DO-178C, IEC 61508, เกณฑ์ทั่วไป |
---

## สรุป
ระบบนิเวศของ Ada สร้างขึ้นโดยเฉพาะสำหรับระบบที่มีความสำคัญด้านความปลอดภัยและมีความน่าเชื่อถือสูง Toolchain มาตรฐานคือ: **GNAT** (อิงตาม GCC) สำหรับการคอมไพล์, **Alire** สำหรับการจัดการแพ็คเกจ, **GPRbuild** สำหรับบิลด์, **GNATprove** และ **SPARK** สำหรับการตรวจสอบอย่างเป็นทางการ และ **AUnit** สำหรับการทดสอบ Ada เชี่ยวชาญด้านการบินและอวกาศ (DO-178C) การป้องกัน การรถไฟ อุปกรณ์การแพทย์ และด้านอื่นๆ ที่ความถูกต้องเป็นสิ่งสำคัญยิ่ง จุดแข็งของ Ada คือการพิมพ์ที่แข็งแกร่ง การทำงานพร้อมกัน (งาน วัตถุที่ได้รับการป้องกัน) การตรวจสอบอย่างเป็นทางการ (SPARK) และการรับรองความปลอดภัย ระบบนิเวศเป็นสิ่งจำเป็นสำหรับระบบฝังตัวที่มีความสำคัญด้านความปลอดภัย