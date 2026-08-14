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
# MATLAB: Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Prelanzamiento | Década de 1970 | Rutinas matriciales Fortran de Cleve Moler (UNM) |
| 1.0 | 1984 | Primer lanzamiento comercial (MathWorks) |
| 2.0 | 1986 | Operaciones matriciales mejoradas |
| 3.0 | 1987 | Matrices dispersas |
| 4.0 | 1992 | **Simulink** introducido |
| 4.2 | 1993 | Matemática simbólica (integración de Maple) |
| 5.0 | 1996 | **Nuevos tipos de datos**: celdas, estructuras, objetos |
| 5.3 | 1999 |  `help desk`, gráficos mejorados |
| 6.0 | 2000 | **Entorno de escritorio**, mejoras en`gui`|
| 6.5 | 2002 |  Sistema de gráficos`handle`|
| 7.0 | 2004 | **Nuevo escritorio**, analizador de código,`mlint`|
| 7.4 | 2007 |  `timeseries`, trazado mejorado |
| 7.6 | 2008 | Mejoras en POO (clases, herencia) |
| 7.12 | 2011 |  `gpuArray`, Caja de herramientas de computación paralela |
| 8.0 | 2012 | **Live Editor** (cuaderno de publicación) |
| 8.1 | 2013 | **Tabulación**, editor mejorado |
| 8.3 | 2014 |  Matrices`categorical`|
| 8.4 | 2014 |  Matrices`string`(texto) |
| 8.5 | 2015 | **Diseñador de aplicaciones**,`tiledlayout`|
| 9.0 | 2015 | **Tipo `string`** (texto dedicado) |
| 9.1 | 2016 |  Matrices`tall`(grandes datos) |
| 9.4 | 2018 | ** Tipo`dictionary`**, mejoras`tiledlayout`|
| 9.6 | 2019 | Mejoras en **Live Editor**, mejoras en`tall`|
| 9.9 | 2020 | **MATLAB en línea**, GPU`tall`|
| 9.10 | 2021 |  Validación `arguments`,`tiledlayout`|
| 9.12 | 2022 | **Unidad MATLAB**, mejoras en`tall`|
| 9.14 | 2023 | **Asistente AI**, generación de código mejorada |
| 9.15 | 2023 |  Mejoras `tall`, computación paralela |
| 2024a | 2024 | **MATLAB Mobile** mejoras, nuevo trazado |
| 2024b | 2024 | Mayor integración de la IA |
| 2025a | 2025 | Desarrollo continuo |
## Hitos importantes
### Orígenes (décadas de 1970 a 1984)
- **Década de 1970**: Cleve Moler escribe rutinas matriciales Fortran en la Universidad de Nuevo México
- **Objetivo**: Dar a los estudiantes acceso a LINPACK/EISPACK sin escribir Fortran
- **1984**: MathWorks fundado por Moler y Jack Little; MATLAB 1.0 lanzado comercialmente
### MATLAB 4–5: La era Matrix (1992–1999)
- **4.0 (1992)**: Simulink — simulación de diagrama de bloques
- **5.0 (1996)**: matrices de celdas, matrices de estructuras, funciones orientadas a objetos
- **5.3 (1999)**: Caja de herramientas de matemáticas simbólicas (basada en Maple)
### MATLAB 6–7: Entorno moderno (2000–2011)
- **6.0 (2000)**: entorno de escritorio (ventana de comandos, espacio de trabajo, editor)
- **7.0 (2004)**: Nuevo escritorio, analizador de código (`mlint`), gráficos mejorados
- **7.6 (2008)**: POO completa: clases, herencia, paquetes, eventos
### MATLAB 8+: Era de la ciencia de datos (2012-presente)
- **8.0 (2012)**: Live Editor: cuadernos interactivos
- **8.5 (2015)**: App Designer: creador de GUI moderno
- **9.0 (2015)**: tipo`string`(manejo de texto dedicado)
- **9.4 (2018)**: tipo `dictionary`
- **9.14 (2023)**: **Asistente de IA**: consultas en lenguaje natural
- **2024**: MATLAB Mobile, integración en la nube, funciones continuas de IA
## Evolución de la sintaxis
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

## Ecosistema de caja de herramientas
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

## Principios clave de diseño
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## Crecimiento del ecosistema
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
