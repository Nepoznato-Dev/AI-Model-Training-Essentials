<!--
---
# Metadata
title: "Prolog"
description: "Comprehensive reference for the Prolog programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prolog, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mở đầu
Prolog (Lập trình logic) là ngôn ngữ lập trình logic được tạo ra vào năm 1972 bởi Alain Colmerauer và Philippe Roussel. Không giống như mọi ngôn ngữ khác trong danh sách này, Prolog không cho máy tính biết *cách* giải quyết vấn đề — bạn khai báo *điều gì* là đúng (sự kiện và quy tắc) và công cụ suy luận của Prolog tìm ra câu trả lời thông qua suy luận logic.
Prolog là ngôn ngữ được lựa chọn cho các hệ thống chuyên gia, xử lý ngôn ngữ tự nhiên và nghiên cứu AI vào những năm 1980. Nó hỗ trợ dự án Hệ thống máy tính thế hệ thứ năm của Nhật Bản và được sử dụng trong Watson của IBM để hiểu ngôn ngữ tự nhiên. Ngày nay, Prolog được sử dụng trong việc giải quyết ràng buộc, lập kế hoạch, suy luận kiểu, lý luận pháp lý và mọi vấn đề đều được thể hiện một cách tự nhiên dưới dạng các mối quan hệ logic.
**Lập trình logic ràng buộc (CLP)** mở rộng Prolog với các bộ giải ràng buộc để lập kế hoạch, định tuyến và phân bổ tài nguyên — những vấn đề cực kỳ khó khăn trong các ngôn ngữ mệnh lệnh.
---

## Tại sao Prolog lại quan trọng
- **Lập trình khai báo**: Mô tả điều gì là đúng, không phải cách tính toán nó. Động cơ thực hiện công việc.
- **Đối sánh mẫu và hợp nhất**: Thuật toán hợp nhất của Prolog mạnh hơn so với đối sánh mẫu trong các ngôn ngữ khác.
- **Tìm kiếm quay lại**: Tự động khám phá tất cả các giải pháp có thể. Không cần thuật toán tìm kiếm thủ công.
- **Tự nhiên cho các vấn đề logic**: Hệ thống chuyên gia, công cụ quy tắc, trình kiểm tra kiểu, trình phân tích cú pháp ngữ pháp — những hệ thống này ánh xạ trực tiếp tới Prolog.
- **Giải quyết ràng buộc**: CLP(FD) giải quyết các vấn đề lập kế hoạch, phân bổ và tổ hợp một cách tinh tế.
- **Tư duy khác biệt**: Learning Prolog thay đổi cách bạn tiếp cận việc giải quyết vấn đề — bạn bắt đầu suy nghĩ về các mối quan hệ và những ràng buộc.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Mô hình rất khác** | Không có biến (chỉ có ràng buộc), không có vòng lặp, không có bài tập | Suy nghĩ theo quan hệ và đệ quy, không phải thay đổi trạng thái |
| **Hiệu suất** | Chậm khi tính toán số và dữ liệu lớn | Dùng để suy luận; ủy quyền tính toán cho C/các ngôn ngữ khác |
| **Gỡ lỗi khó khăn** | Khó theo dõi các lỗi quay lại và thống nhất | Sử dụng các công cụ theo dõi/gỡ lỗi; viết các vị từ xác định |
| **Toán tử cắt (!)** | Cần thiết cho hiệu quả nhưng phá vỡ sự thuần khiết logic | Sử dụng đánh giá if-then-else hoặc đánh giá theo bảng khi có thể |
| **Hệ sinh thái hạn chế** | Ít thư viện, khung công tác hoặc tài nguyên cộng đồng | SWI-Prolog là cách triển khai đầy đủ nhất |
| **Không dành cho ứng dụng chung** | Web, di động, GUI — không phải thế mạnh của Prolog | Sử dụng làm công cụ lý luận đằng sau một ứng dụng web |
---

##Cơ bản về cú pháp
```prolog
% Facts (things that are true)
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).

male(tom).
male(bob).
female(liz).
female(ann).
female(pat).

% Rules (logical implications)
father(X, Y) :- parent(X, Y), male(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Recursion
my_length([], 0).
my_length([_|Tail], N) :-
    my_length(Tail, N1),
    N is N1 + 1.

% List processing
my_append([], L, L).
my_append([H|T1], L2, [H|T3]) :-
    my_append(T1, L2, T3).

my_member(X, [X|_]).
my_member(X, [_|Tail]) :- my_member(X, Tail).

% Negation as failure
dislikes(X, Y) :- \+ likes(X, Y).

% Cut (commit to choices)
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% Constraint Logic Programming
:- use_module(library(clpfd)).
solve_sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_different, Rows),
    columns(Rows, Cols),
    maplist(all_different, Cols),
    maplist(label, Rows).
```

