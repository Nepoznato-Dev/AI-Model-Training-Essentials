---
# Metadata
title: "Ada — Syntax Reference"
description: "Detailed syntax reference for Ada covering tasking, protected objects, generics, contracts, and safety-critical programming patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [ada, syntax-reference, tasking, protected-objects, generics, contracts, safety-critical, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Ada — Tham khảo cú pháp
Tài liệu này cung cấp tài liệu tham khảo cú pháp có cấu trúc, toàn diện cho Ada (2012/2022). Nó bổ sung cho tham chiếu Ada chính bằng cách tập trung vào các mẫu cú pháp đầy đủ, tác vụ, đối tượng được bảo vệ, khái quát và lập trình quan trọng về an toàn.
---

## Toán tử & Biểu thức
| Nhà điều hành | Tên | Ví dụ | Ghi chú |
|----------|------|----------|-------|
| `+``-``*``/``**`| Số học | `A ** 2`| |
| `mod``rem` | Mô-đun/phần còn lại | `A mod B`| `mod`luôn tích cực |
| `&`| Nối | `"hello" & " world"`| |
| `=``/=` | Bình đẳng | `A = B`| |
| `<``>``<=``>=` | So sánh | `A >= B`| |
| `and``or``not``xor` | Hợp lý | `A and B`| |
| `and then``or else` | Đoản mạch | `A and then B`| |
| `in``not in` | Thành viên phạm vi | `X in 1 .. 10`| |
| `:=`| Bài tập | `X := 10`| |
---

## Loại & loại phụ
```ada
-- Scalar types
type Temperature is range -273 .. 5000;
type Byte is mod 256;
type Color is (Red, Green, Blue);

-- Subtypes (constrained views)
subtype Percentage is Integer range 0 .. 100;
subtype Port_Number is Integer range 0 .. 65535;

-- Records
type Point is record
   X : Float;
   Y : Float;
end record;

-- Tagged types (OOP)
type Shape is tagged record
   Name : String(1 .. 20);
end record;

type Circle is new Shape with record
   Radius : Float;
end record;

-- Access types (pointers)
type Node_Ptr is access all Node;
type Node is record
   Value : Integer;
   Next  : Node_Ptr;
end record;
```

---

## Luồng điều khiển
```ada
-- if / elsif / else
if X > 0 then
   Put("positive");
elsif X < 0 then
   Put("negative");
else
   Put("zero");
end if;

-- case (exhaustive)
case Light is
   when Red    => Put("Stop");
   when Yellow => Put("Caution");
   when Green  => Put("Go");
end case;

-- for loop
for I in 1 .. 10 loop
   Put_Line(Integer'Image(I));
end loop;

-- for with reverse
for I in reverse 1 .. 10 loop
   Put_Line(Integer'Image(I));
end loop;

-- while loop
while not Done loop
   Process;
end loop;

-- loop (infinite with exit)
loop
   exit when Condition;
   Do_Something;
end loop;
```

---

## Đối tượng và nhiệm vụ được bảo vệ
```ada
-- Protected object (safe shared state)
protected type Buffer is
   entry Put(Item : Integer);
   entry Get(Item : out Integer);
   function Count return Natural;
private
   Data : array(1 .. 100) of Integer;
   Head, Tail : Positive := 1;
   Size : Natural := 0;
end Buffer;

protected body Buffer is
   entry Put(Item : Integer) when Size < Data'Length is
   begin
      Data(Tail) := Item;
      Tail := (Tail mod Data'Length) + 1;
      Size := Size + 1;
   end Put;

   entry Get(Item : out Integer) when Size > 0 is
   begin
      Item := Data(Head);
      Head := (Head mod Data'Length) + 1;
      Size := Size - 1;
   end Get;

   function Count return Natural is (Size);
end Buffer;

-- Task type
task type Worker is
   entry Start(Job : Integer);
end Worker;

task body Worker is
   My_Job : Integer;
begin
   accept Start(Job : Integer) do
      My_Job := Job;
   end Start;
   -- Process job...
end Worker;
```

---

## Hợp đồng & Xác minh
```ada
-- Pre/postconditions
function Sqrt(X : Float) return Float
   with Pre  => X >= 0.0,
        Post => Sqrt'Result >= 0.0;

-- Type invariants
type Bounded_Int is new Integer
   with Type_Invariant => Bounded_Int in 0 .. 100;

-- Loop invariants
while Condition loop
   -- Loop_Invariant => ...
   pragma Loop_Invariant (X >= 0);
   Process;
end loop;
```

---

## Bản tóm tắt
Cú pháp của Ada dài dòng nhưng chính xác. Mỗi công trình được thiết kế cho sự rõ ràng và an toàn. Các đối tượng được bảo vệ loại bỏ các cuộc đua dữ liệu ở cấp độ ngôn ngữ. Hợp đồng (điều kiện trước/sau, điều kiện bất biến) làm cho các yêu cầu về tính đúng đắn trở nên rõ ràng và có thể kiểm tra được. Generics cung cấp khả năng tái sử dụng an toàn theo kiểu. Đối với các hệ thống quan trọng về an toàn, cú pháp của Ada không phải là gánh nặng — đó là sự đảm bảo rằng mã sẽ thực hiện những gì nó yêu cầu.