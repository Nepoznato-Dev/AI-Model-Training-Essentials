---
# Metadata
title: "MATLAB — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in MATLAB with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [matlab, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# MATLAB - ข้อผิดพลาดทั่วไปและการต่อต้านรูปแบบ
เอกสารนี้รวบรวมข้อผิดพลาด กับดัก และรูปแบบการต่อต้านที่พบบ่อยที่สุดใน MATLAB พร้อมการแก้ไข
---

## 1. การเพิ่มอาร์เรย์ในลูป
```matlab
% ❌ WRONG — O(n²) reallocation
result = [];
for i = 1:10000
    result(end+1) = i^2;
end

% ✅ CORRECT — pre-allocate
result = zeros(1, 10000);
for i = 1:10000
    result(i) = i^2;
end

% ✅ BEST — vectorize
result = (1:10000).^2;
```

---

## 2.`*`กับ`.*`(เมทริกซ์เทียบกับองค์ประกอบที่ชาญฉลาด)
```matlab
% ❌ WRONG — matrix multiplication when element-wise intended
A = [1 2; 3 4];
B = [5 6; 7 8];
C = A * B;   % matrix product, not [5 12; 21 32]

% ✅ CORRECT — element-wise operations
C = A .* B;  % [5 12; 21 32]
C = A .^ 2;  % element-wise power
C = A ./ B;  % element-wise division
```

---

## 3. การใช้`i`และ`j`เป็นตัวแปร
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4. ไม่เข้าใจ`find`เทียบกับการทำดัชนีแบบลอจิคัล
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. การแชโดว์ฟังก์ชันในตัว
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. ไม่ได้ใช้`fprintf`สำหรับเอาต์พุต
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

## สรุป
การออกแบบที่เน้นเมทริกซ์เป็นศูนย์กลางของ MATLAB สร้างกับดัก:`*`เป็นการคูณเมทริกซ์ (ใช้`.*`สำหรับองค์ประกอบที่ชาญฉลาด) การเพิ่มอาร์เรย์ในลูปนั้นช้า (จัดสรรล่วงหน้าหรือเวคเตอร์)`i`/`j`เป็นหน่วยจินตภาพ (อย่าเขียนทับ) และการจัดทำดัชนีเชิงตรรกะเร็วกว่า`find`วิธีของ MATLAB คือ: กำหนดเวกเตอร์ทุกอย่าง จัดสรรล่วงหน้า ใช้การจัดทำดัชนีแบบลอจิคัล และไม่ใช้เงาฟังก์ชันในตัว