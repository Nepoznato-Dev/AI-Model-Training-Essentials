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
# ম্যাটল্যাব — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ MATLAB-তে সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. লুপ-এ ক্রমবর্ধমান অ্যারে
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

## 2.`*`বনাম`.*`(ম্যাট্রিক্স বনাম উপাদান-ভিত্তিক)
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

## 3.`i`এবং`j`ভেরিয়েবল হিসাবে ব্যবহার করা
```matlab
% ❌ WRONG — overwrites imaginary unit
i = 5;
z = 3 + 4*i;  % z = 3 + 20i, not 3 + 4i!

% ✅ CORRECT — use different variable names
idx = 5;
z = 3 + 4i;  % or 3 + 4*1i
```

---

## 4.`find`বনাম লজিক্যাল ইনডেক্সিং বোঝা যাচ্ছে না
```matlab
% ❌ WRONG — using find unnecessarily
indices = find(A > 5);
values = A(indices);

% ✅ CORRECT — logical indexing (faster, cleaner)
values = A(A > 5);
```

---

## 5. শ্যাডোয়িং বিল্ট-ইন ফাংশন
```matlab
% ❌ WRONG — naming variable after built-in
max = 100;   % now max() function is broken!
min = 0;     % now min() function is broken!

% ✅ CORRECT — use different names
maxVal = 100;
minVal = 0;
```

---

## 6. আউটপুটের জন্য`fprintf`ব্যবহার করছেন না
```matlab
% ❌ WRONG — disp with string concatenation
disp(['Result: ' num2str(x)]);

% ✅ CORRECT — fprintf
fprintf('Result: %.4f\n', x);
```

---

## সারাংশ
MATLAB-এর ম্যাট্রিক্স-কেন্দ্রিক নকশা ফাঁদ তৈরি করে:`*`হল ম্যাট্রিক্স গুণন (এলিমেন্ট-ভিত্তিক জন্য`.*`ব্যবহার করুন), লুপগুলিতে ক্রমবর্ধমান অ্যারেগুলি ধীর (প্রি-অ্যালোকেট বা ভেক্টরাইজ),`i`/ `i`/`i` ইউনিট এবং ওভারজেড মার্কিং ইউনিট। লজিক্যাল ইনডেক্সিং`find`এর চেয়ে দ্রুত। MATLAB উপায় হল: সবকিছু ভেক্টরাইজ করুন, প্রাক-বরাদ্দ করুন, লজিক্যাল ইনডেক্সিং ব্যবহার করুন এবং বিল্ট-ইন ফাংশনগুলিকে কখনও ছায়া দেবেন না।