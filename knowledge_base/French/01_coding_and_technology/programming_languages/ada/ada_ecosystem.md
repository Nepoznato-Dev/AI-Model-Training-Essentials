---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ada, ecosystem, tooling, compilers, safety-critical, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ada — Guide de l'écosystème et des outils
Ce guide couvre les outils, bibliothèques et infrastructures essentiels de l'écosystème Ada.
---

## Compilateurs et implémentations
| Compilateur | Tapez | Remarques |
|--------------|------|-------|
| **GNAT** | Open source | Basé sur GCC, le plus largement utilisé |
| **Communauté GNAT** | Gratuit | L'édition gratuite d'AdaCore |
| **GNAT Pro** | Commerciale | Certifié de sécurité, AdaCore |
| **ObjectAda** | Commerciale | Fenêtres, critiques pour la sécurité |
| **Janus/Ada** | Commerciale | Systèmes embarqués |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Systèmes de construction et gestion des packages
| Outil | Objectif |
|------|--------------|
| **Alire** | Gestionnaire de paquets moderne (recommandé) |
| **GPRbuild** | Outil de création de projet |
| **GPR (Projet GNAT)** | Format de fichier de projet |
| **Faire** | Constructions classiques |
```toml
# alire.toml
name = "myapp"
description = "My Ada application"
version = "0.1.0"

[[depends-on]]
gnat = "^13"
gnatcoll = "^24"

[[pins]]
```

```bash
alr init --bin myapp      # create project
alr build                 # build
alr run                   # run
alr get --build gnatcoll  # get dependency
alr search                # search packages
alr index                 # update index
```

```gpr
-- myproject.gpr
project Myproject is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Main use ("main.adb");
   
   package Compiler is
      for Default_Switches ("Ada") use ("-gnatwa", "-gnatVa", "-O2");
   end Compiler;
   
   package Binder is
      for Default_Switches ("Ada") use ("-E");  -- store exceptions
   end Binder;
end Myproject;
```

---

## Sécurité et vérification
| Outil | Objectif |
|------|--------------|
| **GNATprove** | Vérification formelle |
| **ÉTINCELLE** | Sous-ensemble critique pour la sécurité |
| **CodePeer** | Analyse statique |
| **Polyespace** | Vérification de l'exécution |
| **Couverture** | Analyse statique |
```ada
-- SPARK example
package Stack with
   SPARK_Mode
is
   type Bounded_Stack (Capacity : Positive) is tagged private;
   
   procedure Push (S : in out Bounded_Stack; Element : Integer)
      with Pre  => not S.Is_Full,
           Post => not S.Is_Empty and S.Top = Element;
   
   function Is_Full (S : Bounded_Stack) return Boolean;
   function Is_Empty (S : Bounded_Stack) return Boolean;
   
private
   type Bounded_Stack (Capacity : Positive) is tagged record
      Data : array (1 .. Capacity) of Integer;
      Top_Index : Natural := 0;
   end record;
end Stack;
```

---

## Tests
| Cadre | Objectif |
|-----------|---------|
| **UNEUnité** | Cadre de tests unitaires |
| **Ahven** | Tests simples |
| **GNATtest** | Tests basés sur le code |
| **gprbuild** | Construire et tester |
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Stack_Test is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;
   
   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Stack_Test;

package body Stack_Test is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("Stack Tests");
   end Name;
   
   procedure Run_Test (T : in out Test_Case) is
      S : Bounded_Stack (10);
   begin
      Push (S, 42);
      AUnit.Assertions.Assert (Top (S) = 42, "Top should be 42");
      AUnit.Assertions.Assert (not Is_Empty (S), "Should not be empty");
   end Run_Test;
end Stack_Test;
```

---

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Ada.Conteneurs** | Vecteurs, cartes, ensembles |
| **Ada.Strings** | Gestion des chaînes |
| **Ada.Text_IO** | E/S de la console |
| **Ada.Calendrier** | Date/heure |
| **GNATcoll** | Utilitaires GNAT |
| **AWS** | Serveur Web Ada |
| **XML/Ada** | Analyse XML |
| **GID** | Décodage d'images |
| **SDLAda** | Liaisons SDL2 |
| **GLFW** | Fenêtrage OpenGL |
| **Exécution Cortex GNAT** | Intégré (ARM) |
---

## Concurrence
| Fonctionnalité | Objectif |
|---------|---------|
| **Tâches** | Discussions simultanées |
| **Objets protégés** | Données synchronisées |
| **Sélectionnez les déclarations** | Rendez-vous |
| **Appels d'entrée** | Synchronisation |
```ada
task type Worker is
   entry Do_Work (Item : in Integer);
end Worker;

task body Worker is
   Value : Integer;
begin
   loop
      select
         accept Do_Work (Item : in Integer) do
            Value := Item;
         end Do_Work;
         Process (Value);
      or
         terminate;
      end select;
   end loop;
end Worker;
```

---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **GPS (Studio de programmation GNAT)** | L'EDI d'AdaCore |
| **Code VS + Ada** | Prise en charge de la langue Ada |
| **Emacs + mode ada** | Environnement Ada classique |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Binaire statique** | GNAT produit des binaires statiques |
| **Compilation croisée** | Compilation croisée GNAT |
| **Intégré** | Bare-metal, RTOS (Ravenscar) |
| **Docker** | Conteneurisé |
| **Certification de sécurité** | DO-178C, CEI 61508, Critères communs |
---

## Résumé
L'écosystème d'Ada est spécialement conçu pour les systèmes critiques en matière de sécurité et de haute fiabilité. La chaîne d'outils standard est : **GNAT** (basé sur GCC) pour la compilation, **Alire** pour la gestion des packages, **GPRbuild** pour les builds, **GNATprove** et **SPARK** pour la vérification formelle et **AUnit** pour les tests. Ada excelle dans l'aérospatiale (DO-178C), la défense, les chemins de fer, les dispositifs médicaux et tout domaine où l'exactitude est primordiale. Les points forts d'Ada sont le typage fort, la simultanéité (tâches, objets protégés), la vérification formelle (SPARK) et la certification de sécurité. L’écosystème est essentiel pour les systèmes embarqués critiques pour la sécurité.