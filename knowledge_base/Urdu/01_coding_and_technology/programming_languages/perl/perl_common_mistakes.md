---
# Metadata
title: "Perl — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Perl with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# پرل - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز تصحیح کے ساتھ پرل میں سب سے عام غلطیوں، ٹریپس اور اینٹی پیٹرن کی فہرست بناتی ہے۔
---

## 1.`strict`اور`warnings`استعمال نہیں کرنا
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

## 2. اسکیلر بمقابلہ فہرست سیاق و سباق
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

## 3. عالمی متغیرات
```perl
# ❌ WRONG — package variables
$name = "Alice";
sub greet { print "Hello, $name\n"; }

# ✅ CORRECT — lexical variables
my $name = "Alice";
sub greet { print "Hello, $name\n"; }
```

---

## 4. پیچیدہ ڈیٹا کے حوالہ جات کا استعمال نہ کرنا
```perl
# ❌ WRONG — array of arrays (flattened)
my @matrix = ((1,2), (3,4));  # just (1,2,3,4)

# ✅ CORRECT — array of array references
my @matrix = ([1,2], [3,4]);
print $matrix[0][1];  # 2
```

---

## 5. حد بندی کی وضاحت کے بغیر ریجیکس
```perl
# ❌ WRONG — hard to read regex
$s =~ /\/usr\/local\/bin/;

# ✅ CORRECT — use different delimiters
$s =~ m{/usr/local/bin};
```

---

## 6. جدید پرل خصوصیات کا استعمال نہیں کرنا
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

## خلاصہ
پرل کی لچک خطرناک ہے: ہمیشہ `use strict; use warnings;`، سیاق و سباق کو سمجھیں (اسکیلر بمقابلہ فہرست)، لغوی متغیرات (`my`) استعمال کریں، نیسٹڈ ڈیٹا کے لیے حوالہ جات استعمال کریں، اور پرل کی جدید خصوصیات (دستخط، `say`، XQZMARKER3) کو قبول کریں۔ پرل ان لوگوں کو انعام دیتا ہے جو اپنے بھرپور ریجیکس انجن اور CPAN ماحولیاتی نظام کو سمجھداری سے استعمال کرتے ہیں۔