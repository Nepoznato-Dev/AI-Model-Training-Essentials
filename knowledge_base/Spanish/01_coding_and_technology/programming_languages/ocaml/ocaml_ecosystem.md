---
# Metadata
title: "OCaml — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the OCaml ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# OCaml: Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema OCaml.
---

## Implementaciones de OCaml
| Implementación | Notas |
|---------------|-------|
| **OCaml 5** | Actual, con efectos y paralelismo |
| **OCaml 4.14** | Último 4.x (ampliamente utilizado) |
| **Razón** | Sintaxis alternativa (Facebook) |
| **Reescribir** | Sucesor de Modern Reason (BuckleScript) |
| **OCaml nativo** | Compilado en código nativo |
| **js_of_ocaml** | Compilar en JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Herramientas de compilación y gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **Duna** | Sistema de construcción (estándar) |
| **opam** | Administrador de paquetes |
| **ocamlfind** | Buscador de bibliotecas |
| **proyecto-duna** | Configuración del proyecto |
| **fácil** | Administrador de paquetes alternativo |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Sueño** | Pila completa | Web moderna (inspirada en Express) |
| **Cohttp** | HTTP | Cliente/servidor HTTP |
| **Opio** | Ligero | Al estilo de Sinatra |
| **Ocsigen** | Pila completa | Eliom (cliente-servidor) |
| **Transformación** | Ligero | Marco web |
| **Peso** | Asíncrono | Roscado cooperativo |
| **Asíncrono** | Asíncrono | Asíncrono de Jane Street |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **Caqtí** | Base de datos con seguridad de tipos |
| **PG'OCaml** | PostgreSQL (tipo seguro) |
| **sqlite3-ocaml** | Enlaces SQLite |
| **mysql-ocaml** | Enlaces MySQL |
| **postgresql-ocaml** | Enlaces de PostgreSQL |
| **Irmin** | Base de datos tipo Git |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Alcotest** | Pruebas rápidas y coloridas |
| **Unidad** | Pruebas unitarias (estilo xUnit) |
| **QCheck** | Pruebas basadas en propiedades |
| **Palanca** | Pruebas de fuzz |
| **ppx_expect** | Espere pruebas (Jane Street) |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **formato ocaml** | Formato de código |
| **ocp-sangría** | Sangría |
| **ocaml-lsp** | Servidor de idiomas |
| **ppx** | Extensiones de sintaxis |
| **esmerejón** | Soporte IDE (compleciones, tipos) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Núcleo/Base** | Biblioteca estándar de Jane Street |
| **Stdlib** | Biblioteca estándar OCaml |
| **Resultado** | Manejo de errores |
| **Contenedores** | Estructuras de datos |
| **Baterías** | Biblioteca estándar ampliada |
| **Peso** | Hilos ligeros |
| **Asíncrono** | Programación asíncrona |
| **Eio** | E/S basada en efectos (OCaml 5) |
| **Dominio** | Paralelismo (OCaml 5) |
| **ppx_derivando** | Derivar funciones |
| **ppx_yojson_conv** | Derivación JSON |
| **yojson** | Análisis JSON |
| **angstrom** | Combinadores de analizadores |
| **menhir** | Generador de analizador |
| **ocamlgraph** | Biblioteca de gráficos |
| **Zarit** | Precisión arbitraria |
| **Unidad** | Pruebas |
---

## Métodos formales
| Herramienta | Propósito |
|------|---------|
| **Coq** | Asistente de prueba (escrito en OCaml) |
| **Por qué3** | Verificación del programa |
| **Alt-Ergo** | Solucionador SMT |
| **OCaml + pruebas** | Programas verificados |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + plataforma ocaml** | Mejor LSP de OCaml |
| **Emacs + tuareg + merlín** | Entorno OCaml clásico |
| **Vim + Merlín** | Integración Vim |
| **Neovim + ocaml-lsp** | Basado en terminal |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Binario nativo** | `dune build`produce binarios nativos |
| **Enlace estático** | Binarios completamente estáticos |
| **Acoplador** | En contenedores |
| **interruptor opam** | Múltiples versiones de OCaml |
| **Compilación cruzada** | Compilación cruzada |
---

## Resumen
El ecosistema de OCaml se centra en la corrección, el rendimiento y la programación funcional. La pila estándar es: **OCaml 5** como tiempo de ejecución, **Dune** para compilaciones, **opam** para paquetes, **Dream** o **Cohttp** para web, **Caqti** para bases de datos, **Alcotest** para pruebas, **ocamlformat** para formatear y **Merlin** para compatibilidad con IDE. OCaml se destaca en compiladores, verificación formal, sistemas financieros y en cualquier lugar donde la corrección y el rendimiento sean importantes. El sistema de efectos y el paralelismo (Dominios) de OCaml 5 aportan simultaneidad moderna al lenguaje. El ecosistema es esencial para crear compiladores (Coq, F*), demostradores de teoremas y software de alta seguridad.