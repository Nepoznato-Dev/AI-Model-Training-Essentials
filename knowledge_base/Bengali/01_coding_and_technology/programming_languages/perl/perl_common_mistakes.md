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
# পার্ল — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ পার্লের সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1.`strict`এবং`warnings`ব্যবহার করছেন না
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

## 2. স্কেলার বনাম তালিকা প্রসঙ্গ
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

## 3. গ্লোবাল ভেরিয়েবল
```perl
# ❌ WRONG — package variables
$name = "Alice";
sub greet { print "Hello, $name\n"; }

# ✅ CORRECT — lexical variables
my $name = "Alice";
sub greet { print "Hello, $name\n"; }
```

---

## 4. জটিল ডেটার জন্য রেফারেন্স ব্যবহার না করা
```perl
# ❌ WRONG — array of arrays (flattened)
my @matrix = ((1,2), (3,4));  # just (1,2,3,4)

# ✅ CORRECT — array of array references
my @matrix = ([1,2], [3,4]);
print $matrix[0][1];  # 2
```

---

## 5. ডিলিমিটার স্পষ্টতা ছাড়াই রেজেক্স
```perl
# ❌ WRONG — hard to read regex
$s =~ /\/usr\/local\/bin/;

# ✅ CORRECT — use different delimiters
$s =~ m{/usr/local/bin};
```

---

## 6. আধুনিক পার্ল বৈশিষ্ট্য ব্যবহার না করা
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

## সারাংশ
পার্লের নমনীয়তা বিপজ্জনক: সর্বদা`use strict; use warnings;`, প্রসঙ্গ (স্কেলার বনাম তালিকা) বুঝুন, আভিধানিক ভেরিয়েবল ব্যবহার করুন (`my`), নেস্টেড ডেটার জন্য রেফারেন্স ব্যবহার করুন এবং আধুনিক পার্ল বৈশিষ্ট্যগুলি (স্বাক্ষর,`say`, XQZMARKER3) আলিঙ্গন করুন৷ পার্ল তাদের পুরস্কৃত করে যারা এর সমৃদ্ধ রেজেক্স ইঞ্জিন এবং CPAN ইকোসিস্টেম বুদ্ধিমানের সাথে ব্যবহার করে।