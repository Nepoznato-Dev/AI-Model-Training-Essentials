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
# OCaml — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème OCaml.
---

## Implémentations OCaml
| Mise en œuvre | Remarques |
|---------------|-------|
| **OCaml 5** | Actuel, avec effets et parallélisme |
| **OCaml 4.14** | Dernière 4.x (largement utilisée) |
| **Raison** | Syntaxe alternative (Facebook) |
| **Rescript** | Successeur de Modern Reason (BuckleScript) |
| **OCaml natif** | Compilé en code natif |
| **js_of_ocaml** | Compiler en JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Outils de création et gestion des packages
| Outil | Objectif |
|------|--------------|
| **Dune** | Système de construction (standard) |
| **opam** | Gestionnaire de paquets |
| **ocamlfind** | Recherche de bibliothèque |
| **projet-dune** | Configuration du projet |
| **esy** | Gestionnaire de paquets alternatif |
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

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **Rêve** | Pile complète | Web moderne (inspiré d'Express) |
| **Cohttp** | HTTP | Client/serveur HTTP |
| **Opium** | Léger | À la manière de Sinatra |
| **Ocsigène** | Pile complète | Eliom (client-serveur) |
| **Morph** | Léger | Cadre Web |
| **Lwt** | Asynchrone | Enfilage coopératif |
| **Asynchrone** | Asynchrone | Asynchrone de Jane Street |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **Caqti** | Base de données de type sécurisé |
| **PG'OCaml** | PostgreSQL (type sécurisé) |
| **sqlite3-ocaml** | Liaisons SQLite |
| **mysql-ocaml** | Liaisons MySQL |
| **postgresql-ocaml** | Liaisons PostgreSQL |
| **Irmin** | Base de données de type Git |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **Alcotest** | Tests rapides et colorés |
| **Unité** | Tests unitaires (style xUnit) |
| **QVérifiez** | Tests basés sur les propriétés |
| **Pied de biche** | Test de fuzz |
| **ppx_expect** | Attendez-vous à des tests (Jane Street) |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **formatocaml** | Formatage des codes |
| **ocp-indent** | Indentation |
| **ocaml-lsp** | Serveur de langue |
| **ppx** | Extensions de syntaxe |
| **merlin** | Prise en charge de l'IDE (complétions, types) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Noyau / Base** | Bibliothèque standard de Jane Street |
| **Stdlib** | Bibliothèque standard OCaml |
| **Résultat** | Gestion des erreurs |
| **Conteneurs** | Structures de données |
| **Batteries** | Bibliothèque standard étendue |
| **Lwt** | Fils légers |
| **Asynchrone** | Programmation asynchrone |
| **Eio** | E/S basées sur les effets (OCaml 5) |
| **Domaine** | Parallélisme (OCaml 5) |
| **ppx_deriving** | Dériver des fonctions |
| **ppx_yojson_conv** | Dérivation JSON |
| **yojson** | Analyse JSON |
| **angström** | Combinateurs d'analyseurs |
| **menhir** | Générateur d'analyseur |
| **ocamlgraphe** | Bibliothèque de graphiques |
| **Zarith** | Précision arbitraire |
| **Unité** | Tests |
---

## Méthodes formelles
| Outil | Objectif |
|------|--------------|
| **Coq** | Assistant de preuve (écrit en OCaml) |
| **Pourquoi3** | Vérification du programme |
| **Alt-Ergo** | Solveur SMT |
| **OCaml + preuves** | Programmes vérifiés |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **VS Code + plateforme ocaml** | Meilleur LSP OCaml |
| **Emacs + touareg + merlin** | Environnement OCaml classique |
| **Vim + Merlin** | Intégration Vim |
| **Neovim + ocaml-lsp** | Basé sur un terminal |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Binaire natif** | `dune build`produit des binaires natifs |
| **Lien statique** | Binaires entièrement statiques |
| **Docker** | Conteneurisé |
| **commutateur opam** | Plusieurs versions d'OCaml |
| **Compilation croisée** | Compilation croisée |
---

## Résumé
L'écosystème d'OCaml est centré sur l'exactitude, les performances et la programmation fonctionnelle. La pile standard est : **OCaml 5** pour le runtime, **Dune** pour les builds, **opam** pour les packages, **Dream** ou **Cohttp** pour le Web, **Caqti** pour les bases de données, **Alcotest** pour les tests, **ocamlformat** pour le formatage et **Merlin** pour la prise en charge de l'IDE. OCaml excelle dans les compilateurs, la vérification formelle, les systèmes financiers et partout où l'exactitude et la performance comptent. Le système d'effets et le parallélisme (domaines) d'OCaml 5 apportent une concurrence moderne au langage. L'écosystème est essentiel pour créer des compilateurs (Coq, F*), des prouveurs de théorèmes et des logiciels à haute assurance.