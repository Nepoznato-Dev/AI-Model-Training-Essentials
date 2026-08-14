---
# Metadata
title: "Prolog — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Prolog with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [prolog, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Prolog — Những lỗi thường gặp & mẫu phản đối
Tài liệu này liệt kê các lỗi, bẫy và kiểu chống phổ biến nhất trong Prolog kèm theo các bản sửa lỗi.
---

## 1.`=`vs`==`vs `is`
```prolog
% ❌ WRONG — confusing unification with equality
X = 5.          % unifies X with 5
X == 5.         % strict equality (no unification)
X is 2 + 3.     % arithmetic evaluation

% ✅ CORRECT — understand the difference
% = is unification (pattern matching)
% == is strict equality (both sides must be identical)
% is evaluates arithmetic on the right side
```

---

## 2. Sử dụng tính năng Cắt (`!`) Không Đúng Cách
```prolog
% ❌ WRONG — cut in wrong place causes missed solutions
max(X, Y, X) :- X >= Y.
max(X, Y, Y).  % always tries second clause too

% ✅ CORRECT — cut prevents unnecessary backtracking
max(X, _, X) :- X >= 0, !.
max(_, Y, Y).
```

---

## 3. Đệ quy vô hạn
```prolog
% ❌ WRONG — no base case or wrong order
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
% If parent has cycles, this loops forever

% ✅ CORRECT — track visited nodes
ancestor(X, Y, Visited) :-
    parent(X, Y),
    \+ member(X, Visited).
ancestor(X, Y, Visited) :-
    parent(X, Z),
    \+ member(Z, Visited),
    ancestor(Z, Y, [Z|Visited]).
```

---

## 4. Không hiểu Xảy ra Kiểm tra
```prolog
% ❌ WRONG — X = f(X) creates infinite term
?- X = f(X).
% In most Prologs: succeeds (X = f(f(f(f(...)))))
% With occurs check: fails (correct behavior)

% ✅ CORRECT — enable occurs check
% SWI-Prolog: set_prolog_flag(occurs_check, true).
```

---

## 5. Danh sách các thao tác không có bộ tích lũy
```prolog
% ❌ WRONG — inefficient list append
my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).
% O(n) per call, O(n²) for building list

% ✅ CORRECT — use accumulator for building lists
reverse(List, Reversed) :- reverse(List, [], Reversed).
reverse([], Acc, Acc).
reverse([H|T], Acc, Reversed) :- reverse(T, [H|Acc], Reversed).
```

---

## Bản tóm tắt
Mô hình lập trình logic của Prolog tạo ra những cái bẫy độc đáo: gây nhầm lẫn`=`(hợp nhất),`==`(bình đẳng) và`is`(số học); vị trí cắt không chính xác; đệ quy vô hạn mà không cần theo dõi lượt truy cập; và việc kiểm tra xảy ra. Cách của Prolog là: hiểu sâu sắc về sự hợp nhất, sử dụng cắt một cách tiết kiệm và chính xác, sử dụng bộ tích lũy để xây dựng danh sách hiệu quả và luôn cân nhắc việc chấm dứt.