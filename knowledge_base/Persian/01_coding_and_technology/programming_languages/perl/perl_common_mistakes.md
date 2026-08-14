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

# پرل - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوهای پرل را با اصلاحات فهرست می کند.
---

## 1. عدم استفاده از`strict`و `warnings`
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

## 2. اسکالر در مقابل متن فهرست
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

## 3. متغیرهای جهانی
```perl
# ❌ WRONG — package variables
$name = "Alice";
sub greet { print "Hello, $name\n"; }

# ✅ CORRECT — lexical variables
my $name = "Alice";
sub greet { print "Hello, $name\n"; }
```

---

## 4. عدم استفاده از منابع برای داده های پیچیده
```perl
# ❌ WRONG — array of arrays (flattened)
my @matrix = ((1,2), (3,4));  # just (1,2,3,4)

# ✅ CORRECT — array of array references
my @matrix = ([1,2], [3,4]);
print $matrix[0][1];  # 2
```

---

## 5. Regex بدون شفافیت جداکننده
```perl
# ❌ WRONG — hard to read regex
$s =~ /\/usr\/local\/bin/;

# ✅ CORRECT — use different delimiters
$s =~ m{/usr/local/bin};
```

---

## 6. عدم استفاده از ویژگی های مدرن پرل
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

## خلاصه
انعطاف‌پذیری پرل خطرناک است: همیشه `use strict; use warnings;`، درک زمینه (اسکالر در مقابل فهرست)، استفاده از متغیرهای لغوی (`my`)، استفاده از مراجع برای داده‌های تودرتو، و در آغوش گرفتن ویژگی‌های پرل مدرن (امضا، `say`، XQZMARKER3X). پرل به کسانی که از موتور غنی ریجکس و اکوسیستم CPAN عاقلانه استفاده می کنند، پاداش می دهد.