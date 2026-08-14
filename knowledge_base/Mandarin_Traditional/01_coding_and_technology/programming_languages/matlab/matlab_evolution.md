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
# MATLAB — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|預發布 | 20 世紀 70 年代 | Cleve Moler 的 Fortran 矩陣例程 (UNM) |
| 1.0 | 1984 |第一個商業版本 (MathWorks) |
| 2.0 | 1986 |改良的矩陣運算 |
| 3.0 | 1987 |稀疏矩陣|
| 4.0 | 1992 | **Simulink** 介紹 |
| 4.2 | 1993 |符號數學（Maple 積分）|
| 5.0 | 1996 | **新資料型別**：儲存格、結構、物件 |
| 5.3 | 1999 | `help desk`，改進的圖形|
| 6.0 | 2000 | 2000 **桌面環境**，`gui` 改進 |
| 6.5 | 6.5 2002 | `handle`圖形系統|
| 7.0 | 2004 | **新桌面**，程式碼分析器，`mlint` |
| 7.4 | 7.4 2007 | `timeseries`，改進繪圖 |
| 7.6 | 7.6 2008 | OOP 改進（類別、繼承）|
| 7.12 | 7.12 2011 | `gpuArray`，平行計算工具箱|
| 8.0 | 2012 | **即時編輯器**（發佈筆記本）|
| 8.1 | 2013 | **製表符補全**，改進的編輯器 |
| 8.3 | 2014年|`categorical`陣列 |
| 8.4 | 2014年|`string`陣列（文字）|
| 8.5 | 2015 | 2015 **應用程式設計師**，`tiledlayout` |
| 9.0 | 2015 | 2015 **`string`型**（專用文字）|
| 9.1 | 2016 | 2016`tall`陣列（大數據）|
| 9.4 | 9.4 2018 | **`dictionary`型**、`tiledlayout` 改進 |
| 9.6 | 2019 | 2019 **即時編輯器** 改進、`tall` 改進 |
| 9.9 | 9.9 2020 | **MATLAB Online**，`tall` GPU |
| 9.10 | 2021 |`arguments`驗證、`tiledlayout` |
| 9.12 | 2022 | 2022 **MATLAB Drive**、`tall` 改進 |
| 9.14 | 9.14 2023 | **AI Assistant**，改進的程式碼產生 |
| 9.15 | 9.15 2023 |`tall`改進，並行計算 |
| 2024a | 2024a 2024 | 2024 **MATLAB Mobile** 改進，新繪圖 |
| 2024b | 2024b 2024 | 2024進一步人工智慧融合 |
| 2025a | 2025 | 2025持續發展|
## 主要里程碑
### 起源（1970 年代–1984 年）
- **1970 年代**：Cleve Moler 在新墨西哥大學編寫 Fortran 矩陣例程
- **目標**：讓學生無需編寫 Fortran 即可存取 LINPACK/EISPACK
- **1984**：MathWorks 由 Moler 和 Jack Little 創立； MATLAB 1.0 商業發布
### MATLAB 4–5：矩陣時代 (1992–1999)
- **4.0 (1992)**：Simulink — 框圖仿真
- **5.0 (1996)**：元胞數組、結構數組、物件導向的功能
- **5.3 (1999)**：符號數學工具箱（基於 Maple）
### MATLAB 6–7：現代環境（2000–2011）
- **6.0 (2000)**：桌面環境（命令列視窗、工作區、編輯器）
- **7.0 (2004)**：新桌面、程式碼分析器 (`mlint`)、改進的圖形
- **7.6 (2008)**：完整的 OOP — 類別、繼承、套件、事件
### MATLAB 8+：資料科學時代（2012 年至今）
- **8.0 (2012)**：即時編輯器 — 互動筆記本
- **8.5 (2015)**：App Designer — 現代 GUI 建構器
- **9.0 (2015)**：`string` 類型（專用文字處理）
- **9.4 (2018)**：`dictionary` 類型
- **9.14 (2023)**：**AI 助理** — 自然語言查詢
- **2024**：MATLAB Mobile、雲端整合、持續的 AI 功能
## 語法演變
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

## 工具箱生態系統
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

## 關鍵設計原則
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## 生態系成長
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
