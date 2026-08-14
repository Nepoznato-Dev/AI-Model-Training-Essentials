---
# Metadata
title: "OCaml — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the OCaml ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ocaml, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# OCaml — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema OCaml.
---

## Implementações OCaml
| Implementação | Notas |
|---------------|-------|
| **OCaml 5** | Atual, com efeitos e paralelismo |
| **OCaml 4.14** | Último 4.x (amplamente utilizado) |
| **Motivo** | Sintaxe alternativa (Facebook) |
| **ReScript** | Sucessor do Modern Reason (BuckleScript) |
| **OCaml Nativo** | Compilado para código nativo |
| **js_of_ocaml** | Compilar para JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Ferramentas de construção e gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **Duna** | Sistema de construção (padrão) |
| **opam** | Gerenciador de pacotes |
| **ocamlfind** | Localizador de biblioteca |
| **projeto duna** | Configuração do projeto |
| **esy** | Gerenciador de pacotes alternativo |
```bash
# opam
opam init                 # initialize
opam install dune         # install package
opam list                 # list installed
opam update               # update index
opam upgrade              # upgrade packages

# Create project
dune init proj myapp      # new project
dune build                # build
dune runtest              # run tests
```

```lisp
;; dune-project
(lang dune 3.12)
(name myapp)
(generate_opam_files true)

;; dune (executable)
(executable
 (public_name myapp)
 (name main)
 (libraries core async cohttp-lwt-unix))

;; dune (library)
(library
 (name mylib)
 (public_name mylib)
 (libraries core))
```

```opam
# myapp.opam
opam-version: "2.0"
synopsis: "My OCaml application"
depends: [
  "ocaml" {>= "5.0"}
  "dune" {>= "3.0"}
  "core" {>= "v0.16"}
  "async" {>= "v0.16"}
]
```

---

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Sonho** | Pilha completa | Web moderna (inspirada no Express) |
| **Cohttp** | http | Cliente/servidor HTTP |
| **Ópio** | Leve | Semelhante a Sinatra |
| **Ocsigen** | Pilha completa | Eliom (cliente-servidor) |
| **Morfa** | Leve | Estrutura web |
| **Lwt** | Assíncrono | Rosqueamento cooperativo |
| **Assíncrono** | Assíncrono | Assíncrono de Jane Street |
```ocaml
(* Dream example *)
let () =
  Dream.run
  @@ Dream.logger
  @@ Dream.router [
       Dream.get "/" (fun _ -> Dream.html "Hello, World!");
       Dream.get "/users/:id" (fun req ->
         let id = Dream.param "id" req in
         Dream.json {|{"id": "|} ^ id ^ {|"}|});
     ]
```

---

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **Caqti** | Banco de dados com segurança de tipo |
| **PG'OCaml** | PostgreSQL (tipo seguro) |
| **sqlite3-ocaml** | Ligações SQLite |
| **mysql-ocaml** | Ligações MySQL |
| **postgresql-ocaml** | Ligações PostgreSQL |
| **Irmin** | Banco de dados semelhante ao Git |
```ocaml
(* Caqti example *)
module Db = Caqti_connect_sig(S)

let find_user (module Db : Db) id =
  Db.find_opt
    (Caqti_type.(int ->! t2 int string)
       "SELECT id, name FROM users WHERE id = ?")
    id
```

---

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **Alcotest** | Testes rápidos e coloridos |
| **OUunidade** | Teste unitário (estilo xUnit) |
| **QCheck** | Testes baseados em propriedades |
| **Pé-de-cabra** | Teste de difusão |
| **ppx_expect** | Espere testes (Jane Street) |
```ocaml
(* Alcotest example *)
let test_find () =
  let service = UserService.create () in
  let user = UserService.find service 1 in
  Alcotest.(check (option string)) "found user" (Some "Alice") (Option.map User.name user)

let test_not_found () =
  let service = UserService.create () in
  let user = UserService.find service 999 in
  Alcotest.(check (option string)) "not found" None (Option.map User.name user)

let () =
  Alcotest.run "UserService" [
    "find", [
      Alcotest.test_case "finds user" `Quick test_find;
      Alcotest.test_case "not found" `Quick test_not_found;
    ];
  ]
```

---

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **formato ocaml** | Formatação de código |
| **recuo ocp** | Recuo |
| **ocaml-lsp** | Servidor de idiomas |
| **ppx** | Extensões de sintaxe |
| **merlin** | Suporte IDE (conclusões, tipos) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Núcleo/Base** | Biblioteca padrão da Jane Street |
| **Stdlib** | Biblioteca padrão OCaml |
| **Resultado** | Tratamento de erros |
| **Contêineres** | Estruturas de dados |
| **Baterias** | Biblioteca padrão estendida |
| **Lwt** | Fios leves |
| **Assíncrono** | Programação assíncrona |
| **Eio** | E/S baseada em efeitos (OCaml 5) |
| **Domínio** | Paralelismo (OCaml 5) |
| **ppx_derivando** | Derivar funções |
| **ppx_yojson_conv** | Derivação JSON |
| **yojson** | Análise JSON |
| **angstrom** | Combinadores de analisador |
| **menir** | Gerador de analisador |
| **ocamlgraph** | Biblioteca de gráficos |
| **Zarith** | Precisão arbitrária |
| **OUunidade** | Teste |
---

## Métodos Formais
| Ferramenta | Finalidade |
|------|---------|
| **Coq** | Assistente de prova (escrito por OCaml) |
| **Por que3** | Verificação do programa |
| **Alt-Ergo** | Solucionador SMT |
| **OCaml + provas** | Programas verificados |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + plataforma ocaml** | Melhor LSP OCaml |
| **Emacs + tuareg + merlin** | Ambiente OCaml clássico |
| **Vim + Merlin** | Integração Vim |
| **Neovim + ocaml-lsp** | Baseado em terminal |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Binário nativo** | `dune build`produz binários nativos |
| **Vinculação estática** | Binários totalmente estáticos |
| **Docker** | Contentorizado |
| **opam switch** | Várias versões do OCaml |
| **Compilação cruzada** | Compilação cruzada |
---

## Resumo
O ecossistema da OCaml é centrado na correção, desempenho e programação funcional. A pilha padrão é: **OCaml 5** como tempo de execução, **Dune** para compilações, **opam** para pacotes, **Dream** ou **Cohttp** para web, **Caqti** para bancos de dados, **Alcotest** para testes, **ocamlformat** para formatação e **Merlin** para suporte IDE. OCaml é excelente em compiladores, verificação formal, sistemas financeiros e em qualquer lugar que importa correção e desempenho. O sistema de efeitos e paralelismo (Domínios) do OCaml 5 trazem simultaneidade moderna para a linguagem. O ecossistema é essencial para a construção de compiladores (Coq, F*), provadores de teoremas e software de alta segurança.