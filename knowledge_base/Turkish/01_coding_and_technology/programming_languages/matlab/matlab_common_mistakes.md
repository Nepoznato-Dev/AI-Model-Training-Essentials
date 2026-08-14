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
# MATLAB — Yaygın Hatalar ve Anti-Kalıplar
Bu belge, MATLAB'daki en yaygın hataları, tuzakları ve anti-örüntüleri düzeltmelerle birlikte kataloglamaktadır.
---

## 1. Dizileri Döngüler Halinde Büyütmek
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

## 2.`*`ve`.*`(Matris ve Element bazında)
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

## 3.`i`ve `j`'yi Değişken Olarak Kullanmak
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4.`find`ve Mantıksal İndekslemeyi Anlamamak
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. Yerleşik Gölgelendirme İşlevleri
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. Çıkış için`fprintf`Kullanılmaması
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

## Özet
MATLAB'ın matris merkezli tasarımı tuzaklar yaratır:`*`matris çarpımıdır (öğe bazında`.*`kullanın), döngülerde dizilerin büyütülmesi yavaştır (önceden tahsis veya vektörleştirme),`i`/`j`hayali birimlerdir (üzerine yazmayın) ve mantıksal indeksleme `find`'den daha hızlıdır. MATLAB yöntemi şudur: her şeyi vektörize edin, önceden tahsis edin, mantıksal indekslemeyi kullanın ve yerleşik işlevleri asla gölgelemeyin.