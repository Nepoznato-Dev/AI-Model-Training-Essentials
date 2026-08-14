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
# Giriş
Prolog (Mantıkta Programlama), 1972 yılında Alain Colmerauer ve Philippe Roussel tarafından oluşturulan bir mantıksal programlama dilidir. Bu listedeki diğer tüm dillerden farklı olarak Prolog, bilgisayara bir sorunu *nasıl* çözeceğini söylemez; siz *neyin* doğru olduğunu bildirirsiniz (gerçekler ve kurallar) ve Prolog'un çıkarım motoru, mantıksal çıkarım yoluyla cevabı bulur.
Prolog, 1980'lerde uzman sistemler, doğal dil işleme ve yapay zeka araştırmaları için tercih edilen dildi. Japonya'nın Beşinci Nesil Bilgisayar Sistemi projesine güç verdi ve doğal dilin anlaşılması için IBM'in Watson'ında kullanıldı. Günümüzde Prolog, kısıtlama çözme, zamanlama, tür çıkarımı, yasal akıl yürütme ve sorunların doğal olarak mantıksal ilişkiler olarak ifade edildiği her yerde kullanılmaktadır.
**Kısıtlama Mantık Programlaması (CLP)**, Prolog'u, zorunlu dillerde son derece zor olan planlama, yönlendirme ve kaynak tahsisi sorunlarına yönelik kısıtlama çözücülerle genişletir.
---

## Prolog Neden Önemlidir
- **Bildirimsel programlama**: Nasıl hesaplanacağını değil, neyin doğru olduğunu açıklayın. Motor işi yapar.
- **Desen eşleştirme ve birleştirme**: Prolog'un birleştirme algoritması diğer dillerdeki desen eşleştirmeden daha güçlüdür.
- **Geriye dönük arama**: Olası tüm çözümleri otomatik olarak araştırır. Manuel arama algoritmalarına gerek yoktur.
- **Mantık sorunları için doğaldır**: Uzman sistemler, kural motorları, tür denetleyicileri, dilbilgisi ayrıştırıcıları — bunlar doğrudan Prolog'a eşlenir.
- **Kısıtlama çözme**: CLP(FD), planlama, tahsis ve kombinatoryal sorunları zarif bir şekilde çözer.
- **Farklı düşünme**: Prolog'u öğrenmek problem çözmeye yaklaşımınızı değiştirir; ilişkiler ve kısıtlamalar çerçevesinde düşünmeye başlarsınız.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Çok farklı bir paradigma** | Değişken yok (yalnızca bağlamalar), döngü yok, atama yok | Durum değişikliklerini değil, ilişkileri ve özyinelemeyi düşünün |
| **Performans** | Sayısal hesaplama ve büyük veriler için yavaş | Muhakeme için kullanın; hesaplamayı C/diğer dillere devredin |
| **Hata ayıklama zorluğu** | Geri izleme ve birleştirme hatalarının izini sürmek zor | İzleme/hata ayıklama araçlarını kullanın; deterministik yüklemler yazma |
| **Kesme operatörü (!)** | Verimlilik için gerekli ancak mantıksal saflığı bozuyor | Mümkün olduğunda if-then-else veya tablolanmış değerlendirmeyi kullanın |
| **Sınırlı ekosistem** | Az sayıda kütüphane, çerçeve veya topluluk kaynağı | SWI-Prolog en eksiksiz uygulamadır |
| **Genel uygulamalar için değil** | Web, mobil, GUI — Prolog'un gücü değil | Bir web uygulamasının arkasında akıl yürütme motoru olarak kullanın |
---

## Söz Diziminin Temelleri
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

## Gelişmiş Sözdizimi ve Desenler
### Birleştirme Derinlemesine İnceleme
Birleştirme Prolog'un temel mekanizmasıdır; Prolog'un terimleri nasıl "eşleştirdiği" ve değişkenleri nasıl bağladığı budur.
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

### Geriye Dönme ve Seçim Noktaları
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

### Kesin Cümle Dilbilgileri (DCG'ler)
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

### Kısıtlama Mantığı Programlama (CLP)
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

## Mimari ve Sistem Tasarımı
### Mantık Programlama Paradigması
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

### Tipik Proje Yapısı
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

### Modül Sistemi
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

## Proje Yapılandırması ve Oluşturma Sistemi
### SWI-Prolog Yapılandırması
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

### Prolog Programlarını Çalıştırma
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

### Yapı Yapılandırması
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

## Test Etme ve Hata Ayıklama
### Yerleşik İzleme
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

### PLUnit ile Birim Testi
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