---

## Cú pháp & Mẫu nâng cao
### Đi sâu thống nhất
Hợp nhất là cơ chế cốt lõi của Prolog - đó là cách Prolog "khớp" các thuật ngữ và liên kết các biến.
```prolog
% Unification rules:
% 1. Two constants unify if they are identical
%    ?- hello = hello.     -> true
%    ?- hello = world.     -> false
%
% 2. A variable unifies with anything (binding)
%    ?- X = hello.         -> X = hello
%    ?- X = Y.             -> X = Y (shared variable)
%
% 3. Complex terms unify if functors match and all args unify
%    ?- f(X, b) = f(a, Y). -> X = a, Y = b
%    ?- f(a, b) = f(a, c). -> false
%
% 4. Lists unify element by element
%    ?- [H|T] = [1, 2, 3]. -> H = 1, T = [2, 3]

% The == operator (structural equality, no binding)
% ?- X == X.      -> true
% ?- X == Y.      -> false (different variables)
% ?- X = Y, X == Y. -> true (after unification)
```

### Điểm quay lại và lựa chọn
```prolog
% Prolog creates choice points when multiple clauses can match
perm([], []).
perm(L, [H|T]) :-
    select(H, L, Rest),
    perm(Rest, T).

% ?- perm([1,2,3], P).
% P = [1,2,3] ; P = [1,3,2] ; P = [2,1,3] ; ...

% Collecting all solutions
?- findall(X, member(X, [1,2,3,4,5]), All).
% All = [1, 2, 3, 4, 5]

?- bagof(X, parent(Y, X), Children).
% Y = tom, Children = [bob, liz] ;
% Y = bob, Children = [ann, pat].

% Cut operator — prevents backtracking
classify(X, positive) :- X > 0, !.
classify(X, negative) :- X < 0, !.
classify(0, zero).
```

### Ngữ pháp mệnh đề xác định (DCG)
```prolog
% Simple sentence parser
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb.
verb_phrase --> verb, noun_phrase.

determiner --> [the].
determiner --> [a].
noun --> [cat].
noun --> [dog].
noun --> [mouse].
verb --> [chased].
verb --> [ate].

% ?- phrase(sentence, [the, cat, chased, the, mouse]).
% true

% DCG with parse tree construction
sentence(s(NP, VP)) --> noun_phrase(NP), verb_phrase(VP).
noun_phrase(np(Det, N)) --> determiner(Det), noun(N).
verb_phrase(vp(V, NP)) --> verb(V), noun_phrase(NP).
verb_phrase(vp(V)) --> verb(V).

determiner(det(the)) --> [the].
noun(noun(cat)) --> [cat].
verb(verb(chased)) --> [chased].
```

### Lập trình logic ràng buộc (CLP)
```prolog
:- use_module(library(clpfd)).

% SEND + MORE = MONEY puzzle
send_more_money([S,E,N,D,M,O,R,Y]) :-
    Vars = [S,E,N,D,M,O,R,Y],
    Vars ins 0..9,
    all_different(Vars),
    S #> 0, M #> 0,
      S*1000 + E*100 + N*10 + D
    + M*1000 + O*100 + R*10 + E
    #= M*10000 + O*1000 + N*100 + E*10 + Y,
    label(Vars).

% N-Queens problem
n_queens(N, Qs) :-
    length(Qs, N),
    Qs ins 1..N,
    all_different(Qs),
    safe_queens(Qs),
    label(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe_queens(Qs).

no_attack(_, [], _).
no_attack(Q, [Q1|Qs], D) :-
    Q #\= Q1 + D,
    Q #\= Q1 - D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
```

---

## Thiết kế kiến ​​trúc & hệ thống
### Mô hình lập trình logic
```
+---------------------------------------------+
|              Prolog Program                  |
+---------------------------------------------+
|  Facts:     parent(tom, bob).                |
|             color(red).                      |
+---------------------------------------------+
|  Rules:     grandparent(X, Z) :-             |
|               parent(X, Y), parent(Y, Z).    |
+---------------------------------------------+
|  Queries:   ?- grandparent(tom, X).          |
|             -> X = ann ; X = pat.            |
+---------------------------------------------+
```

