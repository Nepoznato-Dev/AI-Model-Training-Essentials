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
# MATLAB — 常見錯誤與反模式
本文檔列出了 MATLAB 中最常見的錯誤、陷阱和反模式，並進行了修正。
---

## 1. 在迴圈中成長數組
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

## 2.`*`與 `.*`（矩陣與元素）
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

## 3. 使用`i`和`j`作為變數
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4. 不懂`find`與邏輯索引
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. 隱藏內建函數
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. 不使用`fprintf`進行輸出
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

＃＃ 概括
MATLAB 以矩陣為中心的設計產生了陷阱：`*`是矩陣乘法（按元素使用`.*`），循環中增長數組的速度很慢（預分配或向量化），`i`/`j`是虛數個單位（不要覆蓋），邏輯數：圖比ZQZQZ（MQZQZ），邏輯數位（不要覆蓋），邏輯數：QZQZQZ（MQZQZ），邏輯數。 MATLAB 的方法是：向量化所有內容、預先分配、使用邏輯索引，並且從不隱藏內建函數。