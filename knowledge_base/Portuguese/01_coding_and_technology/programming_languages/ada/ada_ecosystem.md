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

# Ada — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, bibliotecas e infraestrutura essenciais do ecossistema Ada.
---

## Compiladores e Implementações
| Compilador | Tipo | Notas |
|----------|------|-------|
| **GNAT** | Código aberto | Baseado em GCC, mais utilizado |
| **Comunidade GNAT** | Grátis | Edição gratuita do AdaCore |
| **GNAT Pro** | Comercial | Certificado de segurança, AdaCore |
| **ObjectAda** | Comercial | Janelas essenciais para a segurança |
| **Janus/Ada** | Comercial | Sistemas embarcados |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Construir sistemas e gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **Alire** | Gerenciador de pacotes moderno (recomendado) |
| **GPRbuild** | Ferramenta de construção de projeto |
| **GPR (Projeto GNAT)** | Formato do arquivo do projeto |
| **Fazer** | Construções clássicas |
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

## Segurança e Verificação
| Ferramenta | Finalidade |
|------|---------|
| **GNATprova** | Verificação formal |
| **FAÍSCA** | Subconjunto crítico para a segurança |
| **CodePeer** | Análise estática |
| **Poliespaço** | Verificação de tempo de execução |
| **Cobertura** | Análise estática |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **Unidade** | Estrutura de testes unitários |
| **Ahven** | Teste simples |
| **GNATteste** | Teste baseado em código |
| **gprbuild** | Construir e testar |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Ada.Containers** | Vetores, mapas, conjuntos |
| **Ada.Strings** | Manipulação de strings |
| **Ada.Text_IO** | E/S do console |
| **Ada.Calendário** | Data/hora |
| **GNATcoll** | Utilitários GNAT |
| **AWS** | Servidor Web Ada |
| **XML/ADA** | Análise XML |
| **GID** | Decodificação de imagem |
| **SDLAda** | Ligações SDL2 |
| **GLFW** | Janelas OpenGL |
| **Tempo de execução do Cortex GNAT** | Incorporado (ARM) |
---

## Simultaneidade
| Recurso | Finalidade |
|--------|---------|
| **Tarefas** | Threads simultâneos |
| **Objetos Protegidos** | Dados sincronizados |
| **Selecionar declarações** | Encontro |
| **Chamadas de entrada** | Sincronização |
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

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **GPS (Estúdio de Programação GNAT)** | IDE da AdaCore |
| **Código VS + Ada** | Suporte ao idioma Ada |
| **Emacs + modo ada** | Ambiente Ada clássico |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Binário estático** | GNAT produz binários estáticos |
| **Compilação cruzada** | Compilação cruzada GNAT |
| **Incorporado** | Bare-metal, RTOS (Ravenscar) |
| **Docker** | Contentorizado |
| **Certificação de segurança** | DO-178C, IEC 61508, Critérios Comuns |
---

## Resumo
O ecossistema da Ada foi desenvolvido especificamente para sistemas críticos de segurança e de alta confiabilidade. O conjunto de ferramentas padrão é: **GNAT** (baseado em GCC) para compilação, **Alire** para gerenciamento de pacotes, **GPRbuild** para compilações, **GNATprove** e **SPARK** para verificação formal e **AUnit** para testes. Ada é excelente em aeroespacial (DO-178C), defesa, ferrovia, dispositivos médicos e qualquer domínio onde a correção seja fundamental. Os pontos fortes de Ada são digitação forte, simultaneidade (tarefas, objetos protegidos), verificação formal (SPARK) e certificação de segurança. O ecossistema é essencial para sistemas embarcados críticos para a segurança.