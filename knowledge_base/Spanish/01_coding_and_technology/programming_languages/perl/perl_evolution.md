---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [perl, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Perl: historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| 1.0 | 1987 | Lanzamiento inicial (Larry Wall) |
| 2.0 | 1988 |  Función `study`, mejor expresión regular |
| 3.0 | 1989 |  Variables`my`(alcance léxico) |
| 4.0 | 1991 | `O'Reilly`"Programación Perl" (libro Camel) |
| 5.0 | 1994 | **Principal**: módulos, referencias, cierres,`use strict`|
| 5.6 | 2000 |  Correcciones `our`,`state`(posterior), `v-strings`,`y2k`|
| 5.8 | 2002 | **Soporte Unicode**, `ithreads`,`open`pragma |
| 5.10 | 2007 |  `say`,`//`definido o,`given`/ `when`,`~~`smartmatch |
| 5.12 | 2010 |  `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(sustitución no destructiva), mejoras`package`|
| 5.16 | 2012 |  `__SUB__`,`unicode_eval`|
| 5.18 | 2013 |`$_`léxico, aleatorización hash,`my`en condicionales |
| 5.20 | 2014 | **Firmas de subrutina** (experimental), corte`%hash`|
| 5.22 | 2015 |  Desreferenciación `&`,`<<>>`(apertura segura) |
| 5.24 | 2016 | Postfix desreferenciación estable |
| 5.26 | 2017 | **`$_` léxico en`while`**,`.`en`@INC`eliminado (seguridad) |
| 5.28 | 2018 | Unicode 10.0,`delete`en sectores clave/valor |
| 5.30 | 2019 | `my`en condiciones`for`/`while`|
| 5.32 | 2020 |  Operador `isa`, Unicode 13.0 |
| 5.34 | 2021 |  Bloques`try`/`catch`(experimentales),`defer`|
| 5.36 | 2022 | **`use v5.36`**: firmas habilitadas,`$_`predeterminado,`defer`|
| 5.38 | 2023 |  Palabra clave`class`(experimental),`try`/`catch`estable |
| 5.40 | 2024 |  Operadores bit a bit `^`, mejoras en la lista`for`|
| 5.42 | 2025 | Desarrollo continuo |
## Hitos importantes
### Perl 1–4: La era de las secuencias de comandos (1987–1993)
- **1987**: Larry Wall lanza Perl — "Lenguaje práctico de extracción e informes"
- **Objetivo**: combinar sed, awk, grep y shell en una poderosa herramienta de secuencias de comandos
- **3.0**: alcance léxico (`my`)
- **4.0**: The Camel Book: Perl se adopta ampliamente para tareas de administrador de sistemas
### Perl 5: La edad de oro (1994-2019)
- **5.0 (1994)**: Reescritura completa: **módulos**, **referencias**, **cierres**, **objetos**
- **5.6 (2000)**: `our`, cuerdas en v
- **5.8 (2002)**: **Soporte Unicode**, subprocesos de intérprete (`ithreads`)
- **5.10 (2007)**: `say`,`//`(definido o),`given`/`when`(cambiar), smartmatch
- **5.12–5.28**: mejoras incrementales, actualizaciones de Unicode
### Perl moderno (2020-presente)
- **5.32 (2020)**: Operador`isa`(verificación del tipo de limpiador)
- **5.34 (2021)**: bloques`try`/`catch`(experimental), `defer`
- **5.36 (2022)**: **`use v5.36`** — firmas habilitadas de forma predeterminada,`$_`predeterminada,`defer`
- **5.38 (2023)**: palabra clave`class`(experimental: programación orientada a objetos incorporada),`try`/`catch`estable
- **5.40 (2024)**: mejoras en el operador bit a bit
## Evolución de la sintaxis
```perl
# Perl 1-4: Basic scripting
#!/usr/bin/perl
$name = "World";
print "Hello, $name\n";

# Perl 5.0: References, closures, modules
use strict;
use warnings;
my $greeting = sub { "Hello, $_[0]" };
print $greeting->("World");

# Perl 5.8: Unicode
use utf8;
my $text = "café";

# Perl 5.10: say, defined-or
use v5.10;
say "Hello!";
my $value = $input // 'default';

# Perl 5.20: Subroutine signatures (experimental)
use experimental 'signatures';
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.36: Modern Perl
use v5.36;
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.38: class keyword (experimental)
use experimental 'class';
class Dog {
    field $name :param;
    field $breed :param;
    method bark { say "$name says Woof!" }
}
my $dog = Dog->new(name => "Rex", breed => "Lab");
```

## Ecosistema CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Principios clave de diseño
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Crecimiento del ecosistema
```
1987: Perl 1.0 — sysadmin scripting
1994: Perl 5.0 — modules, OOP, the web CGI era
1995: CPAN launched — module ecosystem
2000: Perl powers the early web (CGI scripts)
2002: Perl 5.8 — Unicode, ithreads
2005: Catalyst, Dancer — web frameworks
2007: Perl 5.10 — modern syntax additions
2010: Moose — modern OOP (meta-object protocol)
2022: Perl 5.36 — modern defaults
2025: Perl still powers sysadmin, bioinformatics, legacy web apps
       CPAN: 200,000+ modules; used by cPanel, DuckDuckGo
```