### Yaygın Hata Ayıklama Modelleri
| Sorun | Belirti | Çözüm |
|-----------|-----------|----------|
| Sonsuz özyineleme | Yığın taşması | Temel durumu kontrol edin; sonlandırma koşulu ekle |
| Çözüm yok | Sorgu false değerini döndürüyor | Değişken örnekleme sırasını kontrol edin |
| Çok fazla çözüm | Beklenmeyen kopyalar | Kes (!) ekleyin veya`setof`|
| Yanlış birleştirme | Değişkenler yanlış bağlandı | Test etmek için `=`'yi kullanın; işlevsellik durumunu kontrol edin |
| Performans sorunu | Yavaş yürütme | Kesimler ekleyin; `table`'yi kullanın; seçim noktalarını kontrol edin |
---

## Birlikte Çalışabilirlik
### C Arayüzü (FFI)
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

### Python Entegrasyonu
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

## Tasarım Desenleri
### Desen 1: Akümülatör (Kuyruk Özyineleme)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Desen 2: Durum İş Parçacığı Oluşturma```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Desen 3: Oluştur ve Test Et```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Desen 4: Fark Listeleri```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Performans ve Optimizasyon
### Kesim Optimizasyonu
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Kuyruk Yinelemesi
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Optimizasyon Kontrol Listesi
| Tekniği | Etki | Açıklama |
|-----------|-----------|------------|
| **Kuyruk yinelemesi** | Yüksek | Sabit yığın alanı için akümülatörleri kullanın |
| **Kes (yeşil)** | Yüksek | Gereksiz seçim noktalarını ortadan kaldırın |
| **Tablolanmış değerlendirme** | Yüksek | `:- table pred/N`sonuçları not eder |
| **dizin oluşturma** | Orta | Ayırıcı argümanı ilk sıraya koyun |
| **Fark listeleri** | Orta | O(1) liste birleştirme |
| **oluşturma testi üzerinden CLP(FD)** | Çok Yüksek | Kaba kuvvet yerine kısıtlamaları kullanın |
---

## Dağıtım ve Gerçek Dünya Kullanımı
### Prolog Uygulamalarını Dağıtma
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Gerçek Dünya Uygulamaları
| Etki Alanı | Prolog Nasıl Kullanılır | Örnek |
|----------|-----------|-----------|
| **Uzman sistemler** | Tıbbi teşhis, arıza tespiti | MYCİN, XCON |
| **NLP** | Dilbilgisi ayrıştırma, anlamsal analiz | Chatbot'lar, QA sistemleri |
| **Tür çıkarımı** | Hindley-Milner tip kontrolü | Haskell/ML prototipleri |
| **Zamanlama** | Çalışan planlama, zaman çizelgeleme | Havayolu mürettebat planlaması |
| **Yasal gerekçe** | Kural bazlı hukuki analiz | Uyumluluk kontrolü |
| **Veritabanı sorgulama** | Veri analizi için veri günlüğü | Sufle motoru |
| **Doğrulama** | Model kontrolü | Donanım doğrulaması |
| **IBM Watson** | Doğal dil anlayışı | Tehlike! sistem |
| **Ericsson** | Telekom yönetimi | Ağ yapılandırma doğrulaması |
---

## Prolog Ne Zaman Kullanılmalı
| Senaryo | Neden Prolog | Daha İyi Alternatif |
|----------|-----------|-----------|
| Kurala dayalı akıl yürütme | Prolog bunun için tasarlandı | Python/Java'da özel kural motorları |
| Kısıtlama memnuniyeti | CLP(FD) zarif ve verimlidir | SAT çözücüler, büyük örnekler için OR-Araçları |
| Dilbilgisi / dil ayrıştırma | DCG (Kesin Cümle Dilbilgileri) yereldir | Üretim için ayrıştırıcı jeneratörler (ANTLR, yacc) |
| Uzman sistemler | Doğal uyum — gerçekler + kurallar = uzman sistem | İş kuralı motorları (Saçmalamalar) |
| Planlama / zaman çizelgeleme | CLP bunları iyi çözüyor | OR-Araçları, OptaPlanner |
| Tip sistem araştırması | Birleşme temeldir | OCaml, Haskell, Rust'ta Uygulama |
| Web uygulamaları | Uygun değil | Python, Node.js, Git |
| Veri bilimi / ML | Ekosistem değil | Python, R |
| Performans açısından kritik kod | Prolog hesaplama açısından yavaştır | C, C++, Pas |
| Genel amaçlı programlama | Mümkün ama tuhaf | Python, Git, Java |
---

