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
# MATLAB — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Pra-rilis | 1970-an | Rutinitas matriks Fortran (UNM) Cleve Moler |
| 1.0 | 1984 | Rilis komersial pertama (MathWorks) |
| 2.0 | 1986 | Peningkatan operasi matriks |
| 3.0 | 1987 | Matriks renggang |
| 4.0 | 1992 | **Simulink** diperkenalkan |
| 4.2 | 1993 | Matematika simbolik (integrasi Maple) |
| 5.0 | 1996 | **Tipe data baru**: sel, struct, objek |
| 5.3 | 1999 |  `help desk`, peningkatan grafis |
| 6.0 | 2000 | **Lingkungan desktop**, peningkatan`gui`|
| 6.5 | 2002 |  Sistem grafis`handle`|
| 7.0 | 2004 | **Desktop baru**, penganalisis kode,`mlint`|
| 7.4 | 2007 | `timeseries`, peningkatan plot |
| 7.6 | 2008 | Peningkatan OOP (kelas, warisan) |
| 7.12 | 2011 |  `gpuArray`, Kotak Peralatan Komputasi Paralel |
| 8.0 | 2012 | **Editor Langsung** (terbitkan buku catatan) |
| 8.1 | 2013 | **Penyelesaian tab**, editor yang ditingkatkan |
| 8.3 | 2014 |  Array`categorical`|
| 8.4 | 2014 |  Array`string`(teks) |
| 8.5 | 2015 | **Perancang Aplikasi**,`tiledlayout`|
| 9.0 | 2015 | ** Tipe `string`** (teks khusus) |
| 9.1 | 2016 |  Array`tall`(data besar) |
| 9.4 | 2018 | ** Tipe `dictionary`**, peningkatan`tiledlayout`|
| 9.6 | 2019 | **Peningkatan Editor Langsung**, peningkatan`tall`|
| 9.9 | 2020 | **MATLAB Daring**, GPU`tall`|
| 9.10 | 2021 |  Validasi `arguments`,`tiledlayout`|
| 9.12 | 2022 | **MATLAB Drive**, peningkatan`tall`|
| 9.14 | 2023 | **Asisten AI**, pembuatan kode yang ditingkatkan |
| 9.15 | 2023 |  Peningkatan `tall`, komputasi paralel |
| 2024a | 2024 | **Peningkatan MATLAB Mobile**, plot baru |
| 2024b | 2024 | Integrasi AI lebih lanjut |
| 2025a | 2025 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Asal Usul (1970an–1984)
- **1970an**: Cleve Moler menulis rutinitas matriks Fortran di Universitas New Mexico
- **Sasaran**: Memberi siswa akses ke LINPACK/EISPACK tanpa menulis Fortran
- **1984**: MathWorks didirikan oleh Moler & Jack Little; MATLAB 1.0 dirilis secara komersial
### MATLAB 4–5: Era Matriks (1992–1999)
- **4.0 (1992)**: Simulink — simulasi diagram blok
- **5.0 (1996)**: Array sel, array struct, fitur berorientasi objek
- **5.3 (1999)**: Kotak Peralatan Matematika Simbolik (berbasis Maple)
### MATLAB 6–7: Lingkungan Modern (2000–2011)
- **6.0 (2000)**: Lingkungan desktop (Jendela Perintah, Ruang Kerja, Editor)
- **7.0 (2004)**: Desktop baru, penganalisis kode (`mlint`), grafis yang ditingkatkan
- **7.6 (2008)**: OOP penuh — kelas, warisan, paket, acara
### MATLAB 8+: Era Ilmu Data (2012–sekarang)
- **8.0 (2012)**: Editor Langsung — buku catatan interaktif
- **8.5 (2015)**: Perancang Aplikasi — pembuat GUI modern
- **9.0 (2015)**: Tipe`string`(penanganan teks khusus)
- **9.4 (2018)**: tipe `dictionary`
- **9.14 (2023)**: **Asisten AI** — kueri bahasa alami
- **2024**: MATLAB Mobile, integrasi cloud, fitur AI lanjutan
## Evolusi Sintaks
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

## Ekosistem Kotak Alat
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

## Prinsip Desain Utama
```
1. "Matrix first" — everything is an array (historically)
2. "Interactive" — try things in Command Window
3. "Visualize everything" — powerful plotting
4. "Toolbox model" — domain-specific extensions
5. "Backward compatible" — old .m files keep working
6. "Engineer-friendly" — math notation, not CS notation
```

## Pertumbuhan Ekosistem
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