###Cấu trúc dự án điển hình
```
prolog-project/
├── src/
│   ├── main.pl              * Entry point
│   ├── rules.pl             * Domain rules
│   ├── facts.pl             * Knowledge base
│   ├── utils.pl             * Utility predicates
│   └── grammar.pl           * DCG definitions
├── tests/
│   ├── test_rules.pl        * Unit tests
│   └── test_grammar.pl      * Grammar tests
├── data/
│   └── knowledge_base.pl    * Fact database
├── Makefile
└── README.md
```

### Hệ thống mô-đun
```prolog
:- module(validator, [
    validate_user/2,
    validate_email/1,
    check_password/1
]).

% Private predicate
is_valid_length(Str, Min, Max) :-
    string_length(Str, Len),
    Len >= Min, Len =< Max.

% Public predicates
validate_user(User, Errors) :-
    findall(Error, validate_field(User, Error), Errors).

validate_field(user(Name, Email, _), Error) :-
    \+ is_valid_length(Name, 2, 50),
    Error = 'Name must be 2-50 characters'.
validate_field(user(_, Email, _), Error) :-
    \+ validate_email(Email),
    Error = 'Invalid email format'.

validate_email(Email) :-
    atom_string(Email, Str),
    sub_string(Str, _, _, _, @).
```
---

## Cấu hình dự án & xây dựng hệ thống
### Cấu hình SWI-Prolog
```prolog
:- set_prolog_flag(verbose, silent).
:- set_prolog_stack(global, limit(2*10**9)).

:- use_module(library(clpfd)).
:- use_module(library(lists)).
:- use_module(library(apply)).

:- dynamic fact_cache/2.

:- table fibonacci/2.
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :-
    N > 1, N1 is N - 1, N2 is N - 2,
    fibonacci(N1, F1), fibonacci(N2, F2),
    F is F1 + F2.
```

### Chạy chương trình Prolog
```bash
# Interactive mode
swipl
?- [main].
?- halt.

# Run query from command line
swipl -g "solve(X), write(X), nl, halt" -s main.pl

# Compile to standalone executable
swipl -o solver -g main -c main.pl

# Run tests
swipl -g "run_tests, halt" -s tests/test_rules.pl
```

### Cấu hình bản dựng
```makefile
SWIPL    = swipl
TARGET   = solver
SOURCES  = src/main.pl src/rules.pl src/utils.pl

$(TARGET): $(SOURCES)
	$(SWIPL) -o $(TARGET) -g main -c $(SOURCES)

test:
	$(SWIPL) -g "run_tests, halt" -s tests/test_rules.pl

run:
	$(SWIPL) -s src/main.pl

clean:
	rm -f $(TARGET)

.PHONY: test run clean
```

---

## Kiểm tra & gỡ lỗi
### Theo dõi tích hợp
```prolog
?- trace.
?- grandparent(tom, X).
[trace]  Call: (10) grandparent(tom, _1234)
[trace]  Call: (11) parent(tom, _1256)
[trace]  Exit: (11) parent(tom, bob)
[trace]  Exit: (10) grandparent(tom, ann)
X = ann.
?- notrace.

?- spy parent/2.
?- nospy parent/2.
```

### Kiểm thử đơn vị với PLUnit
```prolog
:- begin_tests(family).

test(father_basic) :-
    father(tom, bob),
    \+ father(liz, bob).

test(grandparent, set(X == [ann, pat])) :-
    findall(X, grandparent(tom, X), Xs),
    member(X, Xs).

test(list_length) :-
    my_length([], 0),
    my_length([a], 1),
    my_length([1,2,3,4], 4).

:- end_tests(family).
```

### Các mẫu gỡ lỗi phổ biến
| Vấn đề | Triệu chứng | Giải pháp |
|----------|----------|----------|
| Đệ quy vô hạn | tràn ngăn xếp | Kiểm tra trường hợp cơ sở; thêm điều kiện chấm dứt |
| Không có giải pháp | Truy vấn trả về sai | Kiểm tra thứ tự khởi tạo biến |
| Quá nhiều giải pháp | Trùng lặp bất ngờ | Thêm cắt (!) hoặc sử dụng`setof`|
| Thống nhất sai lầm | Các biến bị ràng buộc không chính xác | Sử dụng`=`để kiểm tra; kiểm tra tính chất của hàm số |
| Vấn đề về hiệu suất | Thực thi chậm | Thêm vết cắt; sử dụng `table`; kiểm tra điểm lựa chọn |
---

