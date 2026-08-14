<!--
---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [php, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# PHP: historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| PHP/FI | 1995 | Herramientas de la página de inicio personal (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | Primer PHP moderno; Reescritura de Zeev Suraski y Andi Gutmans |
| PHP 4.0 | 2000 | Zend Engine, soporte de sesión, almacenamiento en búfer de salida |
| PHP 5.0 | 2004 | **modelo POO**, PDO, SQLite, SOAP, iteradores |
| PHP 5.1 | 2005 | Extensión PDO, mejoras de rendimiento |
| PHP 5.2 | 2006 | `json_encode`/ `json_decode`, extensión`filter`|
| PHP 5.3 | 2009 | **Espacios de nombres**, enlaces estáticos tardíos, cierres |
| PHP 5.4 | 2012 | Sintaxis de matriz corta `[]`, características, servidor web integrado |
| PHP 5.5 | 2013 | Generadores, `yield`,`list()`en objetos,`::class`|
| PHP 5.6 | 2014 | Funciones variadicas, expresiones escalares constantes |
| PHP 7.0 | 2015 | **Principal**: Zend Engine 3, sugerencias de tipo escalar, tipos de retorno,`??`|
| PHP 7.1 | 2016 | Tipos que aceptan valores NULL, retorno `void`, iterable, visibilidad constante de clase |
| PHP 7.2 | 2017 |  Sugerencia de tipo `object`, ampliación del tipo de parámetro |
| PHP 7.3 | 2018 | Comas finales en llamadas a funciones,`JsonException`|
| PHP 7.4 | 2019 | **Propiedades escritas**, funciones de flecha, asignación coalescente nula |
| PHP 8.0 | 2020 | **Principal**: JIT, argumentos con nombre, expresión de coincidencia, tipos de unión, atributos |
| PHP 8.1 | 2021 | Enumeraciones, fibras, propiedades `readonly`, tipos de intersección |
| PHP 8.2 | 2022 |  Clases `readonly`, tipos DNF,`null`/`false`/`true`como tipos independientes |
| PHP 8.3 | 2023 | Constantes de clase escritas, atributo `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Ganchos de propiedad, atributo `#[\Deprecated]`, visibilidad asimétrica |
## Hitos importantes
### PHP/FI y PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf lanza "Herramientas de página de inicio personal"
- **1998**: PHP 3 — reescritura completa por Suraski & Gutmans; se convierte en un lenguaje de programación
- Funciones clave: integrado en HTML, manejo de formularios, soporte de bases de datos
### PHP 4: motor Zend (2000–2004)
- **Zend Engine 1**: código de bytes compilado, mucho más rápido
- Manejo de sesiones, almacenamiento en búfer de salida, PEAR
- Primera era del marco de desarrollo web real
### PHP 5: PHP orientado a objetos (2004-2014)
- **5.0**: reescritura completa de programación orientada a objetos: clases, interfaces, excepciones, PDO
- **5.3**: Espacios de nombres (críticos para PHP moderno), cierres, enlaces estáticos tardíos
- **5.4**: Rasgos, sintaxis de matriz corta `[]`, servidor web integrado
- **5.5**: Generadores (`yield`), `finally`
### PHP 7: la revolución del rendimiento (2015-2019)
- **7.0**: Zend Engine 3 — **2 veces más rápido**, declaraciones de tipo escalar, declaraciones de tipo de retorno
- **7.1**: tipos que aceptan valores NULL (`?int`), tipo de retorno nulo
- **7.4**: Propiedades escritas, funciones de flecha `fn() =>`, asignación coalescente nula `??=`
### PHP 8: PHP moderno (2020-presente)
- **8.0**: compilador JIT, argumentos con nombre, expresión de coincidencia, tipos de unión, atributos (`#[...]`), operador nullsafe`?->`
- **8.1**: Enumeraciones, fibras (simultaneidad ligera), propiedades de solo lectura, tipos de intersección
- **8.2**: Clases de solo lectura, tipos DNF,`null`/`false`/`true`como tipos independientes
- **8.3**: Constantes de clase escritas, `#[\Override]`,`json_validate()`
- **8.4**: Ganchos de propiedad, `#[\Deprecated]`, visibilidad asimétrica
## Evolución del sistema tipo
```
PHP 4:    No type hints
PHP 5.0:  Class type hints
PHP 5.1:  Array type hint
PHP 7.0:  Scalar types (int, string, float, bool), return types
PHP 7.1:  Nullable types (?int), void, iterable
PHP 7.2:  object type
PHP 7.4:  Typed properties
PHP 8.0:  Union types (int|string), mixed
PHP 8.1:  Intersection types (A&B), never, first-class callable syntax
PHP 8.2:  DNF types ((A&B)|C), null/false/true standalone
PHP 8.3:  Typed class constants
PHP 8.4:  Property hooks (get/set)
```

## Evolución de la sintaxis
```php
// PHP 3/4: Basic scripting
$users = array(1, 2, 3);

// PHP 5.4: Short array syntax
$users = [1, 2, 3];

// PHP 5.3: Namespaces
namespace App\Models;

// PHP 7.0: Scalar types
function add(int $a, int $b): int { return $a + $b; }

// PHP 7.4: Arrow functions
$doubled = array_map(fn($x) => $x * 2, $numbers);

// PHP 8.0: Named arguments, match
$result = process(value: $input, strict: true);
$label = match($status) { 0 => 'inactive', 1 => 'active', default => 'unknown' };

// PHP 8.1: Enums
enum Status: string { case Active = 'active'; case Inactive = 'inactive'; }

// PHP 8.4: Property hooks
class User {
    public string $name { get => strtoupper($this->name); set; }
}
```

## Principios clave de diseño
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Crecimiento del ecosistema
```
1995: PHP/FI — personal tool
2000: PHP 4 + PEAR — package management begins
2004: PHP 5 + OOP — enterprise adoption
2008: Composer (dependency management) — modern PHP ecosystem
2011: Laravel framework — elegant PHP
2015: PHP 7 — performance revolution
2020: PHP 8 — JIT, modern features
2025: PHP powers ~75% of websites with known server-side language
       WordPress, Wikipedia, Slack, Mailchimp all run on PHP
```
