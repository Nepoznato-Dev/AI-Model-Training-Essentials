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
# पर्ल - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ पर्ल में सुधार के साथ सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1.`strict`और`warnings`का उपयोग नहीं करना
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

## 2. स्केलर बनाम सूची संदर्भ
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

## 3. वैश्विक चर
```perl
# ❌ WRONG — package variables
$name = "Alice";
sub greet { print "Hello, $name\n"; }

# ✅ CORRECT — lexical variables
my $name = "Alice";
sub greet { print "Hello, $name\n"; }
```

---

## 4. जटिल डेटा के लिए संदर्भों का उपयोग न करना
```perl
# ❌ WRONG — array of arrays (flattened)
my @matrix = ((1,2), (3,4));  # just (1,2,3,4)

# ✅ CORRECT — array of array references
my @matrix = ([1,2], [3,4]);
print $matrix[0][1];  # 2
```

---

## 5. सीमांकक स्पष्टता के बिना रेगेक्स
```perl
# ❌ WRONG — hard to read regex
$s =~ /\/usr\/local\/bin/;

# ✅ CORRECT — use different delimiters
$s =~ m{/usr/local/bin};
```

---

## 6. आधुनिक पर्ल सुविधाओं का उपयोग नहीं करना
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

## सारांश
पर्ल का लचीलापन खतरनाक है: हमेशा `use strict; use warnings;`, संदर्भ को समझें (स्केलर बनाम सूची), शाब्दिक चर का उपयोग करें (`my`), नेस्टेड डेटा के लिए संदर्भ का उपयोग करें, और आधुनिक पर्ल सुविधाओं (हस्ताक्षर, `say`, `//`) को अपनाएं। पर्ल उन लोगों को पुरस्कृत करता है जो इसके समृद्ध रेगेक्स इंजन और सीपीएएन पारिस्थितिकी तंत्र का बुद्धिमानी से उपयोग करते हैं।