---
# Metadata
title: "MATLAB — Version History & Evolution"
description: "Comprehensive version history and evolution of MATLAB from origins to modern MATLAB."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# MATLAB — 버전 기록 및 발전
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 시험판 | 1970년대 | Cleve Moler의 포트란 행렬 루틴(UNM) |
| 1.0 | 1984년 | 최초의 상용 릴리스(MathWorks) |
| 2.0 | 1986 | 향상된 매트릭스 작업 |
| 3.0 | 1987 | 희소 행렬 |
| 4.0 | 1992 | **Simulink** 도입 |
| 4.2 | 1993년 | 기호 수학(메이플 통합) |
| 5.0 | 1996 | **새로운 데이터 유형**: 셀, 구조체, 객체 |
| 5.3 | 1999 |  `help desk`, 향상된 그래픽 |
| 6.0 | 2000 | **데스크톱 환경**,`gui`개선 |
| 6.5 | 2002 | `handle`그래픽 시스템 |
| 7.0 | 2004년 | **새로운 데스크탑**, 코드 분석기,`mlint`|
| 7.4 | 2007년 |  `timeseries`, 향상된 플로팅 |
| 7.6 | 2008 | OOP 개선(클래스, 상속) |
| 7.12 | 2011 |  `gpuArray`, 병렬 컴퓨팅 도구 상자 |
| 8.0 | 2012 | **라이브 편집기**(노트 게시) |
| 8.1 | 2013 | **탭 완성**, 향상된 편집기 |
| 8.3 | 2014 | `categorical`어레이 |
| 8.4 | 2014 | `string`배열(텍스트) |
| 8.5 | 2015 | **앱 디자이너**,`tiledlayout`|
| 9.0 | 2015 | **`string`유형** (전용 텍스트) |
| 9.1 | 2016 | `tall`어레이(빅데이터) |
| 9.4 | 2018 | **`dictionary`유형**,`tiledlayout`개선 |
| 9.6 | 2019 | **라이브 편집기** 개선,`tall`개선 |
| 9.9 | 2020 | **MATLAB 온라인**,`tall`GPU |
| 9.10 | 2021 | `arguments`검증,`tiledlayout`|
| 9.12 | 2022 | **MATLAB 드라이브**,`tall`개선 |
| 9.14 | 2023년 | **AI Assistant**, 향상된 코드 생성 |
| 9.15 | 2023년 | `tall`개선, 병렬 컴퓨팅 |
| 2024a | 2024 | **MATLAB Mobile** 개선, 새로운 플로팅 |
| 2024b | 2024 | 추가 AI 통합 |
| 2025a | 2025 | 지속적인 개발 |
## 주요 이정표
### 기원(1970년대~1984년)
- **1970년대**: Cleve Moler가 뉴멕시코 대학교에서 포트란 행렬 루틴을 작성함
- **목표**: 학생들이 Fortran을 작성하지 않고도 LINPACK/EISPACK에 액세스할 수 있도록 합니다.
- **1984**: Moler와 Jack Little이 MathWorks를 설립했습니다. MATLAB 1.0이 상업적으로 출시됨
### MATLAB 4–5: 매트릭스 시대(1992–1999)
- **4.0(1992)**: Simulink — 블록 다이어그램 시뮬레이션
- **5.0(1996)**: 셀 배열, 구조체 배열, 객체 지향 기능
- **5.3(1999)**: Symbolic Math Toolbox(Maple 기반)
### MATLAB 6–7: 현대 환경(2000–2011)
- **6.0(2000)**: 데스크탑 환경(명령창, 작업공간, 편집기)
- **7.0(2004)**: 새로운 데스크톱, 코드 분석기(`mlint`), 향상된 그래픽
- **7.6 (2008)**: 전체 OOP — 클래스, 상속, 패키지, 이벤트
### MATLAB 8+: 데이터 과학 시대(2012~현재)
- **8.0(2012)**: 라이브 편집기 — 대화형 노트북
- **8.5(2015)**: 앱 디자이너 — 최신 GUI 빌더
- **9.0 (2015)**:`string`유형 (전용 텍스트 처리)
- **9.4(2018)**:`dictionary`유형
- **9.14(2023)**: **AI Assistant** — 자연어 쿼리
- **2024**: MATLAB Mobile, 클라우드 통합, 지속적인 AI 기능
## 구문 진화
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

## 툴박스 생태계
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

## 주요 디자인 원칙
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## 생태계 성장
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
