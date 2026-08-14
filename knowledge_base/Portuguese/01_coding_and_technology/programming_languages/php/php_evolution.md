---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# PHP – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| PHP/FI | 1995 | Ferramentas da página inicial pessoal (Rasmus Lerdorf) |
| PHP3.0 | 1998 | Primeiro PHP moderno; Zeev Suraski e Andi Gutmans reescrevem |
| PHP4.0 | 2000 | Zend Engine, suporte de sessão, buffer de saída |
| PHP5.0 | 2004 | **Modelo OOP**, PDO, SQLite, SOAP, iteradores |
| PHP5.1 | 2005 | Extensão PDO, melhorias de desempenho |
| PHP5.2 | 2006 | `json_encode`/`json_decode`, extensão`filter`|
| PHP5.3 | 2009 | **Namespaces**, vinculações estáticas tardias, encerramentos |
| PHP5.4 | 2012 | Sintaxe de array curto`[]`, características, servidor web integrado |
| PHP5.5 | 2013 | Geradores,`yield`,`list()`em objetos,`::class`|
| PHP5.6 | 2014 | Funções variáveis, expressões escalares constantes |
| PHP7.0 | 2015 | **Principal**: Zend Engine 3, dicas de tipo escalar, tipos de retorno,`??`|
| PHP7.1 | 2016 | Tipos anuláveis, retorno `void`, iterável, visibilidade constante de classe |
| PHP7.2 | 2017 |  Dica de tipo `object`, ampliação do tipo de parâmetro |
| PHP7.3 | 2018 | Vírgulas finais em chamadas de função,`JsonException`|
| PHP7.4 | 2019 | **Propriedades digitadas**, funções de seta, atribuição de coalescência nula |
| PHP 8.0 | 2020 | **Principal**: JIT, argumentos nomeados, expressão de correspondência, tipos de união, atributos |
| PHP 8.1 | 2021 | Enums, fibras, propriedades `readonly`, tipos de interseção |
| PHP 8.2 | 2022 |  Classes `readonly`, tipos DNF, `null`/`false`/`true` como tipos independentes |
| PHP 8.3 | 2023 | Constantes de classe digitadas, atributo `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Ganchos de propriedade, atributo `#[\Deprecated]`, visibilidade assimétrica |
## Marcos importantes
### PHP/FI e PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf lança "Ferramentas de página inicial pessoal"
- **1998**: PHP 3 — reescrita completa por Suraski & Gutmans; torna-se uma linguagem de script
- Principais recursos: incorporado em HTML, manipulação de formulários, suporte a banco de dados
### PHP 4 — Mecanismo Zend (2000–2004)
- **Zend Engine 1**: Bytecode compilado, muito mais rápido
- Manipulação de sessão, buffer de saída, PEAR
- Primeira era real de framework de desenvolvimento web
### PHP 5 — PHP Orientado a Objetos (2004–2014)
- **5.0**: Reescrita completa de OOP — classes, interfaces, exceções, PDO
- **5.3**: Namespaces (críticos para PHP moderno), encerramentos, vinculações estáticas tardias
- **5.4**: Características, sintaxe de array curto`[]`, servidor web integrado
- **5.5**: Geradores (`yield`), `finally`
### PHP 7 — A revolução do desempenho (2015–2019)
- **7.0**: Zend Engine 3 — **2x mais rápido**, declarações de tipo escalar, declarações de tipo de retorno
- **7.1**: Tipos anuláveis (`?int`), tipo de retorno nulo
- **7.4**: Propriedades digitadas, funções de seta`fn() =>`, atribuição de coalescência nula `??=`
### PHP 8 — PHP moderno (2020-presente)
- **8.0**: compilador JIT, argumentos nomeados, expressão de correspondência, tipos de união, atributos (`#[...]`), operador nullsafe`?->`
- **8.1**: Enums, fibras (simultaneidade leve), propriedades somente leitura, tipos de interseção
- **8.2**: Classes somente leitura, tipos DNF, `null`/`false`/`true` como tipos independentes
- **8.3**: Constantes de classe digitadas,`#[\Override]`,`json_validate()`
- **8.4**: ganchos de propriedade,`#[\Deprecated]`, visibilidade assimétrica
## Tipo Evolução do Sistema
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

## Evolução da Sintaxe
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

## Princípios-chave de design
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Crescimento do Ecossistema
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
