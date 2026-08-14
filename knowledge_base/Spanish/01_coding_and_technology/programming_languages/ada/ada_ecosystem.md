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

# Ada — Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, bibliotecas e infraestructura esenciales en el ecosistema de Ada.
---

## Compiladores e implementaciones
| Compilador | Tipo | Notas |
|----------|------|-------|
| **GNAT** | Código abierto | Basado en GCC, el más utilizado |
| **Comunidad GNAT** | Gratis | Edición gratuita de AdaCore |
| **GNAT Pro** | Comercial | Certificado de seguridad, AdaCore |
| **ObjetoAda** | Comercial | Ventanas, críticas para la seguridad |
| **Jano/Ada** | Comercial | Sistemas integrados |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Creación de sistemas y gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **Alire** | Administrador de paquetes moderno (recomendado) |
| **Construcción GPR** | Herramienta de construcción de proyectos |
| **GPR (Proyecto GNAT)** | Formato de archivo del proyecto |
| **Hacer** | Construcciones clásicas |
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

## Seguridad y verificación
| Herramienta | Propósito |
|------|---------|
| **GNATprove** | Verificación formal |
| **CHISPA** | Subconjunto crítico para la seguridad |
| **CodePeer** | Análisis estático |
| **Poliespacio** | Verificación en tiempo de ejecución |
| **Cobertura** | Análisis estático |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **UNidad** | Marco de pruebas unitarias |
| **Ahven** | Pruebas sencillas |
| **Prueba GNAT** | Pruebas basadas en código |
| **gprbuild** | Construir y probar |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Ada.Contenedores** | Vectores, mapas, conjuntos |
| **Ada.Strings** | Manejo de cuerdas |
| **Ada.Text_IO** | E/S de consola |
| **Ada.Calendario** | Fecha/hora |
| **GNATcoll** | Utilidades GNAT |
| **AWS** | Servidor Web Ada |
| **XML/Ada** | Análisis XML |
| **GID** | Decodificación de imágenes |
| **SDLAda** | Enlaces SDL2 |
| **GLFW** | Ventanas OpenGL |
| **Tiempo de ejecución de Cortex GNAT** | Integrado (ARM) |
---

## Simultaneidad
| Característica | Propósito |
|---------|---------|
| **Tareas** | Hilos concurrentes |
| **Objetos protegidos** | Datos sincronizados |
| **Seleccionar declaraciones** | Cita |
| **Llamadas de entrada** | Sincronización |
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

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **GPS (Estudio de programación GNAT)** | IDE de AdaCore |
| **Código VS + Ada** | Soporte de idioma Ada |
| **Emacs + modo ada** | Entorno clásico de Ada |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Binario estático** | GNAT produce binarios estáticos |
| **Compilación cruzada** | Compilación cruzada de GNAT |
| **Integrado** | Metal desnudo, RTOS (Ravenscar) |
| **Acoplador** | En contenedores |
| **Certificación de seguridad** | DO-178C, IEC 61508, Criterios comunes |
---

## Resumen
El ecosistema de Ada está diseñado específicamente para sistemas críticos para la seguridad y de alta confiabilidad. La cadena de herramientas estándar es: **GNAT** (basada en GCC) para compilación, **Alire** para administración de paquetes, **GPRbuild** para compilaciones, **GNATprove** y **SPARK** para verificación formal y **AUnit** para pruebas. Ada sobresale en el sector aeroespacial (DO-178C), defensa, ferrocarriles, dispositivos médicos y cualquier ámbito donde la corrección sea primordial. Los puntos fuertes de Ada son la tipificación sólida, la concurrencia (tareas, objetos protegidos), la verificación formal (SPARK) y la certificación de seguridad. El ecosistema es esencial para los sistemas integrados críticos para la seguridad.