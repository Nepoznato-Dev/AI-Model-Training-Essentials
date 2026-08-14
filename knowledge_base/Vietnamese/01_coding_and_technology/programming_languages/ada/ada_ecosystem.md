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
# Ada — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, thư viện và cơ sở hạ tầng thiết yếu trong hệ sinh thái Ada.
---

## Trình biên dịch và triển khai
| Trình biên dịch | Loại | Ghi chú |
|----------|------|-------|
| **GNAT** | Mã nguồn mở | Dựa trên GCC, được sử dụng rộng rãi nhất |
| **Cộng đồng GNAT** | Miễn phí | Phiên bản miễn phí của AdaCore |
| **GNAT Pro** | Thương mại | Đã xác nhận an toàn, AdaCore |
| **ObjectAda** | Thương mại | Windows, yêu cầu an toàn cao |
| **Janus/Ada** | Thương mại | Hệ thống nhúng |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Quản lý hệ thống & gói xây dựng
| Công cụ | Mục đích |
|------|----------|
| **Alire** | Trình quản lý gói hiện đại (được khuyến nghị) |
| **GPRbuild** | Công cụ xây dựng dự án |
| **GPR (Dự án GNAT)** | Định dạng tệp dự án |
| **Thực hiện** | Bản dựng cổ điển |
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

## An toàn & Xác minh
| Công cụ | Mục đích |
|------|----------|
| **GNATchứng minh** | Xác minh chính thức |
| **TIA lửa** | Tập hợp con quan trọng về an toàn |
| **CodePeer** | Phân tích tĩnh |
| **Đa giác** | Xác minh thời gian chạy |
| **Độ che phủ** | Phân tích tĩnh |
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

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **Đơn vị** | Khung kiểm tra đơn vị |
| **Àhven** | Kiểm tra đơn giản |
| **Kiểm tra GNAT** | Kiểm tra dựa trên mã |
| **gprbuild** | Xây dựng và thử nghiệm |
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

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **Ada.Container** | Vectơ, bản đồ, bộ |
| **Ada.Chuỗi** | Xử lý chuỗi |
| **Ada.Text_IO** | Bảng điều khiển I/O |
| **Ada.Lịch** | Ngày/giờ |
| **GNATcoll** | Tiện ích GNAT |
| **AWS** | Máy chủ Web Ada |
| **XML/Ada** | Phân tích cú pháp XML |
| **GID** | Giải mã hình ảnh |
| **SDLada** | Ràng buộc SDL2 |
| **GLFW** | Cửa sổ OpenGL |
| **Thời gian chạy Cortex GNAT** | Nhúng (ARM) |
---

## Đồng thời
| Tính năng | Mục đích |
|----------|----------|
| **Nhiệm vụ** | Chủ đề đồng thời |
| **Đối tượng được bảo vệ** | Dữ liệu được đồng bộ hóa |
| **Chọn câu** | Cuộc hẹn |
| **Cuộc gọi đầu vào** | Đồng bộ hóa |
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

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **GPS (Studio lập trình GNAT)** | IDE của AdaCore |
| **Mã VS + Ada** | Hỗ trợ ngôn ngữ Ada |
| **Emacs + chế độ ada** | Môi trường Ada cổ điển |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Nhị phân tĩnh** | GNAT tạo nhị phân tĩnh |
| **Biên dịch chéo** | Biên dịch chéo GNAT |
| **Đã nhúng** | Kim loại trần, RTOS (Ravenscar) |
| **Docker** | Được đóng gói |
| **Chứng nhận an toàn** | DO-178C, IEC 61508, Tiêu chí chung |
---

## Bản tóm tắt
Hệ sinh thái của Ada được xây dựng có mục đích dành cho các hệ thống có độ tin cậy cao và quan trọng về an toàn. Chuỗi công cụ tiêu chuẩn là: **GNAT** (dựa trên GCC) để biên dịch, **Alire** để quản lý gói, **GPRbuild** cho các bản dựng, **GNATprove** và **SPARK** để xác minh chính thức và **AUnit** để thử nghiệm. Ada vượt trội trong lĩnh vực hàng không vũ trụ (DO-178C), quốc phòng, đường sắt, thiết bị y tế và bất kỳ lĩnh vực nào mà tính chính xác là tối quan trọng. Điểm mạnh của Ada là khả năng gõ mạnh, tính đồng thời (nhiệm vụ, đối tượng được bảo vệ), xác minh chính thức (SPARK) và chứng nhận an toàn. Hệ sinh thái rất cần thiết cho các hệ thống nhúng quan trọng về an toàn.