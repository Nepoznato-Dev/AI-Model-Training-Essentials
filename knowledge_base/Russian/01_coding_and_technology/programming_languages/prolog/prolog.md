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
# Пролог
Пролог (Программирование на логике) — язык логического программирования, созданный в 1972 году Аленом Кольмерауэром и Филиппом Русселем. В отличие от любого другого языка в этом списке, Пролог не говорит компьютеру, *как* решить проблему — вы заявляете, *что* истинно (факты и правила), а машина вывода Пролога находит ответ посредством логического вывода.
Пролог был предпочтительным языком для экспертных систем, обработки естественного языка и исследований искусственного интеллекта в 1980-х годах. Он лег в основу японского проекта компьютерной системы пятого поколения и использовался в IBM Watson для понимания естественного языка. Сегодня Пролог используется для решения ограничений, планирования, вывода типов, юридических рассуждений и везде, где проблемы естественным образом выражаются в виде логических отношений.
**Программирование логики с ограничениями (CLP)** расширяет Пролог средствами решения ограничений для планирования, маршрутизации и распределения ресурсов — задач, которые чрезвычайно сложны в императивных языках.
---

## Почему Пролог так важен
- **Декларативное программирование**: описывайте, что истинно, а не как это вычислить. Двигатель делает свою работу.
- **Сопоставление с образцом и унификация**: алгоритм унификации Пролога более мощный, чем сопоставление с образцом в других языках.
- **Поиск с возвратом**: автоматически исследуются все возможные решения. Никаких алгоритмов ручного поиска не требуется.
- **Естественно для логических задач**: экспертные системы, механизмы правил, средства проверки типов, анализаторы грамматики — все это отображается непосредственно в Прологе.
- **Решение ограничений**: CLP(FD) элегантно решает задачи планирования, распределения и комбинаторики.
- **Другое мышление**: изучение Пролога меняет ваш подход к решению проблем — вы начинаете думать об отношениях и ограничениях.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Совершенно другая парадигма** | Никаких переменных (только привязки), никаких циклов, никаких присваиваний | Думайте об отношениях и рекурсии, а не об изменениях состояния |
| **Производительность** | Медленно для численных вычислений и больших данных | Используйте для рассуждения; делегировать вычисления на C/другие языки |
| **Сложность отладки** | Трудно отследить ошибки возврата и унификации | Используйте инструменты трассировки/отладки; писать детерминированные предикаты |
| **Оператор вырезания (!)** | Необходимо для эффективности, но нарушает логическую чистоту | По возможности используйте if-then-else или табличную оценку |
| **Ограниченная экосистема** | Несколько библиотек, фреймворков и ресурсов сообщества | SWI-Prolog — наиболее полная реализация |
| **Не для обычных приложений** | Веб, мобильные устройства, графический интерфейс — не сильная сторона Пролога | Использование в качестве механизма рассуждения в веб-приложении |
---

## Основы синтаксиса
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

## Расширенный синтаксис и шаблоны
### Подробный обзор объединения
Унификация — это основной механизм Пролога, то есть то, как Пролог «сопоставляет» термины и связывает переменные.
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

### Возврат и точки выбора
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

### Грамматики определенных предложений (DCG)
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

### Программирование логики ограничений (CLP)
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

## Архитектура и системный дизайн
### Парадигма логического программирования
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

### Типичная структура проекта
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

### Система модулей
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

## Конфигурация проекта и система сборки
### Конфигурация SWI-Пролога
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

### Запуск программ Пролога
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

### Конфигурация сборки
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

## Тестирование и отладка
### Встроенная трассировка
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

### Модульное тестирование с помощью PLUnit
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

### Общие шаблоны отладки
| Проблема | Симптом | Решение |
|---------|---------|----------|
| Бесконечная рекурсия | Переполнение стека | Проверьте базовый вариант; добавить условие завершения |
| Нет решений | Запрос возвращает ложь | Проверить порядок создания переменных |
| Слишком много решений | Неожиданные дубликаты | Добавьте вырез (!) или используйте`setof`|
| Неправильное объединение | Переменные привязаны неправильно | Используйте`=`для проверки; проверить арность функтора |
| Проблема с производительностью | Медленное исполнение | Добавьте разрезы; используйте`table`; проверить пункты выбора |
---

## Совместимость
### Интерфейс C (FFI)
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

### Интеграция Python
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

## Шаблоны проектирования
### Шаблон 1: аккумулятор (хвостовая рекурсия)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Шаблон 2: Потоки состояния```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Шаблон 3: Генерация и тестирование```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Шаблон 4: Списки различий```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Производительность и оптимизация
### Оптимизация обрезки
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Хвостовая рекурсия
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Контрольный список оптимизации
| Техника | Воздействие | Описание |
|-----------|--------|-------------|
| **Tail recursion** | Высокий | Используйте аккумуляторы для постоянного места в стеке |
| **Cut (green)** | Высокий | Устраните ненужные точки выбора |
| **Tabled evaluation** | Высокий | `:- table pred/N`запоминает результаты |
| **Indexing** | Средний | Ставьте дискриминирующий аргумент на первое место |
| **Difference lists** | Средний | Объединение списков O(1) |
| **CLP(FD) поверх генератора-теста** | Очень высокий | Используйте ограничения вместо грубой силы |
---

