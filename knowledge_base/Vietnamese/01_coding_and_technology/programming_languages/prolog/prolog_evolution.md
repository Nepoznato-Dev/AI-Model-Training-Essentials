---
# Metadata
title: "Prolog — Version History & Evolution"
description: "Comprehensive version history and evolution of Prolog from origins to modern Prolog."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [prolog, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Prolog — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Tiền Prolog | 1965–70 | Hệ thống Q của Colmerauer, xử lý ngôn ngữ tự nhiên |
| Prolog tôi | 1972 | **Prolog đầu tiên** (Alain Colmerauer, Marseille) |
| 10/12 | 1977 | Edinburgh Prolog của David Warren (trình biên dịch hiệu quả) |
| Prolog ISO | 1995 | **Tiêu chuẩn ISO đầu tiên** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — Prolog mã nguồn mở phổ biến nhất |
| GNU Prolog | 1999 | Daniel Diaz — tổng hợp bản địa |
| ISO thứ 2 | 2012 | Corrigendum 2 (sửa lỗi, làm rõ) |
| SWI 8.x | 2018 | Lập bảng, hợp lý, cải thiện hiệu suất |
| SWI 9.x | 2023 | ** Lập bảng** (mặc định), mô-đun cải tiến, hệ thống đóng gói |
| Máy quét | 2018 | Prolog hiện đại trong Rust — Tương thích ISO |
| Trealla | 2022 | Prolog nhanh trong C — triển khai hiện đại |
## Các cột mốc quan trọng
### Sự ra đời của Prolog (1972)
- **1972**: Alain Colmerauer tạo Prolog tại Đại học Marseille
- **Tên**: "PROgrammation en LOGique" (lập trình logic)
- **Mục tiêu**: Xử lý ngôn ngữ tự nhiên — phân tích các câu tiếng Pháp
- Dựa trên các điều khoản và nghị quyết Horn (Robinson, 1965)
- Thực hiện lần đầu: thống nhất + quay lui
### Edinburgh Prolog (1977)
- **1977**: David Warren tạo ra Prolog DEC-10 tại Edinburgh
- Trình biên dịch hiệu quả — Prolog trở nên thiết thực
- Edinburgh Prolog trở thành triển khai tham khảo
- Ảnh hưởng: Mệnh đề Horn, tìm kiếm theo chiều sâu, toán tử cắt
### Tiêu chuẩn hóa ISO (1995)
- **1995**: Tiêu chuẩn ISO đầu tiên (ISO/IEC 13211-1)
- Định nghĩa: cú pháp, vị từ cài sẵn, số học, I/O
- Đảm bảo tính di động trong quá trình triển khai
### Prolog hiện đại (thập niên 2000–nay)
- **SWI-Prolog**: Được sử dụng rộng rãi nhất — lập bảng, mô-đun, đa luồng, web (Pengines)
- **GNU Prolog**: Biên dịch gốc — thực thi nhanh
- **Scryer Prolog**: Hiện đại, dựa trên Rust, tương thích ISO
- **Tralla Prolog**: Nhanh, nhẹ, dựa trên C
## Tiến hóa cú pháp
```prolog
% Early Prolog (1970s): Basic logic programming
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Query: grandparent(tom, ann).  → true
% Query: grandparent(tom, X).    → X = ann ; X = bob

% Classic: List processing
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

% ISO Prolog: Standardized built-ins
% Arithmetic
X is 2 + 3 * 4.          % X = 14
X =:= 14.                % true (arithmetic equality)
X =\= 15.                % true (arithmetic inequality)

% Constraint Logic Programming (CLP)
:- use_module(library(clpfd)).
sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Cols),
    maplist(all_distinct, Cols).

% Tabling (memoization) — SWI-Prolog 9.x
:- table fib/2.
fib(0, 0).
fib(1, 1).
fib(N, F) :- N > 1, N1 is N-1, N2 is N-2, fib(N1, F1), fib(N2, F2), F is F1+F2.

% Modules (ISO)
:- module(shapes, [area/2]).
area(circle(R), A) :- A is pi * R * R.
area(rect(W, H), A) :- A is W * H.

% DCG (Definite Clause Grammars) — natural language
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb, noun_phrase.
determiner --> [the].
noun --> [cat].
verb --> [chased].
```

## Tiến hóa tính năng
```
1972: Basic Horn clauses, unification, backtracking
1977: DEC-10 Prolog — efficient compiler, cut operator
1980s: DCG (Definite Clause Grammars), difference lists
1990s: Constraint Logic Programming (CLP(FD), CLP(Q))
1995: ISO standard — portable Prolog
2000s: Tabling (memoization), modules, multi-threading
2010s: Tabling becomes default, pack systems, web integration
2020s: Modern implementations (Scryer, Trealla), improved performance
```

## Nguyên tắc thiết kế chính
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## Tăng trưởng hệ sinh thái
```
1972: Prolog created at Marseille — AI research
1977: DEC-10 Prolog — practical implementation
1980s: Japan's Fifth Generation Project — Prolog-based AI computers
1987: SWI-Prolog — open source, becomes most popular
1995: ISO standard — portability
1999: GNU Prolog — native compilation
2000s: Prolog in: expert systems, NLP, type inference, verification
2018: Scryer Prolog — modern Rust implementation
2022: Trealla Prolog — fast C implementation
2025: Prolog used in: IBM Watson (early), natural language processing,
       type systems, theorem proving, scheduling, rule engines
       SWI-Prolog is the reference implementation
```
