<!--
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

-->
# MATLAB - عام غلطیاں اور مخالف پیٹرن
یہ دستاویز MATLAB میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کو تصحیح کے ساتھ کیٹلاگ کرتا ہے۔
---

## 1. لوپس میں بڑھتی ہوئی صفیں۔
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

## 2.`*`بمقابلہ`.*`(میٹرکس بمقابلہ عنصر کے لحاظ سے)
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

## 3.`i`اور`j`کو بطور متغیر استعمال کرنا
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4.`find`بمقابلہ منطقی انڈیکسنگ کو نہ سمجھنا
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. شیڈونگ بلٹ ان فنکشنز
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. آؤٹ پٹ کے لیے`fprintf`استعمال نہیں کرنا
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

## خلاصہ
MATLAB کا میٹرکس-سینٹرک ڈیزائن ٹریپس بناتا ہے:`*`میٹرکس ضرب ہے (عنصر کے لحاظ سے`.*`استعمال کریں)، لوپس میں بڑھتی ہوئی صفیں سست ہیں (پہلے سے مختص یا ویکٹرائز کریں)،`i`/`i`/`i`یونٹ (اوور زیڈ ایم اے) منطقی اشاریہ سازی`find`سے تیز ہے۔ MATLAB طریقہ یہ ہے: ہر چیز کو ویکٹرائز کریں، پہلے سے مختص کریں، منطقی اشاریہ سازی کا استعمال کریں، اور بلٹ ان فنکشنز کو کبھی سایہ نہ کریں۔