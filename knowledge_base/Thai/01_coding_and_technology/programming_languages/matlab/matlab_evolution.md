<!--
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

-->
# MATLAB - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| ก่อนเผยแพร่ | ทศวรรษ 1970 | รูทีนเมทริกซ์ Fortran (UNM) ของ Cleve Moler
| 1.0 | 1984 | การเปิดตัวเชิงพาณิชย์ครั้งแรก (MathWorks) |
| 2.0 | 1986 | ปรับปรุงการดำเนินงานเมทริกซ์ |
| 3.0 | 1987 | เมทริกซ์กระจัดกระจาย |
| 4.0 | 1992 | **Simulink** แนะนำ |
| 4.2 | 1993 | คณิตศาสตร์เชิงสัญลักษณ์ (อินทิเกรตเมเปิ้ล) |
| 5.0 | 1996 | **ประเภทข้อมูลใหม่**: เซลล์ โครงสร้าง วัตถุ |
| 5.3 | 1999 | `help desk`กราฟิกที่ได้รับการปรับปรุง |
| 6.0 | 2000 | **สภาพแวดล้อมเดสก์ท็อป** การปรับปรุง`gui`|
| 6.5 | 2545 | `handle`ระบบกราฟิก |
| 7.0 | 2547 | **เดสก์ท็อปใหม่** ตัววิเคราะห์โค้ด`mlint`|
| 7.4 | 2550 | `timeseries`ปรับปรุงการลงจุด |
| 7.6 | 2551 | การปรับปรุง OOP (คลาส, การสืบทอด) |
| 7.12 | 2554 | `gpuArray`, กล่องเครื่องมือคอมพิวเตอร์แบบขนาน |
| 8.0 | 2555 | **Live Editor** (เผยแพร่สมุดบันทึก) |
| 8.1 | 2013 | **แท็บเสร็จสิ้น** ปรับปรุงตัวแก้ไข |
| 8.3 | 2014 |  อาร์เรย์`categorical`|
| 8.4 | 2014 |  อาร์เรย์`string`(ข้อความ) |
| 8.5 | 2558 | **ผู้ออกแบบแอป**,`tiledlayout`|
| 9.0 | 2558 | ** ประเภท `string`** (ข้อความเฉพาะ) |
| 9.1 | 2559 |  อาร์เรย์`tall`(ข้อมูลขนาดใหญ่) |
| 9.4 | 2018 | ** ประเภท `dictionary`** การปรับปรุง`tiledlayout`|
| 9.6 | 2019 | **การปรับปรุง Live Editor**, การปรับปรุง`tall`|
| 9.9 | 2020 | **MATLAB ออนไลน์**,`tall`GPU |
| 9.10 | 2021 |  การตรวจสอบ `arguments`,`tiledlayout`|
| 9.12 | 2022 | **ไดรฟ์ MATLAB** การปรับปรุง`tall`|
| 9.14 | 2023 | **ผู้ช่วย AI** ปรับปรุงการสร้างโค้ด |
| 9.15 | 2023 |  การปรับปรุง `tall`, การประมวลผลแบบขนาน |
| 2024ก | 2024 | การปรับปรุง **MATLAB Mobile** การวางแผนใหม่ |
| 2024b | 2024 | การบูรณาการ AI เพิ่มเติม |
| 2025ก | 2025 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### ออริจินส์ (ค.ศ. 1970–1984)
- **ทศวรรษ 1970**: Cleve Moler เขียนรูทีนเมทริกซ์ Fortran ที่มหาวิทยาลัยนิวเม็กซิโก
- **เป้าหมาย**: ให้นักเรียนเข้าถึง LINPACK/EISPACK โดยไม่ต้องเขียน Fortran
- **1984**: MathWorks ก่อตั้งโดย Moler & Jack Little; MATLAB 1.0 เปิดตัวในเชิงพาณิชย์
### MATLAB 4–5: ยุคเมทริกซ์ (1992–1999)
- **4.0 (1992)**: Simulink — การจำลองบล็อกไดอะแกรม
- **5.0 (1996)**: อาร์เรย์ของเซลล์, อาร์เรย์โครงสร้าง, คุณลักษณะเชิงวัตถุ
- **5.3 (1999)**: กล่องเครื่องมือทางคณิตศาสตร์เชิงสัญลักษณ์ (แบบ Maple)
### MATLAB 6–7: สภาพแวดล้อมสมัยใหม่ (2000–2011)
- **6.0 (2000)**: สภาพแวดล้อมเดสก์ท็อป (หน้าต่างคำสั่ง พื้นที่ทำงาน ตัวแก้ไข)
- **7.0 (2004)**: เดสก์ท็อปใหม่ ตัววิเคราะห์โค้ด (`mlint`) กราฟิกที่ได้รับการปรับปรุง
- **7.6 (2008)**: OOP แบบเต็ม — คลาส, การสืบทอด, แพ็คเกจ, กิจกรรม
### MATLAB 8+: ยุควิทยาศาสตร์ข้อมูล (2012–ปัจจุบัน)
- **8.0 (2012)**: Live Editor — สมุดบันทึกแบบโต้ตอบ
- **8.5 (2015)**: App Designer — ตัวสร้าง GUI ที่ทันสมัย
- **9.0 (2015)**: ประเภท`string`(การจัดการข้อความเฉพาะ)
- **9.4 (2018)**: ประเภท `dictionary`
- **9.14 (2023)**: **ผู้ช่วย AI** — คำสั่งในภาษาธรรมชาติ
- **2024**: MATLAB Mobile, การบูรณาการระบบคลาวด์, คุณสมบัติ AI อย่างต่อเนื่อง
## วิวัฒนาการไวยากรณ์
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

## ระบบนิเวศกล่องเครื่องมือ
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

## หลักการออกแบบที่สำคัญ
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## การเติบโตของระบบนิเวศ
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
