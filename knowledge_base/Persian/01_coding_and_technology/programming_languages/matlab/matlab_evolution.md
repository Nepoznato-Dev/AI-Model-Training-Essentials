---
# Metadata
title: "MATLAB — Version History & Evolution"
description: "Comprehensive version history and evolution of MATLAB from origins to modern MATLAB."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [matlab, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# MATLAB - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| پیش از انتشار | دهه 1970 | روال های ماتریس فرترن Cleve Moler (UNM) |
| 1.0 | 1984 | اولین نسخه تجاری (MathWorks) |
| 2.0 | 1986 | بهبود عملیات ماتریس |
| 3.0 | 1987 | ماتریس های پراکنده |
| 4.0 | 1992 | **Simulink** معرفی شد |
| 4.2 | 1993 | ریاضیات نمادین (ادغام افرا) |
| 5.0 | 1996 | ** انواع داده های جدید **: سلول ها، ساختارها، اشیاء |
| 5.3 | 1999 |  `help desk`، گرافیک بهبود یافته |
| 6.0 | 2000 | **محیط دسکتاپ**، بهبودهای`gui`|
| 6.5 | 2002 |  سیستم گرافیکی`handle`|
| 7.0 | 2004 | **دسکتاپ جدید**، تحلیلگر کد،`mlint`|
| 7.4 | 2007 |  `timeseries`، نمودار بهبود یافته |
| 7.6 | 2008 | پیشرفت های OOP (کلاس ها، وراثت) |
| 7.12 | 2011 | `gpuArray`, جعبه ابزار محاسبات موازی |
| 8.0 | 2012 | **ویرایشگر زنده** (نشر دفترچه یادداشت) |
| 8.1 | 2013 | **تکمیل برگه**، ویرایشگر بهبود یافته |
| 8.3 | 2014 |  آرایه های`categorical`|
| 8.4 | 2014 |  آرایه های`string`(متن) |
| 8.5 | 2015 | **طراح اپلیکیشن**،`tiledlayout`|
| 9.0 | 2015 | ** نوع `string`** (متن اختصاصی) |
| 9.1 | 2016 |  آرایه های`tall`(داده های بزرگ) |
| 9.4 | 2018 | **`dictionary`نوع **، بهبود`tiledlayout`|
| 9.6 | 2019 | **بهبود ویرایشگر زنده**، بهبودهای`tall`|
| 9.9 | 2020 | **متلب آنلاین**، پردازنده گرافیکی`tall`|
| 9.10 | 2021 |  اعتبارسنجی `arguments`،`tiledlayout`|
| 9.12 | 2022 | **درایو متلب**، بهبودهای`tall`|
| 9.14 | 2023 | **دستیار هوش مصنوعی**، تولید کد بهبود یافته |
| 9.15 | 2023 |  بهبودهای `tall`، محاسبات موازی |
| 2024a | 2024 | ** بهبودهای متلب موبایل**، طرح جدید |
| 2024b | 2024 | ادغام بیشتر هوش مصنوعی |
| 2025a | 2025 | توسعه در حال انجام |
## نقاط عطف اصلی
### ریشه ها (1970-1984)
- **دهه 1970**: کلیو مولر روال های ماتریس فرترن را در دانشگاه نیومکزیکو می نویسد
- **هدف**: امکان دسترسی دانش آموزان به LINPACK/EISPACK بدون نوشتن Fortran
- **1984**: MathWorks توسط Moler & Jack Little تأسیس شد. MATLAB 1.0 به صورت تجاری منتشر شد
### MATLAB 4–5: The Matrix Era (1992–1999)
- **4.0 (1992)**: Simulink — شبیه سازی بلوک دیاگرام
- **5.0 (1996)**: آرایه های سلولی، آرایه های ساختاری، ویژگی های شی گرا
- **5.3 (1999)**: جعبه ابزار ریاضی نمادین (مبتنی بر افرا)
### متلب 6–7: محیط مدرن (2000–2011)
- **6.0 (2000)**: محیط دسکتاپ (پنجره فرمان، فضای کاری، ویرایشگر)
- **7.0 (2004)**: دسکتاپ جدید، تحلیلگر کد (`mlint`)، گرافیک بهبود یافته
- **7.6 (2008)**: OOP کامل - کلاس ها، ارث، بسته ها، رویدادها
### MATLAB 8+: عصر علم داده (2012–اکنون)
- **8.0 (2012)**: ویرایشگر زنده - نوت بوک های تعاملی
- **8.5 (2015)**: طراح برنامه - سازنده رابط کاربری گرافیکی مدرن
- **9.0 (2015)**: نوع`string`(دستورالعمل متن اختصاصی)
- **9.4 (2018)**: نوع `dictionary`
- **9.14 (2023)**: **دستیار هوش مصنوعی** — جستارهای زبان طبیعی
- **2024**: MATLAB Mobile، ادغام ابری، ادامه ویژگی های هوش مصنوعی
## تکامل نحو
```matlab
% Early MATLAB: Basic matrix operations
A = [1 2 3; 4 5 6; 7 8 9];
b = [1; 2; 3];
x = A \ b;  % solve Ax = b

% MATLAB 5.0: Cell arrays, structs
C = {1, 'hello', [1 2 3]};
S.name = 'Alice';
S.age = 30;

% MATLAB 7.6: OOP
classdef MyClass < handle
    properties
        Value = 0;
    end
    methods
        function obj = MyClass(v)
            obj.Value = v;
        end
        function display(obj)
            fprintf('Value: %d\n', obj.Value);
        end
    end
end

% MATLAB 8.0: Live Editor (interactive)
% In Live Editor: mix code, output, text, images

% MATLAB 9.0: string type
s = "Hello, World";
names = ["Alice"; "Bob"; "Charlie"];

% MATLAB 9.4: dictionary
d = dictionary(["a","b","c"], [1, 2, 3]);
val = d("b");  % 2

% MATLAB 9.10: arguments validation
function result = myFunc(x, options)
    arguments
        x (1,:) double {mustBePositive}
        options.Method (1,1) string = "fast"
    end
    % ...
end

% MATLAB 2023+: AI Assistant
% Ask: "How do I fit a polynomial to my data?"
% MATLAB generates: polyfit(x, y, degree)
```

## اکوسیستم جعبه ابزار
```
1992: Simulink — block diagram simulation
1995: Signal Processing Toolbox
1997: Control System Toolbox
2000: Image Processing Toolbox
2004: Parallel Computing Toolbox
2008: Statistics and Machine Learning Toolbox
2012: Deep Learning Toolbox
2015: Text Analytics Toolbox
2017: Reinforcement Learning Toolbox
2020: Lidar Toolbox
2023: AI Assistant (natural language)
2025: 100+ toolboxes covering every engineering domain
```

## اصول کلیدی طراحی
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## رشد اکوسیستم
```
1984: MATLAB 1.0 — academic matrix calculator
1992: Simulink — engineering simulation
2000: MATLAB 6.0 — desktop environment
2004: Parallel Computing Toolbox
2012: Live Editor, Deep Learning Toolbox
2015: App Designer, string type
2018: dictionary type, tall arrays
2023: AI Assistant
2025: MATLAB used by 5M+ engineers worldwide
       100+ toolboxes; used in aerospace, automotive, finance, biotech
       Simulink powers: Tesla, Boeing, NASA, Formula 1
```
