---
# Metadata
title: "Prolog"
description: "Comprehensive reference for the Prolog programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Prólogo
Prolog (Programação em Lógica) é uma linguagem de programação lógica criada em 1972 por Alain Colmerauer e Philippe Roussel. Ao contrário de todas as outras linguagens desta lista, o Prolog não diz ao computador *como* resolver um problema - você declara *o que* é verdadeiro (fatos e regras), e o mecanismo de inferência do Prolog descobre a resposta por meio de dedução lógica.
Prolog foi a linguagem escolhida para sistemas especialistas, processamento de linguagem natural e pesquisa de IA na década de 1980. Ele impulsionou o projeto de sistema de computador de quinta geração do Japão e foi usado no Watson da IBM para compreensão de linguagem natural. Hoje, o Prolog é usado na resolução de restrições, agendamento, inferência de tipos, raciocínio jurídico e em qualquer lugar que os problemas sejam naturalmente expressos como relacionamentos lógicos.
**Programação Lógica de Restrições (CLP)** estende o Prolog com solucionadores de restrições para agendamento, roteamento e alocação de recursos — problemas que são extremamente difíceis em linguagens imperativas.
---

## Por que o Prolog é importante
- **Programação declarativa**: Descreva o que é verdade, não como calculá-lo. O motor faz o trabalho.
- **Correspondência e unificação de padrões**: O algoritmo de unificação do Prolog é mais poderoso do que a correspondência de padrões em outras linguagens.
- **Pesquisa de retrocesso**: explora automaticamente todas as soluções possíveis. Não são necessários algoritmos de pesquisa manual.
- **Natural para problemas lógicos**: Sistemas especialistas, mecanismos de regras, verificadores de tipo, analisadores gramaticais — estes são mapeados diretamente para o Prolog.
- **Solução de restrições**: CLP(FD) resolve problemas de programação, alocação e combinatórios com elegância.
- **Pensamento diferente**: Aprender Prolog muda a forma como você aborda a resolução de problemas – você começa a pensar em relacionamentos e restrições.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Paradigma muito diferente** | Sem variáveis ​​(apenas ligações), sem loops, sem atribuições | Pense em relações e recursividade, não em mudanças de estado |
| **Desempenho** | Lento para computação numérica e grandes volumes de dados | Use para raciocínio; delegar computação para C/outras linguagens |
| **Dificuldade de depuração** | Falhas de retrocesso e unificação difíceis de rastrear | Use ferramentas de rastreamento/depuração; escrever predicados determinísticos |
| **Operador de corte (!)** | Necessário para eficiência, mas quebra a pureza lógica | Use avaliação if-then-else ou tabelada quando possível |
| **Ecossistema limitado** | Poucas bibliotecas, estruturas ou recursos comunitários | SWI-Prolog é a implementação mais completa |
| **Não para aplicativos gerais** | Web, dispositivos móveis, GUI — não o ponto forte do Prolog | Use como mecanismo de raciocínio por trás de um aplicativo da web |
---

## Fundamentos de sintaxe
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

## Sintaxe e padrões avançados
### Aprofundamento da Unificação
A unificação é o mecanismo central do Prolog - é como o Prolog "combina" os termos e vincula as variáveis.
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

### Retrocesso e pontos de escolha
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

### Gramáticas de Cláusulas Definidas (DCGs)
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

### Programação Lógica de Restrições (CLP)
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

## Arquitetura e Design de Sistema
### Paradigma de Programação Lógica
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

### Estrutura Típica de Projeto
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

### Sistema de Módulo
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

## Configuração do projeto e sistema de construção
### Configuração SWI-Prolog
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

### Executando programas Prolog
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

### Configuração de compilação
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

## Teste e depuração
### Rastreamento integrado
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

### Teste unitário com PLUnit
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

### Padrões comuns de depuração
| Problema | Sintoma | Solução |
|--------|---------|----------|
| Recursão infinita | Estouro de pilha | Verifique o caso base; adicionar condição de rescisão |
| Sem soluções | Consulta retorna falso | Verifique a ordem de instanciação de variáveis ​​|
| Muitas soluções | Duplicatas inesperadas | Adicione corte (!) ou use`setof`|
| Unificação errada | Variáveis ​​vinculadas incorretamente | Use`=`para testar; verifique a aridade do functor |
| Problema de desempenho | Execução lenta | Adicione cortes; use `table`; verifique os pontos de escolha |
---

## Interoperabilidade
### Interface C (FFI)
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

### Integração Python
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