## Khả năng tương tác
### Giao diện C (FFI)
```c
/* fast_math.c */
#include <SWI-Prolog.h>
static foreign_t pl_fast_add(term_t A, term_t B, term_t Result) {
    long a, b;
    if (PL_get_long(A, &a) && PL_get_long(B, &b))
        return PL_unify_long(Result, a + b);
    return FALSE;
}
install_t install_fast_math() {
    PL_register_foreign("fast_add", 3, pl_fast_add, 0);
}
```

```prolog
:- load_foreign_library(fast_math).
```

### Tích hợp Python
```prolog
:- use_module(library(unix)).
call_python(Expression, Result) :-
    process_create(path(python3),
        ['-c', atom_concat('print(', Expression, Cmd))],
        [stdout(pipe(Out))]),
    read_line_to_codes(Out, Codes),
    close(Out), number_codes(Result, Codes).
```

---

## Mẫu thiết kế
### Mẫu 1: Tích lũy (Đệ quy đuôi)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Mẫu 2: Phân luồng trạng thái```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Mẫu 3: Tạo và kiểm tra```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Mẫu 4: Danh sách khác biệt```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Hiệu suất & Tối ưu hóa
### Tối ưu hóa cắt
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Đệ quy đuôi
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Danh sách kiểm tra tối ưu hóa
| Kỹ thuật | Tác động | Mô tả |
|----------|----------|-------------|
| **Đệ quy đuôi** | Cao | Sử dụng bộ tích lũy để có không gian ngăn xếp không đổi |
| **Cắt (xanh)** | Cao | Loại bỏ những điểm lựa chọn không cần thiết |
| **Đánh giá theo bảng** | Cao | `:- table pred/N`ghi nhớ kết quả |
| **Lập chỉ mục** | Trung bình | Đặt lập luận phân biệt đối xử lên hàng đầu |
| **Danh sách khác biệt** | Trung bình | Nối danh sách O(1) |
| **CLP(FD) qua thử nghiệm tạo** | Rất Cao | Sử dụng các ràng buộc thay vì vũ phu |
---

## Triển khai & Sử dụng trong Thế giới Thực
### Triển khai ứng dụng Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Ứng dụng trong thế giới thực
| Tên miền | Prolog được sử dụng như thế nào | Ví dụ |
|--------|-------------------|---------|
| **Hệ thống chuyên gia** | Chẩn đoán y tế, phát hiện lỗi | MYCIN, XCON |
| **NLP** | Phân tích ngữ pháp, phân tích ngữ nghĩa | Chatbots, hệ thống QA |
| **Gõ suy luận** | Kiểm tra kiểu Hindley-Milner | Nguyên mẫu Haskell/ML |
| **Lên lịch** | Lập kế hoạch, thời gian biểu cho nhân viên | Lập lịch trình phi hành đoàn hàng không |
| **Lý luận pháp lý** | Phân tích pháp lý dựa trên quy tắc | Kiểm tra tuân thủ |
| **Truy vấn cơ sở dữ liệu** | Datalog để phân tích dữ liệu | Động cơ Soufflé |
| **Xác minh** | Kiểm tra mô hình | Xác minh phần cứng |
| **IBM Watson** | Hiểu ngôn ngữ tự nhiên | Nguy cơ! hệ thống |
| **Ericsson** | Quản lý viễn thông | Xác thực cấu hình mạng |
---

