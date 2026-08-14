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

# Perl — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 1987 | 최초 출시(래리 월) |
| 2.0 | 1988 | `study`함수, 더 나은 정규식 |
| 3.0 | 1989 | `my`변수(어휘적 범위 지정) |
| 4.0 | 1991 | `O'Reilly`"Programming Perl"(카멜북) |
| 5.0 | 1994년 | **주요**: 모듈, 참조, 클로저,`use strict`|
| 5.6 | 2000 | `our`,`state`(나중에),`v-strings`,`y2k`수정 |
| 5.8 | 2002 | **유니코드 지원**,`ithreads`,`open`pragma |
| 5.10 | 2007년 | `say`,`//`정의-또는`given`/`when`,`~~`스마트매치 |
| 5.12 | 2010 | `package NAME VERSION`, `...`(야다야다), 유니코드 5.2 |
| 5.14 | 2011 |  `s///r`(비파괴 대체),`package`개선 |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | 어휘 `$_`, 해시 무작위화, 조건부`my`|
| 5.20 | 2014 | **서브루틴 서명**(실험적),`%hash`슬라이싱 |
| 5.22 | 2015 | `&`역참조, `<<>>`(세이프 오픈) |
| 5.24 | 2016 | 안정적인 후위 역참조 |
| 5.26 | 2017 | **`while`의 어휘`$_`**, `@INC`의 `.`가 제거되었습니다(보안) |
| 5.28 | 2018 | 키/값 슬라이스의 유니코드 10.0,`delete`|
| 5.30 | 2019 | `for`/`while`조건의`my`|
| 5.32 | 2020 | `isa`연산자, 유니코드 13.0 |
| 5.34 | 2021 | `try`/ `catch`(실험적),`defer`블록 |
| 5.36 | 2022 | **`use v5.36`**: 서명 활성화,`$_`기본값,`defer`|
| 5.38 | 2023년 | `class`키워드(실험적),`try`/`catch`안정 |
| 5.40 | 2024 | `^`비트 연산자,`for`목록 개선 |
| 5.42 | 2025 | 지속적인 개발 |
## 주요 이정표
### Perl 1–4: 스크립팅 시대(1987–1993)
- **1987**: Larry Wall이 Perl 출시 — "실용적인 추출 및 보고 언어"
- **목표**: sed, awk, grep, Shell을 하나의 강력한 스크립팅 도구로 결합
- **3.0**: 어휘 범위 지정(`my`)
- **4.0**: The Camel Book — Perl이 시스템 관리 작업에 널리 채택됨
### Perl 5: 황금 시대(1994~2019)
- **5.0 (1994)**: 전체 재작성 — **모듈**, **참조**, **클로저**, **객체**
- **5.6 (2000)**:`our`, v-문자열
- **5.8 (2002)**: **유니코드 지원**, 인터프리터 스레드(`ithreads`)
- **5.10(2007)**:`say`, `//`(정의 또는),`given`/ `when`(스위치), 스마트매치
- **5.12–5.28**: 점진적인 개선, 유니코드 업그레이드
### 모던 펄(2020~현재)
- **5.32 (2020)**:`isa`연산자 (클리너 유형 확인)
- **5.34(2021)**:`try`/ `catch`(실험적),`defer`블록
- **5.36(2022)**: **`use v5.36`** — 기본적으로 활성화된 서명,`$_`기본값,`defer`
- **5.38(2023)**:`class`키워드(실험적 - 내장 OOP),`try`/`catch`안정
- **5.40(2024)**: 비트 연산자 개선
## 구문 진화
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

## CPAN 생태계
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## 주요 디자인 원칙
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## 생태계 성장
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