## Padrões de Projeto
### Padrão 1: Acumulador (recursão de cauda)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Padrão 2: Threading de estado```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Padrão 3: gerar e testar```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Padrão 4: Listas de Diferenças```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Desempenho e otimização
### Otimização de corte
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Recursão de cauda
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Lista de verificação de otimização
| Técnica | Impacto | Descrição |
|-----------|--------|-------------|
| **Recursão de cauda** | Alto | Use acumuladores para espaço de pilha constante |
| **Corte (verde)** | Alto | Elimine pontos de escolha desnecessários |
| **Avaliação tabelada** | Alto | `:- table pred/N`memoiza resultados |
| **Indexação** | Médio | Coloque o argumento discriminatório em primeiro lugar |
| **Listas de diferenças** | Médio | O(1) concatenação de lista |
| **CLP(FD) sobre teste de geração** | Muito alto | Use restrições em vez de força bruta |
---

## Implantação e uso no mundo real
### Implantando aplicativos Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Aplicações do mundo real
| Domínio | Como o Prolog é usado | Exemplo |
|----|-------------------|-----|
| **Sistemas especialistas** | Diagnóstico médico, detecção de falhas | MYCIN, XCON |
| **PNL** | Análise gramatical, análise semântica | Chatbots, sistemas de controle de qualidade |
| **Inferência de tipo** | Verificação de tipo Hindley-Milner | Protótipos Haskell/ML |
| **Agendamento** | Agendamento de funcionários, cronograma | Agendamento de tripulantes de companhias aéreas |
| **Raciocínio jurídico** | Análise jurídica baseada em regras | Verificação de conformidade |
| **Consulta de banco de dados** | Registro de dados para análise de dados | Motor suflê |
| **Verificação** | Verificação de modelo | Verificação de hardware |
| **IBM Watson** | Compreensão da linguagem natural | Perigo! sistema |
| **Ericsson** | Gestão de telecomunicações | Validação de configuração de rede |
---

## Quando usar o Prolog
| Cenário | Por que Prolog | Melhor Alternativa |
|----------|-----------|-------------------|
| Raciocínio baseado em regras | Prolog foi criado para isso | Mecanismos de regras personalizadas em Python/Java |
| Satisfação das restrições | CLP(FD) é elegante e eficiente | Solucionadores SAT, ferramentas OR para grandes instâncias |
| Análise gramatical/linguística | DCG (Gramáticas de Cláusula Definida) são nativas | Geradores de analisador (ANTLR, yacc) para produção |
| Sistemas especialistas | Ajuste natural — fatos + regras = sistema especialista | Mecanismos de regras de negócios (Drools) |
| Agendamento/calendário | CLP resolve bem isso | Ferramentas OR, OptaPlanner |
| Pesquisa de sistema de tipo | A unificação é a base | Implementar em OCaml, Haskell, Rust |
| Aplicações Web | Não adequado | Python, Node.js, Go |
| Ciência de dados / ML | Não o ecossistema | Pitão, R |
| Código crítico para desempenho | Prolog é lento para computação | C, C++, Ferrugem |
| Programação de uso geral | Possível, mas estranho | Python, Go, Java |
---

## Resumo
Prolog é diferente de qualquer outra linguagem de programação. Em vez de escrever instruções passo a passo, você descreve relacionamentos e restrições — e o mecanismo procura soluções por meio de inferência lógica. Isso torna o Prolog ideal para problemas complicados ou detalhados em linguagens imperativas: sistemas especialistas, escalonamento, análise gramatical, satisfação de restrições e qualquer coisa que envolva regras lógicas. A maioria dos programadores nunca usará o Prolog em produção, mas aprendê-lo expande seu pensamento sobre o que a programação pode ser. Unificação, retrocesso e especificação declarativa de problemas são conceitos que influenciam o design da linguagem, a pesquisa de IA e até mesmo a otimização de consultas de banco de dados.
### Comparação de motores Prolog
| Recurso | SWI-Prolog | Prólogo GNU | Tau Prólogo |
|---------|-----------|------------|------------|
| **Licença** | BSD (código aberto) | GPL (código aberto) | BSD (código aberto) |
| **Plataforma** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (navegador) |
| **CLP(FD)** | Biblioteca integrada | Integrado | Não disponível |
| **Suporte DCG** | Completo | Completo | Limitado |
| **Tabelas** | Sim | Não | Não |
| **FFI (chamadas C)** | Sim | Sim | Via JavaScript |
| **Rede** | HTTP, TCP, TLS | TCP | Via JavaScript |
| **Multithreading** | Sim | Não | Não |
| **Gerenciador de pacotes** | `pack_install/1`| Nenhum | npm |
| **Melhor para** | Produção, pesquisa | Resolução de restrições | Aplicativos web, educação |
### Aplicações Web com Pengines
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

### Metaprogramação com afirmação/retração
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