## Khi nào nên sử dụng Prolog
| Kịch bản | Tại sao Prolog | Thay thế tốt hơn |
|----------|-------------|-------------------|
| Lý luận dựa trên quy tắc | Prolog được xây dựng cho việc này | Công cụ quy tắc tùy chỉnh trong Python/Java |
| Hạn chế sự hài lòng | CLP(FD) thanh lịch và hiệu quả | Bộ giải SAT, Công cụ OR cho các trường hợp lớn |
| Phân tích ngữ pháp / ngôn ngữ | DCG (Ngữ pháp mệnh đề xác định) là nguồn gốc | Trình tạo trình phân tích cú pháp (ANTLR, yacc) để sản xuất |
| Hệ thống chuyên gia | Sự phù hợp tự nhiên - sự kiện + quy tắc = hệ thống chuyên gia | Công cụ quy tắc kinh doanh (Drools) |
| Lập kế hoạch/lịch trình | CLP giải quyết tốt những điều này | Công cụ OR, OptaPlanner |
| Nghiên cứu hệ thống kiểu | Thống nhất là nền tảng | Triển khai trong OCaml, Haskell, Rust |
| Ứng dụng web | Không phù hợp | Python, Node.js, Đi |
| Khoa học dữ liệu / ML | Không phải hệ sinh thái | Python, R |
| Mã quan trọng về hiệu suất | Prolog tính toán chậm | C, C++, Rust |
| Lập trình mục đích chung | Có thể nhưng khó xử | Python, Go, Java |
---

## Hỏi đáp tổng hợp
### Q1: Sự hợp nhất của Prolog khác với sự phân công trong các ngôn ngữ khác như thế nào?
**A:** Hợp nhất là khớp mẫu hai chiều, không phải phép gán:
```prolog
% Unification (=) tries to make both sides equal
X = 5.              % X is now 5
5 = X.              % same thing — X is 5
f(X, b) = f(a, Y).  % X = a, Y = b

% Once bound, a variable cannot change (in the same scope)
X = 1, X = 2.      % FAILS — X is already 1

% Anonymous variable _ matches anything
f(a, _) = f(a, b).  % true — _ matches b
```

### Câu 2: Tính năng quay lui hoạt động như thế nào trong Prolog?
**A:** Khi mục tiêu không thành công, Prolog sẽ quay lại điểm lựa chọn cuối cùng và thử giải pháp thay thế tiếp theo:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Câu 3: Làm cách nào để làm việc với các danh sách trong Prolog?
**A:** Danh sách sử dụng khớp mẫu đầu/đuôi:
```prolog
% Pattern matching on lists
[X|Xs] = [1, 2, 3].  % X = 1, Xs = [2, 3]

% Common list predicates
my_length([], 0).
my_length([_|T], N) :- my_length(T, N1), N is N1 + 1.

my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).

my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).
```

### Q4: Khi nào nên sử dụng Prolog thay vì các ngôn ngữ khác?
**A:** Prolog vượt trội ở:
- Sự thỏa mãn ràng buộc (lập kế hoạch, câu đố)
- Hệ thống dựa trên quy tắc (hệ thống chuyên gia, xác nhận)
- Duyệt đồ thị/cây
- Xử lý ngôn ngữ tự nhiên
- Tính toán tượng trưng
- Bất kỳ vấn đề nào được biểu diễn dưới dạng quan hệ logic
### Q5: Những cạm bẫy thường gặp trong Prolog là gì?
**Đ:** Các vấn đề chính:
- Đệ quy vô hạn - luôn đặt trường hợp cơ sở lên hàng đầu
- Quay lại ngoài ý muốn — sử dụng`!`hoặc`once/1`đã cắt 
- Xảy ra kiểm tra - vòng lặp`X = f(X)`theo mặc định (sử dụng`unify_with_occurs_check`)
- Vết cắt màu xanh lá cây (tối ưu hóa) so với vết cắt màu đỏ (thay đổi ý nghĩa) - thích màu xanh lá cây hơn
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Bài 1: Giải bài toán N-Queens
**Bước 1: Tìm hiểu vấn đề**
Đặt N quân hậu lên bàn cờ NxN sao cho không có hai quân hậu nào tấn công lẫn nhau.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng thế hệ dựa trên ràng buộc: đặt các quân hậu theo từng cột, kiểm tra độ an toàn.
**Bước 3: Thực hiện**```prolog
n_queens(N, Qs) :-
    length(Qs, N),
    numlist(1, N, Rows),
    permutation(Rows, Qs),
    safe_queens(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe_queens(Qs).

no_attack(_, [], _).
no_attack(Q, [Q1|Qs], D) :-
    Q =\= Q1,
    abs(Q - Q1) =\= D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
```

