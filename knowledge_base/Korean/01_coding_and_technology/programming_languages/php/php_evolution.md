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

# PHP — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| PHP/FI | 1995 | 개인 홈 페이지 도구(Rasmus Lerdorf) |
| PHP 3.0 | 1998 | 최초의 최신 PHP; Zeev Suraski 및 Andi Gutmans 재작성 |
| PHP 4.0 | 2000 | Zend 엔진, 세션 지원, 출력 버퍼링 |
| PHP 5.0 | 2004년 | **OOP 모델**, PDO, SQLite, SOAP, 반복자 |
| PHP 5.1 | 2005년 | PDO 확장, 성능 ​​개선 |
| PHP 5.2 | 2006년 | `json_encode`/`json_decode`,`filter`확장 |
| PHP 5.3 | 2009 | **네임스페이스**, 후기 정적 바인딩, 클로저 |
| PHP 5.4 | 2012 | 짧은 배열 구문 `[]`, 특성, 내장 웹 서버 |
| PHP 5.5 | 2013 | 생성기, `yield`, 개체의 `list()`,`::class`|
| PHP 5.6 | 2014 | 가변 함수, 상수 스칼라 표현식 |
| PHP 7.0 | 2015 | **주요**: Zend Engine 3, 스칼라 유형 힌트, 반환 유형,`??`|
| PHP 7.1 | 2016 | Null 가능 유형,`void`반환, 반복 가능, 클래스 상수 가시성 |
| PHP 7.2 | 2017 | `object`유형 힌트, 매개변수 유형 확대 |
| PHP 7.3 | 2018 | 함수 호출의 후행 쉼표,`JsonException`|
| PHP 7.4 | 2019 | **입력된 속성**, 화살표 함수, Null 병합 할당 |
| PHP 8.0 | 2020 | **주요**: JIT, 명명된 인수, 일치 표현식, 공용체 유형, 속성 |
| PHP 8.1 | 2021 | 열거형, 파이버,`readonly`속성, 교차 유형 |
| PHP 8.2 | 2022 | `readonly`클래스, DNF 유형,`null`/`false`/ `true`를 독립형 유형으로 |
| PHP 8.3 | 2023년 | 형식화된 클래스 상수,`#[\Override]`속성,`json_validate`|
| PHP 8.4 | 2024 | 속성 후크,`#[\Deprecated]`속성, 비대칭 가시성 |
## 주요 이정표
### PHP/FI 및 PHP 3(1995~1999)
- **1995**: Rasmus Lerdorf가 "개인 홈 페이지 도구" 출시
- **1998**: PHP 3 — Suraski & Gutmans가 완전히 재작성했습니다. 스크립팅 언어가 되다
- 주요 기능: HTML에 내장, 양식 처리, 데이터베이스 지원
### PHP 4 — Zend 엔진(2000-2004)
- **Zend Engine 1**: 컴파일된 바이트코드, 훨씬 더 빠름
- 세션 처리, 출력 버퍼링, PEAR
- 최초의 실제 웹 개발 프레임워크 시대
### PHP 5 — 객체 지향 PHP(2004~2014)
- **5.0**: 완전한 OOP 재작성 — 클래스, 인터페이스, 예외, PDO
- **5.3**: 네임스페이스(최신 PHP에 중요), 클로저, 후기 정적 바인딩
- **5.4**: 특성, 짧은 배열 구문 `[]`, 내장 웹 서버
- **5.5**: 생성기(`yield`), `finally`
### PHP 7 — 성능 혁명(2015-2019)
- **7.0**: Zend Engine 3 — **2배 더 빠름**, 스칼라 유형 선언, 반환 유형 선언
- **7.1**: Null 가능 유형(`?int`), void 반환 유형
- **7.4**: 유형화된 속성, 화살표 기능 `fn() =>`, null 병합 할당 `??=`
### PHP 8 — 최신 PHP(2020~현재)
- **8.0**: JIT 컴파일러, 명명된 인수, 일치 표현식, 공용체 유형, 속성(`#[...]`), nullsafe 연산자`?->`
- **8.1**: 열거형, 파이버(경량 동시성), 읽기 전용 속성, 교차 유형
- **8.2**: 읽기 전용 클래스, DNF 유형,`null`/`false`/`true`독립형 유형
- **8.3**: 형식화된 클래스 상수,`#[\Override]`,`json_validate()`
- **8.4**: 속성 후크,`#[\Deprecated]`, 비대칭 가시성
## 유형 시스템 진화
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

## 구문 진화
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

## 주요 디자인 원칙
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## 생태계 성장
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
