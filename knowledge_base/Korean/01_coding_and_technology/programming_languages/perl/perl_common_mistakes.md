---
# Metadata
title: "Perl — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Perl with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [perl, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Perl — 일반적인 실수 및 안티 패턴
이 문서는 Perl에서 가장 흔히 발생하는 실수, 함정, 안티 패턴을 수정하여 목록화합니다.
---

## 1.`strict`및 `warnings`를 사용하지 않음
```perl
# ❌ WRONG — no safety checks
$x = 5;  # creates global $x silently
print $y;  # typo, prints nothing

# ✅ CORRECT — always use strict and warnings
use strict;
use warnings;
my $x = 5;
```

---

## 2. 스칼라 vs 목록 컨텍스트
```perl
# ❌ WRONG — context confusion
my @arr = (1, 2, 3);
my $count = @arr;  # 3 (scalar context — count)
my ($first) = @arr;  # 1 (list context — first element)
my $first = @arr;    # 3! (scalar context — count, not element)

# ✅ CORRECT — be explicit about context
my $count = scalar @arr;
my ($first) = @arr;
```

---

## 3. 전역 변수
```perl
# ❌ WRONG — package variables
$name = "Alice";
sub greet { print "Hello, $name\n"; }

# ✅ CORRECT — lexical variables
my $name = "Alice";
sub greet { print "Hello, $name\n"; }
```

---

## 4. 복잡한 데이터에 참조를 사용하지 않음
```perl
# ❌ WRONG — array of arrays (flattened)
my @matrix = ((1,2), (3,4));  # just (1,2,3,4)

# ✅ CORRECT — array of array references
my @matrix = ([1,2], [3,4]);
print $matrix[0][1];  # 2
```

---

## 5. 구분 기호 명확성이 없는 정규식
```perl
# ❌ WRONG — hard to read regex
$s =~ /\/usr\/local\/bin/;

# ✅ CORRECT — use different delimiters
$s =~ m{/usr/local/bin};
```

---

## 6. 최신 Perl 기능을 사용하지 않음
```perl
# ❌ WRONG — old Perl style
my $name = shift @_;
my $age = shift @_;

# ✅ CORRECT — modern Perl (5.20+)
sub greet($name, $age) {
    say "Hello, $name! Age: $age";
}

# ✅ CORRECT — say instead of print
say "Hello, world!";

# ✅ CORRECT — // for defined-or
my $value = $input // 'default';
```

---

## 요약
Perl의 유연성은 위험합니다. 항상 `use strict; use warnings;`, 컨텍스트(스칼라 대 목록) 이해, 어휘 변수(`my`) 사용, 중첩 데이터에 대한 참조 사용, 최신 Perl 기능(서명,`say`,`//`)을 수용합니다. Perl은 풍부한 정규식 엔진과 CPAN 생태계를 현명하게 사용하는 사람들에게 보상합니다.