## Sentetik Soru-Cevap
### S1: Prolog'un birleştirilmesinin diğer dillerdeki atamalardan farkı nedir?
**A:** Birleştirme, atama değil, çift yönlü desen eşleştirmedir:
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

### S2: Prolog'da geri izleme nasıl çalışır?
**C:** Bir hedef başarısız olduğunda Prolog son seçim noktasına geri döner ve bir sonraki alternatifi dener:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### S3: Prolog'da listelerle nasıl çalışırım?
**A:** Listelerde baş/kuyruk deseni eşleşmesi kullanılır:
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

### S4: Ne zaman diğer diller yerine Prolog'u kullanmalıyım?
**C:** Prolog şu konularda üstündür:
- Kısıtlama tatmini (zamanlama, bulmacalar)
- Kural tabanlı sistemler (uzman sistemler, doğrulama)
- Grafik/ağaç geçişi
- Doğal dil işleme
- Sembolik hesaplama
- Mantıksal ilişkiler olarak ifade edilebilen herhangi bir problem
### S5: Prolog'daki yaygın tuzaklar nelerdir?
**C:** Temel sorunlar:
- Sonsuz özyineleme — her zaman temel durumu ilk sıraya koyun
- İstenmeyen geri izleme — kesme`!`veya`once/1`kullanın 
- Oluşma kontrolü — varsayılan olarak`X = f(X)`döngüleri (`unify_with_occurs_check` kullanın)
- Yeşil kesimler (optimizasyon) ve kırmızı kesimler (anlamını değiştir) — yeşili tercih et
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: N-Queens Bulmacasını Çözmek
**1. Adım: Sorunu Anlayın**
NxN satranç tahtasına N vezir yerleştirin, böylece iki vezir birbirine saldıramaz.
**2. Adım: Yaklaşımı Belirleyin**
Kısıtlamaya dayalı oluşturmayı kullanın: güvenliği kontrol ederek kraliçeleri sütun sütun yerleştirin.
**3. Adım: Uygulama**```prolog
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

**4. Adım: Doğrulayın**
`?- n_queens(8, Qs).`92 çözüm bulmalıdır.
### Sorun 2: Basit Bir Uzman Sistem Oluşturmak
**1. Adım: Sorunu Anlayın**
Belirtilere göre araba sorunlarını teşhis edin.
**2. Adım: Yaklaşımı Belirleyin**
Tanılama bilgisini kodlamak için Prolog kurallarını kullanın.
**3. Adım: Uygulama**```prolog
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

**4. Adım: Genişletin**
Güven puanları ekleyin, kullanıcıdan etkileşimli olarak semptomları isteyin ve teşhisleri zincirleyin.
---

## Özet
Prolog diğer programlama dillerine benzemez. Adım adım talimatlar yazmak yerine ilişkileri ve kısıtlamaları tanımlarsınız ve motor, mantıksal çıkarım yoluyla çözümler arar. Bu, Prolog'u zorunlu dillerde karmaşık veya ayrıntılı olan problemler için ideal kılar: uzman sistemler, zamanlama, dilbilgisi ayrıştırma, kısıtlama tatmini ve mantıksal kuralları içeren her şey. Çoğu programcı Prolog'u asla üretimde kullanmaz, ancak onu öğrenmek programlamanın ne olabileceğine dair düşüncelerinizi genişletir. Birleştirme, geri izleme ve bildirimsel sorun belirleme, dil tasarımını, yapay zeka araştırmasını ve hatta veritabanı sorgu optimizasyonunu etkileyen kavramlardır.
### Prolog Motorları Karşılaştırması
| Özellik | SWI-Prolog | GNU Giriş | Tau Giriş |
|-----------|-----------|------------|------------|
| **Lisans** | BSD (açık kaynak) | GPL (açık kaynak) | BSD (açık kaynak) |
| **Platform** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (tarayıcı) |
| **CLP(FD)** | Dahili kütüphane | Dahili | Mevcut değil |
| **DCG desteği** | Tam | Tam | Sınırlı |
| **Tablolama** | Evet | Hayır | Hayır |
| **FFI (C çağrıları)** | Evet | Evet | JavaScript aracılığıyla |
| **Ağ oluşturma** | HTTP, TCP, TLS | TCP | JavaScript aracılığıyla |
| **Çoklu iş parçacığı** | Evet | Hayır | Hayır |
| **Paket yöneticisi** | `pack_install/1`| Yok | npm |
| **En iyisi** | Üretim, araştırma | Kısıtlama çözme | Web uygulamaları, eğitim |
### Pengines ile Web Uygulamaları
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

### İddia/geri çekme ile metaprogramlama
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