## Развертывание и использование в реальных условиях
### Развертывание приложений Пролога
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Реальные приложения
| Домен | Как используется Пролог | Пример |
|--------|-------------------|---------|
| **Экспертные системы** | Медицинская диагностика, дефектация | МАЙЦИН, XCON |
| **НЛП** | Грамматический разбор, семантический анализ | Чат-боты, системы контроля качества |
| **Вывод типа** | Проверка типа Хиндли-Милнера | Прототипы Haskell/ML |
| **Расписание** | График работы сотрудников, составление расписания | Планирование экипажа авиакомпании |
| **Юридическое обоснование** | Правовой анализ, основанный на правилах | Проверка соответствия |
| **Запрос к базе данных** | Журнал данных для анализа данных | Суфле двигатель |
| **Проверка** | Проверка модели | Проверка оборудования |
| **IBM Watson** | Понимание естественного языка | Опасность! система |
| **Эрикссон** | Управление телекоммуникациями | Проверка конфигурации сети |
---

## Когда использовать Пролог
| Сценарий | Почему Пролог | Лучшая альтернатива |
|----------|-----------|-------------------|
| Рассуждения, основанные на правилах | Пролог создан для этого | Механизмы пользовательских правил в Python/Java |
| Удовлетворение ограничений | CLP(FD) — элегантно и эффективно | Решатели SAT, OR-инструменты для больших случаев |
| Грамматика/разбор языка | DCG (грамматики определенных предложений) являются родными | Генераторы парсеров (ANTLR, yacc) для производства |
| Экспертные системы | Естественное соответствие — факты + правила = экспертная система | Механизмы бизнес-правил (Drools) |
| Планирование / расписание | CLP хорошо решает эти проблемы | OR-Инструменты, OptaPlanner |
| Типовое исследование системы | Объединение – это основа | Реализация в OCaml, Haskell, Rust |
| Веб-приложения | Не подходит | Python, Node.js, Go |
| Наука о данных / ML | Не экосистема | Питон, Р |
| Код, критичный к производительности | Пролог медленно выполняет вычисления | Си, С++, Руст |
| Программирование общего назначения | Возможно, но неудобно | Питон, Го, Java |
---

## Синтетические вопросы и ответы
### В1: Чем унификация Пролога отличается от присваивания в других языках?
**A:** Унификация — это двунаправленное сопоставление шаблонов, а не присвоение:
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

### Вопрос 2: Как работает возврат в Прологе?
**A:** Если цель не достигнута, Пролог возвращается к последней точке выбора и пробует следующую альтернативу:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Вопрос 3: Как работать со списками в Прологе?
**A:** В списках используется сопоставление шаблонов «голова/хвост»:
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

### Вопрос 4: Когда мне следует использовать Пролог вместо других языков?
**О:** Пролог превосходно справляется со следующими задачами:
- Удовлетворение ограничениями (планирование, головоломки)
- Системы, основанные на правилах (экспертные системы, валидация)
- Обход графа/дерева
- Обработка естественного языка
- Символическое вычисление
- Любая проблема, выражаемая в виде логических отношений.
### Вопрос 5: Каковы типичные ошибки Пролога?
**О:** Ключевые вопросы:
- Бесконечная рекурсия — всегда сначала ставьте базовый вариант
- Непреднамеренный возврат — используйте сокращение`!`или `once/1`. 
- Происходит проверка — цикл`X = f(X)`по умолчанию (используйте`unify_with_occurs_check`)
- Зеленые сокращения (оптимизация) против красных сокращений (изменение значения) — предпочтение зеленому
---

## Решение проблем с цепочкой мыслей
### Задача 1: решение головоломки с N ферзями
**Шаг 1. Поймите проблему**
Разместите N ферзей на шахматной доске NxN так, чтобы никакие два ферзя не атаковали друг друга.
**Шаг 2. Определите подход**
Используйте генерацию на основе ограничений: размещайте ферзей столбец за столбцом, проверяя безопасность.
**Шаг 3. Реализация**```prolog
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

**Шаг 4. Проверка**
`?- n_queens(8, Qs).`должен найти 92 решения.
### Проблема 2: Создание простой экспертной системы
**Шаг 1. Поймите проблему**
Диагностика неисправностей автомобиля по симптомам.
**Шаг 2. Определите подход**
Используйте правила Пролога для кодирования диагностических знаний.
**Шаг 3. Реализация**```prolog
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

**Шаг 4. Продлить**
Добавляйте показатели уверенности, интерактивно спрашивайте пользователя о симптомах и ставьте диагнозы по цепочке.
---

## Краткое содержание
Пролог не похож ни на один другой язык программирования. Вместо написания пошаговых инструкций вы описываете взаимосвязи и ограничения, а движок ищет решения посредством логического вывода. Это делает Пролог идеальным для решения сложных или многословных задач в императивных языках: экспертные системы, планирование, анализ грамматики, удовлетворение ограничений и все, что связано с логическими правилами. Большинство программистов никогда не будут использовать Пролог в работе, но его изучение расширяет ваши представления о том, каким может быть программирование. Унификация, возврат и декларативная спецификация задач — это концепции, которые влияют на проектирование языка, исследования ИИ и даже на оптимизацию запросов к базе данных.
### Сравнение движков Пролога
| Особенность | SWI-Пролог | GNU Пролог | Тау Пролог |
|---------|-----------|------------|------------|
| **Лицензия** | BSD (с открытым исходным кодом) | GPL (с открытым исходным кодом) | BSD (с открытым исходным кодом) |
| **Платформа** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (браузер) |
| **CLP(ФД)** | Встроенная библиотека | Встроенный | Недоступно |
| **Поддержка DCG** | Полный | Полный | Ограниченная |
| **Таблица** | Да | Нет | Нет |
| **FFI (вызовы C)** | Да | Да | Через JavaScript |
| **Сеть** | HTTP, TCP, TLS | TCP | Через JavaScript |
| **Многопоточность** | Да | Нет | Нет |
| **Менеджер пакетов** | `pack_install/1`| Нет | НПМ |
| **Лучший вариант** | Производство, исследования | Решение ограничений | Веб-приложения для образования |
### Веб-приложения с Pengins
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

### Метапрограммирование с утверждением/откатом
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
