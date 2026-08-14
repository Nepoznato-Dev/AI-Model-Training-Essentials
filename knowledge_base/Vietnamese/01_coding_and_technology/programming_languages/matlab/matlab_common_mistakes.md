---
# Metadata
title: "MATLAB — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in MATLAB with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# MATLAB — Những lỗi thường gặp và các mẫu phản đối
Tài liệu này liệt kê các lỗi, bẫy và phản mẫu phổ biến nhất trong MATLAB kèm theo các chỉnh sửa.
---

## 1. Phát triển mảng trong vòng lặp
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

## 2.`*`vs`.*`(Ma trận so với phần tử)
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

## 3. Sử dụng`i`và`j`làm Biến
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4. Không hiểu`find`vs Lập chỉ mục logic
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. Chức năng tạo bóng tích hợp
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. Không sử dụng`fprintf`cho đầu ra
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

## Bản tóm tắt
Thiết kế lấy ma trận làm trung tâm của MATLAB tạo ra các bẫy:`*`là phép nhân ma trận (sử dụng`.*`cho phần tử), việc phát triển mảng trong các vòng lặp chậm (phân bổ trước hoặc vector hóa),`i`/`j`là các đơn vị tưởng tượng (không ghi đè) và lập chỉ mục logic nhanh hơn`find`. Cách MATLAB là: vector hóa mọi thứ, phân bổ trước, sử dụng lập chỉ mục logic và không bao giờ che giấu các hàm dựng sẵn.