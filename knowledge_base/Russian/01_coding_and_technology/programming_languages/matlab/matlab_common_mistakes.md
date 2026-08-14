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

# MATLAB — Распространенные ошибки и антишаблоны
В этом документе перечислены наиболее распространенные ошибки, ловушки и антишаблоны в MATLAB с исправлениями.
---

## 1. Увеличение массивов в циклах
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

## 2.`*`против`.*`(матрица или поэлементно)
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

## 3. Использование`i`и`j`в качестве переменных
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4. Непонимание`find`и логического индексирования
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. Затенение встроенных функций
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. Не использовать`fprintf`для вывода
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

## Краткое содержание
Матрично-ориентированный дизайн MATLAB создает ловушки:`*`— умножение матриц (используйте`.*`для поэлементного анализа), рост массивов в циклах происходит медленно (предварительное выделение или векторизация),`i`/`j`— мнимые единицы (не перезаписывать), а логическое индексирование происходит быстрее, чем `find`. Способ MATLAB: векторизовать все, предварительно выделить, использовать логическую индексацию и никогда не дублировать встроенные функции.