**Bước 4: Xác minh**
`?- n_queens(8, Qs).`sẽ tìm ra 92 giải pháp.
### Bài toán 2: Xây dựng hệ chuyên gia đơn giản
**Bước 1: Tìm hiểu vấn đề**
Chẩn đoán các vấn đề về xe dựa trên các triệu chứng.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng quy tắc Prolog để mã hóa kiến thức chẩn đoán.
**Bước 3: Thực hiện**```prolog
% Facts about symptoms
symptom(car_wont_start).
symptom(clicking_sound).

% Rules
diagnosis(battery_dead) :-
    symptom(car_wont_start),
    symptom(clicking_sound).

diagnosis(starter_motor) :-
    symptom(car_wont_start),
    symptom(single_click),
    \+ symptom(clicking_sound).

diagnosis(out_of_fuel) :-
    symptom(engine_cranks),
    symptom(engine_wont_catch).

% Query
?- diagnosis(X).
```

**Bước 4: Gia hạn**
Thêm điểm tin cậy, hỏi người dùng về các triệu chứng một cách tương tác và chẩn đoán chuỗi.
---

## Bản tóm tắt
Prolog không giống bất kỳ ngôn ngữ lập trình nào khác. Thay vì viết hướng dẫn từng bước, bạn mô tả các mối quan hệ và ràng buộc — và công cụ tìm kiếm giải pháp thông qua suy luận logic. Điều này làm cho Prolog trở nên lý tưởng cho các vấn đề khó xử hoặc dài dòng trong các ngôn ngữ mệnh lệnh: hệ thống chuyên gia, lập kế hoạch, phân tích cú pháp ngữ pháp, thỏa mãn ràng buộc và bất kỳ điều gì liên quan đến quy tắc logic. Hầu hết các lập trình viên sẽ không bao giờ sử dụng Prolog trong sản xuất, nhưng việc học nó sẽ mở rộng suy nghĩ của bạn về việc lập trình có thể là gì. Hợp nhất, quay lui và đặc tả vấn đề khai báo là những khái niệm ảnh hưởng đến thiết kế ngôn ngữ, nghiên cứu AI và thậm chí tối ưu hóa truy vấn cơ sở dữ liệu.
### So sánh động cơ Prolog
| Tính năng | SWI-Prolog | GNU Prolog | Tàu Prolog |
|----------|-------------|-------------|----------||
| **Giấy phép** | BSD (mã nguồn mở) | GPL (mã nguồn mở) | BSD (mã nguồn mở) |
| **Nền tảng** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (trình duyệt) |
| **CLP(FD)** | Thư viện tích hợp | Tích hợp | Không có sẵn |
| **Hỗ trợ DCG** | Đầy đủ | Đầy đủ | Hạn chế |
| **Lập bảng** | Có | Không | Không |
| **FFI (cuộc gọi C)** | Có | Có | Qua JavaScript |
| **Kết nối mạng** | HTTP, TCP, TLS | TCP | Qua JavaScript |
| **Đa luồng** | Có | Không | Không |
| **Quản lý gói** | `pack_install/1`| Không có | npm |
| **Tốt nhất cho** | Sản xuất, nghiên cứu | Giải quyết ràng buộc | Ứng dụng web, giáo dục |
### Ứng dụng web với Pengines
```prolog
% SWI-Prolog Pengines — server-side Prolog accessible from web
:- use_module(library(http/http_server)).
:- use_module(library(pengines)).
:- use_module(library(pengines/apps/sandbox)).

:- http_handler(root(.), http_reply_from_files(web, []), [prefix]).
:- http_handler(root(pengines), pengine_application(sandbox)).

:- server(8080).

% Client-side JavaScript calls Prolog predicates via HTTP
% <script>
% new Pengine({
%   server: "/pengines",
%   ask: "grandparent(tom, X)",
%   ondata: function(data) { console.log(data); }
% });
% </script>
```

### Lập trình meta với xác nhận/rút lại
```prolog
% Dynamic knowledge base modification
:- dynamic student/2.

% Add facts at runtime
add_student(Name, Grade) :-
    assert(student(Name, Grade)).

% Remove facts
remove_student(Name) :-
    retract(student(Name, _)).

% Query and modify
promote_students :-
    forall(
        student(Name, Grade),
        (   Grade < 12,
            NewGrade is Grade + 1,
            retract(student(Name, Grade)),
            assert(student(Name, NewGrade))
        )
    ).

% findall + assert pattern (batch operations)
copy_passing_students :-
    findall(Name, (student(Name, Grade), Grade >= 50), PassList),
    forall(member(Name, PassList),
        assert(passed(Name))).
```
