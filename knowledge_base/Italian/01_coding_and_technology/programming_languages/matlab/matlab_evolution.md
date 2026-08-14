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

# MATLAB: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Pre-release | Anni '70 | Routine della matrice Fortran di Cleve Moler (UNM) |
| 1.0 | 1984 | Prima versione commerciale (MathWorks) |
| 2.0 | 1986 | Operazioni sulle matrici migliorate |
| 3.0 | 1987 | Matrici sparse |
| 4.0 | 1992 | **Simulink** introdotto |
| 4.2 | 1993 | Matematica simbolica (integrazione con Maple) |
| 5.0 | 1996 | **Nuovi tipi di dati**: celle, strutture, oggetti |
| 5.3 | 1999 | `help desk`, grafica migliorata |
| 6.0 | 2000 | **Ambiente desktop**, miglioramenti`gui`|
| 6.5| 2002|  Sistema grafico`handle`|
| 7.0| 2004| **Nuovo desktop**, analizzatore di codice,`mlint`|
| 7.4| 2007| `timeseries`, disegno migliorato |
| 7.6| 2008| Miglioramenti OOP (classi, ereditarietà) |
| 7.12 | 2011 | `gpuArray`, Casella degli strumenti per il calcolo parallelo |
| 8.0 | 2012| **Live Editor** (pubblica taccuino) |
| 8.1 | 2013| **Completamento con tab**, editor migliorato |
| 8.3 | 2014|  Matrici`categorical`|
| 8.4| 2014| `string`matrici (testo) |
| 8,5 | 2015| **Progettista app**,`tiledlayout`|
| 9.0 | 2015| **Tipo `string`** (testo dedicato) |
| 9.1 | 2016|  Array`tall`(big data) |
| 9.4| 2018 | ** Tipo `dictionary`**, miglioramenti`tiledlayout`|
| 9.6| 2019 | Miglioramenti al **Live Editor**, miglioramenti a`tall`|
| 9.9 | 2020 | **MATLAB online**, GPU`tall`|
| 9.10| 2021 |  Convalida `arguments`,`tiledlayout`|
| 9.12| 2022 | **MATLAB Drive**, miglioramenti`tall`|
| 9.14| 2023 | **Assistente AI**, generazione di codice migliorata |
| 9.15| 2023 |  Miglioramenti `tall`, calcolo parallelo |
| 2024a | 2024 | **MATLAB Mobile** miglioramenti, nuovi grafici |
| 2024b | 2024 | Ulteriore integrazione dell'intelligenza artificiale |
| 2025a | 2025 | Sviluppo continuo |
## Traguardi importanti
### Origini (anni '70-1984)
- **anni '70**: Cleve Moler scrive routine di matrice Fortran all'Università del New Mexico
- **Obiettivo**: fornire agli studenti l'accesso a LINPACK/EISPACK senza scrivere Fortran
- **1984**: MathWorks fondata da Moler e Jack Little; MATLAB 1.0 rilasciato in commercio
### MATLAB 4–5: L'era di Matrix (1992–1999)
- **4.0 (1992)**: Simulink — simulazione del diagramma a blocchi
- **5.0 (1996)**: array di celle, array di strutture, funzionalità orientate agli oggetti
- **5.3 (1999)**: Symbolic Math Toolbox (basato su Maple)
### MATLAB 6–7: Ambiente moderno (2000–2011)
- **6.0 (2000)**: ambiente desktop (finestra di comando, area di lavoro, editor)
- **7.0 (2004)**: nuovo desktop, analizzatore di codice (`mlint`), grafica migliorata
- **7.6 (2008)**: OOP completo: classi, ereditarietà, pacchetti, eventi
### MATLAB 8+: Data Science Era (2012-oggi)
- **8.0 (2012)**: Live Editor: quaderni interattivi
- **8.5 (2015)**: App Designer: moderno generatore di GUI
- **9.0 (2015)**: tipo`string`(gestione del testo dedicata)
- **9.4 (2018)**: tipo `dictionary`
- **9.14 (2023)**: **Assistente AI**: query in linguaggio naturale
- **2024**: MATLAB Mobile, integrazione cloud, funzionalità AI continue
## Evoluzione della sintassi
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

## Ecosistema della cassetta degli attrezzi
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

## Principi chiave di progettazione
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## Crescita dell'ecosistema
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
